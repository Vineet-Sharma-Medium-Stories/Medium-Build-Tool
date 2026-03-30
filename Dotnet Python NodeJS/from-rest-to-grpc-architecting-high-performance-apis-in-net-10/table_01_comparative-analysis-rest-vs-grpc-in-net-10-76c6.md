# ## Comparative Analysis: REST vs. gRPC in .NET 10

| Aspect | REST (JSON/HTTP) | gRPC (Protobuf/HTTP/2) with .NET 10 |
|--------|------------------|-------------------------------------|
| **Data Format** | JSON (text, human-readable) ~200-500 bytes per message | Protobuf (binary) ~30-100 bytes per message |
| **Serialization** | System.Text.Json (reflection-based) | Protobuf source generators (compile-time) |
| **Transport** | HTTP/1.1 (separate connections) or HTTP/2 | HTTP/2 multiplexed streams |
| **Performance** | 1,000-5,000 requests/sec per core | 20,000-50,000 requests/sec per core |
| **Streaming** | No native streaming (WebSockets required) | Full support: unary, server, client, bidirectional |
| **Contract** | OpenAPI/Swagger (separate document) | Protobuf (single source of truth) |
| **Code Generation** | Manual DTOs or external tooling | Built-in source generators in .NET SDK |
| **Browser Support** | Native | gRPC-Web via .NET 10 Envoy integration |
| **Caching** | HTTP caching (ETag, Cache-Control) | Not natively supported; handled at application layer |
| **Load Balancing** | Layer 7 (HTTP) with standard algorithms | Layer 5 with client-side load balancing (gRPC LB) |
| **Observability** | ASP.NET Core middleware + OpenTelemetry | Enhanced OpenTelemetry integration with gRPC-specific metrics |
| **Native AOT** | Supported with limitations | Enhanced AOT support with source generators |
| **AI Integration** | Basic (OpenAPI descriptions) | Native AI Minimal APIs for service discovery |
| **Memory Footprint** | Moderate (text parsing) | Low (binary, pooled buffers) |
