# ### When to Use Which Metric

| Scenario | Best Metric | Why |
|----------|-------------|-----|
| Balanced classes | Accuracy | Simple, interpretable |
| Imbalanced classes | F1 Score | Balances precision and recall |
| Spam detection | Precision | False positives annoy users |
| Disease screening | Recall | False negatives risk lives |
| Ranking problems | ROC-AUC | Threshold-independent |
| Multi-class | Macro F1 | Averages across classes |
