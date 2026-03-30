# Azure Kubernetes Service (AKS): Node.js Microservices at Scale

## Orchestrating Express.js Applications with Kubernetes on Azure

### Introduction: The Enterprise Scale Platform for Node.js on Azure

In the [previous installment](#) of this Node.js series, we explored tarball export and security-first workflows—essential for organizations requiring strict compliance and air-gapped deployments. While those approaches prioritize security, enterprises deploying Node.js applications at scale face an additional challenge: **orchestration**. How do you manage dozens of Express.js microservices, handle rolling updates, auto-scale based on demand, and ensure high availability?

Enter **Azure Kubernetes Service (AKS)**—the managed Kubernetes offering from Microsoft that transforms isolated containers into production-grade, self-healing, auto-scaling applications. For the **AI Powered Video Tutorial Portal**—an Express.js application with multiple services (API gateway, course content service, user service, worker processes), Azure Kubernetes Service provides the operational foundation required for enterprise-scale Node.js deployments.

This installment explores the complete workflow for deploying Express.js applications to AKS, from cluster setup to production-grade operations. We'll master Kubernetes concepts for Node.js developers, deployment strategies, Helm charts, GitOps with Flux, cluster autoscaling, and integration with Azure services—all while leveraging the power of Kubernetes for Node.js microservices.

```mermaid
graph TD
    subgraph "Container Build Phase"
        A[Node.js Express App] --> B[Docker Build]
        B --> C[Container Image]
        C --> D[Azure Container Registry]
    end
    
    subgraph "AKS Cluster"
        D --> E[AKS Control Plane]
        E --> F[Worker Nodes]
        F --> G[Pods - Express API]
        F --> H[Pods - Auth Service]
        F --> I[Pods - Worker Service]
    end
    
    subgraph "Production Operations"
        G --> J[Horizontal Pod Autoscaler]
        G --> K[Cluster Autoscaler]
        G --> L[Ingress Controller]
        G --> M[Service Mesh]
    end
    
    style E fill:#48bb78,color:#fff
    style J fill:#2b6cb0,color:#fff
    style L fill:#ff9900,color:#fff
```

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations *(This story)*

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## Understanding Kubernetes for Node.js Developers on Azure

### Why Kubernetes on Azure?

| Challenge | Solution with AKS | Node.js Benefit |
|-----------|-------------------|-----------------|
| **Microservices** | Service discovery and load balancing | Multiple Express.js services communicate seamlessly |
| **Scaling** | Horizontal Pod Autoscaler + Cluster Autoscaler | Auto-scale based on CPU, memory, or custom metrics |
| **Rolling Updates** | Zero-downtime deployments with configurable rollout | No user impact during Express.js version updates |
| **Service Discovery** | Built-in DNS (CoreDNS) | Express.js services find each other by name |
| **Configuration** | ConfigMaps and Secrets + Azure Key Vault | Environment-specific Node.js settings |
| **Networking** | Azure Application Gateway Ingress Controller | HTTP routing, SSL termination |
| **Storage** | Persistent Volumes + Azure Disks/File | Stateful Node.js workloads |
| **Observability** | Prometheus + Grafana + Azure Monitor | Express.js metrics, traces, logs |

### Kubernetes Architecture for Node.js Developers

```mermaid
graph TD
    subgraph "AKS Control Plane (Managed)"
        A[API Server]
        B[etcd]
        C[Scheduler]
        D[Controller Manager]
    end
    
    subgraph "Worker Node 1"
        E[Kubelet]
        F[Container Runtime]
        G[Pod - Express API]
        H[Pod - Express Worker]
    end
    
    subgraph "Worker Node 2"
        I[Kubelet]
        J[Container Runtime]
        K[Pod - Express API]
        L[Pod - MongoDB Sidecar]
    end
    
    A --> E
    A --> I
```

### Key Kubernetes Concepts for Node.js

| Concept | Description | Express.js Analogy |
|---------|-------------|-------------------|
| **Pod** | Smallest deployable unit, one or more containers | A Node.js process instance |
| **Deployment** | Desired state for pods (replicas, updates) | Application deployment configuration |
| **Service** | Stable endpoint for pod access | Load balancer / reverse proxy |
| **Ingress** | HTTP routing to services | Express.js route to service mapping |
| **ConfigMap** | Environment configuration | Node.js .env file |
| **Secret** | Sensitive data (connection strings, keys) | Azure Key Vault reference |
| **HorizontalPodAutoscaler** | Automatic scaling based on metrics | Express.js app scaling based on request load |

---

## AKS Cluster Setup

### Prerequisites

```bash
# Install Azure CLI
brew install azure-cli  # macOS
# or
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash  # Ubuntu

# Install kubectl
az aks install-cli

# Install Helm
brew install helm  # macOS
# or
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install Azure Container Registry extension
az extension add --name containerapp --upgrade
```

### Create AKS Cluster

```bash
# Create resource group
az group create --name rg-courses-aks --location eastus

# Create ACR (if not exists)
az acr create \
    --resource-group rg-courses-aks \
    --name coursetutorials \
    --sku Standard \
    --admin-enabled false

# Create AKS cluster
az aks create \
    --resource-group rg-courses-aks \
    --name courses-aks \
    --node-count 3 \
    --node-vm-size Standard_D2s_v3 \
    --enable-cluster-autoscaler \
    --min-count 2 \
    --max-count 10 \
    --enable-addons monitoring \
    --generate-ssh-keys \
    --attach-acr coursetutorials

# Get credentials
az aks get-credentials \
    --resource-group rg-courses-aks \
    --name courses-aks

# Verify connection
kubectl get nodes
# NAME                                STATUS   ROLES   AGE   VERSION
# aks-nodepool1-12345678-vmss000000   Ready    agent   5m    v1.28.0
# aks-nodepool1-12345678-vmss000001   Ready    agent   5m    v1.28.0
# aks-nodepool1-12345678-vmss000002   Ready    agent   5m    v1.28.0
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
```

```bash
kubectl apply -f namespace.yaml
```

---

## Deploying Express.js to AKS

### ConfigMap for Application Settings

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: courses-api-config
  namespace: courses
data:
  NODE_ENV: "production"
  LOG_LEVEL: "info"
  API_KEY_ENABLED: "true"
  API_KEY_DEFAULT_RATE_LIMIT: "100"
  MONGODB_DB: "courses_portal"
```

### Secrets with Azure Key Vault

```bash
# Create Key Vault
az keyvault create \
    --name courses-kv \
    --resource-group rg-courses-aks \
    --location eastus

# Store secrets
az keyvault secret set \
    --vault-name courses-kv \
    --name mongodb-uri \
    --value "mongodb://username:password@host:10255/db?ssl=true"

az keyvault secret set \
    --vault-name courses-kv \
    --name jwt-secret \
    --value "your-super-secret-jwt-key"

# Install Secrets Store CSI Driver
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver \
    --namespace kube-system

# Install Azure Provider for Secrets Store CSI
kubectl apply -f https://raw.githubusercontent.com/Azure/secrets-store-csi-driver-provider-azure/main/deployment/provider-azure-installer.yaml
```

```yaml
# secret-provider-class.yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: courses-secrets
  namespace: courses
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"
    useVMManagedIdentity: "true"
    userAssignedIdentityID: "your-managed-identity-client-id"
    keyvaultName: "courses-kv"
    objects: |
      array:
        - |
          objectName: mongodb-uri
          objectType: secret
          objectAlias: MONGODB_URI
        - |
          objectName: jwt-secret
          objectType: secret
          objectAlias: JWT_SECRET_KEY
    tenantId: "your-tenant-id"
```

### Express.js Deployment Manifest

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
      containers:
      - name: api
        image: coursetutorials.azurecr.io/courses-api:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 3000
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
        - name: MONGODB_URI
          valueFrom:
            secretKeyRef:
              name: courses-secrets
              key: MONGODB_URI
        - name: JWT_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: courses-secrets
              key: JWT_SECRET_KEY
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
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
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
    targetPort: 3000
    protocol: TCP
    name: http
  type: ClusterIP
```

### Ingress with Azure Application Gateway

```bash
# Install AGIC (Application Gateway Ingress Controller)
az aks enable-addons \
    --resource-group rg-courses-aks \
    --name courses-aks \
    --addons ingress-appgw \
    --appgw-name courses-appgw \
    --appgw-subnet-cidr "10.2.0.0/16"
```

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: courses-api-ingress
  namespace: courses
  annotations:
    kubernetes.io/ingress.class: azure/application-gateway
    appgw.ingress.kubernetes.io/ssl-redirect: "true"
    appgw.ingress.kubernetes.io/backend-path-prefix: "/"
spec:
  tls:
  - hosts:
    - api.coursesportal.com
    secretName: courses-tls
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
```

---

## Deploying Supporting Services

### MongoDB Deployment (StatefulSet)

```yaml
# mongodb-statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
  namespace: courses
spec:
  serviceName: mongodb
  replicas: 1
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
      - name: mongodb
        image: mongo:7.0
        ports:
        - containerPort: 27017
        env:
        - name: MONGO_INITDB_ROOT_USERNAME
          valueFrom:
            secretKeyRef:
              name: mongodb-secret
              key: username
        - name: MONGO_INITDB_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mongodb-secret
              key: password
        volumeMounts:
        - name: mongodb-data
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: mongodb-data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
---
apiVersion: v1
kind: Service
metadata:
  name: mongodb-service
  namespace: courses
spec:
  selector:
    app: mongodb
  ports:
  - port: 27017
    targetPort: 27017
  clusterIP: None
```

### Redis Deployment

```yaml
# redis-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: courses
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7.0-alpine
        ports:
        - containerPort: 6379
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
---
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: courses
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379
```

---

## Advanced Kubernetes Patterns for Node.js

### Horizontal Pod Autoscaling

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
# Enable cluster autoscaler (already enabled during creation)
az aks update \
    --resource-group rg-courses-aks \
    --name courses-aks \
    --enable-cluster-autoscaler \
    --min-count 2 \
    --max-count 10
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
      port: 3000
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: mongodb
    ports:
    - protocol: TCP
      port: 27017
  - to:
    - podSelector:
        matchLabels:
          app: redis
    ports:
    - protocol: TCP
      port: 6379
```

---

## Helm Charts for Express.js on AKS

### Chart Structure

```
courses-chart/
├── Chart.yaml
├── values.yaml
├── values-production.yaml
├── templates/
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret-provider-class.yaml
│   ├── hpa.yaml
│   └── mongodb-statefulset.yaml
└── charts/
    └── mongodb/
```

### Chart.yaml

```yaml
apiVersion: v2
name: courses-api
description: AI Powered Video Tutorial Portal - Express.js on AKS
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
  repository: coursetutorials.azurecr.io/courses-api
  tag: latest
  pullPolicy: Always

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: azure/application-gateway
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
  NODE_ENV: "production"
  LOG_LEVEL: "info"
  API_KEY_ENABLED: "true"

mongodb:
  enabled: false  # Using Azure Cosmos DB
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

# Rollback if needed
helm rollback courses-api 1

# Uninstall
helm uninstall courses-api --namespace courses
```

---

## GitOps with Flux on AKS

### Install Flux

```bash
# Install Flux CLI
curl -s https://fluxcd.io/install.sh | sudo bash

# Bootstrap Flux
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

## Observability with Azure Monitor

### Enable Container Insights

```bash
# Enable Container Insights
az aks enable-addons \
    --resource-group rg-courses-aks \
    --name courses-aks \
    --addons monitoring
```

### OpenTelemetry for Express.js

```javascript
// server.js - OpenTelemetry configuration
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { AzureMonitorTraceExporter } = require('@azure/monitor-opentelemetry-exporter');
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express');
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

// Configure Azure Monitor exporter
const provider = new NodeTracerProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'courses-api',
    [SemanticResourceAttributes.SERVICE_VERSION]: '1.0.0'
  })
});

const exporter = new AzureMonitorTraceExporter({
  connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
});

provider.addSpanProcessor(new BatchSpanProcessor(exporter));
provider.register();

// Register instrumentations
registerInstrumentations({
  instrumentations: [
    new ExpressInstrumentation(),
    new HttpInstrumentation()
  ]
});
```

---

## Cost Optimization on AKS

### Spot Instances for Non-Critical Workloads

```yaml
# Node pool with spot instances
az aks nodepool add \
    --resource-group rg-courses-aks \
    --cluster-name courses-aks \
    --name spotpool \
    --node-count 1 \
    --node-vm-size Standard_D2s_v3 \
    --priority Spot \
    --eviction-policy Delete \
    --spot-max-price -1 \
    --labels workload-type=batch \
    --node-taints "spot=true:NoSchedule"
```

### Right-Size Resource Requests

```yaml
# Monitor actual usage
kubectl top pods -n courses

# Right-size based on actual usage
resources:
  requests:
    memory: "200Mi"  # Actual usage ~180Mi
    cpu: "200m"      # Actual usage ~180m
  limits:
    memory: "400Mi"  # 2x for burst
    cpu: "400m"      # 2x for burst
```

### Cost Breakdown (Estimated)

| Component | Development | Production |
|-----------|-------------|------------|
| **AKS Control Plane** | $0 | $73/mo |
| **Worker Nodes (3 x D2s_v3)** | $150 | $150 |
| **Azure Container Registry** | $5 | $15 |
| **Azure Monitor** | $10 | $50 |
| **Azure Key Vault** | $0 | $5 |
| **Azure Application Gateway** | $25 | $125 |
| **Total** | **~$190/mo** | **~$418/mo** |

---

## Troubleshooting AKS Deployments

### Issue 1: ImagePullBackOff

**Error:** `Failed to pull image`

**Solution:**
```bash
# Verify ACR integration
az aks check-acr \
    --resource-group rg-courses-aks \
    --name courses-aks \
    --acr coursetutorials

# Create image pull secret
kubectl create secret docker-registry acr-secret \
    --docker-server=coursetutorials.azurecr.io \
    --docker-username=$(az acr credential show --name coursetutorials --query username -o tsv) \
    --docker-password=$(az acr credential show --name coursetutorials --query passwords[0].value -o tsv) \
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

### Issue 3: Ingress Not Working

**Error:** `502 Bad Gateway` from Application Gateway

**Solution:**
```bash
# Check service endpoints
kubectl get endpoints -n courses

# Check ingress status
kubectl describe ingress courses-api-ingress -n courses

# Verify AGIC logs
kubectl logs -n kube-system deployment/ingress-appgw-deployment
```

### Issue 4: Node.js Memory Leak

**Error:** `OOMKilled` after running for some time

**Solution:**
```javascript
// Add memory monitoring
const memwatch = require('node-memwatch');
memwatch.on('leak', (info) => {
  console.error('Memory leak detected:', info);
  // Trigger heap dump or restart
});

// Set memory limit in deployment
resources:
  limits:
    memory: "1Gi"
```

---

## Performance Benchmarking on AKS

| Metric | Single Node | AKS (3 Nodes) | AKS (Auto-scale) |
|--------|-------------|---------------|------------------|
| **Deployment Time** | Manual | 2 minutes | 2 minutes |
| **Availability** | Single point | 99.5% | 99.95% |
| **Scaling** | Manual | Manual | Automatic |
| **Cost** | Low | Medium | Optimized |

### Scaling Performance for Node.js

| Replicas | Requests/sec | P99 Latency | CPU Utilization |
|----------|--------------|-------------|-----------------|
| 1 | 800 | 80ms | 85% |
| 3 | 2,200 | 55ms | 70% |
| 5 | 3,500 | 45ms | 68% |
| 10 | 6,500 | 40ms | 65% |

---

## Conclusion: Node.js at Enterprise Scale on AKS

Azure Kubernetes Service represents the enterprise-grade orchestration platform for Node.js Express applications, delivering:

- **Microservices architecture** – Deploy multiple Express.js services with service discovery
- **Auto-scaling** – Scale based on CPU, memory, or custom request metrics
- **Zero-downtime updates** – Rolling deployments with health checks
- **Self-healing** – Automatic restart of failed containers
- **Cost optimization** – Spot instances, right-sizing, cluster autoscaling
- **Enterprise security** – Network policies, secrets management, Azure integration

For the AI Powered Video Tutorial Portal, AKS enables:

- **Multi-service deployment** – API gateway, course service, user service, workers
- **Horizontal scaling** – Handle peak traffic during course launches
- **GitOps workflows** – Declarative infrastructure with Flux
- **Azure service integration** – Cosmos DB, Redis, Key Vault
- **Observability** – Prometheus metrics, OpenTelemetry traces

AKS represents the pinnacle of Node.js container orchestration on Azure—enabling teams to run Express.js applications at enterprise scale with the reliability, security, and operational excellence that production workloads demand.

---

### Stories at a Glance

**Complete Node.js series (10 stories):**

- 📦 **1. NPM + Docker Multi-Stage: The Classic Node.js Approach** – Leveraging npm with optimized multi-stage Docker builds for Express.js applications on Azure Container Registry

- 🧶 **2. Yarn + Docker: Deterministic Dependency Management** – Using Yarn for reproducible builds with Yarn Berry and Plug'n'Play for optimal container performance

- ⚡ **3. pnpm + Docker: Disk-Efficient Node.js Containers** – Leveraging pnpm's content-addressable storage for faster installs and smaller images

- 🚀 **4. Azure Container Apps: Serverless Node.js Deployment** – Deploying Express.js applications to Azure Container Apps with auto-scaling and managed infrastructure

- 💻 **5. Visual Studio Code Dev Containers: Local Development to Production** – Using VS Code Dev Containers for consistent Node.js development environments that mirror Azure production

- 🔧 **6. Azure Developer CLI (azd) with Node.js: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, and infrastructure-as-code with Bicep

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- ☸️ **8. Azure Kubernetes Service (AKS): Node.js Microservices at Scale** – Deploying Express.js applications to AKS, Helm charts, GitOps with Flux, and production-grade operations *(This story)*

- 🤖 **9. GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure

- 🏗️ **10. AWS CDK & Copilot: Multi-Cloud Node.js Container Deployments** – Deploying Node.js Express applications to AWS ECS with AWS Copilot, infrastructure-as-code with CDK, and Fargate serverless orchestration

---

## What's Next?

This concludes our comprehensive Node.js series on containerizing Express.js applications. We've covered the full spectrum of deployment approaches—from npm and Yarn for dependency management, to Azure Container Apps and AKS for serverless and orchestrated deployments.

Whether you're deploying to Azure Container Apps, Azure Kubernetes Service, or multi-cloud with AWS CDK, you now have the complete toolkit to succeed with Node.js containerization on Azure. Each approach serves different use cases, and the right choice depends on your team's experience, operational requirements, and scaling needs.

**Thank you for reading this complete Node.js series!** We've explored every major approach to building, testing, and deploying Node.js Express container images—from local development with VS Code Dev Containers to enterprise-scale orchestration on Azure Kubernetes Service. You're now equipped to choose the right tool for every scenario. Happy containerizing on Azure! 🚀

**Coming next in the series:**
**🤖 GitHub Actions + Container Registry: CI/CD for Node.js** – Automated container builds, testing, and deployment with GitHub Actions workflows to Azure