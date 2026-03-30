# ### Performance Characteristics

| Metric | .NET SDK Native | .NET Docker | Poetry | UV | npm | pnpm |
|--------|-----------------|-------------|--------|-----|-----|------|
| **Build Time** | 45s | 85s | 60s | 15s | 60s | 45s |
| **Image Size** | 78 MB | 198 MB | 350 MB | 350 MB | 300 MB | 200 MB |
| **Startup Time** | 95ms | 185ms | 2-3s | 2-3s | 1-2s | 1-2s |
| **Dependency Resolution** | Built-in | N/A | Deterministic | Deterministic | Non-deterministic | Deterministic |
