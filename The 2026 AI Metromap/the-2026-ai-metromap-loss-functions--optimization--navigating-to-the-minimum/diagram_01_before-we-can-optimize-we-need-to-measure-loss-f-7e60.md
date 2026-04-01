# Before we can optimize, we need to measure. Loss f

```mermaid
---
config:
  theme: base
  layout: elk
---
graph TD
    subgraph "**Loss Functions**"
        Y[True Value y] --> L[Loss = f(y, ŷ)]
        YH[Prediction ŷ] --> L
        L --> O[Optimizer minimizes this]
    end
    
    subgraph "**Regression Losses**"
        MSE[Mean Squared Error<br/>(y - ŷ)²]
        MAE[Mean Absolute Error<br/>|y - ŷ|]
        H[Huber<br/>Combines MSE + MAE]
    end
    
    subgraph "**Classification Losses**"
        BCE[Binary Cross-Entropy<br/>-y·log(ŷ) - (1-y)·log(1-ŷ)]
        CE[Categorical Cross-Entropy<br/>-Σyᵢ·log(ŷᵢ)]
        HL[Hinge Loss<br/>max(0, 1 - y·ŷ)]
    end
    
    style MSE fill:#90be6d,stroke:#333,stroke-width:2px
    style BCE fill:#4d908e,stroke:#333,stroke-width:2px
```
