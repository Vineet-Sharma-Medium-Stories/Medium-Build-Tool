# **Quantization methods explained:**

| Method | Bits | Memory (70B) | Accuracy loss | Use case |
|--------|------|--------------|---------------|----------|
| FP16 | 16 | 140GB | 0% | Impossible on laptop |
| Q8_0 | 8 | 70GB | 2–3% | High-end desktop with 64GB+ |
| Q5_K_M | 5 | 44GB | 4–5% | Desktop with 32GB RAM |
| Q4_K_M | 4 | 35GB (full) / 12GB (quantized weights only) | 5–7% | Laptop with 16GB RAM |
| Q4_K_S | 4 | 33GB | 7–9% | Laptop with 12GB RAM |
| IQ4_XS | 4 | 31GB | 8–10% | Older laptops |
