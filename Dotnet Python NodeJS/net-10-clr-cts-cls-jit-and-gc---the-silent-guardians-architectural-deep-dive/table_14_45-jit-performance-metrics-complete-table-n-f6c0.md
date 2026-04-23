# ### 4.5 JIT Performance Metrics Complete Table (.N

| Optimization Category | Specific Technique | .NET 1.0 | .NET 8 | .NET 10 | Factor Improvement (1.0→10) |
|----------------------|-------------------|----------|--------|---------|------------------------------|
| **Inlining** | Inlining depth | 0 (none) | Up to 20 | Up to 25 + ML | Unlimited (PGO-guided) |
| **Inlining** | PGO-guided inlining | ❌ | ❌ (opt-in) | ✅ (default) | 15-30% hot path improvement |
| **Loop** | Loop unrolling | None | Basic (2x) | ML-predicted (2x-8x) | Up to 4x |
| **Loop** | Loop invariant code motion | ❌ | ✅ | ✅ + PGO | ~2x for invariant-heavy code |
| **Loop** | Range check elimination | ❌ | Loop-invariant only | Loop-invariant + PGO | ~95% elimination |
| **SIMD** | Vector width | None | 256-bit (AVX2) | 512-bit (AVX-512) | 16x (theoretical) |
| **SIMD** | Auto-vectorization | ❌ | Basic loops | Complex patterns | 8x for typical code |
| **Devirtualization** | Single type check | ❌ | ✅ | ✅ + guarded | ~90% virtual call reduction |
| **Devirtualization** | PGO-guided devirt | ❌ | ❌ | ✅ | ~99% when polymorphic |
| **Memory** | Stack allocation | None | Basic (Span<T>) | Enhanced + Pinned OH | ~80% less heap pressure |
| **Memory** | Register allocation | Poor (spills often) | Good (linear scan) | PGO-optimized | ~40% fewer spills |
| **PGO** | Profile collection | ❌ | Dynamic (opt-in) | Dynamic + training mode | 15-30% faster hot paths |
| **Startup** | Tier 0 compilation time | ~50ms | ~8ms | ~2ms | 25x faster |
| **Startup** | Native AOT startup | ❌ | ~5ms | ~0.5ms | 100x faster (vs .NET 1.0) |
| **Exception** | Try/catch overhead | High (SEH) | Moderate | Low (table-based) | ~4x faster |
