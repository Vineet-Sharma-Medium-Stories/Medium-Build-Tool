# ## Real-World Breach Examples and How These Tools 

| Breach | Year | Cause | Which Tool Would Have Helped |
|--------|------|-------|------------------------------|
| **Large Telecom** | 2022 | Unauthenticated API endpoint exposing customer data | API Gateway (auth enforcement) |
| **Ride-sharing Giant** | 2022 | Attacker found hardcoded credentials in internal scripts | Okta/Auth0 (MFA + credential rotation) |
| **Major Wireless Carrier** | 2023 | API enumeration attack exposing customer data | Salt Security (behavioral detection) |
| **Software Giant** | 2023 | Exposed test tenant with overly permissive OAuth | OWASP ZAP (pre-production scanning) |
| **Identity Provider** | 2023 | Service account with excessive privileges | Apigee (fine-grained authorization) |
