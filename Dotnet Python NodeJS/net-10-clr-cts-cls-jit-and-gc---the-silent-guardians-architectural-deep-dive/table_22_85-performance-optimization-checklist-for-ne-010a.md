# ### 8.5 Performance Optimization Checklist for .NE

| Optimization | How to Enable | Expected Gain | Complexity |
|--------------|---------------|---------------|------------|
| Enable PGO | Add `<TieredPGO>true</TieredPGO>` to csproj | 15-30% | Low |
| Enable Server GC | Add `<ServerGarbageCollection>true</ServerGarbageCollection>` | 2x throughput | Low |
| Use Pinned Object Heap | Use `GC.AllocateArray(pinned: true)` for interop buffers | 50% less GC time | Medium |
| Use `Span<T>` | Replace array slices with `Span<T>.Slice` | 80% less allocations | Medium |
| Use `ArrayPool<T>` | `ArrayPool<T>.Shared.Rent/Return` | 90% less allocation | Low |
| Use source gen serialization | `JsonSourceGenerationOptions` | 3x faster JSON | Low |
| Use LibraryImport (P/Invoke) | Replace `DllImport` with `LibraryImport` | 2x faster interop | Low |
| Use `ValueTask` instead of `Task` | For hot async paths | 50% less allocation | Medium |
| Use `record` types | For immutable DTOs | Zero (better semantics) | Low |
| Use `required` members | For constructor validation | Zero (compile-time) | Low |
| Enable Native AOT | `<PublishAot>true</PublishAot>` | 10x faster startup | High (limitations) |
