# ### Choosing the Right Loss Function

| Problem Type | Loss Function | Why |
|--------------|---------------|-----|
| Regression (normal errors) | MSE | Smooth, convex, penalizes large errors |
| Regression (outliers expected) | MAE or Huber | Robust to outliers |
| Binary Classification | Binary Cross-Entropy | Matches sigmoid output, probabilistic interpretation |
| Multi-class Classification | Categorical Cross-Entropy | Softmax + cross-entropy = natural fit |
| Imbalanced Classification | Weighted BCE | Gives more weight to minority class |
