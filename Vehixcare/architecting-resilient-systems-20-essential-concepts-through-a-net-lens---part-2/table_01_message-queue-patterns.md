# table_01_message-queue-patterns


| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Point-to-Point** | One producer, one consumer | Task distribution, work queues |
| **Publish-Subscribe** | One producer, multiple consumers | Event broadcasting, notifications |
| **Request-Reply** | Synchronous-like with async queues | RPC over message queues |
| **Competing Consumers** | Multiple consumers process same queue | Parallel processing, load balancing |
| **Dead Letter Queue** | Failed messages storage | Error handling, manual intervention |
