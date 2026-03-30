# Pip + Docker: The Classic Python Containerization

## Battle-Tested Requirements.txt Approach for FastAPI on Azure

### Introduction: The Foundation of Python Containerization

In the [previous installments](#) of this Python series, we explored modern approaches to Python containerization—Poetry with multi-stage builds for deterministic dependency management, and UV for blazing-fast package installation. While these modern tools offer significant advantages, the **traditional pip + requirements.txt** approach remains the most widely used, battle-tested, and universally compatible method for containerizing Python applications.

For the **AI Powered Video Tutorial Portal**—a FastAPI application with MongoDB integration, JWT authentication, and comprehensive user engagement features—the pip approach offers unparalleled simplicity and compatibility. It works on every Python runtime, every container registry, and every CI/CD platform without requiring additional tooling. For teams new to containerization, migrating legacy applications, or working in environments with strict tooling requirements, pip is the reliable foundation upon which Python containerization was built.

This installment explores the complete workflow for containerizing pip-managed Python applications for Azure, using the Courses Portal API as our case study. We'll master multi-stage builds, layer caching optimization, requirements.txt best practices, and production-grade Azure Container Registry integration—all with the simplicity and ubiquity of the classic pip approach.

```mermaid
graph TD
    subgraph "Traditional Python Workflow"
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
    
    subgraph "Azure Deployment"
        J --> K[Azure Container Registry]
        K --> L[Azure Container Apps]
        K --> M[Azure Kubernetes Service]
        K --> N[Azure App Service]
    end
    
    style F fill:#48bb78,color:#fff
    style G fill:#2b6cb0,color:#fff
    style K fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds

- 📦 **3. Pip + Docker: The Classic Python Containerization** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization *(This story)*

- 🚀 **4. Azure Container Apps: Serverless Python Deployment** – Deploying FastAPI applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent development environments and seamless deployment

- 🔧 **6. Azure Developer CLI (azd) with Python: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Python Microservices at Scale** – Deploying FastAPI applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Python** – Automated container builds, testing, and deployment with GitHub Actions workflows

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Python Container Deployments** – Deploying Python FastAPI applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## Understanding requirements.txt: The Classic Approach

### Why Pip Remains Essential

| Aspect | Pip + requirements.txt | Modern Tools (Poetry/UV) |
|--------|------------------------|-------------------------|
| **Ubiquity** | Every Python installation includes pip | Requires additional installation |
| **Simplicity** | Single file, no configuration | Lock files, configuration files |
| **Compatibility** | Works everywhere | May require specific versions |
| **CI/CD Integration** | Native to all platforms | May need setup steps |
| **Learning Curve** | Minimal | Moderate |
| **Deterministic Builds** | Requires pip freeze | Built-in lock files |

### The requirements.txt Format

```txt
# requirements.txt for AI Powered Video Tutorial Portal
# Production dependencies only

# Core Framework
fastapi==0.104.0
uvicorn[standard]==0.24.0
pydantic[email]==2.5.0

# Database
motor==3.3.0
pymongo==4.5.0

# Authentication
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# HTTP Client
httpx==0.25.0

# Caching & Rate Limiting
redis==5.0.0

# Utilities
python-dotenv==1.0.0
aiofiles==23.2.0
email-validator==2.1.0

# Monitoring
prometheus-client==0.19.0
```

### Generating requirements.txt

```bash
# From active virtual environment
pip freeze > requirements.txt

# From Poetry project
poetry export -f requirements.txt --output requirements.txt --without-hashes

# From UV project
uv pip freeze > requirements.txt
```

---

## The Pip-Optimized Dockerfile: Production-Ready Configuration

Let's examine the complete production Dockerfile for the Courses Portal API, optimized for pip and Azure deployment:

```dockerfile
# ============================================
# AI Powered Video Tutorial Portal - Pip Build
# ============================================
# Production-ready Dockerfile for FastAPI + pip
# Traditional multi-stage build with layer caching optimization

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

# Install runtime dependencies for health checks and monitoring
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
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

# Health check for Azure Container Apps
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run with uvicorn
# Using exec form for proper signal handling
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Layer Analysis and Optimization with Pip

### Layer-by-Layer Breakdown

| Layer | Size | Cache Key | Invalidation |
|-------|------|-----------|--------------|
| `FROM python:3.11-slim` | ~180 MB | Image digest | Rare (base image updates) |
| `COPY requirements.txt` | ~1 KB | File content hash | When requirements change |
| `RUN pip install --user` | ~150-300 MB | requirements.txt | When dependencies change |
| `RUN apt-get install curl` | ~20 MB | Package list | Rare |
| `RUN useradd` | ~1 MB | Command hash | Never |
| `COPY application code` | ~1-10 MB | All source files | Every code change |
| **Final image** | **~350-500 MB** | - | - |

### Optimization Strategies

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
```

**3. Use `--no-deps` for Multi-Stage with Pre-built Wheels**

```dockerfile
# For advanced scenarios with pre-built dependencies
COPY wheels/ /wheels/
RUN pip install --user --no-cache-dir --no-deps /wheels/*.whl
```

**4. Separate Production and Development Dependencies**

```dockerfile
# Production only
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Development (optional, for testing stage)
FROM builder AS dev
COPY requirements-dev.txt .
RUN pip install --user --no-cache-dir -r requirements-dev.txt
```

---

## Advanced Pip Patterns for Production

### Using Pip with `--require-hashes` for Supply Chain Security

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

### Multi-Stage Build with Testing Stage

```dockerfile
# ============================================
# Builder Stage (Common)
# ============================================
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ============================================
# Test Stage
# ============================================
FROM builder AS test
COPY requirements-dev.txt .
RUN pip install --user --no-cache-dir -r requirements-dev.txt
COPY . .
RUN pytest tests/ --cov=./

# ============================================
# Runtime Stage
# ============================================
FROM python:3.11-slim AS runtime
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Using Alpine for Smaller Images

```dockerfile
# Alpine-based build (smaller but potentially slower builds)
FROM python:3.11-alpine AS builder

# Install build dependencies for packages with native extensions
RUN apk add --no-cache gcc musl-dev python3-dev

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-alpine AS runtime
RUN apk add --no-cache curl
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Docker Compose for Local Development with Pip

```yaml
# docker-compose.yml
version: '3.8'

services:
  mongodb:
    image: mongo:7.0
    container_name: courses-mongodb
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
      MONGO_INITDB_DATABASE: courses_portal
    volumes:
      - mongodb_data:/data/db
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7.0-alpine
    container_name: courses-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: runtime
    container_name: courses-api
    ports:
      - "8000:8000"
    environment:
      MONGODB_URI: mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin
      REDIS_HOST: redis
      REDIS_PORT: 6379
      JWT_SECRET_KEY: dev-secret-key-change-in-production
      API_KEY_ENABLED: "true"
    depends_on:
      mongodb:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./logs:/app/logs
      - ./:/app:ro  # Mount code for development (optional)
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Optional: Development service with hot reload
  api-dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    container_name: courses-api-dev
    ports:
      - "8001:8000"
    environment:
      MONGODB_URI: mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin
      REDIS_HOST: redis
      REDIS_PORT: 6379
      JWT_SECRET_KEY: dev-secret-key
    depends_on:
      - mongodb
      - redis
    volumes:
      - ./:/app
    command: uvicorn server:app --host 0.0.0.0 --port 8000 --reload

volumes:
  mongodb_data:
  redis_data:
```

### Development Dockerfile with Hot Reload

```dockerfile
# Dockerfile.dev
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Install development dependencies
RUN pip install --user --no-cache-dir watchdog

# Copy source
COPY . .

ENV PATH=/root/.local/bin:$PATH

# Run with auto-reload
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

---

## CI/CD with GitHub Actions and Pip

```yaml
# .github/workflows/pip-build.yml
name: Pip Docker Build and Deploy

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  ACR_NAME: coursetutorials
  IMAGE_NAME: courses-api
  PYTHON_VERSION: "3.11"

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ env.PYTHON_VERSION }}
    
    - name: Cache pip packages
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
    
    - name: Install dependencies
      run: pip install -r requirements.txt
    
    - name: Run tests
      run: pytest tests/ --cov=./

  build-and-push:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Login to Azure
      uses: azure/login@v1
      with:
        client-id: ${{ secrets.AZURE_CLIENT_ID }}
        tenant-id: ${{ secrets.AZURE_TENANT_ID }}
        subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
    
    - name: Login to ACR
      run: az acr login --name ${{ env.ACR_NAME }}
    
    - name: Build and push with pip
      run: |
        docker build \
          --cache-from ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:latest \
          -t ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }} \
          -t ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:latest \
          .
        docker push ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
        docker push ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:latest
    
    - name: Deploy to Azure Container Apps
      run: |
        az containerapp update \
          --name courses-api \
          --resource-group rg-courses \
          --image ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

---

## Azure DevOps Pipeline with Pip

```yaml
# azure-pipelines.yml
trigger:
- main

variables:
  acrName: 'coursetutorials'
  imageName: 'courses-api'
  pythonVersion: '3.11'

stages:
- stage: Build
  displayName: 'Build and Test'
  jobs:
  - job: Build
    pool:
      vmImage: 'ubuntu-latest'
    steps:
    - task: UsePythonVersion@0
      inputs:
        versionSpec: '$(pythonVersion)'
    
    - task: Cache@2
      inputs:
        key: 'pip | "$(Agent.OS)" | requirements.txt'
        path: $(Pipeline.Workspace)/.cache/pip
        cacheHitVar: PIP_CACHE_RESTORED
    
    - script: |
        pip install -r requirements.txt
        pytest tests/ --junitxml=test-results.xml
      displayName: 'Install and test'
    
    - task: PublishTestResults@2
      inputs:
        testResultsFiles: 'test-results.xml'
        testRunTitle: 'Python Tests'
    
    - task: Docker@2
      displayName: 'Build and push'
      inputs:
        containerRegistry: 'acr-service-connection'
        repository: '$(imageName)'
        command: 'buildAndPush'
        Dockerfile: '**/Dockerfile'
        tags: |
          $(Build.BuildId)
          latest

- stage: Deploy
  displayName: 'Deploy to ACA'
  dependsOn: Build
  jobs:
  - deployment: Deploy
    environment: 'production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureCLI@2
            displayName: 'Update Container App'
            inputs:
              azureSubscription: 'azure-service-connection'
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                az containerapp update \
                  --name courses-api \
                  --resource-group rg-courses \
                  --image $(acrName).azurecr.io/$(imageName):$(Build.BuildId)
```

---

## Security Best Practices with Pip

### Dependency Scanning with Safety

```dockerfile
# Add security scanning to Dockerfile
FROM python:3.11-slim AS security

COPY requirements.txt .
RUN pip install safety
RUN safety check -r requirements.txt --full-report
```

### Using `pip-audit` for Vulnerability Scanning

```bash
# In CI pipeline
pip install pip-audit
pip-audit -r requirements.txt --desc

# In Dockerfile (optional)
RUN pip install pip-audit && pip-audit -r requirements.txt
```

### Never Embed Secrets in Dockerfile

```dockerfile
# BAD - Secret in image layer
ENV DB_PASSWORD=supersecret

# GOOD - Pass at runtime
ENV DB_PASSWORD=
```

```bash
# Pass secrets at runtime
docker run -e DB_PASSWORD=$DB_PASSWORD courses-api:latest

# Or use Azure Key Vault in production
```

---

## Troubleshooting Pip Container Builds

### Issue 1: Build Failures with Native Extensions

**Error:** `Failed to build wheel for some-package`

**Solution:**
```dockerfile
# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Then install Python packages
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
```

### Issue 2: Large Image Size

**Problem:** Image > 800 MB

**Solution:**
```dockerfile
# Use --no-cache-dir
RUN pip install --user --no-cache-dir -r requirements.txt

# Use alpine base (smaller but slower)
FROM python:3.11-alpine

# Clean apt cache
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*
```

### Issue 3: Slow Build Times

**Problem:** Every build reinstalls dependencies

**Solution:**
```dockerfile
# Ensure requirements.txt is copied before code
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .
```

### Issue 4: Missing Dependencies at Runtime

**Error:** `ModuleNotFoundError: No module named 'some_package'`

**Solution:**
```bash
# Verify installation location
docker run --rm --entrypoint python courses-api:latest -c "import site; print(site.getsitepackages())"

# Ensure PATH includes user site-packages
ENV PATH=/root/.local/bin:$PATH
```

---

## Performance Benchmarking

| Metric | Pip (Traditional) | Poetry | UV | Pip Advantage |
|--------|------------------|--------|-----|---------------|
| **Build Time (CI)** | 60-90s | 50-95s | 8-20s | Compatible everywhere |
| **Image Size** | 350-500 MB | 350-500 MB | 350-500 MB | Comparable |
| **Dependency Resolution** | Non-deterministic | Deterministic | Deterministic | Simple |
| **Learning Curve** | Minimal | Moderate | Low | Easiest to learn |
| **Tooling Required** | Python only | Poetry | UV | Python only |

---

## Conclusion: The Enduring Value of Pip

Pip with requirements.txt remains the most universally accessible approach to Python containerization. For the AI Powered Video Tutorial Portal, this approach delivers:

- **Universal compatibility** – Works on every Python runtime, every CI/CD platform
- **Simplicity** – One file, no additional tooling
- **Battle-tested** – Millions of deployments worldwide
- **Easy migration** – Any Python project can use this approach
- **Azure-ready** – Native integration with Azure Container Registry, Container Apps, and AKS

While modern tools like Poetry and UV offer significant advantages in dependency resolution speed and determinism, pip remains the foundation upon which Python containerization was built. For teams new to containers, migrating legacy applications, or working in constrained environments, pip is the reliable, battle-tested foundation that just works.

---

### Stories at a Glance

**Complete Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds

- 📦 **3. Pip + Docker: The Classic Python Containerization** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization *(This story)*

- 🚀 **4. Azure Container Apps: Serverless Python Deployment** – Deploying FastAPI applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent development environments and seamless deployment

- 🔧 **6. Azure Developer CLI (azd) with Python: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Python Microservices at Scale** – Deploying FastAPI applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Python** – Automated container builds, testing, and deployment with GitHub Actions workflows

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Python Container Deployments** – Deploying Python FastAPI applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## What's Next?

Over the coming weeks, each approach in this Python series will be explored in exhaustive detail. We'll examine real-world Azure deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first FastAPI application or an enterprise migrating Python workloads to Azure Kubernetes Service, you'll find practical guidance tailored to your infrastructure requirements.

Pip represents the foundation of Python containerization—simple, reliable, and universally compatible. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from classic pip builds to modern UV workflows, and from rapid prototyping to mission-critical production deployments on Azure Kubernetes Service.

**Coming next in the series:**
**🚀 Azure Container Apps: Serverless Python Deployment** – Deploying FastAPI applications to Azure Container Apps with auto-scaling and managed infrastructure