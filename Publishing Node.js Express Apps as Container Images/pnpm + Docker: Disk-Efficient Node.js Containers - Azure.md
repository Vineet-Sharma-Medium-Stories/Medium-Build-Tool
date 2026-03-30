# pnpm + Docker: Disk-Efficient Node.js Containers - Azure

## Leveraging Content-Addressable Storage for Faster Installs and Smaller Images

### Introduction: The Third Generation of Node.js Package Management

In the [previous installments](#) of this Node.js series, we explored npm with multi-stage builds—the classic foundation—and Yarn Berry with deterministic dependency management. While npm provides ubiquity and Yarn offers reproducibility, a third generation of package managers has emerged that fundamentally reimagines how dependencies are stored and installed: **pnpm**.

pnpm (performant npm) uses a content-addressable storage approach that dramatically reduces disk usage and installation time. For the **AI Powered Video Tutorial Portal**—an Express.js application with MongoDB integration, Winston logging, and comprehensive REST API endpoints—pnpm can reduce container image sizes by 30-50% compared to npm and Yarn, while making installations up to 2x faster through its global content-addressable store.

This installment explores the complete workflow for containerizing pnpm-managed Node.js applications for Azure, using the Courses Portal API as our case study. We'll master pnpm's content-addressable storage, symlink-based node_modules structure, multi-stage Docker optimization, and production-grade Azure Container Registry integration—all while leveraging pnpm's disk-efficient approach to dependency management.

```mermaid
graph TD
    subgraph "npm/Yarn Approach"
        A[Project A] --> B[node_modules (full copy)]
        C[Project B] --> D[node_modules (full copy)]
    end
    
    subgraph "pnpm Approach"
        E[Project A] --> F[symlinks]
        F --> G[Global Content-Addressable Store]
        H[Project B] --> I[symlinks]
        I --> G
    end
    
    subgraph "Azure Benefits"
        G --> J[Smaller Images]
        G --> K[Faster Builds]
        G --> L[Less Storage]
    end
    
    style G fill:#48bb78,color:#fff
    style J fill:#2b6cb0,color:#fff
    style K fill:#2b6cb0,color:#fff
```

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images *(This story)*

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## Understanding pnpm for Node.js on Azure

### What Makes pnpm Different?

| Feature | npm | Yarn | pnpm | Azure Impact |
|---------|-----|------|------|--------------|
| **Storage Model** | Copy per project | Copy per project | Content-addressable store | 30-50% smaller images |
| **node_modules Structure** | Nested (deep) | Nested (deep) | Flat with symlinks | Faster file I/O |
| **Disk Usage (10 projects)** | 10 GB | 10 GB | 1-2 GB | 80-90% less storage |
| **Install Time** | Baseline | 10-20% faster | 30-50% faster | Lower build costs |
| **Monorepo Support** | Limited | Good | Excellent | Workspaces optimized |

### How pnpm Works: Content-Addressable Storage

```mermaid
graph LR
    subgraph "Global Store (~/.pnpm-store)"
        A[express@4.18.2]
        B[mongoose@7.5.0]
        C[winston@3.11.0]
    end
    
    subgraph "Project node_modules"
        D[.pnpm/]
        E[express -> symlink]
        F[mongoose -> symlink]
        G[winston -> symlink]
    end
    
    D --> A
    E --> A
    F --> B
    G --> C
```

### pnpm Core Concepts

| Concept | Description | Azure Benefit |
|---------|-------------|---------------|
| **Content-Addressable Store** | Global storage of package versions | Never download same package twice |
| **Symlink-based node_modules** | Flat structure with symlinks to store | Smaller container layers |
| **pnpm-lock.yaml** | Deterministic lockfile | Reproducible builds |
| **Workspaces** | Native monorepo support | Multiple services in one repo |
| **Filtering** | Selective installation | Faster CI/CD for microservices |

---

## Setting Up pnpm for the Courses Portal API

### Step 1: Install pnpm

```bash
# Install via npm
npm install -g pnpm

# Or via standalone script (recommended for CI)
curl -fsSL https://get.pnpm.io/install.sh | sh -

# Verify installation
pnpm --version
# 8.0.0
```

### Step 2: Configure pnpm for Production

```yaml
# .npmrc - pnpm configuration for Azure
# Use pnpm strict engine
engine-strict=true

# Configure pnpm store location (in container, use /pnpm/store)
store-dir = /pnpm/store

# Enable strict peer dependencies
strict-peer-dependencies=true

# Enable frozen lockfile for CI
frozen-lockfile=true

# Use exact versions
save-exact=true
```

### Step 3: Migrate from npm/package-lock.json

```bash
# Remove existing node_modules
rm -rf node_modules package-lock.json

# Install with pnpm (creates pnpm-lock.yaml)
pnpm install

# Update .gitignore
cat >> .gitignore << EOF
# pnpm
.pnpm-store
EOF

# Commit lockfile
git add pnpm-lock.yaml
git commit -m "Migrate to pnpm"
```

### Step 4: Project Structure with pnpm

```
Courses-Portal-API-NodeJS/
├── node_modules/            # Symlinks to global store
├── .pnpm-store/             # Local cache (not checked in)
├── pnpm-lock.yaml           # Deterministic lockfile
├── .npmrc                   # pnpm configuration
├── package.json
├── Dockerfile.pnpm          # pnpm-optimized Dockerfile
└── ... (application code)
```

---

## The pnpm-Optimized Dockerfile for Azure

### Production Dockerfile with pnpm

```dockerfile
# ============================================
# AI Powered Video Tutorial Portal - pnpm Build for Azure
# ============================================
# Production-ready Dockerfile for Express.js + pnpm
# Optimized for Azure Container Registry with content-addressable storage
# Leverages symlinks for minimal disk usage

# ============================================
# STAGE 1: Builder with pnpm
# ============================================
FROM node:20-alpine AS builder

# Install pnpm globally
RUN npm install -g pnpm@8.0.0

# Set working directory
WORKDIR /app

# Copy package files first for optimal layer caching
COPY package.json pnpm-lock.yaml .npmrc ./

# Install dependencies with pnpm
# --frozen-lockfile: Ensures lockfile matches, fails if changes needed
# --prod: Install production dependencies only
# --ignore-scripts: Skip lifecycle scripts for faster builds
RUN pnpm install --frozen-lockfile --prod --ignore-scripts

# ============================================
# STAGE 2: Runtime Image
# ============================================
FROM node:20-alpine AS runtime

# Install runtime dependencies for health checks
RUN apk add --no-cache curl

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy pnpm store and node_modules structure
# Important: Copy the entire node_modules (symlinks preserved)
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package.json ./package.json

# Copy application source code
COPY --chown=nodejs:nodejs . .

# Create logs directory
RUN mkdir -p logs && chown -R nodejs:nodejs logs

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check for Azure Container Apps
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# Run the application
CMD ["node", "server.js"]
```

### Advanced Dockerfile with pnpm Store Mount

For multi-stage builds with caching:

```dockerfile
# syntax=docker/dockerfile:1.4
FROM node:20-alpine AS builder

RUN npm install -g pnpm@8.0.0

WORKDIR /app

# Copy package files
COPY package.json pnpm-lock.yaml .npmrc ./

# Use BuildKit cache mount for pnpm store
# This caches packages between builds
RUN --mount=type=cache,target=/pnpm/store \
    pnpm install --frozen-lockfile --prod --store-dir=/pnpm/store

FROM node:20-alpine AS runtime

RUN apk add --no-cache curl
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001

WORKDIR /app

# Copy from builder (preserving symlinks)
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package.json ./package.json

COPY --chown=nodejs:nodejs . .

USER nodejs

EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

CMD ["node", "server.js"]
```

---

## Understanding pnpm's node_modules Structure

### Traditional npm Structure (Nested)

```
node_modules/
├── express/
├── mongoose/
│   └── node_modules/
│       └── mongodb/
├── winston/
│   └── node_modules/
│       └── logform/
│           └── node_modules/
│               └── colors/
```

### pnpm Structure (Flat with Symlinks)

```
node_modules/
├── .pnpm/
│   ├── express@4.18.2/
│   │   └── node_modules/
│   │       └── express -> ../../express@4.18.2
│   ├── mongoose@7.5.0/
│   └── winston@3.11.0/
├── express -> .pnpm/express@4.18.2/node_modules/express
├── mongoose -> .pnpm/mongoose@7.5.0/node_modules/mongoose
└── winston -> .pnpm/winston@3.11.0/node_modules/winston
```

### Benefits for Azure Containers

| Aspect | npm | pnpm | Azure Impact |
|--------|-----|------|--------------|
| **node_modules size** | 150-200 MB | 100-150 MB | 30% smaller images |
| **File count** | 30,000+ | 20,000+ | Faster Docker builds |
| **Layer caching** | Changes often | Stable | Better cache hits |
| **Symlink support** | No | Yes | Works in Linux containers |

---

## pnpm Workspaces for Microservices on Azure

### pnpm Workspace Configuration

```yaml
# pnpm-workspace.yaml
packages:
  - 'services/*'
  - 'packages/*'
  - 'shared/*'
```

### Workspace Structure

```
monorepo/
├── services/
│   ├── api/                 # Express.js API service
│   │   ├── package.json
│   │   └── server.js
│   ├── worker/              # Background worker
│   │   └── package.json
│   └── admin/               # Admin dashboard
│       └── package.json
├── packages/
│   ├── shared-models/       # Shared Mongoose models
│   └── shared-utils/        # Shared utilities
└── pnpm-workspace.yaml
```

### Installing Workspace Dependencies

```bash
# Install all dependencies for all services
pnpm install

# Install a package to a specific service
pnpm --filter api add express

# Run script across all services
pnpm -r run test
```

---

## Azure Container Registry Integration with pnpm

### Build and Push to ACR

```bash
# Login to ACR
az acr login --name coursetutorials

# Build with pnpm Dockerfile
docker build -f Dockerfile.pnpm -t courses-api:latest .

# Tag for ACR
docker tag courses-api:latest coursetutorials.azurecr.io/courses-api:latest

# Push to ACR
docker push coursetutorials.azurecr.io/courses-api:latest
```

### ACR Task with pnpm and Cache Mount

```bash
# Create ACR task with pnpm
az acr task create \
    --registry coursetutorials \
    --name pnpm-build \
    --image courses-api:{{.Run.ID}} \
    --context https://github.com/your-org/courses-portal-api-nodejs.git \
    --file Dockerfile.pnpm \
    --git-access-token $GITHUB_TOKEN \
    --set BUILDKIT_PROGRESS=plain
```

---

## GitHub Actions with pnpm

### pnpm-Optimized GitHub Actions Workflow

```yaml
# .github/workflows/pnpm-deploy.yml
name: pnpm CI/CD to Azure

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  ACR_NAME: coursetutorials
  IMAGE_NAME: courses-api
  NODE_VERSION: '20'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ env.NODE_VERSION }}
    
    - name: Install pnpm
      uses: pnpm/action-setup@v2
      with:
        version: 8
        run_install: false
    
    - name: Get pnpm store directory
      id: pnpm-cache
      shell: bash
      run: |
        echo "STORE_PATH=$(pnpm store path)" >> $GITHUB_OUTPUT
    
    - name: Setup pnpm cache
      uses: actions/cache@v3
      with:
        path: ${{ steps.pnpm-cache.outputs.STORE_PATH }}
        key: ${{ runner.os }}-pnpm-store-${{ hashFiles('**/pnpm-lock.yaml') }}
        restore-keys: |
          ${{ runner.os }}-pnpm-store-
    
    - name: Install dependencies
      run: pnpm install --frozen-lockfile
    
    - name: Run tests
      run: pnpm test

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
    
    - name: Build and push with pnpm
      run: |
        docker build -f Dockerfile.pnpm -t ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }} .
        docker push ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
        docker tag ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }} ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:latest
        docker push ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:latest
    
    - name: Deploy to Azure Container Apps
      run: |
        az containerapp update \
          --name courses-api \
          --resource-group rg-courses-portal \
          --image ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

---

## Azure DevOps with pnpm

### YAML Pipeline for Azure DevOps

```yaml
# azure-pipelines.yml
trigger:
- main

variables:
  acrName: 'coursetutorials'
  imageName: 'courses-api'
  nodeVersion: '20'

stages:
- stage: Build
  displayName: 'Build and Test'
  jobs:
  - job: Build
    pool:
      vmImage: 'ubuntu-latest'
    steps:
    - task: NodeTool@0
      inputs:
        versionSpec: '$(nodeVersion)'
    
    - script: |
        npm install -g pnpm
        pnpm --version
      displayName: 'Install pnpm'
    
    - script: |
        pnpm install --frozen-lockfile
        pnpm test
      displayName: 'Install and test'
    
    - script: |
        docker build -f Dockerfile.pnpm -t $(acrName).azurecr.io/$(imageName):$(Build.BuildId) .
        docker push $(acrName).azurecr.io/$(imageName):$(Build.BuildId)
        docker tag $(acrName).azurecr.io/$(imageName):$(Build.BuildId) $(acrName).azurecr.io/$(imageName):latest
        docker push $(acrName).azurecr.io/$(imageName):latest
      displayName: 'Build and push with pnpm'

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
                  --resource-group rg-courses-portal \
                  --image $(acrName).azurecr.io/$(imageName):$(Build.BuildId)
```

---

## Docker Compose with pnpm for Local Development

```yaml
# docker-compose.yml
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

  api:
    build:
      context: .
      dockerfile: Dockerfile.pnpm
      target: runtime
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: development
      MONGODB_URI: mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin
    depends_on:
      - mongodb
    volumes:
      - ./:/app
      - /app/node_modules  # Don't mount node_modules
    command: pnpm run dev

volumes:
  mongodb_data:
```

---

## pnpm Commands Reference

### Common pnpm Commands

| Command | Description | Azure Use Case |
|---------|-------------|----------------|
| `pnpm install` | Install dependencies | Local development |
| `pnpm install --frozen-lockfile` | CI/CD install | GitHub Actions, Azure DevOps |
| `pnpm install --prod` | Production install | Docker builds |
| `pnpm update` | Update dependencies | Security patches |
| `pnpm outdated` | List outdated packages | Dependency audit |
| `pnpm prune` | Remove unnecessary packages | Smaller images |
| `pnpm store prune` | Clean global store | CI/CD cache cleanup |

### pnpm for CI/CD Optimization

```bash
# In CI/CD, use frozen lockfile for deterministic builds
pnpm install --frozen-lockfile --prod

# Check for unused dependencies
pnpm why some-package

# List installed packages with sizes
pnpm list --depth=0
```

---

## Troubleshooting pnpm on Azure

### Issue 1: pnpm Not Found in Container

**Error:** `pnpm: command not found`

**Solution:**
```dockerfile
# Install pnpm globally
RUN npm install -g pnpm@8.0.0

# Or use corepack
RUN corepack enable && corepack prepare pnpm@8.0.0 --activate
```

### Issue 2: Lockfile Mismatch in CI

**Error:** `Lockfile is not up-to-date`

**Solution:**
```bash
# In CI, use frozen-lockfile to fail if mismatch
pnpm install --frozen-lockfile

# To fix locally
pnpm install
git add pnpm-lock.yaml
git commit -m "Update pnpm-lock.yaml"
```

### Issue 3: Symlink Issues in Docker

**Error:** `Error: ELOOP: too many symbolic links`

**Solution:**
```dockerfile
# Ensure symlinks are preserved during COPY
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules

# Or use tar to preserve symlinks
RUN tar -czf node_modules.tar.gz -C /app node_modules
RUN tar -xzf node_modules.tar.gz -C /app
```

### Issue 4: Large pnpm Store in CI

**Problem:** CI cache grows too large

**Solution:**
```yaml
# In GitHub Actions, prune store after install
- name: Install dependencies
  run: |
    pnpm install --frozen-lockfile
    pnpm store prune
```

---

## Performance Benchmarking

| Metric | npm | Yarn | pnpm | Improvement |
|--------|-----|------|------|-------------|
| **Image Size** | 250-350 MB | 250-350 MB | 150-250 MB | 30-40% smaller |
| **Install Time (CI)** | 45-60s | 40-55s | 30-45s | 20-30% faster |
| **node_modules files** | 30,000+ | 30,000+ | 20,000+ | 33% fewer files |
| **Disk Usage (10 projects)** | 10 GB | 10 GB | 2-3 GB | 70-80% less |
| **Azure Storage Cost** | $0.13-0.18/mo | $0.13-0.18/mo | $0.08-0.13/mo | 30% lower |

---

## Conclusion: The pnpm Advantage on Azure

pnpm represents the third generation of Node.js package management, delivering:

- **30-50% smaller container images** – Content-addressable storage eliminates duplication
- **20-30% faster installs** – Global store with symlinks
- **70-80% less disk usage** – Share dependencies across projects
- **Deterministic builds** – Strict lockfile ensures reproducibility
- **Workspace-native** – Excellent monorepo support for microservices

For the AI Powered Video Tutorial Portal, pnpm delivers:

- **Smaller container images** – Lower Azure Container Registry costs
- **Faster CI/CD builds** – Less time in GitHub Actions and Azure DevOps
- **Efficient monorepo support** – Multiple services with shared dependencies
- **Deterministic builds** – Exactly the same dependencies everywhere

pnpm represents the evolution of Node.js package management—bringing disk efficiency, faster installs, and production-grade reliability to containerized applications on Azure.

---

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images *(This story)*

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## What's Next?

Over the coming weeks, each approach in this Node.js series will be explored in exhaustive detail. We'll examine real-world Azure deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first Express.js application or an enterprise migrating Node.js workloads to Azure Kubernetes Service, you'll find practical guidance tailored to your infrastructure requirements.

pnpm represents the pinnacle of Node.js package management—bringing disk efficiency, faster installs, and production-grade reliability to containerized applications on Azure. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from classic npm builds to modern pnpm workflows.

**Coming next in the series:**
**🚀 Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure