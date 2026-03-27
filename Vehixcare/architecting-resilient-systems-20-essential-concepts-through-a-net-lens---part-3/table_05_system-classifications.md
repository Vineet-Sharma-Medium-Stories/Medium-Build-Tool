# table_05_system-classifications


| System Type | CP | AP | CA |
|-------------|----|----|-----|
| **Description** | Consistency + Partition Tolerance | Availability + Partition Tolerance | Consistency + Availability |
| **Characteristics** | Strong consistency, may be unavailable | Always available, may be stale | Consistent and available, can't handle partitions |
| **Examples** | MongoDB (with majority reads), Zookeeper | Cassandra, CouchDB, DynamoDB | Traditional SQL (single node) |
| **Use Cases** | Financial systems, inventory | Social media, user profiles | Internal applications |
