# ### AWS-Specific Advantages

| Capability | AWS Service | Benefit for Vehixcare |
|------------|-------------|----------------------|
| GraphQL real-time | AWS AppSync | Native GraphQL subscriptions with built-in WebSocket management |
| Event-driven scaling | KEDA + SQS | Seamless integration with EKS pod identity |
| Container registry | ECR with cross-region replication | Automatic image replication to failover region |
| Secret management | Secrets Manager + KMS | Automatic secret rotation with CloudWatch Events |
| Database | DocumentDB Global Cluster | 2-minute failover, MongoDB 4.2 compatibility |
| Network | AWS Load Balancer Controller | Native integration with EKS, supports NLB/ALB |
| Monitoring | AMP (Prometheus) + CloudWatch | Managed Prometheus with 15-month retention |
| Cost | Spot Instances for user node group | Additional 60-70% savings for batch processing |
