# ### 1.6 CI/CD Pipeline Flow Diagram

```mermaid
---
config:
  theme: base
  layout: elk
---
flowchart TD
    subgraph "CI/CD Pipeline (GitHub Actions)"
        TF_APPLY["terraform apply"]
        TF_OUTPUT["terraform output"]
        K8S_SECRET["kubectl create secret"]
        K8S_APPLY["kubectl apply"]
        ROLLOUT["kubectl rollout status"]
        SMOKE["Smoke Tests"]
    end
    
    subgraph "Terraform Outputs"
        COSMOS_STR["cosmosdb_mongo_connection_string<br/>sensitive: true"]
        ACR_SERVER["acr_login_server"]
        KUBECONFIG["kubeconfig<br/>sensitive: true"]
        KV_URI["key_vault_uri"]
    end
    
    subgraph "Kubernetes Resources"
        K8S_SECRETS["Secrets: mongo-secret<br/>jwt-secret<br/>google-secret"]
        K8S_SPC["SecretProviderClass<br/>Azure Key Vault"]
        DEPLOYMENTS["Deployments with CSI mounts<br/>Telemetry API | SignalR | Processors"]
        HPA["HorizontalPodAutoscaler<br/>3-20 replicas"]
        SERVICE["LoadBalancer Services<br/>SignalR with session affinity"]
    end
    
    subgraph "AKS Cluster"
        CSI_DRIVER["Secrets Store CSI Driver<br/>pollInterval: 5m"]
        PODS["Pods with mounted secrets<br/>Non-root security context"]
        SIGNALR["SignalR Hub Pods<br/>WebSocket connections"]
        PROCESSOR["Rx.NET Processor Pods<br/>Memory: 4-8 Gi"]
    end
    
    subgraph "Verification"
        HEALTH["Health Checks<br/>/health/live, /health/ready"]
        METRICS["Prometheus Metrics<br/>/metrics endpoint"]
        LOGS["Azure Log Analytics<br/>Container insights"]
    end
    
    TF_APPLY --> TF_OUTPUT
    TF_OUTPUT --> COSMOS_STR
    TF_OUTPUT --> ACR_SERVER
    TF_OUTPUT --> KUBECONFIG
    
    COSMOS_STR -->|base64 encoded| K8S_SECRETS
    KV_URI -->|referenced in| K8S_SPC
    K8S_SPC --> CSI_DRIVER
    CSI_DRIVER -->|mounts secrets| PODS
    
    K8S_SECRETS --> K8S_APPLY
    KUBECONFIG --> K8S_APPLY
    K8S_APPLY --> DEPLOYMENTS
    DEPLOYMENTS --> PODS
    DEPLOYMENTS --> HPA
    DEPLOYMENTS --> SERVICE
    
    SERVICE --> SIGNALR
    DEPLOYMENTS --> PROCESSOR
    
    ACR_SERVER -->|Image pull| PODS
    
    K8S_APPLY --> ROLLOUT
    ROLLOUT --> SMOKE
    SMOKE --> HEALTH
    SMOKE --> METRICS
    SMOKE --> LOGS
```
