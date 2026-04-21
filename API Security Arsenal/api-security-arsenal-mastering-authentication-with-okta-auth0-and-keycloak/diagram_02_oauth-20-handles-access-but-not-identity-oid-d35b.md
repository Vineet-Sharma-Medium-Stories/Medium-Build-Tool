# OAuth 2.0 handles *access* but not *identity*. OID

```mermaid
flowchart LR
    subgraph OAuth [OAuth 2.0 Only]
        Access[Access Token] --> API[API Call]
        Note1["Knows: 'This token allows access'"]
        Note2["Does NOT know: 'Who is the user?'"]
    end
    
    subgraph OIDC [OAuth 2.0 + OIDC]
        Access2[Access Token] --> API2[API Call]
        ID[ID Token (JWT)] --> Client[Client App]
        Note3["ID Token contains: user_id, email, name, etc."]
    end
```
