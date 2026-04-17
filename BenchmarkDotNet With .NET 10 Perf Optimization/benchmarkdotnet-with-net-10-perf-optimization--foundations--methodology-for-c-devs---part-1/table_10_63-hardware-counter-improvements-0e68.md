# ### 6.3 Hardware Counter Improvements

| Counter                   | Baseline | Optimized | Improvement   | What It Means               |
| ------------------------- | -------- | --------- | ------------- | --------------------------- |
| L1 Cache Miss Rate        | 15%      | 4%        | 73% reduction | Better data locality        |
| L2 Cache Miss Rate        | 32%      | 8%        | 75% reduction | Working set fits in L2      |
| Branch Misprediction Rate | 12%      | 3%        | 75% reduction | Predictable branching       |
| Instructions per Cycle    | 1.2      | 2.8       | 2.3x          | Better pipeline utilization |
| TLB Misses                | 5%       | 1%        | 80% reduction | Large page benefits         |
