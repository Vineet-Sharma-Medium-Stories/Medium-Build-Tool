# **Configuration comparison across gateways:**

| Strategy        | Kong | NGINX | AWS Gateway         | Azure APIM    | GCP Endpoints | Tyk |
| --------------- | ---- | ----- | ------------------- | ------------- | ------------- | --- |
| Fixed window    | ✅    | ✅     | ✅                   | ✅             | ✅             | ✅   |
| Sliding window  | ✅    | ❌     | ❌                   | ✅             | ❌             | ✅   |
| Token bucket    | ❌    | ❌     | ✅ (burst)           | ❌             | ❌             | ❌   |
| Per-user limits | ✅    | ✅     | ✅ (via usage plans) | ✅             | ✅             | ✅   |
| Per-API key     | ✅    | ✅     | ✅                   | ✅             | ✅             | ✅   |
| Redis-backed    | ✅    | ✅     | N/A (managed)       | N/A (managed) | N/A (managed) | ✅   |
