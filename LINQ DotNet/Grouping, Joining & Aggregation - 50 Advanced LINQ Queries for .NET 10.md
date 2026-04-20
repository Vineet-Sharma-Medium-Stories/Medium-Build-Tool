# Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10
### Deep dive on multi-key grouping, all join types (Group, Left, Right, Full), conditional aggregation, running totals, set operations, and pagination. Patterns covered: Multi-Key Grouping, GroupJoin, Full Outer Join, Left Join, Conditional Aggregation, Running Totals, Set Operations, Pagination, Distinct, Lookup,

![Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10](<images/Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10.png>)

> **📌 New in .NET 10 & LINQ:** This series leverages the latest .NET 10 features including collection expressions (`[..]`), primary constructors, `IAsyncEnumerable<T>`, `TimeSpan.From*` improvements, `SearchValues<T>` for string searching, enhanced `DateOnly`/`TimeOnly` support, and the new `System.Linq.AsyncExtensions` for async LINQ operations.

---

## 🎯 Introduction: Why LINQ in .NET 10 Changes Everything

### The Evolution of Data Querying in .NET

Language Integrated Query (LINQ) revolutionized .NET development when it was introduced in .NET Framework 3.5 (2007). Fast forward to **.NET 10** — LINQ has evolved from a simple collection querying tool into a **comprehensive data manipulation ecosystem** that spans:

- **In-memory collections** (`IEnumerable<T>`)
- **Remote databases** (`IQueryable<T>` via Entity Framework Core)
- **XML/JSON documents** (LINQ to XML)
- **Cloud storage** (Azure Cosmos DB LINQ provider)
- **Real-time streams** (`IAsyncEnumerable<T>` with async LINQ)
- **Graph data** (Apache Age, Neo4j LINQ providers)

### Why LINQ Matters More Than Ever in .NET 10

| Capability | Traditional Approach | LINQ in .NET 10 | Productivity Gain |
|------------|---------------------|-----------------|-------------------|
| **Query Syntax** | SQL strings or nested loops | Native C# syntax with IntelliSense | 5x faster development |
| **Type Safety** | Runtime errors for column names | Compile-time checking | 90% fewer query bugs |
| **Cross-Source Queries** | Manual data reconciliation | Unified syntax for any data source | 70% less code |
| **Parallel Processing** | Manual `Parallel.ForEach` | `.AsParallel()` with automatic partitioning | 10x simpler concurrency |
| **Async Data Streams** | Complex `IAsyncEnumerable` manual iteration | `.Await()` and `.AwaitCompletion()` | Built-in backpressure handling |
| **Performance Optimization** | Manual caching strategies | `.AsNoTracking()`, `.AsSplitQuery()` | 40% faster by default |

### What's New in .NET 10 LINQ?

```csharp
// .NET 10 specific improvements

// 1. Enhanced collection expressions
var products = new List<Product> { p1, p2, p3 };  // Traditional
var products = [p1, p2, p3];                      // .NET 10 - simpler syntax

// 2. Primary constructors with records
public record Employee(string Name, decimal Salary);  // Immutable with less code

// 3. Async LINQ extensions
await foreach (var item in dbContext.Orders
    .Where(o => o.Amount > 100)
    .AsAsyncEnumerable())
{
    Console.WriteLine(item);
}

// 4. Enhanced DateOnly/TimeOnly support in LINQ queries
var todaysOrders = orders.Where(o => o.OrderDate == DateOnly.FromDateTime(DateTime.Today));

// 5. Improved GroupBy with custom equality comparers
var grouped = employees.GroupBy(e => e.Department, StringComparer.OrdinalIgnoreCase);

// 6. New TryGetNonEnumeratedCount for performance checks
if (query.TryGetNonEnumeratedCount(out int count) && count > 1000)
{
    // Optimize for large datasets
}

// 7. Chunk improvements with better memory allocation
foreach (var chunk in data.Chunk(1000))
{
    await ProcessBatchAsync(chunk);
}
```

### The Business Case for Mastering LINQ in .NET 10

**For Individual Developers:**
- 📈 **25-40% faster development** of data access layers
- 🐛 **Significantly fewer bugs** due to compile-time validation
- 🔧 **More maintainable code** with declarative rather than imperative style
- 💰 **Higher market value** — LINQ expertise is in top 5 requested .NET skills

**For Teams and Organizations:**
- 🔄 **Consistent patterns** across all data access code
- 📊 **Better performance** with automatic optimization opportunities
- 🔍 **Easier code reviews** with predictable query patterns
- 🚀 **Faster onboarding** for new team members

---

## 📚 Story List

📚 **Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10 (Queries 1-12)** — Deep dive on multi-key grouping, all join types (Group, Left, Right, Full), conditional aggregation, running totals, set operations, and pagination. Patterns covered: Multi-Key Grouping, GroupJoin, Full Outer Join, Left Join, Conditional Aggregation, Running Totals, Set Operations, Pagination, Distinct, Lookup, Zip, Aggregate.

📎 **You are here: Part 1 — below**

---

📚 **Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10 (Queries 13-25)** — Deep dive on dynamic filtering, SelectMany flattening, Zip operations, custom projections, conditional mapping, mixed type handling, and index-based selection. Patterns covered: Dynamic Filtering, SelectMany, Zip, Custom Projections, Let Clause, OfType, Cast, Select with Index, Where filtering, Take/Skip, SelectMany cross joins.

📎 **Read the full story: Part 2 — coming soon**


📚 **Advanced Data Shaping & Grouping - 50 Advanced LINQ Queries for .NET 10 (Queries 26-38)** — Deep dive on pivot tables, recursive queries, time-series analysis, window functions, composite keys, hierarchical data, and incremental aggregation. Patterns covered: Pivot Tables, Recursive Queries, Time-Based Grouping, Window Functions, Composite Keys, Hierarchical Flattening, Incremental Aggregation, Lookup, ToDictionary, GroupBy with Custom Comparer.

📎 **Read the full story: Part 3 — coming soon**


📚 **Performance & Optimization - 50 Advanced LINQ Queries for .NET 10 (Queries 39-50)** — Deep dive on batch processing, lazy evaluation, error handling, parallel LINQ (PLINQ), IQueryable optimization, async streams, and memory-efficient techniques. Patterns covered: Batch Processing, Chunking, Lazy Evaluation, Error Handling, Safe Navigation, PLINQ, IQueryable vs IEnumerable, Async LINQ, Streaming, Caching, Expression Trees.

📎 **Read the full story: Part 4 — coming soon**



## 📖 Part 1: Grouping, Joining & Aggregation (Queries 1-12)


### Query 1: Multi-Key Grouping with Calculations

#### Real-World Scenario
A retail chain with 500+ stores across 3 countries needs a **regional performance dashboard**. For each combination of (Country, StoreType, ProductCategory), calculate:
- Total revenue
- Average transaction value
- Top-selling product
- Month-over-month growth

#### Business Impact
This query powers the executive dashboard viewed by 50+ regional managers daily, tracking $50M+ in quarterly sales.

#### Legacy Approach (.NET Framework 2.0)

```csharp
// ~45 lines of nested loops and manual aggregation
public class LegacySalesAggregator
{
    public List<RegionalReport> GetRegionalReports(List<Sale> sales)
    {
        var dict = new Dictionary<string, Dictionary<string, Dictionary<string, List<Sale>>>>();
        
        foreach (var sale in sales)
        {
            if (!dict.ContainsKey(sale.Country))
                dict[sale.Country] = new Dictionary<string, Dictionary<string, List<Sale>>>();
            
            var storeDict = dict[sale.Country];
            if (!storeDict.ContainsKey(sale.StoreType))
                storeDict[sale.StoreType] = new Dictionary<string, List<Sale>>();
            
            var categoryDict = storeDict[sale.StoreType];
            if (!categoryDict.ContainsKey(sale.ProductCategory))
                categoryDict[sale.ProductCategory] = new List<Sale>();
            
            categoryDict[sale.ProductCategory].Add(sale);
        }
        
        var results = new List<RegionalReport>();
        foreach (var country in dict)
        foreach (var store in country.Value)
        foreach (var category in store.Value)
        {
            var salesList = category.Value;
            results.Add(new RegionalReport
            {
                Country = country.Key,
                StoreType = store.Key,
                ProductCategory = category.Key,
                TotalRevenue = salesList.Sum(s => s.Amount),
                AverageTransaction = salesList.Average(s => s.Amount),
                TopProduct = salesList.GroupBy(s => s.Product)
                    .OrderByDescending(g => g.Count())
                    .First().Key
            });
        }
        return results;
    }
}

public class RegionalReport
{
    public string Country { get; set; }
    public string StoreType { get; set; }
    public string ProductCategory { get; set; }
    public decimal TotalRevenue { get; set; }
    public double AverageTransaction { get; set; }
    public string TopProduct { get; set; }
}

public class Sale
{
    public string Country { get; set; }
    public string StoreType { get; set; }
    public string ProductCategory { get; set; }
    public string Product { get; set; }
    public decimal Amount { get; set; }
    public DateTime SaleDate { get; set; }
}
```

#### .NET 10 Implementation

```csharp
// Modern approach: ~12 lines with composite keys and collection expressions
public record Sale(
    string Country,
    string StoreType,
    string ProductCategory,
    string Product,
    decimal Amount,
    DateOnly SaleDate
);

public record RegionalReport(
    string Country,
    string StoreType,
    string ProductCategory,
    decimal TotalRevenue,
    double AverageTransaction,
    string TopProduct,
    int TransactionCount,
    decimal GrowthPercent
);

public class ModernSalesAggregator
{
    public List<RegionalReport> GetRegionalReports(List<Sale> sales, DateOnly previousMonthStart)
    {
        var currentSales = sales.Where(s => s.SaleDate >= previousMonthStart);
        
        return currentSales
            .GroupBy(s => new { s.Country, s.StoreType, s.ProductCategory })
            .Select(g => new RegionalReport(
                Country: g.Key.Country,
                StoreType: g.Key.StoreType,
                ProductCategory: g.Key.ProductCategory,
                TotalRevenue: g.Sum(s => s.Amount),
                AverageTransaction: g.Average(s => (double)s.Amount),
                TopProduct: g.GroupBy(s => s.Product)
                    .MaxBy(pg => pg.Count())?.Key ?? "N/A",
                TransactionCount: g.Count(),
                GrowthPercent: CalculateGrowth(g, sales, previousMonthStart)
            ))
            .OrderBy(r => r.Country)
            .ThenByDescending(r => r.TotalRevenue)
            .ToList();
    }
    
    private static decimal CalculateGrowth(
        IGrouping<dynamic, Sale> currentGroup,
        List<Sale> allSales,
        DateOnly previousMonthStart)
    {
        var previousMonthStartDate = previousMonthStart.AddMonths(-1);
        
        var previousTotal = allSales
            .Where(s => s.Country == currentGroup.Key.Country &&
                        s.StoreType == currentGroup.Key.StoreType &&
                        s.ProductCategory == currentGroup.Key.ProductCategory &&
                        s.SaleDate >= previousMonthStartDate &&
                        s.SaleDate < previousMonthStart)
            .Sum(s => s.Amount);
        
        var currentTotal = currentGroup.Sum(s => s.Amount);
        return previousTotal == 0 ? 100m : (currentTotal - previousTotal) / previousTotal * 100;
    }
}

// Usage example
var sales = new List<Sale>
{
    new Sale("USA", "Flagship", "Electronics", "Laptop", 1200m, new DateOnly(2024, 1, 15)),
    new Sale("USA", "Flagship", "Electronics", "Phone", 800m, new DateOnly(2024, 1, 20)),
    new Sale("UK", "Outlet", "Clothing", "Jacket", 150m, new DateOnly(2024, 1, 10)),
};

var aggregator = new ModernSalesAggregator();
var reports = aggregator.GetRegionalReports(sales, new DateOnly(2024, 1, 1));
```

#### Key .NET 10 Features Used

✅ **Record types** with primary constructors for immutable data models

✅ **DateOnly** type for date operations without time component

✅ **Collection expressions** for list initialization

✅ **Dynamic grouping keys** with anonymous types

✅ **MaxBy** LINQ method for efficient max value extraction

✅ **Spread operator** for collection expressions



### Query 2: GroupJoin - Hierarchical Department-Employee Reporting

#### Real-World Scenario
An HR system needs to generate **organization charts** showing:
- Each department with its employees (even empty departments)
- Employees without departments (unassigned)
- Manager-subordinate relationships
- Department hierarchy levels

#### Business Impact
Used by 200+ HR managers across enterprise, tracking 10,000+ employees, reducing org chart generation time from 2 hours to 5 seconds.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyOrgChartBuilder
{
    public List<DepartmentReport> BuildOrgChart(List<Department> departments, List<Employee> employees)
    {
        var results = new List<DepartmentReport>();
        
        foreach (var dept in departments)
        {
            var deptEmployees = new List<Employee>();
            foreach (var emp in employees)
            {
                if (emp.DepartmentId == dept.Id)
                {
                    deptEmployees.Add(emp);
                }
            }
            
            var employeeDetails = new List<EmployeeDetail>();
            decimal totalSalary = 0;
            decimal maxSalary = 0;
            decimal minSalary = decimal.MaxValue;
            
            foreach (var emp in deptEmployees)
            {
                employeeDetails.Add(new EmployeeDetail
                {
                    Name = emp.Name,
                    Position = emp.Position,
                    Salary = emp.Salary,
                    IsManager = emp.Position.Contains("Manager") || emp.Id == dept.ManagerId
                });
                totalSalary += emp.Salary;
                if (emp.Salary > maxSalary) maxSalary = emp.Salary;
                if (emp.Salary < minSalary) minSalary = emp.Salary;
            }
            
            var subDepartments = new List<string>();
            foreach (var d in departments)
            {
                if (d.ManagerId == dept.Id)
                {
                    subDepartments.Add(d.Name);
                }
            }
            
            string managerName = null;
            foreach (var emp in employees)
            {
                if (emp.Id == dept.ManagerId)
                {
                    managerName = emp.Name;
                    break;
                }
            }
            
            results.Add(new DepartmentReport
            {
                DepartmentName = dept.Name,
                DepartmentLevel = dept.Level,
                EmployeeCount = deptEmployees.Count,
                TotalSalary = totalSalary,
                AverageSalary = deptEmployees.Count > 0 ? totalSalary / deptEmployees.Count : 0,
                MaxSalary = maxSalary,
                MinSalary = minSalary == decimal.MaxValue ? 0 : minSalary,
                Employees = employeeDetails,
                SubDepartments = subDepartments,
                ManagerName = managerName
            });
        }
        
        return results;
    }
}

public class Department
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int? ManagerId { get; set; }
    public int Level { get; set; }
}

public class Employee
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int DepartmentId { get; set; }
    public string Position { get; set; }
    public decimal Salary { get; set; }
}

public class DepartmentReport
{
    public string DepartmentName { get; set; }
    public int DepartmentLevel { get; set; }
    public int EmployeeCount { get; set; }
    public decimal TotalSalary { get; set; }
    public decimal AverageSalary { get; set; }
    public decimal MaxSalary { get; set; }
    public decimal MinSalary { get; set; }
    public List<EmployeeDetail> Employees { get; set; }
    public List<string> SubDepartments { get; set; }
    public string ManagerName { get; set; }
}

public class EmployeeDetail
{
    public string Name { get; set; }
    public string Position { get; set; }
    public decimal Salary { get; set; }
    public bool IsManager { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Department(int Id, string Name, int? ManagerId, int Level);
public record Employee(int Id, string Name, int DepartmentId, string Position, decimal Salary, DateOnly HireDate);

public record DepartmentReport(
    string DepartmentName,
    int DepartmentLevel,
    int EmployeeCount,
    decimal TotalSalary,
    decimal AverageSalary,
    decimal MaxSalary,
    decimal MinSalary,
    List<EmployeeDetail> Employees,
    List<string> SubDepartments,
    string? ManagerName
);

public record EmployeeDetail(
    string Name, 
    string Position, 
    decimal Salary, 
    bool IsManager,
    int TenureYears,
    string PerformanceRating
);

public class OrgChartBuilder
{
    public List<DepartmentReport> BuildOrgChart(List<Department> departments, List<Employee> employees)
    {
        var currentDate = DateOnly.FromDateTime(DateTime.Today);
        
        // GroupJoin: each department gets its employees (even if none)
        return departments
            .GroupJoin(
                employees,
                dept => dept.Id,
                emp => emp.DepartmentId,
                (dept, deptEmployees) => new DepartmentReport(
                    DepartmentName: dept.Name,
                    DepartmentLevel: dept.Level,
                    EmployeeCount: deptEmployees.Count(),
                    TotalSalary: deptEmployees.Sum(e => e.Salary),
                    AverageSalary: deptEmployees.DefaultIfEmpty().Average(e => e?.Salary ?? 0),
                    MaxSalary: deptEmployees.Any() ? deptEmployees.Max(e => e.Salary) : 0,
                    MinSalary: deptEmployees.Any() ? deptEmployees.Min(e => e.Salary) : 0,
                    Employees: deptEmployees
                        .Select(e => new EmployeeDetail(
                            Name: e.Name,
                            Position: e.Position,
                            Salary: e.Salary,
                            IsManager: e.Position.Contains("Manager") || e.Id == dept.ManagerId,
                            TenureYears: (int)((currentDate.DayNumber - e.HireDate.DayNumber) / 365.25),
                            PerformanceRating: CalculatePerformanceRating(e)
                        ))
                        .OrderByDescending(e => e.IsManager)
                        .ThenByDescending(e => e.Salary)
                        .ToList(),
                    SubDepartments: departments
                        .Where(d => d.ManagerId == dept.Id)
                        .Select(d => d.Name)
                        .ToList(),
                    ManagerName: employees.FirstOrDefault(e => e.Id == dept.ManagerId)?.Name
                ))
            .OrderBy(r => r.DepartmentLevel)
            .ThenBy(r => r.DepartmentName)
            .ToList();
    }
    
    private static string CalculatePerformanceRating(Employee e)
    {
        return e.Salary switch
        {
            > 100000 => "Excellent",
            > 70000 => "Good",
            > 40000 => "Satisfactory",
            _ => "Needs Improvement"
        };
    }
    
    // Find unassigned employees (Left Join simulation)
    public List<Employee> GetUnassignedEmployees(List<Department> departments, List<Employee> employees)
    {
        var departmentIds = departments.Select(d => d.Id).ToHashSet();
        return [.. employees.Where(e => !departmentIds.Contains(e.DepartmentId))];
    }
    
    // Find departments without employees (Right Join simulation)
    public List<Department> GetEmptyDepartments(List<Department> departments, List<Employee> employees)
    {
        var departmentsWithEmployees = employees.Select(e => e.DepartmentId).ToHashSet();
        return [.. departments.Where(d => !departmentsWithEmployees.Contains(d.Id))];
    }
}
```

#### Key .NET 10 Features Used

✅ **GroupJoin** for hierarchical one-to-many relationships

✅ **DateOnly.DayNumber** for accurate tenure calculation

✅ **Collection expressions** with spread operator `[..]`

✅ **Switch expressions** for performance rating logic

✅ **DefaultIfEmpty** for handling empty groups in aggregation

✅ **Record types** with multiple constructors

✅ **Primary constructors** for immutable data models



### Query 3: Full Outer Join - Customer-Order Reconciliation

#### Real-World Scenario
A financial system needs to reconcile **customers with their orders** and vice versa:
- Customers who haven't ordered (for marketing campaigns)
- Orphaned orders (system errors where customer was deleted)
- Complete customer-order matrix for audit
- Data quality scoring for compliance reporting

#### Business Impact
Critical for financial audit compliance (SOX, GDPR), identifying $2M+ in orphaned orders annually, reducing data quality issues by 95%.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyOrderReconciler
{
    public List<ReconciliationRecord> FullOuterReconciliation(List<Customer> customers, List<Order> orders)
    {
        var results = new List<ReconciliationRecord>();
        var processedCustomerIds = new HashSet<int>();
        
        // Process matches and left side (customers without orders)
        foreach (var customer in customers)
        {
            var customerOrders = new List<Order>();
            foreach (var order in orders)
            {
                if (order.CustomerId == customer.Id)
                {
                    customerOrders.Add(order);
                    processedCustomerIds.Add(customer.Id);
                }
            }
            
            if (customerOrders.Count == 0)
            {
                // Customer with no orders
                results.Add(new ReconciliationRecord
                {
                    CustomerName = customer.Name,
                    CustomerEmail = customer.Email,
                    CustomerStatus = customer.Status,
                    OrderId = null,
                    OrderAmount = null,
                    OrderDate = null,
                    OrderStatus = "No Order",
                    ReconciliationStatus = "⚠️ Warning - Inactive Customer",
                    ActionRequired = "Marketing: Send re-engagement campaign",
                    Priority = "P2 - Medium"
                });
            }
            else
            {
                foreach (var order in customerOrders)
                {
                    results.Add(new ReconciliationRecord
                    {
                        CustomerName = customer.Name,
                        CustomerEmail = customer.Email,
                        CustomerStatus = customer.Status,
                        OrderId = order.Id,
                        OrderAmount = order.Amount,
                        OrderDate = order.OrderDate,
                        OrderStatus = order.Status,
                        ReconciliationStatus = order.Status == "Cancelled" ? "ℹ️ Info - Cancelled Order" : "✅ Valid - Matched",
                        ActionRequired = order.Amount > 10000 ? "Audit: Flag for quarterly review" : "None",
                        Priority = order.Amount > 10000 ? "P1 - High" : "P3 - Low"
                    });
                }
            }
        }
        
        // Process right side (orders without customers - orphaned)
        foreach (var order in orders)
        {
            if (!processedCustomerIds.Contains(order.CustomerId))
            {
                results.Add(new ReconciliationRecord
                {
                    CustomerName = "⚠️ ORPHANED ORDER",
                    CustomerEmail = "N/A",
                    CustomerStatus = "Deleted",
                    OrderId = order.Id,
                    OrderAmount = order.Amount,
                    OrderDate = order.OrderDate,
                    OrderStatus = order.Status,
                    ReconciliationStatus = "❌ Critical - Orphaned Order",
                    ActionRequired = "Immediate: Investigate customer deletion, restore if possible",
                    Priority = "P0 - Critical"
                });
            }
        }
        
        return results;
    }
}

public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Status { get; set; }
}

public class Order
{
    public int Id { get; set; }
    public int CustomerId { get; set; }
    public decimal Amount { get; set; }
    public DateTime OrderDate { get; set; }
    public string Status { get; set; }
}

public class ReconciliationRecord
{
    public string CustomerName { get; set; }
    public string CustomerEmail { get; set; }
    public string CustomerStatus { get; set; }
    public int? OrderId { get; set; }
    public decimal? OrderAmount { get; set; }
    public DateTime? OrderDate { get; set; }
    public string OrderStatus { get; set; }
    public string ReconciliationStatus { get; set; }
    public string ActionRequired { get; set; }
    public string Priority { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Customer(int Id, string Name, string Email, DateOnly RegisteredDate, string Status);
public record Order(int Id, int CustomerId, decimal Amount, DateTime OrderDate, string Status, string PaymentMethod);

public record ReconciliationRecord(
    string CustomerName,
    string CustomerEmail,
    string CustomerStatus,
    int? OrderId,
    decimal? OrderAmount,
    DateTime? OrderDate,
    string OrderStatus,
    string ReconciliationStatus,
    string ActionRequired,
    string Priority
);

public record ReconciliationSummary(
    int TotalCustomers,
    int TotalOrders,
    int OrphanedCount,
    decimal OrphanedValue,
    int InactiveCustomerCount,
    double DataQualityScore
);

public class OrderReconciler
{
    public List<ReconciliationRecord> FullOuterReconciliation(List<Customer> customers, List<Order> orders)
    {
        // Left join: customers with their orders
        var leftJoin = from c in customers
                       join o in orders on c.Id equals o.CustomerId into customerOrders
                       from o in customerOrders.DefaultIfEmpty()
                       select new { Customer = c, Order = o };
        
        // Right join: orders with their customers
        var rightJoin = from o in orders
                        join c in customers on o.CustomerId equals c.Id into orderCustomers
                        from c in orderCustomers.DefaultIfEmpty()
                        select new { Customer = c, Order = o };
        
        // Full outer join using Union with custom comparer
        return leftJoin
            .Union(rightJoin)
            .Distinct()
            .Select(x => new ReconciliationRecord(
                CustomerName: x.Customer?.Name ?? "⚠️ ORPHANED ORDER",
                CustomerEmail: x.Customer?.Email ?? "N/A",
                CustomerStatus: x.Customer?.Status ?? "Deleted",
                OrderId: x.Order?.Id,
                OrderAmount: x.Order?.Amount,
                OrderDate: x.Order?.OrderDate,
                OrderStatus: x.Order?.Status ?? "No Order",
                ReconciliationStatus: (x.Customer, x.Order) switch
                {
                    (null, not null) => "❌ Critical - Orphaned Order",
                    (not null, null) => "⚠️ Warning - Inactive Customer",
                    (not null, not null) when x.Order.Status == "Cancelled" => "ℹ️ Info - Cancelled Order",
                    (not null, not null) => "✅ Valid - Matched",
                    (null, null) => "❓ Error - Impossible State"
                },
                ActionRequired: (x.Customer, x.Order) switch
                {
                    (null, not null) => "Immediate: Investigate customer deletion, restore if possible",
                    (not null, null) => "Marketing: Send re-engagement campaign within 7 days",
                    (not null, not null) when x.Order.Amount > 10000 => "Audit: Flag for quarterly review",
                    _ => "None required"
                },
                Priority: (x.Customer, x.Order) switch
                {
                    (null, not null) => "P0 - Critical",
                    (not null, null) when x.Customer.Status == "Active" => "P1 - High",
                    (not null, null) => "P2 - Medium",
                    _ => "P3 - Low"
                }
            ))
            .OrderBy(r => r.Priority)
            .ThenBy(r => r.ReconciliationStatus)
            .ThenBy(r => r.CustomerName)
            .ToList();
    }
    
    // Using collection expressions for anomaly detection
    public (List<Customer> InactiveCustomers, List<Order> OrphanedOrders, ReconciliationSummary Summary) 
        GetAnomalies(List<Customer> customers, List<Order> orders)
    {
        var customerIds = customers.Select(c => c.Id).ToHashSet();
        var orderCustomerIds = orders.Select(o => o.CustomerId).ToHashSet();
        
        var inactiveCustomers = customers
            .Where(c => !orderCustomerIds.Contains(c.Id) && c.Status == "Active")
            .ToList();
        
        var orphanedOrders = orders
            .Where(o => !customerIds.Contains(o.CustomerId))
            .ToList();
        
        return (
            InactiveCustomers: [.. inactiveCustomers],
            OrphanedOrders: [.. orphanedOrders],
            Summary: new ReconciliationSummary(
                TotalCustomers: customers.Count,
                TotalOrders: orders.Count,
                OrphanedCount: orphanedOrders.Count,
                OrphanedValue: orphanedOrders.Sum(o => o.Amount),
                InactiveCustomerCount: inactiveCustomers.Count,
                DataQualityScore: CalculateDataQualityScore(customers, orders)
            )
        );
    }
    
    private static double CalculateDataQualityScore(List<Customer> customers, List<Order> orders)
    {
        var matchedCustomers = customers.Count(c => orders.Any(o => o.CustomerId == c.Id));
        var matchedOrders = orders.Count(o => customers.Any(c => c.Id == o.CustomerId));
        
        var customerScore = matchedCustomers / (double)customers.Count * 50;
        var orderScore = matchedOrders / (double)orders.Count * 50;
        
        return Math.Round(customerScore + orderScore, 2);
    }
}
```

#### Key .NET 10 Features Used

✅ **LINQ Query Syntax** with `join...into` for clarity

✅ **Tuple deconstruction** for multiple return values

✅ **Switch expressions** for complex conditional logic

✅ **Collection expressions** `[..]` for list creation

✅ **Records with multiple constructors** for immutable DTOs

✅ **Union and Distinct** for full outer join simulation



### Query 4: Left Join with DefaultIfEmpty - Customer Retention Report

#### Real-World Scenario
A subscription-based SaaS company needs to identify **customers at risk of churn**:
- Customers with no activity in last 30 days
- Customers with decreasing usage patterns
- Trial users who haven't converted
- Annual subscribers approaching renewal

#### Business Impact
Reduces customer churn by 25% through targeted retention campaigns, saving $5M+ in annual recurring revenue.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyRetentionAnalytics
{
    public List<ChurnRiskReport> IdentifyAtRiskCustomers(List<Subscriber> subscribers, List<UsageEvent> usageEvents, int daysThreshold = 30)
    {
        var results = new List<ChurnRiskReport>();
        var cutoffDate = DateTime.Now.AddDays(-daysThreshold);
        
        foreach (var subscriber in subscribers)
        {
            var recentUsage = new List<UsageEvent>();
            foreach (var usage in usageEvents)
            {
                if (usage.SubscriberId == subscriber.Id && usage.EventDate >= cutoffDate)
                {
                    recentUsage.Add(usage);
                }
            }
            
            int daysSinceLastActivity;
            if (subscriber.LastActivityDate.HasValue)
            {
                daysSinceLastActivity = (DateTime.Now - subscriber.LastActivityDate.Value).Days;
            }
            else
            {
                daysSinceLastActivity = (DateTime.Now - subscriber.SubscriptionDate).Days;
            }
            
            string riskLevel;
            string recommendedAction;
            bool sendRetentionEmail;
            
            if (subscriber.IsTrial && daysSinceLastActivity > 7)
            {
                riskLevel = "🔴 Critical - Trial Expiring";
                recommendedAction = "Send conversion reminder before trial ends";
                sendRetentionEmail = true;
            }
            else if (daysSinceLastActivity > 60)
            {
                riskLevel = "🔴 Critical - Inactive > 60 days";
                recommendedAction = "Escalate to account manager + 50% discount offer";
                sendRetentionEmail = true;
            }
            else if (daysSinceLastActivity > 30)
            {
                riskLevel = "🟠 High - Inactive > 30 days";
                recommendedAction = "Send re-engagement campaign with feature highlights";
                sendRetentionEmail = true;
            }
            else if (daysSinceLastActivity > 14 && recentUsage.Count == 0)
            {
                riskLevel = "🟡 Medium - Low engagement";
                recommendedAction = "Send upgrade incentives";
                sendRetentionEmail = true;
            }
            else if (daysSinceLastActivity > 7 && subscriber.IsTrial)
            {
                riskLevel = "🟡 Medium - Trial at risk";
                recommendedAction = "Send conversion reminder";
                sendRetentionEmail = true;
            }
            else
            {
                riskLevel = "🟢 Low - Active customer";
                recommendedAction = "Monitor standard nurture campaign";
                sendRetentionEmail = false;
            }
            
            results.Add(new ChurnRiskReport
            {
                CustomerName = subscriber.Name,
                Email = subscriber.Email,
                Plan = subscriber.Plan,
                DaysSinceLastActivity = daysSinceLastActivity,
                TotalUsageEvents = recentUsage.Count,
                TotalApiCalls = recentUsage.Sum(u => u.ApiCalls),
                RiskLevel = riskLevel,
                RecommendedAction = recommendedAction,
                SendRetentionEmail = sendRetentionEmail
            });
        }
        
        return results;
    }
}

public class Subscriber
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Plan { get; set; }
    public DateTime SubscriptionDate { get; set; }
    public DateTime? LastActivityDate { get; set; }
    public bool IsTrial { get; set; }
}

public class UsageEvent
{
    public int SubscriberId { get; set; }
    public DateTime EventDate { get; set; }
    public string Feature { get; set; }
    public int DurationMinutes { get; set; }
    public decimal ApiCalls { get; set; }
}

public class ChurnRiskReport
{
    public string CustomerName { get; set; }
    public string Email { get; set; }
    public string Plan { get; set; }
    public int DaysSinceLastActivity { get; set; }
    public int TotalUsageEvents { get; set; }
    public decimal TotalApiCalls { get; set; }
    public string RiskLevel { get; set; }
    public string RecommendedAction { get; set; }
    public bool SendRetentionEmail { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Subscriber(
    int Id,
    string Name,
    string Email,
    string Plan,
    DateTime SubscriptionDate,
    DateTime? LastActivityDate,
    bool IsTrial
);

public record UsageEvent(
    int SubscriberId,
    DateTime EventDate,
    string Feature,
    int DurationMinutes,
    decimal ApiCalls
);

public record ChurnRiskReport(
    string CustomerName,
    string Email,
    string Plan,
    int DaysSinceLastActivity,
    int TotalUsageEvents,
    decimal TotalApiCalls,
    string RiskLevel,
    string RecommendedAction,
    bool SendRetentionEmail
);

public class RetentionAnalytics
{
    public List<ChurnRiskReport> IdentifyAtRiskCustomers(
        List<Subscriber> subscribers,
        List<UsageEvent> usageEvents,
        int daysThreshold = 30)
    {
        var cutoffDate = DateTime.Now.AddDays(-daysThreshold);
        
        // Left join to include customers with no usage
        return subscribers
            .GroupJoin(
                usageEvents.Where(u => u.EventDate >= cutoffDate),
                s => s.Id,
                u => u.SubscriberId,
                (subscriber, recentUsage) => new { subscriber, recentUsage }
            )
            .SelectMany(
                x => x.recentUsage.DefaultIfEmpty(),
                (x, usage) => new { x.subscriber, usage }
            )
            .GroupBy(x => x.subscriber.Id)
            .Select(g => new
            {
                Subscriber = g.First().subscriber,
                UsageEvents = g.Where(x => x.usage != null).Select(x => x.usage).ToList(),
                DaysSinceLastActivity = g.First().subscriber.LastActivityDate.HasValue
                    ? (DateTime.Now - g.First().subscriber.LastActivityDate.Value).Days
                    : (DateTime.Now - g.First().subscriber.SubscriptionDate).Days
            })
            .Select(x => new ChurnRiskReport(
                CustomerName: x.Subscriber.Name,
                Email: x.Subscriber.Email,
                Plan: x.Subscriber.Plan,
                DaysSinceLastActivity: x.DaysSinceLastActivity,
                TotalUsageEvents: x.UsageEvents.Count,
                TotalApiCalls: x.UsageEvents.Sum(u => u.ApiCalls),
                RiskLevel: CalculateRiskLevel(x.DaysSinceLastActivity, x.UsageEvents.Count, x.Subscriber.IsTrial),
                RecommendedAction: GetRecommendedAction(x.DaysSinceLastActivity, x.UsageEvents.Count, x.Subscriber.Plan),
                SendRetentionEmail: x.DaysSinceLastActivity > 15
            ))
            .OrderByDescending(r => r.RiskLevel)
            .ThenBy(r => r.DaysSinceLastActivity)
            .ToList();
    }
    
    private static string CalculateRiskLevel(int daysInactive, int usageCount, bool isTrial)
    {
        if (isTrial && daysInactive > 7) return "🔴 Critical - Trial Expiring";
        if (daysInactive > 60) return "🔴 Critical - Inactive > 60 days";
        if (daysInactive > 30) return "🟠 High - Inactive > 30 days";
        if (daysInactive > 14 && usageCount == 0) return "🟡 Medium - Low engagement";
        if (daysInactive > 7 && isTrial) return "🟡 Medium - Trial at risk";
        return "🟢 Low - Active customer";
    }
    
    private static string GetRecommendedAction(int daysInactive, int usageCount, string plan)
    {
        return (daysInactive, usageCount, plan) switch
        {
            (> 60, _, _) => "Escalate to account manager + 50% discount offer",
            (> 30, _, "Enterprise") => "Schedule executive business review",
            (> 30, _, _) => "Send re-engagement campaign with feature highlights",
            (> 14, 0, "Free") => "Send upgrade incentives",
            (> 7, _, "Trial") => "Send conversion reminder before trial ends",
            _ => "Monitor standard nurture campaign"
        };
    }
}
```

#### Key .NET 10 Features Used

✅ **GroupJoin with SelectMany** for left join simulation

✅ **DefaultIfEmpty** for including unmatched items

✅ **Tuple patterns** in switch expressions for complex logic

✅ **Record types** for immutable data transfer objects

✅ **Collection expressions** for list initialization

✅ **DateTime calculations** with proper null handling



### Query 5: Conditional Aggregation - Multi-Metric KPI Dashboard

#### Real-World Scenario
A sales analytics dashboard needs to compute **multiple KPIs in a single pass** over millions of transactions:
- Total sales, average order value, max/min order
- Sales by payment method (Credit/Debit/Cash/Gift)
- Weekend vs weekday performance
- Returns ratio and net revenue
- Hourly sales distribution

#### Business Impact
Reduces database round trips from 15+ to 1, cutting dashboard load time from 30 seconds to 2 seconds for 10M+ transactions.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacySalesAnalyticsEngine
{
    public SalesAnalytics ComputeAnalytics(List<Transaction> transactions, DateTime date)
    {
        var dayTransactions = new List<Transaction>();
        foreach (var t in transactions)
        {
            if (t.Timestamp.Date == date)
            {
                dayTransactions.Add(t);
            }
        }
        
        if (dayTransactions.Count == 0)
        {
            return new SalesAnalytics();
        }
        
        decimal grossSales = 0;
        decimal returnsAmount = 0;
        int transactionCount = 0;
        decimal maxAmount = decimal.MinValue;
        decimal minAmount = decimal.MaxValue;
        var paymentMethodTotals = new Dictionary<string, decimal>();
        var channelCounts = new Dictionary<string, int>();
        decimal weekendSales = 0;
        decimal weekdaySales = 0;
        int weekendCount = 0;
        int weekdayCount = 0;
        var hourlySales = new Dictionary<int, decimal>();
        var productQuantities = new Dictionary<string, int>();
        var transactionAmounts = new List<decimal>();
        
        foreach (var t in dayTransactions)
        {
            bool isWeekend = t.Timestamp.DayOfWeek == DayOfWeek.Saturday || t.Timestamp.DayOfWeek == DayOfWeek.Sunday;
            int hour = t.Timestamp.Hour;
            
            if (!t.IsReturn)
            {
                grossSales += t.Amount;
                transactionAmounts.Add(t.Amount);
                
                if (!paymentMethodTotals.ContainsKey(t.PaymentMethod))
                    paymentMethodTotals[t.PaymentMethod] = 0;
                paymentMethodTotals[t.PaymentMethod] += t.Amount;
                
                if (!channelCounts.ContainsKey(t.SalesChannel))
                    channelCounts[t.SalesChannel] = 0;
                channelCounts[t.SalesChannel]++;
                
                if (isWeekend)
                {
                    weekendSales += t.Amount;
                    weekendCount++;
                }
                else
                {
                    weekdaySales += t.Amount;
                    weekdayCount++;
                }
                
                if (!hourlySales.ContainsKey(hour))
                    hourlySales[hour] = 0;
                hourlySales[hour] += t.Amount;
                
                if (!productQuantities.ContainsKey(t.ProductSku))
                    productQuantities[t.ProductSku] = 0;
                productQuantities[t.ProductSku] += t.Quantity;
            }
            else
            {
                returnsAmount += t.Amount;
            }
            
            if (t.Amount > maxAmount) maxAmount = t.Amount;
            if (t.Amount < minAmount) minAmount = t.Amount;
            transactionCount++;
        }
        
        transactionAmounts.Sort();
        decimal medianTransaction = 0;
        if (transactionAmounts.Count > 0)
        {
            int mid = transactionAmounts.Count / 2;
            if (transactionAmounts.Count % 2 == 0)
                medianTransaction = (transactionAmounts[mid - 1] + transactionAmounts[mid]) / 2;
            else
                medianTransaction = transactionAmounts[mid];
        }
        
        var topProducts = productQuantities.OrderByDescending(kvp => kvp.Value).Take(5)
            .ToDictionary(kvp => kvp.Key, kvp => kvp.Value);
        
        string bestPerformingHour = hourlySales.OrderByDescending(h => h.Value).First().Key.ToString("00:00");
        string mostPopularPaymentMethod = paymentMethodTotals.OrderByDescending(p => p.Value).First().Key;
        
        return new SalesAnalytics
        {
            Date = date,
            GrossSales = grossSales,
            NetSales = grossSales - returnsAmount,
            ReturnsAmount = returnsAmount,
            ReturnsRate = grossSales > 0 ? returnsAmount / grossSales : 0,
            TotalTransactions = transactionCount,
            AverageOrderValue = transactionCount > 0 ? (double)(grossSales / transactionCount) : 0,
            MaxTransaction = maxAmount == decimal.MinValue ? 0 : maxAmount,
            MinTransaction = minAmount == decimal.MaxValue ? 0 : minAmount,
            MedianTransaction = medianTransaction,
            SalesByPaymentMethod = paymentMethodTotals,
            TransactionsByChannel = channelCounts,
            SalesByDayType = (weekendSales, weekdaySales, weekendCount, weekdayCount),
            HourlySales = hourlySales,
            TopProducts = topProducts,
            BestPerformingHour = bestPerformingHour,
            MostPopularPaymentMethod = mostPopularPaymentMethod
        };
    }
}

public class Transaction
{
    public string TransactionId { get; set; }
    public decimal Amount { get; set; }
    public DateTime Timestamp { get; set; }
    public string PaymentMethod { get; set; }
    public bool IsReturn { get; set; }
    public string ProductSku { get; set; }
    public int Quantity { get; set; }
    public string SalesChannel { get; set; }
    public string Region { get; set; }
}

public class SalesAnalytics
{
    public DateTime Date { get; set; }
    public decimal GrossSales { get; set; }
    public decimal NetSales { get; set; }
    public decimal ReturnsAmount { get; set; }
    public decimal ReturnsRate { get; set; }
    public int TotalTransactions { get; set; }
    public double AverageOrderValue { get; set; }
    public decimal MaxTransaction { get; set; }
    public decimal MinTransaction { get; set; }
    public decimal MedianTransaction { get; set; }
    public Dictionary<string, decimal> SalesByPaymentMethod { get; set; }
    public Dictionary<string, int> TransactionsByChannel { get; set; }
    public (decimal WeekendSales, decimal WeekdaySales, int WeekendCount, int WeekdayCount) SalesByDayType { get; set; }
    public Dictionary<int, decimal> HourlySales { get; set; }
    public Dictionary<string, int> TopProducts { get; set; }
    public string BestPerformingHour { get; set; }
    public string MostPopularPaymentMethod { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Transaction(
    string TransactionId,
    decimal Amount,
    DateTime Timestamp,
    string PaymentMethod,
    bool IsReturn,
    string ProductSku,
    int Quantity,
    string SalesChannel,
    string Region
);

public record SalesAnalytics(
    DateTime Date,
    decimal GrossSales,
    decimal NetSales,
    decimal ReturnsAmount,
    decimal ReturnsRate,
    int TotalTransactions,
    double AverageOrderValue,
    decimal MaxTransaction,
    decimal MinTransaction,
    decimal MedianTransaction,
    Dictionary<string, decimal> SalesByPaymentMethod,
    Dictionary<string, int> TransactionsByChannel,
    (decimal WeekendSales, decimal WeekdaySales, int WeekendCount, int WeekdayCount) SalesByDayType,
    Dictionary<int, decimal> HourlySales,
    Dictionary<string, int> TopProducts,
    string BestPerformingHour,
    string MostPopularPaymentMethod
);

public class SalesAnalyticsEngine
{
    public SalesAnalytics ComputeAnalytics(List<Transaction> transactions, DateTime date)
    {
        var dayTransactions = transactions.Where(t => t.Timestamp.Date == date).ToList();
        
        if (!dayTransactions.Any())
            return CreateEmptyAnalytics(date);
        
        // Single-pass aggregation using LINQ's Aggregate for complex state
        var result = dayTransactions.Aggregate(
            seed: new AnalyticsAccumulator(),
            func: (acc, t) => acc.AddTransaction(t)
        );
        
        return new SalesAnalytics(
            Date: date,
            GrossSales: result.GrossSales,
            NetSales: result.NetSales,
            ReturnsAmount: result.ReturnsAmount,
            ReturnsRate: result.GrossSales > 0 ? result.ReturnsAmount / result.GrossSales : 0,
            TotalTransactions: result.TransactionCount,
            AverageOrderValue: result.TransactionCount > 0 
                ? (double)(result.GrossSales / result.TransactionCount) : 0,
            MaxTransaction: result.MaxAmount,
            MinTransaction: result.MinAmount == decimal.MaxValue ? 0 : result.MinAmount,
            MedianTransaction: CalculateMedian(result.TransactionAmounts),
            SalesByPaymentMethod: result.PaymentMethodTotals,
            TransactionsByChannel: result.ChannelCounts,
            SalesByDayType: (result.WeekendSales, result.WeekdaySales, result.WeekendCount, result.WeekdayCount),
            HourlySales: result.HourlySales,
            TopProducts: result.ProductQuantities
                .OrderByDescending(kvp => kvp.Value)
                .Take(5)
                .ToDictionary(kvp => kvp.Key, kvp => kvp.Value),
            BestPerformingHour: result.HourlySales.MaxBy(h => h.Value).Key.ToString("00:00"),
            MostPopularPaymentMethod: result.PaymentMethodTotals.MaxBy(p => p.Value).Key
        );
    }
    
    private static decimal CalculateMedian(List<decimal> amounts)
    {
        if (!amounts.Any()) return 0;
        var sorted = amounts.OrderBy(a => a).ToList();
        var mid = sorted.Count / 2;
        return sorted.Count % 2 == 0 
            ? (sorted[mid - 1] + sorted[mid]) / 2 
            : sorted[mid];
    }
    
    private static SalesAnalytics CreateEmptyAnalytics(DateTime date) =>
        new(date, 0, 0, 0, 0, 0, 0, 0, 0, 0, new(), new(), (0, 0, 0, 0), new(), new(), "N/A", "N/A");
}

// Accumulator struct for performance (reduces heap allocations)
public struct AnalyticsAccumulator
{
    public decimal GrossSales { get; private set; }
    public decimal ReturnsAmount { get; private set; }
    public decimal NetSales => GrossSales - ReturnsAmount;
    public int TransactionCount { get; private set; }
    public decimal MaxAmount { get; private set; }
    public decimal MinAmount { get; private set; }
    public List<decimal> TransactionAmounts { get; private set; }
    public Dictionary<string, decimal> PaymentMethodTotals { get; private set; }
    public Dictionary<string, int> ChannelCounts { get; private set; }
    public decimal WeekendSales { get; private set; }
    public decimal WeekdaySales { get; private set; }
    public int WeekendCount { get; private set; }
    public int WeekdayCount { get; private set; }
    public Dictionary<int, decimal> HourlySales { get; private set; }
    public Dictionary<string, int> ProductQuantities { get; private set; }
    
    public AnalyticsAccumulator()
    {
        GrossSales = 0;
        ReturnsAmount = 0;
        TransactionCount = 0;
        MaxAmount = decimal.MinValue;
        MinAmount = decimal.MaxValue;
        TransactionAmounts = [];
        PaymentMethodTotals = [];
        ChannelCounts = [];
        WeekendSales = 0;
        WeekdaySales = 0;
        WeekendCount = 0;
        WeekdayCount = 0;
        HourlySales = [];
        ProductQuantities = [];
    }
    
    public AnalyticsAccumulator AddTransaction(Transaction t)
    {
        var isWeekend = t.Timestamp.DayOfWeek is DayOfWeek.Saturday or DayOfWeek.Sunday;
        var hour = t.Timestamp.Hour;
        
        if (!t.IsReturn)
        {
            GrossSales += t.Amount;
            TransactionAmounts.Add(t.Amount);
            
            // Payment method totals
            PaymentMethodTotals[t.PaymentMethod] = 
                PaymentMethodTotals.GetValueOrDefault(t.PaymentMethod) + t.Amount;
            
            // Channel counts
            ChannelCounts[t.SalesChannel] = 
                ChannelCounts.GetValueOrDefault(t.SalesChannel) + 1;
            
            // Day type totals
            if (isWeekend)
            {
                WeekendSales += t.Amount;
                WeekendCount++;
            }
            else
            {
                WeekdaySales += t.Amount;
                WeekdayCount++;
            }
            
            // Hourly distribution
            HourlySales[hour] = HourlySales.GetValueOrDefault(hour) + t.Amount;
            
            // Product quantities
            ProductQuantities[t.ProductSku] = 
                ProductQuantities.GetValueOrDefault(t.ProductSku) + t.Quantity;
        }
        else
        {
            ReturnsAmount += t.Amount;
        }
        
        MaxAmount = Math.Max(MaxAmount, t.Amount);
        MinAmount = Math.Min(MinAmount, t.Amount);
        TransactionCount++;
        
        return this;
    }
}
```

#### Key .NET 10 Features Used

✅ **Record types** for immutable analytics DTOs

✅ **Collection expressions** `[]` for zero-initialization

✅ **Struct accumulator** for reduced heap allocations

✅ **Default dictionary values** with `GetValueOrDefault`

✅ **MaxBy** LINQ method for efficient maximum finding

✅ **Tuple deconstruction** for multi-value returns

✅ **Primary constructors** (via record syntax)



### Query 6: Running Totals - Stock Portfolio Analysis

#### Real-World Scenario
A stock trading platform needs to calculate **running balances and position values**:
- Daily portfolio value over time
- Cumulative profit/loss per trade
- Maximum drawdown calculation
- 20-day moving average
- Sharpe ratio and volatility metrics

#### Business Impact
Enables real-time portfolio tracking for 100,000+ active traders, processing 1M+ trades daily with sub-second latency.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyPortfolioAnalyzer
{
    public List<PortfolioSnapshot> CalculateRunningTotals(List<Trade> trades, decimal initialCapital = 10000m)
    {
        var sortedTrades = trades.OrderBy(t => t.TradeDate).ToList();
        var snapshots = new List<PortfolioSnapshot>();
        
        decimal cumulativePnL = 0;
        decimal peakValue = initialCapital;
        var priceWindow = new Queue<decimal>();
        var dailyReturns = new List<decimal>();
        var positionBySymbol = new Dictionary<string, int>();
        
        foreach (var trade in sortedTrades)
        {
            // Update position
            int quantityChange = trade.TradeType == "BUY" ? trade.Quantity : -trade.Quantity;
            if (!positionBySymbol.ContainsKey(trade.Symbol))
                positionBySymbol[trade.Symbol] = 0;
            positionBySymbol[trade.Symbol] += quantityChange;
            
            decimal tradeValue = trade.Price * trade.Quantity + trade.Commission;
            decimal dailyPnL = trade.TradeType == "BUY" ? -tradeValue : tradeValue;
            cumulativePnL += dailyPnL;
            
            decimal portfolioValue = initialCapital + cumulativePnL;
            
            if (portfolioValue > peakValue) peakValue = portfolioValue;
            decimal drawdown = peakValue > 0 ? (peakValue - portfolioValue) / peakValue : 0;
            
            priceWindow.Enqueue(trade.Price);
            if (priceWindow.Count > 20) priceWindow.Dequeue();
            decimal runningAvg = priceWindow.Count > 0 ? priceWindow.Average() : 0;
            
            if (dailyPnL != 0)
            {
                decimal dailyReturn = dailyPnL / portfolioValue;
                dailyReturns.Add(dailyReturn);
            }
            
            decimal volatility = 0;
            if (dailyReturns.Count >= 2)
            {
                decimal mean = dailyReturns.Average();
                double variance = 0;
                foreach (var ret in dailyReturns)
                {
                    variance += Math.Pow((double)(ret - mean), 2);
                }
                variance /= (dailyReturns.Count - 1);
                volatility = (decimal)Math.Sqrt(variance);
            }
            
            snapshots.Add(new PortfolioSnapshot
            {
                Date = trade.TradeDate,
                Symbol = trade.Symbol,
                Price = trade.Price,
                Position = positionBySymbol.GetValueOrDefault(trade.Symbol, 0),
                DailyPnL = dailyPnL,
                CumulativePnL = cumulativePnL,
                PortfolioValue = portfolioValue,
                RunningAverage20Day = runningAvg,
                MaxDrawdown = drawdown,
                Volatility30Day = volatility,
                TradeCount = snapshots.Count + 1
            });
        }
        
        return snapshots;
    }
}

public class Trade
{
    public string Symbol { get; set; }
    public DateTime TradeDate { get; set; }
    public decimal Price { get; set; }
    public int Quantity { get; set; }
    public string TradeType { get; set; } // "BUY" or "SELL"
    public decimal Commission { get; set; }
}

public class PortfolioSnapshot
{
    public DateTime Date { get; set; }
    public string Symbol { get; set; }
    public decimal Price { get; set; }
    public int Position { get; set; }
    public decimal DailyPnL { get; set; }
    public decimal CumulativePnL { get; set; }
    public decimal PortfolioValue { get; set; }
    public decimal RunningAverage20Day { get; set; }
    public decimal MaxDrawdown { get; set; }
    public decimal Volatility30Day { get; set; }
    public int TradeCount { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record Trade(
    string Symbol,
    DateTime TradeDate,
    decimal Price,
    int Quantity,
    string TradeType, // "BUY" or "SELL"
    decimal Commission
);

public record PortfolioSnapshot(
    DateTime Date,
    string Symbol,
    decimal Price,
    int Position,
    decimal DailyPnL,
    decimal CumulativePnL,
    decimal PortfolioValue,
    decimal RunningAverage20Day,
    decimal MaxDrawdown,
    decimal Volatility30Day,
    int TradeCount
);

public class PortfolioAnalyzer
{
    public List<PortfolioSnapshot> CalculateRunningTotals(List<Trade> trades, decimal initialCapital = 10000m)
    {
        var sortedTrades = trades.OrderBy(t => t.TradeDate).ToList();
        var snapshots = new List<PortfolioSnapshot>();
        
        decimal cumulativePnL = 0;
        decimal peakValue = initialCapital;
        var priceWindow = new Queue<decimal>();
        var dailyReturns = new List<decimal>();
        var positionBySymbol = new Dictionary<string, int>();
        
        foreach (var trade in sortedTrades)
        {
            // Update position
            var quantityChange = trade.TradeType == "BUY" ? trade.Quantity : -trade.Quantity;
            positionBySymbol[trade.Symbol] = positionBySymbol.GetValueOrDefault(trade.Symbol) + quantityChange;
            
            var tradeValue = trade.Price * trade.Quantity + trade.Commission;
            var dailyPnL = trade.TradeType == "BUY" ? -tradeValue : tradeValue;
            cumulativePnL += dailyPnL;
            
            var portfolioValue = initialCapital + cumulativePnL;
            
            // Track peak for drawdown calculation
            if (portfolioValue > peakValue) peakValue = portfolioValue;
            var drawdown = peakValue > 0 ? (peakValue - portfolioValue) / peakValue : 0;
            
            // Maintain 20-day window for moving average
            priceWindow.Enqueue(trade.Price);
            if (priceWindow.Count > 20) priceWindow.Dequeue();
            var runningAvg = priceWindow.Average();
            
            // Calculate volatility from daily returns
            if (dailyPnL != 0)
            {
                var dailyReturn = dailyPnL / portfolioValue;
                dailyReturns.Add(dailyReturn);
            }
            
            var volatility = CalculateVolatility(dailyReturns);
            
            snapshots.Add(new PortfolioSnapshot(
                Date: trade.TradeDate,
                Symbol: trade.Symbol,
                Price: trade.Price,
                Position: positionBySymbol.GetValueOrDefault(trade.Symbol, 0),
                DailyPnL: dailyPnL,
                CumulativePnL: cumulativePnL,
                PortfolioValue: portfolioValue,
                RunningAverage20Day: runningAvg,
                MaxDrawdown: drawdown,
                Volatility30Day: volatility,
                TradeCount: snapshots.Count + 1
            ));
        }
        
        return snapshots;
    }
    
    private static decimal CalculateVolatility(List<decimal> returns)
    {
        if (returns.Count < 2) return 0;
        
        var mean = returns.Average();
        var variance = returns.Sum(r => Math.Pow((double)(r - mean), 2)) / (returns.Count - 1);
        return (decimal)Math.Sqrt(variance);
    }
    
    // Custom running aggregate extension
    public IEnumerable<PortfolioSnapshot> CalculateWithRunningAggregate(List<Trade> trades, decimal initialCapital = 10000m)
    {
        return trades
            .OrderBy(t => t.TradeDate)
            .RunningAggregate(
                seed: new TradeAccumulator(initialCapital),
                func: (acc, trade) => acc.AddTrade(trade),
                resultSelector: (acc, trade, index) => acc.ToSnapshot(trade, index)
            );
    }
}

// .NET 10 running aggregate extension
public static class LinqRunningExtensions
{
    public static IEnumerable<TResult> RunningAggregate<TSource, TAccumulate, TResult>(
        this IEnumerable<TSource> source,
        TAccumulate seed,
        Func<TAccumulate, TSource, TAccumulate> func,
        Func<TAccumulate, TSource, int, TResult> resultSelector)
    {
        var accumulator = seed;
        var index = 0;
        foreach (var item in source)
        {
            accumulator = func(accumulator, item);
            yield return resultSelector(accumulator, item, index);
            index++;
        }
    }
}

public class TradeAccumulator
{
    private readonly decimal _initialCapital;
    private readonly Dictionary<string, int> _positions;
    private readonly Queue<decimal> _priceWindow;
    private readonly List<decimal> _dailyReturns;
    
    public decimal CumulativePnL { get; private set; }
    public decimal PeakValue { get; private set; }
    public int TradeCount { get; private set; }
    
    public TradeAccumulator(decimal initialCapital)
    {
        _initialCapital = initialCapital;
        _positions = [];
        _priceWindow = [];
        _dailyReturns = [];
        CumulativePnL = 0;
        PeakValue = initialCapital;
        TradeCount = 0;
    }
    
    public TradeAccumulator AddTrade(Trade trade)
    {
        var quantityChange = trade.TradeType == "BUY" ? trade.Quantity : -trade.Quantity;
        _positions[trade.Symbol] = _positions.GetValueOrDefault(trade.Symbol) + quantityChange;
        
        var tradeValue = trade.Price * trade.Quantity + trade.Commission;
        var dailyPnL = trade.TradeType == "BUY" ? -tradeValue : tradeValue;
        CumulativePnL += dailyPnL;
        
        var portfolioValue = _initialCapital + CumulativePnL;
        if (portfolioValue > PeakValue) PeakValue = portfolioValue;
        
        _priceWindow.Enqueue(trade.Price);
        if (_priceWindow.Count > 20) _priceWindow.Dequeue();
        
        if (dailyPnL != 0)
        {
            _dailyReturns.Add(dailyPnL / portfolioValue);
        }
        
        TradeCount++;
        return this;
    }
    
    public PortfolioSnapshot ToSnapshot(Trade trade, int index)
    {
        var portfolioValue = _initialCapital + CumulativePnL;
        var drawdown = PeakValue > 0 ? (PeakValue - portfolioValue) / PeakValue : 0;
        var runningAvg = _priceWindow.Any() ? _priceWindow.Average() : 0;
        var volatility = CalculateVolatility(_dailyReturns);
        
        return new PortfolioSnapshot(
            Date: trade.TradeDate,
            Symbol: trade.Symbol,
            Price: trade.Price,
            Position: _positions.GetValueOrDefault(trade.Symbol, 0),
            DailyPnL: trade.TradeType == "BUY" ? -(trade.Price * trade.Quantity + trade.Commission) : trade.Price * trade.Quantity - trade.Commission,
            CumulativePnL: CumulativePnL,
            PortfolioValue: portfolioValue,
            RunningAverage20Day: runningAvg,
            MaxDrawdown: drawdown,
            Volatility30Day: volatility,
            TradeCount: index + 1
        );
    }
    
    private static decimal CalculateVolatility(List<decimal> returns)
    {
        if (returns.Count < 2) return 0;
        var mean = returns.Average();
        var variance = returns.Sum(r => Math.Pow((double)(r - mean), 2)) / (returns.Count - 1);
        return (decimal)Math.Sqrt(variance);
    }
}
```

#### Key .NET 10 Features Used

✅ **Record types** for immutable trade and snapshot models

✅ **Collection expressions** `[]` for dictionary initialization

✅ **Custom LINQ extension** with RunningAggregate pattern

✅ **GetValueOrDefault** for safe dictionary access

✅ **Queue<T>** with LINQ Average method

✅ **Math.Pow** with decimal-to-double conversion

✅ **Primary constructors** via record syntax



### Query 7: Set Operations - Customer Segmentation for Marketing

#### Real-World Scenario
A marketing team needs to identify **customer segments** for targeted campaigns:
- **Power Users**: Customers who bought from both Web and Mobile channels
- **At-Risk**: Previously active customers with no purchases in last 90 days
- **Cross-sell Candidates**: Bought Product A but not Product B
- **Newly Acquired**: First-time buyers in last 30 days
- **Loyal Customers**: Purchased in 3+ consecutive months

#### Business Impact
Increases marketing ROI by 40% through targeted campaigns, reaching 500,000+ customers with personalized offers.

#### Legacy Approach (.NET Framework 2.0)

```csharp
public class LegacyCustomerSegmentationEngine
{
    public List<CustomerSegment> IdentifySegments(List<CustomerPurchase> purchases, DateTime analysisDate)
    {
        var webCustomers = new HashSet<int>();
        var mobileCustomers = new HashSet<int>();
        var storeCustomers = new HashSet<int>();
        var electronicsCustomers = new HashSet<int>();
        var accessoriesCustomers = new HashSet<int>();
        var allCustomers = new HashSet<int>();
        
        foreach (var p in purchases)
        {
            allCustomers.Add(p.CustomerId);
            if (p.Channel == "Web") webCustomers.Add(p.CustomerId);
            if (p.Channel == "Mobile") mobileCustomers.Add(p.CustomerId);
            if (p.Channel == "Store") storeCustomers.Add(p.CustomerId);
            if (p.ProductCategory == "Electronics") electronicsCustomers.Add(p.CustomerId);
            if (p.ProductCategory == "Accessories") accessoriesCustomers.Add(p.CustomerId);
        }
        
        var thirtyDaysAgo = analysisDate.AddDays(-30);
        var ninetyDaysAgo = analysisDate.AddDays(-90);
        
        var activeCustomers = new HashSet<int>();
        var newCustomers = new HashSet<int>();
        var customerFirstPurchase = new Dictionary<int, DateTime>();
        
        foreach (var p in purchases)
        {
            if (p.PurchaseDate >= ninetyDaysAgo)
                activeCustomers.Add(p.CustomerId);
            
            if (!customerFirstPurchase.ContainsKey(p.CustomerId) || p.PurchaseDate < customerFirstPurchase[p.CustomerId])
                customerFirstPurchase[p.CustomerId] = p.PurchaseDate;
        }
        
        foreach (var kvp in customerFirstPurchase)
        {
            if (kvp.Value >= thirtyDaysAgo)
                newCustomers.Add(kvp.Key);
        }
        
        // Power Users: Web AND Mobile AND Store
        var powerUsers = new HashSet<int>(webCustomers);
        powerUsers.IntersectWith(mobileCustomers);
        powerUsers.IntersectWith(storeCustomers);
        
        // Cross-sell: Electronics NOT Accessories
        var crossSell = new HashSet<int>(electronicsCustomers);
        crossSell.ExceptWith(accessoriesCustomers);
        
        // At-risk: Active NOT New
        var atRisk = new HashSet<int>(activeCustomers);
        atRisk.ExceptWith(newCustomers);
        
        var segments = new List<CustomerSegment>();
        
        // Build Power Users segment
        var powerUserNames = new List<string>();
        foreach (var customerId in powerUsers.Take(5))
        {
            foreach (var p in purchases)
            {
                if (p.CustomerId == customerId)
                {
                    powerUserNames.Add($"{p.CustomerName} ({p.Email})");
                    break;
                }
            }
        }
        
        decimal powerUserValue = 0;
        foreach (var p in purchases)
        {
            if (powerUsers.Contains(p.CustomerId))
                powerUserValue += p.Amount;
        }
        
        segments.Add(new CustomerSegment
        {
            SegmentName = "🏆 Power Users",
            SegmentColor = "#FFD700",
            Description = "Customers who purchase across Web, Mobile, and Store channels",
            SampleCustomers = powerUserNames,
            Count = powerUsers.Count,
            TotalPotentialValue = powerUserValue,
            RecommendedCampaign = "VIP Early Access Program",
            CampaignChannel = "All Channels",
            EstimatedROI = 0.35m
        });
        
        // Similar blocks for other segments...
        
        return segments;
    }
}

public class CustomerPurchase
{
    public int CustomerId { get; set; }
    public string CustomerName { get; set; }
    public string Email { get; set; }
    public string Channel { get; set; }
    public string ProductCategory { get; set; }
    public string ProductSku { get; set; }
    public DateTime PurchaseDate { get; set; }
    public decimal Amount { get; set; }
    public int Quantity { get; set; }
}

public class CustomerSegment
{
    public string SegmentName { get; set; }
    public string SegmentColor { get; set; }
    public string Description { get; set; }
    public List<string> SampleCustomers { get; set; }
    public int Count { get; set; }
    public decimal TotalPotentialValue { get; set; }
    public string RecommendedCampaign { get; set; }
    public string CampaignChannel { get; set; }
    public decimal EstimatedROI { get; set; }
}
```

#### .NET 10 Implementation

```csharp
public record CustomerPurchase(
    int CustomerId,
    string CustomerName,
    string Email,
    string Channel,
    string ProductCategory,
    string ProductSku,
    DateTime PurchaseDate,
    decimal Amount,
    int Quantity
);

public record CustomerSegment(
    string SegmentName,
    string SegmentColor,
    string Description,
    List<string> SampleCustomers,
    int Count,
    decimal TotalPotentialValue,
    string RecommendedCampaign,
    string CampaignChannel,
    decimal EstimatedROI
);

public record CustomerPreference(
    int CustomerId,
    string Name,
    string PreferredChannel,
    decimal TotalSpend
);

public class CustomerSegmentationEngine
{
    public List<CustomerSegment> IdentifySegments(List<CustomerPurchase> purchases, DateTime analysisDate)
    {
        var webCustomers = purchases.Where(p => p.Channel == "Web").Select(p => p.CustomerId).ToHashSet();
        var mobileCustomers = purchases.Where(p => p.Channel == "Mobile").Select(p => p.CustomerId).ToHashSet();
        var storeCustomers = purchases.Where(p => p.Channel == "Store").Select(p => p.CustomerId).ToHashSet();
        
        var electronicsCustomers = purchases.Where(p => p.ProductCategory == "Electronics").Select(p => p.CustomerId).ToHashSet();
        var accessoriesCustomers = purchases.Where(p => p.ProductCategory == "Accessories").Select(p => p.CustomerId).ToHashSet();
        
        var thirtyDaysAgo = analysisDate.AddDays(-30);
        var ninetyDaysAgo = analysisDate.AddDays(-90);
        
        var activeCustomers = purchases
            .Where(p => p.PurchaseDate >= ninetyDaysAgo)
            .Select(p => p.CustomerId)
            .ToHashSet();
        
        var newCustomers = purchases
            .Where(p => p.PurchaseDate >= thirtyDaysAgo)
            .GroupBy(p => p.CustomerId)
            .Where(g => g.Count() == 1)
            .Select(g => g.Key)
            .ToHashSet();
        
        // Customers with 3+ consecutive months of purchases
        var loyalCustomers = purchases
            .GroupBy(p => p.CustomerId)
            .Where(g => HasConsecutiveMonths(g.ToList(), 3))
            .Select(g => g.Key)
            .ToHashSet();
        
        // High-value customers (top 10% by spend)
        var customerSpends = purchases
            .GroupBy(p => p.CustomerId)
            .Select(g => new { CustomerId = g.Key, TotalSpend = g.Sum(p => p.Amount) })
            .OrderByDescending(x => x.TotalSpend)
            .ToList();
        
        var top10PercentCount = Math.Max(1, (int)(customerSpends.Count * 0.1));
        var highValueCustomers = customerSpends
            .Take(top10PercentCount)
            .Select(x => x.CustomerId)
            .ToHashSet();
        
        return
        [
            new CustomerSegment(
                SegmentName: "🏆 Power Users",
                SegmentColor: "#FFD700",
                Description: "Customers who purchase across Web, Mobile, and Store channels",
                SampleCustomers: GetCustomerNames(webCustomers.Intersect(mobileCustomers).Intersect(storeCustomers), purchases, 5),
                Count: webCustomers.Intersect(mobileCustomers).Intersect(storeCustomers).Count,
                TotalPotentialValue: CalculateSegmentValue(purchases, webCustomers.Intersect(mobileCustomers).Intersect(storeCustomers)),
                RecommendedCampaign: "VIP Early Access Program",
                CampaignChannel: "All Channels",
                EstimatedROI: 0.35m
            ),
            
            new CustomerSegment(
                SegmentName: "⚠️ At-Risk Customers",
                SegmentColor: "#FF6B6B",
                Description: $"Active customers with no purchases in last 90 days",
                SampleCustomers: GetCustomerNames(activeCustomers.Except(newCustomers), purchases, 5),
                Count: activeCustomers.Except(newCustomers).Count,
                TotalPotentialValue: CalculateSegmentValue(purchases, activeCustomers.Except(newCustomers)),
                RecommendedCampaign: "We Miss You - 25% Discount",
                CampaignChannel: "Email + Push",
                EstimatedROI: 0.20m
            ),
            
            new CustomerSegment(
                SegmentName: "🔄 Cross-sell Candidates",
                SegmentColor: "#4ECDC4",
                Description: "Bought Electronics but never bought Accessories",
                SampleCustomers: GetCustomerNames(electronicsCustomers.Except(accessoriesCustomers), purchases, 5),
                Count: electronicsCustomers.Except(accessoriesCustomers).Count,
                TotalPotentialValue: CalculateSegmentValue(purchases, electronicsCustomers.Except(accessoriesCustomers)) * 0.3m,
                RecommendedCampaign: "Complete Your Setup - Accessories Bundle",
                CampaignChannel: "Email + On-site Widget",
                EstimatedROI: 0.28m
            ),
            
            new CustomerSegment(
                SegmentName: "🌟 Newly Acquired",
                SegmentColor: "#95E77D",
                Description: "First-time buyers in last 30 days",
                SampleCustomers: GetCustomerNames(newCustomers, purchases, 5),
                Count: newCustomers.Count,
                TotalPotentialValue: CalculateSegmentValue(purchases, newCustomers) * 0.8m,
                RecommendedCampaign: "Welcome Series + Next Purchase Discount",
                CampaignChannel: "Email Onboarding",
                EstimatedROI: 0.40m
            ),
            
            new CustomerSegment(
                SegmentName: "💎 Loyal Customers",
                SegmentColor: "#9B59B6",
                Description: "Purchased in 3+ consecutive months",
                SampleCustomers: GetCustomerNames(loyalCustomers, purchases, 5),
                Count: loyalCustomers.Count,
                TotalPotentialValue: CalculateSegmentValue(purchases, loyalCustomers),
                RecommendedCampaign: "Loyalty Rewards Program Invitation",
                CampaignChannel: "Personalized Email",
                EstimatedROI: 0.45m
            ),
            
            new CustomerSegment(
                SegmentName: "💰 High Value",
                SegmentColor: "#E67E22",
                Description: "Top 10% of customers by total spend",
                SampleCustomers: GetCustomerNames(highValueCustomers, purchases, 5),
                Count: highValueCustomers.Count,
                TotalPotentialValue: CalculateSegmentValue(purchases, highValueCustomers),
                RecommendedCampaign: "Premium Concierge Service",
                CampaignChannel: "Personal Call + Email",
                EstimatedROI: 0.30m
            )
        ];
    }
    
    private static bool HasConsecutiveMonths(List<CustomerPurchase> customerPurchases, int monthsRequired)
    {
        var months = customerPurchases
            .Select(p => new DateTime(p.PurchaseDate.Year, p.PurchaseDate.Month, 1))
            .Distinct()
            .OrderBy(d => d)
            .ToList();
        
        if (months.Count < monthsRequired) return false;
        
        var consecutiveCount = 1;
        for (int i = 1; i < months.Count; i++)
        {
            if (months[i].AddMonths(-1) == months[i - 1])
            {
                consecutiveCount++;
                if (consecutiveCount >= monthsRequired) return true;
            }
            else
            {
                consecutiveCount = 1;
            }
        }
        return false;
    }
    
    private static List<string> GetCustomerNames(HashSet<int> customerIds, List<CustomerPurchase> purchases, int take)
    {
        return purchases
            .Where(p => customerIds.Contains(p.CustomerId))
            .Select(p => $"{p.CustomerName} ({p.Email})")
            .Distinct()
            .Take(take)
            .ToList();
    }
    
    private static decimal CalculateSegmentValue(List<CustomerPurchase> purchases, HashSet<int> customerIds)
    {
        return purchases
            .Where(p => customerIds.Contains(p.CustomerId))
            .Sum(p => p.Amount);
    }
    
    // Symmetric difference for unique channel preference
    public List<CustomerPreference> GetSingleChannelPreferences(List<CustomerPurchase> purchases)
    {
        var webOnly = purchases.Where(p => p.Channel == "Web").Select(p => p.CustomerId).ToHashSet();
        var mobileOnly = purchases.Where(p => p.Channel == "Mobile").Select(p => p.CustomerId).ToHashSet();
        var storeOnly = purchases.Where(p => p.Channel == "Store").Select(p => p.CustomerId).ToHashSet();
        
        var allChannelCustomers = webOnly.Union(mobileOnly).Union(storeOnly);
        var multiChannelCustomers = webOnly.Intersect(mobileOnly)
            .Union(webOnly.Intersect(storeOnly))
            .Union(mobileOnly.Intersect(storeOnly));
        
        var singleChannelCustomers = allChannelCustomers.Except(multiChannelCustomers).ToList();
        
        return singleChannelCustomers.Select(customerId =>
        {
            var channel = webOnly.Contains(customerId) ? "Web" :
                         mobileOnly.Contains(customerId) ? "Mobile" : "Store";
            var totalSpend = purchases.Where(p => p.CustomerId == customerId).Sum(p => p.Amount);
            var customerName = purchases.First(p => p.CustomerId == customerId).CustomerName;
            
            return new CustomerPreference(customerId, customerName, channel, totalSpend);
        }).ToList();
    }
}
```

#### Key .NET 10 Features Used

✅ **HashSet<T>** with LINQ set operations (Intersect, Except, Union)

✅ **Collection expressions** `[..]` for list creation

✅ **Record types** for immutable segment definitions

✅ **Tuple returns** for multiple values

✅ **Take with LINQ** for limiting sample sizes

✅ **GroupBy with multiple aggregates** for customer spend analysis

✅ **Distinct with custom logic** for unique customer names



## 📊 Query Performance Comparison (Part 1)

| Query | Legacy LoC | .NET 10 LoC | Reduction | Key Performance Gain |
|-------|------------|-------------|-----------|---------------------|
| Query 1: Multi-Key Grouping | 45 | 12 | 73% | Single-pass aggregation |
| Query 2: GroupJoin Hierarchy | 38 | 15 | 61% | Built-in hierarchical mapping |
| Query 3: Full Outer Join | 52 | 18 | 65% | Union + Distinct optimization |
| Query 4: Left Join | 35 | 14 | 60% | GroupJoin with DefaultIfEmpty |
| Query 5: Conditional Aggregation | 60 | 20 | 67% | Struct accumulator reduces GC |
| Query 6: Running Totals | 48 | 22 | 54% | Custom RunningAggregate extension |
| Query 7: Set Operations | 35 | 10 | 71% | HashSet intersection/except |



## 🔜 Coming in Part 2: Filtering, Projection & Transformation (Queries 13-25)

**What to expect in Part 2:**

| Query | Pattern | Difficulty | Real-World Use Case |
|-------|---------|------------|---------------------|
| 13 | Dynamic Filtering with PredicateBuilder | ⭐⭐⭐ | Multi-field search with user input |
| 14 | SelectMany for Nested Collections | ⭐⭐ | Flattening order → items → details |
| 15 | Zip for Parallel Processing | ⭐⭐ | Merging data from 3+ sources |
| 16 | Custom Projections with Expression Trees | ⭐⭐⭐⭐ | Runtime field selection |
| 17 | Conditional Mapping with Let clause | ⭐⭐ | Complex calculated fields |
| 18 | OfType for Mixed Type Collections | ⭐ | Processing heterogeneous data |
| 19 | Cast for Safe Type Conversion | ⭐ | Converting non-generic collections |
| 20 | Select with Index | ⭐ | Pagination with row numbers |
| 21 | Where filtering with multiple conditions | ⭐⭐ | Complex business rule filtering |
| 22 | Take/Skip for pagination | ⭐ | API endpoint pagination |
| 23 | SelectMany for cross joins | ⭐⭐ | Variant/Cartesian product generation |
| 24 | Let clause for intermediate values | ⭐⭐ | Reusable query sub-expressions |
| 25 | Conditional Where with switch | ⭐⭐⭐ | User-configurable filters |

📎 **Read the full story: Part 2 — coming soon**



## 🎯 Key Takeaways from Part 1

1. **LINQ eliminates 60-70% of boilerplate code** compared to imperative approaches
2. **GroupJoin is your go-to** for hierarchical data relationships (department → employees)
3. **Full Outer Joins** can be simulated with Union + Distinct for complete reconciliation
4. **Single-pass aggregations** using Aggregate or custom accumulators dramatically reduce database round trips
5. **Set operations** (Intersect, Except, Union) are perfect for customer segmentation
6. **Running totals** are achievable with custom RunningAggregate extension patterns
7. **.NET 10 features** like collection expressions `[..]`, primary constructors, and record types make LINQ even cleaner and more performant
8. **Struct accumulators** reduce heap allocations for high-frequency aggregation scenarios



## 📚 Complete Story List (50 Advanced LINQ Queries for .NET 10)

📚 **Grouping, Joining & Aggregation - 50 Advanced LINQ Queries for .NET 10 (Queries 1-12)** — Deep dive on multi-key grouping, all join types (Group, Left, Right, Full), conditional aggregation, running totals, set operations, and pagination. Patterns covered: Multi-Key Grouping, GroupJoin, Full Outer Join, Left Join, Conditional Aggregation, Running Totals, Set Operations, Pagination, Distinct, Lookup, Zip, Aggregate.

📎 **You are here: Part 1 — above**



📚 **Filtering, Projection & Transformation - 50 Advanced LINQ Queries for .NET 10 (Queries 13-25)** — Deep dive on dynamic filtering, SelectMany flattening, Zip operations, custom projections, conditional mapping, mixed type handling, and index-based selection. Patterns covered: Dynamic Filtering, SelectMany, Zip, Custom Projections, Let Clause, OfType, Cast, Select with Index, Where filtering, Take/Skip, SelectMany cross joins.

📎 **Read the full story: Part 2 — coming soon**



📚 **Advanced Data Shaping & Grouping - 50 Advanced LINQ Queries for .NET 10 (Queries 26-38)** — Deep dive on pivot tables, recursive queries, time-series analysis, window functions, composite keys, hierarchical data, and incremental aggregation. Patterns covered: Pivot Tables, Recursive Queries, Time-Based Grouping, Window Functions, Composite Keys, Hierarchical Flattening, Incremental Aggregation, Lookup, ToDictionary, GroupBy with Custom Comparer.

📎 **Read the full story: Part 3 — coming soon**



📚 **Performance & Optimization - 50 Advanced LINQ Queries for .NET 10 (Queries 39-50)** — Deep dive on batch processing, lazy evaluation, error handling, parallel LINQ (PLINQ), IQueryable optimization, async streams, and memory-efficient techniques. Patterns covered: Batch Processing, Chunking, Lazy Evaluation, Error Handling, Safe Navigation, PLINQ, IQueryable vs IEnumerable, Async LINQ, Streaming, Caching, Expression Trees.

📎 **Read the full story: Part 4 — coming soon**

> Coming soon! Want it sooner? Let me know with a clap or comment below


*� Questions? Drop a response - I read and reply to every comment.*  
*📌 Save this story to your reading list - it helps other engineers discover it.*  
**🔗 Follow me →**

- **[Medium](mvineetsharma.medium.com)** - mvineetsharma.medium.com
- **[LinkedIn](www.linkedin.com/in/vineet-sharma-architect)** -  [www.linkedin.com/in/vineet-sharma-architect](http://www.linkedin.com/in/vineet-sharma-architect)

*In-depth .NET, Node.js, Python, Cloud Architecture, and System Design. New articles weekly*
