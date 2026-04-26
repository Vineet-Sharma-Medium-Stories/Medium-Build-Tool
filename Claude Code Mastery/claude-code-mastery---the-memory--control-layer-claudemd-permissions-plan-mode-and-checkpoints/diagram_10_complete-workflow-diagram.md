# ### Complete Workflow Diagram

```mermaid
graph TB
    subgraph "1. Project Setup"
        A[Create CLAUDE.md] --> B[Configure Permissions]
        B --> C[Start Claude Session]
    end
    
    subgraph "2. Feature Development"
        C --> D[Enable Plan Mode]
        D --> E[Request Feature]
        E --> F[Review Plan]
        F --> G{Approved?}
        G -->|Yes| H[Execute]
        G -->|No| I[Edit Plan]
        I --> F
    end
    
    subgraph "3. Safe Execution"
        H --> J[Auto Checkpoint]
        J --> K[Implement Files]
        K --> L[Run Tests]
        L --> M{Tests Pass?}
        M -->|Yes| N[Success Checkpoint]
        M -->|No| O[Failure Checkpoint]
        O --> P{Fix or Revert?}
        P -->|Fix| Q[Apply Fixes]
        Q --> L
        P -->|Revert| R[/checkpoints restore]
        R --> K
    end
    
    subgraph "4. Completion"
        N --> S[Final Review]
        S --> T[Commit to Git]
        T --> U[Feature Complete]
    end
    
    style A fill:#e1f5fe
    style D fill:#e1f5fe
    style J fill:#e1f5fe
    style N fill:#c8e6c9
    style U fill:#c8e6c9
```
