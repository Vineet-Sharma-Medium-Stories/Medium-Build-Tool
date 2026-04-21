# **Flow comparison table:**

| Flow | Frontend | Backend | Refresh Tokens | PKCE Required | Use Case |
|------|----------|---------|----------------|---------------|----------|
| Authorization Code | No | Yes | Yes | No (but recommended) | Traditional web app |
| Auth Code + PKCE | Yes | Yes | Yes | Yes | SPA, mobile app |
| Implicit (deprecated) | Yes | No | No | N/A | ❌ Do not use |
| Client Credentials | No | Yes | Yes (opt-in) | N/A | Server-to-server |
| Device Code | No | No (polling) | Yes | N/A | Smart TV, CLI |
| Resource Owner Password | No | Yes | Yes | N/A | ❌ Do not use (legacy only) |
