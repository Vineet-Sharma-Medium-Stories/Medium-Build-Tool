# table_06_distributed-system-patterns


| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Leader Election** | One node coordinates others | Raft, Paxos, ZooKeeper |
| **Distributed Lock** | Mutual exclusion across nodes | Redis Redlock, ZooKeeper |
| **Consensus** | Agreement on a value | Raft consensus algorithm |
| **Gossip Protocol** | Epidemic information propagation | Membership lists, failure detection |
| **Distributed Queue** | Shared work distribution | Kafka, RabbitMQ |
