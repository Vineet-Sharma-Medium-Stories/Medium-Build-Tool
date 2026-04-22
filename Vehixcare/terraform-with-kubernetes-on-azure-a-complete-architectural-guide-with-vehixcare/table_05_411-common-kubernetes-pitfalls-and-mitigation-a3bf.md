# ### 4.11 Common Kubernetes Pitfalls and Mitigation

| Pitfall | Mitigation |
|---------|------------|
| **SignalR connection drops** during pod restarts | Use LoadBalancer with session affinity (`sessionAffinity: ClientIP`). Configure Azure SignalR Service backplane. Set `terminationGracePeriodSeconds: 60`. |
| **MongoDB connection pool exhaustion** under high telemetry load | Set `maxPoolSize: 200` in connection string. Configure HPA based on MongoDB connection metrics. Implement retry logic with exponential backoff. |
| **Rx.NET event processor backpressure** causing memory leaks | Use bounded queues with `new BoundedCapacity(10000)`. Implement `Buffer` or `Window` operators with timeouts. Set memory limits and monitoring. |
| **Geo-fence query performance** with thousands of boundaries | Create 2dsphere indexes on coordinates. Implement spatial partitioning. Cache active geo-fences in Redis with TTL. |
| **Pod startup time** for .NET 9.0 containers (JIT compilation) | Use `startupProbe` with `failureThreshold: 30`. Enable ReadyToRun (R2R) compilation. Use `initialDelaySeconds: 30`. |
| **Secret rotation** without pod restart | Use Secrets Store CSI Driver with `pollInterval: 5m`. Enable auto-rotation with `rotationPollInterval`. |
| **Multi-provider eventing configuration** (Event Grid, EventBridge, Kafka) | Use environment variables to switch providers. Implement provider abstraction interface. Test all providers in staging. |
| **SignalR scale-out** across multiple pods | Use Azure SignalR Service (PaaS) instead of self-hosted. Or configure Redis backplane with `azure-redis`. |
| **Telemetry data loss** on pod crash | Implement idempotent telemetry ingestion with idempotency keys. Use dead-letter queues for failed events. Enable Cosmos DB point-in-time recovery. |
| **JWT token validation failures** after key rotation | Store public keys in Azure Key Vault with versioning. Implement key caching with short TTL. Use well-known configuration endpoint for JWKS. |
| **OOM kills** on Rx.NET processors | Set memory limits equal to requests. Profile memory usage with dotnet-monitor. Use `GC.SetGCServerMode(true)`. |
| **Calico network policy performance** | Use `profile: "calico"` with `network_policy = "azure"` for better performance. Limit policy count. |
| **AKS node image updates** causing disruption | Use `maintenance_window` for planned upgrades. Enable `auto_upgrade_channel = "stable"`. Test in staging first. |
