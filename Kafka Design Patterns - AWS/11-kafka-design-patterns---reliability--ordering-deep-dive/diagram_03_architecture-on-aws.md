# ### Architecture on AWS

```mermaid
---
config:
  layout: elk
  theme: base
---
graph TB
    subgraph "Kafka MSK Cluster"
        Main[main_topic: order_events<br/>Messages: 0-999]
        DLQ[DLQ Topic: order_events.dlq<br/>Poison messages only]
    end
    
    subgraph "Consumer Application"
        C[Consumer Service<br/>process_order()]
        R[Retry Tracker<br/>max_retries=3]
    end
    
    subgraph "Alerting & Monitoring"
        CW[CloudWatch Alarm<br/>DLQ message count > 0]
        SNS[SNS Topic]
        Ops[On-call Engineer]
        Replay[DLQ Replay Tool<br/>Manual or automated]
    end
    
    Main -->|read| C
    C -->|success| Commit[Commit offset]
    C -->|failure| R
    
    R -->|retry count < 3| Retry[Retry later<br/>don't commit]
    R -->|retry count = 3| SendDLQ[Send to DLQ]
    
    SendDLQ --> DLQ
    SendDLQ --> Commit
    
    DLQ -->|CloudWatch metric| CW
    CW --> SNS --> Ops
    
    DLQ -->|inspect & replay| Replay
    Replay -->|republished| Main
    
    style DLQ fill:#f99,stroke:#333,stroke-width:2px
    style Ops fill:#ffcc00,stroke:#333
```
