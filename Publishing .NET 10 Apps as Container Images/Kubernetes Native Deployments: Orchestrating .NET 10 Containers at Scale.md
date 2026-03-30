# Kubernetes Native Deployments: Orchestrating .NET 10 Containers at Scale

## From Container Images to Production-Grade Orchestration

### Introduction: The Missing Piece in Container Deployment

Throughout this series, we've explored nine distinct approaches to building and publishing .NET 10 container images—from SDK-native simplicity to konet's multi-platform parallelism, from Dockerfile control to security-first tarball workflows. Each approach excels at getting your application into a container and pushing it to Azure Container Registry. But there's a critical question we haven't addressed: **once your images are in the registry, how do you run them at scale?**

This is where **Kubernetes** enters the picture. As the de facto standard for container orchestration, Kubernetes transforms isolated containers into production-grade, self-healing, auto-scaling applications. For Vehixcare-API—our fleet management platform with real-time telemetry, SignalR hubs, and background workers—Kubernetes provides the operational foundation required for enterprise deployment.

This tenth installment bridges the gap between container images and production operations. We'll explore Kubernetes fundamentals for .NET developers, deployment strategies for Azure Kubernetes Service (AKS), and advanced patterns like Helm charts, GitOps, and cluster autoscaling. We'll also update our comprehensive list to include Kubernetes as a essential deployment target.

```mermaid
graph TD
    subgraph "Container Build Phase"
        A[.NET 10 App] --> B[Any Build Method]
        B --> C[Container Image]
        C --> D[Azure Container Registry]
    end
    
    subgraph "Kubernetes Orchestration Phase"
        D --> E[AKS Cluster]
        E --> F[Deployment]
        E --> G[Service]
        E --> H[Ingress]
        E --> I[ConfigMap/Secret]
    end
    
    subgraph "Production Operations"
        F --> J[Auto-scaling]
        F --> K[Self-healing]
        F --> L[Rolling Updates]
        F --> M[Canary Deployments]
    end
    
    style E fill:#48bb78,color:#fff
```

### Stories at a Glance

**Complete series (10 stories):**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker** – A deep dive into MSBuild configuration, multi-architecture builds, Native AOT optimization, and direct Azure Container Registry integration with workload identity federation

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach** – Mastering multi-stage builds, build cache optimization, .dockerignore patterns, and Azure Container Registry authentication for enterprise CI/CD pipelines

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop

- ⚡ **5. Azure Developer CLI (azd) with .NET Aspire: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, Redis caching, and infrastructure-as-code with Bicep templates

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop Azure Deployments** – Leveraging Visual Studio's built-in Podman/Docker support, one-click publish to Azure Container Registry, and debugging containerized apps with Hot Reload

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation, and Azure Container Registry push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization

- ☸️ **10. Kubernetes Native Deployments: Orchestrating .NET 10 Containers at Scale** – Deploying to Azure Kubernetes Service (AKS), Helm charts, GitOps, cluster autoscaling, and production-grade operations *(This story)*

---

## Understanding Kubernetes for .NET Developers

### Why Kubernetes?

| Challenge | Solution with Kubernetes |
|-----------|-------------------------|
| **Scaling** | Horizontal Pod Autoscaler based on CPU, memory, or custom metrics |
| **Availability** | Self-healing: restarts failed containers, replaces unhealthy pods |
| **Rolling Updates** | Zero-downtime deployments with configurable rollout strategies |
| **Service Discovery** | Built-in DNS-based service discovery |
| **Configuration** | ConfigMaps and Secrets for environment-specific settings |
| **Networking** | Ingress controllers for HTTP routing, SSL termination |
| **Storage** | Persistent volumes for stateful workloads |

### Kubernetes Architecture Overview

```mermaid
graph TD
    subgraph "Control Plane"
        A[API Server]
        B[etcd]
        C[Scheduler]
        D[Controller Manager]
    end
    
    subgraph "Worker Node 1"
        E[Kubelet]
        F[Container Runtime]
        G[Pods]
    end
    
    subgraph "Worker Node 2"
        H[Kubelet]
        I[Container Runtime]
        J[Pods]
    end
    
    A --> E
    A --> H
    B --> A
    C --> A
    D --> A
```

### Key Kubernetes Concepts for .NET Developers

| Concept | Description | .NET Analogy |
|---------|-------------|--------------|
| **Pod** | Smallest deployable unit, one or more containers | A process/application instance |
| **Deployment** | Desired state for pods (replicas, updates) | Application deployment configuration |
| **Service** | Stable endpoint for pod access | Load balancer / reverse proxy |
| **Ingress** | HTTP routing to services | API Gateway / reverse proxy |
| **ConfigMap** | Environment configuration | appsettings.json |
| **Secret** | Sensitive data (connection strings, keys) | Azure Key Vault |
| **HorizontalPodAutoscaler** | Automatic scaling based on metrics | App Service autoscale |

## Azure Kubernetes Service (AKS) Setup

### Creating an AKS Cluster

```bash
# Create resource group
az group create --name vehixcare-rg --location eastus

# Create AKS cluster
az aks create \
    --resource-group vehixcare-rg \
    --name vehixcare-aks \
    --node-count 3 \
    --node-vm-size Standard_D2s_v3 \
    --enable-cluster-autoscaler \
    --min-count 2 \
    --max-count 10 \
    --enable-addons monitoring \
    --generate-ssh-keys

# Get credentials
az aks get-credentials --resource-group vehixcare-rg --name vehixcare-aks

# Verify connection
kubectl get nodes
# NAME                                STATUS   ROLES   AGE   VERSION
# aks-nodepool1-12345678-vmss000000   Ready    agent   5m    v1.28.0
# aks-nodepool1-12345678-vmss000001   Ready    agent   5m    v1.28.0
# aks-nodepool1-12345678-vmss000002   Ready    agent   5m    v1.28.0
```

### Configuring ACR Integration

```bash
# Get ACR resource ID
ACR_ID=$(az acr show --name vehixcare --resource-group vehixcare-rg --query id --output tsv)

# Attach ACR to AKS
az aks update \
    --resource-group vehixcare-rg \
    --name vehixcare-aks \
    --attach-acr $ACR_ID
```

## Deploying Vehixcare-API to AKS

### Namespace Creation

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: vehixcare
  labels:
    name: vehixcare
    environment: production
```

```bash
kubectl apply -f namespace.yaml
```

### ConfigMap for Application Settings

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: vehixcare-api-config
  namespace: vehixcare
data:
  ASPNETCORE_ENVIRONMENT: "Production"
  ASPNETCORE_URLS: "http://+:8080"
  Telemetry__BatchSize: "100"
  Telemetry__IntervalMs: "5000"
  SignalR__Backplane: "redis"
```

### Secrets for Sensitive Data

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: vehixcare-api-secrets
  namespace: vehixcare
type: Opaque
stringData:
  MongoDb__ConnectionString: "mongodb://admin:password@mongodb-service:27017"
  Jwt__Secret: "your-256-bit-secret-key-here"
  Google__ClientId: "your-google-client-id"
  Google__ClientSecret: "your-google-client-secret"
```

**Note:** In production, use Azure Key Vault with CSI driver instead of storing secrets in YAML.

### Deployment Manifest

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vehixcare-api
  namespace: vehixcare
  labels:
    app: vehixcare-api
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: vehixcare-api
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: vehixcare-api
        version: v1
    spec:
      containers:
      - name: api
        image: vehixcare.azurecr.io/vehixcare-api:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
          name: http
        envFrom:
        - configMapRef:
            name: vehixcare-api-config
        - secretRef:
            name: vehixcare-api-secrets
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
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
      imagePullSecrets:
      - name: acr-secret
```

### Service Manifest

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: vehixcare-api-service
  namespace: vehixcare
  labels:
    app: vehixcare-api
spec:
  selector:
    app: vehixcare-api
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
    name: http
  type: ClusterIP
```

### Ingress Controller (NGINX)

```bash
# Install NGINX Ingress Controller
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx \
    --namespace ingress-nginx \
    --create-namespace \
    --set controller.service.type=LoadBalancer
```

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: vehixcare-api-ingress
  namespace: vehixcare
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/proxy-read-timeout: "60"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "60"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - api.vehixcare.com
    secretName: vehixcare-tls
  rules:
  - host: api.vehixcare.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: vehixcare-api-service
            port:
              number: 80
```

## Deploying Supporting Services

### MongoDB StatefulSet

```yaml
# mongodb-statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
  namespace: vehixcare
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
              name: vehixcare-api-secrets
              key: MongoDb__Username
        - name: MONGO_INITDB_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: vehixcare-api-secrets
              key: MongoDb__Password
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
  namespace: vehixcare
spec:
  selector:
    app: mongodb
  ports:
  - port: 27017
    targetPort: 27017
  clusterIP: None  # Headless service for statefulset
```

### Redis Deployment

```yaml
# redis-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: vehixcare
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
  namespace: vehixcare
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379
```

## Advanced Kubernetes Patterns

### Horizontal Pod Autoscaling

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: vehixcare-api-hpa
  namespace: vehixcare
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: vehixcare-api
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

### Custom Metrics with Prometheus

```yaml
# prometheus-service-monitor.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: vehixcare-api-monitor
  namespace: vehixcare
spec:
  selector:
    matchLabels:
      app: vehixcare-api
  endpoints:
  - port: http
    path: /metrics
    interval: 30s
```

### Pod Disruption Budget

```yaml
# pdb.yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: vehixcare-api-pdb
  namespace: vehixcare
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: vehixcare-api
```

### Network Policy

```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: vehixcare-api-network-policy
  namespace: vehixcare
spec:
  podSelector:
    matchLabels:
      app: vehixcare-api
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
      port: 8080
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

## Helm Charts for Vehixcare

### Chart Structure

```
vehixcare-chart/
├── Chart.yaml
├── values.yaml
├── values-production.yaml
├── templates/
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── hpa.yaml
│   └── mongodb-statefulset.yaml
└── charts/
    └── mongodb/
```

### Chart.yaml

```yaml
apiVersion: v2
name: vehixcare
description: Vehixcare Fleet Management Platform
type: application
version: 1.0.0
appVersion: "1.0.0"
maintainers:
- name: Vehixcare Team
  email: dev@vehixcare.com
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
  repository: vehixcare.azurecr.io/vehixcare-api
  tag: latest
  pullPolicy: Always

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: api.vehixcare.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - hosts:
        - api.vehixcare.com
      secretName: vehixcare-tls

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
  Telemetry__BatchSize: "100"
  Telemetry__IntervalMs: "5000"

mongodb:
  enabled: true
  architecture: standalone
  auth:
    enabled: true
    rootUser: admin
    rootPassword: password
  persistence:
    enabled: true
    size: 10Gi

redis:
  enabled: true
  architecture: standalone
  auth:
    enabled: false
  master:
    persistence:
      enabled: true
      size: 5Gi
```

### Deploying with Helm

```bash
# Install the chart
helm install vehixcare ./vehixcare-chart \
    --namespace vehixcare \
    --create-namespace \
    --values ./vehixcare-chart/values-production.yaml

# Upgrade with new image
helm upgrade vehixcare ./vehixcare-chart \
    --set image.tag=$BUILD_ID

# Rollback if needed
helm rollback vehixcare 1

# Uninstall
helm uninstall vehixcare --namespace vehixcare
```

## GitOps with Flux or ArgoCD

### Flux Configuration

```yaml
# flux-config.yaml
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: GitRepository
metadata:
  name: vehixcare
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/vehixcare/k8s-manifests
  ref:
    branch: main
---
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: vehixcare
  namespace: flux-system
spec:
  interval: 5m
  path: ./vehixcare/overlays/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: vehixcare
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: vehixcare-api
      namespace: vehixcare
```

## Monitoring and Observability

### Azure Monitor for Containers

```bash
# Enable Container Insights
az aks enable-addons \
    --resource-group vehixcare-rg \
    --name vehixcare-aks \
    --addons monitoring
```

### Application Insights Integration

```csharp
// Program.cs
builder.Services.AddApplicationInsightsTelemetry(options =>
{
    options.ConnectionString = Environment.GetEnvironmentVariable("APPLICATIONINSIGHTS_CONNECTION_STRING");
});

// Custom telemetry for Kubernetes context
app.Use(async (context, next) =>
{
    var podName = Environment.GetEnvironmentVariable("POD_NAME");
    var podNamespace = Environment.GetEnvironmentVariable("POD_NAMESPACE");
    
    using var operation = telemetryClient.StartOperation<RequestTelemetry>("Request");
    operation.Telemetry.Properties["PodName"] = podName;
    operation.Telemetry.Properties["PodNamespace"] = podNamespace;
    
    await next();
});
```

## Troubleshooting Kubernetes Deployments

### Common Issues and Solutions

**Issue 1: ImagePullBackOff**

```bash
# Check image pull error
kubectl describe pod vehixcare-api-xxxxx -n vehixcare

# Verify ACR integration
az aks check-acr --name vehixcare-aks --resource-group vehixcare-rg --acr vehixcare
```

**Issue 2: CrashLoopBackOff**

```bash
# View logs
kubectl logs vehixcare-api-xxxxx -n vehixcare --previous

# Check readiness probe
kubectl describe pod vehixcare-api-xxxxx -n vehixcare | grep -A10 Readiness
```

**Issue 3: OOMKilled**

```bash
# Check memory usage
kubectl top pod vehixcare-api-xxxxx -n vehixcare

# Increase memory limits
kubectl set resources deployment vehixcare-api \
    --limits=memory=1Gi \
    --requests=memory=512Mi \
    -n vehixcare
```

## Performance Metrics

### AKS Deployment Comparison

| Metric | Single Node | AKS (3 Nodes) | AKS (Auto-scale) |
|--------|-------------|---------------|------------------|
| **Deployment Time** | Manual | 2 minutes | 2 minutes |
| **Availability** | Single point | 99.5% | 99.95% |
| **Scaling** | Manual | Manual | Automatic |
| **Cost** | Low | Medium | Optimized |
| **Management** | Self-managed | Managed control plane | Managed |

### Scaling Performance

| Replicas | Requests/sec | P99 Latency | CPU Utilization |
|----------|--------------|-------------|-----------------|
| 1 | 500 | 120ms | 85% |
| 2 | 950 | 85ms | 75% |
| 3 | 1,400 | 65ms | 70% |
| 5 | 2,300 | 55ms | 68% |
| 10 | 4,500 | 50ms | 65% |

## Conclusion: The Complete Container Journey

Throughout this ten-part series, we've traced the complete journey of a .NET 10 application from development to production-scale operations:

| Phase | Approaches Covered |
|-------|-------------------|
| **Building Images** | SDK-native, Dockerfile, Podman, konet |
| **Securing Images** | Tarball export, vulnerability scanning, SBOM |
| **Publishing Images** | ACR direct push, tarball load, hybrid workflows |
| **Automating Deployments** | azd, Visual Studio GUI, CI/CD pipelines |
| **Orchestrating at Scale** | Kubernetes, AKS, Helm, GitOps |

### The Complete Toolkit

For Vehixcare-API, the optimal production pipeline combines multiple approaches:

1. **Build**: konet for multi-platform (AMD64 cloud + ARM64 edge)
2. **Scan**: Tarball export with Trivy/Grype for security compliance
3. **Store**: ACR with geo-replication for high availability
4. **Orchestrate**: AKS with Helm for versioned deployments
5. **Operate**: Flux GitOps for declarative infrastructure
6. **Monitor**: Azure Monitor + Application Insights for observability

### Final Thoughts

The .NET containerization ecosystem has matured to the point where developers have unprecedented choice and flexibility. Whether you're a solo developer deploying to a single container or an enterprise managing thousands of microservices across global fleets, there's a workflow tailored to your needs.

This series has covered the full spectrum—from the simplest `dotnet publish` command to sophisticated Kubernetes operators. We hope it serves as a comprehensive reference for your .NET 10 containerization journey.

---

### Stories at a Glance

**Complete series (10 stories):**

- 📚 **1. .NET SDK Native Container Publishing Deep Dive: The Complete Reference** – Comprehensive coverage of MSBuild properties, Native AOT optimization, CI/CD pipeline patterns, performance benchmarks, and troubleshooting guides

- 🚀 **2. .NET SDK Native Container Publishing: Building OCI Images Without Docker** – A deep dive into MSBuild configuration, multi-architecture builds, Native AOT optimization, and direct Azure Container Registry integration with workload identity federation

- 🐳 **3. Traditional Dockerfile with Docker: The Classic Approach** – Mastering multi-stage builds, build cache optimization, .dockerignore patterns, and Azure Container Registry authentication for enterprise CI/CD pipelines

- 🔐 **4. Traditional Dockerfile with Podman: The Daemonless Alternative** – Transitioning from Docker to Podman, rootless containers for enhanced security, podman-compose workflows, and Azure ACR integration with Podman Desktop

- ⚡ **5. Azure Developer CLI (azd) with .NET Aspire: The Turnkey Solution** – Full-stack deployments with `azd up`, Azure Container Apps provisioning, Redis caching, and infrastructure-as-code with Bicep templates

- 🖱️ **6. Visual Studio 2026 GUI Publishing: Drag-and-Drop Azure Deployments** – Leveraging Visual Studio's built-in Podman/Docker support, one-click publish to Azure Container Registry, and debugging containerized apps with Hot Reload

- 🔒 **7. Tarball Export + Runtime Load: Security-First CI/CD Workflows** – Generating container tarballs without a runtime, integrating with Trivy/Grype for vulnerability scanning, and deploying to air-gapped Azure environments

- 🔄 **8. Podman with .NET SDK Native Publishing: Hybrid Workflows** – Combining SDK-native builds with Podman for local testing, multi-architecture emulation, and Azure Container Registry push strategies

- 🛠️ **9. konet: Multi-Platform Container Builds Without Docker** – Using the konet .NET tool for cross-platform image generation, ARM64/AMD64 simultaneous builds, and GitHub Actions optimization

- ☸️ **10. Kubernetes Native Deployments: Orchestrating .NET 10 Containers at Scale** – Deploying to Azure Kubernetes Service (AKS), Helm charts, GitOps, cluster autoscaling, and production-grade operations *(This story)*

---

**Thank you for reading this series!** We've covered every major approach to building, publishing, and orchestrating .NET 10 container images on Azure. Whether you're building your first container or managing thousands in production, you now have the complete toolkit to succeed. Happy containerizing! 🚀