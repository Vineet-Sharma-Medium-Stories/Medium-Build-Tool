# table_01_vertical-scaling-techniques


| Technique | Description | Implementation |
|-----------|-------------|----------------|
| **Memory Optimization** | Reduce allocations, use pooling | ArrayPool, ObjectPool, Span<T> |
| **CPU Optimization** | Vectorization, SIMD, parallel processing | Vector<T>, SIMD intrinsics |
| **I/O Optimization** | Async I/O, buffer management | Pipelines, memory-mapped files |
| **GC Optimization** | Reduce GC pressure | Structs, object pooling, LOH management |
| **Threading Optimization** | Efficient concurrency | ThreadPool, Task Parallel Library |
