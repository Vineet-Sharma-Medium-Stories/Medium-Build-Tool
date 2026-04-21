# ## Real-World Breach Examples and Lessons

| Breach | Year | Cause | Lesson | Prevention |
|--------|------|-------|--------|------------|
| **Uber** | 2022 | Hardcoded service account credentials in PowerShell scripts | Never hardcode credentials. Rotate service account keys. | Use workload identity (AWS IAM, GCP Workload Identity) |
| **Okta** | 2023 | Service account with excessive privileges | Least privilege applies to service accounts too. | Regular privilege audits. Short-lived tokens. |
| **Microsoft** | 2023 | Test tenant with overly permissive OAuth | Staging/production separation is critical. | Separate IdP tenants for staging. Different audiences. |
| **Ride-sharing co** | 2022 | JWT accepted without audience validation | Validate every claim. | Always validate `aud`, `iss`, `exp`. |
| **Social media co** | 2021 | API key leak in mobile app binary | API keys in client apps cannot be kept secret. | Use OAuth with PKCE, not API keys. |
