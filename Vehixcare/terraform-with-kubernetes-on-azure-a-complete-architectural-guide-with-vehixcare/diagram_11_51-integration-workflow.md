# ### 5.1 Integration Workflow

```mermaid
---
config:
  theme: base
  layout: elk
---
flowchart TD
    subgraph "CI/CD Pipeline (GitHub Actions)"
        TF_APPLY[terraform apply]
        TF_OUTPUT[terraform output -json]
        K8S_SECRET[kubectl create secret]
        K8S_APPLY[kubectl apply]
        ROLLOUT[kubectl rollout status]
    end
    
    subgraph "Terraform State Outputs"
        COSMOS_STR[cosmosdb_mongo_connection_string<br/>sensitive]
        ACR_SERVER[acr_login_server]
        KUBECONFIG[kubeconfig<br/>sensitive]
        KV_URI[key_vault_uri]
    end
    
    subgraph "Kubernetes Resources"
        K8S_SECRETS[Secrets: mongo-secret<br/>jwt-secret]
        K8S_SPC[SecretProviderClass]
        DEPLOYMENTS[Deployments with CSI mounts]
        HPA[HorizontalPodAutoscaler]
        SERVICE[LoadBalancer Services]
    end
    
    subgraph "AKS Cluster"
        CSI_DRIVER[Secrets Store CSI Driver]
        PODS[Pods with mounted secrets]
        SIGNALR[SignalR Hub Pods]
        PROCESSOR[Rx.NET Processor Pods]
    end
    
    TF_APPLY --> TF_OUTPUT
    TF_OUTPUT --> COSMOS_STR
    TF_OUTPUT --> ACR_SERVER
    TF_OUTPUT --> KUBECONFIG
    
    COSMOS_STR --> |base64 encoded| K8S_SECRETS
    KV_URI --> |referenced in| K8S_SPC
    K8S_SPC --> CSI_DRIVER
    CSI_DRIVER --> PODS
    
    K8S_SECRETS --> K8S_APPLY
    KUBECONFIG --> K8S_APPLY
    K8S_APPLY --> DEPLOYMENTS
    DEPLOYMENTS --> PODS
    DEPLOYMENTS --> HPA
    DEPLOYMENTS --> SERVICE
    
    SERVICE --> SIGNALR
    DEPLOYMENTS --> PROCESSOR
    
    ACR_SERVER --> |Image pull| PODS
```
