Here is the **AWS Bonus Story** – a complete, detailed deployment guide for AWS, following the exact same structure as the Azure bonus story.

---

# Zero-Cost AI: Deploy from Laptop to AWS (Bonus)

## A Complete Handbook for Deploying Your Zero-Cost AI Stack to AWS ECS, S3 for Model Storage, and EC2 with GPU for High-Performance Inference — with CloudWatch Observability and Auto-Scaling

---

## Introduction

You have built a complete zero-cost AI stack that runs on your laptop and deploys to HuggingFace Spaces for free. You have seen how to deploy to Azure. Now it's time for AWS – the most comprehensive cloud platform with the broadest selection of GPU instances and global reach.

AWS offers capabilities that neither HuggingFace nor Azure can match: P4d instances with NVIDIA A100 GPUs (40GB HBM2), Inferentia chips for cost-effective inference, 24 regions globally, and services like SageMaker for ML orchestration.

The conventional approach would be to rewrite your application using AWS-specific SDKs, SageMaker endpoints, and proprietary APIs. This locks you in and takes weeks.

But this is the Zero-Cost AI handbook, and we don't do lock-in.

In this AWS bonus story, you will deploy your existing Docker container – the same one from the HuggingFace deployment – to AWS ECS (Elastic Container Service) with zero code changes. You will add S3 for model caching and user data. You will optionally add EC2 GPU instances (G4dn with NVIDIA T4 or P4d with A100) for 10-100x faster inference. You will optionally integrate Amazon Bedrock for foundation model fallback. And you will set up CloudWatch for observability with auto-scaling based on demand.

No rewrite. No lock-in. Just the same portable stack running on AWS's global infrastructure.

---

## Takeaway from the Cloud Portability Story

This bonus story builds directly on **Zero-Cost AI: Scaling AI Deployments to Azure, AWS & GCP Without Rewrites**. That story established:

- **Core AI logic is portable.** Your LangGraph agent, RAG pipeline, MCP tools, and prompt engineering run unchanged on any cloud.

- **Docker containers are the portable unit.** The same `Dockerfile` that deployed to HuggingFace deploys to AWS ECS.

- **Storage requires cloud-specific adaptation.** AWS uses S3 for object storage and EBS for block storage.

- **Authentication is cloud-specific.** AWS uses IAM roles and policies.

With these takeaways in place, you are ready to deploy to AWS.

---

## Stories in This Series (Updated with AWS Bonus)

**1.** Zero-Cost AI: The $0 Stack That Actually Works  
**2.** Zero-Cost AI: Frontend on Your Laptop, Deployed for Free  
**3.** Zero-Cost AI: Agent Orchestration on a Laptop Without Paying  
**4.** Zero-Cost AI: Replacing GPT-4 with Llama 3.3 70B Locally  
**5.** Zero-Cost AI: Tool Use on a Laptop via Model Context Protocol  
**6.** Zero-Cost AI: Code Agents on a Laptop Without Subscriptions  
**7.** Zero-Cost AI: Deploy from Laptop to HuggingFace for Free  
**8.** Zero-Cost AI: Observability on a Laptop Without Datadog  
**9.** Zero-Cost AI: RAG Pipeline on a Laptop for Free  
**10.** Zero-Cost AI: Data Layer on a Laptop Without Cloud Spend  
**11.** Zero-Cost AI: Scaling AI Deployments to Azure, AWS & GCP Without Rewrites  

**📎 (Bonus)** Zero-Cost AI: Deploy from Laptop to Azure  
*Step-by-step deployment to Azure Container Instances, Azure Blob Storage, and Azure OpenAI (optional).*

**📎 (Bonus)** Zero-Cost AI: Deploy from Laptop to AWS *(you are here)*  
*Step-by-step deployment to AWS ECS, S3 for model storage, and EC2 with GPU for high-performance inference.*

**📎 (Bonus)** Zero-Cost AI: Deploy from Laptop to GCP  
*Step-by-step deployment to Google Cloud Run, Cloud Storage, and GKE for Kubernetes-based scaling.*

---

## AWS Deployment Architecture

The diagram below shows how your zero-cost AI stack deploys to AWS.

```mermaid
flowchart TB
    User[👤 User Browser] --> Frontend[🖥️ Frontend\nVercel / CloudFront]
    Frontend --> ALB[⚖️ Application Load Balancer]
    ALB --> ECS[🐳 ECS Fargate\nYour Docker container\nServerless containers]
    
    ECS --> Ollama[🤖 Ollama LLM\nLlama 3.3 70B\nInside container]
    
    ECS --> S3[📦 S3 Bucket\nModel cache (8GB)\nUser uploads\nLogs\nCheckpoints]
    
    ECS --> EFS[📁 EFS\nPersistent storage\nSQLite database\nRAG vectors]
    
    ECS --> Bedrock[🔌 Optional: Amazon Bedrock\nClaude/GPT fallback\nWhen local model uncertain]
    
    ECS --> GPU[💪 Optional: EC2 GPU\nG4dn (T4) or P4d (A100)\nFor faster inference]
    
    ECS --> CW[📊 CloudWatch\nLogs | Metrics | Alerts\nX-Ray for tracing]
    
    style ECS fill:#ff9900,stroke:#cc7a00,stroke-width:3px,color:#000
    style S3 fill:#ff9900,stroke:#cc7a00,stroke-width:2px,color:#000
    style Bedrock fill:#ff9900,stroke:#cc7a00,stroke-width:2px,color:#000
    style GPU fill:#ff9900,stroke:#cc7a00,stroke-width:2px,color:#000
```

### AWS Services Used (Free Tier Available)

| Service | Purpose | Cost Estimate |
|---------|---------|---------------|
| **ECS Fargate** | Run your Docker container (serverless) | $0.04-0.50/hour (CPU) / $0.50-3.00/hour (GPU) |
| **S3** | Model cache, user uploads, logs | $0.023/GB-month (first 5GB free for 12 months) |
| **EFS** | Persistent SQLite, checkpoints | $0.30/GB-month |
| **EC2 GPU (G4dn)** | NVIDIA T4 GPU for faster inference | $0.526/hour (on-demand) |
| **EC2 GPU (P4d)** | NVIDIA A100 for maximum performance | $32.77/hour |
| **Amazon Bedrock** | Optional Claude/GPT fallback | Pay per token |
| **CloudWatch** | Logs, metrics, alarms | First 5GB logs free, 10 metrics free |
| **ECR** | Store Docker images | 0.5 GB-month free |

**Free tier:** 12 months free for EC2 t2.micro, 5GB S3, and 10 CloudWatch metrics.

---

## Step 1: Prepare Your Docker Container for AWS

Your existing Dockerfile from the HuggingFace deployment works on AWS with minor additions for S3 integration.

```dockerfile
# Dockerfile.aws
# Extended Dockerfile for AWS deployment

FROM ollama/ollama:0.5.1 as ollama-base
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    ca-certificates \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

# Install Ollama
COPY --from=ollama-base /usr/bin/ollama /usr/bin/ollama

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install boto3 aws-xray-sdk

# Copy application
COPY . .

# Create directories
RUN mkdir -p /root/.ollama /app/data /app/logs

# Copy AWS-specific entrypoint
COPY entrypoint_aws.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=180s --retries=3 \
    CMD curl -f http://localhost:11434/api/tags || exit 1

EXPOSE 11434 8000 7860

ENTRYPOINT ["/entrypoint.sh"]
```

### AWS-Specific Entrypoint Script

```bash
#!/bin/bash
# entrypoint_aws.sh
# Entrypoint with S3 integration

set -e

echo "🚀 Starting Zero-Cost AI Stack on AWS"
echo "======================================"

# Assume IAM role for S3 access (handled by ECS task role)
if [ -n "$S3_MODEL_BUCKET" ]; then
    echo "📦 Checking for model in S3 bucket: $S3_MODEL_BUCKET"
    
    # Check if model exists in S3
    if aws s3 ls "s3://$S3_MODEL_BUCKET/models/llama3.3-70b-q4_K_M/" --region "$AWS_REGION" 2>/dev/null; then
        echo "✅ Model found in S3, downloading..."
        aws s3 cp "s3://$S3_MODEL_BUCKET/models/llama3.3-70b-q4_K_M/" /root/.ollama/models/ --recursive
    else
        echo "⚠️ Model not in S3, will download from Ollama"
    fi
fi

# Start Ollama
echo "📡 Starting Ollama server..."
ollama serve &
OLLAMA_PID=$!

# Wait for Ollama
for i in {1..60}; do
    if curl -s http://localhost:11434/api/tags > /dev/null; then
        echo "✅ Ollama is ready"
        break
    fi
    echo "   Waiting... ($i/60)"
    sleep 2
done

# Pull model if not present
if ! ollama list | grep -q "llama3.3:70b-instruct-q4_K_M"; then
    echo "🦙 Pulling Llama 3.3 70B (first deployment, 10-15 minutes)..."
    ollama pull llama3.3:70b-instruct-q4_K_M
    
    # Upload to S3 for next deployment
    if [ -n "$S3_MODEL_BUCKET" ]; then
        echo "📤 Uploading model to S3 for caching..."
        aws s3 cp /root/.ollama/models/ "s3://$S3_MODEL_BUCKET/models/llama3.3-70b-q4_K_M/" --recursive
    fi
fi

# Mount EFS for persistent storage (mounted via ECS task definition)
if [ -d "/mnt/efs" ]; then
    echo "📁 EFS volume detected, linking to /app/data"
    ln -sf /mnt/efs /app/data
fi

# Start agent and frontend
python -m uvicorn agent_api:app --host 0.0.0.0 --port 8000 &
streamlit run app.py --server.port 7860 --server.address 0.0.0.0 &

echo "======================================"
echo "✅ All components started on AWS!"
echo "======================================"

wait $OLLAMA_PID
```

---

## Step 2: Create AWS Resources

### Option A: AWS CLI (Recommended)

```bash
# Configure AWS CLI (if not already done)
aws configure

# Set region
AWS_REGION="us-east-1"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Create S3 bucket for model storage (globally unique name)
BUCKET_NAME="zero-cost-ai-models-$(date +%s)"
aws s3 mb "s3://$BUCKET_NAME" --region $AWS_REGION

# Create ECR repository for Docker images
aws ecr create-repository \
    --repository-name zero-cost-ai \
    --region $AWS_REGION

# Get ECR login token and push image
aws ecr get-login-password --region $AWS_REGION | \
    docker login --username AWS --password-stdin "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

# Build and push Docker image
docker build -t zero-cost-ai -f Dockerfile.aws .
docker tag zero-cost-ai:latest "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/zero-cost-ai:latest"
docker push "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/zero-cost-ai:latest"

# Create EFS for persistent storage
aws efs create-file-system \
    --creation-token zero-cost-ai-efs \
    --performance-mode generalPurpose \
    --throughput-mode bursting \
    --region $AWS_REGION

# Get EFS ID (save for later)
EFS_ID=$(aws efs describe-file-systems \
    --creation-token zero-cost-ai-efs \
    --query 'FileSystems[0].FileSystemId' \
    --output text)

echo "EFS_ID=$EFS_ID"
echo "S3_BUCKET=$BUCKET_NAME"
```

### Option B: Terraform (Infrastructure as Code)

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# S3 Bucket for models
resource "aws_s3_bucket" "models" {
  bucket = "zero-cost-ai-models-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}

# ECR Repository
resource "aws_ecr_repository" "app" {
  name = "zero-cost-ai"
}

# EFS for persistent storage
resource "aws_efs_file_system" "data" {
  creation_token = "zero-cost-ai-efs"
  performance_mode = "generalPurpose"
  throughput_mode = "bursting"
}

# EFS Mount Target (in each subnet)
resource "aws_efs_mount_target" "data" {
  count = length(data.aws_subnets.default.ids)
  file_system_id = aws_efs_file_system.data.id
  subnet_id      = data.aws_subnets.default.ids[count.index]
  security_groups = [aws_security_group.efs.id]
}

# IAM Role for ECS Task
resource "aws_iam_role" "ecs_task" {
  name = "zero-cost-ai-ecs-task-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
    }]
  })
}

# IAM Policy for S3 access
resource "aws_iam_policy" "s3_access" {
  name = "zero-cost-ai-s3-access"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ]
      Resource = [
        aws_s3_bucket.models.arn,
        "${aws_s3_bucket.models.arn}/*"
      ]
    }]
  })
}

# Attach policy to role
resource "aws_iam_role_policy_attachment" "s3" {
  role       = aws_iam_role.ecs_task.name
  policy_arn = aws_iam_policy.s3_access.arn
}

# ECS Cluster
resource "aws_ecs_cluster" "main" {
  name = "zero-cost-ai-cluster"
}

# ECS Task Definition
resource "aws_ecs_task_definition" "app" {
  family                   = "zero-cost-ai"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 2048   # 2 vCPU
  memory                   = 16384  # 16 GB RAM
  execution_role_arn       = aws_iam_role.ecs_task.arn
  task_role_arn            = aws_iam_role.ecs_task.arn

  container_definitions = jsonencode([{
    name  = "zero-cost-ai"
    image = "${aws_ecr_repository.app.repository_url}:latest"
    portMappings = [
      { containerPort = 7860, protocol = "tcp" },
      { containerPort = 8000, protocol = "tcp" }
    ]
    environment = [
      { name = "LLM_MODEL", value = "llama3.3:70b-instruct-q4_K_M" },
      { name = "LOG_LEVEL", value = "INFO" },
      { name = "S3_MODEL_BUCKET", value = aws_s3_bucket.models.id },
      { name = "AWS_REGION", value = "us-east-1" }
    ]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        "awslogs-group"         = "/ecs/zero-cost-ai"
        "awslogs-region"        = "us-east-1"
        "awslogs-stream-prefix" = "ecs"
      }
    }
  }])
}

# CloudWatch Log Group
resource "aws_cloudwatch_log_group" "app" {
  name = "/ecs/zero-cost-ai"
  retention_in_days = 7
}

# Security Group
resource "aws_security_group" "app" {
  name        = "zero-cost-ai-sg"
  description = "Security group for Zero-Cost AI"

  ingress {
    from_port   = 7860
    to_port     = 7860
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ECS Service
resource "aws_ecs_service" "app" {
  name            = "zero-cost-ai-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = data.aws_subnets.default.ids
    security_groups  = [aws_security_group.app.id]
    assign_public_ip = true
  }
}

# Outputs
output "ecs_service_url" {
  value = aws_ecs_service.app.name
}

output "s3_bucket" {
  value = aws_s3_bucket.models.id
}
```

---

## Step 3: Deploy to AWS ECS Fargate

### CPU Deployment (Cost-Effective)

```bash
# Create ECS cluster
aws ecs create-cluster --cluster-name zero-cost-ai-cluster

# Register task definition (CPU optimized)
aws ecs register-task-definition \
    --family zero-cost-ai \
    --network-mode awsvpc \
    --requires-compatibilities FARGATE \
    --cpu "2048" \
    --memory "16384" \
    --execution-role-arn "arn:aws:iam::$ACCOUNT_ID:role/ecsTaskExecutionRole" \
    --task-role-arn "arn:aws:iam::$ACCOUNT_ID:role/zero-cost-ai-ecs-task-role" \
    --container-definitions "[{
        \"name\": \"zero-cost-ai\",
        \"image\": \"${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/zero-cost-ai:latest\",
        \"portMappings\": [
            {\"containerPort\": 7860, \"protocol\": \"tcp\"},
            {\"containerPort\": 8000, \"protocol\": \"tcp\"}
        ],
        \"environment\": [
            {\"name\": \"LLM_MODEL\", \"value\": \"llama3.3:70b-instruct-q4_K_M\"},
            {\"name\": \"S3_MODEL_BUCKET\", \"value\": \"$BUCKET_NAME\"},
            {\"name\": \"AWS_REGION\", \"value\": \"$AWS_REGION\"}
        ],
        \"logConfiguration\": {
            \"logDriver\": \"awslogs\",
            \"options\": {
                \"awslogs-group\": \"/ecs/zero-cost-ai\",
                \"awslogs-region\": \"$AWS_REGION\",
                \"awslogs-stream-prefix\": \"ecs\"
            }
        }
    }]"

# Create service
aws ecs create-service \
    --cluster zero-cost-ai-cluster \
    --service-name zero-cost-ai-service \
    --task-definition zero-cost-ai \
    --desired-count 1 \
    --launch-type FARGATE \
    --network-configuration "{
        \"awsvpcConfiguration\": {
            \"subnets\": [\"subnet-xxxxx\"],
            \"securityGroups\": [\"sg-xxxxx\"],
            \"assignPublicIp\": \"ENABLED\"
        }
    }"

# Get service status
aws ecs describe-services \
    --cluster zero-cost-ai-cluster \
    --services zero-cost-ai-service \
    --query 'services[0].status'
```

### GPU Deployment (EC2 with NVIDIA T4)

For GPU-accelerated inference, deploy to EC2 instead of Fargate.

```bash
# Request G4dn instance limit increase (if needed)
aws service-quotas request-service-quota-increase \
    --service-code ec2 \
    --quota-code L-12345678 \
    --desired-value 1

# Launch G4dn.xlarge instance with NVIDIA T4 GPU
aws ec2 run-instances \
    --image-id ami-0c55b159cbfafe1f0 \
    --instance-type g4dn.xlarge \
    --key-name your-key-pair \
    --security-group-ids sg-xxxxx \
    --subnet-id subnet-xxxxx \
    --user-data "file://gpu-startup-script.sh"

# GPU startup script (gpu-startup-script.sh)
cat > gpu-startup-script.sh << 'EOF'
#!/bin/bash
# Install NVIDIA drivers
sudo apt-get update
sudo apt-get install -y nvidia-driver-535

# Install Docker and NVIDIA container toolkit
curl -fsSL https://get.docker.com | sh
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# Pull and run your container with GPU
docker run -d \
    --gpus all \
    -p 7860:7860 \
    -p 8000:8000 \
    -e NVIDIA_VISIBLE_DEVICES=all \
    -e LLM_MODEL="llama3.3:70b-instruct-q4_K_M" \
    ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/zero-cost-ai:latest
EOF
```

---

## Step 4: Optional – Amazon Bedrock Fallback Integration

Add Amazon Bedrock (Claude 3.5 or Llama models) as a fallback when your local model is uncertain.

### Create Bedrock Access

```bash
# Request model access (one-time)
aws bedrock list-foundation-models --region us-east-1

# Enable Claude 3.5 Sonnet
aws bedrock put-model-invocation-logging-configuration \
    --logging-config '{
        "cloudWatchConfig": {
            "logGroupName": "/aws/bedrock/zero-cost-ai"
        }
    }'
```

### Fallback Logic in Agent

```python
# bedrock_fallback.py
import boto3
import json
import os

class BedrockFallbackLLM:
    """Hybrid LLM with Amazon Bedrock fallback."""
    
    def __init__(self):
        # Local Ollama
        self.local_endpoint = os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434")
        
        # Bedrock client
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=os.environ.get("AWS_REGION", "us-east-1")
        )
        
        self.fallback_model = os.environ.get("BEDROCK_MODEL", "anthropic.claude-3-sonnet-20240229-v1:0")
    
    def should_use_fallback(self, local_response: str) -> bool:
        """Determine if local response is low quality."""
        indicators = [
            "I don't know",
            "I'm not sure",
            "cannot answer",
            "no information",
            "uncertain",
            "maybe"
        ]
        score = sum(1 for ind in indicators if ind in local_response.lower())
        return score >= 2  # If two or more indicators
    
    async def generate(self, prompt: str) -> str:
        """Generate with local LLM, fallback to Bedrock if needed."""
        
        # Try local first
        local_response = await self._call_local(prompt)
        
        # Check quality
        if self.should_use_fallback(local_response):
            print("⚠️ Local LLM uncertain, falling back to Amazon Bedrock")
            return await self._call_bedrock(prompt)
        
        return local_response
    
    async def _call_local(self, prompt: str) -> str:
        """Call local Ollama."""
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.local_endpoint}/api/generate",
                json={"model": "llama3.3:70b-instruct-q4_K_M", "prompt": prompt}
            ) as resp:
                data = await resp.json()
                return data.get("response", "")
    
    async def _call_bedrock(self, prompt: str) -> str:
        """Call Amazon Bedrock (Claude 3.5)."""
        
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        })
        
        response = self.bedrock.invoke_model(
            modelId=self.fallback_model,
            contentType="application/json",
            accept="application/json",
            body=body
        )
        
        result = json.loads(response['body'].read())
        return result.get("content", [{}])[0].get("text", "")
```

---

## Step 5: AWS X-Ray for Distributed Tracing

Enable AWS X-Ray to trace requests through your application.

```python
# xray_integration.py
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.aiohttp.client import aws_xray_trace_config
import aiohttp

# Configure X-Ray
xray_recorder.configure(
    service='Zero-Cost-AI',
    daemon_address='127.0.0.1:2000'
)

@xray_recorder.capture('agent.run')
async def run_agent(user_input: str) -> str:
    """Run agent with X-Ray tracing."""
    
    subsegment = xray_recorder.begin_subsegment('llm_inference')
    try:
        response = await call_llm(user_input)
        subsegment.put_annotation('response_length', len(response))
        subsegment.put_metadata('input', user_input[:100])
        return response
    except Exception as e:
        subsegment.add_exception(e, stack=False)
        raise
    finally:
        xray_recorder.end_subsegment()
```

### Enable X-Ray on ECS

```json
// Add to container definition
{
    "name": "zero-cost-ai",
    "image": "...",
    "environment": [
        {"name": "AWS_XRAY_DAEMON_ADDRESS", "value": "127.0.0.1:2000"}
    ]
}

// Add X-Ray sidecar container
{
    "name": "xray-daemon",
    "image": "amazon/aws-xray-daemon:latest",
    "portMappings": [
        {"containerPort": 2000, "protocol": "udp"}
    ]
}
```

---

## Step 6: Auto-Scaling Configuration

Configure ECS service auto-scaling based on CPU and memory usage.

```bash
# Register scalable target
aws application-autoscaling register-scalable-target \
    --service-namespace ecs \
    --scalable-dimension ecs:service:DesiredCount \
    --resource-id service/zero-cost-ai-cluster/zero-cost-ai-service \
    --min-capacity 1 \
    --max-capacity 10

# Create scaling policy (CPU-based)
aws application-autoscaling put-scaling-policy \
    --service-namespace ecs \
    --scalable-dimension ecs:service:DesiredCount \
    --resource-id service/zero-cost-ai-cluster/zero-cost-ai-service \
    --policy-name zero-cost-ai-cpu-scaling \
    --policy-type TargetTrackingScaling \
    --target-tracking-scaling-policy-configuration '{
        "TargetValue": 70.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "ECSServiceAverageCPUUtilization"
        }
    }'

# Create scaling policy (memory-based)
aws application-autoscaling put-scaling-policy \
    --service-namespace ecs \
    --scalable-dimension ecs:service:DesiredCount \
    --resource-id service/zero-cost-ai-cluster/zero-cost-ai-service \
    --policy-name zero-cost-ai-memory-scaling \
    --policy-type TargetTrackingScaling \
    --target-tracking-scaling-policy-configuration '{
        "TargetValue": 75.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "ECSServiceAverageMemoryUtilization"
        }
    }'
```

---

## Step 7: CloudWatch Dashboards and Alarms

### Create CloudWatch Dashboard

```bash
# Create dashboard JSON
cat > dashboard.json << 'EOF'
{
    "widgets": [
        {
            "type": "metric",
            "properties": {
                "metrics": [
                    [ "AWS/ECS", "CPUUtilization", "ServiceName", "zero-cost-ai-service" ],
                    [ ".", "MemoryUtilization", ".", "." ]
                ],
                "period": 300,
                "stat": "Average",
                "region": "us-east-1",
                "title": "ECS Resource Utilization"
            }
        },
        {
            "type": "log",
            "properties": {
                "query": "SOURCE '/aws/ecs/zero-cost-ai' | fields @timestamp, @message | filter @message like /llm_request_completed/ | sort @timestamp desc | limit 100",
                "region": "us-east-1",
                "title": "LLM Request Logs",
                "view": "table"
            }
        },
        {
            "type": "metric",
            "properties": {
                "metrics": [
                    [ "ZeroCostAI", "LLMLatency", { "stat": "p95" } ]
                ],
                "period": 60,
                "stat": "Average",
                "region": "us-east-1",
                "title": "LLM Latency (P95)"
            }
        }
    ]
}
EOF

# Create dashboard
aws cloudwatch put-dashboard \
    --dashboard-name "Zero-Cost-AI" \
    --dashboard-body file://dashboard.json
```

### Set Up Alarms

```bash
# CPU alarm
aws cloudwatch put-metric-alarm \
    --alarm-name "zero-cost-ai-high-cpu" \
    --alarm-description "Alert when CPU exceeds 80%" \
    --metric-name CPUUtilization \
    --namespace AWS/ECS \
    --statistic Average \
    --period 300 \
    --evaluation-periods 2 \
    --threshold 80 \
    --comparison-operator GreaterThanThreshold \
    --dimensions Name=ServiceName,Value=zero-cost-ai-service \
    --alarm-actions arn:aws:sns:us-east-1:$ACCOUNT_ID:zero-cost-ai-alerts

# Error rate alarm
aws cloudwatch put-metric-alarm \
    --alarm-name "zero-cost-ai-high-errors" \
    --alarm-description "Alert when error rate exceeds 5%" \
    --metric-name ErrorRate \
    --namespace ZeroCostAI \
    --statistic Average \
    --period 60 \
    --evaluation-periods 3 \
    --threshold 5 \
    --comparison-operator GreaterThanThreshold
```

---

## Step 8: Cost Estimation for AWS

### Monthly Cost Calculator

| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| **ECS Fargate (CPU)** | 2 vCPU, 16GB RAM | $30-50 |
| **EC2 G4dn (GPU)** | 4 vCPU, 16GB RAM, T4 GPU | $380 (on-demand) |
| **EC2 P4d (GPU)** | 96 vCPU, 1152GB RAM, 8x A100 | $23,000 (on-demand) |
| **Spot Instances** | G4dn (70% discount) | $115 |
| **S3 Storage** | 50GB (model + logs) | $1.15 |
| **EFS** | 50GB (persistent data) | $15 |
| **ECR** | Storage and requests | $0-5 |
| **CloudWatch** | Logs and metrics | $0-10 |
| **Bedrock** | Optional (10K queries) | $25-50 |

**Total (CPU only with Spot):** ~$50-80/month  
**Total (GPU with Spot):** ~$150-200/month  
**Total (On-demand GPU):** ~$400-500/month  

### Cost-Saving Strategies

| Strategy | Savings | Implementation |
|----------|---------|----------------|
| **Spot Instances** | 70-90% | Use EC2 Spot for non-production |
| **S3 Intelligent-Tiering** | 20-40% | Auto-move cold data |
| **Fargate Savings Plan** | 20-30% | 1-year commitment |
| **Graviton Processors** | 10-20% | Use ARM-based instances |
| **Inferentia Chips** | 40-50% | Use Inf1 instances for inference |

---

## What's Next

You have successfully deployed your zero-cost AI stack to AWS. Your same Docker container – unchanged from the HuggingFace deployment – now runs on AWS ECS Fargate with S3 storage, EFS persistence, and optional GPU acceleration.

### Other Bonus Stories

📎 **Read** [Zero-Cost AI: Deploy from Laptop to Azure (Bonus)]  
*Step-by-step deployment to Azure Container Instances, Azure Blob Storage, and Azure OpenAI (optional).*

📎 **Read** [Zero-Cost AI: Deploy from Laptop to GCP (Bonus)]  
*Step-by-step deployment to Google Cloud Run, Cloud Storage, and GKE for Kubernetes-based scaling.*

---

**Your zero-cost AI stack is now running on AWS.** The same portable container, the same environment variables, the same core logic – just deployed to the world's most comprehensive cloud platform.

> *"AWS ECS Fargate lets you run containers without managing servers. Your zero-cost AI stack deploys in minutes, scales automatically, and costs only what you use." — Zero-Cost AI Handbook*

---

**Estimated read time for this bonus story:** 35-45 minutes.

**Would you like me to write the GCP Bonus Story next, following the same detailed structure?**