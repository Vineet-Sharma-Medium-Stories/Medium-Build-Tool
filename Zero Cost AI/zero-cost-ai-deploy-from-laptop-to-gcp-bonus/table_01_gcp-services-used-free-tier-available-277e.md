# ### GCP Services Used (Free Tier Available)

| Service | Purpose | Cost Estimate |
|---------|---------|---------------|
| **Cloud Run** | Serverless container (autoscaling to zero) | $0.10-0.50/hour (active), $0 when idle |
| **Cloud Storage (GCS)** | Model cache, user uploads, logs | $0.020/GB-month (first 5GB free) |
| **Filestore** | Persistent SQLite, checkpoints | $0.20-0.30/GB-month |
| **GKE with TPU v5e** | TPU pods for AI inference | $1.50-4.50/hour |
| **Vertex AI** | Optional Gemini fallback | Pay per token |
| **Cloud Monitoring** | Logs, metrics, alerts | First 5GB logs free |
| **Artifact Registry** | Store Docker images | 0.5 GB-month free |
| **Cloud Run jobs** | Batch inference | $0.01-0.10/job |
