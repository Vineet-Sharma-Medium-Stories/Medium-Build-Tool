# table_02_rate-limiting-algorithms


| Algorithm | Description | Pros | Cons |
|-----------|-------------|------|------|
| **Token Bucket** | Tokens replenish at fixed rate; requests consume tokens | Smooth traffic, handles bursts | Complex state tracking |
| **Leaky Bucket** | Requests processed at fixed rate; excess queued | Constant output rate | May queue requests |
| **Fixed Window** | Counts requests in fixed time windows | Simple, low overhead | Window boundary spikes |
| **Sliding Window** | Rolling time window counting | More accurate than fixed | Higher overhead |
| **Concurrency** | Limits concurrent requests | Prevents resource exhaustion | Doesn't limit total requests |
