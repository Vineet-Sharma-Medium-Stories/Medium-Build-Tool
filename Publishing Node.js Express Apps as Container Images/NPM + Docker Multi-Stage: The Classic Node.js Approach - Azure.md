# NPM + Docker Multi-Stage: The Classic Node.js Approach - Azure

## Building Production-Ready Express.js Containers for Azure with npm

### Introduction: The Foundation of Node.js Containerization on Azure

In the [introductory installment](#) of this Node.js series, we explored the landscape of container deployment options for Express.js applications on Azure—from traditional npm-based builds to modern pnpm workflows, and from Azure Container Apps to Kubernetes orchestration. Now, we dive deep into what remains the most widely used and battle-tested approach for Node.js containerization: **npm with multi-stage Docker builds**.

npm (Node Package Manager) has been the cornerstone of the Node.js ecosystem since its inception. For the **AI Powered Video Tutorial Portal**—an Express.js application with MongoDB integration, Winston logging, Swagger documentation, and comprehensive REST API endpoints—npm provides a straightforward, reliable foundation for containerization. This project showcases the patterns that have made Node.js the premier choice for API development: modular architecture, async/await patterns, and robust error handling.

This installment explores the complete workflow for containerizing npm-managed Node.js applications for Azure, using the Courses Portal API as our case study. We'll master multi-stage builds, layer caching optimization, environment-specific configurations, and production-grade Azure Container Registry integration—all while leveraging the simplicity and ubiquity of npm.

```mermaid
graph TD
    subgraph "Development"
        A[package.json] --> B[npm install]
        B --> C[Local Development]
    end
    
    subgraph "Container Build (Multi-Stage)"
        D[Builder Stage] --> E[npm ci]
        E --> F[Install Dependencies]
        F --> G[Runtime Stage]
        G --> H[Copy App Code]
    end
    
    subgraph "Azure Deployment"
        H --> I[Azure Container Registry]
        I --> J[Azure Container Apps]
        I --> K[Azure Kubernetes Service]
        I --> L[Azure App Service]
    end
    
    style D fill:#2b6cb0,color:#fff
    style G fill:#48bb78,color:#fff
    style I fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry *(This story)*

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## Understanding the Courses Portal API Architecture

Before diving into containerization, let's understand what we're deploying on Azure. The **AI Powered Video Tutorial Portal** is a comprehensive Express.js application with:

### Solution Structure
```
Courses-Portal-API-NodeJS/
├── config/
│   ├── database.js        # MongoDB connection
│   ├── logger.js          # Winston logger setup
│   └── swagger.js         # Swagger/OpenAPI configuration
├── controllers/
│   ├── courseController.js
│   ├── courseContentController.js
│   └── courseSectionAssetsController.js
├── middleware/
│   ├── cors.js
│   └── errorHandler.js
├── models/
│   ├── Course.js
│   ├── CourseContent.js
│   └── CourseSectionAssets.js
├── routes/
│   ├── courseRoutes.js
│   ├── courseContentRoutes.js
│   └── courseSectionAssetsRoutes.js
├── services/
│   └── loggingService.js
├── logs/
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── package.json
├── server.js
└── setup.js
```

### Key Dependencies for Azure

| Dependency | Version | Purpose |
|------------|---------|---------|
| **express** | ^4.18.0 | Web framework |
| **mongoose** | ^7.0.0 | MongoDB ODM |
| **winston** | ^3.11.0 | Structured logging |
| **morgan** | ^1.10.0 | HTTP request logging |
| **dotenv** | ^16.3.0 | Environment configuration |
| **swagger-ui-express** | ^5.0.0 | API documentation |
| **swagger-jsdoc** | ^6.2.0 | OpenAPI specification |
| **cors** | ^2.8.5 | Cross-origin resource sharing |
| **helmet** | ^7.0.0 | Security headers |

---

## The npm-Optimized Dockerfile: Production-Ready Configuration

Let's examine the complete production Dockerfile for the Courses Portal API, optimized for npm and Azure deployment:

```dockerfile
# ============================================
# AI Powered Video Tutorial Portal - npm Build for Azure
# ============================================
# Production-ready Dockerfile for Express.js + npm
# Optimized for Azure Container Registry and Container Apps

# ============================================
# STAGE 1: Builder with npm
# ============================================
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files first for optimal layer caching
# These files change less frequently than source code
COPY package*.json ./

# Install production dependencies only
# Using npm ci for deterministic builds (respects package-lock.json)
# --omit=dev: Exclude development dependencies
RUN npm ci --only=production --omit=dev

# ============================================
# STAGE 2: Runtime Image
# ============================================
FROM node:20-alpine AS runtime

# Install runtime dependencies for health checks and monitoring
RUN apk add --no-cache \
    curl \
    tzdata

# Create non-root user for security
# This reduces attack surface in production
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy installed node_modules from builder stage
# This includes all production dependencies installed via npm
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules

# Copy application source code
# Separating from dependencies for better layer caching
COPY --chown=nodejs:nodejs . .

# Create logs directory with proper permissions
RUN mkdir -p logs && chown -R nodejs:nodejs logs

# Switch to non-root user
USER nodejs

# Expose port (Express default)
EXPOSE 3000

# Health check for Azure Container Apps
# Checks application health endpoint
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# Run the application
CMD ["node", "server.js"]
```

---

## Understanding the Package.json Structure

### package.json for Production

```json
{
  "name": "courses-portal-api",
  "version": "1.0.0",
  "description": "AI Powered Video Tutorial Portal - Express.js Backend",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "setup": "node setup.js",
    "test": "jest",
    "lint": "eslint .",
    "docker:dev": "docker-compose up --build",
    "docker:down": "docker-compose down"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.5.0",
    "winston": "^3.11.0",
    "morgan": "^1.10.0",
    "dotenv": "^16.3.1",
    "swagger-ui-express": "^5.0.0",
    "swagger-jsdoc": "^6.2.8",
    "cors": "^2.8.5",
    "helmet": "^7.0.0",
    "express-rate-limit": "^6.10.0",
    "compression": "^1.7.4"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.7.0",
    "supertest": "^6.3.3",
    "eslint": "^8.50.0",
    "eslint-config-airbnb-base": "^15.0.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  }
}
```

---

## Layer Analysis and Optimization for Azure ECR

### Layer-by-Layer Breakdown

| Layer | Size | Cache Key | Azure Impact |
|-------|------|-----------|--------------|
| `FROM node:20-alpine` | ~130 MB | Image digest | $0.07/GB-month |
| `COPY package*.json` | ~10 KB | File content hashes | Negligible |
| `RUN npm ci` | ~100-200 MB | package-lock.json | $0.05-0.10/GB-month |
| `RUN apk add curl` | ~5 MB | Package list | Minimal |
| `COPY application code` | ~1-5 MB | All source files | Minimal |
| **Final image** | **~250-350 MB** | - | **$0.13-0.18/GB-month** |

### Optimization Strategies for Azure

**1. Dependency Caching**

The Dockerfile copies `package.json` and `package-lock.json` before any source code. This means:

- ✅ Dependency layers are cached until `package.json` changes
- ✅ Package installation is skipped on code-only changes
- ✅ Faster builds in Azure DevOps and GitHub Actions

**2. Production-Only Dependencies**

```dockerfile
RUN npm ci --only=production --omit=dev
```

- ✅ Excludes `nodemon`, `jest`, `eslint`, `supertest`
- ✅ Reduces final image size by 100-200 MB
- ✅ Lower Azure Container Registry storage costs

**3. Alpine Base Image Benefits**

| Base Image | Size | Security | Build Speed |
|------------|------|----------|-------------|
| `node:20` | ~1 GB | Full OS | Slower |
| `node:20-slim` | ~300 MB | Minimal | Medium |
| `node:20-alpine` | ~130 MB | Minimal | Fastest |

**4. Non-Root User Security**

```dockerfile
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs
```

- ✅ Prevents privilege escalation if container is compromised
- ✅ Required for Azure security best practices
- ✅ Aligns with compliance frameworks

---

## Environment Configuration for Azure

### .env File for Local Development

```bash
# .env.example
# Server Configuration
NODE_ENV=development
PORT=3000

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/courses_portal

# Logging
LOG_LEVEL=info

# Security
CORS_ORIGIN=http://localhost:3000

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

### Docker Runtime Environment Variables

```bash
# Run with environment variables
docker run -d \
    -p 3000:3000 \
    -e NODE_ENV=production \
    -e MONGODB_URI="mongodb://azure-cosmos:10255/courses_portal?ssl=true" \
    -e LOG_LEVEL=info \
    --name courses-api \
    coursetutorials.azurecr.io/courses-api:latest
```

---

## Azure Container Registry Integration

### Creating and Configuring ACR

```bash
# Create resource group
az group create --name rg-courses-portal --location eastus

# Create Azure Container Registry
az acr create \
    --resource-group rg-courses-portal \
    --name coursetutorials \
    --sku Standard \
    --admin-enabled false

# Enable image scanning
az acr update \
    --name coursetutorials \
    --resource-group rg-courses-portal \
    --admin-enabled false \
    --allow-trusted-services true

# Login to ACR
az acr login --name coursetutorials
```

### Building and Pushing to ACR

```bash
# Build with npm-optimized Dockerfile
docker build -t courses-api:latest -f Dockerfile.npm .

# Tag for ACR
docker tag courses-api:latest coursetutorials.azurecr.io/courses-api:latest
docker tag courses-api:latest coursetutorials.azurecr.io/courses-api:$(date +%Y%m%d-%H%M%S)

# Push to ACR
docker push coursetutorials.azurecr.io/courses-api:latest
docker push coursetutorials.azurecr.io/courses-api:$(date +%Y%m%d-%H%M%S)
```

### ACR Tasks for Automated Builds

```bash
# Create a task that builds on code push
az acr task create \
    --registry coursetutorials \
    --name courses-api-build \
    --image courses-api:{{.Run.ID}} \
    --context https://github.com/your-org/courses-portal-api-nodejs.git \
    --file Dockerfile \
    --git-access-token $GITHUB_TOKEN
```

---

## Docker Compose for Local Development

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

  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: runtime
    container_name: courses-api
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: development
      MONGODB_URI: mongodb://admin:password@mongodb:27017/courses_portal?authSource=admin
      LOG_LEVEL: debug
    depends_on:
      mongodb:
        condition: service_healthy
    volumes:
      - ./logs:/app/logs
      - ./:/app:ro
      - /app/node_modules
    command: npm run dev

volumes:
  mongodb_data:
```

---

## Health Check Implementation for Azure

### Health Check Endpoint in Express.js

```javascript
// server.js - Health check for Azure Container Apps
const express = require('express');
const mongoose = require('mongoose');

const app = express();

// Liveness probe - checks if app is running
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    service: 'courses-api',
    version: process.env.npm_package_version || '1.0.0',
    environment: process.env.NODE_ENV || 'development'
  });
});

// Readiness probe - checks if app is ready to serve traffic
app.get('/ready', async (req, res) => {
  const checks = {
    database: false,
    server: true
  };

  // Check database connection
  try {
    if (mongoose.connection.readyState === 1) {
      checks.database = true;
    } else {
      throw new Error('Database not connected');
    }
  } catch (error) {
    return res.status(503).json({
      status: 'not ready',
      checks,
      error: error.message
    });
  }

  res.status(200).json({
    status: 'ready',
    checks
  });
});

// Graceful shutdown for Azure
process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(() => {
    console.log('HTTP server closed');
    mongoose.connection.close(false, () => {
      console.log('MongoDB connection closed');
      process.exit(0);
    });
  });
});
```

---

## CI/CD with GitHub Actions and npm

### GitHub Actions Workflow for Node.js

```yaml
# .github/workflows/deploy.yml
name: Node.js CI/CD to Azure

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
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test

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
    
    - name: Build and push
      run: |
        docker build -t ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }} .
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

## Advanced npm Patterns for Production

### Using npm ci vs npm install

| Command | Use Case | Benefit |
|---------|----------|---------|
| `npm ci` | CI/CD pipelines | Respects lockfile, faster, deterministic |
| `npm install` | Local development | Updates lockfile, allows version updates |

```dockerfile
# In Dockerfile - always use npm ci for production
RUN npm ci --only=production --omit=dev
```

### npm Audit for Security

```bash
# Run security audit
npm audit --production

# Fix vulnerabilities automatically
npm audit fix --production
```

### npm Dedupe for Smaller node_modules

```bash
# Deduplicate dependencies for smaller image
npm dedupe

# Results in smaller node_modules size
du -sh node_modules
# 45MB before dedupe
# 38MB after dedupe
```

### npm Scripts for Azure Deployment

```json
{
  "scripts": {
    "prestart": "npm run setup && npm run migrate",
    "start": "node server.js",
    "setup": "node setup.js",
    "migrate": "node scripts/migrate.js",
    "health": "curl http://localhost:3000/health",
    "docker:build": "docker build -t courses-api .",
    "docker:run": "docker run -p 3000:3000 courses-api"
  }
}
```

---

## Troubleshooting npm Container Builds on Azure

### Issue 1: npm ci Fails Due to Lockfile Mismatch

**Error:** `npm ERR! Invalid: lock file's some-package@1.0.0 does not satisfy some-package@1.0.1`

**Solution:**
```bash
# Regenerate lockfile locally
npm install
git add package-lock.json
git commit -m "Update package-lock.json"
```

### Issue 2: Large node_modules Size

**Problem:** Final image > 500 MB

**Solution:**
```dockerfile
# Use Alpine base
FROM node:20-alpine

# Use npm ci with production only
RUN npm ci --only=production --omit=dev

# Run npm dedupe
RUN npm dedupe

# Clean npm cache
RUN npm cache clean --force
```

### Issue 3: Node.js Version Mismatch

**Error:** `Node.js version mismatch: Expected 18, got 20`

**Solution:**
```dockerfile
# Use specific Node.js version
FROM node:18-alpine

# Or set engine-strict in .npmrc
RUN echo "engine-strict=true" > .npmrc
```

### Issue 4: MongoDB Connection Timeout

**Error:** `MongoNetworkError: failed to connect to server`

**Solution:**
```javascript
// Add connection retry logic
const connectWithRetry = async () => {
  const MAX_RETRIES = 5;
  const RETRY_INTERVAL = 5000;
  
  for (let i = 0; i < MAX_RETRIES; i++) {
    try {
      await mongoose.connect(process.env.MONGODB_URI);
      console.log('MongoDB connected');
      return;
    } catch (err) {
      console.log(`Retry ${i + 1}/${MAX_RETRIES}: ${err.message}`);
      await new Promise(resolve => setTimeout(resolve, RETRY_INTERVAL));
    }
  }
  process.exit(1);
};
```

---

## Performance Benchmarking

| Metric | npm (Alpine) | npm (Slim) | npm (Full) | Improvement |
|--------|--------------|------------|------------|-------------|
| **Image Size** | 250-350 MB | 400-500 MB | 900-1100 MB | 60-75% smaller |
| **Build Time (CI)** | 45-60s | 60-90s | 90-120s | 50% faster |
| **Container Startup** | 1-2s | 2-3s | 3-5s | 60% faster |
| **Memory Usage** | 80-120 MB | 100-150 MB | 150-200 MB | 40% lower |
| **Azure Storage Cost** | $0.13-0.18/mo | $0.20-0.25/mo | $0.45-0.55/mo | 60-70% lower |

---

## Conclusion: The npm Advantage on Azure

npm with multi-stage Docker builds remains the foundation of Node.js containerization on Azure. For the AI Powered Video Tutorial Portal, this approach delivers:

- **Universal compatibility** – Works with every Node.js project, every Azure region
- **Simplicity** – One package manager, no additional tooling
- **Battle-tested** – Millions of deployments on Azure worldwide
- **Deterministic builds** – `npm ci` ensures reproducible installs
- **Azure-ready** – Native integration with ACR, Container Apps, and AKS

For teams building Node.js Express applications for Azure, npm-based multi-stage builds are the reliable, battle-tested foundation that just works.

---

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry *(This story)*

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images

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

npm represents the foundation of Node.js containerization on Azure—simple, reliable, and universally compatible. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from classic npm builds to modern pnpm workflows, and from rapid prototyping to mission-critical production deployments on Azure Kubernetes Service.

**Coming next in the series:**
**🧶 Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance