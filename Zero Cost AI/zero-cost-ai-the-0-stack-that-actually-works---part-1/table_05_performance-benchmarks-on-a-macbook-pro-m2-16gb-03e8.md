# **Performance benchmarks on a MacBook Pro M2 (16GB

| Operation | Time | Tokens/second |
|-----------|------|---------------|
| Model load (first call) | 8.2 seconds | N/A |
| Prompt processing (100 tokens) | 0.45 seconds | 222 tokens/sec |
| Generation (50 tokens) | 3.8 seconds | 13 tokens/sec |
| Generation (500 tokens) | 38 seconds | 13 tokens/sec |
| Batch inference (10 prompts) | 42 seconds | ~120 tokens/sec total |
