# **Circuit Breaker States:**

| State | Description | Behavior |
|-------|-------------|----------|
| **Closed** | Normal operation | Requests flow through, failures counted |
| **Open** | Service considered failed | All requests fail fast, no calls to service |
| **Half-Open** | Testing recovery | Limited requests allowed, success closes circuit |
