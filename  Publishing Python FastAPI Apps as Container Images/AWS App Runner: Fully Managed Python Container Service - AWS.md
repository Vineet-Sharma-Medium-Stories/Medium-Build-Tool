# AWS App Runner: Fully Managed Python Container Service - AWS

## Deploying FastAPI Applications with Zero Infrastructure Management

### Introduction: The Simplicity of Fully Managed Python Deployments on AWS

In the [previous installment](#) of this AWS Python series, we explored GitHub Actions for CI/CD—the automation backbone that enables teams to ship FastAPI applications faster and safer. While CI/CD automates the deployment process, a fundamental question remains: **how do you run your containerized Python applications without managing servers, clusters, or even containers?**

Enter **AWS App Runner**—a fully managed container application service that eliminates infrastructure management entirely. For the **AI Powered Video Tutorial Portal**—a FastAPI application with MongoDB integration, JWT authentication, and API key management—AWS App Runner provides the simplest possible deployment experience on AWS: you provide the code or container image, and App Runner handles everything else—load balancing, auto-scaling, SSL certificates, and security updates.

This final installment explores the complete workflow for deploying FastAPI applications to AWS App Runner. We'll master service creation, auto-scaling configuration, environment management, and integration with AWS services—all without touching a single EC2 instance, ECS cluster, or Kubernetes node.

```mermaid
graph TD
    subgraph "Developer Workflow"
        A[FastAPI Code] --> B[GitHub Repository]
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

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management *(This story)*

---

## Understanding AWS App Runner

### What Is AWS App Runner?

AWS App Runner is a fully managed container application service that makes it easy to build, deploy, and scale containerized web applications and APIs. Unlike ECS or EKS, App Runner requires no infrastructure management:

| Feature | Description | Benefit for FastAPI |
|---------|-------------|---------------------|
| **Zero Infrastructure** | No servers, clusters, or containers to manage | Focus on code, not ops |
| **Automatic Scaling** | Scales based on traffic patterns | Handle traffic spikes automatically |
| **Built-in Load Balancing** | Automatic distribution across instances | No ALB to configure |
| **Automatic SSL/TLS** | Free certificates for custom domains | Secure HTTPS out of the box |
| **Source Code Integration** | Deploy directly from GitHub or ECR | Push to deploy |
| **Pay-per-use Pricing** | Pay only for vCPU and memory used | Cost-effective for variable workloads |

### App Runner Architecture for FastAPI

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

## Deploying FastAPI from Source Code

### Step 1: Prepare FastAPI Application

```python
# server.py
from fastapi import FastAPI
import os

app = FastAPI(title="Courses Portal API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Courses Portal API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "courses-api"}

@app.get("/ready")
async def ready():
    # Check database connection, etc.
    return {"status": "ready"}
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
runtime: python3
build:
  commands:
    - pip install -r requirements.txt
run:
  command: uvicorn server:app --host 0.0.0.0 --port 8000
  network:
    port: 8000
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
            "RepositoryUrl": "https://github.com/courses-portal/courses-portal-api",
            "SourceCodeVersion": {
                "Type": "BRANCH",
                "Value": "main"
            },
            "CodeConfiguration": {
                "ConfigurationSource": "API",
                "CodeConfigurationValues": {
                    "Runtime": "PYTHON_3",
                    "BuildCommand": "pip install -r requirements.txt",
                    "StartCommand": "uvicorn server:app --host 0.0.0.0 --port 8000",
                    "Port": "8000",
                    "RuntimeEnvironmentVariables": [
                        {"Name": "ASPNETCORE_ENVIRONMENT", "Value": "Production"},
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
                "Port": "8000",
                "RuntimeEnvironmentVariables": [
                    {"Name": "ASPNETCORE_ENVIRONMENT", "Value": "Production"},
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

## FastAPI Configuration for App Runner

### Health Check Endpoints

```python
# server.py
import os
import time
from fastapi import FastAPI, Response
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_environment: str = os.getenv("ASPNETCORE_ENVIRONMENT", "Development")
    mongodb_uri: str = os.getenv("MONGODB_URI", "")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "dev-secret")
    
    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(title="Courses Portal API")

@app.get("/health")
async def health():
    """Liveness probe - checks if app is running"""
    return {
        "status": "healthy",
        "service": "courses-api",
        "version": "1.0.0",
        "environment": settings.app_environment
    }

@app.get("/ready")
async def ready():
    """Readiness probe - checks if app is ready to serve traffic"""
    status = "ready"
    checks = []
    
    # Check database connection if configured
    if settings.mongodb_uri:
        try:
            # Database connection check
            checks.append({"component": "database", "status": "connected"})
        except Exception as e:
            status = "not ready"
            checks.append({"component": "database", "status": "disconnected", "error": str(e)})
    
    # Check JWT secret
    if not settings.jwt_secret_key or settings.jwt_secret_key == "dev-secret":
        checks.append({"component": "jwt", "status": "warning", "message": "Using default secret"})
    
    return {
        "status": status,
        "checks": checks,
        "environment": settings.app_environment
    }, 200 if status == "ready" else 503
```

### Environment Configuration

```python
# config.py
import os
import boto3
import json
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Runner injects environment variables
    app_environment: str = os.getenv("ASPNETCORE_ENVIRONMENT", "Development")
    port: int = int(os.getenv("PORT", "8000"))
    
    # Secrets from AWS Secrets Manager
    mongodb_uri: str = os.getenv("MONGODB_URI", "")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "")
    redis_uri: str = os.getenv("REDIS_URI", "")
    
    # Feature flags
    api_key_enabled: bool = os.getenv("API_KEY_ENABLED", "true").lower() == "true"
    continue_watching_enabled: bool = True
    bookmarks_enabled: bool = True
    
    # App Runner specific
    app_runner_instance_id: str = os.getenv("AWS_APPRUNNER_INSTANCE_ID", "unknown")
    
    def get_secret(self, secret_name: str) -> str:
        """Retrieve secret from AWS Secrets Manager (for advanced cases)"""
        if os.getenv("AWS_EXECUTION_ENV") == "AWS_AppRunner":
            client = boto3.client("secretsmanager", region_name=os.getenv("AWS_REGION", "us-east-1"))
            try:
                response = client.get_secret_value(SecretId=secret_name)
                secret = json.loads(response["SecretString"])
                return list(secret.values())[0]
            except Exception:
                pass
        return os.getenv(secret_name.replace("/", "_").upper(), "")

settings = Settings()
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
                "Port": "8000",
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
                "Port": "8000"
              }
            }
          }'
```

---

## Monitoring and Observability

### CloudWatch Logs

```python
# Configure logging for CloudWatch
import logging
import os

# App Runner automatically streams logs to CloudWatch
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} "
        f"duration={duration:.3f}s"
    )
    
    return response
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

```python
# Add X-Ray tracing
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.fastapi import XRayMiddleware

# Configure X-Ray
xray_recorder.configure(service="courses-api")

# Add middleware
app.add_middleware(XRayMiddleware, xray_recorder=xray_recorder)

# Create custom segments
@xray_recorder.capture('MongoDB_Query')
async def get_courses():
    async with xray_recorder.in_subsegment('find_courses'):
        return await db.courses.find().to_list(100)
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
```python
# Ensure health endpoint returns 200
@app.get("/health")
async def health():
    return {"status": "healthy"}  # FastAPI returns 200 by default

# Check if dependencies are ready
@app.get("/ready")
async def ready():
    try:
        # Check database connection
        await db.client.admin.command('ping')
        return {"status": "ready"}
    except:
        return {"status": "not ready"}, 503
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
runtime: python3
build:
  commands:
    - pip install -r requirements.txt
    - pip install uvicorn
run:
  command: uvicorn server:app --host 0.0.0.0 --port 8000
  network:
    port: 8000
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
| **Idle (0 requests)** | $0 | $0 (scale to zero not available) |
| **Low Traffic (10 req/sec)** | ~$15/mo | ~$30/mo |
| **Medium Traffic (100 req/sec)** | ~$50/mo | ~$80/mo |
| **High Traffic (1000 req/sec)** | ~$300/mo | ~$400/mo |

---

## Conclusion: The Simplicity of AWS App Runner

AWS App Runner represents the simplest possible path to deploying FastAPI applications on AWS:

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

AWS App Runner is the perfect choice for teams that want to focus on building FastAPI applications without managing infrastructure—making it the ideal final installment in our comprehensive AWS Python containerization series.

---

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management *(This story)*

---

## Conclusion: The Complete AWS Python Containerization Journey

This concludes our comprehensive AWS Python series on containerizing FastAPI applications. We've covered the full spectrum of deployment approaches—from local development with VS Code Dev Containers to enterprise-scale orchestration on Amazon EKS, and from classic pip builds to modern UV workflows.

Each approach serves different use cases:

| Use Case | Recommended Approach |
|----------|---------------------|
| **Rapid prototyping** | AWS App Runner |
| **Microservices** | AWS Copilot + ECS |
| **Full control** | AWS CDK + ECS |
| **Kubernetes expertise** | Amazon EKS |
| **Lowest cost** | UV + ECS with Graviton |
| **Security compliance** | Tarball export + Amazon Inspector |
| **Local development** | VS Code Dev Containers |

**Thank you for reading this complete AWS Python series!** We've explored every major approach to building, testing, and deploying Python FastAPI container images on AWS. You're now equipped to choose the right tool for every scenario—from rapid prototyping to mission-critical production deployments. Happy containerizing on AWS! 🚀