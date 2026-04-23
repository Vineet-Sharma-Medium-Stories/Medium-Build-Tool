# ### 7.1 .NET 8 → .NET 10 Breaking Changes (Complet

| Area | .NET 8 Behavior | .NET 10 Behavior | Mitigation Strategy |
|------|----------------|------------------|---------------------|
| `BinaryFormatter` | Obsolete, throws | Removed completely | Migrate to `System.Text.Json` or `MessagePack` |
| `Half` arithmetic | Throws on overflow | Saturates (hardware) | Add explicit overflow checks with `checked` |
| P/Invoke defaults | `CharSet = Ansi` | `CharSet = Utf8` (faster) | Explicitly specify `CharSet` in `[DllImport]` |
| Unmanaged callers | Requires `UnmanagedCallersOnly` | Same + Native AOT-friendly | Use `[UnmanagedCallConv]` for calling conventions |
| `Assembly.CodeBase` | Obsolete | Removed | Use `Assembly.Location` or `Assembly.FullName` |
| `AppDomain` APIs | Partially working | Further restricted | Use `AssemblyLoadContext` for isolation |
| `GC.RegisterForFullGCNotification` | Works | Enhanced parameters | Update parameter values |
| `HttpClient` defaults | HTTP/1.1 | HTTP/2 (if supported) | Explicitly set `DefaultRequestVersion` |
| `Activity` API | Basic | Enhanced (OpenTelemetry) | Update to new activity tags |
| `TimeProvider` | ❌ | ✅ (C# 8/.NET 8) | Use for testable time |
| `JsonSerializer` source gen | Optional | Recommended default | Enable `JsonSourceGenerationOptions` |
