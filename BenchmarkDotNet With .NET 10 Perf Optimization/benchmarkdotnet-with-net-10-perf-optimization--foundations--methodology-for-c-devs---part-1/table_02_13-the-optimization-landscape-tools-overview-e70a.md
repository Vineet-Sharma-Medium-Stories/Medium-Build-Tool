# ### 1.3 The Optimization Landscape: Tools Overview

| Tool                | Best For                                                     | Limitations                        | When to Use in Vehixcare                                       |
| ------------------- | ------------------------------------------------------------ | ---------------------------------- | -------------------------------------------------------------- |
| **BenchmarkDotNet** | Micro-benchmarks, algorithm comparison, regression detection | No I/O, no async complex workflows | **Primary focus** - Driver scoring, serialization, geo-fencing |
| **dotnet-trace**    | Production profiling, GC analysis, event tracing             | Noisy, requires interpretation     | After Benchmarks identify hotspots in production               |
| **dotnet-counters** | Live metric monitoring (CPU, memory, GC)                     | Surface-level only                 | During load testing and canary deployments                     |
| **dotnet-stack**    | Live stack traces for hung processes                         | Performance overhead               | Debugging production deadlocks                                 |
| **dotnet-gcdump**   | GC heap analysis                                             | Single snapshot only               | Investigating memory leaks                                     |
| **Apache JMeter**   | Full API endpoint load testing                               | Complex setup, no micro-benchmarks | Integration/E2E testing of complete API surface                |
| **k6**              | Load testing with JavaScript/TypeScript scripts              | No .NET native integration         | API stress testing for telemetry ingestion endpoints           |
| **NBomber**         | .NET-native load testing and simulation                      | Less mature than JMeter            | Scenario-based load tests for SignalR hubs                     |
| **OpenTelemetry**   | Distributed tracing, metrics collection                      | High overhead, production-only     | Post-optimization monitoring across microservices              |
| **PerfView**        | Deep Windows ETW analysis                                    | Windows-only, complex              | Investigating GC patterns and JIT issues                       |
| **EventPipe**       | Cross-platform event tracing                                 | Requires interpretation            | Linux container profiling                                      |
| **Valgrind**        | Memory leak detection on Linux                               | Slow, no .NET-specific             | Native memory investigations                                   |
