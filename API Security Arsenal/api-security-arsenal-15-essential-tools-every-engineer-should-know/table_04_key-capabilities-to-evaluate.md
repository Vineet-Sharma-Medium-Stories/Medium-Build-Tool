# **Key capabilities to evaluate:**

| Capability | Why It Matters | Example Use Case |
|------------|----------------|-------------------|
| Rate limiting | Prevents DDoS and brute force | 100 requests per minute per API key |
| Request validation | Blocks malformed payloads | Reject JSON with unexpected fields |
| IP whitelisting/blacklisting | Restricts access by geography or threat intel | Block traffic from known malicious IP ranges |
| Request/response transformation | Hides internal implementation details | Remove `X-Internal-Server` headers |
| Analytics and logging | Provides visibility into API usage | Track error rates by endpoint |
