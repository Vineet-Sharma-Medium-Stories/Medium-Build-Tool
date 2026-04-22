# ### 1.4 Network Topology Diagram (AWS VPC)

```mermaid
---
config:
  theme: base
  layout: elk
---
graph LR
    subgraph "AWS VPC: 10.0.0.0/16"
        SUBNET1["private-eks-a<br/>10.0.0.0/19<br/>EKS Worker Nodes (AZ a)<br/>Max 8,192 IPs<br/>NACL: nacl-eks"]
        SUBNET2["private-eks-b<br/>10.0.32.0/19<br/>EKS Worker Nodes (AZ b)<br/>Max 8,192 IPs"]
        SUBNET3["private-eks-c<br/>10.0.64.0/19<br/>EKS Worker Nodes (AZ c)<br/>Max 8,192 IPs"]
        SUBNET4["private-nlb<br/>10.0.160.0/20<br/>Network Load Balancer<br/>Max 4,096 IPs"]
        SUBNET5["private-vpce<br/>10.0.176.0/20<br/>VPC Endpoints<br/>Max 4,096 IPs"]
        SUBNET6["public-eks-a<br/>10.0.96.0/19<br/>NAT Gateway / Bastion (AZ a)<br/>Max 8,192 IPs"]
        SUBNET7["public-eks-b<br/>10.0.128.0/19<br/>NAT Gateway / Bastion (AZ b)"]
    end
    
    subgraph "AWS Resources"
        EKS[EKS Cluster<br/>System Pool: 3-5 t3.large<br/>User Pool: 5-20 m5.2xlarge]
        NLB[Network Load Balancer<br/>Cross-zone enabled]
        VPCE1[VPC Endpoint - DocumentDB]
        VPCE2[VPC Endpoint - Secrets Manager]
        VPCE3[VPC Endpoint - ECR]
        BASTION[Bastion Host (Session Manager)]
    end
    
    subgraph "Managed Services"
        DOCDB[DocumentDB<br/>VPC Endpoint Only]
        SM[Secrets Manager<br/>VPC Endpoint Only]
        ECR[ECR<br/>VPC Endpoint + Interface]
    end
    
    SUBNET1 --> EKS
    SUBNET2 --> EKS
    SUBNET3 --> EKS
    SUBNET4 --> NLB
    SUBNET5 --> VPCE1
    SUBNET5 --> VPCE2
    SUBNET5 --> VPCE3
    
    VPCE1 --> DOCDB
    VPCE2 --> SM
    VPCE3 --> ECR
    EKS --> ECR
```
