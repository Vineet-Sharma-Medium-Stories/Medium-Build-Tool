# ### 2.3 Technology Stack

| Layer                       | Technology                                 | Version | .NET 10 Advantage                                          |
| --------------------------- | ------------------------------------------ | ------- | ---------------------------------------------------------- |
| **Backend Framework**       | ASP.NET Core                               | 10.0    | Native AOT, PGO, SIMD intrinsics, improved minimal APIs    |
| **Database**                | MongoDB                                    | 7.0+    | Bulk operations, change streams, native .NET 10 driver     |
| **Real-time Communication** | SignalR                                    | 10.0    | WebSocket compression, group management, Redis backplane   |
| **Reactive Processing**     | Rx.NET                                     | 6.0.1   | Async enumerables, channels, System.Threading.RateLimiting |
| **Authentication**          | JWT Bearer + Google OAuth 2.0              | 10.0    | Source-generated validation, improved token handling       |
| **Containerization**        | Docker & Kubernetes                        | 1.30+   | Native container optimizations, cgroup v2 support          |
| **Event Bus**               | Kafka / Azure Event Grid / AWS EventBridge | Latest  | High-throughput serialization with MessagePack             |
| **Caching**                 | Redis                                      | 7.2+    | RESP3 protocol, client-side caching                        |
