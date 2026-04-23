# **Core responsibilities of CTS:**

| Responsibility | Description | Example |
|----------------|-------------|---------|
| **Type definition** | Defines rules for visibility, inheritance, polymorphism, and encapsulation | `public`, `private`, `protected`, `internal` |
| **Type membership** | Specifies fields, methods, properties, events, and nested types | Properties with get/set accessors |
| **Type relationships** | Defines inheritance, implementation, and composition semantics | `class Dog : Animal, IBark` |
| **Type compatibility** | Establishes rules for implicit/explicit conversions, boxing, and unboxing | `int i = 42; object o = i;` (boxing) |
| **Cross-language integration** | Ensures a C# `int` is the same as a VB.NET `Integer` and F# `int` | `int` (C#) = `Integer` (VB.NET) = `int` (F#) = `System.Int32` (CTS) |
| **Type safety enforcement** | Prevents invalid casts, buffer overruns, and memory corruption | Runtime type checking on `as` and `is` operators |
| **Metadata generation** | Produces self-describing type information in assemblies | Reflection APIs, serialization, debugging |
