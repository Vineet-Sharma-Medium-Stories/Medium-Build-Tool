# Every CTS type can contain the following member ty

| Member Type | Description | Accessibility Modifiers | .NET 10 Enhancement |
|-------------|-------------|------------------------|---------------------|
| **Fields** | Data storage within type | `public`, `private`, `protected`, `internal`, `protected internal`, `private protected` | `ref` fields (ref structs) |
| **Constants** | Compile-time immutable values | `public const int Max = 100;` | Improved interop with `StringSyntaxAttribute` |
| **Properties** | Get/set accessors with logic | Same as fields | `field` keyword contextual (C# 13 preview) |
| **Methods** | Executable code blocks | Same as fields + `virtual`, `abstract`, `override`, `sealed override` | Generic math constraints |
| **Constructors** | Instance initialization | `public`, `private`, `protected`, `internal`, `static` | Primary constructors (C# 12) |
| **Events** | Notification mechanism | `public event EventHandler Clicked;` | Improved event source generation |
| **Indexers** | Array-like access | `public T this[int index] { get; set; }` | `ref` returning indexers |
| **Operators** | Type-specific operations | `public static T operator +(T a, T b)` | Generic math operators |
| **Conversions** | Implicit/explicit conversion | `public static implicit operator T(U value)` | User-defined checked operators |
| **Nested types** | Types within types | All accessibility levels | Improved static nested type analysis |
| **Finalizers** | Cleanup before GC (not recommended) | `~ClassName()` | Not enhanced (use `SafeHandle`) |
