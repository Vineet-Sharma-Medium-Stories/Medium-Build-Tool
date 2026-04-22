# Terraform with Kubernetes on AWS: A Complete Architectural Guide With Vehixcare

## From Infrastructure as Code to Real-Time Fleet Telemetry — A Complete Cloud-Native Journey on Amazon Web Services with Vehixcare Platform

**Keywords:** Infrastructure as Code, Amazon EKS (Elastic Kubernetes Service), Amazon DocumentDB (MongoDB-compatible), Terraform State Management, Pod Identity, Horizontal Pod Autoscaler, Secrets Store CSI Driver, AWS CNI, IRSA, Multi-Region Failover, AWS AppSync, Event-Driven Architecture, Rx.NET, Geo-fencing, Telemetry Processing, KEDA, Amazon EventBridge

![Terraform with Kubernetes on AWS: A Complete Architectural Guide With Vehixcare](images/Terraform-with-Kubernetes-on-AWS-A-Complete-Architectural-Guide-With-Vehixcare.png)

> **A Note on Origins:** This guide is the **AWS adaptation** of the original Azure-based architecture. The source material, *"Terraform with Kubernetes on Azure: A Complete Architectural Guide With Vehixcare"* by Vineet Sharma, is available on Medium at [https://medium.com/@mvineetsharma/terraform-with-kubernetes-on-azure-a-complete-architectural-guide-with-vehixcare-270315058bc3?sk=f391b74ec4245e73c319c05d51480dbd](https://medium.com/@mvineetsharma/terraform-with-kubernetes-on-azure-a-complete-architectural-guide-with-vehixcare-270315058bc3?sk=f391b74ec4245e73c319c05d51480dbd). All architectural patterns, Vehixcare feature mappings, and .NET 9.0 implementation details from the original have been preserved and re-implemented for AWS services.

---

## Introduction: Terraform and Kubernetes on AWS

When building cloud-native applications on Amazon Web Services, infrastructure teams face a critical architectural decision: how to provision cloud resources and how to deploy applications. Two dominant tools emerge—Terraform and Kubernetes—but they serve fundamentally different purposes.

**Terraform** is an infrastructure-as-code tool that provisions AWS resources such as VPCs, EKS clusters, DocumentDB accounts, and Secrets Manager. It uses a declarative language called HCL (HashiCorp Configuration Language) and maintains a state file that maps your configuration to real AWS resources. When you run `terraform apply`, Terraform makes API calls to AWS Cloud Control API to create, update, or delete resources. Terraform's job ends the moment the infrastructure is ready—it does not care about pod replicas, rolling updates, or whether your API responds to health checks.

**Kubernetes** is a container orchestration platform that schedules, scales, and manages application workloads inside a cluster. On AWS, EKS (Elastic Kubernetes Service) provides a managed control plane while you manage worker nodes and application deployments. Kubernetes handles pod scheduling, automatic restarts of failed containers, rolling updates with zero downtime, service discovery via DNS, horizontal scaling based on metrics, and secret injection.

These tools are not competitors. Terraform manages the **cloud control plane**—everything outside the container boundary. Kubernetes manages the **application data plane**—everything inside the cluster. EKS sits at the intersection: Terraform creates the EKS cluster, and Kubernetes runs workloads inside it.

This document provides a complete implementation guide for both tools working in harmony, using **Vehixcare**—a .NET 9.0 fleet telemetry platform with real-time GPS tracking, driver behavior analysis, geo-fencing, and real-time streaming—as the reference application. The complete source code is available at [https://gitlab.com/mvineetsharma/Vehixcare-AI/Vehixcare-API](https://gitlab.com/mvineetsharma/Vehixcare-AI/Vehixcare-API).

---

## 1. Vehixcare Platform: Features and Infrastructure Mapping (AWS Edition)

Vehixcare is a comprehensive fleet management and vehicle telemetry platform built with .NET 9.0, ASP.NET Core, and MongoDB. Below are its core features and how each maps to Terraform and Kubernetes concepts on AWS:

![cloud control plane](images/table_01_vehixcare-is-a-comprehensive-fleet-management-and-5ce8.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_01_vehixcare-is-a-comprehensive-fleet-management-and-5ce8.md)


**Technical Features and Infrastructure Mapping (AWS):**

![Real-time Vehicle Telemetry](images/table_02_technical-features-and-infrastructure-mapping-a-0d6d.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_02_technical-features-and-infrastructure-mapping-a-0d6d.md)


---

## 1. Architecture Overview

### 1.1 High-Level Architecture Diagram (AWS)

```mermaid
```

![MongoDB Change Streams](images/diagram_01_11-high-level-architecture-diagram-aws-3ada.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_01_11-high-level-architecture-diagram-aws-3ada.md)


### 1.2 Deployment Workflow Sequence Diagram (AWS)

```mermaid
```

![Diagram](images/diagram_02_12-deployment-workflow-sequence-diagram-aws-7edd.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_02_12-deployment-workflow-sequence-diagram-aws-7edd.md)


### 1.3 Telemetry Processing Sequence Diagram (AWS)

```mermaid
```

![Diagram](images/diagram_03_13-telemetry-processing-sequence-diagram-aws-b657.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_03_13-telemetry-processing-sequence-diagram-aws-b657.md)


### 1.4 Network Topology Diagram (AWS VPC)

```mermaid
```

![Diagram](images/diagram_04_14-network-topology-diagram-aws-vpc-110c.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_04_14-network-topology-diagram-aws-vpc-110c.md)


### 1.5 Responsibility Matrix Diagram (AWS Edition)

```mermaid
```

![Diagram](images/diagram_05_15-responsibility-matrix-diagram-aws-edition-abf5.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_05_15-responsibility-matrix-diagram-aws-edition-abf5.md)


### 1.6 CI/CD Pipeline Flow Diagram (AWS)

```mermaid
```

![Diagram](images/diagram_06_16-cicd-pipeline-flow-diagram-aws-f6cf.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_06_16-cicd-pipeline-flow-diagram-aws-f6cf.md)


### 1.7 EKS Cluster Node Groups Diagram

```mermaid
```

![Diagram](images/diagram_07_17-eks-cluster-node-groups-diagram-8dce.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_07_17-eks-cluster-node-groups-diagram-8dce.md)


### 1.8 Amazon DocumentDB Architecture Diagram

```mermaid
```

![Diagram](images/diagram_08_18-amazon-documentdb-architecture-diagram-b82b.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_08_18-amazon-documentdb-architecture-diagram-b82b.md)


### 1.9 AWS Secrets Manager Architecture Diagram

```mermaid
```

![Diagram](images/diagram_09_19-aws-secrets-manager-architecture-diagram-105a.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_09_19-aws-secrets-manager-architecture-diagram-105a.md)


### 1.10 Data Flow: MongoDB Operations with DocumentDB

```mermaid
```

![Diagram](images/diagram_10_110-data-flow-mongodb-operations-with-docume-f782.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_10_110-data-flow-mongodb-operations-with-docume-f782.md)


---

## 2. Core Concepts Deep Dive (AWS Context)

### 2.1 Terraform Core Concepts (AWS Edition)

**State Management:** Terraform maintains a state file that maps your HCL configuration to real AWS resources. For Vehixcare production, state lives in S3 bucket (`vehixcare-tfstate-prod`) with DynamoDB state locking to prevent concurrent modifications. Losing this file means Terraform cannot track existing resources, leading to drift or accidental duplication. The backend configuration uses `s3` backend with `dynamodb_table` parameter for locking across environments.

**Provider Configuration:** The AWS provider translates Terraform resources into AWS API calls. Each resource block—whether for a VPC, EKS cluster, or DocumentDB—contains arguments that map directly to AWS's Cloud Control API or service-specific APIs. The `default_tags` block configures provider-level tagging.

**Dependency Resolution:** Terraform automatically builds a dependency graph from your configuration. When you reference `aws_subnet.private_eks_a.id` inside an EKS cluster definition, Terraform knows to create the subnet before the cluster. This implicit ordering prevents race conditions during provisioning.

**Plan and Apply Cycle:** `terraform plan` shows what will change; `terraform apply` executes the changes. For Vehixcare, the CI/CD pipeline runs `terraform plan` on every PR and `terraform apply` only on merge to main.

**Resource Lifecycle:** Terraform manages resources through Create (provision via AWS API), Read (refresh state from AWS), Update (modify existing resource), and Delete (destroy resource). Some resources require replacement rather than in-place updates (e.g., changing `instance_type` on an Auto Scaling Group forces replacement).

**Data Sources:** Terraform data sources read information from AWS without creating resources. For Vehixcare, `data "aws_caller_identity" "current"` retrieves the current AWS account ID for IAM role configuration.

**Modules:** Terraform modules encapsulate resource groups into reusable components. Vehixcare modules include `vpc`, `eks-cluster`, `documentdb`, `monitoring`, and `secrets-manager`.

### 2.2 Kubernetes Core Concepts (AWS Edition)

**Pods:** The smallest deployable unit. Vehixcare's telemetry API runs in its own pod with a container for the API and optionally sidecars for logging (Fluent Bit) or metrics (Prometheus exporter). Pods are ephemeral—when a pod fails, Kubernetes replaces it.

**Deployments:** Declarative updates for pods. Vehixcare uses `strategy: RollingUpdate` with `maxSurge: 1` and `maxUnavailable: 0` for zero-downtime updates.

**Services:** Stable network endpoints. Types include:
- **ClusterIP** (default): Internal-only. Used for telemetry API internal communication.
- **NodePort:** Static port on each node.
- **LoadBalancer:** Provisions AWS NLB. Vehixcare uses this for AppSync resolvers.
- **ExternalName:** Maps to external DNS.

**Ingress:** HTTP/HTTPS routing. On AWS, the AWS Load Balancer Controller provisions Application Load Balancers or Network Load Balancers based on Ingress resources.

**Horizontal Pod Autoscaler (HPA):** Scales pods based on CPU, memory, or custom metrics. Vehixcare scales Telemetry API when telemetry messages per second exceed 1000 using Prometheus metrics.

**ConfigMaps and Secrets:** Configuration data injected into pods. For production, Vehixcare uses AWS Secrets Manager with Secrets Store CSI Driver to mount secrets directly.

**Controllers and Operators:** Controllers watch cluster state. The AWS Load Balancer Controller manages AWS load balancers; KEDA provides event-driven autoscaling; Prometheus Operator manages monitoring.

**Namespaces:** Virtual clusters for isolation. Vehixcare uses `vehixcare-telemetry`, `vehixcare-appsync`, `vehixcare-background`, and `vehixcare-monitoring`.

**Resource Quotas and Limits:** Vehixcare's telemetry API requests 1000m CPU and 2Gi memory, limits 3000m CPU and 4Gi memory.

### 2.3 Responsibility Matrix (AWS)

![ConfigMaps and Secrets:](images/table_03_23-responsibility-matrix-aws.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_03_23-responsibility-matrix-aws.md)


---

## 3. Terraform on AWS: Complete Implementation

### 3.1 Backend and Provider Configuration

```hcl
# backend.tf
terraform {
  required_version = ">= 1.5.0"
  
  backend "s3" {
    bucket         = "vehixcare-tfstate-prod"
    key            = "vehixcare-prod.tfstate"
    region         = "us-east-1"
    dynamodb_table = "vehixcare-terraform-locks"
    encrypt        = true
  }
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Application = "vehixcare"
      ManagedBy   = "terraform"
      CostCenter  = "fleet-platform"
    }
  }
}

# variables.tf
variable "aws_region" {
  description = "AWS region for primary deployment"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}

variable "aws_access_key_id" {
  description = "AWS access key for CI/CD"
  type        = string
  sensitive   = true
}

variable "aws_secret_access_key" {
  description = "AWS secret key for CI/CD"
  type        = string
  sensitive   = true
}

variable "google_oauth_client_id" {
  description = "Google OAuth client ID"
  type        = string
  sensitive   = true
}

variable "google_oauth_client_secret" {
  description = "Google OAuth client secret"
  type        = string
  sensitive   = true
}

# main.tf
resource "aws_resourcegroups_group" "vehixcare" {
  name = "rg-vehixcare-production"
  
  resource_query {
    query = jsonencode({
      ResourceTypeFilters = ["AWS::AllSupported"]
      TagFilters = [
        {
          Key    = "Application"
          Values = ["vehixcare"]
        }
      ]
    })
  }
  
  tags = {
    Environment = "production"
    Application = "vehixcare"
  }
}
```

### 3.2 Network Topology with VPC and Subnets

```hcl
# networking.tf
data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "vehixcare" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name        = "vpc-vehixcare"
    Environment = "production"
    Purpose     = "vehixcare-core-network"
  }
}

# Private subnets for EKS worker nodes (3 AZs)
resource "aws_subnet" "private_eks" {
  count             = 3
  vpc_id            = aws_vpc.vehixcare.id
  cidr_block        = cidrsubnet(aws_vpc.vehixcare.cidr_block, 5, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = false
  
  tags = {
    Name                                 = "private-eks-${data.aws_availability_zones.available.names[count.index]}"
    "kubernetes.io/cluster/${var.cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb"    = "1"
    Environment                          = "production"
  }
}

# Public subnets for NAT Gateways and Bastion (2 AZs)
resource "aws_subnet" "public_eks" {
  count             = 2
  vpc_id            = aws_vpc.vehixcare.id
  cidr_block        = cidrsubnet(aws_vpc.vehixcare.cidr_block, 5, count.index + 6)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name                                 = "public-eks-${data.aws_availability_zones.available.names[count.index]}"
    "kubernetes.io/cluster/${var.cluster_name}" = "shared"
    "kubernetes.io/role/elb"             = "1"
    Environment                          = "production"
  }
}

# Private subnet for Network Load Balancer
resource "aws_subnet" "private_nlb" {
  count             = 3
  vpc_id            = aws_vpc.vehixcare.id
  cidr_block        = cidrsubnet(aws_vpc.vehixcare.cidr_block, 4, count.index + 12)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = false
  
  tags = {
    Name        = "private-nlb-${data.aws_availability_zones.available.names[count.index]}"
    Environment = "production"
  }
}

# Private subnet for VPC Endpoints
resource "aws_subnet" "private_vpce" {
  count             = 3
  vpc_id            = aws_vpc.vehixcare.id
  cidr_block        = cidrsubnet(aws_vpc.vehixcare.cidr_block, 4, count.index + 18)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = false
  
  tags = {
    Name        = "private-vpce-${data.aws_availability_zones.available.names[count.index]}"
    Environment = "production"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "vehixcare" {
  vpc_id = aws_vpc.vehixcare.id
  
  tags = {
    Name        = "igw-vehixcare"
    Environment = "production"
  }
}

# Elastic IPs for NAT Gateways
resource "aws_eip" "nat" {
  count = 2
  domain = "vpc"
  
  tags = {
    Name        = "nat-eip-${count.index + 1}"
    Environment = "production"
  }
}

# NAT Gateways in public subnets
resource "aws_nat_gateway" "vehixcare" {
  count         = 2
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public_eks[count.index].id
  
  tags = {
    Name        = "nat-gw-${count.index + 1}"
    Environment = "production"
  }
}

# Route Tables
resource "aws_route_table" "private" {
  count  = 3
  vpc_id = aws_vpc.vehixcare.id
  
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.vehixcare[count.index % 2].id
  }
  
  tags = {
    Name        = "rt-private-${data.aws_availability_zones.available.names[count.index]}"
    Environment = "production"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.vehixcare.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.vehixcare.id
  }
  
  tags = {
    Name        = "rt-public"
    Environment = "production"
  }
}

# Route Table Associations
resource "aws_route_table_association" "private_eks" {
  count          = 3
  subnet_id      = aws_subnet.private_eks[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

resource "aws_route_table_association" "public_eks" {
  count          = 2
  subnet_id      = aws_subnet.public_eks[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private_nlb" {
  count          = 3
  subnet_id      = aws_subnet.private_nlb[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

resource "aws_route_table_association" "private_vpce" {
  count          = 3
  subnet_id      = aws_subnet.private_vpce[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# Security Group for EKS Control Plane
resource "aws_security_group" "eks_cluster" {
  name        = "sg-eks-cluster"
  description = "Security group for EKS cluster control plane"
  vpc_id      = aws_vpc.vehixcare.id
  
  ingress {
    description = "Allow API server access from VPC"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.vehixcare.cidr_block]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name        = "sg-eks-cluster"
    Environment = "production"
  }
}

# Security Group for EKS Worker Nodes
resource "aws_security_group" "eks_nodes" {
  name        = "sg-eks-nodes"
  description = "Security group for EKS worker nodes"
  vpc_id      = aws_vpc.vehixcare.id
  
  ingress {
    description     = "Allow node-to-node communication"
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    self            = true
  }
  
  ingress {
    description     = "Allow API server to nodes"
    from_port       = 10250
    to_port         = 10250
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_cluster.id]
  }
  
  ingress {
    description     = "Allow SSH from bastion"
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    cidr_blocks     = ["10.0.96.0/19", "10.0.128.0/19"]
  }
  
  ingress {
    description     = "Allow SignalR/AppSync WebSocket ports"
    from_port       = 5000
    to_port         = 5500
    protocol        = "tcp"
    cidr_blocks     = [aws_vpc.vehixcare.cidr_block]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name        = "sg-eks-nodes"
    Environment = "production"
  }
}
```

### 3.3 Amazon DocumentDB with MongoDB API

```hcl
# documentdb.tf
resource "aws_docdb_subnet_group" "vehixcare" {
  name       = "docdb-subnet-group-vehixcare"
  subnet_ids = aws_subnet.private_eks[*].id
  
  tags = {
    Name        = "docdb-subnet-group"
    Environment = "production"
  }
}

resource "aws_docdb_cluster_parameter_group" "vehixcare" {
  family      = "docdb4.0"
  name        = "docdb-param-group-vehixcare"
  description = "Parameter group for Vehixcare DocumentDB"
  
  parameter {
    name  = "ttl_monitor"
    value = "enabled"
  }
  
  parameter {
    name  = "change_streams_enabled"
    value = "enabled"
  }
  
  parameter {
    name  = "profiler_enabled"
    value = "disabled"
  }
  
  tags = {
    Environment = "production"
  }
}

resource "aws_docdb_cluster" "vehixcare" {
  cluster_identifier              = "docdb-vehixcare-prod"
  engine                          = "docdb"
  engine_version                  = "4.0.0"
  master_username                 = var.docdb_username
  master_password                 = var.docdb_password
  backup_retention_period         = 35
  preferred_backup_window         = "02:00-03:00"
  preferred_maintenance_window    = "sun:03:00-sun:04:00"
  skip_final_snapshot             = false
  final_snapshot_identifier       = "docdb-vehixcare-final-snapshot"
  storage_encrypted               = true
  kms_key_id                      = aws_kms_key.documentdb.arn
  db_subnet_group_name            = aws_docdb_subnet_group.vehixcare.name
  vpc_security_group_ids          = [aws_security_group.documentdb.id]
  db_cluster_parameter_group_name = aws_docdb_cluster_parameter_group.vehixcare.name
  
  # Global cluster configuration for multi-region
  global_cluster_identifier = aws_docdb_global_cluster.vehixcare.id
  
  tags = {
    Environment = "production"
    Database    = "documentdb"
    Workload    = "vehixcare-core"
  }
}

# Global cluster for cross-region replication
resource "aws_docdb_global_cluster" "vehixcare" {
  global_cluster_identifier = "global-docdb-vehixcare"
  engine                    = "docdb"
  engine_version            = "4.0.0"
  
  # Primary region
  source_db_cluster_identifier = aws_docdb_cluster.vehixcare.arn
}

# Read replicas in primary region
resource "aws_docdb_cluster_instance" "writer" {
  cluster_identifier = aws_docdb_cluster.vehixcare.id
  identifier         = "docdb-writer"
  instance_class     = "db.r5.2xlarge"
  
  tags = {
    Environment = "production"
    Role        = "writer"
  }
}

resource "aws_docdb_cluster_instance" "reader" {
  count              = 3
  cluster_identifier = aws_docdb_cluster.vehixcare.id
  identifier         = "docdb-reader-${count.index + 1}"
  instance_class     = "db.r5.2xlarge"
  
  tags = {
    Environment = "production"
    Role        = "reader"
  }
}

# Security Group for DocumentDB
resource "aws_security_group" "documentdb" {
  name        = "sg-documentdb"
  description = "Security group for DocumentDB"
  vpc_id      = aws_vpc.vehixcare.id
  
  ingress {
    description     = "DocumentDB from EKS nodes"
    from_port       = 27017
    to_port         = 27017
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_nodes.id]
  }
  
  tags = {
    Name        = "sg-documentdb"
    Environment = "production"
  }
}

# VPC Endpoint for DocumentDB
resource "aws_vpc_endpoint" "documentdb" {
  vpc_id              = aws_vpc.vehixcare.id
  service_name        = "com.amazonaws.${var.aws_region}.rds"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = aws_subnet.private_vpce[*].id
  security_group_ids  = [aws_security_group.documentdb.id]
  
  private_dns_enabled = true
  
  tags = {
    Name        = "vpce-documentdb"
    Environment = "production"
  }
}

# KMS key for DocumentDB encryption
resource "aws_kms_key" "documentdb" {
  description             = "KMS key for DocumentDB encryption"
  deletion_window_in_days = 7
  enable_key_rotation     = true
  
  tags = {
    Environment = "production"
    Purpose     = "documentdb-encryption"
  }
}

# Outputs
output "documentdb_connection_string" {
  value     = "mongodb://${aws_docdb_cluster.vehixcare.master_username}:${urlencode(aws_docdb_cluster.vehixcare.master_password)}@${aws_docdb_cluster.vehixcare.endpoint}:27017/?replicaSet=rs0&tls=true&tlsCAFile=global-bundle.pem&retryWrites=false"
  sensitive = true
}

output "documentdb_endpoint" {
  value = aws_docdb_cluster.vehixcare.endpoint
}
```

### 3.4 Amazon ECR with Cross-Region Replication

```hcl
# ecr.tf
resource "aws_ecr_repository" "vehixcare_api" {
  name                 = "vehixcare-api"
  image_tag_mutability = "MUTABLE"
  
  image_scanning_configuration {
    scan_on_push = true
  }
  
  encryption_configuration {
    encryption_type = "KMS"
    kms_key         = aws_kms_key.ecr.arn
  }
  
  tags = {
    Environment = "production"
    Service     = "telemetry-api"
  }
}

resource "aws_ecr_repository" "vehixcare_hubs" {
  name                 = "vehixcare-hubs"
  image_tag_mutability = "MUTABLE"
  
  image_scanning_configuration {
    scan_on_push = true
  }
  
  tags = {
    Environment = "production"
    Service     = "appsync-resolvers"
  }
}

resource "aws_ecr_repository" "vehixcare_processor" {
  name                 = "vehixcare-processor"
  image_tag_mutability = "MUTABLE"
  
  image_scanning_configuration {
    scan_on_push = true
  }
  
  tags = {
    Environment = "production"
    Service     = "background-processor"
  }
}

resource "aws_ecr_repository" "vehixcare_geofence" {
  name                 = "vehixcare-geofence"
  image_tag_mutability = "MUTABLE"
  
  image_scanning_configuration {
    scan_on_push = true
  }
  
  tags = {
    Environment = "production"
    Service     = "geofence-monitor"
  }
}

# Cross-region replication for ECR
resource "aws_ecr_replication_configuration" "vehixcare" {
  replication_configuration {
    rule {
      destination {
        region      = "us-west-2"
        registry_id = data.aws_caller_identity.current.account_id
      }
    }
  }
}

# Lifecycle policy for ECR
resource "aws_ecr_lifecycle_policy" "vehixcare_api" {
  repository = aws_ecr_repository.vehixcare_api.name
  
  policy = jsonencode({
    rules = [
      {
        rulePriority = 1
        description  = "Keep last 30 images"
        selection = {
          tagStatus     = "tagged"
          tagPrefixList = ["v"]
          countType     = "imageCountMoreThan"
          countNumber   = 30
        }
        action = {
          type = "expire"
        }
      },
      {
        rulePriority = 2
        description  = "Expire untagged images after 14 days"
        selection = {
          tagStatus   = "untagged"
          countType   = "sinceImagePushed"
          countUnit   = "days"
          countNumber = 14
        }
        action = {
          type = "expire"
        }
      }
    ]
  })
}

# KMS key for ECR encryption
resource "aws_kms_key" "ecr" {
  description             = "KMS key for ECR encryption"
  deletion_window_in_days = 7
  enable_key_rotation     = true
}

# Outputs
output "ecr_repository_urls" {
  value = {
    api       = aws_ecr_repository.vehixcare_api.repository_url
    hubs      = aws_ecr_repository.vehixcare_hubs.repository_url
    processor = aws_ecr_repository.vehixcare_processor.repository_url
    geofence  = aws_ecr_repository.vehixcare_geofence.repository_url
  }
}
```

### 3.5 AWS Secrets Manager with KMS

```hcl
# secrets-manager.tf
data "aws_caller_identity" "current" {}

# KMS key for Secrets Manager
resource "aws_kms_key" "secrets_manager" {
  description             = "KMS key for Secrets Manager"
  deletion_window_in_days = 7
  enable_key_rotation     = true
  
  tags = {
    Environment = "production"
    Purpose     = "secrets-encryption"
  }
}

resource "aws_kms_alias" "secrets_manager" {
  name          = "alias/vehixcare-secrets"
  target_key_id = aws_kms_key.secrets_manager.key_id
}

# Random password for JWT secret
resource "random_password" "jwt_secret" {
  length  = 64
  special = false
  min_upper = 2
  min_lower = 2
  min_numeric = 2
}

# DocumentDB connection string secret
resource "aws_secretsmanager_secret" "documentdb_connection" {
  name                    = "vehixcare/documentdb-connection-string"
  description             = "DocumentDB connection string for Vehixcare"
  recovery_window_in_days = 7
  kms_key_id              = aws_kms_key.secrets_manager.arn
  
  tags = {
    Environment = "production"
    Application = "vehixcare"
  }
}

resource "aws_secretsmanager_secret_version" "documentdb_connection" {
  secret_id     = aws_secretsmanager_secret.documentdb_connection.id
  secret_string = "mongodb://${var.docdb_username}:${urlencode(var.docdb_password)}@${aws_docdb_cluster.vehixcare.endpoint}:27017/?replicaSet=rs0&tls=true&tlsCAFile=global-bundle.pem&retryWrites=false"
}

# JWT signing secret
resource "aws_secretsmanager_secret" "jwt_secret" {
  name                    = "vehixcare/jwt-signing-secret"
  description             = "JWT signing secret for Vehixcare"
  recovery_window_in_days = 7
  kms_key_id              = aws_kms_key.secrets_manager.arn
  
  tags = {
    Environment = "production"
    Application = "vehixcare"
  }
}

resource "aws_secretsmanager_secret_version" "jwt_secret" {
  secret_id     = aws_secretsmanager_secret.jwt_secret.id
  secret_string = random_password.jwt_secret.result
}

# Google OAuth secrets
resource "aws_secretsmanager_secret" "google_client_id" {
  name                    = "vehixcare/google-oauth-client-id"
  description             = "Google OAuth client ID"
  recovery_window_in_days = 7
  kms_key_id              = aws_kms_key.secrets_manager.arn
}

resource "aws_secretsmanager_secret_version" "google_client_id" {
  secret_id     = aws_secretsmanager_secret.google_client_id.id
  secret_string = var.google_oauth_client_id
}

resource "aws_secretsmanager_secret" "google_client_secret" {
  name                    = "vehixcare/google-oauth-client-secret"
  description             = "Google OAuth client secret"
  recovery_window_in_days = 7
  kms_key_id              = aws_kms_key.secrets_manager.arn
}

resource "aws_secretsmanager_secret_version" "google_client_secret" {
  secret_id     = aws_secretsmanager_secret.google_client_secret.id
  secret_string = var.google_oauth_client_secret
}

# VPC Endpoint for Secrets Manager
resource "aws_vpc_endpoint" "secrets_manager" {
  vpc_id              = aws_vpc.vehixcare.id
  service_name        = "com.amazonaws.${var.aws_region}.secretsmanager"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = aws_subnet.private_vpce[*].id
  security_group_ids  = [aws_security_group.vpce.id]
  
  private_dns_enabled = true
  
  tags = {
    Name        = "vpce-secretsmanager"
    Environment = "production"
  }
}

# Security group for VPC endpoints
resource "aws_security_group" "vpce" {
  name        = "sg-vpce"
  description = "Security group for VPC endpoints"
  vpc_id      = aws_vpc.vehixcare.id
  
  ingress {
    description     = "Allow from VPC"
    from_port       = 443
    to_port         = 443
    protocol        = "tcp"
    cidr_blocks     = [aws_vpc.vehixcare.cidr_block]
  }
  
  tags = {
    Name        = "sg-vpce"
    Environment = "production"
  }
}

# Outputs
output "secrets_manager_arns" {
  value = {
    documentdb = aws_secretsmanager_secret.documentdb_connection.arn
    jwt        = aws_secretsmanager_secret.jwt_secret.arn
    google_id  = aws_secretsmanager_secret.google_client_id.arn
    google_secret = aws_secretsmanager_secret.google_client_secret.arn
  }
  sensitive = true
}
```

### 3.6 EKS Cluster with Managed Node Groups

```hcl
# eks-cluster.tf
data "aws_iam_policy_document" "eks_cluster_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "eks_cluster" {
  name               = "eks-cluster-vehixcare"
  assume_role_policy = data.aws_iam_policy_document.eks_cluster_assume_role.json
  
  tags = {
    Environment = "production"
  }
}

resource "aws_iam_role_policy_attachment" "eks_cluster_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks_cluster.name
}

resource "aws_iam_role_policy_attachment" "eks_service_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
  role       = aws_iam_role.eks_cluster.name
}

# EKS Cluster
resource "aws_eks_cluster" "vehixcare" {
  name     = "eks-vehixcare-prod"
  role_arn = aws_iam_role.eks_cluster.arn
  version  = "1.28"
  
  vpc_config {
    subnet_ids              = aws_subnet.private_eks[*].id
    security_group_ids      = [aws_security_group.eks_cluster.id]
    endpoint_private_access = true
    endpoint_public_access  = false
  }
  
  kubernetes_network_config {
    service_ipv4_cidr = "172.20.0.0/16"
    ip_family         = "ipv4"
  }
  
  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
  
  tags = {
    Environment = "production"
    Application = "vehixcare"
    ManagedBy   = "terraform"
  }
}

# Node group IAM role
data "aws_iam_policy_document" "eks_node_group_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "eks_node_group" {
  name               = "eks-nodegroup-vehixcare"
  assume_role_policy = data.aws_iam_policy_document.eks_node_group_assume_role.json
  
  tags = {
    Environment = "production"
  }
}

resource "aws_iam_role_policy_attachment" "eks_worker_node_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.eks_node_group.name
}

resource "aws_iam_role_policy_attachment" "eks_cni_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.eks_node_group.name
}

resource "aws_iam_role_policy_attachment" "eks_ecr_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.eks_node_group.name
}

# System Node Group (critical cluster components)
resource "aws_eks_node_group" "system" {
  cluster_name    = aws_eks_cluster.vehixcare.name
  node_group_name = "system-group"
  node_role_arn   = aws_iam_role.eks_node_group.arn
  subnet_ids      = aws_subnet.private_eks[*].id
  instance_types  = ["t3.large"]
  capacity_type   = "ON_DEMAND"
  
  scaling_config {
    desired_size = 3
    min_size     = 3
    max_size     = 5
  }
  
  update_config {
    max_unavailable = 1
  }
  
  labels = {
    "node-group" = "system"
    "environment" = "production"
    "critical" = "true"
  }
  
  taint {
    key    = "CriticalAddonsOnly"
    value  = "true"
    effect = "NO_SCHEDULE"
  }
  
  tags = {
    Environment = "production"
    NodeGroup   = "system"
  }
  
  depends_on = [
    aws_iam_role_policy_attachment.eks_worker_node_policy,
    aws_iam_role_policy_attachment.eks_cni_policy,
    aws_iam_role_policy_attachment.eks_ecr_policy,
  ]
}

# User Node Group (application workloads)
resource "aws_eks_node_group" "user" {
  cluster_name    = aws_eks_cluster.vehixcare.name
  node_group_name = "user-group"
  node_role_arn   = aws_iam_role.eks_node_group.arn
  subnet_ids      = aws_subnet.private_eks[*].id
  instance_types  = ["m5.2xlarge"]
  capacity_type   = "ON_DEMAND"
  
  scaling_config {
    desired_size = 5
    min_size     = 5
    max_size     = 20
  }
  
  update_config {
    max_unavailable = 1
  }
  
  labels = {
    "node-group" = "user"
    "environment" = "production"
    "workload" = "telemetry"
  }
  
  tags = {
    Environment = "production"
    NodeGroup   = "user"
  }
  
  depends_on = [
    aws_iam_role_policy_attachment.eks_worker_node_policy,
    aws_iam_role_policy_attachment.eks_cni_policy,
    aws_iam_role_policy_attachment.eks_ecr_policy,
  ]
}

# OIDC provider for EKS (required for IRSA)
data "tls_certificate" "eks_oidc" {
  url = aws_eks_cluster.vehixcare.identity[0].oidc[0].issuer
}

resource "aws_iam_openid_connect_provider" "eks" {
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = [data.tls_certificate.eks_oidc.certificates[0].sha1_fingerprint]
  url             = aws_eks_cluster.vehixcare.identity[0].oidc[0].issuer
}

# Outputs
output "kubeconfig" {
  value = sensitive(templatefile("${path.module}/kubeconfig.tpl", {
    cluster_name = aws_eks_cluster.vehixcare.name
    endpoint     = aws_eks_cluster.vehixcare.endpoint
    ca_data      = aws_eks_cluster.vehixcare.certificate_authority[0].data
  }))
  sensitive = true
}

output "eks_cluster_name" {
  value = aws_eks_cluster.vehixcare.name
}
```

### 3.7 AWS Load Balancer Controller and Network Load Balancer

```hcl
# lb-controller.tf
# IAM role for AWS Load Balancer Controller
data "aws_iam_policy_document" "lb_controller_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Federated"
      identifiers = [aws_iam_openid_connect_provider.eks.arn]
    }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test     = "StringEquals"
      variable = "${replace(aws_iam_openid_connect_provider.eks.url, "https://", "")}:aud"
      values   = ["sts.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "lb_controller" {
  name               = "aws-load-balancer-controller"
  assume_role_policy = data.aws_iam_policy_document.lb_controller_assume_role.json
}

resource "aws_iam_policy" "lb_controller" {
  name        = "AWSLoadBalancerControllerPolicy"
  description = "Policy for AWS Load Balancer Controller"
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "iam:CreateServiceLinkedRole",
          "ec2:DescribeAccountAttributes",
          "ec2:DescribeAddresses",
          "ec2:DescribeAvailabilityZones",
          "ec2:DescribeInternetGateways",
          "ec2:DescribeVpcs",
          "ec2:DescribeSubnets",
          "ec2:DescribeSecurityGroups",
          "ec2:DescribeNetworkInterfaces",
          "ec2:DescribeNetworkInterfaceAttribute",
          "ec2:CreateSecurityGroup",
          "ec2:CreateNetworkInterface",
          "ec2:ModifyNetworkInterfaceAttribute",
          "ec2:DeleteNetworkInterface",
          "ec2:AuthorizeSecurityGroupIngress",
          "ec2:RevokeSecurityGroupIngress",
          "elasticloadbalancing:DescribeLoadBalancers",
          "elasticloadbalancing:DescribeLoadBalancerAttributes",
          "elasticloadbalancing:DescribeListeners",
          "elasticloadbalancing:DescribeListenerAttributes",
          "elasticloadbalancing:DescribeTargetGroups",
          "elasticloadbalancing:DescribeTargetGroupAttributes",
          "elasticloadbalancing:DescribeTargetHealth",
          "elasticloadbalancing:CreateLoadBalancer",
          "elasticloadbalancing:CreateListener",
          "elasticloadbalancing:CreateTargetGroup",
          "elasticloadbalancing:RegisterTargets",
          "elasticloadbalancing:DeleteLoadBalancer",
          "elasticloadbalancing:DeleteListener",
          "elasticloadbalancing:DeleteTargetGroup",
          "elasticloadbalancing:ModifyLoadBalancerAttributes",
          "elasticloadbalancing:ModifyListener",
          "elasticloadbalancing:ModifyTargetGroup",
          "elasticloadbalancing:ModifyTargetGroupAttributes",
          "elasticloadbalancing:DeregisterTargets",
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lb_controller" {
  policy_arn = aws_iam_policy.lb_controller.arn
  role       = aws_iam_role.lb_controller.name
}

# Network Load Balancer (for AppSync GraphQL subscriptions)
resource "aws_lb" "vehixcare_nlb" {
  name               = "nlb-vehixcare"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.private_nlb[*].id
  
  enable_deletion_protection = true
  
  tags = {
    Environment = "production"
    Service     = "appsync-subscriptions"
  }
}

resource "aws_lb_target_group" "appsync" {
  name        = "tg-appsync"
  port        = 80
  protocol    = "TCP"
  vpc_id      = aws_vpc.vehixcare.id
  target_type = "ip"
  
  health_check {
    protocol = "HTTP"
    path     = "/health/live"
    interval = 30
    timeout  = 10
  }
  
  tags = {
    Environment = "production"
  }
}

resource "aws_lb_listener" "appsync" {
  load_balancer_arn = aws_lb.vehixcare_nlb.arn
  port              = 443
  protocol          = "TLS"
  ssl_policy        = "ELBSecurityPolicy-TLS13-1-2-2021-06"
  certificate_arn   = aws_acm_certificate.vehixcare.arn
  
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.appsync.arn
  }
}

# ACM Certificate for NLB
resource "aws_acm_certificate" "vehixcare" {
  domain_name       = "api.vehixcare.com"
  validation_method = "DNS"
  
  tags = {
    Environment = "production"
  }
}
```

### 3.8 Common Terraform Pitfalls and Mitigations (AWS)

![Table](images/table_04_38-common-terraform-pitfalls-and-mitigations-c656.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_04_38-common-terraform-pitfalls-and-mitigations-c656.md)


---

## 4. Kubernetes on AWS (EKS): Complete Implementation

### 4.1 Namespace Strategy

```yaml
# namespaces.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare-telemetry
  labels:
    name: vehixcare-telemetry
    environment: production
    pod-security.kubernetes.io/enforce: restricted
---
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare-appsync
  labels:
    name: vehixcare-appsync
    environment: production
---
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare-background
  labels:
    name: vehixcare-background
    environment: production
---
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare-monitoring
  labels:
    name: vehixcare-monitoring
---
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare-ingress
  labels:
    name: vehixcare-ingress
---
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare-keda
  labels:
    name: vehixcare-keda
```

### 4.2 Secret Provider Class for AWS Secrets Manager

```yaml
# secret-provider-class.yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: aws-secrets-manager
  namespace: vehixcare-telemetry
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "vehixcare/documentdb-connection-string"
        objectType: "secretsmanager"
        jmesPath:
          - path: "secret_string"
            objectAlias: "connection-string"
      - objectName: "vehixcare/jwt-signing-secret"
        objectType: "secretsmanager"
        jmesPath:
          - path: "secret_string"
            objectAlias: "jwt-secret"
      - objectName: "vehixcare/google-oauth-client-id"
        objectType: "secretsmanager"
        jmesPath:
          - path: "secret_string"
            objectAlias: "client-id"
      - objectName: "vehixcare/google-oauth-client-secret"
        objectType: "secretsmanager"
        jmesPath:
          - path: "secret_string"
            objectAlias: "client-secret"
    region: "us-east-1"
  secretObjects:
  - secretName: documentdb-secret
    type: Opaque
    data:
    - objectName: connection-string
      key: connection-string
  - secretName: jwt-secret
    type: Opaque
    data:
    - objectName: jwt-secret
      key: secret
  - secretName: google-secret
    type: Opaque
    data:
    - objectName: client-id
      key: client-id
    - objectName: client-secret
      key: client-secret
---
# Service Account with IRSA for Secrets Manager access
apiVersion: v1
kind: ServiceAccount
metadata:
  name: telemetry-api-sa
  namespace: vehixcare-telemetry
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT_ID:role/secrets-manager-access
```

### 4.3 Telemetry API Deployment (AWS Edition)

```yaml
# telemetry-api-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: telemetry-api
  namespace: vehixcare-telemetry
  labels:
    app: vehixcare
    service: telemetry
    version: v2
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: vehixcare
      service: telemetry
  template:
    metadata:
      labels:
        app: vehixcare
        service: telemetry
        version: v2
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: telemetry-api-sa
      
      nodeSelector:
        node-group: user
      
      containers:
      - name: telemetry-api
        image: ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-api:3.2.1
        imagePullPolicy: Always
        
        ports:
        - containerPort: 8080
          name: http
          protocol: TCP
        
        env:
        - name: ConnectionStrings__MongoDB
          valueFrom:
            secretKeyRef:
              name: documentdb-secret
              key: connection-string
        - name: ConnectionStrings__MongoDB__Database
          value: "vehixcare-telemetry"
        - name: ConnectionStrings__MongoDB__Options
          value: "retryWrites=true&tls=true&tlsCAFile=/etc/ssl/certs/global-bundle.pem&maxPoolSize=200"
        
        - name: Authentication__Jwt__Secret
          valueFrom:
            secretKeyRef:
              name: jwt-secret
              key: secret
        - name: Authentication__Jwt__Issuer
          value: "vehixcare.com"
        - name: Authentication__Jwt__Audience
          value: "api.vehixcare.com"
        
        - name: Authentication__Google__ClientId
          valueFrom:
            secretKeyRef:
              name: google-secret
              key: client-id
        - name: Authentication__Google__ClientSecret
          valueFrom:
            secretKeyRef:
              name: google-secret
              key: client-secret
        
        - name: Eventing__Provider
          value: "AWS"
        - name: Eventing__AWS__EventBusName
          value: "vehixcare-telemetry-bus"
        - name: Eventing__AWS__Region
          value: "us-east-1"
        
        - name: ASPNETCORE_ENVIRONMENT
          value: "Production"
        
        resources:
          requests:
            cpu: "1000m"
            memory: "2Gi"
          limits:
            cpu: "3000m"
            memory: "4Gi"
        
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        
        startupProbe:
          httpGet:
            path: /health/startup
            port: 8080
          initialDelaySeconds: 0
          periodSeconds: 5
          failureThreshold: 30
        
        volumeMounts:
        - name: secrets-store
          mountPath: "/mnt/secrets"
          readOnly: true
        - name: documentdb-ca
          mountPath: "/etc/ssl/certs"
          readOnly: true
        
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          capabilities:
            drop:
            - ALL
          readOnlyRootFilesystem: true
      
      volumes:
      - name: secrets-store
        csi:
          driver: secrets-store.csi.k8s.io
          readOnly: true
          volumeAttributes:
            secretProviderClass: "aws-secrets-manager"
      - name: documentdb-ca
        configMap:
          name: documentdb-ca-bundle
      
      securityContext:
        fsGroup: 1000
      
      terminationGracePeriodSeconds: 60
      
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - vehixcare
                - key: service
                  operator: In
                  values:
                  - telemetry
              topologyKey: kubernetes.io/hostname
---
apiVersion: v1
kind: Service
metadata:
  name: telemetry-api-service
  namespace: vehixcare-telemetry
  labels:
    app: vehixcare
    service: telemetry
spec:
  selector:
    app: vehixcare
    service: telemetry
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
    name: http
  type: ClusterIP
```

### 4.4 Horizontal Pod Autoscaler with Custom Metrics (AWS)

```yaml
# telemetry-hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: telemetry-api-hpa
  namespace: vehixcare-telemetry
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: telemetry-api
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  - type: Pods
    pods:
      metric:
        name: telemetry_messages_per_second
      target:
        type: AverageValue
        averageValue: "1000"
  - type: Pods
    pods:
      metric:
        name: mongodb_connection_pool_usage
      target:
        type: AverageValue
        averageValue: "150"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
      selectPolicy: Min
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 30
      selectPolicy: Max
```

### 4.5 KEDA Scaler for Event-Driven Autoscaling (AWS SQS)

```yaml
# keda-scaler.yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: notification-scaler
  namespace: vehixcare-background
spec:
  scaleTargetRef:
    name: notification-processor
  minReplicaCount: 1
  maxReplicaCount: 50
  triggers:
  - type: aws-sqs-queue
    metadata:
      queueURL: https://sqs.us-east-1.amazonaws.com/ACCOUNT_ID/vehixcare-telemetry-queue
      queueLength: "10"
      awsRegion: "us-east-1"
    authenticationRef:
      name: keda-trigger-auth-sqs
---
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-sqs
  namespace: vehixcare-background
spec:
  podIdentity:
    provider: aws
    roleArn: arn:aws:iam::ACCOUNT_ID:role/keda-sqs-access
```

### 4.6 AppSync Resolver Deployment for Real-time Streaming

```yaml
# appsync-resolver-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: appsync-resolver
  namespace: vehixcare-appsync
  labels:
    app: vehixcare
    component: appsync
spec:
  replicas: 2
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: vehixcare
      component: appsync
  template:
    metadata:
      labels:
        app: vehixcare
        component: appsync
    spec:
      containers:
      - name: appsync-resolver
        image: ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-hubs:latest
        imagePullPolicy: Always
        
        ports:
        - containerPort: 8080
          name: http
        
        env:
        - name: ConnectionStrings__MongoDB
          valueFrom:
            secretKeyRef:
              name: documentdb-secret
              key: connection-string
        - name: AppSync__ApiId
          value: "YOUR_APPSYNC_API_ID"
        - name: AppSync__Endpoint
          value: "https://xxxxxxxxxxxxxxxxxx.appsync-api.us-east-1.amazonaws.com/graphql"
        
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "2000m"
            memory: "2Gi"
        
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
          initialDelaySeconds: 20
          periodSeconds: 10
        
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: appsync-resolver-service
  namespace: vehixcare-appsync
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
    service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "3600"
spec:
  selector:
    app: vehixcare
    component: appsync
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
    name: http
  type: LoadBalancer
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
```

### 4.7 Rx.NET Background Processor Deployment

```yaml
# background-processor-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: behavior-processor
  namespace: vehixcare-background
  labels:
    app: vehixcare
    component: processor
    type: rxnet
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vehixcare
      component: processor
  template:
    metadata:
      labels:
        app: vehixcare
        component: processor
        type: rxnet
    spec:
      containers:
      - name: processor
        image: ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-processor:latest
        imagePullPolicy: Always
        
        env:
        - name: ConnectionStrings__MongoDB
          valueFrom:
            secretKeyRef:
              name: documentdb-secret
              key: connection-string
        - name: ConnectionStrings__MongoDB__Database
          value: "vehixcare-telemetry"
        
        - name: RxNET__BufferTimeoutSeconds
          value: "5"
        - name: RxNET__MaxBufferSize
          value: "10000"
        - name: RxNET__ThrottleMilliseconds
          value: "100"
        - name: RxNET__WindowCount
          value: "1000"
        - name: RxNET__WindowTimeSeconds
          value: "10"
        
        - name: Eventing__Provider
          value: "Kafka"
        - name: Eventing__Kafka__BootstrapServers
          value: "kafka-cluster.kafka:9092"
        - name: Eventing__Kafka__Topic
          value: "telemetry-events"
        - name: Eventing__Kafka__ConsumerGroup
          value: "behavior-processor"
        
        resources:
          requests:
            cpu: "2000m"
            memory: "4Gi"
          limits:
            cpu: "4000m"
            memory: "8Gi"
        
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 5
```

### 4.8 Geo-fence Monitor Deployment

```yaml
# geofence-monitor-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: geofence-monitor
  namespace: vehixcare-background
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vehixcare
      service: geofence
  template:
    metadata:
      labels:
        app: vehixcare
        service: geofence
    spec:
      containers:
      - name: geofence-monitor
        image: ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-geofence:latest
        env:
        - name: ConnectionStrings__MongoDB
          valueFrom:
            secretKeyRef:
              name: documentdb-secret
              key: connection-string
        - name: GEO__CACHE_TTL_SECONDS
          value: "300"
        - name: GEO__BATCH_SIZE
          value: "1000"
        - name: GEO__REDIS_ENDPOINT
          value: "vehixcare-cache.xxxxxx.ng.0001.use1.cache.amazonaws.com:6379"
        resources:
          requests:
            cpu: "1000m"
            memory: "2Gi"
          limits:
            cpu: "2000m"
            memory: "4Gi"
```

### 4.9 Ingress with AWS Load Balancer Controller

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: vehixcare-ingress
  namespace: vehixcare-telemetry
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}]'
    alb.ingress.kubernetes.io/ssl-redirect: "443"
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:us-east-1:ACCOUNT_ID:certificate/xxxxx
    alb.ingress.kubernetes.io/healthcheck-path: /health/live
    alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
    alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "10"
    alb.ingress.kubernetes.io/healthy-threshold-count: "3"
    alb.ingress.kubernetes.io/unhealthy-threshold-count: "3"
    alb.ingress.kubernetes.io/load-balancer-attributes: idle_timeout.timeout_seconds=3600
    alb.ingress.kubernetes.io/group.name: vehixcare
    alb.ingress.kubernetes.io/wafv2-acl-arn: arn:aws:wafv2:us-east-1:ACCOUNT_ID:regional/webacl/vehixcare-waf/xxxxx
spec:
  rules:
  - host: api.vehixcare.com
    http:
      paths:
      - path: /api/telemetry
        pathType: Prefix
        backend:
          service:
            name: telemetry-api-service
            port:
              number: 80
      - path: /api/vehicles
        pathType: Prefix
        backend:
          service:
            name: telemetry-api-service
            port:
              number: 80
      - path: /api/drivers
        pathType: Prefix
        backend:
          service:
            name: telemetry-api-service
            port:
              number: 80
      - path: /api/geofences
        pathType: Prefix
        backend:
          service:
            name: telemetry-api-service
            port:
              number: 80
  - host: dashboard.vehixcare.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: dashboard-service
            port:
              number: 80
```

### 4.10 Prometheus ServiceMonitor for Metrics Collection

```yaml
# servicemonitor.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: vehixcare-telemetry
  namespace: vehixcare-monitoring
spec:
  selector:
    matchLabels:
      app: vehixcare
      service: telemetry
  endpoints:
  - port: http
    path: /metrics
    interval: 30s
    scrapeTimeout: 10s
  namespaceSelector:
    matchNames:
    - vehixcare-telemetry
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: vehixcare-appsync
  namespace: vehixcare-monitoring
spec:
  selector:
    matchLabels:
      app: vehixcare
      component: appsync
  endpoints:
  - port: http
    path: /metrics
    interval: 30s
```

### 4.11 Common Kubernetes Pitfalls and Mitigations (AWS)

![Table](images/table_05_411-common-kubernetes-pitfalls-and-mitigation-a3bf.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_05_411-common-kubernetes-pitfalls-and-mitigation-a3bf.md)


---

## 5. Stitching Together: Terraform and Kubernetes Integration (AWS)

### 5.1 Integration Workflow (AWS)

```mermaid
```

![Calico network policy performance](images/diagram_11_51-integration-workflow-aws.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/diagram_11_51-integration-workflow-aws.md)


### 5.2 Complete GitHub Actions CI/CD Pipeline (AWS)

```yaml
# .github/workflows/deploy-aws.yml
name: Deploy Vehixcare to EKS

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options:
        - staging
        - production

env:
  AWS_REGION: us-east-1
  EKS_CLUSTER_NAME: eks-vehixcare-prod
  ECR_REPOSITORY: vehixcare-api
  NAMESPACE: vehixcare-telemetry

jobs:
  terraform:
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment || 'staging' }}
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
        with:
          terraform_version: 1.5.0
      
      - name: Terraform Init
        run: terraform init
        working-directory: ./terraform/aws
      
      - name: Terraform Plan
        run: terraform plan -out=tfplan
        working-directory: ./terraform/aws
      
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve tfplan
        working-directory: ./terraform/aws
      
      - name: Get Terraform Outputs
        if: github.ref == 'refs/heads/main'
        id: tf-output
        run: |
          echo "documentdb_connection=$(terraform output -raw documentdb_connection_string)" >> $GITHUB_OUTPUT
          echo "ecr_url=$(terraform output -raw ecr_repository_urls)" >> $GITHUB_OUTPUT
          echo "kubeconfig=$(terraform output -raw kubeconfig)" >> $GITHUB_OUTPUT
        working-directory: ./terraform/aws

  build-and-push:
    runs-on: ubuntu-latest
    needs: terraform
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Login to Amazon ECR
        uses: aws-actions/amazon-ecr-login@v1
      
      - name: Build and Push Telemetry API
        run: |
          docker build -t ${{ needs.terraform.outputs.ecr_url }}:${{ github.sha }} -f Vehixcare.API/Dockerfile .
          docker build -t ${ECR_REPOSITORY%/*}/vehixcare-hubs:${{ github.sha }} -f Vehixcare.Hubs/Dockerfile .
          docker build -t ${ECR_REPOSITORY%/*}/vehixcare-processor:${{ github.sha }} -f Vehixcare.BackgroundServices/Dockerfile .
          docker build -t ${ECR_REPOSITORY%/*}/vehixcare-geofence:${{ github.sha }} -f Vehixcare.GeoFence/Dockerfile .
          
          docker push ${{ needs.terraform.outputs.ecr_url }}:${{ github.sha }}
          docker push ${ECR_REPOSITORY%/*}/vehixcare-hubs:${{ github.sha }}
          docker push ${ECR_REPOSITORY%/*}/vehixcare-processor:${{ github.sha }}
          docker push ${ECR_REPOSITORY%/*}/vehixcare-geofence:${{ github.sha }}
      
      - name: Tag Latest
        run: |
          docker tag ${{ needs.terraform.outputs.ecr_url }}:${{ github.sha }} ${{ needs.terraform.outputs.ecr_url }}:latest
          docker push ${{ needs.terraform.outputs.ecr_url }}:latest

  deploy-kubernetes:
    runs-on: ubuntu-latest
    needs: [terraform, build-and-push]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Setup kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'latest'
      
      - name: Update kubeconfig
        run: |
          aws eks update-kubeconfig --name ${{ env.EKS_CLUSTER_NAME }} --region ${{ env.AWS_REGION }}
      
      - name: Create DocumentDB Secret from Terraform Output
        run: |
          kubectl create secret generic documentdb-secret \
            --namespace ${{ env.NAMESPACE }} \
            --from-literal=connection-string="${{ needs.terraform.outputs.documentdb_connection }}" \
            --dry-run=client -o yaml | kubectl apply -f -
      
      - name: Apply SecretProviderClass
        run: |
          envsubst < k8s/secret-provider-class.yaml | kubectl apply -f -
      
      - name: Deploy Telemetry API
        run: |
          sed -i "s|ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-api:latest|${{ needs.terraform.outputs.ecr_url }}:${{ github.sha }}|g" k8s/telemetry-api-deployment.yaml
          kubectl apply -f k8s/namespaces.yaml
          kubectl apply -f k8s/telemetry-api-deployment.yaml
          kubectl apply -f k8s/telemetry-hpa.yaml
      
      - name: Deploy AppSync Resolver
        run: |
          sed -i "s|ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-hubs:latest|${ECR_REPOSITORY%/*}/vehixcare-hubs:${{ github.sha }}|g" k8s/appsync-resolver-deployment.yaml
          kubectl apply -f k8s/appsync-resolver-deployment.yaml
      
      - name: Deploy Background Processors
        run: |
          sed -i "s|ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/vehixcare-processor:latest|${ECR_REPOSITORY%/*}/vehixcare-processor:${{ github.sha }}|g" k8s/background-processor-deployment.yaml
          kubectl apply -f k8s/background-processor-deployment.yaml
          kubectl apply -f k8s/geofence-monitor-deployment.yaml
      
      - name: Deploy Ingress
        run: |
          kubectl apply -f k8s/ingress.yaml
      
      - name: Wait for Rollout
        run: |
          kubectl rollout status deployment/telemetry-api -n ${{ env.NAMESPACE }} --timeout=5m
          kubectl rollout status deployment/appsync-resolver -n vehixcare-appsync --timeout=5m
          kubectl rollout status deployment/behavior-processor -n vehixcare-background --timeout=5m
      
      - name: Verify DocumentDB Connection
        run: |
          kubectl exec -n ${{ env.NAMESPACE }} deployment/telemetry-api -- \
            curl -s http://localhost:8080/health/db
      
      - name: Post-Deployment Smoke Tests
        run: |
          kubectl exec -n ${{ env.NAMESPACE }} deployment/telemetry-api -- \
            curl -X POST http://localhost:8080/api/telemetry \
            -H "Content-Type: application/json" \
            -d '{"vehicleId":"test","gpsSpeed":60,"engineRPM":2000}'
```

---

## 6. Summary: Terraform vs Kubernetes on AWS

![6. Summary: Terraform vs Kubernetes on AWS](images/table_06_6-summary-terraform-vs-kubernetes-on-aws-dd7c.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_06_6-summary-terraform-vs-kubernetes-on-aws-dd7c.md)


**The Golden Rule (AWS Edition):** Terraform provisions what AWS bills for. Kubernetes runs what customers interact with. Neither replaces the other—they form a complete cloud-native stack on AWS.

---

## Conclusion: How This Architecture Benefits Vehixcare on AWS

The Terraform and Kubernetes integration documented above delivers measurable operational and business benefits for the Vehixcare fleet telemetry platform on AWS. Below is a summary of how each architectural decision translates to real-world advantages.

---

### Operational Benefits

**Zero-Downtime Deployments:** Kubernetes rolling updates with `maxSurge: 1` and `maxUnavailable: 0` allow Vehixcare to deploy new versions of the Telemetry API without interrupting active GPS data ingestion. Deployments complete in under 60 seconds with no dropped connections.

**Automatic Scaling Based on Telemetry Load:** The Horizontal Pod Autoscaler scales the Telemetry API from 3 to 20 replicas when telemetry messages exceed 1,000 per second. During peak hours, the platform automatically adds capacity. During off-peak, it scales down, reducing AWS costs by approximately 35%.

**Self-Healing Infrastructure:** Kubernetes liveness probes detect when the Telemetry API loses DocumentDB connectivity. The system automatically restarts affected pods within 15 seconds.

**Secure Secret Management Without Human Touch:** The Secrets Store CSI driver polls AWS Secrets Manager every 5 minutes. When Vehixcare rotates JWT signing keys, pods receive new secrets within the polling window—no pod restart required.

**Multi-Region Resilience:** Terraform configures DocumentDB Global Cluster with automatic failover between us-east-1 (primary) and us-west-2 (secondary). When a regional outage occurs, promotion completes within minutes.

**Efficient Resource Utilization:** Separating system node groups (t3.large, 3-5 nodes) from user node groups (m5.2xlarge, 5-20 nodes) prevents telemetry processing workloads from starving critical cluster components.

---

### Feature-Specific Benefits (AWS)

**Real-time Vehicle Telemetry:** The AppSync resolver deployment with NLB and session affinity maintains WebSocket connections across pod restarts. Fleet dashboards receive live GPS updates via GraphQL subscriptions with sub-second latency.

**Driver Behavior Analysis:** Rx.NET background processors run in dedicated pods with memory limits (8 Gi maximum) and backpressure handling (`Buffer(TimeSpan.FromSeconds(5))`). KEDA scales the processor from 2 to 15 pods based on SQS queue depth.

**Geo-fencing:** The dedicated geo-fence monitor pod caches active boundaries in ElastiCache (Redis, TTL 300 seconds), reducing DocumentDB query load by 90%. Vehicle boundary crossings trigger alerts within 500 milliseconds.

**Anti-theft Protection:** DocumentDB change stream processors run as Kubernetes deployments, triggering anomaly detection and immediate alerts.

**Multi-tenant Architecture:** Kubernetes namespaces isolate workloads. Network policies (Calico) restrict cross-namespace communication. DocumentDB partition keys (`organization_id`) ensure tenant data isolation.

---

### Cost and Performance Metrics (AWS vs. Azure)

![Geo-fencing:](images/table_07_cost-and-performance-metrics-aws-vs-azure-0a78.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_07_cost-and-performance-metrics-aws-vs-azure-0a78.md)


---

### AWS-Specific Advantages

![7% lower on AWS](images/table_08_aws-specific-advantages.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_08_aws-specific-advantages.md)


---

### Summary: Why This Architecture Works for Vehixcare on AWS

![Table](images/table_09_summary-why-this-architecture-works-for-vehix-c886.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_09_summary-why-this-architecture-works-for-vehix-c886.md)


**Final Verdict:** Terraform provides the reproducible, auditable foundation of AWS resources. Kubernetes provides the resilient, auto-scaling runtime for Vehixcare's telemetry processing. Together, they reduce costs by 35%, increase throughput by 5x, and eliminate deployment-related downtime. The architecture transforms Vehixcare from a fragile, manually-operated platform into a self-healing, cloud-native system that can scale to millions of vehicles.

---

## Appendix: Service Mapping (Azure → AWS)

![Final Verdict:](images/table_10_appendix-service-mapping-azure--aws-81c1.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/terraform-with-kubernetes-on-aws-a-complete-architectural-guide-with-vehixcare/table_10_appendix-service-mapping-azure--aws-81c1.md)


---

*This AWS adaptation maintains all Vehixcare .NET 9.0 application code, Rx.NET telemetry processing pipelines, geo-fencing algorithms, and driver behavior scoring logic from the original Azure architecture. Only the underlying cloud infrastructure and service mappings have been adapted for AWS.*

*Original article: "Terraform with Kubernetes on Azure: A Complete Architectural Guide With Vehixcare" by Vineet Sharma*
*Link: [https://medium.com/@mvineetsharma/terraform-with-kubernetes-on-azure-a-complete-architectural-guide-with-vehixcare-270315058bc3?sk=f391b74ec4245e73c319c05d51480dbd](https://medium.com/@mvineetsharma/terraform-with-kubernetes-on-azure-a-complete-architectural-guide-with-vehixcare-270315058bc3?sk=f391b74ec4245e73c319c05d51480dbd)*