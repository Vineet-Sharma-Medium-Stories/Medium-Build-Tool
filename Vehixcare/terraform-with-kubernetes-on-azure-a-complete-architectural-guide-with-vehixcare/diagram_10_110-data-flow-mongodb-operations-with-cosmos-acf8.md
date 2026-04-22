# ### 1.10 Data Flow: MongoDB Operations with Cosmos

```mermaid
---
config:
  theme: base
  layout: elk
---
flowchart LR
    subgraph "Vehixcare Microservices"
        TELEMETRY_API["Telemetry API"]
        BEHAVIOR_API["Behavior API"]
        GEOFENCE_API["Geo-fence API"]
        COMMAND_API["Command API"]
    end
    
    subgraph "Connection Layer"
        MC["MongoDB Go Driver"]
        TLS["TLS 1.3"]
        POOL["Connection Pool<br/>maxPoolSize: 200"]
    end
    
    subgraph "Cosmos DB MongoDB"
        subgraph "West Europe (Primary - Priority 0)"
            PE1["Private Endpoint"]
            GW1["Gateway"]
            SVC1["Region 1<br/>Write Primary"]
            DATA1["(Data Partition 1<br/>Shard: vehicle_id<br/>Range 0-3FFF)"]
            DATA2["(Data Partition 2<br/>Shard: vehicle_id<br/>Range 4000-7FFF)"]
            DATA3["(Data Partition 3<br/>Shard: vehicle_id<br/>Range 8000-BFFF)"]
            DATA4["(Data Partition 4<br/>Shard: vehicle_id<br/>Range C000-FFFF)"]
        end
        
        subgraph "North Europe (Replica - Priority 1)"
            PE2["Private Endpoint"]
            GW2["Gateway"]
            SVC2["Region 2<br/>Read Replica<br/>Automatic Failover"]
        end
    end
    
    TELEMETRY_API --> MC --> TLS --> PE1
    BEHAVIOR_API --> MC --> TLS --> PE1
    GEOFENCE_API --> MC --> TLS --> PE1
    COMMAND_API --> MC --> TLS --> PE1
    
    PE1 --> GW1
    GW1 --> POOL
    POOL --> SVC1
    SVC1 --> DATA1
    SVC1 --> DATA2
    SVC1 --> DATA3
    SVC1 --> DATA4
    
    SVC1 -- "Asynchronous Replication (sub-10ms)" --> SVC2
    
    COMMAND_API --> MC --> TLS --> PE2
    PE2 --> GW2 --> SVC2
```
