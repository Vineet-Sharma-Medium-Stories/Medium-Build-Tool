# ### Behavioral Patterns (Object Interaction)

| Pattern | Purpose | Spotify Example | .NET 10 Feature |
|---------|---------|-----------------|-----------------|
| **Observer** | One-to-many notifications | UI updates on playback | IObservable<T> |
| **Strategy** | Interchangeable algorithms | Recommendation algorithms | Strategy interface |
| **Command** | Encapsulate requests | User actions + Undo | Channel<T> + MediatR |
| **State** | State-dependent behavior | Player states | State pattern + State machine |
| **Chain of Resp.** | Request processing pipeline | Playback validation | Middleware pipeline |
| **Template Method** | Algorithm skeleton | Playlist generation | Abstract base |
| **Visitor** | Operations on object structures | Analytics reports | Double dispatch |
