# ```

```mermaid
flowchart TB
    subgraph "Checkpoint Creation"
        A[Action Trigger] --> B{Checkpoint Type}
        
        B -->|Auto| C[Significant Operation]
        B -->|Manual| D[User Request]
        
        C --> E[Pre-Operation Snapshot]
        D --> E
        
        E --> F[Git Commit with Metadata]
        F --> G[Store in Checkpoint Registry]
    end
    
    subgraph "Checkpoint Management"
        H[/checkpoints list] --> I[Display Timeline]
        J[/checkpoints diff] --> K[Show Changes]
        L[/checkpoints restore] --> M[Git Reset]
        
        M --> N[Update Working Directory]
        N --> O[Session State Restored]
    end
    
    subgraph "Auto-Triggers"
        P[Before Write >3 files] --> E
        Q[Before Migration] --> E
        R[After Test Failure] --> E
        S[Session Start] --> E
        T[Before External API] --> E
    end
    
    style E fill:#e1f5fe
    style M fill:#fff9c4
    style O fill:#c8e6c9
```
