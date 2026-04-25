# **React Native vs Web Differences**:

| Aspect | Web (EventSource) | React Native (Custom fetch) |
|--------|-------------------|-------------------------------|
| Auto-reconnect | Built-in | Manual with exponential backoff |
| Last-Event-ID | Automatic | Must store & send custom header |
| Connection limit | 6 per domain | No hard limit (device-specific) |
| Background behavior | Tab inactive throttles | Requires native module |
