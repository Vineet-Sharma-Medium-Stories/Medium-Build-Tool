# Pip + Docker: The Classic Python Containerization - AWS

## Battle-Tested Requirements.txt Approach for FastAPI on Amazon ECR

### Introduction: The Foundation of Python Containerization on AWS

In the [previous installments](#) of this AWS Python series, we explored modern approaches to Python containerization—Poetry with multi-stage builds for deterministic dependency management, and UV for blazing-fast package installation. While these modern tools offer significant advantages, the **traditional pip + requirements.txt** approach remains the most widely used, battle-tested, and universally compatible method for containerizing Python applications on AWS.

For the **AI Powered Video Tutorial Portal**—a FastAPI application with MongoDB integration, JWT authentication, and comprehensive user engagement features—the pip approach offers unparalleled simplicity and compatibility. It works on every Python runtime, every AWS region, and every CI/CD platform without requiring additional tooling. For teams new to containerization, migrating legacy applications, or working in AWS environments with strict tooling requirements, pip is the reliable foundation upon which Python containerization on Amazon ECR was built.

This installment explores the complete workflow for containerizing pip-managed Python applications for AWS, using the Courses Portal API as our case study. We'll master multi-stage builds, layer caching optimization, requirements.txt best practices, and production-grade Amazon ECR integration—all with the simplicity and ubiquity of the classic pip approach.

```mermaid
graph TD
    subgraph "Traditional Python Workflow on AWS"
        A[requirements.txt] --> B[pip install]
        B --> C[Virtual Environment]
        C --> D[Application Code]
    end
    
    subgraph "Container Build (Multi-Stage)"
        E[Builder Stage] --> F[COPY requirements.txt]
        F --> G[pip install --user]
        G --> H[Runtime Stage]
        H --> I[Copy Dependencies]
        I --> J[Copy App Code]
    end
    
    subgraph "AWS Deployment"
        J --> K[Amazon ECR]
        K --> L[ECS Fargate]
        K --> M[Amazon EKS]
        K --> N[AWS App Runner]
    end
    
    style F fill:#48bb78,color:#fff
    style G fill:#2b6cb0,color:#fff
    style K fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS *(This story)*

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## Understanding requirements.txt: The Classic Approach for AWS

### Why Pip Remains Essential on AWS

| Aspect | Pip + requirements.txt | Modern Tools (Poetry/UV) | AWS Impact |
|--------|------------------------|-------------------------|------------|
| **Ubiquity** | Every Python installation includes pip | Requires additional installation | Works on all EC2 AMIs |
| **Simplicity** | Single file, no configuration | Lock files, configuration files | Easier to debug |
| **Compatibility** | Works everywhere | May require specific versions | Universal AWS region support |
| **CI/CD Integration** | Native to CodeBuild, CodePipeline | May need setup steps | Faster pipeline setup |
| **Learning Curve** | Minimal | Moderate | Team onboarding |
| **Deterministic Builds** | Requires pip freeze | Built-in lock files | Requires discipline |

### The requirements.txt Format for AWS

```txt
# requirements.txt for AI Powered Video Tutorial Portal
# Production dependencies only - optimized for Amazon ECR

# Core Framework
fastapi==0.104.0
uvicorn[standard]==0.24.0
pydantic[email]==2.5.0

# Database (Amazon DocumentDB compatible)
motor==3.3.0
pymongo==4.5.0

# Authentication
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# AWS SDK (for Secrets Manager, Parameter Store)
boto3==1.28.0
aiobotocore==2.5.0

# HTTP Client
httpx==0.25.0

# Caching & Rate Limiting (ElastiCache Redis)
redis==5.0.0

# Utilities
python-dotenv==1.0.0
aiofiles==23.2.0
email-validator==2.1.0

# Monitoring (CloudWatch)
prometheus-client==0.19.0
```

### Generating requirements.txt for AWS

```bash
# From active virtual environment
pip freeze > requirements.txt

# From Poetry project
poetry export -f requirements.txt --output requirements.txt --without-hashes

# From UV project
uv pip freeze > requirements.txt

# Pin specific versions for reproducibility
pip freeze | grep -E "fastapi|uvicorn|motor|boto3" > requirements.txt
```

---

## The Pip-Optimized Dockerfile for AWS: Production-Ready Configuration

Let's examine the complete production Dockerfile for the Courses Portal API, optimized for pip and AWS deployment:

```dockerfile
# ============================================
# AI Powered Video Tutorial Portal - Pip Build for AWS
# ============================================
# Production-ready Dockerfile for FastAPI + pip
# Traditional multi-stage build with layer caching optimization
# Optimized for Amazon ECR, ECS Fargate, and AWS Graviton

# ============================================
# STAGE 1: Builder with pip
# ============================================
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Copy requirements first for optimal layer caching
# This layer only changes when dependencies change
COPY requirements.txt .

# Install dependencies to a user-owned directory for better caching
# --user: Install to user site-packages
# --no-cache-dir: Don't cache locally (we use Docker layer cache)
# --no-warn-script-location: Cleaner output
RUN pip install --user --no-cache-dir --no-warn-script-location -r requirements.txt

# ============================================
# STAGE 2: Runtime Image
# ============================================
FROM python:3.11-slim AS runtime

# Install runtime dependencies for health checks and AWS metadata
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security (AWS best practice)
RUN useradd --create-home --shell /bin/bash appuser && \
    mkdir -p /app/logs && \
    chown -R appuser:appuser /app

WORKDIR /app

# Copy installed Python packages from builder stage
# This includes all production dependencies
COPY --from=builder /root/.local /root/.local

# Copy application source code
COPY . .

# Ensure scripts in PATH
ENV PATH=/root/.local/bin:$PATH

# Set ownership of application files
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port (FastAPI default)
EXPOSE 8000

# Health check for ECS/ALB and App Runner
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run with uvicorn
# Using exec form for proper signal handling
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Layer Analysis and Optimization for AWS ECR

### Layer-by-Layer Breakdown

| Layer | Size | Cache Key | AWS ECR Cost Impact |
|-------|------|-----------|---------------------|
| `FROM python:3.11-slim` | ~180 MB | Image digest | $0.09/GB-month |
| `COPY requirements.txt` | ~1 KB | File content hash | Negligible |
| `RUN pip install --user` | ~150-300 MB | requirements.txt | $0.08-0.15/GB-month |
| `RUN apt-get install curl` | ~20 MB | Package list | $0.01/GB-month |
| `RUN useradd` | ~1 MB | Command hash | Negligible |
| `COPY application code` | ~1-10 MB | All source files | Minimal |
| **Final image** | **~350-500 MB** | - | **$0.18-0.25/GB-month** |

### Optimization Strategies for AWS

**1. Dependency Caching - The Golden Rule**

```dockerfile
# GOOD: Copy requirements first
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# BAD: Copy all code first
COPY . .
RUN pip install --user -r requirements.txt  # Runs on every code change!
```

**2. Use `--no-cache-dir` for Smaller Images**

```dockerfile
RUN pip install --user --no-cache-dir -r requirements.txt
# Saves ~50-100 MB by not storing pip cache
# Reduces ECR storage costs by 20-30%
```

**3. Use `--require-hashes` for Supply Chain Security**

```txt
# requirements.hash.txt
fastapi==0.104.0 \
    --hash=sha256:abcdef1234567890...
uvicorn[standard]==0.24.0 \
    --hash=sha256:1234567890abcdef...
```

```dockerfile
COPY requirements.hash.txt .
RUN pip install --user --no-cache-dir --require-hashes -r requirements.hash.txt
```

**4. Use Multi-Stage with Testing Stage for AWS CodeBuild**

```dockerfile
# ============================================
# Builder Stage (Common)
# ============================================
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ============================================
# Test Stage (AWS CodeBuild)
# ============================================
FROM builder AS test
COPY requirements-dev.txt .
RUN pip install --user --no-cache-dir -r requirements-dev.txt
COPY . .
RUN pytest tests/ --cov=./

# ============================================
# Runtime Stage (Production)
# ============================================
FROM python:3.11-slim AS runtime
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Amazon ECR Integration

### Create ECR Repository

```bash
# Create ECR repository with image scanning
aws ecr create-repository \
    --repository-name courses-api \
    --image-scanning-configuration scanOnPush=true \
    --encryption-configuration encryptionType=AES256 \
    --region us-east-1

# Get repository URI
ECR_URI=$(aws ecr describe-repositories --repository-names courses-api --query 'repositories[0].repositoryUri' --output text)
echo $ECR_URI
# 123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api
```

### Build and Push to ECR

```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin $ECR_URI

# Build with pip-optimized Dockerfile
docker build -t courses-api:latest -f Dockerfile.pip .

# Tag for ECR
docker tag courses-api:latest $ECR_URI:latest
docker tag courses-api:latest $ECR_URI:$(date +%Y%m%d-%H%M%S)

# Push to ECR
docker push $ECR_URI:latest
docker push $ECR_URI:$(date +%Y%m%d-%H%M%S)
```

---

## AWS CodeBuild Integration with Pip

### buildspec.yml for Pip

```yaml
# buildspec.yml - Pip-based build for AWS CodeBuild
version: 0.2

env:
  variables:
    PYTHON_VERSION: "3.11"
    ECR_REPOSITORY: "courses-api"

phases:
  install:
    runtime-versions:
      python: $PYTHON_VERSION
    commands:
      - echo "Python version: $(python --version)"
      - pip install --upgrade pip

  pre_build:
    commands:
      - echo "Logging into Amazon ECR..."
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}

  build:
    commands:
      - echo "Building Docker image with pip..."
      - docker build -t $ECR_REPOSITORY:$IMAGE_TAG -f Dockerfile.pip .
      - docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
      - docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:latest

  post_build:
    commands:
      - echo "Pushing to ECR..."
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:latest
      - printf '[{"name":"api","imageUri":"%s"}]' $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json
```

---

## AWS Secrets Manager Integration

### Storing Secrets

```bash
# Store secrets in AWS Secrets Manager
aws secretsmanager create-secret \
    --name courses-portal/jwt-secret \
    --secret-string '{"secret":"your-super-secret-jwt-key-change-in-production"}'

aws secretsmanager create-secret \
    --name courses-portal/mongodb-uri \
    --secret-string '{"uri":"mongodb://username:password@host:27017/courses_portal?ssl=true"}'

aws secretsmanager create-secret \
    --name courses-portal/redis-uri \
    --secret-string '{"uri":"redis://redis-cluster.xxxxx.ng.0001.use1.cache.amazonaws.com:6379"}'
```

### Accessing Secrets from Python

```python
# config.py - AWS Secrets Manager integration
import boto3
import json
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # AWS region
    aws_region: str = os.getenv("AWS_REGION", "us-east-1")
    
    # Secrets Manager client (lazy initialization)
    _secrets_client = None
    
    @property
    def secrets_client(self):
        if self._secrets_client is None:
            self._secrets_client = boto3.client("secretsmanager", region_name=self.aws_region)
        return self._secrets_client
    
    def get_secret(self, secret_name: str) -> str:
        """Retrieve secret from AWS Secrets Manager or fallback to env"""
        try:
            response = self.secrets_client.get_secret_value(SecretId=secret_name)
            secret = json.loads(response["SecretString"])
            return list(secret.values())[0]
        except Exception as e:
            # Fallback to environment variable for local development
            env_key = secret_name.replace("/", "_").upper()
            return os.getenv(env_key, "")
    
    @property
    def jwt_secret_key(self) -> str:
        return self.get_secret("courses-portal/jwt-secret")
    
    @property
    def mongodb_uri(self) -> str:
        return self.get_secret("courses-portal/mongodb-uri")
    
    @property
    def redis_uri(self) -> str:
        return self.get_secret("courses-portal/redis-uri")

settings = Settings()
```

---

## AWS Copilot with Pip

### Copilot Manifest for Pip

```yaml
# copilot/api/manifest.yml
name: api
type: Load Balanced Web Service

image:
  build:
    dockerfile: Dockerfile.pip
  port: 8000

platform:
  os: linux
  arch: arm64  # Use Graviton for cost savings

cpu: 512
memory: 1024

variables:
  ASPNETCORE_ENVIRONMENT: Production
  AWS_REGION: us-east-1

secrets:
  JWT_SECRET_KEY: /copilot/courses-portal/production/secrets/JWT_SECRET_KEY
  MONGODB_URI: /copilot/courses-portal/production/secrets/MONGODB_URI
  REDIS_URI: /copilot/courses-portal/production/secrets/REDIS_URI

count:
  range: 2-10
  cpu_percentage: 70
  memory_percentage: 80

healthcheck:
  path: /health
  interval: 30s
  timeout: 5s
```

```bash
# Initialize Copilot with pip Dockerfile
copilot init \
    --app courses-portal \
    --name api \
    --type "Load Balanced Web Service" \
    --dockerfile ./Dockerfile.pip \
    --port 8000

# Deploy
copilot deploy --env prod
```

---

## Troubleshooting Pip Container Builds on AWS

### Issue 1: Build Failures with Native Extensions

**Error:** `Failed to build wheel for some-package`

**Solution:**
```dockerfile
# Install build dependencies for packages with native extensions
FROM python:3.11-slim AS builder

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
```

### Issue 2: Large Image Size for Lambda

**Problem:** Image > 250 MB (Lambda limit)

**Solution:**
```dockerfile
# Use Alpine for smaller images
FROM python:3.11-alpine AS builder
FROM python:3.11-alpine AS runtime

# Install only required packages
RUN apk add --no-cache curl
```

### Issue 3: ECR Authentication Failed

**Error:** `unauthorized: authentication required`

**Solution:**
```bash
# Refresh ECR token
aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin $ECR_URI

# Verify credentials
aws sts get-caller-identity
```

### Issue 4: Secrets Manager Access Denied

**Error:** `AccessDeniedException`

**Solution:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:courses-portal/*"
    }
  ]
}
```

---

## Performance Benchmarking on AWS

| Metric | Pip (Traditional) | Poetry | UV | Pip Advantage |
|--------|------------------|--------|-----|---------------|
| **CodeBuild Time** | 60-90s | 50-95s | 8-20s | Compatible everywhere |
| **Image Size** | 350-500 MB | 350-500 MB | 350-500 MB | Comparable |
| **ECR Storage Cost** | $0.18-0.25/mo | $0.18-0.25/mo | $0.15-0.20/mo | Moderate |
| **Dependency Resolution** | Non-deterministic | Deterministic | Deterministic | Simple |
| **Tooling Required** | Python only | Poetry | UV | Python only |
| **Learning Curve** | Minimal | Moderate | Low | Easiest to learn |

---

## Conclusion: The Enduring Value of Pip on AWS

Pip with requirements.txt remains the most universally accessible approach to Python containerization on AWS. For the AI Powered Video Tutorial Portal, this approach delivers:

- **Universal compatibility** – Works on every Python runtime, every AWS region, every CI/CD platform
- **Simplicity** – One file, no additional tooling
- **Battle-tested** – Millions of deployments on AWS worldwide
- **Easy migration** – Any Python project can use this approach
- **AWS-ready** – Native integration with ECR, ECS, CodeBuild, and Secrets Manager

While modern tools like Poetry and UV offer significant advantages in dependency resolution speed and determinism, pip remains the foundation upon which Python containerization on AWS was built. For teams new to containers, migrating legacy applications, or working in constrained environments, pip is the reliable, battle-tested foundation that just works on AWS.

---

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS *(This story)*

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## What's Next?

Over the coming weeks, each approach in this AWS Python series will be explored in exhaustive detail. We'll examine real-world AWS deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first FastAPI application on AWS Fargate or an enterprise migrating Python workloads to Amazon EKS, you'll find practical guidance tailored to your infrastructure requirements.

Pip represents the foundation of Python containerization on AWS—simple, reliable, and universally compatible. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from classic pip builds to modern UV workflows, and from rapid prototyping to mission-critical production deployments on Amazon EKS.

**Coming next in the series:**
**🚀 AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices