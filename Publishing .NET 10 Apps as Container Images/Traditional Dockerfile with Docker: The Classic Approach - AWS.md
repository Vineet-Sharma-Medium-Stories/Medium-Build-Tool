# Traditional Dockerfile with Docker: The Classic Approach - AWS

## Mastering Containerization with Industry-Standard Tooling on Amazon Web Services

### Introduction: The Foundation of Containerized .NET Applications on AWS

In the [previous installments](#) of this AWS series, we explored the cutting-edge world of SDK-native container publishing—building OCI images without Docker, achieving 78% smaller images and 39% faster builds on AWS Graviton processors. While SDK-native represents the future, the traditional Dockerfile with Docker remains the **industry standard** for containerizing .NET applications on Amazon Web Services, and for good reason.

The Dockerfile approach, now over a decade old, has evolved into a sophisticated, battle-tested methodology that offers something no other approach can match: **complete transparency and control**. Every layer is explicitly defined, every dependency is documented in code, and the build process is fully observable. For organizations deploying to AWS—whether on EC2, ECS, or EKS—this visibility is non-negotiable, especially when subject to regulatory compliance like FedRAMP or HIPAA.

In this installment, we'll master the Dockerfile approach for AWS using Vehixcare-API as our case study—a sophisticated .NET 9.0 fleet management platform with real-time telemetry, SignalR hubs, MongoDB (Amazon DocumentDB) integration, and multiple background services. We'll explore multi-stage builds, layer caching optimization, .dockerignore patterns, and production-grade Amazon ECR integration with IAM roles and EC2 instance profiles.

```mermaid
graph TD
    subgraph "Traditional Docker Build Pipeline on AWS"
        A[Source Code] --> B[Docker Build Context]
        B --> C[Docker Daemon]
        C --> D[Multi-stage Build]
        D --> E[Build Stage<br/>SDK + Dependencies]
        D --> F[Runtime Stage<br/>Only Runtime + App]
        E --> G[Container Image]
        F --> G
        G --> H[Amazon ECR]
        H --> I[ECS/EKS/EC2]
    end
    
    style D fill:#48bb78,color:#fff
    style E fill:#2b6cb0,color:#fff
    style F fill:#48bb78,color:#fff
    style H fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete AWS series (10 stories):**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference - AWS** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides for Amazon ECR

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker - AWS** – A deep dive into MSBuild configuration, multi-architecture builds (Graviton ARM64), and direct Amazon ECR integration with IAM roles

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach - AWS** – Mastering multi-stage builds, build cache optimization, and Amazon ECR authentication for enterprise CI/CD pipelines on AWS *(This story)*

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative - AWS** – Transitioning from Docker to Podman, rootless containers for enhanced security, and Amazon ECR integration with Podman Desktop

- 🏗️ **5. AWS CDK & Copilot: Infrastructure as Code for Containers - AWS** – Deploying to Amazon ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless container orchestration

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop AWS Deployments - AWS** – Leveraging Visual Studio's AWS Toolkit, one-click publish to Amazon ECR, and debugging containerized apps on AWS

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs without a runtime, integrating with Amazon Inspector for vulnerability scanning, and deploying to air-gapped AWS environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows - AWS** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation (x64 to Graviton), and Amazon ECR push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker - AWS** – Using the konet .NET tool for cross-platform image generation, AMD64/ARM64 (Graviton) simultaneous builds, and AWS CodeBuild optimization

- ☸️ **10. Kubernetes Native Deployments: Orchestrating .NET 10 Containers on Amazon EKS - AWS** – Deploying to Amazon EKS, Helm charts, GitOps with Flux, ALB Ingress Controller, and production-grade operations

---

## Understanding the Docker Build Process on AWS

Before diving into Vehixcare's Dockerfile for AWS, we must understand how Docker builds container images in the AWS ecosystem. The process involves several key components that interact with AWS services.

### Docker Build Context

When you run `docker build` on an EC2 instance or in CodeBuild, Docker packages the **build context**—typically the current directory—and sends it to the Docker daemon:

```bash
# The '.' specifies the build context
docker build -t vehixcare-api:latest .
```

**What's included for Vehixcare on AWS:** Everything in the current directory (and subdirectories) is sent to the Docker daemon, unless excluded by `.dockerignore`. This context can be large—for Vehixcare, it includes:
- Source code (10-50 MB)
- Project files (1-5 MB)
- Git history (100-500 MB)
- Binaries and obj folders (50-200 MB)
- Documentation and assets (5-50 MB)
- AWS SDK assemblies (10-20 MB)

**Why it matters for AWS:** Large build contexts increase CodeBuild execution time and EC2 costs. Optimizing context size is critical for CI/CD pipelines.

### Dockerfile Instructions for AWS

Each instruction in a Dockerfile creates a **layer** in the final image. Layers are cached, so ordering matters significantly for AWS deployments:

| Instruction | Purpose | AWS Relevance |
|-------------|---------|---------------|
| `FROM` | Base image | Use Amazon Linux or MCR images |
| `WORKDIR` | Set working directory | Metadata only, no size impact |
| `COPY` | Copy files from context | Creates layer with copied files |
| `RUN` | Execute commands | Creates layer with command output |
| `ENV` | Set environment variables | Configure AWS region, credentials |
| `EXPOSE` | Document ports | For ECS/ALB port mapping |
| `ENTRYPOINT` | Set default executable | Configure entry point for ECS |

---

## The Vehixcare-API Dockerfile: Production-Ready for AWS

Let's examine Vehixcare's complete production Dockerfile optimized for AWS, with detailed commentary on each section:

```dockerfile
# ============================================
# VEHIXCARE-API DOCKERFILE - AWS OPTIMIZED
# ============================================
# Optimized for Amazon ECS, EKS, and EC2 deployments

# ============================================
# STAGE 1: Base Runtime Image
# ============================================
# Use the official ASP.NET Core runtime image
# Can also use Amazon Linux-based images for better AWS integration
FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS base
# FROM public.ecr.aws/amazonlinux/amazonlinux:2023 AS base

WORKDIR /app

# Expose ports (documentation only, does not publish ports)
# 8080 for HTTP (ALB/ECS), 8443 for HTTPS
EXPOSE 8080
EXPOSE 8443

# Create a non-root user for security
# Running as non-root reduces attack surface on EC2
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# ============================================
# STAGE 2: Build Image with SDK
# ============================================
# Use the full SDK image for compilation
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Copy project files first to maximize layer caching
# Project files change infrequently, so this layer is cached
COPY ["Vehixcare.API/Vehixcare.API.csproj", "Vehixcare.API/"]
COPY ["Vehixcare.Business/Vehixcare.Business.csproj", "Vehixcare.Business/"]
COPY ["Vehixcare.Common/Vehixcare.Common.csproj", "Vehixcare.Common/"]
COPY ["Vehixcare.Data/Vehixcare.Data.csproj", "Vehixcare.Data/"]
COPY ["Vehixcare.Hubs/Vehixcare.Hubs.csproj", "Vehixcare.Hubs/"]
COPY ["Vehixcare.Models/Vehixcare.Models.csproj", "Vehixcare.Models/"]
COPY ["Vehixcare.Repository/Vehixcare.Repository.csproj", "Vehixcare.Repository/"]
COPY ["Vehixcare.BackgroundServices/Vehixcare.BackgroundServices.csproj", "Vehixcare.BackgroundServices/"]

# Restore dependencies
# This layer is cached until any .csproj file changes
RUN dotnet restore "Vehixcare.API/Vehixcare.API.csproj"

# Copy the remaining source code
# This layer invalidates when any source file changes
COPY . .

# Build the application
WORKDIR "/src/Vehixcare.API"
RUN dotnet build "Vehixcare.API.csproj" -c Release -o /app/build

# ============================================
# STAGE 3: Publish Optimized Artifacts
# ============================================
FROM build AS publish
# Publish with AWS optimizations:
# - Release configuration
# - Trimming to remove unused code (reduces size by 50-70%)
# - ReadyToRun for faster startup on EC2/ECS
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish \
    --no-restore \
    --no-build \
    /p:PublishTrimmed=true \
    /p:PublishReadyToRun=true \
    /p:TrimMode=partial

# ============================================
# STAGE 4: Final Runtime Image
# ============================================
FROM base AS final
WORKDIR /app

# Copy published artifacts from the publish stage
COPY --from=publish /app/publish .

# Configure AWS environment variables
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:8080;https://+:8443
ENV AWS_REGION=us-east-1
ENV AWS_ECR_REPOSITORY=vehixcare-api

# Health check for ECS/ALB
# ECS uses health checks to determine container health
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Set the entry point
ENTRYPOINT ["dotnet", "Vehixcare.API.dll"]
```

---

## Amazon Linux Base Images for Better AWS Integration

### Using Amazon Linux 2023 Base Images

```dockerfile
# Use Amazon Linux 2023 base image for native AWS integration
FROM public.ecr.aws/amazonlinux/amazonlinux:2023 AS base

# Install .NET runtime on Amazon Linux
RUN dnf install -y dotnet-runtime-9.0 && \
    dnf clean all

WORKDIR /app
EXPOSE 8080

# Create non-root user
RUN adduser appuser && \
    chown -R appuser:appuser /app
USER appuser
```

### Using AWS-Specific .NET Images

```dockerfile
# Use AWS official .NET images
FROM public.ecr.aws/dotnet/aspnet:9.0 AS base
FROM public.ecr.aws/dotnet/sdk:9.0 AS build
```

**Benefits of Amazon Linux Base Images:**
- Pre-configured with AWS tools (AWS CLI, SSM Agent)
- Optimized for EC2 and ECS
- Smaller size (Amazon Linux is minimal)
- Native integration with CloudWatch, X-Ray

---

## Layer-by-Layer Analysis for AWS ECR

| Layer | Size | Cache Key | AWS ECR Storage Cost |
|-------|------|-----------|---------------------|
| `FROM aspnet:9.0` | ~190 MB | Image digest | $0.10 per GB-month |
| `RUN adduser` | ~1 MB | Command hash | Minimal |
| `COPY project files` | ~50 KB | File content hashes | Negligible |
| `RUN dotnet restore` | ~500 MB | .csproj + nuget.config | $0.25 per GB-month |
| `COPY source code` | ~5-15 MB | All source files | Minimal |
| `RUN dotnet build` | ~200 MB | Source + bin/obj | $0.10 per GB-month |
| `RUN dotnet publish` | ~150 MB | Build output | $0.08 per GB-month |
| `COPY --from=publish` | ~150 MB | Published output | $0.08 per GB-month |
| **Final image** | **~195 MB** | - | **$0.10 per GB-month** |

---

## Optimizing the Dockerfile for AWS

### 1. Multi-Stage Build Optimization for ECS

The multi-stage pattern separates the SDK-heavy build environment from the lean runtime environment, critical for ECS task start times:

```dockerfile
# Build stage: Includes SDK (~1.2 GB)
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
# ... compile application ...

# Runtime stage: Only runtime (~190 MB)
FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
COPY --from=build /app/publish .
```

**Result:** Final image size reduced from 1.4 GB to ~195 MB, reducing ECS task pull time by 80%.

### 2. Layer Caching Optimization for CodeBuild

Ordering `COPY` commands from least-frequently-changed to most-frequently-changed:

```dockerfile
# Good: Project files first (change rarely)
COPY *.csproj ./
RUN dotnet restore

# Bad: Source code first (changes constantly)
COPY . ./
RUN dotnet restore  # Restores every build! Increases CodeBuild time.
```

### 3. AWS-Specific Trimming

```dockerfile
# Publish with AWS SDK trimming
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish \
    /p:PublishTrimmed=true \
    /p:TrimMode=partial \
    /p:TrimmerRootAssembly=AWSSDK.Core \
    /p:TrimmerRootAssembly=AWSSDK.SimpleNotificationService
```

### 4. Multi-Architecture Builds for Graviton

```dockerfile
# Multi-stage builds for both architectures
FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:9.0 AS build
ARG TARGETARCH
RUN dotnet publish -c Release -r linux-$TARGETARCH -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
COPY --from=build /app/publish .
```

---

## The .dockerignore File: Optimizing Build Context for AWS

A well-configured `.dockerignore` file is essential for fast builds on AWS CodeBuild:

```dockerignore
# .NET build artifacts
bin/
obj/
out/
publish/
*.user
*.suo
*.cache

# Git
.git/
.gitignore
.gitattributes

# Development tools
.vscode/
.idea/
.vs/
*.swp
*.swo

# Documentation
docs/
README*.md
CHANGES.md
*.pdf
*.docx

# Test outputs
TestResults/
coverage/
*.trx
*.coverage

# Logs
logs/
*.log
*.tmp

# Docker artifacts
Dockerfile
docker-compose*.yml
.dockerignore

# AWS credentials (NEVER commit!)
.aws/
credentials
config

# Secrets
*.pfx
*.pem
*.key
secrets.json
appsettings.Production.json

# CI/CD
.github/
.gitlab/
codebuild/
buildspec.yml

# Seed data (large files)
Vehixcare.SeedData/Data/
*.dump
*.backup

# OS files
.DS_Store
Thumbs.db
```

**Impact on CodeBuild performance:**

| Metric | Without .dockerignore | With .dockerignore |
|--------|----------------------|-------------------|
| Build context size | 350 MB | 15 MB |
| Context upload to S3 | 12 seconds | 0.5 seconds |
| First build time | 95 seconds | 45 seconds |
| CodeBuild cost | $0.025 | $0.012 |

---

## Amazon ECR Authentication

### Authentication Methods

**Method 1: EC2 Instance Profile**

When running on EC2 with an IAM role:

```bash
# No explicit authentication needed - uses instance profile
docker build -t vehixcare-api:latest .
docker tag vehixcare-api:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/vehixcare-api:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/vehixcare-api:latest
```

**IAM Role Policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload",
        "ecr:PutImage"
      ],
      "Resource": "*"
    }
  ]
}
```

**Method 2: AWS CLI with Docker Credential Helper**

```bash
# Install credential helper
sudo apt install amazon-ecr-credential-helper

# Configure Docker
cat ~/.docker/config.json
{
  "credsStore": "ecr-login"
}

# Docker automatically authenticates
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/vehixcare-api:latest
```

**Method 3: Manual Login (CodeBuild)**

```bash
# In CodeBuild pre_build phase
aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

---

## AWS CodeBuild Integration

### buildspec.yml with Docker Build

```yaml
# buildspec.yml
version: 0.2

env:
  variables:
    DOTNET_VERSION: "9.0"
    ECR_REPOSITORY: "vehixcare-api"
    AWS_ACCOUNT_ID: "123456789012"
    AWS_DEFAULT_REGION: "us-east-1"

phases:
  install:
    runtime-versions:
      dotnet: $DOTNET_VERSION
      docker: 20
    commands:
      - echo "Installing dependencies..."
      - apt-get update && apt-get install -y curl

  pre_build:
    commands:
      - echo "Logging into Amazon ECR..."
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}

  build:
    commands:
      - echo "Building Docker image..."
      - docker build -t $ECR_REPOSITORY:$IMAGE_TAG -f Dockerfile .
      - docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
      - docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:latest

  post_build:
    commands:
      - echo "Pushing Docker image to ECR..."
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:latest
      - printf '[{"name":"api","imageUri":"%s"}]' $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json
```

---

## AWS ECS Task Definition

### ECS Task Definition with Docker Image

```json
{
  "family": "vehixcare-api",
  "taskRoleArn": "arn:aws:iam::123456789012:role/ecsTaskRole",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecsExecutionRole",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "runtimePlatform": {
    "operatingSystemFamily": "LINUX",
    "cpuArchitecture": "ARM64"
  },
  "containerDefinitions": [
    {
      "name": "api",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/vehixcare-api:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ASPNETCORE_ENVIRONMENT",
          "value": "Production"
        },
        {
          "name": "AWS_REGION",
          "value": "us-east-1"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/vehixcare-api",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

---

## Docker Compose for Local AWS Development

```yaml
# docker-compose.yml - Local development with AWS services
version: '3.8'

services:
  mongodb:
    image: mongo:7.0
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
    volumes:
      - mongodb_data:/data/db

  localstack:
    image: localstack/localstack:latest
    ports:
      - "4566:4566"
    environment:
      - SERVICES=sns,sqs
      - AWS_DEFAULT_REGION=us-east-1
    volumes:
      - localstack_data:/var/lib/localstack

  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: final
    ports:
      - "8080:8080"
    environment:
      ASPNETCORE_ENVIRONMENT: Development
      AWS_REGION: us-east-1
      AWS_ACCESS_KEY_ID: test
      AWS_SECRET_ACCESS_KEY: test
      AWS_ENDPOINT_URL: http://localstack:4566
      MONGODB_CONNECTION_STRING: mongodb://admin:password@mongodb:27017
    depends_on:
      - mongodb
      - localstack
    volumes:
      - ./Vehixcare.API:/app
      - ~/.nuget/packages:/root/.nuget/packages:ro

volumes:
  mongodb_data:
  localstack_data:
```

---

## Advanced Dockerfile Patterns for AWS

### Build Arguments for Environment-Specific Configuration

```dockerfile
# Define build arguments with defaults
ARG ENVIRONMENT=Production
ARG BUILD_VERSION=1.0.0
ARG COMMIT_SHA=unknown
ARG AWS_REGION=us-east-1

# Use build arguments in the build stage
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
ARG ENVIRONMENT
ARG BUILD_VERSION
ARG COMMIT_SHA
ARG AWS_REGION

# Pass build arguments to the compiler
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish \
    /p:Environment=$ENVIRONMENT \
    /p:Version=$BUILD_VERSION \
    /p:SourceRevisionId=$COMMIT_SHA \
    /p:AWSRegion=$AWS_REGION

# Pass to final stage
FROM base AS final
ARG ENVIRONMENT
ARG AWS_REGION
ENV ASPNETCORE_ENVIRONMENT=$ENVIRONMENT
ENV AWS_REGION=$AWS_REGION
```

**Build with arguments:**
```bash
docker build \
    --build-arg ENVIRONMENT=Staging \
    --build-arg BUILD_VERSION=2.0.0 \
    --build-arg COMMIT_SHA=$(git rev-parse --short HEAD) \
    --build-arg AWS_REGION=us-west-2 \
    -t vehixcare-api:staging .
```

### Cache Mounts for Faster Package Restoration

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Use cache mount for NuGet packages
RUN --mount=type=cache,id=nuget,target=/root/.nuget/packages \
    dotnet restore "Vehixcare.API/Vehixcare.API.csproj"

COPY . .
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish
```

### Health Check Implementation for ECS

```csharp
// Program.cs - Health check endpoint for ECS
app.MapHealthChecks("/health", new HealthCheckOptions
{
    ResponseWriter = async (context, report) =>
    {
        context.Response.ContentType = "application/json";
        var result = new
        {
            status = report.Status.ToString(),
            checks = report.Entries.Select(e => new
            {
                name = e.Key,
                status = e.Value.Status.ToString(),
                description = e.Value.Description,
                duration = e.Value.Duration
            }),
            totalDuration = report.TotalDuration,
            // AWS-specific metadata
            environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT"),
            region = Environment.GetEnvironmentVariable("AWS_REGION")
        };
        await context.Response.WriteAsync(JsonSerializer.Serialize(result));
    }
});

// Add health checks for AWS services
builder.Services.AddHealthChecks()
    .AddMongoDb(connectionString, "MongoDB", HealthStatus.Degraded)
    .AddUrlGroup(new Uri("https://sns.us-east-1.amazonaws.com"), "SNS", HealthStatus.Degraded)
    .AddCheck<AwsCredentialsHealthCheck>("AWS Credentials");
```

---

## Troubleshooting Docker on AWS

### Issue 1: ECR Authentication Failed

**Error:** `unauthorized: authentication required`

**Solution:**
```bash
# Verify IAM role permissions
aws sts get-caller-identity

# Refresh ECR login
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# Check repository existence
aws ecr describe-repositories --repository-names vehixcare-api
```

### Issue 2: Large Image Size for Lambda

**Problem:** Lambda has 10GB image limit, but 195MB is fine.

**Solution:** Further optimize:
```dockerfile
# Use Alpine-based images
FROM mcr.microsoft.com/dotnet/aspnet:9.0-alpine AS base

# Enable additional trimming
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish \
    /p:PublishTrimmed=true \
    /p:PublishSingleFile=true \
    /p:InvariantGlobalization=true
```

### Issue 3: ECS Task Fails to Start

**Error:** `Task failed to start: HEALTHCHECK failed`

**Solution:**
```bash
# Verify health check endpoint locally
docker run -p 8080:8080 vehixcare-api:latest
curl http://localhost:8080/health

# Check health check configuration
docker inspect vehixcare-api:latest | grep -A10 Healthcheck
```

### Issue 4: X-Ray Tracing Not Working

**Error:** `X-Ray daemon not found`

**Solution:** Add X-Ray daemon as sidecar in ECS task definition:
```json
{
  "containerDefinitions": [
    {
      "name": "xray-daemon",
      "image": "amazon/aws-xray-daemon:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 2000,
          "protocol": "udp"
        }
      ]
    }
  ]
}
```

---

## Security Best Practices for AWS

### Non-Root User Execution

```dockerfile
# Create non-root user
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser
```

### Secrets Management (Never in Dockerfile)

```bash
# BAD - Secret in image layer
ENV DB_PASSWORD=supersecret

# GOOD - Pass via ECS secrets or Parameter Store
# ECS task definition:
{
  "secrets": [
    {
      "name": "DB_PASSWORD",
      "valueFrom": "arn:aws:secretsmanager:us-east-1:123456789012:secret:vehixcare/db-password"
    }
  ]
}
```

### Vulnerability Scanning with Amazon Inspector

```bash
# Scan image with Amazon Inspector
aws inspector2 scan-findings \
    --filter-criteria '{"resourceType":[{"comparison":"EQUALS","value":"AWS_ECR_CONTAINER_IMAGE"}]}'

# Enable ECR scanning
aws ecr put-image-scanning-configuration \
    --repository-name vehixcare-api \
    --image-scanning-configuration scanOnPush=true
```

---

## Performance Comparison: Dockerfile vs. SDK-Native on AWS

| Metric | Traditional Dockerfile | SDK-Native (Trimmed) | Improvement |
|--------|------------------------|---------------------|-------------|
| **CodeBuild Time** | 85 seconds | 52 seconds | 39% faster |
| **Image Size** | 198 MB | 78 MB | 61% smaller |
| **Push to ECR** | 14 seconds | 9 seconds | 36% faster |
| **Pull from ECR** | 18 seconds | 11 seconds | 39% faster |
| **ECS Task Start** | 185 ms | 95 ms | 49% faster |
| **ECR Storage Cost** | $0.10/mo | $0.04/mo | 60% lower |
| **Layer Count** | 8-12 | 4-6 | Simpler |

---

## Conclusion: The Enduring Value of Dockerfiles on AWS

While SDK-native publishing offers compelling advantages for new projects, the traditional Dockerfile approach remains essential for AWS deployments:

- **Complex multi-stage builds** with custom intermediate images
- **Legacy applications** with specific base image requirements (Amazon Linux)
- **Multi-container orchestration** with ECS task definitions
- **Teams requiring full transparency** into the build process
- **Organizations with established Docker CI/CD pipelines** in CodeBuild

The Dockerfile format has evolved into a sophisticated domain-specific language that, when mastered, provides unparalleled control over container builds on AWS. As we've seen with Vehixcare-API, a well-optimized Dockerfile can achieve excellent performance while maintaining the transparency and flexibility that production environments demand.

---

### Stories at a Glance

**Complete AWS series (10 stories):**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference - AWS** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides for Amazon ECR

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker - AWS** – A deep dive into MSBuild configuration, multi-architecture builds (Graviton ARM64), and direct Amazon ECR integration with IAM roles

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach - AWS** – Mastering multi-stage builds, build cache optimization, and Amazon ECR authentication for enterprise CI/CD pipelines on AWS *(This story)*

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative - AWS** – Transitioning from Docker to Podman, rootless containers for enhanced security, and Amazon ECR integration with Podman Desktop

- 🏗️ **5. AWS CDK & Copilot: Infrastructure as Code for Containers - AWS** – Deploying to Amazon ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless container orchestration

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop AWS Deployments - AWS** – Leveraging Visual Studio's AWS Toolkit, one-click publish to Amazon ECR, and debugging containerized apps on AWS

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs without a runtime, integrating with Amazon Inspector for vulnerability scanning, and deploying to air-gapped AWS environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows - AWS** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation (x64 to Graviton), and Amazon ECR push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker - AWS** – Using the konet .NET tool for cross-platform image generation, AMD64/ARM64 (Graviton) simultaneous builds, and AWS CodeBuild optimization

- ☸️ **10. Kubernetes Native Deployments: Orchestrating .NET 10 Containers on Amazon EKS - AWS** – Deploying to Amazon EKS, Helm charts, GitOps with Flux, ALB Ingress Controller, and production-grade operations

---

## What's Next?

Over the coming weeks, each approach in this AWS series will be explored in exhaustive detail. We'll examine real-world AWS deployment scenarios, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first containerized application on AWS Fargate or an enterprise migrating thousands of workloads to Amazon EKS, you'll find practical guidance tailored to your infrastructure requirements.

The evolution from Dockerfile-centric builds to SDK-native containerization reflects a maturing ecosystem where .NET 10 stands at the forefront of developer experience on AWS. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from rapid prototyping on AWS Graviton to mission-critical production deployments on Amazon EKS.

**Coming next in the series:**
**🔐 Traditional Dockerfile with Podman: The Daemonless Alternative - AWS** – Transitioning from Docker to Podman, rootless containers for enhanced security, and Amazon ECR integration with Podman Desktop