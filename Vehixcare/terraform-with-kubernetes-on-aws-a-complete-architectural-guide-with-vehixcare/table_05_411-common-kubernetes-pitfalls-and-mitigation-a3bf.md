# ### 4.11 Common Kubernetes Pitfalls and Mitigation

| Pitfall | Mitigation |
|---------|------------|
| **AppSync connection drops** during pod restarts | Use NLB with session affinity (`sessionAffinity: ClientIP`). Set `terminationGracePeriodSeconds: 60`. |
| **DocumentDB connection pool exhaustion** | Set `maxPoolSize: 200`. Implement retry logic with exponential backoff. |
| **Rx.NET event processor backpressure** | Use bounded queues with `BoundedCapacity(10000)`. Implement `Buffer` operators. |
| **Geo-fence query performance** | Create 2dsphere indexes. Implement spatial partitioning. Cache in ElastiCache (Redis). |
| **Pod startup time** for .NET 9.0 | Use `startupProbe` with `failureThreshold: 30`. Enable ReadyToRun (R2R) compilation. |
| **Secret rotation** without pod restart | Use Secrets Store CSI Driver with `pollInterval: 5m`. |
| **Multi-provider eventing configuration** | Use environment variables. Implement provider abstraction. |
| **IRSA permission issues** | Verify OIDC provider. Check service account annotations. |
| **Telemetry data loss** on pod crash | Implement idempotent ingestion. Use dead-letter queues (SQS DLQ). |
| **JWT token validation failures** | Store public keys in Secrets Manager with versioning. Use JWKS endpoint. |
| **OOM kills** on Rx.NET processors | Set memory limits equal to requests. Profile with dotnet-monitor. |
| **Calico network policy performance** | Use AWS VPC CNI with security groups for network policies. |
| **EKS node image updates** | Use managed node groups with `update_config`. Test in staging first. |
| **VPC CNI IP exhaustion** | Enable `WARM_IP_TARGET`. Use secondary CIDR for pods. |
