# ### 5.2 GC Evolution Complete Timeline (Detailed)

| Feature | .NET 1.0 (2002) | .NET 2.0 (2005) | .NET 4.0 (2010) | .NET 4.5 (2012) | .NET 8 (2023) | .NET 10 (2025) |
|---------|-----------------|-----------------|-----------------|-----------------|---------------|-----------------|
| **Generations** | 3 (0,1,2) | 3 | 3 | 3 | 3 | 3 + segments |
| **Background GC** | ❌ Stop-the-world | ❌ | ❌ (still blocking) | ✅ Workstation/Server | ✅ Enhanced | ✅ + adaptive |
| **Large Object Heap (LOH)** | Single, no compaction | Single, no compaction | Single, no compaction | Single, no compaction | Single + optional compaction | Segmented + background compaction |
| **Pinned Object Heap** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ NEW |
| **Heap count** | 1 default | 1 per CPU (server mode) | NUMA-aware | NUMA-aware | NUMA-aware + static | NUMA-aware + dynamic balancing |
| **GC modes** | Workstation only | Workstation/Server | Workstation/Server | Workstation/Server + LowLatency | Workstation/Server + SustainedLowLatency | + Dynamic switching |
| **Card table** | Basic | Basic | Basic | Basic | Adaptive | Cache-friendly |
| **Memory pressure API** | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ Enhanced |
| **Segment size** | Fixed (depends) | Fixed | Fixed | Fixed | Configurable | Adaptive |
| **GC pause time (typical)** | ~50-200ms | ~30-100ms | ~20-80ms | ~10-30ms | ~1-5ms | ~0.5-2ms |
| **Throughput (allocs/sec)** | ~500K | ~1M | ~2M | ~3M | ~5M | ~8M |
