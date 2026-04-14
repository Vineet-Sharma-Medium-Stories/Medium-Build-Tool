# The diagram below shows how your zero-cost AI stac

```mermaid
flowchart TB
    User[👤 User Browser] --> Frontend[🖥️ Frontend\nVercel / Cloud CDN]
    Frontend --> CloudRun[☁️ Cloud Run\nServerless container\nAutoscaling to zero]
    
    CloudRun --> Ollama[🤖 Ollama LLM\nLlama 3.3 70B\nInside container]
    
    CloudRun --> GCS[📦 Cloud Storage (GCS)\nModel cache (8GB)\nUser uploads\nLogs\nCheckpoints]
    
    CloudRun --> Filestore[📁 Filestore\nPersistent storage\nSQLite database\nRAG vectors]
    
    CloudRun --> VertexAI[🔌 Optional: Vertex AI\nGemini/Claude fallback\nWhen local model uncertain]
    
    CloudRun --> GKE[💪 Optional: GKE with TPU\nTPU v5e pods\nFor maximum AI performance]
    
    CloudRun --> Monitoring[📊 Cloud Monitoring\nLogs | Metrics | Alerts\nCloud Trace for tracing]
    
    style CloudRun fill:#4285f4,stroke:#3367d6,stroke-width:3px,color:#fff
    style GCS fill:#4285f4,stroke:#3367d6,stroke-width:2px,color:#fff
    style VertexAI fill:#4285f4,stroke:#3367d6,stroke-width:2px,color:#fff
    style GKE fill:#4285f4,stroke:#3367d6,stroke-width:2px,color:#fff
```
