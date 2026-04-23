# ## Appendix B: System Requirements for .NET 10 Fea

| Feature | Minimum CPU | OS Support | RAM Recommendation | Notes |
|---------|-------------|------------|--------------------|-------|
| AVX-512 | Intel Skylake-X / Ice Lake, AMD Zen 4 | Windows 11 22H2+, Linux 5.10+ | N/A | Software fallback available |
| Vector512 | Same as AVX-512 | Same as AVX-512 | N/A | Requires hardware support |
| Pinned Object Heap | Any x64, ARM64 | Windows 10+, Linux, macOS | +4MB overhead | On by default |
| Server GC | Any dual-core + | All | +1 heap per core (e.g., 8-core = +8 heaps) | Configurable |
| Native AOT | Any | Same as runtime | Smaller than JIT (~1/3) | No JIT allowed |
| PGO | Any | All | +2-5% memory for counters | On by default in .NET 10 |
| Tiered Compilation | Any | All | Minimal | On by default |
| Background GC | Any | All | +1-2 threads | On by default (server) |
