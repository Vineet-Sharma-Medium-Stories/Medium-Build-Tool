# ### Azure Implementation Options

| Option | Best For | Scaling | Cost Model | Features |
| --- | --- | --- | --- | --- |
| **Azure API Management** | Enterprise APIs with developer portal | Auto-scale with premium tier | Consumption/Developer/Standard/Premium | Developer portal, analytics, policies, caching |
| **Azure Application Gateway** | Layer 7 load balancing + WAF | Auto-scaling available | Per hour + data processed | WAF, SSL termination, cookie affinity |
| **Azure Front Door** | Global HTTP load balancing | Global auto-scaling | Per request + outbound data | Global routing, acceleration, CDN |
| **Custom YARP in App Service** | Full control, simple needs | App Service scaling | App Service cost only | Full code control, customization |
