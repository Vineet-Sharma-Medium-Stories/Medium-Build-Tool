# **JWT validation checklist (for your API):**

| Validation Step | Why It Matters | If Missing |
|----------------|----------------|------------|
| Verify signature | Token wasn't tampered with | Attacker can forge tokens |
| Check expiration (`exp`) | Token isn't expired | Stolen tokens work forever |
| Verify issuer (`iss`) | Token came from your IdP | Attackers can use their own tokens |
| Check audience (`aud`) | Token is meant for your API | Token meant for other service works |
| Validate not-before (`nbf`) | Token isn't active yet | Clock skew attacks |
| Check revocation | Token wasn't explicitly revoked | Compromised tokens remain valid |
