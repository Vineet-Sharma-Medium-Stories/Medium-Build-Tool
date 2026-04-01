# ### Common Data Cleaning Challenges and Strategies

| Challenge | What It Reveals | Strategic Approach |
|-----------|-----------------|---------------------|
| **Missing values** | Data collection issues, user behavior, system failures | Don't just drop. Understand why. Is it random? Systematic? Does it correlate with outcomes? |
| **Outliers** | Edge cases, measurement errors, real but rare events | Investigate before removing. Outliers often contain the most interesting insights. |
| **Duplicate records** | System logging issues, data entry errors | Deduplication strategy depends on domain. One user, multiple sessions? Keep context. |
| **Inconsistent formats** | Multiple data sources, poor validation | Standardize early. Document your assumptions. Future you will thank you. |
| **Imbalanced classes** | Rare events are actually rare | Balance carefully. Sometimes imbalance is the signal, not the problem. |
