# Clean Architecture Anti-Pattern - Exception: Across Real-World Domains - Part 5
## Four complete case studies: Payment Processing, Inventory Management, Healthcare Scheduling, and Logistics Tracking.

## Introduction: Theory Meets Practice

In **Part 1** of this series, we established the architectural violation of using exceptions for domain outcomes. In **Part 2**, we quantified the performance cost. In **Part 3**, we provided the comprehensive taxonomy distinguishing infrastructure from domain concerns. In **Part 4**, we delivered the complete Result pattern implementation with .NET 10 features.

This story brings all these principles together through four complete, real-world case studies. Each case study demonstrates the Result pattern in action across distinct business domains, showing how to:

- Model domain outcomes using the Result pattern
- Distinguish infrastructure exceptions from domain outcomes
- Integrate with external services and databases
- Handle complex business rules with functional composition
- Test domain logic without exception assertions

---

## Key Takeaways from Previous Stories

| Story | Key Takeaway |
|-------|--------------|
| **1. 🏛️ A .NET Developer's Guide - Part 1** | Domain exceptions at presentation boundaries violate Clean Architecture. The Result pattern restores proper layer separation. |
| **2. 🎭 Domain Logic in Disguise - Part 2** | Exceptions for domain outcomes are 28x slower and allocate 10x more memory than Result pattern failures. |
| **3. 🔍 Defining the Boundary - Part 3** | Determinism distinguishes infrastructure (non-deterministic) from domain outcomes (deterministic). |
| **4. ⚙️ Building the Result Pattern - Part 4** | Complete Result<T> and DomainError implementation with functional extensions and .NET 10 features. |

This story applies these principles to real business domains, demonstrating the pattern's versatility and power.

---

## Case Study 1: Payment Processing Domain

### 1.1 Domain Context

A payment processing system must handle:
- Multiple payment methods (credit card, bank transfer, digital wallet)
- Fraud detection and risk scoring
- Idempotency for duplicate prevention
- Integration with external payment gateways
- Complex business rules for different regions

### 1.2 Domain Model

```csharp
// Domain/Payment/PaymentTransaction.cs
namespace Domain.Payment;

public class PaymentTransaction
{
    public Guid Id { get; private set; }
    public Guid CustomerId { get; private set; }
    public decimal Amount { get; private set; }
    public string Currency { get; private set; }
    public PaymentMethod PaymentMethod { get; private set; }
    public PaymentStatus Status { get; private set; }
    public string IdempotencyKey { get; private set; }
    public DateTime CreatedAt { get; private set; }
    public DateTime? ProcessedAt { get; private set; }
    public string? GatewayTransactionId { get; private set; }
    public string? DeclineReason { get; private set; }
    public decimal? RiskScore { get; private set; }
    
    private PaymentTransaction() { } // EF Core
    
    public static PaymentTransaction Create(
        Guid customerId,
        decimal amount,
        string currency,
        PaymentMethod paymentMethod,
        string idempotencyKey)
    {
        return new PaymentTransaction
        {
            Id = Guid.NewGuid(),
            CustomerId = customerId,
            Amount = amount,
            Currency = currency,
            PaymentMethod = paymentMethod,
            Status = PaymentStatus.Pending,
            IdempotencyKey = idempotencyKey,
            CreatedAt = DateTime.UtcNow
        };
    }
    
    public Result<Unit> MarkAsSuccessful(string gatewayTransactionId)
    {
        if (Status != PaymentStatus.Pending)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("payment.invalid_state",
                    $"Cannot mark payment {Id} as successful. Current status: {Status}"));
        }
        
        Status = PaymentStatus.Successful;
        ProcessedAt = DateTime.UtcNow;
        GatewayTransactionId = gatewayTransactionId;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> MarkAsDeclined(string declineReason)
    {
        if (Status != PaymentStatus.Pending)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("payment.invalid_state",
                    $"Cannot mark payment {Id} as declined. Current status: {Status}"));
        }
        
        Status = PaymentStatus.Declined;
        ProcessedAt = DateTime.UtcNow;
        DeclineReason = declineReason;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> MarkAsFraudSuspected(decimal riskScore)
    {
        if (Status != PaymentStatus.Pending)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("payment.invalid_state",
                    $"Cannot mark payment {Id} for fraud review. Current status: {Status}"));
        }
        
        Status = PaymentStatus.FraudReview;
        RiskScore = riskScore;
        
        return Result<Unit>.Success(Unit.Default);
    }
}

public enum PaymentStatus
{
    Pending,
    Successful,
    Declined,
    FraudReview,
    Refunded,
    Failed
}

public enum PaymentMethod
{
    CreditCard,
    DebitCard,
    BankTransfer,
    DigitalWallet,
    BuyNowPayLater
}
```

### 1.3 Domain Service with Result Pattern

```csharp
// Domain/Services/PaymentService.cs
namespace Domain.Services;

public interface IPaymentService
{
    Task<Result<PaymentTransaction>> ProcessPaymentAsync(PaymentRequest request, CancellationToken ct);
    Task<Result<PaymentTransaction>> GetPaymentStatusAsync(Guid paymentId, CancellationToken ct);
    Task<Result<RefundTransaction>> RefundPaymentAsync(RefundRequest request, CancellationToken ct);
}

public class PaymentService : IPaymentService
{
    private readonly IPaymentRepository _paymentRepository;
    private readonly IPaymentGateway _gateway;
    private readonly IFraudDetectionService _fraudDetection;
    private readonly ICustomerRepository _customerRepository;
    private readonly ILogger<PaymentService> _logger;
    
    public PaymentService(
        IPaymentRepository paymentRepository,
        IPaymentGateway gateway,
        IFraudDetectionService fraudDetection,
        ICustomerRepository customerRepository,
        ILogger<PaymentService> logger)
    {
        _paymentRepository = paymentRepository;
        _gateway = gateway;
        _fraudDetection = fraudDetection;
        _customerRepository = customerRepository;
        _logger = logger;
    }
    
    public async Task<Result<PaymentTransaction>> ProcessPaymentAsync(
        PaymentRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate request
        if (request.Amount <= 0)
        {
            return Result<PaymentTransaction>.Failure(
                DomainError.Validation("amount", "Payment amount must be positive"));
        }
        
        if (request.Amount > 50000)
        {
            return Result<PaymentTransaction>.Failure(
                DomainError.BusinessRule("payment.limit_exceeded",
                    "Payments exceeding $50,000 require manual approval"));
        }
        
        // DOMAIN OUTCOME: Validate customer exists
        var customerResult = await _customerRepository.GetByIdAsync(request.CustomerId, ct);
        if (customerResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(customerResult.Error);
        }
        
        var customer = customerResult.Value;
        
        // DOMAIN OUTCOME: Check customer status
        if (customer.IsBlocked)
        {
            return Result<PaymentTransaction>.Failure(
                DomainError.BusinessRule("customer.blocked",
                    "Customer account is blocked from processing payments"));
        }
        
        // DOMAIN OUTCOME: Idempotency check
        var existingResult = await _paymentRepository.GetByIdempotencyKeyAsync(
            request.IdempotencyKey, ct);
            
        if (existingResult.IsSuccess && existingResult.Value != null)
        {
            _logger.LogInformation("Duplicate payment prevented for key {Key}",
                request.IdempotencyKey);
            return Result<PaymentTransaction>.Success(existingResult.Value);
        }
        
        // Create payment transaction
        var payment = PaymentTransaction.Create(
            request.CustomerId,
            request.Amount,
            request.Currency,
            request.PaymentMethod,
            request.IdempotencyKey);
        
        // DOMAIN OUTCOME: Fraud detection (domain rule)
        var fraudResult = await _fraudDetection.AnalyzeTransactionAsync(
            payment, customer, request, ct);
            
        if (fraudResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(fraudResult.Error);
        }
        
        if (fraudResult.Value.RiskScore > 0.8m) // High risk threshold
        {
            payment.MarkAsFraudSuspected(fraudResult.Value.RiskScore);
            await _paymentRepository.AddAsync(payment, ct);
            await _paymentRepository.SaveChangesAsync(ct);
            
            return Result<PaymentTransaction>.Failure(
                DomainError.BusinessRule("payment.fraud_suspected",
                    "Transaction flagged for fraud review. Please contact support.",
                    new { riskScore = fraudResult.Value.RiskScore }));
        }
        
        // Save pending transaction
        var saveResult = await _paymentRepository.AddAsync(payment, ct);
        if (saveResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(saveResult.Error);
        }
        
        await _paymentRepository.SaveChangesAsync(ct);
        
        try
        {
            // INFRASTRUCTURE CALL: External payment gateway
            var gatewayResponse = await _gateway.ProcessPaymentAsync(
                new GatewayPaymentRequest
                {
                    PaymentId = payment.Id,
                    Amount = request.Amount,
                    Currency = request.Currency,
                    PaymentMethod = request.PaymentMethod,
                    CardDetails = request.CardDetails,
                    IdempotencyKey = request.IdempotencyKey
                }, ct);
            
            // DOMAIN OUTCOMES: Process gateway response
            return gatewayResponse.Status switch
            {
                GatewayPaymentStatus.Success =>
                    await HandleSuccessfulPayment(payment, gatewayResponse, ct),
                    
                GatewayPaymentStatus.InsufficientFunds =>
                    await HandleDeclinedPayment(payment, "Insufficient funds", ct),
                    
                GatewayPaymentStatus.CardDeclined =>
                    await HandleDeclinedPayment(payment, gatewayResponse.DeclineReason ?? "Card declined", ct),
                    
                GatewayPaymentStatus.InvalidCvv =>
                    await HandleDeclinedPayment(payment, "Invalid CVV code", ct),
                    
                GatewayPaymentStatus.ExpiredCard =>
                    await HandleDeclinedPayment(payment, "Card expired", ct),
                    
                GatewayPaymentStatus.FraudSuspected =>
                    await HandleFraudSuspectedPayment(payment, gatewayResponse.RiskScore ?? 0.5m, ct),
                    
                _ => Result<PaymentTransaction>.Failure(
                    DomainError.BusinessRule("payment.unknown_gateway_status",
                        $"Unknown gateway status: {gatewayResponse.Status}"))
            };
        }
        catch (HttpRequestException ex) when (ex.StatusCode == HttpStatusCode.ServiceUnavailable)
        {
            // INFRASTRUCTURE EXCEPTION - Transient
            _logger.LogWarning(ex, "Payment gateway unavailable for payment {PaymentId}", payment.Id);
            throw new ExternalServiceInfrastructureException(
                "PaymentGateway",
                "Payment gateway temporarily unavailable",
                HttpStatusCode.ServiceUnavailable,
                isTransient: true,
                errorCode: "PAY_GW_503",
                innerException: ex)
            {
                RetryAfter = TimeSpan.FromSeconds(30)
            };
        }
        catch (HttpRequestException ex) when (ex.StatusCode == HttpStatusCode.GatewayTimeout)
        {
            // INFRASTRUCTURE EXCEPTION - Transient
            _logger.LogWarning(ex, "Payment gateway timeout for payment {PaymentId}", payment.Id);
            throw new ExternalServiceInfrastructureException(
                "PaymentGateway",
                "Payment gateway timeout",
                HttpStatusCode.GatewayTimeout,
                isTransient: true,
                errorCode: "PAY_GW_TIMEOUT",
                innerException: ex);
        }
        catch (TimeoutException ex)
        {
            // INFRASTRUCTURE EXCEPTION - Transient
            _logger.LogWarning(ex, "Payment gateway timeout for payment {PaymentId}", payment.Id);
            throw new ExternalServiceInfrastructureException(
                "PaymentGateway",
                "Payment gateway timeout",
                isTransient: true,
                errorCode: "PAY_GW_TIMEOUT",
                innerException: ex);
        }
        catch (HttpRequestException ex) when (ex.StatusCode == HttpStatusCode.Forbidden)
        {
            // INFRASTRUCTURE EXCEPTION - Permanent
            _logger.LogError(ex, "Payment gateway authentication failed for payment {PaymentId}", payment.Id);
            throw new ExternalServiceInfrastructureException(
                "PaymentGateway",
                "Payment gateway authentication failed",
                HttpStatusCode.Forbidden,
                isTransient: false,
                errorCode: "PAY_GW_AUTH",
                innerException: ex)
            {
                ResolutionInstructions = "Verify API keys and merchant account configuration",
                RequiresManualIntervention = true
            };
        }
    }
    
    private async Task<Result<PaymentTransaction>> HandleSuccessfulPayment(
        PaymentTransaction payment,
        GatewayPaymentResponse response,
        CancellationToken ct)
    {
        var markResult = payment.MarkAsSuccessful(response.TransactionId);
        if (markResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(markResult.Error);
        }
        
        var updateResult = await _paymentRepository.UpdateAsync(payment, ct);
        if (updateResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(updateResult.Error);
        }
        
        await _paymentRepository.SaveChangesAsync(ct);
        
        _logger.LogInformation("Payment {PaymentId} processed successfully. Gateway TXN: {GatewayTxnId}",
            payment.Id, response.TransactionId);
        
        return Result<PaymentTransaction>.Success(payment);
    }
    
    private async Task<Result<PaymentTransaction>> HandleDeclinedPayment(
        PaymentTransaction payment,
        string declineReason,
        CancellationToken ct)
    {
        var markResult = payment.MarkAsDeclined(declineReason);
        if (markResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(markResult.Error);
        }
        
        var updateResult = await _paymentRepository.UpdateAsync(payment, ct);
        if (updateResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(updateResult.Error);
        }
        
        await _paymentRepository.SaveChangesAsync(ct);
        
        // DOMAIN OUTCOME: Return domain error for declined payment
        return Result<PaymentTransaction>.Failure(
            DomainError.BusinessRule("payment.declined", declineReason));
    }
    
    private async Task<Result<PaymentTransaction>> HandleFraudSuspectedPayment(
        PaymentTransaction payment,
        decimal riskScore,
        CancellationToken ct)
    {
        var markResult = payment.MarkAsFraudSuspected(riskScore);
        if (markResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(markResult.Error);
        }
        
        var updateResult = await _paymentRepository.UpdateAsync(payment, ct);
        if (updateResult.IsFailure)
        {
            return Result<PaymentTransaction>.Failure(updateResult.Error);
        }
        
        await _paymentRepository.SaveChangesAsync(ct);
        
        // DOMAIN OUTCOME: Return domain error for fraud suspicion
        return Result<PaymentTransaction>.Failure(
            DomainError.BusinessRule("payment.fraud_suspected",
                "Transaction flagged for fraud review. Please contact support.",
                new { riskScore }));
    }
}
```

### 1.4 Key Takeaways from Payment Processing

| Concept | Implementation |
|---------|----------------|
| **Domain Outcomes** | Insufficient funds, card declined, invalid CVV, fraud suspicion |
| **Infrastructure Exceptions** | Gateway timeout, 503 unavailable, authentication failure |
| **Idempotency** | Duplicate requests return existing result |
| **Fraud Detection** | Domain rule with risk scoring before gateway call |
| **State Management** | Payment entity encapsulates state transition rules |

---

## Case Study 2: Inventory Management Domain

### 2.1 Domain Context

An inventory management system must handle:
- High concurrency (multiple users reserving same product)
- Multi-warehouse distribution
- Reservation expiration and release
- Safety stock and reorder points
- Bulk operations for cart checkout

### 2.2 Domain Model

```csharp
// Domain/Inventory/InventoryItem.cs
namespace Domain.Inventory;

public class InventoryItem
{
    public Guid Id { get; private set; }
    public Guid ProductId { get; private set; }
    public Guid WarehouseId { get; private set; }
    public int PhysicalQuantity { get; private set; }
    public int ReservedQuantity { get; private set; }
    public int SafetyStock { get; private set; }
    public int ReorderPoint { get; private set; }
    public bool TrackInventory { get; private set; }
    
    public int AvailableQuantity => PhysicalQuantity - ReservedQuantity - SafetyStock;
    
    private InventoryItem() { }
    
    public static InventoryItem Create(
        Guid productId,
        Guid warehouseId,
        int initialQuantity,
        int safetyStock = 0,
        int reorderPoint = 0)
    {
        return new InventoryItem
        {
            Id = Guid.NewGuid(),
            ProductId = productId,
            WarehouseId = warehouseId,
            PhysicalQuantity = initialQuantity,
            ReservedQuantity = 0,
            SafetyStock = safetyStock,
            ReorderPoint = reorderPoint,
            TrackInventory = true
        };
    }
    
    public Result<Reservation> Reserve(int quantity, Guid orderId, TimeSpan reservationDuration)
    {
        if (!TrackInventory)
        {
            return Result<Reservation>.Success(
                Reservation.CreateUnreserved(orderId, ProductId, quantity));
        }
        
        if (quantity <= 0)
        {
            return Result<Reservation>.Failure(
                DomainError.Validation("quantity", "Reservation quantity must be positive"));
        }
        
        if (AvailableQuantity < quantity)
        {
            return Result<Reservation>.Failure(
                DomainError.OutOfStock(ProductId.ToString(), quantity, AvailableQuantity));
        }
        
        ReservedQuantity += quantity;
        
        return Result<Reservation>.Success(
            Reservation.Create(Id, orderId, ProductId, quantity, reservationDuration));
    }
    
    public Result<Unit> ReleaseReservation(int quantity)
    {
        if (quantity <= 0)
        {
            return Result<Unit>.Failure(
                DomainError.Validation("quantity", "Release quantity must be positive"));
        }
        
        if (ReservedQuantity < quantity)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("inventory.reservation_mismatch",
                    $"Cannot release {quantity} units. Only {ReservedQuantity} units reserved."));
        }
        
        ReservedQuantity -= quantity;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> Restock(int quantity)
    {
        if (quantity <= 0)
        {
            return Result<Unit>.Failure(
                DomainError.Validation("quantity", "Restock quantity must be positive"));
        }
        
        PhysicalQuantity += quantity;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public bool NeedsReorder() => TrackInventory && AvailableQuantity <= ReorderPoint;
}

// Domain/Inventory/Reservation.cs
public class Reservation
{
    public Guid Id { get; private set; }
    public Guid? InventoryItemId { get; private set; }
    public Guid OrderId { get; private set; }
    public Guid ProductId { get; private set; }
    public int Quantity { get; private set; }
    public DateTime ExpiresAt { get; private set; }
    public ReservationStatus Status { get; private set; }
    
    private Reservation() { }
    
    public static Reservation Create(
        Guid inventoryItemId,
        Guid orderId,
        Guid productId,
        int quantity,
        TimeSpan duration)
    {
        return new Reservation
        {
            Id = Guid.NewGuid(),
            InventoryItemId = inventoryItemId,
            OrderId = orderId,
            ProductId = productId,
            Quantity = quantity,
            ExpiresAt = DateTime.UtcNow.Add(duration),
            Status = ReservationStatus.Active
        };
    }
    
    public static Reservation CreateUnreserved(Guid orderId, Guid productId, int quantity)
    {
        return new Reservation
        {
            Id = Guid.NewGuid(),
            InventoryItemId = null,
            OrderId = orderId,
            ProductId = productId,
            Quantity = quantity,
            ExpiresAt = DateTime.MaxValue,
            Status = ReservationStatus.Unreserved
        };
    }
    
    public bool IsExpired() => Status == ReservationStatus.Active && DateTime.UtcNow > ExpiresAt;
    
    public Result<Unit> Release()
    {
        if (Status != ReservationStatus.Active)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("reservation.invalid_state",
                    $"Cannot release reservation {Id}. Current status: {Status}"));
        }
        
        Status = ReservationStatus.Released;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> Confirm()
    {
        if (Status != ReservationStatus.Active)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("reservation.invalid_state",
                    $"Cannot confirm reservation {Id}. Current status: {Status}"));
        }
        
        if (IsExpired())
        {
            Status = ReservationStatus.Expired;
            return Result<Unit>.Failure(
                DomainError.BusinessRule("reservation.expired",
                    $"Reservation {Id} has expired"));
        }
        
        Status = ReservationStatus.Confirmed;
        
        return Result<Unit>.Success(Unit.Default);
    }
}

public enum ReservationStatus
{
    Active,
    Confirmed,
    Released,
    Expired,
    Unreserved
}
```

### 2.3 Domain Service with Result Pattern

```csharp
// Domain/Services/InventoryService.cs
namespace Domain.Services;

public interface IInventoryService
{
    Task<Result<Reservation>> ReserveAsync(ReserveRequest request, CancellationToken ct);
    Task<Result<Unit>> ReleaseReservationAsync(Guid reservationId, CancellationToken ct);
    Task<Result<BulkReservationResult>> BulkReserveAsync(BulkReserveRequest request, CancellationToken ct);
    Task<Result<AvailabilityResult>> CheckAvailabilityAsync(CheckAvailabilityRequest request, CancellationToken ct);
}

public class InventoryService : IInventoryService
{
    private readonly IInventoryRepository _inventoryRepository;
    private readonly IReservationRepository _reservationRepository;
    private readonly IProductRepository _productRepository;
    private readonly IDistributedLock _distributedLock;
    private readonly ILogger<InventoryService> _logger;
    
    public InventoryService(
        IInventoryRepository inventoryRepository,
        IReservationRepository reservationRepository,
        IProductRepository productRepository,
        IDistributedLock distributedLock,
        ILogger<InventoryService> logger)
    {
        _inventoryRepository = inventoryRepository;
        _reservationRepository = reservationRepository;
        _productRepository = productRepository;
        _distributedLock = distributedLock;
        _logger = logger;
    }
    
    public async Task<Result<Reservation>> ReserveAsync(ReserveRequest request, CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate request
        if (request.Quantity <= 0)
        {
            return Result<Reservation>.Failure(
                DomainError.Validation("quantity", "Reservation quantity must be positive"));
        }
        
        if (request.Quantity > 1000)
        {
            return Result<Reservation>.Failure(
                DomainError.BusinessRule("reservation.quantity_exceeded",
                    "Cannot reserve more than 1000 units in a single reservation"));
        }
        
        // DOMAIN OUTCOME: Validate product exists
        var productResult = await _productRepository.GetByIdAsync(request.ProductId, ct);
        if (productResult.IsFailure)
        {
            return Result<Reservation>.Failure(productResult.Error);
        }
        
        var product = productResult.Value;
        
        // DOMAIN OUTCOME: Check minimum order quantity
        if (request.Quantity < product.MinimumOrderQuantity)
        {
            return Result<Reservation>.Failure(
                DomainError.Validation("quantity",
                    $"Minimum order quantity for {product.Name} is {product.MinimumOrderQuantity}"));
        }
        
        // INFRASTRUCTURE: Distributed lock to prevent race conditions
        var lockKey = $"inventory:reservation:{request.ProductId}";
        await using var lockHandle = await _distributedLock.AcquireAsync(lockKey, TimeSpan.FromSeconds(30), ct);
        
        if (lockHandle is null)
        {
            _logger.LogWarning("Lock contention for product {ProductId}", request.ProductId);
            return Result<Reservation>.Failure(
                DomainError.Conflict("System busy processing inventory. Please retry."));
        }
        
        try
        {
            // Find best warehouse for this product
            var inventoryResult = await _inventoryRepository.FindBestWarehouseAsync(
                request.ProductId, request.Quantity, ct);
                
            if (inventoryResult.IsFailure)
            {
                return Result<Reservation>.Failure(inventoryResult.Error);
            }
            
            var inventoryItem = inventoryResult.Value;
            
            if (inventoryItem is null)
            {
                return Result<Reservation>.Failure(
                    DomainError.OutOfStock(request.ProductId.ToString(), request.Quantity, 0));
            }
            
            // Check for existing reservation by same order
            var existingResult = await _reservationRepository.GetActiveByOrderAndProductAsync(
                request.OrderId, request.ProductId, ct);
                
            if (existingResult.IsSuccess && existingResult.Value != null)
            {
                _logger.LogInformation("Reservation already exists for order {OrderId}, product {ProductId}",
                    request.OrderId, request.ProductId);
                return Result<Reservation>.Success(existingResult.Value);
            }
            
            // DOMAIN OUTCOME: Create reservation
            var reservationResult = inventoryItem.Reserve(
                request.Quantity,
                request.OrderId,
                TimeSpan.FromMinutes(request.ReservationMinutes ?? 30));
                
            if (reservationResult.IsFailure)
            {
                return Result<Reservation>.Failure(reservationResult.Error);
            }
            
            var reservation = reservationResult.Value;
            
            // Save changes
            var updateResult = await _inventoryRepository.UpdateInventoryAsync(inventoryItem, ct);
            if (updateResult.IsFailure)
            {
                return Result<Reservation>.Failure(updateResult.Error);
            }
            
            var saveResult = await _reservationRepository.AddAsync(reservation, ct);
            if (saveResult.IsFailure)
            {
                // Compensate: release the reserved quantity
                inventoryItem.ReleaseReservation(request.Quantity);
                await _inventoryRepository.UpdateInventoryAsync(inventoryItem, ct);
                return Result<Reservation>.Failure(saveResult.Error);
            }
            
            await _inventoryRepository.SaveChangesAsync(ct);
            
            _logger.LogInformation("Reservation {ReservationId} created for order {OrderId}, product {ProductId}, quantity {Quantity}",
                reservation.Id, request.OrderId, request.ProductId, request.Quantity);
            
            return Result<Reservation>.Success(reservation);
        }
        catch (SqlException ex) when (ex.Number == 1205) // Deadlock
        {
            _logger.LogWarning(ex, "Deadlock during inventory reservation for product {ProductId}", request.ProductId);
            throw new DatabaseInfrastructureException(
                "Database deadlock during inventory reservation", ex.Number, "DB_DEADLOCK", ex);
        }
        catch (SqlException ex) when (ex.Number == -2) // Timeout
        {
            _logger.LogError(ex, "Database timeout during inventory reservation for product {ProductId}", request.ProductId);
            throw new DatabaseInfrastructureException(
                "Database timeout during inventory reservation", ex.Number, "DB_TIMEOUT", ex);
        }
    }
    
    public async Task<Result<BulkReservationResult>> BulkReserveAsync(
        BulkReserveRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate request
        if (request.Items.Count == 0)
        {
            return Result<BulkReservationResult>.Failure(
                DomainError.Validation("items", "Bulk reservation must contain at least one item"));
        }
        
        // Sort products to prevent deadlocks (consistent lock ordering)
        var orderedItems = request.Items
            .OrderBy(i => i.ProductId)
            .ToList();
        
        var reservations = new List<Reservation>();
        var failedItems = new List<BulkReservationFailure>();
        
        // Process each item with lock
        foreach (var item in orderedItems)
        {
            var reserveRequest = new ReserveRequest
            {
                ProductId = item.ProductId,
                OrderId = request.OrderId,
                Quantity = item.Quantity,
                ReservationMinutes = request.ReservationMinutes
            };
            
            var result = await ReserveAsync(reserveRequest, ct);
            
            if (result.IsSuccess)
            {
                reservations.Add(result.Value);
            }
            else
            {
                failedItems.Add(new BulkReservationFailure
                {
                    ProductId = item.ProductId,
                    Quantity = item.Quantity,
                    Reason = result.Error.Message,
                    ErrorCode = result.Error.Code
                });
                
                // DOMAIN OUTCOME: All-or-nothing policy
                if (request.FailurePolicy == BulkReservationFailurePolicy.AllOrNothing)
                {
                    // Release all successful reservations
                    foreach (var reservation in reservations)
                    {
                        await ReleaseReservationAsync(reservation.Id, ct);
                    }
                    
                    return Result<BulkReservationResult>.Failure(
                        DomainError.BusinessRule("bulk_reservation.failed",
                            "Bulk reservation failed. All reservations released.",
                            new { failedItems }));
                }
            }
        }
        
        var result = new BulkReservationResult
        {
            SuccessfulReservations = reservations,
            FailedItems = failedItems,
            OverallStatus = failedItems.Any() ? BulkReservationStatus.PartialSuccess : BulkReservationStatus.Success,
            ExpiresAt = reservations.Min(r => r.ExpiresAt)
        };
        
        return Result<BulkReservationResult>.Success(result);
    }
    
    public async Task<Result<Unit>> ReleaseReservationAsync(Guid reservationId, CancellationToken ct)
    {
        var reservationResult = await _reservationRepository.GetByIdAsync(reservationId, ct);
        if (reservationResult.IsFailure)
        {
            return Result<Unit>.Failure(reservationResult.Error);
        }
        
        var reservation = reservationResult.Value;
        
        if (reservation.Status != ReservationStatus.Active)
        {
            // Already released or expired - consider it done
            return Result<Unit>.Success(Unit.Default);
        }
        
        // Check if expired
        if (reservation.IsExpired())
        {
            reservation.Release(); // Will mark as expired
            await _reservationRepository.UpdateAsync(reservation, ct);
            await _reservationRepository.SaveChangesAsync(ct);
            return Result<Unit>.Success(Unit.Default);
        }
        
        // INFRASTRUCTURE: Lock to update inventory
        var lockKey = $"inventory:reservation:{reservation.ProductId}";
        await using var lockHandle = await _distributedLock.AcquireAsync(lockKey, TimeSpan.FromSeconds(30), ct);
        
        if (lockHandle is null)
        {
            return Result<Unit>.Failure(
                DomainError.Conflict("System busy processing inventory. Please retry."));
        }
        
        try
        {
            var inventoryResult = await _inventoryRepository.GetByProductAndWarehouseAsync(
                reservation.ProductId, reservation.InventoryItemId!.Value, ct);
                
            if (inventoryResult.IsSuccess && inventoryResult.Value != null)
            {
                inventoryResult.Value.ReleaseReservation(reservation.Quantity);
                await _inventoryRepository.UpdateInventoryAsync(inventoryResult.Value, ct);
            }
            
            var releaseResult = reservation.Release();
            if (releaseResult.IsFailure)
            {
                return releaseResult;
            }
            
            await _reservationRepository.UpdateAsync(reservation, ct);
            await _reservationRepository.SaveChangesAsync(ct);
            
            _logger.LogInformation("Reservation {ReservationId} released", reservationId);
            
            return Result<Unit>.Success(Unit.Default);
        }
        catch (SqlException ex) when (ex.Number == 1205)
        {
            _logger.LogWarning(ex, "Deadlock releasing reservation {ReservationId}", reservationId);
            throw new DatabaseInfrastructureException(
                "Database deadlock releasing reservation", ex.Number, "DB_DEADLOCK", ex);
        }
    }
}
```

### 2.4 Key Takeaways from Inventory Management

| Concept | Implementation |
|---------|----------------|
| **Domain Outcomes** | Out of stock, minimum order quantity, reservation conflicts |
| **Infrastructure Exceptions** | Database deadlock, timeout, lock contention |
| **Concurrency** | Distributed locks for consistent reservation |
| **Bulk Operations** | All-or-nothing semantics with compensation |
| **Reservation Lifecycle** | Active → Confirmed/Released/Expired state machine |

---

## Case Study 3: Healthcare Scheduling Domain

### 3.1 Domain Context

A healthcare scheduling system must handle:
- Provider availability and leave management
- Double-booking prevention (patient safety)
- Insurance verification integration
- EMR system synchronization
- Appointment type rules (urgent care, routine, specialist)

### 3.2 Domain Model

```csharp
// Domain/Healthcare/Appointment.cs
namespace Domain.Healthcare;

public class Appointment
{
    public Guid Id { get; private set; }
    public Guid PatientId { get; private set; }
    public Guid ProviderId { get; private set; }
    public DateTime StartTime { get; private set; }
    public DateTime EndTime { get; private set; }
    public AppointmentType Type { get; private set; }
    public AppointmentStatus Status { get; private set; }
    public string? Reason { get; private set; }
    public bool IsTelehealth { get; private set; }
    public string? InsuranceEligibilityId { get; private set; }
    public bool RequiresReconciliation { get; private set; }
    public DateTime CreatedAt { get; private set; }
    
    private Appointment() { }
    
    public static Appointment Schedule(
        Guid patientId,
        Guid providerId,
        DateTime startTime,
        DateTime endTime,
        AppointmentType type,
        bool isTelehealth = false)
    {
        return new Appointment
        {
            Id = Guid.NewGuid(),
            PatientId = patientId,
            ProviderId = providerId,
            StartTime = startTime,
            EndTime = endTime,
            Type = type,
            Status = AppointmentStatus.Scheduled,
            IsTelehealth = isTelehealth,
            CreatedAt = DateTime.UtcNow
        };
    }
    
    public Result<Unit> Cancel(string reason)
    {
        if (Status != AppointmentStatus.Scheduled && Status != AppointmentStatus.Confirmed)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("appointment.cancel_invalid_state",
                    $"Cannot cancel appointment {Id}. Current status: {Status}"));
        }
        
        if (StartTime < DateTime.UtcNow.AddHours(24))
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("appointment.cancel_window_expired",
                    "Appointments must be cancelled at least 24 hours in advance"));
        }
        
        Status = AppointmentStatus.Cancelled;
        Reason = reason;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> Confirm()
    {
        if (Status != AppointmentStatus.Scheduled)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("appointment.confirm_invalid_state",
                    $"Cannot confirm appointment {Id}. Current status: {Status}"));
        }
        
        Status = AppointmentStatus.Confirmed;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> MarkNoShow()
    {
        if (Status != AppointmentStatus.Scheduled && Status != AppointmentStatus.Confirmed)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("appointment.no_show_invalid_state",
                    $"Cannot mark no-show for appointment {Id}. Current status: {Status}"));
        }
        
        Status = AppointmentStatus.NoShow;
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> Complete()
    {
        if (Status != AppointmentStatus.Confirmed)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("appointment.complete_invalid_state",
                    $"Cannot complete appointment {Id}. Current status: {Status}"));
        }
        
        Status = AppointmentStatus.Completed;
        
        return Result<Unit>.Success(Unit.Default);
    }
}

public enum AppointmentType
{
    Routine,
    UrgentCare,
    Specialist,
    FollowUp,
    Vaccination,
    PhysicalExam
}

public enum AppointmentStatus
{
    Scheduled,
    Confirmed,
    Completed,
    Cancelled,
    NoShow
}

// Domain/Healthcare/ProviderSchedule.cs
public class ProviderSchedule
{
    public Guid ProviderId { get; private set; }
    public DayOfWeek DayOfWeek { get; private set; }
    public TimeOnly StartTime { get; private set; }
    public TimeOnly EndTime { get; private set; }
    public bool IsAvailable { get; private set; }
    
    public bool IsWithinWorkingHours(DateTime time)
    {
        if (!IsAvailable) return false;
        
        var timeOfDay = TimeOnly.FromDateTime(time);
        return timeOfDay >= StartTime && timeOfDay < EndTime;
    }
}
```

### 3.3 Domain Service with Result Pattern

```csharp
// Domain/Services/AppointmentSchedulingService.cs
namespace Domain.Services;

public interface IAppointmentSchedulingService
{
    Task<Result<Appointment>> ScheduleAppointmentAsync(ScheduleAppointmentRequest request, CancellationToken ct);
    Task<Result<Appointment>> RescheduleAppointmentAsync(RescheduleAppointmentRequest request, CancellationToken ct);
    Task<Result<Unit>> CancelAppointmentAsync(CancelAppointmentRequest request, CancellationToken ct);
    Task<Result<IReadOnlyList<TimeSlot>>> GetAvailableSlotsAsync(AvailabilityRequest request, CancellationToken ct);
}

public class AppointmentSchedulingService : IAppointmentSchedulingService
{
    private readonly IAppointmentRepository _appointmentRepository;
    private readonly IPatientRepository _patientRepository;
    private readonly IProviderRepository _providerRepository;
    private readonly IInsuranceVerificationService _insuranceService;
    private readonly IEmrIntegrationService _emrService;
    private readonly ILogger<AppointmentSchedulingService> _logger;
    
    public AppointmentSchedulingService(
        IAppointmentRepository appointmentRepository,
        IPatientRepository patientRepository,
        IProviderRepository providerRepository,
        IInsuranceVerificationService insuranceService,
        IEmrIntegrationService emrService,
        ILogger<AppointmentSchedulingService> logger)
    {
        _appointmentRepository = appointmentRepository;
        _patientRepository = patientRepository;
        _providerRepository = providerRepository;
        _insuranceService = insuranceService;
        _emrService = emrService;
        _logger = logger;
    }
    
    public async Task<Result<Appointment>> ScheduleAppointmentAsync(
        ScheduleAppointmentRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate patient exists
        var patientResult = await _patientRepository.GetByIdAsync(request.PatientId, ct);
        if (patientResult.IsFailure)
        {
            return Result<Appointment>.Failure(patientResult.Error);
        }
        var patient = patientResult.Value;
        
        // DOMAIN OUTCOME: Validate provider exists and is active
        var providerResult = await _providerRepository.GetByIdAsync(request.ProviderId, ct);
        if (providerResult.IsFailure)
        {
            return Result<Appointment>.Failure(providerResult.Error);
        }
        var provider = providerResult.Value;
        
        if (!provider.IsActive)
        {
            return Result<Appointment>.Failure(
                DomainError.BusinessRule("provider.inactive",
                    $"Provider {provider.Name} is not currently accepting appointments"));
        }
        
        // DOMAIN OUTCOME: Validate appointment duration
        var duration = request.EndTime - request.StartTime;
        if (duration < TimeSpan.FromMinutes(15))
        {
            return Result<Appointment>.Failure(
                DomainError.Validation("duration", "Appointment duration must be at least 15 minutes"));
        }
        
        if (duration > provider.MaxAppointmentDuration)
        {
            return Result<Appointment>.Failure(
                DomainError.Validation("duration",
                    $"Appointment duration cannot exceed {provider.MaxAppointmentDuration.TotalMinutes} minutes"));
        }
        
        // DOMAIN OUTCOME: Validate scheduling window
        var daysInAdvance = (request.StartTime.Date - DateTime.UtcNow.Date).Days;
        if (daysInAdvance > provider.MaxAdvanceBookingDays)
        {
            return Result<Appointment>.Failure(
                DomainError.Validation("startTime",
                    $"Cannot book appointments more than {provider.MaxAdvanceBookingDays} days in advance"));
        }
        
        if (daysInAdvance < provider.MinAdvanceBookingDays)
        {
            return Result<Appointment>.Failure(
                DomainError.Validation("startTime",
                    $"Appointments must be booked at least {provider.MinAdvanceBookingDays} days in advance"));
        }
        
        // DOMAIN OUTCOME: Check provider availability
        var isAvailableResult = await _providerRepository.IsAvailableAsync(
            request.ProviderId, request.StartTime, request.EndTime, ct);
            
        if (isAvailableResult.IsFailure)
        {
            return Result<Appointment>.Failure(isAvailableResult.Error);
        }
        
        if (!isAvailableResult.Value)
        {
            return Result<Appointment>.Failure(
                DomainError.Conflict("Provider not available during requested time"));
        }
        
        // DOMAIN OUTCOME: Check for double-booking (patient safety)
        var conflictingResult = await _appointmentRepository.GetConflictingAppointmentsAsync(
            request.ProviderId, request.StartTime, request.EndTime, ct);
            
        if (conflictingResult.IsSuccess && conflictingResult.Value.Any())
        {
            return Result<Appointment>.Failure(
                DomainError.Conflict("Time slot already booked",
                    new { conflictingAppointments = conflictingResult.Value.Select(a => a.Id) }));
        }
        
        // DOMAIN OUTCOME: Check if provider is on leave
        var leaveResult = await _providerRepository.CheckLeaveAsync(
            request.ProviderId, request.StartTime, request.EndTime, ct);
            
        if (leaveResult.IsSuccess && leaveResult.Value.IsOnLeave)
        {
            return Result<Appointment>.Failure(
                DomainError.BusinessRule("provider.on_leave",
                    $"Provider is on leave from {leaveResult.Value.LeaveStart} to {leaveResult.Value.LeaveEnd}"));
        }
        
        // DOMAIN OUTCOME: Insurance verification
        var insuranceResult = await _insuranceService.VerifyEligibilityAsync(
            request.PatientId, request.ProviderId, request.StartTime, ct);
            
        if (insuranceResult.IsFailure)
        {
            return Result<Appointment>.Failure(insuranceResult.Error);
        }
        
        var eligibility = insuranceResult.Value;
        
        if (!eligibility.IsEligible)
        {
            return Result<Appointment>.Failure(
                DomainError.BusinessRule("insurance.not_eligible",
                    $"Insurance verification failed: {eligibility.IneligibilityReason}"));
        }
        
        // Create appointment
        var appointment = Appointment.Schedule(
            request.PatientId,
            request.ProviderId,
            request.StartTime,
            request.EndTime,
            request.AppointmentType,
            request.IsTelehealth);
        
        try
        {
            // INFRASTRUCTURE: Save to local database
            var saveResult = await _appointmentRepository.AddAsync(appointment, ct);
            if (saveResult.IsFailure)
            {
                return Result<Appointment>.Failure(saveResult.Error);
            }
            
            await _appointmentRepository.SaveChangesAsync(ct);
            
            // INFRASTRUCTURE: Sync with EMR system
            try
            {
                var emrResult = await _emrService.CreateAppointmentRecordAsync(
                    new EmrAppointmentRequest
                    {
                        AppointmentId = appointment.Id,
                        PatientId = appointment.PatientId,
                        ProviderId = appointment.ProviderId,
                        StartTime = appointment.StartTime,
                        EndTime = appointment.EndTime,
                        AppointmentType = appointment.Type
                    }, ct);
                    
                if (emrResult.IsFailure)
                {
                    // INFRASTRUCTURE: EMR sync failed - mark for reconciliation
                    _logger.LogError("EMR sync failed for appointment {AppointmentId}: {Error}",
                        appointment.Id, emrResult.Error.Message);
                    appointment.RequiresReconciliation = true;
                    await _appointmentRepository.UpdateAsync(appointment, ct);
                    await _appointmentRepository.SaveChangesAsync(ct);
                }
            }
            catch (HttpRequestException ex) when (ex.StatusCode == HttpStatusCode.ServiceUnavailable)
            {
                // INFRASTRUCTURE EXCEPTION - EMR system down
                _logger.LogWarning(ex, "EMR system unavailable for appointment {AppointmentId}",
                    appointment.Id);
                appointment.RequiresReconciliation = true;
                await _appointmentRepository.UpdateAsync(appointment, ct);
                await _appointmentRepository.SaveChangesAsync(ct);
            }
            
            _logger.LogInformation("Appointment {AppointmentId} scheduled for patient {PatientId} with provider {ProviderId}",
                appointment.Id, request.PatientId, request.ProviderId);
            
            return Result<Appointment>.Success(appointment);
        }
        catch (DbUpdateException ex) when (ex.InnerException?.Message.Contains("unique constraint") == true)
        {
            // INFRASTRUCTURE: Could be domain (double-booking) caught by constraint
            if (ex.InnerException.Message.Contains("IX_Appointments_Provider_Time"))
            {
                return Result<Appointment>.Failure(
                    DomainError.Conflict("Time slot was just booked by another patient"));
            }
            
            _logger.LogError(ex, "Database error scheduling appointment");
            throw new DatabaseInfrastructureException(
                "Database error during appointment scheduling", 0, "DB_ERR", ex);
        }
    }
    
    public async Task<Result<IReadOnlyList<TimeSlot>>> GetAvailableSlotsAsync(
        AvailabilityRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate provider exists
        var providerResult = await _providerRepository.GetByIdAsync(request.ProviderId, ct);
        if (providerResult.IsFailure)
        {
            return Result<IReadOnlyList<TimeSlot>>.Failure(providerResult.Error);
        }
        var provider = providerResult.Value;
        
        // DOMAIN OUTCOME: Validate date range
        if (request.EndDate < request.StartDate)
        {
            return Result<IReadOnlyList<TimeSlot>>.Failure(
                DomainError.Validation("endDate", "End date must be after start date"));
        }
        
        if ((request.EndDate - request.StartDate).Days > 30)
        {
            return Result<IReadOnlyList<TimeSlot>>.Failure(
                DomainError.Validation("dateRange", "Date range cannot exceed 30 days"));
        }
        
        try
        {
            // INFRASTRUCTURE: Get schedule and existing appointments
            var scheduleResult = await _providerRepository.GetScheduleAsync(
                request.ProviderId, request.StartDate, request.EndDate, ct);
                
            if (scheduleResult.IsFailure)
            {
                return Result<IReadOnlyList<TimeSlot>>.Failure(scheduleResult.Error);
            }
            
            var existingAppointments = await _appointmentRepository.GetByProviderAndDateRangeAsync(
                request.ProviderId, request.StartDate, request.EndDate, ct);
            
            // Generate available slots based on working hours minus existing appointments
            var slots = GenerateAvailableSlots(
                scheduleResult.Value,
                existingAppointments,
                request.AppointmentDuration,
                request.AppointmentType);
            
            return Result<IReadOnlyList<TimeSlot>>.Success(slots.AsReadOnly());
        }
        catch (SqlException ex) when (ex.Number == -2)
        {
            _logger.LogError(ex, "Database timeout getting availability");
            throw new DatabaseInfrastructureException(
                "Database timeout retrieving availability", ex.Number, "DB_TIMEOUT", ex);
        }
    }
    
    private List<TimeSlot> GenerateAvailableSlots(
        ProviderSchedule schedule,
        IReadOnlyList<Appointment> existingAppointments,
        int durationMinutes,
        AppointmentType type)
    {
        var slots = new List<TimeSlot>();
        // Implementation would generate time slots based on working hours
        // and filter out booked slots
        return slots;
    }
}
```

### 3.4 Key Takeaways from Healthcare Scheduling

| Concept | Implementation |
|---------|----------------|
| **Domain Outcomes** | Provider unavailable, double-booking, insurance ineligible, leave conflict |
| **Infrastructure Exceptions** | EMR system unavailable, database timeout, insurance service down |
| **Patient Safety** | Double-booking prevention with domain rules |
| **Regulatory Compliance** | Audit logging and reconciliation flags |
| **External Integration** | EMR sync with graceful degradation and retry |

---

## Case Study 4: Logistics Tracking Domain

### 4.1 Domain Context

A logistics tracking system must handle:
- Real-time GPS location updates
- Carrier API integration
- Delivery window management
- Proof of delivery (signature, photo)
- Route optimization with multiple stops

### 4.2 Domain Model

```csharp
// Domain/Logistics/Shipment.cs
namespace Domain.Logistics;

public class Shipment
{
    public Guid Id { get; private set; }
    public string TrackingNumber { get; private set; }
    public Guid CustomerId { get; private set; }
    public Address OriginAddress { get; private set; }
    public Address DestinationAddress { get; private set; }
    public ShipmentStatus Status { get; private set; }
    public DateTime CreatedAt { get; private set; }
    public DateTime? EstimatedDeliveryDate { get; private set; }
    public DateTime? ActualDeliveryDate { get; private set; }
    public DateTime? DeliveryWindowStart { get; private set; }
    public DateTime? DeliveryWindowEnd { get; private set; }
    public bool RequiresSignature { get; private set; }
    public Guid? AssignedDriverId { get; private set; }
    public List<ShipmentLocation> LocationHistory { get; private set; } = new();
    public List<ShipmentEvent> Events { get; private set; } = new();
    
    private Shipment() { }
    
    public static Shipment Create(
        Guid customerId,
        Address origin,
        Address destination,
        bool requiresSignature = false)
    {
        return new Shipment
        {
            Id = Guid.NewGuid(),
            TrackingNumber = GenerateTrackingNumber(),
            CustomerId = customerId,
            OriginAddress = origin,
            DestinationAddress = destination,
            Status = ShipmentStatus.Created,
            CreatedAt = DateTime.UtcNow,
            RequiresSignature = requiresSignature
        };
    }
    
    public Result<Unit> AssignDriver(Guid driverId)
    {
        if (Status != ShipmentStatus.Created && Status != ShipmentStatus.ReadyForPickup)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("shipment.assign_driver_invalid_state",
                    $"Cannot assign driver to shipment {Id}. Current status: {Status}"));
        }
        
        AssignedDriverId = driverId;
        Status = ShipmentStatus.Assigned;
        
        Events.Add(ShipmentEvent.DriverAssigned(driverId, DateTime.UtcNow));
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<Unit> UpdateLocation(GeoCoordinates location, DateTime timestamp, LocationSource source)
    {
        if (Status == ShipmentStatus.Delivered)
        {
            return Result<Unit>.Failure(
                DomainError.BusinessRule("shipment.already_delivered",
                    "Cannot update location for already delivered shipment"));
        }
        
        // DOMAIN RULE: Validate location plausibility
        if (LocationHistory.Any())
        {
            var lastLocation = LocationHistory.Last();
            var distance = CalculateDistance(
                lastLocation.Coordinates.Latitude, lastLocation.Coordinates.Longitude,
                location.Latitude, location.Longitude);
                
            var timeSinceLastUpdate = DateTime.UtcNow - lastLocation.Timestamp;
            var maxPlausibleDistance = 120 * timeSinceLastUpdate.TotalHours; // 120 km/h max
            
            if (distance > maxPlausibleDistance * 1.5)
            {
                // Domain outcome: location is implausible
                return Result<Unit>.Failure(
                    DomainError.BusinessRule("shipment.location_implausible",
                        $"Location update distance {distance:F2}km in {timeSinceLastUpdate.TotalHours:F1} hours exceeds plausible range",
                        new { distance, timeSinceLastUpdate }));
            }
        }
        
        var locationUpdate = new ShipmentLocation
        {
            Id = Guid.NewGuid(),
            ShipmentId = Id,
            Coordinates = location,
            Timestamp = timestamp,
            Source = source
        };
        
        LocationHistory.Add(locationUpdate);
        
        // Update status based on location proximity to destination
        var distanceToDestination = CalculateDistance(
            location.Latitude, location.Longitude,
            DestinationAddress.Coordinates.Latitude, DestinationAddress.Coordinates.Longitude);
            
        if (distanceToDestination < 0.1) // Within 100 meters
        {
            Status = ShipmentStatus.ArrivedAtDestination;
        }
        else if (distanceToDestination < 10) // Within 10 km
        {
            Status = ShipmentStatus.NearDestination;
        }
        
        return Result<Unit>.Success(Unit.Default);
    }
    
    public Result<DeliveryConfirmation> ConfirmDelivery(
        string confirmedBy,
        byte[]? signatureData = null,
        byte[]? photoEvidence = null)
    {
        if (Status == ShipmentStatus.Delivered)
        {
            return Result<DeliveryConfirmation>.Failure(
                DomainError.BusinessRule("shipment.already_delivered",
                    $"Shipment {Id} has already been delivered"));
        }
        
        if (RequiresSignature && (signatureData == null || signatureData.Length == 0))
        {
            return Result<DeliveryConfirmation>.Failure(
                DomainError.Validation("signature", "Signature is required for this shipment"));
        }
        
        // DOMAIN RULE: Check delivery window
        if (DeliveryWindowStart.HasValue && DeliveryWindowEnd.HasValue)
        {
            var now = DateTime.UtcNow;
            if (now < DeliveryWindowStart.Value)
            {
                return Result<DeliveryConfirmation>.Failure(
                    DomainError.BusinessRule("delivery.too_early",
                        $"Delivery attempted before window. Window starts at {DeliveryWindowStart.Value}"));
            }
        }
        
        Status = ShipmentStatus.Delivered;
        ActualDeliveryDate = DateTime.UtcNow;
        
        var confirmation = new DeliveryConfirmation
        {
            Id = Guid.NewGuid(),
            ShipmentId = Id,
            ConfirmedAt = DateTime.UtcNow,
            ConfirmedBy = confirmedBy,
            SignatureData = signatureData,
            PhotoEvidence = photoEvidence
        };
        
        Events.Add(ShipmentEvent.Delivered(confirmedBy, DateTime.UtcNow));
        
        return Result<DeliveryConfirmation>.Success(confirmation);
    }
    
    private static string GenerateTrackingNumber() =>
        $"SHIP{DateTime.UtcNow:yyyyMMdd}{Guid.NewGuid():N}".Substring(0, 16).ToUpper();
    
    private static double CalculateDistance(double lat1, double lon1, double lat2, double lon2)
    {
        // Haversine formula for distance in km
        var R = 6371;
        var dLat = (lat2 - lat1) * Math.PI / 180;
        var dLon = (lon2 - lon1) * Math.PI / 180;
        var a = Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
                Math.Cos(lat1 * Math.PI / 180) * Math.Cos(lat2 * Math.PI / 180) *
                Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
        var c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
        return R * c;
    }
}

public enum ShipmentStatus
{
    Created,
    ReadyForPickup,
    Assigned,
    PickedUp,
    InTransit,
    NearDestination,
    ArrivedAtDestination,
    Delivered,
    Exception,
    Cancelled
}

public record ShipmentLocation
{
    public Guid Id { get; init; }
    public Guid ShipmentId { get; init; }
    public GeoCoordinates Coordinates { get; init; }
    public DateTime Timestamp { get; init; }
    public LocationSource Source { get; init; }
}

public record GeoCoordinates
{
    public double Latitude { get; init; }
    public double Longitude { get; init; }
}

public enum LocationSource
{
    GPS,
    CarrierAPI,
    Manual,
    Geofence
}
```

### 4.3 Domain Service with Result Pattern

```csharp
// Domain/Services/LogisticsTrackingService.cs
namespace Domain.Services;

public interface ILogisticsTrackingService
{
    Task<Result<Shipment>> CreateShipmentAsync(CreateShipmentRequest request, CancellationToken ct);
    Task<Result<Shipment>> UpdateLocationAsync(UpdateLocationRequest request, CancellationToken ct);
    Task<Result<DeliveryConfirmation>> ConfirmDeliveryAsync(ConfirmDeliveryRequest request, CancellationToken ct);
    Task<Result<ShipmentStatus>> GetShipmentStatusAsync(string trackingNumber, CancellationToken ct);
    Task<Result<RouteOptimization>> OptimizeRouteAsync(RouteOptimizationRequest request, CancellationToken ct);
}

public class LogisticsTrackingService : ILogisticsTrackingService
{
    private readonly IShipmentRepository _shipmentRepository;
    private readonly ICarrierIntegrationService _carrierService;
    private readonly IGeocodingService _geocodingService;
    private readonly IRouteOptimizer _routeOptimizer;
    private readonly ILogger<LogisticsTrackingService> _logger;
    
    public LogisticsTrackingService(
        IShipmentRepository shipmentRepository,
        ICarrierIntegrationService carrierService,
        IGeocodingService geocodingService,
        IRouteOptimizer routeOptimizer,
        ILogger<LogisticsTrackingService> logger)
    {
        _shipmentRepository = shipmentRepository;
        _carrierService = carrierService;
        _geocodingService = geocodingService;
        _routeOptimizer = routeOptimizer;
        _logger = logger;
    }
    
    public async Task<Result<Shipment>> CreateShipmentAsync(
        CreateShipmentRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate packages
        if (request.Packages.Count == 0)
        {
            return Result<Shipment>.Failure(
                DomainError.Validation("packages", "Shipment must contain at least one package"));
        }
        
        // DOMAIN OUTCOME: Validate addresses via geocoding
        var originGeoResult = await _geocodingService.GeocodeAddressAsync(request.OriginAddress, ct);
        if (originGeoResult.IsFailure)
        {
            return Result<Shipment>.Failure(
                DomainError.Validation("originAddress", $"Invalid origin address: {originGeoResult.Error.Message}"));
        }
        
        var destinationGeoResult = await _geocodingService.GeocodeAddressAsync(request.DestinationAddress, ct);
        if (destinationGeoResult.IsFailure)
        {
            return Result<Shipment>.Failure(
                DomainError.Validation("destinationAddress", $"Invalid destination address: {destinationGeoResult.Error.Message}"));
        }
        
        request.OriginAddress.Coordinates = originGeoResult.Value;
        request.DestinationAddress.Coordinates = destinationGeoResult.Value;
        
        // DOMAIN OUTCOME: Check if destination is serviceable
        var serviceableResult = await _carrierService.IsServiceableAsync(
            request.DestinationAddress.Country,
            request.DestinationAddress.PostalCode,
            ct);
            
        if (serviceableResult.IsFailure)
        {
            return Result<Shipment>.Failure(serviceableResult.Error);
        }
        
        if (!serviceableResult.Value)
        {
            return Result<Shipment>.Failure(
                DomainError.BusinessRule("destination.not_serviceable",
                    "Destination is not within our service area"));
        }
        
        // Create shipment
        var shipment = Shipment.Create(
            request.CustomerId,
            request.OriginAddress,
            request.DestinationAddress,
            request.RequiresSignature);
        
        try
        {
            // INFRASTRUCTURE: Save locally
            var saveResult = await _shipmentRepository.AddAsync(shipment, ct);
            if (saveResult.IsFailure)
            {
                return Result<Shipment>.Failure(saveResult.Error);
            }
            
            await _shipmentRepository.SaveChangesAsync(ct);
            
            // INFRASTRUCTURE: Register with carrier
            try
            {
                var carrierResult = await _carrierService.RegisterShipmentAsync(
                    new CarrierRegistrationRequest
                    {
                        ShipmentId = shipment.Id,
                        Origin = shipment.OriginAddress,
                        Destination = shipment.DestinationAddress,
                        Packages = request.Packages,
                        ServiceLevel = request.ServiceLevel
                    }, ct);
                    
                if (carrierResult.IsSuccess)
                {
                    shipment.AssignCarrierTrackingNumber(carrierResult.Value.TrackingNumber);
                    await _shipmentRepository.UpdateAsync(shipment, ct);
                    await _shipmentRepository.SaveChangesAsync(ct);
                }
                else
                {
                    // DOMAIN OUTCOME: Carrier registration failed
                    return Result<Shipment>.Failure(carrierResult.Error);
                }
            }
            catch (HttpRequestException ex) when (ex.StatusCode == HttpStatusCode.ServiceUnavailable)
            {
                // INFRASTRUCTURE EXCEPTION: Carrier service down
                _logger.LogWarning(ex, "Carrier service unavailable for shipment {ShipmentId}", shipment.Id);
                shipment.MarkCarrierSyncRequired();
                await _shipmentRepository.UpdateAsync(shipment, ct);
                await _shipmentRepository.SaveChangesAsync(ct);
                // Continue - shipment created, will sync later
            }
            
            return Result<Shipment>.Success(shipment);
        }
        catch (DbUpdateException ex)
        {
            _logger.LogError(ex, "Database error creating shipment");
            throw new DatabaseInfrastructureException(
                "Database error during shipment creation", 0, "DB_ERR", ex);
        }
    }
    
    public async Task<Result<Shipment>> UpdateLocationAsync(
        UpdateLocationRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate tracking number
        if (string.IsNullOrWhiteSpace(request.TrackingNumber))
        {
            return Result<Shipment>.Failure(
                DomainError.Validation("trackingNumber", "Tracking number is required"));
        }
        
        var shipmentResult = await _shipmentRepository.GetByTrackingNumberAsync(request.TrackingNumber, ct);
        if (shipmentResult.IsFailure)
        {
            return Result<Shipment>.Failure(shipmentResult.Error);
        }
        
        var shipment = shipmentResult.Value;
        
        // DOMAIN OUTCOME: Validate location
        if (request.Location.Latitude < -90 || request.Location.Latitude > 90 ||
            request.Location.Longitude < -180 || request.Location.Longitude > 180)
        {
            return Result<Shipment>.Failure(
                DomainError.Validation("location", "Invalid coordinates"));
        }
        
        // Update location (domain logic with plausibility check)
        var updateResult = shipment.UpdateLocation(
            request.Location,
            request.Timestamp ?? DateTime.UtcNow,
            request.Source);
            
        if (updateResult.IsFailure)
        {
            return Result<Shipment>.Failure(updateResult.Error);
        }
        
        try
        {
            var saveResult = await _shipmentRepository.UpdateAsync(shipment, ct);
            if (saveResult.IsFailure)
            {
                return Result<Shipment>.Failure(saveResult.Error);
            }
            
            await _shipmentRepository.SaveChangesAsync(ct);
            
            // INFRASTRUCTURE: Publish to real-time tracking hub (fire and forget)
            try
            {
                await _carrierService.PublishLocationUpdateAsync(shipment.TrackingNumber, request.Location, ct);
            }
            catch (Exception ex)
            {
                _logger.LogWarning(ex, "Failed to publish location update for {TrackingNumber}", request.TrackingNumber);
                // Non-critical, continue
            }
            
            return Result<Shipment>.Success(shipment);
        }
        catch (DbUpdateConcurrencyException ex)
        {
            _logger.LogWarning(ex, "Concurrency conflict updating location for {TrackingNumber}", request.TrackingNumber);
            throw new DatabaseInfrastructureException(
                "Concurrency conflict updating location", 0, "DB_CONCURRENCY", ex);
        }
    }
    
    public async Task<Result<DeliveryConfirmation>> ConfirmDeliveryAsync(
        ConfirmDeliveryRequest request,
        CancellationToken ct)
    {
        var shipmentResult = await _shipmentRepository.GetByTrackingNumberAsync(request.TrackingNumber, ct);
        if (shipmentResult.IsFailure)
        {
            return Result<DeliveryConfirmation>.Failure(shipmentResult.Error);
        }
        
        var shipment = shipmentResult.Value;
        
        // DOMAIN OUTCOME: Confirm delivery (includes signature validation)
        var confirmationResult = shipment.ConfirmDelivery(
            request.ConfirmedBy,
            request.SignatureData,
            request.PhotoEvidence);
            
        if (confirmationResult.IsFailure)
        {
            return Result<DeliveryConfirmation>.Failure(confirmationResult.Error);
        }
        
        try
        {
            var saveResult = await _shipmentRepository.UpdateAsync(shipment, ct);
            if (saveResult.IsFailure)
            {
                return Result<DeliveryConfirmation>.Failure(saveResult.Error);
            }
            
            await _shipmentRepository.AddDeliveryConfirmationAsync(confirmationResult.Value, ct);
            await _shipmentRepository.SaveChangesAsync(ct);
            
            // INFRASTRUCTURE: Notify carrier of delivery
            try
            {
                await _carrierService.ReportDeliveryAsync(
                    shipment.CarrierTrackingNumber,
                    confirmationResult.Value,
                    ct);
            }
            catch (HttpRequestException ex)
            {
                _logger.LogError(ex, "Failed to notify carrier of delivery for {TrackingNumber}", request.TrackingNumber);
                shipment.MarkCarrierSyncRequired();
                await _shipmentRepository.UpdateAsync(shipment, ct);
                await _shipmentRepository.SaveChangesAsync(ct);
            }
            
            _logger.LogInformation("Delivery confirmed for shipment {TrackingNumber}", request.TrackingNumber);
            
            return Result<DeliveryConfirmation>.Success(confirmationResult.Value);
        }
        catch (DbUpdateException ex)
        {
            _logger.LogError(ex, "Database error confirming delivery for {TrackingNumber}", request.TrackingNumber);
            throw new DatabaseInfrastructureException(
                "Database error during delivery confirmation", 0, "DB_ERR", ex);
        }
    }
    
    public async Task<Result<RouteOptimization>> OptimizeRouteAsync(
        RouteOptimizationRequest request,
        CancellationToken ct)
    {
        // DOMAIN OUTCOME: Validate shipments exist
        var shipmentsResult = await _shipmentRepository.GetByIdsAsync(request.ShipmentIds, ct);
        if (shipmentsResult.IsFailure)
        {
            return Result<RouteOptimization>.Failure(shipmentsResult.Error);
        }
        
        var shipments = shipmentsResult.Value;
        
        if (shipments.Count == 0)
        {
            return Result<RouteOptimization>.Failure(
                DomainError.Validation("shipmentIds", "At least one shipment is required"));
        }
        
        try
        {
            // INFRASTRUCTURE: Call route optimization service
            var optimizationResult = await _routeOptimizer.OptimizeAsync(
                request.StartingLocation,
                shipments.Select(s => s.DestinationAddress.Coordinates).ToList(),
                ct);
                
            if (optimizationResult.IsFailure)
            {
                return Result<RouteOptimization>.Failure(optimizationResult.Error);
            }
            
            var optimization = optimizationResult.Value;
            
            // DOMAIN OUTCOME: Validate optimization results
            if (optimization.TotalDistance > request.MaxDistanceKm)
            {
                return Result<RouteOptimization>.Failure(
                    DomainError.BusinessRule("route.distance_exceeded",
                        $"Optimized route distance {optimization.TotalDistance:F1}km exceeds maximum {request.MaxDistanceKm}km"));
            }
            
            return Result<RouteOptimization>.Success(optimization);
        }
        catch (TimeoutException ex)
        {
            _logger.LogError(ex, "Route optimization timeout");
            throw new ExternalServiceInfrastructureException(
                "RouteOptimizer",
                "Route optimization timed out",
                isTransient: true,
                errorCode: "ROUTE_TIMEOUT",
                innerException: ex);
        }
    }
}
```

### 4.4 Key Takeaways from Logistics Tracking

| Concept | Implementation |
|---------|----------------|
| **Domain Outcomes** | Invalid address, unserviceable location, implausible GPS update, delivery window violation |
| **Infrastructure Exceptions** | Carrier API unavailable, geocoding service timeout, route optimization failure |
| **Real-time Tracking** | Location plausibility validation with distance-over-time checks |
| **Proof of Delivery** | Signature and photo evidence with business rules |
| **Carrier Integration** | Graceful degradation with sync-required flags |

---

## Cross-Domain Patterns Summary

| Pattern | Payment | Inventory | Healthcare | Logistics |
|---------|---------|----------|------------|----------|
| **Domain State Machine** | Payment Status | Reservation Status | Appointment Status | Shipment Status |
| **Idempotency** | Idempotency Key | N/A | N/A | Tracking Number |
| **External Integration** | Payment Gateway | N/A | EMR, Insurance | Carrier, Geocoding |
| **Concurrency Control** | N/A | Distributed Lock | N/A | Optimistic Concurrency |
| **Compensation** | N/A | Release Reservation | N/A | Carrier Sync Flag |
| **Plausibility Check** | Fraud Detection | N/A | N/A | Location Distance |

---

## What We Learned in This Story

| Domain | Key Learning |
|--------|--------------|
| **Payment Processing** | Idempotency keys prevent duplicate charges; fraud detection is a domain rule before gateway calls |
| **Inventory Management** | Distributed locks prevent overselling; all-or-nothing semantics with compensation |
| **Healthcare Scheduling** | Double-booking prevention is patient safety; EMR sync failures require reconciliation |
| **Logistics Tracking** | Location plausibility validates GPS data; delivery windows enforce business SLAs |

---

## Next Story

The next story in the series provides the complete infrastructure resilience implementation.

---

**6. 🛡️ Clean Architecture Anti-Pattern - Exception: Infrastructure Resilience - Part 6** – Global exception handling middleware, Polly v8 retry policies, circuit breakers, and transient vs non-transient failure classification. Health check integration, service discovery patterns, and custom infrastructure exception types. Complete middleware pipeline configuration for .NET 10 applications.

---

## References to Previous Stories

This story applies the principles established in:

**1. 🏛️ Clean Architecture Anti-Pattern - Exception: A .NET Developer's Guide - Part 1** – Architectural violation and decision framework.

**2. 🎭 Clean Architecture Anti-Pattern - Exception: Domain Logic in Disguise - Part 2** – Performance optimization by eliminating exceptions for domain outcomes.

**3. 🔍 Clean Architecture Anti-Pattern - Exception: Defining the Boundary - Part 3** – Taxonomy applied throughout all case studies.

**4. ⚙️ Clean Architecture Anti-Pattern - Exception: Building the Result Pattern - Part 4** – Result<T> and DomainError implementation used in all services.

---

## Series Overview

1. **🏛️ Clean Architecture Anti-Pattern - Exception: A .NET Developer's Guide - Part 1** – Foundational principles, architectural violation, domain-infrastructure distinction, Result pattern, and decision framework.

2. **🎭 Clean Architecture Anti-Pattern - Exception: Domain Logic in Disguise - Part 2** – Performance implications of exception-based domain logic. Stack trace overhead, GC pressure analysis, and why expected outcomes should never throw exceptions.

3. **🔍 Clean Architecture Anti-Pattern - Exception: Defining the Boundary - Part 3** – Comprehensive taxonomy distinguishing infrastructure exceptions from domain outcomes. Decision matrices and classification patterns across all infrastructure layers.

4. **⚙️ Clean Architecture Anti-Pattern - Exception: Building the Result Pattern - Part 4** – Complete implementation of Result<T> and DomainError with functional extensions. Source generation, .NET 10 features, and API design best practices.

5. **🏢 Clean Architecture Anti-Pattern - Exception: Across Real-World Domains - Part 5** – Four complete case studies: Payment Processing, Inventory Management, Healthcare Scheduling, and Logistics Tracking. *(This Story)*

6. **🛡️ Clean Architecture Anti-Pattern - Exception: Infrastructure Resilience - Part 6** – Global exception handling middleware, Polly retry policies, circuit breakers, and health check integration.

7. **🧪 Clean Architecture Anti-Pattern - Exception: Testing & Observability - Part 7** – Unit testing domain logic without exceptions, infrastructure failure testing, OpenTelemetry, metrics with .NET Meters, and production dashboards.

8. **🚀 Clean Architecture Anti-Pattern - Exception: The Road Ahead - Part 8** – Implementation checklist, migration strategies, .NET 10 roadmap, and Native AOT compatibility.

---

---
*� Questions? Drop a response - I read and reply to every comment.*
*📌 Save this story to your reading list - it helps other engineers discover it.*
**🔗 Follow me →**
- [**Medium**](mvineetsharma.medium.com) - mvineetsharma.medium.com
- [**LinkedIn**](www.linkedin.com/in/vineet-sharma-architect) -  www.linkedin.com/in/vineet-sharma-architect

*In-depth .NET, Node.js, Python, Cloud Architecture, and System Design. New articles weekly*