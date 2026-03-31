# **Cache Types:**

| Cache Type | Storage | Latency | Use Case |
|------------|---------|---------|----------|
| L1 (In-Memory) | RAM | Microseconds | Per-instance, frequently accessed data |
| L2 (Distributed) | Redis/Memcached | Milliseconds | Shared across instances, session data |
| L3 (Database) | Disk | 10-100ms | Persistent storage, authoritative source |
