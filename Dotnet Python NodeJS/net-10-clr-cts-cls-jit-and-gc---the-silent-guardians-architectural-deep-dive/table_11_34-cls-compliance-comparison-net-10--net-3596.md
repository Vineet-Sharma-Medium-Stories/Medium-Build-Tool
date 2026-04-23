# ### 3.4 CLS Compliance Comparison (.NET 1.0 → .NET

| Feature | CLS Compliant? | .NET 1.0 | .NET 8 | .NET 10 | Notes |
|---------|---------------|----------|--------|---------|-------|
| `UInt32` parameters | ❌ No | Must hide | Must hide | Must hide | Use `Int64` with validation |
| `UInt32` return type | ❌ No | Must hide | Must hide | Must hide | Use `Int64` |
| `sbyte` (signed byte) | ❌ No | Must hide | Must hide | Must hide | Use `short` (Int16) |
| Function pointers | ❌ No | N/A | Not CLS | Not CLS | Use delegates for public API |
| Overloaded methods (diff params) | ✅ Yes | ✓ | ✓ | ✓ | Standard practice |
| Overloaded methods (diff return only) | ❌ No | ❌ | ❌ | ❌ | Compiler error |
| Case-sensitive names | ⚠️ Caution | ✓ | ✓ | ✓ + CA1014 | VB.NET is case-insensitive |
| Default interface methods | ⚠️ Depends | N/A | ✓ (C# 8+) | ✓ | Languages may not support |
| Generic covariance (`out T`) | ✅ Yes | ❌ No | ✓ (limited) | ✓ (full) | .NET 10 completes support |
| Generic contravariance (`in T`) | ✅ Yes | ❌ No | ✓ (limited) | ✓ (full) | .NET 10 completes support |
| `ref` returns | ❌ No | ❌ | ❌ | ❌ | Never CLS-compliant |
| `ref struct` | ❌ No | N/A | ❌ | ❌ | Can't be exposed publicly |
| `required` keyword (C# 11) | ✅ Yes | N/A | ✓ | ✓ | CLS-compliant, languages must support |
| `static abstract` interfaces | ✅ Yes | N/A | ✓ | ✓ | Generic math scenario |
