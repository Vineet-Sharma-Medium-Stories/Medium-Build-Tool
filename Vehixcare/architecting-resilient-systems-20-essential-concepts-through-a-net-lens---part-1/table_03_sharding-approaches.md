# **Sharding Approaches:**

| Approach | Description | Pros | Cons |
|----------|-------------|------|------|
| **Range-Based** | Data partitioned by value ranges | Simple, efficient for range queries | Risk of hot spots |
| **Hash-Based** | Consistent hash distribution | Even distribution, no hot spots | Inefficient for range queries |
| **Directory-Based** | Lookup table for shard mapping | Flexible, easy to rebalance | Additional lookup overhead |
| **Geographic** | Partitioned by region | Data locality, compliance | Cross-region queries complex |
