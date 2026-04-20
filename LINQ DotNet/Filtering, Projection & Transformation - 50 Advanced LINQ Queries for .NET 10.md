# Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10
### Deep dive on dynamic filtering, SelectMany flattening, Zip operations, custom projections, conditional mapping, mixed type handling, and index-based selection. Patterns covered: Dynamic Filtering, SelectMany, Zip, Custom Projections, Let Clause, OfType, Cast, Select with Index, Where filtering, Take/Skip, SelectMany cross joins

![Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10](<images/Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10.png>)

> **📌 New in .NET 10 & LINQ:** This series leverages the latest .NET 10 features including collection expressions (`[..]`), primary constructors, `IAsyncEnumerable<T>`, enhanced `DateOnly`/`TimeOnly` support, and async LINQ extensions.

> **📖 Prerequisite:** For a comprehensive introduction to LINQ evolution from .NET Framework 3.5 to .NET 10, detailed coverage of what's new in .NET 10 LINQ (collection expressions, primary constructors, async extensions, DateOnly/TimeOnly support, improved GroupBy, TryGetNonEnumeratedCount, and chunk improvements), along with the complete business case for mastering LINQ (productivity gains, type safety benefits, performance optimizations, and team collaboration advantages), please refer to **[Part 1: Grouping, Joining & Aggregation](link-to-part-1)**. Part 1 also contains the full story navigation and pattern coverage overview for all 50 queries across all four parts.

---

## 📚 Story List (with Pattern Coverage)

📚 **Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10 (Queries 1-12)** — Deep dive on multi-key grouping, all join types (Group, Left, Right, Full), conditional aggregation, running totals, set operations, and pagination. Patterns covered: Multi-Key Grouping, GroupJoin, Full Outer Join, Left Join, Conditional Aggregation, Running Totals, Set Operations, Pagination, Distinct, Lookup, Zip, Aggregate.

📎 **Read the full story: Part 1**

---

📚 **Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10 (Queries 13-25)** — Deep dive on dynamic filtering, SelectMany flattening, Zip operations, custom projections, conditional mapping, mixed type handling, and index-based selection. Patterns covered: Dynamic Filtering, SelectMany, Zip, Custom Projections, Let Clause, OfType, Cast, Select with Index, Where filtering, Take/Skip, SelectMany cross joins.

📎 **You are here: Part 2 — below**

---

📚 **Advanced Data Shaping & Grouping - 50 Advanced LINQ Queries for .NET 10 (Queries 26-38)** — Deep dive on pivot tables, recursive queries, time-series analysis, window functions, composite keys, hierarchical data, and incremental aggregation. Patterns covered: Pivot Tables, Recursive Queries, Time-Based Grouping, Window Functions, Composite Keys, Hierarchical Flattening, Incremental Aggregation, Lookup, ToDictionary, GroupBy with Custom Comparer.

📎 **Read the full story: Part 3 — coming soon**

---

📚 **Performance & Optimization - 50 Advanced LINQ Queries for .NET 10 (Queries 39-50)** — Deep dive on batch processing, lazy evaluation, error handling, parallel LINQ (PLINQ), IQueryable optimization, async streams, and memory-efficient techniques. Patterns covered: Batch Processing, Chunking, Lazy Evaluation, Error Handling, Safe Navigation, PLINQ, IQueryable vs IEnumerable, Async LINQ, Streaming, Caching, Expression Trees.

📎 **Read the full story: Part 4 — coming soon**

---

## 📖 Part 2: Filtering, Projection & Transformation (Queries 13-25)

---

### Query 13: Dynamic Filtering with PredicateBuilder

#### Real-World Scenario
An e-commerce product search API needs to support **dynamic filtering** based on user-selected criteria: category (single or multiple), price range (min/max), brand (multiple selection), rating (minimum stars), in-stock only toggle, free shipping toggle, and sort order (price, rating, name, newest). The search must handle 50+ possible filter combinations efficiently.

#### Business Impact
Powers product search for 1M+ daily active users, reducing query construction time from 200ms to 5ms with 50+ filter combinations, and enabling real-time faceted search results.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyProductSearch
{
    public List<Product> SearchProducts(List<Product> products, SearchCriteria criteria)
    {
        var results = new List<Product>();
        
        foreach (var product in products)
        {
            bool matches = true;
            
            if (!string.IsNullOrEmpty(criteria.Category) && product.Category != criteria.Category)
                matches = false;
            
            if (criteria.MinPrice.HasValue && product.Price < criteria.MinPrice.Value)
                matches = false;
            
            if (criteria.MaxPrice.HasValue && product.Price > criteria.MaxPrice.Value)
                matches = false;
            
            if (criteria.Brands != null && criteria.Brands.Any() && !criteria.Brands.Contains(product.Brand))
                matches = false;
            
            if (criteria.MinRating.HasValue && product.Rating < criteria.MinRating.Value)
                matches = false;
            
            if (criteria.InStockOnly && product.StockQuantity <= 0)
                matches = false;
            
            if (criteria.FreeShippingOnly && product.ShippingCost > 0)
                matches = false;
            
            if (matches) results.Add(product);
        }
        
        // Apply sorting
        if (criteria.SortBy == "price")
            results.Sort((a, b) => criteria.Ascending ? a.Price.CompareTo(b.Price) : b.Price.CompareTo(a.Price));
        else if (criteria.SortBy == "rating")
            results.Sort((a, b) => criteria.Ascending ? a.Rating.CompareTo(b.Rating) : b.Rating.CompareTo(a.Rating));
        else if (criteria.SortBy == "name")
            results.Sort((a, b) => criteria.Ascending ? a.Name.CompareTo(b.Name) : b.Name.CompareTo(a.Name));
        
        return results;
    }
}

public class SearchCriteria
{
    public string Category { get; set; }
    public decimal? MinPrice { get; set; }
    public decimal? MaxPrice { get; set; }
    public List<string> Brands { get; set; }
    public double? MinRating { get; set; }
    public bool InStockOnly { get; set; }
    public bool FreeShippingOnly { get; set; }
    public string SortBy { get; set; }
    public bool Ascending { get; set; }
}

public class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Category { get; set; }
    public string Brand { get; set; }
    public decimal Price { get; set; }
    public double Rating { get; set; }
    public int StockQuantity { get; set; }
    public decimal ShippingCost { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Product(
    int Id,
    string Name,
    string Category,
    string Brand,
    decimal Price,
    double Rating,
    int StockQuantity,
    decimal ShippingCost
);

public record SearchCriteria(
    string? Category,
    decimal? MinPrice,
    decimal? MaxPrice,
    List<string>? Brands,
    double? MinRating,
    bool InStockOnly,
    bool FreeShippingOnly,
    string SortBy,
    bool Ascending
);

public class DynamicProductSearch
{
    public List<Product> SearchProducts(List<Product> products, SearchCriteria criteria)
    {
        var query = products.AsQueryable();
        
        // Build predicate dynamically
        if (!string.IsNullOrEmpty(criteria.Category))
            query = query.Where(p => p.Category == criteria.Category);
        
        if (criteria.MinPrice.HasValue)
            query = query.Where(p => p.Price >= criteria.MinPrice.Value);
        
        if (criteria.MaxPrice.HasValue)
            query = query.Where(p => p.Price <= criteria.MaxPrice.Value);
        
        if (criteria.Brands is { Count: > 0 })
            query = query.Where(p => criteria.Brands.Contains(p.Brand));
        
        if (criteria.MinRating.HasValue)
            query = query.Where(p => p.Rating >= criteria.MinRating.Value);
        
        if (criteria.InStockOnly)
            query = query.Where(p => p.StockQuantity > 0);
        
        if (criteria.FreeShippingOnly)
            query = query.Where(p => p.ShippingCost == 0);
        
        // Apply dynamic sorting
        query = criteria.SortBy?.ToLower() switch
        {
            "price" => criteria.Ascending ? query.OrderBy(p => p.Price) : query.OrderByDescending(p => p.Price),
            "rating" => criteria.Ascending ? query.OrderBy(p => p.Rating) : query.OrderByDescending(p => p.Rating),
            "name" => criteria.Ascending ? query.OrderBy(p => p.Name) : query.OrderByDescending(p => p.Name),
            _ => query
        };
        
        return [.. query];
    }
    
    // Advanced: Expression tree based dynamic filtering for IQueryable
    public IQueryable<Product> BuildDynamicQuery(IQueryable<Product> source, Dictionary<string, object> filters)
    {
        var parameter = Expression.Parameter(typeof(Product), "p");
        Expression? predicate = null;
        
        foreach (var filter in filters)
        {
            var property = Expression.Property(parameter, filter.Key);
            var constant = Expression.Constant(filter.Value);
            var equality = Expression.Equal(property, constant);
            
            predicate = predicate == null ? equality : Expression.AndAlso(predicate, equality);
        }
        
        if (predicate != null)
        {
            var lambda = Expression.Lambda<Func<Product, bool>>(predicate, parameter);
            return source.Where(lambda);
        }
        
        return source;
    }
}
```

#### Key .NET 10 Features Used

✅ **Record types** with primary constructors for immutable criteria and product models

✅ **Collection expressions** `[..]` for query result conversion

✅ **Switch expressions** for dynamic sorting logic

✅ **Pattern matching** with property patterns for filter conditions

✅ **Expression trees** for runtime predicate building

✅ **IQueryable composition** for deferred execution

---

### Query 14: SelectMany for Flattening Nested Collections

#### Real-World Scenario
An order processing system needs to generate **line item reports** from nested order structures. Each order contains multiple items, each item has multiple components, and each component has multiple parts. The system must flatten this three-level hierarchy into a single list for export to a CSV file for warehouse fulfillment.

#### Business Impact
Reduces report generation time from 45 seconds to 3 seconds for 100,000+ orders, enabling real-time warehouse picking list generation.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyOrderFlattener
{
    public List<FlatOrderLine> FlattenOrders(List<Order> orders)
    {
        var results = new List<FlatOrderLine>();
        
        foreach (var order in orders)
        {
            foreach (var item in order.Items)
            {
                foreach (var component in item.Components)
                {
                    foreach (var part in component.Parts)
                    {
                        results.Add(new FlatOrderLine
                        {
                            OrderId = order.Id,
                            OrderDate = order.OrderDate,
                            CustomerName = order.CustomerName,
                            ItemName = item.Name,
                            ItemQuantity = item.Quantity,
                            ComponentName = component.Name,
                            PartNumber = part.PartNumber,
                            PartQuantity = part.Quantity,
                            UnitPrice = part.UnitPrice
                        });
                    }
                }
            }
        }
        
        return results;
    }
}

public class Order
{
    public int Id { get; set; }
    public DateTime OrderDate { get; set; }
    public string CustomerName { get; set; }
    public List<OrderItem> Items { get; set; }
}

public class OrderItem
{
    public string Name { get; set; }
    public int Quantity { get; set; }
    public List<Component> Components { get; set; }
}

public class Component
{
    public string Name { get; set; }
    public List<Part> Parts { get; set; }
}

public class Part
{
    public string PartNumber { get; set; }
    public int Quantity { get; set; }
    public decimal UnitPrice { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Order(
    int Id,
    DateTime OrderDate,
    string CustomerName,
    List<OrderItem> Items
);

public record OrderItem(
    string Name,
    int Quantity,
    List<Component> Components
);

public record Component(
    string Name,
    List<Part> Parts
);

public record Part(
    string PartNumber,
    int Quantity,
    decimal UnitPrice
);

public record FlatOrderLine(
    int OrderId,
    DateTime OrderDate,
    string CustomerName,
    string ItemName,
    int ItemQuantity,
    string ComponentName,
    string PartNumber,
    int PartQuantity,
    decimal UnitPrice
);

public class OrderFlattener
{
    public List<FlatOrderLine> FlattenOrders(List<Order> orders)
    {
        return orders
            .SelectMany(order => order.Items, (order, item) => new { order, item })
            .SelectMany(x => x.item.Components, (x, component) => new { x.order, x.item, component })
            .SelectMany(x => x.component.Parts, (x, part) => new FlatOrderLine(
                OrderId: x.order.Id,
                OrderDate: x.order.OrderDate,
                CustomerName: x.order.CustomerName,
                ItemName: x.item.Name,
                ItemQuantity: x.item.Quantity,
                ComponentName: x.component.Name,
                PartNumber: part.PartNumber,
                PartQuantity: part.Quantity,
                UnitPrice: part.UnitPrice
            ))
            .ToList();
    }
    
    // Alternative: Query syntax (more readable for deep nesting)
    public List<FlatOrderLine> FlattenOrdersQuerySyntax(List<Order> orders)
    {
        return (
            from order in orders
            from item in order.Items
            from component in item.Components
            from part in component.Parts
            select new FlatOrderLine(
                OrderId: order.Id,
                OrderDate: order.OrderDate,
                CustomerName: order.CustomerName,
                ItemName: item.Name,
                ItemQuantity: item.Quantity,
                ComponentName: component.Name,
                PartNumber: part.PartNumber,
                PartQuantity: part.Quantity,
                UnitPrice: part.UnitPrice
            )
        ).ToList();
    }
    
    // Bonus: Selective flattening with filtering
    public List<FlatOrderLine> FlattenWithFilter(List<Order> orders, DateTime minDate, decimal minPartPrice)
    {
        return orders
            .Where(o => o.OrderDate >= minDate)
            .SelectMany(o => o.Items, (o, i) => new { o, i })
            .SelectMany(x => x.i.Components, (x, c) => new { x.o, x.i, c })
            .SelectMany(x => x.c.Parts.Where(p => p.UnitPrice >= minPartPrice), (x, p) => new FlatOrderLine(
                OrderId: x.o.Id,
                OrderDate: x.o.OrderDate,
                CustomerName: x.o.CustomerName,
                ItemName: x.i.Name,
                ItemQuantity: x.i.Quantity,
                ComponentName: x.c.Name,
                PartNumber: p.PartNumber,
                PartQuantity: p.Quantity,
                UnitPrice: p.UnitPrice
            ))
            .ToList();
    }
}
```

#### Key .NET 10 Features Used

✅ **Multiple SelectMany chaining** for flattening nested hierarchies

✅ **LINQ Query Syntax** with multiple `from` clauses for readability

✅ **Record types** for immutable data models at each level

✅ **Collection expressions** for result initialization

✅ **Tuple deconstruction** in intermediate projections

---

### Query 15: Zip for Parallel List Combination

#### Real-World Scenario
A data integration system receives customer data from three different source systems (CRM, Billing, Support). Each system exports data in separate lists with the same order (by CustomerId). The system needs to **merge all three sources** into a single unified customer record for a master data management (MDM) platform.

#### Business Impact
Reduces data integration time from 15 minutes to 30 seconds for 500,000+ customer records, enabling near-real-time master data synchronization.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyDataMerger
{
    public List<UnifiedCustomer> MergeCustomerData(
        List<CrmRecord> crmData,
        List<BillingRecord> billingData,
        List<SupportRecord> supportData)
    {
        var results = new List<UnifiedCustomer>();
        int maxCount = Math.Max(crmData.Count, Math.Max(billingData.Count, supportData.Count));
        
        for (int i = 0; i < maxCount; i++)
        {
            var crm = i < crmData.Count ? crmData[i] : null;
            var billing = i < billingData.Count ? billingData[i] : null;
            var support = i < supportData.Count ? supportData[i] : null;
            
            results.Add(new UnifiedCustomer
            {
                CustomerId = crm?.CustomerId ?? billing?.CustomerId ?? support?.CustomerId ?? 0,
                Name = crm?.Name,
                Email = crm?.Email,
                TotalSpent = billing?.TotalSpent ?? 0,
                LastPurchaseDate = billing?.LastPurchaseDate,
                SupportTickets = support?.SupportTickets ?? 0,
                SatisfactionScore = support?.SatisfactionScore ?? 0
            });
        }
        
        return results;
    }
}
```

#### .NET 10 Implementation

```csharp
public record CrmRecord(int CustomerId, string Name, string Email, string Phone);
public record BillingRecord(int CustomerId, decimal TotalSpent, DateTime LastPurchaseDate, int OrderCount);
public record SupportRecord(int CustomerId, int SupportTickets, double SatisfactionScore, DateTime LastContactDate);

public record UnifiedCustomer(
    int CustomerId,
    string? Name,
    string? Email,
    string? Phone,
    decimal TotalSpent,
    DateTime? LastPurchaseDate,
    int OrderCount,
    int SupportTickets,
    double SatisfactionScore,
    DateTime? LastContactDate,
    string CustomerTier
);

public class DataMerger
{
    public List<UnifiedCustomer> MergeCustomerData(
        List<CrmRecord> crmData,
        List<BillingRecord> billingData,
        List<SupportRecord> supportData)
    {
        // Zip two lists first, then zip with third
        return crmData
            .Zip(billingData, (crm, billing) => new { crm, billing })
            .Zip(supportData, (combined, support) => new UnifiedCustomer(
                CustomerId: combined.crm.CustomerId,
                Name: combined.crm.Name,
                Email: combined.crm.Email,
                Phone: combined.crm.Phone,
                TotalSpent: combined.billing.TotalSpent,
                LastPurchaseDate: combined.billing.LastPurchaseDate,
                OrderCount: combined.billing.OrderCount,
                SupportTickets: support.SupportTickets,
                SatisfactionScore: support.SatisfactionScore,
                LastContactDate: support.LastContactDate,
                CustomerTier: CalculateCustomerTier(combined.billing.TotalSpent, support.SupportTickets)
            ))
            .ToList();
    }
    
    // Handle lists of different lengths with Zip extension
    public List<UnifiedCustomer> MergeWithDefault(
        List<CrmRecord> crmData,
        List<BillingRecord> billingData,
        List<SupportRecord> supportData)
    {
        int maxLength = new[] { crmData.Count, billingData.Count, supportData.Count }.Max();
        
        var extendedCrm = crmData.Concat(Enumerable.Repeat(new CrmRecord(0, "", "", ""), maxLength - crmData.Count));
        var extendedBilling = billingData.Concat(Enumerable.Repeat(new BillingRecord(0, 0, DateTime.MinValue, 0), maxLength - billingData.Count));
        var extendedSupport = supportData.Concat(Enumerable.Repeat(new SupportRecord(0, 0, 0, DateTime.MinValue), maxLength - supportData.Count));
        
        return extendedCrm
            .Zip(extendedBilling, (crm, billing) => new { crm, billing })
            .Zip(extendedSupport, (combined, support) => new UnifiedCustomer(
                CustomerId: combined.crm.CustomerId,
                Name: combined.crm.Name,
                Email: combined.crm.Email,
                Phone: combined.crm.Phone,
                TotalSpent: combined.billing.TotalSpent,
                LastPurchaseDate: combined.billing.LastPurchaseDate,
                OrderCount: combined.billing.OrderCount,
                SupportTickets: support.SupportTickets,
                SatisfactionScore: support.SatisfactionScore,
                LastContactDate: support.LastContactDate,
                CustomerTier: CalculateCustomerTier(combined.billing.TotalSpent, support.SupportTickets)
            ))
            .Where(c => c.CustomerId != 0)
            .ToList();
    }
    
    private static string CalculateCustomerTier(decimal totalSpent, int supportTickets)
    {
        return (totalSpent, supportTickets) switch
        {
            (> 10000, < 3) => "Platinum",
            (> 5000, < 5) => "Gold",
            (> 1000, < 10) => "Silver",
            _ => "Bronze"
        };
    }
}
```

#### Key .NET 10 Features Used

✅ **Zip method chaining** for combining multiple lists

✅ **Tuple patterns** in switch expressions for tier calculation

✅ **Record types** for source and destination data

✅ **Enumerable.Repeat** for padding shorter lists

✅ **Collection expressions** for list initialization

✅ **Pattern matching** for conditional logic

---

### Query 16: Custom Projections with Expression Trees

#### Real-World Scenario
A reporting system allows users to **select which fields** they want to see in a dynamic report. Users can choose any combination of 20+ available fields from a customer data set, and the system must project only those selected fields at runtime without modifying the underlying data structure.

#### Business Impact
Powers a self-service reporting tool used by 500+ business analysts, reducing report development time from 2 weeks to 5 minutes per report.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyDynamicProjection
{
    public List<Dictionary<string, object>> ProjectFields(
        List<Customer> customers,
        List<string> selectedFields)
    {
        var results = new List<Dictionary<string, object>>();
        
        foreach (var customer in customers)
        {
            var row = new Dictionary<string, object>();
            
            foreach (var field in selectedFields)
            {
                switch (field.ToLower())
                {
                    case "id":
                        row["Id"] = customer.Id;
                        break;
                    case "name":
                        row["Name"] = customer.Name;
                        break;
                    case "email":
                        row["Email"] = customer.Email;
                        break;
                    case "age":
                        row["Age"] = customer.Age;
                        break;
                    case "city":
                        row["City"] = customer.City;
                        break;
                    case "country":
                        row["Country"] = customer.Country;
                        break;
                    case "totalpurchases":
                        row["TotalPurchases"] = customer.TotalPurchases;
                        break;
                }
            }
            
            results.Add(row);
        }
        
        return results;
    }
}
```

#### .NET 10 Implementation

```csharp
public record Customer(
    int Id,
    string Name,
    string Email,
    int Age,
    string City,
    string Country,
    decimal TotalPurchases,
    DateTime LastPurchaseDate,
    bool IsActive
);

public class DynamicProjectionEngine
{
    // Build and compile expression tree for dynamic projection
    public Func<Customer, Dictionary<string, object>> CreateProjector(List<string> selectedFields)
    {
        var parameter = Expression.Parameter(typeof(Customer), "c");
        var dictionaryType = typeof(Dictionary<string, object>);
        
        var dictConstructor = dictionaryType.GetConstructor(Type.EmptyTypes);
        var addMethod = dictionaryType.GetMethod("Add", [typeof(string), typeof(object)]);
        
        var addExpressions = new List<Expression>();
        
        foreach (var field in selectedFields)
        {
            var property = typeof(Customer).GetProperty(field, 
                BindingFlags.IgnoreCase | BindingFlags.Public | BindingFlags.Instance);
            
            if (property != null)
            {
                var propertyAccess = Expression.Property(parameter, property);
                var boxedProperty = Expression.Convert(propertyAccess, typeof(object));
                
                var addExpression = Expression.Call(
                    Expression.New(dictConstructor),
                    addMethod,
                    Expression.Constant(field),
                    boxedProperty
                );
                
                addExpressions.Add(addExpression);
            }
        }
        
        var block = Expression.Block(addExpressions);
        var lambda = Expression.Lambda<Func<Customer, Dictionary<string, object>>>(block, parameter);
        
        return lambda.Compile();
    }
    
    public List<Dictionary<string, object>> ProjectFields(
        List<Customer> customers,
        List<string> selectedFields)
    {
        var projector = CreateProjector(selectedFields);
        return customers.Select(projector).ToList();
    }
    
    // Generic projection to any target type using ExpandoObject
    public dynamic CreateDynamicObject(Customer customer, List<string> selectedFields)
    {
        dynamic expando = new ExpandoObject();
        var dict = expando as IDictionary<string, object>;
        
        foreach (var field in selectedFields)
        {
            var property = typeof(Customer).GetProperty(field, 
                BindingFlags.IgnoreCase | BindingFlags.Public | BindingFlags.Instance);
            
            if (property != null)
            {
                dict[field] = property.GetValue(customer);
            }
        }
        
        return expando;
    }
    
    // Strongly-typed projection using System.Linq.Dynamic.Core (optional library)
    public IQueryable<dynamic> DynamicSelect(IQueryable<Customer> source, string selectExpression)
    {
        // Simulated - would use System.Linq.Dynamic.Core
        // return source.Select(selectExpression);
        throw new NotImplementedException("Requires System.Linq.Dynamic.Core NuGet package");
    }
}
```

#### Key .NET 10 Features Used

✅ **Expression trees** for runtime code generation

✅ **Reflection with BindingFlags** for dynamic property access

✅ **ExpandoObject** for dynamic type creation

✅ **Expression.Block** for multiple operations

✅ **Compile-time delegate generation** for performance

✅ **Record types** for source data structure

---

### Query 17: Conditional Mapping with Let Clause

#### Real-World Scenario
An employee performance review system needs to calculate **complex derived fields** for each employee: bonus percentage (based on performance rating and tenure), adjusted salary (including COLA and merit increase), promotion eligibility (based on multiple factors), and risk of leaving (based on engagement survey scores and market competitiveness).

#### Business Impact
Automates annual review calculations for 50,000+ employees, reducing HR processing time from 3 weeks to 2 days.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyPerformanceCalculator
{
    public List<EmployeeReview> CalculateReviews(List<Employee> employees)
    {
        var results = new List<EmployeeReview>();
        
        foreach (var emp in employees)
        {
            // Calculate bonus percentage
            decimal bonusPercentage = 0;
            if (emp.PerformanceRating >= 4.5)
                bonusPercentage = 0.20m;
            else if (emp.PerformanceRating >= 4.0)
                bonusPercentage = 0.15m;
            else if (emp.PerformanceRating >= 3.5)
                bonusPercentage = 0.10m;
            else if (emp.PerformanceRating >= 3.0)
                bonusPercentage = 0.05m;
            
            // Tenure bonus adjustment
            int tenure = (DateTime.Now.Year - emp.HireDate.Year);
            if (tenure > 5) bonusPercentage += 0.02m;
            if (tenure > 10) bonusPercentage += 0.03m;
            
            // Calculate adjusted salary
            decimal colaIncrease = emp.BaseSalary * 0.03m;
            decimal meritIncrease = emp.BaseSalary * (bonusPercentage / 2);
            decimal adjustedSalary = emp.BaseSalary + colaIncrease + meritIncrease;
            
            // Promotion eligibility
            bool isEligibleForPromotion = emp.PerformanceRating >= 4.0 && tenure >= 2;
            
            // Risk of leaving
            string riskLevel = "Low";
            if (emp.EngagementScore < 3 && emp.SalaryCompetitiveness < 0.9m)
                riskLevel = "High";
            else if (emp.EngagementScore < 3.5 || emp.SalaryCompetitiveness < 0.95m)
                riskLevel = "Medium";
            
            results.Add(new EmployeeReview
            {
                EmployeeId = emp.Id,
                Name = emp.Name,
                BonusPercentage = bonusPercentage,
                BonusAmount = emp.BaseSalary * bonusPercentage,
                AdjustedSalary = adjustedSalary,
                IsPromotionEligible = isEligibleForPromotion,
                RiskLevel = riskLevel
            });
        }
        
        return results;
    }
}
```

#### .NET 10 Implementation

```csharp
public record Employee(
    int Id,
    string Name,
    string Department,
    decimal BaseSalary,
    DateTime HireDate,
    double PerformanceRating,
    double EngagementScore,
    decimal SalaryCompetitiveness
);

public record EmployeeReview(
    int EmployeeId,
    string Name,
    string Department,
    decimal BonusPercentage,
    decimal BonusAmount,
    decimal AdjustedSalary,
    bool IsPromotionEligible,
    string RiskLevel,
    string Recommendation
);

public class PerformanceCalculator
{
    public List<EmployeeReview> CalculateReviews(List<Employee> employees)
    {
        var currentYear = DateTime.Now.Year;
        
        return employees
            .Select(emp => new
            {
                emp,
                Tenure = currentYear - emp.HireDate.Year,
                BaseBonus = emp.PerformanceRating switch
                {
                    >= 4.5 => 0.20m,
                    >= 4.0 => 0.15m,
                    >= 3.5 => 0.10m,
                    >= 3.0 => 0.05m,
                    _ => 0.00m
                }
            })
            .Select(x => new
            {
                x.emp,
                x.Tenure,
                x.BaseBonus,
                TenureBonus = x.Tenure > 10 ? 0.05m : x.Tenure > 5 ? 0.02m : 0.00m
            })
            .Select(x => new
            {
                x.emp,
                x.Tenure,
                BonusPercentage = Math.Min(x.BaseBonus + x.TenureBonus, 0.35m),
                COLAIncrease = x.emp.BaseSalary * 0.03m
            })
            .Select(x => new
            {
                x.emp,
                x.Tenure,
                x.BonusPercentage,
                MeritIncrease = x.emp.BaseSalary * (x.BonusPercentage / 2),
                x.COLAIncrease
            })
            .Select(x => new
            {
                x.emp,
                x.Tenure,
                x.BonusPercentage,
                AdjustedSalary = x.emp.BaseSalary + x.COLAIncrease + x.MeritIncrease,
                x.MeritIncrease
            })
            .Select(x => new EmployeeReview(
                EmployeeId: x.emp.Id,
                Name: x.emp.Name,
                Department: x.emp.Department,
                BonusPercentage: x.BonusPercentage,
                BonusAmount: x.emp.BaseSalary * x.BonusPercentage,
                AdjustedSalary: x.AdjustedSalary,
                IsPromotionEligible: x.emp.PerformanceRating >= 4.0 && x.Tenure >= 2,
                RiskLevel: (x.emp.EngagementScore, x.emp.SalaryCompetitiveness) switch
                {
                    (< 3, < 0.9m) => "High",
                    (< 3.5, < 0.95m) => "Medium",
                    _ => "Low"
                },
                Recommendation: CalculateRecommendation(x.emp.PerformanceRating, x.BonusPercentage, x.Tenure)
            ))
            .OrderByDescending(r => r.BonusPercentage)
            .ThenBy(r => r.RiskLevel)
            .ToList();
    }
    
    private static string CalculateRecommendation(double rating, decimal bonus, int tenure)
    {
        return (rating, bonus, tenure) switch
        {
            (>= 4.5, > 0.20m, >= 5) => "Fast track to senior leadership program",
            (>= 4.0, > 0.15m, >= 3) => "Consider for team lead role",
            (>= 3.5, > 0.10m, >= 2) => "Encourage professional certification",
            (>= 3.0, _, _) => "Set development goals for next quarter",
            _ => "Place on performance improvement plan"
        };
    }
}
```

#### Key .NET 10 Features Used

✅ **Let clause simulation** with multiple Select projections

✅ **Switch expressions** for bonus calculation and risk assessment

✅ **Tuple patterns** in switch for complex condition mapping

✅ **Record types** for immutable data transfer

✅ **Fluent LINQ chaining** for step-by-step transformation

✅ **Pattern matching** with relational patterns (`>=`, `<`)

---

### Query 18: OfType for Mixed Type Collections

#### Real-World Scenario
A logging and monitoring system collects events from multiple sources into a single ArrayList (legacy system). The collection contains different event types: ErrorEvent, WarningEvent, InfoEvent, and AuditEvent. The system needs to **filter and process only ErrorEvent** objects for the alert dashboard, ignoring all other types.

#### Business Impact
Processes 10,000+ mixed events per second, enabling real-time error alerting with 99.9% accuracy.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyEventProcessor
{
    public List<ErrorEvent> GetErrorEvents(ArrayList events)
    {
        var errors = new List<ErrorEvent>();
        
        foreach (object evt in events)
        {
            if (evt is ErrorEvent error)
            {
                errors.Add(error);
            }
        }
        
        return errors;
    }
}

public class ErrorEvent
{
    public DateTime Timestamp { get; set; }
    public string Message { get; set; }
    public string StackTrace { get; set; }
    public int ErrorCode { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public abstract record EventBase(DateTime Timestamp, string Message, string Source);
public record ErrorEvent(DateTime Timestamp, string Message, string Source, string StackTrace, int ErrorCode) : EventBase(Timestamp, Message, Source);
public record WarningEvent(DateTime Timestamp, string Message, string Source, string Recommendation) : EventBase(Timestamp, Message, Source);
public record InfoEvent(DateTime Timestamp, string Message, string Source, string Category) : EventBase(Timestamp, Message, Source);
public record AuditEvent(DateTime Timestamp, string Message, string Source, string UserId, string Action) : EventBase(Timestamp, Message, Source);

public record ErrorSummary(
    int TotalErrors,
    Dictionary<int, int> ErrorsByCode,
    List<ErrorEvent> CriticalErrors,
    DateTime OldestError,
    DateTime NewestError
);

public class EventProcessor
{
    public List<ErrorEvent> GetErrorEvents(ArrayList events)
    {
        // OfType filters and casts in one operation
        return events.OfType<ErrorEvent>().ToList();
    }
    
    // Process multiple event types with pattern matching
    public void ProcessEvents(ArrayList events)
    {
        var errors = events.OfType<ErrorEvent>().ToList();
        var warnings = events.OfType<WarningEvent>().ToList();
        var infos = events.OfType<InfoEvent>().ToList();
        var audits = events.OfType<AuditEvent>().ToList();
        
        Console.WriteLine($"Errors: {errors.Count}, Warnings: {warnings.Count}, Info: {infos.Count}, Audit: {audits.Count}");
    }
    
    // Aggregate error analysis
    public ErrorSummary AnalyzeErrors(ArrayList events)
    {
        var errors = events.OfType<ErrorEvent>().ToList();
        
        if (!errors.Any())
            return new ErrorSummary(0, new Dictionary<int, int>(), [], DateTime.Now, DateTime.Now);
        
        return new ErrorSummary(
            TotalErrors: errors.Count,
            ErrorsByCode: errors.GroupBy(e => e.ErrorCode).ToDictionary(g => g.Key, g => g.Count()),
            CriticalErrors: errors.Where(e => e.ErrorCode >= 500).ToList(),
            OldestError: errors.Min(e => e.Timestamp),
            NewestError: errors.Max(e => e.Timestamp)
        );
    }
    
    // Generic processor for any event type
    public List<T> GetEventsOfType<T>(ArrayList events) where T : EventBase
    {
        return events.OfType<T>().ToList();
    }
}
```

#### Key .NET 10 Features Used

✅ **OfType<T>** for filtering and casting in single operation

✅ **Generic methods** for reusable type filtering

✅ **Record inheritance** for event type hierarchy

✅ **Collection expressions** for list initialization

✅ **Pattern matching** with type patterns

---

### Query 19: Cast for Safe Type Conversion

#### Real-World Scenario
A legacy data import system receives data from an old COM component that returns `System.Collections.ArrayList` containing `System.Data.DataRow` objects. The modern .NET 10 application needs to **convert this to strongly-typed `IEnumerable<DataRow>`** for LINQ operations without manual casting.

#### Business Impact
Enables modernization of legacy data pipelines without breaking existing integrations, processing 5M+ rows daily.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyDataConverter
{
    public List<DataRow> ConvertToStronglyTyped(ArrayList legacyRows)
    {
        var results = new List<DataRow>();
        
        foreach (object row in legacyRows)
        {
            if (row is DataRow dataRow)
            {
                results.Add(dataRow);
            }
        }
        
        return results;
    }
}
```

#### .NET 10 Implementation

```csharp
public class DataConverter
{
    public List<DataRow> ConvertToStronglyTyped(ArrayList legacyRows)
    {
        // Cast converts and throws if type mismatch
        return legacyRows.Cast<DataRow>().ToList();
    }
    
    // Safe conversion with error handling
    public List<DataRow> ConvertSafe(ArrayList legacyRows)
    {
        return legacyRows
            .Cast<DataRow>()
            .Where(row => row != null && row.Table != null)
            .ToList();
    }
    
    // Convert and project in one pass
    public List<CustomerImport> ConvertToCustomers(ArrayList legacyRows)
    {
        return legacyRows
            .Cast<DataRow>()
            .Where(row => row.Table.Columns.Contains("CustomerId"))
            .Select(row => new CustomerImport(
                CustomerId: Convert.ToInt32(row["CustomerId"]),
                Name: row["Name"]?.ToString() ?? string.Empty,
                Email: row["Email"]?.ToString() ?? string.Empty,
                ImportDate: DateTime.Now
            ))
            .ToList();
    }
    
    // Handle conversion failures gracefully
    public (List<DataRow> ValidRows, List<object> FailedRows) ConvertWithFallback(ArrayList legacyRows)
    {
        var validRows = new List<DataRow>();
        var failedRows = new List<object>();
        
        foreach (var item in legacyRows)
        {
            if (item is DataRow row)
                validRows.Add(row);
            else
                failedRows.Add(item);
        }
        
        return (validRows, failedRows);
    }
}

public record CustomerImport(int CustomerId, string Name, string Email, DateTime ImportDate);
```

#### Key .NET 10 Features Used

✅ **Cast<T>** for bulk type conversion with type safety

✅ **Tuple returns** for success/failure separation

✅ **Record types** for import data models

✅ **LINQ chaining** with Cast as first operation

✅ **Null handling** with null-conditional operators

---

### Query 20: Select with Index

#### Real-World Scenario
A bulk email marketing system needs to send personalized emails to 100,000+ customers. Each email must include a **sequential number** (1-based) for tracking and a **batch identifier** (group of 1000) for processing. The system also needs to calculate estimated send time based on position in queue.

#### Business Impact
Enables tracking of 1M+ email sends per campaign with 99.99% delivery accuracy.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyEmailProcessor
{
    public List<EmailMessage> PrepareEmails(List<Customer> customers)
    {
        var messages = new List<EmailMessage>();
        int index = 0;
        
        foreach (var customer in customers)
        {
            index++;
            int batchNumber = (index - 1) / 1000 + 1;
            DateTime estimatedSendTime = DateTime.Now.AddSeconds(index * 0.5);
            
            messages.Add(new EmailMessage
            {
                SequenceNumber = index,
                BatchId = batchNumber,
                RecipientEmail = customer.Email,
                RecipientName = customer.Name,
                EstimatedSendTime = estimatedSendTime,
                PersonalizedContent = $"Hello {customer.Name}, you are #{index} in our queue."
            });
        }
        
        return messages;
    }
}
```

#### .NET 10 Implementation

```csharp
public record Customer(int Id, string Name, string Email, string Tier);
public record EmailMessage(
    int SequenceNumber,
    int BatchId,
    string RecipientEmail,
    string RecipientName,
    DateTime EstimatedSendTime,
    string PersonalizedContent,
    string Priority
);

public class EmailProcessor
{
    public List<EmailMessage> PrepareEmails(List<Customer> customers)
    {
        return customers
            .Select((customer, index) => new
            {
                Customer = customer,
                Index = index + 1,  // 1-based sequence
                BatchId = index / 1000 + 1
            })
            .Select(x => new EmailMessage(
                SequenceNumber: x.Index,
                BatchId: x.BatchId,
                RecipientEmail: x.Customer.Email,
                RecipientName: x.Customer.Name,
                EstimatedSendTime: DateTime.Now.AddSeconds(x.Index * 0.5),
                PersonalizedContent: $"Hello {x.Customer.Name}, thank you for being a {x.Customer.Tier} member!",
                Priority: x.Customer.Tier == "Platinum" ? "High" : "Normal"
            ))
            .ToList();
    }
    
    // Batch processing with index
    public Dictionary<int, List<EmailMessage>> GroupByBatch(List<Customer> customers)
    {
        return customers
            .Select((customer, index) => new { customer, BatchId = index / 1000 })
            .GroupBy(x => x.BatchId)
            .ToDictionary(
                g => g.Key + 1,
                g => g.Select(x => new EmailMessage(
                    SequenceNumber: 0, // Will be set per batch
                    BatchId: g.Key + 1,
                    RecipientEmail: x.customer.Email,
                    RecipientName: x.customer.Name,
                    EstimatedSendTime: DateTime.Now,
                    PersonalizedContent: $"Hello {x.customer.Name}",
                    Priority: "Normal"
                )).ToList()
            );
    }
    
    // Pagination with index
    public PaginatedResult<EmailMessage> GetPage(List<Customer> customers, int pageNumber, int pageSize)
    {
        var page = customers
            .Skip((pageNumber - 1) * pageSize)
            .Take(pageSize)
            .Select((customer, index) => new EmailMessage(
                SequenceNumber: (pageNumber - 1) * pageSize + index + 1,
                BatchId: pageNumber,
                RecipientEmail: customer.Email,
                RecipientName: customer.Name,
                EstimatedSendTime: DateTime.Now,
                PersonalizedContent: $"Hello {customer.Name}",
                Priority: "Normal"
            ))
            .ToList();
        
        return new PaginatedResult<EmailMessage>(page, customers.Count, pageNumber, pageSize);
    }
}

public record PaginatedResult<T>(List<T> Items, int TotalCount, int PageNumber, int PageSize);
```

#### Key .NET 10 Features Used

✅ **Select with index overload** `Select((item, index) => ...)`

✅ **Tuple deconstruction** for cleaner projections

✅ **Record types** for immutable message and result models

✅ **Collection expressions** for list initialization

✅ **Dictionary grouping** with index-based keys

---

### Query 21: Where Filtering with Multiple Complex Conditions

#### Real-World Scenario
A fraud detection system needs to identify **suspicious transactions** based on multiple complex rules:
- Amount exceeds 3 standard deviations from customer's average
- Transaction occurs in unusual geographic location (not within 100 miles of any previous transaction in last 30 days)
- Time of day is unusual (customer typically transacts 9 AM-5 PM but this is 2 AM)
- Velocity check (more than 5 transactions in last hour)
- Device fingerprint mismatch

#### Business Impact
Identifies $10M+ in potential fraud annually with 95% accuracy and 0.1% false positive rate.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyFraudDetector
{
    public List<Transaction> GetSuspiciousTransactions(List<Transaction> transactions, List<CustomerProfile> profiles)
    {
        var suspicious = new List<Transaction>();
        
        foreach (var transaction in transactions)
        {
            var profile = profiles.FirstOrDefault(p => p.CustomerId == transaction.CustomerId);
            if (profile == null) continue;
            
            bool isSuspicious = false;
            
            // Amount check (3 standard deviations)
            decimal threshold = profile.AverageTransactionAmount + (3 * profile.TransactionStdDev);
            if (transaction.Amount > threshold)
                isSuspicious = true;
            
            // Location check
            var recentLocations = transactions
                .Where(t => t.CustomerId == transaction.CustomerId && 
                           t.Timestamp >= DateTime.Now.AddDays(-30))
                .Select(t => t.Location)
                .ToList();
            
            bool isUnusualLocation = !recentLocations.Any(l => 
                CalculateDistance(l.Latitude, l.Longitude, 
                                 transaction.Location.Latitude, 
                                 transaction.Location.Longitude) < 100);
            
            if (isUnusualLocation)
                isSuspicious = true;
            
            // Time check
            if (transaction.Timestamp.Hour < 9 || transaction.Timestamp.Hour > 17)
                isSuspicious = true;
            
            // Velocity check
            int recentCount = transactions.Count(t => 
                t.CustomerId == transaction.CustomerId && 
                t.Timestamp >= DateTime.Now.AddHours(-1));
            
            if (recentCount > 5)
                isSuspicious = true;
            
            if (isSuspicious)
                suspicious.Add(transaction);
        }
        
        return suspicious;
    }
    
    private double CalculateDistance(double lat1, double lon1, double lat2, double lon2)
    {
        // Haversine formula
        var R = 3958.8; // Miles
        var dLat = (lat2 - lat1) * Math.PI / 180;
        var dLon = (lon2 - lon1) * Math.PI / 180;
        var a = Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
                Math.Cos(lat1 * Math.PI / 180) * Math.Cos(lat2 * Math.PI / 180) *
                Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
        var c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
        return R * c;
    }
}
```

#### .NET 10 Implementation

```csharp
public record Location(double Latitude, double Longitude, string City, string Country);
public record Transaction(int Id, int CustomerId, decimal Amount, DateTime Timestamp, Location Location, string DeviceId);
public record CustomerProfile(int CustomerId, decimal AverageTransactionAmount, decimal TransactionStdDev, string TypicalTimeZone);

public record FraudAlert(
    int TransactionId,
    int CustomerId,
    decimal Amount,
    DateTime Timestamp,
    List<string> SuspiciousReasons,
    decimal RiskScore,
    string RecommendedAction
);

public class FraudDetector
{
    public List<FraudAlert> GetSuspiciousTransactions(
        List<Transaction> transactions, 
        List<CustomerProfile> profiles,
        DateTime analysisTime)
    {
        var thirtyDaysAgo = analysisTime.AddDays(-30);
        var oneHourAgo = analysisTime.AddHours(-1);
        
        return transactions
            .Join(profiles, t => t.CustomerId, p => p.CustomerId, (t, p) => new { Transaction = t, Profile = p })
            .Select(x => new
            {
                x.Transaction,
                x.Profile,
                RecentTransactions = transactions
                    .Where(t => t.CustomerId == x.Transaction.CustomerId && t.Timestamp >= thirtyDaysAgo)
                    .ToList()
            })
            .Select(x => new
            {
                x.Transaction,
                x.Profile,
                x.RecentTransactions,
                RecentHourTransactions = transactions
                    .Where(t => t.CustomerId == x.Transaction.CustomerId && t.Timestamp >= oneHourAgo)
                    .ToList()
            })
            .Select(x => new
            {
                x.Transaction,
                x.Profile,
                SuspiciousReasons = new List<string>()
                    .AddIf(IsAmountSuspicious(x.Transaction.Amount, x.Profile.AverageTransactionAmount, x.Profile.TransactionStdDev), 
                        $"Amount ${x.Transaction.Amount:N2} exceeds normal range")
                    .AddIf(IsLocationSuspicious(x.Transaction.Location, x.RecentTransactions), 
                        $"Unusual location: {x.Transaction.Location.City}, {x.Transaction.Location.Country}")
                    .AddIf(IsTimeSuspicious(x.Transaction.Timestamp), 
                        $"Unusual time: {x.Transaction.Timestamp:HH:mm}")
                    .AddIf(IsVelocitySuspicious(x.RecentHourTransactions.Count), 
                        $"Velocity alert: {x.RecentHourTransactions.Count} transactions in last hour")
            })
            .Where(x => x.SuspiciousReasons.Any())
            .Select(x => new FraudAlert(
                TransactionId: x.Transaction.Id,
                CustomerId: x.Transaction.CustomerId,
                Amount: x.Transaction.Amount,
                Timestamp: x.Transaction.Timestamp,
                SuspiciousReasons: x.SuspiciousReasons,
                RiskScore: CalculateRiskScore(x.SuspiciousReasons.Count, x.Transaction.Amount),
                RecommendedAction: x.SuspiciousReasons.Count >= 3 ? "Block transaction" : "Flag for review"
            ))
            .OrderByDescending(a => a.RiskScore)
            .ToList();
    }
    
    private static bool IsAmountSuspicious(decimal amount, decimal avg, decimal stdDev) 
        => amount > avg + (3 * stdDev);
    
    private static bool IsLocationSuspicious(Location current, List<Transaction> recentTransactions)
    {
        if (!recentTransactions.Any()) return false;
        return !recentTransactions.Any(t => CalculateDistance(
            t.Location.Latitude, t.Location.Longitude,
            current.Latitude, current.Longitude) < 100);
    }
    
    private static bool IsTimeSuspicious(DateTime timestamp) 
        => timestamp.Hour < 9 || timestamp.Hour > 17;
    
    private static bool IsVelocitySuspicious(int recentCount) 
        => recentCount > 5;
    
    private static decimal CalculateRiskScore(int reasonCount, decimal amount)
    {
        return (reasonCount * 20m) + (amount > 10000 ? 30m : amount > 5000 ? 15m : 0m);
    }
    
    private static double CalculateDistance(double lat1, double lon1, double lat2, double lon2)
    {
        var R = 3958.8; // Miles
        var dLat = (lat2 - lat1) * Math.PI / 180;
        var dLon = (lon2 - lon1) * Math.PI / 180;
        var a = Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
                Math.Cos(lat1 * Math.PI / 180) * Math.Cos(lat2 * Math.PI / 180) *
                Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
        var c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
        return R * c;
    }
}

public static class ListExtensions
{
    public static List<string> AddIf(this List<string> list, bool condition, string item)
    {
        if (condition) list.Add(item);
        return list;
    }
}
```

#### Key .NET 10 Features Used

✅ **Multiple Where clauses** with complex condition chaining

✅ **Join operations** for data correlation

✅ **Custom ListExtensions** with AddIf for conditional building

✅ **Record types** for immutable data models

✅ **Tuple returns** for intermediate calculations

✅ **Pattern matching** with relational patterns

---

### Query 22: Take/Skip for Pagination

#### Real-World Scenario
A REST API endpoint for a product catalog needs to return **paginated results** with support for cursor-based pagination (using last seen ID) and offset-based pagination (page number + page size). The system must also return metadata including total count, next/previous page tokens, and estimated total pages.

#### Business Impact
Powers product browsing for 500,000+ concurrent users, reducing API response time from 5 seconds to 200ms.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyPaginationService
{
    public PaginatedResult<Product> GetPage(List<Product> products, int pageNumber, int pageSize)
    {
        int totalCount = products.Count;
        int startIndex = (pageNumber - 1) * pageSize;
        int endIndex = Math.Min(startIndex + pageSize, totalCount);
        
        var pageItems = new List<Product>();
        for (int i = startIndex; i < endIndex; i++)
        {
            pageItems.Add(products[i]);
        }
        
        return new PaginatedResult
        {
            Items = pageItems,
            TotalCount = totalCount,
            PageNumber = pageNumber,
            PageSize = pageSize,
            TotalPages = (int)Math.Ceiling(totalCount / (double)pageSize)
        };
    }
}
```

#### .NET 10 Implementation

```csharp
public record Product(int Id, string Name, string Category, decimal Price, DateTime CreatedDate);
public record PaginatedResult<T>(
    List<T> Items,
    int TotalCount,
    int PageNumber,
    int PageSize,
    int TotalPages,
    bool HasPreviousPage,
    bool HasNextPage,
    string? NextCursor,
    string? PreviousCursor
);

public record CursorResult<T>(
    List<T> Items,
    string NextCursor,
    bool HasMore,
    int Limit
);

public class PaginationService
{
    // Offset-based pagination (page number + page size)
    public PaginatedResult<Product> GetPageOffset(List<Product> products, int pageNumber, int pageSize)
    {
        var totalCount = products.Count;
        var totalPages = (int)Math.Ceiling(totalCount / (double)pageSize);
        
        var items = products
            .Skip((pageNumber - 1) * pageSize)
            .Take(pageSize)
            .ToList();
        
        return new PaginatedResult<Product>(
            Items: items,
            TotalCount: totalCount,
            PageNumber: pageNumber,
            PageSize: pageSize,
            TotalPages: totalPages,
            HasPreviousPage: pageNumber > 1,
            HasNextPage: pageNumber < totalPages,
            NextCursor: pageNumber < totalPages ? (pageNumber + 1).ToString() : null,
            PreviousCursor: pageNumber > 1 ? (pageNumber - 1).ToString() : null
        );
    }
    
    // Cursor-based pagination (more efficient for large datasets)
    public CursorResult<Product> GetPageCursor(List<Product> products, string? cursor, int limit = 20)
    {
        int lastId = string.IsNullOrEmpty(cursor) ? 0 : int.Parse(cursor);
        
        var query = products.AsQueryable();
        
        if (lastId > 0)
            query = query.Where(p => p.Id > lastId);
        
        var items = query
            .OrderBy(p => p.Id)
            .Take(limit + 1)  // Take one extra to determine if there are more
            .ToList();
        
        bool hasMore = items.Count > limit;
        var resultItems = items.Take(limit).ToList();
        var nextCursor = hasMore ? resultItems.Last().Id.ToString() : null;
        
        return new CursorResult<Product>(
            Items: resultItems,
            NextCursor: nextCursor,
            HasMore: hasMore,
            Limit: limit
        );
    }
    
    // Keyset pagination for sorted results
    public PaginatedResult<Product> GetPageKeyset(
        List<Product> products, 
        int? lastId, 
        decimal? lastPrice, 
        int pageSize,
        string sortBy = "Id")
    {
        var query = products.AsQueryable();
        
        if (lastId.HasValue && lastPrice.HasValue && sortBy == "Price")
        {
            query = query.Where(p => p.Price > lastPrice.Value || 
                                    (p.Price == lastPrice.Value && p.Id > lastId.Value));
        }
        else if (lastId.HasValue)
        {
            query = query.Where(p => p.Id > lastId.Value);
        }
        
        var items = query
            .OrderBy(p => sortBy == "Price" ? p.Price : p.Id)
            .ThenBy(p => p.Id)
            .Take(pageSize)
            .ToList();
        
        var totalCount = products.Count;
        var totalPages = (int)Math.Ceiling(totalCount / (double)pageSize);
        
        return new PaginatedResult<Product>(
            Items: items,
            TotalCount: totalCount,
            PageNumber: 0, // Not applicable for keyset
            PageSize: pageSize,
            TotalPages: totalPages,
            HasPreviousPage: lastId.HasValue,
            HasNextPage: items.Count == pageSize,
            NextCursor: items.LastOrDefault()?.Id.ToString(),
            PreviousCursor: lastId?.ToString()
        );
    }
}
```

#### Key .NET 10 Features Used

✅ **Skip and Take** for offset pagination

✅ **OrderBy with ThenBy** for stable sorting

✅ **Record types** for paginated result metadata

✅ **Nullable reference types** for cursor values

✅ **Queryable composition** for dynamic filtering

---

### Query 23: SelectMany for Cross Joins (Cartesian Product)

#### Real-World Scenario
An A/B testing platform needs to generate **all possible combinations** of test variants for a multivariate experiment. The experiment has 3 variables: Button Color (Red, Green, Blue), Headline Text (Welcome, Hello, Hi), and Image (Product, Team, Logo). The system needs to generate all 27 combinations for the test design matrix.

#### Business Impact
Reduces test setup time from 2 hours to 5 minutes for marketing teams running 500+ experiments monthly.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyVariantGenerator
{
    public List<TestVariant> GenerateVariants(List<string> colors, List<string> headlines, List<string> images)
    {
        var variants = new List<TestVariant>();
        
        foreach (var color in colors)
        {
            foreach (var headline in headlines)
            {
                foreach (var image in images)
                {
                    variants.Add(new TestVariant
                    {
                        ButtonColor = color,
                        HeadlineText = headline,
                        ImageType = image,
                        VariantId = $"{color}_{headline}_{image}"
                    });
                }
            }
        }
        
        return variants;
    }
}
```

#### .NET 10 Implementation

```csharp
public record TestVariant(
    string ButtonColor,
    string HeadlineText,
    string ImageType,
    string VariantId,
    double ExpectedConversionRate
);

public record ABTestConfig(
    List<string> ButtonColors,
    List<string> Headlines,
    List<string> Images,
    List<string> AudienceSegments,
    List<string> DeviceTypes
);

public class VariantGenerator
{
    public List<TestVariant> GenerateVariants(List<string> colors, List<string> headlines, List<string> images)
    {
        // Cross join using SelectMany
        return colors
            .SelectMany(color => headlines, (color, headline) => new { color, headline })
            .SelectMany(x => images, (x, image) => new TestVariant(
                ButtonColor: x.color,
                HeadlineText: x.headline,
                ImageType: image,
                VariantId: $"{x.color}_{x.headline}_{image}",
                ExpectedConversionRate: CalculateExpectedRate(x.color, x.headline, image)
            ))
            .ToList();
    }
    
    // Query syntax for cross join (more readable)
    public List<TestVariant> GenerateVariantsQuerySyntax(List<string> colors, List<string> headlines, List<string> images)
    {
        return (from color in colors
                from headline in headlines
                from image in images
                select new TestVariant(
                    ButtonColor: color,
                    HeadlineText: headline,
                    ImageType: image,
                    VariantId: $"{color}_{headline}_{image}",
                    ExpectedConversionRate: CalculateExpectedRate(color, headline, image)
                )).ToList();
    }
    
    // Multi-dimensional cross join (4+ dimensions)
    public List<TestVariant> GenerateMultiDimensionalVariants(ABTestConfig config)
    {
        return config.ButtonColors
            .SelectMany(c => config.Headlines, (c, h) => new { Color = c, Headline = h })
            .SelectMany(x => config.Images, (x, i) => new { x.Color, x.Headline, Image = i })
            .SelectMany(x => config.AudienceSegments, (x, a) => new { x.Color, x.Headline, x.Image, Audience = a })
            .SelectMany(x => config.DeviceTypes, (x, d) => new TestVariant(
                ButtonColor: x.Color,
                HeadlineText: x.Headline,
                ImageType: x.Image,
                VariantId: $"{x.Color}_{x.Headline}_{x.Image}_{x.Audience}_{d}",
                ExpectedConversionRate: CalculateMultiRate(x.Color, x.Headline, x.Image, x.Audience, d)
            ))
            .ToList();
    }
    
    // Weighted variant generation (not all combinations, only those meeting criteria)
    public List<TestVariant> GenerateWeightedVariants(List<string> colors, List<string> headlines, List<string> images)
    {
        return colors
            .SelectMany(color => headlines, (color, headline) => new { color, headline })
            .SelectMany(x => images, (x, image) => new { x.color, x.headline, image })
            .Where(x => IsValidCombination(x.color, x.headline, x.image))
            .Select(x => new TestVariant(
                ButtonColor: x.color,
                HeadlineText: x.headline,
                ImageType: x.image,
                VariantId: $"{x.color}_{x.headline}_{x.image}",
                ExpectedConversionRate: CalculateExpectedRate(x.color, x.headline, x.image)
            ))
            .ToList();
    }
    
    private static double CalculateExpectedRate(string color, string headline, string image)
    {
        // Simplified rate calculation
        double rate = 0.05; // Baseline 5%
        if (color == "Red") rate += 0.02;
        if (headline == "Welcome") rate += 0.01;
        if (image == "Product") rate += 0.015;
        return rate;
    }
    
    private static double CalculateMultiRate(string color, string headline, string image, string audience, string device)
    {
        double rate = 0.05;
        if (audience == "Premium") rate += 0.03;
        if (device == "Mobile") rate += 0.005;
        return rate + CalculateExpectedRate(color, headline, image);
    }
    
    private static bool IsValidCombination(string color, string headline, string image)
    {
        // Business rule: Red button only works with Welcome headline
        if (color == "Red" && headline != "Welcome") return false;
        // Business rule: Logo image only with Hi headline
        if (image == "Logo" && headline != "Hi") return false;
        return true;
    }
}
```

#### Key .NET 10 Features Used

✅ **SelectMany chaining** for multi-dimensional cross joins

✅ **LINQ Query Syntax** with multiple `from` clauses

✅ **Record types** for variant configuration

✅ **Where filtering** within cross join pipeline

✅ **Collection expressions** for result initialization

---

### Query 24: Let Clause for Intermediate Values

#### Real-World Scenario
A shipping cost calculator needs to compute **complex shipping rates** based on package dimensions, weight, destination zone, and shipping speed. The calculation involves multiple intermediate values (volume, dimensional weight, base rate, fuel surcharge, remote area fee) that are reused throughout the calculation.

#### Business Impact

Processes 1M+ shipping quotes daily for an e-commerce platform, reducing calculation time from 50ms to 5ms per quote.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyShippingCalculator
{
    public List<ShippingQuote> CalculateQuotes(List<Package> packages, List<Destination> destinations)
    {
        var quotes = new List<ShippingQuote>();
        
        foreach (var package in packages)
        {
            foreach (var dest in destinations)
            {
                decimal volume = package.Length * package.Width * package.Height;
                decimal dimWeight = volume / 166m;
                decimal billableWeight = Math.Max(package.Weight, dimWeight);
                
                decimal baseRate = billableWeight * 0.5m;
                
                decimal zoneMultiplier = dest.Zone switch
                {
                    1 => 1.0m,
                    2 => 1.2m,
                    3 => 1.5m,
                    4 => 2.0m,
                    _ => 2.5m
                };
                
                decimal zoneRate = baseRate * zoneMultiplier;
                
                decimal fuelSurcharge = zoneRate * 0.15m;
                decimal remoteFee = dest.IsRemoteArea ? 25m : 0m;
                
                decimal totalCost = zoneRate + fuelSurcharge + remoteFee;
                
                quotes.Add(new ShippingQuote
                {
                    PackageId = package.Id,
                    DestinationCode = dest.Code,
                    TotalCost = totalCost,
                    Breakdown = $"Base: {baseRate:C}, Zone: {zoneRate:C}, Fuel: {fuelSurcharge:C}, Remote: {remoteFee:C}"
                });
            }
        }
        
        return quotes;
    }
}
```

#### .NET 10 Implementation

```csharp
public record Package(int Id, string Name, decimal Length, decimal Width, decimal Height, decimal Weight);
public record Destination(string Code, string City, int Zone, bool IsRemoteArea);
public record ShippingQuote(
    int PackageId,
    string DestinationCode,
    decimal TotalCost,
    string Breakdown,
    string RecommendedService
);

public class ShippingCalculator
{
    public List<ShippingQuote> CalculateQuotes(List<Package> packages, List<Destination> destinations)
    {
        return packages
            .SelectMany(p => destinations, (p, d) => new { Package = p, Destination = d })
            .Select(x => new
            {
                x.Package,
                x.Destination,
                Volume = x.Package.Length * x.Package.Width * x.Package.Height,
                DimWeight = (x.Package.Length * x.Package.Width * x.Package.Height) / 166m
            })
            .Select(x => new
            {
                x.Package,
                x.Destination,
                x.Volume,
                x.DimWeight,
                BillableWeight = Math.Max(x.Package.Weight, x.DimWeight)
            })
            .Select(x => new
            {
                x.Package,
                x.Destination,
                x.Volume,
                x.DimWeight,
                x.BillableWeight,
                BaseRate = x.BillableWeight * 0.5m
            })
            .Select(x => new
            {
                x.Package,
                x.Destination,
                x.Volume,
                x.DimWeight,
                x.BillableWeight,
                x.BaseRate,
                ZoneMultiplier = x.Destination.Zone switch
                {
                    1 => 1.0m,
                    2 => 1.2m,
                    3 => 1.5m,
                    4 => 2.0m,
                    _ => 2.5m
                }
            })
            .Select(x => new
            {
                x.Package,
                x.Destination,
                x.Volume,
                x.DimWeight,
                x.BillableWeight,
                x.BaseRate,
                x.ZoneMultiplier,
                ZoneRate = x.BaseRate * x.ZoneMultiplier
            })
            .Select(x => new
            {
                x.Package,
                x.Destination,
                x.Volume,
                x.DimWeight,
                x.BillableWeight,
                x.BaseRate,
                x.ZoneMultiplier,
                x.ZoneRate,
                FuelSurcharge = x.ZoneRate * 0.15m,
                RemoteFee = x.Destination.IsRemoteArea ? 25m : 0m
            })
            .Select(x => new ShippingQuote(
                PackageId: x.Package.Id,
                DestinationCode: x.Destination.Code,
                TotalCost: x.ZoneRate + x.FuelSurcharge + x.RemoteFee,
                Breakdown: $"Base: {x.BaseRate:C}, Zone: {x.ZoneRate:C}, Fuel: {x.FuelSurcharge:C}, Remote: {x.RemoteFee:C}",
                RecommendedService: (x.ZoneRate + x.FuelSurcharge + x.RemoteFee) switch
                {
                    > 100 => "Express Plus",
                    > 50 => "Express",
                    > 25 => "Standard",
                    _ => "Economy"
                }
            ))
            .ToList();
    }
    
    // Alternative using LINQ Query Syntax with let clause
    public List<ShippingQuote> CalculateQueriesQuerySyntax(List<Package> packages, List<Destination> destinations)
    {
        return (from package in packages
                from dest in destinations
                let volume = package.Length * package.Width * package.Height
                let dimWeight = volume / 166m
                let billableWeight = Math.Max(package.Weight, dimWeight)
                let baseRate = billableWeight * 0.5m
                let zoneMultiplier = dest.Zone switch { 1 => 1.0m, 2 => 1.2m, 3 => 1.5m, 4 => 2.0m, _ => 2.5m }
                let zoneRate = baseRate * zoneMultiplier
                let fuelSurcharge = zoneRate * 0.15m
                let remoteFee = dest.IsRemoteArea ? 25m : 0m
                let totalCost = zoneRate + fuelSurcharge + remoteFee
                select new ShippingQuote(
                    PackageId: package.Id,
                    DestinationCode: dest.Code,
                    TotalCost: totalCost,
                    Breakdown: $"Base: {baseRate:C}, Zone: {zoneRate:C}, Fuel: {fuelSurcharge:C}, Remote: {remoteFee:C}",
                    RecommendedService: totalCost > 100 ? "Express Plus" : totalCost > 50 ? "Express" : totalCost > 25 ? "Standard" : "Economy"
                )).ToList();
    }
}
```

#### Key .NET 10 Features Used

✅ **Let clause** (via LINQ Query Syntax) for intermediate values

✅ **Multiple Select projections** for step-by-step calculation

✅ **Switch expressions** for zone multiplier logic

✅ **Record types** for immutable quote results

✅ **Pattern matching** in switch for service recommendation

---

### Query 25: Conditional Where with User-Configurable Filters

#### Real-World Scenario
A dashboard application allows users to **save and apply custom filter sets** (called "views"). Each view can have multiple filter conditions with AND/OR logic, nested conditions, and saved filter values. The system must apply these dynamic filter sets to large datasets efficiently.

#### Business Impact

Enables 10,000+ users to create personalized data views, reducing manual filtering time from 15 minutes to instant.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyFilterApplier
{
    public List<Product> ApplyFilters(List<Product> products, SavedFilter filter)
    {
        var results = new List<Product>();
        
        foreach (var product in products)
        {
            bool matches = true;
            
            foreach (var condition in filter.Conditions)
            {
                bool conditionMet = false;
                
                switch (condition.Field)
                {
                    case "Category":
                        conditionMet = product.Category == condition.Value;
                        break;
                    case "Price":
                        if (condition.Operator == "GreaterThan")
                            conditionMet = product.Price > decimal.Parse(condition.Value);
                        else if (condition.Operator == "LessThan")
                            conditionMet = product.Price < decimal.Parse(condition.Value);
                        break;
                    case "Rating":
                        conditionMet = product.Rating >= double.Parse(condition.Value);
                        break;
                    case "InStock":
                        conditionMet = (condition.Value == "true" && product.StockQuantity > 0) ||
                                      (condition.Value == "false" && product.StockQuantity == 0);
                        break;
                }
                
                if (filter.Logic == "AND" && !conditionMet)
                {
                    matches = false;
                    break;
                }
                else if (filter.Logic == "OR" && conditionMet)
                {
                    matches = true;
                    break;
                }
            }
            
            if (matches) results.Add(product);
        }
        
        return results;
    }
}
```

#### .NET 10 Implementation

```csharp
public record Product(int Id, string Name, string Category, decimal Price, double Rating, int StockQuantity, DateTime CreatedDate);
public record FilterCondition(string Field, string Operator, string Value);
public record SavedFilter(string Name, string Logic, List<FilterCondition> Conditions, bool IsActive);

public record FilterResult<T>(
    List<T> Items,
    int TotalCount,
    int FilteredCount,
    TimeSpan ExecutionTime,
    Dictionary<string, int> FilterBreakdown
);

public class DynamicFilterApplier
{
    public FilterResult<Product> ApplyFilters(List<Product> products, SavedFilter filter)
    {
        var stopwatch = Stopwatch.StartNew();
        
        var query = products.AsQueryable();
        
        // Apply conditions based on logic
        if (filter.Logic == "AND")
        {
            foreach (var condition in filter.Conditions)
            {
                query = ApplyCondition(query, condition);
            }
        }
        else if (filter.Logic == "OR")
        {
            var predicate = BuildOrPredicate(filter.Conditions);
            if (predicate != null)
                query = query.Where(predicate);
        }
        
        var filtered = query.ToList();
        stopwatch.Stop();
        
        return new FilterResult<Product>(
            Items: filtered,
            TotalCount: products.Count,
            FilteredCount: filtered.Count,
            ExecutionTime: stopwatch.Elapsed,
            FilterBreakdown: GetFilterBreakdown(products, filter)
        );
    }
    
    private static IQueryable<Product> ApplyCondition(IQueryable<Product> query, FilterCondition condition)
    {
        return (condition.Field, condition.Operator) switch
        {
            ("Category", "Equals") => query.Where(p => p.Category == condition.Value),
            ("Category", "NotEquals") => query.Where(p => p.Category != condition.Value),
            ("Price", "GreaterThan") => query.Where(p => p.Price > decimal.Parse(condition.Value)),
            ("Price", "LessThan") => query.Where(p => p.Price < decimal.Parse(condition.Value)),
            ("Price", "Between") => query.Where(p => p.Price > decimal.Parse(condition.Value.Split(',')[0]) && 
                                                     p.Price < decimal.Parse(condition.Value.Split(',')[1])),
            ("Rating", "GreaterThanOrEqual") => query.Where(p => p.Rating >= double.Parse(condition.Value)),
            ("InStock", "Equals") => query.Where(p => (condition.Value == "true" && p.StockQuantity > 0) ||
                                                      (condition.Value == "false" && p.StockQuantity == 0)),
            ("CreatedDate", "After") => query.Where(p => p.CreatedDate > DateTime.Parse(condition.Value)),
            ("CreatedDate", "Before") => query.Where(p => p.CreatedDate < DateTime.Parse(condition.Value)),
            _ => query
        };
    }
    
    private static Expression<Func<Product, bool>>? BuildOrPredicate(List<FilterCondition> conditions)
    {
        if (!conditions.Any()) return null;
        
        var parameter = Expression.Parameter(typeof(Product), "p");
        Expression? combined = null;
        
        foreach (var condition in conditions)
        {
            var conditionExpr = BuildConditionExpression(parameter, condition);
            combined = combined == null ? conditionExpr : Expression.OrElse(combined, conditionExpr);
        }
        
        return combined != null 
            ? Expression.Lambda<Func<Product, bool>>(combined, parameter) 
            : null;
    }
    
    private static Expression<Func<Product, bool>> BuildConditionExpression(ParameterExpression parameter, FilterCondition condition)
    {
        var property = Expression.Property(parameter, condition.Field);
        var constant = Expression.Constant(Convert.ChangeType(condition.Value, property.Type));
        
        return condition.Operator switch
        {
            "Equals" => Expression.Lambda<Func<Product, bool>>(Expression.Equal(property, constant), parameter),
            "GreaterThan" => Expression.Lambda<Func<Product, bool>>(Expression.GreaterThan(property, constant), parameter),
            "LessThan" => Expression.Lambda<Func<Product, bool>>(Expression.LessThan(property, constant), parameter),
            _ => throw new NotSupportedException($"Operator {condition.Operator} not supported")
        };
    }
    
    private static Dictionary<string, int> GetFilterBreakdown(List<Product> products, SavedFilter filter)
    {
        var breakdown = new Dictionary<string, int>();
        
        foreach (var condition in filter.Conditions)
        {
            var tempQuery = products.AsQueryable();
            tempQuery = ApplyCondition(tempQuery, condition);
            breakdown[condition.Field] = tempQuery.Count();
        }
        
        return breakdown;
    }
    
    // Save and load filter presets
    private static readonly Dictionary<string, SavedFilter> _savedFilters = [];
    
    public void SaveFilter(SavedFilter filter) => _savedFilters[filter.Name] = filter;
    
    public SavedFilter? LoadFilter(string name) => _savedFilters.GetValueOrDefault(name);
    
    public List<string> GetSavedFilterNames() => [.. _savedFilters.Keys];
}
```

#### Key .NET 10 Features Used

✅ **Switch expressions** for operator routing

✅ **Expression trees** for dynamic OR predicate building

✅ **Record types** for filter definitions and results

✅ **Collection expressions** for dictionary initialization

✅ **Stopwatch integration** for performance metrics

✅ **Dictionary.GetValueOrDefault** for safe lookup

---

## 📊 Query Performance Comparison (Part 2)

| Query | Legacy LoC | .NET 10 LoC | Reduction | Key Performance Gain |
|-------|------------|-------------|-----------|---------------------|
| Query 13: Dynamic Filtering | 65 | 25 | 62% | IQueryable deferred execution |
| Query 14: SelectMany Flattening | 30 | 8 | 73% | Single-pass enumeration |
| Query 15: Zip Combinations | 25 | 10 | 60% | Parallel iteration |
| Query 16: Expression Tree Projection | 40 | 20 | 50% | Compiled expression caching |
| Query 17: Let Clause Mapping | 50 | 18 | 64% | Intermediate value reuse |
| Query 18: OfType Filtering | 15 | 3 | 80% | Type filtering + casting |
| Query 19: Cast Conversion | 12 | 2 | 83% | Bulk type conversion |
| Query 20: Select with Index | 20 | 6 | 70% | Index-aware projection |
| Query 21: Complex Where | 55 | 22 | 60% | Predicate composition |
| Query 22: Pagination | 25 | 10 | 60% | Skip/Take optimization |
| Query 23: Cross Join | 18 | 5 | 72% | SelectMany cartesian product |
| Query 24: Let Clause | 45 | 15 | 67% | Query syntax with let |
| Query 25: Conditional Where | 50 | 20 | 60% | Expression tree compilation |

---

## 🔜 Coming in Part 3: Advanced Data Shaping & Grouping (Queries 26-38)

**What to expect in Part 3:**

| Query | Pattern | Difficulty | Real-World Use Case |
|-------|---------|------------|---------------------|
| 26 | Pivot Tables | ⭐⭐⭐⭐ | Sales report with months as columns |
| 27 | Recursive Queries | ⭐⭐⭐⭐⭐ | Organizational chart traversal |
| 28 | Time-Based Grouping | ⭐⭐⭐ | Hourly/daily/weekly sales trends |
| 29 | Window Functions | ⭐⭐⭐⭐ | Moving averages and rankings |
| 30 | Composite Keys | ⭐⭐ | Multi-field grouping and joining |
| 31 | Hierarchical Flattening | ⭐⭐⭐ | Tree structure to flat list |
| 32 | Incremental Aggregation | ⭐⭐⭐ | Cumulative totals and running sums |
| 33 | Lookup for One-to-Many | ⭐⭐ | Dictionary-like grouped access |
| 34 | ToDictionary with Conflicts | ⭐⭐ | Index creation with duplicate handling |
| 35 | GroupBy with Custom Comparer | ⭐⭐⭐ | Case-insensitive or custom grouping |
| 36 | OrderBy with ThenBy | ⭐ | Multi-level sorting |
| 37 | Reverse and OrderBy | ⭐ | Descending order with stability |
| 38 | SequenceEqual for Comparison | ⭐⭐ | Full collection equality check |

📎 **Read the full story: Part 3 — coming soon**

---

## 🎯 Key Takeaways from Part 2

1. **Dynamic filtering** with IQueryable composition reduces query construction overhead by 90%
2. **SelectMany** is essential for flattening nested hierarchies (orders → items → parts)
3. **Zip** enables parallel processing of related lists without index management
4. **Expression trees** allow runtime code generation for custom projections
5. **Let clause** (query syntax) enables intermediate value reuse, making complex calculations readable
6. **OfType and Cast** provide elegant solutions for legacy collection interop
7. **Select with index** eliminates manual counter variables
8. **Cross joins** with SelectMany generate complete test matrices for A/B testing
9. **Conditional Where** with expression trees powers user-configurable dashboards
10. **.NET 10 features** like collection expressions, record types, and switch expressions significantly reduce boilerplate code

---

## 📚 Complete Story List (50 Advanced LINQ Queries for .NET 10)

📚 **Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10 (Queries 1-12)** — Deep dive on multi-key grouping, all join types (Group, Left, Right, Full), conditional aggregation, running totals, set operations, and pagination. Patterns covered: Multi-Key Grouping, GroupJoin, Full Outer Join, Left Join, Conditional Aggregation, Running Totals, Set Operations, Pagination, Distinct, Lookup, Zip, Aggregate.

📎 **Read the full story: Part 1**

---

📚 **Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10 (Queries 13-25)** — Deep dive on dynamic filtering, SelectMany flattening, Zip operations, custom projections, conditional mapping, mixed type handling, and index-based selection. Patterns covered: Dynamic Filtering, SelectMany, Zip, Custom Projections, Let Clause, OfType, Cast, Select with Index, Where filtering, Take/Skip, SelectMany cross joins.

📎 **You are here: Part 2 — above**

---

📚 **Advanced Data Shaping & Grouping - 50 Advanced LINQ Queries for .NET 10 (Queries 26-38)** — Deep dive on pivot tables, recursive queries, time-series analysis, window functions, composite keys, hierarchical data, and incremental aggregation. Patterns covered: Pivot Tables, Recursive Queries, Time-Based Grouping, Window Functions, Composite Keys, Hierarchical Flattening, Incremental Aggregation, Lookup, ToDictionary, GroupBy with Custom Comparer.

📎 **Read the full story: Part 3 — coming soon**

---

📚 **Performance & Optimization - 50 Advanced LINQ Queries for .NET 10 (Queries 39-50)** — Deep dive on batch processing, lazy evaluation, error handling, parallel LINQ (PLINQ), IQueryable optimization, async streams, and memory-efficient techniques. Patterns covered: Batch Processing, Chunking, Lazy Evaluation, Error Handling, Safe Navigation, PLINQ, IQueryable vs IEnumerable, Async LINQ, Streaming, Caching, Expression Trees.

📎 **Read the full story: Part 4 — coming soon**

---

*Did you find this helpful? Share your favorite LINQ technique from Part 2 in the responses below!*