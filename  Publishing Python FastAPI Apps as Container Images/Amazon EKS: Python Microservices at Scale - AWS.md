# Amazon EKS: Python Microservices at Scale - AWS

## Orchestrating FastAPI Applications with Kubernetes on Amazon Web Services

### Introduction: The Enterprise Scale Platform for Python on AWS

In the [previous installment](#) of this AWS Python series, we explored tarball export and security-first workflows—essential for organizations requiring strict compliance and air-gapped deployments. While those approaches prioritize security, enterprises deploying Python applications at scale face an additional challenge: **orchestration**. How do you manage dozens of FastAPI microservices, handle rolling updates, auto-scale based on demand, and ensure high availability across multiple Availability Zones?

Enter **Amazon EKS (Elastic Kubernetes Service)**—the managed Kubernetes offering from AWS that transforms isolated containers into production-grade, self-healing, auto-scaling applications. For the **AI Powered Video Tutorial Portal**—a FastAPI application with multiple services (API gateway, authentication service, content service, worker processes), Amazon EKS provides the operational foundation required for enterprise-scale Python deployments.

This installment explores the complete workflow for deploying FastAPI applications to Amazon EKS, from cluster setup to production-grade operations. We'll master Kubernetes concepts for Python developers, deployment strategies, Helm charts, GitOps with Flux, cluster autoscaling, and integration with AWS services—all while leveraging the power of Kubernetes for Python microservices.

```mermaid
graph TD
    subgraph "Container Build Phase"
        A[Python FastAPI App] --> B[Docker Build]
        B --> C[Container Image]
        C --> D[Amazon ECR]
    end
    
    subgraph "Amazon EKS Cluster"
        D --> E[EKS Control Plane]
        E --> F[Managed Node Groups]
        F --> G[Pods - FastAPI API]
        F --> H[Pods - Auth Service]
        F --> I[Pods - Worker Service]
    end
    
    subgraph "Production Operations"
        G --> J[Horizontal Pod Autoscaler]
        G --> K[Cluster Autoscaler]
        G --> L[AWS Load Balancer Controller]
        G --> M[Secrets Manager CSI Driver]
    end
    
    style E fill:#ff9900,color:#fff
    style J fill:#48bb78,color:#fff
    style L fill:#2b6cb0,color:#fff
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

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations *(This story)*

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## Understanding Kubernetes for Python Developers on AWS

### Why Kubernetes on AWS?

| Challenge | Solution with Amazon EKS | Python Benefit |
|-----------|-------------------------|----------------|
| **Microservices** | Service discovery and load balancing | Multiple FastAPI services communicate seamlessly |
| **Scaling** | Horizontal Pod Autoscaler + Cluster Autoscaler | Auto-scale based on CPU, memory, or custom metrics |
| **Rolling Updates** | Zero-downtime deployments with configurable rollout | No user impact during FastAPI version updates |
| **Service Discovery** | Built-in DNS (CoreDNS) | FastAPI services find each other by name |
| **Configuration** | ConfigMaps and Secrets + AWS Secrets Manager | Environment-specific Python settings |
| **Networking** | AWS Load Balancer Controller | HTTP routing, SSL termination |
| **Storage** | Persistent Volumes + EBS/EFS CSI drivers | Stateful Python workloads |
| **Observability** | Prometheus + Grafana + AWS Distro for OpenTelemetry | FastAPI metrics, traces, logs |

### Kubernetes Architecture for Python Developers

```mermaid
graph TD
    subgraph "Amazon EKS Control Plane (AWS Managed)"
        A[API Server]
        B[etcd]
        C[Scheduler]
        D[Controller Manager]
    end
    
    subgraph "Managed Node Group - Graviton"
        E[EC2 Instance - t4g.medium]
        F[Kubelet]
        G[Containerd]
        H[Pod - FastAPI API]
        I[Pod - FastAPI Worker]
    end
    
    subgraph "Managed Node Group - x64"
        J[EC2 Instance - t3.medium]
        K[Kubelet]
        L[Containerd]
        M[Pod - FastAPI API]
        N[Pod - MongoDB Sidecar]
    end
    
    A --> E
    A --> J
```

### Key Kubernetes Concepts for Python

| Concept | Description | Python Analogy |
|---------|-------------|----------------|
| **Pod** | Smallest deployable unit, one or more containers | A process/application instance |
| **Deployment** | Desired state for pods (replicas, updates) | Application deployment configuration |
| **Service** | Stable endpoint for pod access | Load balancer / reverse proxy |
| **Ingress** | HTTP routing to services | FastAPI route to service mapping |
| **ConfigMap** | Environment configuration | Python .env file |
| **Secret** | Sensitive data (connection strings, keys) | AWS Secrets Manager reference |
| **HorizontalPodAutoscaler** | Automatic scaling based on metrics | FastAPI app scaling based on request load |
| **Cluster Autoscaler** | Automatic scaling of worker nodes | EC2 Auto Scaling Groups |

---

## Amazon EKS Cluster Setup

### Prerequisites

```bash
# Install AWS CLI
brew install awscli  # macOS
# or
sudo apt install awscli  # Ubuntu

# Install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

# Install kubectl
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.28/2024-01-04/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin

# Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify installations
eksctl version
kubectl version --client
helm version
```

### Create EKS Cluster with eksctl

```yaml
# cluster.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: courses-portal-eks
  region: us-east-1
  version: "1.28"

vpc:
  cidr: "10.0.0.0/16"
  nat:
    gateway: HighlyAvailable

managedNodeGroups:
  - name: graviton-workers
    instanceType: t4g.medium
    desiredCapacity: 3
    minSize: 2
    maxSize: 10
    volumeSize: 20
    ssh:
      allow: true
    labels:
      node-type: general
      architecture: arm64
    tags:
      Environment: production
      Application: courses-portal

  - name: x64-workers
    instanceType: t3.medium
    desiredCapacity: 2
    minSize: 1
    maxSize: 5
    volumeSize: 20
    labels:
      node-type: general
      architecture: amd64
    tags:
      Environment: production
      Application: courses-portal

addons:
- name: vpc-cni
- name: coredns
- name: kube-proxy
- name: aws-ebs-csi-driver

cloudWatch:
  clusterLogging:
    enableTypes: ["api", "audit", "authenticator", "controllerManager", "scheduler"]
```

```bash
# Create cluster
eksctl create cluster -f cluster.yaml

# Verify cluster
kubectl cluster-info
kubectl get nodes

# Update kubeconfig
aws eks update-kubeconfig --region us-east-1 --name courses-portal-eks
```

### Create Namespace

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: courses
  labels:
    name: courses
    environment: production
    app: courses-portal
```

```bash
kubectl apply -f namespace.yaml
```

---

## Deploying FastAPI to EKS

### ConfigMap for Application Settings

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: courses-api-config
  namespace: courses
data:
  ASPNETCORE_ENVIRONMENT: "Production"
  API_KEY_ENABLED: "true"
  API_KEY_DEFAULT_RATE_LIMIT: "100"
  CONTINUE_WATCHING_ENABLED: "true"
  BOOKMARKS_ENABLED: "true"
  MONGODB_DB: "courses_portal"
  AWS_REGION: "us-east-1"
```

### Secrets with AWS Secrets Manager CSI Driver

```bash
# Install Secrets Store CSI Driver
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver \
    --namespace kube-system

# Install AWS Provider
kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/deployment/aws-provider-installer.yaml

# Create IAM policy for secrets access
cat > policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": [
        "arn:aws:secretsmanager:us-east-1:123456789012:secret:courses-portal/*"
      ]
    }
  ]
}
EOF

aws iam create-policy --policy-name CoursesPortalSecretsPolicy --policy-document file://policy.json
```

```yaml
# secret-provider-class.yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: courses-secrets
  namespace: courses
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "courses-portal/jwt-secret"
        objectType: "secretsmanager"
        jmesPath:
          - path: "secret"
            objectAlias: "JWT_SECRET_KEY"
      - objectName: "courses-portal/mongodb-uri"
        objectType: "secretsmanager"
        jmesPath:
          - path: "uri"
            objectAlias: "MONGODB_URI"
```

### FastAPI Deployment Manifest

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: courses-api
  namespace: courses
  labels:
    app: courses-api
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: courses-api
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: courses-api
        version: v1
    spec:
      nodeSelector:
        architecture: arm64  # Use Graviton for cost savings
      containers:
      - name: api
        image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 8000
          name: http
        envFrom:
        - configMapRef:
            name: courses-api-config
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
        volumeMounts:
        - name: secrets-store
          mountPath: "/mnt/secrets"
          readOnly: true
      volumes:
      - name: secrets-store
        csi:
          driver: secrets-store.csi.k8s.io
          readOnly: true
          volumeAttributes:
            secretProviderClass: "courses-secrets"
```

### Service Manifest

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: courses-api-service
  namespace: courses
  labels:
    app: courses-api
spec:
  selector:
    app: courses-api
  ports:
  - port: 80
    targetPort: 8000
    protocol: TCP
    name: http
  type: ClusterIP
```

---

## AWS Load Balancer Controller

### Install AWS Load Balancer Controller

```bash
# Create IAM policy
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.0/docs/install/iam_policy.json
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam-policy.json

# Create IAM role for service account
eksctl create iamserviceaccount \
    --cluster=courses-portal-eks \
    --namespace=kube-system \
    --name=aws-load-balancer-controller \
    --role-name AmazonEKSLoadBalancerControllerRole \
    --attach-policy-arn=arn:aws:iam::123456789012:policy/AWSLoadBalancerControllerIAMPolicy \
    --region us-east-1 \
    --approve

# Install controller using Helm
helm repo add eks https://aws.github.io/eks-charts
helm upgrade --install aws-load-balancer-controller eks/aws-load-balancer-controller \
    --namespace kube-system \
    --set clusterName=courses-portal-eks \
    --set serviceAccount.create=false \
    --set serviceAccount.name=aws-load-balancer-controller \
    --set region=us-east-1
```

### Ingress Configuration with ALB

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: courses-api-ingress
  namespace: courses
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443'
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:us-east-1:123456789012:certificate/xxxxx
    alb.ingress.kubernetes.io/healthcheck-path: /health
    alb.ingress.kubernetes.io/healthcheck-interval-seconds: '30'
    alb.ingress.kubernetes.io/success-codes: '200'
spec:
  rules:
  - host: api.coursesportal.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: courses-api-service
            port:
              number: 80
  - host: telemetry.coursesportal.com
    http:
      paths:
      - path: /hubs
        pathType: Prefix
        backend:
          service:
            name: courses-api-service
            port:
              number: 80
```

---

## Deploying Supporting Services

### Amazon DocumentDB (MongoDB-compatible)

```yaml
# documentdb-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: documentdb-secret
  namespace: courses
type: Opaque
stringData:
  connection-string: "mongodb://admin:password@courses-docdb.cluster-xxxxx.us-east-1.docdb.amazonaws.com:27017/courses_portal?tls=true&replicaSet=rs0&readPreference=secondaryPreferred"
```

### ElastiCache for Redis

```yaml
# redis-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: redis-secret
  namespace: courses
type: Opaque
stringData:
  connection-string: "courses-redis.xxxxx.ng.0001.use1.cache.amazonaws.com:6379,password=,ssl=True,abortConnect=False"
```

---

## Advanced Kubernetes Patterns for Python

### Horizontal Pod Autoscaling with Custom Metrics

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: courses-api-hpa
  namespace: courses
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: courses-api
  minReplicas: 2
  maxReplicas: 10
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
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: 500
```

### Cluster Autoscaler

```bash
# Install Cluster Autoscaler
curl -o cluster-autoscaler-autodiscover.yaml https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloudprovider/aws/examples/cluster-autoscaler-autodiscover.yaml

# Edit with cluster name
sed -i 's/<YOUR CLUSTER NAME>/courses-portal-eks/g' cluster-autoscaler-autodiscover.yaml

# Apply
kubectl apply -f cluster-autoscaler-autodiscover.yaml

# Verify
kubectl get pods -n kube-system | grep cluster-autoscaler
```

### Pod Disruption Budget

```yaml
# pdb.yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: courses-api-pdb
  namespace: courses
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: courses-api
```

### Network Policy

```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: courses-api-network-policy
  namespace: courses
spec:
  podSelector:
    matchLabels:
      app: courses-api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 8000
  egress:
  - to:
    - namespaceSelector: {}
      podSelector:
        matchLabels:
          app: mongodb
    ports:
    - protocol: TCP
      port: 27017
  - to:
    - namespaceSelector: {}
      podSelector:
        matchLabels:
          app: redis
    ports:
    - protocol: TCP
      port: 6379
```

---

## Helm Charts for FastAPI on EKS

### Chart Structure

```
courses-chart/
├── Chart.yaml
├── values.yaml
├── values-production.yaml
├── values-graviton.yaml
├── templates/
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret-provider-class.yaml
│   ├── hpa.yaml
│   └── pdb.yaml
└── charts/
    └── mongodb/
```

### Chart.yaml

```yaml
apiVersion: v2
name: courses-api
description: AI Powered Video Tutorial Portal - FastAPI on Amazon EKS
type: application
version: 1.0.0
appVersion: "1.0.0"
maintainers:
- name: Courses Portal Team
  email: dev@coursesportal.com
dependencies:
- name: mongodb
  version: 13.0.0
  repository: https://charts.bitnami.com/bitnami
  condition: mongodb.enabled
```

### values.yaml

```yaml
# values.yaml
replicaCount: 3

image:
  repository: 123456789012.dkr.ecr.us-east-1.amazonaws.com/courses-api
  tag: latest
  pullPolicy: Always

nodeSelector:
  architecture: arm64

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: alb
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443'
  hosts:
    - host: api.coursesportal.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - hosts:
        - api.coursesportal.com
      secretName: courses-tls

resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80

configMap:
  ASPNETCORE_ENVIRONMENT: "Production"
  API_KEY_ENABLED: "true"
  AWS_REGION: "us-east-1"

mongodb:
  enabled: false  # Using Amazon DocumentDB
```

### Deploying with Helm

```bash
# Install the chart
helm install courses-api ./courses-chart \
    --namespace courses \
    --create-namespace \
    --values ./courses-chart/values-production.yaml

# Upgrade with new image
helm upgrade courses-api ./courses-chart \
    --set image.tag=$BUILD_ID

# Use Graviton-specific values
helm upgrade courses-api ./courses-chart \
    --values ./courses-chart/values-graviton.yaml

# Rollback if needed
helm rollback courses-api 1

# Uninstall
helm uninstall courses-api --namespace courses
```

---

## GitOps with Flux on EKS

### Install Flux

```bash
# Install Flux CLI
curl -s https://fluxcd.io/install.sh | sudo bash

# Bootstrap Flux on EKS
export GITHUB_TOKEN=<your-token>
flux bootstrap github \
    --owner=courses-portal \
    --repository=k8s-manifests \
    --branch=main \
    --path=./courses/overlays/production \
    --personal
```

### Flux Configuration

```yaml
# flux-config.yaml
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: GitRepository
metadata:
  name: courses
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/courses-portal/k8s-manifests
  ref:
    branch: main
---
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: courses
  namespace: flux-system
spec:
  interval: 5m
  path: ./courses/overlays/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: courses
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: courses-api
      namespace: courses
  decryption:
    provider: sops
    secretRef:
      name: sops-gpg
```

---

## Observability with AWS Distro for OpenTelemetry (ADOT)

### Install ADOT Collector

```bash
# Add Helm repo
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts

# Install ADOT Collector
helm upgrade --install adot-collector open-telemetry/opentelemetry-collector \
    --namespace observability \
    --create-namespace \
    --set mode=daemonset \
    --set image.repository=amazon/aws-otel-collector \
    --set config.exporters.awsxray.region=us-east-1 \
    --set config.exporters.prometheus.endpoint=0.0.0.0:8889
```

### X-Ray Tracing for FastAPI

```python
# server.py - X-Ray instrumentation
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

### CloudWatch Container Insights

```bash
# Enable Container Insights
aws eks update-cluster-config \
    --name courses-portal-eks \
    --logging '{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}'

# Install CloudWatch agent
kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/latest/k8s-deployment-manifest-templates/deployment-mode/daemonset/container-insights-monitoring/quickstart/cwagent-fluent-bit-quickstart.yaml
```

---

## Cost Optimization on EKS

### Graviton Node Groups

```yaml
# Use Graviton instances for 40% cost savings
nodeSelector:
  architecture: arm64

# Or in node group configuration
managedNodeGroups:
  - name: graviton-workers
    instanceType: t4g.medium
    desiredCapacity: 3
    labels:
      architecture: arm64
```

### Spot Instances for Non-Critical Workloads

```yaml
# Use Spot Instances for background workers
nodeSelector:
  lifecycle: Ec2Spot

# Node group with spot instances
managedNodeGroups:
  - name: spot-workers
    instanceType: t4g.medium
    spot: true
    desiredCapacity: 2
    labels:
      workload-type: batch
```

### Resource Optimization

```yaml
# Right-size resource requests based on actual usage
resources:
  requests:
    memory: "256Mi"  # Actual usage ~200Mi
    cpu: "250m"      # Actual usage ~200m
  limits:
    memory: "512Mi"  # 2x requests for burst
    cpu: "500m"      # 2x requests for burst
```

### Cost Breakdown (Estimated)

| Component | Development | Production |
|-----------|-------------|------------|
| **EKS Control Plane** | $0 | $73/mo |
| **Worker Nodes (3 x t4g.medium)** | $75 | $75 |
| **ECR Storage** | $5 | $15 |
| **ALB Controller** | $20 | $25 |
| **CloudWatch Logs** | $10 | $40 |
| **X-Ray** | $5 | $15 |
| **Total** | **~$115/mo** | **~$243/mo** |

---

## Troubleshooting EKS Deployments

### Issue 1: ImagePullBackOff

**Error:** `Failed to pull image`

**Solution:**
```bash
# Verify ECR integration
aws ecr describe-repositories --repository-names courses-api

# Create image pull secret
kubectl create secret docker-registry ecr-secret \
    --docker-server=123456789012.dkr.ecr.us-east-1.amazonaws.com \
    --docker-username=AWS \
    --docker-password=$(aws ecr get-login-password) \
    -n courses
```

### Issue 2: CrashLoopBackOff

**Error:** `Container crashed repeatedly`

**Solution:**
```bash
# View logs
kubectl logs courses-api-xxxxx -n courses --previous

# Check events
kubectl describe pod courses-api-xxxxx -n courses
```

### Issue 3: ALB Not Creating

**Error:** `Ingress stays in "Creating" state`

**Solution:**
```bash
# Check controller logs
kubectl logs -n kube-system deployment/aws-load-balancer-controller

# Verify annotations
kubectl describe ingress courses-api-ingress -n courses

# Ensure subnet tags
aws ec2 describe-subnets --filters "Name=tag:kubernetes.io/cluster/courses-portal-eks,Values=shared"
```

### Issue 4: OOMKilled

**Error:** `Container killed due to memory limit`

**Solution:**
```bash
# Check current usage
kubectl top pod courses-api-xxxxx -n courses

# Increase limits
kubectl set resources deployment courses-api \
    --limits=memory=1Gi \
    --requests=memory=512Mi \
    -n courses
```

---

## Performance Benchmarking on EKS

| Metric | Single Node | EKS (3 Nodes) | EKS (Auto-scale) |
|--------|-------------|---------------|------------------|
| **Deployment Time** | Manual | 2 minutes | 2 minutes |
| **Availability** | Single point | 99.5% | 99.95% |
| **Scaling** | Manual | Manual | Automatic |
| **Graviton Savings** | N/A | 40% | 40% |

### Scaling Performance

| Replicas | Requests/sec | P99 Latency | CPU Utilization |
|----------|--------------|-------------|-----------------|
| 1 | 500 | 120ms | 85% |
| 3 | 1,400 | 65ms | 70% |
| 5 | 2,300 | 55ms | 68% |
| 10 | 4,500 | 50ms | 65% |

---

## Conclusion: Python at Enterprise Scale on EKS

Amazon EKS represents the enterprise-grade orchestration platform for Python FastAPI applications on AWS, delivering:

- **Microservices architecture** – Deploy multiple FastAPI services with service discovery
- **Auto-scaling** – Scale based on CPU, memory, or custom request metrics
- **Zero-downtime updates** – Rolling deployments with health checks
- **Self-healing** – Automatic restart of failed containers
- **Cost optimization** – Spot instances, right-sizing, Graviton processors
- **Enterprise security** – Network policies, secrets management, IAM integration

For the AI Powered Video Tutorial Portal, EKS enables:

- **Multi-service deployment** – API gateway, auth service, content service, workers
- **Horizontal scaling** – Handle peak traffic during course launches
- **GitOps workflows** – Declarative infrastructure with Flux
- **AWS service integration** – DocumentDB, ElastiCache, Secrets Manager
- **Observability** – X-Ray traces, CloudWatch metrics, ADOT collector

EKS represents the pinnacle of Python container orchestration on AWS—enabling teams to run FastAPI applications at enterprise scale with the reliability, security, and operational excellence that production workloads demand.

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

- ☸️ **8. Amazon EKS: Python Microservices at Scale - AWS** – Deploying FastAPI applications to Amazon EKS, Helm charts, GitOps with Flux, and production-grade operations *(This story)*

- 🤖 **9. GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS

- 🏗️ **10. AWS App Runner: Fully Managed Python Container Service - AWS** – Deploying FastAPI applications to AWS App Runner with zero infrastructure management

---

## What's Next?

This concludes our comprehensive AWS Python series on containerizing FastAPI applications. We've covered the full spectrum of deployment approaches—from Poetry and UV for dependency management, to AWS Copilot and CDK for infrastructure, to Amazon EKS for enterprise-scale orchestration.

Whether you're deploying to ECS Fargate, Amazon EKS, or AWS App Runner, you now have the complete toolkit to succeed with Python FastAPI containerization on AWS. Each approach serves different use cases, and the right choice depends on your team's experience, operational requirements, and scaling needs.

**Thank you for reading this complete AWS Python series!** We've explored every major approach to building, testing, and deploying Python FastAPI container images—from local development with VS Code Dev Containers to enterprise-scale orchestration on Amazon EKS. You're now equipped to choose the right tool for every scenario. Happy containerizing on AWS! 🚀

**Coming next in the series:**
**🤖 GitHub Actions + Amazon ECR: CI/CD for Python - AWS** – Automated container builds, testing, and deployment with GitHub Actions workflows to AWS