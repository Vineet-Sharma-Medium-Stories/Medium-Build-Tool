# ### 1.2 Layer Responsibilities (.NET 10)

| Layer | Primary Role | Key Features in .NET 10 |
|-------|--------------|--------------------------|
| **CLS** | Define rules for language interoperability | Extended generic variance rules, async method shape unification |
| **CTS** | Define and organize all data types | Added native support for `Half`, `Int128`, `UInt128`, `Vector512` |
| **CLR** | Execute and manage .NET applications | Enhanced PGO, dynamic adaptation, improved GC (Gen0/Gen1/Gen2 + BGC), Pinned Object Heap |
| **JIT** | Compile IL to optimized native code | Tiered compilation v3, AVX-512 support, loop unrolling heuristics, ML-guided inlining |
