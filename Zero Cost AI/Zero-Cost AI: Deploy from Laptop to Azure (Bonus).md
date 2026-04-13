Here is the **Azure Bonus Story** – a complete, detailed deployment guide for Azure, following the exact same structure as the main handbook stories.

---

# Zero-Cost AI: Deploy from Laptop to Azure (Bonus)

## A Complete Handbook for Deploying Your Zero-Cost AI Stack to Azure Container Instances, Azure Blob Storage, and Azure Files — with Optional GPU Acceleration and Azure OpenAI Fallback

---

## Introduction

You have built a complete zero-cost AI stack that runs on your laptop and deploys to HuggingFace Spaces for free. It works beautifully. But now you need more.

More RAM. More vCPUs. GPUs for faster inference. Enterprise security. Compliance certifications. Integration with your organization's Azure subscription.

HuggingFace Spaces free tier gives you 16GB RAM and 2 vCPUs. Azure gives you up to 448GB RAM, 128 vCPUs, NVIDIA T4, A100, and H100 GPUs, global availability, and enterprise-grade security.

The conventional approach would be to rewrite your application using Azure-specific SDKs, Azure Machine Learning, and proprietary APIs. This locks you in and takes weeks.

But this is the Zero-Cost AI handbook, and we don't do lock-in.

In this Azure bonus story, you will deploy your existing Docker container – the same one from the HuggingFace deployment – to Azure Container Instances with zero code changes. You will add Azure Blob Storage for model caching and user data. You will optionally add GPU acceleration for 10-100x faster inference. You will optionally integrate Azure OpenAI as a fallback LLM when your local model needs help. And you will set up Azure Monitor for observability.

No rewrite. No lock-in. Just the same portable stack running on Azure's enterprise infrastructure.

---

## Takeaway from the Cloud Portability Story

This bonus story builds directly on **Zero-Cost AI: Scaling AI Deployments to Azure, AWS & GCP Without Rewrites**. That story established:

- **Core AI logic is portable.** Your LangGraph agent, RAG pipeline, MCP tools, and prompt engineering run unchanged on any cloud.

- **Environment variables abstract cloud details.** Your code reads configuration from environment variables, not hardcoded values.

- **Docker containers are the portable unit.** The same `Dockerfile` that deployed to HuggingFace deploys to Azure.

- **Storage requires cloud-specific adaptation.** Object storage (Blob) and persistent volumes (Azure Files) need SDK changes.

- **Authentication is cloud-specific.** Azure uses Azure AD and Managed Identities.

With these takeaways in place, you are ready to deploy to Azure.

---

## Stories in This Series (Updated with Bonus)

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

**📎 (Bonus)** Zero-Cost AI: Deploy from Laptop to Azure *(you are here)*  
*Step-by-step deployment to Azure Container Instances, Azure Blob Storage, and Azure OpenAI (optional) — keeping your core Llama 3.3 stack portable.*

**📎 (Bonus)** Zero-Cost AI: Deploy from Laptop to AWS  
*Step-by-step deployment to AWS ECS, S3 for model storage, and EC2 with GPU for high-performance inference.*

**📎 (Bonus)** Zero-Cost AI: Deploy from Laptop to GCP  
*Step-by-step deployment to Google Cloud Run, Cloud Storage, and GKE for Kubernetes-based scaling.*

---

## Azure Deployment Architecture

The diagram below shows how your zero-cost AI stack deploys to Azure.

```mermaid
flowchart TB
    User[👤 User Browser] --> Frontend[🖥️ Frontend\nVercel / Static Web App]
    Frontend --> ACI[🐳 Azure Container Instances\nYour Docker container\nCPU or GPU]\
    
    ACI --> Ollama[🤖 Ollama LLM\nLlama 3.3 70B\nInside container]
    
    ACI --> Blob[📦 Azure Blob Storage\nModel cache (8GB)\nUser uploads\nLogs]
    
    ACI --> Files[📁 Azure Files\nPersistent checkpoints\nSQLite database\nRAG vectors]
    
    ACI --> OpenAI[🔌 Optional: Azure OpenAI\nGPT-4 fallback\nWhen local model uncertain]
    
    ACI --> Monitor[📊 Azure Monitor\nLogs | Metrics | Alerts]
    
    style ACI fill:#0078d4,stroke:#005a9e,stroke-width:3px,color:#fff
    style Blob fill:#0078d4,stroke:#005a9e,stroke-width:2px,color:#fff
    style Files fill:#0078d4,stroke:#005a9e,stroke-width:2px,color:#fff
    style OpenAI fill:#0078d4,stroke:#005a9e,stroke-width:2px,color:#fff
```

### Azure Services Used (Free Credits Available)

| Service | Purpose | Cost Estimate |
|---------|---------|---------------|
| **Container Instances (ACI)** | Run your Docker container | $0.01-0.50/hour (CPU) / $0.50-3.00/hour (GPU) |
| **Blob Storage** | Model cache, user uploads, logs | $0.015-0.05/GB-month |
| **Azure Files** | Persistent SQLite, checkpoints | $0.05-0.10/GB-month |
| **Azure OpenAI** | Optional GPT-4 fallback | $2.50-10/1M tokens |
| **Azure Monitor** | Logs, metrics, alerts | First 5GB logs free |
| **Container Registry (ACR)** | Store Docker images | Basic tier free (1 image, 10GB) |

**New user credit:** $200 free credit for first 30 days.

---

## Step 1: Prepare Your Docker Container for Azure

Your existing Dockerfile from the HuggingFace deployment works on Azure with minor additions.

```dockerfile
# Dockerfile.azure
# Extended Dockerfile for Azure deployment

FROM ollama/ollama:0.5.1 as ollama-base
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Azure CLI (for Blob storage access)
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Ollama
COPY --from=ollama-base /usr/bin/ollama /usr/bin/ollama

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install azure-storage-blob azure-identity azure-monitor-opentelemetry

# Copy application
COPY . .

# Create directories
RUN mkdir -p /root/.ollama /app/data /app/logs

# Copy Azure-specific entrypoint
COPY entrypoint_azure.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=180s --retries=3 \
    CMD curl -f http://localhost:11434/api/tags || exit 1

EXPOSE 11434 8000 7860

ENTRYPOINT ["/entrypoint.sh"]
```

### Azure-Specific Entrypoint Script

```bash
#!/bin/bash
# entrypoint_azure.sh
# Entrypoint with Azure Blob Storage integration

set -e

echo "🚀 Starting Zero-Cost AI Stack on Azure"
echo "========================================="

# Azure Blob Storage for model cache
if [ -n "$AZURE_STORAGE_CONNECTION_STRING" ]; then
    echo "📦 Downloading model from Azure Blob Storage..."
    az storage blob download \
        --container-name "ai-models" \
        --name "llama3.3-70b-q4_K_M.ollama" \
        --file "/root/.ollama/models/blobs/sha256-xxx" \
        --connection-string "$AZURE_STORAGE_CONNECTION_STRING" || true
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
    
    # Upload to Blob Storage for next deployment
    if [ -n "$AZURE_STORAGE_CONNECTION_STRING" ]; then
        echo "📤 Uploading model to Blob Storage for caching..."
        MODEL_PATH=$(ollama list --json | jq -r '.models[] | select(.name=="llama3.3:70b-instruct-q4_K_M") | .digest')
        az storage blob upload \
            --container-name "ai-models" \
            --name "llama3.3-70b-q4_K_M.ollama" \
            --file "/root/.ollama/models/blobs/$MODEL_PATH" \
            --connection-string "$AZURE_STORAGE_CONNECTION_STRING"
    fi
fi

# Mount Azure Files for persistent storage
if [ -n "$AZURE_FILES_SHARE" ]; then
    echo "📁 Mounting Azure Files share..."
    mkdir -p /app/data
    mount -t cifs "$AZURE_FILES_SHARE" /app/data \
        -o username="$AZURE_FILES_USERNAME",password="$AZURE_FILES_PASSWORD",uid=$(id -u),gid=$(id -g)
fi

# Start agent and frontend
python -m uvicorn agent_api:app --host 0.0.0.0 --port 8000 &
streamlit run app.py --server.port 7860 --server.address 0.0.0.0 &

echo "========================================="
echo "✅ All components started on Azure!"
echo "========================================="

wait $OLLAMA_PID
```

---

## Step 2: Create Azure Resources

### Option A: Azure CLI (Recommended)

```bash
# Login to Azure
az login

# Create resource group
az group create --name "zero-cost-ai-rg" --location "eastus"

# Create Azure Container Registry (ACR) - Free tier
az acr create \
    --resource-group "zero-cost-ai-rg" \
    --name "zerocostai" \
    --sku Basic \
    --admin-enabled true

# Build and push Docker image
az acr build \
    --resource-group "zero-cost-ai-rg" \
    --registry "zerocostai" \
    --image "zero-cost-ai:latest" \
    --file Dockerfile.azure .

# Create Blob Storage account
az storage account create \
    --name "zerocostaistorage" \
    --resource-group "zero-cost-ai-rg" \
    --location "eastus" \
    --sku Standard_LRS \
    --kind StorageV2

# Create Blob container for models
az storage container create \
    --name "ai-models" \
    --account-name "zerocostaistorage" \
    --public-access off

# Create Azure Files share for persistent data
az storage share create \
    --name "ai-data" \
    --account-name "zerocostaistorage" \
    --quota 50

# Get connection string
STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
    --name "zerocostaistorage" \
    --resource-group "zero-cost-ai-rg" \
    --query connectionString \
    --output tsv)

echo "Storage connection string: $STORAGE_CONNECTION_STRING"
```

### Option B: Terraform (Infrastructure as Code)

```hcl
# main.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "zero-cost-ai-rg"
  location = "East US"
}

# Container Registry
resource "azurerm_container_registry" "acr" {
  name                = "zerocostai"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

# Storage Account
resource "azurerm_storage_account" "storage" {
  name                     = "zerocostaistorage"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Blob Container
resource "azurerm_storage_container" "models" {
  name                  = "ai-models"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

# File Share
resource "azurerm_storage_share" "data" {
  name                 = "ai-data"
  storage_account_name = azurerm_storage_account.storage.name
  quota                = 50
}

# Container Instance (CPU)
resource "azurerm_container_group" "ai" {
  name                = "zero-cost-ai"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"

  container {
    name   = "zero-cost-ai"
    image  = "${azurerm_container_registry.acr.login_server}/zero-cost-ai:latest"
    cpu    = 2
    memory = 16  # GB

    ports {
      port     = 7860
      protocol = "TCP"
    }

    ports {
      port     = 8000
      protocol = "TCP"
    }

    environment_variables = {
      "AZURE_STORAGE_CONNECTION_STRING" = azurerm_storage_account.storage.primary_connection_string
      "LLM_MODEL"                       = "llama3.3:70b-instruct-q4_K_M"
      "LOG_LEVEL"                       = "INFO"
    }
  }

  ip_address_type     = "Public"
  dns_name_label      = "zero-cost-ai"
  restart_policy      = "OnFailure"
  
  tags = {
    environment = "production"
    cost-center = "ai"
  }
}
```

---

## Step 3: Deploy to Azure Container Instances (ACI)

### CPU Deployment (Cost-Effective)

```bash
# Create Container Instance with 16GB RAM, 2 vCPUs
az container create \
    --resource-group "zero-cost-ai-rg" \
    --name "zero-cost-ai-cpu" \
    --image "zerocostai.azurecr.io/zero-cost-ai:latest" \
    --registry-login-server "zerocostai.azurecr.io" \
    --registry-username "zerocostai" \
    --registry-password $(az acr credential show --name "zerocostai" --query "passwords[0].value" -o tsv) \
    --cpu 2 \
    --memory 16 \
    --os-type Linux \
    --ports 7860 8000 \
    --ip-address Public \
    --dns-name-label "zero-cost-ai" \
    --environment-variables \
        LLM_MODEL="llama3.3:70b-instruct-q4_K_M" \
        LOG_LEVEL="INFO" \
        AZURE_STORAGE_CONNECTION_STRING="$STORAGE_CONNECTION_STRING"

# Get the public IP
az container show \
    --resource-group "zero-cost-ai-rg" \
    --name "zero-cost-ai-cpu" \
    --query "ipAddress.ip" \
    --output tsv

# Access your app at: http://<IP>:7860
```

### GPU Deployment (High Performance)

```bash
# Create Container Instance with NVIDIA T4 GPU
az container create \
    --resource-group "zero-cost-ai-rg" \
    --name "zero-cost-ai-gpu" \
    --image "zerocostai.azurecr.io/zero-cost-ai:latest" \
    --registry-login-server "zerocostai.azurecr.io" \
    --registry-username "zerocostai" \
    --registry-password $(az acr credential show --name "zerocostai" --query "passwords[0].value" -o tsv) \
    --cpu 6 \
    --memory 56 \
    --gpu-resources "V100" \
    --os-type Linux \
    --ports 7860 8000 \
    --ip-address Public \
    --dns-name-label "zero-cost-ai-gpu" \
    --environment-variables \
        LLM_MODEL="llama3.3:70b-instruct-q4_K_M" \
        LOG_LEVEL="INFO"

# Expected cost: ~$2-3/hour
```

---

## Step 4: Optional – Azure OpenAI Fallback Integration

Add Azure OpenAI as a fallback when your local Llama model is uncertain.

### Create Azure OpenAI Resource

```bash
# Deploy Azure OpenAI (requires approval)
az cognitiveservices account create \
    --name "zero-cost-ai-openai" \
    --resource-group "zero-cost-ai-rg" \
    --location "eastus" \
    --kind "OpenAI" \
    --sku "S0"

# Deploy GPT-4 model
az cognitiveservices account deployment create \
    --name "zero-cost-ai-openai" \
    --resource-group "zero-cost-ai-rg" \
    --deployment-name "gpt-4" \
    --model-name "gpt-4" \
    --model-version "0613" \
    --model-format "OpenAI" \
    --sku-capacity 1 \
    --sku-name "Standard"
```

### Fallback Logic in Agent

```python
# azure_fallback.py
import openai
from openai import AzureOpenAI
import os

class HybridLLM:
    """Hybrid LLM that falls back to Azure OpenAI when local model is uncertain."""
    
    def __init__(self):
        # Local Ollama
        self.local_endpoint = os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434")
        
        # Azure OpenAI (optional)
        self.azure_client = None
        if os.environ.get("AZURE_OPENAI_ENDPOINT"):
            self.azure_client = AzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_API_KEY"],
                api_version="2024-02-15-preview"
            )
    
    def should_use_fallback(self, local_response: str) -> bool:
        """Determine if local response is low quality."""
        indicators = [
            "I don't know",
            "I'm not sure",
            "uncertain",
            "cannot answer",
            "no information"
        ]
        return any(indicator in local_response.lower() for indicator in indicators)
    
    async def generate(self, prompt: str) -> str:
        """Generate with local LLM, fallback to Azure OpenAI if needed."""
        
        # Try local first
        local_response = await self._call_local(prompt)
        
        # Check quality
        if self.should_use_fallback(local_response) and self.azure_client:
            print("⚠️ Local LLM uncertain, falling back to Azure OpenAI")
            return await self._call_azure_openai(prompt)
        
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
    
    async def _call_azure_openai(self, prompt: str) -> str:
        """Call Azure OpenAI GPT-4."""
        response = self.azure_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
```

---

## Step 5: Azure Monitor for Observability

### Enable Azure Monitor for Container Instances

```bash
# Enable container insights
az monitor log-analytics workspace create \
    --resource-group "zero-cost-ai-rg" \
    --workspace-name "zero-cost-ai-logs"

az monitor log-analytics workspace get-shared-keys \
    --resource-group "zero-cost-ai-rg" \
    --workspace-name "zero-cost-ai-logs"

# Add to container instance
az container update \
    --resource-group "zero-cost-ai-rg" \
    --name "zero-cost-ai-cpu" \
    --log-analytics-workspace-id "workspace-id" \
    --log-analytics-workspace-key "workspace-key"
```

### Query Logs with KQL

```kusto
// Azure Log Analytics query
ContainerLog
| where ContainerName == "zero-cost-ai"
| where LogEntry contains "llm_request_completed"
| extend duration_ms = extract("duration_ms\":(\\d+)", 1, LogEntry)
| project timestamp, duration_ms
| summarize avg_duration = avg(todouble(duration_ms)) by bin(timestamp, 1h)
| render timechart
```

### Set Up Alerts

```bash
# Create alert for high latency
az monitor metrics alert create \
    --name "High LLM Latency" \
    --resource-group "zero-cost-ai-rg" \
    --scopes "/subscriptions/xxx/resourceGroups/zero-cost-ai-rg/providers/Microsoft.ContainerInstance/containerGroups/zero-cost-ai-cpu" \
    --condition "avg Percentage CPU > 80" \
    --description "CPU usage exceeds 80%" \
    --action email "your-email@example.com"
```

---

## Step 6: Cost Estimation for Azure

### Monthly Cost Calculator

| Component | Configuration | Monthly Cost |
|-----------|---------------|--------------|
| **ACI (CPU)** | 2 vCPU, 16GB RAM | $30-50 |
| **ACI (GPU)** | 6 vCPU, 56GB RAM, V100 | $500-800 |
| **Blob Storage** | 50GB (model + logs) | $1-2 |
| **Azure Files** | 50GB (persistent data) | $2-3 |
| **ACR** | Basic tier | $0-5 |
| **Azure Monitor** | 5GB logs | $0 (free) |
| **Azure OpenAI** | Optional (10K queries) | $25-50 |

**Total (CPU only):** ~$35-60/month  
**Total (GPU):** ~$550-900/month  

**Cost-saving tips:**
- Use spot instances for non-production (70% discount)
- Stop containers when not in use
- Use Azure free credits ($200 for new users)

---

## What's Next

You have successfully deployed your zero-cost AI stack to Azure. Your same Docker container – unchanged from the HuggingFace deployment – now runs on Azure Container Instances with Blob storage, persistent files, and optional GPU acceleration.

### Other Bonus Stories

📎 **Read** [Zero-Cost AI: Deploy from Laptop to AWS (Bonus)]  
*Step-by-step deployment to AWS ECS, S3 for model storage, and EC2 with GPU for high-performance inference.*

📎 **Read** [Zero-Cost AI: Deploy from Laptop to GCP (Bonus)]  
*Step-by-step deployment to Google Cloud Run, Cloud Storage, and GKE for Kubernetes-based scaling.*

---

**Your zero-cost AI stack is now running on Azure.** The same portable container, the same environment variables, the same core logic – just deployed to enterprise infrastructure.

> *"Azure Container Instances is the easiest path from zero-cost AI to enterprise AI. No orchestration, no Kubernetes, just your container running in the cloud." — Zero-Cost AI Handbook*

---

**Would you like me to write the AWS Bonus Story next, following the same detailed structure?**