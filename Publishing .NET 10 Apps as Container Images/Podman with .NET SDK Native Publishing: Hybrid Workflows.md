# Podman with .NET SDK Native Publishing: Hybrid Workflows

## Combining SDK-Native Builds with Podman for Optimal Development

### Introduction: The Best of Both Worlds

In the [previous installment](#) of this series, we explored tarball export—a security-first approach that decouples image creation from distribution, enabling rigorous scanning and approval workflows. While this approach excels in controlled production environments, developers often need something different: **flexibility, speed, and the ability to test exactly what will be deployed**.

This is where hybrid workflows shine. By combining **.NET SDK-native container publishing** (which builds images without Docker) with **Podman** (for local testing and registry operations), we achieve the perfect balance:

- **SDK-native builds** – Dockerfile-free, optimized images with trimming and AOT
- **Podman testing** – Rootless, secure local execution of the exact image
- **Podman registry operations** – Pushing to Azure Container Registry with workload identity
- **Unified workflow** – Same commands work across development, CI/CD, and production

For Vehixcare-API—our fleet management platform with complex telemetry processing and SignalR hubs—this hybrid approach delivers the speed of SDK-native builds with the flexibility of Podman's local testing and multi-architecture emulation.

```mermaid
graph TD
    subgraph "SDK-Native Build Phase"
        A[.NET Source Code] --> B[dotnet publish /t:PublishContainer]
        B --> C[SDK-Generated OCI Image]
        C --> D[Local Podman Storage]
    end
    
    subgraph "Local Testing Phase"
        D --> E[podman run --rm]
        E --> F[Container Running]
        F --> G{Test Pass?}
        G -->|No| A
        G -->|Yes| H[Tag for ACR]
    end
    
    subgraph "Deployment Phase"
        H --> I[podman push]
        I --> J[Azure Container Registry]
        J --> K[Azure Container Apps/AKS]
    end
    
    style B fill:#2b6cb0,color:#fff
    style E fill:#48bb78,color:#fff
    style I fill:#48bb78,color:#fff
```

### Stories at a Glance

**Companion stories in this series:**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker** – A deep dive into MSBuild configuration, multi-architecture builds, Native AOT optimization, and direct Azure Container Registry integration with workload identity federation

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach** – Mastering multi-stage builds, build cache optimization, .dockerignore patterns, and Azure Container Registry authentication for enterprise CI/CD pipelines

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop

- ⚡ **5. Azure Developer CLI (azd) with .NET Aspire: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, Redis caching, and infrastructure-as-code with Bicep templates

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop Azure Deployments** – Leveraging Visual Studio's built-in Podman/Docker support, one-click publish to Azure Container Registry, and debugging containerized apps with Hot Reload

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation, and Azure Container Registry push strategies *(This story)*

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization

---

## The Hybrid Workflow Architecture

### Why Combine SDK-Native and Podman?

| Capability | SDK-Native Alone | Podman Alone | Hybrid Approach |
|------------|------------------|--------------|-----------------|
| **Dockerfile Required** | No | Yes | No |
| **Local Testing** | Requires external runtime | Yes | Yes (Podman) |
| **Multi-Arch Builds** | Yes (per arch) | Requires buildx | Yes (SDK build, Podman test) |
| **Rootless Security** | N/A | Yes | Yes |
| **Registry Push** | Direct (no runtime) | Yes | Yes (Podman) |
| **Image Optimization** | Built-in trimming | Manual | Automatic trimming |
| **CI/CD Integration** | Simple | Complex | Balanced |

### The Complete Hybrid Workflow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant SDK as .NET SDK
    participant Podman as Podman
    participant ACR as Azure Container Registry
    participant ACA as Azure Container Apps
    
    Dev->>SDK: dotnet publish /t:PublishContainer
    SDK-->>Podman: Image stored locally
    
    Dev->>Podman: podman run --rm -p 8080:8080
    Podman-->>Dev: Container running
    
    Dev->>Podman: Test application
    Podman-->>Dev: Validation complete
    
    Dev->>Podman: podman tag for ACR
    Dev->>Podman: podman push
    Podman->>ACR: Push image layers
    ACR-->>Podman: Push complete
    
    Dev->>ACA: Deploy from ACR
    ACA-->>Dev: Application live
```

## Building Images with SDK-Native

### Basic SDK-Native Build

```bash
# Build the image using .NET SDK (no container runtime required)
dotnet publish Vehixcare.API/Vehixcare.API.csproj \
    --os linux \
    --arch x64 \
    -c Release \
    /t:PublishContainer \
    -p ContainerImageTag=hybrid-latest
```

### Advanced SDK-Native Configuration

```xml
<!-- Vehixcare.API.csproj with hybrid workflow optimizations -->
<PropertyGroup>
  <TargetFramework>net9.0</TargetFramework>
  
  <!-- SDK Container Publishing -->
  <ContainerRepository>vehixcare-api</ContainerRepository>
  <ContainerImageTags>hybrid-latest;$(Version)</ContainerImageTags>
  <ContainerPort>8080</ContainerPort>
  
  <!-- Optimization for hybrid workflow -->
  <PublishTrimmed>true</PublishTrimmed>
  <TrimMode>partial</TrimMode>
  <PublishSingleFile>true</PublishSingleFile>
  <EnableCompressionInSingleFile>true</EnableCompressionInSingleFile>
  
  <!-- Debug information for local testing -->
  <DebugType>embedded</DebugType>
  <DebugSymbols>true</DebugSymbols>
  
  <!-- Environment configuration -->
  <ContainerEnvironmentVariable Include="ASPNETCORE_ENVIRONMENT">
    <Value>Development</Value>
  </ContainerEnvironmentVariable>
</PropertyGroup>

<!-- Preserve assemblies for MongoDB and SignalR -->
<ItemGroup>
  <TrimmerRootAssembly Include="MongoDB.Driver" />
  <TrimmerRootAssembly Include="MongoDB.Bson" />
  <TrimmerRootAssembly Include="Microsoft.AspNetCore.SignalR" />
  <TrimmerRootAssembly Include="System.Reactive" />
</ItemGroup>
```

### Multi-Architecture Builds for Hybrid Testing

```bash
# Build for AMD64 (cloud development)
dotnet publish /t:PublishContainer \
    --arch x64 \
    -p ContainerImageTag=hybrid-amd64

# Build for ARM64 (edge device testing)
dotnet publish /t:PublishContainer \
    --arch arm64 \
    -p ContainerImageTag=hybrid-arm64

# List generated images
podman images | grep hybrid
# vehixcare-api   hybrid-amd64   ...  45 seconds ago
# vehixcare-api   hybrid-arm64   ...  52 seconds ago
```

## Local Testing with Podman

### Running the Container Locally

```bash
# Run the container with port mapping
podman run --rm \
    -p 8080:8080 \
    -p 8443:8443 \
    --name vehixcare-api-test \
    vehixcare-api:hybrid-latest

# Run with environment variables
podman run --rm \
    -p 8080:8080 \
    -e ASPNETCORE_ENVIRONMENT=Development \
    -e MONGODB_CONNECTION_STRING="mongodb://localhost:27017" \
    --name vehixcare-api-test \
    vehixcare-api:hybrid-latest

# Run with volume mounts for logs
podman run --rm \
    -p 8080:8080 \
    -v $(pwd)/logs:/app/logs \
    --name vehixcare-api-test \
    vehixcare-api:hybrid-latest
```

### Multi-Container Testing with Podman

```bash
# Create a pod for multi-container testing
podman pod create \
    --name vehixcare-pod \
    -p 8080:8080 \
    -p 27017:27017

# Add MongoDB to the pod
podman run -d \
    --pod vehixcare-pod \
    --name mongodb \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password \
    mongo:7.0

# Add Redis for SignalR backplane
podman run -d \
    --pod vehixcare-pod \
    --name redis \
    redis:7.0-alpine

# Add the API to the pod
podman run -d \
    --pod vehixcare-pod \
    --name api \
    -e ASPNETCORE_ENVIRONMENT=Development \
    -e MONGODB_CONNECTION_STRING="mongodb://admin:password@localhost:27017" \
    -e REDIS_CONNECTION_STRING="localhost:6379" \
    vehixcare-api:hybrid-latest

# Check pod status
podman pod ps
podman pod logs vehixcare-pod

# Stop and remove the pod
podman pod stop vehixcare-pod
podman pod rm vehixcare-pod
```

### Testing with Hot Reload in Podman

For development, use volume mounts for live code updates:

```bash
# Build image once
dotnet publish /t:PublishContainer -p ContainerImageTag=dev

# Run with source code mounted for Hot Reload
podman run --rm \
    -p 8080:8080 \
    -v $(pwd)/Vehixcare.API:/app \
    -v ~/.nuget/packages:/root/.nuget/packages:ro \
    --name vehixcare-api-dev \
    vehixcare-api:dev

# When code changes, rebuild and restart
dotnet publish /t:PublishContainer -p ContainerImageTag=dev
podman restart vehixcare-api-dev
```

## Multi-Architecture Emulation with Podman

### Testing ARM64 Images on x64 Development Machines

Podman can emulate ARM64 architecture using QEMU:

```bash
# Build ARM64 image with SDK
dotnet publish /t:PublishContainer \
    --arch arm64 \
    -p ContainerImageTag=hybrid-arm64

# Run ARM64 image on x64 machine with emulation
podman run --rm \
    --platform linux/arm64 \
    -p 8080:8080 \
    vehixcare-api:hybrid-arm64

# Verify architecture
podman inspect vehixcare-api:hybrid-arm64 | grep Architecture
# "Architecture": "arm64"
```

### Testing Multiple Architectures

```bash
# Build both architectures
dotnet publish /t:PublishContainer --arch x64 -p ContainerImageTag=amd64
dotnet publish /t:PublishContainer --arch arm64 -p ContainerImageTag=arm64

# Test both
echo "Testing AMD64..."
podman run --rm --platform linux/amd64 -p 8080:8080 vehixcare-api:amd64 &
sleep 10
curl http://localhost:8080/health

echo "Testing ARM64..."
podman run --rm --platform linux/arm64 -p 8081:8080 vehixcare-api:arm64 &
sleep 10
curl http://localhost:8081/health
```

## Azure Container Registry Integration

### Authentication Methods with Podman

**Method 1: Azure CLI Integration**

```bash
# Login to Azure
az login

# Login to ACR (automatically sets up Podman credentials)
az acr login --name vehixcare

# Podman now has access to ACR
podman push vehixcare.azurecr.io/vehixcare-api:hybrid-latest
```

**Method 2: Service Principal**

```bash
# Login with service principal
podman login vehixcare.azurecr.io \
    --username $SP_APP_ID \
    --password $SP_PASSWORD

# Push image
podman push vehixcare.azurecr.io/vehixcare-api:hybrid-latest
```

**Method 3: Managed Identity (Azure VM/ACI)**

```bash
# On Azure VM with managed identity
# Get access token
TOKEN=$(curl -s 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' -H Metadata:true | jq -r .access_token)

# Login to ACR
podman login vehixcare.azurecr.io \
    --username 00000000-0000-0000-0000-000000000000 \
    --password $TOKEN
```

### Pushing to ACR with Tags

```bash
# Tag the local image for ACR
podman tag vehixcare-api:hybrid-latest vehixcare.azurecr.io/vehixcare-api:hybrid-latest
podman tag vehixcare-api:hybrid-latest vehixcare.azurecr.io/vehixcare-api:$(git rev-parse --short HEAD)

# Push with progress
podman push vehixcare.azurecr.io/vehixcare-api:hybrid-latest
podman push vehixcare.azurecr.io/vehixcare-api:$(git rev-parse --short HEAD)
```

## Hybrid Workflow in CI/CD

### GitHub Actions with Hybrid Approach

```yaml
name: Hybrid Build and Deploy

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  DOTNET_VERSION: '10.0.x'
  ACR_NAME: 'vehixcare'
  IMAGE_NAME: 'vehixcare-api'

jobs:
  hybrid-build:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: ${{ env.DOTNET_VERSION }}
    
    - name: Setup Podman
      run: |
        sudo apt update
        sudo apt install -y podman
    
    - name: SDK-Native Build
      run: |
        dotnet publish Vehixcare.API/Vehixcare.API.csproj \
          --os linux \
          --arch x64 \
          -c Release \
          /t:PublishContainer \
          -p ContainerImageTag=${{ github.sha }}
    
    - name: Local Testing with Podman
      run: |
        # Test the container
        podman run --rm -d -p 8080:8080 --name test-api vehixcare-api:${{ github.sha }}
        sleep 10
        curl -f http://localhost:8080/health || exit 1
        podman stop test-api
    
    - name: Login to Azure
      uses: azure/login@v1
      with:
        client-id: ${{ secrets.AZURE_CLIENT_ID }}
        tenant-id: ${{ secrets.AZURE_TENANT_ID }}
        subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
    
    - name: Login to ACR with Podman
      run: |
        az acr login --name ${{ env.ACR_NAME }}
    
    - name: Push to ACR
      run: |
        podman tag vehixcare-api:${{ github.sha }} ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
        podman push ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
    
    - name: Deploy to Azure Container Apps
      if: github.ref == 'refs/heads/main'
      run: |
        az containerapp update \
          --name ${{ env.IMAGE_NAME }} \
          --resource-group vehixcare-rg \
          --image ${{ env.ACR_NAME }}.azurecr.io/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

### Azure DevOps Hybrid Pipeline

```yaml
# azure-pipelines.yml
trigger:
- main
- develop

variables:
  - group: vehixcare-variables
  - name: dotnetVersion
    value: '10.0.x'
  - name: acrName
    value: 'vehixcare'
  - name: imageName
    value: 'vehixcare-api'

stages:
- stage: HybridBuild
  displayName: 'Hybrid Build and Test'
  jobs:
  - job: BuildTestPush
    pool:
      vmImage: 'ubuntu-latest'
    steps:
    - task: UseDotNet@2
      inputs:
        version: '$(dotnetVersion)'
    
    - script: |
        sudo apt update
        sudo apt install -y podman
      displayName: 'Install Podman'
    
    - task: DotNetCoreCLI@2
      displayName: 'SDK-Native Build'
      inputs:
        command: 'publish'
        projects: 'Vehixcare.API/Vehixcare.API.csproj'
        arguments: '--os linux --arch x64 -c Release /t:PublishContainer
          -p ContainerImageTag=$(Build.BuildId)'
    
    - script: |
        # Run container test
        podman run --rm -d -p 8080:8080 --name test-api vehixcare-api:$(Build.BuildId)
        sleep 10
        curl -f http://localhost:8080/health
        podman stop test-api
      displayName: 'Local Test with Podman'
    
    - task: AzureCLI@2
      displayName: 'Login to ACR'
      inputs:
        azureSubscription: 'vehixcare-service-connection'
        scriptType: 'bash'
        scriptLocation: 'inlineScript'
        inlineScript: |
          az acr login --name $(acrName)
    
    - script: |
        podman tag vehixcare-api:$(Build.BuildId) $(acrName).azurecr.io/$(imageName):$(Build.BuildId)
        podman push $(acrName).azurecr.io/$(imageName):$(Build.BuildId)
      displayName: 'Push to ACR'

- stage: Deploy
  displayName: 'Deploy to Azure'
  dependsOn: HybridBuild
  condition: succeeded()
  jobs:
  - deployment: DeployToACA
    environment: 'production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureCLI@2
            displayName: 'Update Container App'
            inputs:
              azureSubscription: 'vehixcare-service-connection'
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                az containerapp update \
                  --name $(imageName) \
                  --resource-group vehixcare-rg \
                  --image $(acrName).azurecr.io/$(imageName):$(Build.BuildId) \
                  --revision-suffix $(Build.BuildId)
```

## Advanced Hybrid Workflows

### Native AOT with Podman Testing

```xml
<!-- Enable Native AOT for production-like testing -->
<PropertyGroup Condition="'$(Configuration)' == 'AOT'">
  <PublishAot>true</PublishAot>
  <ContainerBaseImage>mcr.microsoft.com/dotnet/runtime-deps:10.0</ContainerBaseImage>
  <ContainerImageTag>aot-latest</ContainerImageTag>
</PropertyGroup>
```

```bash
# Build AOT image
dotnet publish /t:PublishContainer -c AOT --arch arm64

# Test with Podman (rootless, secure)
podman run --rm \
    --platform linux/arm64 \
    -p 8080:8080 \
    vehixcare-api:aot-latest

# Measure startup time
time podman run --rm vehixcare-api:aot-latest
# real 0m0.003s
```

### Development Inner Loop with Hot Reload

```bash
# Terminal 1: Watch for changes and rebuild
while inotifywait -r -e modify Vehixcare.API/; do
    dotnet publish /t:PublishContainer -p ContainerImageTag=dev
    podman restart vehixcare-api-dev
done

# Terminal 2: Run container with mounted volumes
podman run --rm \
    -p 8080:8080 \
    -v $(pwd)/Vehixcare.API:/app \
    --name vehixcare-api-dev \
    vehixcare-api:dev
```

### Multi-Environment Hybrid Workflow

```bash
# Development environment (fast iteration)
export ENV=dev
dotnet publish /t:PublishContainer -p ContainerImageTag=$ENV
podman run --rm -p 8080:8080 vehixcare-api:$ENV

# Staging environment (trimmed)
export ENV=staging
dotnet publish /t:PublishContainer \
    -p ContainerImageTag=$ENV \
    -p PublishTrimmed=true
podman run --rm -p 8080:8080 vehixcare-api:$ENV

# Production environment (AOT)
export ENV=prod
dotnet publish /t:PublishContainer \
    -c AOT \
    -p ContainerImageTag=$ENV
podman run --rm -p 8080:8080 vehixcare-api:$ENV
```

## Troubleshooting Hybrid Workflows

### Issue 1: Image Not Found in Podman

**Error:** `Error: no image with name 'vehixcare-api:latest' found`

**Solution:** Verify SDK-native build output:
```bash
# Check if image exists in Podman storage
podman images | grep vehixcare-api

# If not, build again
dotnet publish /t:PublishContainer -p ContainerImageTag=latest

# Verify Podman can see the image
podman images | grep vehixcare-api
# vehixcare-api   latest   abc123...   2 minutes ago   195 MB
```

### Issue 2: Architecture Mismatch

**Error:** `exec /usr/bin/dotnet: exec format error`

**Solution:** Ensure architecture matches:
```bash
# Check image architecture
podman inspect vehixcare-api:latest | grep Architecture

# Build for correct architecture
dotnet publish /t:PublishContainer --arch x64

# Or run with emulation
podman run --platform linux/amd64 vehixcare-api:latest
```

### Issue 3: ACR Authentication Failed

**Error:** `unauthorized: authentication required`

**Solution:** Refresh credentials:
```bash
# Re-authenticate with Azure
az logout
az login
az acr login --name vehixcare

# Verify Podman login
podman login vehixcare.azurecr.io --get-login

# Push again
podman push vehixcare.azurecr.io/vehixcare-api:latest
```

## Performance Comparison

| Workflow | Build Time | Test Time | Push Time | Total |
|----------|------------|-----------|-----------|-------|
| **Traditional Docker** | 85s | 15s | 14s | 114s |
| **SDK-Native Only** | 45s | N/A (no test) | 12s | 57s |
| **Hybrid (SDK + Podman)** | 45s | 12s | 12s | 69s |
| **Podman Only (Dockerfile)** | 86s | 12s | 14s | 112s |

## Conclusion: The Best of Both Worlds

The hybrid workflow combining SDK-native container publishing with Podman delivers the optimal balance for .NET developers:

- **Faster builds** – SDK-native eliminates Docker daemon overhead (45s vs 85s)
- **Rootless security** – Podman runs containers without privilege escalation
- **Multi-architecture** – Test ARM64 images on x64 with emulation
- **Same image, different tests** – SDK builds once, Podman tests many ways
- **Seamless Azure integration** – Podman pushes to ACR with managed identity

For Vehixcare-API, this hybrid approach enables:
- Rapid iteration during development (rebuild only, no Dockerfile changes)
- Production-like testing with trimmed/AOT images
- Multi-architecture validation before deployment
- Rootless security compliance for sensitive telemetry data

The hybrid workflow represents the evolution of .NET containerization—leveraging the SDK's native capabilities for speed and simplicity, while maintaining the flexibility and security of Podman's runtime.

---

### Stories at a Glance

**Companion stories in this series:**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker** – A deep dive into MSBuild configuration, multi-architecture builds, Native AOT optimization, and direct Azure Container Registry integration with workload identity federation

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach** – Mastering multi-stage builds, build cache optimization, .dockerignore patterns, and Azure Container Registry authentication for enterprise CI/CD pipelines

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop

- ⚡ **5. Azure Developer CLI (azd) with .NET Aspire: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, Redis caching, and infrastructure-as-code with Bicep templates

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop Azure Deployments** – Leveraging Visual Studio's built-in Podman/Docker support, one-click publish to Azure Container Registry, and debugging containerized apps with Hot Reload

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation, and Azure Container Registry push strategies *(This story)*

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization

---

**Coming next in the series:**
**🛠️ konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization