# ### 1.3 Telemetry Processing Sequence Diagram

```mermaid
---
config:
  theme: base
  layout: elk
---
sequenceDiagram
    participant V as Vehicle Device
    participant API as Telemetry API Pod
    participant TS as Telemetry Service<br/>(Rx.NET Pipeline)
    participant DB as Cosmos DB MongoDB
    participant EG as Azure Event Grid
    participant SH as SignalR Hub
    participant C as Client Dashboard

    V->>API: POST /api/vehicles/{id}/telemetry
    API->>API: Validate JWT + Organization scope
    API->>API: Check rate limits (1000 req/sec)
    API->>TS: IngestTelemetryAsync(telemetry)
    
    TS->>TS: Rx.NET - Buffer(TimeSpan.FromSeconds(5))
    TS->>TS: Rx.NET - Throttle burst telemetry
    TS->>DB: Store raw telemetry (TripLogs collection)
    TS->>DB: Update vehicle status (Vehicles collection)
    
    par Parallel Processing
        TS->>TS: Driver Behavior Scoring
        TS->>DB: Update driver behavior score
        TS->>SH: Broadcast behavior alert
    and
        TS->>TS: Geo-fence Boundary Check
        TS->>DB: Query active geo-fences (2dsphere index)
        TS->>SH: Broadcast entry/exit event
    and
        TS->>TS: Anti-theft Detection
        TS->>DB: Check unauthorized movement pattern
        TS->>SH: Broadcast theft alert
    and
        TS->>EG: Publish telemetry event
        EG->>EG: Filter to subscribed services
        EG->>EG: Retry policy (3 attempts, exponential backoff)
    end
    
    TS->>SH: Broadcast TelemetryUpdate
    SH->>C: SignalR push - Real-time telemetry
    C->>C: Update dashboard UI
```
