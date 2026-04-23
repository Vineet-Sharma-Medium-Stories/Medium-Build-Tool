# ### 6.2 Performance Benchmark Complete Table (.NET

```mermaid
---
config:
  theme: base
  layout: elk
---
xychart-beta
    title "Relative Performance Improvement (Higher = Better) .NET 1.0 = 1.0x"
    x-axis ["Math ops", "String concat", "Array sum", "Object alloc", "Exception throw", "Native interop", "Dictionary lookup", "Reflection call"]
    y-axis "Relative Speed" 0 to 14
    line [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    line [5.2, 3.8, 6.1, 4.2, 2.5, 3.5, 4.8, 2.2]
    line [8.4, 5.9, 9.7, 6.8, 3.9, 8.2, 7.1, 3.5]
```
