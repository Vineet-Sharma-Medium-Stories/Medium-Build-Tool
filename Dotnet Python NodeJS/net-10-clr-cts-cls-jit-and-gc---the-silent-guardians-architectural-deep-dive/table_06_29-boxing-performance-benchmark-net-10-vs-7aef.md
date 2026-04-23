# ### 2.9 Boxing Performance Benchmark: .NET 1.0 vs 

| Operation | .NET 1.0 (boxed) | .NET 8 (generic) | .NET 10 (generic + PGO) | Improvement |
|-----------|-----------------|------------------|-------------------------|-------------|
| 1M integer additions (in List) | ~45ms, 1M allocs | ~8ms, 0 allocs | ~5ms, 0 allocs | **9x faster** |
| 1M dictionary lookups | ~60ms, 1M allocs | ~12ms, 0 allocs | ~9ms, 0 allocs | **6.7x faster** |
| Array of structs iteration | ~30ms (boxing for interface) | ~3ms | ~2ms | **15x faster** |
| Enum to string conversion | ~25ms (reflection) | ~5ms (code generation) | ~3ms (cached) | **8.3x faster** |
