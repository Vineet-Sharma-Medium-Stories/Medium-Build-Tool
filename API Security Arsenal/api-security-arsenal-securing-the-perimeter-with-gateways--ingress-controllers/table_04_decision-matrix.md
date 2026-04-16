# **Decision matrix:**

| Consideration  | Use API Gateway      | Use Service Mesh       | Use Both                                |
| -------------- | -------------------- | ---------------------- | --------------------------------------- |
| Traffic source | External clients     | Internal services      | Both                                    |
| Authentication | OAuth, JWT, API keys | mTLS (SPIFFE)          | Gateway for external, mesh for internal |
| Rate limiting  | Client-based         | Service-based          | Both                                    |
| Observability  | Request/response     | Network-level          | Combined                                |
| Team maturity  | Ops-focused          | Platform-focused       | Large org                               |
| Example tools  | Kong, AWS Gateway    | Istio, Linkerd, Consul | Kong + Istio                            |
