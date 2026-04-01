# The original Transformer had two parts: encoder (r

```mermaid
---
config:
  theme: base
  layout: elk
---
graph TD
    subgraph "**Encoder-Decoder (BERT, T5)**"
        E[Encoder<br/>Bidirectional<br/>Sees all tokens] --> D[Decoder<br/>Autoregressive<br/>Generates one at a time]
    end
    
    subgraph "**Decoder-Only (GPT)**"
        D2[Decoder<br/>Autoregressive<br/>Generates one at a time] --> O[Output]
    end
    
    subgraph "**Why Decoder-Only Won**"
        R1[Simplicity<br/>One architecture, not two]
        R2[Scalability<br/>Easier to scale]
        R3[Generative<br/>Built for generation]
    end
    
    style D2 fill:#ffd700,stroke:#333,stroke-width:4px
```
