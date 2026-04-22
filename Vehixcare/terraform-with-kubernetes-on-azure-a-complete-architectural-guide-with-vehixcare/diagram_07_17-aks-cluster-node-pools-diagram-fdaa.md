# ### 1.7 AKS Cluster Node Pools Diagram

```mermaid
---
config:
  theme: base
  layout: elk
---
graph TB
    subgraph "AKS Cluster: aks-vehixcare-prod"
        subgraph "System Node Pool (systempool)"
            S1["Node 1<br/>D4s_v3<br/>Zone 1"]
            S2["Node 2<br/>D4s_v3<br/>Zone 2"]
            S3["Node 3<br/>D4s_v3<br/>Zone 3"]
            S4["Node 4 (scaled)<br/>D4s_v3<br/>Zone 1"]
            
            subgraph "System Pods (Tainted: CriticalAddonsOnly=true:NoSchedule)"
                COREDNS["CoreDNS<br/>DNS resolution"]
                METRICS["Metrics Server<br/>Resource metrics"]
                TUNNEL["AKS Tunnel<br/>Control plane comms"]
                CSI["CSI Drivers<br/>Secrets Store + Azure Disk"]
                CALICO["Calico CNI<br/>Network policy"]
            end
        end
        
        subgraph "User Node Pool (userpool)"
            U1["Node 1<br/>D8s_v3<br/>Zone 1"]
            U2["Node 2<br/>D8s_v3<br/>Zone 2"]
            U3["Node 3<br/>D8s_v3<br/>Zone 3"]
            U4["Node 4<br/>D8s_v3<br/>Zone 1"]
            U5["Node 5<br/>D8s_v3<br/>Zone 2"]
            U6["Node 6 (scaled)<br/>D8s_v3<br/>Zone 3"]
            
            subgraph "User Pods (No Taints)"
                BOOKING["Telemetry API Pods<br/>3-20 replicas<br/>CPU: 1-3 cores"]
                BEHAVIOR["Behavior Processor Pods<br/>2-15 replicas<br/>Memory: 4-8 Gi"]
                GEOFENCE["Geo-fence Monitor Pods<br/>2-10 replicas"]
                SIGNALR["SignalR Hub Pods<br/>2-5 replicas<br/>Session affinity"]
            end
        end
    end
    
    subgraph "Azure CNI Networking"
        VNET["vnet-vehixcare<br/>10.0.0.0/8"]
        POD_CIDR["Pod CIDR: 10.244.0.0/16<br/>65,536 IPs"]
        SVC_CIDR["Service CIDR: 10.245.0.0/16<br/>65,536 IPs"]
    end
    
    subgraph "Node Labels & Taints"
        SYS_LABEL["nodepool-type: system<br/>environment: production<br/>critical: true"]
        USER_LABEL["nodepool-type: user<br/>environment: production<br/>workload: telemetry"]
    end
    
    S1 --> VNET
    S2 --> VNET
    U1 --> VNET
    U2 --> VNET
    
    BOOKING --> POD_CIDR
    SIGNALR --> SVC_CIDR
```
