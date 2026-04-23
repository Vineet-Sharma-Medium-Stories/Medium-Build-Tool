# All CTS primitive types map directly to .NET Frame

| CTS Type (Full Name) | C# Alias | VB.NET Alias | F# Alias | Size (bytes) | Range / Precision | .NET 10 Notes |
|---------------------|----------|--------------|----------|--------------|-------------------|---------------|
| `System.Boolean` | `bool` | `Boolean` | `bool` | 1 (actual), 4 (stack) | `true` / `false` | Atomic operations guaranteed |
| `System.Byte` | `byte` | `Byte` | `byte` | 1 | 0 to 255 | Stack allocation optimization |
| `System.SByte` | `sbyte` | `SByte` | `sbyte` | 1 | -128 to 127 | CLS non-compliant |
| `System.Char` | `char` | `Char` | `char` | 2 | U+0000 to U+FFFF (UTF-16) | Unicode 15.0 support |
| `System.Int16` | `short` | `Short` | `int16` | 2 | -32,768 to 32,767 | Fast signed operations |
| `System.UInt16` | `ushort` | `UShort` | `uint16` | 2 | 0 to 65,535 | CLS non-compliant |
| `System.Int32` | `int` | `Integer` | `int` | 4 | -2.1B to 2.1B | Most efficient integer size |
| `System.UInt32` | `uint` | `UInteger` | `uint32` | 4 | 0 to 4.2B | CLS non-compliant |
| `System.Int64` | `long` | `Long` | `int64` | 8 | -9.2 quintillion to 9.2 quintillion | Hardware accelerated on x64 |
| `System.UInt64` | `ulong` | `ULong` | `uint64` | 8 | 0 to 18.4 quintillion | CLS non-compliant |
| `System.Int128` | `Int128` | `Int128` | `int128` | 16 | ±1.7e38 | **New in .NET 10** - Hardware accelerated on x64 with `MUL` instruction |
| `System.UInt128` | `UInt128` | `UInt128` | `uint128` | 16 | 0 to 3.4e38 | **New in .NET 10** |
| `System.Half` | `Half` | `Half` | `half` | 2 | ±65504, precision ~3.3 digits | **Enhanced in .NET 10** - Full hardware acceleration on AVX-512 |
| `System.Single` | `float` | `Single` | `float32` | 4 | ±3.4e38, precision ~7 digits | IEEE 754 compliant |
| `System.Double` | `double` | `Double` | `float` | 8 | ±1.7e308, precision ~15 digits | Hardware accelerated |
| `System.Decimal` | `decimal` | `Decimal` | `decimal` | 16 | ±7.9e28, precision 28-29 digits | Financial calculations, not hardware accelerated |
| `System.IntPtr` | `nint` | `IntPtr` | `nativeint` | 4/8 (platform) | Platform-dependent | Native integer - improved marshaling in .NET 10 |
| `System.UIntPtr` | `nuint` | `UIntPtr` | `unativeint` | 4/8 (platform) | Platform-dependent | CLS non-compliant |
