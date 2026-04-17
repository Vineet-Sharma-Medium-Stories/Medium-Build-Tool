# ### 1.5 BenchmarkDotNet Attributes: Complete Refer

| Attribute                      | Purpose                           | Vehixcare Usage Example              | Advanced Options                                      |
| ------------------------------ | --------------------------------- | ------------------------------------ | ----------------------------------------------------- |
| `[Benchmark]`                  | Marks method to benchmark         | Telemetry deserialization methods    | `[Benchmark(Description="...")]`                      |
| `[Benchmark(Baseline = true)]` | Reference point for comparison    | Current JSON serializer as baseline  | Only one per class                                    |
| `[MemoryDiagnoser]`            | Tracks allocations per operation  | Detect GC pressure in scoring engine | `[MemoryDiagnoser(true)]` for pinned objects          |
| `[SimpleJob]`                  | Configures runtime and iterations | Compare .NET 8 vs 9 vs 10            | `invocationCount`, `unrollFactor`                     |
| `[Params]`                     | Test multiple input sizes         | Fleet sizes: 100, 1000, 10000        | Can use `[ParamsSource]` for dynamic values           |
| `[GlobalSetup]`                | Runs once before all benchmarks   | Initialize test data and connections | Async version: `[GlobalSetup(Target = "Setup")]`      |
| `[IterationSetup]`             | Runs before each iteration        | Reset state between runs             | Avoid heavy operations (affects measurement)          |
| `[HardwareCounters]`           | Collects CPU metrics              | Cache misses in geo-fencing          | `HardwareCounter.CacheMisses`, `BranchMispredictions` |
| `[DisassemblyDiagnoser]`       | Shows generated assembly code     | Analyze JIT output for SIMD          | `printSource: true, maxDepth: 5`                      |
| `[Orderer]`                    | Controls result ordering          | Fastest to slowest                   | `SummaryOrderPolicy.FastestToSlowest`                 |
| `[GroupBenchmarksBy]`          | Groups benchmarks in output       | By category                          | `BenchmarkLogicalGroupRule.ByCategory`                |
| `[ExceptionDiagnoser]`         | Tracks exception statistics       | Monitor timeouts under stress        | Shows exception counts per benchmark                  |
| `[TailCallDiagnoser]`          | Detects tail call optimizations   | Verify recursive method optimization | Helps with recursive parsing scenarios                |
| `[ThreadingDiagnoser]`         | Tracks thread pool statistics     | Monitor thread contention            | Shows thread count, pending work items                |
