# **Partitioning Strategies:**

| Strategy | Description | Best For | Example |
|----------|-------------|----------|---------|
| **Range Partitioning** | Partition by value ranges | Time-series data, ordered keys | Service history by date |
| **Hash Partitioning** | Partition by hash of key | Even distribution, random access | User sessions by ID |
| **List Partitioning** | Partition by discrete values | Categorical data | Tenant data by region |
| **Composite Partitioning** | Multiple strategies combined | Complex query patterns | Date + tenant ID |
| **Round-Robin** | Sequential distribution | Simple load balancing | Log data |
