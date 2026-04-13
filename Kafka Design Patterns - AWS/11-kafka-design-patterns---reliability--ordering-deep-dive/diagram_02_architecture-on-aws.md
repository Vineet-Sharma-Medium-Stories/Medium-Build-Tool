# ### Architecture on AWS

```mermaid
---
config:
  layout: elk
  theme: base
---
graph LR
    subgraph "Kafka Consumer"
        M[Message<br/>key=order_123<br/>offset=42<br/>partition=0]
    end
    
    subgraph "Idempotency Store"
        D[(DynamoDB Table<br/>pk: order_123:0:42<br/>ttl: 7 days)]
    end
    
    subgraph "Business Logic"
        B[Process order]
        C[Charge credit card]
        E[Send confirmation]
    end
    
    subgraph "AWS Services"
        CW[CloudWatch Metrics]
        SN[SNS Alert]
    end
    
    M -->|1. Extract key| D
    D -->|2. Conditional PUT| D
    D -->|3a. Success (first time)| B
    D -->|3b. Failure (duplicate)| Skip[Skip processing]
    
    B -->|4. Execute| C
    C -->|5. Commit offset| M
    C -->|6. Emit metrics| CW
    
    Skip -->|6. Emit duplicate metric| CW
    CW -->|7. Alert if high duplicate rate| SN
    
    style D fill:#ffd,stroke:#333,stroke-width:2px
```
