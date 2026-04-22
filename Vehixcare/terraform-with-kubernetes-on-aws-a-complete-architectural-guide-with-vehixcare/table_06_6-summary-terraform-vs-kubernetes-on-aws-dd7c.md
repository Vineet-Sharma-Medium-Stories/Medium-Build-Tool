# ## 6. Summary: Terraform vs Kubernetes on AWS

| Layer | Tool | Responsibility | Vehixcare Example (AWS) |
|-------|------|----------------|--------------------------|
| **Cloud Infrastructure** | Terraform | VPC, subnets, DocumentDB (40,000 IOPS), EKS cluster (3+5 nodes), ECR, Secrets Manager (KMS) | Provision DocumentDB with 40,000 IOPS autoscale for telemetry ingestion, global cluster to us-west-2 |
| **Container Orchestration** | Kubernetes | Pod scheduling, rolling updates (maxSurge:1), service discovery (ClusterIP/NLB), HPA (3-20 replicas) | Scale Telemetry API from 3 to 20 pods based on 1000 telemetry messages/sec |
| **Application Health** | Kubernetes | Liveness/readiness/startup probes, auto-restart, termination grace period (60s) | Restart telemetry API pod if DocumentDB connection fails; 30s startup probe |
| **Secret Management** | Both | Terraform creates secrets in Secrets Manager (KMS); Kubernetes CSI mounts with 5m poll interval | JWT signing key rotated without pod restart via CSI driver polling |
| **Event Streaming** | Both | Terraform creates EventBridge event buses; Kubernetes runs Rx.NET processors with backpressure | Driver behavior scoring via Rx.NET buffer windows (5s/10000 messages) |
| **Real-time Communication** | Kubernetes | AppSync resolver with NLB, session affinity (ClientIP, 10800s) | Live telemetry streaming to 5000+ concurrent fleet dashboards via GraphQL subscriptions |
| **Geo-fencing** | Both | Terraform creates 2dsphere indexes; Kubernetes runs monitor with ElastiCache (Redis) | Detect vehicle entry/exit from 10,000+ active geo-fences |
| **Multi-tenancy** | Both | Terraform configures partition keys (organization_id); Kubernetes enforces RBAC and network policies | Isolate telemetry data for 500+ organizations |
