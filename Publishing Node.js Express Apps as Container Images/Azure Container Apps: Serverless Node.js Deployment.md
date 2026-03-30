# Azure Container Apps: Serverless Node.js Deployment

## Deploying Express.js Applications with Auto-Scaling and Managed Infrastructure

### Introduction: The Serverless Evolution for Node.js on Azure

In the [previous installments](#) of this Node.js series, we explored the complete spectrum of container build strategies—from the classic npm approach to modern pnpm workflows. While these techniques produce container images ready for deployment, a critical question remains: **how do you run these containers in production at scale, with minimal infrastructure management?**

Enter **Azure Container Apps**—a serverless container platform that represents the sweet spot between infrastructure-as-a-service (IaaS) and fully managed platforms. For the **AI Powered Video Tutorial Portal**—an Express.js application with MongoDB integration, Winston logging, and comprehensive REST API endpoints—Azure Container Apps provides the ideal deployment target, offering automatic scaling, integrated networking, built-in monitoring, and pay-per-use pricing, all while leveraging the Node.js ecosystem.

This installment explores the complete workflow for deploying Express.js applications to Azure Container Apps, from initial configuration to production-grade operations. We'll master auto-scaling rules, health probes, environment management, and integration with Azure services like Cosmos DB (MongoDB-compatible) and Redis Cache—all while leveraging the serverless benefits that make Container Apps the modern choice for Node.js workloads.

```mermaid
graph TD
    subgraph "Container Build Phase"
        A[Node.js Express App] --> B[Docker Build]
        B --> C[Container Image]
        C --> D[Azure Container Registry]
    end
    
    subgraph "Azure Container Apps"
        D --> E[Container App]
        E --> F[Auto-Scaling Rules]
        E --> G[Revision Management]
        E --> H[Ingress Configuration]
        F --> I[Scale to Zero]
        G --> J[Rolling Updates]
        H --> K[HTTPS Endpoints]
    end
    
    subgraph "Azure Services"
        E --> L[(Azure Cosmos DB<br/>MongoDB API)]
        E --> M[Azure Redis Cache]
        E --> N[Application Insights]
        L --> O[Persistent Data]
        M --> P[Session/Backplane]
        N --> Q[Monitoring/Tracing]
    end
    
    style E fill:#48bb78,color:#fff
    style F fill:#2b6cb0,color:#fff
    style K fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure *(This story)*

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## Understanding Azure Container Apps

### What Makes Azure Container Apps Special?

| Feature | Azure Container Apps | AKS | App Service | Functions |
|---------|---------------------|-----|-------------|-----------|
| **Serverless** | ✅ (scale to zero) | ❌ | ❌ | ✅ |
| **Container Support** | ✅ (any container) | ✅ | ⚠️ (limited) | ⚠️ (custom) |
| **Kubernetes API** | ❌ (simplified) | ✅ | ❌ | ❌ |
| **Auto-scaling** | ✅ (HTTP, CPU, memory) | ✅ (HPA) | ✅ (manual) | ✅ (event-driven) |
| **Cold Start** | ~2-5 seconds | N/A | N/A | <1 second |
| **Complexity** | Low | High | Low | Low |
| **Cost Model** | Pay per vCPU/memory | Node-based | Plan-based | Execution-based |

### Core Concepts for Node.js Developers

| Concept | Description | Express.js Relevance |
|---------|-------------|---------------------|
| **Container App** | Individual application unit | Your Express.js service |
| **Environment** | Secure boundary for multiple apps | Shared networking, logging |
| **Revision** | Immutable version of container app | Blue/green deployments |
| **Scale Rule** | Auto-scaling trigger | HTTP requests, CPU, memory |
| **Ingress** | External access configuration | HTTPS, traffic splitting |
| **Dapr** | Distributed application runtime | State management, pub/sub |
| **KEDA** | Kubernetes-based Event Driven Autoscaler | Custom metrics |

---

## Prerequisites and Initial Setup

### Azure CLI Installation

```bash
# Install Azure CLI (macOS)
brew install azure-cli

# Install Azure CLI (Ubuntu/Debian)
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install Azure CLI (Windows - PowerShell)
winget install -e --id Microsoft.AzureCLI

# Login to Azure
az login

# Install Container Apps extension
az extension add --name containerapp --upgrade

# Register required providers
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.OperationalInsights
```

### Create Resource Group and Environment

```bash
# Create resource group
az group create \
    --name rg-courses-portal \
    --location eastus

# Create Log Analytics workspace
az monitor log-analytics workspace create \
    --resource-group rg-courses-portal \
    --workspace-name logs-courses-portal

# Get workspace ID and key
WORKSPACE_ID=$(az monitor log-analytics workspace show \
    --resource-group rg-courses-portal \
    --workspace-name logs-courses-portal \
    --query customerId -o tsv)

WORKSPACE_KEY=$(az monitor log-analytics workspace get-shared-keys \
    --resource-group rg-courses-portal \
    --workspace-name logs-courses-portal \
    --query primarySharedKey -o tsv)

# Create Container Apps Environment
az containerapp env create \
    --name env-courses-portal \
    --resource-group rg-courses-portal \
    --location eastus \
    --logs-workspace-id $WORKSPACE_ID \
    --logs-workspace-key $WORKSPACE_KEY
```

---

## Deploying the Express.js API

### Container App Configuration

```bash
# Create the container app
az containerapp create \
    --name courses-api \
    --resource-group rg-courses-portal \
    --environment env-courses-portal \
    --image coursetutorials.azurecr.io/courses-api:latest \
    --target-port 3000 \
    --ingress external \
    --cpu 0.5 \
    --memory 1.0Gi \
    --min-replicas 0 \
    --max-replicas 10 \
    --scale-rule-name http \
    --scale-rule-http-concurrency 50 \
    --env-vars \
        NODE_ENV=Production \
        MONGODB_URI="mongodb://courses-db:10255/courses_portal?ssl=true" \
        LOG_LEVEL=info

# Get the application URL
az containerapp show \
    --name courses-api \
    --resource-group rg-courses-portal \
    --query properties.configuration.ingress.fqdn
```

### Advanced Configuration with YAML

```yaml
# containerapp.yaml
apiVersion: apps/v1
kind: ContainerApp
metadata:
  name: courses-api
  resourceGroup: rg-courses-portal
  environment: env-courses-portal
properties:
  configuration:
    ingress:
      external: true
      targetPort: 3000
      traffic:
        - latestRevision: true
          weight: 100
    registries:
      - server: coursetutorials.azurecr.io
        username: coursetutorials
        passwordSecretRef: acr-password
    secrets:
      - name: acr-password
        value: "your-acr-password"
      - name: mongodb-uri
        value: "mongodb://username:password@host:10255/db?ssl=true"
  template:
    containers:
      - image: coursetutorials.azurecr.io/courses-api:latest
        name: api
        env:
          - name: NODE_ENV
            value: Production
          - name: MONGODB_URI
            secretRef: mongodb-uri
          - name: LOG_LEVEL
            value: info
        resources:
          cpu: 0.5
          memory: 1Gi
        probes:
          - type: Liveness
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          - type: Readiness
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 5
    scale:
      minReplicas: 0
      maxReplicas: 10
      rules:
        - name: http
          http:
            metadata:
              concurrentRequests: "50"
        - name: cpu
          custom:
            type: cpu
            metadata:
              threshold: "70"
```

```bash
# Apply YAML configuration
az containerapp create --yaml containerapp.yaml
```

---

## Auto-Scaling Configuration for Node.js

### HTTP-Based Scaling

```bash
# Scale based on concurrent HTTP requests
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --scale-rule-name http \
    --scale-rule-http-concurrency 50
```

### CPU and Memory-Based Scaling

```bash
# Scale based on CPU utilization
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --scale-rule-name cpu \
    --scale-rule-custom-type cpu \
    --scale-rule-custom-metadata threshold=70
```

### Multiple Scale Rules

```yaml
# scale-rules.yaml
scale:
  minReplicas: 0
  maxReplicas: 10
  rules:
    - name: http
      http:
        metadata:
          concurrentRequests: "50"
    - name: cpu
      custom:
        type: cpu
        metadata:
          threshold: "70"
    - name: memory
      custom:
        type: memory
        metadata:
          threshold: "80"
    - name: queue
      custom:
        type: azure-servicebus
        metadata:
          queueName: courses-queue
          namespace: courses-sb
          messageCount: "10"
```

---

## Express.js Configuration for Azure Container Apps

### Health Check Endpoints

```javascript
// server.js - Health check for Container Apps
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

  // Check MongoDB connection
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

### Environment Configuration

```javascript
// config.js
require('dotenv').config();

module.exports = {
  // Application
  nodeEnv: process.env.NODE_ENV || 'development',
  port: parseInt(process.env.PORT || '3000', 10),
  
  // Database
  mongodbUri: process.env.MONGODB_URI || 'mongodb://localhost:27017/courses_portal',
  
  // Logging
  logLevel: process.env.LOG_LEVEL || 'info',
  
  // Feature flags
  apiKeyEnabled: process.env.API_KEY_ENABLED === 'true',
  continueWatchingEnabled: true,
  bookmarksEnabled: true,
  
  // Rate limiting
  rateLimitWindowMs: parseInt(process.env.RATE_LIMIT_WINDOW_MS || '900000', 10),
  rateLimitMaxRequests: parseInt(process.env.RATE_LIMIT_MAX_REQUESTS || '100', 10)
};
```

---

## Integration with Azure Services

### Azure Cosmos DB (MongoDB API)

```bash
# Create Cosmos DB account with MongoDB API
az cosmosdb create \
    --name courses-db \
    --resource-group rg-courses-portal \
    --kind MongoDB \
    --locations regionName=eastus failoverPriority=0

# Get connection string
az cosmosdb keys list \
    --name courses-db \
    --resource-group rg-courses-portal \
    --type connection-strings

# Update container app with connection string
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --set-env-vars \
        MONGODB_URI="mongodb://courses-db:10255/courses_portal?ssl=true"
```

### Azure Cache for Redis

```bash
# Create Redis cache
az redis create \
    --name courses-redis \
    --resource-group rg-courses-portal \
    --location eastus \
    --sku Basic \
    --vm-size c0

# Get Redis connection string
az redis show \
    --name courses-redis \
    --resource-group rg-courses-portal \
    --query hostName

# Update container app
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --set-env-vars \
        REDIS_HOST=courses-redis.redis.cache.windows.net \
        REDIS_PORT=6380
```

### Application Insights

```bash
# Create Application Insights
az monitor app-insights component create \
    --app courses-insights \
    --resource-group rg-courses-portal \
    --location eastus \
    --application-type web

# Get instrumentation key
az monitor app-insights component show \
    --app courses-insights \
    --resource-group rg-courses-portal \
    --query instrumentationKey

# Add to container app
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --set-env-vars \
        APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=xxxxx;IngestionEndpoint=https://eastus-0.in.applicationinsights.azure.com/"
```

---

## Logging and Monitoring for Node.js

### Winston Configuration for Azure

```javascript
// config/logger.js
const winston = require('winston');
const { ApplicationInsightsTransport } = require('winston-azure-application-insights');

const transports = [
  // Console transport for local development
  new winston.transports.Console({
    format: winston.format.combine(
      winston.format.colorize(),
      winston.format.simple()
    )
  })
];

// Add Application Insights in production
if (process.env.NODE_ENV === 'production' && process.env.APPLICATIONINSIGHTS_CONNECTION_STRING) {
  transports.push(
    new ApplicationInsightsTransport({
      connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
    })
  );
}

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  transports
});

module.exports = logger;
```

### Morgan Middleware with Azure Integration

```javascript
// middleware/logging.js
const morgan = require('morgan');
const logger = require('../config/logger');

// Morgan stream for Winston
const stream = {
  write: (message) => {
    logger.info(message.trim());
  }
};

// Custom morgan format with correlation ID
morgan.token('correlation-id', (req) => {
  return req.headers['x-correlation-id'] || 'no-correlation-id';
});

const morganFormat = ':method :url :status :response-time ms - :correlation-id';

// Export morgan middleware
const morganMiddleware = morgan(morganFormat, { stream });

module.exports = morganMiddleware;
```

---

## Revision Management and Traffic Splitting

### Create New Revision

```bash
# Update with new image (creates new revision)
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --image coursetutorials.azurecr.io/courses-api:v2.0.0
```

### Traffic Splitting (Canary Deployment)

```bash
# Split traffic between revisions
az containerapp ingress traffic set \
    --name courses-api \
    --resource-group rg-courses-portal \
    --revision-weight latest=90 courses-api--v1=10
```

### Blue/Green Deployment

```bash
# Create new revision (green)
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --image coursetutorials.azurecr.io/courses-api:v2.0.0 \
    --revision-suffix green

# Test green revision
curl https://courses-api.green.env-courses-portal.eastus.azurecontainerapps.io/health

# Switch 100% traffic to green
az containerapp ingress traffic set \
    --name courses-api \
    --resource-group rg-courses-portal \
    --revision-weight courses-api--green=100

# Deactivate old revision (blue)
az containerapp revision deactivate \
    --name courses-api--blue \
    --resource-group rg-courses-portal
```

---

## Monitoring and Logging

### View Container Logs

```bash
# Stream logs from container app
az containerapp logs show \
    --name courses-api \
    --resource-group rg-courses-portal \
    --tail 100

# Follow logs in real-time
az containerapp logs show \
    --name courses-api \
    --resource-group rg-courses-portal \
    --follow
```

### Custom Metrics for Node.js

```javascript
// middleware/metrics.js
const prometheus = require('prom-client');
const express = require('express');

// Create metrics
const requestCount = new prometheus.Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'route', 'status']
});

const requestDuration = new prometheus.Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'route'],
  buckets: [0.1, 0.3, 0.5, 1, 2, 5]
});

// Middleware to collect metrics
const metricsMiddleware = (req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    
    requestCount.labels(req.method, req.route?.path || req.path, res.statusCode).inc();
    requestDuration.labels(req.method, req.route?.path || req.path).observe(duration);
  });
  
  next();
};

// Metrics endpoint
const metricsEndpoint = (req, res) => {
  res.set('Content-Type', prometheus.register.contentType);
  res.end(prometheus.register.metrics());
};

module.exports = { metricsMiddleware, metricsEndpoint };
```

---

## Cost Optimization

### Scale to Zero Configuration

```bash
# Configure scale to zero (default after 30 minutes idle)
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --min-replicas 0 \
    --max-replicas 10

# Scale to zero faster
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --scale-rule-idle-timeout 300  # 5 minutes
```

### Resource Optimization

```bash
# Right-size CPU and memory based on usage
az containerapp update \
    --name courses-api \
    --resource-group rg-courses-portal \
    --cpu 0.25 \
    --memory 0.5Gi

# Monitor actual usage
az containerapp show \
    --name courses-api \
    --resource-group rg-courses-portal \
    --query properties.template.containers[0].resources
```

### Cost Breakdown (Estimated)

| Component | SKU | Estimated Monthly Cost |
|-----------|-----|----------------------|
| **Container App (idle)** | 0 vCPU, 0 memory | $0 |
| **Container App (active)** | 0.5 vCPU, 1GB memory | ~$15-30 |
| **Azure Cosmos DB** | Serverless | ~$10-50 |
| **Azure Redis Cache** | Basic (C0) | ~$15 |
| **Log Analytics** | 5GB/day | ~$60 |
| **Application Insights** | 5GB/day | ~$30 |
| **Total (active)** | | **~$150-200/mo** |
| **Total (idle)** | | **~$100-120/mo** |

---

## Troubleshooting

### Issue 1: Container Fails to Start

**Error:** `CrashLoopBackOff` in Container App

**Solution:**
```bash
# Check logs
az containerapp logs show --name courses-api --resource-group rg-courses-portal --tail 50

# Verify health check
az containerapp show --name courses-api --resource-group rg-courses-portal --query properties.template.containers[0].probes

# Test locally
docker run -p 3000:3000 coursetutorials.azurecr.io/courses-api:latest
```

### Issue 2: Scaling Not Working

**Error:** `Scale rule not triggering`

**Solution:**
```bash
# Check scale rules
az containerapp show --name courses-api --resource-group rg-courses-portal --query properties.template.scale

# Verify KEDA is enabled
az containerapp env show --name env-courses-portal --resource-group rg-courses-portal --query properties.kedaConfiguration

# Test with load
hey -z 30s -c 10 https://courses-api.eastus.azurecontainerapps.io/health
```

### Issue 3: Cold Start Latency

**Problem:** First request after scale-to-zero takes 5-10 seconds

**Solution:**
```javascript
// Add warm-up endpoint for monitoring
app.on('listening', async () => {
  // Pre-load dependencies
  await mongoose.connection.db.admin().ping();
  // Warm up any other connections
  console.log('Application warmed up');
});
```

---

## Conclusion: The Serverless Node.js Future

Azure Container Apps represents the ideal deployment target for Node.js Express applications, offering:

- **True serverless** – Scale to zero when idle, pay only for what you use
- **Container-native** – Bring any container, any framework, any dependencies
- **Integrated Azure services** – Native connections to Cosmos DB, Redis, and Application Insights
- **Simplified operations** – No Kubernetes clusters to manage, no virtual machines to patch
- **Production-ready** – Built-in health checks, traffic splitting, and revision management

For the AI Powered Video Tutorial Portal, Azure Container Apps delivers the perfect balance of flexibility and operational simplicity—allowing the Node.js team to focus on building features rather than managing infrastructure.

---

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure *(This story)*

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## What's Next?

Over the coming weeks, each approach in this Node.js series will be explored in exhaustive detail. We'll examine real-world Azure deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first Express.js application or an enterprise migrating Node.js workloads to Azure Kubernetes Service, you'll find practical guidance tailored to your infrastructure requirements.

Azure Container Apps represents the sweet spot in the Node.js deployment spectrum—offering serverless simplicity with container flexibility. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from rapid prototyping with VS Code Dev Containers to mission-critical production deployments on Azure Kubernetes Service.

**Coming next in the series:**
**💻 Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production