# table_05_azure-messaging-options


| Service | Pattern | Max Size | Ordering | Exactly-Once | Best For |
| --- | --- | --- | --- | --- | --- |
| **Service Bus** | Queue/Topic | 256KB-100MB | Sessions | Via duplicate detection | Enterprise messaging, transactions |
| **Event Hubs** | Event stream | 1MB | Partition | At-least-once | Telemetry, event ingestion at scale |
| **Storage Queue** | Simple queue | 64KB | No | At-least-once | Simple, low-cost, large queues |
| **Event Grid** | Push events | 64KB | No | At-least-once | Reactive event routing, serverless |
