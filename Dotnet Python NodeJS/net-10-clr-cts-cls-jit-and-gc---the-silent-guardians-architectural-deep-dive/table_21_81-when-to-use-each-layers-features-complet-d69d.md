# ### 8.1 When to Use Each Layer's Features (Complet

| Feature | Best Used For | Version Added | .NET 10 Improvement | Performance Impact |
|---------|---------------|---------------|----------------------|--------------------|
| **CLS compliance** | Public libraries consumed by VB.NET, F#, IronPython | 1.0 | Extended generic variance rules | Zero (compile-time only) |
| **Int128/UInt128** | Cryptographic ops, large integer ranges, hashing, big number math | 10 | Hardware acceleration on x64 (`MUL` instruction) | ~100x vs BigInteger |
| **Vector512** | ML inference, image processing, scientific computing, audio processing | 10 | Requires AVX-512, fallback to 256-bit | ~16x vs scalar |
| **Pinned Object Heap** | High-frequency native interop, `Span<byte>` with native interop, real-time | 10 | Eliminates GC fragmentation | ~50% less GC time |
| **Tiered Compilation** | All apps (on by default) — improves startup and steady-state | 8 | Tier 0 instrumentation + PGO | 25x faster startup |
| **Native AOT** | Microservices, CLI tools, containerized deployments, serverless | 10 (prod) | Production-ready, single EXE | 2ms startup, 20MB memory |
| **Generic Math** | Numeric algorithms across int, float, Half, Vector, etc. | 7 (C# 11) | Enhanced for Vector512 | Zero boxing overhead |
| **PGO** | Long-running server workloads, performance-critical paths | 8 (opt-in) | Default + training mode | 15-30% hot path improvement |
| **Span<T>** | Zero-copy parsing, array slicing, stack allocation | 7 (C# 7.2) | Enhanced with MemoryManager | ~80% less allocations |
| **Record types** | Immutable DTOs, value objects, aggregate roots | 9 (C# 9) | Record structs | Same as class/struct |
| **Required members** | Object construction validation, required properties | 11 (C# 11) | Constructor equivalence | Zero runtime cost |
| **Collection expressions** | Array/list initialization, collection literals | 12 (C# 12) | Compile-time optimized | Zero allocation when possible |
