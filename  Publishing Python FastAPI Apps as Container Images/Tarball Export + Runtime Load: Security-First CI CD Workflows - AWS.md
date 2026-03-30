# Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS

## Building Secure Python Container Pipelines with Amazon Inspector and Air-Gapped Deployments

### Introduction: The Security Imperative for Python Applications on AWS

In the [previous installment](#) of this AWS Python series, we explored AWS App Runner—the fully managed container service that eliminates infrastructure management entirely. While App Runner prioritizes developer velocity, many organizations face a different priority: **security**. In regulated industries like finance, healthcare, and government, container images cannot be pushed directly to registries without passing through rigorous security gates—vulnerability scanning, license compliance checks, and approval workflows.

For the **AI Powered Video Tutorial Portal**—a FastAPI application handling user authentication, API keys, course content, and user engagement data—this security-first approach is not optional; it's mandatory for compliance frameworks like HIPAA, PCI DSS, and FedRAMP on AWS.

This is where **tarball export** becomes indispensable. By decoupling image creation from image distribution, the Docker `save`/`load` workflow enables security-first CI/CD pipelines where images are built, scanned, approved, and only then loaded into production registries. This installment explores the complete security-first workflow for Python FastAPI applications on AWS: generating container tarballs, integrating with Amazon Inspector and third-party scanners (Trivy, Grype, Syft), implementing approval gates, and deploying to air-gapped AWS environments like AWS GovCloud and AWS Outposts.

```mermaid
graph LR
    subgraph "Build Phase (Isolated Network)"
        A[docker build] --> B[Container Tarball]
        B --> C[Amazon S3 Artifact Storage]
    end
    
    subgraph "Security Phase (Security Account)"
        C --> D[Amazon Inspector Scan]
        C --> E[Trivy Scan]
        C --> F[Grype License Scan]
        C --> G[Syft SBOM Generation]
        D --> H{Security Gate}
        E --> H
        F --> H
        G --> H
    end
    
    subgraph "Deployment Phase (Production Account)"
        H -->|Approved| I[Load into Docker/Podman]
        H -->|Rejected| J[Return to Dev]
        I --> K[Push to Amazon ECR]
        K --> L[AWS Deployment ECS/EKS/App Runner]
    end
    
    style B fill:#e53e3e,color:#fff
    style D fill:#ff9900,color:#fff
    style H fill:#ed8936,color:#fff
    style K fill:#48bb78,color:#fff
```

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments *(This story)*

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## Understanding Tarball Export for Python Containers on AWS

### What Is a Container Tarball?

A container tarball is a portable archive containing a complete OCI (Open Container Initiative) image. Unlike Docker images stored in a local daemon, tarballs are **self-contained files** that can be:

- Stored in Amazon S3 for artifact management
- Transferred across air-gapped networks (AWS GovCloud, AWS Outposts)
- Scanned by Amazon Inspector for vulnerabilities
- Signed for supply chain integrity with AWS Signer
- Loaded into any OCI-compliant runtime on AWS

### Tarball Structure for Python Applications

```bash
# Extract and examine a container tarball
tar -xzf courses-api.tar.gz
tree courses-api/

courses-api/
├── blobs/
│   └── sha256/
│       ├── a1b2c3d4e5f6...  # Base OS layer (Amazon Linux 2)
│       ├── b2c3d4e5f6g7...  # Python runtime layer
│       ├── c3d4e5f6g7h8...  # Python dependencies layer
│       └── d4e5f6g7h8i9...  # Application code layer
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
| **Air-Gapped Deployments** | Impossible | Native support | AWS GovCloud/Outposts |
| **Approval Workflows** | Complex | Built-in | DoD Impact Level |

---

## Generating Container Tarballs for Python on AWS

### Building and Exporting Tarball

```bash
# Build the FastAPI container image
docker build -t courses-api:latest -f Dockerfile .

# Save the image as a tarball
docker save courses-api:latest -o courses-api.tar

# Compress for storage (recommended for S3)
gzip courses-api.tar
# Creates courses-api.tar.gz

# Verify tarball contents
tar -tzf courses-api.tar.gz | head -10
# blobs/
# blobs/sha256/
# blobs/sha256/a1b2c3...
# index.json
# oci-layout
```

### Multi-Architecture Tarball Export for Graviton

```bash
# Build for multiple architectures
docker build --platform linux/amd64 -t courses-api:amd64 -f Dockerfile .
docker build --platform linux/arm64 -t courses-api:arm64 -f Dockerfile .

# Save as separate tarballs
docker save courses-api:amd64 -o courses-api-amd64.tar
docker save courses-api:arm64 -o courses-api-arm64.tar

# Create multi-arch manifest tarball
docker manifest create courses-api:latest \
    courses-api:amd64 \
    courses-api:arm64

docker save courses-api:latest -o courses-api-multiarch.tar
```

### Store Tarball in Amazon S3

```bash
# Create S3 bucket for artifact storage
aws s3 mb s3://courses-portal-artifacts --region us-east-1

# Enable versioning for audit trail
aws s3api put-bucket-versioning \
    --bucket courses-portal-artifacts \
    --versioning-configuration Status=Enabled

# Upload tarball
aws s3 cp courses-api.tar.gz \
    s3://courses-portal-artifacts/images/courses-api-$(date +%Y%m%d-%H%M%S).tar.gz

# Set lifecycle policy for older artifacts
aws s3api put-bucket-lifecycle-configuration \
    --bucket courses-portal-artifacts \
    --lifecycle-configuration '{
        "Rules": [{
            "Status": "Enabled",
            "Prefix": "images/",
            "Expiration": {
                "Days": 90
            }
        }]
    }'
```

---

## Security Scanning Workflow on AWS

### Comprehensive Scanning Pipeline

```mermaid
graph TD
    subgraph "Build"
        A[Tarball] --> B[Upload to S3]
    end
    
    subgraph "AWS Security Services"
        B --> C[Amazon Inspector]
        B --> D[AWS CodeBuild with Trivy]
        B --> E[AWS CodeBuild with Grype]
        B --> F[AWS CodeBuild with Syft]
        
        C --> C1[OS Vulnerabilities]
        C --> C2[Python Library CVEs]
        C --> C3[Critical Severity Scan]
        
        D --> D1[License Detection]
        D --> D2[Risk Assessment]
        
        E --> E1[SPDX SBOM]
        E --> E2[CycloneDX SBOM]
    end
    
    subgraph "Policy Enforcement"
        C1 --> G{AWS Config Rules}
        C2 --> G
        C3 --> G
        D1 --> G
        E1 --> G
    end
```

### Step 1: Amazon Inspector Vulnerability Scanning

Amazon Inspector is AWS's native vulnerability management service that scans container images:

```bash
# Enable Amazon Inspector
aws inspector2 enable --resource-types ECR

# Create a temporary ECR repository for scanning
aws ecr create-repository --repository-name temp-scan

# Load tarball to temporary repository
docker load -i courses-api.tar.gz
docker tag courses-api:latest $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/temp-scan:scan
docker push $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/temp-scan:scan

# Wait for Inspector to scan (usually 2-5 minutes)
aws inspector2 list-findings --filter-criteria '{
    "resourceType": [{"comparison": "EQUALS", "value": "AWS_ECR_CONTAINER_IMAGE"}],
    "severity": [{"comparison": "EQUALS", "value": "CRITICAL"}]
}'

# Get detailed scan results
aws inspector2 get-findings --finding-arns arn:aws:inspector2:us-east-1:123456789012:finding/xxxxx

# Clean up temporary repository
aws ecr delete-repository --repository-name temp-scan --force
```

### Step 2: Vulnerability Scanning with Trivy

Trivy (from Aqua Security) provides comprehensive vulnerability scanning:

```bash
# Install Trivy on EC2 or CodeBuild
wget https://github.com/aquasecurity/trivy/releases/download/v0.48.0/trivy_0.48.0_Linux-64bit.deb
sudo dpkg -i trivy_0.48.0_Linux-64bit.deb

# Scan tarball directly
trivy image --input courses-api.tar.gz \
    --severity HIGH,CRITICAL \
    --format sarif \
    --output trivy-results.sarif \
    --exit-code 1 \
    --ignore-unfixed \
    --vuln-type os,library \
    --scanners vuln,secret,config
```

**Sample Output:**
```
courses-api.tar.gz (debian 12.0)
===================================
Total: 42 vulnerabilities (UNKNOWN: 0, LOW: 15, MEDIUM: 18, HIGH: 7, CRITICAL: 2)

┌───────────────┬────────────────┬──────────┬───────────────────┬───────────────┐
│    Library    │ Vulnerability  │ Severity │  Installed Version│ Fixed Version │
├───────────────┼────────────────┼──────────┼───────────────────┼───────────────┤
│ libc6         │ CVE-2023-4911  │ HIGH     │ 2.36-9+deb12u1    │ 2.36-9+deb12u2│
│ python3.11    │ CVE-2023-40217 │ HIGH     │ 3.11.2-6          │ 3.11.2-7      │
│ cryptography  │ CVE-2023-38325 │ CRITICAL │ 41.0.0            │ 41.0.1        │
└───────────────┴────────────────┴──────────┴───────────────────┴───────────────┘
```

### Step 3: License Compliance with Grype

Grype (from Anchore) identifies software licenses and compliance issues:

```bash
# Install Grype
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin

# Scan tarball
grype courses-api.tar.gz \
    --fail-on high \
    --output table \
    --only-fixed \
    --scope all-layers
```

**Sample Output:**
```
NAME              INSTALLED   LICENSES      VULNERABILITIES
fastapi           0.104.0     MIT           (none)
pydantic          2.5.0       MIT           (none)
motor             3.3.0       Apache-2.0    (1 medium)
redis             5.0.0       MIT           (none)
cryptography      41.0.0      BSD-3-Clause  (1 critical)

License Summary:
- MIT: 12 packages (allowed)
- Apache-2.0: 3 packages (allowed)
- BSD-3-Clause: 1 package (allowed)
- GPL-3.0: 0 packages
```

### Step 4: SBOM Generation with Syft

Syft generates Software Bill of Materials (SBOM) in industry-standard formats:

```bash
# Install Syft
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

# Generate SPDX SBOM
syft courses-api.tar.gz \
    -o spdx-json \
    > sbom-courses-api.spdx.json

# Generate CycloneDX SBOM
syft courses-api.tar.gz \
    -o cyclonedx-json \
    > sbom-courses-api.cyclonedx.json

# Upload SBOM to S3 for audit
aws s3 cp sbom-courses-api.spdx.json \
    s3://courses-portal-artifacts/sboms/sbom-$(date +%Y%m%d).spdx.json
```

---

## AWS CodeBuild Security Pipeline

### buildspec-security.yml

```yaml
# buildspec-security.yml
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.11
      docker: 20
    commands:
      - echo "Installing security tools..."
      # Install Trivy
      - wget https://github.com/aquasecurity/trivy/releases/download/v0.48.0/trivy_0.48.0_Linux-64bit.deb
      - sudo dpkg -i trivy_0.48.0_Linux-64bit.deb
      # Install Grype
      - curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
      # Install Syft
      - curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

  pre_build:
    commands:
      - echo "Building Docker image..."
      - docker build -t courses-api:scan .
      - echo "Saving image as tarball..."
      - docker save courses-api:scan -o courses-api.tar
      - gzip courses-api.tar

  build:
    commands:
      - echo "Running security scans..."
      
      # Trivy scan
      - trivy image --input courses-api.tar.gz --severity HIGH,CRITICAL --format sarif --output trivy-results.sarif --exit-code 1
      
      # Grype license scan
      - grype courses-api.tar.gz --fail-on high --output json > grype-results.json
      
      # Check for restricted licenses
      - DENIED_COUNT=$(jq '.matches[] | select(.artifact.licenses[] | .value == "GPL-3.0" or .value == "AGPL-3.0")' grype-results.json | wc -l)
      - |
        if [ $DENIED_COUNT -gt 0 ]; then
          echo "Found $DENIED_COUNT restricted licenses!"
          exit 1
        fi
      
      # Generate SBOM
      - syft courses-api.tar.gz -o spdx-json > sbom.spdx.json

  post_build:
    commands:
      - echo "Uploading artifacts to S3..."
      - aws s3 cp courses-api.tar.gz s3://courses-portal-artifacts/images/courses-api-$CODEBUILD_RESOLVED_SOURCE_VERSION.tar.gz
      - aws s3 cp trivy-results.sarif s3://courses-portal-artifacts/scan-results/
      - aws s3 cp sbom.spdx.json s3://courses-portal-artifacts/sboms/

artifacts:
  files:
    - courses-api.tar.gz
    - sbom.spdx.json
    - trivy-results.sarif
```

---

## Complete CI/CD Pipeline with Security Gates

### GitHub Actions Security-First Pipeline

```yaml
# .github/workflows/secure-deploy.yml
name: Secure Python Container Build and Deploy to AWS

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AWS_ACCOUNT_ID: 123456789012
  AWS_REGION: us-east-1
  ECR_REPOSITORY: courses-api

jobs:
  secure-build:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
      security-events: write
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Run Python tests
      run: |
        pip install -r requirements.txt
        pytest tests/ --cov=./

    - name: Build Docker image
      run: |
        docker build -t ${{ env.ECR_REPOSITORY }}:${{ github.sha }} .
        docker save ${{ env.ECR_REPOSITORY }}:${{ github.sha }} -o image.tar
        gzip image.tar

    - name: Install security tools
      run: |
        # Install Trivy
        wget https://github.com/aquasecurity/trivy/releases/download/v0.48.0/trivy_0.48.0_Linux-64bit.deb
        sudo dpkg -i trivy_0.48.0_Linux-64bit.deb
        # Install Grype
        curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
        # Install Syft
        curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

    - name: Run Trivy vulnerability scan
      id: trivy
      continue-on-error: true
      run: |
        trivy image --input image.tar.gz \
          --severity HIGH,CRITICAL \
          --format sarif \
          --output trivy-results.sarif \
          --exit-code 1
        echo "status=$?" >> $GITHUB_OUTPUT

    - name: Upload Trivy results to GitHub Security
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: trivy-results.sarif

    - name: Run Grype license scan
      id: grype
      continue-on-error: true
      run: |
        grype image.tar.gz --fail-on high --output json > grype-results.json
        DENIED_COUNT=$(jq '.matches[] | select(.artifact.licenses[] | .value == "GPL-3.0" or .value == "AGPL-3.0")' grype-results.json | wc -l)
        if [ $DENIED_COUNT -gt 0 ]; then
          echo "status=failed" >> $GITHUB_OUTPUT
          exit 1
        else
          echo "status=passed" >> $GITHUB_OUTPUT
        fi

    - name: Generate SBOM
      run: |
        syft image.tar.gz -o spdx-json > sbom.spdx.json

    - name: Security Gate
      if: steps.trivy.outputs.status != '0' || steps.grype.outputs.status != 'passed'
      run: |
        echo "❌ Security gate failed!"
        echo "Trivy status: ${{ steps.trivy.outputs.status }}"
        echo "Grype status: ${{ steps.grype.outputs.status }}"
        exit 1

    - name: Configure AWS credentials
      if: success()
      uses: aws-actions/configure-aws-credentials@v2
      with:
        role-to-assume: arn:aws:iam::${{ env.AWS_ACCOUNT_ID }}:role/github-actions-role
        aws-region: ${{ env.AWS_REGION }}

    - name: Login to Amazon ECR
      if: success()
      uses: aws-actions/amazon-ecr-login@v1

    - name: Load and push approved image to ECR
      if: success()
      run: |
        docker load -i image.tar.gz
        docker tag ${{ env.ECR_REPOSITORY }}:${{ github.sha }} ${{ env.AWS_ACCOUNT_ID }}.dkr.ecr.${{ env.AWS_REGION }}.amazonaws.com/${{ env.ECR_REPOSITORY }}:${{ github.sha }}
        docker push ${{ env.AWS_ACCOUNT_ID }}.dkr.ecr.${{ env.AWS_REGION }}.amazonaws.com/${{ env.ECR_REPOSITORY }}:${{ github.sha }}

    - name: Deploy to AWS App Runner
      if: success()
      run: |
        aws apprunner update-service \
          --service-arn arn:aws:apprunner:${{ env.AWS_REGION }}:${{ env.AWS_ACCOUNT_ID }}:service/courses-api/xxxxx \
          --source-configuration '{
            "ImageRepository": {
              "ImageIdentifier": "${{ env.AWS_ACCOUNT_ID }}.dkr.ecr.${{ env.AWS_REGION }}.amazonaws.com/${{ env.ECR_REPOSITORY }}:${{ github.sha }}",
              "ImageConfiguration": {
                "Port": "8000"
              }
            }
          }'
```

---

## Air-Gapped Deployments with AWS GovCloud and Outposts

### Transferring Tarballs Across Air-Gapped Networks

For AWS GovCloud, AWS Outposts, or air-gapped environments:

```mermaid
graph LR
    A[Build Network<br/>Commercial AWS] -->|Export| B[courses-api.tar.gz]
    B -->|AWS Snowball| C[Air-Gapped Network<br/>GovCloud/Outposts]
    C -->|Load| D[Docker/Podman]
    D -->|Push| E[Local ECR]
    E -->|Deploy| F[ECS/EKS on Outposts]
```

### Deploying to AWS Outposts

```bash
# On Outpost (air-gapped network)
# 1. Transfer tarball via Snowball or physical media
# 2. Load image
docker load -i /media/courses-api.tar.gz

# 3. Push to Outpost ECR
docker tag courses-api:latest $OUTPOST_ACCOUNT.dkr.ecr.$REGION.outposts.amazonaws.com/courses-api:latest
docker push $OUTPOST_ACCOUNT.dkr.ecr.$REGION.outposts.amazonaws.com/courses-api:latest

# 4. Deploy to ECS on Outpost
aws ecs create-service \
    --cluster courses-outpost-cluster \
    --service-name courses-api \
    --task-definition courses-api \
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
docker load -i ./courses-api.tar.gz
docker tag courses-api:latest $GOV_ACCOUNT.dkr.ecr.us-gov-west-1.amazonaws.com/courses-api:latest
docker push $GOV_ACCOUNT.dkr.ecr.us-gov-west-1.amazonaws.com/courses-api:latest
```

---

## Image Signing with AWS Signer

### Set Up AWS Signer

```bash
# Create signing profile
aws signer put-signing-profile \
    --profile-name courses-portal-images \
    --platform-id AWSLambda-SHA384-ECDSA

# Sign the image (after loading to ECR)
aws signer start-signing-job \
    --source '{
        "s3": {
            "bucketName": "courses-portal-artifacts",
            "key": "images/courses-api-latest.tar.gz",
            "version": "1"
        }
    }' \
    --destination '{
        "s3": {
            "bucketName": "courses-portal-artifacts",
            "prefix": "signed/"
        }
    }' \
    --profile-name courses-portal-images

# Verify signature
aws signer describe-signing-job \
    --job-id xxxxx-xxxxx-xxxxx
```

---

## Compliance Frameworks

### NIST SP 800-190 Compliance for Python

| Requirement | AWS Implementation | Verification |
|-------------|-------------------|--------------|
| **Image Scanning** | Amazon Inspector + Trivy | Scan before deployment |
| **SBOM Generation** | Syft + S3 | SPDX stored in audit log |
| **Vulnerability Management** | Block HIGH/CRITICAL findings | Security gate in pipeline |
| **Image Signing** | AWS Signer | Verify before deployment |
| **Least Privilege** | Non-root user in Dockerfile | User ID check |
| **Audit Trail** | AWS CloudTrail + S3 Versioning | All operations logged |

### FedRAMP High Requirements

```bash
# FedRAMP High requirements for Python containers
# 1. Image must be scanned for vulnerabilities
trivy image --input courses-api.tar.gz --severity HIGH,CRITICAL --exit-code 1

# 2. SBOM must be generated and stored
syft courses-api.tar.gz -o spdx-json > sbom.spdx.json
aws s3 cp sbom.spdx.json s3://courses-portal-artifacts/sboms/

# 3. Image must be signed
aws signer start-signing-job --profile-name courses-portal-images --source '{"s3":{"bucketName":"courses-portal-artifacts","key":"images/courses-api.tar.gz"}}'

# 4. Audit logs must be enabled
aws cloudtrail create-trail --name courses-portal-trail --s3-bucket-name courses-portal-audit-logs
aws cloudtrail start-logging --name courses-portal-trail
```

---

## Troubleshooting Security Pipelines

### Issue 1: Amazon Inspector Not Finding Images

**Error:** `No findings found for image`

**Solution:**
```bash
# Enable ECR scanning
aws ecr put-image-scanning-configuration \
    --repository-name courses-api \
    --image-scanning-configuration scanOnPush=true

# Wait for scan to complete (5-10 minutes)
aws ecr describe-image-scan-findings \
    --repository-name courses-api \
    --image-id imageTag=latest
```

### Issue 2: Trivy False Positives

**Problem:** Vulnerability reported but not applicable to Python application.

**Solution:**
```yaml
# .trivyignore
# CVE-2024-12345 - This CVE affects Java libraries, not Python
CVE-2024-12345
# CVE-2024-67890 - Patched in next release, not exploitable
CVE-2024-67890
```

```bash
trivy image --input courses-api.tar.gz --ignorefile .trivyignore
```

### Issue 3: Large Tarball Size

**Problem:** Tarball exceeds artifact storage limits.

**Solution:**
```dockerfile
# Use multi-stage builds with minimal base
FROM python:3.11-slim AS builder
# ... build deps ...

FROM python:3.11-slim AS runtime
# ... copy only needed files ...

# Use Alpine for even smaller images
FROM python:3.11-alpine AS runtime
```

### Issue 4: SBOM Generation Fails

**Error:** `Error: unable to generate SBOM`

**Solution:**
```bash
# Validate tarball integrity
tar -tzf courses-api.tar.gz | head -10
# Should show blobs/ and index.json

# If corrupted, regenerate
docker save courses-api:latest -o courses-api.tar
gzip courses-api.tar
```

---

## Performance Metrics

| Step | Time | Notes |
|------|------|-------|
| **docker build** | 45-90s | Depends on dependencies |
| **docker save** | 10-20s | Creates tarball |
| **Trivy Scan** | 30-60s | Cached base layers |
| **Amazon Inspector** | 2-5 minutes | After ECR push |
| **Grype Scan** | 20-40s | License analysis |
| **Syft SBOM** | 10-20s | Generation |
| **S3 Upload** | 10-30s | Network dependent |
| **Load + Push** | 15-30s | Runtime required |

---

## Conclusion: Security as Code for Python on AWS

Tarball export transforms container delivery from an uncontrolled push model to a controlled, auditable supply chain for Python applications on AWS. For the AI Powered Video Tutorial Portal, this security-first approach ensures:

- **No vulnerable images reach production** – Blocked by Trivy and Amazon Inspector security gates
- **Complete supply chain visibility** – SBOMs for every image in S3
- **License compliance** – Automated detection of restricted licenses (GPL, AGPL)
- **Air-gapped support** – Deploy to AWS GovCloud and Outposts
- **Audit trail** – Every image is scanned, signed, and approved
- **FedRAMP compliance** – Meets federal security requirements

While direct registry pushes offer convenience, security-first organizations require the control and visibility that tarball export provides. By integrating Amazon Inspector, Trivy, Grype, Syft, and AWS Signer into your CI/CD pipeline, you can achieve the same level of security automation that major government and enterprise organizations require for Python workloads on AWS.

---

### Stories at a Glance

**Complete AWS Python series (10 stories):**

- 🐍 **1. Poetry + Docker Multi-Stage: The Modern Python Approach - AWS** – Leveraging Poetry for dependency management with optimized multi-stage Docker builds for FastAPI applications on Amazon ECR

- ⚡ **2. UV + Docker: Blazing Fast Python Package Management - AWS** – Using the ultra-fast UV package installer for sub-second dependency resolution in container builds for AWS Graviton

- 📦 **3. Pip + Docker: The Classic Python Containerization - AWS** – Traditional requirements.txt approach with multi-stage builds and layer caching optimization for Amazon ECS

- 🚀 **4. AWS Copilot: The Turnkey Container Solution - AWS** – Deploying FastAPI applications to Amazon ECS with AWS Copilot, Fargate, and built-in best practices

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production - AWS** – Using VS Code Dev Containers for consistent development environments that mirror AWS production

- 🏗️ **6. AWS CDK with Python: Infrastructure as Code for Containers - AWS** – Defining FastAPI infrastructure with Python CDK, deploying to ECS Fargate with auto-scaling

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows - AWS** – Generating container tarballs, integrating with Amazon Inspector, and deploying to air-gapped AWS environments *(This story)*

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## What's Next?

Over the coming weeks, each approach in this AWS Python series will be explored in exhaustive detail. We'll examine real-world AWS deployment scenarios for the AI Powered Video Tutorial Portal, benchmark performance across methods, and provide production-ready patterns for CI/CD pipelines. Whether you're a startup deploying your first FastAPI application on AWS Fargate or an enterprise migrating Python workloads to Amazon EKS, you'll find practical guidance tailored to your infrastructure requirements.

Tarball export represents the security-first evolution of Python container delivery on AWS—ensuring that every image is scanned, verified, and approved before reaching production. By mastering these ten approaches, you'll be equipped to choose the right tool for every scenario—from rapid prototyping to FedRAMP-compliant production deployments on AWS GovCloud.

**Coming next in the series:**
**☸️ Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations