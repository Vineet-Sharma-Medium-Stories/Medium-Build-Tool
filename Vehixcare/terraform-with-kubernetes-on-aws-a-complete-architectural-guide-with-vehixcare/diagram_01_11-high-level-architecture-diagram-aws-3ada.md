# ### 1.1 High-Level Architecture Diagram (AWS)

```mermaid
---
config:
  theme: base
  layout: elk
---
graph TB
    subgraph "Internet / Vehicle IoT"
        VEHICLES[Fleet Vehicles<br/>GPS/Telemetry Devices]
        USERS[Fleet Managers<br/>Web Dashboards]
        MOBILE[Driver Mobile Apps]
    end
    
    subgraph "AWS Global"
        subgraph "us-east-1 Region - Terraform Managed"
            VPC[vpc-vehixcare: 10.0.0.0/16]
            SUBNET_EKS_PRV[private-eks-a: 10.0.0.0/19<br/>private-eks-b: 10.0.32.0/19<br/>private-eks-c: 10.0.64.0/19]
            SUBNET_EKS_PUB[public-eks-a: 10.0.96.0/19<br/>public-eks-b: 10.0.128.0/19]
            SUBNET_NLB[private-nlb: 10.0.160.0/20]
            SUBNET_VPCE[private-vpce: 10.0.176.0/20]
            
            NLB[Network Load Balancer]
            EKS[EKS Cluster<br/>eks-vehixcare-prod]
            ECR[ECR Repository<br/>Cross-region replication]
            SM[Secrets Manager<br/>Encrypted with KMS]
            
            subgraph "Amazon DocumentDB (MongoDB-compatible)"
                DOCDB[DocumentDB Cluster<br/>MongoDB 4.2<br/>Session Consistency]
                DB_TELEMETRY[(vehixcare-telemetry<br/>Shard: vehicle_id<br/>TTL: 30 days)]
                DB_FLEET[(vehixcare-fleet<br/>Shard: organization_id)]
                DB_ANALYTICS[(vehixcare-analytics<br/>Shard: driver_id)]
            end
        end
        
        subgraph "Kubernetes Managed Workloads"
            NS_APP[Namespace: vehixcare-apps]
            
            subgraph "Microservices with HPA"
                TELEMETRY[Telemetry API<br/>HPA: 3-20 replicas<br/>CPU/RU/Telemetry-rate]
                BEHAVIOR[Driver Behavior Service<br/>HPA: 2-15 replicas<br/>Rx.NET pipelines]
                GEOFENCE[Geo-fence Monitor<br/>HPA: 2-10 replicas]
                NOTIFY[Notification Service<br/>KEDA: 1-50 replicas]
                COMMAND[Vehicle Command Service<br/>HPA: 2-8 replicas]
            end
            
            APPSYNC[AppSync API<br/>Real-time streaming]
            INGRESS[AWS Load Balancer Controller<br/>Ingress]
            CSI[Secrets Store CSI<br/>Secrets Manager integration]
        end
        
        subgraph "Eventing Layer - Multi-Provider"
            EVENTBRIDGE[AWS EventBridge]
            EVENTGRID[Azure Event Grid]
            MSK[Amazon MSK - Apache Kafka]
        end
        
        subgraph "us-west-2 Region (Failover)"
            DOCDB_REPLICA[DocumentDB Replica<br/>Read Priority 1]
        end
    end
    
    subgraph "CI/CD Pipeline"
        GH[GitHub Actions]
        TF_APPLY[terraform apply]
        KUBECTL[kubectl apply]
        BUILD[Container Build<br/>.NET 9.0 Docker]
    end
    
    VEHICLES --> NLB
    USERS --> CDN --> NLB
    MOBILE --> NLB
    
    NLB --> INGRESS
    INGRESS --> TELEMETRY
    INGRESS --> COMMAND
    INGRESS --> APPSYNC
    
    TELEMETRY --> DOCDB
    TELEMETRY --> EVENTBRIDGE
    TELEMETRY --> EVENTGRID
    TELEMETRY --> MSK
    
    APPSYNC --> DOCDB
    APPSYNC --> MOBILE
    APPSYNC --> USERS
    
    GEOFENCE --> DOCDB
    BEHAVIOR --> DOCDB
    
    TELEMETRY --> SM
    COMMAND --> SM
    
    DOCDB -.-> DOCDB_REPLICA
    
    GH --> BUILD --> ECR
    ECR --> EKS
    GH --> TF_APPLY --> EKS
    GH --> KUBECTL --> EKS
    
    EKS --> SM
```
