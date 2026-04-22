# **Technical Features and Infrastructure Mapping:**

| Technical Feature | Implementation | Terraform Role | Kubernetes Role |
|-------------------|---------------|----------------|-----------------|
| **RESTful API with JWT** | ASP.NET Core controllers, JWT Bearer authentication with Google OAuth | Create Key Vault for JWT signing secrets (HSM-backed), configure access policies | Deploy API pods (3-20 replicas), inject secrets via CSI driver with polling, HPA scaling |
| **SignalR Real-time** | WebSocket connections for live telemetry streaming to dashboards | Provision Azure Load Balancer with session affinity (ClientIP, 10800s timeout), configure health probes | Deploy SignalR Hub pods with backplane (Azure Redis Cache), session affinity service |
| **Google OAuth** | Social login for fleet managers and drivers | Create Key Vault secrets for OAuth client ID and secret, configure redirect URIs | Mount secrets to API pods, implement OAuth callback handlers, manage token refresh |
| **Rx.NET Event-driven** | Reactive pipelines for telemetry processing with backpressure handling | Provision Azure Service Bus or Kafka topics, configure Event Grid subscriptions | Deploy background processor pods with memory limits (4-8 Gi), Rx.NET buffer windows (5s/10000 messages) |
| **Multi-provider Eventing** | Azure Event Grid, AWS EventBridge, Apache Kafka support | Create Event Grid topics and subscriptions, configure private endpoints for Kafka | Run event adapter pods, configuration via ConfigMaps, provider abstraction interface |
| **MongoDB Change Streams** | Real-time database change notifications for geo-fence triggers | Enable change feed in Cosmos DB, configure partition key routing | Deploy change stream processor pods, resume tokens for fault tolerance |
| **Health Checks** | /health, /ready, /live endpoints for probe detection | Configure Application Gateway health probes (interval 30s, timeout 30s, unhealthy threshold 3) | Implement liveness/readiness/startup probes in deployment manifests |
| **Prometheus Metrics** | /metrics endpoint for telemetry and business metrics | Deploy Prometheus with Azure Monitor integration | Configure ServiceMonitor, PodMonitor resources for scraping |
