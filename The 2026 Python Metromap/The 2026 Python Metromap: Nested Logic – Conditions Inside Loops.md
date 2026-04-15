# The 2026 Python Metromap: Nested Logic – Conditions Inside Loops

## Series A: Foundations Station | Story 6 of 7

![The 2026 Python Metromap/images/Nested Logic – Conditions Inside Loops](images/Nested Logic – Conditions Inside Loops.png)

## 📖 Introduction

**Welcome to the sixth stop on the Foundations Station Line.**

You've mastered variables, collections, operators, control flow, and loops. You can store data, transform it, make decisions, and repeat operations. But real-world problems aren't simple—they combine these concepts in powerful ways.

What happens when you need to check conditions inside loops? When you need to loop inside loops? When you need to validate complex nested data structures? That's where nested logic comes in.

Nested logic is the combination of control flow statements inside loops, and loops inside loops. It's how you validate every cell in a Sudoku grid, calculate grades for every student in every class, or filter products across multiple categories. It's where simple concepts combine to solve complex problems.

This story—**The 2026 Python Metromap: Nested Logic – Conditions Inside Loops**—is your guide to combining conditions and loops. We'll build a complete Sudoku validator that checks rows, columns, and subgrids. We'll create a student grade matrix analyzer that processes multiple classes and students. We'll build a multi-condition search filter for product inventory. And we'll implement a complete order validation system with nested business rules.

**Let's nest some logic.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories)

- 🔧 **The 2026 Python Metromap: Variables & Data Types – The Rails of Python** – Integers, floats, strings, booleans; storing customer orders; type conversion; input/output operations.

- 🏗️ **The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets** – Shopping carts with lists; user profiles with dictionaries; analytics with sets; configuration with tuples.

- 📦 **The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More** – Building a discount engine; age verification; loan approval calculator.

- 🚦 **The 2026 Python Metromap: Control Flow – if, elif, else** – Grade calculator; shipping cost estimator; customer support ticket routing.

- 🔁 **The 2026 Python Metromap: Loops – for, while, break, continue** – Batch file processor; API retry mechanism; pagination system.

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter. **⬅️ YOU ARE HERE**

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🧩 Section 1: Conditions Inside Loops – Filtering and Validation

Placing conditions inside loops allows you to filter, validate, or transform each item based on criteria.

**SOLID Principle Applied: Single Responsibility** – Each condition inside a loop has one validation purpose.

**Design Pattern: Filter Pattern** – Conditions act as filters that determine which items pass through.

```python
"""
CONDITIONS INSIDE LOOPS: FILTERING AND VALIDATION

This section covers placing if statements inside loops to filter
and validate data during iteration.

SOLID Principle: Single Responsibility
- Each condition has one validation purpose

Design Pattern: Filter Pattern
- Conditions filter items passing through the loop
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import re


def demonstrate_basic_nested_conditions():
    """
    Demonstrates basic if statements inside for loops.
    
    Conditions inside loops are the foundation of data filtering.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC CONDITIONS INSIDE LOOPS")
    print("=" * 60)
    
    # FILTERING NUMBERS
    print("\n1. FILTERING NUMBERS")
    print("-" * 40)
    
    numbers = [12, 7, 23, 8, 15, 30, 5, 18, 42, 9]
    
    print(f"Original list: {numbers}")
    
    # Filter even numbers
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    print(f"Even numbers: {evens}")
    
    # Filter numbers between 10 and 25
    in_range = []
    for num in numbers:
        if 10 <= num <= 25:
            in_range.append(num)
    print(f"Numbers between 10-25: {in_range}")
    
    # FILTERING STRINGS
    print("\n2. FILTERING STRINGS")
    print("-" * 40)
    
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    
    print(f"Original words: {words}")
    
    # Filter words longer than 5 characters
    long_words = []
    for word in words:
        if len(word) > 5:
            long_words.append(word)
    print(f"Words longer than 5 chars: {long_words}")
    
    # Filter words starting with vowel
    vowels = "aeiou"
    vowel_words = []
    for word in words:
        if word[0].lower() in vowels:
            vowel_words.append(word)
    print(f"Words starting with vowel: {vowel_words}")
    
    # FILTERING DICTIONARIES
    print("\n3. FILTERING DICTIONARIES")
    print("-" * 40)
    
    products = [
        {"name": "Laptop", "price": 999, "category": "electronics", "in_stock": True},
        {"name": "Mouse", "price": 25, "category": "electronics", "in_stock": True},
        {"name": "Notebook", "price": 5, "category": "stationery", "in_stock": False},
        {"name": "Monitor", "price": 299, "category": "electronics", "in_stock": True},
        {"name": "Pen", "price": 2, "category": "stationery", "in_stock": True},
        {"name": "Keyboard", "price": 75, "category": "electronics", "in_stock": False}
    ]
    
    print("Products:")
    for p in products[:3]:
        print(f"  {p}")
    print("  ...")
    
    # Filter electronics in stock
    available_electronics = []
    for product in products:
        if product["category"] == "electronics" and product["in_stock"]:
            available_electronics.append(product["name"])
    print(f"Available electronics: {available_electronics}")
    
    # Filter products under $50
    affordable = []
    for product in products:
        if product["price"] < 50:
            affordable.append(f"{product['name']} (${product['price']})")
    print(f"Products under $50: {affordable}")
    
    # MULTIPLE CONDITIONS
    print("\n4. MULTIPLE CONDITIONS IN ONE LOOP")
    print("-" * 40)
    
    scores = [85, 92, 78, 65, 95, 88, 72, 91, 83, 79]
    
    # Categorize each score
    categories = []
    for score in scores:
        if score >= 90:
            categories.append("A")
        elif score >= 80:
            categories.append("B")
        elif score >= 70:
            categories.append("C")
        elif score >= 60:
            categories.append("D")
        else:
            categories.append("F")
    
    print("Score categories:")
    for score, category in zip(scores[:5], categories[:5]):
        print(f"  {score} → {category}")
    print("  ...")
    
    # ACCUMULATING WITH CONDITIONS
    print("\n5. ACCUMULATING WITH CONDITIONS")
    print("-" * 40)
    
    # Calculate sum of even numbers only
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_sum = 0
    odd_sum = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    print(f"Sum of evens: {even_sum}")
    print(f"Sum of odds: {odd_sum}")
    print(f"Total: {even_sum + odd_sum}")


def demonstrate_validation_loops():
    """
    Demonstrates using conditions inside loops for data validation.
    
    Validation loops check each item against business rules.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: VALIDATION LOOPS")
    print("=" * 60)
    
    # EMAIL VALIDATION FOR LIST
    print("\n1. VALIDATING EMAIL ADDRESSES")
    print("-" * 40)
    
    email_list = [
        "alice@example.com",
        "invalid-email",
        "bob@gmail.com",
        "missing@domain",
        "charlie@company.co.uk",
        "",
        "diana@site.org"
    ]
    
    valid_emails = []
    invalid_emails = []
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    for email in email_list:
        if not email:
            invalid_emails.append((email, "Empty email"))
        elif not re.match(email_pattern, email):
            invalid_emails.append((email, "Invalid format"))
        else:
            valid_emails.append(email)
    
    print(f"Valid emails ({len(valid_emails)}):")
    for email in valid_emails:
        print(f"  ✓ {email}")
    
    print(f"\nInvalid emails ({len(invalid_emails)}):")
    for email, reason in invalid_emails:
        print(f"  ✗ {email} → {reason}")
    
    # ORDER VALIDATION
    print("\n2. VALIDATING ORDERS")
    print("-" * 40)
    
    orders = [
        {"id": "ORD-001", "amount": 150, "status": "paid", "items": 3},
        {"id": "ORD-002", "amount": -25, "status": "pending", "items": 1},
        {"id": "ORD-003", "amount": 75, "status": "shipped", "items": 0},
        {"id": "ORD-004", "amount": 200, "status": "paid", "items": 4},
        {"id": "ORD-005", "amount": 0, "status": "cancelled", "items": 2}
    ]
    
    valid_orders = []
    invalid_orders = []
    
    for order in orders:
        errors = []
        
        if order["amount"] <= 0:
            errors.append(f"Invalid amount: ${order['amount']}")
        
        if order["items"] <= 0:
            errors.append(f"No items in order")
        
        if order["status"] not in ["pending", "paid", "shipped", "delivered", "cancelled"]:
            errors.append(f"Invalid status: {order['status']}")
        
        if errors:
            invalid_orders.append({"order": order, "errors": errors})
        else:
            valid_orders.append(order)
    
    print(f"Valid orders: {len(valid_orders)}")
    print(f"Invalid orders: {len(invalid_orders)}")
    
    for invalid in invalid_orders:
        print(f"\n  Order {invalid['order']['id']}:")
        for error in invalid['errors']:
            print(f"    ❌ {error}")
    
    # USER INPUT VALIDATION LOOP
    print("\n3. USER INPUT VALIDATION LOOP")
    print("-" * 40)
    
    # Simulated user inputs
    simulated_inputs = ["25", "-5", "abc", "100", "150", "quit"]
    input_index = 0
    
    valid_ages = []
    
    print("  (Simulated user input for demonstration)")
    
    while input_index < len(simulated_inputs):
        user_input = simulated_inputs[input_index]
        input_index += 1
        
        if user_input.lower() == "quit":
            print("  User quit")
            break
        
        # Validate age
        if not user_input.isdigit():
            print(f"  Invalid: '{user_input}' is not a number")
            continue
        
        age = int(user_input)
        
        if age < 0:
            print(f"  Invalid: Age cannot be negative ({age})")
            continue
        
        if age > 120:
            print(f"  Invalid: Age seems unrealistic ({age})")
            continue
        
        valid_ages.append(age)
        print(f"  Valid age: {age}")
    
    print(f"\nValid ages collected: {valid_ages}")


def build_multi_condition_filter():
    """
    Complete multi-condition product search filter.
    
    This demonstrates a real-world search system that filters
    products based on multiple criteria using nested conditions.
    
    SOLID Principles Applied:
    - Single Responsibility: Each filter condition is separate
    - Open/Closed: New filter criteria can be added
    
    Design Patterns:
    - Specification Pattern: Each filter is a specification
    - Composite Pattern: Multiple filters combined
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: MULTI-CONDITION PRODUCT FILTER")
    print("=" * 60)
    
    from typing import List, Dict, Any, Callable, Optional
    from enum import Enum
    from dataclasses import dataclass, field
    
    class ProductCategory(Enum):
        ELECTRONICS = "electronics"
        CLOTHING = "clothing"
        BOOKS = "books"
        HOME = "home"
        TOYS = "toys"
        SPORTS = "sports"
    
    class SortBy(Enum):
        PRICE_ASC = "price_asc"
        PRICE_DESC = "price_desc"
        NAME_ASC = "name_asc"
        NAME_DESC = "name_desc"
        RATING_DESC = "rating_desc"
    
    @dataclass
    class Product:
        """Represents a product in the catalog."""
        id: str
        name: str
        category: ProductCategory
        price: float
        rating: float
        in_stock: bool
        brand: str
        tags: List[str] = field(default_factory=list)
        
        def __str__(self) -> str:
            return f"{self.name} - ${self.price} ({self.rating}★)"
    
    @dataclass
    class FilterCriteria:
        """Filter criteria for product search."""
        categories: Optional[List[ProductCategory]] = None
        min_price: Optional[float] = None
        max_price: Optional[float] = None
        min_rating: Optional[float] = None
        in_stock_only: bool = False
        brands: Optional[List[str]] = None
        tags: Optional[List[str]] = None
        search_term: Optional[str] = None
    
    class ProductFilter:
        """
        Filters products based on multiple criteria.
        
        Design Pattern: Specification Pattern - Each filter is a specification
        """
        
        def __init__(self, products: List[Product]):
            self.products = products
        
        def apply_category_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by product category."""
            if criteria.categories:
                return product.category in criteria.categories
            return True
        
        def apply_price_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by price range."""
            if criteria.min_price is not None and product.price < criteria.min_price:
                return False
            if criteria.max_price is not None and product.price > criteria.max_price:
                return False
            return True
        
        def apply_rating_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by minimum rating."""
            if criteria.min_rating is not None:
                return product.rating >= criteria.min_rating
            return True
        
        def apply_stock_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by stock availability."""
            if criteria.in_stock_only:
                return product.in_stock
            return True
        
        def apply_brand_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by brand."""
            if criteria.brands:
                return product.brand in criteria.brands
            return True
        
        def apply_tags_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by tags."""
            if criteria.tags:
                return any(tag in product.tags for tag in criteria.tags)
            return True
        
        def apply_search_filter(self, product: Product, criteria: FilterCriteria) -> bool:
            """Filter by search term in name or tags."""
            if criteria.search_term:
                term_lower = criteria.search_term.lower()
                if term_lower in product.name.lower():
                    return True
                if any(term_lower in tag.lower() for tag in product.tags):
                    return True
                return False
            return True
        
        def filter(self, criteria: FilterCriteria) -> List[Product]:
            """
            Apply all filter criteria to the product list.
            
            Uses nested conditions inside a loop to apply multiple filters.
            """
            filtered = []
            
            for product in self.products:
                # Apply each filter condition (short-circuit evaluation)
                if not self.apply_category_filter(product, criteria):
                    continue
                
                if not self.apply_price_filter(product, criteria):
                    continue
                
                if not self.apply_rating_filter(product, criteria):
                    continue
                
                if not self.apply_stock_filter(product, criteria):
                    continue
                
                if not self.apply_brand_filter(product, criteria):
                    continue
                
                if not self.apply_tags_filter(product, criteria):
                    continue
                
                if not self.apply_search_filter(product, criteria):
                    continue
                
                # All filters passed
                filtered.append(product)
            
            return filtered
        
        def sort(self, products: List[Product], sort_by: SortBy) -> List[Product]:
            """Sort filtered products."""
            if sort_by == SortBy.PRICE_ASC:
                return sorted(products, key=lambda p: p.price)
            elif sort_by == SortBy.PRICE_DESC:
                return sorted(products, key=lambda p: p.price, reverse=True)
            elif sort_by == SortBy.NAME_ASC:
                return sorted(products, key=lambda p: p.name)
            elif sort_by == SortBy.NAME_DESC:
                return sorted(products, key=lambda p: p.name, reverse=True)
            elif sort_by == SortBy.RATING_DESC:
                return sorted(products, key=lambda p: p.rating, reverse=True)
            return products
        
        def get_statistics(self, products: List[Product]) -> Dict[str, Any]:
            """Get statistics for filtered products."""
            if not products:
                return {"count": 0}
            
            prices = [p.price for p in products]
            ratings = [p.rating for p in products]
            
            return {
                "count": len(products),
                "min_price": min(prices),
                "max_price": max(prices),
                "avg_price": sum(prices) / len(prices),
                "avg_rating": sum(ratings) / len(ratings),
                "categories": list(set(p.category for p in products)),
                "brands": list(set(p.brand for p in products))
            }
    
    # DEMONSTRATION
    print("\n📦 DEMONSTRATION: PRODUCT FILTER SYSTEM")
    print("-" * 40)
    
    # Create sample products
    sample_products = [
        Product("P001", "MacBook Pro", ProductCategory.ELECTRONICS, 1299.99, 4.8, True, "Apple", ["laptop", "premium"]),
        Product("P002", "Sony Headphones", ProductCategory.ELECTRONICS, 199.99, 4.5, True, "Sony", ["audio", "wireless"]),
        Product("P003", "Nike Running Shoes", ProductCategory.SPORTS, 89.99, 4.2, True, "Nike", ["shoes", "running"]),
        Product("P004", "Python Cookbook", ProductCategory.BOOKS, 49.99, 4.7, True, "O'Reilly", ["programming", "python"]),
        Product("P005", "Coffee Maker", ProductCategory.HOME, 79.99, 4.3, False, "Breville", ["kitchen", "coffee"]),
        Product("P006", "iPhone 15", ProductCategory.ELECTRONICS, 999.99, 4.9, True, "Apple", ["phone", "premium"]),
        Product("P007", "The Pragmatic Programmer", ProductCategory.BOOKS, 39.99, 4.8, True, "Addison-Wesley", ["programming"]),
        Product("P008", "Adidas Backpack", ProductCategory.SPORTS, 49.99, 4.1, True, "Adidas", ["bag", "sports"]),
        Product("P009", "Desk Lamp", ProductCategory.HOME, 29.99, 4.0, True, "IKEA", ["lighting", "office"]),
        Product("P010", "Mechanical Keyboard", ProductCategory.ELECTRONICS, 149.99, 4.6, False, "Logitech", ["keyboard", "gaming"])
    ]
    
    print("Product catalog loaded:")
    for p in sample_products[:5]:
        print(f"  {p}")
    print(f"  ... and {len(sample_products) - 5} more")
    
    # Create filter
    product_filter = ProductFilter(sample_products)
    
    # Test various filter combinations
    print("\n1. FILTER: Electronics only")
    print("-" * 40)
    
    criteria = FilterCriteria(
        categories=[ProductCategory.ELECTRONICS]
    )
    results = product_filter.filter(criteria)
    print(f"Found {len(results)} products:")
    for p in results:
        print(f"  {p}")
    
    print("\n2. FILTER: Electronics under $200, in stock")
    print("-" * 40)
    
    criteria = FilterCriteria(
        categories=[ProductCategory.ELECTRONICS],
        max_price=200,
        in_stock_only=True
    )
    results = product_filter.filter(criteria)
    print(f"Found {len(results)} products:")
    for p in results:
        print(f"  {p}")
    
    print("\n3. FILTER: Books with rating >= 4.5")
    print("-" * 40)
    
    criteria = FilterCriteria(
        categories=[ProductCategory.BOOKS],
        min_rating=4.5
    )
    results = product_filter.filter(criteria)
    print(f"Found {len(results)} products:")
    for p in results:
        print(f"  {p}")
    
    print("\n4. FILTER: Products with 'programming' tag")
    print("-" * 40)
    
    criteria = FilterCriteria(
        tags=["programming"]
    )
    results = product_filter.filter(criteria)
    print(f"Found {len(results)} products:")
    for p in results:
        print(f"  {p}")
    
    print("\n5. FILTER: Apple products under $1000")
    print("-" * 40)
    
    criteria = FilterCriteria(
        brands=["Apple"],
        max_price=1000,
        in_stock_only=True
    )
    results = product_filter.filter(criteria)
    print(f"Found {len(results)} products:")
    for p in results:
        print(f"  {p}")
    
    print("\n6. COMPLEX FILTER: Electronics or Books, 4+ stars, in stock")
    print("-" * 40)
    
    criteria = FilterCriteria(
        categories=[ProductCategory.ELECTRONICS, ProductCategory.BOOKS],
        min_rating=4.0,
        in_stock_only=True
    )
    results = product_filter.filter(criteria)
    print(f"Found {len(results)} products:")
    for p in results:
        print(f"  {p}")
    
    # Sort results
    print("\n7. SORTED RESULTS (by rating descending)")
    print("-" * 40)
    
    sorted_results = product_filter.sort(results, SortBy.RATING_DESC)
    for p in sorted_results:
        print(f"  {p.name}: {p.rating}★ - ${p.price}")
    
    # Statistics
    print("\n8. FILTER STATISTICS")
    print("-" * 40)
    
    stats = product_filter.get_statistics(results)
    print(f"Count: {stats['count']}")
    print(f"Price range: ${stats['min_price']:.2f} - ${stats['max_price']:.2f}")
    print(f"Average price: ${stats['avg_price']:.2f}")
    print(f"Average rating: {stats['avg_rating']:.1f}★")
    print(f"Categories: {[c.value for c in stats['categories']]}")
    print(f"Brands: {stats['brands']}")


if __name__ == "__main__":
    demonstrate_basic_nested_conditions()
    demonstrate_validation_loops()
    build_multi_condition_filter()
```

---

## 🧩 Section 2: Nested Loops – Iterating Over Multi-dimensional Data

Nested loops are loops inside loops. They're essential for working with multi-dimensional data like matrices, grids, and nested collections.

**SOLID Principle Applied: Single Responsibility** – Each loop level has one iteration responsibility.

**Design Pattern: Iterator Pattern** – Nested iterators traverse multi-dimensional structures.

```python
"""
NESTED LOOPS: ITERATING OVER MULTI-DIMENSIONAL DATA

This section covers loops inside loops for multi-dimensional data.

SOLID Principle: Single Responsibility
- Each loop level has one iteration responsibility

Design Pattern: Iterator Pattern
- Nested iterators traverse multi-dimensional structures
"""

from typing import List, Any, Dict, Tuple
import time


def demonstrate_basic_nested_loops():
    """
    Demonstrates basic nested loop patterns.
    
    Nested loops are essential for matrices, grids, and combinations.
    """
    print("=" * 60)
    print("SECTION 2A: BASIC NESTED LOOPS")
    print("=" * 60)
    
    # 2D LIST (MATRIX) ITERATION
    print("\n1. ITERATING OVER A 2D MATRIX")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matrix:")
    for row in matrix:
        for value in row:
            print(f"  {value}", end=" ")
        print()
    
    # WITH INDEX ACCESS
    print("\n2. WITH INDEX ACCESS")
    print("-" * 40)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"  matrix[{i}][{j}] = {matrix[i][j]}")
    
    # GENERATING COMBINATIONS
    print("\n3. GENERATING COMBINATIONS")
    print("-" * 40)
    
    colors = ["red", "green", "blue"]
    sizes = ["S", "M", "L"]
    
    print("All color-size combinations:")
    for color in colors:
        for size in sizes:
            print(f"  {color} - {size}")
    
    # GENERATING COORDINATES
    print("\n4. GENERATING COORDINATES")
    print("-" * 40)
    
    coordinates = []
    for x in range(3):
        for y in range(3):
            coordinates.append((x, y))
    
    print(f"All coordinates in 3x3 grid: {coordinates}")
    
    # MULTIPLICATION TABLE
    print("\n5. MULTIPLICATION TABLE")
    print("-" * 40)
    
    print("Multiplication Table (1-5):")
    print("    ", end="")
    for i in range(1, 6):
        print(f"{i:4}", end="")
    print()
    print("    " + "-" * 20)
    
    for i in range(1, 6):
        print(f"{i:2} |", end="")
        for j in range(1, 6):
            print(f"{i * j:4}", end="")
        print()
    
    # NESTED LOOP WITH BREAK
    print("\n6. BREAK IN NESTED LOOPS")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    target = 10
    found = False
    
    print(f"Searching for {target} in matrix:")
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            print(f"  Checking ({i},{j}) = {value}")
            if value == target:
                print(f"    ✓ Found at ({i}, {j})!")
                found = True
                break
        if found:
            break
    
    if not found:
        print(f"  {target} not found")


def demonstrate_nested_loop_patterns():
    """
    Demonstrates common nested loop patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: NESTED LOOP PATTERNS")
    print("=" * 60)
    
    # TRIANGULAR PATTERNS
    print("\n1. TRIANGULAR PATTERNS")
    print("-" * 40)
    
    n = 5
    
    print("Lower triangle:")
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()
    
    print("\nUpper triangle:")
    for i in range(n):
        for j in range(n - i):
            print("*", end="")
        print()
    
    # DIAGONAL TRAVERSAL
    print("\n2. DIAGONAL TRAVERSAL")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Main diagonal:")
    for i in range(len(matrix)):
        print(f"  matrix[{i}][{i}] = {matrix[i][i]}")
    
    print("\nAnti-diagonal:")
    for i in range(len(matrix)):
        j = len(matrix) - 1 - i
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}")
    
    # BORDER TRAVERSAL
    print("\n3. BORDER TRAVERSAL")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    rows, cols = len(matrix), len(matrix[0])
    border = []
    
    # Top row
    for j in range(cols):
        border.append(matrix[0][j])
    
    # Right column (excluding corners)
    for i in range(1, rows - 1):
        border.append(matrix[i][cols - 1])
    
    # Bottom row (reverse)
    if rows > 1:
        for j in range(cols - 1, -1, -1):
            border.append(matrix[rows - 1][j])
    
    # Left column (excluding corners)
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            border.append(matrix[i][0])
    
    print(f"Border traversal: {border}")
    
    # FLATTENING NESTED LISTS
    print("\n4. FLATTENING NESTED LISTS")
    print("-" * 40)
    
    nested = [[1, 2], [3, 4, 5], [6, 7], [8, 9, 10]]
    
    flattened = []
    for sublist in nested:
        for item in sublist:
            flattened.append(item)
    
    print(f"Nested: {nested}")
    print(f"Flattened: {flattened}")
    
    # FINDING MAX IN 2D
    print("\n5. FINDING MAXIMUM IN 2D")
    print("-" * 40)
    
    matrix = [
        [3, 7, 2, 8],
        [5, 9, 1, 4],
        [6, 2, 8, 3],
        [7, 5, 4, 9]
    ]
    
    max_value = matrix[0][0]
    max_pos = (0, 0)
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_pos = (i, j)
    
    print(f"Maximum value: {max_value} at position {max_pos}")
    
    # ROW AND COLUMN SUMS
    print("\n6. ROW AND COLUMN SUMS")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    
    col_sums = [0] * len(matrix[0])
    for row in matrix:
        for j, value in enumerate(row):
            col_sums[j] += value
    
    print(f"Matrix:")
    for row in matrix:
        print(f"  {row}")
    print(f"Row sums: {row_sums}")
    print(f"Column sums: {col_sums}")


def build_sudoku_validator():
    """
    Complete Sudoku validator using nested loops and conditions.
    
    This demonstrates a real-world system that validates Sudoku puzzles
    by checking rows, columns, and 3x3 subgrids.
    
    SOLID Principles Applied:
    - Single Responsibility: Each validation method checks one aspect
    - Open/Closed: New validation rules can be added
    
    Design Patterns:
    - Strategy Pattern: Different validation strategies
    - Composite Pattern: Multiple validation rules combined
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: SUDOKU VALIDATOR")
    print("=" * 60)
    
    from typing import List, Tuple, Optional, Set
    from dataclasses import dataclass
    
    @dataclass
    class ValidationResult:
        """Result of Sudoku validation."""
        is_valid: bool
        errors: List[str]
        row_errors: List[int]
        col_errors: List[int]
        box_errors: List[int]
    
    class SudokuValidator:
        """
        Validates Sudoku puzzles using nested loops.
        
        Design Pattern: Strategy Pattern - Different validation strategies
        """
        
        def __init__(self, board: List[List[int]]):
            """
            Initialize validator with a 9x9 Sudoku board.
            
            Args:
                board: 9x9 list of lists with numbers 0-9 (0 represents empty)
            """
            self.board = board
            self.size = 9
            self.box_size = 3
        
        def validate_board_size(self) -> Tuple[bool, str]:
            """Check if board is 9x9."""
            if len(self.board) != 9:
                return False, f"Board has {len(self.board)} rows, expected 9"
            
            for i, row in enumerate(self.board):
                if len(row) != 9:
                    return False, f"Row {i} has {len(row)} columns, expected 9"
            
            return True, "Board size valid"
        
        def validate_cell_values(self) -> List[str]:
            """Check if all cell values are between 0 and 9."""
            errors = []
            for i in range(self.size):
                for j in range(self.size):
                    value = self.board[i][j]
                    if value < 0 or value > 9:
                        errors.append(f"Cell ({i},{j}) has invalid value {value}")
            return errors
        
        def validate_row(self, row: int) -> Tuple[bool, Set[int]]:
            """
            Validate a single row.
            
            Returns:
                Tuple of (is_valid, set of duplicates)
            """
            seen = set()
            duplicates = set()
            
            for col in range(self.size):
                value = self.board[row][col]
                if value != 0:  # Skip empty cells
                    if value in seen:
                        duplicates.add(value)
                    seen.add(value)
            
            return len(duplicates) == 0, duplicates
        
        def validate_column(self, col: int) -> Tuple[bool, Set[int]]:
            """
            Validate a single column.
            
            Returns:
                Tuple of (is_valid, set of duplicates)
            """
            seen = set()
            duplicates = set()
            
            for row in range(self.size):
                value = self.board[row][col]
                if value != 0:
                    if value in seen:
                        duplicates.add(value)
                    seen.add(value)
            
            return len(duplicates) == 0, duplicates
        
        def validate_box(self, box_row: int, box_col: int) -> Tuple[bool, Set[int]]:
            """
            Validate a single 3x3 box.
            
            Args:
                box_row: Box row index (0-2)
                box_col: Box column index (0-2)
                
            Returns:
                Tuple of (is_valid, set of duplicates)
            """
            seen = set()
            duplicates = set()
            
            start_row = box_row * self.box_size
            start_col = box_col * self.box_size
            
            for i in range(self.box_size):
                for j in range(self.box_size):
                    value = self.board[start_row + i][start_col + j]
                    if value != 0:
                        if value in seen:
                            duplicates.add(value)
                        seen.add(value)
            
            return len(duplicates) == 0, duplicates
        
        def validate_all_rows(self) -> Tuple[bool, List[int], Set[int]]:
            """Validate all rows using nested loops."""
            row_errors = []
            all_duplicates = set()
            
            for row in range(self.size):
                is_valid, duplicates = self.validate_row(row)
                if not is_valid:
                    row_errors.append(row)
                    all_duplicates.update(duplicates)
            
            return len(row_errors) == 0, row_errors, all_duplicates
        
        def validate_all_columns(self) -> Tuple[bool, List[int], Set[int]]:
            """Validate all columns using nested loops."""
            col_errors = []
            all_duplicates = set()
            
            for col in range(self.size):
                is_valid, duplicates = self.validate_column(col)
                if not is_valid:
                    col_errors.append(col)
                    all_duplicates.update(duplicates)
            
            return len(col_errors) == 0, col_errors, all_duplicates
        
        def validate_all_boxes(self) -> Tuple[bool, List[int], Set[int]]:
            """Validate all 3x3 boxes using nested loops."""
            box_errors = []
            all_duplicates = set()
            
            for box_row in range(self.box_size):
                for box_col in range(self.box_size):
                    box_num = box_row * self.box_size + box_col
                    is_valid, duplicates = self.validate_box(box_row, box_col)
                    if not is_valid:
                        box_errors.append(box_num)
                        all_duplicates.update(duplicates)
            
            return len(box_errors) == 0, box_errors, all_duplicates
        
        def validate_complete(self) -> ValidationResult:
            """
            Run complete validation of the Sudoku board.
            
            Uses nested loops and conditions to check all constraints.
            """
            errors = []
            row_errors = []
            col_errors = []
            box_errors = []
            
            # Check board size
            size_valid, size_error = self.validate_board_size()
            if not size_valid:
                errors.append(size_error)
                return ValidationResult(False, errors, [], [], [])
            
            # Check cell values
            value_errors = self.validate_cell_values()
            errors.extend(value_errors)
            
            # Validate rows
            rows_valid, rows_invalid, row_dups = self.validate_all_rows()
            if not rows_valid:
                errors.append(f"Row validation failed: rows {rows_invalid}")
                row_errors = rows_invalid
            
            # Validate columns
            cols_valid, cols_invalid, col_dups = self.validate_all_columns()
            if not cols_valid:
                errors.append(f"Column validation failed: columns {cols_invalid}")
                col_errors = cols_invalid
            
            # Validate boxes
            boxes_valid, boxes_invalid, box_dups = self.validate_all_boxes()
            if not boxes_valid:
                errors.append(f"Box validation failed: boxes {boxes_invalid}")
                box_errors = boxes_invalid
            
            is_valid = size_valid and not value_errors and rows_valid and cols_valid and boxes_valid
            
            return ValidationResult(
                is_valid=is_valid,
                errors=errors,
                row_errors=row_errors,
                col_errors=col_errors,
                box_errors=box_errors
            )
        
        def print_board(self) -> None:
            """Print the Sudoku board with formatting."""
            print("\n" + "-" * 25)
            for i in range(self.size):
                row_str = "| "
                for j in range(self.size):
                    val = self.board[i][j] if self.board[i][j] != 0 else "."
                    row_str += f"{val} "
                    if (j + 1) % 3 == 0:
                        row_str += "| "
                print(row_str)
                if (i + 1) % 3 == 0:
                    print("-" * 25)
        
        def highlight_errors(self, result: ValidationResult) -> None:
            """Print board with error highlighting."""
            print("\n" + "=" * 25)
            print("BOARD WITH ERRORS:")
            
            for i in range(self.size):
                row_str = "| "
                for j in range(self.size):
                    val = self.board[i][j] if self.board[i][j] != 0 else "."
                    
                    # Check if this cell is in error
                    in_error = False
                    if i in result.row_errors:
                        in_error = True
                    if j in result.col_errors:
                        in_error = True
                    
                    # Check box error
                    box_num = (i // 3) * 3 + (j // 3)
                    if box_num in result.box_errors:
                        in_error = True
                    
                    if in_error and self.board[i][j] != 0:
                        row_str += f"[{val}]"
                    else:
                        row_str += f" {val} "
                    
                    if (j + 1) % 3 == 0:
                        row_str += "| "
                
                print(row_str)
                if (i + 1) % 3 == 0:
                    print("-" * 25)
    
    # DEMONSTRATION
    print("\n🔢 DEMONSTRATION: SUDOKU VALIDATOR")
    print("-" * 40)
    
    # Valid Sudoku puzzle
    valid_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    # Invalid Sudoku puzzle (row duplicate)
    invalid_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [5, 0, 0, 0, 8, 0, 0, 7, 9]  # Duplicate 5 in column 0
    ]
    
    print("1. VALID SUDOKU BOARD")
    print("-" * 40)
    
    validator = SudokuValidator(valid_board)
    validator.print_board()
    
    result = validator.validate_complete()
    
    print(f"\nValidation Result: {'✓ VALID' if result.is_valid else '✗ INVALID'}")
    
    if not result.is_valid:
        print("Errors:")
        for error in result.errors:
            print(f"  • {error}")
    
    print("\n2. INVALID SUDOKU BOARD")
    print("-" * 40)
    
    validator = SudokuValidator(invalid_board)
    validator.print_board()
    
    result = validator.validate_complete()
    
    print(f"\nValidation Result: {'✓ VALID' if result.is_valid else '✗ INVALID'}")
    
    if not result.is_valid:
        print("Errors:")
        for error in result.errors:
            print(f"  • {error}")
    
    if result.row_errors:
        print(f"  • Invalid rows: {result.row_errors}")
    if result.col_errors:
        print(f"  • Invalid columns: {result.col_errors}")
    if result.box_errors:
        print(f"  • Invalid boxes: {result.box_errors}")
    
    # Highlight errors
    validator.highlight_errors(result)
    
    print("\n3. NESTED LOOP ANALYSIS")
    print("-" * 40)
    
    print("The Sudoku validator uses nested loops for:")
    print("  • Row validation: for row in range(9): for col in range(9)")
    print("  • Column validation: for col in range(9): for row in range(9)")
    print("  • Box validation: for i in range(3): for j in range(3)")
    print("  • Error highlighting: for row in range(9): for col in range(9)")
    
    print("\nComplexity: O(9×9) = O(81) per validation pass")


if __name__ == "__main__":
    demonstrate_basic_nested_loops()
    demonstrate_nested_loop_patterns()
    build_sudoku_validator()
```

---

## 🎯 Section 3: Student Grade Matrix Analyzer

A complete system for analyzing grades across multiple classes, students, and assignments using nested logic.

**SOLID Principles Applied:**
- Single Responsibility: Each analyzer has one purpose
- Open/Closed: New analysis methods can be added
- Dependency Inversion: Depends on abstractions

**Design Patterns:**
- Composite Pattern: Students in classes form hierarchy
- Strategy Pattern: Different analysis strategies
- Visitor Pattern: Traverse grade structure

```python
"""
STUDENT GRADE MATRIX ANALYZER

This section builds a complete system for analyzing grades
across multiple classes, students, and assignments using nested logic.

SOLID Principles Applied:
- Single Responsibility: Each analyzer has one purpose
- Open/Closed: New analysis methods can be added

Design Patterns:
- Composite Pattern: Students in classes form hierarchy
- Strategy Pattern: Different analysis strategies
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import statistics


class GradeLevel(Enum):
    """Grade levels."""
    FRESHMAN = 9
    SOPHOMORE = 10
    JUNIOR = 11
    SENIOR = 12


class AssignmentType(Enum):
    """Types of assignments with different weights."""
    HOMEWORK = "homework"
    QUIZ = "quiz"
    TEST = "test"
    PROJECT = "project"
    FINAL = "final"


@dataclass
class Assignment:
    """Represents a single assignment."""
    name: str
    type: AssignmentType
    max_score: float
    weight: float  # Percentage weight in final grade
    score: Optional[float] = None


@dataclass
class Student:
    """Represents a student."""
    id: str
    name: str
    grade_level: GradeLevel
    assignments: List[Assignment] = field(default_factory=list)
    
    def calculate_average(self) -> float:
        """Calculate weighted average for this student."""
        if not self.assignments:
            return 0.0
        
        total_weighted_score = 0.0
        total_weight = 0.0
        
        for assignment in self.assignments:
            if assignment.score is not None:
                percentage = (assignment.score / assignment.max_score) * 100
                total_weighted_score += percentage * assignment.weight
                total_weight += assignment.weight
        
        if total_weight == 0:
            return 0.0
        
        return total_weighted_score / total_weight
    
    def calculate_letter_grade(self) -> str:
        """Convert numeric average to letter grade."""
        avg = self.calculate_average()
        
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def get_missing_assignments(self) -> List[Assignment]:
        """Get list of assignments not yet submitted."""
        return [a for a in self.assignments if a.score is None]
    
    def get_lowest_score(self) -> Optional[float]:
        """Get lowest assignment score."""
        scores = [a.score for a in self.assignments if a.score is not None]
        return min(scores) if scores else None
    
    def get_highest_score(self) -> Optional[float]:
        """Get highest assignment score."""
        scores = [a.score for a in self.assignments if a.score is not None]
        return max(scores) if scores else None


@dataclass
class Class:
    """Represents a class with multiple students."""
    name: str
    code: str
    teacher: str
    students: List[Student] = field(default_factory=list)
    
    def calculate_class_average(self) -> float:
        """Calculate average grade for the entire class."""
        if not self.students:
            return 0.0
        
        total = sum(s.calculate_average() for s in self.students)
        return total / len(self.students)
    
    def get_grade_distribution(self) -> Dict[str, int]:
        """Get distribution of letter grades in the class."""
        distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        
        for student in self.students:
            grade = student.calculate_letter_grade()
            distribution[grade] = distribution.get(grade, 0) + 1
        
        return distribution
    
    def get_top_students(self, n: int = 3) -> List[Student]:
        """Get top N students by average."""
        sorted_students = sorted(
            self.students,
            key=lambda s: s.calculate_average(),
            reverse=True
        )
        return sorted_students[:n]
    
    def get_struggling_students(self, threshold: float = 70) -> List[Student]:
        """Get students below threshold."""
        return [s for s in self.students if s.calculate_average() < threshold]
    
    def get_assignment_statistics(self) -> Dict[str, Any]:
        """Calculate statistics for each assignment."""
        stats = {}
        
        for assignment_name in self._get_all_assignment_names():
            scores = []
            for student in self.students:
                for assignment in student.assignments:
                    if assignment.name == assignment_name and assignment.score is not None:
                        percentage = (assignment.score / assignment.max_score) * 100
                        scores.append(percentage)
            
            if scores:
                stats[assignment_name] = {
                    "average": statistics.mean(scores),
                    "median": statistics.median(scores),
                    "min": min(scores),
                    "max": max(scores),
                    "std_dev": statistics.stdev(scores) if len(scores) > 1 else 0
                }
        
        return stats
    
    def _get_all_assignment_names(self) -> List[str]:
        """Get unique assignment names across all students."""
        names = set()
        for student in self.students:
            for assignment in student.assignments:
                names.add(assignment.name)
        return sorted(names)


class GradeAnalyzer:
    """
    Complete grade analysis system using nested loops.
    
    Design Pattern: Visitor Pattern - Traverses grade structure
    """
    
    def __init__(self, classes: List[Class]):
        self.classes = classes
    
    def get_school_average(self) -> float:
        """Calculate average across all classes."""
        if not self.classes:
            return 0.0
        
        total = sum(c.calculate_class_average() for c in self.classes)
        return total / len(self.classes)
    
    def get_grade_level_summary(self) -> Dict[GradeLevel, Dict[str, Any]]:
        """Get summary statistics by grade level."""
        summary = {}
        
        for level in GradeLevel:
            students_in_level = []
            for class_obj in self.classes:
                for student in class_obj.students:
                    if student.grade_level == level:
                        students_in_level.append(student)
            
            if students_in_level:
                averages = [s.calculate_average() for s in students_in_level]
                summary[level] = {
                    "count": len(students_in_level),
                    "average": statistics.mean(averages),
                    "median": statistics.median(averages),
                    "min": min(averages),
                    "max": max(averages)
                }
            else:
                summary[level] = {"count": 0}
        
        return summary
    
    def get_assignment_analysis(self) -> Dict[str, Any]:
        """Analyze all assignments across all classes."""
        all_scores = []
        missing_submissions = 0
        total_assignments = 0
        
        for class_obj in self.classes:
            for student in class_obj.students:
                for assignment in student.assignments:
                    total_assignments += 1
                    if assignment.score is None:
                        missing_submissions += 1
                    else:
                        percentage = (assignment.score / assignment.max_score) * 100
                        all_scores.append(percentage)
        
        return {
            "total_assignments": total_assignments,
            "missing_submissions": missing_submissions,
            "completion_rate": ((total_assignments - missing_submissions) / total_assignments * 100) if total_assignments > 0 else 0,
            "average_score": statistics.mean(all_scores) if all_scores else 0,
            "median_score": statistics.median(all_scores) if all_scores else 0,
            "min_score": min(all_scores) if all_scores else 0,
            "max_score": max(all_scores) if all_scores else 0
        }
    
    def find_at_risk_students(self, threshold: float = 65) -> List[Tuple[Student, Class, float]]:
        """Find students below threshold across all classes."""
        at_risk = []
        
        for class_obj in self.classes:
            for student in class_obj.students:
                avg = student.calculate_average()
                if avg < threshold:
                    at_risk.append((student, class_obj, avg))
        
        return sorted(at_risk, key=lambda x: x[2])
    
    def generate_report(self) -> str:
        """Generate comprehensive school report."""
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("SCHOOL GRADE ANALYSIS REPORT")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        # Overall statistics
        school_avg = self.get_school_average()
        total_students = sum(len(c.students) for c in self.classes)
        
        report_lines.append(f"\n📊 OVERALL STATISTICS:")
        report_lines.append(f"  Total Classes: {len(self.classes)}")
        report_lines.append(f"  Total Students: {total_students}")
        report_lines.append(f"  School Average: {school_avg:.1f}%")
        
        # Class summaries
        report_lines.append(f"\n📚 CLASS SUMMARIES:")
        for class_obj in self.classes:
            class_avg = class_obj.calculate_class_average()
            report_lines.append(f"\n  {class_obj.name} ({class_obj.code})")
            report_lines.append(f"    Teacher: {class_obj.teacher}")
            report_lines.append(f"    Students: {len(class_obj.students)}")
            report_lines.append(f"    Class Average: {class_avg:.1f}%")
            
            # Grade distribution
            distribution = class_obj.get_grade_distribution()
            report_lines.append(f"    Grade Distribution: A:{distribution['A']} B:{distribution['B']} C:{distribution['C']} D:{distribution['D']} F:{distribution['F']}")
            
            # Top students
            top = class_obj.get_top_students(3)
            if top:
                report_lines.append(f"    Top Students: {', '.join([f'{s.name}({s.calculate_average():.0f}%)' for s in top])}")
        
        # Grade level summary
        report_lines.append(f"\n🎓 GRADE LEVEL SUMMARY:")
        level_summary = self.get_grade_level_summary()
        for level, stats in level_summary.items():
            if stats["count"] > 0:
                report_lines.append(f"  {level.name}: {stats['count']} students, Avg: {stats['average']:.1f}%")
        
        # At-risk students
        at_risk = self.find_at_risk_students()
        if at_risk:
            report_lines.append(f"\n⚠️ AT-RISK STUDENTS (Below 65%):")
            for student, class_obj, avg in at_risk[:10]:
                report_lines.append(f"  {student.name} ({class_obj.name}): {avg:.1f}%")
        
        # Assignment analysis
        assignment_analysis = self.get_assignment_analysis()
        report_lines.append(f"\n📝 ASSIGNMENT ANALYSIS:")
        report_lines.append(f"  Total Assignments: {assignment_analysis['total_assignments']}")
        report_lines.append(f"  Completion Rate: {assignment_analysis['completion_rate']:.1f}%")
        report_lines.append(f"  Average Score: {assignment_analysis['average_score']:.1f}%")
        
        report_lines.append("\n" + "=" * 60)
        
        return "\n".join(report_lines)


def build_grade_matrix():
    """
    Build and demonstrate the complete grade analysis system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: STUDENT GRADE MATRIX ANALYZER")
    print("=" * 60)
    
    # Create sample data
    print("\n📚 BUILDING GRADE MATRIX")
    print("-" * 40)
    
    # Define assignments
    assignments = [
        Assignment("Homework 1", AssignmentType.HOMEWORK, 100, 10),
        Assignment("Homework 2", AssignmentType.HOMEWORK, 100, 10),
        Assignment("Quiz 1", AssignmentType.QUIZ, 50, 5),
        Assignment("Quiz 2", AssignmentType.QUIZ, 50, 5),
        Assignment("Midterm", AssignmentType.TEST, 100, 25),
        Assignment("Project", AssignmentType.PROJECT, 100, 25),
        Assignment("Final", AssignmentType.FINAL, 100, 20)
    ]
    
    # Create students with varying performance
    students_data = [
        # Class 1: Computer Science
        ("CS-001", "Alice Chen", GradeLevel.SENIOR, [95, 92, 88, 90, 94, 96, 91]),
        ("CS-002", "Bob Smith", GradeLevel.SENIOR, [85, 82, 78, 80, 84, 86, 81]),
        ("CS-003", "Charlie Brown", GradeLevel.SENIOR, [75, 72, 68, 70, 74, 76, 71]),
        ("CS-004", "Diana Prince", GradeLevel.SENIOR, [98, 95, 94, 96, 97, 98, 95]),
        ("CS-005", "Eve Wilson", GradeLevel.SENIOR, [65, 62, 58, 60, 64, 66, 61]),
        
        # Class 2: Mathematics
        ("MATH-001", "Frank Castle", GradeLevel.JUNIOR, [88, 85, 82, 84, 88, 90, 85]),
        ("MATH-002", "Grace Hopper", GradeLevel.JUNIOR, [92, 90, 88, 91, 93, 94, 92]),
        ("MATH-003", "Henry Ford", GradeLevel.JUNIOR, [78, 75, 72, 74, 78, 80, 75]),
        ("MATH-004", "Irene Adler", GradeLevel.JUNIOR, [85, 82, 80, 83, 85, 87, 84]),
        
        # Class 3: Physics
        ("PHY-001", "Jack Ryan", GradeLevel.SOPHOMORE, [82, 80, 78, 79, 82, 84, 80]),
        ("PHY-002", "Katherine Johnson", GradeLevel.SOPHOMORE, [95, 93, 91, 92, 94, 95, 93]),
        ("PHY-003", "Leo Tolstoy", GradeLevel.SOPHOMORE, [70, 68, 65, 67, 70, 72, 68]),
        
        # Class 4: English
        ("ENG-001", "Mary Shelley", GradeLevel.FRESHMAN, [85, 88, 90, 87, 85, 86, 88]),
        ("ENG-002", "Nathaniel Hawthorne", GradeLevel.FRESHMAN, [78, 80, 82, 79, 78, 80, 79]),
        ("ENG-003", "Oscar Wilde", GradeLevel.FRESHMAN, [92, 94, 96, 93, 92, 94, 93])
    ]
    
    # Build classes using nested loops
    classes = []
    
    # Group students by class
    class_groups = {
        "CS": ("Computer Science", "Prof. Turing"),
        "MATH": ("Mathematics", "Prof. Euler"),
        "PHY": ("Physics", "Prof. Einstein"),
        "ENG": ("English", "Prof. Shakespeare")
    }
    
    for student_data in students_data:
        student_id, name, level, scores = student_data
        class_prefix = student_id.split("-")[0]
        class_name, teacher = class_groups.get(class_prefix, ("General", "Staff"))
        
        # Find or create class
        class_obj = None
        for c in classes:
            if c.code == class_prefix:
                class_obj = c
                break
        
        if class_obj is None:
            class_obj = Class(class_name, class_prefix, teacher)
            classes.append(class_obj)
        
        # Create student with assignments
        student_assignments = []
        for i, (assignment, score) in enumerate(zip(assignments, scores)):
            student_assignments.append(Assignment(
                name=assignment.name,
                type=assignment.type,
                max_score=assignment.max_score,
                weight=assignment.weight,
                score=score
            ))
        
        # Add missing assignment for some students
        if student_id == "CS-005":
            student_assignments[-1].score = None  # Missing final exam
        
        student = Student(student_id, name, level, student_assignments)
        class_obj.students.append(student)
    
    # Create analyzer
    analyzer = GradeAnalyzer(classes)
    
    # Print individual student reports
    print("\n1. INDIVIDUAL STUDENT REPORTS")
    print("-" * 40)
    
    for class_obj in classes[:2]:  # Show first 2 classes
        for student in class_obj.students[:2]:  # Show first 2 students
            print(f"\n  Student: {student.name} ({class_obj.name})")
            print(f"    Average: {student.calculate_average():.1f}%")
            print(f"    Letter Grade: {student.calculate_letter_grade()}")
            print(f"    Highest Score: {student.get_highest_score():.0f}")
            print(f"    Lowest Score: {student.get_lowest_score():.0f}")
            missing = student.get_missing_assignments()
            if missing:
                print(f"    Missing: {', '.join(a.name for a in missing)}")
    
    # Class summaries
    print("\n2. CLASS SUMMARIES")
    print("-" * 40)
    
    for class_obj in classes:
        print(f"\n  {class_obj.name} ({class_obj.code})")
        print(f"    Class Average: {class_obj.calculate_class_average():.1f}%")
        
        distribution = class_obj.get_grade_distribution()
        print(f"    Grade Distribution: A:{distribution['A']} B:{distribution['B']} C:{distribution['C']} D:{distribution['D']} F:{distribution['F']}")
        
        top = class_obj.get_top_students(2)
        print(f"    Top Students: {', '.join([f'{s.name}({s.calculate_average():.0f}%)' for s in top])}")
        
        struggling = class_obj.get_struggling_students(70)
        if struggling:
            print(f"    Struggling (<70%): {', '.join([s.name for s in struggling])}")
    
    # Assignment statistics
    print("\n3. ASSIGNMENT STATISTICS")
    print("-" * 40)
    
    for class_obj in classes:
        print(f"\n  {class_obj.name}:")
        stats = class_obj.get_assignment_statistics()
        for assignment, data in list(stats.items())[:3]:  # Show first 3
            print(f"    {assignment}: Avg {data['average']:.1f}% (Min {data['min']:.0f}%, Max {data['max']:.0f}%)")
    
    # Grade level summary
    print("\n4. GRADE LEVEL SUMMARY")
    print("-" * 40)
    
    level_summary = analyzer.get_grade_level_summary()
    for level, stats in level_summary.items():
        if stats["count"] > 0:
            print(f"  {level.name}: {stats['count']} students, Avg: {stats['average']:.1f}%")
    
    # At-risk students
    print("\n5. AT-RISK STUDENTS")
    print("-" * 40)
    
    at_risk = analyzer.find_at_risk_students(70)
    for student, class_obj, avg in at_risk:
        print(f"  {student.name} ({class_obj.name}): {avg:.1f}%")
    
    # Complete report
    print("\n6. COMPLETE SCHOOL REPORT")
    print("-" * 40)
    
    report = analyzer.generate_report()
    print(report)


if __name__ == "__main__":
    build_grade_matrix()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Conditions Inside Loops** – Filter data during iteration. Validate each item against business rules. Use continue for early skipping.

- **Nested Loops** – Iterate over multi-dimensional data. Process matrices, grids, and nested collections. Be mindful of time complexity (O(n²) for 2D).

- **Multi-Condition Filter** – Combine multiple filter criteria. Use short-circuit evaluation with continue statements. Build complex search systems.

- **Sudoku Validator** – Validate rows, columns, and subgrids using nested loops. Track errors and highlight invalid cells.

- **Grade Matrix Analyzer** – Process nested data structures (classes → students → assignments). Calculate statistics across multiple dimensions. Generate comprehensive reports.

- **SOLID Principles Applied** – Single Responsibility (each validation function has one purpose), Open/Closed (new filters can be added), Dependency Inversion (abstractions over implementations).

- **Design Patterns Used** – Filter Pattern (conditions as filters), Iterator Pattern (nested iteration), Specification Pattern (composite criteria), Visitor Pattern (traverse grade structure), Composite Pattern (hierarchical data).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Loops – for, while, break, continue

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 6 | 1 | 86% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **11** | **41** | **21%** |

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap: Reading the Map
4. Series 0, Story 4: The 2026 Python Metromap: Avoiding Derailments
5. Series 0, Story 5: The 2026 Python Metromap: From Passenger to Driver
6. Series A, Story 1: The 2026 Python Metromap: Variables & Data Types – The Rails of Python
7. Series A, Story 2: The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets
8. Series A, Story 3: The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More
9. Series A, Story 4: The 2026 Python Metromap: Control Flow – if, elif, else
10. Series A, Story 5: The 2026 Python Metromap: Loops – for, while, break, continue
11. Series A, Story 6: The 2026 Python Metromap: Nested Logic – Conditions Inside Loops

**Next Story:** Series A, Story 7: The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users

---

## 📝 Your Invitation

You've mastered nested logic. Now build something with what you've learned:

1. **Build a product search engine** – Create a multi-condition filter with categories, price ranges, ratings, and stock status.

2. **Create a Sudoku validator** – Implement row, column, and box validation. Add error highlighting.

3. **Build a grade analyzer** – Process grades for multiple classes. Calculate statistics and identify at-risk students.

4. **Create a matrix processor** – Implement matrix addition, multiplication, and transposition using nested loops.

5. **Build a validation system** – Validate complex nested data structures with multiple business rules.

**You've mastered nested logic. Next stop: Input/Output & Type Casting!**

---

*Found this helpful? Clap, comment, and share what you built with nested logic. Next stop: Input/Output & Type Casting!* 🚇