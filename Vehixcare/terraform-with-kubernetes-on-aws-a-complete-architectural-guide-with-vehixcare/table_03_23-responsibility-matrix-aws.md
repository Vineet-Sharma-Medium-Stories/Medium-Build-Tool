# ### 2.3 Responsibility Matrix (AWS)

| Concern | Terraform | Kubernetes |
|---------|-----------|------------|
| Provision AWS VPC and subnets with CIDR 10.0.0.0/16 | ✅ Creates | ❌ Cannot |
| Create EKS cluster with system and user node groups | ✅ Provisions cluster (15 min apply) | ❌ Cannot |
| Deploy ECR with cross-region replication and lifecycle policies | ✅ Creates repository | ❌ Cannot |
| Configure DocumentDB with 40,000 IOPS autoscale | ✅ Creates cluster, databases, collections | ❌ Cannot |
| Manage DocumentDB connection strings and secrets | ✅ Outputs to state (sensitive) | ✅ Injects via CSI driver with polling |
| Autoscale based on telemetry ingestion rate (1000 msg/sec) | ❌ Not possible | ✅ HPA with custom Prometheus metrics |
| Handle AppSync GraphQL subscriptions with session affinity | ❌ No awareness | ✅ LoadBalancer service with ClientIP affinity |
| Process Rx.NET event streams with backpressure | ❌ No capability | ✅ Deployments with memory limits (4-8 Gi) |
| Configure EventBridge event buses and rules | ✅ Creates buses, rules | ❌ Cannot |
| Rotate JWT signing keys without pod restart | ⚠️ Requires terraform apply | ✅ CSI driver with pollInterval: 5m |
| Restart failed containers on crash loop | ❌ Cannot | ✅ Liveness probes (HTTP GET /health/live) |
| Rolling updates without downtime | ❌ Replace-only | ✅ Deployment with maxSurge: 1 |
| Create geospatial indexes for geo-fencing | ✅ Creates 2dsphere indexes | ❌ Cannot |
| Configure Prometheus scraping and Grafana dashboards | ✅ Deploy with Helm provider | ✅ ServiceMonitor resources |
| Implement network policies for tenant isolation | ❌ Cannot | ✅ Calico network policies |
