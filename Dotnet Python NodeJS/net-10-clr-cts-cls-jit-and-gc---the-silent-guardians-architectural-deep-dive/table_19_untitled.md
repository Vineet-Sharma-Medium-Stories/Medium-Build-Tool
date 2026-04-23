# ```

| Benchmark Category | .NET 1.0 | .NET 8 | .NET 10 | .NET 10 / .NET 1.0 |
|--------------------|----------|--------|---------|---------------------|
| Integer arithmetic (ops/ms) | 10M | 52M | 84M | **8.4x** |
| String concatenation (ops/ms) | 1M | 3.8M | 5.9M | **5.9x** |
| Array sum (elements/ms) | 20M | 122M | 194M | **9.7x** |
| Object allocation (alloc/ms) | 0.5M | 2.1M | 3.4M | **6.8x** |
| Exception throw/catch (ops/ms) | 0.05M | 0.125M | 0.195M | **3.9x** |
| P/Invoke call (calls/ms) | 0.8M | 2.8M | 6.6M (POH) | **8.25x** |
| Dictionary lookup (ops/ms) | 3M | 14.4M | 21.3M | **7.1x** |
| Reflection property get (ops/ms) | 0.15M | 0.33M | 0.525M | **3.5x** |
| Async task creation (tasks/ms) | N/A | 0.8M | 1.6M (ValueTask) | **2x vs .NET 8** |
| LINQ over array (ops/ms) | N/A | 8M | 15M | **1.9x vs .NET 8** |
