# **CloudWatch Alarm configuration:**

| Alarm                 | Condition                      | Action                |
| --------------------- | ------------------------------ | --------------------- |
| OutboxLagHigh         | > 10,000 records for 5 minutes | Page on-call engineer |
| OutboxAgeHigh         | > 300 seconds                  | Page on-call engineer |
| DebeziumConnectorDown | Connector status = FAILED      | Page on-call engineer |
