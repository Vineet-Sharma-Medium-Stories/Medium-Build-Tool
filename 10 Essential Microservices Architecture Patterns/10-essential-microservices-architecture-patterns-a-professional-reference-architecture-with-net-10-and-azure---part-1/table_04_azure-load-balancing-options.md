# table_04_azure-load-balancing-options


| Option | Layer | Algorithm | Session Affinity | Global | WAF | SSL Offload |
| --- | --- | --- | --- | --- | --- | --- |
| **Azure Load Balancer** | L4 | Hash, Round Robin | Source IP | No | No | No |
| **Application Gateway** | L7 | Round Robin, Weighted | Cookie | No | Yes | Yes |
| **Azure Front Door** | L7 | Latency, Priority, Weighted | Cookie | Yes | Yes | Yes |
| **Traffic Manager** | DNS | Performance, Priority, Weighted | None | Yes | No | No |
| **Container Apps** | L7 | Automatic, weighted revisions | Auto | Regional | No | Yes |
