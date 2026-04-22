# ## 6. Summary: Terraform vs Kubernetes on Azure

| Layer | Tool | Responsibility | Vehixcare Example |
|-------|------|----------------|-------------------|
| **Cloud Infrastructure** | Terraform | VNet, subnets, NSGs, Cosmos DB (40,000 RU/s), AKS cluster (3+5 nodes), ACR, Key Vault (HSM) | Provision Cosmos DB with 40,000 RU/s autoscale for telemetry ingestion, geo-replicated to North Europe |
| **Container Orchestration** | Kubernetes | Pod scheduling, rolling updates (maxSurge:1), service discovery (ClusterIP/LoadBalancer), HPA (3-20 replicas) | Scale Telemetry API from 3 to 20 pods based on 1000 telemetry messages/sec |
| **Application Health** | Kubernetes | Liveness/readiness/startup probes, auto-restart, termination grace period (60s) | Restart telemetry API pod if MongoDB connection fails; 30s startup probe grace period |
| **Secret Management** | Both | Terraform creates secrets in Key Vault (HSM-backed); Kubernetes CSI mounts with 5m poll interval | JWT signing key rotated without pod restart via CSI driver polling |
| **Event Streaming** | Both | Terraform creates Event Grid topics; Kubernetes runs Rx.NET processors with backpressure | Driver behavior scoring via Rx.NET buffer windows (5s/10000 messages) |
| **Real-time Communication** | Kubernetes | SignalR hub with LoadBalancer, session affinity (ClientIP, 10800s) | Live telemetry streaming to 5000+ concurrent fleet dashboards |
| **Geo-fencing** | Both | Terraform creates 2dsphere indexes; Kubernetes runs monitor with Redis cache | Detect vehicle entry/exit from 10,000+ active geo-fences |
| **Multi-tenancy** | Both | Terraform configures partition keys (organization_id); Kubernetes enforces RBAC and network policies | Isolate telemetry data for 500+ organizations |
