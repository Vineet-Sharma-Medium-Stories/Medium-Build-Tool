# **Technical Features and Infrastructure Mapping (A

| Technical Feature | Implementation | Terraform Role | Kubernetes Role |
|-------------------|---------------|----------------|-----------------|
| **RESTful API with JWT** | ASP.NET Core controllers, JWT Bearer authentication with Google OAuth | Create Secrets Manager for JWT signing secrets, configure access policies | Deploy API pods (3-20 replicas), inject secrets via CSI driver with polling, HPA scaling |
| **Real-time Streaming** | GraphQL subscriptions for live telemetry streaming to dashboards | Provision AWS AppSync API with WebSocket support, configure custom domain | Deploy AppSync resolver pods, session affinity service |
| **Google OAuth** | Social login for fleet managers and drivers | Create Secrets Manager secrets for OAuth client ID and secret, configure redirect URIs | Mount secrets to API pods, implement OAuth callback handlers, manage token refresh |
| **Rx.NET Event-driven** | Reactive pipelines for telemetry processing with backpressure handling | Provision Amazon SQS or MSK (Kafka) topics, configure EventBridge rules | Deploy background processor pods with memory limits (4-8 Gi), Rx.NET buffer windows (5s/10000 messages) |
| **Multi-provider Eventing** | AWS EventBridge, Azure Event Grid, Apache Kafka support | Create EventBridge event buses and rules, configure VPC endpoints for MSK | Run event adapter pods, configuration via ConfigMaps, provider abstraction interface |
| **MongoDB Change Streams** | Real-time database change notifications for geo-fence triggers | Enable change streams in DocumentDB, configure partition key routing | Deploy change stream processor pods, resume tokens for fault tolerance |
| **Health Checks** | /health, /ready, /live endpoints for probe detection | Configure Network Load Balancer health probes (interval 30s, timeout 30s, unhealthy threshold 3) | Implement liveness/readiness/startup probes in deployment manifests |
| **Prometheus Metrics** | /metrics endpoint for telemetry and business metrics | Deploy Prometheus with AMP (Amazon Managed Service for Prometheus) integration | Configure ServiceMonitor, PodMonitor resources for scraping |
