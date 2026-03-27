# Architecting Resilient Systems: 20 Essential Concepts Through a .NET Lens - Part 2

## Distribution & Communication — Consistent Hashing, Message Queues, Rate Limiting, API Gateway, Microservices Architecture


![alt text](<https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/Part 2: Distribution & Communication — Consistent Hashing, Message Queues, Rate Limiting, API.png>)


*This is Part 2 of a 4-part series exploring system design concepts through the Vehixcare-API implementation. In this series, we'll cover 20 essential distributed system patterns with practical .NET code examples, MongoDB integration, and SOLID principles.*


**Companion stories in this series: Explore the complete architecture journey**

- **[🏗️ Part 1:** *Foundation & Resilience – Load Balancing, Caching, Database Sharding, Replication, Circuit Breaker* ](#)** 

- **📡 Part 2:** *Distribution & Communication – Consistent Hashing, Message Queues, Rate Limiting, API Gateway, Microservices* *(Current)* 

- **🏛️ Part 3:** *Architecture & Scale – Monolithic Architecture, Event-Driven Architecture, CAP Theorem, Distributed Systems, Horizontal Scaling*

- **⚙️ Part 4:** *Optimization & Operations – Vertical Scaling, Data Partitioning, Idempotency, Service Discovery, Observability *

---

## Introduction: Connecting the Distributed World

In Part 1, we established the foundation of distributed systems with load balancing, caching, sharding, replication, and circuit breakers. Now, we move to the critical layer that enables services to communicate effectively, scale independently, and handle complex distributed workflows.

In this part, we'll explore how Vehixcare manages:
- **Data distribution** across nodes with consistent hashing
- **Asynchronous communication** using message queues for decoupled service interactions
- **Traffic control** with rate limiting to protect system resources
- **Unified access** through API Gateway for all client applications
- **Service decomposition** using microservices architecture for independent scalability

---

## Concept 6: Consistent Hashing — Distributing Data Evenly Across Nodes

![alt text](<https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/Consistent Hashing.png>)

Consistent hashing minimizes rebalancing when nodes are added or removed from a distributed system. This makes it ideal for cache distribution, database sharding, and load balancing where node membership changes dynamically.

### Deep Dive into Consistent Hashing

**The Problem with Traditional Hashing:**
- Traditional hash-based distribution (hash(key) % N) causes massive redistribution when N changes
- Adding or removing a node can require moving up to 1/N of all keys
- For caches, this can cause cache stampede and database overload

**How Consistent Hashing Solves This:**
- Maps both nodes and keys to the same hash ring (0 to 2^64 - 1)
- Keys are assigned to the first node clockwise from their hash position
- Adding a node only requires redistributing keys from its immediate neighbor
- Typically only about 1/N of keys need to move when N changes

**Virtual Nodes:**
- Physical nodes are represented by multiple virtual nodes on the ring
- Ensures even distribution when nodes have different capacities
- Provides better load balancing with fewer data movements

### Vehixcare Consistent Hashing Implementation

```csharp
// 1. Core consistent hash ring implementation
public class ConsistentHashRing<TNode> where TNode : class
{
    private readonly SortedDictionary<ulong, TNode> _ring;
    private readonly Dictionary<TNode, List<ulong>> _nodeHashes;
    private readonly int _virtualNodes;
    private readonly IHashAlgorithm _hashAlgorithm;
    private readonly ReaderWriterLockSlim _lock;
    private readonly ILogger<ConsistentHashRing<TNode>> _logger;
    
    public ConsistentHashRing(int virtualNodes = 150, IHashAlgorithm hashAlgorithm = null)
    {
        _virtualNodes = virtualNodes;
        _hashAlgorithm = hashAlgorithm ?? new MurmurHash3();
        _ring = new SortedDictionary<ulong, TNode>();
        _nodeHashes = new Dictionary<TNode, List<ulong>>();
        _lock = new ReaderWriterLockSlim();
        _logger = LoggerFactory.Create(b => b.AddConsole()).CreateLogger<ConsistentHashRing<TNode>>();
    }
    
    // Add a node to the hash ring with virtual nodes
    public void AddNode(TNode node)
    {
        _lock.EnterWriteLock();
        try
        {
            if (_nodeHashes.ContainsKey(node))
                throw new ArgumentException("Node already exists in the ring");
            
            var hashes = new List<ulong>();
            
            for (int i = 0; i < _virtualNodes; i++)
            {
                // Create virtual node identifier
                var virtualNodeKey = $"{node.GetHashCode()}-vnode-{i}";
                var hash = _hashAlgorithm.ComputeHash(virtualNodeKey);
                
                _ring[hash] = node;
                hashes.Add(hash);
            }
            
            _nodeHashes[node] = hashes;
            
            _logger.LogInformation("Added node {Node} with {VirtualNodes} virtual nodes", 
                node.ToString(), _virtualNodes);
        }
        finally
        {
            _lock.ExitWriteLock();
        }
    }
    
    // Remove a node from the hash ring
    public void RemoveNode(TNode node)
    {
        _lock.EnterWriteLock();
        try
        {
            if (!_nodeHashes.TryGetValue(node, out var hashes))
                return;
            
            foreach (var hash in hashes)
            {
                _ring.Remove(hash);
            }
            
            _nodeHashes.Remove(node);
            
            _logger.LogInformation("Removed node {Node}", node.ToString());
        }
        finally
        {
            _lock.ExitWriteLock();
        }
    }
    
    // Get the node responsible for a key
    public TNode GetNode(string key)
    {
        _lock.EnterReadLock();
        try
        {
            if (!_ring.Any())
                throw new InvalidOperationException("No nodes in hash ring");
            
            var hash = _hashAlgorithm.ComputeHash(key);
            
            // Find the first node with hash >= key hash
            // Binary search for O(log n) performance
            var node = FindFirstNodeWithHashGreaterOrEqual(hash);
            
            return node;
        }
        finally
        {
            _lock.ExitReadLock();
        }
    }
    
    // Binary search for efficient node lookup
    private TNode FindFirstNodeWithHashGreaterOrEqual(ulong hash)
    {
        var keys = _ring.Keys.ToList();
        var index = BinarySearch(keys, hash);
        
        if (index >= keys.Count)
        {
            // Wrap around to first node
            return _ring[keys[0]];
        }
        
        return _ring[keys[index]];
    }
    
    private int BinarySearch(List<ulong> sortedKeys, ulong target)
    {
        int left = 0;
        int right = sortedKeys.Count - 1;
        
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            
            if (sortedKeys[mid] == target)
                return mid;
            
            if (sortedKeys[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        
        return left;
    }
    
    // Get all nodes (useful for debugging)
    public IEnumerable<TNode> GetAllNodes()
    {
        _lock.EnterReadLock();
        try
        {
            return _nodeHashes.Keys.ToList();
        }
        finally
        {
            _lock.ExitReadLock();
        }
    }
    
    // Get distribution statistics
    public Dictionary<TNode, int> GetDistribution(IEnumerable<string> keys)
    {
        _lock.EnterReadLock();
        try
        {
            var distribution = new Dictionary<TNode, int>();
            
            foreach (var key in keys)
            {
                var node = GetNode(key);
                distribution[node] = distribution.GetValueOrDefault(node, 0) + 1;
            }
            
            return distribution;
        }
        finally
        {
            _lock.ExitReadLock();
        }
    }
}
```
**MurmurHash3 implementation for high-performance hashing**
```csharp
// 2. MurmurHash3 implementation for high-performance hashing
public interface IHashAlgorithm
{
    ulong ComputeHash(string input);
    ulong ComputeHash(byte[] input);
}

public class MurmurHash3 : IHashAlgorithm
{
    private const uint Seed = 0x9747b28c;
    
    public ulong ComputeHash(string input)
    {
        return ComputeHash(Encoding.UTF8.GetBytes(input));
    }
    
    public ulong ComputeHash(byte[] input)
    {
        const uint c1 = 0xcc9e2d51;
        const uint c2 = 0x1b873593;
        const int r1 = 15;
        const int r2 = 13;
        const uint m = 5;
        const uint n = 0xe6546b64;
        
        int length = input.Length;
        int remainder = length % 4;
        int blocks = length / 4;
        
        uint h1 = Seed;
        
        // Process 4-byte blocks
        for (int i = 0; i < blocks; i++)
        {
            uint k1 = BitConverter.ToUInt32(input, i * 4);
            
            k1 *= c1;
            k1 = RotateLeft(k1, r1);
            k1 *= c2;
            
            h1 ^= k1;
            h1 = RotateLeft(h1, r2);
            h1 = h1 * m + n;
        }
        
        // Process remaining bytes
        if (remainder > 0)
        {
            uint k1 = 0;
            for (int i = 0; i < remainder; i++)
            {
                k1 |= (uint)input[blocks * 4 + i] << (i * 8);
            }
            
            k1 *= c1;
            k1 = RotateLeft(k1, r1);
            k1 *= c2;
            
            h1 ^= k1;
        }
        
        // Finalization
        h1 ^= (uint)length;
        h1 = FinalizeMix(h1);
        
        // Combine two 32-bit hashes into 64-bit for larger key space
        uint h2 = FinalizeMix(h1 ^ Seed);
        
        return ((ulong)h1 << 32) | h2;
    }
    
    private static uint RotateLeft(uint x, int r)
    {
        return (x << r) | (x >> (32 - r));
    }
    
    private static uint FinalizeMix(uint h)
    {
        h ^= h >> 16;
        h *= 0x85ebca6b;
        h ^= h >> 13;
        h *= 0xc2b2ae35;
        h ^= h >> 16;
        
        return h;
    }
}

```
**Jump Consistent Hash implementation for even better distribution**
```csharp
// 3. Jump Consistent Hash implementation for even better distribution
public class JumpConsistentHash : IHashAlgorithm
{
    public ulong ComputeHash(string input)
    {
        return ComputeHash(Encoding.UTF8.GetBytes(input));
    }
    
    public ulong ComputeHash(byte[] input)
    {
        // Use xxHash for initial 64-bit hash
        var xxHash = new System.IO.Hashing.XxHash64();
        xxHash.Append(input);
        var hash = xxHash.GetCurrentHashAsUInt64();
        
        return hash;
    }
    
    // Jump consistent hash algorithm - O(log n) time, O(1) space
    public int GetBucket(ulong key, int numBuckets)
    {
        long b = -1;
        long j = 0;
        
        while (j < numBuckets)
        {
            b = j;
            key = key * 2862933555777941757UL + 1;
            j = (long)((b + 1) * ((double)(1L << 31) / (double)((key >> 33) + 1)));
        }
        
        return (int)b;
    }
}

```
**Consistent hash cache sharding for Redis cluster**
```csharp
// 4. Consistent hash cache sharding for Redis cluster
public class ConsistentHashCacheShard : ICacheShard
{
    private readonly ConsistentHashRing<string> _hashRing;
    private readonly Dictionary<string, IDistributedCache> _cacheInstances;
    private readonly ILogger<ConsistentHashCacheShard> _logger;
    
    public ConsistentHashCacheShard(ILogger<ConsistentHashCacheShard> logger)
    {
        _hashRing = new ConsistentHashRing<string>(virtualNodes: 150);
        _cacheInstances = new Dictionary<string, IDistributedCache>();
        _logger = logger;
    }
    
    public void RegisterCacheNode(string nodeId, IDistributedCache cache, int weight = 1)
    {
        // For weighted nodes, add more virtual nodes
        var virtualNodes = 150 * weight;
        _hashRing.AddNode(nodeId);
        _cacheInstances[nodeId] = cache;
        
        _logger.LogInformation("Registered cache node {NodeId} with weight {Weight}", nodeId, weight);
    }
    
    public void RemoveCacheNode(string nodeId)
    {
        _hashRing.RemoveNode(nodeId);
        _cacheInstances.Remove(nodeId);
        
        _logger.LogInformation("Removed cache node {NodeId}", nodeId);
    }
    
    public IDistributedCache GetCacheForKey(string key)
    {
        var nodeId = _hashRing.GetNode(key);
        return _cacheInstances[nodeId];
    }
    
    public async Task<T> GetOrAddAsync<T>(
        string key, 
        Func<Task<T>> factory, 
        TimeSpan? expiry = null, 
        CancellationToken ct = default)
    {
        var cache = GetCacheForKey(key);
        
        // Try to get from cache
        var cachedValue = await cache.GetStringAsync(key, ct);
        if (cachedValue != null)
        {
            return JsonSerializer.Deserialize<T>(cachedValue);
        }
        
        // Cache miss - execute factory
        var value = await factory();
        
        // Store in cache
        var serialized = JsonSerializer.Serialize(value);
        var options = new DistributedCacheEntryOptions
        {
            AbsoluteExpirationRelativeToNow = expiry ?? TimeSpan.FromMinutes(30)
        };
        
        await cache.SetStringAsync(key, serialized, options, ct);
        
        return value;
    }
    
    // Rebalance when nodes are added or removed
    public async Task RebalanceAsync(CancellationToken ct)
    {
        _logger.LogInformation("Starting cache rebalance");
        
        // Get all existing keys (this would need a way to enumerate keys across all nodes)
        // For production, you'd use Redis SCAN or similar
        
        // Re-distribute keys according to new ring
        // Keys that move to new nodes would need to be migrated
        
        _logger.LogInformation("Cache rebalance completed");
    }
}

```
**Consistent hash load balancer for service instances**
```csharp
// 5. Consistent hash load balancer for service instances
public class ConsistentHashLoadBalancer : ILoadBalancer
{
    private readonly ConsistentHashRing<ServiceInstance> _hashRing;
    private readonly ILogger<ConsistentHashLoadBalancer> _logger;
    
    public ConsistentHashLoadBalancer(ILogger<ConsistentHashLoadBalancer> logger)
    {
        _hashRing = new ConsistentHashRing<ServiceInstance>(virtualNodes: 100);
        _logger = logger;
    }
    
    public void AddInstance(ServiceInstance instance)
    {
        _hashRing.AddNode(instance);
        _logger.LogInformation("Added service instance {InstanceId} at {Address}", 
            instance.Id, instance.Address);
    }
    
    public void RemoveInstance(ServiceInstance instance)
    {
        _hashRing.RemoveNode(instance);
        _logger.LogInformation("Removed service instance {InstanceId}", instance.Id);
    }
    
    public ServiceInstance GetInstance(string requestKey)
    {
        return _hashRing.GetNode(requestKey);
    }
    
    public async Task<HttpResponseMessage> ForwardRequestAsync(
        HttpRequestMessage request,
        string requestKey,
        CancellationToken ct)
    {
        var instance = GetInstance(requestKey);
        var client = new HttpClient();
        request.RequestUri = new Uri(instance.Address + request.RequestUri.PathAndQuery);
        
        return await client.SendAsync(request, ct);
    }
}

// 6. Service instance model
public record ServiceInstance
{
    public string Id { get; init; }
    public string Address { get; init; }
    public int Port { get; init; }
    public string Version { get; init; }
    public Dictionary<string, string> Metadata { get; init; }
    
    public override string ToString() => $"{Id} ({Address}:{Port})";
    
    public override int GetHashCode() => Id.GetHashCode();
}
```

### Consistent Hashing Architecture Diagram

```mermaid
```

![### Consistent Hashing Architecture Diagram](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/diagram_01_consistent-hashing-architecture-diagram-3eff.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/diagram_01_consistent-hashing-architecture-diagram-3eff.md)


---

## Concept 7: Message Queues — Enabling Asynchronous Communication Between Distributed Components

![alt text](<https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/Message Queues.png>)

Message queues decouple system components, enabling reliable asynchronous communication and buffering during traffic spikes. Vehixcare uses Azure Service Bus and RabbitMQ for different workload types.

### Deep Dive into Message Queues

**Benefits of Message Queues:**
- **Decoupling**: Producers and consumers don't need to know about each other
- **Reliability**: Messages persist until processed, preventing data loss
- **Scalability**: Consumers can scale independently based on load
- **Load Leveling**: Buffers traffic spikes to protect consumers
- **Fault Tolerance**: Failed messages can be retried or dead-lettered

**Message Queue Patterns:**

![**Message Queue Patterns:**](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_01_message-queue-patterns.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_01_message-queue-patterns.md)


### Vehixcare Message Queue Implementation

```csharp
// 1. Message contracts
public interface IMessage
{
    string MessageId { get; }
    string CorrelationId { get; }
    DateTime CreatedAt { get; }
    string MessageType { get; }
}

public abstract record BaseMessage : IMessage
{
    public string MessageId { get; init; } = Guid.NewGuid().ToString();
    public string CorrelationId { get; init; }
    public DateTime CreatedAt { get; init; } = DateTime.UtcNow;
    public abstract string MessageType { get; }
}

// Vehicle service messages
public record VehicleServiceRequestedMessage : BaseMessage
{
    public override string MessageType => "Vehicle.Service.Requested";
    public string VehicleId { get; init; }
    public string ServiceType { get; init; }
    public DateTime ScheduledTime { get; init; }
    public string CustomerId { get; init; }
    public string TenantId { get; init; }
    public Dictionary<string, string> Metadata { get; init; }
}

public record VehicleServicedMessage : BaseMessage
{
    public override string MessageType => "Vehicle.Serviced";
    public string VehicleId { get; init; }
    public string ServiceId { get; init; }
    public DateTime ServiceDate { get; init; }
    public decimal Cost { get; init; }
    public int Odometer { get; init; }
}

// Telemetry messages
public record VehicleTelemetryMessage : BaseMessage
{
    public override string MessageType => "Vehicle.Telemetry";
    public string VehicleId { get; init; }
    public DateTime Timestamp { get; init; }
    public Dictionary<string, object> TelemetryData { get; init; }
    public GeoLocation Location { get; init; }
}

// Notification messages
public record NotificationMessage : BaseMessage
{
    public override string MessageType => "Notification.Send";
    public string RecipientId { get; init; }
    public NotificationType Type { get; init; }
    public string Title { get; init; }
    public string Body { get; init; }
    public Dictionary<string, string> Data { get; init; }
}

public enum NotificationType
{
    Email,
    Sms,
    Push,
    Webhook
}

```
**Message queue abstraction**
```csharp
// 2. Message queue abstraction
public interface IMessageQueue
{
    Task PublishAsync<T>(T message, CancellationToken ct = default) where T : IMessage;
    Task SubscribeAsync<T>(Func<T, CancellationToken, Task> handler, CancellationToken ct = default) where T : IMessage;
    Task SubscribeAsync(string queueName, Func<string, CancellationToken, Task> handler, CancellationToken ct = default);
}

// 3. Azure Service Bus implementation
public class AzureServiceBusQueue : IMessageQueue
{
    private readonly ServiceBusClient _client;
    private readonly ServiceBusSender _sender;
    private readonly Dictionary<string, ServiceBusProcessor> _processors;
    private readonly ILogger<AzureServiceBusQueue> _logger;
    private readonly JsonSerializerOptions _jsonOptions;
    
    public AzureServiceBusQueue(IConfiguration config, ILogger<AzureServiceBusQueue> logger)
    {
        _client = new ServiceBusClient(config["ServiceBus:ConnectionString"]);
        _sender = _client.CreateSender(config["ServiceBus:QueueName"]);
        _processors = new Dictionary<string, ServiceBusProcessor>();
        _logger = logger;
        _jsonOptions = new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase
        };
    }
    
    public async Task PublishAsync<T>(T message, CancellationToken ct = default) where T : IMessage
    {
        var serialized = JsonSerializer.Serialize(message, _jsonOptions);
        var serviceBusMessage = new ServiceBusMessage(serialized)
        {
            MessageId = message.MessageId,
            CorrelationId = message.CorrelationId,
            ContentType = "application/json",
            Subject = message.MessageType,
            TimeToLive = TimeSpan.FromDays(1)
        };
        
        // Add custom properties for routing
        serviceBusMessage.ApplicationProperties.Add("MessageType", message.MessageType);
        serviceBusMessage.ApplicationProperties.Add("CreatedAt", message.CreatedAt);
        
        await _sender.SendMessageAsync(serviceBusMessage, ct);
        
        _logger.LogDebug("Published message {MessageId} of type {MessageType}", 
            message.MessageId, message.MessageType);
    }
    
    public async Task SubscribeAsync<T>(Func<T, CancellationToken, Task> handler, CancellationToken ct = default) where T : IMessage
    {
        var queueName = typeof(T).Name;
        await SubscribeAsync(queueName, async (messageBody, token) =>
        {
            var message = JsonSerializer.Deserialize<T>(messageBody, _jsonOptions);
            if (message != null)
            {
                await handler(message, token);
            }
        }, ct);
    }
    
    public async Task SubscribeAsync(string queueName, Func<string, CancellationToken, Task> handler, CancellationToken ct = default)
    {
        var processor = _client.CreateProcessor(queueName, new ServiceBusProcessorOptions
        {
            MaxConcurrentCalls = 10,
            AutoCompleteMessages = false,
            MaxAutoLockRenewalDuration = TimeSpan.FromMinutes(5),
            PrefetchCount = 50
        });
        
        processor.ProcessMessageAsync += async args =>
        {
            try
            {
                var messageBody = args.Message.Body.ToString();
                await handler(messageBody, args.CancellationToken);
                
                await args.CompleteMessageAsync(args.Message);
                
                _logger.LogDebug("Processed message {MessageId}", args.Message.MessageId);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error processing message {MessageId}", args.Message.MessageId);
                
                // Move to dead letter after max retries
                if (args.Message.DeliveryCount >= 5)
                {
                    await args.DeadLetterMessageAsync(args.Message, 
                        deadLetterReason: "Max delivery attempts exceeded",
                        deadLetterErrorDescription: ex.Message);
                }
                else
                {
                    await args.AbandonMessageAsync(args.Message);
                }
            }
        };
        
        processor.ProcessErrorAsync += args =>
        {
            _logger.LogError(args.Exception, "Service Bus processor error");
            return Task.CompletedTask;
        };
        
        await processor.StartProcessingAsync(ct);
        _processors[queueName] = processor;
        
        _logger.LogInformation("Subscribed to queue {QueueName}", queueName);
    }
    
    public async Task StopAsync(CancellationToken ct = default)
    {
        foreach (var processor in _processors.Values)
        {
            await processor.StopProcessingAsync(ct);
            await processor.DisposeAsync();
        }
        
        await _sender.DisposeAsync();
        await _client.DisposeAsync();
    }
}


```
**RabbitMQ implementation for high-throughput scenarios**
```csharp
// 4. RabbitMQ implementation for high-throughput scenarios
public class RabbitMqQueue : IMessageQueue
{
    private readonly IConnection _connection;
    private readonly IModel _channel;
    private readonly ILogger<RabbitMqQueue> _logger;
    private readonly JsonSerializerOptions _jsonOptions;
    private readonly Dictionary<string, AsyncEventingBasicConsumer> _consumers;
    
    public RabbitMqQueue(IConfiguration config, ILogger<RabbitMqQueue> logger)
    {
        var factory = new ConnectionFactory
        {
            HostName = config["RabbitMQ:Host"],
            Port = int.Parse(config["RabbitMQ:Port"]),
            UserName = config["RabbitMQ:Username"],
            Password = config["RabbitMQ:Password"],
            VirtualHost = config["RabbitMQ:VirtualHost"],
            DispatchConsumersAsync = true
        };
        
        _connection = factory.CreateConnection();
        _channel = _connection.CreateModel();
        _logger = logger;
        _jsonOptions = new JsonSerializerOptions { PropertyNamingPolicy = JsonNamingPolicy.CamelCase };
        _consumers = new Dictionary<string, AsyncEventingBasicConsumer>();
        
        // Configure dead letter exchange
        _channel.ExchangeDeclare("vehixcare.dlx", ExchangeType.Direct, durable: true);
        _channel.QueueDeclare("vehixcare.deadletter", durable: true, exclusive: false, autoDelete: false);
        _channel.QueueBind("vehixcare.deadletter", "vehixcare.dlx", "");
    }
    
    public async Task PublishAsync<T>(T message, CancellationToken ct = default) where T : IMessage
    {
        var serialized = JsonSerializer.Serialize(message, _jsonOptions);
        var body = Encoding.UTF8.GetBytes(serialized);
        
        var properties = _channel.CreateBasicProperties();
        properties.MessageId = message.MessageId;
        properties.CorrelationId = message.CorrelationId;
        properties.Timestamp = new AmqpTimestamp(DateTimeOffset.UtcNow.ToUnixTimeSeconds());
        properties.Type = message.MessageType;
        properties.Persistent = true;
        
        _channel.BasicPublish(
            exchange: "",
            routingKey: message.MessageType,
            basicProperties: properties,
            body: body);
        
        await Task.CompletedTask;
        
        _logger.LogDebug("Published message {MessageId} to RabbitMQ", message.MessageId);
    }
    
    public async Task SubscribeAsync<T>(Func<T, CancellationToken, Task> handler, CancellationToken ct = default) where T : IMessage
    {
        var queueName = typeof(T).Name;
        
        // Declare queue with dead letter configuration
        var arguments = new Dictionary<string, object>
        {
            { "x-dead-letter-exchange", "vehixcare.dlx" },
            { "x-dead-letter-routing-key", queueName },
            { "x-max-retries", 3 }
        };
        
        _channel.QueueDeclare(queueName, durable: true, exclusive: false, autoDelete: false, arguments: arguments);
        
        var consumer = new AsyncEventingBasicConsumer(_channel);
        consumer.Received += async (sender, args) =>
        {
            try
            {
                var body = Encoding.UTF8.GetString(args.Body.ToArray());
                var message = JsonSerializer.Deserialize<T>(body, _jsonOptions);
                
                if (message != null)
                {
                    await handler(message, ct);
                }
                
                _channel.BasicAck(args.DeliveryTag, false);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error processing RabbitMQ message");
                
                // Check if we've retried enough times
                var retryCount = GetRetryCount(args.BasicProperties);
                
                if (retryCount >= 3)
                {
                    _channel.BasicNack(args.DeliveryTag, false, false);
                    _logger.LogWarning("Message dead-lettered after {RetryCount} retries", retryCount);
                }
                else
                {
                    _channel.BasicNack(args.DeliveryTag, false, true);
                }
            }
        };
        
        _channel.BasicConsume(queue: queueName, autoAck: false, consumer: consumer);
        _consumers[queueName] = consumer;
        
        await Task.CompletedTask;
        
        _logger.LogInformation("Subscribed to RabbitMQ queue {QueueName}", queueName);
    }
    
    private int GetRetryCount(IBasicProperties properties)
    {
        if (properties.Headers != null && properties.Headers.ContainsKey("x-retry-count"))
        {
            return Convert.ToInt32(properties.Headers["x-retry-count"]);
        }
        return 0;
    }
    
    public async Task SubscribeAsync(string queueName, Func<string, CancellationToken, Task> handler, CancellationToken ct = default)
    {
        await SubscribeAsync<object>(async (msg, token) =>
        {
            await handler(JsonSerializer.Serialize(msg), token);
        }, ct);
    }
    
    public void Dispose()
    {
        _channel?.Close();
        _connection?.Close();
    }
}

```
**Message processor background service**
```csharp

// 5. Message processor background service
public class VehicleServiceMessageProcessor : BackgroundService
{
    private readonly IMessageQueue _messageQueue;
    private readonly IServiceProvider _serviceProvider;
    private readonly ILogger<VehicleServiceMessageProcessor> _logger;
    
    public VehicleServiceMessageProcessor(
        IMessageQueue messageQueue,
        IServiceProvider serviceProvider,
        ILogger<VehicleServiceMessageProcessor> logger)
    {
        _messageQueue = messageQueue;
        _serviceProvider = serviceProvider;
        _logger = logger;
    }
    
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _logger.LogInformation("Vehicle Service Message Processor started");
        
        // Subscribe to vehicle service requests
        await _messageQueue.SubscribeAsync<VehicleServiceRequestedMessage>(
            ProcessServiceRequestAsync, stoppingToken);
        
        // Subscribe to telemetry messages
        await _messageQueue.SubscribeAsync<VehicleTelemetryMessage>(
            ProcessTelemetryAsync, stoppingToken);
        
        // Subscribe to service completion messages
        await _messageQueue.SubscribeAsync<VehicleServicedMessage>(
            ProcessServiceCompletionAsync, stoppingToken);
        
        // Keep the service running
        await Task.Delay(Timeout.Infinite, stoppingToken);
    }
    
    private async Task ProcessServiceRequestAsync(
        VehicleServiceRequestedMessage message, 
        CancellationToken ct)
    {
        using var scope = _serviceProvider.CreateScope();
        var serviceScheduler = scope.ServiceProvider.GetRequiredService<IServiceScheduler>();
        var notificationService = scope.ServiceProvider.GetRequiredService<INotificationService>();
        
        _logger.LogInformation("Processing service request for vehicle {VehicleId}", message.VehicleId);
        
        try
        {
            // Schedule the service
            var scheduled = await serviceScheduler.ScheduleServiceAsync(
                message.VehicleId,
                message.ServiceType,
                message.ScheduledTime,
                ct);
            
            // Send confirmation notification
            await notificationService.SendAsync(new NotificationMessage
            {
                RecipientId = message.CustomerId,
                Type = NotificationType.Email,
                Title = "Service Scheduled",
                Body = $"Your {message.ServiceType} service has been scheduled for {message.ScheduledTime}",
                Data = new Dictionary<string, string>
                {
                    ["ServiceId"] = scheduled.Id,
                    ["VehicleId"] = message.VehicleId
                }
            }, ct);
            
            _logger.LogInformation("Successfully processed service request {MessageId}", message.MessageId);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to process service request {MessageId}", message.MessageId);
            throw; // Re-throw to trigger retry
        }
    }
    
    private async Task ProcessTelemetryAsync(VehicleTelemetryMessage message, CancellationToken ct)
    {
        using var scope = _serviceProvider.CreateScope();
        var telemetryRepository = scope.ServiceProvider.GetRequiredService<IVehicleTelemetryRepository>();
        var diagnosticService = scope.ServiceProvider.GetRequiredService<IDiagnosticService>();
        
        _logger.LogDebug("Processing telemetry for vehicle {VehicleId}", message.VehicleId);
        
        try
        {
            // Store telemetry
            await telemetryRepository.AddTelemetryAsync(message, ct);
            
            // Check for critical diagnostics
            var criticalIssues = diagnosticService.CheckForCriticalIssues(message.TelemetryData);
            
            if (criticalIssues.Any())
            {
                await _messageQueue.PublishAsync(new NotificationMessage
                {
                    RecipientId = message.VehicleId,
                    Type = NotificationType.Push,
                    Title = "Critical Issue Detected",
                    Body = $"Critical issues detected: {string.Join(", ", criticalIssues)}",
                    Data = criticalIssues.ToDictionary(i => i.Code, i => i.Description)
                }, ct);
            }
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to process telemetry for {VehicleId}", message.VehicleId);
            throw;
        }
    }
    
    private async Task ProcessServiceCompletionAsync(VehicleServicedMessage message, CancellationToken ct)
    {
        using var scope = _serviceProvider.CreateScope();
        var notificationService = scope.ServiceProvider.GetRequiredService<INotificationService>();
        var analyticsService = scope.ServiceProvider.GetRequiredService<IAnalyticsService>();
        
        _logger.LogInformation("Processing service completion for vehicle {VehicleId}", message.VehicleId);
        
        try
        {
            // Send completion notification
            await notificationService.SendAsync(new NotificationMessage
            {
                RecipientId = message.VehicleId,
                Type = NotificationType.Email,
                Title = "Service Completed",
                Body = $"Your vehicle service (ID: {message.ServiceId}) has been completed. Total cost: {message.Cost:C}"
            }, ct);
            
            // Update analytics
            await analyticsService.RecordServiceCompletionAsync(message, ct);
            
            // Check if maintenance is due
            await CheckAndScheduleNextMaintenance(message, ct);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to process service completion {MessageId}", message.MessageId);
            throw;
        }
    }
    
    private async Task CheckAndScheduleNextMaintenance(VehicleServicedMessage message, CancellationToken ct)
    {
        using var scope = _serviceProvider.CreateScope();
        var maintenanceService = scope.ServiceProvider.GetRequiredService<IMaintenanceService>();
        
        var nextMaintenance = await maintenanceService.CalculateNextMaintenanceAsync(message.VehicleId, message.Odometer, ct);
        
        if (nextMaintenance.DaysUntilDue <= 30)
        {
            await _messageQueue.PublishAsync(new NotificationMessage
            {
                RecipientId = message.VehicleId,
                Type = NotificationType.Email,
                Title = "Upcoming Maintenance",
                Body = $"Your next maintenance is due in {nextMaintenance.DaysUntilDue} days or {nextMaintenance.OdometerUntilDue} miles",
                Data = new Dictionary<string, string>
                {
                    ["DueDate"] = nextMaintenance.DueDate.ToString(),
                    ["Odometer"] = nextMaintenance.OdometerDue.ToString()
                }
            }, ct);
        }
    }
}
```

### Message Queue Architecture Diagram

```mermaid
```

![### Message Queue Architecture Diagram](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/diagram_02_message-queue-architecture-diagram-7443.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/diagram_02_message-queue-architecture-diagram-7443.md)


---

## Concept 8: Rate Limiting — Controlling Request Rate to Prevent Abuse and Overload

![alt text](<https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/Rate Limiting.png>)

Rate limiting protects system resources from excessive usage while ensuring fair access for all clients. Vehixcare implements multi-dimensional rate limiting with ASP.NET Core's built-in rate limiter and Redis-based distributed rate limiting.

### Deep Dive into Rate Limiting

**Rate Limiting Algorithms:**

![**Rate Limiting Algorithms:**](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_02_rate-limiting-algorithms.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_02_rate-limiting-algorithms.md)


**Rate Limiting Dimensions:**
- **User/Client ID**: Per-user limits for fair usage
- **IP Address**: Prevent distributed attacks
- **API Key**: Per-application limits
- **Endpoint**: Different limits for different operations
- **Tenant**: Multi-tenant limits
- **Global**: System-wide limits

### Vehixcare Rate Limiting Implementation

```csharp
// 1. ASP.NET Core rate limiting configuration
public static class RateLimitingConfiguration
{
    public static IServiceCollection AddVehixcareRateLimiting(
        this IServiceCollection services, 
        IConfiguration config)
    {
        services.AddRateLimiter(options =>
        {
            options.RejectionStatusCode = StatusCodes.Status429TooManyRequests;
            
            // Global concurrency limiter
            options.GlobalLimiter = PartitionedRateLimiter.Create<HttpContext, string>(
                httpContext =>
                {
                    var clientId = httpContext.User.Identity?.Name ?? 
                                  httpContext.Request.Headers["X-Client-Id"].ToString();
                    
                    if (string.IsNullOrEmpty(clientId))
                        clientId = httpContext.Connection.RemoteIpAddress?.ToString() ?? "anonymous";
                    
                    return RateLimitPartition.GetConcurrencyLimiter(
                        clientId,
                        _ => new ConcurrencyLimiterOptions
                        {
                            PermitLimit = 50,
                            QueueProcessingOrder = QueueProcessingOrder.OldestFirst,
                            QueueLimit = 10
                        });
                });
            
            // Token bucket for bursty workloads
            options.AddPolicy("token-bucket", httpContext =>
            {
                var clientId = httpContext.User.Identity?.Name ?? "anonymous";
                
                return RateLimitPartition.GetTokenBucketLimiter(
                    clientId,
                    _ => new TokenBucketRateLimiterOptions
                    {
                        TokenLimit = 100,
                        QueueLimit = 20,
                        ReplenishmentPeriod = TimeSpan.FromSeconds(10),
                        TokensPerPeriod = 20,
                        AutoReplenishment = true,
                        QueueProcessingOrder = QueueProcessingOrder.OldestFirst
                    });
            });
            
            // Fixed window for simple endpoints
            options.AddPolicy("fixed-window", httpContext =>
            {
                var endpoint = httpContext.Request.Path.ToString();
                var tenantId = httpContext.User.Claims.FirstOrDefault(c => c.Type == "tenant")?.Value ?? "default";
                
                return RateLimitPartition.GetFixedWindowLimiter(
                    $"{tenantId}:{endpoint}",
                    _ => new FixedWindowRateLimiterOptions
                    {
                        PermitLimit = 1000,
                        Window = TimeSpan.FromMinutes(1),
                        QueueLimit = 50,
                        QueueProcessingOrder = QueueProcessingOrder.OldestFirst
                    });
            });
            
            // Sliding window for accurate rate limiting
            options.AddPolicy("sliding-window", httpContext =>
            {
                var apiKey = httpContext.Request.Headers["X-API-Key"].ToString();
                
                return RateLimitPartition.GetSlidingWindowLimiter(
                    apiKey,
                    _ => new SlidingWindowRateLimiterOptions
                    {
                        PermitLimit = 100,
                        Window = TimeSpan.FromMinutes(1),
                        SegmentsPerWindow = 6, // 10-second segments
                        QueueLimit = 10,
                        QueueProcessingOrder = QueueProcessingOrder.OldestFirst
                    });
            });
            
            // Endpoint-specific limits
            options.AddPolicy("vehicle-search", httpContext =>
            {
                var searchType = httpContext.Request.Query["type"].ToString();
                var limit = searchType == "premium" ? 100 : 20;
                
                return RateLimitPartition.GetFixedWindowLimiter(
                    httpContext.User.Identity?.Name ?? "anonymous",
                    _ => new FixedWindowRateLimiterOptions
                    {
                        PermitLimit = limit,
                        Window = TimeSpan.FromMinutes(1),
                        QueueLimit = 5
                    });
            });
            
            options.AddPolicy("bulk-operations", httpContext =>
            {
                var tenantId = httpContext.User.Claims.FirstOrDefault(c => c.Type == "tenant")?.Value;
                
                return RateLimitPartition.GetTokenBucketLimiter(
                    tenantId ?? "unknown",
                    _ => new TokenBucketRateLimiterOptions
                    {
                        TokenLimit = 10,
                        QueueLimit = 2,
                        ReplenishmentPeriod = TimeSpan.FromMinutes(1),
                        TokensPerPeriod = 5,
                        AutoReplenishment = true
                    });
            });
            
            // Dynamic rate limiting based on system load
            options.AddPolicy("adaptive", httpContext =>
            {
                var currentLoad = SystemLoadMonitor.GetCurrentLoad();
                var dynamicLimit = currentLoad switch
                {
                    < 0.5 => 1000,
                    < 0.7 => 500,
                    < 0.8 => 200,
                    _ => 50
                };
                
                return RateLimitPartition.GetSlidingWindowLimiter(
                    httpContext.User.Identity?.Name ?? "anonymous",
                    _ => new SlidingWindowRateLimiterOptions
                    {
                        PermitLimit = dynamicLimit,
                        Window = TimeSpan.FromSeconds(10),
                        SegmentsPerWindow = 10,
                        QueueLimit = 10
                    });
            });
            
            // Custom response for rate limit exceeded
            options.OnRejected = async (context, cancellationToken) =>
            {
                context.HttpContext.Response.StatusCode = StatusCodes.Status429TooManyRequests;
                context.HttpContext.Response.Headers.RetryAfter = 
                    context.Lease?.RetryAfter?.TotalSeconds.ToString() ?? "60";
                
                await context.HttpContext.Response.WriteAsJsonAsync(new
                {
                    error = "Rate limit exceeded",
                    message = "Too many requests. Please slow down.",
                    retryAfter = context.Lease?.RetryAfter?.TotalSeconds,
                    limit = context.Lease?.Metadata["Limit"],
                    remaining = context.Lease?.Metadata["Remaining"],
                    reset = context.Lease?.Metadata["Reset"]
                }, cancellationToken);
            };
        });
        
        return services;
    }
}

// 2. Distributed rate limiting with Redis
public class DistributedRateLimiter
{
    private readonly IDatabase _redisDb;
    private readonly ILogger<DistributedRateLimiter> _logger;
    private readonly LuaScript _rateLimitScript;
    
    public DistributedRateLimiter(IConnectionMultiplexer redis, ILogger<DistributedRateLimiter> logger)
    {
        _redisDb = redis.GetDatabase();
        _logger = logger;
        
        // Lua script for atomic rate limiting operations
        _rateLimitScript = LuaScript.Prepare(@"
            local key = KEYS[1]
            local limit = tonumber(ARGV[1])
            local window = tonumber(ARGV[2])
            local now = tonumber(ARGV[3])
            
            local current = redis.call('ZCOUNT', key, now - window, now)
            
            if current < limit then
                redis.call('ZADD', key, now, now)
                redis.call('EXPIRE', key, window)
                return {1, limit - current - 1}
            else
                local oldest = redis.call('ZRANGE', key, 0, 0, 'WITHSCORES')
                local retryAfter = (tonumber(oldest[2]) + window) - now
                return {0, retryAfter}
            end
        ");
    }
    
    public async Task<RateLimitResult> IsAllowedAsync(
        string key, 
        int limit, 
        TimeSpan window,
        CancellationToken ct)
    {
        var now = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
        var windowSeconds = (long)window.TotalSeconds;
        
        try
        {
            var result = await _rateLimitScript.EvaluateAsync(
                _redisDb,
                new[] { $"ratelimit:{key}" },
                new[] { limit.ToString(), windowSeconds.ToString(), now.ToString() });
            
            var results = (RedisResult[])result;
            var allowed = (long)results[0] == 1;
            
            if (allowed)
            {
                var remaining = (long)results[1];
                return new RateLimitResult
                {
                    Allowed = true,
                    Remaining = remaining,
                    Limit = limit,
                    Reset = DateTimeOffset.UtcNow.AddSeconds(windowSeconds)
                };
            }
            else
            {
                var retryAfter = (long)results[1];
                return new RateLimitResult
                {
                    Allowed = false,
                    RetryAfter = TimeSpan.FromSeconds(retryAfter),
                    Limit = limit,
                    Reset = DateTimeOffset.UtcNow.AddSeconds(retryAfter)
                };
            }
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Redis rate limit check failed for {Key}", key);
            
            // Fallback to local in-memory rate limiting
            return await FallbackRateLimitAsync(key, limit, window, ct);
        }
    }
    
    private async Task<RateLimitResult> FallbackRateLimitAsync(
        string key, 
        int limit, 
        TimeSpan window,
        CancellationToken ct)
    {
        // Simple in-memory fallback
        var cacheKey = $"ratelimit_fallback:{key}";
        var current = await MemoryCache.GetOrCreateAsync(cacheKey, entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = window;
            return Task.FromResult(0);
        });
        
        if (current < limit)
        {
            MemoryCache.Set(cacheKey, current + 1, window);
            return new RateLimitResult
            {
                Allowed = true,
                Remaining = limit - current - 1,
                Limit = limit
            };
        }
        
        return new RateLimitResult
        {
            Allowed = false,
            Limit = limit,
            RetryAfter = window
        };
    }
}

// 3. Rate limit result model
public record RateLimitResult
{
    public bool Allowed { get; init; }
    public int Limit { get; init; }
    public int Remaining { get; init; }
    public TimeSpan? RetryAfter { get; init; }
    public DateTimeOffset? Reset { get; init; }
}

// 4. Rate limiting middleware for custom scenarios
public class RateLimitingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly DistributedRateLimiter _rateLimiter;
    private readonly ILogger<RateLimitingMiddleware> _logger;
    
    public RateLimitingMiddleware(
        RequestDelegate next,
        DistributedRateLimiter rateLimiter,
        ILogger<RateLimitingMiddleware> logger)
    {
        _next = next;
        _rateLimiter = rateLimiter;
        _logger = logger;
    }
    
    public async Task InvokeAsync(HttpContext context)
    {
        // Determine rate limit key based on multiple factors
        var key = GetRateLimitKey(context);
        
        // Get rate limit configuration for this endpoint
        var (limit, window) = GetRateLimitConfig(context);
        
        var result = await _rateLimiter.IsAllowedAsync(key, limit, window, context.RequestAborted);
        
        if (!result.Allowed)
        {
            context.Response.StatusCode = StatusCodes.Status429TooManyRequests;
            context.Response.Headers.Append("X-RateLimit-Limit", result.Limit.ToString());
            context.Response.Headers.Append("X-RateLimit-Remaining", "0");
            context.Response.Headers.Append("X-RateLimit-Reset", result.Reset?.ToUnixTimeSeconds().ToString());
            context.Response.Headers.Append("Retry-After", result.RetryAfter?.TotalSeconds.ToString());
            
            await context.Response.WriteAsJsonAsync(new
            {
                error = "Rate limit exceeded",
                message = $"Too many requests. Rate limit: {limit} requests per {window.TotalSeconds} seconds.",
                retryAfter = result.RetryAfter?.TotalSeconds
            });
            
            _logger.LogWarning("Rate limit exceeded for {Key}", key);
            return;
        }
        
        // Add rate limit headers
        context.Response.Headers.Append("X-RateLimit-Limit", result.Limit.ToString());
        context.Response.Headers.Append("X-RateLimit-Remaining", result.Remaining.ToString());
        if (result.Reset.HasValue)
        {
            context.Response.Headers.Append("X-RateLimit-Reset", result.Reset.Value.ToUnixTimeSeconds().ToString());
        }
        
        await _next(context);
    }
    
    private string GetRateLimitKey(HttpContext context)
    {
        var parts = new List<string>();
        
        // Add client identification
        if (context.User.Identity?.IsAuthenticated == true)
        {
            parts.Add($"user:{context.User.Identity.Name}");
        }
        else if (context.Request.Headers.ContainsKey("X-API-Key"))
        {
            parts.Add($"apikey:{context.Request.Headers["X-API-Key"]}");
        }
        else
        {
            parts.Add($"ip:{context.Connection.RemoteIpAddress}");
        }
        
        // Add endpoint
        parts.Add($"endpoint:{context.Request.Path}");
        
        // Add tenant if available
        var tenantId = context.User.Claims.FirstOrDefault(c => c.Type == "tenant")?.Value;
        if (tenantId != null)
        {
            parts.Add($"tenant:{tenantId}");
        }
        
        return string.Join(":", parts);
    }
    
    private (int Limit, TimeSpan Window) GetRateLimitConfig(HttpContext context)
    {
        // Default configuration
        var limit = 100;
        var window = TimeSpan.FromMinutes(1);
        
        // Override based on endpoint
        var path = context.Request.Path.ToString();
        
        if (path.Contains("/api/vehicles/search"))
        {
            limit = 20;
            window = TimeSpan.FromMinutes(1);
        }
        else if (path.Contains("/api/vehicles/bulk"))
        {
            limit = 5;
            window = TimeSpan.FromMinutes(10);
        }
        else if (path.Contains("/api/telemetry"))
        {
            limit = 200;
            window = TimeSpan.FromSeconds(30);
        }
        else if (context.User.IsInRole("Premium"))
        {
            limit = 500;
            window = TimeSpan.FromMinutes(1);
        }
        
        return (limit, window);
    }
}

// 5. Rate limit dashboard and monitoring
public class RateLimitDashboard
{
    private readonly IDatabase _redisDb;
    private readonly ILogger<RateLimitDashboard> _logger;
    
    public RateLimitDashboard(IConnectionMultiplexer redis, ILogger<RateLimitDashboard> logger)
    {
        _redisDb = redis.GetDatabase();
        _logger = logger;
    }
    
    public async Task<Dictionary<string, RateLimitStats>> GetTopViolatorsAsync(int top = 10)
    {
        var stats = new Dictionary<string, RateLimitStats>();
        
        // Scan Redis keys for rate limit entries
        var server = _redisDb.Multiplexer.GetServer(_redisDb.Multiplexer.GetEndPoints().First());
        var keys = server.Keys(pattern: "ratelimit:*");
        
        foreach (var key in keys)
        {
            var count = await _redisDb.SortedSetLengthAsync(key);
            if (count > 0)
            {
                var keyName = key.ToString().Replace("ratelimit:", "");
                stats[keyName] = new RateLimitStats
                {
                    Key = keyName,
                    RequestCount = (int)count,
                    LastRequest = await GetLastRequestTimeAsync(key)
                };
            }
        }
        
        return stats.OrderByDescending(s => s.Value.RequestCount)
                    .Take(top)
                    .ToDictionary(x => x.Key, x => x.Value);
    }
    
    private async Task<DateTime> GetLastRequestTimeAsync(RedisKey key)
    {
        var lastRequest = await _redisDb.SortedSetRangeByRankWithScoresAsync(key, -1, -1);
        if (lastRequest.Any())
        {
            return DateTimeOffset.FromUnixTimeSeconds((long)lastRequest.First().Score).UtcDateTime;
        }
        return DateTime.UtcNow;
    }
    
    public async Task ResetLimitAsync(string key)
    {
        await _redisDb.KeyDeleteAsync($"ratelimit:{key}");
        _logger.LogInformation("Reset rate limit for {Key}", key);
    }
}

public record RateLimitStats
{
    public string Key { get; init; }
    public int RequestCount { get; init; }
    public DateTime LastRequest { get; init; }
}
```

### Rate Limiting Architecture Diagram

```mermaid
```

![### Rate Limiting Architecture Diagram](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/diagram_03_rate-limiting-architecture-diagram-a88c.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/diagram_03_rate-limiting-architecture-diagram-a88c.md)


---

## Concept 9: API Gateway — Central Entry Point Managing Requests, Authentication, and Routing

![alt text](<https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/API Gateway.png>)

The API Gateway serves as the single entry point for all clients, handling cross-cutting concerns like authentication, routing, aggregation, and rate limiting. Vehixcare implements this using YARP (Yet Another Reverse Proxy) with custom middleware.

### Deep Dive into API Gateway

**API Gateway Responsibilities:**
- **Request Routing**: Direct requests to appropriate microservices
- **Authentication/Authorization**: Validate tokens and enforce policies
- **Rate Limiting**: Protect backend services from abuse
- **Response Aggregation**: Combine multiple service responses
- **Protocol Translation**: Convert between protocols (HTTP, WebSocket, gRPC)
- **Caching**: Cache responses to reduce backend load
- **Logging/Monitoring**: Centralized observability
- **Circuit Breaking**: Prevent cascading failures

**Gateway Patterns:**

![**Gateway Patterns:**](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_03_gateway-patterns.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_03_gateway-patterns.md)


### Vehixcare API Gateway Implementation
**API Gateway configuration with YARP**
```csharp
// 1. API Gateway configuration with YARP
public class ApiGatewayConfiguration
{
    public static WebApplication ConfigureGateway(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);
        
        // Authentication with multiple providers
        builder.Services.AddAuthentication()
            .AddJwtBearer("VehicleApp", options =>
            {
                options.Authority = builder.Configuration["Auth:Authority"];
                options.Audience = builder.Configuration["Auth:Audience"];
                options.TokenValidationParameters = new TokenValidationParameters
                {
                    ValidateIssuer = true,
                    ValidateAudience = true,
                    ValidateLifetime = true,
                    ClockSkew = TimeSpan.FromSeconds(30),
                    ValidIssuers = builder.Configuration.GetSection("Auth:ValidIssuers").Get<string[]>(),
                    ValidAudiences = builder.Configuration.GetSection("Auth:ValidAudiences").Get<string[]>()
                };
                options.Events = new JwtBearerEvents
                {
                    OnAuthenticationFailed = context =>
                    {
                        var logger = context.HttpContext.RequestServices.GetRequiredService<ILogger<Program>>();
                        logger.LogWarning(context.Exception, "Authentication failed");
                        return Task.CompletedTask;
                    },
                    OnTokenValidated = context =>
                    {
                        var logger = context.HttpContext.RequestServices.GetRequiredService<ILogger<Program>>();
                        var claims = context.Principal?.Claims.Select(c => $"{c.Type}:{c.Value}");
                        logger.LogDebug("Token validated for user: {User}, Claims: {Claims}",
                            context.Principal?.Identity?.Name, string.Join(", ", claims ?? []));
                        return Task.CompletedTask;
                    }
                };
            })
            .AddApiKey("ThirdParty", options =>
            {
                options.KeyName = "X-API-Key";
                options.KeyHeader = "X-API-Key";
                options.ValidateKey = (key, context) =>
                {
                    var validator = context.RequestServices.GetRequiredService<IApiKeyValidator>();
                    return validator.ValidateAsync(key);
                };
            });
        
        // Authorization policies
        builder.Services.AddAuthorization(options =>
        {
            options.AddPolicy("VehicleRead", policy =>
                policy.RequireClaim("scope", "vehicles:read")
                      .RequireAuthenticatedUser());
                
            options.AddPolicy("VehicleWrite", policy =>
                policy.RequireClaim("scope", "vehicles:write")
                      .RequireClaim("role", "ServiceManager", "Admin"));
                    
            options.AddPolicy("AdminOnly", policy =>
                policy.RequireRole("Admin")
                      .RequireClaim("tenant", "enterprise"));
            
            options.AddPolicy("TelemetryAccess", policy =>
                policy.RequireAssertion(context =>
                    context.User.HasClaim(c => c.Type == "scope" && c.Value == "telemetry:read") ||
                    context.User.HasClaim(c => c.Type == "role" && c.Value == "TelemetryViewer")));
        });
        
        // Configure YARP
        builder.Services.AddReverseProxy()
            .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"))
            .AddTransforms(builder =>
            {
                // Add correlation ID for distributed tracing
                builder.AddRequestTransform(async context =>
                {
                    var correlationId = context.HttpContext.TraceIdentifier;
                    context.ProxyRequest.Headers.Add("X-Correlation-ID", correlationId);
                    context.ProxyRequest.Headers.Add("X-Forwarded-For", 
                        context.HttpContext.Connection.RemoteIpAddress?.ToString());
                    context.ProxyRequest.Headers.Add("X-Forwarded-Proto", 
                        context.HttpContext.Request.Scheme);
                    await ValueTask.CompletedTask;
                });
                
                // Add JWT token forwarding
                builder.AddRequestTransform(async context =>
                {
                    var token = await context.HttpContext.GetTokenAsync("access_token");
                    if (!string.IsNullOrEmpty(token))
                    {
                        context.ProxyRequest.Headers.Authorization = $"Bearer {token}";
                    }
                    await ValueTask.CompletedTask;
                });
                
                // Add API key forwarding for third-party
                builder.AddRequestTransform(context =>
                {
                    if (context.HttpContext.Request.Headers.TryGetValue("X-API-Key", out var apiKey))
                    {
                        context.ProxyRequest.Headers.Add("X-API-Key", apiKey.ToString());
                    }
                    return ValueTask.CompletedTask;
                });
                
                // Add tenant context forwarding
                builder.AddRequestTransform(context =>
                {
                    var tenantId = context.HttpContext.User.Claims
                        .FirstOrDefault(c => c.Type == "tenant")?.Value;
                    if (!string.IsNullOrEmpty(tenantId))
                    {
                        context.ProxyRequest.Headers.Add("X-Tenant-ID", tenantId);
                    }
                    return ValueTask.CompletedTask;
                });
            })
            .AddLoadBalancingPolicy<ConsistentHashLoadBalancingPolicy>("consistent-hash");
        
        // Rate limiting
        builder.Services.AddVehixcareRateLimiting(builder.Configuration);
        
        // Caching for responses
        builder.Services.AddResponseCaching();
        
        // Health checks
        builder.Services.AddHealthChecks()
            .AddUrlGroup(new Uri("http://vehicle-service:8080/health"), "vehicle-service")
            .AddUrlGroup(new Uri("http://scheduler-service:8081/health"), "scheduler-service")
            .AddUrlGroup(new Uri("http://notification-service:8082/health"), "notification-service")
            .AddRedis(builder.Configuration["Redis:ConnectionString"], "redis-cache");
        
        // API aggregator for composite responses
        builder.Services.AddScoped<IApiAggregator, VehicleDashboardAggregator>();
        
        // OpenTelemetry for observability
        builder.Services.AddOpenTelemetry()
            .WithTracing(tracing => tracing
                .AddAspNetCoreInstrumentation()
                .AddHttpClientInstrumentation()
                .AddOtlpExporter())
            .WithMetrics(metrics => metrics
                .AddAspNetCoreInstrumentation()
                .AddPrometheusExporter());
        
        var app = builder.Build();
        
        // Middleware pipeline
        app.UseResponseCaching();
        app.UseAuthentication();
        app.UseAuthorization();
        app.UseRateLimiter();
        
        // Custom request logging middleware
        app.Use(async (context, next) =>
        {
            var sw = Stopwatch.StartNew();
            await next();
            sw.Stop();
            
            context.Response.Headers.Append("X-Response-Time-ms", sw.ElapsedMilliseconds.ToString());
            context.Response.Headers.Append("X-Gateway-Version", "2.0.0");
            
            var logger = context.RequestServices.GetRequiredService<ILogger<Program>>();
            logger.LogDebug("Request {Method} {Path} completed in {Duration}ms with status {StatusCode}",
                context.Request.Method, context.Request.Path, sw.ElapsedMilliseconds, context.Response.StatusCode);
        });
        
        // Aggregate endpoints
        app.MapGet("/api/dashboard/{vehicleId}", async (string vehicleId, IApiAggregator aggregator) =>
        {
            return await aggregator.GetVehicleDashboardAsync(vehicleId);
        }).RequireAuthorization("VehicleRead");
        
        app.MapGet("/api/vehicles/{vehicleId}/full", async (string vehicleId, IApiAggregator aggregator) =>
        {
            return await aggregator.GetFullVehicleDetailsAsync(vehicleId);
        }).RequireAuthorization("VehicleRead");
        
        // Health endpoints
        app.MapHealthChecks("/health", new HealthCheckOptions
        {
            ResponseWriter = async (context, report) =>
            {
                context.Response.ContentType = "application/json";
                var result = new
                {
                    status = report.Status.ToString(),
                    checks = report.Entries.Select(e => new
                    {
                        name = e.Key,
                        status = e.Value.Status.ToString(),
                        description = e.Value.Description,
                        duration = e.Value.Duration
                    }),
                    totalDuration = report.TotalDuration
                };
                await context.Response.WriteAsJsonAsync(result);
            }
        });
        
        app.MapHealthChecks("/health/ready", new HealthCheckOptions
        {
            Predicate = _ => true
        });
        
        app.MapHealthChecks("/health/live", new HealthCheckOptions
        {
            Predicate = _ => false
        });
        
        // Metrics endpoint for Prometheus
        app.MapMetrics();
        
        // Reverse proxy routes
        app.MapReverseProxy();
        
        return app;
    }
}

// 2. Custom load balancing policy for consistent hashing
public class ConsistentHashLoadBalancingPolicy : ILoadBalancingPolicy
{
    private readonly ConcurrentDictionary<string, ConsistentHashRing<string>> _rings = new();
    
    public string Name => "consistent-hash";
    
    public DestinationState? PickDestination(
        HttpContext context,
        ClusterState cluster,
        IReadOnlyList<DestinationState> availableDestinations)
    {
        if (availableDestinations.Count == 0)
            return null;
        
        // Get or create hash ring for this cluster
        var ring = _rings.GetOrAdd(cluster.ClusterId, _ =>
        {
            var newRing = new ConsistentHashRing<string>(virtualNodes: 100);
            foreach (var dest in availableDestinations)
            {
                newRing.AddNode(dest.DestinationId);
            }
            return newRing;
        });
        
        // Determine request key for consistent routing
        var requestKey = GetRequestKey(context);
        
        // Get destination ID from consistent hash
        var destinationId = ring.GetNode(requestKey);
        
        // Find matching destination
        return availableDestinations.FirstOrDefault(d => d.DestinationId == destinationId);
    }
    
    private string GetRequestKey(HttpContext context)
    {
        // Use combination of factors for consistent routing
        var parts = new List<string>();
        
        // Session affinity from cookie
        if (context.Request.Cookies.TryGetValue("session_id", out var sessionId))
        {
            parts.Add($"session:{sessionId}");
        }
        
        // User ID for authenticated requests
        if (context.User.Identity?.IsAuthenticated == true)
        {
            parts.Add($"user:{context.User.Identity.Name}");
        }
        
        // API key for third-party
        if (context.Request.Headers.TryGetValue("X-API-Key", out var apiKey))
        {
            parts.Add($"apikey:{apiKey}");
        }
        
        // Request path for endpoint affinity
        parts.Add($"path:{context.Request.Path}");
        
        // Fallback to IP address
        if (!parts.Any())
        {
            parts.Add($"ip:{context.Connection.RemoteIpAddress}");
        }
        
        return string.Join("|", parts);
    }
}

// 3. API aggregator for composite responses
public interface IApiAggregator
{
    Task<DashboardResponse> GetVehicleDashboardAsync(string vehicleId);
    Task<FullVehicleDetails> GetFullVehicleDetailsAsync(string vehicleId);
}

public class VehicleDashboardAggregator : IApiAggregator
{
    private readonly IHttpClientFactory _httpClientFactory;
    private readonly ICacheService _cache;
    private readonly ILogger<VehicleDashboardAggregator> _logger;
    
    public VehicleDashboardAggregator(
        IHttpClientFactory httpClientFactory,
        ICacheService cache,
        ILogger<VehicleDashboardAggregator> logger)
    {
        _httpClientFactory = httpClientFactory;
        _cache = cache;
        _logger = logger;
    }
    
    public async Task<DashboardResponse> GetVehicleDashboardAsync(string vehicleId)
    {
        var cacheKey = $"dashboard:{vehicleId}";
        
        // Try cache first
        var cached = await _cache.GetAsync<DashboardResponse>(cacheKey);
        if (cached != null)
            return cached;
        
        // Parallel calls to multiple services
        var tasks = new Dictionary<string, Task<HttpResponseMessage>>
        {
            ["vehicle"] = _httpClientFactory.CreateClient("vehicle-service")
                .GetAsync($"/api/vehicles/{vehicleId}"),
            ["services"] = _httpClientFactory.CreateClient("scheduler-service")
                .GetAsync($"/api/services?vehicleId={vehicleId}&limit=5"),
            ["notifications"] = _httpClientFactory.CreateClient("notification-service")
                .GetAsync($"/api/notifications?vehicleId={vehicleId}&unreadOnly=true"),
            ["telemetry"] = _httpClientFactory.CreateClient("telemetry-service")
                .GetAsync($"/api/telemetry/{vehicleId}/latest"),
            ["maintenance"] = _httpClientFactory.CreateClient("maintenance-service")
                .GetAsync($"/api/maintenance/predictions?vehicleId={vehicleId}")
        };
        
        await Task.WhenAll(tasks.Values);
        
        // Combine responses with error handling
        var dashboard = new DashboardResponse
        {
            VehicleId = vehicleId,
            Timestamp = DateTime.UtcNow
        };
        
        try
        {
            if (tasks["vehicle"].Result.IsSuccessStatusCode)
                dashboard.Vehicle = await tasks["vehicle"].Result.Content.ReadFromJsonAsync<VehicleDto>();
            else
                _logger.LogWarning("Failed to fetch vehicle data for {VehicleId}", vehicleId);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error fetching vehicle data for {VehicleId}", vehicleId);
        }
        
        try
        {
            if (tasks["services"].Result.IsSuccessStatusCode)
                dashboard.RecentServices = await tasks["services"].Result.Content.ReadFromJsonAsync<List<ServiceDto>>();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error fetching services for {VehicleId}", vehicleId);
        }
        
        try
        {
            if (tasks["notifications"].Result.IsSuccessStatusCode)
                dashboard.UnreadNotifications = await tasks["notifications"].Result.Content.ReadFromJsonAsync<List<NotificationDto>>();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error fetching notifications for {VehicleId}", vehicleId);
        }
        
        try
        {
            if (tasks["telemetry"].Result.IsSuccessStatusCode)
                dashboard.LatestTelemetry = await tasks["telemetry"].Result.Content.ReadFromJsonAsync<TelemetryDto>();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error fetching telemetry for {VehicleId}", vehicleId);
        }
        
        try
        {
            if (tasks["maintenance"].Result.IsSuccessStatusCode)
                dashboard.MaintenancePredictions = await tasks["maintenance"].Result.Content.ReadFromJsonAsync<List<MaintenancePrediction>>();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error fetching maintenance predictions for {VehicleId}", vehicleId);
        }
        
        // Cache for 5 minutes
        await _cache.SetAsync(cacheKey, dashboard, TimeSpan.FromMinutes(5));
        
        return dashboard;
    }
    
    public async Task<FullVehicleDetails> GetFullVehicleDetailsAsync(string vehicleId)
    {
        var dashboard = await GetVehicleDashboardAsync(vehicleId);
        
        // Additional parallel calls for full details
        var additionalTasks = new Dictionary<string, Task<HttpResponseMessage>>
        {
            ["history"] = _httpClientFactory.CreateClient("vehicle-service")
                .GetAsync($"/api/vehicles/{vehicleId}/history"),
            ["parts"] = _httpClientFactory.CreateClient("parts-service")
                .GetAsync($"/api/parts?vehicleId={vehicleId}"),
            ["warranty"] = _httpClientFactory.CreateClient("warranty-service")
                .GetAsync($"/api/warranty/{vehicleId}")
        };
        
        await Task.WhenAll(additionalTasks.Values);
        
        return new FullVehicleDetails
        {
            Dashboard = dashboard,
            ServiceHistory = additionalTasks["history"].Result.IsSuccessStatusCode ?
                await additionalTasks["history"].Result.Content.ReadFromJsonAsync<List<ServiceRecord>>() : null,
            PartsInventory = additionalTasks["parts"].Result.IsSuccessStatusCode ?
                await additionalTasks["parts"].Result.Content.ReadFromJsonAsync<List<Part>>() : null,
            WarrantyInfo = additionalTasks["warranty"].Result.IsSuccessStatusCode ?
                await additionalTasks["warranty"].Result.Content.ReadFromJsonAsync<WarrantyInfo>() : null
        };
    }
}

// 4. Response models
public record DashboardResponse
{
    public string VehicleId { get; init; }
    public DateTime Timestamp { get; init; }
    public VehicleDto Vehicle { get; init; }
    public List<ServiceDto> RecentServices { get; init; }
    public List<NotificationDto> UnreadNotifications { get; init; }
    public TelemetryDto LatestTelemetry { get; init; }
    public List<MaintenancePrediction> MaintenancePredictions { get; init; }
}

public record FullVehicleDetails
{
    public DashboardResponse Dashboard { get; init; }
    public List<ServiceRecord> ServiceHistory { get; init; }
    public List<Part> PartsInventory { get; init; }
    public WarrantyInfo WarrantyInfo { get; init; }
}
```

### API Gateway Architecture Diagram

```mermaid
```

![### API Gateway Architecture Diagram](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/diagram_04_api-gateway-architecture-diagram-1751.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/diagram_04_api-gateway-architecture-diagram-1751.md)


---

## Concept 10: Microservices Architecture — Independent, Deployable, Loosely Coupled Services

![alt text](<https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/Microservices Architecture.png>)

Microservices architecture enables independent development, deployment, and scaling of system components. Vehixcare's microservices are organized around business capabilities with clear bounded contexts.

### Deep Dive into Microservices

**Microservices Characteristics:**
- **Independent Deployment**: Each service can be deployed without affecting others
- **Decentralized Data Management**: Each service owns its data
- **Technology Heterogeneity**: Services can use different tech stacks
- **Resilience**: Failure isolation prevents cascading failures
- **Scalability**: Services scale independently
- **Organizational Alignment**: Teams aligned with business capabilities

**Microservices vs. Monolith:**

![**Microservices vs. Monolith:**](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_04_microservices-vs-monolith.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_04_microservices-vs-monolith.md)


### Vehixcare Microservices Implementation

```csharp
// 1. Service base abstraction
public abstract class MicroserviceBase
{
    protected readonly ILogger _logger;
    protected readonly IConfiguration _config;
    protected readonly IHealthCheckRegistry _healthRegistry;
    protected readonly string _serviceName;
    protected readonly string _serviceVersion;
    protected readonly string _instanceId;
    
    protected MicroserviceBase(
        ILogger logger,
        IConfiguration config,
        IHealthCheckRegistry healthRegistry)
    {
        _logger = logger;
        _config = config;
        _healthRegistry = healthRegistry;
        _serviceName = config["Service:Name"];
        _serviceVersion = config["Service:Version"];
        _instanceId = $"{Environment.MachineName}-{Guid.NewGuid():N}";
    }
    
    public async Task RunAsync(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);
        
        // Service identity
        builder.Services.AddSingleton<IServiceIdentity>(sp => 
            new ServiceIdentity
            {
                Name = _serviceName,
                Version = _serviceVersion,
                InstanceId = _instanceId,
                StartTime = DateTime.UtcNow
            });
        
        // Configuration
        builder.Configuration
            .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
            .AddJsonFile($"appsettings.{builder.Environment.EnvironmentName}.json", optional: true)
            .AddEnvironmentVariables()
            .AddConsulConfiguration();
        
        // OpenTelemetry for observability
        builder.Services.AddOpenTelemetry()
            .WithTracing(tracing => tracing
                .SetResourceBuilder(ResourceBuilder.CreateDefault()
                    .AddService(_serviceName, _serviceVersion, _instanceId))
                .AddAspNetCoreInstrumentation()
                .AddHttpClientInstrumentation()
                .AddSqlClientInstrumentation()
                .AddRedisInstrumentation()
                .AddOtlpExporter())
            .WithMetrics(metrics => metrics
                .AddAspNetCoreInstrumentation()
                .AddRuntimeInstrumentation()
                .AddPrometheusExporter());
        
        // Health checks
        ConfigureHealthChecks(builder.Services);
        
        // Service discovery
        builder.Services.AddConsulServiceDiscovery();
        
        // Message bus integration
        builder.Services.AddServiceBusIntegration();
        
        // Circuit breaker for dependencies
        ConfigureResiliencePolicies(builder.Services);
        
        // Database context
        ConfigureDatabase(builder.Services);
        
        // Caching
        builder.Services.AddStackExchangeRedisCache(options =>
        {
            options.Configuration = _config["Redis:ConnectionString"];
            options.InstanceName = $"{_serviceName}:";
        });
        
        // Controllers
        builder.Services.AddControllers()
            .AddJsonOptions(options =>
            {
                options.JsonSerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
                options.JsonSerializerOptions.DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull;
            });
        
        // Swagger for API documentation
        builder.Services.AddEndpointsApiExplorer();
        builder.Services.AddSwaggerGen(options =>
        {
            options.SwaggerDoc("v1", new OpenApiInfo
            {
                Title = $"{_serviceName} API",
                Version = _serviceVersion,
                Description = $"Vehixcare {_serviceName} microservice"
            });
            
            options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
            {
                Name = "Authorization",
                Type = SecuritySchemeType.Http,
                Scheme = "Bearer",
                BearerFormat = "JWT",
                In = ParameterLocation.Header,
                Description = "Enter 'Bearer' followed by your JWT token"
            });
            
            options.AddSecurityRequirement(new OpenApiSecurityRequirement
            {
                {
                    new OpenApiSecurityScheme
                    {
                        Reference = new OpenApiReference
                        {
                            Type = ReferenceType.SecurityScheme,
                            Id = "Bearer"
                        }
                    },
                    Array.Empty<string>()
                }
            });
        });
        
        var app = builder.Build();
        
        // Middleware pipeline
        if (app.Environment.IsDevelopment())
        {
            app.UseSwagger();
            app.UseSwaggerUI();
        }
        
        app.UseAuthentication();
        app.UseAuthorization();
        
        // Kubernetes probes
        app.MapGet("/health/live", async () => 
            Results.Ok(new { status = "alive", service = _serviceName, instance = _instanceId }));
        
        app.MapGet("/health/ready", async () =>
        {
            var healthReport = await _healthRegistry.CheckHealthAsync();
            return healthReport.Status == HealthStatus.Healthy 
                ? Results.Ok(new { status = "ready", checks = healthReport.Entries })
                : Results.StatusCode(503);
        });
        
        app.MapGet("/health/startup", async () =>
        {
            // Check if service is fully initialized
            var isReady = await IsServiceReadyAsync();
            return isReady 
                ? Results.Ok(new { status = "ready" })
                : Results.StatusCode(503);
        });
        
        app.MapMetrics();
        app.MapControllers();
        
        // Register with service discovery
        await RegisterWithServiceDiscoveryAsync(app.Lifetime.ApplicationStopping);
        
        _logger.LogInformation("Service {Name} v{Version} started with instance {InstanceId}", 
            _serviceName, _serviceVersion, _instanceId);
        
        await app.RunAsync();
    }
    
    protected abstract void ConfigureHealthChecks(IServiceCollection services);
    protected abstract void ConfigureDatabase(IServiceCollection services);
    protected abstract void ConfigureResiliencePolicies(IServiceCollection services);
    protected virtual Task<bool> IsServiceReadyAsync() => Task.FromResult(true);
    
    private async Task RegisterWithServiceDiscoveryAsync(CancellationToken ct)
    {
        var registration = new ServiceRegistration
        {
            Id = _instanceId,
            Name = _serviceName,
            Version = _serviceVersion,
            Address = _config["Service:Address"],
            Port = int.Parse(_config["Service:Port"]),
            HealthCheckUrl = $"{_config["Service:Address"]}:{_config["Service:Port"]}/health/live",
            Tags = _config.GetSection("Service:Tags").Get<string[]>(),
            Metadata = new Dictionary<string, string>
            {
                ["environment"] = _config["Environment"],
                ["version"] = _serviceVersion,
                ["start_time"] = DateTime.UtcNow.ToString("o")
            }
        };
        
        var discovery = _config["ServiceDiscovery:Type"];
        
        if (discovery == "consul")
        {
            await RegisterWithConsulAsync(registration, ct);
        }
        else if (discovery == "kubernetes")
        {
            await RegisterWithKubernetesAsync(registration, ct);
        }
    }
    
    private async Task RegisterWithConsulAsync(ServiceRegistration registration, CancellationToken ct)
    {
        var consulClient = new ConsulClient(cfg =>
        {
            cfg.Address = new Uri(_config["ServiceDiscovery:Consul:Address"]);
        });
        
        var agentRegistration = new AgentServiceRegistration
        {
            ID = registration.Id,
            Name = registration.Name,
            Address = registration.Address.Split(':')[0],
            Port = registration.Port,
            Tags = registration.Tags,
            Meta = registration.Metadata,
            Check = new AgentServiceCheck
            {
                HTTP = registration.HealthCheckUrl,
                Interval = TimeSpan.FromSeconds(10),
                Timeout = TimeSpan.FromSeconds(5),
                DeregisterCriticalServiceAfter = TimeSpan.FromMinutes(1)
            }
        };
        
        await consulClient.Agent.ServiceRegister(agentRegistration, ct);
        
        _logger.LogInformation("Registered with Consul: {ServiceId}", registration.Id);
    }
    
    private async Task RegisterWithKubernetesAsync(ServiceRegistration registration, CancellationToken ct)
    {
        // Kubernetes uses DNS for service discovery
        // No explicit registration needed
        _logger.LogInformation("Using Kubernetes DNS for service discovery");
        await Task.CompletedTask;
    }
}

// 2. Vehicle Service implementation
public class VehicleService : MicroserviceBase
{
    public VehicleService(
        ILogger<VehicleService> logger,
        IConfiguration config,
        IHealthCheckRegistry healthRegistry)
        : base(logger, config, healthRegistry)
    {
    }
    
    protected override void ConfigureHealthChecks(IServiceCollection services)
    {
        services.AddHealthChecks()
            .AddDbContextCheck<VehicleDbContext>("vehicle-db")
            .AddRedis(_config["Redis:ConnectionString"], "redis-cache")
            .AddUrlGroup(new Uri(_config["ServiceDependencies:SchedulerService"]), "scheduler-service")
            .AddUrlGroup(new Uri(_config["ServiceDependencies:NotificationService"]), "notification-service")
            .AddProcessAllocatedMemoryHealthCheck(512 * 1024 * 1024, "memory-check");
    }
    
    protected override void ConfigureDatabase(IServiceCollection services)
    {
        services.AddDbContext<VehicleDbContext>(options =>
            options.UseSqlServer(_config.GetConnectionString("VehicleDb"),
                sqlOptions =>
                {
                    sqlOptions.EnableRetryOnFailure(5, TimeSpan.FromSeconds(10), null);
                    sqlOptions.CommandTimeout(30);
                }));
    }
    
    protected override void ConfigureResiliencePolicies(IServiceCollection services)
    {
        services.AddHttpClient("scheduler-service", client =>
        {
            client.BaseAddress = new Uri(_config["ServiceDependencies:SchedulerService"]);
            client.Timeout = TimeSpan.FromSeconds(30);
        })
        .AddPolicyHandler(GetRetryPolicy())
        .AddPolicyHandler(GetCircuitBreakerPolicy());
    }
    
    private IAsyncPolicy<HttpResponseMessage> GetRetryPolicy()
    {
        return HttpPolicyExtensions
            .HandleTransientHttpError()
            .Or<TimeoutException>()
            .WaitAndRetryAsync(3, retryAttempt => 
                TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)),
                onRetry: (outcome, timespan, retryCount, context) =>
                {
                    _logger.LogWarning("Retry {RetryCount} after {Delay}s", 
                        retryCount, timespan.TotalSeconds);
                });
    }
    
    private IAsyncPolicy<HttpResponseMessage> GetCircuitBreakerPolicy()
    {
        return HttpPolicyExtensions
            .HandleTransientHttpError()
            .CircuitBreakerAsync(5, TimeSpan.FromSeconds(30),
                onBreak: (ex, breakDelay) =>
                {
                    _logger.LogError(ex, "Circuit broken for {BreakDelay}s", breakDelay.TotalSeconds);
                },
                onReset: () =>
                {
                    _logger.LogInformation("Circuit reset");
                });
    }
}

// 3. Vehicle Service API Controllers
[ApiController]
[Route("api/[controller]")]
[Authorize]
public class VehiclesController : ControllerBase
{
    private readonly IVehicleService _vehicleService;
    private readonly ILogger<VehiclesController> _logger;
    
    public VehiclesController(IVehicleService vehicleService, ILogger<VehiclesController> logger)
    {
        _vehicleService = vehicleService;
        _logger = logger;
    }
    
    [HttpGet]
    [Authorize(Policy = "VehicleRead")]
    public async Task<ActionResult<IEnumerable<VehicleDto>>> GetAll(
        [FromQuery] int page = 1,
        [FromQuery] int pageSize = 20,
        CancellationToken ct = default)
    {
        var vehicles = await _vehicleService.GetAllAsync(page, pageSize, ct);
        return Ok(vehicles);
    }
    
    [HttpGet("{id}")]
    [Authorize(Policy = "VehicleRead")]
    public async Task<ActionResult<VehicleDto>> GetById(string id, CancellationToken ct)
    {
        var vehicle = await _vehicleService.GetByIdAsync(id, ct);
        if (vehicle == null)
            return NotFound();
            
        return Ok(vehicle);
    }
    
    [HttpPost]
    [Authorize(Policy = "VehicleWrite")]
    public async Task<ActionResult<VehicleDto>> Create(
        CreateVehicleRequest request,
        CancellationToken ct)
    {
        var vehicle = await _vehicleService.CreateAsync(request, ct);
        return CreatedAtAction(nameof(GetById), new { id = vehicle.Id }, vehicle);
    }
    
    [HttpPut("{id}")]
    [Authorize(Policy = "VehicleWrite")]
    public async Task<ActionResult<VehicleDto>> Update(
        string id,
        UpdateVehicleRequest request,
        CancellationToken ct)
    {
        var vehicle = await _vehicleService.UpdateAsync(id, request, ct);
        if (vehicle == null)
            return NotFound();
            
        return Ok(vehicle);
    }
    
    [HttpDelete("{id}")]
    [Authorize(Policy = "AdminOnly")]
    public async Task<ActionResult> Delete(string id, CancellationToken ct)
    {
        var deleted = await _vehicleService.DeleteAsync(id, ct);
        if (!deleted)
            return NotFound();
            
        return NoContent();
    }
    
    [HttpGet("{id}/service-history")]
    [Authorize(Policy = "VehicleRead")]
    public async Task<ActionResult<IEnumerable<ServiceRecord>>> GetServiceHistory(
        string id,
        CancellationToken ct)
    {
        var history = await _vehicleService.GetServiceHistoryAsync(id, ct);
        return Ok(history);
    }
}
```

### Microservices Architecture Diagram

```mermaid
```

![### Microservices Architecture Diagram](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/diagram_05_microservices-architecture-diagram-1f2e.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/diagram_05_microservices-architecture-diagram-1f2e.md)


### SOLID Principles in Microservices

![### SOLID Principles in Microservices](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_05_solid-principles-in-microservices-ea4e.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_05_solid-principles-in-microservices-ea4e.md)


### Design Patterns in Microservices

![### Design Patterns in Microservices](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_06_design-patterns-in-microservices-ec44.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_06_design-patterns-in-microservices-ec44.md)


---

## Summary: Part 2 — Distribution & Communication

In this second part of our series, we've explored the critical communication and distribution patterns that enable services to work together effectively:

![In this second part of our series, we've explored the critical communication and distribution patterns that enable services to work together effectively:](https://raw.githubusercontent.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool/refs/heads/main/Vehixcare/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/images/table_07_in-this-second-part-of-our-series-weve-explored-fcc0.png)

[View Source](https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/architecting-resilient-systems-20-essential-concepts-through-a-net-lens---part-2/table_07_in-this-second-part-of-our-series-weve-explored-fcc0.md)


These five concepts work together to create a scalable, resilient communication layer that can handle millions of requests while maintaining loose coupling between services.

### Key Takeaways from Part 2

1. **Consistent hashing is essential for cache efficiency** — Without it, adding nodes would invalidate most cached data
2. **Message queues provide crucial decoupling** — They allow services to evolve independently and handle traffic spikes
3. **Rate limiting protects system stability** — It ensures fair resource allocation and prevents abuse
4. **API Gateway simplifies client development** — It handles cross-cutting concerns centrally
5. **Microservices enable organizational scaling** — They allow teams to work independently and deploy frequently

### Coming Up in Part 3

In Part 3, we'll explore architecture patterns and system design tradeoffs:

- **Monolithic Architecture**: When to start with a monolith and how to evolve
- **Event-Driven Architecture**: Building reactive, loosely coupled systems
- **CAP Theorem**: Understanding consistency, availability, and partition tolerance tradeoffs
- **Distributed Systems**: Managing complexity across multiple nodes
- **Horizontal Scaling**: Adding more machines to handle increasing load

In Part 4, we'll explore optimization and operational patterns:

- **Vertical Scaling**: Increasing resources of a single machine
- **Data Partitioning**: Dividing data for performance and scalability
- **Idempotency**: Ensuring repeated requests produce same result
- **Service Discovery**: Automatically detecting services
- **Observability**: Monitoring logs, metrics, and traces

These concepts will help you make informed architectural decisions based on your specific requirements.

## Complete Series Recap

- **[🏗️ Part 1:** *Foundation & Resilience – Load Balancing, Caching, Database Sharding, Replication, Circuit Breaker* ](#)** 

- **📡 Part 2:** *Distribution & Communication – Consistent Hashing, Message Queues, Rate Limiting, API Gateway, Microservices* *(Current)* 

- **🏛️ Part 3:** *Architecture & Scale – Monolithic Architecture, Event-Driven Architecture, CAP Theorem, Distributed Systems, Horizontal Scaling*

- **⚙️ Part 4:** *Optimization & Operations – Vertical Scaling, Data Partitioning, Idempotency, Service Discovery, Observability *
---

*Continue to [Part 3: Architecture & Scale →](#)*

**Explore the Complete Implementation:** For the full source code, deployment configurations, and comprehensive documentation, visit the **Vehixcare-API repository**: [https://gitlab.com/mvineetsharma/Vehixcare-AI/Vehixcare-API](https://gitlab.com/mvineetsharma/Vehixcare-AI/Vehixcare-API)

*Questions? Feedback? Comment? leave a response below. If you're implementing something similar and want to discuss architectural tradeoffs, I'm always happy to connect with fellow engineers tackling these challenges.*