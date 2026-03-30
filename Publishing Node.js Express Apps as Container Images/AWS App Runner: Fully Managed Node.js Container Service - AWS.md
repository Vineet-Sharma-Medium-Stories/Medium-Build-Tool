# AWS App Runner: Fully Managed Node.js Container Service - AWS

## Deploying Express.js Applications with Zero Infrastructure Management

### Introduction: The Simplicity of Fully Managed Node.js Deployments on AWS

In the [previous installment](#) of this AWS Node.js series, we explored GitHub Actions for CI/CD—the automation backbone that enables teams to ship Express.js applications faster and safer. While CI/CD automates the deployment process, a fundamental question remains: **how do you run your containerized Node.js applications without managing servers, clusters, or even containers?**

Enter **AWS App Runner**—a fully managed container application service that eliminates infrastructure management entirely. For the **AI Powered Video Tutorial Portal**—an Express.js application with MongoDB integration, Winston logging, and comprehensive REST API endpoints—AWS App Runner provides the simplest possible deployment experience on AWS: you provide the code or container image, and App Runner handles everything else—load balancing, auto-scaling, SSL certificates, and security updates.

This final installment explores the complete workflow for deploying Express.js applications to AWS App Runner. We'll master service creation, auto-scaling configuration, environment management, and integration with AWS services—all without touching a single EC2 instance, ECS cluster, or Kubernetes node.

```mermaid
graph TD
    subgraph "Developer Workflow"
        A[Node.js Express Code] --> B[GitHub Repository]
        B --> C[App Runner Service]
    end
    
    subgraph "AWS App Runner (Fully Managed)"
        C --> D[Automatic Build]
        C --> E[Container Deployment]
        C --> F[Auto Scaling]
        C --> G[Load Balancing]
        C --> H[SSL/TLS Certificates]
    end
    
    subgraph "AWS Services"
        C --> I[Amazon ECR]
        C --> J[Secrets Manager]
        C --> K[CloudWatch Logs]
    end
    
    style C fill:#ff9900,color:#fff
    style F fill:#48bb78,color:#fff
```

### Stories at a Glance

**Complete AWS Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach - AWS** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Amazon ECR

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management - AWS** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance on AWS Graviton

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers - AWS** – Leveraging pnpm's content-addressable storage for faster installs and smaller images on Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying Express.js applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent Node.js development environments that mirror AWS production

- 🏗️ **6. AWS CDK with TypeScript: Infrastructure as Code for Containers - AWS** – Defining Express.js infrastructure with TypeScript CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Node.js Microservices at Scale - AWS** – Deploying Express.js applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Node.js - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Node.js Container Service - AWS** – Deploying Express.js applications to AWS App Runner with zero infrastructure management *(This story)*

---

## Understanding AWS App Runner

### What Is AWS App Runner?

AWS App Runner is a fully managed container application service that makes it easy to build, deploy, and scale containerized web applications and APIs. Unlike ECS or EKS, App Runner requires no infrastructure management:

| Feature | Description | Benefit for Express.js |
|---------|-------------|----------------------|
| **Zero Infrastructure** | No servers, clusters, or containers to manage | Focus on code, not ops |
| **Automatic Scaling** | Scales based on traffic patterns | Handle traffic spikes automatically |
| **Built-in Load Balancing** | Automatic distribution across instances | No ALB to configure |
| **Automatic SSL/TLS** | Free certificates for custom domains | Secure HTTPS out of the box |
| **Source Code Integration** | Deploy directly from GitHub or ECR | Push to deploy |
| **Pay-per-use Pricing** | Pay only for vCPU and memory used | Cost-effective for variable workloads |

### App Runner Architecture for Express.js

```mermaid
graph LR
    subgraph "App Runner Service"
        A[Source<br/>GitHub/ECR] --> B[Build<br/>Automatic]
        B --> C[Deploy<br/>Rolling Update]
        C --> D[Auto Scaling<br/>Configurable]
        D --> E[Load Balancer<br/>Built-in]
    end
    
    subgraph "Runtime"
        E --> F[App Runner Instance 1]
        E --> G[App Runner Instance 2]
        E --> H[App Runner Instance N]
    end
    
    subgraph "Monitoring"
        F --> I[CloudWatch Logs]
        G --> I
        H --> I
    end
```

---

## Prerequisites

### Install AWS CLI

```bash
# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Verify installation
aws --version
# aws-cli/2.15.0 Python/3.11.6 Linux/5.10.0 source/x86_64.ubuntu.20

# Configure credentials
aws configure
AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name: us-east-1
Default output format: json
```

---

## Deploying Express.js from Source Code

### Step 1: Prepare Express.js Application

```javascript
// server.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Courses Portal API', status: 'running' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', service: 'courses-api' });
});

app.get('/ready', async (req, res) => {
  // Check database connection, etc.
  res.json({ status: 'ready' });
});

module.exports = app;
```

### Step 2: Create App Runner Service via Console

1. **Navigate to AWS App Runner Console**
2. **Click "Create Service"**
3. **Select Source: GitHub**
4. **Connect GitHub repository**
5. **Configure build settings:**

```yaml
# apprunner.yaml - Optional configuration file
version: 1.0
runtime: nodejs20
build:
  commands:
    - npm install
run:
  command: node server.js
  network:
    port: 3000
```

### Step 3: Create App Runner Service via CLI

```bash
# Create App Runner service from source
aws apprunner create-service \
    --service-name courses-api \
    --source-configuration '{
        "AuthenticationConfiguration": {
            "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/github/xxxxx"
        },
        "CodeRepository": {
            "RepositoryUrl": "https://github.com/courses-portal/courses-portal-api-nodejs",
            "SourceCodeVersion": {
                "Type": "BRANCH",
                "Value": "main"
            },
            "CodeConfiguration": {
                "ConfigurationSource": "API",
                "CodeConfigurationValues": {
                    "Runtime": "NODEJS_20",
                    "BuildCommand": "npm install",
                    "StartCommand": "node server.js",
                    "Port": "3000",
                    "RuntimeEnvironmentVariables": [
                        {"Name": "NODE_ENV", "Value": "production"},
                        {"Name": "API_KEY_ENABLED", "Value": "true"}
                    ]
                }
            }
        }
    }' \
    --instance-configuration '{
        "Cpu": "1 vCPU",
        "Memory": "2 GB"
    }' \
    --health-check-configuration '{
        "Protocol": "HTTP",
        "Path": "/health",
        "Interval": 30,
        "Timeout": 5,
        "HealthyThreshold": 2,
        "UnhealthyThreshold": 3
    }' \
    --auto-scaling-configuration-arn "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/default/1/xxxxx"
```

---

## Deploying from Amazon ECR

### Step 1: Build and Push to ECR

```bash
# Build Docker image
docker build -t courses-api:latest -f Dockerfile .

# Login to ECR
aws ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com

# Create ECR repository
aws ecr create-repository --repository-name courses-api

# Tag and push
docker tag courses-api:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api:latest
```

### Step 2: Create App Runner Service from ECR

```bash
aws apprunner create-service \
    --service-name courses-api-ecr \
    --source-configuration '{
        "ImageRepository": {
            "ImageIdentifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api:latest",
            "ImageConfiguration": {
                "Port": "3000",
                "RuntimeEnvironmentVariables": [
                    {"Name": "NODE_ENV", "Value": "production"},
                    {"Name": "API_KEY_ENABLED", "Value": "true"}
                ]
            }
        }
    }' \
    --instance-configuration '{
        "Cpu": "1 vCPU",
        "Memory": "2 GB"
    }' \
    --auto-scaling-configuration-arn "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/default/1/xxxxx"
```

---

## Express.js Configuration for App Runner

### Health Check Endpoints

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    service: 'courses-api',
    version: process.env.npm_package_version || '1.0.0',
    environment: process.env.NODE_ENV || 'development'
  });
});

app.get('/ready', async (req, res) => {
  const checks = { database: false, server: true };
  
  // Check database connection if configured
  if (process.env.MONGODB_URI) {
    try {
      await mongoose.connection.db.admin().ping();
      checks.database = true;
    } catch (error) {
      return res.status(503).json({
        status: 'not ready',
        checks,
        error: error.message
      });
    }
  }
  
  res.status(200).json({ status: 'ready', checks });
});
```

### Environment Configuration

```javascript
// config.js
module.exports = {
  // App Runner injects environment variables
  nodeEnv: process.env.NODE_ENV || 'development',
  port: parseInt(process.env.PORT || '3000', 10),
  
  // Secrets from AWS Secrets Manager
  mongodbUri: process.env.MONGODB_URI || '',
  jwtSecretKey: process.env.JWT_SECRET_KEY || '',
  redisUri: process.env.REDIS_URI || '',
  
  // Feature flags
  apiKeyEnabled: process.env.API_KEY_ENABLED === 'true',
  continueWatchingEnabled: true,
  bookmarksEnabled: true,
  
  // App Runner specific
  appRunnerInstanceId: process.env.AWS_APPRUNNER_INSTANCE_ID || 'unknown'
};
```

---

## Auto-Scaling Configuration

### Default Auto-Scaling

```json
{
  "AutoScalingConfiguration": {
    "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/courses-api-scaling/1/xxxxx",
    "AutoScalingConfigurationName": "courses-api-scaling",
    "AutoScalingConfigurationRevision": 1,
    "MinSize": 1,
    "MaxSize": 10,
    "CreatedAt": "2024-01-15T10:00:00Z",
    "DeletedAt": null,
    "Latest": true
  }
}
```

### Custom Auto-Scaling Configuration

```bash
# Create custom auto-scaling configuration
aws apprunner create-auto-scaling-configuration \
    --auto-scaling-configuration-name courses-api-scaling \
    --min-size 2 \
    --max-size 20 \
    --max-concurrency 100

# Update service with custom auto-scaling
aws apprunner update-service \
    --service-arn arn:aws:apprunner:us-east-1:123456789012:service/courses-api/xxxxx \
    --auto-scaling-configuration-arn arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/courses-api-scaling/1/xxxxx
```

---

## Custom Domains and SSL

### Add Custom Domain

```bash
# Associate custom domain
aws apprunner associate-custom-domain \
    --service-arn arn:aws:apprunner:us-east-1:123456789012:service/courses-api/xxxxx \
    --domain-name api.coursesportal.com

# Verify DNS records
aws apprunner describe-custom-domains \
    --service-arn arn:aws:apprunner:us-east-1:123456789012:service/courses-api/xxxxx
```

### DNS Configuration

```bash
# Add CNAME record to Route 53
aws route53 change-resource-record-sets \
    --hosted-zone-id Z1234567890 \
    --change-batch '{
        "Changes": [{
            "Action": "CREATE",
            "ResourceRecordSet": {
                "Name": "api.coursesportal.com",
                "Type": "CNAME",
                "TTL": 300,
                "ResourceRecords": [{
                    "Value": "xxxxx.us-east-1.awsapprunner.com"
                }]
            }
        }]
    }'
```

---

## Secrets Management

### Store Secrets in AWS Secrets Manager

```bash
# Create secrets
aws secretsmanager create-secret \
    --name courses-portal/jwt-secret \
    --secret-string '{"secret":"your-super-secret-jwt-key"}'

aws secretsmanager create-secret \
    --name courses-portal/mongodb-uri \
    --secret-string '{"uri":"mongodb://username:password@host:27017/courses_portal?ssl=true"}'
```

### Configure App Runner to Use Secrets

```bash
# Create service with secrets
aws apprunner create-service \
    --service-name courses-api \
    --source-configuration '{
        "ImageRepository": {
            "ImageIdentifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api:latest",
            "ImageConfiguration": {
                "Port": "3000",
                "RuntimeEnvironmentSecrets": [
                    {
                        "Name": "JWT_SECRET_KEY",
                        "Value": "arn:aws:secretsmanager:us-east-1:123456789012:secret:courses-portal/jwt-secret-xxxxx"
                    },
                    {
                        "Name": "MONGODB_URI",
                        "Value": "arn:aws:secretsmanager:us-east-1:123456789012:secret:courses-portal/mongodb-uri-xxxxx"
                    }
                ]
            }
        }
    }' \
    --instance-configuration '{
        "Cpu": "1 vCPU",
        "Memory": "2 GB"
    }'
```

---

## CI/CD with GitHub Actions

### GitHub Actions Workflow for App Runner

```yaml
# .github/workflows/apprunner-deploy.yml
name: Deploy to AWS App Runner

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        role-to-assume: arn:aws:iam::123456789012:role/github-actions-role
        aws-region: us-east-1
    
    - name: Login to Amazon ECR
      uses: aws-actions/amazon-ecr-login@v1
    
    - name: Build and push to ECR
      run: |
        docker build -t courses-api:${{ github.sha }} .
        docker tag courses-api:${{ github.sha }} ${{ secrets.ECR_REGISTRY }}/courses-api:${{ github.sha }}
        docker push ${{ secrets.ECR_REGISTRY }}/courses-api:${{ github.sha }}
    
    - name: Update App Runner service
      run: |
        aws apprunner update-service \
          --service-arn arn:aws:apprunner:us-east-1:123456789012:service/courses-api/xxxxx \
          --source-configuration '{
            "ImageRepository": {
              "ImageIdentifier": "${{ secrets.ECR_REGISTRY }}/courses-api:${{ github.sha }}",
              "ImageConfiguration": {
                "Port": "3000"
              }
            }
          }'
```

---

## Monitoring and Observability

### CloudWatch Logs

```javascript
// Configure logging for CloudWatch
const winston = require('winston');

// App Runner automatically streams logs to CloudWatch
const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    })
  ]
});

// Middleware for request logging
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    logger.info(`${req.method} ${req.url} ${res.statusCode} ${duration}ms`);
  });
  next();
});
```

### Access Logs

```bash
# View logs in CloudWatch
aws logs get-log-events \
    --log-group-name /aws/apprunner/courses-api/application \
    --log-stream-name $(aws logs describe-log-streams \
        --log-group-name /aws/apprunner/courses-api/application \
        --order-by LastEventTime \
        --descending \
        --limit 1 \
        --query 'logStreams[0].logStreamName' \
        --output text) \
    --limit 50
```

### X-Ray Tracing

```javascript
// Add X-Ray tracing
const AWSXRay = require('aws-xray-sdk');

// Configure X-Ray
app.use(AWSXRay.express.openSegment('courses-api'));

// Capture AWS SDK calls
const AWS = AWSXRay.captureAWS(require('aws-sdk'));

// Custom segments
app.get('/courses/:id', async (req, res) => {
  const segment = AWSXRay.getSegment();
  const subsegment = segment.addNewSubsegment('getCourseFromDB');
  
  try {
    const course = await db.collection('courses').findOne({ _id: req.params.id });
    subsegment.close();
    res.json(course);
  } catch (err) {
    subsegment.close(err);
    throw err;
  }
});

app.use(AWSXRay.express.closeSegment());
```

---

## Troubleshooting App Runner

### Issue 1: Service Fails to Start

**Error:** `Service is in FAILED state`

**Solution:**
```bash
# Check service logs
aws apprunner describe-service --service-arn arn:aws:apprunner:us-east-1:123456789012:service/courses-api/xxxxx

# View operation history
aws apprunner list-operations --service-arn arn:aws:apprunner:us-east-1:123456789012:service/courses-api/xxxxx
```

### Issue 2: Health Check Failing

**Error:** `Health check failed with status code 503`

**Solution:**
```javascript
// Ensure health endpoint returns 200
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

// Check if dependencies are ready
app.get('/ready', async (req, res) => {
  try {
    // Check database connection
    await mongoose.connection.db.admin().ping();
    res.status(200).json({ status: 'ready' });
  } catch (err) {
    res.status(503).json({ status: 'not ready' });
  }
});
```

### Issue 3: Secrets Not Found

**Error:** `Secret not found: arn:aws:secretsmanager:...`

**Solution:**
```bash
# Verify secret exists
aws secretsmanager get-secret-value \
    --secret-id courses-portal/jwt-secret

# Check IAM role permissions
aws iam simulate-principal-policy \
    --policy-source-arn arn:aws:iam::123456789012:role/AppRunnerInstanceRole \
    --action-names secretsmanager:GetSecretValue
```

### Issue 4: Build Failure from Source

**Error:** `Build failed: Command failed`

**Solution:**
```yaml
# apprunner.yaml - Specify build commands
version: 1.0
runtime: nodejs20
build:
  commands:
    - npm install
    - npm run build
run:
  command: node server.js
  network:
    port: 3000
```

---

## Performance Metrics

| Metric | App Runner | ECS Fargate | EKS |
|--------|------------|-------------|-----|
| **Time to First Deployment** | 5-10 minutes | 15-30 minutes | 30-60 minutes |
| **Infrastructure Management** | Zero | Minimal | Full control |
| **Auto-Scaling** | Automatic | Configurable | Configurable |
| **Custom Domains** | Built-in | Via ALB | Via Ingress |
| **Cost** | Pay per vCPU/memory | Pay per task | Node-based |
| **Learning Curve** | Minimal | Moderate | Steep |

### Cost Comparison

| Workload | App Runner | ECS Fargate |
|----------|------------|-------------|
| **Idle (0 requests)** | $0 (scale to zero) | $0 (scale to zero not available) |
| **Low Traffic (10 req/sec)** | ~$15/mo | ~$30/mo |
| **Medium Traffic (100 req/sec)** | ~$50/mo | ~$80/mo |
| **High Traffic (1000 req/sec)** | ~$300/mo | ~$400/mo |

---

## Conclusion: The Simplicity of AWS App Runner for Node.js

AWS App Runner represents the simplest possible path to deploying Node.js Express applications on AWS:

- **Zero infrastructure management** – No servers, clusters, or containers to manage
- **Automatic everything** – Builds, deployments, scaling, SSL certificates
- **Pay-per-use pricing** – Cost-effective for variable workloads
- **Fast iteration** – Code to production in minutes
- **AWS service integration** – Secrets Manager, CloudWatch, X-Ray

For the AI Powered Video Tutorial Portal, AWS App Runner enables:

- **Rapid prototyping** – Deploy changes in minutes
- **Production-ready defaults** – Health checks, auto-scaling, SSL
- **Focus on code** – No infrastructure to maintain
- **Cost optimization** – Scale to zero in development
- **Simple CI/CD** – GitHub integration with automatic deployments

AWS App Runner is the perfect choice for teams that want to focus on building Express.js applications without managing infrastructure—making it the ideal final installment in our comprehensive AWS Node.js containerization series.

---

### Stories at a Glance

**Complete AWS Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach - AWS** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Amazon ECR

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management - AWS** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance on AWS Graviton

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers - AWS** – Leveraging pnpm's content-addressable storage for faster installs and smaller images on Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying Express.js applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent Node.js development environments that mirror AWS production

- 🏗️ **6. AWS CDK with TypeScript: Infrastructure as Code for Containers - AWS** – Defining Express.js infrastructure with TypeScript CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Node.js Microservices at Scale - AWS** – Deploying Express.js applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Node.js - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Node.js Container Service - AWS** – Deploying Express.js applications to AWS App Runner with zero infrastructure management *(This story)*

---

## Conclusion: The Complete AWS Node.js Containerization Journey

This concludes our comprehensive AWS Node.js series on containerizing Express.js applications. We've covered the full spectrum of deployment approaches—from local development with VS Code Dev Containers to enterprise-scale orchestration on Amazon EKS, and from classic npm builds to modern pnpm workflows.

Each approach serves different use cases:

| Use Case | Recommended Approach |
|----------|---------------------|
| **Rapid prototyping** | AWS App Runner |
| **Microservices** | AWS Copilot + ECS |
| **Full control** | AWS CDK + ECS |
| **Kubernetes expertise** | Amazon EKS |
| **Lowest cost** | pnpm + ECS with Graviton |
| **Security compliance** | Tarball export + Amazon Inspector |
| **Local development** | VS Code Dev Containers |

**Thank you for reading this complete AWS Node.js series!** We've explored every major approach to building, testing, and deploying Node.js Express container images on AWS. You're now equipped to choose the right tool for every scenario—from rapid prototyping to mission-critical production deployments. Happy containerizing on AWS! 🚀