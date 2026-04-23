# ### 3.3 CLS Compliance Detailed Rules Table

| Rule | Requirement | Example (Not Allowed) | Example (Allowed) |
|------|-------------|----------------------|-------------------|
| **2** | No unsigned identifiers | `public void Process(uint value)` | `public void Process(long value)` |
| **3** | No pointers | `public unsafe void Copy(int* src)` | `public void Copy(IntPtr src)` or `Span<int>` |
| **4** | No return-type-only overloads | `int Get() { return 1; }` and `string Get() { return ""; }` | Overload by parameters: `int Get(int x)` |
| **5** | No ref/out/array rank-only overloads | `void Process(ref int x)` and `void Process(out int x)` | Use different names: `ProcessByRef`, `ProcessByOut` |
| **6** | Public signature types CLS-compliant | `public void TakeMyStruct(MyNonCompliantStruct s)` | Use CLS-compliant wrapper |
| **10** | Generic variance rules | `interface I<out T> where T : struct` | `interface I<out T> where T : class` |
| **12** | Matching accessor visibility | `public int X { get; private set; }` | `public int X { get; }` or both public |
