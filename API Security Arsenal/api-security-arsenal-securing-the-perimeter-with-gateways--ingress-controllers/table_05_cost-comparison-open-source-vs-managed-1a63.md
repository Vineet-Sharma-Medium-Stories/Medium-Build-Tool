# ## Cost Comparison: Open-Source vs. Managed

| Gateway         | Entry Cost         | Operational Overhead  | Scaling Cost               |
| --------------- | ------------------ | --------------------- | -------------------------- |
| Kong (OSS)      | $0                 | High (self-managed)   | Add nodes                  |
| NGINX (OSS)     | $0                 | High (self-managed)   | Add nodes + LB             |
| Tyk (OSS)       | $0                 | Medium (self-managed) | Add nodes + Redis          |
| AWS Gateway     | $0 upfront         | Low (fully managed)   | $3.50 per million requests |
| Azure APIM      | $0.04/hour (basic) | Low (managed)         | Consumption tier available |
| GCP Endpoints   | $0 upfront         | Low (managed)         | $2 per million requests    |
| Kong Enterprise | Custom             | Medium                | Includes support           |
| NGINX Plus      | ~$2500/node/year   | Medium                | Per-node licensing         |
