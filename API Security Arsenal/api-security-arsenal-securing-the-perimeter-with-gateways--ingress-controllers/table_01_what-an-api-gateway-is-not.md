# **What an API gateway is NOT:**

| Misconception                                   | Reality                                                                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------ |
| "A gateway replaces my backend security"        | No — it adds a layer, but your backend must still validate everything                |
| "A gateway is just a load balancer"             | Load balancers distribute traffic; gateways enforce policies                         |
| "I can skip authentication if I have a gateway" | The gateway can *verify* auth, but your backend still needs to know *who* is calling |
| "One gateway fits all use cases"                | Different gateways excel at different things — choose carefully                      |
