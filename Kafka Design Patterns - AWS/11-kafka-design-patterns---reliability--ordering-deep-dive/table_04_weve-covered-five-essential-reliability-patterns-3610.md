# We've covered five essential reliability patterns 

| Pattern                      | Problem Solved                                    | AWS Services                                       |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Transactional Outbox**     | Dual-write inconsistency between DB and Kafka     | RDS/Aurora + MSK Connect (Debezium) or Lambda      |
| **Idempotent Consumer**      | Duplicate messages causing duplicate side effects | DynamoDB (conditional writes) or ElastiCache Redis |
| **Partition Key / Ordering** | Out-of-order event processing                     | MSK with high-cardinality keys                     |
| **Dead Letter Queue**        | Poison messages blocking processing               | MSK (DLQ topics) + CloudWatch alarms               |
| **Retry with Backoff**       | Transient failures causing data loss              | MSK (retry topics) or SQS redrive policies         |
