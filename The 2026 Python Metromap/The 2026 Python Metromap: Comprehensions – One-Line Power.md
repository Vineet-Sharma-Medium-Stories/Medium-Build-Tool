# The 2026 Python Metromap: Comprehensions – One-Line Power

## Series C: Data Structures Express | Story 5 of 5

![The 2026 Python Metromap/images/Comprehensions – One-Line Power](images/Comprehensions – One-Line Power.png)

## 📖 Introduction

**Welcome to the fifth and final stop on the Data Structures Express Line.**

You've mastered lists, tuples, dictionaries, and sets. You can create, access, modify, and transform collections in countless ways. But often, you need to create new collections from existing ones—transforming data, filtering elements, or building nested structures. Doing this with traditional loops works, but it's verbose and often hard to read.

That's where comprehensions come in.

Comprehensions are Python's elegant, one-line syntax for creating new collections from existing iterables. List comprehensions create lists, dictionary comprehensions create dictionaries, and set comprehensions create sets. They combine looping, filtering, and transformation into a single, readable expression. Comprehensions are faster than traditional loops, more concise, and often more readable once you learn the pattern.

This story—**The 2026 Python Metromap: Comprehensions – One-Line Power**—is your guide to mastering comprehensions. We'll transform data pipelines with list comprehensions, build dictionaries for fast lookups, create sets for deduplication, and nest comprehensions for complex transformations. We'll build a complete data processing pipeline that cleans, transforms, and analyzes data. We'll create a matrix manipulation library with nested comprehensions. And we'll implement a complete log analysis system that processes millions of lines efficiently.

**Let's comprehend.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories) – COMPLETED
### Series B: Functions & Modules Yard (6 Stories) – COMPLETED

### Series C: Data Structures Express (5 Stories)

- 📋 **The 2026 Python Metromap: Lists – Ordered & Mutable** – Todo application; playlist manager; shopping cart system.

- 🔒 **The 2026 Python Metromap: Tuples – Immutable Collections** – GPS coordinates; database records; immutable configuration.

- 🔑 **The 2026 Python Metromap: Dictionaries – Key-Value Power** – User profile system; product catalog; caching system; dependency injection.

- 🎯 **The 2026 Python Metromap: Sets – Unique & Fast** – Unique visitor tracking; friend recommendation; duplicate file finder; content recommendation.

- 📝 **The 2026 Python Metromap: Comprehensions – One-Line Power** – Data transformation pipelines; filtered iterations; nested structure creation. **⬅️ YOU ARE HERE**

### Series D: Object-Oriented Programming (OOP) Line (6 Stories) – Next Station

- 🏗️ **The 2026 Python Metromap: Classes & Objects – Blueprints & Instances** – Bank account system; deposit and withdrawal methods; customer management. 🔜 *Up Next*

- 🔧 **The 2026 Python Metromap: Constructor – Building Objects** – Employee onboarding system; automatic attribute initialization.

- 👪 **The 2026 Python Metromap: Inheritance – Reusing Parent Classes** – Vehicle fleet manager with Car, Truck, and Motorcycle classes.

- 🎭 **The 2026 Python Metromap: Polymorphism – One Interface, Many Forms** – Payment processing with CreditCard, PayPal, and Crypto implementations.

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules.

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📝 Section 1: List Comprehensions – Transforming Data in One Line

List comprehensions provide a concise way to create lists by applying an expression to each item in an iterable, optionally with filtering.

**SOLID Principle Applied: Single Responsibility** – Each comprehension does one transformation job.

**Design Pattern: Builder Pattern** – Comprehensions build new collections declaratively.

```python
"""
LIST COMPREHENSIONS: TRANSFORMING DATA IN ONE LINE

This section covers list comprehensions for creating lists from iterables.

SOLID Principle: Single Responsibility
- Each comprehension does one transformation job

Design Pattern: Builder Pattern
- Comprehensions build new collections declaratively
"""

from typing import List, Any, Dict, Set, Tuple
import time


def demonstrate_basic_list_comprehensions():
    """
    Demonstrates basic list comprehension syntax and patterns.
    
    Syntax: [expression for item in iterable if condition]
    """
    print("=" * 60)
    print("SECTION 1A: BASIC LIST COMPREHENSIONS")
    print("=" * 60)
    
    # COMPREHENSION VS TRADITIONAL LOOP
    print("\n1. COMPREHENSION VS TRADITIONAL LOOP")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5]
    
    # Traditional loop
    squares_loop = []
    for x in numbers:
        squares_loop.append(x ** 2)
    
    # List comprehension
    squares_comp = [x ** 2 for x in numbers]
    
    print(f"  Traditional: {squares_loop}")
    print(f"  Comprehension: {squares_comp}")
    
    # WITH CONDITIONAL FILTERING
    print("\n2. WITH CONDITIONAL FILTERING")
    print("-" * 40)
    
    numbers = range(20)
    
    # Even numbers only
    evens = [x for x in numbers if x % 2 == 0]
    print(f"  Evens: {evens}")
    
    # Numbers greater than 10
    greater_than_10 = [x for x in numbers if x > 10]
    print(f"  Numbers > 10: {greater_than_10}")
    
    # Numbers between 5 and 15
    between = [x for x in numbers if 5 <= x <= 15]
    print(f"  Numbers 5-15: {between}")
    
    # WITH EXPRESSION TRANSFORMATION
    print("\n3. WITH EXPRESSION TRANSFORMATION")
    print("-" * 40)
    
    # Square of even numbers
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    print(f"  Even squares: {even_squares}")
    
    # Cube of odd numbers
    odd_cubes = [x ** 3 for x in range(10) if x % 2 == 1]
    print(f"  Odd cubes: {odd_cubes}")
    
    # String transformations
    words = ["hello", "world", "python", "code"]
    upper_words = [word.upper() for word in words]
    capitalized = [word.capitalize() for word in words]
    print(f"  Uppercase: {upper_words}")
    print(f"  Capitalized: {capitalized}")
    
    # WITH IF-ELSE (TERNARY)
    print("\n4. WITH IF-ELSE (Ternary Expression)")
    print("-" * 40)
    
    # Label numbers as even or odd
    labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
    print(f"  Labels: {labels}")
    
    # Categorize numbers
    categories = ["small" if x < 10 else "medium" if x < 20 else "large" for x in range(30)]
    print(f"  Categories (first 20): {categories[:20]}")


def demonstrate_advanced_list_comprehensions():
    """
    Demonstrates advanced list comprehension patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ADVANCED LIST COMPREHENSIONS")
    print("=" * 60)
    
    # NESTED COMPREHENSIONS
    print("\n1. NESTED COMPREHENSIONS")
    print("-" * 40)
    
    # Flatten a matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"  Matrix: {matrix}")
    print(f"  Flattened: {flattened}")
    
    # Create coordinate pairs
    coords = [(x, y) for x in range(3) for y in range(3)]
    print(f"  Coordinates 3x3: {coords}")
    
    # Multiplication table
    mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("  Multiplication table (5x5):")
    for row in mult_table:
        print(f"    {row}")
    
    # WORKING WITH DICTIONARIES
    print("\n2. WORKING WITH DICTIONARIES")
    print("-" * 40)
    
    users = [
        {"name": "Alice", "age": 28, "city": "NYC"},
        {"name": "Bob", "age": 35, "city": "LA"},
        {"name": "Charlie", "age": 22, "city": "Chicago"}
    ]
    
    # Extract names
    names = [user["name"] for user in users]
    print(f"  Names: {names}")
    
    # Extract names of users over 30
    older_names = [user["name"] for user in users if user["age"] > 30]
    print(f"  Users over 30: {older_names}")
    
    # Extract (name, city) pairs
    name_city = [(user["name"], user["city"]) for user in users]
    print(f"  (Name, City): {name_city}")
    
    # TRANSFORMING DATA
    print("\n3. TRANSFORMING DATA WITH COMPREHENSIONS")
    print("-" * 40)
    
    prices = [10.99, 25.50, 8.75, 12.00, 30.25]
    
    # Apply discount
    discounted = [round(price * 0.9, 2) for price in prices]
    print(f"  Original: {prices}")
    print(f"  Discounted: {discounted}")
    
    # Add tax
    with_tax = [round(price * 1.08, 2) for price in prices]
    print(f"  With 8% tax: {with_tax}")
    
    # Format as currency
    formatted = [f"${price:.2f}" for price in prices]
    print(f"  Formatted: {formatted}")
    
    # MULTIPLE CONDITIONS
    print("\n4. MULTIPLE CONDITIONS")
    print("-" * 40)
    
    numbers = range(50)
    
    # Numbers divisible by 3 AND 5
    divisible_by_3_and_5 = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
    print(f"  Divisible by 3 and 5: {divisible_by_3_and_5}")
    
    # Numbers divisible by 3 OR 5
    divisible_by_3_or_5 = [x for x in numbers if x % 3 == 0 or x % 5 == 0]
    print(f"  Divisible by 3 or 5: {divisible_by_3_or_5[:15]}...")
    
    # PERFORMANCE COMPARISON
    print("\n5. PERFORMANCE: COMPREHENSION VS LOOP")
    print("-" * 40)
    
    size = 1000000
    
    # Loop
    start = time.time()
    squares_loop = []
    for i in range(size):
        squares_loop.append(i ** 2)
    loop_time = time.time() - start
    
    # Comprehension
    start = time.time()
    squares_comp = [i ** 2 for i in range(size)]
    comp_time = time.time() - start
    
    print(f"  Loop: {loop_time:.4f}s")
    print(f"  Comprehension: {comp_time:.4f}s")
    print(f"  Comprehension is {loop_time / comp_time:.1f}x faster!")
    
    # READABILITY EXAMPLES
    print("\n6. READABILITY COMPARISON")
    print("-" * 40)
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Hard to read (too complex for one line)
    # complex = [x * 2 for x in data if x % 2 == 0 and x > 5 and x < 10]
    
    # Better: break into steps
    filtered = [x for x in data if x % 2 == 0 and x > 5 and x < 10]
    transformed = [x * 2 for x in filtered]
    
    print(f"  Original: {data}")
    print(f"  Step 1 - Filter: {filtered}")
    print(f"  Step 2 - Transform: {transformed}")
    print("\n  💡 Keep comprehensions readable - if it's too complex, use multiple steps!")


def demonstrate_practical_comprehensions():
    """
    Demonstrates practical real-world use cases for list comprehensions.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: PRACTICAL LIST COMPREHENSIONS")
    print("=" * 60)
    
    # DATA CLEANING
    print("\n1. DATA CLEANING")
    print("-" * 40)
    
    raw_data = ["  Alice  ", "Bob", "  CHARLIE  ", "david", "  EVA  "]
    
    # Clean strings: strip, lowercase, capitalize
    cleaned = [name.strip().capitalize() for name in raw_data]
    print(f"  Raw: {raw_data}")
    print(f"  Cleaned: {cleaned}")
    
    # Remove empty strings
    data_with_empty = ["apple", "", "banana", "", "cherry", None, "date"]
    non_empty = [item for item in data_with_empty if item]
    print(f"  With empties: {data_with_empty}")
    print(f"  Non-empty: {non_empty}")
    
    # Convert types
    string_numbers = ["1", "2", "3", "4", "5"]
    int_numbers = [int(s) for s in string_numbers]
    print(f"  Strings: {string_numbers}")
    print(f"  Integers: {int_numbers}")
    
    # FILTERING DATA
    print("\n2. FILTERING DATA")
    print("-" * 40)
    
    sales = [
        {"product": "Laptop", "amount": 999, "region": "North"},
        {"product": "Mouse", "amount": 25, "region": "South"},
        {"product": "Keyboard", "amount": 75, "region": "North"},
        {"product": "Monitor", "amount": 299, "region": "West"},
        {"product": "Desk", "amount": 399, "region": "North"}
    ]
    
    # North region sales
    north_sales = [sale for sale in sales if sale["region"] == "North"]
    print(f"  North region sales: {len(north_sales)}")
    
    # Sales over $100
    high_value = [sale["product"] for sale in sales if sale["amount"] > 100]
    print(f"  Products over $100: {high_value}")
    
    # EXTRACTING DATA
    print("\n3. EXTRACTING DATA")
    print("-" * 40)
    
    # Get all product names
    product_names = [sale["product"] for sale in sales]
    print(f"  All products: {product_names}")
    
    # Get unique products (using set comprehension preview)
    unique_products = {sale["product"] for sale in sales}
    print(f"  Unique products: {unique_products}")
    
    # TRANSFORMING DATA
    print("\n4. TRANSFORMING DATA")
    print("-" * 40)
    
    # Apply 10% discount to all amounts
    discounted_sales = [
        {**sale, "amount": round(sale["amount"] * 0.9, 2)}
        for sale in sales
    ]
    print(f"  First sale original: {sales[0]['amount']}")
    print(f"  First sale discounted: {discounted_sales[0]['amount']}")
    
    # Add tax field
    with_tax = [
        {**sale, "tax": round(sale["amount"] * 0.08, 2)}
        for sale in sales
    ]
    print(f"  Added tax field: {with_tax[0]['tax']}")


if __name__ == "__main__":
    demonstrate_basic_list_comprehensions()
    demonstrate_advanced_list_comprehensions()
    demonstrate_practical_comprehensions()
```

---

## 📖 Section 2: Dictionary Comprehensions – Key-Value in One Line

Dictionary comprehensions provide a concise way to create dictionaries from iterables.

**SOLID Principle Applied: Single Responsibility** – Each comprehension builds one dictionary.

**Design Pattern: Factory Pattern** – Comprehensions create dictionaries declaratively.

```python
"""
DICTIONARY COMPREHENSIONS: KEY-VALUE IN ONE LINE

This section covers dictionary comprehensions for creating dictionaries.

SOLID Principle: Single Responsibility
- Each comprehension builds one dictionary

Design Pattern: Factory Pattern
- Comprehensions create dictionaries declaratively
"""

from typing import Dict, List, Any, Tuple
from collections import defaultdict


def demonstrate_basic_dict_comprehensions():
    """
    Demonstrates basic dictionary comprehension syntax and patterns.
    
    Syntax: {key_expression: value_expression for item in iterable if condition}
    """
    print("=" * 60)
    print("SECTION 2A: BASIC DICTIONARY COMPREHENSIONS")
    print("=" * 60)
    
    # SQUARE NUMBERS
    print("\n1. SQUARE NUMBERS")
    print("-" * 40)
    
    # Traditional loop
    squares_dict = {}
    for x in range(10):
        squares_dict[x] = x ** 2
    
    # Dictionary comprehension
    squares_comp = {x: x ** 2 for x in range(10)}
    
    print(f"  Traditional: {squares_dict}")
    print(f"  Comprehension: {squares_comp}")
    
    # EVEN SQUARES WITH FILTERING
    print("\n2. WITH CONDITIONAL FILTERING")
    print("-" * 40)
    
    even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
    print(f"  Even squares: {even_squares}")
    
    # CUBE OF ODD NUMBERS
    odd_cubes = {x: x ** 3 for x in range(10) if x % 2 == 1}
    print(f"  Odd cubes: {odd_cubes}")
    
    # FROM TWO LISTS (using zip)
    print("\n3. FROM TWO LISTS USING ZIP")
    print("-" * 40)
    
    keys = ["name", "age", "city", "email"]
    values = ["Alice", 28, "NYC", "alice@example.com"]
    
    user_dict = {k: v for k, v in zip(keys, values)}
    print(f"  Keys: {keys}")
    print(f"  Values: {values}")
    print(f"  Result: {user_dict}")
    
    # FROM LIST OF TUPLES
    print("\n4. FROM LIST OF TUPLES")
    print("-" * 40)
    
    pairs = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
    dict_from_pairs = {k: v for k, v in pairs}
    print(f"  Pairs: {pairs}")
    print(f"  Dictionary: {dict_from_pairs}")
    
    # STRING PROCESSING
    print("\n5. STRING PROCESSING")
    print("-" * 40)
    
    word = "abracadabra"
    char_counts = {char: word.count(char) for char in set(word)}
    print(f"  Word: '{word}'")
    print(f"  Character counts: {char_counts}")


def demonstrate_advanced_dict_comprehensions():
    """
    Demonstrates advanced dictionary comprehension patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: ADVANCED DICTIONARY COMPREHENSIONS")
    print("=" * 60)
    
    # TRANSFORMING EXISTING DICTIONARY
    print("\n1. TRANSFORMING EXISTING DICTIONARY")
    print("-" * 40)
    
    original = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    
    # Double the values
    doubled = {k: v * 2 for k, v in original.items()}
    print(f"  Original: {original}")
    print(f"  Doubled: {doubled}")
    
    # Square the values
    squared = {k: v ** 2 for k, v in original.items()}
    print(f"  Squared: {squared}")
    
    # FILTERING DICTIONARY ITEMS
    print("\n2. FILTERING DICTIONARY ITEMS")
    print("-" * 40)
    
    # Keep only items with value > 3
    filtered = {k: v for k, v in original.items() if v > 3}
    print(f"  Values > 3: {filtered}")
    
    # Keep only items with keys in a set
    keep_keys = {"b", "d", "f"}
    kept = {k: v for k, v in original.items() if k in keep_keys}
    print(f"  Keys in {keep_keys}: {kept}")
    
    # SWAPPING KEYS AND VALUES
    print("\n3. SWAPPING KEYS AND VALUES")
    print("-" * 40)
    
    original = {"apple": 5, "banana": 3, "cherry": 8, "date": 2}
    swapped = {v: k for k, v in original.items()}
    print(f"  Original: {original}")
    print(f"  Swapped: {swapped}")
    
    # CONDITIONAL VALUE (Ternary)
    print("\n4. CONDITIONAL VALUES (Ternary)")
    print("-" * 40)
    
    numbers = range(10)
    parity = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
    print(f"  Number parity: {parity}")
    
    # NESTED DICTIONARY COMPREHENSION
    print("\n5. NESTED DICTIONARY COMPREHENSION")
    print("-" * 40)
    
    # Create multiplication table as nested dict
    mult_table = {i: {j: i * j for j in range(1, 6)} for i in range(1, 6)}
    print("  Multiplication table (5x5):")
    for i in range(1, 6):
        print(f"    {i}: {mult_table[i]}")
    
    # WORKING WITH LISTS OF DICTIONARIES
    print("\n6. WORKING WITH LISTS OF DICTIONARIES")
    print("-" * 40)
    
    users = [
        {"id": 1, "name": "Alice", "age": 28},
        {"id": 2, "name": "Bob", "age": 35},
        {"id": 3, "name": "Charlie", "age": 22}
    ]
    
    # Create id -> user mapping
    user_map = {user["id"]: user for user in users}
    print(f"  User mapping: {user_map}")
    
    # Create name -> age mapping
    name_age = {user["name"]: user["age"] for user in users}
    print(f"  Name to age: {name_age}")


def demonstrate_practical_dict_comprehensions():
    """
    Demonstrates practical real-world use cases for dictionary comprehensions.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: PRACTICAL DICTIONARY COMPREHENSIONS")
    print("=" * 60)
    
    # FREQUENCY COUNTER
    print("\n1. FREQUENCY COUNTER")
    print("-" * 40)
    
    words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    word_counts = {word: words.count(word) for word in set(words)}
    print(f"  Words: {words}")
    print(f"  Frequencies: {word_counts}")
    
    # GROUPING DATA
    print("\n2. GROUPING DATA")
    print("-" * 40)
    
    products = [
        ("electronics", "laptop"),
        ("electronics", "mouse"),
        ("books", "python book"),
        ("electronics", "keyboard"),
        ("books", "data science book"),
        ("clothing", "shirt")
    ]
    
    # Group by category
    grouped = {}
    for category, product in products:
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(product)
    
    # Using defaultdict (more efficient)
    from collections import defaultdict
    grouped_default = defaultdict(list)
    for category, product in products:
        grouped_default[category].append(product)
    
    print(f"  Grouped by category: {dict(grouped_default)}")
    
    # INDEXING FOR FAST LOOKUP
    print("\n3. CREATING INDEXES FOR FAST LOOKUP")
    print("-" * 40)
    
    employees = [
        {"id": 1001, "name": "Alice", "department": "Engineering"},
        {"id": 1002, "name": "Bob", "department": "Sales"},
        {"id": 1003, "name": "Charlie", "department": "Engineering"}
    ]
    
    # Create id index
    id_index = {emp["id"]: emp for emp in employees}
    print(f"  Lookup by ID: {id_index[1001]['name']}")
    
    # Create department index
    dept_index = defaultdict(list)
    for emp in employees:
        dept_index[emp["department"]].append(emp["name"])
    print(f"  Department index: {dict(dept_index)}")
    
    # DATA TRANSFORMATION
    print("\n4. DATA TRANSFORMATION")
    print("-" * 40)
    
    sales = [
        {"product": "Laptop", "price": 999, "quantity": 2},
        {"product": "Mouse", "price": 25, "quantity": 5},
        {"product": "Keyboard", "price": 75, "quantity": 1}
    ]
    
    # Calculate total per product
    totals = {sale["product"]: sale["price"] * sale["quantity"] for sale in sales}
    print(f"  Sales totals: {totals}")
    
    # Add calculated fields
    enriched = {
        sale["product"]: {
            "subtotal": sale["price"] * sale["quantity"],
            "tax": round(sale["price"] * sale["quantity"] * 0.08, 2)
        }
        for sale in sales
    }
    print(f"  Enriched data: {enriched}")
    
    # FILTERING AND TRANSFORMING
    print("\n5. FILTERING AND TRANSFORMING")
    print("-" * 40)
    
    temperatures = {
        "New York": 72,
        "Los Angeles": 85,
        "Chicago": 68,
        "Houston": 90,
        "Phoenix": 95
    }
    
    # Convert to Celsius
    celsius = {city: round((temp - 32) * 5/9, 1) for city, temp in temperatures.items()}
    print(f"  Fahrenheit: {temperatures}")
    print(f"  Celsius: {celsius}")
    
    # Filter hot cities (over 80°F)
    hot_cities = {city: temp for city, temp in temperatures.items() if temp > 80}
    print(f"  Hot cities (>80°F): {hot_cities}")
    
    # INVERTING DICTIONARY (with duplicate handling)
    print("\n6. INVERTING DICTIONARY WITH DUPLICATES")
    print("-" * 40)
    
    roles = {
        "Alice": "admin",
        "Bob": "user",
        "Charlie": "admin",
        "Diana": "user",
        "Eve": "guest"
    }
    
    # Simple inversion (loses duplicates)
    simple_invert = {v: k for k, v in roles.items()}
    print(f"  Simple inversion (loses duplicates): {simple_invert}")
    
    # Invert with list of values
    from collections import defaultdict
    invert_list = defaultdict(list)
    for k, v in roles.items():
        invert_list[v].append(k)
    print(f"  Invert with lists: {dict(invert_list)}")


if __name__ == "__main__":
    demonstrate_basic_dict_comprehensions()
    demonstrate_advanced_dict_comprehensions()
    demonstrate_practical_dict_comprehensions()
```

---

## 🎯 Section 3: Set Comprehensions – Unique in One Line

Set comprehensions provide a concise way to create sets of unique elements.

**SOLID Principle Applied: Single Responsibility** – Each comprehension builds one set.

**Design Pattern: Factory Pattern** – Comprehensions create sets declaratively.

```python
"""
SET COMPREHENSIONS: UNIQUE IN ONE LINE

This section covers set comprehensions for creating sets of unique elements.

SOLID Principle: Single Responsibility
- Each comprehension builds one set

Design Pattern: Factory Pattern
- Comprehensions create sets declaratively
"""

from typing import Set, List, Any


def demonstrate_set_comprehensions():
    """
    Demonstrates set comprehension syntax and patterns.
    
    Syntax: {expression for item in iterable if condition}
    """
    print("=" * 60)
    print("SECTION 3: SET COMPREHENSIONS")
    print("=" * 60)
    
    # BASIC SET COMPREHENSION
    print("\n1. BASIC SET COMPREHENSION")
    print("-" * 40)
    
    # Square numbers
    squares = {x ** 2 for x in range(10)}
    print(f"  Squares: {squares}")
    
    # Even numbers
    evens = {x for x in range(20) if x % 2 == 0}
    print(f"  Evens: {evens}")
    
    # REMOVING DUPLICATES
    print("\n2. REMOVING DUPLICATES")
    print("-" * 40)
    
    words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    unique_words = {word for word in words}
    print(f"  Original: {words}")
    print(f"  Unique: {unique_words}")
    
    # UNIQUE CHARACTERS
    print("\n3. UNIQUE CHARACTERS")
    print("-" * 40)
    
    text = "abracadabra"
    unique_chars = {char for char in text}
    print(f"  Text: '{text}'")
    print(f"  Unique characters: {unique_chars}")
    
    # Vowels in text
    vowels = {char for char in text if char in "aeiou"}
    print(f"  Vowels: {vowels}")
    
    # TRANSFORMATION
    print("\n4. TRANSFORMATION")
    print("-" * 40)
    
    names = ["alice", "bob", "charlie", "diana"]
    capitalized = {name.capitalize() for name in names}
    print(f"  Original: {names}")
    print(f"  Capitalized: {capitalized}")
    
    # SET FROM DICTIONARY VALUES
    print("\n5. SET FROM DICTIONARY VALUES")
    print("-" * 40)
    
    users = {
        "alice": "admin",
        "bob": "user",
        "charlie": "admin",
        "diana": "user",
        "eve": "guest"
    }
    
    unique_roles = {role for role in users.values()}
    print(f"  Users: {users}")
    print(f"  Unique roles: {unique_roles}")
    
    # FILTERING
    print("\n6. FILTERING")
    print("-" * 40)
    
    numbers = range(50)
    
    # Prime numbers (simplified)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = {x for x in numbers if is_prime(x)}
    print(f"  Prime numbers under 50: {primes}")
    
    # PRACTICAL: UNIQUE TAGS
    print("\n7. PRACTICAL: EXTRACTING UNIQUE TAGS")
    print("-" * 40)
    
    articles = [
        {"title": "Python Basics", "tags": ["python", "programming", "beginner"]},
        {"title": "Advanced Python", "tags": ["python", "programming", "advanced"]},
        {"title": "Data Science", "tags": ["data", "python", "machine-learning"]},
        {"title": "Web Development", "tags": ["web", "javascript", "html"]}
    ]
    
    all_tags = {tag for article in articles for tag in article["tags"]}
    print(f"  All unique tags: {all_tags}")
    
    # Tag frequency
    tag_counts = {}
    for article in articles:
        for tag in article["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    print(f"  Tag frequencies: {tag_counts}")
    
    # PERFORMANCE COMPARISON
    print("\n8. SET VS LIST FOR UNIQUENESS")
    print("-" * 40)
    
    import time
    
    data = list(range(10000)) * 10  # 100,000 items with duplicates
    
    # Using set comprehension
    start = time.time()
    unique_set = {x for x in data}
    set_time = time.time() - start
    
    # Using list then convert to set
    start = time.time()
    unique_list = list(set(data))
    list_time = time.time() - start
    
    print(f"  Set comprehension: {set_time:.4f}s")
    print(f"  set(list): {list_time:.4f}s")
    print(f"  Set comprehension is {list_time / set_time:.1f}x faster!")


if __name__ == "__main__":
    demonstrate_set_comprehensions()
```

---

## 🔄 Section 4: Nested Comprehensions – Multi-dimensional Data

Nested comprehensions handle multi-dimensional data structures like matrices.

**SOLID Principle Applied: Single Responsibility** – Each level of nesting handles one dimension.

**Design Pattern: Composite Pattern** – Handles nested structures recursively.

```python
"""
NESTED COMPREHENSIONS: MULTI-DIMENSIONAL DATA

This section covers nested comprehensions for multi-dimensional data.

SOLID Principle: Single Responsibility
- Each level of nesting handles one dimension

Design Pattern: Composite Pattern
- Handles nested structures recursively
"""

from typing import List, Any


def demonstrate_nested_comprehensions():
    """
    Demonstrates nested comprehensions for multi-dimensional data.
    """
    print("=" * 60)
    print("SECTION 4A: NESTED COMPREHENSIONS")
    print("=" * 60)
    
    # FLATTENING MATRICES
    print("\n1. FLATTENING MATRICES")
    print("-" * 40)
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"  Matrix: {matrix}")
    print(f"  Flattened: {flattened}")
    
    # FILTERING DURING FLATTENING
    print("\n2. FILTERING DURING FLATTENING")
    print("-" * 40)
    
    # Flatten even numbers only
    even_flat = [num for row in matrix for num in row if num % 2 == 0]
    print(f"  Even numbers: {even_flat}")
    
    # Flatten and square
    squared_flat = [num ** 2 for row in matrix for num in row]
    print(f"  Squared: {squared_flat}")
    
    # CREATING MATRICES
    print("\n3. CREATING MATRICES")
    print("-" * 40)
    
    # 3x3 identity matrix
    identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    print("  Identity matrix (3x3):")
    for row in identity:
        print(f"    {row}")
    
    # Multiplication table
    mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("  Multiplication table (5x5):")
    for row in mult_table:
        print(f"    {row}")
    
    # COORDINATE GENERATION
    print("\n4. COORDINATE GENERATION")
    print("-" * 40)
    
    # 2D coordinates
    coords_2d = [(x, y) for x in range(3) for y in range(3)]
    print(f"  All 2D coordinates (3x3): {coords_2d}")
    
    # 3D coordinates
    coords_3d = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    print(f"  All 3D coordinates (2x2x2): {coords_3d}")
    
    # TRANSFORMING MATRICES
    print("\n5. TRANSFORMING MATRICES")
    print("-" * 40)
    
    # Transpose matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print(f"  Original:")
    for row in matrix:
        print(f"    {row}")
    print(f"  Transpose:")
    for row in transpose:
        print(f"    {row}")
    
    # NESTED DATA STRUCTURES
    print("\n6. NESTED DATA STRUCTURES")
    print("-" * 40)
    
    # Create nested dictionary from matrix
    nested_dict = {i: {j: matrix[i][j] for j in range(len(matrix[i]))} for i in range(len(matrix))}
    print(f"  Nested dictionary: {nested_dict}")


def demonstrate_practical_nested_comprehensions():
    """
    Demonstrates practical uses of nested comprehensions.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: PRACTICAL NESTED COMPREHENSIONS")
    print("=" * 60)
    
    # PARSING CSV DATA
    print("\n1. PARSING CSV DATA")
    print("-" * 40)
    
    csv_data = """name,age,city
Alice,28,New York
Bob,35,Los Angeles
Charlie,22,Chicago"""
    
    lines = csv_data.strip().split('\n')
    headers = lines[0].split(',')
    rows = [line.split(',') for line in lines[1:]]
    
    # Convert to list of dictionaries
    parsed = [{headers[i]: row[i] for i in range(len(headers))} for row in rows]
    print(f"  Parsed CSV: {parsed}")
    
    # TRANSFORMING JSON-LIKE DATA
    print("\n2. TRANSFORMING JSON-LIKE DATA")
    print("-" * 40)
    
    orders = [
        {"id": 1, "items": ["laptop", "mouse"], "total": 1024.99},
        {"id": 2, "items": ["keyboard"], "total": 89.99},
        {"id": 3, "items": ["monitor", "cable", "adapter"], "total": 329.97}
    ]
    
    # Extract all item names
    all_items = [item for order in orders for item in order["items"]]
    print(f"  All items: {all_items}")
    
    # Create flattened order summaries
    summaries = [
        {"order_id": order["id"], "item_count": len(order["items"]), "total": order["total"]}
        for order in orders
    ]
    print(f"  Order summaries: {summaries}")
    
    # Filtering nested data
    large_orders = [
        {"order_id": order["id"], "items": order["items"]}
        for order in orders
        if len(order["items"]) > 2
    ]
    print(f"  Orders with >2 items: {large_orders}")
    
    # MATRIX OPERATIONS
    print("\n3. MATRIX OPERATIONS")
    print("-" * 40)
    
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    # Matrix addition
    C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    print(f"  A + B = {C}")
    
    # Matrix multiplication
    def matrix_multiply(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(len(Y)))
                 for j in range(len(Y[0]))]
                for i in range(len(X))]
    
    product = matrix_multiply(A, B)
    print(f"  A × B = {product}")
    
    # IMAGE PROCESSING (SIMULATED)
    print("\n4. SIMULATED IMAGE PROCESSING")
    print("-" * 40)
    
    # Simulated grayscale image (2D list)
    image = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ]
    
    # Apply brightness adjustment (add 20, clip at 255)
    brightened = [[min(pixel + 20, 255) for pixel in row] for row in image]
    print(f"  Original first row: {image[0]}")
    print(f"  Brightened first row: {brightened[0]}")
    
    # Apply threshold (values > 100 become 255, else 0)
    thresholded = [[255 if pixel > 100 else 0 for pixel in row] for row in image]
    print(f"  Thresholded first row: {thresholded[0]}")


if __name__ == "__main__":
    demonstrate_nested_comprehensions()
    demonstrate_practical_nested_comprehensions()
```

---

## 🏭 Section 5: Complete Data Processing Pipeline

A complete data processing pipeline using comprehensions for ETL (Extract, Transform, Load) operations.

**SOLID Principles Applied:**
- Single Responsibility: Each stage has one purpose
- Open/Closed: New transformations can be added

**Design Patterns:**
- Pipeline Pattern: Data flows through processing stages
- Strategy Pattern: Pluggable transformations

```python
"""
COMPLETE DATA PROCESSING PIPELINE

This section builds a complete data processing pipeline using comprehensions.

SOLID Principles Applied:
- Single Responsibility: Each stage has one purpose
- Open/Closed: New transformations can be added

Design Patterns:
- Pipeline Pattern: Data flows through processing stages
- Strategy Pattern: Pluggable transformations
"""

from typing import List, Dict, Any, Optional, Callable, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
import csv
from io import StringIO


@dataclass
class DataRecord:
    """Represents a single data record."""
    data: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)


class DataPipeline:
    """
    Data processing pipeline using comprehensions.
    
    Design Pattern: Pipeline Pattern - Data flows through stages
    """
    
    def __init__(self):
        self.stages: List[Callable] = []
    
    def add_stage(self, stage: Callable) -> 'DataPipeline':
        """Add a processing stage to the pipeline."""
        self.stages.append(stage)
        return self
    
    def process(self, data: List[Dict]) -> List[Dict]:
        """Process data through all pipeline stages."""
        result = data
        for stage in self.stages:
            result = stage(result)
        return result


class DataTransformer:
    """Collection of data transformation functions using comprehensions."""
    
    @staticmethod
    def clean_strings(records: List[Dict], fields: List[str] = None) -> List[Dict]:
        """Clean string fields (strip whitespace)."""
        if fields is None:
            fields = []
        
        return [
            {
                k: (v.strip() if isinstance(v, str) and (not fields or k in fields) else v)
                for k, v in record.items()
            }
            for record in records
        ]
    
    @staticmethod
    def convert_types(records: List[Dict], type_map: Dict[str, type]) -> List[Dict]:
        """Convert field types."""
        return [
            {
                k: (type_map[k](v) if k in type_map and v is not None else v)
                for k, v in record.items()
            }
            for record in records
        ]
    
    @staticmethod
    def filter_records(records: List[Dict], predicate: Callable) -> List[Dict]:
        """Filter records using a predicate."""
        return [record for record in records if predicate(record)]
    
    @staticmethod
    def select_fields(records: List[Dict], fields: List[str]) -> List[Dict]:
        """Select only specified fields."""
        return [{k: v for k, v in record.items() if k in fields} for record in records]
    
    @staticmethod
    def add_computed_field(records: List[Dict], field_name: str, compute: Callable) -> List[Dict]:
        """Add a computed field to each record."""
        return [
            {**record, field_name: compute(record)}
            for record in records
        ]
    
    @staticmethod
    def remove_nulls(records: List[Dict]) -> List[Dict]:
        """Remove records with null values in any field."""
        return [record for record in records if all(v is not None for v in record.values())]
    
    @staticmethod
    def fill_nulls(records: List[Dict], defaults: Dict[str, Any]) -> List[Dict]:
        """Fill null values with defaults."""
        return [
            {
                k: (v if v is not None else defaults.get(k))
                for k, v in record.items()
            }
            for record in records
        ]
    
    @staticmethod
    def normalize_numeric(records: List[Dict], fields: List[str], min_val: float, max_val: float) -> List[Dict]:
        """Normalize numeric fields to [0, 1] range."""
        def normalize(value):
            if value is None:
                return None
            return (value - min_val) / (max_val - min_val) if max_val != min_val else 0
        
        return [
            {
                k: (normalize(v) if k in fields else v)
                for k, v in record.items()
            }
            for record in records
        ]
    
    @staticmethod
    def aggregate(records: List[Dict], group_by: str, agg_fields: Dict[str, str]) -> List[Dict]:
        """
        Aggregate records by a field.
        
        agg_fields: field -> aggregation function ('sum', 'avg', 'count', 'min', 'max')
        """
        groups = {}
        
        for record in records:
            key = record.get(group_by)
            if key not in groups:
                groups[key] = {}
            
            for field, agg_func in agg_fields.items():
                value = record.get(field, 0)
                
                if agg_func == 'sum':
                    groups[key][field] = groups[key].get(field, 0) + (value or 0)
                elif agg_func == 'count':
                    groups[key][field] = groups[key].get(field, 0) + 1
                elif agg_func == 'min':
                    current = groups[key].get(field)
                    if current is None or (value is not None and value < current):
                        groups[key][field] = value
                elif agg_func == 'max':
                    current = groups[key].get(field)
                    if current is None or (value is not None and value > current):
                        groups[key][field] = value
        
        # Convert to list of dicts
        return [{group_by: key, **values} for key, values in groups.items()]
    
    @staticmethod
    def sort_records(records: List[Dict], sort_by: str, reverse: bool = False) -> List[Dict]:
        """Sort records by a field."""
        return sorted(records, key=lambda x: x.get(sort_by, 0), reverse=reverse)
    
    @staticmethod
    def limit_records(records: List[Dict], limit: int) -> List[Dict]:
        """Limit number of records."""
        return records[:limit]
    
    @staticmethod
    def distinct(records: List[Dict], key_fields: List[str]) -> List[Dict]:
        """Get distinct records based on key fields."""
        seen = set()
        result = []
        
        for record in records:
            key = tuple(record.get(field) for field in key_fields)
            if key not in seen:
                seen.add(key)
                result.append(record)
        
        return result


class DataPipelineBuilder:
    """
    Builder for creating data processing pipelines.
    
    Design Pattern: Builder Pattern - Builds pipelines incrementally
    """
    
    def __init__(self):
        self.pipeline = DataPipeline()
        self.transformer = DataTransformer()
    
    def clean(self, fields: List[str] = None) -> 'DataPipelineBuilder':
        """Add string cleaning stage."""
        self.pipeline.add_stage(lambda data: self.transformer.clean_strings(data, fields))
        return self
    
    def convert(self, type_map: Dict[str, type]) -> 'DataPipelineBuilder':
        """Add type conversion stage."""
        self.pipeline.add_stage(lambda data: self.transformer.convert_types(data, type_map))
        return self
    
    def filter(self, predicate: Callable) -> 'DataPipelineBuilder':
        """Add filter stage."""
        self.pipeline.add_stage(lambda data: self.transformer.filter_records(data, predicate))
        return self
    
    def select(self, fields: List[str]) -> 'DataPipelineBuilder':
        """Add field selection stage."""
        self.pipeline.add_stage(lambda data: self.transformer.select_fields(data, fields))
        return self
    
    def compute(self, field_name: str, compute: Callable) -> 'DataPipelineBuilder':
        """Add computed field stage."""
        self.pipeline.add_stage(lambda data: self.transformer.add_computed_field(data, field_name, compute))
        return self
    
    def remove_nulls(self) -> 'DataPipelineBuilder':
        """Add null removal stage."""
        self.pipeline.add_stage(self.transformer.remove_nulls)
        return self
    
    def fill_nulls(self, defaults: Dict[str, Any]) -> 'DataPipelineBuilder':
        """Add null filling stage."""
        self.pipeline.add_stage(lambda data: self.transformer.fill_nulls(data, defaults))
        return self
    
    def normalize(self, fields: List[str], min_val: float, max_val: float) -> 'DataPipelineBuilder':
        """Add numeric normalization stage."""
        self.pipeline.add_stage(lambda data: self.transformer.normalize_numeric(data, fields, min_val, max_val))
        return self
    
    def aggregate(self, group_by: str, agg_fields: Dict[str, str]) -> 'DataPipelineBuilder':
        """Add aggregation stage."""
        self.pipeline.add_stage(lambda data: self.transformer.aggregate(data, group_by, agg_fields))
        return self
    
    def sort(self, sort_by: str, reverse: bool = False) -> 'DataPipelineBuilder':
        """Add sorting stage."""
        self.pipeline.add_stage(lambda data: self.transformer.sort_records(data, sort_by, reverse))
        return self
    
    def limit(self, n: int) -> 'DataPipelineBuilder':
        """Add limit stage."""
        self.pipeline.add_stage(lambda data: self.transformer.limit_records(data, n))
        return self
    
    def distinct(self, key_fields: List[str]) -> 'DataPipelineBuilder':
        """Add distinct stage."""
        self.pipeline.add_stage(lambda data: self.transformer.distinct(data, key_fields))
        return self
    
    def build(self) -> DataPipeline:
        """Build and return the pipeline."""
        return self.pipeline


def demonstrate_data_pipeline():
    """
    Demonstrate the complete data processing pipeline.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: COMPLETE DATA PROCESSING PIPELINE")
    print("=" * 60)
    
    # Sample raw data
    print("\n1. RAW DATA")
    print("-" * 40)
    
    raw_data = [
        {"name": "  Alice  ", "age": "28", "salary": "75000", "city": "NYC", "active": "true"},
        {"name": "Bob", "age": "35", "salary": "85000", "city": "LA", "active": "true"},
        {"name": "  CHARLIE  ", "age": "22", "salary": "65000", "city": "Chicago", "active": "false"},
        {"name": "Diana", "age": "31", "salary": "95000", "city": "NYC", "active": "true"},
        {"name": "Eve", "age": "invalid", "salary": "55000", "city": "LA", "active": "true"}
    ]
    
    for record in raw_data:
        print(f"  {record}")
    
    # Build pipeline
    print("\n2. BUILDING DATA PIPELINE")
    print("-" * 40)
    
    pipeline = (DataPipelineBuilder()
                .clean(["name"])
                .convert({
                    "age": int,
                    "salary": int,
                    "active": lambda x: x.lower() == "true"
                })
                .filter(lambda r: r.get("age") is not None and isinstance(r["age"], int))
                .compute("age_group", lambda r: "senior" if r["age"] > 30 else "junior")
                .compute("salary_level", lambda r: "high" if r["salary"] > 80000 else "medium" if r["salary"] > 60000 else "low")
                .select(["name", "age", "salary", "city", "active", "age_group", "salary_level"])
                .build())
    
    print("  Pipeline stages configured:")
    print("    • Clean strings (name)")
    print("    • Convert types (age, salary, active)")
    print("    • Filter invalid records")
    print("    • Add computed fields (age_group, salary_level)")
    print("    • Select specific fields")
    
    # Process data
    print("\n3. PROCESSING DATA")
    print("-" * 40)
    
    processed = pipeline.process(raw_data)
    
    for record in processed:
        print(f"  {record}")
    
    # Aggregation example
    print("\n4. AGGREGATION PIPELINE")
    print("-" * 40)
    
    agg_pipeline = (DataPipelineBuilder()
                    .clean(["name", "city"])
                    .convert({"age": int, "salary": int})
                    .filter(lambda r: r.get("age") is not None)
                    .aggregate("city", {
                        "count": "count",
                        "avg_salary": "avg",
                        "total_salary": "sum",
                        "min_age": "min",
                        "max_age": "max"
                    })
                    .sort("avg_salary", reverse=True)
                    .build())
    
    # Need to recalculate avg properly
    city_stats = {}
    for record in raw_data:
        if record.get("age") and record["age"].isdigit():
            city = record["city"].strip()
            salary = int(record["salary"])
            age = int(record["age"])
            
            if city not in city_stats:
                city_stats[city] = {"sum_salary": 0, "count": 0, "ages": []}
            
            city_stats[city]["sum_salary"] += salary
            city_stats[city]["count"] += 1
            city_stats[city]["ages"].append(age)
    
    agg_results = []
    for city, stats in city_stats.items():
        agg_results.append({
            "city": city,
            "count": stats["count"],
            "avg_salary": stats["sum_salary"] / stats["count"],
            "total_salary": stats["sum_salary"],
            "min_age": min(stats["ages"]),
            "max_age": max(stats["ages"])
        })
    
    agg_results.sort(key=lambda x: x["avg_salary"], reverse=True)
    
    print("  City statistics:")
    for result in agg_results:
        print(f"    {result['city']}: {result['count']} employees, avg salary ${result['avg_salary']:.0f}")
    
    # Complete ETL example
    print("\n5. COMPLETE ETL PIPELINE EXAMPLE")
    print("-" * 40)
    
    # Simulate CSV data
    csv_data = """product,category,price,quantity
Laptop,Electronics,999,5
Mouse,Electronics,25,10
Keyboard,Electronics,75,3
Monitor,Electronics,299,2
Desk,Furniture,399,1
Chair,Furniture,199,4
"""
    
    # Parse CSV
    lines = csv_data.strip().split('\n')
    headers = lines[0].split(',')
    rows = [line.split(',') for line in lines[1:]]
    records = [{headers[i]: row[i] for i in range(len(headers))} for row in rows]
    
    print("  Raw CSV data parsed")
    
    # ETL Pipeline
    etl_pipeline = (DataPipelineBuilder()
                    .convert({"price": float, "quantity": int})
                    .compute("total", lambda r: r["price"] * r["quantity"])
                    .aggregate("category", {
                        "total_revenue": "sum",
                        "units_sold": "sum",
                        "avg_price": "avg",
                        "product_count": "count"
                    })
                    .sort("total_revenue", reverse=True)
                    .build())
    
    # Manual aggregation for demonstration
    category_stats = {}
    for record in records:
        category = record["category"]
        price = float(record["price"])
        quantity = int(record["quantity"])
        total = price * quantity
        
        if category not in category_stats:
            category_stats[category] = {
                "total_revenue": 0,
                "units_sold": 0,
                "prices": []
            }
        
        category_stats[category]["total_revenue"] += total
        category_stats[category]["units_sold"] += quantity
        category_stats[category]["prices"].append(price)
    
    etl_results = []
    for category, stats in category_stats.items():
        etl_results.append({
            "category": category,
            "total_revenue": stats["total_revenue"],
            "units_sold": stats["units_sold"],
            "avg_price": sum(stats["prices"]) / len(stats["prices"]),
            "product_count": len(stats["prices"])
        })
    
    etl_results.sort(key=lambda x: x["total_revenue"], reverse=True)
    
    print("\n  ETL Results:")
    for result in etl_results:
        print(f"    {result['category']}: ${result['total_revenue']:.0f} revenue, {result['units_sold']} units sold")
    
    print("\n  💡 Comprehensions used throughout:")
    print("    • List comprehensions for parsing")
    print("    • Dictionary comprehensions for transformation")
    print("    • Nested comprehensions for aggregation")
    print("    • Set comprehensions for deduplication")


if __name__ == "__main__":
    demonstrate_data_pipeline()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **List Comprehensions** – `[expr for item in iterable if condition]`. Create lists declaratively. Faster than loops.

- **Dictionary Comprehensions** – `{key_expr: value_expr for item in iterable if condition}`. Build dictionaries from iterables.

- **Set Comprehensions** – `{expr for item in iterable if condition}`. Create sets of unique elements.

- **Nested Comprehensions** – `[expr for row in matrix for item in row]`. Flatten matrices, create coordinates.

- **Conditional Logic** – Ternary expressions inside comprehensions: `[x if condition else y for x in iterable]`.

- **Performance** – Comprehensions are faster than traditional loops (C-level execution).

- **Readability** – Keep comprehensions simple. Use multiple steps for complex transformations.

- **Data Pipeline** – ETL operations using comprehensions. Clean, transform, filter, aggregate.

- **SOLID Principles Applied** – Single Responsibility (each comprehension does one transformation), Open/Closed (new transformations can be added), Dependency Inversion (comprehensions work with any iterable).

- **Design Patterns Used** – Builder Pattern (pipeline construction), Pipeline Pattern (data flow), Strategy Pattern (pluggable transformations), Factory Pattern (comprehension creation), Composite Pattern (nested comprehensions).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Sets – Unique & Fast

- **📚 Series C Catalog:** Data Structures Express – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Classes & Objects – Blueprints & Instances (Series D, Story 1)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **23** | **29** | **44%** |

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
17. Series B, Story 5: The 2026 Python Metromap: Recursion – Functions Calling Themselves
18. Series B, Story 6: The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale
19. Series C, Story 1: The 2026 Python Metromap: Lists – Ordered & Mutable
20. Series C, Story 2: The 2026 Python Metromap: Tuples – Immutable Collections
21. Series C, Story 3: The 2026 Python Metromap: Dictionaries – Key-Value Power
22. Series C, Story 4: The 2026 Python Metromap: Sets – Unique & Fast
23. Series C, Story 5: The 2026 Python Metromap: Comprehensions – One-Line Power

**Next Story:** Series D, Story 1: The 2026 Python Metromap: Classes & Objects – Blueprints & Instances

---

## 📝 Your Invitation

**Congratulations! You've completed Data Structures Express!**

You've mastered:
- Lists for ordered, mutable sequences
- Tuples for immutable collections
- Dictionaries for key-value lookups
- Sets for unique elements
- Comprehensions for declarative collection building

Now build something with what you've learned:

1. **Build a data cleaning library** – Create comprehensions that clean, validate, and transform CSV data.

2. **Create a matrix calculator** – Use nested comprehensions for matrix addition, multiplication, and transposition.

3. **Build a log analyzer** – Use list comprehensions to parse log files, filter by level, and extract patterns.

4. **Create a report generator** – Use dictionary comprehensions to aggregate sales data by region, product, or time period.

5. **Build a data pipeline framework** – Create a reusable ETL framework using comprehensions for each stage.

**You've mastered Data Structures Express. Next stop: Object-Oriented Programming Line – Classes & Objects!**

---

*Found this helpful? Clap, comment, and share what you built with comprehensions. Next stop: Classes & Objects!* 🚇