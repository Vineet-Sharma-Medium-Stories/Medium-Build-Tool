# The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful

## Series B: Functions & Modules Yard | Story 4 of 6

![The 2026 Python Metromap/images/Lambda Functions – Anonymous and Powerful](images/Lambda Functions – Anonymous and Powerful.png)

## 📖 Introduction

**Welcome to the fourth stop on the Functions & Modules Yard Line.**

You've mastered defining functions with `def`, passing arguments in multiple ways, and returning structured results. But sometimes you need a function that's so small and specific that giving it a name feels like overkill. Sometimes you need a function that exists only for a single operation—like sorting a list by a specific key, filtering a collection, or transforming data on the fly.

That's where lambda functions come in.

Lambda functions are anonymous, single-expression functions. They're defined with the `lambda` keyword, take any number of arguments, and return the result of a single expression. They're perfect for short, throwaway functions that you use once and never need again—especially as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

This story—**The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful**—is your guide to writing and using lambda functions effectively. We'll master sorting with custom keys—sorting products by price, users by name, or orders by date. We'll use `map()` and `filter()` for data transformation pipelines. We'll build a complete data processing pipeline that cleans, transforms, and analyzes data. And we'll create a dynamic query builder that uses lambdas for flexible filtering.

**Let's get anonymous.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories) – COMPLETED

- 🔧 **Variables & Data Types** – Integers, floats, strings, booleans; storing customer orders.
- 🏗️ **Collections** – Lists, tuples, dicts, sets; shopping carts, user profiles.
- 📦 **Operators** – Arithmetic, comparison, logical; discount engine, loan approval.
- 🚦 **Control Flow** – if, elif, else; grade calculator, shipping estimator.
- 🔁 **Loops** – for, while, break, continue; batch processor, retry mechanism.
- 🧩 **Nested Logic** – Conditions inside loops; Sudoku validator, grade matrix.
- 📥📤 **Input/Output & Type Casting** – CLI calculator, registration form, quiz system, POS terminal.

### Series B: Functions & Modules Yard (6 Stories)

- 🔧 **The 2026 Python Metromap: Defining Functions – The Workhorses of Python** – Payment processing module; validation functions; error handling.

- 📋 **The 2026 Python Metromap: Arguments – Positional, Keyword, and Default** – Flexible report generator for PDF, CSV, and JSON outputs.

- 📤 **The 2026 Python Metromap: Return Values – Getting Results Back** – API response formatter; standardized success and error responses.

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines. **⬅️ YOU ARE HERE**

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver. 🔜 *Up Next*

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## ⚡ Section 1: Lambda Function Basics

Lambda functions are anonymous, single-expression functions defined with the `lambda` keyword.

**SOLID Principle Applied: Single Responsibility** – Lambdas are ideal for simple, single-purpose operations.

**Design Pattern: Strategy Pattern** – Lambdas provide lightweight strategy implementations.

```python
"""
LAMBDA FUNCTION BASICS

This section covers the fundamentals of lambda functions.

SOLID Principle: Single Responsibility
- Lambdas are ideal for simple, single-purpose operations

Design Pattern: Strategy Pattern
- Lambdas provide lightweight strategy implementations
"""

from typing import List, Dict, Any, Callable, Tuple
import math


def demonstrate_lambda_basics():
    """
    Demonstrates basic lambda function syntax and usage.
    
    Lambda functions are defined with the 'lambda' keyword,
    followed by parameters, a colon, and an expression.
    """
    print("=" * 60)
    print("SECTION 1A: LAMBDA FUNCTION BASICS")
    print("=" * 60)
    
    # BASIC LAMBDA SYNTAX
    print("\n1. BASIC LAMBDA SYNTAX")
    print("-" * 40)
    
    # Traditional function
    def add_traditional(a, b):
        return a + b
    
    # Lambda equivalent
    add_lambda = lambda a, b: a + b
    
    print(f"  Traditional: add_traditional(5, 3) = {add_traditional(5, 3)}")
    print(f"  Lambda: add_lambda(5, 3) = {add_lambda(5, 3)}")
    
    # SINGLE PARAMETER LAMBDA
    print("\n2. SINGLE PARAMETER LAMBDA")
    print("-" * 40)
    
    square = lambda x: x ** 2
    cube = lambda x: x ** 3
    is_even = lambda x: x % 2 == 0
    
    print(f"  square(5) = {square(5)}")
    print(f"  cube(5) = {cube(5)}")
    print(f"  is_even(5) = {is_even(5)}")
    print(f"  is_even(4) = {is_even(4)}")
    
    # MULTIPLE PARAMETERS
    print("\n3. MULTIPLE PARAMETERS")
    print("-" * 40)
    
    multiply = lambda x, y: x * y
    power = lambda base, exp: base ** exp
    max_of_three = lambda a, b, c: max(a, b, c)
    
    print(f"  multiply(6, 7) = {multiply(6, 7)}")
    print(f"  power(2, 10) = {power(2, 10)}")
    print(f"  max_of_three(10, 25, 15) = {max_of_three(10, 25, 15)}")
    
    # NO PARAMETERS
    print("\n4. NO PARAMETERS")
    print("-" * 40)
    
    greet = lambda: "Hello, World!"
    pi = lambda: 3.14159
    
    print(f"  greet() = {greet()}")
    print(f"  pi() = {pi()}")
    
    # LAMBDA WITH CONDITIONAL (ternary operator)
    print("\n5. LAMBDA WITH CONDITIONAL EXPRESSION")
    print("-" * 40)
    
    abs_value = lambda x: x if x >= 0 else -x
    sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
    
    print(f"  abs_value(-5) = {abs_value(-5)}")
    print(f"  abs_value(5) = {abs_value(5)}")
    print(f"  sign(-10) = {sign(-10)}")
    print(f"  sign(0) = {sign(0)}")
    print(f"  sign(10) = {sign(10)}")
    
    # LAMBDA WITH MULTIPLE EXPRESSIONS? (Not directly supported)
    print("\n6. LAMBDA LIMITATIONS")
    print("-" * 40)
    
    print("  ⚠️ Lambda functions can only contain a SINGLE expression")
    print("  ⚠️ No statements (assignment, print, return, etc.)")
    print("  ⚠️ No multiple lines")
    print("  ⚠️ No annotations (type hints)")
    
    # This would cause SyntaxError:
    # bad_lambda = lambda x: x = x + 1; return x
    
    # Workaround: Use tuple for multiple operations
    multi_operation = lambda x: (x + 1, x * 2, x ** 2)
    print(f"  Workaround using tuple: multi_operation(5) = {multi_operation(5)}")


def demonstrate_lambda_vs_regular():
    """
    Compares lambda functions with regular functions.
    
    Shows when to use each and their trade-offs.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: LAMBDA VS REGULAR FUNCTIONS")
    print("=" * 60)
    
    # WHEN LAMBDAS ARE APPROPRIATE
    print("\n1. WHEN TO USE LAMBDAS")
    print("-" * 40)
    
    print("  ✓ Simple operations (single expression)")
    print("  ✓ Used as arguments to higher-order functions")
    print("  ✓ Short-lived, one-time use functions")
    print("  ✓ When naming would add unnecessary verbosity")
    
    # Examples of appropriate lambda use
    numbers = [1, 2, 3, 4, 5]
    
    # Good use: simple transformation
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"  map(lambda x: x * 2, {numbers}) = {doubled}")
    
    # Good use: simple filtering
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  filter(lambda x: x % 2 == 0, {numbers}) = {evens}")
    
    # Good use: simple sorting key
    words = ["apple", "banana", "cherry", "date"]
    sorted_by_len = sorted(words, key=lambda w: len(w))
    print(f"  sorted({words}, key=lambda w: len(w)) = {sorted_by_len}")
    
    # WHEN REGULAR FUNCTIONS ARE BETTER
    print("\n2. WHEN TO USE REGULAR FUNCTIONS")
    print("-" * 40)
    
    print("  ✓ Complex logic (multiple statements)")
    print("  ✓ Functions with side effects (print, file I/O)")
    print("  ✓ Functions called multiple times with same logic")
    print("  ✓ When readability would suffer")
    print("  ✓ When you need documentation/docstrings")
    
    # Bad lambda (hard to read)
    bad_lambda = lambda x: (x[0] * x[1] if x[0] > 0 else -x[0] * x[1]) if x[1] != 0 else 0
    
    # Good regular function (readable)
    def calculate_product(pair):
        """Calculate product of two numbers with sign handling."""
        a, b = pair
        if b == 0:
            return 0
        if a > 0:
            return a * b
        return -a * b
    
    print(f"  Bad lambda: hard to understand at a glance")
    print(f"  Good function: clear name, docstring, readable logic")
    
    # READABILITY COMPARISON
    print("\n3. READABILITY COMPARISON")
    print("-" * 40)
    
    # Hard to read
    result1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
    
    # Easier to read with regular functions
    def is_even(x): return x % 2 == 0
    def square(x): return x ** 2
    
    result2 = list(map(square, filter(is_even, range(10))))
    
    # Most readable with list comprehension
    result3 = [x ** 2 for x in range(10) if x % 2 == 0]
    
    print(f"  Lambda chain: {result1}")
    print(f"  Named functions: {result2}")
    print(f"  List comprehension: {result3} (most readable)")
    
    # CAPTURING VARIABLES
    print("\n4. CAPTURING VARIABLES (Closures)")
    print("-" * 40)
    
    def make_multiplier(n):
        """Return a function that multiplies by n."""
        return lambda x: x * n
    
    double = make_multiplier(2)
    triple = make_multiplier(3)
    
    print(f"  double(5) = {double(5)}")
    print(f"  triple(5) = {triple(5)}")
    
    # LAMBDA IN LOOPS (Common Pitfall)
    print("\n5. ⚠️ LAMBDA IN LOOPS - BE CAREFUL!")
    print("-" * 40)
    
    # This creates lambdas that all capture the same variable
    multipliers = []
    for i in range(3):
        multipliers.append(lambda x: x * i)
    
    print("  Creating lambdas in a loop without default argument:")
    for m in multipliers:
        print(f"    multiplier(5) = {m(5)}")  # All use i=2!
    
    # Fix: Capture current value using default argument
    multipliers_fixed = []
    for i in range(3):
        multipliers_fixed.append(lambda x, i=i: x * i)
    
    print("\n  Fixed with default argument capture:")
    for m in multipliers_fixed:
        print(f"    multiplier(5) = {m(5)}")


def demonstrate_lambda_methods():
    """
    Demonstrates common methods that work with lambda functions.
    
    Lambda functions work with any function that expects a callable.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: LAMBDA WITH BUILT-IN FUNCTIONS")
    print("=" * 60)
    
    # LAMBDA WITH SORTED()
    print("\n1. LAMBDA WITH sorted()")
    print("-" * 40)
    
    products = [
        {"name": "Laptop", "price": 999, "rating": 4.5},
        {"name": "Mouse", "price": 25, "rating": 4.2},
        {"name": "Keyboard", "price": 75, "rating": 4.7},
        {"name": "Monitor", "price": 299, "rating": 4.4},
        {"name": "USB Cable", "price": 10, "rating": 4.0}
    ]
    
    # Sort by price
    by_price = sorted(products, key=lambda p: p["price"])
    print("  Sorted by price (ascending):")
    for p in by_price[:3]:
        print(f"    {p['name']}: ${p['price']}")
    
    # Sort by rating (descending)
    by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)
    print("\n  Sorted by rating (descending):")
    for p in by_rating[:3]:
        print(f"    {p['name']}: {p['rating']}★")
    
    # Sort by multiple criteria (price then rating)
    by_price_then_rating = sorted(products, key=lambda p: (p["price"], p["rating"]))
    print("\n  Sorted by price, then rating:")
    for p in by_price_then_rating:
        print(f"    {p['name']}: ${p['price']}, {p['rating']}★")
    
    # LAMBDA WITH max() AND min()
    print("\n2. LAMBDA WITH max() AND min()")
    print("-" * 40)
    
    most_expensive = max(products, key=lambda p: p["price"])
    highest_rated = max(products, key=lambda p: p["rating"])
    cheapest = min(products, key=lambda p: p["price"])
    
    print(f"  Most expensive: {most_expensive['name']} (${most_expensive['price']})")
    print(f"  Highest rated: {highest_rated['name']} ({highest_rated['rating']}★)")
    print(f"  Cheapest: {cheapest['name']} (${cheapest['price']})")
    
    # LAMBDA WITH map()
    print("\n3. LAMBDA WITH map()")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5]
    
    squares = list(map(lambda x: x ** 2, numbers))
    cubes = list(map(lambda x: x ** 3, numbers))
    add_one = list(map(lambda x: x + 1, numbers))
    
    print(f"  numbers: {numbers}")
    print(f"  squares: {squares}")
    print(f"  cubes: {cubes}")
    print(f"  add_one: {add_one}")
    
    # LAMBDA WITH filter()
    print("\n4. LAMBDA WITH filter()")
    print("-" * 40)
    
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 == 1, numbers))
    greater_than_three = list(filter(lambda x: x > 3, numbers))
    
    print(f"  numbers: {numbers}")
    print(f"  evens: {evens}")
    print(f"  odds: {odds}")
    print(f"  greater than 3: {greater_than_three}")
    
    # LAMBDA WITH reduce()
    print("\n5. LAMBDA WITH reduce()")
    print("-" * 40)
    
    from functools import reduce
    
    product = reduce(lambda a, b: a * b, numbers)
    sum_of_squares = reduce(lambda a, b: a + b ** 2, numbers, 0)
    max_value = reduce(lambda a, b: a if a > b else b, numbers)
    
    print(f"  product of {numbers} = {product}")
    print(f"  sum of squares of {numbers} = {sum_of_squares}")
    print(f"  max of {numbers} = {max_value}")
    
    # CHAINING map AND filter
    print("\n6. CHAINING map() AND filter()")
    print("-" * 40)
    
    # Square of even numbers
    result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
    print(f"  Squares of evens 0-9: {result}")
    
    # Same with list comprehension (more readable)
    result_comp = [x ** 2 for x in range(10) if x % 2 == 0]
    print(f"  Same with comprehension: {result_comp}")
    
    # Complex pipeline: filter, transform, then aggregate
    data = [10, 25, 30, 45, 50, 65, 70, 85, 90]
    
    # Get average of numbers > 50, doubled
    filtered = filter(lambda x: x > 50, data)
    doubled = map(lambda x: x * 2, filtered)
    average = reduce(lambda a, b: a + b, doubled, 0) / len(list(filter(lambda x: x > 50, data)))
    
    print(f"  Average of numbers > 50, doubled: {average:.1f}")


if __name__ == "__main__":
    demonstrate_lambda_basics()
    demonstrate_lambda_vs_regular()
    demonstrate_lambda_methods()
```

---

## 🔧 Section 2: Sorting with Custom Keys

Lambda functions are perfect for providing custom sort keys to the `sorted()` function.

**SOLID Principle Applied: Open/Closed** – Sorting behavior can be customized without modifying the data structure.

**Design Pattern: Strategy Pattern** – The key function is a sorting strategy.

```python
"""
SORTING WITH CUSTOM KEYS

This section demonstrates using lambda functions for custom sorting.

SOLID Principle: Open/Closed
- Sorting behavior can be customized without modifying data

Design Pattern: Strategy Pattern
- Key function is a sorting strategy
"""

from typing import List, Dict, Any, Tuple
from datetime import datetime
import math


def demonstrate_basic_sorting():
    """
    Demonstrates basic sorting with lambda key functions.
    """
    print("=" * 60)
    print("SECTION 2A: BASIC SORTING WITH LAMBDAS")
    print("=" * 60)
    
    # SORTING NUMBERS WITH CUSTOM LOGIC
    print("\n1. SORTING NUMBERS")
    print("-" * 40)
    
    numbers = [10, -5, 3, -8, 7, -2, 1]
    
    # Sort by absolute value
    by_abs = sorted(numbers, key=lambda x: abs(x))
    print(f"  Original: {numbers}")
    print(f"  By absolute value: {by_abs}")
    
    # Sort by distance from zero
    by_distance = sorted(numbers, key=lambda x: abs(x - 0))
    print(f"  By distance from zero: {by_distance}")
    
    # Sort by value modulo
    by_mod = sorted(numbers, key=lambda x: x % 5)
    print(f"  By modulo 5: {by_mod}")
    
    # SORTING STRINGS
    print("\n2. SORTING STRINGS")
    print("-" * 40)
    
    words = ["apple", "Banana", "cherry", "Date", "elderberry"]
    
    # Case-insensitive sort
    case_insensitive = sorted(words, key=lambda s: s.lower())
    print(f"  Original: {words}")
    print(f"  Case-insensitive: {case_insensitive}")
    
    # Sort by length
    by_length = sorted(words, key=lambda s: len(s))
    print(f"  By length: {by_length}")
    
    # Sort by last character
    by_last_char = sorted(words, key=lambda s: s[-1])
    print(f"  By last character: {by_last_char}")
    
    # Sort by vowel count
    def vowel_count(s):
        return sum(1 for c in s.lower() if c in "aeiou")
    
    by_vowels = sorted(words, key=lambda s: vowel_count(s))
    print(f"  By vowel count: {by_vowels}")
    
    # SORTING DICTIONARIES
    print("\n3. SORTING DICTIONARIES")
    print("-" * 40)
    
    users = [
        {"name": "Alice", "age": 28, "score": 95},
        {"name": "Bob", "age": 35, "score": 87},
        {"name": "Charlie", "age": 22, "score": 92},
        {"name": "Diana", "age": 31, "score": 98}
    ]
    
    # Sort by age
    by_age = sorted(users, key=lambda u: u["age"])
    print("  Sorted by age:")
    for u in by_age:
        print(f"    {u['name']}: {u['age']}")
    
    # Sort by score (descending)
    by_score = sorted(users, key=lambda u: u["score"], reverse=True)
    print("\n  Sorted by score (highest first):")
    for u in by_score:
        print(f"    {u['name']}: {u['score']}")
    
    # Sort by name length
    by_name_len = sorted(users, key=lambda u: len(u["name"]))
    print("\n  Sorted by name length:")
    for u in by_name_len:
        print(f"    {u['name']}: {len(u['name'])} chars")


def demonstrate_multi_criteria_sorting():
    """
    Demonstrates sorting by multiple criteria using tuple keys.
    
    Lambda returns a tuple for primary, secondary, etc. sorting.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: MULTI-CRITERIA SORTING")
    print("=" * 60)
    
    # SORTING BY MULTIPLE FIELDS
    print("\n1. SORTING BY MULTIPLE FIELDS")
    print("-" * 40)
    
    students = [
        {"name": "Alice", "grade": "A", "score": 95},
        {"name": "Bob", "grade": "B", "score": 85},
        {"name": "Charlie", "grade": "A", "score": 92},
        {"name": "Diana", "grade": "B", "score": 88},
        {"name": "Eve", "grade": "A", "score": 98}
    ]
    
    # Sort by grade (A first), then by score (highest first)
    sorted_students = sorted(
        students,
        key=lambda s: (s["grade"], -s["score"])  # Negative for descending
    )
    
    print("  Sorted by grade (A first), then score (highest first):")
    for s in sorted_students:
        print(f"    {s['name']}: {s['grade']} ({s['score']})")
    
    # SORTING PRODUCTS
    print("\n2. SORTING PRODUCTS")
    print("-" * 40)
    
    products = [
        {"name": "Laptop", "category": "Electronics", "price": 999, "rating": 4.5},
        {"name": "Mouse", "category": "Electronics", "price": 25, "rating": 4.2},
        {"name": "Desk", "category": "Furniture", "price": 299, "rating": 4.3},
        {"name": "Chair", "category": "Furniture", "price": 199, "rating": 4.1},
        {"name": "Monitor", "category": "Electronics", "price": 299, "rating": 4.6},
        {"name": "Lamp", "category": "Furniture", "price": 45, "rating": 4.0}
    ]
    
    # Sort by category, then by price (ascending), then by rating (descending)
    sorted_products = sorted(
        products,
        key=lambda p: (p["category"], p["price"], -p["rating"])
    )
    
    print("  Sorted by category, then price (lowest first), then rating (highest first):")
    current_category = None
    for p in sorted_products:
        if p["category"] != current_category:
            print(f"\n    --- {p['category']} ---")
            current_category = p["category"]
        print(f"      {p['name']}: ${p['price']}, {p['rating']}★")
    
    # SORTING WITH CUSTOM TRANSFORMATIONS
    print("\n3. SORTING WITH CUSTOM TRANSFORMATIONS")
    print("-" * 40)
    
    coordinates = [(1, 2), (3, 1), (2, 3), (0, 0), (4, 5)]
    
    # Sort by Euclidean distance from origin
    by_distance = sorted(coordinates, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
    print(f"  Coordinates: {coordinates}")
    print(f"  By distance from origin: {by_distance}")
    
    # Sort by Manhattan distance
    by_manhattan = sorted(coordinates, key=lambda p: abs(p[0]) + abs(p[1]))
    print(f"  By Manhattan distance: {by_manhattan}")
    
    # Sort by x then y
    by_xy = sorted(coordinates, key=lambda p: (p[0], p[1]))
    print(f"  By x then y: {by_xy}")


def demonstrate_advanced_sorting():
    """
    Demonstrates advanced sorting techniques with lambda functions.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: ADVANCED SORTING TECHNIQUES")
    print("=" * 60)
    
    # SORTING WITH CUSTOM OBJECTS
    print("\n1. SORTING CUSTOM OBJECTS")
    print("-" * 40)
    
    from dataclasses import dataclass
    
    @dataclass
    class Task:
        name: str
        priority: int
        due_date: str
        completed: bool
        
        def __repr__(self):
            return f"{self.name}(P{self.priority})"
    
    tasks = [
        Task("Fix bug", 1, "2024-01-15", False),
        Task("Write docs", 3, "2024-01-10", False),
        Task("Deploy", 1, "2024-01-20", False),
        Task("Review PR", 2, "2024-01-12", True),
        Task("Meeting", 3, "2024-01-08", False)
    ]
    
    # Sort by priority (higher priority first), then by due date
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (t.priority, t.due_date)
    )
    print(f"  Sorted by priority (1 highest), then due date: {sorted_tasks}")
    
    # Sort with completed tasks at the end
    sorted_with_status = sorted(
        tasks,
        key=lambda t: (t.completed, t.priority, t.due_date)
    )
    print(f"  Incomplete tasks first: {sorted_with_status}")
    
    # SORTING WITH NESTED DATA
    print("\n2. SORTING NESTED DATA")
    print("-" * 40)
    
    orders = [
        {"id": 1, "customer": {"name": "Alice", "tier": "gold"}, "total": 299},
        {"id": 2, "customer": {"name": "Bob", "tier": "silver"}, "total": 150},
        {"id": 3, "customer": {"name": "Charlie", "tier": "gold"}, "total": 450},
        {"id": 4, "customer": {"name": "Diana", "tier": "platinum"}, "total": 89}
    ]
    
    # Sort by customer tier (platinum first), then by total (highest first)
    tier_order = {"platinum": 1, "gold": 2, "silver": 3, "bronze": 4}
    
    sorted_orders = sorted(
        orders,
        key=lambda o: (tier_order.get(o["customer"]["tier"], 99), -o["total"])
    )
    
    print("  Sorted by customer tier, then total (highest first):")
    for o in sorted_orders:
        print(f"    {o['customer']['name']} ({o['customer']['tier']}): ${o['total']}")
    
    # PARTIAL SORTING (nlargest, nsmallest)
    print("\n3. PARTIAL SORTING (nlargest, nsmallest)")
    print("-" * 40)
    
    import heapq
    
    numbers = [45, 12, 78, 34, 89, 23, 67, 91, 56]
    
    # Get 3 largest
    largest_3 = heapq.nlargest(3, numbers)
    smallest_3 = heapq.nsmallest(3, numbers)
    
    print(f"  Numbers: {numbers}")
    print(f"  3 largest: {largest_3}")
    print(f"  3 smallest: {smallest_3}")
    
    # With key function
    products = [
        {"name": "Laptop", "price": 999},
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 75},
        {"name": "Monitor", "price": 299},
        {"name": "Desk", "price": 399}
    ]
    
    most_expensive_2 = heapq.nlargest(2, products, key=lambda p: p["price"])
    print(f"\n  2 most expensive products:")
    for p in most_expensive_2:
        print(f"    {p['name']}: ${p['price']}")
    
    # STABLE SORTING
    print("\n4. STABLE SORTING (preserves order for equal keys)")
    print("-" * 40)
    
    data = [
        ("Alice", 25, "Engineer"),
        ("Bob", 30, "Designer"),
        ("Charlie", 25, "Manager"),
        ("Diana", 30, "Engineer"),
        ("Eve", 25, "Designer")
    ]
    
    # Sort by age (stable: original order preserved within same age)
    by_age = sorted(data, key=lambda x: x[1])
    print("  Sorted by age (stable):")
    for item in by_age:
        print(f"    {item}")
    
    # Sort by age, then by job (using tuple key)
    by_age_job = sorted(data, key=lambda x: (x[1], x[2]))
    print("\n  Sorted by age, then job:")
    for item in by_age_job:
        print(f"    {item}")


if __name__ == "__main__":
    demonstrate_basic_sorting()
    demonstrate_multi_criteria_sorting()
    demonstrate_advanced_sorting()
```

---

## 🔄 Section 3: Data Transformation Pipelines

Lambda functions with `map()` and `filter()` create powerful data transformation pipelines.

**SOLID Principle Applied: Single Responsibility** – Each transformation step does one thing.

**Design Pattern: Pipeline Pattern** – Data flows through transformation stages.

```python
"""
DATA TRANSFORMATION PIPELINES

This section demonstrates building data pipelines with map and filter.

SOLID Principle: Single Responsibility
- Each transformation step does one thing

Design Pattern: Pipeline Pattern
- Data flows through transformation stages
"""

from typing import List, Dict, Any, Callable, Tuple, Optional
from functools import reduce
import re


def demonstrate_map_pipelines():
    """
    Demonstrates building pipelines with map() for transformations.
    """
    print("=" * 60)
    print("SECTION 3A: MAP PIPELINES")
    print("=" * 60)
    
    # BASIC MAP TRANSFORMATIONS
    print("\n1. BASIC MAP TRANSFORMATIONS")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5]
    
    # Multiple transformations
    doubled = list(map(lambda x: x * 2, numbers))
    squared = list(map(lambda x: x ** 2, numbers))
    stringified = list(map(lambda x: f"Number: {x}", numbers))
    
    print(f"  Original: {numbers}")
    print(f"  Doubled: {doubled}")
    print(f"  Squared: {squared}")
    print(f"  Stringified: {stringified}")
    
    # CHAINING MAP OPERATIONS
    print("\n2. CHAINING MAP OPERATIONS")
    print("-" * 40)
    
    # Chain: double → add 10 → square
    result = list(
        map(lambda x: x ** 2,
            map(lambda x: x + 10,
                map(lambda x: x * 2, numbers)
            )
        )
    )
    print(f"  Chain: double → add 10 → square")
    print(f"  Result: {result}")
    
    # Using composition (cleaner)
    def compose(*functions):
        """Compose multiple functions right to left."""
        def composed(x):
            for f in reversed(functions):
                x = f(x)
            return x
        return composed
    
    double = lambda x: x * 2
    add_ten = lambda x: x + 10
    square = lambda x: x ** 2
    
    transform = compose(square, add_ten, double)
    result = list(map(transform, numbers))
    print(f"  Using function composition: {result}")
    
    # TRANSFORMING DICTIONARIES
    print("\n3. TRANSFORMING DICTIONARIES")
    print("-" * 40)
    
    users = [
        {"name": "alice", "age": 28, "email": "ALICE@EXAMPLE.COM"},
        {"name": "bob", "age": 35, "email": "BOB@EXAMPLE.COM"},
        {"name": "charlie", "age": 22, "email": "CHARLIE@EXAMPLE.COM"}
    ]
    
    # Standardize user data
    standardized = list(map(
        lambda u: {
            "name": u["name"].capitalize(),
            "age": u["age"],
            "email": u["email"].lower()
        },
        users
    ))
    
    print("  Standardized users:")
    for u in standardized:
        print(f"    {u}")
    
    # Add computed fields
    with_computed = list(map(
        lambda u: {
            **u,
            "is_adult": u["age"] >= 18,
            "age_group": "senior" if u["age"] >= 65 else "adult" if u["age"] >= 18 else "minor"
        },
        standardized
    ))
    
    print("\n  With computed fields:")
    for u in with_computed:
        print(f"    {u['name']}: {u['age']} ({u['age_group']})")
    
    # TRANSFORMING STRINGS
    print("\n4. TRANSFORMING STRINGS")
    print("-" * 40)
    
    texts = [
        "  Hello World  ",
        "PYTHON PROGRAMMING",
        "data science 101",
        "  clean me up  "
    ]
    
    # Clean and normalize text
    cleaned = list(map(
        lambda s: s.strip().lower().replace(" ", "_"),
        texts
    ))
    print(f"  Original: {texts}")
    print(f"  Cleaned: {cleaned}")


def demonstrate_filter_pipelines():
    """
    Demonstrates building pipelines with filter() for filtering.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: FILTER PIPELINES")
    print("=" * 60)
    
    # BASIC FILTERING
    print("\n1. BASIC FILTERING")
    print("-" * 40)
    
    numbers = list(range(20))
    
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 == 1, numbers))
    primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))
    
    print(f"  Numbers: {numbers}")
    print(f"  Evens: {evens}")
    print(f"  Odds: {odds}")
    print(f"  Primes: {primes}")
    
    # FILTERING DICTIONARIES
    print("\n2. FILTERING DICTIONARIES")
    print("-" * 40)
    
    products = [
        {"name": "Laptop", "price": 999, "in_stock": True, "category": "Electronics"},
        {"name": "Mouse", "price": 25, "in_stock": True, "category": "Electronics"},
        {"name": "Keyboard", "price": 75, "in_stock": False, "category": "Electronics"},
        {"name": "Desk", "price": 299, "in_stock": True, "category": "Furniture"},
        {"name": "Chair", "price": 199, "in_stock": False, "category": "Furniture"}
    ]
    
    # In stock products
    in_stock = list(filter(lambda p: p["in_stock"], products))
    print("  In stock products:")
    for p in in_stock:
        print(f"    {p['name']} (${p['price']})")
    
    # Electronics under $100
    cheap_electronics = list(filter(
        lambda p: p["category"] == "Electronics" and p["price"] < 100,
        products
    ))
    print("\n  Electronics under $100:")
    for p in cheap_electronics:
        print(f"    {p['name']} (${p['price']})")
    
    # COMBINING FILTER AND MAP
    print("\n3. COMBINING FILTER AND MAP")
    print("-" * 40)
    
    # Get names of in-stock electronics
    result = list(map(
        lambda p: p["name"],
        filter(lambda p: p["category"] == "Electronics" and p["in_stock"], products)
    ))
    print(f"  In-stock electronics: {result}")
    
    # Get total value of in-stock products
    total_value = sum(map(
        lambda p: p["price"],
        filter(lambda p: p["in_stock"], products)
    ))
    print(f"  Total value of in-stock products: ${total_value}")
    
    # FILTERING STRINGS
    print("\n4. FILTERING STRINGS")
    print("-" * 40)
    
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    
    # Words longer than 5 letters
    long_words = list(filter(lambda w: len(w) > 5, words))
    print(f"  Words > 5 chars: {long_words}")
    
    # Words starting with vowel
    vowel_words = list(filter(lambda w: w[0] in "aeiou", words))
    print(f"  Words starting with vowel: {vowel_words}")
    
    # Words containing 'e'
    has_e = list(filter(lambda w: 'e' in w, words))
    print(f"  Words containing 'e': {has_e}")


def demonstrate_pipeline_chaining():
    """
    Demonstrates chaining multiple operations in a pipeline.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: PIPELINE CHAINING")
    print("=" * 60)
    
    # COMPLEX DATA PIPELINE
    print("\n1. COMPLEX DATA PROCESSING PIPELINE")
    print("-" * 40)
    
    sales_data = [
        {"date": "2024-01-01", "product": "Laptop", "quantity": 2, "price": 999, "region": "North"},
        {"date": "2024-01-02", "product": "Mouse", "quantity": 5, "price": 25, "region": "South"},
        {"date": "2024-01-03", "product": "Laptop", "quantity": 1, "price": 999, "region": "East"},
        {"date": "2024-01-04", "product": "Keyboard", "quantity": 3, "price": 75, "region": "West"},
        {"date": "2024-01-05", "product": "Mouse", "quantity": 10, "price": 25, "region": "North"},
        {"date": "2024-01-06", "product": "Monitor", "quantity": 2, "price": 299, "region": "South"},
        {"date": "2024-01-07", "product": "Laptop", "quantity": 1, "price": 999, "region": "West"}
    ]
    
    # Pipeline: filter laptops → calculate revenue → sort by revenue
    laptop_revenue = sorted(
        map(
            lambda s: {"product": s["product"], "revenue": s["quantity"] * s["price"]},
            filter(lambda s: s["product"] == "Laptop", sales_data)
        ),
        key=lambda x: x["revenue"],
        reverse=True
    )
    
    print("  Laptop sales by revenue (highest first):")
    for sale in laptop_revenue:
        print(f"    {sale['product']}: ${sale['revenue']}")
    
    # REGION SALES SUMMARY
    print("\n2. REGION SALES SUMMARY")
    print("-" * 40)
    
    regions = set(map(lambda s: s["region"], sales_data))
    
    for region in regions:
        region_sales = list(filter(lambda s: s["region"] == region, sales_data))
        total_revenue = sum(map(lambda s: s["quantity"] * s["price"], region_sales))
        total_units = sum(map(lambda s: s["quantity"], region_sales))
        print(f"  {region}: {total_units} units, ${total_revenue:,.2f}")
    
    # TOP PRODUCTS
    print("\n3. TOP PRODUCTS")
    print("-" * 40)
    
    products = set(map(lambda s: s["product"], sales_data))
    product_sales = []
    
    for product in products:
        product_data = list(filter(lambda s: s["product"] == product, sales_data))
        total_units = sum(map(lambda s: s["quantity"], product_data))
        total_revenue = sum(map(lambda s: s["quantity"] * s["price"], product_data))
        product_sales.append({"product": product, "units": total_units, "revenue": total_revenue})
    
    top_by_units = sorted(product_sales, key=lambda p: p["units"], reverse=True)
    top_by_revenue = sorted(product_sales, key=lambda p: p["revenue"], reverse=True)
    
    print("  Top by units sold:")
    for p in top_by_units:
        print(f"    {p['product']}: {p['units']} units")
    
    print("\n  Top by revenue:")
    for p in top_by_revenue:
        print(f"    {p['product']}: ${p['revenue']:,.2f}")
    
    # USING REDUCE FOR AGGREGATION
    print("\n4. USING REDUCE FOR AGGREGATION")
    print("-" * 40)
    
    from functools import reduce
    
    # Total revenue across all sales
    total_revenue = reduce(
        lambda acc, sale: acc + sale["quantity"] * sale["price"],
        sales_data,
        0
    )
    print(f"  Total revenue: ${total_revenue:,.2f}")
    
    # Count sales per product
    def count_by_product(acc, sale):
        product = sale["product"]
        acc[product] = acc.get(product, 0) + 1
        return acc
    
    sales_count = reduce(count_by_product, sales_data, {})
    print(f"  Sales count per product: {sales_count}")
    
    # Build pipeline class for reusable operations
    print("\n5. REUSABLE PIPELINE CLASS")
    print("-" * 40)
    
    class Pipeline:
        """Simple pipeline for data transformation."""
        
        def __init__(self, data):
            self.data = data
        
        def filter(self, predicate):
            """Filter data using predicate."""
            self.data = list(filter(predicate, self.data))
            return self
        
        def map(self, transform):
            """Transform data using function."""
            self.data = list(map(transform, self.data))
            return self
        
        def reduce(self, func, initial=None):
            """Reduce data using function."""
            if initial is not None:
                return reduce(func, self.data, initial)
            return reduce(func, self.data)
        
        def collect(self):
            """Return the current data."""
            return self.data
    
    # Use pipeline
    result = (Pipeline(sales_data)
              .filter(lambda s: s["region"] == "North")
              .map(lambda s: s["product"])
              .collect())
    
    print(f"  Products sold in North region: {result}")
    
    # Pipeline with multiple operations
    north_revenue = (Pipeline(sales_data)
                     .filter(lambda s: s["region"] == "North")
                     .map(lambda s: s["quantity"] * s["price"])
                     .reduce(lambda a, b: a + b, 0))
    
    print(f"  Total revenue from North region: ${north_revenue:,.2f}")


if __name__ == "__main__":
    demonstrate_map_pipelines()
    demonstrate_filter_pipelines()
    demonstrate_pipeline_chaining()
```

---

## 🏭 Section 4: Dynamic Query Builder

A complete dynamic query builder that uses lambda functions for flexible filtering and transformation.

**SOLID Principles Applied:**
- Single Responsibility: Each query component has one purpose
- Open/Closed: New query operations can be added

**Design Patterns:**
- Builder Pattern: Builds queries incrementally
- Specification Pattern: Lambda functions as specifications
- Fluent Interface: Method chaining for readability

```python
"""
DYNAMIC QUERY BUILDER

This section builds a complete dynamic query builder using lambda functions.

SOLID Principles Applied:
- Single Responsibility: Each query component has one purpose
- Open/Closed: New operations can be added

Design Patterns:
- Builder Pattern: Builds queries incrementally
- Specification Pattern: Lambdas as specifications
- Fluent Interface: Method chaining for readability
"""

from typing import List, Dict, Any, Callable, Optional, Union, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import re


class Query:
    """
    Dynamic query builder for collections.
    
    Design Pattern: Fluent Interface - Method chaining
    """
    
    def __init__(self, data: List[Dict]):
        self._original_data = data
        self._filtered_data = data.copy()
        self._transformations = []
        self._aggregations = []
    
    def where(self, predicate: Callable[[Dict], bool]) -> 'Query':
        """
        Filter data using predicate.
        
        Args:
            predicate: Function that returns True for items to keep
            
        Returns:
            Self for method chaining
        """
        self._filtered_data = [item for item in self._filtered_data if predicate(item)]
        return self
    
    def select(self, *fields: str) -> 'Query':
        """
        Select specific fields from each item.
        
        Args:
            fields: Field names to select
            
        Returns:
            Self for method chaining
        """
        self._filtered_data = [
            {field: item.get(field) for field in fields}
            for item in self._filtered_data
        ]
        return self
    
    def map(self, transform: Callable[[Dict], Any]) -> 'Query':
        """
        Transform each item using a function.
        
        Args:
            transform: Transformation function
            
        Returns:
            Self for method chaining
        """
        self._filtered_data = [transform(item) for item in self._filtered_data]
        return self
    
    def order_by(self, key_func: Callable[[Dict], Any], reverse: bool = False) -> 'Query':
        """
        Sort data by key function.
        
        Args:
            key_func: Function to extract sort key
            reverse: Sort in reverse order
            
        Returns:
            Self for method chaining
        """
        self._filtered_data = sorted(self._filtered_data, key=key_func, reverse=reverse)
        return self
    
    def limit(self, n: int) -> 'Query':
        """
        Limit results to n items.
        
        Args:
            n: Maximum number of items
            
        Returns:
            Self for method chaining
        """
        self._filtered_data = self._filtered_data[:n]
        return self
    
    def offset(self, n: int) -> 'Query':
        """
        Skip first n items.
        
        Args:
            n: Number of items to skip
            
        Returns:
            Self for method chaining
        """
        self._filtered_data = self._filtered_data[n:]
        return self
    
    def distinct(self, key_func: Optional[Callable] = None) -> 'Query':
        """
        Get distinct items.
        
        Args:
            key_func: Function to determine uniqueness
            
        Returns:
            Self for method chaining
        """
        if key_func:
            seen = set()
            unique = []
            for item in self._filtered_data:
                key = key_func(item)
                if key not in seen:
                    seen.add(key)
                    unique.append(item)
            self._filtered_data = unique
        else:
            # For simple values, use set
            self._filtered_data = list(set(self._filtered_data))
        return self
    
    def aggregate(self, aggregations: Dict[str, Callable]) -> Dict[str, Any]:
        """
        Perform aggregations on the data.
        
        Args:
            aggregations: Dict of name -> aggregation function
            
        Returns:
            Dictionary of aggregation results
        """
        results = {}
        for name, func in aggregations.items():
            results[name] = func(self._filtered_data)
        return results
    
    def group_by(self, key_func: Callable[[Dict], Any]) -> 'GroupedQuery':
        """
        Group data by key function.
        
        Args:
            key_func: Function to extract group key
            
        Returns:
            GroupedQuery for further aggregation
        """
        groups = {}
        for item in self._filtered_data:
            key = key_func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        return GroupedQuery(groups)
    
    def exists(self) -> bool:
        """Check if any items match the query."""
        return len(self._filtered_data) > 0
    
    def count(self) -> int:
        """Get number of matching items."""
        return len(self._filtered_data)
    
    def first(self) -> Optional[Dict]:
        """Get first matching item."""
        return self._filtered_data[0] if self._filtered_data else None
    
    def last(self) -> Optional[Dict]:
        """Get last matching item."""
        return self._filtered_data[-1] if self._filtered_data else None
    
    def all(self) -> List[Dict]:
        """Get all matching items."""
        return self._filtered_data.copy()
    
    def to_list(self) -> List:
        """Convert to list (after transformations)."""
        return self._filtered_data


class GroupedQuery:
    """Query for grouped data."""
    
    def __init__(self, groups: Dict[Any, List]):
        self.groups = groups
    
    def aggregate(self, aggregations: Dict[str, Callable]) -> Dict[Any, Dict]:
        """
        Apply aggregations to each group.
        
        Args:
            aggregations: Dict of name -> aggregation function
            
        Returns:
            Dictionary of group -> aggregation results
        """
        results = {}
        for key, items in self.groups.items():
            group_result = {}
            for name, func in aggregations.items():
                group_result[name] = func(items)
            results[key] = group_result
        return results
    
    def count(self) -> Dict[Any, int]:
        """Count items in each group."""
        return {key: len(items) for key, items in self.groups.items()}
    
    def keys(self) -> List:
        """Get group keys."""
        return list(self.groups.keys())


class QueryBuilder:
    """
    Factory for creating common query predicates.
    
    Design Pattern: Factory Pattern - Creates predicate functions
    """
    
    @staticmethod
    def equals(field: str, value: Any) -> Callable:
        """Create predicate for exact equality."""
        return lambda item: item.get(field) == value
    
    @staticmethod
    def not_equals(field: str, value: Any) -> Callable:
        """Create predicate for inequality."""
        return lambda item: item.get(field) != value
    
    @staticmethod
    def greater_than(field: str, value: Union[int, float]) -> Callable:
        """Create predicate for greater than."""
        return lambda item: item.get(field, float('-inf')) > value
    
    @staticmethod
    def less_than(field: str, value: Union[int, float]) -> Callable:
        """Create predicate for less than."""
        return lambda item: item.get(field, float('inf')) < value
    
    @staticmethod
    def between(field: str, min_val: Union[int, float], max_val: Union[int, float]) -> Callable:
        """Create predicate for range."""
        return lambda item: min_val <= item.get(field, float('-inf')) <= max_val
    
    @staticmethod
    def contains(field: str, substring: str) -> Callable:
        """Create predicate for substring containment."""
        return lambda item: substring.lower() in str(item.get(field, "")).lower()
    
    @staticmethod
    def starts_with(field: str, prefix: str) -> Callable:
        """Create predicate for string prefix."""
        return lambda item: str(item.get(field, "")).lower().startswith(prefix.lower())
    
    @staticmethod
    def ends_with(field: str, suffix: str) -> Callable:
        """Create predicate for string suffix."""
        return lambda item: str(item.get(field, "")).lower().endswith(suffix.lower())
    
    @staticmethod
    def matches_regex(field: str, pattern: str) -> Callable:
        """Create predicate for regex match."""
        regex = re.compile(pattern, re.IGNORECASE)
        return lambda item: bool(regex.search(str(item.get(field, ""))))
    
    @staticmethod
    def in_list(field: str, values: List) -> Callable:
        """Create predicate for value in list."""
        return lambda item: item.get(field) in values
    
    @staticmethod
    def not_in_list(field: str, values: List) -> Callable:
        """Create predicate for value not in list."""
        return lambda item: item.get(field) not in values
    
    @staticmethod
    def and_(*predicates: Callable) -> Callable:
        """Combine multiple predicates with AND."""
        return lambda item: all(p(item) for p in predicates)
    
    @staticmethod
    def or_(*predicates: Callable) -> Callable:
        """Combine multiple predicates with OR."""
        return lambda item: any(p(item) for p in predicates)
    
    @staticmethod
    def not_(predicate: Callable) -> Callable:
        """Negate a predicate."""
        return lambda item: not predicate(item)


def demonstrate_query_builder():
    """
    Demonstrate the dynamic query builder.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: DYNAMIC QUERY BUILDER")
    print("=" * 60)
    
    # Sample data
    products = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999, "rating": 4.5, "in_stock": True},
        {"id": 2, "name": "Mouse", "category": "Electronics", "price": 25, "rating": 4.2, "in_stock": True},
        {"id": 3, "name": "Keyboard", "category": "Electronics", "price": 75, "rating": 4.7, "in_stock": False},
        {"id": 4, "name": "Monitor", "category": "Electronics", "price": 299, "rating": 4.4, "in_stock": True},
        {"id": 5, "name": "Desk", "category": "Furniture", "price": 399, "rating": 4.3, "in_stock": True},
        {"id": 6, "name": "Chair", "category": "Furniture", "price": 199, "rating": 4.1, "in_stock": False},
        {"id": 7, "name": "Lamp", "category": "Furniture", "price": 45, "rating": 4.0, "in_stock": True},
        {"id": 8, "name": "USB Cable", "category": "Electronics", "price": 10, "rating": 3.9, "in_stock": True}
    ]
    
    qb = QueryBuilder
    
    print("\n1. BASIC QUERIES")
    print("-" * 40)
    
    # Electronics under $100
    result = (Query(products)
              .where(qb.equals("category", "Electronics"))
              .where(qb.less_than("price", 100))
              .select("name", "price")
              .all())
    
    print("  Electronics under $100:")
    for p in result:
        print(f"    {p['name']}: ${p['price']}")
    
    # In-stock products with rating >= 4.5
    result = (Query(products)
              .where(qb.and_(
                  qb.equals("in_stock", True),
                  qb.greater_than("rating", 4.4)
              ))
              .order_by(lambda p: p["rating"], reverse=True)
              .all())
    
    print("\n  In-stock products with rating >= 4.5:")
    for p in result:
        print(f"    {p['name']}: {p['rating']}★, ${p['price']}")
    
    print("\n2. ADVANCED FILTERING")
    print("-" * 40)
    
    # Products with name containing 'e'
    result = (Query(products)
              .where(qb.contains("name", "e"))
              .select("name")
              .all())
    print(f"  Products with 'e' in name: {[p['name'] for p in result]}")
    
    # Products with price between $50 and $300
    result = (Query(products)
              .where(qb.between("price", 50, 300))
              .select("name", "price")
              .order_by(lambda p: p["price"])
              .all())
    
    print("\n  Products between $50 and $300:")
    for p in result:
        print(f"    {p['name']}: ${p['price']}")
    
    print("\n3. PAGINATION")
    print("-" * 40)
    
    # Page 1 of electronics (2 per page)
    page = 1
    per_page = 2
    
    result = (Query(products)
              .where(qb.equals("category", "Electronics"))
              .offset((page - 1) * per_page)
              .limit(per_page)
              .select("name")
              .all())
    
    print(f"  Page {page} of Electronics (limit {per_page}): {[p['name'] for p in result]}")
    
    print("\n4. AGGREGATIONS")
    print("-" * 40)
    
    # Aggregations on electronics
    electronics_query = Query(products).where(qb.equals("category", "Electronics"))
    
    aggregations = {
        "count": len,
        "total_value": lambda items: sum(i["price"] for i in items),
        "avg_price": lambda items: sum(i["price"]) / len(items) if items else 0,
        "min_price": lambda items: min(i["price"] for i in items),
        "max_price": lambda items: max(i["price"] for i in items),
        "avg_rating": lambda items: sum(i["rating"]) / len(items) if items else 0
    }
    
    stats = electronics_query.aggregate(aggregations)
    print("  Electronics statistics:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"    {key}: {value:.2f}")
        else:
            print(f"    {key}: {value}")
    
    print("\n5. GROUP BY")
    print("-" * 40)
    
    # Group by category
    grouped = (Query(products)
               .group_by(lambda p: p["category"]))
    
    # Count per category
    counts = grouped.count()
    print("  Products per category:")
    for category, count in counts.items():
        print(f"    {category}: {count}")
    
    # Aggregations per category
    group_aggregations = {
        "count": len,
        "total_value": lambda items: sum(i["price"] for i in items),
        "avg_price": lambda items: sum(i["price"]) / len(items) if items else 0
    }
    
    category_stats = grouped.aggregate(group_aggregations)
    print("\n  Category statistics:")
    for category, stats in category_stats.items():
        print(f"    {category}: {stats['count']} products, ${stats['total_value']:.0f} total, ${stats['avg_price']:.0f} avg")
    
    print("\n6. COMPLEX QUERIES WITH COMPOSITION")
    print("-" * 40)
    
    # Expensive in-stock electronics OR affordable furniture
    result = (Query(products)
              .where(qb.or_(
                  qb.and_(
                      qb.equals("category", "Electronics"),
                      qb.equals("in_stock", True),
                      qb.greater_than("price", 200)
                  ),
                  qb.and_(
                      qb.equals("category", "Furniture"),
                      qb.less_than("price", 100)
                  )
              ))
              .order_by(lambda p: p["price"])
              .all())
    
    print("  Complex query results:")
    for p in result:
        print(f"    {p['name']} ({p['category']}): ${p['price']}")
    
    print("\n7. TRANSFORMATIONS")
    print("-" * 40)
    
    # Apply 10% discount to all electronics
    discounted = (Query(products)
                  .where(qb.equals("category", "Electronics"))
                  .map(lambda p: {**p, "price": round(p["price"] * 0.9, 2)})
                  .select("name", "price")
                  .all())
    
    print("  Electronics with 10% discount:")
    for p in discounted:
        print(f"    {p['name']}: ${p['price']}")
    
    # Check existence
    has_expensive = (Query(products)
                     .where(qb.greater_than("price", 1000))
                     .exists())
    
    print(f"\n  Has product over $1000: {has_expensive}")


if __name__ == "__main__":
    demonstrate_query_builder()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Lambda Syntax** – `lambda parameters: expression`. Single expression only. No statements.

- **When to Use Lambdas** – Simple operations, function arguments, short-lived functions. Not for complex logic.

- **When Not to Use Lambdas** – Complex logic, multiple statements, functions needing docstrings, repeated use.

- **Sorting with Lambdas** – Custom sort keys with `sorted()`, `max()`, `min()`. Multi-criteria sorting with tuples.

- **Map Pipeline** – Transform data with `map()`. Chain multiple transformations. Use composition for clarity.

- **Filter Pipeline** – Filter data with `filter()`. Combine with `map()` for powerful pipelines.

- **Query Builder** – Dynamic query building with lambda predicates. Fluent interface for readability.

- **SOLID Principles Applied** – Single Responsibility (each lambda does one thing), Open/Closed (new predicates can be added), Dependency Inversion (depends on callable abstraction).

- **Design Patterns Used** – Strategy Pattern (sorting keys), Pipeline Pattern (data transformation), Builder Pattern (query construction), Specification Pattern (predicates), Fluent Interface (method chaining).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Return Values – Getting Results Back

- **📚 Series B Catalog:** Functions & Modules Yard – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Recursion – Functions Calling Themselves (Series B, Story 5)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 4 | 2 | 67% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **16** | **36** | **31%** |

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
12. Series A, Story 7: The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users
13. Series B, Story 1: The 2026 Python Metromap: Defining Functions – The Workhorses of Python
14. Series B, Story 2: The 2026 Python Metromap: Arguments – Positional, Keyword, and Default
15. Series B, Story 3: The 2026 Python Metromap: Return Values – Getting Results Back
16. Series B, Story 4: The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful

**Next Story:** Series B, Story 5: The 2026 Python Metromap: Recursion – Functions Calling Themselves

---

## 📝 Your Invitation

You've mastered lambda functions. Now build something with what you've learned:

1. **Build a sorting utility** – Create functions that sort products by price, rating, name, or custom criteria using lambda keys.

2. **Create a data pipeline** – Build a pipeline that reads CSV data, filters rows, transforms columns, and aggregates results.

3. **Build a query builder** – Add more predicates (is_null, is_empty, before_date, after_date). Add support for OR and NOT combinations.

4. **Create a validation library** – Use lambda functions for custom validation rules. Compose validators with and_/or_.

5. **Build a reporting system** – Use lambda functions for custom aggregations and groupings.

**You've mastered lambda functions. Next stop: Recursion!**

---

*Found this helpful? Clap, comment, and share what you built with lambda functions. Next stop: Recursion!* 🚇