# ### 6.1 Complete Runtime Comparison Matrix

| Feature Area | .NET 1.0 (2002) | .NET 8 (2023) | .NET 10 (2025) |
|--------------|-----------------|---------------|-----------------|
| **JIT Tiers** | 1 | 2 (Quick + Optimizing) | 3 (Instrumented + Quick + Opt) |
| **PGO** | None | Dynamic (opt-in) | Dynamic (default + training mode) |
| **AVX Support** | None | AVX2 | AVX-512 + auto-vectorization |
| **Native AOT** | ❌ | ✅ Experimental | ✅ Production |
| **Generic Variance** | Invariant | Covariant/Contravariant (partial) | Full + user-defined |
| **Half precision** | ❌ | Basic | Full math + hardware acceleration |
| **String interning** | Manual (`String.Intern`) | Automatic + dedup | Automatic + LOH-optimized |
| **Exception handling** | SEH-based | SEH + EH | Enhanced unwinding + faster catch |
| **Pinned handling** | GCHandle (fragments) | Same | Pinned Object Heap (no fragment) |
| **GC modes** | Workstation | Workstation/Server | + LowLatency, SustainedLowLatency |
| **Span<T>** | ❌ | ✅ | ✅ + MemoryManager |
| **Default interface methods** | ❌ | ✅ (C# 8) | ✅ + CLS compliance |
| **Function pointers** | ❌ | ✅ (C# 9) | ✅ + Native AOT |
| **Static abstract interfaces** | ❌ | ✅ (C# 11) | ✅ + generic math improvements |
| **Collection expressions** | ❌ | ❌ | ✅ (C# 12) |
| **Required members** | ❌ | ✅ (C# 11) | ✅ + constructor equivalence |
| **Record types** | ❌ | ✅ (C# 9) | ✅ + record struct |
| **NonNullable reference types** | ❌ | ✅ (C# 8) | ✅ + stricter analysis |
| **Generic math (`INumber<T>`)** | ❌ | ✅ (C# 11/.NET 7) | ✅ + additional interfaces |
| **Int128/UInt128** | ❌ | ❌ | ✅ Native |
| **Vector512** | ❌ | ❌ | ✅ AVX-512 |
| **Pinned Object Heap** | ❌ | ❌ | ✅ |
