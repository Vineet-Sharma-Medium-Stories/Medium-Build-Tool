# **Why .NET 10 for Spotify?**

| Requirement | .NET 10 Solution |
|-------------|------------------|
| Millions of concurrent streams | Native AOT, minimal GC pressure |
| Event-driven playback | System.Reactive, IObservable<T> |
| Async I/O operations | Task, IAsyncEnumerable, ValueTask |
| Database performance | EF Core 10, compiled queries |
| Thread-safe resource sharing | Channel<T>, ConcurrentDictionary |
| Resilient microservices | Polly, HttpClientFactory |
