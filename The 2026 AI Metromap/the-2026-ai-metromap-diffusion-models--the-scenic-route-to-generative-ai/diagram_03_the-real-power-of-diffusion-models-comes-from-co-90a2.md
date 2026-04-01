# The real power of diffusion models comes from **co

```mermaid
---
config:
  theme: base
  layout: elk
---
graph TD
    subgraph "**Conditioning Methods**"
        T[Text Prompt<br/>"A cat sitting on a mat"] --> C[Conditioning<br/>Embedding]
        
        I[Image<br/>Style reference] --> C
        
        S[Sketch/Mask<br/>Spatial constraints] --> C
        
        C --> D[Diffusion Model<br/>U-Net + Cross-Attention]
        
        D --> O[Generated Image<br/>Matches condition]
    end
    
    style C fill:#ffd700,stroke:#333,stroke-width:2px
    style O fill:#90be6d,stroke:#333,stroke-width:4px
```
