# **Performance characteristics on a laptop (16GB RA

| Metric | Value |
|--------|-------|
| Agent step latency | 3–5 seconds (includes LLM call) |
| Tool call latency | 50–200ms (depends on tool) |
| State checkpoint size | 10KB per step |
| Concurrent agents supported | 5–10 (limited by RAM) |
| Max steps before timeout | 50 (configurable) |
