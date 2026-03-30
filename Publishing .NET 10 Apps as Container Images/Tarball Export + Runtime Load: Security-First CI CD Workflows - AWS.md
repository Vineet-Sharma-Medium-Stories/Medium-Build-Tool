# Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS

## Building Secure Container Pipelines with Amazon Inspector and Air-Gapped Deployments

### Introduction: The Security Imperative on AWS

In the [previous installment](#) of this AWS series, we explored Visual Studio 2026 GUI publishing—the most accessible path to containerized AWS deployments for .NET developers. While GUI tooling prioritizes developer productivity, many organizations face a different priority: **security**. In regulated industries like finance, healthcare, and government, container images cannot be pushed directly to Amazon ECR without passing through rigorous security gates—vulnerability scanning, license compliance checks, and approval workflows.

This is where **tarball export** becomes indispensable on AWS. By decoupling image creation from image distribution, the .NET SDK's tarball export capability enables security-first CI/CD pipelines where images are built, scanned, approved, and only then loaded into production registries. For Vehixcare-API—our fleet management platform handling sensitive vehicle telemetry and driver behavior data—this security-first approach is not optional; it's mandatory for FedRAMP and HIPAA compliance.

This installment explores the complete security-first workflow for AWS: generating container tarballs without a container runtime, integrating with Amazon Inspector for vulnerability scanning, implementing approval gates with AWS CodePipeline, and deploying to air-gapped AWS environments like AWS GovCloud and AWS Outposts. We'll demonstrate how tarball export transforms container delivery from a continuous push model to a controlled, auditable supply chain.

```mermaid
graph LR
    subgraph "Build Phase (Isolated Network)"
        A[dotnet publish] --> B[Container Tarball]
        B --> C[Amazon S3 Artifact Storage]
    end
    
    subgraph "Security Phase (Security Account)"
        C --> D[Amazon Inspector Scan]
        C --> E[Grype License Scan]
        C --> F[Syft SBOM Generation]
        D --> G{Security Gate}
        E --> G
        F --> G
    end
    
    subgraph "Deployment Phase (Production Account)"
        G -->|Approved| H[Load into Podman/Docker]
        G -->|Rejected| I[Return to Dev]
        H --> J[Push to Amazon ECR]
        J --> K[AWS Deployment ECS/EKS]
    end
    
    style B fill:#e53e3e,color:#fff
    style D fill:#ff9900,color:#fff
    style G fill:#ed8936,color:#fff
    style J fill:#48bb78,color:#fff
```

### Stories at a Glance

**Complete AWS series (10 stories):**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference - AWS** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides for Amazon ECR

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker - AWS** – A deep dive into MSBuild configuration, multi-architecture builds (Graviton ARM64), and direct Amazon ECR integration with IAM roles

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach - AWS** – Mastering multi-stage builds, build cache optimization, and Amazon ECR authentication for enterprise CI/CD pipelines on AWS

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative - AWS** – Transitioning from Docker to Podman, rootless containers for enhanced security, and Amazon ECR integration with Podman Desktop

- 🏗️ **5. AWS CDK & Copilot: Infrastructure as Code for Containers - AWS** – Deploying to Amazon ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless container orchestration

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop AWS Deployments - AWS** – Leveraging Visual Studio's AWS Toolkit, one-click publish to Amazon ECR, and debugging containerized apps on AWS

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs without a runtime, integrating with Amazon Inspector for vulnerability scanning, and deploying to air-gapped AWS environments *(This story)*

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows - AWS** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation (x64 to Graviton), and Amazon ECR push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker - AWS** – Using the konet .NET tool for cross-platform image generation, AMD64/ARM64 (Graviton) simultaneous builds, and AWS CodeBuild optimization

- ☸️ **10. Kubernetes Native Deployments: Orchestrating .NET 10 Containers on Amazon EKS - AWS** – Deploying to Amazon EKS, Helm charts, GitOps with Flux, ALB Ingress Controller, and production-grade operations

---

## Understanding Tarball Export for AWS

### What Is a Container Tarball?

A container tarball is a portable archive containing a complete OCI (Open Container Initiative) image. Unlike Docker images stored in a local daemon, tarballs are **self-contained files** that can be:

- Stored in Amazon S3 for artifact management
- Transferred across air-gapped networks (GovCloud, Outposts)
- Scanned by Amazon Inspector for vulnerabilities
- Signed for supply chain integrity with AWS Signer
- Loaded into any OCI-compliant runtime on AWS

### Tarball Structure for AWS

```bash
# Extract and examine a container tarball
tar -xzf vehixcare-api.tar.gz
tree vehixcare-api/

vehixcare-api/
├── blobs/
│   └── sha256/
│       ├── a1b2c3d4e5f6...  # Base OS layer (Amazon Linux 2)
│       ├── b2c3d4e5f6g7...  # .NET runtime layer
│       ├── c3d4e5f6g7h8...  # Application layer
│       └── d4e5f6g7h8i9...  # Image configuration
├── index.json               # Image index (points to manifest)
└── oci-layout               # Version marker
```

### Why Tarball Export Matters for AWS Security

| Security Requirement | Direct Push to ECR | Tarball Export | AWS Compliance Impact |
|---------------------|-------------------|----------------|----------------------|
| **Vulnerability Scanning** | After push (remediation harder) | Before push (block at source) | FedRAMP requirement |
| **License Compliance** | After push | Before push | HIPAA requirement |
| **SBOM Generation** | Optional | Mandatory in workflow | Executive Order 14028 |
| **Image Signing** | Possible | Enforced before loading | NIST SP 800-190 |
| **Air-Gapped Deployments** | Impossible | Native support | GovCloud/Outposts |
| **Approval Workflows** | Complex | Built-in | DoD Impact Level |

---

## Generating Container Tarballs for AWS

### Basic Tarball Export

```bash
# Generate tarball without pushing to ECR
dotnet publish Vehixcare.API/Vehixcare.API.csproj \
    --os linux \
    --arch x64 \
    -c Release \
    /t:PublishContainer \
    -p ContainerArchiveOutputPath=./output/vehixcare-api.tar.gz
```

### Compressed vs. Uncompressed Tarballs

```bash
# Uncompressed OCI layout directory (for scanning)
dotnet publish /t:PublishContainer \
    -p ContainerArchiveOutputPath=./output/vehixcare-api-oci

# Compressed tarball (recommended for S3 storage)
dotnet publish /t:PublishContainer \
    -p ContainerArchiveOutputPath=./output/vehixcare-api.tar.gz
```

### Multi-Architecture Tarball Export for AWS

```bash
# Export for x64 (Intel/AMD EC2)
dotnet publish /t:PublishContainer \
    --arch x64 \
    -p ContainerArchiveOutputPath=./output/vehixcare-api-amd64.tar.gz

# Export for ARM64 (AWS Graviton)
dotnet publish /t:PublishContainer \
    --arch arm64 \
    -p ContainerArchiveOutputPath=./output/vehixcare-api-arm64.tar.gz

# Create multi-arch manifest tarball (requires Docker/Podman)
docker manifest create vehixcare-api:latest \
    vehixcare-api-amd64:latest \
    vehixcare-api-arm64:latest

docker manifest push vehixcare-api:latest
docker save vehixcare-api:latest -o vehixcare-api-multiarch.tar
```

### Store Tarball in Amazon S3

```bash
# Create S3 bucket for artifact storage
aws s3 mb s3://vehixcare-artifacts --region us-east-1

# Upload tarball
aws s3 cp ./output/vehixcare-api.tar.gz \
    s3://vehixcare-artifacts/images/vehixcare-api-$(date +%Y%m%d-%H%M%S).tar.gz

# Enable versioning for audit trail
aws s3api put-bucket-versioning \
    --bucket vehixcare-artifacts \
    --versioning-configuration Status=Enabled
```

---

## Security Scanning Workflow with AWS Services

### Comprehensive Scanning Pipeline

```mermaid
graph TD
    subgraph "Build"
        A[Tarball] --> B[Upload to S3]
    end
    
    subgraph "AWS Security Services"
        B --> C[Amazon Inspector]
        B --> D[AWS CodeBuild with Grype]
        B --> E[AWS CodeBuild with Syft]
        
        C --> C1[OS Vulnerabilities]
        C --> C2[.NET Library CVEs]
        C --> C3[Critical Severity Scan]
        
        D --> D1[License Detection]
        D --> D2[Risk Assessment]
        
        E --> E1[SPDX SBOM]
        E --> E2[CycloneDX SBOM]
    end
    
    subgraph "Policy Enforcement"
        C1 --> F{AWS Config Rules}
        C2 --> F
        C3 --> F
        D1 --> F
        E1 --> F
    end
```

### Step 1: Amazon Inspector Vulnerability Scanning

Amazon Inspector is AWS's native vulnerability management service that scans container images:

```bash
# Enable Amazon Inspector
aws inspector2 enable --resource-types ECR

# Create scan configuration
aws inspector2 create-filter \
    --name vehixcare-critical \
    --filter-action SUPPRESS \
    --filter-criteria '{
        "severity": [{"comparison": "EQUALS", "value": "CRITICAL"}],
        "resourceType": [{"comparison": "EQUALS", "value": "AWS_ECR_CONTAINER_IMAGE"}]
    }'

# Scan tarball (must be loaded to ECR first)
# Alternatively, use Amazon Inspector on ECR after push
```

**Scanning with Amazon Inspector via ECR:**

```bash
# Create temporary ECR repository for scanning
aws ecr create-repository --repository-name temp-scan

# Load tarball to temporary repository
podman load -i ./output/vehixcare-api.tar.gz
podman tag vehixcare-api:latest $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/temp-scan:scan
podman push $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/temp-scan:scan

# Wait for Inspector to scan (usually 2-5 minutes)
aws inspector2 list-findings --filter-criteria '{
    "resourceType": [{"comparison": "EQUALS", "value": "AWS_ECR_CONTAINER_IMAGE"}],
    "severity": [{"comparison": "EQUALS", "value": "CRITICAL"}]
}'

# Get scan results
aws inspector2 get-findings --finding-arns arn:aws:inspector2:us-east-1:123456789012:finding/xxxxx

# Clean up temporary repository
aws ecr delete-repository --repository-name temp-scan --force
```

### Step 2: License Compliance with Grype on AWS CodeBuild

```yaml
# buildspec-license-scan.yml
version: 0.2

phases:
  install:
    runtime-versions:
      dotnet: 9.0
    commands:
      - echo "Installing Grype..."
      - curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
      - grype version

  build:
    commands:
      - echo "Downloading tarball from S3..."
      - aws s3 cp s3://vehixcare-artifacts/images/vehixcare-api-latest.tar.gz ./image.tar.gz
      
      - echo "Running Grype license scan..."
      - grype ./image.tar.gz \
          --fail-on high \
          --output json \
          > grype-results.json
      
      - echo "Checking for restricted licenses..."
      - DENIED_COUNT=$(jq '.matches[] | select(.artifact.licenses[] | .value == "GPL-3.0" or .value == "AGPL-3.0")' grype-results.json | wc -l)
      - if [ $DENIED_COUNT -gt 0 ]; then
          echo "Found $DENIED_COUNT restricted licenses!";
          exit 1;
        else
          echo "License scan passed";
        fi

artifacts:
  files:
    - grype-results.json
  discard-paths: yes
```

### Step 3: SBOM Generation with Syft

```yaml
# buildspec-sbom.yml
version: 0.2

phases:
  install:
    commands:
      - echo "Installing Syft..."
      - curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
      - syft version

  build:
    commands:
      - echo "Downloading tarball..."
      - aws s3 cp s3://vehixcare-artifacts/images/vehixcare-api-latest.tar.gz ./image.tar.gz
      
      - echo "Generating SPDX SBOM..."
      - syft ./image.tar.gz -o spdx-json > sbom.spdx.json
      
      - echo "Generating CycloneDX SBOM..."
      - syft ./image.tar.gz -o cyclonedx-json > sbom.cyclonedx.json
      
      - echo "Uploading SBOM to S3..."
      - aws s3 cp sbom.spdx.json s3://vehixcare-artifacts/sboms/
      - aws s3 cp sbom.cyclonedx.json s3://vehixcare-artifacts/sboms/

artifacts:
  files:
    - sbom.spdx.json
    - sbom.cyclonedx.json
```

### Step 4: Image Signing with AWS Signer

AWS Signer provides code signing for container images:

```bash
# Create signing profile
aws signer put-signing-profile \
    --profile-name vehixcare-images \
    --platform-id AWSLambda-SHA384-ECDSA

# Sign the image (after loading to ECR)
aws signer start-signing-job \
    --source '{
        "s3": {
            "bucketName": "vehixcare-artifacts",
            "key": "images/vehixcare-api-latest.tar.gz",
            "version": "1"
        }
    }' \
    --destination '{
        "s3": {
            "bucketName": "vehixcare-artifacts",
            "prefix": "signed/"
        }
    }' \
    --profile-name vehixcare-images

# Verify signature
aws signer describe-signing-job \
    --job-id xxxxx-xxxxx-xxxxx
```

---

## Complete CI/CD Pipeline with AWS CodePipeline

### Step 1: Build Stage with Tarball Export

```yaml
# buildspec-build.yml
version: 0.2

env:
  variables:
    DOTNET_VERSION: "9.0"
    IMAGE_NAME: "vehixcare-api"

phases:
  install:
    runtime-versions:
      dotnet: $DOTNET_VERSION
    commands:
      - echo "Installing .NET SDK..."
      - dotnet --version

  build:
    commands:
      - echo "Building application..."
      - dotnet restore
      - dotnet build -c Release
      
      - echo "Exporting container tarball..."
      - dotnet publish Vehixcare.API/Vehixcare.API.csproj \
          --os linux \
          --arch x64 \
          -c Release \
          /t:PublishContainer \
          -p ContainerArchiveOutputPath=./output/$IMAGE_NAME.tar.gz \
          -p ContainerImageTag=$CODEBUILD_RESOLVED_SOURCE_VERSION

  post_build:
    commands:
      - echo "Uploading tarball to S3..."
      - aws s3 cp ./output/$IMAGE_NAME.tar.gz s3://vehixcare-artifacts/images/$IMAGE_NAME-$CODEBUILD_RESOLVED_SOURCE_VERSION.tar.gz
      - aws s3 cp ./output/$IMAGE_NAME.tar.gz s3://vehixcare-artifacts/images/$IMAGE_NAME-latest.tar.gz

artifacts:
  files:
    - output/*.tar.gz
  discard-paths: yes
```

### Step 2: Security Scanning Stage

```yaml
# buildspec-security.yml
version: 0.2

phases:
  install:
    commands:
      - echo "Installing security tools..."
      - curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
      - curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

  pre_build:
    commands:
      - echo "Downloading image from S3..."
      - aws s3 cp s3://vehixcare-artifacts/images/vehixcare-api-latest.tar.gz ./image.tar.gz

  build:
    commands:
      - echo "Running vulnerability scan..."
      - grype ./image.tar.gz --fail-on high --output json > grype-results.json
      
      - echo "Generating SBOM..."
      - syft ./image.tar.gz -o spdx-json > sbom.spdx.json
      
      - echo "Checking security gates..."
      - CRITICAL_COUNT=$(jq '.matches[] | select(.vulnerability.severity == "Critical")' grype-results.json | wc -l)
      - if [ $CRITICAL_COUNT -gt 0 ]; then
          echo "Found $CRITICAL_COUNT critical vulnerabilities!";
          exit 1;
        else
          echo "Security scan passed";
        fi

  post_build:
    commands:
      - echo "Uploading scan results..."
      - aws s3 cp grype-results.json s3://vehixcare-artifacts/scan-results/
      - aws s3 cp sbom.spdx.json s3://vehixcare-artifacts/sboms/

artifacts:
  files:
    - grype-results.json
    - sbom.spdx.json
```

### Step 3: Approval Stage (Manual)

```yaml
# CodePipeline approval stage
# Defined in CloudFormation/CDK
```

### Step 4: Load and Push to ECR

```yaml
# buildspec-deploy.yml
version: 0.2

phases:
  install:
    commands:
      - echo "Installing Podman..."
      - sudo yum install podman -y
      - podman --version

  pre_build:
    commands:
      - echo "Downloading approved tarball..."
      - aws s3 cp s3://vehixcare-artifacts/images/vehixcare-api-latest.tar.gz ./image.tar.gz
      
      - echo "Logging into Amazon ECR..."
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | podman login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com

  build:
    commands:
      - echo "Loading image into Podman..."
      - podman load -i ./image.tar.gz
      
      - echo "Tagging image for ECR..."
      - podman tag vehixcare-api:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/vehixcare-api:$CODEBUILD_RESOLVED_SOURCE_VERSION
      - podman tag vehixcare-api:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/vehixcare-api:approved
      
      - echo "Pushing to ECR..."
      - podman push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/vehixcare-api:$CODEBUILD_RESOLVED_SOURCE_VERSION
      - podman push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/vehixcare-api:approved

  post_build:
    commands:
      - echo "Deployment complete!"
```

---

## Air-Gapped Deployments with AWS Outposts and GovCloud

### Transferring Tarballs Across Air-Gapped Networks

For AWS GovCloud, AWS Outposts, or air-gapped environments:

```mermaid
graph LR
    A[Build Network<br/>Commercial AWS] -->|Export| B[vehixcare-api.tar.gz]
    B -->|AWS Snowball| C[Air-Gapped Network<br/>GovCloud/Outposts]
    C -->|Load| D[Podman/Docker]
    D -->|Push| E[Local ECR]
    E -->|Deploy| F[ECS/EKS on Outposts]
```

### Deploying to AWS Outposts

```bash
# On Outpost (air-gapped network)
# 1. Transfer tarball via Snowball or physical media
# 2. Load image
podman load -i /media/vehixcare-api.tar.gz

# 3. Push to Outpost ECR
podman tag vehixcare-api:latest $OUTPOST_ACCOUNT.dkr.ecr.$REGION.outposts.amazonaws.com/vehixcare-api:latest
podman push $OUTPOST_ACCOUNT.dkr.ecr.$REGION.outposts.amazonaws.com/vehixcare-api:latest

# 4. Deploy to ECS on Outpost
aws ecs create-service \
    --cluster vehixcare-outpost-cluster \
    --service-name vehixcare-api \
    --task-definition vehixcare-api \
    --desired-count 3
```

### AWS GovCloud Deployment

```bash
# Configure GovCloud profile
aws configure --profile govcloud
AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name: us-gov-west-1

# Load and push to GovCloud ECR
podman load -i ./vehixcare-api.tar.gz
podman tag vehixcare-api:latest $GOV_ACCOUNT.dkr.ecr.us-gov-west-1.amazonaws.com/vehixcare-api:latest
podman push $GOV_ACCOUNT.dkr.ecr.us-gov-west-1.amazonaws.com/vehixcare-api:latest
```

---

## AWS CodePipeline with Approval Gates

### CloudFormation Pipeline with Security Gates

```yaml
# pipeline.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Vehixcare Secure CI/CD Pipeline

Resources:
  VehixcarePipeline:
    Type: AWS::CodePipeline::Pipeline
    Properties:
      Name: vehixcare-secure-pipeline
      RoleArn: arn:aws:iam::123456789012:role/CodePipelineRole
      Stages:
        - Name: Source
          Actions:
            - Name: Source
              ActionTypeId:
                Category: Source
                Owner: AWS
                Provider: CodeCommit
                Version: 1
              Configuration:
                RepositoryName: vehixcare-repo
                BranchName: main
              OutputArtifacts:
                - Name: SourceArtifact
        
        - Name: Build
          Actions:
            - Name: BuildImage
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: 1
              Configuration:
                ProjectName: vehixcare-build
              InputArtifacts:
                - Name: SourceArtifact
              OutputArtifacts:
                - Name: BuildArtifact
        
        - Name: SecurityScan
          Actions:
            - Name: ScanImage
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: 1
              Configuration:
                ProjectName: vehixcare-security-scan
              InputArtifacts:
                - Name: BuildArtifact
              OutputArtifacts:
                - Name: ScanArtifact
        
        - Name: Approval
          Actions:
            - Name: ManualApproval
              ActionTypeId:
                Category: Approval
                Owner: AWS
                Provider: Manual
                Version: 1
              Configuration:
                NotificationArn: arn:aws:sns:us-east-1:123456789012:vehixcare-approval-topic
              RunOrder: 1
        
        - Name: Deploy
          Actions:
            - Name: DeployToECR
              ActionTypeId:
                Category: Build
                Owner: AWS
                Provider: CodeBuild
                Version: 1
              Configuration:
                ProjectName: vehixcare-deploy
              InputArtifacts:
                - Name: BuildArtifact
```

---

## Compliance Frameworks on AWS

### NIST SP 800-190 Compliance

NIST SP 800-190 (Container Security) requirements mapped to AWS services:

| Requirement | AWS Implementation | Verification |
|-------------|-------------------|--------------|
| **Image Scanning** | Amazon Inspector | Scan before deployment |
| **SBOM Generation** | Syft + S3 | SPDX/ CycloneDX stored |
| **Vulnerability Management** | Amazon Inspector + AWS Security Hub | Block CRITICAL findings |
| **Image Signing** | AWS Signer | Verify signatures |
| **Least Privilege** | IAM Roles | Non-root user in container |
| **Audit Trail** | AWS CloudTrail | All API calls logged |

### FedRAMP Compliance for Vehixcare

```bash
# FedRAMP High requirements
# 1. Image must be scanned for vulnerabilities
aws inspector2 list-findings --filter-criteria '{
    "severity": [{"comparison": "EQUALS", "value": "CRITICAL"}],
    "findingStatus": [{"comparison": "EQUALS", "value": "ACTIVE"}]
}'
# Must return 0 findings

# 2. SBOM must be generated and stored
aws s3 ls s3://vehixcare-artifacts/sboms/
# sbom.spdx.json must exist

# 3. Image must be signed
aws signer list-signing-jobs --status Succeeded
# Must have recent signing job

# 4. Audit logs must be enabled
aws cloudtrail describe-trails
# Must have trail for all regions
```

---

## Troubleshooting Security Pipelines

### Issue 1: Amazon Inspector Not Finding Images

**Error:** `No findings found for image`

**Solution:**
```bash
# Verify ECR scanning is enabled
aws ecr describe-repositories --repository-name vehixcare-api | \
    jq '.repositories[0].imageScanningConfiguration'

# Enable scanning
aws ecr put-image-scanning-configuration \
    --repository-name vehixcare-api \
    --image-scanning-configuration scanOnPush=true

# Wait for scan to complete (5-10 minutes)
aws ecr describe-image-scan-findings \
    --repository-name vehixcare-api \
    --image-id imageTag=latest
```

### Issue 2: Grype Fails with Large Tarball

**Error:** `Error: failed to parse image: context deadline exceeded`

**Solution:**
```bash
# Increase memory for CodeBuild
# buildspec.yml
env:
  compute-type: BUILD_GENERAL1_LARGE
  phases:
    build:
      commands:
        - export GRYPE_MAX_CONTAINER_SIZE=2G
        - grype ./image.tar.gz --timeout 5m
```

### Issue 3: SBOM Generation Fails

**Error:** `Error: unable to generate SBOM`

**Solution:**
```bash
# Validate tarball integrity
tar -tzf ./image.tar.gz | head -10
# Should show blobs/ and index.json

# Regenerate tarball if corrupted
dotnet publish /t:PublishContainer \
    -p ContainerArchiveOutputPath=./output/vehixcare-api.tar.gz
```

---

## Performance Metrics

| Step | Time | Notes |
|------|------|-------|
| **dotnet publish (tarball)** | 45-60s | No container runtime |
| **S3 Upload** | 10-20s | Depends on image size |
| **Amazon Inspector Scan** | 2-5 minutes | Automatic after ECR push |
| **Grype Scan** | 30-60s | License analysis |
| **Syft SBOM** | 15-30s | Generation |
| **Tarball Transfer** | Variable | Network/air-gap dependent |
| **Load + Push to ECR** | 15-20s | Runtime required |

---

## Conclusion: Security as Code on AWS

Tarball export transforms container delivery from an uncontrolled push model to a controlled, auditable supply chain on AWS. For Vehixcare-API, this security-first approach ensures:

- **No vulnerable images reach production** – Blocked by Amazon Inspector
- **Complete supply chain visibility** – SBOMs for every image in S3
- **License compliance** – Automated detection of restricted licenses
- **Air-gapped support** – Deploy to GovCloud and Outposts
- **Audit trail** – Every image is scanned, signed, and approved
- **FedRAMP compliance** – Meets federal security requirements

While direct registry pushes offer convenience, security-first organizations require the control and visibility that tarball export provides. By integrating Amazon Inspector, Grype, Syft, and AWS Signer into your CI/CD pipeline, you can achieve the same level of security automation that major government and enterprise organizations require.

---

### Stories at a Glance

**Complete AWS series (10 stories):**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference - AWS** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides for Amazon ECR

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker - AWS** – A deep dive into MSBuild configuration, multi-architecture builds (Graviton ARM64), and direct Amazon ECR integration with IAM roles

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach - AWS** – Mastering multi-stage builds, build cache optimization, and Amazon ECR authentication for enterprise CI/CD pipelines on AWS

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative - AWS** – Transitioning from Docker to Podman, rootless containers for enhanced security, and Amazon ECR integration with Podman Desktop

- 🏗️ **5. AWS CDK & Copilot: Infrastructure as Code for Containers - AWS** – Deploying to Amazon ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless container orchestration

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop AWS Deployments - AWS** – Leveraging Visual Studio's AWS Toolkit, one-click publish to Amazon ECR, and debugging containerized apps on AWS

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs without a runtime, integrating with Amazon Inspector for vulnerability scanning, and deploying to air-gapped AWS environments *(This story)*

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows - AWS** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation (x64 to Graviton), and Amazon ECR push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker - AWS** – Using the konet .NET tool for cross-platform image generation, AMD64/ARM64 (Graviton) simultaneous builds, and AWS CodeBuild optimization

- ☸️ **10. Kubernetes Native Deployments: Orchestrating .NET 10 Containers on Amazon EKS - AWS** – Deploying to Amazon EKS, Helm charts, GitOps with Flux, ALB Ingress Controller, and production-grade operations

---

## What's Next?

Over the coming weeks, each approach in this AWS series will be explored in exhaustive detail. We'll examine real-world AWS deployment scenarios, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first containerized application on AWS Fargate or an enterprise migrating thousands of workloads to Amazon EKS, you'll find practical guidance tailored to your infrastructure requirements.

The evolution from push-based deployments to security-first, air-gapped workflows reflects a maturing ecosystem where .NET 10 stands at the forefront of secure container development on AWS. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from rapid prototyping to FedRAMP-compliant production deployments.

**Coming next in the series:**
**🔄 Podman with .NET SDK Native Publishing: Hybrid Workflows - AWS** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation (x64 to Graviton), and Amazon ECR push strategies