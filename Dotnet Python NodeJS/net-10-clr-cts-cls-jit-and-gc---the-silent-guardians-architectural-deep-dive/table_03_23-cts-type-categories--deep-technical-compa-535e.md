# ### 2.3 CTS Type Categories — Deep Technical Compa

| Aspect | Value Types | Reference Types |
|--------|-------------|-----------------|
| **Memory location** | Stack (local variables) or inline within objects (fields) | GC Heap (managed heap) |
| **Default value** | Zero/null representation (0, 0.0, false, '\0') | `null` reference |
| **Assignment semantics** | Copy by value (entire content duplicated) | Copy by reference (pointer copied) |
| **Equality comparison** | Value equality by default (compare bits) | Reference equality by default (compare pointers) |
| **Inheritance** | Sealed (cannot derive from value types) | Open (can inherit unless sealed) |
| **Base type** | `System.ValueType` → `System.Object` | `System.Object` (or custom base class) |
| **Can be null** | No (unless `Nullable<T>` wrapper used) | Yes |
| **Boxing cost** | Required to treat as object (heap allocation) | No boxing needed |
| **GC pressure** | None (no GC allocation for locals) | Creates GC pressure |
| **Use case** | Small, immutable data, frequent allocation | Larger objects, polymorphic behavior |
