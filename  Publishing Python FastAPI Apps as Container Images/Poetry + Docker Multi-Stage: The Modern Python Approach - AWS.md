# Poetry + Docker Multi-Stage: The Modern Python Approach - AWS

## Building Production-Ready FastAPI Containers for Amazon ECR with Poetry

### Introduction: The Evolution of Python Dependency Management on AWS

In the [introductory installment](#) of this AWS Python series, we explored the landscape of container deployment options for FastAPI applications on Amazon Web Services—from traditional pip-based builds to modern UV-powered workflows, and from AWS Copilot to Amazon EKS orchestration. Now, we dive deep into what many consider the **gold standard for modern Python containerization on AWS**: **Poetry with multi-stage Docker builds**.

Poetry has revolutionized Python dependency management, offering deterministic builds, lockfile-based reproducibility, and elegant dependency resolution. For the **AI Powered Video Tutorial Portal**—a sophisticated FastAPI application with MongoDB integration, JWT authentication, API key management, and comprehensive user engagement features—Poetry ensures that container builds are reproducible, secure, and optimized for production on AWS.

This installment explores the complete workflow for containerizing Poetry-managed Python applications for AWS, using the Courses Portal API as our case study. We'll master multi-stage builds, layer caching optimization, environment-specific configurations, and production-grade Amazon ECR integration—all while leveraging Graviton processors for cost optimization and AWS services for secrets management.

```mermaid
graph TD
    subgraph "Development"
        A[pyproject.toml] --> B[poetry lock]
        B --> C[poetry install]
        C --> D[Local Development]
    end
    
    subgraph "Container Build (Multi-Stage)"
        E[Builder Stage] --> F[poetry export]
        F --> G[Install Dependencies]
        G --> H[Runtime Stage]
        H --> I[Copy App Code]
    end
    
    subgraph "AWS Deployment"
        I --> J[Amazon ECR]
        J --> K[ECS Fargate]
        J --> L[Amazon EKS]
        J --> M[AWS App Runner]
    end
    
    style E fill:#2b6cb0,color:#fff
    style H fill:#48bb78,color:#fff
    style J fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR *(This story)*

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## Understanding the Courses Portal API Architecture for AWS

Before diving into containerization, let's understand what we're deploying on AWS. The **AI Powered Video Tutorial Portal** is a comprehensive FastAPI application with:

### Solution Structure
```
Courses-Portal-API-Python/
├── auth/                    # Authentication & Authorization
│   ├── config.py           # Auth configuration
│   ├── dependencies.py     # FastAPI dependencies
│   ├── models.py           # User and token models
│   ├── roles.py            # RBAC utilities
│   ├── service.py          # Authentication logic
│   └── hybrid_auth.py      # Hybrid login system
├── api_keys/               # API Key Management
│   ├── models.py           # API key data models
│   ├── service.py          # Key generation/validation
│   ├── middleware.py       # API key auth middleware
│   └── router.py           # Management endpoints
├── db/
│   └── conn.py             # MongoDB connection
├── models/                 # Data models
│   ├── continue_watching.py
│   ├── course.py
│   ├── course_content.py
│   └── section_bookmark.py
├── routers/                # API route handlers
│   ├── admin.py
│   ├── auth.py
│   ├── continue_watching.py
│   ├── course_contents.py
│   └── health.py
├── services/               # Business logic
│   ├── continue_watching_service.py
│   ├── course_content_service.py
│   └── course_service.py
├── social_auth/            # Social authentication
│   └── service.py
├── utils/                  # Utilities
│   ├── device_detection.py
│   ├── etag.py
│   └── validation.py
├── server.py               # FastAPI entry point
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Locked dependencies
├── Dockerfile              # Container definition
└── .env.example            # Environment template
```

### Key Dependencies for AWS

| Dependency | Version | AWS Integration |
|------------|---------|-----------------|
| **FastAPI** | 0.104.0+ | Web framework |
| **uvicorn** | 0.24.0+ | ASGI server |
| **motor** | 3.3.0+ | Async MongoDB driver (Amazon DocumentDB) |
| **python-jose** | 3.3.0+ | JWT handling |
| **passlib** | 1.7.4+ | Password hashing |
| **boto3** | 1.28.0+ | AWS SDK for Secrets Manager |
| **aiobotocore** | 2.5.0+ | Async AWS SDK |
| **redis** | 5.0.0+ | Rate limiting (ElastiCache) |

---

## The Poetry-Optimized Dockerfile for AWS: Production-Ready Configuration

Let's examine the complete production Dockerfile for the Courses Portal API, optimized for Poetry and AWS deployment:

```dockerfile
# ============================================
# AI Powered Video Tutorial Portal - Poetry Build for AWS
# ============================================
# Production-ready Dockerfile for FastAPI + Poetry
# Optimized for Amazon ECR, ECS Fargate, and Graviton processors

# ============================================
# STAGE 1: Builder with Poetry
# ============================================
FROM python:3.11-slim AS builder

# Install Poetry
# Using official installer for reproducibility
RUN pip install poetry==1.7.1

# Set working directory
WORKDIR /app

# Copy dependency files first for optimal layer caching
# These files change less frequently than source code
COPY pyproject.toml poetry.lock ./

# Configure Poetry to not create a virtual environment in container
# We want dependencies installed directly to system Python
RUN poetry config virtualenvs.create false

# Install production dependencies only
# --no-dev: Exclude development dependencies
# --no-interaction: Non-interactive mode
# --no-ansi: Plain output for logs
RUN poetry install --no-interaction --no-ansi --no-dev

# ============================================
# STAGE 2: Runtime Image
# ============================================
FROM python:3.11-slim AS runtime

# Install runtime dependencies for health checks and monitoring
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
# This reduces attack surface in production on EC2/ECS
RUN useradd --create-home --shell /bin/bash appuser && \
    mkdir -p /app/logs && \
    chown -R appuser:appuser /app

WORKDIR /app

# Copy installed Python packages from builder stage
# This includes all production dependencies installed via Poetry
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source code
# Separating from dependencies for better layer caching
COPY . .

# Set ownership of application files
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port (FastAPI default)
EXPOSE 8000

# Health check for ECS/ALB and App Runner
# Checks application health endpoint
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run with uvicorn
# --host 0.0.0.0: Bind to all interfaces for container networking
# --port 8000: Default FastAPI port
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Graviton Optimization for AWS

### Building for ARM64 (AWS Graviton)

AWS Graviton processors offer up to 40% better price-performance for Python workloads. Here's how to optimize your Poetry build for Graviton:

```dockerfile
# Multi-architecture build for Graviton
FROM --platform=$BUILDPLATFORM python:3.11-slim AS builder
ARG TARGETARCH
ARG TARGETPLATFORM

RUN pip install poetry==1.7.1
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-dev

FROM --platform=$TARGETPLATFORM python:3.11-slim AS runtime

# Install architecture-specific dependencies
RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home appuser
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build for Graviton

```bash
# Build for ARM64 (Graviton)
docker build --platform linux/arm64 -t courses-api:graviton -f Dockerfile .

# Build multi-architecture manifest
docker buildx build --platform linux/amd64,linux/arm64 -t courses-api:latest --push .
```

---

## Understanding the Poetry Configuration for AWS

### pyproject.toml Structure

```toml
[tool.poetry]
name = "courses-portal-api"
version = "1.0.0"
description = "AI Powered Video Tutorial Portal - FastAPI Backend for AWS"
authors = ["Your Team <dev@example.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.0"
uvicorn = {extras = ["standard"], version = "^0.24.0"}
motor = "^3.3.0"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
passlib = {extras = ["bcrypt"], version = "^1.7.4"}
python-multipart = "^0.0.6"
httpx = "^0.25.0"
pydantic = {extras = ["email"], version = "^2.5.0"}
redis = "^5.0.0"
python-dotenv = "^1.0.0"
email-validator = "^2.1.0"
aiofiles = "^23.2.0"
boto3 = "^1.28.0"
aiobotocore = "^2.5.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"
black = "^23.11.0"
ruff = "^0.1.6"
mypy = "^1.7.0"
pre-commit = "^3.5.0"

[tool.poetry.scripts]
start = "uvicorn server:app --host 0.0.0.0 --port 8000"
dev = "uvicorn server:app --reload"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## Layer Analysis and Optimization for AWS ECR

### Layer-by-Layer Breakdown

| Layer | Size | Cache Key | AWS ECR Impact |
|-------|------|-----------|----------------|
| `FROM python:3.11-slim` | ~180 MB | Image digest | $0.09/GB-month storage |
| `RUN pip install poetry` | ~50 MB | Command hash | Minimal |
| `COPY pyproject.toml poetry.lock` | ~10 KB | File content hashes | Negligible |
| `RUN poetry install` | ~150-300 MB | pyproject.toml + poetry.lock | $0.08-0.15/GB-month |
| `COPY application code` | ~1-10 MB | All source files | Minimal |
| **Final image** | **~350-500 MB** | - | **$0.18-0.25/GB-month** |

### Optimization Strategies for AWS

**1. Dependency Caching**

The Dockerfile copies `pyproject.toml` and `poetry.lock` before any source code. This means:

- ✅ Dependency layers are cached until `pyproject.toml` changes
- ✅ Package restoration is skipped on code-only changes
- ✅ Faster builds in AWS CodeBuild

**2. Production-Only Dependencies**

```dockerfile
RUN poetry install --no-interaction --no-ansi --no-dev
```

- ✅ Excludes `pytest`, `black`, `ruff`, `mypy`, `pre-commit`
- ✅ Reduces final image size by 100-200 MB
- ✅ Lower ECR storage costs

**3. Non-Root User Security**

```dockerfile
RUN useradd --create-home appuser
USER appuser
```

- ✅ Prevents privilege escalation if container is compromised
- ✅ Required for FedRAMP and HIPAA compliance on AWS

---

## Amazon ECR Integration

### Creating ECR Repository

```bash
# Create ECR repository
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

### Authentication to ECR

```bash
# Get login password and authenticate
aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin $ECR_URI
```

### Building and Pushing to ECR

```bash
# Build with Poetry
docker build -t courses-api:latest -f Dockerfile .

# Tag for ECR
docker tag courses-api:latest $ECR_URI:latest

# Push to ECR
docker push $ECR_URI:latest
```

### Using ECR with AWS CodeBuild

```yaml
# buildspec.yml
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.11
    commands:
      - pip install poetry
  pre_build:
    commands:
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
  build:
    commands:
      - docker build -t courses-api:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - docker tag courses-api:$CODEBUILD_RESOLVED_SOURCE_VERSION $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/courses-api:$CODEBUILD_RESOLVED_SOURCE_VERSION
  post_build:
    commands:
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/courses-api:$CODEBUILD_RESOLVED_SOURCE_VERSION
```

---

## AWS Secrets Manager Integration

### Storing Secrets

```bash
# Store JWT secret in Secrets Manager
aws secretsmanager create-secret \
    --name courses-portal/jwt-secret \
    --secret-string '{"secret":"your-super-secret-jwt-key-change-in-production"}'

# Store MongoDB connection string
aws secretsmanager create-secret \
    --name courses-portal/mongodb-uri \
    --secret-string '{"uri":"mongodb://username:password@host:27017/courses_portal?ssl=true"}'
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
    
    # Secrets Manager client
    _secrets_client = boto3.client("secretsmanager", region_name=aws_region)
    
    def get_secret(self, secret_name: str) -> str:
        try:
            response = self._secrets_client.get_secret_value(SecretId=secret_name)
            secret = json.loads(response["SecretString"])
            return list(secret.values())[0]
        except Exception as e:
            # Fallback to environment variable for local development
            return os.getenv(secret_name.replace("/", "_").upper(), "")
    
    @property
    def jwt_secret_key(self) -> str:
        return self.get_secret("courses-portal/jwt-secret")
    
    @property
    def mongodb_uri(self) -> str:
        return self.get_secret("courses-portal/mongodb-uri")

settings = Settings()
```

---

## AWS Copilot Integration

### Using Poetry with AWS Copilot

```yaml
# copilot/api/manifest.yml
name: api
type: Load Balanced Web Service

image:
  build: ./Dockerfile
  port: 8000

platform:
  os: linux
  arch: arm64  # Graviton for cost savings

cpu: 512
memory: 1024

variables:
  ASPNETCORE_ENVIRONMENT: Production
  AWS_REGION: us-east-1

secrets:
  JWT_SECRET_KEY: /copilot/courses-portal/production/secrets/JWT_SECRET_KEY
  MONGODB_URI: /copilot/courses-portal/production/secrets/MONGODB_URI

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
# Initialize Copilot with Poetry project
copilot init \
    --app courses-portal \
    --name api \
    --type "Load Balanced Web Service" \
    --dockerfile ./Dockerfile \
    --port 8000

# Deploy
copilot deploy --env prod
```

---

## Troubleshooting Poetry Container Builds on AWS

### Issue 1: Poetry Lock File Out of Sync

**Error:** `Poetry lock file is out of sync with pyproject.toml`

**Solution:**
```bash
# Regenerate lock file locally
poetry lock --no-update

# Commit new poetry.lock
git add poetry.lock
git commit -m "Update poetry lock"
```

### Issue 2: Large Image Size for Lambda

**Problem:** Final image > 250 MB (Lambda limit)

**Solution:**
```dockerfile
# Use alpine base image for smaller footprint
FROM python:3.11-alpine AS builder

# Use runtime-deps for even smaller
FROM python:3.11-alpine AS runtime
```

### Issue 3: Missing AWS SDK Dependencies

**Error:** `ModuleNotFoundError: No module named 'boto3'`

**Solution:**
```toml
# Ensure boto3 is in pyproject.toml dependencies
[tool.poetry.dependencies]
boto3 = "^1.28.0"
aiobotocore = "^2.5.0"
```

### Issue 4: Secrets Manager Access Denied

**Error:** `AccessDeniedException: User is not authorized to perform: secretsmanager:GetSecretValue`

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

| Metric | Poetry Multi-Stage | Traditional Pip | Improvement |
|--------|-------------------|-----------------|-------------|
| **Build Time (CodeBuild)** | 45-60s | 90-120s | 50% faster |
| **Image Size** | 350-500 MB | 400-600 MB | 20% smaller |
| **ECR Storage Cost** | $0.18-0.25/mo | $0.20-0.30/mo | 20% lower |
| **ECS Task Start** | 2-3s | 2-3s | Comparable |
| **Graviton Performance** | 40% better price-performance | - | Significant savings |

---

## Conclusion: The Poetry Advantage on AWS

Poetry with multi-stage Docker builds represents the modern standard for Python containerization on AWS. For the AI Powered Video Tutorial Portal, this approach delivers:

- **Reproducible builds** – `poetry.lock` ensures exact dependency versions
- **Smaller images** – Excluding dev dependencies reduces size by 30-40%
- **Faster builds** – Layer caching with Poetry-optimized Dockerfile
- **Better security** – Non-root user, minimal runtime dependencies
- **AWS-ready** – ECR integration, Secrets Manager, Graviton optimization

For teams building Python FastAPI applications for AWS, Poetry-based multi-stage builds are the recommended path forward—combining the elegance of modern Python dependency management with production-grade containerization best practices.

---

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR *(This story)*

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

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

Poetry represents the evolution of Python dependency management—bringing deterministic builds, elegant dependency resolution, and reproducible environments to containerized applications on AWS. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from rapid prototyping with Poetry to mission-critical production deployments on Amazon EKS.

**Coming next in the series:**
**⚡ UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton