# table_03_azure-implementation-matrix


| Service | Discovery Mechanism | Use Case | Registration Method |
| --- | --- | --- | --- |
| **Azure Container Apps** | Internal DNS + Dapr | Containerized microservices | Automatic via environment |
| **App Service with VNet** | Private endpoints | Web apps in VNet | Manual via DNS |
| **AKS** | K8s DNS + Headless services | Complex orchestration | Automatic via K8s API |
| **Azure Traffic Manager** | DNS routing | Global distribution | Manual configuration |
| **Azure Front Door** | Global load balancing | CDN + routing | Manual backend config |
