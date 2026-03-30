# Visual Studio Code Dev Containers: Local Development to Production

## Consistent Python Environments from Development to Azure

### Introduction: The Environment Consistency Challenge

In the [previous installment](#) of this Python series, we explored Azure Container Apps—the serverless platform that transforms how we deploy FastAPI applications at scale. While production deployment is critical, an equally important challenge exists **before** deployment: ensuring that every developer on your team works in a consistent environment that mirrors production.

Enter **Visual Studio Code Dev Containers**—a revolutionary approach to development environments that brings containerization to the inner development loop. For the **AI Powered Video Tutorial Portal**—a FastAPI application with MongoDB integration, JWT authentication, and complex dependency trees—Dev Containers ensure that every developer, every CI/CD runner, and every environment runs the exact same Python version, the exact same dependencies, and the exact same configuration.

This installment explores the complete workflow for using Dev Containers with Python FastAPI applications, from initial setup to production parity. We'll master devcontainer.json configuration, Dockerfile optimization for development, multi-stage container strategies, and seamless integration with Azure deployment pipelines—all while ensuring that what runs on your laptop runs identically in production.

```mermaid
graph TD
    subgraph "Development Environment"
        A[VS Code] --> B[Dev Container]
        B --> C[Python 3.11]
        B --> D[Poetry/UV/Pip]
        B --> E[Application Code]
        B --> F[MongoDB Container]
        B --> G[Redis Container]
    end
    
    subgraph "Build Pipeline"
        H[Same Container] --> I[Docker Build]
        I --> J[Production Image]
    end
    
    subgraph "Azure Production"
        J --> K[Azure Container Registry]
        K --> L[Azure Container Apps]
        K --> M[Azure Kubernetes Service]
    end
    
    style B fill:#48bb78,color:#fff
    style H fill:#2b6cb0,color:#fff
    style K fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds

- 📦 **3. Pip + Docker: The Classic Python Containerization** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization

- 🚀 **4. Azure Container Apps: Serverless Python Deployment** – Deploying FastAPI applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent development environments and seamless deployment *(This story)*

- 🔧 **6. Azure Developer CLI (azd) with Python: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Python Microservices at Scale** – Deploying FastAPI applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Python** – Automated container builds, testing, and deployment with GitHub Actions workflows

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Python Container Deployments** – Deploying Python FastAPI applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## Understanding Dev Containers

### What Are Dev Containers?

Dev Containers are development environments running inside Docker containers, providing:

| Feature | Benefit |
|---------|---------|
| **Environment Consistency** | Every developer runs identical Python, dependencies, and tools |
| **Onboarding Speed** | New developers clone and open—no manual setup |
| **Dependency Isolation** | No conflicts with local Python installations |
| **Production Parity** | Develop in the same container base used in production |
| **Reproducible Builds** | Same environment for local dev, CI, and staging |
| **Toolchain Management** | Specific versions of linters, formatters, and test tools |

### Dev Container Architecture

```mermaid
graph LR
    subgraph "Host Machine"
        A[VS Code] --> B[Docker Engine]
        B --> C[Dev Container]
        C --> D[Python 3.11]
        C --> E[VS Code Server]
        C --> F[Extensions]
        C --> G[Application Code]
        C --> H[MongoDB Container]
        C --> I[Redis Container]
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

# Verify Docker is running
docker --version
# Docker version 24.0.7

# Verify Dev Container extension
code --list-extensions | grep remote-containers
# ms-vscode-remote.remote-containers
```

---

## The Dev Container Configuration

### Project Structure

```
Courses-Portal-API-Python/
├── .devcontainer/
│   ├── devcontainer.json      # Dev container configuration
│   ├── Dockerfile              # Development container definition
│   ├── docker-compose.yml      # Multi-container development
│   └── library-scripts/        # Optional setup scripts
├── src/
│   ├── server.py
│   ├── auth/
│   ├── routers/
│   └── models/
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

### devcontainer.json - Complete Configuration

```json
{
  "name": "Courses Portal API - Python",
  "build": {
    "dockerfile": "Dockerfile",
    "context": "..",
    "args": {
      "VARIANT": "3.11",
      "INSTALL_POETRY": "true",
      "INSTALL_UV": "false"
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
        "ms-toolsai.jupyter",
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
        "python.formatting.blackPath": "/usr/local/bin/black",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.organizeImports": "explicit"
        },
        "[python]": {
          "editor.defaultFormatter": "ms-python.black-formatter"
        }
      }
    }
  },
  "forwardPorts": [8000, 27017, 6379],
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
    }
  },
  "mounts": [
    "source=${env:HOME}${env:USERPROFILE}/.azure,target=/home/vscode/.azure,type=bind,consistency=cached",
    "source=${env:HOME}${env:USERPROFILE}/.cache/pip,target=/home/vscode/.cache/pip,type=bind,consistency=cached"
  ],
  "postCreateCommand": "bash .devcontainer/post-create.sh",
  "postStartCommand": "bash .devcontainer/post-start.sh",
  "remoteUser": "vscode",
  "containerEnv": {
    "PYTHONPATH": "/workspaces/Courses-Portal-API-Python/src",
    "MONGODB_URI": "mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin",
    "REDIS_HOST": "redis",
    "REDIS_PORT": "6379",
    "JWT_SECRET_KEY": "dev-secret-key-change-in-production"
  },
  "runArgs": ["--network=host"]
}
```

---

## Development Dockerfile

### Dockerfile for Development Container

```dockerfile
# .devcontainer/Dockerfile
ARG VARIANT=3.11
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    mongodb-mongosh \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

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

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

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
    httpx

# Set user
USER vscode
WORKDIR /workspaces/Courses-Portal-API-Python
```

---

## Docker Compose for Multi-Container Development

### docker-compose.yml for Dev Container

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
        INSTALL_UV: "false"
    volumes:
      - ..:/workspaces/Courses-Portal-API-Python:cached
      - ~/.azure:/home/vscode/.azure:ro
      - ~/.cache/pip:/home/vscode/.cache/pip
      - /var/run/docker.sock:/var/run/docker.sock
    command: sleep infinity
    environment:
      - PYTHONPATH=/workspaces/Courses-Portal-API-Python/src
      - MONGODB_URI=mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    network_mode: service:network
    depends_on:
      - mongodb
      - redis
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

  network:
    image: alpine:3.19
    command: sleep infinity
    network_mode: bridge

volumes:
  mongodb-data:
  redis-data:
```

---

## Post-Creation Scripts

### post-create.sh

```bash
#!/bin/bash
# .devcontainer/post-create.sh

set -e

echo "🔧 Running post-create setup..."

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

# Seed database if seed script exists
if [ -f "scripts/seed.py" ]; then
    echo "🌱 Seeding database..."
    python scripts/seed.py
fi

echo "✅ Post-start setup complete!"
```

---

## VS Code Settings and Workspace

### Recommended Workspace Settings

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
    "--cov-report=xml"
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
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/__pycache__/**": true,
    "**/.pytest_cache/**": true,
    "**/.mypy_cache/**": true
  },
  "debug.inlineValues": true,
  "debug.onTaskErrors": "showErrors"
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
    "ms-toolsai.jupyter",
    "github.copilot",
    "mongodb.mongodb-vscode",
    "redhat.vscode-yaml",
    "ms-azuretools.vscode-docker",
    "ms-azuretools.vscode-azurecontainerapps",
    "eamodio.gitlens"
  ]
}
```

---

## Debugging Configuration

### Launch Configuration for FastAPI

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
        "ASPNETCORE_ENVIRONMENT": "Development"
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
        "--cov=src",
        "--cov-report=term"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    }
  ]
}
```

---

## Development Workflow

### Opening the Project in Dev Container

```bash
# Clone the repository
git clone https://gitlab.com/mvineetsharma/ai-powered-video-tutorial-portal/Courses-Portal-API-Python.git
cd Courses-Portal-API-Python

# Open in VS Code
code .

# When prompted, click "Reopen in Container"
# Or use command palette: Ctrl+Shift+P -> "Dev Containers: Reopen in Container"
```

### Common Development Commands

```bash
# Inside dev container, run the application
uvicorn server:app --host 0.0.0.0 --port 8000 --reload

# Run tests
pytest tests/ -v --cov=src

# Run linter
flake8 src/ tests/

# Run formatter
black src/ tests/

# Import sorting
isort src/ tests/

# Type checking
mypy src/

# Database seeding
python scripts/seed.py

# Run in debug mode (from VS Code)
# Press F5 with "Python: FastAPI (Uvicorn)" configuration
```

---

## Production Image from Dev Container

### Multi-Stage Dockerfile for Production

```dockerfile
# Dockerfile.prod
# Build stage - uses same dependencies as dev container
FROM mcr.microsoft.com/devcontainers/python:3.11 AS builder

WORKDIR /app

# Copy dependency files
COPY requirements.txt .
COPY pyproject.toml . 2>/dev/null || true
COPY poetry.lock . 2>/dev/null || true

# Install dependencies (using pip for production)
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

# Set ownership
RUN chown -R appuser:appuser /app
USER appuser

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Building Production Image

```bash
# Build from within dev container
docker build -f Dockerfile.prod -t coursetutorials.azurecr.io/courses-api:latest .

# Push to ACR
az acr login --name coursetutorials
docker push coursetutorials.azurecr.io/courses-api:latest
```

---

## Azure Integration from Dev Container

### Azure CLI in Dev Container

```bash
# Login to Azure
az login

# Verify subscription
az account show

# Deploy to Container Apps
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --image coursetutorials.azurecr.io/courses-api:latest
```

### Service Principal for CI/CD

```bash
# Create service principal for deployment
az ad sp create-for-rbac \
    --name courses-api-deployer \
    --role contributor \
    --scopes /subscriptions/$(az account show --query id -o tsv)/resourceGroups/rg-courses-portal \
    --sdk-auth > azure-credentials.json
```

---

## Troubleshooting Dev Containers

### Issue 1: Docker Not Running

**Error:** `Cannot connect to the Docker daemon`

**Solution:**
```bash
# Start Docker Desktop
# On macOS/Linux
sudo systemctl start docker

# Verify
docker ps
```

### Issue 2: Permission Denied on Mounts

**Error:** `Permission denied` on mounted volumes

**Solution:**
```json
// In devcontainer.json
"mounts": [
  "source=${env:HOME}${env:USERPROFILE}/.azure,target=/home/vscode/.azure,type=bind,consistency=cached,readonly"
]
```

### Issue 3: Slow Container Build

**Problem:** Dev container rebuild takes 5+ minutes

**Solution:**
- Use `--mount=type=cache` for pip/poetry
- Pre-build dev container image
- Use Docker layer caching in CI

### Issue 4: MongoDB Connection Failed

**Error:** `pymongo.errors.ServerSelectionTimeoutError`

**Solution:**
```yaml
# In docker-compose.yml, ensure MongoDB health check
healthcheck:
  test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
  interval: 10s
  timeout: 5s
  retries: 5
```

---

## Performance Metrics

| Metric | Traditional Setup | Dev Containers | Improvement |
|--------|------------------|----------------|-------------|
| **New Developer Onboarding** | 2-4 hours | 15 minutes | 80% faster |
| **Environment Consistency** | Variable | Identical | 100% consistent |
| **"Works on My Machine" Issues** | Frequent | Rare | 95% reduction |
| **CI/CD Parity** | Manual sync | Automatic | Perfect parity |
| **Python Version Conflicts** | Common | Never | Eliminated |
| **Dependency Conflicts** | Common | Never | Eliminated |

---

## Conclusion: The Dev Container Advantage

Visual Studio Code Dev Containers represent a paradigm shift in Python development, delivering:

- **Instant onboarding** – New developers clone and open the project—no setup required
- **Perfect consistency** – Every developer, CI runner, and staging environment runs identical Python versions and dependencies
- **Production parity** – Develop in the same container base used in Azure production
- **Isolated dependencies** – No conflicts with system Python or other projects
- **Toolchain standardization** – Same linters, formatters, and test runners across the team

For the AI Powered Video Tutorial Portal, Dev Containers ensure that every developer contributes in an environment that perfectly mirrors production—eliminating "works on my machine" issues and accelerating the journey from development to Azure deployment.

---

### Stories at a Glance

**Complete Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds

- 📦 **3. Pip + Docker: The Classic Python Containerization** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization

- 🚀 **4. Azure Container Apps: Serverless Python Deployment** – Deploying FastAPI applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent development environments and seamless deployment *(This story)*

- 🔧 **6. Azure Developer CLI (azd) with Python: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Python Microservices at Scale** – Deploying FastAPI applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Python** – Automated container builds, testing, and deployment with GitHub Actions workflows

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Python Container Deployments** – Deploying Python FastAPI applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## What's Next?

Over the coming weeks, each approach in this Python series will be explored in exhaustive detail. We'll examine real-world Azure deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first FastAPI application or an enterprise migrating Python workloads to Azure Kubernetes Service, you'll find practical guidance tailored to your infrastructure requirements.

Dev Containers represent the foundation of modern Python development—ensuring that what you build on your laptop runs identically in production. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from consistent development environments to mission-critical production deployments on Azure Kubernetes Service.

**Coming next in the series:**
**🔧 Azure Developer CLI (azd) with Python: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep