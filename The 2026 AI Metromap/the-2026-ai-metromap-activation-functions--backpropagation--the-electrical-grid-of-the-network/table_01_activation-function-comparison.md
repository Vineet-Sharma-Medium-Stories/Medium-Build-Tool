# ### Activation Function Comparison

| Function | Range | Derivative | Pros | Cons |
|----------|-------|------------|------|------|
| **Sigmoid** | (0, 1) | σ(z)(1-σ(z)) | Smooth, probabilistic | Vanishing gradients, not zero-centered |
| **Tanh** | (-1, 1) | 1 - tanh²(z) | Zero-centered | Still vanishing gradients |
| **ReLU** | [0, ∞) | 0 if z<0, 1 if z>0 | Fast, no vanishing | Dying ReLU (neurons die) |
| **Leaky ReLU** | (-∞, ∞) | α if z<0, 1 if z>0 | Fixes dying ReLU | Extra parameter |
| **Swish** | (-∞, ∞) | σ(z) + z·σ(z)(1-σ(z)) | Smooth, non-monotonic | More computation |
| **GELU** | (-∞, ∞) | Complex | Used in Transformers | Complex derivative |
