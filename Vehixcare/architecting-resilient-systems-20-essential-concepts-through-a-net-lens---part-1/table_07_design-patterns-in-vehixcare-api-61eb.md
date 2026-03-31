# ### Design Patterns in Vehixcare-API

| Pattern | Implementation | Location | Benefit |
|---------|---------------|----------|---------|
| **Repository** | Data access abstraction | `VehicleRepository`, `MongoVehicleTelemetryRepository` | Decouples data access logic |
| **Unit of Work** | Transaction coordination | `IUnitOfWork`, `UnitOfWork` | Ensures transaction consistency |
| **Factory** | Object creation abstraction | `VehicleFactory`, `ServiceRequestFactory` | Centralizes object creation |
| **Strategy** | Algorithm selection | `IVehicleServiceStrategy`, `PricingStrategy` | Enables runtime algorithm switching |
| **Observer** | Event notification | `IEventPublisher`, `IEventSubscriber` | Loose coupling between components |
| **Decorator** | Behavior enhancement | `CachedVehicleRepository`, `LoggedVehicleRepository` | Adds behavior without modification |
| **Adapter** | Third-party integration | `PaymentGatewayAdapter`, `NotificationAdapter` | Integrates external services |
| **Facade** | Complex subsystem simplification | `VehicleServiceFacade` | Provides simplified interface |
| **Singleton** | Shared resource management | `MongoDbConnectionPool` | Controls resource usage |
| **Builder** | Complex object construction | `VehicleQueryBuilder`, `ServiceBookingBuilder` | Simplifies object creation |
| **Circuit Breaker** | Failure handling | `ResilientMongoServiceClient` | Prevents cascading failures |
| **Saga** | Distributed transactions | `ServiceBookingSaga` | Manages distributed consistency |
| **CQRS** | Command-Query separation | `VehicleCommandHandler`, `VehicleQueryHandler` | Separates reads from writes |
