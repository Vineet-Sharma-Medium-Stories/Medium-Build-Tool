# ## Appendix: Service Mapping (Azure → AWS)

| Azure Service | AWS Equivalent | Vehixcare Usage |
|---------------|----------------|-----------------|
| AKS (Azure Kubernetes Service) | EKS (Elastic Kubernetes Service) | Container orchestration |
| Cosmos DB MongoDB API | Amazon DocumentDB (MongoDB-compatible) | Telemetry data storage |
| Azure Container Registry | Amazon ECR | Container image registry |
| Azure Key Vault | AWS Secrets Manager + KMS | Secret management |
| Azure Virtual Network | Amazon VPC | Network isolation |
| Application Gateway WAF | AWS WAF + Load Balancer Controller | Ingress + WAF |
| Azure Load Balancer | Network Load Balancer (NLB) | Traffic distribution |
| Azure Active Directory | IAM Roles + IRSA | Authentication/authorization |
| Azure Event Grid | Amazon EventBridge | Event routing |
| Azure Service Bus | Amazon SQS + SNS | Message queuing |
| Azure SignalR Service | AWS AppSync (GraphQL subscriptions) | Real-time streaming |
| Azure Monitor | Amazon CloudWatch + AMP | Monitoring and observability |
| Azure Bastion | EC2 Instance Connect + Session Manager | Secure management access |
| Azure Private Endpoint | VPC Endpoint (Interface) | Private service access |
| Azure DNS | Amazon Route 53 | DNS management |
| Azure CDN | Amazon CloudFront | Content delivery |
| Azure Functions | AWS Lambda | Serverless compute |
| Azure Redis Cache | Amazon ElastiCache (Redis) | Caching layer |
| Azure Log Analytics | Amazon CloudWatch Logs | Log aggregation |
