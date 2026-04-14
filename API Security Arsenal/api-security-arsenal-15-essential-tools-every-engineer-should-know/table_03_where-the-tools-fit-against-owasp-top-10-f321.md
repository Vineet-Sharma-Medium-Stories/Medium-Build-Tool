# **Where the tools fit against OWASP Top 10:**

| OWASP Risk | Primary Defense Tools | Secondary Tools |
|------------|----------------------|------------------|
| Broken Object Level Authorization (API1) | Auth0, Okta, Keycloak | Burp Suite (testing) |
| Broken Authentication (API2) | Okta, Auth0, Keycloak | OWASP ZAP |
| Broken Object Property Level Authorization (API3) | Apigee, Salt Security | Postman |
| Unrestricted Resource Consumption (API4) | Kong, NGINX, AWS Gateway | Cloudflare |
| Broken Function Level Authorization (API5) | Okta, Auth0, Keycloak | Burp Suite |
| Unrestricted Access to Business Flows (API6) | Salt Security, Apigee | Cloudflare |
| Server Side Request Forgery (API7) | Cloudflare, AWS Gateway | OWASP ZAP |
| Security Misconfiguration (API8) | All gateways + testing tools | OWASP ZAP |
| Improper Inventory Management (API9) | Apigee, Kong, Tyk | Postman |
| Unsafe Consumption of APIs (API10) | OWASP ZAP, Burp Suite | Salt Security |
