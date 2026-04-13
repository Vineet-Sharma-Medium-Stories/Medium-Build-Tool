# **When to use Redis vs DynamoDB:**

| Characteristic           | DynamoDB                  | Redis                    |
| ------------------------ | ------------------------- | ------------------------ |
| **Latency**              | Single-digit milliseconds | Sub-millisecond          |
| **Throughput**           | Unlimited (on-demand)     | Limited by instance size |
| **Persistence**          | Durable by default        | Optional (snapshots/AOF) |
| **TTL**                  | Native                    | Native                   |
| **Operational overhead** | Serverless                | Managed ElastiCache      |
| **Best for**             | Up to 10k msg/sec         | 10k-100k+ msg/sec        |
