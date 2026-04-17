# ### Canary Deployment Checklist

| Phase            | Duration | Success Criteria                           | Rollback Trigger                             |
| ---------------- | -------- | ------------------------------------------ | -------------------------------------------- |
| **5% canary**    | 24 hours | Error rate < 0.1%, latency < baseline +10% | Error rate > 0.5% or latency > baseline +50% |
| **25% canary**   | 24 hours | CPU < 70%, memory < 80%                    | CPU > 85% or memory > 90%                    |
| **50% canary**   | 24 hours | GC pause < 100ms, throughput > baseline    | GC pause > 500ms                             |
| **100% rollout** | -        | All metrics stable for 1 week              | Any regression > 20%                         |
