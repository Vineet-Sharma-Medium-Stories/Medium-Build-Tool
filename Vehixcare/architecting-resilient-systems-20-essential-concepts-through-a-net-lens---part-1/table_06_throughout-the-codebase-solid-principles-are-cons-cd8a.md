# Throughout the codebase, SOLID principles are cons

| Principle | Implementation | Example |
|-----------|---------------|---------|
| **Single Responsibility** | Each class has one reason to change | `VehicleValidator`, `VehicleRepository`, `VehicleNotifier` separated |
| **Open/Closed** | Open for extension, closed for modification | `IVehicleServiceStrategy` with multiple implementations |
| **Liskov Substitution** | Derived classes can substitute base classes | `SqlVehicleRepository` and `MongoVehicleRepository` both implement `IVehicleRepository` |
| **Interface Segregation** | Segregated interfaces for specific needs | `IVehicleReader`, `IVehicleWriter`, `IVehicleSearcher` separate |
| **Dependency Inversion** | Depend on abstractions, not concretions | All services depend on interfaces, not concrete implementations |
