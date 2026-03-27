# table_01_load-balancing-algorithms


| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| Round Robin | Cycles through servers sequentially | Evenly distributed, similar-capacity servers |
| Least Connections | Directs traffic to server with fewest active connections | Long-lived connections, variable request duration |
| Least Time | Considers response time and connections | Performance-sensitive applications |
| IP Hash | Uses client IP to determine server | Session persistence without cookies |
| Consistent Hash | Maps requests to servers using hash ring | Cache-friendly distribution |
| Weighted | Assigns weights based on server capacity | Heterogeneous server infrastructure |
