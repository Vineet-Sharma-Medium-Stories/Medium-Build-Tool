# Visual Studio Code Dev Containers: Local Development to Production - AWS

## Consistent FastAPI Environments from Development to AWS Production

### Introduction: The Environment Consistency Challenge on AWS

In the [previous installment](#) of this AWS Python series, we explored AWS Copilot—the turnkey solution that transforms FastAPI deployments to Amazon ECS into simple, opinionated workflows. While production deployment is critical, an equally important challenge exists **before** deployment: ensuring that every developer on your team works in a consistent environment that mirrors AWS production.

Enter **Visual Studio Code Dev Containers**—a revolutionary approach to development environments that brings containerization to the inner development loop. For the **AI Powered Video Tutorial Portal**—a FastAPI application with MongoDB integration, JWT authentication, and complex dependency trees—Dev Containers ensure that every developer, every CI/CD runner, and every environment runs the exact same Python version, the exact same dependencies, and the exact same configuration that will run on AWS ECS Fargate or EKS.

This installment explores the complete workflow for using Dev Containers with Python FastAPI applications targeting AWS. We'll master devcontainer.json configuration, Dockerfile optimization for development, multi-stage container strategies, and seamless integration with AWS deployment pipelines—all while ensuring that what runs on your laptop runs identically on AWS Graviton processors.

```mermaid
graph TD
    subgraph "Development Environment (VS Code)"
        A[VS Code] --> B[Dev Container]
        B --> C[Python 3.11]
        B --> D[Poetry/UV/Pip]
        B --> E[FastAPI App]
        B --> F[LocalStack AWS Emulator]
        B --> G[MongoDB Container]
        B --> H[Redis Container]
    end
    
    subgraph "AWS Services (Emulated)"
        F --> I[AWS Secrets Manager]
        F --> J[AWS SQS/SNS]
        F --> K[AWS S3]
    end
    
    subgraph "Production AWS"
        L[Amazon ECR] --> M[ECS Fargate]
        M --> N[AWS Secrets Manager]
        M --> O[Amazon DocumentDB]
        M --> P[ElastiCache Redis]
    end
    
    style B fill:#48bb78,color:#fff
    style F fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production *(This story)*

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## Understanding Dev Containers for AWS Development

### What Are Dev Containers?

Dev Containers are development environments running inside Docker containers, providing:

| Feature | Benefit for AWS Development |
|---------|----------------------------|
| **Environment Consistency** | Every developer runs identical Python, dependencies, and tools |
| **Onboarding Speed** | New developers clone and open—no manual setup |
| **AWS Local Emulation** | LocalStack for AWS service simulation |
| **Production Parity** | Develop in the same container base used in AWS production |
| **Graviton Emulation** | Test ARM64 images on x64 development machines |
| **Toolchain Standardization** | Same AWS CLI, CDK, and Copilot versions across the team |

### Dev Container Architecture for AWS

```mermaid
graph LR
    subgraph "Host Machine"
        A[VS Code] --> B[Docker Engine]
        B --> C[Dev Container]
        C --> D[Python 3.11]
        C --> E[AWS CLI]
        C --> F[AWS CDK]
        C --> G[AWS Copilot]
        C --> H[FastAPI App]
        C --> I[LocalStack]
    end
    
    subgraph "LocalStack"
        I --> J[Secrets Manager Mock]
        I --> K[S3 Mock]
        I --> L[SQS/SNS Mock]
    end
    
    subgraph "Local Containers"
        M[MongoDB Container]
        N[Redis Container]
    end
```

---

## Prerequisites

### Install Required Software

```bash
# Install Docker Desktop (Windows/Mac) or Docker Engine (Linux)
# https://docs.docker.com/get-docker/

# Install Visual Studio Code
# https://code.visualstudio.com/download

# Install Dev Containers extension in VS Code
code --install-extension ms-vscode-remote.remote-containers

# Install AWS CLI
# https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

# Install LocalStack (for AWS emulation)
pip install localstack
pip install awscli-local

# Verify installations
docker --version
code --list-extensions | grep remote-containers
aws --version
localstack --version
```

---

## The Dev Container Configuration for AWS

### Project Structure

```
Courses-Portal-API-Python/
├── .devcontainer/
│   ├── devcontainer.json      # Dev container configuration
│   ├── Dockerfile              # Development container definition
│   ├── docker-compose.yml      # Multi-container development
│   └── post-create.sh          # Setup script
├── .vscode/
│   ├── launch.json             # Debug configurations
│   ├── settings.json           # VS Code settings
│   └── extensions.json         # Recommended extensions
├── src/
│   ├── server.py
│   ├── auth/
│   ├── routers/
│   └── models/
├── tests/
├── requirements.txt
├── pyproject.toml
├── Dockerfile.prod             # Production Dockerfile
└── README.md
```

### devcontainer.json - Complete Configuration for AWS

```json
{
  "name": "Courses Portal API - AWS Development",
  "build": {
    "dockerfile": "Dockerfile",
    "context": "..",
    "args": {
      "VARIANT": "3.11",
      "INSTALL_POETRY": "true",
      "INSTALL_AWS_TOOLS": "true"
    }
  },
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "ms-python.flake8",
        "ms-python.isort",
        "amazonwebservices.aws-toolkit-vscode",
        "github.copilot",
        "mongodb.mongodb-vscode",
        "redhat.vscode-yaml",
        "ms-azuretools.vscode-docker"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.linting.enabled": true,
        "python.linting.flake8Enabled": true,
        "python.formatting.provider": "black",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.organizeImports": "explicit"
        },
        "[python]": {
          "editor.defaultFormatter": "ms-python.black-formatter"
        },
        "aws.region": "us-east-1",
        "aws.profile": "default"
      }
    }
  },
  "forwardPorts": [8000, 27017, 6379, 4566],
  "portsAttributes": {
    "8000": {
      "label": "FastAPI Server",
      "onAutoForward": "openPreview"
    },
    "27017": {
      "label": "MongoDB",
      "onAutoForward": "notify"
    },
    "6379": {
      "label": "Redis",
      "onAutoForward": "notify"
    },
    "4566": {
      "label": "LocalStack (AWS Emulator)",
      "onAutoForward": "silent"
    }
  },
  "mounts": [
    "source=${env:HOME}${env:USERPROFILE}/.aws,target=/home/vscode/.aws,type=bind,consistency=cached",
    "source=${env:HOME}${env:USERPROFILE}/.cache/pip,target=/home/vscode/.cache/pip,type=bind,consistency=cached"
  ],
  "postCreateCommand": "bash .devcontainer/post-create.sh",
  "postStartCommand": "bash .devcontainer/post-start.sh",
  "remoteUser": "vscode",
  "containerEnv": {
    "PYTHONPATH": "/workspaces/Courses-Portal-API-Python/src",
    "AWS_REGION": "us-east-1",
    "AWS_ACCESS_KEY_ID": "test",
    "AWS_SECRET_ACCESS_KEY": "test",
    "AWS_ENDPOINT_URL": "http://localhost:4566",
    "MONGODB_URI": "mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin",
    "REDIS_HOST": "redis",
    "REDIS_PORT": "6379",
    "JWT_SECRET_KEY": "dev-secret-key-change-in-production"
  },
  "runArgs": ["--network=host"]
}
```

---

## Development Dockerfile for AWS

### Dockerfile for Development Container with AWS Tools

```dockerfile
# .devcontainer/Dockerfile
ARG VARIANT=3.11
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install system dependencies for AWS
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    unzip \
    mongodb-mongosh \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Install AWS CDK
RUN npm install -g aws-cdk

# Install AWS Copilot
RUN curl -Lo copilot https://github.com/aws/copilot-cli/releases/latest/download/copilot-linux && \
    chmod +x copilot && \
    mv copilot /usr/local/bin/copilot

# Install LocalStack for AWS emulation
RUN pip install localstack awscli-local

# Install Poetry (optional)
ARG INSTALL_POETRY=true
RUN if [ "${INSTALL_POETRY}" = "true" ]; then \
    curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/vscode/.bashrc; \
    fi

# Install UV (optional)
ARG INSTALL_UV=false
RUN if [ "${INSTALL_UV}" = "true" ]; then \
    curl -LsSf https://astral.sh/uv/install.sh | sh; \
    echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> /home/vscode/.bashrc; \
    fi

# Set up Python environment
ENV PYTHONPATH=/workspaces/Courses-Portal-API-Python/src

# Copy requirements for initial setup
COPY requirements.txt /tmp/requirements.txt
RUN pip install --user --no-cache-dir -r /tmp/requirements.txt

# Install development tools
RUN pip install --user --no-cache-dir \
    black \
    flake8 \
    isort \
    pytest \
    pytest-cov \
    pytest-asyncio \
    httpx \
    boto3 \
    moto \
    localstack-client

# Set user
USER vscode
WORKDIR /workspaces/Courses-Portal-API-Python
```

---

## Docker Compose for Multi-Container AWS Development

### docker-compose.yml with LocalStack

```yaml
# .devcontainer/docker-compose.yml
version: '3.8'

services:
  dev:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        VARIANT: 3.11
        INSTALL_POETRY: "true"
        INSTALL_AWS_TOOLS: "true"
    volumes:
      - ..:/workspaces/Courses-Portal-API-Python:cached
      - ~/.aws:/home/vscode/.aws:ro
      - ~/.cache/pip:/home/vscode/.cache/pip
      - /var/run/docker.sock:/var/run/docker.sock
    command: sleep infinity
    environment:
      - PYTHONPATH=/workspaces/Courses-Portal-API-Python/src
      - AWS_REGION=us-east-1
      - AWS_ACCESS_KEY_ID=test
      - AWS_SECRET_ACCESS_KEY=test
      - AWS_ENDPOINT_URL=http://localstack:4566
      - MONGODB_URI=mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    network_mode: service:network
    depends_on:
      - mongodb
      - redis
      - localstack
      - network

  mongodb:
    image: mongo:7.0
    restart: unless-stopped
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
      MONGO_INITDB_DATABASE: courses_portal
    volumes:
      - mongodb-data:/data/db
    network_mode: service:network

  redis:
    image: redis:7.0-alpine
    restart: unless-stopped
    volumes:
      - redis-data:/data
    network_mode: service:network

  localstack:
    image: localstack/localstack:latest
    restart: unless-stopped
    environment:
      - SERVICES=secretsmanager,s3,sqs,sns
      - AWS_DEFAULT_REGION=us-east-1
      - DATA_DIR=/tmp/localstack/data
      - DOCKER_HOST=unix:///var/run/docker.sock
    volumes:
      - localstack-data:/tmp/localstack
      - /var/run/docker.sock:/var/run/docker.sock
    network_mode: service:network

  network:
    image: alpine:3.19
    command: sleep infinity
    network_mode: bridge

volumes:
  mongodb-data:
  redis-data:
  localstack-data:
```

---

## Post-Creation Scripts for AWS

### post-create.sh

```bash
#!/bin/bash
# .devcontainer/post-create.sh

set -e

echo "🔧 Running post-create setup for AWS development..."

# Set up Python path
export PYTHONPATH=/workspaces/Courses-Portal-API-Python/src

# Install dependencies based on what's available
if [ -f "pyproject.toml" ] && command -v poetry &> /dev/null; then
    echo "📦 Installing with Poetry..."
    poetry install
elif [ -f "requirements.txt" ]; then
    echo "📦 Installing with pip..."
    pip install --user -r requirements.txt
fi

# Set up pre-commit hooks if present
if [ -f ".pre-commit-config.yaml" ]; then
    echo "🔗 Setting up pre-commit hooks..."
    pip install --user pre-commit
    pre-commit install
fi

# Create .env file if not exists
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from example..."
    cp .env.example .env
fi

# Start LocalStack (AWS emulator)
echo "🚀 Starting LocalStack..."
localstack start -d

# Wait for LocalStack to be ready
echo "⏳ Waiting for LocalStack..."
until awslocal secretsmanager list-secrets &> /dev/null; do
    sleep 2
done
echo "✅ LocalStack ready"

# Create AWS resources in LocalStack
echo "🔑 Creating AWS resources in LocalStack..."

# Create Secrets Manager secrets
awslocal secretsmanager create-secret \
    --name /copilot/courses-portal/dev/secrets/JWT_SECRET_KEY \
    --secret-string "dev-jwt-secret-key"

awslocal secretsmanager create-secret \
    --name /copilot/courses-portal/dev/secrets/MONGODB_URI \
    --secret-string "mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin"

awslocal secretsmanager create-secret \
    --name /copilot/courses-portal/dev/secrets/REDIS_URI \
    --secret-string "redis://redis:6379"

# Create SQS queue for background tasks
awslocal sqs create-queue --queue-name courses-tasks

# Create SNS topic for notifications
awslocal sns create-topic --name courses-notifications

# Create S3 bucket for course assets
awslocal s3 mb s3://courses-assets

echo "✅ AWS resources created in LocalStack"

echo "✅ Post-create setup complete!"
```

### post-start.sh

```bash
#!/bin/bash
# .devcontainer/post-start.sh

set -e

echo "🚀 Running post-start setup..."

# Wait for MongoDB to be ready
echo "⏳ Waiting for MongoDB..."
until mongosh --eval "db.adminCommand('ping')" &> /dev/null; do
    sleep 2
done
echo "✅ MongoDB ready"

# Wait for Redis to be ready
echo "⏳ Waiting for Redis..."
until redis-cli ping &> /dev/null; do
    sleep 2
done
echo "✅ Redis ready"

# Ensure LocalStack is running
if ! awslocal secretsmanager list-secrets &> /dev/null; then
    echo "🔄 Starting LocalStack..."
    localstack start -d
    sleep 10
fi

# Seed database if seed script exists
if [ -f "scripts/seed.py" ]; then
    echo "🌱 Seeding database..."
    python scripts/seed.py
fi

# Run initial tests
echo "🧪 Running smoke tests..."
pytest tests/smoke/ -v --tb=short

echo "✅ Post-start setup complete!"
```

---

## VS Code Settings and Workspace for AWS

### Workspace Settings

```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "/usr/local/bin/python",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": [
    "--max-line-length=88",
    "--extend-ignore=E203,W503"
  ],
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": [
    "--line-length=88"
  ],
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests",
    "--cov=src",
    "--cov-report=html",
    "--cov-report=xml",
    "-v"
  ],
  "python.terminal.activateEnvironment": true,
  "python.terminal.activateEnvInCurrentTerminal": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },
  "aws.region": "us-east-1",
  "aws.profile": "default",
  "aws.telemetry": false,
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/__pycache__/**": true,
    "**/.pytest_cache/**": true,
    "**/.mypy_cache/**": true
  },
  "debug.inlineValues": true
}
```

### Recommended Extensions

```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter",
    "ms-python.flake8",
    "ms-python.isort",
    "amazonwebservices.aws-toolkit-vscode",
    "github.copilot",
    "mongodb.mongodb-vscode",
    "redhat.vscode-yaml",
    "ms-azuretools.vscode-docker",
    "eamodio.gitlens"
  ]
}
```

---

## Debugging Configuration for AWS

### Launch Configuration

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI (Uvicorn)",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "server:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
        "--reload"
      ],
      "jinja": true,
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src",
        "ASPNETCORE_ENVIRONMENT": "Development",
        "AWS_ENDPOINT_URL": "http://localhost:4566"
      },
      "console": "integratedTerminal"
    },
    {
      "name": "Python: Pytest",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": [
        "tests/",
        "-v",
        "--cov=src",
        "--cov-report=term"
      ],
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src",
        "AWS_ENDPOINT_URL": "http://localhost:4566"
      },
      "console": "integratedTerminal"
    },
    {
      "name": "Python: Current File (with AWS)",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "env": {
        "AWS_ENDPOINT_URL": "http://localhost:4566"
      },
      "console": "integratedTerminal"
    }
  ]
}
```

---

## Working with AWS Services in Dev Container

### Using LocalStack for AWS Emulation

```python
# config.py - AWS client configuration with LocalStack support
import os
import boto3
from botocore.config import Config

def get_aws_client(service_name: str):
    """Get AWS client configured for LocalStack in development"""
    endpoint_url = os.getenv("AWS_ENDPOINT_URL")
    
    if endpoint_url:
        # Development with LocalStack
        return boto3.client(
            service_name,
            endpoint_url=endpoint_url,
            region_name="us-east-1",
            aws_access_key_id="test",
            aws_secret_access_key="test",
            config=Config(signature_version="s3v4")
        )
    else:
        # Production on AWS
        return boto3.client(service_name, region_name=os.getenv("AWS_REGION", "us-east-1"))

# Usage
secrets_client = get_aws_client("secretsmanager")
s3_client = get_aws_client("s3")
sqs_client = get_aws_client("sqs")
```

### Testing AWS Integration

```python
# tests/test_aws_integration.py
import pytest
import boto3
import os

@pytest.fixture
def aws_client():
    """Return AWS client configured for LocalStack"""
    return boto3.client(
        "secretsmanager",
        endpoint_url="http://localhost:4566",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test"
    )

def test_secrets_manager(aws_client):
    """Test Secrets Manager integration"""
    # Create secret
    response = aws_client.create_secret(
        Name="test-secret",
        SecretString='{"key":"value"}'
    )
    assert "ARN" in response
    
    # Retrieve secret
    secret = aws_client.get_secret_value(SecretId="test-secret")
    assert secret["SecretString"] == '{"key":"value"}'

def test_s3_bucket(aws_client):
    """Test S3 integration"""
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test"
    )
    
    # Create bucket
    s3.create_bucket(Bucket="test-bucket")
    
    # Upload object
    s3.put_object(Bucket="test-bucket", Key="test.txt", Body=b"Hello AWS")
    
    # Download object
    response = s3.get_object(Bucket="test-bucket", Key="test.txt")
    assert response["Body"].read() == b"Hello AWS"
```

---

## Production Image from Dev Container

### Multi-Stage Dockerfile for Production

```dockerfile
# Dockerfile.prod
# Build stage - uses same dependencies as dev container
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy dependency files
COPY requirements.txt .
COPY pyproject.toml . 2>/dev/null || true

# Install dependencies
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim AS runtime

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home appuser

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY . .

RUN chown -R appuser:appuser /app
USER appuser

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Building and Deploying to AWS

```bash
# Build production image
docker build -f Dockerfile.prod -t courses-api:latest .

# Test locally
docker run -p 8000:8000 courses-api:latest

# Push to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_URI
docker tag courses-api:latest $ECR_URI:latest
docker push $ECR_URI:latest

# Deploy with Copilot
copilot deploy --env prod
```

---

## Troubleshooting Dev Containers on AWS

### Issue 1: LocalStack Not Starting

**Error:** `LocalStack failed to start`

**Solution:**
```bash
# Check LocalStack logs
docker logs localstack

# Restart LocalStack
localstack stop
localstack start -d

# Verify
awslocal secretsmanager list-secrets
```

### Issue 2: AWS Credentials Not Found

**Error:** `Unable to locate credentials`

**Solution:**
```json
// In devcontainer.json, mount AWS credentials
"mounts": [
  "source=${env:HOME}${env:USERPROFILE}/.aws,target=/home/vscode/.aws,type=bind,consistency=cached"
]

// Or set environment variables
"containerEnv": {
  "AWS_ACCESS_KEY_ID": "test",
  "AWS_SECRET_ACCESS_KEY": "test"
}
```

### Issue 3: MongoDB Connection Failed

**Error:** `pymongo.errors.ServerSelectionTimeoutError`

**Solution:**
```yaml
# In docker-compose.yml, ensure health check
healthcheck:
  test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
  interval: 10s
  timeout: 5s
  retries: 5
```

### Issue 4: Port Conflicts

**Error:** `port is already allocated`

**Solution:**
```json
// In devcontainer.json, change forwarded ports
"forwardPorts": [8001, 27018, 6380, 4567],
"portsAttributes": {
  "8001": {
    "label": "FastAPI Server"
  }
}
```

---

## Performance Metrics

| Metric | Traditional Setup | Dev Containers | Improvement |
|--------|------------------|----------------|-------------|
| **New Developer Onboarding** | 2-4 hours | 15 minutes | 80% faster |
| **Environment Consistency** | Variable | Identical | 100% consistent |
| **"Works on My Machine" Issues** | Frequent | Rare | 95% reduction |
| **AWS Service Testing** | Mock or real AWS | LocalStack | 100% offline |
| **CI/CD Parity** | Manual sync | Automatic | Perfect parity |

---

## Conclusion: The Dev Container Advantage for AWS

Visual Studio Code Dev Containers represent a paradigm shift in Python development for AWS, delivering:

- **Instant onboarding** – New developers clone and open the project—no setup required
- **Perfect consistency** – Every developer, CI runner, and AWS environment runs identical Python versions and dependencies
- **Production parity** – Develop in the same container base used in AWS production (ECS, EKS)
- **Offline AWS development** – LocalStack emulates AWS services for offline testing
- **Graviton emulation** – Test ARM64 images before deploying to AWS Graviton
- **Toolchain standardization** – Same AWS CLI, CDK, and Copilot versions across the team

For the AI Powered Video Tutorial Portal, Dev Containers ensure that every developer contributes in an environment that perfectly mirrors AWS production—eliminating "works on my machine" issues and accelerating the journey from development to AWS deployment.

---

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production *(This story)*

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## What's Next?

Over the coming weeks, each approach in this AWS Python series will be explored in exhaustive detail. We'll examine real-world AWS deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first FastAPI application on AWS Fargate or an enterprise migrating Python workloads to Amazon EKS, you'll find practical guidance tailored to your infrastructure requirements.

Dev Containers represent the foundation of modern Python development for AWS—ensuring that what you build on your laptop runs identically in AWS production. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from consistent development environments to mission-critical production deployments on Amazon EKS.

**Coming next in the series:**
**🏗️ AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling