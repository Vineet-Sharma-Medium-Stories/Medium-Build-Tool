# The 2026 Python Metromap: Lists – Ordered & Mutable

## Series C: Data Structures Express | Story 1 of 5

![The 2026 Python Metromap/images/Lists – Ordered and Mutable](images/Lists – Ordered and Mutable.png)

## 📖 Introduction

**Welcome to the first stop on the Data Structures Express Line.**

You've completed Foundations Station and Functions & Modules Yard. You've mastered variables, operators, control flow, loops, functions, recursion, and packages. You can write code that makes decisions, repeats operations, and organizes logic into reusable modules. But there's a fundamental gap—you've been working primarily with single values.

Real-world applications deal with collections of data. A shopping cart has multiple items. A playlist has many songs. A student roster has dozens of names. A transaction log has thousands of entries. You need a way to store, access, and manipulate these collections efficiently.

That's where lists come in.

Lists are ordered, mutable sequences that can hold any type of data. They're the most versatile and frequently used data structure in Python. You can add items, remove items, sort them, slice them, and iterate over them. Lists form the backbone of data manipulation in Python.

This story—**The 2026 Python Metromap: Lists – Ordered & Mutable**—is your guide to mastering Python lists. We'll build a complete todo application with add, remove, complete, and reorder operations. We'll create a playlist manager with shuffle, repeat, and playlist persistence. We'll implement a transaction log with filtering and search. And we'll build a complete shopping cart system that demonstrates all list operations in a real-world context.

**Let's build with lists.**

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

- 📋 **The 2026 Python Metromap: Lists – Ordered & Mutable** – Todo application; playlist manager; shopping cart system. **⬅️ YOU ARE HERE**

- 🔒 **The 2026 Python Metromap: Tuples – Immutable Collections** – GPS coordinates; database records; immutable configuration. 🔜 *Up Next*

- 🔑 **The 2026 Python Metromap: Dictionaries – Key-Value Power** – User profile cache; product catalog; dependency injection container.

- 🎯 **The 2026 Python Metromap: Sets – Unique & Fast** – Duplicate removal; friend recommendation engine; common visitor detection.

- 📝 **The 2026 Python Metromap: Comprehensions – One-Line Power** – Data transformation pipelines; filtered iterations; nested structure creation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📋 Section 1: List Fundamentals – Creation, Access, and Modification

Lists are ordered, mutable sequences. They can hold any data type and allow duplicate values.

**SOLID Principle Applied: Single Responsibility** – Lists maintain ordered sequences; each method performs one operation.

**Design Pattern: Collection Pattern** – Provides uniform interface for accessing, modifying, and iterating over grouped data.

```python
"""
LIST FUNDAMENTALS: CREATION, ACCESS, AND MODIFICATION

This section covers the basics of creating, accessing, and modifying lists.

SOLID Principle: Single Responsibility
- Lists maintain ordered sequences
- Each method performs one specific operation

Design Pattern: Collection Pattern
- Uniform interface for grouped data
"""

from typing import List, Any, Optional
import time


def demonstrate_list_creation():
    """
    Demonstrates different ways to create lists.
    """
    print("=" * 60)
    print("SECTION 1A: CREATING LISTS")
    print("=" * 60)
    
    # EMPTY LISTS
    print("\n1. CREATING EMPTY LISTS")
    print("-" * 40)
    
    empty_brackets = []
    empty_constructor = list()
    
    print(f"  empty_brackets: {empty_brackets} (type: {type(empty_brackets).__name__})")
    print(f"  empty_constructor: {empty_constructor}")
    
    # LISTS WITH INITIAL VALUES
    print("\n2. LISTS WITH INITIAL VALUES")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry", "date"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True, None]
    
    print(f"  fruits: {fruits}")
    print(f"  numbers: {numbers}")
    print(f"  mixed: {mixed}")
    
    # LISTS FROM OTHER ITERABLES
    print("\n3. LISTS FROM OTHER ITERABLES")
    print("-" * 40)
    
    # From range
    range_list = list(range(5))
    print(f"  list(range(5)): {range_list}")
    
    # From string
    char_list = list("Python")
    print(f"  list('Python'): {char_list}")
    
    # From tuple
    tuple_data = (1, 2, 3)
    list_from_tuple = list(tuple_data)
    print(f"  list((1, 2, 3)): {list_from_tuple}")
    
    # From set (order not guaranteed)
    set_data = {3, 1, 2}
    list_from_set = list(set_data)
    print(f"  list({{3, 1, 2}}): {list_from_set}")
    
    # LIST COMPREHENSIONS (preview)
    print("\n4. LIST COMPREHENSIONS")
    print("-" * 40)
    
    squares = [x ** 2 for x in range(10)]
    evens = [x for x in range(20) if x % 2 == 0]
    
    print(f"  squares 0-9: {squares}")
    print(f"  evens 0-19: {evens}")
    
    # LISTS WITH REPETITION
    print("\n5. LISTS WITH REPETITION")
    print("-" * 40)
    
    zeros = [0] * 5
    pattern = [1, 2] * 3
    
    print(f"  [0] * 5: {zeros}")
    print(f"  [1, 2] * 3: {pattern}")


def demonstrate_list_access():
    """
    Demonstrates accessing elements in lists.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ACCESSING LIST ELEMENTS")
    print("=" * 60)
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    
    print(f"  List: {fruits}")
    
    # POSITIVE INDEXING
    print("\n1. POSITIVE INDEXING (0-based)")
    print("-" * 40)
    
    print(f"  fruits[0]: {fruits[0]}  # First element")
    print(f"  fruits[1]: {fruits[1]}  # Second element")
    print(f"  fruits[2]: {fruits[2]}  # Third element")
    print(f"  fruits[3]: {fruits[3]}  # Fourth element")
    
    # NEGATIVE INDEXING
    print("\n2. NEGATIVE INDEXING (from end)")
    print("-" * 40)
    
    print(f"  fruits[-1]: {fruits[-1]}  # Last element")
    print(f"  fruits[-2]: {fruits[-2]}  # Second last")
    print(f"  fruits[-3]: {fruits[-3]}  # Third last")
    
    # SLICING
    print("\n3. SLICING [start:end:step]")
    print("-" * 40)
    
    print(f"  fruits[1:4]: {fruits[1:4]}      # Elements 1-3 (end exclusive)")
    print(f"  fruits[:3]: {fruits[:3]}        # First 3 elements")
    print(f"  fruits[3:]: {fruits[3:]}        # Elements from index 3 to end")
    print(f"  fruits[::2]: {fruits[::2]}      # Every other element")
    print(f"  fruits[::-1]: {fruits[::-1]}    # Reversed list")
    
    # SLICING WITH VARIABLES
    print("\n4. SLICING WITH VARIABLES")
    print("-" * 40)
    
    start = 2
    end = 5
    print(f"  start = {start}, end = {end}")
    print(f"  fruits[start:end]: {fruits[start:end]}")
    
    # CHECKING EXISTENCE
    print("\n5. CHECKING EXISTENCE")
    print("-" * 40)
    
    print(f"  'banana' in fruits: {'banana' in fruits}")
    print(f"  'mango' in fruits: {'mango' in fruits}")
    print(f"  'apple' not in fruits: {'apple' not in fruits}")
    
    # FINDING INDEX
    print("\n6. FINDING INDEX")
    print("-" * 40)
    
    print(f"  fruits.index('cherry'): {fruits.index('cherry')}")
    
    # Finding index with start parameter
    duplicate_fruits = ["apple", "banana", "apple", "cherry", "apple"]
    print(f"  duplicate_fruits: {duplicate_fruits}")
    print(f"  duplicate_fruits.index('apple'): {duplicate_fruits.index('apple')}")
    print(f"  duplicate_fruits.index('apple', 1): {duplicate_fruits.index('apple', 1)}")
    print(f"  duplicate_fruits.index('apple', 2): {duplicate_fruits.index('apple', 2)}")
    
    # COUNTING OCCURRENCES
    print("\n7. COUNTING OCCURRENCES")
    print("-" * 40)
    
    print(f"  duplicate_fruits.count('apple'): {duplicate_fruits.count('apple')}")
    print(f"  duplicate_fruits.count('banana'): {duplicate_fruits.count('banana')}")
    print(f"  duplicate_fruits.count('grape'): {duplicate_fruits.count('grape')}")
    
    # LENGTH
    print("\n8. LIST LENGTH")
    print("-" * 40)
    
    print(f"  len(fruits): {len(fruits)}")
    print(f"  len(empty_list): {len([])}")


def demonstrate_list_modification():
    """
    Demonstrates modifying lists (adding, removing, changing elements).
    
    Lists are mutable - they can be changed after creation.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: MODIFYING LISTS")
    print("=" * 60)
    
    # MODIFYING BY INDEX
    print("\n1. MODIFYING BY INDEX")
    print("-" * 40)
    
    colors = ["red", "green", "blue", "yellow"]
    print(f"  Original: {colors}")
    
    colors[1] = "emerald"
    print(f"  After colors[1] = 'emerald': {colors}")
    
    colors[-1] = "gold"
    print(f"  After colors[-1] = 'gold': {colors}")
    
    # SLICE ASSIGNMENT
    print("\n2. SLICE ASSIGNMENT")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"  Original: {numbers}")
    
    # Replace a slice
    numbers[2:5] = [30, 40, 50]
    print(f"  After numbers[2:5] = [30, 40, 50]: {numbers}")
    
    # Insert using slice
    numbers[2:2] = [20, 25]
    print(f"  After numbers[2:2] = [20, 25]: {numbers}")
    
    # Delete using slice
    numbers[4:7] = []
    print(f"  After numbers[4:7] = []: {numbers}")
    
    # ADDING ELEMENTS
    print("\n3. ADDING ELEMENTS (append, insert, extend)")
    print("-" * 40)
    
    shopping_list = []
    print(f"  Start: {shopping_list}")
    
    # append() - adds to end
    shopping_list.append("milk")
    print(f"  append('milk'): {shopping_list}")
    
    shopping_list.append("eggs")
    shopping_list.append("bread")
    print(f"  append more: {shopping_list}")
    
    # insert() - adds at specific position
    shopping_list.insert(1, "butter")
    print(f"  insert(1, 'butter'): {shopping_list}")
    
    shopping_list.insert(0, "cheese")
    print(f"  insert(0, 'cheese'): {shopping_list}")
    
    # extend() - adds multiple elements
    shopping_list.extend(["yogurt", "cereal"])
    print(f"  extend(['yogurt', 'cereal']): {shopping_list}")
    
    # REMOVING ELEMENTS
    print("\n4. REMOVING ELEMENTS (remove, pop, del, clear)")
    print("-" * 40)
    
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"  Original: {items}")
    
    # remove() - removes first occurrence by value
    items.remove("cherry")
    print(f"  remove('cherry'): {items}")
    
    # pop() - removes and returns by index (default last)
    removed = items.pop()
    print(f"  pop(): removed '{removed}', list: {items}")
    
    removed = items.pop(0)
    print(f"  pop(0): removed '{removed}', list: {items}")
    
    # del - deletes by index or slice
    del items[1]
    print(f"  del items[1]: {items}")
    
    # clear() - removes all elements
    items.clear()
    print(f"  clear(): {items}")
    
    # LIST CONCATENATION
    print("\n5. LIST CONCATENATION (+)")
    print("-" * 40)
    
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    
    list_c = list_a + list_b
    print(f"  {list_a} + {list_b} = {list_c}")
    
    # Original lists unchanged
    print(f"  Original list_a: {list_a} (unchanged)")
    print(f"  Original list_b: {list_b} (unchanged)")
    
    # IN-PLACE EXTEND (+=)
    print("\n6. IN-PLACE EXTEND (+=)")
    print("-" * 40)
    
    list_a += list_b
    print(f"  list_a += list_b: {list_a}")
    
    # LIST REPETITION (*=)
    print("\n7. LIST REPETITION (*=)")
    print("-" * 40)
    
    pattern = [1, 2]
    pattern *= 3
    print(f"  [1, 2] *= 3: {pattern}")


def demonstrate_list_copying():
    """
    Demonstrates different ways to copy lists.
    
    Important: Assignment does NOT copy - it creates a reference.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: COPYING LISTS")
    print("=" * 60)
    
    # ASSIGNMENT (DOES NOT COPY)
    print("\n1. ASSIGNMENT (DOES NOT COPY - References same list)")
    print("-" * 40)
    
    original = [1, 2, [3, 4]]
    assignment = original
    
    print(f"  original: {original}")
    print(f"  assignment: {assignment}")
    
    assignment[0] = 99
    print(f"\n  After assignment[0] = 99:")
    print(f"  original: {original} (changed!)")
    print(f"  assignment: {assignment}")
    
    print("\n  ⚠️ Assignment creates a reference, not a copy!")
    
    # SHALLOW COPY METHODS
    print("\n2. SHALLOW COPY METHODS")
    print("-" * 40)
    
    original = [1, 2, [3, 4]]
    
    # Method 1: slice
    slice_copy = original[:]
    
    # Method 2: list() constructor
    constructor_copy = list(original)
    
    # Method 3: copy() method
    copy_method = original.copy()
    
    print(f"  original: {original}")
    print(f"  slice_copy: {slice_copy}")
    print(f"  constructor_copy: {constructor_copy}")
    print(f"  copy_method: {copy_method}")
    
    # Modifying shallow copy's top-level elements
    slice_copy[0] = 99
    print(f"\n  After modifying top-level element:")
    print(f"  original: {original} (unchanged)")
    print(f"  slice_copy: {slice_copy}")
    
    # Modifying nested list (affects all shallow copies!)
    original[2][0] = 999
    print(f"\n  After modifying nested list:")
    print(f"  original: {original}")
    print(f"  slice_copy: {slice_copy} (changed!)")
    print(f"  constructor_copy: {constructor_copy} (changed!)")
    print(f"  copy_method: {copy_method} (changed!)")
    
    print("\n  ⚠️ Shallow copies only copy top-level elements!")
    print("     Nested objects are still referenced.")
    
    # DEEP COPY
    print("\n3. DEEP COPY (copies nested structures)")
    print("-" * 40)
    
    import copy
    
    original = [1, 2, [3, 4]]
    deep_copy = copy.deepcopy(original)
    
    print(f"  original: {original}")
    print(f"  deep_copy: {deep_copy}")
    
    # Modify nested list in deep copy
    deep_copy[2][0] = 999
    print(f"\n  After modifying deep_copy's nested list:")
    print(f"  original: {original} (unchanged)")
    print(f"  deep_copy: {deep_copy}")
    
    print("\n  ✓ Deep copy creates independent copies of all nested objects")
    
    # WHEN TO USE EACH
    print("\n4. WHEN TO USE EACH COPYING METHOD")
    print("-" * 40)
    
    print("""
    Assignment (=):
        - Use when you want another reference to the same list
        - Changes to one affect the other
    
    Shallow Copy ([:], list(), .copy()):
        - Use for flat lists (no nested objects)
        - More memory efficient than deep copy
        - Faster than deep copy
    
    Deep Copy (copy.deepcopy()):
        - Use for nested structures (lists within lists)
        - Creates completely independent copy
        - Slower and uses more memory
    """)


if __name__ == "__main__":
    demonstrate_list_creation()
    demonstrate_list_access()
    demonstrate_list_modification()
    demonstrate_list_copying()
```

---

## 🔧 Section 2: List Methods – Sorting, Reversing, and Searching

Lists have powerful built-in methods for sorting, reversing, and searching.

**SOLID Principle Applied: Interface Segregation** – Each method provides focused functionality.

**Design Pattern: Command Pattern** – Methods modify the list in-place or return new lists.

```python
"""
LIST METHODS: SORTING, REVERSING, AND SEARCHING

This section covers advanced list methods for manipulation.

SOLID Principle: Interface Segregation
- Each method provides focused functionality

Design Pattern: Command Pattern
- Methods modify the list or return new lists
"""

from typing import List, Any, Callable
import random


def demonstrate_sorting():
    """
    Demonstrates sorting lists with sort() and sorted().
    
    sort() - sorts in-place (modifies original)
    sorted() - returns new sorted list (original unchanged)
    """
    print("=" * 60)
    print("SECTION 2A: SORTING LISTS")
    print("=" * 60)
    
    # BASIC SORTING
    print("\n1. BASIC SORTING")
    print("-" * 40)
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"  Original: {numbers}")
    
    # sort() - modifies original
    numbers.sort()
    print(f"  After sort(): {numbers}")
    
    # sort(reverse=True) - descending
    numbers.sort(reverse=True)
    print(f"  After sort(reverse=True): {numbers}")
    
    # SORTED() - returns new list
    print("\n2. SORTED() FUNCTION (returns new list)")
    print("-" * 40)
    
    original = [3, 1, 4, 1, 5]
    sorted_new = sorted(original)
    
    print(f"  original: {original} (unchanged)")
    print(f"  sorted(original): {sorted_new}")
    
    # SORTING STRINGS
    print("\n3. SORTING STRINGS")
    print("-" * 40)
    
    words = ["banana", "Apple", "cherry", "date", "Elderberry"]
    print(f"  Original: {words}")
    
    # Default sort (case-sensitive, uppercase before lowercase)
    words.sort()
    print(f"  Default sort: {words}")
    
    # Case-insensitive sort
    words.sort(key=str.lower)
    print(f"  Case-insensitive: {words}")
    
    # Sort by length
    words.sort(key=len)
    print(f"  By length: {words}")
    
    # Sort by length, then alphabetically
    words.sort(key=lambda w: (len(w), w.lower()))
    print(f"  By length, then alphabetically: {words}")
    
    # SORTING DICTIONARIES
    print("\n4. SORTING LISTS OF DICTIONARIES")
    print("-" * 40)
    
    products = [
        {"name": "Laptop", "price": 999, "rating": 4.5},
        {"name": "Mouse", "price": 25, "rating": 4.2},
        {"name": "Keyboard", "price": 75, "rating": 4.7},
        {"name": "Monitor", "price": 299, "rating": 4.4}
    ]
    
    print("  Original products:")
    for p in products:
        print(f"    {p['name']}: ${p['price']}, {p['rating']}★")
    
    # Sort by price
    products.sort(key=lambda p: p["price"])
    print("\n  Sorted by price (ascending):")
    for p in products:
        print(f"    {p['name']}: ${p['price']}")
    
    # Sort by rating (descending)
    products.sort(key=lambda p: p["rating"], reverse=True)
    print("\n  Sorted by rating (descending):")
    for p in products:
        print(f"    {p['name']}: {p['rating']}★")
    
    # Sort by multiple criteria (price then rating)
    products.sort(key=lambda p: (p["price"], p["rating"]))
    print("\n  Sorted by price, then rating:")
    for p in products:
        print(f"    {p['name']}: ${p['price']}, {p['rating']}★")
    
    # SORTING CUSTOM OBJECTS
    print("\n5. SORTING CUSTOM OBJECTS")
    print("-" * 40)
    
    from dataclasses import dataclass
    
    @dataclass
    class Task:
        name: str
        priority: int
        due_date: str
        
        def __repr__(self):
            return f"{self.name}(P{self.priority})"
    
    tasks = [
        Task("Fix bug", 1, "2024-01-15"),
        Task("Write docs", 3, "2024-01-10"),
        Task("Deploy", 2, "2024-01-20"),
        Task("Review PR", 1, "2024-01-12")
    ]
    
    print(f"  Original tasks: {tasks}")
    
    # Sort by priority
    tasks.sort(key=lambda t: t.priority)
    print(f"  By priority: {tasks}")
    
    # Sort by due date
    tasks.sort(key=lambda t: t.due_date)
    print(f"  By due date: {tasks}")
    
    # Sort by priority, then due date
    tasks.sort(key=lambda t: (t.priority, t.due_date))
    print(f"  By priority, then due date: {tasks}")
    
    # STABLE SORTING
    print("\n6. STABLE SORTING (preserves order for equal keys)")
    print("-" * 40)
    
    data = [
        ("Alice", 25, "Engineer"),
        ("Bob", 30, "Designer"),
        ("Charlie", 25, "Manager"),
        ("Diana", 30, "Engineer"),
        ("Eve", 25, "Designer")
    ]
    
    print(f"  Original: {data}")
    
    # Sort by age (stable: original order preserved within same age)
    data.sort(key=lambda x: x[1])
    print(f"  After sort by age: {data}")
    
    # Sort by job (age order preserved within same job)
    data.sort(key=lambda x: x[2])
    print(f"  After sort by job: {data}")


def demonstrate_reversing():
    """
    Demonstrates reversing lists with reverse() and slicing.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: REVERSING LISTS")
    print("=" * 60)
    
    # REVERSE() METHOD (in-place)
    print("\n1. REVERSE() METHOD (modifies original)")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5]
    print(f"  Original: {numbers}")
    
    numbers.reverse()
    print(f"  After reverse(): {numbers}")
    
    # REVERSED() FUNCTION (returns iterator)
    print("\n2. REVERSED() FUNCTION (returns iterator)")
    print("-" * 40)
    
    original = [1, 2, 3, 4, 5]
    reversed_iter = reversed(original)
    
    print(f"  original: {original}")
    print(f"  reversed(original): {list(reversed_iter)}")
    print(f"  original after reversed(): {original} (unchanged)")
    
    # SLICING FOR REVERSAL
    print("\n3. SLICING FOR REVERSAL")
    print("-" * 40)
    
    original = [1, 2, 3, 4, 5]
    reversed_slice = original[::-1]
    
    print(f"  original: {original}")
    print(f"  original[::-1]: {reversed_slice}")
    print(f"  original unchanged: {original}")
    
    # PRACTICAL: REVERSING STRINGS IN LIST
    print("\n4. PRACTICAL: REVERSING STRINGS IN A LIST")
    print("-" * 40)
    
    words = ["hello", "world", "python", "code"]
    reversed_words = [w[::-1] for w in words]
    
    print(f"  Original: {words}")
    print(f"  Reversed strings: {reversed_words}")


def demonstrate_searching():
    """
    Demonstrates searching in lists.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: SEARCHING IN LISTS")
    print("=" * 60)
    
    # INDEX() METHOD
    print("\n1. INDEX() METHOD")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry", "date", "banana", "elderberry"]
    print(f"  List: {fruits}")
    
    print(f"  index('cherry'): {fruits.index('cherry')}")
    print(f"  index('banana'): {fruits.index('banana')}")
    print(f"  index('banana', 2): {fruits.index('banana', 2)}")
    
    # Handling ValueError
    print("\n2. HANDLING INDEX NOT FOUND")
    print("-" * 40)
    
    try:
        index = fruits.index("mango")
        print(f"  index('mango'): {index}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    # Safe search function
    def safe_index(lst: List, value: Any, default: int = -1) -> int:
        """Return index of value, or default if not found."""
        try:
            return lst.index(value)
        except ValueError:
            return default
    
    print(f"  safe_index('mango'): {safe_index(fruits, 'mango')}")
    print(f"  safe_index('cherry'): {safe_index(fruits, 'cherry')}")
    
    # COUNT() METHOD
    print("\n3. COUNT() METHOD")
    print("-" * 40)
    
    numbers = [1, 2, 3, 2, 4, 2, 5, 2, 6]
    print(f"  numbers: {numbers}")
    print(f"  count(2): {numbers.count(2)}")
    print(f"  count(7): {numbers.count(7)}")
    
    # FINDING ALL OCCURRENCES
    print("\n4. FINDING ALL OCCURRENCES")
    print("-" * 40)
    
    def find_all_indices(lst: List, value: Any) -> List[int]:
        """Return list of all indices where value occurs."""
        return [i for i, v in enumerate(lst) if v == value]
    
    print(f"  find_all_indices(2): {find_all_indices(numbers, 2)}")
    print(f"  find_all_indices(5): {find_all_indices(numbers, 5)}")
    
    # USING LIST COMPREHENSION FOR SEARCH
    print("\n5. SEARCHING WITH CONDITIONS")
    print("-" * 40)
    
    numbers = [10, 25, 30, 45, 50, 65, 70, 85, 90]
    
    # Find numbers greater than 50
    greater_than_50 = [n for n in numbers if n > 50]
    print(f"  Numbers > 50: {greater_than_50}")
    
    # Find numbers between 30 and 70
    in_range = [n for n in numbers if 30 <= n <= 70]
    print(f"  Numbers 30-70: {in_range}")
    
    # Find first number greater than 50
    first_match = next((n for n in numbers if n > 50), None)
    print(f"  First number > 50: {first_match}")


def demonstrate_list_comprehensions_advanced():
    """
    Demonstrates advanced list comprehension patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: ADVANCED LIST COMPREHENSIONS")
    print("=" * 60)
    
    # NESTED COMPREHENSIONS
    print("\n1. NESTED COMPREHENSIONS")
    print("-" * 40)
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Flatten matrix
    flattened = [num for row in matrix for num in row]
    print(f"  Flattened matrix: {flattened}")
    
    # Create coordinate pairs
    coords = [(x, y) for x in range(3) for y in range(3)]
    print(f"  All coordinates 3x3: {coords}")
    
    # CONDITIONAL COMPREHENSIONS
    print("\n2. CONDITIONAL COMPREHENSIONS")
    print("-" * 40)
    
    numbers = range(20)
    
    # Even numbers only
    evens = [x for x in numbers if x % 2 == 0]
    print(f"  Evens: {evens}")
    
    # Even numbers squared
    even_squares = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"  Even squares: {even_squares}")
    
    # WITH IF-ELSE (ternary)
    print("\n3. TERNARY IN COMPREHENSIONS")
    print("-" * 40)
    
    labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
    print(f"  Number labels: {labels}")
    
    # TRANSFORMING DATA
    print("\n4. TRANSFORMING DATA")
    print("-" * 40)
    
    names = ["alice", "bob", "charlie", "diana"]
    
    # Capitalize
    capitalized = [name.capitalize() for name in names]
    print(f"  Capitalized: {capitalized}")
    
    # Add prefix
    prefixed = [f"Mr./Ms. {name.capitalize()}" for name in names]
    print(f"  With title: {prefixed}")
    
    # FILTERING AND TRANSFORMING
    print("\n5. FILTERING AND TRANSFORMING")
    print("-" * 40)
    
    products = [
        {"name": "Laptop", "price": 999, "category": "electronics"},
        {"name": "Mouse", "price": 25, "category": "electronics"},
        {"name": "Notebook", "price": 5, "category": "stationery"},
        {"name": "Monitor", "price": 299, "category": "electronics"},
        {"name": "Pen", "price": 2, "category": "stationery"}
    ]
    
    # Names of electronics under $100
    cheap_electronics = [
        p["name"] for p in products 
        if p["category"] == "electronics" and p["price"] < 100
    ]
    print(f"  Cheap electronics: {cheap_electronics}")
    
    # Apply discount to electronics
    discounted = [
        {**p, "price": round(p["price"] * 0.9, 2)}
        for p in products
        if p["category"] == "electronics"
    ]
    print(f"  Discounted electronics: {[(p['name'], p['price']) for p in discounted]}")
    
    # SET COMPREHENSIONS (preview)
    print("\n6. SET COMPREHENSIONS")
    print("-" * 40)
    
    # Unique first letters
    words = ["apple", "banana", "cherry", "date", "apple", "banana"]
    first_letters = {word[0] for word in words}
    print(f"  Unique first letters: {first_letters}")
    
    # DICTIONARY COMPREHENSIONS (preview)
    print("\n7. DICTIONARY COMPREHENSIONS")
    print("-" * 40)
    
    # Word length mapping
    word_lengths = {word: len(word) for word in words}
    print(f"  Word lengths: {word_lengths}")


if __name__ == "__main__":
    demonstrate_sorting()
    demonstrate_reversing()
    demonstrate_searching()
    demonstrate_list_comprehensions_advanced()
```

---

## 📝 Section 3: Building a Todo Application

A complete todo application that demonstrates all list operations in a practical context.

**SOLID Principles Applied:**
- Single Responsibility: Each function handles one aspect of todo management
- Open/Closed: New features can be added without modifying existing code

**Design Patterns:**
- Command Pattern: Todo operations as commands
- Repository Pattern: Todo storage and retrieval
- Iterator Pattern: Iterating through todos

```python
"""
TODO APPLICATION: COMPLETE LIST DEMONSTRATION

This section builds a complete todo application using lists.

SOLID Principles Applied:
- Single Responsibility: Each function handles one aspect
- Open/Closed: New features can be added

Design Patterns:
- Command Pattern: Todo operations as commands
- Repository Pattern: Todo storage and retrieval
- Iterator Pattern: Iterating through todos
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
import os


@dataclass
class TodoItem:
    """Represents a single todo item."""
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    priority: int = 2  # 1=high, 2=medium, 3=low
    tags: List[str] = field(default_factory=list)
    
    def mark_completed(self) -> None:
        """Mark todo as completed."""
        self.completed = True
        self.completed_at = datetime.now()
    
    def mark_incomplete(self) -> None:
        """Mark todo as incomplete."""
        self.completed = False
        self.completed_at = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "priority": self.priority,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TodoItem':
        """Create TodoItem from dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            completed=data["completed"],
            created_at=datetime.fromisoformat(data["created_at"]),
            completed_at=datetime.fromisoformat(data["completed_at"]) if data["completed_at"] else None,
            priority=data.get("priority", 2),
            tags=data.get("tags", [])
        )
    
    def __str__(self) -> str:
        status = "✓" if self.completed else "○"
        priority_symbols = {1: "!", 2: " ", 3: "↓"}
        priority_sym = priority_symbols.get(self.priority, " ")
        return f"{status} [{priority_sym}] {self.id}: {self.title}"


class TodoRepository:
    """
    Repository for storing and retrieving todos.
    
    Design Pattern: Repository Pattern - Data access abstraction
    """
    
    def __init__(self, storage_file: str = "todos.json"):
        self.storage_file = storage_file
        self.todos: List[TodoItem] = []
        self.next_id = 1
        self._load()
    
    def _load(self) -> None:
        """Load todos from file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.todos = [TodoItem.from_dict(item) for item in data]
                    if self.todos:
                        self.next_id = max(t.id for t in self.todos) + 1
            except (json.JSONDecodeError, FileNotFoundError):
                print(f"  Could not load todos from {self.storage_file}")
    
    def _save(self) -> None:
        """Save todos to file."""
        with open(self.storage_file, 'w') as f:
            json.dump([t.to_dict() for t in self.todos], f, indent=2)
    
    def add(self, title: str, description: str = "", priority: int = 2, tags: List[str] = None) -> TodoItem:
        """Add a new todo."""
        todo = TodoItem(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags or []
        )
        self.todos.append(todo)
        self.next_id += 1
        self._save()
        return todo
    
    def get_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """Get todo by ID."""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def update(self, todo_id: int, **kwargs) -> Optional[TodoItem]:
        """Update a todo."""
        todo = self.get_by_id(todo_id)
        if not todo:
            return None
        
        for key, value in kwargs.items():
            if hasattr(todo, key):
                setattr(todo, key, value)
        
        self._save()
        return todo
    
    def delete(self, todo_id: int) -> bool:
        """Delete a todo by ID."""
        original_length = len(self.todos)
        self.todos = [t for t in self.todos if t.id != todo_id]
        if len(self.todos) < original_length:
            self._save()
            return True
        return False
    
    def complete(self, todo_id: int) -> Optional[TodoItem]:
        """Mark todo as completed."""
        todo = self.get_by_id(todo_id)
        if todo and not todo.completed:
            todo.mark_completed()
            self._save()
        return todo
    
    def incomplete(self, todo_id: int) -> Optional[TodoItem]:
        """Mark todo as incomplete."""
        todo = self.get_by_id(todo_id)
        if todo and todo.completed:
            todo.mark_incomplete()
            self._save()
        return todo
    
    def get_all(self, include_completed: bool = True) -> List[TodoItem]:
        """Get all todos, optionally filtering completed."""
        if include_completed:
            return self.todos.copy()
        return [t for t in self.todos if not t.completed]
    
    def get_by_priority(self, priority: int, include_completed: bool = False) -> List[TodoItem]:
        """Get todos by priority."""
        return [t for t in self.todos if t.priority == priority and (include_completed or not t.completed)]
    
    def get_by_tag(self, tag: str, include_completed: bool = False) -> List[TodoItem]:
        """Get todos by tag."""
        return [t for t in self.todos if tag in t.tags and (include_completed or not t.completed)]
    
    def search(self, query: str) -> List[TodoItem]:
        """Search todos by title or description."""
        query_lower = query.lower()
        return [
            t for t in self.todos
            if query_lower in t.title.lower() or query_lower in t.description.lower()
        ]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get todo statistics."""
        total = len(self.todos)
        completed = sum(1 for t in self.todos if t.completed)
        pending = total - completed
        
        # Priority distribution
        priority_counts = {1: 0, 2: 0, 3: 0}
        for t in self.todos:
            if not t.completed:
                priority_counts[t.priority] = priority_counts.get(t.priority, 0) + 1
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total * 100) if total > 0 else 0,
            "priority_pending": priority_counts,
            "oldest_pending": min(
                (t.created_at for t in self.todos if not t.completed),
                default=None
            ),
            "newest_pending": max(
                (t.created_at for t in self.todos if not t.completed),
                default=None
            )
        }
    
    def clear_completed(self) -> int:
        """Remove all completed todos."""
        count_before = len(self.todos)
        self.todos = [t for t in self.todos if not t.completed]
        count_removed = count_before - len(self.todos)
        if count_removed > 0:
            self._save()
        return count_removed
    
    def reorder(self, new_order: List[int]) -> bool:
        """
        Reorder todos based on list of IDs.
        
        Args:
            new_order: List of todo IDs in desired order
            
        Returns:
            True if reorder successful
        """
        if set(new_order) != {t.id for t in self.todos}:
            return False
        
        id_to_todo = {t.id: t for t in self.todos}
        self.todos = [id_to_todo[tid] for tid in new_order]
        self._save()
        return True


class TodoCLI:
    """
    Command-line interface for todo application.
    
    Design Pattern: Command Pattern - CLI commands mapped to repository methods
    """
    
    def __init__(self):
        self.repo = TodoRepository()
        self.running = True
    
    def display_todos(self, todos: List[TodoItem] = None) -> None:
        """Display todos in formatted table."""
        if todos is None:
            todos = self.repo.get_all()
        
        if not todos:
            print("\n  No todos found.")
            return
        
        print("\n" + "=" * 70)
        print(f"{'ID':<4} {'Status':<2} {'Priority':<3} {'Title':<40} {'Created':<12}")
        print("-" * 70)
        
        for todo in todos:
            status = "✓" if todo.completed else "○"
            priority_symbol = {1: "! ", 2: "  ", 3: "↓"}.get(todo.priority, "  ")
            created_str = todo.created_at.strftime("%m/%d %H:%M")
            title_display = todo.title[:37] + "..." if len(todo.title) > 40 else todo.title
            print(f"{todo.id:<4} {status:<2} {priority_symbol:<3} {title_display:<40} {created_str:<12}")
        
        print("=" * 70)
    
    def display_statistics(self) -> None:
        """Display todo statistics."""
        stats = self.repo.get_statistics()
        
        print("\n" + "=" * 50)
        print("TODO STATISTICS")
        print("=" * 50)
        print(f"  Total todos: {stats['total']}")
        print(f"  Completed: {stats['completed']}")
        print(f"  Pending: {stats['pending']}")
        print(f"  Completion rate: {stats['completion_rate']:.1f}%")
        print(f"\n  Pending by priority:")
        print(f"    High (!): {stats['priority_pending'].get(1, 0)}")
        print(f"    Medium ( ): {stats['priority_pending'].get(2, 0)}")
        print(f"    Low (↓): {stats['priority_pending'].get(3, 0)}")
        print("=" * 50)
    
    def add_todo(self) -> None:
        """Add a new todo."""
        print("\n" + "-" * 40)
        title = input("  Title: ").strip()
        if not title:
            print("  Title is required!")
            return
        
        description = input("  Description (optional): ").strip()
        
        print("  Priority: 1=High, 2=Medium, 3=Low")
        priority_str = input("  Priority (default 2): ").strip()
        priority = int(priority_str) if priority_str.isdigit() and 1 <= int(priority_str) <= 3 else 2
        
        tags_str = input("  Tags (comma-separated, optional): ").strip()
        tags = [t.strip() for t in tags_str.split(",")] if tags_str else []
        
        todo = self.repo.add(title, description, priority, tags)
        print(f"  ✅ Todo #{todo.id} added!")
    
    def complete_todo(self) -> None:
        """Mark a todo as completed."""
        self.display_todos([t for t in self.repo.get_all() if not t.completed])
        
        todo_id_str = input("\n  Enter todo ID to complete: ").strip()
        if not todo_id_str.isdigit():
            print("  Invalid ID!")
            return
        
        todo = self.repo.complete(int(todo_id_str))
        if todo:
            print(f"  ✅ Todo #{todo.id} marked as completed!")
        else:
            print("  Todo not found or already completed.")
    
    def delete_todo(self) -> None:
        """Delete a todo."""
        self.display_todos()
        
        todo_id_str = input("\n  Enter todo ID to delete: ").strip()
        if not todo_id_str.isdigit():
            print("  Invalid ID!")
            return
        
        if self.repo.delete(int(todo_id_str)):
            print(f"  ✅ Todo #{todo_id_str} deleted!")
        else:
            print("  Todo not found.")
    
    def search_todos(self) -> None:
        """Search todos by keyword."""
        query = input("\n  Search term: ").strip()
        if not query:
            return
        
        results = self.repo.search(query)
        print(f"\n  Found {len(results)} matching todos:")
        self.display_todos(results)
    
    def filter_by_priority(self) -> None:
        """Filter todos by priority."""
        priority_str = input("\n  Priority (1=High, 2=Medium, 3=Low): ").strip()
        if not priority_str.isdigit() or int(priority_str) not in [1, 2, 3]:
            print("  Invalid priority!")
            return
        
        priority = int(priority_str)
        include_completed = input("  Include completed? (y/n): ").strip().lower() == 'y'
        
        results = self.repo.get_by_priority(priority, include_completed)
        self.display_todos(results)
    
    def filter_by_tag(self) -> None:
        """Filter todos by tag."""
        tag = input("\n  Tag: ").strip()
        if not tag:
            return
        
        include_completed = input("  Include completed? (y/n): ").strip().lower() == 'y'
        
        results = self.repo.get_by_tag(tag, include_completed)
        self.display_todos(results)
    
    def clear_completed(self) -> None:
        """Clear all completed todos."""
        confirm = input("  Delete all completed todos? (y/n): ").strip().lower()
        if confirm == 'y':
            count = self.repo.clear_completed()
            print(f"  ✅ Removed {count} completed todos!")
    
    def show_help(self) -> None:
        """Display help information."""
        help_text = """
╔══════════════════════════════════════════════════════════════════╗
║                      TODO APPLICATION HELP                       ║
╠══════════════════════════════════════════════════════════════════╣
║  Commands:                                                       ║
║    list / l     - List all todos                                 ║
║    add / a      - Add a new todo                                 ║
║    complete / c - Mark a todo as completed                       ║
║    delete / d   - Delete a todo                                  ║
║    search / s   - Search todos                                   ║
║    priority / p - Filter by priority                             ║
║    tag / t      - Filter by tag                                  ║
║    clear / cl   - Clear completed todos                          ║
║    stats / st   - Show statistics                                ║
║    help / h     - Show this help                                 ║
║    quit / q     - Exit application                               ║
╚══════════════════════════════════════════════════════════════════╝
"""
        print(help_text)
    
    def run(self) -> None:
        """Run the todo application main loop."""
        print("\n" + "=" * 50)
        print("     WELCOME TO TODO APPLICATION")
        print("=" * 50)
        
        self.show_help()
        
        while self.running:
            try:
                command = input("\n> ").strip().lower()
                
                if command in ['list', 'l']:
                    self.display_todos()
                elif command in ['add', 'a']:
                    self.add_todo()
                elif command in ['complete', 'c']:
                    self.complete_todo()
                elif command in ['delete', 'd']:
                    self.delete_todo()
                elif command in ['search', 's']:
                    self.search_todos()
                elif command in ['priority', 'p']:
                    self.filter_by_priority()
                elif command in ['tag', 't']:
                    self.filter_by_tag()
                elif command in ['clear', 'cl']:
                    self.clear_completed()
                elif command in ['stats', 'st']:
                    self.display_statistics()
                elif command in ['help', 'h']:
                    self.show_help()
                elif command in ['quit', 'q', 'exit']:
                    print("\n  Goodbye! 👋")
                    self.running = False
                elif command:
                    print("  Unknown command. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n\n  Use 'quit' to exit")
            except Exception as e:
                print(f"  Error: {e}")


def demonstrate_todo_application():
    """
    Demonstrate the todo application (non-interactive demo).
    """
    print("\n" + "=" * 60)
    print("SECTION 3: TODO APPLICATION")
    print("=" * 60)
    
    # Create a temporary repository for demo
    repo = TodoRepository("demo_todos.json")
    
    # Add sample todos
    print("\n1. ADDING SAMPLE TODOS")
    print("-" * 40)
    
    repo.add("Complete Python Metromap Series", "Finish all stories", priority=1, tags=["learning", "python"])
    repo.add("Review pull requests", "Check team PRs", priority=1, tags=["work"])
    repo.add("Buy groceries", "Milk, eggs, bread, cheese", priority=3, tags=["personal", "shopping"])
    repo.add("Write blog post", "About list comprehensions", priority=2, tags=["writing"])
    repo.add("Exercise", "30 minutes cardio", priority=2, tags=["health"])
    
    print("  Added 5 sample todos")
    
    # Display all todos
    print("\n2. DISPLAYING ALL TODOS")
    print("-" * 40)
    
    todos = repo.get_all()
    for todo in todos:
        print(f"  {todo}")
    
    # Complete a todo
    print("\n3. COMPLETING A TODO")
    print("-" * 40)
    
    repo.complete(3)
    print("  Completed todo #3 (Buy groceries)")
    
    # Display pending todos
    print("\n4. PENDING TODOS")
    print("-" * 40)
    
    pending = repo.get_all(include_completed=False)
    for todo in pending:
        print(f"  {todo}")
    
    # Filter by priority
    print("\n5. HIGH PRIORITY TODOS")
    print("-" * 40)
    
    high_priority = repo.get_by_priority(1)
    for todo in high_priority:
        print(f"  {todo}")
    
    # Search
    print("\n6. SEARCH RESULTS (searching for 'python')")
    print("-" * 40)
    
    results = repo.search("python")
    for todo in results:
        print(f"  {todo}")
    
    # Statistics
    print("\n7. STATISTICS")
    print("-" * 40)
    
    stats = repo.get_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.1f}")
        else:
            print(f"  {key}: {value}")
    
    # Clear completed
    print("\n8. CLEARING COMPLETED TODOS")
    print("-" * 40)
    
    count = repo.clear_completed()
    print(f"  Removed {count} completed todos")
    
    # Final list
    print("\n9. FINAL TODO LIST")
    print("-" * 40)
    
    for todo in repo.get_all():
        print(f"  {todo}")
    
    # Clean up demo file
    if os.path.exists("demo_todos.json"):
        os.remove("demo_todos.json")
        print("\n  Cleaned up demo file")
    
    print("\n💡 To run the interactive todo application:")
    print("   app = TodoCLI()")
    print("   app.run()")


if __name__ == "__main__":
    demonstrate_todo_application()
```

---

## 🛒 Section 4: Shopping Cart System

A complete shopping cart system demonstrating lists in an e-commerce context.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of the cart
- Open/Closed: New discount types can be added

**Design Patterns:**
- Builder Pattern: Builds cart incrementally
- Strategy Pattern: Different discount strategies

```python
"""
SHOPPING CART SYSTEM: COMPLETE LIST DEMONSTRATION

This section builds a complete shopping cart system using lists.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New discount types can be added

Design Patterns:
- Builder Pattern: Builds cart incrementally
- Strategy Pattern: Different discount strategies
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class Product:
    """Product in the catalog."""
    sku: str
    name: str
    price: float
    category: str
    tax_rate: float = 0.08
    in_stock: bool = True
    
    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


@dataclass
class CartItem:
    """Item in the shopping cart."""
    product: Product
    quantity: int
    
    def subtotal(self) -> float:
        """Calculate line item subtotal."""
        return self.product.price * self.quantity
    
    def tax(self) -> float:
        """Calculate line item tax."""
        return self.subtotal() * self.product.tax_rate
    
    def total(self) -> float:
        """Calculate line item total."""
        return self.subtotal() + self.tax()
    
    def __str__(self) -> str:
        return f"{self.quantity}x {self.product.name} @ ${self.product.price:.2f} = ${self.subtotal():.2f}"


class Inventory:
    """
    Product inventory management.
    
    Design Pattern: Repository Pattern - Product storage
    """
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self._initialize_inventory()
    
    def _initialize_inventory(self) -> None:
        """Initialize with sample products."""
        sample_products = [
            ("P001", "Laptop", 999.99, "Electronics", 0.08),
            ("P002", "Wireless Mouse", 29.99, "Electronics", 0.08),
            ("P003", "Mechanical Keyboard", 89.99, "Electronics", 0.08),
            ("P004", "USB-C Monitor", 299.99, "Electronics", 0.08),
            ("P005", "Premium Notebook", 4.99, "Stationery", 0.05),
            ("P006", "Gel Pen Set", 2.99, "Stationery", 0.05),
            ("P007", "Laptop Backpack", 49.99, "Accessories", 0.07),
            ("P008", "Water Bottle", 19.99, "Accessories", 0.07)
        ]
        
        for sku, name, price, category, tax_rate in sample_products:
            self.products[sku] = Product(sku, name, price, category, tax_rate)
    
    def get_product(self, sku: str) -> Optional[Product]:
        """Get product by SKU."""
        return self.products.get(sku)
    
    def search(self, query: str) -> List[Product]:
        """Search products by name or SKU."""
        query_lower = query.lower()
        return [
            p for p in self.products.values()
            if query_lower in p.name.lower() or query_lower in p.sku.lower()
        ]
    
    def list_all(self) -> List[Product]:
        """List all products."""
        return list(self.products.values())


class DiscountStrategy:
    """Base class for discount strategies."""
    
    def apply(self, subtotal: float) -> Tuple[float, str]:
        """Apply discount and return (discount_amount, description)."""
        raise NotImplementedError


class PercentageDiscount(DiscountStrategy):
    """Percentage-based discount."""
    
    def __init__(self, percentage: float, code: str, description: str):
        self.percentage = percentage
        self.code = code
        self.description = description
    
    def apply(self, subtotal: float) -> Tuple[float, str]:
        discount = subtotal * (self.percentage / 100)
        return discount, f"{self.description} ({self.percentage}% off)"


class FixedDiscount(DiscountStrategy):
    """Fixed amount discount."""
    
    def __init__(self, amount: float, code: str, description: str):
        self.amount = amount
        self.code = code
        self.description = description
    
    def apply(self, subtotal: float) -> Tuple[float, str]:
        discount = min(self.amount, subtotal)
        return discount, f"{self.description} (${self.amount:.2f} off)"


class FreeShippingDiscount(DiscountStrategy):
    """Free shipping discount (affects shipping, not subtotal)."""
    
    def __init__(self, code: str):
        self.code = code
    
    def apply(self, subtotal: float) -> Tuple[float, str]:
        return 0, "Free shipping"


class ShoppingCart:
    """
    Shopping cart with list-based item storage.
    
    Design Pattern: Builder Pattern - Add items incrementally
    """
    
    def __init__(self):
        self.items: List[CartItem] = []
        self.discount: Optional[DiscountStrategy] = None
        self.shipping_cost: float = 5.99
    
    def add_item(self, product: Product, quantity: int = 1) -> 'ShoppingCart':
        """Add item to cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        # Check if already in cart
        for item in self.items:
            if item.product.sku == product.sku:
                item.quantity += quantity
                print(f"  Updated {product.name}: {item.quantity} total")
                return self
        
        self.items.append(CartItem(product, quantity))
        print(f"  Added {quantity}x {product.name}")
        return self
    
    def remove_item(self, sku: str) -> 'ShoppingCart':
        """Remove item from cart."""
        original_length = len(self.items)
        self.items = [item for item in self.items if item.product.sku != sku]
        if len(self.items) < original_length:
            print(f"  Removed product {sku}")
        else:
            print(f"  Product {sku} not found")
        return self
    
    def update_quantity(self, sku: str, quantity: int) -> 'ShoppingCart':
        """Update item quantity."""
        if quantity <= 0:
            return self.remove_item(sku)
        
        for item in self.items:
            if item.product.sku == sku:
                item.quantity = quantity
                print(f"  Updated quantity to {quantity}")
                return self
        
        print(f"  Product {sku} not found")
        return self
    
    def apply_discount(self, discount: DiscountStrategy) -> 'ShoppingCart':
        """Apply discount to cart."""
        self.discount = discount
        print(f"  Applied discount: {discount.code}")
        return self
    
    def clear(self) -> 'ShoppingCart':
        """Clear the cart."""
        self.items.clear()
        self.discount = None
        print("  Cart cleared")
        return self
    
    def subtotal(self) -> float:
        """Calculate subtotal."""
        return sum(item.subtotal() for item in self.items)
    
    def discount_amount(self) -> float:
        """Calculate discount amount."""
        if not self.discount:
            return 0.0
        discount, _ = self.discount.apply(self.subtotal())
        return discount
    
    def discounted_subtotal(self) -> float:
        """Calculate subtotal after discount."""
        return self.subtotal() - self.discount_amount()
    
    def tax(self) -> float:
        """Calculate total tax."""
        return sum(item.tax() for item in self.items)
    
    def shipping(self) -> float:
        """Calculate shipping cost."""
        # Free shipping for orders over $50
        if self.discounted_subtotal() >= 50:
            return 0.0
        return self.shipping_cost
    
    def total(self) -> float:
        """Calculate final total."""
        return self.discounted_subtotal() + self.tax() + self.shipping()
    
    def item_count(self) -> int:
        """Get total number of items (sum of quantities)."""
        return sum(item.quantity for item in self.items)
    
    def unique_items_count(self) -> int:
        """Get number of unique products."""
        return len(self.items)
    
    def is_empty(self) -> bool:
        """Check if cart is empty."""
        return len(self.items) == 0
    
    def get_summary(self) -> Dict[str, Any]:
        """Get cart summary."""
        return {
            "items": [(item.product.name, item.quantity, item.subtotal()) for item in self.items],
            "subtotal": self.subtotal(),
            "discount": self.discount_amount(),
            "discounted_subtotal": self.discounted_subtotal(),
            "tax": self.tax(),
            "shipping": self.shipping(),
            "total": self.total(),
            "item_count": self.item_count(),
            "unique_items": self.unique_items_count()
        }
    
    def display(self) -> None:
        """Display cart contents."""
        if self.is_empty():
            print("\n  Cart is empty")
            return
        
        print("\n" + "-" * 50)
        print("SHOPPING CART")
        print("-" * 50)
        
        for item in self.items:
            print(f"  {item.quantity}x {item.product.name}")
            print(f"     @ ${item.product.price:.2f} = ${item.subtotal():.2f}")
        
        print("-" * 50)
        print(f"  Subtotal: ${self.subtotal():.2f}")
        
        if self.discount:
            discount_amt, discount_desc = self.discount.apply(self.subtotal())
            print(f"  Discount: -${discount_amt:.2f} ({discount_desc})")
            print(f"  After discount: ${self.discounted_subtotal():.2f}")
        
        print(f"  Tax: ${self.tax():.2f}")
        print(f"  Shipping: ${self.shipping():.2f}")
        print("-" * 50)
        print(f"  TOTAL: ${self.total():.2f}")
        print("-" * 50)
    
    def checkout(self, payment_method: str, amount_paid: float) -> Dict[str, Any]:
        """Process checkout."""
        if self.is_empty():
            raise ValueError("Cannot checkout empty cart")
        
        total_due = self.total()
        
        if amount_paid < total_due:
            raise ValueError(f"Insufficient payment. Due: ${total_due:.2f}")
        
        order = {
            "order_id": f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "timestamp": datetime.now().isoformat(),
            "items": self.get_summary()["items"],
            "subtotal": self.subtotal(),
            "discount": self.discount_amount(),
            "tax": self.tax(),
            "shipping": self.shipping(),
            "total": total_due,
            "payment_method": payment_method,
            "amount_paid": amount_paid,
            "change": amount_paid - total_due,
            "status": "completed"
        }
        
        self.clear()
        return order


class ShoppingCartCLI:
    """
    Command-line interface for shopping cart.
    
    Design Pattern: Command Pattern - CLI commands
    """
    
    def __init__(self):
        self.inventory = Inventory()
        self.cart = ShoppingCart()
        self.running = True
    
    def browse_products(self) -> None:
        """Display all products."""
        print("\n" + "-" * 60)
        print("PRODUCT CATALOG")
        print("-" * 60)
        print(f"{'SKU':<8} {'Name':<25} {'Price':<10} {'Category':<15}")
        print("-" * 60)
        
        for product in self.inventory.list_all():
            print(f"{product.sku:<8} {product.name:<25} ${product.price:<9.2f} {product.category:<15}")
        print("-" * 60)
    
    def search_products(self) -> None:
        """Search for products."""
        query = input("\n  Enter search term: ").strip()
        if not query:
            return
        
        results = self.inventory.search(query)
        
        if not results:
            print(f"  No products found matching '{query}'")
            return
        
        print(f"\n  Found {len(results)} products:")
        for product in results:
            print(f"    {product.sku}: {product.name} - ${product.price:.2f}")
    
    def add_to_cart(self) -> None:
        """Add product to cart."""
        sku = input("\n  Enter product SKU: ").strip().upper()
        product = self.inventory.get_product(sku)
        
        if not product:
            print(f"  Product '{sku}' not found")
            return
        
        quantity_str = input("  Enter quantity (default 1): ").strip()
        quantity = int(quantity_str) if quantity_str.isdigit() else 1
        
        if quantity <= 0:
            print("  Quantity must be positive")
            return
        
        self.cart.add_item(product, quantity)
    
    def view_cart(self) -> None:
        """Display cart contents."""
        self.cart.display()
    
    def update_cart(self) -> None:
        """Update cart items."""
        if self.cart.is_empty():
            print("  Cart is empty")
            return
        
        self.cart.display()
        print("\n  Update options:")
        print("    1. Remove item")
        print("    2. Change quantity")
        print("    3. Clear cart")
        
        choice = input("\n  Choice: ").strip()
        
        if choice == "1":
            sku = input("  Enter SKU to remove: ").strip().upper()
            self.cart.remove_item(sku)
        elif choice == "2":
            sku = input("  Enter SKU to update: ").strip().upper()
            quantity_str = input("  Enter new quantity: ").strip()
            if quantity_str.isdigit():
                self.cart.update_quantity(sku, int(quantity_str))
            else:
                print("  Invalid quantity")
        elif choice == "3":
            confirm = input("  Clear entire cart? (y/n): ").strip().lower()
            if confirm == 'y':
                self.cart.clear()
    
    def apply_discount(self) -> None:
        """Apply discount to cart."""
        if self.cart.is_empty():
            print("  Cart is empty")
            return
        
        code = input("\n  Enter discount code: ").strip().upper()
        
        discounts = {
            "SAVE10": PercentageDiscount(10, "SAVE10", "10% off"),
            "SAVE20": PercentageDiscount(20, "SAVE20", "20% off"),
            "WELCOME": PercentageDiscount(15, "WELCOME", "Welcome discount"),
            "FREESHIP": FreeShippingDiscount("FREESHIP")
        }
        
        if code not in discounts:
            print(f"  Invalid discount code: {code}")
            return
        
        self.cart.apply_discount(discounts[code])
    
    def checkout(self) -> None:
        """Process checkout."""
        if self.cart.is_empty():
            print("  Cannot checkout: Cart is empty")
            return
        
        self.cart.display()
        
        print("\n  Payment methods:")
        print("    1. Credit Card")
        print("    2. PayPal")
        print("    3. Cash")
        
        payment_choice = input("\n  Select payment method: ").strip()
        payment_methods = {"1": "Credit Card", "2": "PayPal", "3": "Cash"}
        
        if payment_choice not in payment_methods:
            print("  Invalid payment method")
            return
        
        payment_method = payment_methods[payment_choice]
        total = self.cart.total()
        
        print(f"\n  Total due: ${total:.2f}")
        
        if payment_method == "Cash":
            cash_str = input("  Enter cash amount: ").strip()
            try:
                cash = float(cash_str)
                if cash < total:
                    print(f"  Insufficient payment. Need ${total - cash:.2f} more")
                    return
                change = cash - total
                if change > 0:
                    print(f"  Change: ${change:.2f}")
            except ValueError:
                print("  Invalid amount")
                return
        
        order = self.cart.checkout(payment_method, total)
        
        print("\n" + "=" * 50)
        print("ORDER CONFIRMATION")
        print("=" * 50)
        print(f"  Order ID: {order['order_id']}")
        print(f"  Total: ${order['total']:.2f}")
        print(f"  Payment: {order['payment_method']}")
        print("=" * 50)
        print("  Thank you for shopping!")
    
    def show_help(self) -> None:
        """Display help information."""
        help_text = """
╔══════════════════════════════════════════════════════════════════╗
║                    SHOPPING CART HELP                            ║
╠══════════════════════════════════════════════════════════════════╣
║  Commands:                                                       ║
║    browse / b  - Browse all products                             ║
║    search / s  - Search products                                 ║
║    add / a     - Add product to cart                             ║
║    view / v    - View cart                                       ║
║    update / u  - Update cart (remove/change quantity)            ║
║    discount / d - Apply discount code                            ║
║    checkout / c - Proceed to checkout                            ║
║    help / h    - Show this help                                  ║
║    quit / q    - Exit application                                ║
╚══════════════════════════════════════════════════════════════════╝
"""
        print(help_text)
    
    def run(self) -> None:
        """Run the shopping cart CLI."""
        print("\n" + "=" * 50)
        print("    WELCOME TO METROMAP MART")
        print("=" * 50)
        
        self.show_help()
        
        while self.running:
            try:
                command = input("\n> ").strip().lower()
                
                if command in ['browse', 'b']:
                    self.browse_products()
                elif command in ['search', 's']:
                    self.search_products()
                elif command in ['add', 'a']:
                    self.add_to_cart()
                elif command in ['view', 'v']:
                    self.view_cart()
                elif command in ['update', 'u']:
                    self.update_cart()
                elif command in ['discount', 'd']:
                    self.apply_discount()
                elif command in ['checkout', 'c']:
                    self.checkout()
                elif command in ['help', 'h']:
                    self.show_help()
                elif command in ['quit', 'q', 'exit']:
                    print("\n  Thank you for shopping! Goodbye! 👋")
                    self.running = False
                elif command:
                    print("  Unknown command. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n\n  Use 'quit' to exit")
            except Exception as e:
                print(f"  Error: {e}")


def demonstrate_shopping_cart():
    """
    Demonstrate the shopping cart system (non-interactive demo).
    """
    print("\n" + "=" * 60)
    print("SECTION 4: SHOPPING CART SYSTEM")
    print("=" * 60)
    
    inventory = Inventory()
    cart = ShoppingCart()
    
    print("\n1. BROWSING PRODUCTS")
    print("-" * 40)
    
    for product in inventory.list_all():
        print(f"  {product.sku}: {product.name} - ${product.price:.2f}")
    
    print("\n2. ADDING ITEMS TO CART")
    print("-" * 40)
    
    laptop = inventory.get_product("P001")
    mouse = inventory.get_product("P002")
    notebook = inventory.get_product("P005")
    
    cart.add_item(laptop, 1)
    cart.add_item(mouse, 2)
    cart.add_item(notebook, 3)
    
    cart.display()
    
    print("\n3. APPLYING DISCOUNT")
    print("-" * 40)
    
    discount = PercentageDiscount(10, "SAVE10", "10% off")
    cart.apply_discount(discount)
    cart.display()
    
    print("\n4. CART SUMMARY")
    print("-" * 40)
    
    summary = cart.get_summary()
    for key, value in summary.items():
        if isinstance(value, float):
            print(f"  {key}: ${value:.2f}")
        else:
            print(f"  {key}: {value}")
    
    print("\n5. CHECKOUT")
    print("-" * 40)
    
    total = cart.total()
    order = cart.checkout("Credit Card", total)
    
    print(f"  Order ID: {order['order_id']}")
    print(f"  Total paid: ${order['amount_paid']:.2f}")
    print(f"  Status: {order['status']}")
    
    print("\n6. CART AFTER CHECKOUT (should be empty)")
    print("-" * 40)
    
    cart.display()
    
    print("\n💡 To run the interactive shopping cart:")
    print("   cli = ShoppingCartCLI()")
    print("   cli.run()")


if __name__ == "__main__":
    demonstrate_shopping_cart()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **List Creation** – `[]` or `list()`. Can hold any types. Allow duplicates.

- **Accessing Elements** – Indexing (`[0]`), negative indexing (`[-1]`), slicing (`[1:4]`).

- **Modifying Lists** – `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `del`, `clear()`.

- **List Methods** – `sort()`, `reverse()`, `index()`, `count()`, `copy()`.

- **Sorting** – `sort()` modifies in-place. `sorted()` returns new list. Custom keys with `key=`.

- **List Comprehensions** – `[expr for item in iterable if condition]`. Nested comprehensions for flattening.

- **Copying** – Assignment creates reference. Shallow copy with `[:]`, `list()`, `.copy()`. Deep copy with `copy.deepcopy()`.

- **Todo Application** – Complete CRUD operations. Search, filter, statistics, persistence.

- **Shopping Cart** – Product catalog, cart operations, discounts, checkout.

- **SOLID Principles Applied** – Single Responsibility (each method one operation), Open/Closed (new features extendable), Interface Segregation (focused methods).

- **Design Patterns Used** – Collection Pattern (list interface), Command Pattern (operations), Repository Pattern (storage), Builder Pattern (incremental building), Strategy Pattern (discounts), Iterator Pattern (iteration).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale

- **📚 Series C Catalog:** Data Structures Express – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Tuples – Immutable Collections (Series C, Story 2)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 1 | 4 | 20% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **19** | **33** | **37%** |

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

**Next Story:** Series C, Story 2: The 2026 Python Metromap: Tuples – Immutable Collections

---

## 📝 Your Invitation

You've mastered lists. Now build something with what you've learned:

1. **Build a playlist manager** – Create a playlist with add, remove, shuffle, repeat, and save/load functionality.

2. **Create a transaction log** – Build a system that logs transactions, allows filtering by date/amount, and generates summaries.

3. **Build a task manager** – Extend the todo app with due dates, reminders, and categories.

4. **Create a gradebook** – Store student grades, calculate averages, find highest/lowest, generate reports.

5. **Build a queue system** – Implement a FIFO queue using lists (append/pop(0)) or collections.deque.

**You've mastered lists. Next stop: Tuples!**

---

*Found this helpful? Clap, comment, and share what you built with lists. Next stop: Tuples!* 🚇