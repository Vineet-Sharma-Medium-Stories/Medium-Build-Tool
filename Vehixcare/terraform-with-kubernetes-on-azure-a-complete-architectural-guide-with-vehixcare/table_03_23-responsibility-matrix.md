# ### 2.3 Responsibility Matrix

| Concern | Terraform | Kubernetes |
|---------|-----------|------------|
| Provision Azure VNet and subnets with CIDR 10.0.0.0/8 | ✅ Creates | ❌ Cannot |
| Create AKS cluster with system and user node pools | ✅ Provisions cluster (15 min apply) | ❌ Cannot |
| Deploy ACR with geo-replication and retention policies | ✅ Creates Premium SKU registry | ❌ Cannot |
| Configure Cosmos DB MongoDB with 40,000 RU/s autoscale | ✅ Creates account, databases, collections | ❌ Cannot |
| Manage MongoDB connection strings and secrets | ✅ Outputs to state (sensitive) | ✅ Injects via CSI driver with polling |
| Autoscale based on telemetry ingestion rate (1000 msg/sec) | ❌ Not possible | ✅ HPA with custom Prometheus metrics |
| Handle SignalR WebSocket connections with session affinity | ❌ No awareness | ✅ LoadBalancer service with ClientIP affinity, 10800s timeout |
| Process Rx.NET event streams with backpressure | ❌ No capability | ✅ Deployments with memory limits (4-8 Gi), buffer operators |
| Configure Event Grid topics and subscriptions | ✅ Creates topics, event subscriptions | ❌ Cannot |
| Rotate JWT signing keys without pod restart | ⚠️ Requires terraform apply | ✅ CSI driver with pollInterval: 5m |
| Restart failed containers on crash loop | ❌ Cannot | ✅ Liveness probes (HTTP GET /health/live) |
| Rolling updates without downtime | ❌ Replace-only | ✅ Deployment with maxSurge: 1, maxUnavailable: 0 |
| Create geospatial indexes for geo-fencing | ✅ Creates 2dsphere indexes | ❌ Cannot |
| Configure Prometheus scraping and Grafana dashboards | ✅ Deploy with Helm provider | ✅ ServiceMonitor resources |
| Implement network policies for tenant isolation | ❌ Cannot | ✅ Calico network policies |
