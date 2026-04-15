# The 2026 Python Metromap: Tuples – Immutable Collections

## Series C: Data Structures Express | Story 2 of 5

![The 2026 Python Metromap/images/Tuples – Immutable Collections](images/Tuples – Immutable Collections.png)

## 📖 Introduction

**Welcome to the second stop on the Data Structures Express Line.**

You've mastered lists—ordered, mutable sequences perfect for collections that change over time. But not all data should change. GPS coordinates shouldn't be modified accidentally. Database record identifiers should remain constant. Configuration settings should be fixed once defined. For these use cases, you need immutability.

That's where tuples come in.

Tuples are ordered, immutable sequences. Once created, they cannot be changed—no adding, no removing, no modifying elements. This immutability makes tuples perfect for fixed data: coordinates, RGB color values, database records, function return values, and configuration constants. They're also hashable, meaning they can be used as dictionary keys (unlike lists).

This story—**The 2026 Python Metromap: Tuples – Immutable Collections**—is your guide to mastering Python tuples. We'll explore tuple creation, unpacking, and named tuples. We'll build a GPS coordinate system for delivery routing. We'll create an immutable configuration manager for application settings. We'll implement a database record system using named tuples. And we'll build a complete immutable data pipeline that demonstrates the power of tuple-based programming.

**Let's lock it down.**

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

### Series B: Functions & Modules Yard (6 Stories) – COMPLETED

- 🔧 **Defining Functions** – Payment processing module; validation functions; error handling.
- 📋 **Arguments** – Flexible report generator for PDF, CSV, and JSON outputs.
- 📤 **Return Values** – API response formatter; standardized success and error responses.
- ⚡ **Lambda Functions** – Sorting custom objects; filtering data streams; mapping pipelines.
- 🔄 **Recursion** – Directory tree traversal; factorial calculations; Tower of Hanoi solver.
- 📦 **Modules & Packages** – Reusable utility library; multi-file project structure; publishing packages.

### Series C: Data Structures Express (5 Stories)

- 📋 **The 2026 Python Metromap: Lists – Ordered & Mutable** – Todo application; playlist manager; shopping cart system.

- 🔒 **The 2026 Python Metromap: Tuples – Immutable Collections** – GPS coordinates; database records; immutable configuration. **⬅️ YOU ARE HERE**

- 🔑 **The 2026 Python Metromap: Dictionaries – Key-Value Power** – User profile cache; product catalog; dependency injection container. 🔜 *Up Next*

- 🎯 **The 2026 Python Metromap: Sets – Unique & Fast** – Duplicate removal; friend recommendation engine; common visitor detection.

- 📝 **The 2026 Python Metromap: Comprehensions – One-Line Power** – Data transformation pipelines; filtered iterations; nested structure creation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔒 Section 1: Tuple Fundamentals – Creation, Access, and Immutability

Tuples are ordered, immutable sequences. Once created, they cannot be modified.

**SOLID Principle Applied: Interface Segregation** – Tuples provide only read-only operations, no modification methods.

**Design Pattern: Value Object Pattern** – Tuples are immutable value objects; equality based on content, not identity.

```python
"""
TUPLE FUNDAMENTALS: CREATION, ACCESS, AND IMMUTABILITY

This section covers the basics of creating, accessing, and using tuples.

SOLID Principle: Interface Segregation
- Tuples provide only read-only operations

Design Pattern: Value Object Pattern
- Immutable value objects; equality based on content
"""

from typing import Tuple, Any, Optional
import sys


def demonstrate_tuple_creation():
    """
    Demonstrates different ways to create tuples.
    
    Tuples are created with parentheses () or tuple() constructor.
    Single-element tuples need a trailing comma.
    """
    print("=" * 60)
    print("SECTION 1A: CREATING TUPLES")
    print("=" * 60)
    
    # EMPTY TUPLES
    print("\n1. CREATING EMPTY TUPLES")
    print("-" * 40)
    
    empty_parens = ()
    empty_constructor = tuple()
    
    print(f"  empty_parens: {empty_parens} (type: {type(empty_parens).__name__})")
    print(f"  empty_constructor: {empty_constructor}")
    
    # TUPLES WITH VALUES
    print("\n2. TUPLES WITH VALUES")
    print("-" * 40)
    
    coordinates = (10, 20)
    rgb = (255, 128, 0)
    mixed = (1, "hello", 3.14, True, None)
    
    print(f"  coordinates: {coordinates}")
    print(f"  rgb: {rgb}")
    print(f"  mixed: {mixed}")
    
    # SINGLE-ELEMENT TUPLES (NOTE THE COMMA!)
    print("\n3. SINGLE-ELEMENT TUPLES (IMPORTANT!)")
    print("-" * 40)
    
    single_element = (42,)  # With comma - this is a tuple
    not_a_tuple = (42)      # Without comma - just an integer
    
    print(f"  single_element: {single_element} (type: {type(single_element).__name__})")
    print(f"  not_a_tuple: {not_a_tuple} (type: {type(not_a_tuple).__name__})")
    
    # TUPLE PACKING (parentheses optional)
    print("\n4. TUPLE PACKING (parentheses optional)")
    print("-" * 40)
    
    packed = 1, 2, 3
    print(f"  packed: {packed} (type: {type(packed).__name__})")
    
    # TUPLES FROM OTHER ITERABLES
    print("\n5. TUPLES FROM OTHER ITERABLES")
    print("-" * 40)
    
    # From list
    from_list = tuple([1, 2, 3])
    print(f"  tuple([1, 2, 3]): {from_list}")
    
    # From string
    from_string = tuple("Python")
    print(f"  tuple('Python'): {from_string}")
    
    # From range
    from_range = tuple(range(5))
    print(f"  tuple(range(5)): {from_range}")
    
    # TUPLE COMPREHENSION? (Not directly - use generator expression)
    print("\n6. TUPLE COMPREHENSION (via generator)")
    print("-" * 40)
    
    # Generator expression converted to tuple
    squares = tuple(x ** 2 for x in range(10))
    print(f"  tuple(x**2 for x in range(10)): {squares}")


def demonstrate_tuple_access():
    """
    Demonstrates accessing elements in tuples.
    
    Tuples support the same indexing and slicing as lists.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ACCESSING TUPLE ELEMENTS")
    print("=" * 60)
    
    colors = ("red", "green", "blue", "yellow", "purple", "orange", "pink")
    
    print(f"  Tuple: {colors}")
    
    # POSITIVE INDEXING
    print("\n1. POSITIVE INDEXING (0-based)")
    print("-" * 40)
    
    print(f"  colors[0]: {colors[0]}  # First element")
    print(f"  colors[1]: {colors[1]}  # Second element")
    print(f"  colors[2]: {colors[2]}  # Third element")
    
    # NEGATIVE INDEXING
    print("\n2. NEGATIVE INDEXING (from end)")
    print("-" * 40)
    
    print(f"  colors[-1]: {colors[-1]}  # Last element")
    print(f"  colors[-2]: {colors[-2]}  # Second last")
    print(f"  colors[-3]: {colors[-3]}  # Third last")
    
    # SLICING
    print("\n3. SLICING [start:end:step]")
    print("-" * 40)
    
    print(f"  colors[1:4]: {colors[1:4]}      # Elements 1-3")
    print(f"  colors[:3]: {colors[:3]}        # First 3 elements")
    print(f"  colors[3:]: {colors[3:]}        # Elements from index 3")
    print(f"  colors[::2]: {colors[::2]}      # Every other element")
    print(f"  colors[::-1]: {colors[::-1]}    # Reversed tuple")
    
    # CHECKING EXISTENCE
    print("\n4. CHECKING EXISTENCE")
    print("-" * 40)
    
    print(f"  'blue' in colors: {'blue' in colors}")
    print(f"  'black' in colors: {'black' in colors}")
    print(f"  'red' not in colors: {'red' not in colors}")
    
    # FINDING INDEX
    print("\n5. FINDING INDEX")
    print("-" * 40)
    
    print(f"  colors.index('yellow'): {colors.index('yellow')}")
    
    # COUNTING OCCURRENCES
    print("\n6. COUNTING OCCURRENCES")
    print("-" * 40)
    
    duplicate_tuple = (1, 2, 3, 2, 4, 2, 5)
    print(f"  duplicate_tuple: {duplicate_tuple}")
    print(f"  duplicate_tuple.count(2): {duplicate_tuple.count(2)}")
    print(f"  duplicate_tuple.count(6): {duplicate_tuple.count(6)}")
    
    # LENGTH
    print("\n7. TUPLE LENGTH")
    print("-" * 40)
    
    print(f"  len(colors): {len(colors)}")
    print(f"  len(empty_tuple): {len(())}")


def demonstrate_tuple_immutability():
    """
    Demonstrates that tuples cannot be modified.
    
    This is the key difference between tuples and lists.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: TUPLE IMMUTABILITY")
    print("=" * 60)
    
    point = (10, 20)
    print(f"  Original tuple: {point}")
    
    # ATTEMPTING TO MODIFY (will raise TypeError)
    print("\n1. CANNOT MODIFY ELEMENTS")
    print("-" * 40)
    
    try:
        # This will raise TypeError
        point[0] = 99
    except TypeError as e:
        print(f"  Error: {e}")
    
    # ATTEMPTING TO ADD ELEMENTS
    print("\n2. CANNOT ADD ELEMENTS")
    print("-" * 40)
    
    try:
        # Tuples have no append method
        point.append(30)
    except AttributeError as e:
        print(f"  Error: {e}")
    
    # ATTEMPTING TO REMOVE ELEMENTS
    print("\n3. CANNOT REMOVE ELEMENTS")
    print("-" * 40)
    
    try:
        # Tuples have no remove method
        point.remove(10)
    except AttributeError as e:
        print(f"  Error: {e}")
    
    # WHY IMMUTABILITY MATTERS
    print("\n4. WHY IMMUTABILITY MATTERS")
    print("-" * 40)
    
    print("""
    Benefits of immutability:
    ✓ Thread-safe (no race conditions)
    ✓ Can be used as dictionary keys (hashable)
    ✓ More memory efficient
    ✓ Prevents accidental modification
    ✓ Easier to reason about (value never changes)
    """)
    
    # COMPARING LIST AND TUPLE MEMORY
    print("\n5. MEMORY EFFICIENCY")
    print("-" * 40)
    
    list_data = [1, 2, 3, 4, 5]
    tuple_data = (1, 2, 3, 4, 5)
    
    list_size = sys.getsizeof(list_data)
    tuple_size = sys.getsizeof(tuple_data)
    
    print(f"  List size: {list_size} bytes")
    print(f"  Tuple size: {tuple_size} bytes")
    print(f"  Tuple is {list_size - tuple_size} bytes smaller!")


def demonstrate_tuple_operations():
    """
    Demonstrates operations that work with tuples.
    
    Even though tuples are immutable, some operations create new tuples.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: TUPLE OPERATIONS")
    print("=" * 60)
    
    # CONCATENATION (creates new tuple)
    print("\n1. CONCATENATION (+)")
    print("-" * 40)
    
    tuple_a = (1, 2, 3)
    tuple_b = (4, 5, 6)
    
    tuple_c = tuple_a + tuple_b
    print(f"  {tuple_a} + {tuple_b} = {tuple_c}")
    print(f"  Original tuple_a: {tuple_a} (unchanged)")
    
    # REPETITION (creates new tuple)
    print("\n2. REPETITION (*)")
    print("-" * 40)
    
    pattern = (1, 2)
    repeated = pattern * 3
    print(f"  {pattern} * 3 = {repeated}")
    
    # COMPARISON
    print("\n3. COMPARISON")
    print("-" * 40)
    
    print(f"  (1, 2, 3) == (1, 2, 3): {(1, 2, 3) == (1, 2, 3)}")
    print(f"  (1, 2, 3) == (1, 2, 4): {(1, 2, 3) == (1, 2, 4)}")
    print(f"  (1, 2) < (1, 2, 3): {(1, 2) < (1, 2, 3)}")
    print(f"  (1, 2, 3) > (1, 2): {(1, 2, 3) > (1, 2)}")
    
    # USING TUPLES AS DICTIONARY KEYS
    print("\n4. TUPLES AS DICTIONARY KEYS (lists cannot!)")
    print("-" * 40)
    
    # Dictionary with tuple keys
    coordinates = {
        (0, 0): "Origin",
        (1, 0): "East",
        (0, 1): "North",
        (-1, 0): "West",
        (0, -1): "South"
    }
    
    print(f"  coordinates[(0, 0)]: {coordinates[(0, 0)]}")
    print(f"  coordinates[(1, 0)]: {coordinates[(1, 0)]}")
    
    # This would fail with lists (unhashable type)
    try:
        bad_dict = {[1, 2]: "value"}
    except TypeError as e:
        print(f"\n  Error: {e} (lists cannot be dictionary keys)")


def demonstrate_tuple_unpacking():
    """
    Demonstrates tuple unpacking for elegant variable assignment.
    
    Unpacking is one of Python's most elegant features.
    """
    print("\n" + "=" * 60)
    print("SECTION 1E: TUPLE UNPACKING")
    print("=" * 60)
    
    # BASIC UNPACKING
    print("\n1. BASIC UNPACKING")
    print("-" * 40)
    
    point = (10, 20)
    x, y = point
    print(f"  point = {point}")
    print(f"  x = {x}, y = {y}")
    
    # UNPACKING FROM FUNCTION RETURN
    print("\n2. UNPACKING FROM FUNCTION RETURN")
    print("-" * 40)
    
    def get_min_max(numbers):
        """Return both min and max as a tuple."""
        return min(numbers), max(numbers)
    
    min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2])
    print(f"  min = {min_val}, max = {max_val}")
    
    # SWAPPING VARIABLES (elegant!)
    print("\n3. SWAPPING VARIABLES")
    print("-" * 40)
    
    a, b = 5, 10
    print(f"  Before: a = {a}, b = {b}")
    
    a, b = b, a  # Swap using tuple unpacking
    print(f"  After: a = {a}, b = {b}")
    
    # EXTENDED UNPACKING (*)
    print("\n4. EXTENDED UNPACKING (*)")
    print("-" * 40)
    
    numbers = (1, 2, 3, 4, 5)
    
    first, *rest = numbers
    print(f"  first = {first}, rest = {rest}")
    
    *rest, last = numbers
    print(f"  rest = {rest}, last = {last}")
    
    first, *middle, last = numbers
    print(f"  first = {first}, middle = {middle}, last = {last}")
    
    # IGNORING VALUES WITH _
    print("\n5. IGNORING VALUES")
    print("-" * 40)
    
    data = (10, 20, 30, 40, 50)
    first, second, *_, last = data
    print(f"  data = {data}")
    print(f"  first = {first}, second = {second}, last = {last}")
    
    # UNPACKING NESTED TUPLES
    print("\n6. UNPACKING NESTED TUPLES")
    print("-" * 40)
    
    nested = ((1, 2), (3, 4), (5, 6))
    
    for a, b in nested:
        print(f"  a = {a}, b = {b}")
    
    # DEEP UNPACKING
    print("\n7. DEEP UNPACKING")
    print("-" * 40)
    
    person = ("Alice", 28, ("New York", "NY", "10001"))
    name, age, (city, state, zipcode) = person
    print(f"  name = {name}, age = {age}")
    print(f"  city = {city}, state = {state}, zip = {zipcode}")


if __name__ == "__main__":
    demonstrate_tuple_creation()
    demonstrate_tuple_access()
    demonstrate_tuple_immutability()
    demonstrate_tuple_operations()
    demonstrate_tuple_unpacking()
```

---

## 📛 Section 2: Named Tuples – Self-Documenting Tuples

Named tuples give field names to tuple elements, making code more readable and self-documenting.

**SOLID Principle Applied: Interface Segregation** – Named tuples provide named field access alongside positional access.

**Design Pattern: Value Object Pattern** – Named tuples are immutable value objects with named fields.

```python
"""
NAMED TUPLES: SELF-DOCUMENTING TUPLES

This section covers namedtuple for creating self-documenting tuples.

SOLID Principle: Interface Segregation
- Named tuples provide named field access

Design Pattern: Value Object Pattern
- Immutable value objects with named fields
"""

from typing import List, Dict, Any, Optional
from collections import namedtuple
from dataclasses import dataclass
import sys


def demonstrate_namedtuple_basics():
    """
    Demonstrates creating and using named tuples.
    
    namedtuple creates a tuple subclass with named fields.
    """
    print("=" * 60)
    print("SECTION 2A: NAMEDTUPLE BASICS")
    print("=" * 60)
    
    # CREATING A NAMEDTUPLE CLASS
    print("\n1. CREATING A NAMEDTUPLE CLASS")
    print("-" * 40)
    
    # Syntax: namedtuple('ClassName', ['field1', 'field2', ...])
    Point = namedtuple('Point', ['x', 'y'])
    RGB = namedtuple('RGB', ['red', 'green', 'blue'])
    Person = namedtuple('Person', ['name', 'age', 'city'])
    
    print("  Defined Point, RGB, and Person namedtuple classes")
    
    # CREATING INSTANCES
    print("\n2. CREATING INSTANCES")
    print("-" * 40)
    
    # Positional arguments
    p1 = Point(10, 20)
    print(f"  Point(10, 20): {p1}")
    
    # Keyword arguments (more readable!)
    p2 = Point(x=30, y=40)
    print(f"  Point(x=30, y=40): {p2}")
    
    color = RGB(red=255, green=128, blue=0)
    print(f"  RGB(red=255, green=128, blue=0): {color}")
    
    person = Person(name="Alice", age=28, city="New York")
    print(f"  Person(name='Alice', age=28, city='New York'): {person}")
    
    # ACCESSING FIELDS
    print("\n3. ACCESSING FIELDS")
    print("-" * 40)
    
    # By index (tuple-style)
    print(f"  p1[0] (x): {p1[0]}, p1[1] (y): {p1[1]}")
    
    # By name (self-documenting!)
    print(f"  p1.x: {p1.x}, p1.y: {p1.y}")
    print(f"  color.red: {color.red}, color.blue: {color.blue}")
    print(f"  person.name: {person.name}, person.age: {person.age}")
    
    # COMPARISON
    print("\n4. COMPARISON")
    print("-" * 40)
    
    p3 = Point(10, 20)
    p4 = Point(15, 25)
    
    print(f"  p1 == p3: {p1 == p3}")
    print(f"  p1 == p4: {p1 == p4}")
    
    # CONVERSION TO DICTIONARY
    print("\n5. CONVERSION TO DICTIONARY (_asdict())")
    print("-" * 40)
    
    as_dict = person._asdict()
    print(f"  person._asdict(): {as_dict}")
    
    # CREATING NEW INSTANCE WITH REPLACED FIELDS
    print("\n6. CREATING NEW INSTANCE (_replace())")
    print("-" * 40)
    
    older_person = person._replace(age=29)
    print(f"  Original: {person}")
    print(f"  Modified: {older_person}")
    print(f"  Original unchanged: {person}")
    
    # GETTING FIELD NAMES
    print("\n7. GETTING FIELD NAMES (_fields)")
    print("-" * 40)
    
    print(f"  Point._fields: {Point._fields}")
    print(f"  Person._fields: {Person._fields}")
    
    # DEFAULT VALUES (using __defaults__)
    print("\n8. DEFAULT VALUES")
    print("-" * 40)
    
    # Create namedtuple with defaults (Python 3.7+)
    Product = namedtuple('Product', ['name', 'price', 'in_stock'], defaults=['Unknown', 0.0, True])
    
    product1 = Product("Laptop")
    product2 = Product("Mouse", 29.99)
    product3 = Product("Keyboard", 89.99, True)
    
    print(f"  Product with only name: {product1}")
    print(f"  Product with name and price: {product2}")
    print(f"  Product with all fields: {product3}")


def demonstrate_namedtuple_methods():
    """
    Demonstrates advanced namedtuple methods and patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: NAMEDTUPLE METHODS AND PATTERNS")
    print("=" * 60)
    
    # CREATING FROM LIST OR TUPLE
    print("\n1. CREATING FROM SEQUENCE (_make())")
    print("-" * 40)
    
    Point = namedtuple('Point', ['x', 'y'])
    
    data = [10, 20]
    point = Point._make(data)
    print(f"  Point._make([10, 20]): {point}")
    
    # CONVERTING TO LIST
    print("\n2. CONVERTING TO LIST (_asdict() then list)")
    print("-" * 40)
    
    person = namedtuple('Person', ['name', 'age'])("Alice", 28)
    as_list = list(person)
    print(f"  list(person): {as_list}")
    
    # NAMEDTUPLES IN DATA STRUCTURES
    print("\n3. NAMEDTUPLES IN LISTS")
    print("-" * 40)
    
    Stock = namedtuple('Stock', ['symbol', 'price', 'volume'])
    
    portfolio = [
        Stock("AAPL", 175.50, 1000),
        Stock("GOOGL", 140.25, 500),
        Stock("MSFT", 330.75, 800),
        Stock("AMZN", 145.00, 600)
    ]
    
    print("  Portfolio:")
    for stock in portfolio:
        print(f"    {stock.symbol}: ${stock.price:.2f} ({stock.volume} shares)")
    
    # Sorting namedtuples
    by_price = sorted(portfolio, key=lambda s: s.price, reverse=True)
    print("\n  Sorted by price (highest first):")
    for stock in by_price:
        print(f"    {stock.symbol}: ${stock.price:.2f}")
    
    # Filtering namedtuples
    high_volume = [s for s in portfolio if s.volume > 700]
    print("\n  High volume stocks (>700):")
    for stock in high_volume:
        print(f"    {stock.symbol}: {stock.volume} shares")
    
    # NAMEDTUPLE VS REGULAR TUPLE
    print("\n4. NAMEDTUPLE VS REGULAR TUPLE")
    print("-" * 40)
    
    # Regular tuple (hard to understand)
    employee1 = ("Alice", 28, "Engineer", 85000)
    
    # Named tuple (self-documenting)
    Employee = namedtuple('Employee', ['name', 'age', 'title', 'salary'])
    employee2 = Employee(name="Alice", age=28, title="Engineer", salary=85000)
    
    print("  Regular tuple: employee1[2] = ? (needs documentation)")
    print("  Named tuple: employee2.title = 'Engineer' (self-documenting)")
    
    # NAMEDTUPLE VS DATACLASS
    print("\n5. NAMEDTUPLE VS DATACLASS")
    print("-" * 40)
    
    @dataclass
    class EmployeeDataClass:
        name: str
        age: int
        title: str
        salary: float
    
    # Memory comparison
    nt = Employee("Bob", 35, "Manager", 95000)
    dc = EmployeeDataClass("Bob", 35, "Manager", 95000)
    
    nt_size = sys.getsizeof(nt)
    dc_size = sys.getsizeof(dc) + sum(sys.getsizeof(v) for v in dc.__dict__.values())
    
    print(f"  Namedtuple size: ~{nt_size} bytes")
    print(f"  Dataclass size: ~{dc_size} bytes")
    print("  Namedtuples are more memory efficient!")
    
    print("\n  When to use namedtuple:")
    print("    ✓ Simple data containers")
    print("    ✓ Memory-efficient storage")
    print("    ✓ When you need tuple behavior (iterable, hashable)")
    print("    ✓ When fields are fixed and known at creation")
    
    print("\n  When to use dataclass:")
    print("    ✓ Need mutable fields")
    print("    ✓ Need methods beyond simple access")
    print("    ✓ Need default factories (lists, dicts)")
    print("    ✓ Need inheritance and complex behavior")


def demonstrate_practical_namedtuple():
    """
    Demonstrates practical uses of namedtuple.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: PRACTICAL NAMEDTUPLE USES")
    print("=" * 60)
    
    # USE CASE 1: CSV DATA PROCESSING
    print("\n1. CSV DATA PROCESSING")
    print("-" * 40)
    
    # Define record structure
    SalesRecord = namedtuple('SalesRecord', ['date', 'product', 'quantity', 'price', 'region'])
    
    # Simulate CSV data
    csv_data = [
        ("2024-01-01", "Laptop", 2, 999.99, "North"),
        ("2024-01-02", "Mouse", 5, 25.00, "South"),
        ("2024-01-03", "Laptop", 1, 999.99, "East"),
        ("2024-01-04", "Keyboard", 3, 75.00, "West"),
        ("2024-01-05", "Mouse", 10, 25.00, "North")
    ]
    
    # Convert to namedtuples
    records = [SalesRecord._make(row) for row in csv_data]
    
    # Process data using named fields
    total_revenue = sum(r.quantity * r.price for r in records)
    laptop_sales = sum(r.quantity for r in records if r.product == "Laptop")
    north_sales = sum(r.quantity for r in records if r.region == "North")
    
    print(f"  Total revenue: ${total_revenue:,.2f}")
    print(f"  Laptop units sold: {laptop_sales}")
    print(f"  North region units: {north_sales}")
    
    # Group by product using named fields
    product_totals = {}
    for record in records:
        product_totals[record.product] = product_totals.get(record.product, 0) + record.quantity
    
    print(f"  Sales by product: {product_totals}")
    
    # USE CASE 2: API RESPONSE PARSING
    print("\n2. API RESPONSE PARSING")
    print("-" * 40)
    
    # Simulated API response
    api_response = {
        "user": {
            "id": 12345,
            "name": "Alice Chen",
            "email": "alice@example.com"
        },
        "status": "success",
        "code": 200
    }
    
    # Define response structure
    ApiResponse = namedtuple('ApiResponse', ['user_id', 'user_name', 'user_email', 'status', 'code'])
    
    # Parse response into namedtuple
    parsed = ApiResponse(
        user_id=api_response["user"]["id"],
        user_name=api_response["user"]["name"],
        user_email=api_response["user"]["email"],
        status=api_response["status"],
        code=api_response["code"]
    )
    
    print(f"  Response: {parsed}")
    print(f"  User ID: {parsed.user_id}")
    print(f"  User Name: {parsed.user_name}")
    print(f"  Status: {parsed.status}")
    
    # USE CASE 3: FUNCTION RETURN VALUES
    print("\n3. FUNCTION RETURN VALUES")
    print("-" * 40)
    
    # Instead of returning a tuple (hard to understand)
    def analyze_data_bad(data):
        """Returns (mean, median, mode, std_dev)"""
        # ... calculations ...
        return (10.5, 10.0, 8.0, 3.2)  # What's what?
    
    # With namedtuple (self-documenting)
    Statistics = namedtuple('Statistics', ['mean', 'median', 'mode', 'std_dev'])
    
    def analyze_data_good(data):
        """Returns Statistics with mean, median, mode, std_dev"""
        # ... calculations ...
        return Statistics(mean=10.5, median=10.0, mode=8.0, std_dev=3.2)
    
    result = analyze_data_good([1, 2, 3, 4, 5])
    print(f"  Mean: {result.mean}")
    print(f"  Median: {result.median}")
    print(f"  Mode: {result.mode}")
    print(f"  Std Dev: {result.std_dev}")
    
    # USE CASE 4: CONFIGURATION CONSTANTS
    print("\n4. CONFIGURATION CONSTANTS")
    print("-" * 40)
    
    DatabaseConfig = namedtuple('DatabaseConfig', ['host', 'port', 'database', 'user', 'timeout'])
    
    DB_CONFIG = DatabaseConfig(
        host="localhost",
        port=5432,
        database="myapp",
        user="app_user",
        timeout=30
    )
    
    print(f"  DB_HOST: {DB_CONFIG.host}")
    print(f"  DB_PORT: {DB_CONFIG.port}")
    print(f"  DB_NAME: {DB_CONFIG.database}")
    
    # IMMUTABILITY BENEFIT
    print("\n5. IMMUTABILITY IN ACTION")
    print("-" * 40)
    
    try:
        DB_CONFIG.host = "remotehost"  # This will fail!
    except AttributeError as e:
        print(f"  Cannot modify config: {e}")
    print("  Configuration remains constant - safe from accidental changes!")


if __name__ == "__main__":
    demonstrate_namedtuple_basics()
    demonstrate_namedtuple_methods()
    demonstrate_practical_namedtuple()
```

---

## 🗺️ Section 3: GPS Coordinate System

A complete GPS coordinate system using tuples for immutable location data.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of coordinate management
- Open/Closed: New coordinate operations can be added

**Design Patterns:**
- Value Object Pattern: Coordinates are immutable value objects
- Factory Pattern: Creates coordinate objects from different formats

```python
"""
GPS COORDINATE SYSTEM

This section builds a complete GPS coordinate system using tuples.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New operations can be added

Design Patterns:
- Value Object Pattern: Immutable coordinate objects
- Factory Pattern: Creates coordinates from different formats
"""

from typing import Tuple, List, Optional, Dict, Any
from math import radians, sin, cos, sqrt, atan2
from dataclasses import dataclass
from collections import namedtuple
import json


# Basic coordinate as a tuple
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])


class GPSCoordinate:
    """
    Immutable GPS coordinate using tuple internally.
    
    Design Pattern: Value Object Pattern - Immutable by design
    """
    
    def __init__(self, latitude: float, longitude: float):
        """
        Initialize a GPS coordinate.
        
        Args:
            latitude: Latitude in degrees (-90 to 90)
            longitude: Longitude in degrees (-180 to 180)
        """
        self._validate_coordinate(latitude, longitude)
        self._coord = Coordinate(latitude, longitude)
    
    def _validate_coordinate(self, lat: float, lon: float) -> None:
        """Validate coordinate ranges."""
        if not -90 <= lat <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {lat}")
        if not -180 <= lon <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {lon}")
    
    @property
    def latitude(self) -> float:
        """Get latitude."""
        return self._coord.latitude
    
    @property
    def longitude(self) -> float:
        """Get longitude."""
        return self._coord.longitude
    
    def to_tuple(self) -> Tuple[float, float]:
        """Convert to tuple."""
        return (self.latitude, self.longitude)
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary."""
        return {"latitude": self.latitude, "longitude": self.longitude}
    
    def distance_to(self, other: 'GPSCoordinate') -> float:
        """
        Calculate distance to another coordinate using Haversine formula.
        
        Args:
            other: Another GPSCoordinate
            
        Returns:
            Distance in kilometers
        """
        R = 6371  # Earth's radius in kilometers
        
        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)
        lat2 = radians(other.latitude)
        lon2 = radians(other.longitude)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        return R * c
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, GPSCoordinate):
            return False
        return self._coord == other._coord
    
    def __hash__(self) -> int:
        return hash(self._coord)
    
    def __repr__(self) -> str:
        return f"GPSCoordinate({self.latitude}, {self.longitude})"
    
    def __str__(self) -> str:
        # Format: 40° 42' 51.6" N, 74° 0' 21.6" W
        lat_dir = "N" if self.latitude >= 0 else "S"
        lon_dir = "E" if self.longitude >= 0 else "W"
        
        lat_abs = abs(self.latitude)
        lon_abs = abs(self.longitude)
        
        lat_deg = int(lat_abs)
        lat_min = int((lat_abs - lat_deg) * 60)
        lat_sec = (lat_abs - lat_deg - lat_min / 60) * 3600
        
        lon_deg = int(lon_abs)
        lon_min = int((lon_abs - lon_deg) * 60)
        lon_sec = (lon_abs - lon_deg - lon_min / 60) * 3600
        
        return f"{lat_deg}° {lat_min}' {lat_sec:.1f}\" {lat_dir}, {lon_deg}° {lon_min}' {lon_sec:.1f}\" {lon_dir}"


class CoordinateFactory:
    """
    Factory for creating coordinates from various formats.
    
    Design Pattern: Factory Pattern - Creates coordinates from different sources
    """
    
    @staticmethod
    def from_decimal(lat: float, lon: float) -> GPSCoordinate:
        """Create coordinate from decimal degrees."""
        return GPSCoordinate(lat, lon)
    
    @staticmethod
    def from_dms(lat_deg: int, lat_min: int, lat_sec: float, lat_dir: str,
                 lon_deg: int, lon_min: int, lon_sec: float, lon_dir: str) -> GPSCoordinate:
        """Create coordinate from degrees, minutes, seconds."""
        lat = lat_deg + lat_min / 60 + lat_sec / 3600
        lon = lon_deg + lon_min / 60 + lon_sec / 3600
        
        if lat_dir.upper() == 'S':
            lat = -lat
        if lon_dir.upper() == 'W':
            lon = -lon
        
        return GPSCoordinate(lat, lon)
    
    @staticmethod
    def from_tuple(coord_tuple: Tuple[float, float]) -> GPSCoordinate:
        """Create coordinate from tuple."""
        return GPSCoordinate(coord_tuple[0], coord_tuple[1])
    
    @staticmethod
    def from_dict(coord_dict: Dict[str, float]) -> GPSCoordinate:
        """Create coordinate from dictionary."""
        return GPSCoordinate(coord_dict['latitude'], coord_dict['longitude'])


class Route:
    """
    Route consisting of multiple waypoints.
    
    Design Pattern: Composite Pattern - Route contains multiple coordinates
    """
    
    def __init__(self, name: str):
        self.name = name
        self.waypoints: List[GPSCoordinate] = []
    
    def add_waypoint(self, coordinate: GPSCoordinate) -> 'Route':
        """Add a waypoint to the route."""
        self.waypoints.append(coordinate)
        return self
    
    def total_distance(self) -> float:
        """Calculate total route distance in kilometers."""
        if len(self.waypoints) < 2:
            return 0.0
        
        total = 0.0
        for i in range(len(self.waypoints) - 1):
            total += self.waypoints[i].distance_to(self.waypoints[i + 1])
        return total
    
    def get_bounds(self) -> Tuple[GPSCoordinate, GPSCoordinate]:
        """Get bounding box of the route."""
        if not self.waypoints:
            raise ValueError("Route has no waypoints")
        
        lats = [w.latitude for w in self.waypoints]
        lons = [w.longitude for w in self.waypoints]
        
        min_coord = GPSCoordinate(min(lats), min(lons))
        max_coord = GPSCoordinate(max(lats), max(lons))
        
        return min_coord, max_coord
    
    def get_center(self) -> GPSCoordinate:
        """Get center of the route."""
        min_coord, max_coord = self.get_bounds()
        center_lat = (min_coord.latitude + max_coord.latitude) / 2
        center_lon = (min_coord.longitude + max_coord.longitude) / 2
        return GPSCoordinate(center_lat, center_lon)
    
    def __len__(self) -> int:
        return len(self.waypoints)
    
    def __getitem__(self, index: int) -> GPSCoordinate:
        return self.waypoints[index]
    
    def __iter__(self):
        return iter(self.waypoints)
    
    def __repr__(self) -> str:
        return f"Route('{self.name}', {len(self.waypoints)} waypoints)"


class DeliveryRouteOptimizer:
    """
    Optimizes delivery routes using coordinate calculations.
    
    Design Pattern: Strategy Pattern - Different optimization strategies
    """
    
    def __init__(self):
        self.warehouse: Optional[GPSCoordinate] = None
        self.delivery_points: List[GPSCoordinate] = []
    
    def set_warehouse(self, coordinate: GPSCoordinate) -> 'DeliveryRouteOptimizer':
        """Set warehouse location."""
        self.warehouse = coordinate
        return self
    
    def add_delivery_point(self, coordinate: GPSCoordinate) -> 'DeliveryRouteOptimizer':
        """Add a delivery point."""
        self.delivery_points.append(coordinate)
        return self
    
    def nearest_neighbor_route(self) -> Route:
        """
        Optimize route using nearest neighbor algorithm.
        
        Returns:
            Route starting from warehouse visiting all points
        """
        if not self.warehouse:
            raise ValueError("Warehouse not set")
        
        if not self.delivery_points:
            raise ValueError("No delivery points")
        
        unvisited = self.delivery_points.copy()
        route = Route("Optimized Delivery Route")
        current = self.warehouse
        route.add_waypoint(current)
        
        while unvisited:
            # Find nearest unvisited point
            nearest = min(unvisited, key=lambda p: current.distance_to(p))
            route.add_waypoint(nearest)
            current = nearest
            unvisited.remove(nearest)
        
        # Return to warehouse
        route.add_waypoint(self.warehouse)
        
        return route
    
    def route_by_region(self) -> Dict[str, Route]:
        """Group deliveries by geographic region."""
        if not self.delivery_points:
            return {}
        
        # Simple region classification by latitude bands
        regions = {
            "north": [],
            "central": [],
            "south": []
        }
        
        for point in self.delivery_points:
            if point.latitude > 40:
                regions["north"].append(point)
            elif point.latitude < 30:
                regions["south"].append(point)
            else:
                regions["central"].append(point)
        
        routes = {}
        for region_name, points in regions.items():
            if points:
                route = Route(f"{region_name.capitalize()} Region Route")
                # Sort by distance from warehouse if available
                if self.warehouse:
                    points.sort(key=lambda p: self.warehouse.distance_to(p))
                for point in points:
                    route.add_waypoint(point)
                routes[region_name] = route
        
        return routes
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get delivery statistics."""
        if not self.delivery_points:
            return {"error": "No delivery points"}
        
        distances_from_warehouse = []
        if self.warehouse:
            distances_from_warehouse = [self.warehouse.distance_to(p) for p in self.delivery_points]
        
        return {
            "total_deliveries": len(self.delivery_points),
            "avg_distance_from_warehouse": sum(distances_from_warehouse) / len(distances_from_warehouse) if distances_from_warehouse else 0,
            "min_distance": min(distances_from_warehouse) if distances_from_warehouse else 0,
            "max_distance": max(distances_from_warehouse) if distances_from_warehouse else 0,
            "warehouse_set": self.warehouse is not None
        }


def demonstrate_gps_system():
    """
    Demonstrate the GPS coordinate system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: GPS COORDINATE SYSTEM")
    print("=" * 60)
    
    # Create coordinates
    print("\n1. CREATING COORDINATES")
    print("-" * 40)
    
    # Using factory
    nyc = CoordinateFactory.from_decimal(40.7128, -74.0060)
    la = CoordinateFactory.from_decimal(34.0522, -118.2437)
    chicago = CoordinateFactory.from_decimal(41.8781, -87.6298)
    houston = CoordinateFactory.from_decimal(29.7604, -95.3698)
    phoenix = CoordinateFactory.from_decimal(33.4484, -112.0740)
    
    print(f"  New York: {nyc}")
    print(f"  Los Angeles: {la}")
    print(f"  Chicago: {chicago}")
    print(f"  Houston: {houston}")
    print(f"  Phoenix: {phoenix}")
    
    # Calculate distances
    print("\n2. CALCULATING DISTANCES")
    print("-" * 40)
    
    nyc_to_la = nyc.distance_to(la)
    nyc_to_chicago = nyc.distance_to(chicago)
    la_to_phoenix = la.distance_to(phoenix)
    
    print(f"  NYC to LA: {nyc_to_la:.1f} km ({nyc_to_la * 0.6214:.1f} miles)")
    print(f"  NYC to Chicago: {nyc_to_chicago:.1f} km")
    print(f"  LA to Phoenix: {la_to_phoenix:.1f} km")
    
    # Create delivery optimizer
    print("\n3. DELIVERY ROUTE OPTIMIZATION")
    print("-" * 40)
    
    optimizer = DeliveryRouteOptimizer()
    optimizer.set_warehouse(nyc)
    optimizer.add_delivery_point(chicago)
    optimizer.add_delivery_point(houston)
    optimizer.add_delivery_point(phoenix)
    optimizer.add_delivery_point(la)
    
    stats = optimizer.get_statistics()
    print(f"  Statistics:")
    print(f"    Total deliveries: {stats['total_deliveries']}")
    print(f"    Avg distance from warehouse: {stats['avg_distance_from_warehouse']:.1f} km")
    
    # Optimized route
    print("\n4. NEAREST NEIGHBOR ROUTE")
    print("-" * 40)
    
    optimized_route = optimizer.nearest_neighbor_route()
    print(f"  Route: {optimized_route.name}")
    print(f"  Waypoints: {len(optimized_route)}")
    print(f"  Total distance: {optimized_route.total_distance():.1f} km")
    
    # Show waypoints
    print("  Waypoints:")
    for i, wp in enumerate(optimized_route):
        print(f"    {i}: {wp}")
    
    # Region-based routing
    print("\n5. REGION-BASED ROUTING")
    print("-" * 40)
    
    region_routes = optimizer.route_by_region()
    for region, route in region_routes.items():
        print(f"  {region.capitalize()} region: {len(route)} deliveries")
    
    # Bounding box
    print("\n6. ROUTE BOUNDING BOX")
    print("-" * 40)
    
    min_coord, max_coord = optimized_route.get_bounds()
    center = optimized_route.get_center()
    
    print(f"  Min coordinate: {min_coord}")
    print(f"  Max coordinate: {max_coord}")
    print(f"  Center: {center}")
    
    # Using coordinates as dictionary keys
    print("\n7. COORDINATES AS DICTIONARY KEYS (Hashable!)")
    print("-" * 40)
    
    city_coordinates = {
        nyc: "New York City",
        la: "Los Angeles",
        chicago: "Chicago"
    }
    
    for coord, city in city_coordinates.items():
        print(f"  {city}: {coord}")


if __name__ == "__main__":
    demonstrate_gps_system()
```

---

## 💾 Section 4: Immutable Configuration System

A complete immutable configuration system using tuples for application settings.

**SOLID Principles Applied:**
- Single Responsibility: Configuration is separate from business logic
- Interface Segregation: Read-only access to config values

**Design Patterns:**
- Singleton Pattern: Single source of truth for config
- Value Object Pattern: Immutable configuration values
- Builder Pattern: Builds configuration from multiple sources

```python
"""
IMMUTABLE CONFIGURATION SYSTEM

This section builds an immutable configuration system using tuples.

SOLID Principles Applied:
- Single Responsibility: Configuration separate from business logic
- Interface Segregation: Read-only access to config values

Design Patterns:
- Singleton Pattern: Single source of truth for config
- Value Object Pattern: Immutable configuration values
- Builder Pattern: Builds config from multiple sources
"""

from typing import Dict, Any, Optional, List, Tuple
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
import os
import json


# Configuration as namedtuple
DatabaseConfig = namedtuple('DatabaseConfig', [
    'host', 'port', 'database', 'user', 'password', 'pool_size', 'timeout'
])

APIConfig = namedtuple('APIConfig', [
    'base_url', 'api_key', 'timeout', 'max_retries', 'rate_limit'
])

CacheConfig = namedtuple('CacheConfig', [
    'enabled', 'ttl_seconds', 'max_size', 'redis_host', 'redis_port'
])

LoggingConfig = namedtuple('LoggingConfig', [
    'level', 'format', 'file_path', 'max_bytes', 'backup_count'
])

FeatureFlags = namedtuple('FeatureFlags', [
    'dark_mode', 'beta_features', 'analytics', 'debug_mode', 'cache_enabled'
])


class Environment(Enum):
    """Environment types."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class ConfigBuilder:
    """
    Builder for creating immutable configuration.
    
    Design Pattern: Builder Pattern - Builds config incrementally
    """
    
    def __init__(self):
        self._database = None
        self._api = None
        self._cache = None
        self._logging = None
        self._features = None
        self._environment = Environment.DEVELOPMENT
    
    def set_database(self, host: str = "localhost", port: int = 5432,
                     database: str = "app", user: str = "postgres",
                     password: str = "", pool_size: int = 10,
                     timeout: int = 30) -> 'ConfigBuilder':
        """Set database configuration."""
        self._database = DatabaseConfig(
            host=host, port=port, database=database,
            user=user, password=password, pool_size=pool_size,
            timeout=timeout
        )
        return self
    
    def set_api(self, base_url: str = "https://api.example.com",
                api_key: str = "", timeout: int = 30,
                max_retries: int = 3, rate_limit: int = 100) -> 'ConfigBuilder':
        """Set API configuration."""
        self._api = APIConfig(
            base_url=base_url, api_key=api_key, timeout=timeout,
            max_retries=max_retries, rate_limit=rate_limit
        )
        return self
    
    def set_cache(self, enabled: bool = True, ttl_seconds: int = 300,
                  max_size: int = 1000, redis_host: str = "localhost",
                  redis_port: int = 6379) -> 'ConfigBuilder':
        """Set cache configuration."""
        self._cache = CacheConfig(
            enabled=enabled, ttl_seconds=ttl_seconds, max_size=max_size,
            redis_host=redis_host, redis_port=redis_port
        )
        return self
    
    def set_logging(self, level: str = "INFO",
                    format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    file_path: str = "app.log", max_bytes: int = 10485760,
                    backup_count: int = 5) -> 'ConfigBuilder':
        """Set logging configuration."""
        self._logging = LoggingConfig(
            level=level, format=format_str, file_path=file_path,
            max_bytes=max_bytes, backup_count=backup_count
        )
        return self
    
    def set_features(self, dark_mode: bool = False, beta_features: bool = False,
                     analytics: bool = True, debug_mode: bool = False,
                     cache_enabled: bool = True) -> 'ConfigBuilder':
        """Set feature flags."""
        self._features = FeatureFlags(
            dark_mode=dark_mode, beta_features=beta_features,
            analytics=analytics, debug_mode=debug_mode,
            cache_enabled=cache_enabled
        )
        return self
    
    def set_environment(self, env: Environment) -> 'ConfigBuilder':
        """Set environment."""
        self._environment = env
        return self
    
    def from_env_vars(self) -> 'ConfigBuilder':
        """Load configuration from environment variables."""
        # Database
        self._database = DatabaseConfig(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            database=os.getenv("DB_NAME", "app"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
            pool_size=int(os.getenv("DB_POOL_SIZE", "10")),
            timeout=int(os.getenv("DB_TIMEOUT", "30"))
        )
        
        # API
        self._api = APIConfig(
            base_url=os.getenv("API_BASE_URL", "https://api.example.com"),
            api_key=os.getenv("API_KEY", ""),
            timeout=int(os.getenv("API_TIMEOUT", "30")),
            max_retries=int(os.getenv("API_MAX_RETRIES", "3")),
            rate_limit=int(os.getenv("API_RATE_LIMIT", "100"))
        )
        
        # Environment
        env_map = {
            "development": Environment.DEVELOPMENT,
            "staging": Environment.STAGING,
            "production": Environment.PRODUCTION,
            "testing": Environment.TESTING
        }
        env_str = os.getenv("ENVIRONMENT", "development").lower()
        self._environment = env_map.get(env_str, Environment.DEVELOPMENT)
        
        return self
    
    def from_json_file(self, filepath: str) -> 'ConfigBuilder':
        """Load configuration from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if "database" in data:
            db = data["database"]
            self._database = DatabaseConfig(
                host=db.get("host", "localhost"),
                port=db.get("port", 5432),
                database=db.get("database", "app"),
                user=db.get("user", "postgres"),
                password=db.get("password", ""),
                pool_size=db.get("pool_size", 10),
                timeout=db.get("timeout", 30)
            )
        
        if "api" in data:
            api = data["api"]
            self._api = APIConfig(
                base_url=api.get("base_url", "https://api.example.com"),
                api_key=api.get("api_key", ""),
                timeout=api.get("timeout", 30),
                max_retries=api.get("max_retries", 3),
                rate_limit=api.get("rate_limit", 100)
            )
        
        return self
    
    def build(self) -> 'AppConfig':
        """Build the immutable configuration."""
        if not self._database:
            self.set_database()
        if not self._api:
            self.set_api()
        if not self._cache:
            self.set_cache()
        if not self._logging:
            self.set_logging()
        if not self._features:
            self.set_features()
        
        return AppConfig(
            database=self._database,
            api=self._api,
            cache=self._cache,
            logging=self._logging,
            features=self._features,
            environment=self._environment
        )


class AppConfig:
    """
    Immutable application configuration.
    
    Design Pattern: Value Object Pattern - Immutable configuration
    """
    
    def __init__(self, database: DatabaseConfig, api: APIConfig,
                 cache: CacheConfig, logging: LoggingConfig,
                 features: FeatureFlags, environment: Environment):
        self._database = database
        self._api = api
        self._cache = cache
        self._logging = logging
        self._features = features
        self._environment = environment
    
    @property
    def database(self) -> DatabaseConfig:
        """Get database configuration."""
        return self._database
    
    @property
    def api(self) -> APIConfig:
        """Get API configuration."""
        return self._api
    
    @property
    def cache(self) -> CacheConfig:
        """Get cache configuration."""
        return self._cache
    
    @property
    def logging(self) -> LoggingConfig:
        """Get logging configuration."""
        return self._logging
    
    @property
    def features(self) -> FeatureFlags:
        """Get feature flags."""
        return self._features
    
    @property
    def environment(self) -> Environment:
        """Get environment."""
        return self._environment
    
    def is_production(self) -> bool:
        """Check if running in production."""
        return self._environment == Environment.PRODUCTION
    
    def is_development(self) -> bool:
        """Check if running in development."""
        return self._environment == Environment.DEVELOPMENT
    
    def get_database_url(self) -> str:
        """Build database connection URL."""
        return f"postgresql://{self._database.user}:{self._database.password}@{self._database.host}:{self._database.port}/{self._database.database}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "database": self._database._asdict(),
            "api": self._api._asdict(),
            "cache": self._cache._asdict(),
            "logging": self._logging._asdict(),
            "features": self._features._asdict(),
            "environment": self._environment.value
        }
    
    def validate(self) -> List[str]:
        """Validate configuration and return list of issues."""
        issues = []
        
        # Database validation
        if not self._database.host:
            issues.append("Database host is required")
        if not 1 <= self._database.port <= 65535:
            issues.append(f"Invalid database port: {self._database.port}")
        
        # API validation
        if self.is_production() and not self._api.base_url.startswith("https://"):
            issues.append("Production API must use HTTPS")
        
        # Cache validation
        if self._cache.enabled and self.is_production():
            if not self._cache.redis_host:
                issues.append("Redis host required when cache enabled in production")
        
        return issues


# Predefined configurations for different environments
class Configurations:
    """Predefined configuration presets."""
    
    @staticmethod
    def development() -> AppConfig:
        """Development configuration."""
        return (ConfigBuilder()
                .set_environment(Environment.DEVELOPMENT)
                .set_database(host="localhost", database="app_dev")
                .set_cache(enabled=True, ttl_seconds=60)
                .set_features(debug_mode=True, analytics=False)
                .build())
    
    @staticmethod
    def production() -> AppConfig:
        """Production configuration."""
        return (ConfigBuilder()
                .set_environment(Environment.PRODUCTION)
                .set_database(host="prod-db.example.com", pool_size=20)
                .set_cache(enabled=True, ttl_seconds=300, max_size=10000)
                .set_logging(level="WARNING")
                .set_features(dark_mode=True, analytics=True, debug_mode=False)
                .build())
    
    @staticmethod
    def testing() -> AppConfig:
        """Testing configuration."""
        return (ConfigBuilder()
                .set_environment(Environment.TESTING)
                .set_database(database="app_test")
                .set_cache(enabled=False)
                .set_logging(level="DEBUG", file_path="test.log")
                .build())


def demonstrate_config_system():
    """
    Demonstrate the immutable configuration system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: IMMUTABLE CONFIGURATION SYSTEM")
    print("=" * 60)
    
    # Using builder pattern
    print("\n1. BUILDING CONFIGURATION WITH BUILDER")
    print("-" * 40)
    
    config = (ConfigBuilder()
              .set_database(host="db.example.com", port=5432, database="myapp")
              .set_api(base_url="https://api.example.com/v1", timeout=60)
              .set_cache(enabled=True, ttl_seconds=300)
              .set_features(dark_mode=True, beta_features=False)
              .set_environment(Environment.PRODUCTION)
              .build())
    
    print(f"  Database host: {config.database.host}")
    print(f"  Database port: {config.database.port}")
    print(f"  API base URL: {config.api.base_url}")
    print(f"  Cache enabled: {config.cache.enabled}")
    print(f"  Dark mode: {config.features.dark_mode}")
    print(f"  Environment: {config.environment.value}")
    
    # Using presets
    print("\n2. PREDEFINED CONFIGURATIONS")
    print("-" * 40)
    
    dev_config = Configurations.development()
    prod_config = Configurations.production()
    
    print(f"  Development DB: {dev_config.database.database}")
    print(f"  Production DB: {prod_config.database.database}")
    print(f"  Dev debug mode: {dev_config.features.debug_mode}")
    print(f"  Prod debug mode: {prod_config.features.debug_mode}")
    
    # Database URL
    print("\n3. DATABASE URL")
    print("-" * 40)
    
    db_url = config.get_database_url()
    print(f"  Database URL: {db_url}")
    
    # Configuration validation
    print("\n4. CONFIGURATION VALIDATION")
    print("-" * 40)
    
    issues = config.validate()
    if issues:
        print("  Configuration issues:")
        for issue in issues:
            print(f"    ⚠️ {issue}")
    else:
        print("  ✅ Configuration is valid")
    
    # Immutability demonstration
    print("\n5. IMMUTABILITY DEMONSTRATION")
    print("-" * 40)
    
    try:
        # This would raise AttributeError
        config.database.host = "newhost"
    except AttributeError as e:
        print(f"  Cannot modify: {e}")
    
    print("  Configuration values are immutable and cannot be changed!")
    
    # Environment-specific logic
    print("\n6. ENVIRONMENT-SPECIFIC LOGIC")
    print("-" * 40)
    
    print(f"  Is production: {config.is_production()}")
    print(f"  Is development: {config.is_development()}")
    
    # To dictionary
    print("\n7. CONFIGURATION AS DICTIONARY")
    print("-" * 40)
    
    config_dict = config.to_dict()
    print(f"  Top-level keys: {list(config_dict.keys())}")
    
    # Comparison with default config
    print("\n8. CONFIGURATION COMPARISON")
    print("-" * 40)
    
    default_config = ConfigBuilder().build()
    print(f"  Custom config equals default: {config.database == default_config.database}")
    print("  Each configuration is a unique immutable value object")


if __name__ == "__main__":
    demonstrate_config_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Tuple Basics** – Created with `()` or `tuple()`. Ordered, immutable sequences.

- **Tuple Access** – Indexing `[0]`, slicing `[1:4]`, negative indexing `[-1]`. Same as lists.

- **Immutability** – Cannot modify after creation. No `append()`, `remove()`, or item assignment.

- **Benefits** – Thread-safe, hashable (can be dict keys), memory efficient, prevents accidental modification.

- **Tuple Unpacking** – `a, b = (1, 2)`. Swap variables: `a, b = b, a`. Extended unpacking with `*`.

- **Named Tuples** – `namedtuple('ClassName', ['field1', 'field2'])`. Field access by name. Self-documenting.

- **Namedtuple Methods** – `_asdict()`, `_replace()`, `_make()`, `_fields`. Memory efficient.

- **GPS Coordinate System** – Immutable coordinates with distance calculation. Factory pattern for creation.

- **Route Optimization** – Nearest neighbor algorithm. Region-based routing. Bounding box calculation.

- **Configuration System** – Immutable config with builder pattern. Environment-specific presets. Validation.

- **SOLID Principles Applied** – Interface Segregation (read-only tuple interface), Single Responsibility (config separate from logic), Open/Closed (new config sources can be added).

- **Design Patterns Used** – Value Object Pattern (immutable tuples), Factory Pattern (coordinate creation), Builder Pattern (config building), Singleton Pattern (config presets), Composite Pattern (route with waypoints), Strategy Pattern (route optimization).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Lists – Ordered & Mutable

- **📚 Series C Catalog:** Data Structures Express – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Dictionaries – Key-Value Power (Series C, Story 3)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 2 | 3 | 40% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **20** | **32** | **38%** |

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

**Next Story:** Series C, Story 3: The 2026 Python Metromap: Dictionaries – Key-Value Power

---

## 📝 Your Invitation

You've mastered tuples. Now build something with what you've learned:

1. **Build a route planner** – Create a system that calculates distances between multiple points, finds shortest paths, and generates turn-by-turn directions.

2. **Create an immutable settings manager** – Build a configuration system that loads from JSON/YAML and provides read-only access.

3. **Build a data record system** – Use namedtuples to represent database records, API responses, or CSV data.

4. **Create a geometric shape library** – Represent points, lines, rectangles, and circles as immutable tuples.

5. **Build a version tracking system** – Store immutable snapshots of data at different points in time.

**You've mastered tuples. Next stop: Dictionaries!**

---

*Found this helpful? Clap, comment, and share what you built with tuples. Next stop: Dictionaries!* 🚇