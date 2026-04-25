# ## Chapter 8: Common Pitfalls & Fixes

| Problem | Solution |
|---------|----------|
| Connection drops after 60s | Set `Response.Headers["Keep-Alive"] = "timeout=120"` and handle client reconnects via `Last-Event-ID` |
| Memory grows unbounded | Use bounded channel with `DropOldest` |
| Browser shows "pending" forever | Send a dummy `: heartbeat\n\n` comment every 30s |
| .NET 10 preview bug: `SseResult` doesn’t flush | Workaround: `await Response.WriteAsync(": keepalive\n\n"); await Response.Body.FlushAsync();` |
| React Native fetch stream hangs on Android | Add `react-native-fetch-blob` polyfill or use `XMLHttpRequest` |
| Mobile app consumes too much data | Compress SSE payloads with gzip (`.NET 10` native compression) |
