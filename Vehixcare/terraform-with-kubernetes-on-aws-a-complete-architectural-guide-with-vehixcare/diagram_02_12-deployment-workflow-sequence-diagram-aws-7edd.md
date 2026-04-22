# ### 1.2 Deployment Workflow Sequence Diagram (AWS)

```mermaid
---
config:
  theme: base
  layout: elk
---
sequenceDiagram
    participant Dev as Developer
    participant GH as GitHub Actions
    participant TF as Terraform Cloud
    participant AWS as AWS Cloud Control API
    participant ECR as Amazon ECR
    participant EKS as EKS Cluster
    participant K8s as Kubernetes API
    
    Dev->>GH: Push code change
    GH->>GH: Run tests
    
    alt Infrastructure Change
        GH->>TF: terraform plan
        TF->>AWS: Read current state
        AWS-->>TF: Return resources
        TF-->>GH: Plan output
        Dev->>GH: Approve apply
        GH->>TF: terraform apply
        TF->>AWS: Create/Update resources
        AWS-->>TF: Resource IDs
        TF-->>GH: Apply complete
    end
    
    alt Application Deployment
        GH->>GH: Build container image
        GH->>ECR: docker push
        ECR-->>GH: Image digest
        GH->>K8s: kubectl set image
        K8s->>EKS: Rolling update
        EKS->>K8s: New pods ready
        K8s->>EKS: Terminate old pods
        EKS-->>GH: Deployment complete
    end
    
    alt Secret Rotation
        GH->>AWS: Update Secrets Manager secret
        AWS->>SM: Store new version
        GH->>K8s: Restart pods
        K8s->>EKS: CSI driver refreshes secrets
    end
```
