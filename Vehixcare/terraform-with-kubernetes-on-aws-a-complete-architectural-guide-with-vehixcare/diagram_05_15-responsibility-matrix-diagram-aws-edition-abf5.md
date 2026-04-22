# ### 1.5 Responsibility Matrix Diagram (AWS Edition

```mermaid
---
config:
  theme: base
  layout: elk
---
graph TD
    subgraph "Provisioning Responsibility"
        direction TB
        T[Terraform] --> |Creates| AWSR[AWS Resources]
        T --> |Manages| STATE[Terraform State<br/>S3 Backend + DynamoDB Lock]
        T --> |Destroys| AWSR
        
        K[Kubernetes] --> |Schedules| PODS[Pods]
        K --> |Scales| HPA[Horizontal Pod Autoscaler<br/>3-20 replicas]
        K --> |Routes| SVC[Services/Ingress<br/>ClusterIP/NLB]
        K --> |Heals| RESTART[Restart Policy<br/>Liveness/Readiness Probes]
        K --> |Configures| CM[ConfigMaps/Secrets<br/>CSI Driver Integration]
    end
    
    subgraph "Boundary Lines"
        LINE1[❌ Terraform never manages Pods or Deployments]
        LINE2[❌ Kubernetes never provisions EC2 or DocumentDB]
        LINE3[✅ Terraform creates EKS cluster + node groups]
        LINE4[✅ Kubernetes runs workloads inside EKS]
        LINE5[✅ Terraform outputs become Kubernetes secrets]
    end
    
    AWSR --> EKS[EKS Cluster]
    EKS --> K
    
    style LINE1 fill:#ffcccc
    style LINE2 fill:#ffcccc
    style LINE3 fill:#ccffcc
    style LINE4 fill:#ccffcc
    style LINE5 fill:#ccffff
```
