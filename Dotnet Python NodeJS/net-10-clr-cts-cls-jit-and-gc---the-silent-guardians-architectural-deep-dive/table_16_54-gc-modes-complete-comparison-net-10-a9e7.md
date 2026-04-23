# ### 5.4 GC Modes Complete Comparison (.NET 10)

| GC Mode | Description | Best For | Typical Pause | Throughput | Memory Footprint |
|---------|-------------|----------|---------------|------------|------------------|
| **Workstation (Interactive)** | Single heap, optimized for UI responsiveness | Desktop apps, GUI | ~1-5ms | Medium | Lower |
| **Workstation (Background)** | Concurrent mark, foreground compact | Interactive services | ~0.5-2ms | Medium | Lower |
| **Server** | One heap per CPU, high throughput | Backend services, APIs | ~5-20ms | Very high | Higher (×CPU count) |
| **Server + Background** | Concurrent, per-CPU heaps | High-scale services | ~2-10ms | Highest | Higher |
| **LowLatency** | Minimal pauses, disables Gen2 | Real-time, gaming | <1ms | Lower | Higher (deferred collection) |
| **SustainedLowLatency** | Balanced low-latency | Trading, streaming | ~1ms | Medium-High | Medium |
