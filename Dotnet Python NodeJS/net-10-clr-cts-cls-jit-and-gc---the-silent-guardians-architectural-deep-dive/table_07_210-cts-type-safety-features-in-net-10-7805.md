# ### 2.10 CTS Type Safety Features in .NET 10

| Safety Feature | .NET 1.0 | .NET 10 | Description |
|----------------|----------|---------|-------------|
| **Covariant arrays** | ✅ | ✅ | `string[]` to `object[]` (with runtime check) |
| **Type constraints** | ❌ | ✅ | `where T : class, new()` |
| **Generic variance** | ❌ | ✅ full | `IEnumerable<out T>`, `IComparer<in T>` |
| **NonNullable reference types** | ❌ | ✅ | `string?` vs `string` - compile-time null safety |
| **Required members** | ❌ | ✅ (C# 11) | `required int Id { get; init; }` |
| **Caller info attributes** | ❌ | ✅ | `[CallerMemberName]` for logging |
| **Disallow null for generics** | ❌ | ✅ | `where T : notnull` |
