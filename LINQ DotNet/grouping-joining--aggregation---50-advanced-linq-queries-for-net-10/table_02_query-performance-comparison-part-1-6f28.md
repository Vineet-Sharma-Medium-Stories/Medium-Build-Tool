# ## 📊 Query Performance Comparison (Part 1)

| Query | Legacy LoC | .NET 10 LoC | Reduction | Key Performance Gain |
|-------|------------|-------------|-----------|---------------------|
| Query 1: Multi-Key Grouping | 45 | 12 | 73% | Single-pass aggregation |
| Query 2: GroupJoin Hierarchy | 38 | 15 | 61% | Built-in hierarchical mapping |
| Query 3: Full Outer Join | 52 | 18 | 65% | Union + Distinct optimization |
| Query 4: Left Join | 35 | 14 | 60% | GroupJoin with DefaultIfEmpty |
| Query 5: Conditional Aggregation | 60 | 20 | 67% | Struct accumulator reduces GC |
| Query 6: Running Totals | 48 | 22 | 54% | Custom RunningAggregate extension |
| Query 7: Set Operations | 35 | 10 | 71% | HashSet intersection/except |
