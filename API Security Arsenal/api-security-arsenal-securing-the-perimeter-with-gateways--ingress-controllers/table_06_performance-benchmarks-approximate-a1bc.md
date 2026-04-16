# ## Performance Benchmarks (Approximate)

| Gateway       | Latency (p99) | Throughput (req/sec) | Notes              |
| ------------- | ------------- | -------------------- | ------------------ |
| NGINX         | 1-2ms         | 50,000+              | Fastest            |
| Kong          | 2-5ms         | 30,000+              | Plugin overhead    |
| Tyk           | 3-6ms         | 25,000+              | Analytics overhead |
| AWS Gateway   | 5-10ms        | 10,000+              | Regional latency   |
| Azure APIM    | 8-15ms        | 8,000+               | Policy processing  |
| GCP Endpoints | 5-10ms        | 10,000+              | ESP overhead       |
