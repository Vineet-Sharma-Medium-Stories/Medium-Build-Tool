# Traditional Dockerfile with Docker: The Classic Approach

## Mastering Containerization with Industry-Standard Tooling

### Introduction: The Foundation of Containerized .NET Applications

In the [previous installments](#) of this series, we explored the cutting-edge world of SDK-native container publishing—building OCI images without Docker, achieving 78% smaller images and 39% faster builds with the Vehixcare-API fleet management platform. While SDK-native represents the future, the traditional Dockerfile with Docker remains the **industry standard** for containerizing .NET applications, and for good reason.

The Dockerfile approach, now over a decade old, has evolved into a sophisticated, battle-tested methodology that offers something no other approach can match: **complete transparency and control**. Every layer is explicitly defined, every dependency is documented in code, and the build process is fully observable. For organizations subject to regulatory compliance, running mission-critical workloads, or managing complex multi-container applications, this visibility is non-negotiable.

In this installment, we'll master the Dockerfile approach using Vehixcare-API as our case study—a sophisticated .NET 9.0 fleet management platform with real-time telemetry, SignalR hubs, MongoDB integration, and multiple background services. We'll explore multi-stage builds, layer caching optimization, .dockerignore patterns, and production-grade Azure Container Registry integration.

```mermaid
graph TD
    subgraph "Traditional Docker Build Pipeline"
        A[Source Code] --> B[Docker Build Context]
        B --> C[Docker Daemon]
        C --> D[Multi-stage Build]
        D --> E[Build Stage<br/>SDK + Dependencies]
        D --> F[Runtime Stage<br/>Only Runtime + App]
        E --> G[Container Image]
        F --> G
        G --> H[Azure Container Registry]
        H --> I[Kubernetes/ACA]
    end
    
    style D fill:#48bb78,color:#fff
    style E fill:#2b6cb0,color:#fff
    style F fill:#48bb78,color:#fff
```

### Stories at a Glance

**Companion stories in this series:**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker** – A deep dive into MSBuild configuration, multi-architecture builds, Native AOT optimization, and direct Azure Container Registry integration with workload identity federation

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach** – Mastering multi-stage builds, build cache optimization, .dockerignore patterns, and Azure Container Registry authentication for enterprise CI/CD pipelines *(This story)*

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop

- ⚡ **5. Azure Developer CLI (azd) with .NET Aspire: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, Redis caching, and infrastructure-as-code with Bicep templates

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop Azure Deployments** – Leveraging Visual Studio's built-in Podman/Docker support, one-click publish to Azure Container Registry, and debugging containerized apps with Hot Reload

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation, and Azure Container Registry push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization

---

## Understanding the Docker Build Process

Before diving into Vehixcare's Dockerfile, we must understand how Docker builds container images. The process involves several key components:

### Docker Build Context

When you run `docker build`, Docker packages the **build context**—typically the current directory—and sends it to the Docker daemon:

```bash
# The '.' specifies the build context
docker build -t vehixcare-api:latest .
```

**What's included:** Everything in the current directory (and subdirectories) is sent to the Docker daemon, unless excluded by `.dockerignore`. This context can be large—for Vehixcare, it includes:
- Source code (10-50 MB)
- Project files (1-5 MB)
- Git history (100-500 MB)
- Binaries and obj folders (50-200 MB)
- Documentation and assets (5-50 MB)

**Why it matters:** Large build contexts slow down builds and waste bandwidth. Optimizing context size is critical for CI/CD pipelines.

### Dockerfile Instructions

Each instruction in a Dockerfile creates a **layer** in the final image. Layers are cached, so ordering matters significantly:

| Instruction | Purpose | Layer Characteristics |
|-------------|---------|----------------------|
| `FROM` | Base image | Creates new stage, resets layer cache |
| `WORKDIR` | Set working directory | Metadata only, no size impact |
| `COPY` | Copy files from context | Creates layer with copied files |
| `RUN` | Execute commands | Creates layer with command output |
| `ENV` | Set environment variables | Metadata only |
| `EXPOSE` | Document ports | Metadata only |
| `ENTRYPOINT` | Set default executable | Metadata only |

## The Vehixcare-API Dockerfile: Production-Ready Configuration

Let's examine Vehixcare's complete production Dockerfile, with detailed commentary on each section:

```dockerfile
# ============================================
# STAGE 1: Base Runtime Image
# ============================================
# Use the official ASP.NET Core runtime image as base
# This image is ~190MB and contains the .NET runtime but not the SDK
FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS base
WORKDIR /app

# Expose ports (documentation only, does not publish ports)
# 8080 for HTTP, 8443 for HTTPS
EXPOSE 8080
EXPOSE 8443

# Create a non-root user for security
# Running as non-root reduces attack surface
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# ============================================
# STAGE 2: Build Image with SDK
# ============================================
# Use the full SDK image for compilation
# This image is ~1.2GB but is not included in final image
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
# This layer is cached only if source code changes
WORKDIR "/src/Vehixcare.API"
RUN dotnet build "Vehixcare.API.csproj" -c Release -o /app/build

# ============================================
# STAGE 3: Publish Optimized Artifacts
# ============================================
FROM build AS publish
# Publish with optimizations:
# - Release configuration
# - Trimming to remove unused code (reduces size by 50-70%)
# - ReadyToRun for faster startup
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

# Configure environment variables
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:8080;https://+:8443

# Health check for orchestration platforms
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Set the entry point
ENTRYPOINT ["dotnet", "Vehixcare.API.dll"]
```

### Layer-by-Layer Analysis

Let's analyze each layer's size and cache behavior:

| Layer | Size | Cache Key | Invalidation Trigger |
|-------|------|-----------|---------------------|
| `FROM aspnet:9.0` | ~190 MB | Image digest | Rare (base image updates) |
| `RUN adduser` | ~1 MB | Command hash | Never (only once) |
| `COPY project files` | ~50 KB | File content hashes | When any .csproj changes |
| `RUN dotnet restore` | ~500 MB | .csproj + nuget.config | When packages change |
| `COPY source code` | ~5-15 MB | All source files | Every code change |
| `RUN dotnet build` | ~200 MB | Source + bin/obj | Every code change |
| `RUN dotnet publish` | ~150 MB | Build output | Every code change |
| `COPY --from=publish` | ~150 MB | Published output | Every code change |
| **Final image** | **~195 MB** | - | - |

### Optimizing the Dockerfile for Vehixcare

#### 1. Multi-Stage Build Optimization

The multi-stage pattern separates the SDK-heavy build environment from the lean runtime environment:

```dockerfile
# Build stage: Includes SDK (~1.2 GB)
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
# ... compile application ...

# Runtime stage: Only runtime (~190 MB)
FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
COPY --from=build /app/publish .
```

**Result:** Final image size reduced from 1.4 GB to ~195 MB.

#### 2. Layer Caching Optimization

Ordering `COPY` commands from least-frequently-changed to most-frequently-changed:

```dockerfile
# Good: Project files first (change rarely)
COPY *.csproj ./
RUN dotnet restore

# Bad: Source code first (changes constantly)
COPY . ./
RUN dotnet restore  # Restores every build!
```

#### 3. Multi-Stage Build with Multiple Projects

Vehixcare has 7+ projects. Copying all project files individually ensures optimal caching:

```dockerfile
# Copy each project's .csproj individually
COPY ["Vehixcare.API/Vehixcare.API.csproj", "Vehixcare.API/"]
COPY ["Vehixcare.Business/Vehixcare.Business.csproj", "Vehixcare.Business/"]
# ... continue for all projects

# Restore the main project (restores all dependencies)
RUN dotnet restore "Vehixcare.API/Vehixcare.API.csproj"
```

## The .dockerignore File: Optimizing Build Context

A well-configured `.dockerignore` file is essential for fast builds. Here's Vehixcare's optimized `.dockerignore`:

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

# Secrets
*.pfx
*.pem
*.key
secrets.json
appsettings.Production.json

# CI/CD
.github/
.gitlab/
azure-pipelines.yml

# Seed data (large files)
Vehixcare.SeedData/Data/
*.dump
*.backup

# OS files
.DS_Store
Thumbs.db
```

**Impact on build performance:**

| Metric | Without .dockerignore | With .dockerignore |
|--------|----------------------|-------------------|
| Build context size | 350 MB | 15 MB |
| Context upload time | 12 seconds | 0.5 seconds |
| First build time | 95 seconds | 45 seconds |

## Advanced Dockerfile Patterns for Vehixcare

### Build Arguments for Environment-Specific Configuration

```dockerfile
# Define build arguments with defaults
ARG ENVIRONMENT=Production
ARG BUILD_VERSION=1.0.0
ARG COMMIT_SHA=unknown

# Use build arguments in the build stage
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
ARG ENVIRONMENT
ARG BUILD_VERSION
ARG COMMIT_SHA

# Pass build arguments to the compiler
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish \
    /p:Environment=$ENVIRONMENT \
    /p:Version=$BUILD_VERSION \
    /p:SourceRevisionId=$COMMIT_SHA

# Pass to final stage
FROM base AS final
ARG ENVIRONMENT
ENV ASPNETCORE_ENVIRONMENT=$ENVIRONMENT
```

**Build with arguments:**
```bash
docker build \
    --build-arg ENVIRONMENT=Staging \
    --build-arg BUILD_VERSION=2.0.0 \
    --build-arg COMMIT_SHA=$(git rev-parse --short HEAD) \
    -t vehixcare-api:staging .
```

### Multi-Platform Builds with Buildx

Docker Buildx enables building for multiple architectures from a single build:

```bash
# Create a new builder instance
docker buildx create --name multiarch --use

# Build for both AMD64 and ARM64
docker buildx build \
    --platform linux/amd64,linux/arm64 \
    -t vehixcare.azurecr.io/vehixcare-api:latest \
    --push \
    .
```

### Using Cache Mounts for Faster Package Restoration

Docker 18.09+ supports cache mounts to persist NuGet packages between builds:

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Use cache mount for NuGet packages
RUN --mount=type=cache,id=nuget,target=/root/.nuget/packages \
    dotnet restore "Vehixcare.API/Vehixcare.API.csproj"

COPY . .
RUN dotnet publish "Vehixcare.API.csproj" -c Release -o /app/publish
```

### Health Check Implementation

Vehixcare's health check endpoint provides detailed system status:

```csharp
// Program.cs
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
            totalDuration = report.TotalDuration
        };
        await context.Response.WriteAsync(JsonSerializer.Serialize(result));
    }
});
```

## Azure Container Registry Integration

### Authentication Methods

**Method 1: Azure CLI (Local Development)**
```bash
# Login to Azure
az login

# Login to ACR
az acr login --name vehixcare

# Build and push
docker build -t vehixcare.azurecr.io/vehixcare-api:latest .
docker push vehixcare.azurecr.io/vehixcare-api:latest
```

**Method 2: Service Principal (CI/CD)**
```bash
# Login with service principal
docker login vehixcare.azurecr.io \
    --username $SP_APP_ID \
    --password $SP_PASSWORD

# Build and push
docker build -t vehixcare.azurecr.io/vehixcare-api:$BUILD_ID .
docker push vehixcare.azurecr.io/vehixcare-api:$BUILD_ID
```

**Method 3: Managed Identity (Azure DevOps)**
```yaml
- task: Docker@2
  inputs:
    containerRegistry: 'ACR Service Connection'
    repository: 'vehixcare-api'
    command: 'buildAndPush'
    Dockerfile: '**/Dockerfile'
    tags: '$(Build.BuildId)'
```

### ACR Tasks for Automated Builds

Azure Container Registry Tasks can build Docker images directly in Azure:

```bash
# Create a quick task
az acr build \
    --registry vehixcare \
    --image vehixcare-api:latest \
    --file Dockerfile \
    .
```

## Docker Compose for Local Development

Vehixcare uses Docker Compose for local development with MongoDB:

```yaml
# docker-compose.yml
version: '3.8'

services:
  mongodb:
    image: mongo:7.0
    container_name: vehixcare-mongodb
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
      MONGO_INITDB_DATABASE: vehixcare
    volumes:
      - mongodb_data:/data/db
      - ./scripts/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: final
      args:
        ENVIRONMENT: Development
    container_name: vehixcare-api
    ports:
      - "8080:8080"
      - "8443:8443"
    environment:
      ASPNETCORE_ENVIRONMENT: Development
      ASPNETCORE_URLS: http://+:8080;https://+:8443
      MONGODB_CONNECTION_STRING: mongodb://admin:password@mongodb:27017/vehixcare?authSource=admin
    depends_on:
      mongodb:
        condition: service_healthy
    volumes:
      - ./Vehixcare.API:/app
      - ~/.nuget/packages:/root/.nuget/packages:ro
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  seed-data:
    build:
      context: .
      dockerfile: Dockerfile.seed
    container_name: vehixcare-seed
    environment:
      MONGODB_CONNECTION_STRING: mongodb://admin:password@mongodb:27017/vehixcare?authSource=admin
    depends_on:
      mongodb:
        condition: service_healthy
    restart: "no"

volumes:
  mongodb_data:
```

### Dockerfile for Seed Data

```dockerfile
# Dockerfile.seed
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src
COPY ["Vehixcare.SeedData/Vehixcare.SeedData.csproj", "Vehixcare.SeedData/"]
COPY ["Vehixcare.Data/Vehixcare.Data.csproj", "Vehixcare.Data/"]
COPY ["Vehixcare.Models/Vehixcare.Models.csproj", "Vehixcare.Models/"]
RUN dotnet restore "Vehixcare.SeedData/Vehixcare.SeedData.csproj"
COPY . .
WORKDIR "/src/Vehixcare.SeedData"
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/runtime:9.0 AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "Vehixcare.SeedData.dll"]
```

## CI/CD Pipeline Integration

### GitHub Actions with Docker Build

```yaml
name: Docker Build and Push

on:
  push:
    branches: [main, develop]
    tags: ['v*']
  pull_request:
    branches: [main]

env:
  ACR_NAME: vehixcare
  IMAGE_NAME: vehixcare-api
  DOCKERFILE_PATH: ./Dockerfile

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      id-token: write

    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Cache Docker layers
      uses: actions/cache@v3
      with:
        path: /tmp/.buildx-cache
        key: ${{ runner.os }}-buildx-${{ github.sha }}
        restore-keys: |
          ${{ runner.os }}-buildx-

    - name: Login to Azure
      uses: azure/login@v1
      with:
        client-id: ${{ secrets.AZURE_CLIENT_ID }}
        tenant-id: ${{ secrets.AZURE_TENANT_ID }}
        subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

    - name: Login to ACR
      run: az acr login --name ${{ env.ACR_NAME }}

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        file: ${{ env.DOCKERFILE_PATH }}
        push: ${{ github.event_name != 'pull_request' }}
        tags: |
          ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
          ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:latest
          ${{ github.ref_type == 'tag' && format('{0}.azurecr.io/{1}:{2}', env.ACR_NAME, env.IMAGE_NAME, github.ref_name) || '' }}
        cache-from: type=local,src=/tmp/.buildx-cache
        cache-to: type=local,dest=/tmp/.buildx-cache-new,mode=max
        build-args: |
          BUILD_VERSION=${{ github.sha }}
          COMMIT_SHA=${{ github.sha }}
          ENVIRONMENT=${{ github.ref == 'refs/heads/main' && 'Production' || 'Staging' }}

    - name: Move cache
      run: |
        rm -rf /tmp/.buildx-cache
        mv /tmp/.buildx-cache-new /tmp/.buildx-cache

    - name: Deploy to Azure Container Apps
      if: github.ref == 'refs/heads/main'
      run: |
        az containerapp update \
          --name vehixcare-api \
          --resource-group vehixcare-rg \
          --image ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }} \
          --revision-suffix ${{ github.sha }}
```

### Azure DevOps Pipeline

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
    - main
    - develop
  tags:
    include:
    - v*

variables:
  dockerRegistryServiceConnection: 'ACR-Service-Connection'
  imageRepository: 'vehixcare-api'
  containerRegistry: 'vehixcare.azurecr.io'
  dockerfilePath: '$(Build.SourcesDirectory)/Dockerfile'
  tag: '$(Build.BuildId)'

stages:
- stage: Build
  displayName: 'Build and push stage'
  jobs:
  - job: Build
    displayName: 'Build'
    pool:
      vmImage: 'ubuntu-latest'
    steps:
    - task: Docker@2
      displayName: 'Build and push'
      inputs:
        containerRegistry: '$(dockerRegistryServiceConnection)'
        repository: '$(imageRepository)'
        command: 'buildAndPush'
        Dockerfile: '$(dockerfilePath)'
        buildContext: '$(Build.SourcesDirectory)'
        tags: |
          $(tag)
          latest
          $(Build.SourceBranchName)
        arguments: '--build-arg BUILD_VERSION=$(Build.BuildId) --build-arg COMMIT_SHA=$(Build.SourceVersion)'

    - task: AzureCLI@2
      displayName: 'Deploy to ACA'
      inputs:
        azureSubscription: 'vehixcare-service-connection'
        scriptType: 'bash'
        scriptLocation: 'inlineScript'
        inlineScript: |
          az containerapp update \
            --name vehixcare-api \
            --resource-group vehixcare-rg \
            --image $(containerRegistry)/$(imageRepository):$(tag) \
            --revision-suffix $(Build.BuildId)
```

## Security Best Practices

### Non-Root User Execution

```dockerfile
# Create non-root user
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser
```

### Minimal Base Images

```dockerfile
# Use runtime-deps for even smaller images (no .NET runtime)
FROM mcr.microsoft.com/dotnet/runtime-deps:9.0 AS base
# For self-contained deployments only
```

### Secret Management

Never embed secrets in Docker images:

```dockerfile
# BAD - Secret in image layer
ENV DB_PASSWORD=supersecret

# GOOD - Pass at runtime
ENV DB_PASSWORD=
```

```bash
# Pass secrets at runtime
docker run -e DB_PASSWORD=$DB_PASSWORD vehixcare-api:latest

# Or use Docker secrets (Swarm)
echo "supersecret" | docker secret create db_password -
```

### Vulnerability Scanning

```bash
# Scan with Trivy
trivy image vehixcare.azurecr.io/vehixcare-api:latest

# Scan with Docker Scout
docker scout quickview vehixcare.azurecr.io/vehixcare-api:latest

# Scan with Snyk
snyk container test vehixcare.azurecr.io/vehixcare-api:latest
```

## Troubleshooting Common Dockerfile Issues

### Issue 1: Large Image Size

**Problem:** Final image is 800MB+ when it should be ~200MB.

**Diagnosis:**
```bash
# Analyze image layers
docker history vehixcare-api:latest --no-trunc

# Check layer sizes
docker history vehixcare-api:latest --format "{{.Size}} {{.CreatedBy}}"
```

**Solution:** Ensure multi-stage builds are properly separating SDK and runtime.

### Issue 2: Slow Build Times

**Problem:** Every build takes 5+ minutes.

**Diagnosis:**
```bash
# Check if cache is being invalidated
docker build --progress=plain -t vehixcare-api:latest . 2>&1 | grep "CACHED"
```

**Solution:** Optimize layer order and use `.dockerignore`.

### Issue 3: Permission Denied When Writing to /app

**Problem:** `UnauthorizedAccessException: Access to the path '/app/logs' is denied.`

**Solution:** Ensure non-root user has write permissions:
```dockerfile
RUN mkdir -p /app/logs && chown -R appuser:appuser /app/logs
USER appuser
```

### Issue 4: Health Check Failing

**Problem:** Container shows unhealthy in orchestrators.

**Solution:** Implement a proper health check endpoint and ensure `curl` is available:
```dockerfile
# Install curl if needed
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1
```

## Performance Comparison: Dockerfile vs. SDK-Native

| Metric | Traditional Dockerfile | SDK-Native (Trimmed) |
|--------|------------------------|---------------------|
| **Build Time** | 85 seconds | 52 seconds |
| **Image Size** | 198 MB | 78 MB |
| **Push Time** | 14 seconds | 9 seconds |
| **Startup Time** | 185 ms | 95 ms |
| **Layer Count** | 8-12 | 4-6 |
| **Cache Efficiency** | Manual | Automatic |
| **Build Context** | 15 MB (ignored) | N/A |

## Conclusion: The Enduring Value of Dockerfiles

While SDK-native publishing offers compelling advantages for new projects, the traditional Dockerfile approach remains essential for:

- **Complex multi-stage builds** with custom intermediate images
- **Legacy applications** with specific base image requirements
- **Multi-container orchestration** with docker-compose
- **Teams requiring full transparency** into the build process
- **Organizations with established Docker CI/CD pipelines**

The Dockerfile format has evolved into a sophisticated domain-specific language that, when mastered, provides unparalleled control over container builds. As we've seen with Vehixcare-API, a well-optimized Dockerfile can achieve excellent performance while maintaining the transparency and flexibility that production environments demand.

---

### Stories at a Glance

**Companion stories in this series:**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker** – A deep dive into MSBuild configuration, multi-architecture builds, Native AOT optimization, and direct Azure Container Registry integration with workload identity federation

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach** – Mastering multi-stage builds, build cache optimization, .dockerignore patterns, and Azure Container Registry authentication for enterprise CI/CD pipelines *(This story)*

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop

- ⚡ **5. Azure Developer CLI (azd) with .NET Aspire: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, Redis caching, and infrastructure-as-code with Bicep templates

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop Azure Deployments** – Leveraging Visual Studio's built-in Podman/Docker support, one-click publish to Azure Container Registry, and debugging containerized apps with Hot Reload

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation, and Azure Container Registry push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization

---

**Coming next in the series:**
**🔐 Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop