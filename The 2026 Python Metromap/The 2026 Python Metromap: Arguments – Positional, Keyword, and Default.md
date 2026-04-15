# The 2026 Python Metromap: Arguments – Positional, Keyword, and Default

## Series B: Functions & Modules Yard | Story 2 of 6

![The 2026 Python Metromap/images/Arguments – Positional, Keyword, and Default](images/Arguments – Positional, Keyword, and Default.png)

## 📖 Introduction

**Welcome to the second stop on the Functions & Modules Yard Line.**

You've mastered defining functions. You know how to encapsulate logic into reusable blocks, add docstrings, and follow best practices. But there's more to functions than just defining them—how you pass data into functions is just as important.

Arguments are the inputs that make functions flexible. Positional arguments are passed in order. Keyword arguments are passed by name, making code more readable. Default arguments provide fallback values when callers don't specify them. And variable-length arguments (`*args` and `**kwargs`) let you handle any number of inputs.

This story—**The 2026 Python Metromap: Arguments – Positional, Keyword, and Default**—is your guide to mastering function arguments. We'll build a flexible report generator that can output PDF, CSV, or JSON with different options. We'll create a configuration system that handles defaults and overrides. We'll build a data processing pipeline that accepts variable numbers of transformations. And we'll implement a complete API client that demonstrates all argument types in action.

**Let's pass some arguments.**

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

- 📋 **The 2026 Python Metromap: Arguments – Positional, Keyword, and Default** – Flexible report generator for PDF, CSV, and JSON outputs. **⬅️ YOU ARE HERE**

- 📤 **The 2026 Python Metromap: Return Values – Getting Results Back** – API response formatter; standardized success and error responses. 🔜 *Up Next*

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines.

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver.

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📋 Section 1: Positional Arguments – The Basics

Positional arguments are passed to a function in the order they are defined. The first argument goes to the first parameter, the second to the second, and so on.

**SOLID Principle Applied: Interface Segregation** – Functions should have clear, predictable parameter orders.

**Design Pattern: Command Pattern** – Arguments are the command data passed to the function.

```python
"""
POSITIONAL ARGUMENTS: THE BASICS

This section covers positional arguments - arguments passed in order.

SOLID Principle: Interface Segregation
- Functions should have clear, predictable parameter orders

Design Pattern: Command Pattern
- Arguments are command data passed to the function
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import time


def demonstrate_positional_arguments():
    """
    Demonstrates positional arguments in functions.
    
    Positional arguments are matched by position/order.
    """
    print("=" * 60)
    print("SECTION 1A: POSITIONAL ARGUMENTS")
    print("=" * 60)
    
    # BASIC POSITIONAL ARGUMENTS
    print("\n1. BASIC POSITIONAL ARGUMENTS")
    print("-" * 40)
    
    def create_user(name, age, email):
        """Create a user with positional arguments."""
        return {
            "name": name,
            "age": age,
            "email": email
        }
    
    # Arguments passed in the defined order
    user1 = create_user("Alice", 28, "alice@example.com")
    user2 = create_user("Bob", 35, "bob@example.com")
    
    print(f"  User 1: {user1}")
    print(f"  User 2: {user2}")
    
    # ORDER MATTERS!
    print("\n2. ORDER MATTERS")
    print("-" * 40)
    
    # Different order produces different results
    wrong_user = create_user("alice@example.com", "Alice", 28)
    print(f"  Wrong order: {wrong_user}")
    print("  ⚠️ The function doesn't know you swapped name and email!")
    
    # MULTIPLE ARGUMENTS
    print("\n3. MULTIPLE POSITIONAL ARGUMENTS")
    print("-" * 40)
    
    def calculate_shipping(weight, distance, base_rate, multiplier):
        """Calculate shipping cost with multiple factors."""
        return (base_rate + weight * 0.5) * (1 + distance * multiplier / 100)
    
    cost = calculate_shipping(5.5, 150, 5.0, 0.05)
    print(f"  Shipping cost: ${cost:.2f}")
    
    # MIXING TYPES
    print("\n4. MIXING TYPES")
    print("-" * 40)
    
    def process_order(order_id, items, is_express, notes):
        """Process order with mixed argument types."""
        return {
            "order_id": order_id,
            "item_count": len(items),
            "express": is_express,
            "notes": notes
        }
    
    result = process_order(10042, ["laptop", "mouse"], True, "Gift wrap")
    print(f"  Processed: {result}")
    
    # REQUIRED ARGUMENTS (no defaults)
    print("\n5. REQUIRED ARGUMENTS")
    print("-" * 40)
    
    def send_message(recipient, subject, body):
        """All arguments are required."""
        return f"To: {recipient}\nSubject: {subject}\nBody: {body}"
    
    # All three arguments required
    message = send_message("alice@example.com", "Hello", "How are you?")
    print(f"  Message sent to alice@example.com")
    
    # This would raise TypeError:
    # send_message("alice@example.com", "Hello")  # Missing body


def demonstrate_argument_passing():
    """
    Demonstrates how arguments are passed (pass by object reference).
    
    Python uses "pass by object reference" - mutable objects can be modified.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: HOW ARGUMENTS ARE PASSED")
    print("=" * 60)
    
    # IMMUTABLE ARGUMENTS (cannot be modified)
    print("\n1. IMMUTABLE ARGUMENTS (int, str, tuple, bool)")
    print("-" * 40)
    
    def modify_immutable(x):
        print(f"  Inside function before: x = {x}, id = {id(x)}")
        x = x + 10
        print(f"  Inside function after: x = {x}, id = {id(x)}")
        return x
    
    value = 5
    print(f"Outside before: value = {value}, id = {id(value)}")
    result = modify_immutable(value)
    print(f"Outside after: value = {value}, id = {id(value)} (unchanged!)")
    print(f"Returned: {result}")
    
    print("\n  ⚠️ Immutable arguments cannot be changed outside the function")
    
    # MUTABLE ARGUMENTS (can be modified)
    print("\n2. MUTABLE ARGUMENTS (list, dict, set)")
    print("-" * 40)
    
    def modify_mutable(items):
        print(f"  Inside before: {items}, id = {id(items)}")
        items.append("new item")
        items[0] = "changed"
        print(f"  Inside after: {items}, id = {id(items)}")
    
    my_list = ["a", "b", "c"]
    print(f"Outside before: {my_list}, id = {id(my_list)}")
    modify_mutable(my_list)
    print(f"Outside after: {my_list}, id = {id(my_list)} (modified!)")
    
    print("\n  ✓ Mutable arguments CAN be modified outside the function")
    
    # AVOIDING MUTATION (copy before modifying)
    print("\n3. AVOIDING MUTATION (defensive copying)")
    print("-" * 40)
    
    def safe_process(items):
        """Process without modifying original."""
        # Create a copy before modifying
        items_copy = items.copy()
        items_copy.append("new")
        items_copy[0] = "changed"
        return items_copy
    
    original = ["x", "y", "z"]
    print(f"Original: {original}")
    result = safe_process(original)
    print(f"Result (modified copy): {result}")
    print(f"Original (unchanged): {original}")
    
    # BEST PRACTICE: Document mutation behavior
    print("\n4. BEST PRACTICE: Document mutation")
    print("-" * 40)
    
    def update_user_profile(profile: dict, updates: dict) -> dict:
        """
        Update user profile with new values.
        
        WARNING: This function modifies the profile dictionary in-place.
        Consider using copy if you need to preserve original.
        
        Args:
            profile: User profile dict (modified in-place)
            updates: Updates to apply
            
        Returns:
            The modified profile (same object)
        """
        profile.update(updates)
        return profile
    
    user = {"name": "Alice", "age": 28}
    print(f"Before: {user}")
    update_user_profile(user, {"age": 29, "city": "NYC"})
    print(f"After: {user} (modified in-place)")


def demonstrate_required_vs_optional():
    """
    Demonstrates the difference between required and optional arguments.
    
    Required arguments have no default value and must be provided.
    Optional arguments have default values and can be omitted.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: REQUIRED VS OPTIONAL ARGUMENTS")
    print("=" * 60)
    
    # REQUIRED ARGUMENTS
    print("\n1. REQUIRED ARGUMENTS (no defaults)")
    print("-" * 40)
    
    def connect_to_db(host, port, username, password):
        """All four arguments are required."""
        return f"Connecting to {host}:{port} as {username}"
    
    # Must provide all four
    result = connect_to_db("localhost", 5432, "admin", "secret")
    print(f"  {result}")
    
    # OPTIONAL ARGUMENTS (with defaults)
    print("\n2. OPTIONAL ARGUMENTS (with defaults)")
    print("-" * 40)
    
    def search_products(query, category="all", sort_by="name", limit=10):
        """
        Search products with optional parameters.
        
        Args:
            query: Search term (required)
            category: Product category (default: "all")
            sort_by: Sort field (default: "name")
            limit: Max results (default: 10)
        """
        return {
            "query": query,
            "category": category,
            "sort_by": sort_by,
            "limit": limit
        }
    
    # Only required argument
    result1 = search_products("laptop")
    print(f"  Only query: {result1}")
    
    # Override some defaults
    result2 = search_products("laptop", category="electronics")
    print(f"  With category: {result2}")
    
    # Override multiple
    result3 = search_products("laptop", category="electronics", limit=25)
    print(f"  With category and limit: {result3}")
    
    # All arguments (positional)
    result4 = search_products("laptop", "electronics", "price", 25)
    print(f"  All positional: {result4}")
    
    # RULE: Required arguments must come before optional arguments
    print("\n3. IMPORTANT RULE")
    print("-" * 40)
    
    print("  def func(required1, required2, optional1='default', optional2='default'):")
    print("  ✓ Required parameters must come before optional parameters")
    print("  ✗ def func(optional='default', required):  # SyntaxError!")


if __name__ == "__main__":
    demonstrate_positional_arguments()
    demonstrate_argument_passing()
    demonstrate_required_vs_optional()
```

---

## 🔑 Section 2: Keyword Arguments – Clarity and Flexibility

Keyword arguments are passed by name rather than position. They make code more readable and allow arguments to be passed in any order.

**SOLID Principle Applied: Interface Segregation** – Keyword arguments make function interfaces self-documenting.

**Design Pattern: Named Parameter Pattern** – Parameters identified by name improves code clarity.

```python
"""
KEYWORD ARGUMENTS: CLARITY AND FLEXIBILITY

This section covers keyword arguments - arguments passed by name.

SOLID Principle: Interface Segregation
- Keyword arguments make interfaces self-documenting

Design Pattern: Named Parameter Pattern
- Parameters identified by name improves clarity
"""

from typing import Dict, Any, Optional, List
from datetime import datetime


def demonstrate_keyword_arguments():
    """
    Demonstrates keyword arguments for clarity and flexibility.
    
    Keyword arguments are passed with parameter names.
    """
    print("=" * 60)
    print("SECTION 2A: KEYWORD ARGUMENTS")
    print("=" * 60)
    
    # BASIC KEYWORD ARGUMENTS
    print("\n1. BASIC KEYWORD ARGUMENTS")
    print("-" * 40)
    
    def create_product(name, price, category, in_stock):
        """Create a product with clear parameter names."""
        return {
            "name": name,
            "price": price,
            "category": category,
            "in_stock": in_stock
        }
    
    # Positional arguments (order matters)
    product1 = create_product("Laptop", 999.99, "Electronics", True)
    
    # Keyword arguments (order doesn't matter!)
    product2 = create_product(
        name="Mouse",
        price=29.99,
        category="Electronics",
        in_stock=True
    )
    
    # Mixed order with keywords
    product3 = create_product(
        in_stock=True,
        name="Keyboard",
        category="Accessories",
        price=89.99
    )
    
    print(f"  Product 1 (positional): {product1['name']} - ${product1['price']}")
    print(f"  Product 2 (keywords): {product2['name']} - ${product2['price']}")
    print(f"  Product 3 (mixed order): {product3['name']} - ${product3['price']}")
    
    # READABILITY BENEFIT
    print("\n2. READABILITY BENEFIT")
    print("-" * 40)
    
    # Hard to read - what do these numbers mean?
    def send_email(server, port, username, password, recipient, subject, body, is_html, priority):
        pass
    
    # Without keywords (unclear)
    # send_email("smtp.gmail.com", 587, "user", "pass", "alice@example.com", "Hello", "Body", False, 1)
    
    # With keywords (self-documenting!)
    # send_email(
    #     server="smtp.gmail.com",
    #     port=587,
    #     username="user",
    #     password="pass",
    #     recipient="alice@example.com",
    #     subject="Hello",
    #     body="Body",
    #     is_html=False,
    #     priority=1
    # )
    
    print("  Keyword arguments make function calls self-documenting")
    
    # MIXING POSITIONAL AND KEYWORD
    print("\n3. MIXING POSITIONAL AND KEYWORD ARGUMENTS")
    print("-" * 40)
    
    def configure_logging(level, format_type, output_file, max_size, backup_count):
        """Configure logging with mixed arguments."""
        return {
            "level": level,
            "format": format_type,
            "file": output_file,
            "max_size_mb": max_size,
            "backups": backup_count
        }
    
    # Positional first, then keyword
    config = configure_logging(
        "INFO",                    # positional
        "json",                    # positional
        output_file="app.log",     # keyword
        max_size=10,               # keyword
        backup_count=5             # keyword
    )
    
    print(f"  Config: {config}")
    
    # RULE: Positional arguments must come before keyword arguments
    print("\n4. IMPORTANT RULE")
    print("-" * 40)
    
    print("  def func(pos1, pos2, kw1='default', kw2='default'):")
    print("  ✓ Correct: func(1, 2, kw2='b')")
    print("  ✗ Incorrect: func(kw2='b', 1, 2)  # SyntaxError")
    print("  ✗ Incorrect: func(1, kw1='a', 2)   # SyntaxError")


def demonstrate_default_arguments():
    """
    Demonstrates default arguments and common pitfalls.
    
    Default arguments provide fallback values when not specified.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: DEFAULT ARGUMENTS")
    print("=" * 60)
    
    # SIMPLE DEFAULTS
    print("\n1. SIMPLE DEFAULT ARGUMENTS")
    print("-" * 40)
    
    def greet(name, greeting="Hello", punctuation="!"):
        """Greet with customizable greeting and punctuation."""
        return f"{greeting}, {name}{punctuation}"
    
    print(f"  greet('Alice'): {greet('Alice')}")
    print(f"  greet('Bob', 'Hi'): {greet('Bob', 'Hi')}")
    print(f"  greet('Charlie', greeting='Hey', punctuation='?'): {greet('Charlie', greeting='Hey', punctuation='?')}")
    
    # MULTIPLE DEFAULTS
    print("\n2. MULTIPLE DEFAULTS")
    print("-" * 40)
    
    def create_user(
        username,
        email,
        is_active=True,
        is_admin=False,
        notifications=True,
        theme="light"
    ):
        """Create user with many optional settings."""
        return {
            "username": username,
            "email": email,
            "is_active": is_active,
            "is_admin": is_admin,
            "notifications": notifications,
            "theme": theme
        }
    
    # Minimal arguments
    user1 = create_user("alice", "alice@example.com")
    print(f"  Minimal: {user1}")
    
    # Override some defaults
    user2 = create_user("bob", "bob@example.com", is_admin=True, theme="dark")
    print(f"  Override some: {user2}")
    
    # Override with keyword
    user3 = create_user(
        "charlie",
        "charlie@example.com",
        notifications=False,
        is_active=False
    )
    print(f"  Override with keywords: {user3}")
    
    # COMMON PITFALL: Mutable default arguments
    print("\n3. ⚠️ COMMON PITFALL: MUTABLE DEFAULTS")
    print("-" * 40)
    
    # BAD - mutable default (list)
    def add_item_bad(item, items=[]):
        """BAD: Default list is shared across calls!"""
        items.append(item)
        return items
    
    print("  Bad function with mutable default:")
    print(f"    add_item_bad('a'): {add_item_bad('a')}")
    print(f"    add_item_bad('b'): {add_item_bad('b')}")  # ['a', 'b'] - unexpected!
    print(f"    add_item_bad('c'): {add_item_bad('c')}")  # ['a', 'b', 'c'] - accumulating!
    
    # GOOD - use None as default
    def add_item_good(item, items=None):
        """GOOD: Use None and create new list each time."""
        if items is None:
            items = []
        items.append(item)
        return items
    
    print("\n  Good function with None default:")
    print(f"    add_item_good('a'): {add_item_good('a')}")
    print(f"    add_item_good('b'): {add_item_good('b')}")
    print(f"    add_item_good('c'): {add_item_good('c')}")
    
    # BAD - mutable default (dict)
    def update_config_bad(key, value, config={}):
        """BAD: Default dict is shared across calls!"""
        config[key] = value
        return config
    
    print("\n  Bad dict default (shared across calls):")
    print(f"    update_config_bad('theme', 'dark'): {update_config_bad('theme', 'dark')}")
    print(f"    update_config_bad('lang', 'en'): {update_config_bad('lang', 'en')}")  # Has previous!
    
    # GOOD - use None for dict
    def update_config_good(key, value, config=None):
        """GOOD: Create new dict each time."""
        if config is None:
            config = {}
        config[key] = value
        return config
    
    print("\n  Good dict default:")
    print(f"    update_config_good('theme', 'dark'): {update_config_good('theme', 'dark')}")
    print(f"    update_config_good('lang', 'en'): {update_config_good('lang', 'en')}")
    
    # DYNAMIC DEFAULTS
    print("\n4. DYNAMIC DEFAULTS (using functions)")
    print("-" * 40)
    
    from datetime import datetime
    
    def log_message(message, timestamp=None):
        """Use None and compute default at runtime."""
        if timestamp is None:
            timestamp = datetime.now()
        
        return f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    
    print(f"  log_message('First'): {log_message('First')}")
    print(f"  log_message('Second'): {log_message('Second')}")
    print(f"  log_message('Custom', datetime(2024, 1, 1)): {log_message('Custom', datetime(2024, 1, 1))}")


def demonstrate_parameter_order_rules():
    """
    Demonstrates the correct order of parameters.
    
    Order: positional → default → *args → keyword-only → **kwargs
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: PARAMETER ORDER RULES")
    print("=" * 60)
    
    # CORRECT ORDER
    print("\n1. CORRECT PARAMETER ORDER")
    print("-" * 40)
    
    def correct_order(
        required,           # positional (required)
        optional="default", # positional with default
        *args,              # variable positional
        kw_only=None,       # keyword-only (requires name)
        **kwargs            # variable keyword
    ):
        """Demonstrates correct parameter order."""
        return {
            "required": required,
            "optional": optional,
            "args": args,
            "kw_only": kw_only,
            "kwargs": kwargs
        }
    
    result = correct_order(
        "req",                          # positional
        "opt",                          # optional positional
        1, 2, 3,                        # *args
        kw_only="keyword only",         # keyword-only
        extra1="value1",                # **kwargs
        extra2="value2"                 # **kwargs
    )
    
    print(f"  Result: {result}")
    
    # KEYWORD-ONLY ARGUMENTS (after *)
    print("\n2. KEYWORD-ONLY ARGUMENTS")
    print("-" * 40)
    
    def configure(host, port, *, ssl=False, timeout=30):
        """
        Parameters after '*' are keyword-only.
        They cannot be passed positionally.
        """
        return f"Host: {host}:{port}, SSL: {ssl}, Timeout: {timeout}"
    
    # Correct - using keywords for ssl and timeout
    config1 = configure("localhost", 8080, ssl=True, timeout=60)
    print(f"  With keywords: {config1}")
    
    # This would raise TypeError:
    # configure("localhost", 8080, True, 60)  # ssl and timeout are keyword-only!
    
    # POSITIONAL-ONLY ARGUMENTS (Python 3.8+, using /)
    print("\n3. POSITIONAL-ONLY ARGUMENTS (using /)")
    print("-" * 40)
    
    def create_point(x, y, /, z=0):
        """
        Parameters before '/' are positional-only.
        They cannot be passed as keywords.
        """
        return (x, y, z)
    
    # Correct - positional for x and y
    point1 = create_point(10, 20)
    point2 = create_point(10, 20, z=30)
    print(f"  Point 1: {point1}")
    print(f"  Point 2: {point2}")
    
    # This would raise TypeError:
    # create_point(x=10, y=20)  # x and y are positional-only!
    
    # COMPLETE PARAMETER ORDER
    print("\n4. COMPLETE PARAMETER ORDER SUMMARY")
    print("-" * 40)
    
    print("""
    def func(
        positional_only,      # before '/'
        /,                    # separator
        positional_or_keyword, # after '/', before '*'
        *,                    # separator
        keyword_only,         # after '*'
        **kwargs              # variable keyword
    ):
        pass
    """)
    
    print("  Order from left to right:")
    print("    1. Positional-only parameters (before /)")
    print("    2. Positional-or-keyword parameters")
    print("    3. *args (variable positional)")
    print("    4. Keyword-only parameters (after *)")
    print("    5. **kwargs (variable keyword)")


if __name__ == "__main__":
    demonstrate_keyword_arguments()
    demonstrate_default_arguments()
    demonstrate_parameter_order_rules()
```

---

## 📦 Section 3: Variable-Length Arguments – *args and **kwargs

Variable-length arguments allow functions to accept any number of positional or keyword arguments.

**SOLID Principle Applied: Open/Closed** – Functions with *args/**kwargs can handle new argument types without modification.

**Design Pattern: Adapter Pattern** – *args/**kwargs adapt variable inputs to fixed function signatures.

```python
"""
VARIABLE-LENGTH ARGUMENTS: *args AND **kwargs

This section covers *args (variable positional) and **kwargs (variable keyword).

SOLID Principle: Open/Closed
- Functions can handle new argument types without modification

Design Pattern: Adapter Pattern
- *args/**kwargs adapt variable inputs to fixed signatures
"""

from typing import Any, List, Dict, Tuple
from functools import wraps


def demonstrate_args():
    """
    Demonstrates *args for variable positional arguments.
    
    *args collects extra positional arguments into a tuple.
    """
    print("=" * 60)
    print("SECTION 3A: *args - VARIABLE POSITIONAL ARGUMENTS")
    print("=" * 60)
    
    # BASIC *args
    print("\n1. BASIC *args")
    print("-" * 40)
    
    def sum_all(*args):
        """Sum any number of arguments."""
        total = sum(args)
        return total
    
    print(f"  sum_all(1, 2) = {sum_all(1, 2)}")
    print(f"  sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
    print(f"  sum_all() = {sum_all()}")
    
    # *args with regular parameters
    print("\n2. *args WITH REGULAR PARAMETERS")
    print("-" * 40)
    
    def greet(greeting, *names):
        """Greet multiple people with the same greeting."""
        results = []
        for name in names:
            results.append(f"{greeting}, {name}!")
        return results
    
    result = greet("Hello", "Alice", "Bob", "Charlie")
    print(f"  greet('Hello', 'Alice', 'Bob', 'Charlie'): {result}")
    
    # *args type is tuple
    print("\n3. *args TYPE (tuple)")
    print("-" * 40)
    
    def inspect_args(*args):
        print(f"  Type: {type(args).__name__}")
        print(f"  Length: {len(args)}")
        print(f"  Contents: {args}")
    
    inspect_args(1, 2, 3, "hello", True)
    
    # UNPACKING WITH * (pass list as arguments)
    print("\n4. UNPACKING LISTS WITH *")
    print("-" * 40)
    
    def multiply(a, b, c):
        """Multiply three numbers."""
        return a * b * c
    
    numbers = [2, 3, 4]
    result = multiply(*numbers)  # Unpacks to multiply(2, 3, 4)
    print(f"  multiply(*[2, 3, 4]) = {result}")
    
    # Unpacking with *args in function call
    def process_items(operation, *items):
        """Process items with given operation."""
        if operation == "sum":
            return sum(items)
        elif operation == "product":
            result = 1
            for item in items:
                result *= item
            return result
        elif operation == "count":
            return len(items)
        return None
    
    values = [10, 20, 30, 40, 50]
    print(f"  values = {values}")
    print(f"  process_items('sum', *values) = {process_items('sum', *values)}")
    print(f"  process_items('product', *values) = {process_items('product', *values)}")
    print(f"  process_items('count', *values) = {process_items('count', *values)}")
    
    # PRACTICAL: LOGGING FUNCTION
    print("\n5. PRACTICAL: LOGGING FUNCTION")
    print("-" * 40)
    
    from datetime import datetime
    
    def log(level, *messages):
        """Log multiple messages at once."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        for msg in messages:
            print(f"[{timestamp}] {level}: {msg}")
    
    log("INFO", "User logged in", "Session started", "Loading preferences")
    log("ERROR", "Connection failed", "Retry attempt 1", "Retry attempt 2", "Giving up")


def demonstrate_kwargs():
    """
    Demonstrates **kwargs for variable keyword arguments.
    
    **kwargs collects extra keyword arguments into a dictionary.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: **kwargs - VARIABLE KEYWORD ARGUMENTS")
    print("=" * 60)
    
    # BASIC **kwargs
    print("\n1. BASIC **kwargs")
    print("-" * 40)
    
    def print_kwargs(**kwargs):
        """Print all keyword arguments."""
        for key, value in kwargs.items():
            print(f"  {key} = {value}")
    
    print_kwargs(name="Alice", age=28, city="NYC")
    
    # **kwargs TYPE (dict)
    print("\n2. **kwargs TYPE (dictionary)")
    print("-" * 40)
    
    def inspect_kwargs(**kwargs):
        print(f"  Type: {type(kwargs).__name__}")
        print(f"  Keys: {list(kwargs.keys())}")
        print(f"  Values: {list(kwargs.values())}")
    
    inspect_kwargs(a=1, b=2, c=3)
    
    # **kwargs WITH REGULAR PARAMETERS
    print("\n3. **kwargs WITH REGULAR PARAMETERS")
    print("-" * 40)
    
    def create_profile(name, email, **extra):
        """Create user profile with optional extra fields."""
        profile = {
            "name": name,
            "email": email
        }
        profile.update(extra)
        return profile
    
    profile1 = create_profile("Alice", "alice@example.com")
    profile2 = create_profile("Bob", "bob@example.com", age=35, city="LA", is_admin=True)
    
    print(f"  Minimal: {profile1}")
    print(f"  With extras: {profile2}")
    
    # UNPACKING WITH ** (pass dict as keyword arguments)
    print("\n4. UNPACKING DICTIONARIES WITH **")
    print("-" * 40)
    
    def format_person(name, age, city):
        """Format person information."""
        return f"{name}, {age} years old, from {city}"
    
    person_dict = {"name": "Alice", "age": 28, "city": "NYC"}
    result = format_person(**person_dict)  # Unpacks to format_person(name="Alice", age=28, city="NYC")
    print(f"  format_person(**{person_dict}) = {result}")
    
    # COMBINING *args AND **kwargs
    print("\n5. COMBINING *args AND **kwargs")
    print("-" * 40)
    
    def universal_function(*args, **kwargs):
        """Accept any arguments."""
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
    
    universal_function(1, 2, 3, name="Alice", age=28)
    
    # PRACTICAL: WRAPPER FUNCTION
    print("\n6. PRACTICAL: FUNCTION WRAPPER")
    print("-" * 40)
    
    def timer(func):
        """Decorator that times function execution."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"  {func.__name__} took {end - start:.4f}s")
            return result
        return wrapper
    
    import time
    
    @timer
    def slow_function(*args, **kwargs):
        """Slow function that sleeps."""
        time.sleep(0.1)
        return sum(args)
    
    result = slow_function(1, 2, 3, 4, 5)
    print(f"  Result: {result}")
    
    # FORWARDING ARGUMENTS
    print("\n7. FORWARDING ARGUMENTS TO ANOTHER FUNCTION")
    print("-" * 40)
    
    def send_request(url, method="GET", **kwargs):
        """
        Send HTTP request.
        
        kwargs can include headers, params, data, etc.
        """
        print(f"  URL: {url}")
        print(f"  Method: {method}")
        print(f"  Extra kwargs: {kwargs}")
        # In real code: requests.request(method, url, **kwargs)
    
    def api_call(endpoint, **kwargs):
        """API wrapper that forwards arguments."""
        url = f"https://api.example.com/{endpoint}"
        send_request(url, **kwargs)
    
    api_call("users", method="POST", headers={"Auth": "token"}, data={"name": "Alice"})
    
    # PRACTICAL: CONFIGURATION OVERRIDES
    print("\n8. PRACTICAL: CONFIGURATION OVERRIDES")
    print("-" * 40)
    
    DEFAULT_CONFIG = {
        "host": "localhost",
        "port": 8080,
        "debug": False,
        "log_level": "INFO"
    }
    
    def get_config(**overrides):
        """Get configuration with user overrides."""
        config = DEFAULT_CONFIG.copy()
        config.update(overrides)
        return config
    
    print(f"  Default: {get_config()}")
    print(f"  Override port: {get_config(port=9090)}")
    print(f"  Multiple overrides: {get_config(port=9090, debug=True, log_level='DEBUG')}")


def demonstrate_args_kwargs_patterns():
    """
    Demonstrates common patterns with *args and **kwargs.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: COMMON *args/**kwargs PATTERNS")
    print("=" * 60)
    
    # PATTERN 1: Function that can handle any arguments
    print("\n1. PATTERN: FORWARDING TO ANOTHER FUNCTION")
    print("-" * 40)
    
    def log_and_call(func, *args, **kwargs):
        """Log function call and execute."""
        print(f"  Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  Result: {result}")
        return result
    
    def add(a, b):
        return a + b
    
    log_and_call(add, 5, 3)
    
    # PATTERN 2: Building query strings
    print("\n2. PATTERN: BUILDING QUERY STRINGS")
    print("-" * 40)
    
    def build_query(base_url, **params):
        """Build URL with query parameters."""
        if not params:
            return base_url
        
        query_parts = [f"{key}={value}" for key, value in params.items()]
        query_string = "&".join(query_parts)
        return f"{base_url}?{query_string}"
    
    url = build_query("https://api.example.com/search", q="python", page=2, limit=10)
    print(f"  URL: {url}")
    
    # PATTERN 3: Merging dictionaries
    print("\n3. PATTERN: MERGING DICTIONARIES")
    print("-" * 40)
    
    def merge_dicts(**kwargs):
        """Merge multiple dictionaries passed as kwargs."""
        result = {}
        for key, value in kwargs.items():
            if isinstance(value, dict):
                result.update(value)
            else:
                result[key] = value
        return result
    
    merged = merge_dicts(
        user={"name": "Alice", "age": 28},
        settings={"theme": "dark"},
        extra="value"
    )
    print(f"  Merged: {merged}")
    
    # PATTERN 4: Flexible initialization
    print("\n4. PATTERN: FLEXIBLE CLASS INITIALIZATION")
    print("-" * 40)
    
    class FlexibleConfig:
        """Class that accepts any configuration parameters."""
        
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
        
        def __repr__(self):
            attrs = [f"{k}={v}" for k, v in self.__dict__.items()]
            return f"FlexibleConfig({', '.join(attrs)})"
    
    config1 = FlexibleConfig(host="localhost", port=8080)
    config2 = FlexibleConfig(name="Alice", age=28, city="NYC", active=True)
    
    print(f"  Config 1: {config1}")
    print(f"  Config 2: {config2}")
    
    # PATTERN 5: Argument validation
    print("\n5. PATTERN: ARGUMENT VALIDATION")
    print("-" * 40)
    
    def validate_required(required_args, **kwargs):
        """Validate that all required arguments are present."""
        missing = [arg for arg in required_args if arg not in kwargs]
        if missing:
            raise ValueError(f"Missing required arguments: {missing}")
        return True
    
    try:
        validate_required(["name", "email"], name="Alice")
    except ValueError as e:
        print(f"  Validation error: {e}")
    
    validate_required(["name", "email"], name="Alice", email="alice@example.com")
    print("  Validation passed")


if __name__ == "__main__":
    import time
    demonstrate_args()
    demonstrate_kwargs()
    demonstrate_args_kwargs_patterns()
```

---

## 🏭 Section 4: Flexible Report Generator

A complete report generator that demonstrates all argument types: positional, keyword, default, *args, and **kwargs.

**SOLID Principles Applied:**
- Single Responsibility: Each report format handler has one job
- Open/Closed: New formats can be added without modifying existing code

**Design Patterns:**
- Strategy Pattern: Different formatting strategies
- Factory Pattern: Creates appropriate formatter based on format type

```python
"""
FLEXIBLE REPORT GENERATOR

This section builds a complete report generator that demonstrates
all argument types: positional, keyword, default, *args, **kwargs.

SOLID Principles Applied:
- Single Responsibility: Each formatter handles one format
- Open/Closed: New formats can be added

Design Patterns:
- Strategy Pattern: Different formatting strategies
- Factory Pattern: Creates formatter based on format type
"""

from typing import List, Dict, Any, Optional, Callable
from datetime import datetime
import json
import csv
from io import StringIO


class ReportFormatter:
    """
    Base class for report formatters.
    
    Design Pattern: Strategy Pattern - Different formatting strategies
    """
    
    def format(self, data: List[Dict], **options) -> str:
        """Format data as string."""
        raise NotImplementedError
    
    def extension(self) -> str:
        """Get file extension."""
        raise NotImplementedError


class CSVFormatter(ReportFormatter):
    """Format report as CSV."""
    
    def extension(self) -> str:
        return "csv"
    
    def format(self, data: List[Dict], **options) -> str:
        """
        Format data as CSV.
        
        Options:
            delimiter: CSV delimiter (default: ",")
            include_header: Include header row (default: True)
        """
        delimiter = options.get("delimiter", ",")
        include_header = options.get("include_header", True)
        
        if not data:
            return ""
        
        output = StringIO()
        fieldnames = list(data[0].keys())
        
        writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=delimiter)
        
        if include_header:
            writer.writeheader()
        
        writer.writerows(data)
        
        return output.getvalue()


class JSONFormatter(ReportFormatter):
    """Format report as JSON."""
    
    def extension(self) -> str:
        return "json"
    
    def format(self, data: List[Dict], **options) -> str:
        """
        Format data as JSON.
        
        Options:
            indent: Indentation level (default: 2)
            sort_keys: Sort dictionary keys (default: False)
        """
        indent = options.get("indent", 2)
        sort_keys = options.get("sort_keys", False)
        
        return json.dumps(data, indent=indent, sort_keys=sort_keys)


class HTMLFormatter(ReportFormatter):
    """Format report as HTML."""
    
    def extension(self) -> str:
        return "html"
    
    def format(self, data: List[Dict], **options) -> str:
        """
        Format data as HTML table.
        
        Options:
            title: Report title (default: "Report")
            border: Table border (default: 1)
        """
        title = options.get("title", "Report")
        border = options.get("border", 1)
        
        if not data:
            return f"<html><body><h1>{title}</h1><p>No data available</p></body></html>"
        
        html = []
        html.append("<html>")
        html.append("<head><title>{title}</title></head>")
        html.append("<body>")
        html.append(f"<h1>{title}</h1>")
        html.append(f"<table border='{border}'>")
        
        # Header row
        html.append("<tr>")
        for key in data[0].keys():
            html.append(f"<th>{key}</th>")
        html.append("</tr>")
        
        # Data rows
        for row in data:
            html.append("<tr>")
            for value in row.values():
                html.append(f"<td>{value}</td>")
            html.append("</tr>")
        
        html.append("</table>")
        html.append(f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
        html.append("</body>")
        html.append("</html>")
        
        return "\n".join(html)


class MarkdownFormatter(ReportFormatter):
    """Format report as Markdown."""
    
    def extension(self) -> str:
        return "md"
    
    def format(self, data: List[Dict], **options) -> str:
        """
        Format data as Markdown table.
        
        Options:
            title: Report title (default: "Report")
        """
        title = options.get("title", "Report")
        
        if not data:
            return f"# {title}\n\nNo data available"
        
        md = []
        md.append(f"# {title}\n")
        
        # Header row
        headers = list(data[0].keys())
        md.append("| " + " | ".join(headers) + " |")
        md.append("|" + "|".join([" --- " for _ in headers]) + "|")
        
        # Data rows
        for row in data:
            values = [str(row.get(key, "")) for key in headers]
            md.append("| " + " | ".join(values) + " |")
        
        md.append(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        
        return "\n".join(md)


class TextFormatter(ReportFormatter):
    """Format report as plain text."""
    
    def extension(self) -> str:
        return "txt"
    
    def format(self, data: List[Dict], **options) -> str:
        """
        Format data as plain text.
        
        Options:
            title: Report title (default: "Report")
        """
        title = options.get("title", "Report")
        
        if not data:
            return f"{title}\n{'=' * len(title)}\n\nNo data available"
        
        lines = []
        lines.append(title)
        lines.append("=" * len(title))
        lines.append("")
        
        # Determine column widths
        headers = list(data[0].keys())
        widths = {h: len(h) for h in headers}
        
        for row in data:
            for h in headers:
                widths[h] = max(widths[h], len(str(row.get(h, ""))))
        
        # Header row
        header_line = " | ".join(h.ljust(widths[h]) for h in headers)
        lines.append(header_line)
        lines.append("-" * len(header_line))
        
        # Data rows
        for row in data:
            row_line = " | ".join(str(row.get(h, "")).ljust(widths[h]) for h in headers)
            lines.append(row_line)
        
        lines.append("")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return "\n".join(lines)


class ReportGenerator:
    """
    Flexible report generator with multiple format support.
    
    Design Pattern: Factory Pattern - Creates appropriate formatter
    """
    
    def __init__(self):
        self.formatters: Dict[str, ReportFormatter] = {
            "csv": CSVFormatter(),
            "json": JSONFormatter(),
            "html": HTMLFormatter(),
            "md": MarkdownFormatter(),
            "txt": TextFormatter()
        }
    
    def register_formatter(self, name: str, formatter: ReportFormatter) -> 'ReportGenerator':
        """Register a new formatter."""
        self.formatters[name] = formatter
        return self
    
    def generate(
        self,
        data: List[Dict],
        format_type: str = "json",
        filename: Optional[str] = None,
        *,
        save_to_file: bool = False,
        **format_options
    ) -> str:
        """
        Generate report in specified format.
        
        Args:
            data: List of dictionaries to report
            format_type: Output format (csv, json, html, md, txt)
            filename: Output filename (if save_to_file=True)
            save_to_file: Whether to save to file
            **format_options: Format-specific options
            
        Returns:
            Formatted report string
        """
        if format_type not in self.formatters:
            raise ValueError(f"Unsupported format: {format_type}")
        
        formatter = self.formatters[format_type]
        report_content = formatter.format(data, **format_options)
        
        if save_to_file:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"report_{timestamp}.{formatter.extension()}"
            
            with open(filename, 'w') as f:
                f.write(report_content)
            print(f"  Report saved to: {filename}")
        
        return report_content
    
    def generate_multi_format(
        self,
        data: List[Dict],
        *formats,
        **options
    ) -> Dict[str, str]:
        """
        Generate report in multiple formats.
        
        Args:
            data: List of dictionaries to report
            *formats: Variable number of format types
            **options: Format options (applied to all)
            
        Returns:
            Dictionary mapping format to content
        """
        results = {}
        
        for fmt in formats:
            results[fmt] = self.generate(data, fmt, **options)
        
        return results


def create_sample_data() -> List[Dict]:
    """Create sample data for report demonstration."""
    return [
        {"id": 1, "name": "Alice Chen", "department": "Engineering", "salary": 85000, "active": True},
        {"id": 2, "name": "Bob Smith", "department": "Sales", "salary": 72000, "active": True},
        {"id": 3, "name": "Charlie Brown", "department": "Engineering", "salary": 92000, "active": False},
        {"id": 4, "name": "Diana Prince", "department": "Marketing", "salary": 68000, "active": True},
        {"id": 5, "name": "Eve Wilson", "department": "Sales", "salary": 78000, "active": True}
    ]


def demonstrate_report_generator():
    """
    Demonstrate the flexible report generator with all argument types.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: FLEXIBLE REPORT GENERATOR")
    print("=" * 60)
    
    data = create_sample_data()
    generator = ReportGenerator()
    
    print("\n1. GENERATING DIFFERENT FORMATS")
    print("-" * 40)
    
    # JSON format
    print("\n  JSON Report:")
    json_report = generator.generate(data, format_type="json", indent=2)
    print(f"    {json_report[:150]}...")
    
    # CSV format with custom delimiter
    print("\n  CSV Report (pipe-delimited):")
    csv_report = generator.generate(data, format_type="csv", delimiter="|")
    print(f"    {csv_report[:150]}...")
    
    # HTML format with custom title
    print("\n  HTML Report:")
    html_report = generator.generate(data, format_type="html", title="Employee Report", border=0)
    print(f"    {html_report[:150]}...")
    
    # Markdown format
    print("\n  Markdown Report:")
    md_report = generator.generate(data, format_type="md", title="Employee Directory")
    print(f"    {md_report[:150]}...")
    
    # Text format
    print("\n  Text Report:")
    txt_report = generator.generate(data, format_type="txt", title="Employee List")
    print(f"    {txt_report[:150]}...")
    
    # MULTI-FORMAT GENERATION (using *args)
    print("\n2. MULTI-FORMAT GENERATION (*args)")
    print("-" * 40)
    
    results = generator.generate_multi_format(data, "json", "csv", "txt", indent=2)
    for fmt, content in results.items():
        print(f"  {fmt.upper()}: {len(content)} characters")
    
    # SAVING TO FILE
    print("\n3. SAVING TO FILE (save_to_file=True)")
    print("-" * 40)
    
    generator.generate(data, format_type="json", save_to_file=True, filename="report.json")
    generator.generate(data, format_type="csv", save_to_file=True, filename="report.csv")
    generator.generate(data, format_type="html", save_to_file=True, filename="report.html", title="Employee Report")
    
    # CUSTOM FORMATTER REGISTRATION
    print("\n4. CUSTOM FORMATTER REGISTRATION")
    print("-" * 40)
    
    class YAMLFormatter(ReportFormatter):
        """Custom YAML formatter."""
        
        def extension(self) -> str:
            return "yaml"
        
        def format(self, data: List[Dict], **options) -> str:
            import yaml
            return yaml.dump(data, default_flow_style=False)
    
    generator.register_formatter("yaml", YAMLFormatter())
    yaml_report = generator.generate(data, format_type="yaml")
    print(f"  YAML Report length: {len(yaml_report)} characters")
    print(f"  {yaml_report[:200]}...")
    
    # DEMONSTRATING ALL ARGUMENT TYPES
    print("\n5. ARGUMENT TYPES SUMMARY")
    print("-" * 40)
    
    print("""
    def generate(
        self,
        data,                    # POSITIONAL (required)
        format_type="json",      # POSITIONAL with DEFAULT
        filename=None,           # POSITIONAL with DEFAULT
        *,                       # KEYWORD-ONLY separator
        save_to_file=False,      # KEYWORD-ONLY
        **format_options         # VARIABLE KEYWORD (**kwargs)
    ):
        pass
    """)
    
    print("  Examples:")
    print("    # Positional only")
    print("    generate(data)")
    print("    # Positional with format override")
    print("    generate(data, 'csv')")
    print("    # Keyword arguments (any order)")
    print("    generate(data, save_to_file=True, format_type='html')")
    print("    # Format-specific options via **kwargs")
    print("    generate(data, 'csv', delimiter='|', include_header=False)")


if __name__ == "__main__":
    demonstrate_report_generator()
```

---

## 🌐 Section 5: API Client with Flexible Arguments

A complete API client that demonstrates all argument types in a real-world scenario.

**SOLID Principles Applied:**
- Single Responsibility: Each function handles one aspect of API communication
- Dependency Inversion: High-level functions depend on abstractions

**Design Patterns:**
- Builder Pattern: Builds requests incrementally
- Adapter Pattern: Adapts Python calls to HTTP requests

```python
"""
API CLIENT WITH FLEXIBLE ARGUMENTS

This section builds a complete API client demonstrating all argument types.

SOLID Principles Applied:
- Single Responsibility: Each function handles one aspect
- Dependency Inversion: Depends on abstractions

Design Patterns:
- Builder Pattern: Builds requests incrementally
- Adapter Pattern: Adapts Python calls to HTTP
"""

from typing import Dict, Any, Optional, List, Union
from enum import Enum
from datetime import datetime
import json
import hashlib
import time
import random


class HTTPMethod(Enum):
    """HTTP methods."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class APIResponse:
    """API response wrapper."""
    
    def __init__(self, status_code: int, data: Any, headers: Dict = None):
        self.status_code = status_code
        self.data = data
        self.headers = headers or {}
        self.success = 200 <= status_code < 300
    
    def json(self) -> Any:
        """Return data as JSON."""
        return self.data
    
    def __str__(self) -> str:
        return f"APIResponse({self.status_code}, success={self.success})"


class APIClient:
    """
    Flexible API client with comprehensive argument support.
    
    Design Pattern: Builder Pattern - Build requests incrementally
    """
    
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        **default_headers
    ):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for all requests
            api_key: API key for authentication
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts
            **default_headers: Default headers to include in all requests
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            **default_headers
        }
        
        if api_key:
            self.default_headers["Authorization"] = f"Bearer {api_key}"
    
    def _build_url(self, endpoint: str, *path_parts, **query_params) -> str:
        """
        Build URL from endpoint, path parts, and query parameters.
        
        Args:
            endpoint: API endpoint
            *path_parts: Additional path segments
            **query_params: Query parameters
            
        Returns:
            Complete URL
        """
        # Combine endpoint with path parts
        parts = [endpoint.strip('/')]
        parts.extend(str(p).strip('/') for p in path_parts if p)
        url = f"{self.base_url}/{'/'.join(parts)}"
        
        # Add query parameters
        if query_params:
            # Remove None values
            params = {k: v for k, v in query_params.items() if v is not None}
            if params:
                query_string = "&".join(f"{k}={v}" for k, v in params.items())
                url = f"{url}?{query_string}"
        
        return url
    
    def _make_request(
        self,
        method: HTTPMethod,
        url: str,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **request_kwargs
    ) -> APIResponse:
        """
        Make HTTP request (simulated).
        
        In production, this would use the requests library.
        """
        # Merge headers
        final_headers = self.default_headers.copy()
        if headers:
            final_headers.update(headers)
        
        # Simulate request
        print(f"  → {method.value} {url}")
        if data:
            print(f"    Data: {json.dumps(data, indent=2)[:100]}...")
        
        # Simulate response (for demonstration)
        time.sleep(0.1)  # Simulate network delay
        
        # Generate mock response based on endpoint
        if "/users" in url:
            if method == HTTPMethod.GET:
                mock_data = {
                    "users": [
                        {"id": 1, "name": "Alice", "email": "alice@example.com"},
                        {"id": 2, "name": "Bob", "email": "bob@example.com"}
                    ],
                    "total": 2
                }
            elif method == HTTPMethod.POST:
                mock_data = {"id": random.randint(100, 999), **data}
            else:
                mock_data = {"success": True}
        elif "/user/" in url:
            user_id = url.split("/")[-1]
            if method == HTTPMethod.GET:
                mock_data = {"id": int(user_id), "name": f"User {user_id}", "email": f"user{user_id}@example.com"}
            elif method == HTTPMethod.DELETE:
                mock_data = {"deleted": True}
            else:
                mock_data = {"updated": True}
        else:
            mock_data = {"status": "ok", "message": "Request processed"}
        
        return APIResponse(200, mock_data, {"content-type": "application/json"})
    
    def request(
        self,
        method: Union[HTTPMethod, str],
        endpoint: str,
        *path_parts,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> APIResponse:
        """
        Make an API request with flexible arguments.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            endpoint: API endpoint
            *path_parts: Additional path segments
            data: Request body data
            headers: Additional headers
            **kwargs: Query parameters and other options
            
        Returns:
            APIResponse object
        """
        # Convert string method to enum
        if isinstance(method, str):
            method = HTTPMethod(method.upper())
        
        # Separate query params from other kwargs
        query_params = {}
        request_kwargs = {}
        
        for key, value in kwargs.items():
            if key in ["timeout", "verify", "auth"]:
                request_kwargs[key] = value
            else:
                query_params[key] = value
        
        # Build URL
        url = self._build_url(endpoint, *path_parts, **query_params)
        
        # Make request with retry logic
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                return self._make_request(method, url, data, headers, **request_kwargs)
            except Exception as e:
                last_error = e
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
        
        raise Exception(f"Request failed after {self.max_retries} attempts: {last_error}")
    
    # Convenience methods with different argument patterns
    
    def get(self, endpoint: str, *path_parts, **kwargs) -> APIResponse:
        """GET request."""
        return self.request("GET", endpoint, *path_parts, **kwargs)
    
    def post(self, endpoint: str, *path_parts, data: Optional[Dict] = None, **kwargs) -> APIResponse:
        """POST request."""
        return self.request("POST", endpoint, *path_parts, data=data, **kwargs)
    
    def put(self, endpoint: str, *path_parts, data: Optional[Dict] = None, **kwargs) -> APIResponse:
        """PUT request."""
        return self.request("PUT", endpoint, *path_parts, data=data, **kwargs)
    
    def delete(self, endpoint: str, *path_parts, **kwargs) -> APIResponse:
        """DELETE request."""
        return self.request("DELETE", endpoint, *path_parts, **kwargs)
    
    def patch(self, endpoint: str, *path_parts, data: Optional[Dict] = None, **kwargs) -> APIResponse:
        """PATCH request."""
        return self.request("PATCH", endpoint, *path_parts, data=data, **kwargs)


class UserAPI:
    """
    User management API wrapper.
    
    Demonstrates wrapping an API client with specific methods.
    """
    
    def __init__(self, client: APIClient):
        self.client = client
    
    def list_users(
        self,
        page: int = 1,
        limit: int = 20,
        sort_by: str = "id",
        sort_order: str = "asc",
        **filters
    ) -> APIResponse:
        """
        List users with pagination and filtering.
        
        Args:
            page: Page number
            limit: Items per page
            sort_by: Sort field
            sort_order: Sort order (asc/desc)
            **filters: Additional filters (name, email, etc.)
        """
        return self.client.get(
            "users",
            page=page,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            **filters
        )
    
    def get_user(self, user_id: int, include_details: bool = False) -> APIResponse:
        """
        Get user by ID.
        
        Args:
            user_id: User identifier
            include_details: Whether to include detailed information
        """
        return self.client.get("users", user_id, details=include_details)
    
    def create_user(
        self,
        name: str,
        email: str,
        role: str = "user",
        is_active: bool = True,
        **extra_fields
    ) -> APIResponse:
        """
        Create a new user.
        
        Args:
            name: User's full name
            email: User's email address
            role: User role (admin, user, guest)
            is_active: Whether user is active
            **extra_fields: Additional user fields
        """
        data = {
            "name": name,
            "email": email,
            "role": role,
            "is_active": is_active,
            **extra_fields
        }
        return self.client.post("users", data=data)
    
    def update_user(
        self,
        user_id: int,
        *,
        name: Optional[str] = None,
        email: Optional[str] = None,
        role: Optional[str] = None,
        is_active: Optional[bool] = None,
        **extra_fields
    ) -> APIResponse:
        """
        Update an existing user.
        
        Args:
            user_id: User identifier
            name: New name (optional)
            email: New email (optional)
            role: New role (optional)
            is_active: New active status (optional)
            **extra_fields: Additional fields to update
        """
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        if role is not None:
            data["role"] = role
        if is_active is not None:
            data["is_active"] = is_active
        data.update(extra_fields)
        
        return self.client.put("users", user_id, data=data)
    
    def delete_user(self, user_id: int, permanent: bool = False) -> APIResponse:
        """
        Delete a user.
        
        Args:
            user_id: User identifier
            permanent: Whether to permanently delete (vs soft delete)
        """
        return self.client.delete("users", user_id, permanent=permanent)


def demonstrate_api_client():
    """
    Demonstrate the API client with all argument types.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: API CLIENT WITH FLEXIBLE ARGUMENTS")
    print("=" * 60)
    
    # Create client with default headers
    client = APIClient(
        base_url="https://api.example.com/v1",
        api_key="test-api-key-123",
        timeout=30,
        X-Custom-Header="custom-value",
        X-App-Version="1.0.0"
    )
    
    print("\n1. BASIC GET REQUESTS")
    print("-" * 40)
    
    # GET with path parameters (positional)
    response = client.get("users")
    print(f"  GET /users: {response.status_code}")
    
    # GET with path parts (*args)
    response = client.get("users", 123)
    print(f"  GET /users/123: {response.status_code}")
    
    # GET with query parameters (**kwargs)
    response = client.get("users", page=2, limit=10, sort_by="name")
    print(f"  GET /users?page=2&limit=10&sort_by=name: {response.status_code}")
    
    print("\n2. POST REQUESTS WITH DATA")
    print("-" * 40)
    
    # POST with data
    response = client.post("users", data={"name": "Alice", "email": "alice@example.com"})
    print(f"  POST /users: {response.status_code}")
    
    print("\n3. USER API WRAPPER (keyword-only arguments)")
    print("-" * 40)
    
    user_api = UserAPI(client)
    
    # List users with filters
    response = user_api.list_users(page=1, limit=5, sort_by="name")
    print(f"  list_users(page=1, limit=5): {response.status_code}")
    
    # Get specific user
    response = user_api.get_user(123, include_details=True)
    print(f"  get_user(123, include_details=True): {response.status_code}")
    
    # Create user with extra fields
    response = user_api.create_user(
        name="Charlie Brown",
        email="charlie@example.com",
        role="admin",
        department="Engineering",
        manager_id=100
    )
    print(f"  create_user(name='Charlie', role='admin', department='Engineering'): {response.status_code}")
    
    # Update user (keyword-only after user_id)
    response = user_api.update_user(
        123,
        name="Charles Brown",
        role="super_admin",
        is_active=False
    )
    print(f"  update_user(123, name='Charles', role='super_admin'): {response.status_code}")
    
    # Delete user
    response = user_api.delete_user(123, permanent=True)
    print(f"  delete_user(123, permanent=True): {response.status_code}")
    
    print("\n4. ARGUMENT TYPES SUMMARY")
    print("-" * 40)
    
    print("""
    APIClient.__init__(
        base_url,              # POSITIONAL (required)
        api_key=None,          # POSITIONAL with DEFAULT
        timeout=30,            # POSITIONAL with DEFAULT
        max_retries=3,         # POSITIONAL with DEFAULT
        **default_headers      # VARIABLE KEYWORD
    )
    
    APIClient.request(
        method,                # POSITIONAL (required)
        endpoint,              # POSITIONAL (required)
        *path_parts,           # VARIABLE POSITIONAL (*args)
        data=None,             # KEYWORD-ONLY (after *)
        headers=None,          # KEYWORD-ONLY
        **kwargs               # VARIABLE KEYWORD (query params)
    )
    
    UserAPI.update_user(
        user_id,               # POSITIONAL (required)
        *,                     # KEYWORD-ONLY separator
        name=None,             # KEYWORD-ONLY
        email=None,            # KEYWORD-ONLY
        role=None,             # KEYWORD-ONLY
        is_active=None,        # KEYWORD-ONLY
        **extra_fields         # VARIABLE KEYWORD
    )
    """)


if __name__ == "__main__":
    demonstrate_api_client()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Positional Arguments** – Passed in defined order. Required unless default provided. Order matters.

- **Keyword Arguments** – Passed by name. Self-documenting. Can be in any order. Must come after positional arguments.

- **Default Arguments** – Provide fallback values. Evaluated at function definition. ⚠️ Mutable defaults (list, dict) are shared across calls—use None instead.

- ***args (Variable Positional)** – Collects extra positional args into tuple. Great for functions that need variable inputs.

- ****kwargs (Variable Keyword)** – Collects extra keyword args into dict. Great for configuration and forwarding.

- **Parameter Order** – Positional → Default → *args → Keyword-only → **kwargs

- **Keyword-Only Arguments** – Placed after `*` in parameter list. Cannot be passed positionally.

- **Positional-Only Arguments** – Placed before `/` in parameter list. Cannot be passed as keywords.

- **Report Generator** – Flexible reports with CSV, JSON, HTML, Markdown, Text. Demonstrates all argument types.

- **API Client** – Real-world API wrapper with comprehensive argument patterns.

- **SOLID Principles Applied** – Interface Segregation (clear parameter interfaces), Open/Closed (new formats can be added), Dependency Inversion (abstractions).

- **Design Patterns Used** – Strategy Pattern (report formatters), Factory Pattern (formatter creation), Builder Pattern (request building), Adapter Pattern (API adaptation).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Defining Functions – The Workhorses of Python

- **📚 Series B Catalog:** Functions & Modules Yard – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Return Values – Getting Results Back (Series B, Story 3)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 2 | 4 | 33% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **14** | **38** | **27%** |

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

**Next Story:** Series B, Story 3: The 2026 Python Metromap: Return Values – Getting Results Back

---

## 📝 Your Invitation

You've mastered function arguments. Now build something with what you've learned:

1. **Build a report generator** – Add PDF, Excel, and XML formatters. Use *args for multiple formats.

2. **Create a flexible API client** – Add authentication, rate limiting, and response caching. Use **kwargs for query parameters.

3. **Build a configuration system** – Use default arguments for settings. Allow overrides via **kwargs.

4. **Create a logging utility** – Use *args for multiple messages. Use **kwargs for structured logging.

5. **Build a data validator** – Use keyword-only arguments for validation rules. Use **kwargs for custom rules.

**You've mastered function arguments. Next stop: Return Values!**

---

*Found this helpful? Clap, comment, and share what you built with different argument types. Next stop: Return Values!* 🚇