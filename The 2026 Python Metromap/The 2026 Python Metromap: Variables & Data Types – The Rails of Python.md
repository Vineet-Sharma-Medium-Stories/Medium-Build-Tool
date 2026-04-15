# The 2026 Python Metromap: Variables & Data Types – The Rails of Python

## Series A: Foundations Station | Story 1 of 7

![The 2026 Python Metromap/images/Variables and Data Types – The Rails of Python](images/Variables and Data Types – The Rails of Python.png)

## 📖 Introduction

**Welcome to the first stop on the Foundations Station Line.**

You've completed the Map & Mindset series. You understand how to navigate the Metromap. You know how to avoid derailments. You're ready to drive.

Now it's time to lay the first rails.

Every Python program, from a simple script to a complex AI system, is built on the same foundation: variables and data types. Variables are the containers that hold information. Data types define what kind of information they hold—numbers, text, true/false values, and more. Without these, your code is just empty tracks.

This story—**The 2026 Python Metromap: Variables & Data Types – The Rails of Python**—is your hands-on introduction to Python's core building blocks. We'll explore integers for whole numbers, floats for decimals, strings for text, and booleans for true/false logic. We'll see how to store customer orders, track product prices, manage inventory quantities, and handle order status. We'll master type conversion, input/output operations, and the operators that transform data.

Most importantly, we'll build real things. By the end of this story, you'll have built an e-commerce order tracking system that calculates totals, applies discounts, and generates receipts. You'll understand not just what variables are, but why they matter.

**Let's lay the rails.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories)

- 🔧 **The 2026 Python Metromap: Variables & Data Types – The Rails of Python** – Integers, floats, strings, booleans; storing customer orders; type conversion; input/output operations. **⬅️ YOU ARE HERE**

- 🏗️ **The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets** – Shopping carts with lists; user profiles with dictionaries; analytics with sets; configuration with tuples. 🔜 *Up Next*

- 📦 **The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More** – Building a discount engine; age verification; loan approval calculator.

- 🚦 **The 2026 Python Metromap: Control Flow – if, elif, else** – Grade calculator; shipping cost estimator; customer support ticket routing.

- 🔁 **The 2026 Python Metromap: Loops – for, while, break, continue** – Batch file processor; API retry mechanism; pagination system.

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter.

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🧱 Section 1: Understanding Variables – The Containers of Data

A variable is a named container that stores a value. Think of it as a labeled box where you put information. You can create a variable, put data in it, change that data later, and retrieve it whenever you need it.

**SOLID Principle Applied: Single Responsibility** – Each variable has one clear purpose. A variable that stores a customer name shouldn't also store an order total. This makes code predictable and debuggable.

**Design Pattern: Repository Pattern** – Variables act as a simple repository for single values, providing a named reference to stored data.

```python
"""
VARIABLES: THE CONTAINERS OF DATA

This section demonstrates how variables work as named containers
that store and reference data in memory.

SOLID Principle: Single Responsibility
- Each variable serves one clear purpose
- Variables are named to reflect their single responsibility

Design Pattern: Repository Pattern (Simplified)
- Variables act as repositories for single values
- Provides named access to stored data
"""

def demonstrate_variable_basics():
    """
    Demonstrates fundamental variable operations.
    
    Variables are created with assignment operator (=)
    They can be reassigned to new values at any time
    Variable names should be descriptive and follow conventions
    """
    print("=" * 60)
    print("SECTION 1: VARIABLE BASICS")
    print("=" * 60)
    
    # VARIABLE CREATION
    # Variables are created when you first assign a value
    print("\n1. CREATING VARIABLES")
    print("-" * 40)
    
    # Each variable has a single, clear responsibility
    customer_name = "Alice Chen"          # Stores customer identity
    order_number = 10042                  # Stores order identifier
    product_price = 29.99                 # Stores monetary value
    is_premium_member = True              # Stores boolean status
    
    # The type() function reveals what kind of data a variable holds
    print(f"customer_name = '{customer_name}' → type: {type(customer_name).__name__}")
    print(f"order_number = {order_number} → type: {type(order_number).__name__}")
    print(f"product_price = {product_price} → type: {type(product_price).__name__}")
    print(f"is_premium_member = {is_premium_member} → type: {type(is_premium_member).__name__}")
    
    # VARIABLE NAMING CONVENTIONS
    print("\n2. VARIABLE NAMING CONVENTIONS")
    print("-" * 40)
    
    # Python uses snake_case for variable names (PEP 8)
    # Words separated by underscores, all lowercase
    first_name = "Bob"                    # ✓ Good: clear, descriptive
    last_name = "Smith"                   # ✓ Good: follows convention
    order_total_usd = 149.99              # ✓ Good: includes units when helpful
    
    # Bad naming examples (commented out - don't do this)
    # fn = "Bob"                          # ✗ Too short, unclear meaning
    # orderTotalUSD = 149.99              # ✗ camelCase, not Python convention
    # x = 149.99                          # ✗ No meaning, just a letter
    
    print(f"Good variable names: {first_name}, {last_name}, {order_total_usd}")
    
    # VARIABLE REASSIGNMENT
    print("\n3. VARIABLE REASSIGNMENT")
    print("-" * 40)
    
    # Variables can be changed after creation
    current_status = "pending"
    print(f"Initial status: {current_status}")
    
    # Reassigning to a new value
    current_status = "processing"
    print(f"After first update: {current_status}")
    
    current_status = "shipped"
    print(f"After second update: {current_status}")
    
    # Variables can change type when reassigned (but this is usually bad practice)
    flexible_variable = 42
    print(f"flexible_variable as int: {flexible_variable} ({type(flexible_variable).__name__})")
    
    flexible_variable = "now a string"
    print(f"flexible_variable as str: {flexible_variable} ({type(flexible_variable).__name__})")
    
    print("\n⚠️ Note: Changing variable types is possible but discouraged.")
    print("   It makes code harder to understand and debug.")
    
    # MULTIPLE ASSIGNMENT
    print("\n4. MULTIPLE ASSIGNMENT")
    print("-" * 40)
    
    # Assign multiple variables in one line
    x, y, z = 10, 20, 30
    print(f"x={x}, y={y}, z={z}")
    
    # Assign the same value to multiple variables
    a = b = c = 100
    print(f"a={a}, b={b}, c={c}")
    
    # Swapping variables (Python makes this elegant)
    first = "apple"
    second = "banana"
    print(f"Before swap: first={first}, second={second}")
    
    first, second = second, first  # Swap without temporary variable
    print(f"After swap: first={first}, second={second}")


def demonstrate_variable_scope():
    """
    Demonstrates variable scope - where variables are accessible.
    
    Scope determines which parts of code can see and use a variable.
    - Local scope: Inside a function, only accessible within that function
    - Global scope: Outside any function, accessible everywhere
    - Enclosing scope: In nested functions
    - Built-in scope: Python's built-in names
    
    SOLID Principle: Single Responsibility
    - Variables should have the smallest necessary scope
    - Global variables should be avoided or used sparingly
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: VARIABLE SCOPE")
    print("=" * 60)
    
    # GLOBAL VARIABLES
    # Defined outside any function, accessible everywhere
    # Use sparingly - they make code harder to reason about
    global_store_name = "Metromap Mart"  # Global scope
    print(f"\nGlobal variable: {global_store_name}")
    
    def show_local_scope():
        """Demonstrates local variables within a function."""
        # LOCAL VARIABLE
        # Only exists inside this function
        local_discount_rate = 0.10
        print(f"  Inside function - local_discount_rate: {local_discount_rate}")
        print(f"  Inside function - can read global: {global_store_name}")
        # Cannot modify global without 'global' keyword
    
    def try_modify_global():
        """Demonstrates modifying global variables."""
        # Without 'global' keyword, this creates a LOCAL variable
        global_store_name = "Local Store"  # This is local, not global!
        print(f"  Inside try_modify_global - local version: {global_store_name}")
    
    def actually_modify_global():
        """Demonstrates proper global variable modification."""
        global global_store_name  # Declare intent to modify global
        global_store_name = "Modified Global Store"
        print(f"  Inside actually_modify_global - modified global: {global_store_name}")
    
    show_local_scope()
    try_modify_global()
    print(f"After try_modify_global (global unchanged): {global_store_name}")
    
    actually_modify_global()
    print(f"After actually_modify_global (global changed): {global_store_name}")
    
    # ENCLOSING SCOPE (for nested functions)
    print("\n5. ENCLOSING SCOPE (NONLOCAL)")
    print("-" * 40)
    
    def outer_function():
        """Outer function with its own variable."""
        outer_variable = "I'm from outer"
        
        def inner_function():
            """Inner function that can access outer's variables."""
            nonlocal outer_variable  # Declare intent to modify enclosing variable
            outer_variable = "Modified by inner"
            print(f"  Inside inner_function: {outer_variable}")
        
        inner_function()
        print(f"Back in outer_function: {outer_variable}")
    
    outer_function()
    
    print("\n📚 SCOPE RULES SUMMARY (LEGB Rule):")
    print("   Local → Enclosing → Global → Built-in")
    print("   Python looks for variables in this order")


if __name__ == "__main__":
    demonstrate_variable_basics()
    demonstrate_variable_scope()
```

---

## 🔢 Section 2: Numeric Data Types – Integers and Floats

Numbers are everywhere in programming. Integers (int) are whole numbers. Floats (float) are decimal numbers. Understanding the difference is crucial for accurate calculations, especially with money.

**SOLID Principle Applied: Interface Segregation** – Different numeric types serve different purposes. Integers for counting (whole items). Floats for measurements (continuous values). The interface for each is optimized for its use case.

**Design Pattern: Value Object Pattern** – Numeric values are immutable; operations create new values rather than modifying existing ones.

```python
"""
NUMERIC DATA TYPES: INTEGERS AND FLOATS

This section covers whole numbers (integers) and decimal numbers (floats),
their operations, and important considerations like floating-point precision.

SOLID Principle: Interface Segregation
- Integers and floats have distinct interfaces for their purposes
- Integers excel at counting and indexing
- Floats handle continuous measurements and division

Design Pattern: Value Object Pattern
- Numeric values are immutable
- Operations return new values rather than modifying originals
"""

def demonstrate_integers():
    """
    Demonstrates integer (int) operations.
    
    Integers are whole numbers: -2, -1, 0, 1, 2, 3...
    They are used for counting, indexing, and discrete quantities.
    Integers have unlimited precision in Python.
    """
    print("=" * 60)
    print("SECTION 2A: INTEGER (int) DATA TYPE")
    print("=" * 60)
    
    # INTEGER CREATION
    print("\n1. CREATING INTEGERS")
    print("-" * 40)
    
    # Positive integers
    item_count = 5
    order_quantity = 3
    customer_id = 10042
    
    # Negative integers (for debts, temperature below zero, etc.)
    temperature_celsius = -5
    account_balance = -50
    
    # Zero is also an integer
    inventory_count = 0
    
    print(f"Positive integers: {item_count}, {order_quantity}, {customer_id}")
    print(f"Negative integers: {temperature_celsius}, {account_balance}")
    print(f"Zero: {inventory_count}")
    
    # INTEGER OPERATIONS
    print("\n2. INTEGER ARITHMETIC OPERATIONS")
    print("-" * 40)
    
    a = 17
    b = 4
    
    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b):          {a + b}")
    print(f"Subtraction (a - b):       {a - b}")
    print(f"Multiplication (a * b):    {a * b}")
    print(f"Division (a / b):          {a / b}   → Returns float!")
    print(f"Floor Division (a // b):   {a // b}  → Integer division, rounds down")
    print(f"Modulus (a % b):           {a % b}   → Remainder after division")
    print(f"Exponentiation (a ** b):   {a ** b}  → a raised to power b")
    
    # PRACTICAL USE CASE: Order Processing with Integers
    print("\n3. PRACTICAL USE CASE: ORDER QUANTITIES")
    print("-" * 40)
    
    def calculate_order_total(unit_price_cents: int, quantity: int) -> int:
        """
        Calculate order total in cents using integer arithmetic.
        
        Using cents avoids floating-point precision issues with money.
        
        Args:
            unit_price_cents: Price per unit in cents (integer)
            quantity: Number of units ordered (integer)
            
        Returns:
            Total price in cents (integer)
        """
        # All integer operations - no floating-point errors
        subtotal_cents = unit_price_cents * quantity
        return subtotal_cents
    
    # Example: Product costs $29.99 (2999 cents), quantity 3
    price_cents = 2999
    quantity = 3
    
    total_cents = calculate_order_total(price_cents, quantity)
    total_dollars = total_cents / 100
    
    print(f"Product price: ${price_cents / 100:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total in cents: {total_cents}¢")
    print(f"Total in dollars: ${total_dollars:.2f}")
    
    # INTEGER PROPERTIES
    print("\n4. INTEGER PROPERTIES AND METHODS")
    print("-" * 40)
    
    number = -42
    
    print(f"Original: {number}")
    print(f"Absolute value (abs()): {abs(number)}")
    print(f"Convert to string (str()): '{str(number)}'")
    print(f"Binary representation (bin()): {bin(number)}")
    print(f"Hexadecimal (hex()): {hex(number)}")


def demonstrate_floats():
    """
    Demonstrates floating-point (float) operations.
    
    Floats represent decimal numbers: 3.14, 2.718, 0.001
    Used for measurements, percentages, and continuous values.
    WARNING: Floats have precision limitations! Not all decimals can be represented exactly.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: FLOAT DATA TYPE")
    print("=" * 60)
    
    # FLOAT CREATION
    print("\n1. CREATING FLOATS")
    print("-" * 40)
    
    # Standard decimal notation
    price = 29.99
    tax_rate = 0.08
    discount_percentage = 0.15
    
    # Scientific notation (for very large or small numbers)
    avogadro = 6.022e23  # 6.022 × 10²³
    electron_mass = 9.109e-31  # 9.109 × 10⁻³¹
    
    print(f"Standard floats: price=${price}, tax_rate={tax_rate}")
    print(f"Scientific notation: Avogadro's number = {avogadro:.2e}")
    print(f"Scientific notation: Electron mass = {electron_mass:.2e}")
    
    # FLOAT OPERATIONS
    print("\n2. FLOAT ARITHMETIC OPERATIONS")
    print("-" * 40)
    
    a = 10.5
    b = 3.2
    
    print(f"a = {a}, b = {b}")
    print(f"Addition:           {a + b}")
    print(f"Subtraction:        {a - b}")
    print(f"Multiplication:     {a * b}")
    print(f"Division:           {a / b}")
    print(f"Floor Division:     {a // b}  → Note: result is float, not int")
    print(f"Modulus:            {a % b}")
    print(f"Exponentiation:     {a ** b}")
    
    # IMPORTANT: FLOATING-POINT PRECISION
    print("\n3. FLOATING-POINT PRECISION (CRITICAL!)")
    print("-" * 40)
    
    # This is not a bug - it's how floating-point math works
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"Is 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
    print("This happens because 0.1 and 0.2 cannot be represented exactly in binary.")
    
    # Solution: Use rounding or the decimal module for precise calculations
    print("\nSolutions for precision issues:")
    
    # Method 1: Round to acceptable decimal places
    rounded = round(0.1 + 0.2, 10)
    print(f"Method 1 - Rounding: round(0.1 + 0.2, 10) = {rounded}")
    
    # Method 2: Use integers (cents instead of dollars)
    cents = 10 + 20  # Represent 0.10 and 0.20 as 10 and 20 cents
    dollars = cents / 100
    print(f"Method 2 - Using integers: {cents}¢ = ${dollars}")
    
    # PRACTICAL USE CASE: Price Calculation with Floats
    print("\n4. PRACTICAL USE CASE: PRICE CALCULATION")
    print("-" * 40)
    
    def calculate_price_with_tax(price: float, tax_rate: float) -> float:
        """
        Calculate final price including tax.
        
        Args:
            price: Base price (float)
            tax_rate: Tax rate as decimal (float, e.g., 0.08 for 8%)
            
        Returns:
            Final price including tax (float)
        """
        # Note: For production financial systems, use Decimal or cents (integers)
        tax_amount = price * tax_rate
        final_price = price + tax_amount
        
        # Round to 2 decimal places for currency
        return round(final_price, 2)
    
    base_price = 29.99
    tax = 0.08
    
    final = calculate_price_with_tax(base_price, tax)
    print(f"Base price: ${base_price}")
    print(f"Tax rate: {tax * 100}%")
    print(f"Final price: ${final}")
    
    # FLOAT METHODS AND FUNCTIONS
    print("\n5. FLOAT METHODS AND UTILITIES")
    print("-" * 40)
    
    value = 3.14159265359
    
    print(f"Original: {value}")
    print(f"Round to 2 decimals: {round(value, 2)}")
    print(f"Round to integer: {round(value)}")
    print(f"Floor (math.floor): {int(value)}")  # Truncates toward zero
    print(f"Convert to string: '{str(value)}'")


def demonstrate_type_conversion():
    """
    Demonstrates converting between numeric types.
    
    Type conversion (casting) changes a value from one data type to another.
    This is essential when working with user input or combining different types.
    
    SOLID Principle: Liskov Substitution
    - Converted values should behave predictably in their new type
    - int to float is safe (widening)
    - float to int loses information (narrowing)
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: TYPE CONVERSION (CASTING)")
    print("=" * 60)
    
    # INT TO FLOAT (Widening - Safe, no data loss)
    print("\n1. INT TO FLOAT CONVERSION")
    print("-" * 40)
    
    integer_value = 42
    float_value = float(integer_value)
    print(f"int {integer_value} → float {float_value} (safe, no data loss)")
    
    # FLOAT TO INT (Narrowing - May lose data)
    print("\n2. FLOAT TO INT CONVERSION")
    print("-" * 40)
    
    float_values = [3.14, 3.99, 3.01, -2.7]
    
    for f in float_values:
        truncated = int(f)  # Truncates toward zero
        rounded = round(f)  # Rounds to nearest integer
        print(f"float {f} → int (truncate): {truncated}, int (round): {rounded}")
    
    # STRING TO NUMBER (For user input processing)
    print("\n3. STRING TO NUMBER CONVERSION")
    print("-" * 40)
    
    # User input comes as strings - must convert to numbers
    user_input_int = "42"
    user_input_float = "3.14"
    
    converted_int = int(user_input_int)
    converted_float = float(user_input_float)
    
    print(f"String '{user_input_int}' → int: {converted_int} (type: {type(converted_int).__name__})")
    print(f"String '{user_input_float}' → float: {converted_float} (type: {type(converted_float).__name__})")
    
    # NUMBER TO STRING (For display and concatenation)
    print("\n4. NUMBER TO STRING CONVERSION")
    print("-" * 40)
    
    number = 12345
    number_str = str(number)
    print(f"int {number} → str: '{number_str}'")
    
    # STRING TO NUMBER WITH ERROR HANDLING
    print("\n5. SAFE STRING TO NUMBER CONVERSION")
    print("-" * 40)
    
    def safe_int_convert(value: str, default: int = 0) -> int:
        """
        Safely convert string to integer with error handling.
        
        Args:
            value: String to convert
            default: Default value if conversion fails
            
        Returns:
            Converted integer or default value
        """
        try:
            return int(value)
        except ValueError:
            print(f"  Warning: Could not convert '{value}' to int. Using default {default}")
            return default
    
    test_values = ["42", "3.14", "not a number", "100"]
    
    for val in test_values:
        result = safe_int_convert(val)
        print(f"safe_int_convert('{val}') = {result}")


def demonstrate_enhanced_ecommerce_system():
    """
    Complete e-commerce order tracking system demonstrating all concepts.
    
    This system uses proper type handling, precision management,
    and demonstrates real-world application of numeric types.
    
    SOLID Principles Applied:
    - Single Responsibility: Each function has one job
    - Open/Closed: System can be extended with new discount types
    - Dependency Inversion: High-level modules depend on abstractions
    
    Design Patterns:
    - Value Object: MonetaryAmount encapsulates currency operations
    - Strategy: Different discount calculation strategies
    - Factory: Creates order objects with proper validation
    """
    from decimal import Decimal, ROUND_HALF_UP
    from typing import Dict, List, Optional, Tuple
    from dataclasses import dataclass
    from datetime import datetime
    
    print("\n" + "=" * 60)
    print("SECTION 2D: COMPLETE E-COMMERCE SYSTEM")
    print("=" * 60)
    
    # Use Decimal for financial calculations (no floating-point errors)
    # This is a Value Object pattern implementation
    @dataclass(frozen=True)
    class MonetaryAmount:
        """
        Value Object for monetary amounts.
        
        Immutable by design - operations return new instances.
        Uses Decimal for perfect precision with currency.
        
        SOLID: Single Responsibility - Only handles monetary value operations
        Design Pattern: Value Object - Immutable, equality by value
        """
        amount: Decimal
        
        def __post_init__(self):
            """Validate and normalize the amount."""
            # Ensure two decimal places for currency
            object.__setattr__(self, 'amount', self.amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        
        @classmethod
        def from_dollars(cls, dollars: float) -> 'MonetaryAmount':
            """Create MonetaryAmount from float dollars."""
            return cls(Decimal(str(dollars)))
        
        @classmethod
        def from_cents(cls, cents: int) -> 'MonetaryAmount':
            """Create MonetaryAmount from integer cents."""
            return cls(Decimal(cents) / Decimal(100))
        
        def add(self, other: 'MonetaryAmount') -> 'MonetaryAmount':
            """Add two monetary amounts."""
            return MonetaryAmount(self.amount + other.amount)
        
        def subtract(self, other: 'MonetaryAmount') -> 'MonetaryAmount':
            """Subtract another monetary amount."""
            return MonetaryAmount(self.amount - other.amount)
        
        def multiply(self, multiplier: int) -> 'MonetaryAmount':
            """Multiply by an integer quantity."""
            return MonetaryAmount(self.amount * Decimal(multiplier))
        
        def apply_percentage(self, percentage: Decimal) -> 'MonetaryAmount':
            """Apply a percentage (e.g., 0.08 for 8% tax)."""
            return MonetaryAmount(self.amount * percentage)
        
        def to_dollars(self) -> float:
            """Convert to float dollars (for display only)."""
            return float(self.amount)
        
        def to_cents(self) -> int:
            """Convert to integer cents."""
            return int(self.amount * Decimal(100))
        
        def __str__(self) -> str:
            return f"${self.amount:.2f}"
    
    # Product class using the Value Object pattern
    @dataclass
    class Product:
        """
        Represents a product in the catalog.
        
        SOLID: Single Responsibility - Manages product information only
        """
        sku: str
        name: str
        price: MonetaryAmount
        category: str
        taxable: bool = True
        
        def __str__(self) -> str:
            return f"{self.name} (SKU: {self.sku}) - {self.price}"
    
    # Discount strategy abstract base class
    from abc import ABC, abstractmethod
    
    class DiscountStrategy(ABC):
        """
        Abstract base class for discount strategies.
        
        SOLID: Open/Closed - New discount types can be added without modifying existing code
        SOLID: Liskov Substitution - All discount strategies can be used interchangeably
        Design Pattern: Strategy - Encapsulates different discount calculation algorithms
        """
        
        @abstractmethod
        def calculate(self, subtotal: MonetaryAmount) -> MonetaryAmount:
            """Calculate discount amount based on subtotal."""
            pass
        
        @abstractmethod
        def get_description(self) -> str:
            """Return human-readable discount description."""
            pass
    
    class PercentageDiscount(DiscountStrategy):
        """Discount as a percentage of the subtotal."""
        
        def __init__(self, percentage: Decimal, code: str, description: str):
            """
            Initialize percentage discount.
            
            Args:
                percentage: Discount percentage as Decimal (e.g., Decimal('0.10') for 10%)
                code: Discount code for application
                description: Human-readable description
            """
            self.percentage = percentage
            self.code = code
            self._description = description
        
        def calculate(self, subtotal: MonetaryAmount) -> MonetaryAmount:
            """Calculate percentage discount."""
            return subtotal.apply_percentage(self.percentage)
        
        def get_description(self) -> str:
            return f"{self._description} ({self.percentage * 100}% off)"
    
    class FixedAmountDiscount(DiscountStrategy):
        """Fixed amount discount off the subtotal."""
        
        def __init__(self, amount: MonetaryAmount, code: str, description: str):
            """
            Initialize fixed amount discount.
            
            Args:
                amount: Fixed discount amount
                code: Discount code for application
                description: Human-readable description
            """
            self.amount = amount
            self.code = code
            self._description = description
        
        def calculate(self, subtotal: MonetaryAmount) -> MonetaryAmount:
            """Calculate fixed discount, but not below zero."""
            if self.amount.amount > subtotal.amount:
                return subtotal  # Can't discount below zero
            return self.amount
        
        def get_description(self) -> str:
            return f"{self._description} (${self.amount.to_dollars():.2f} off)"
    
    class OrderItem:
        """Represents a single line item in an order."""
        
        def __init__(self, product: Product, quantity: int):
            self.product = product
            self.quantity = quantity
        
        def subtotal(self) -> MonetaryAmount:
            """Calculate line item subtotal."""
            return self.product.price.multiply(self.quantity)
        
        def __str__(self) -> str:
            return f"{self.quantity}x {self.product.name} @ {self.product.price} = {self.subtotal()}"
    
    class Order:
        """
        Represents a customer order.
        
        SOLID: Single Responsibility - Manages order lifecycle and calculations
        Design Pattern: Builder - Order can be built incrementally
        """
        
        def __init__(self, order_id: int, customer_name: str):
            self.order_id = order_id
            self.customer_name = customer_name
            self.items: List[OrderItem] = []
            self.discount: Optional[DiscountStrategy] = None
            self.tax_rate: Decimal = Decimal('0.08')  # 8% default
            self.created_at: datetime = datetime.now()
            self.status: str = "pending"
        
        def add_item(self, product: Product, quantity: int) -> 'Order':
            """
            Add a product to the order.
            
            Returns self for method chaining (Builder pattern).
            """
            if quantity <= 0:
                raise ValueError(f"Quantity must be positive, got {quantity}")
            
            self.items.append(OrderItem(product, quantity))
            return self
        
        def apply_discount(self, discount: DiscountStrategy) -> 'Order':
            """Apply a discount to the order."""
            self.discount = discount
            return self
        
        def set_tax_rate(self, rate: Decimal) -> 'Order':
            """Set the tax rate for this order."""
            self.tax_rate = rate
            return self
        
        def calculate_subtotal(self) -> MonetaryAmount:
            """Calculate subtotal of all items."""
            subtotal = MonetaryAmount(Decimal('0'))
            for item in self.items:
                subtotal = subtotal.add(item.subtotal())
            return subtotal
        
        def calculate_discount_amount(self) -> MonetaryAmount:
            """Calculate total discount amount."""
            if not self.discount:
                return MonetaryAmount(Decimal('0'))
            
            subtotal = self.calculate_subtotal()
            return self.discount.calculate(subtotal)
        
        def calculate_tax_amount(self) -> MonetaryAmount:
            """Calculate tax amount on discounted subtotal."""
            subtotal = self.calculate_subtotal()
            discount_amount = self.calculate_discount_amount()
            taxable_amount = subtotal.subtract(discount_amount)
            return taxable_amount.apply_percentage(self.tax_rate)
        
        def calculate_total(self) -> MonetaryAmount:
            """Calculate final total after discounts and tax."""
            subtotal = self.calculate_subtotal()
            discount_amount = self.calculate_discount_amount()
            tax_amount = self.calculate_tax_amount()
            
            after_discount = subtotal.subtract(discount_amount)
            final_total = after_discount.add(tax_amount)
            
            return final_total
        
        def generate_receipt(self) -> str:
            """Generate a formatted receipt string."""
            receipt_lines = []
            receipt_lines.append("=" * 60)
            receipt_lines.append(f"METROMAP MART - ORDER #{self.order_id}")
            receipt_lines.append("=" * 60)
            receipt_lines.append(f"Customer: {self.customer_name}")
            receipt_lines.append(f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            receipt_lines.append(f"Status: {self.status.upper()}")
            receipt_lines.append("-" * 60)
            receipt_lines.append("ITEMS:")
            
            for item in self.items:
                receipt_lines.append(f"  {item}")
            
            receipt_lines.append("-" * 60)
            
            subtotal = self.calculate_subtotal()
            receipt_lines.append(f"Subtotal: {subtotal}")
            
            if self.discount:
                discount_amount = self.calculate_discount_amount()
                receipt_lines.append(f"Discount ({self.discount.get_description()}): -{discount_amount}")
            
            tax_amount = self.calculate_tax_amount()
            receipt_lines.append(f"Tax ({self.tax_rate * 100}%): {tax_amount}")
            
            receipt_lines.append("-" * 60)
            receipt_lines.append(f"TOTAL: {self.calculate_total()}")
            receipt_lines.append("=" * 60)
            
            return "\n".join(receipt_lines)
        
        def process_payment(self, payment_amount: MonetaryAmount) -> Tuple[bool, str]:
            """
            Process payment for the order.
            
            Returns:
                Tuple of (success, message)
            """
            total = self.calculate_total()
            
            if payment_amount.amount < total.amount:
                shortfall = total.subtract(payment_amount)
                return False, f"Insufficient payment. Short by {shortfall}"
            
            change = payment_amount.subtract(total)
            self.status = "paid"
            
            return True, f"Payment successful. Change: {change}"
    
    # DEMONSTRATION
    print("\n📦 CREATING PRODUCT CATALOG")
    print("-" * 40)
    
    # Create products using MonetaryAmount
    laptop = Product(
        sku="TECH-001",
        name="UltraBook Pro",
        price=MonetaryAmount.from_dollars(1299.99),
        category="Electronics",
        taxable=True
    )
    
    mouse = Product(
        sku="TECH-002",
        name="Wireless Mouse",
        price=MonetaryAmount.from_dollars(29.99),
        category="Electronics",
        taxable=True
    )
    
    cable = Product(
        sku="TECH-003",
        name="USB-C Cable",
        price=MonetaryAmount.from_dollars(19.99),
        category="Accessories",
        taxable=True
    )
    
    notebook = Product(
        sku="OFF-001",
        name="Premium Notebook",
        price=MonetaryAmount.from_dollars(12.99),
        category="Office",
        taxable=False  # Some items may be tax-exempt
    )
    
    print(f"Added: {laptop}")
    print(f"Added: {mouse}")
    print(f"Added: {cable}")
    print(f"Added: {notebook}")
    
    # Create and build an order
    print("\n🛒 CREATING ORDER")
    print("-" * 40)
    
    order = Order(order_id=10042, customer_name="Alice Chen")
    order.add_item(laptop, 1)
    order.add_item(mouse, 2)
    order.add_item(notebook, 3)
    
    # Apply a discount
    discount = PercentageDiscount(
        percentage=Decimal('0.10'),
        code="SAVE10",
        description="10% off entire purchase"
    )
    order.apply_discount(discount)
    
    # Set tax rate (could vary by location)
    order.set_tax_rate(Decimal('0.0875'))  # 8.75% sales tax
    
    # Generate and print receipt
    print("\n🧾 ORDER RECEIPT")
    print(order.generate_receipt())
    
    # Process payment
    print("\n💳 PAYMENT PROCESSING")
    print("-" * 40)
    
    total = order.calculate_total()
    print(f"Total due: {total}")
    
    # Customer pays with $1600
    payment = MonetaryAmount.from_dollars(1600.00)
    success, message = order.process_payment(payment)
    print(f"Payment: {payment}")
    print(f"Result: {message}")
    
    # Display type information
    print("\n📊 TYPE SUMMARY")
    print("-" * 40)
    print(f"laptop.price type: {type(laptop.price).__name__}")
    print(f"laptop.price.amount type: {type(laptop.price.amount).__name__}")
    print(f"order.calculate_total() type: {type(order.calculate_total()).__name__}")


def demonstrate_numeric_best_practices():
    """
    Summarizes best practices for working with numeric types.
    
    This section provides guidelines for choosing the right numeric type
    and avoiding common pitfalls.
    """
    print("\n" + "=" * 60)
    print("SECTION 2E: NUMERIC BEST PRACTICES SUMMARY")
    print("=" * 60)
    
    best_practices = [
        ("Use integers for counting", 
         "Items in cart, quantity, page numbers, indices"),
        
        ("Use integers for currency when possible", 
         "Store as cents (2999 instead of 29.99) to avoid floating-point errors"),
        
        ("Use Decimal for financial calculations", 
         "When you must use decimal numbers with money, use Decimal from decimal module"),
        
        ("Use floats for scientific/measurement", 
         "Temperature, distance, weight - where small precision errors are acceptable"),
        
        ("Never compare floats for equality directly", 
         "Use math.isclose() or round() with tolerance"),
        
        ("Convert user input explicitly", 
         "Always use int() or float() on input() results"),
        
        ("Use type hints", 
         "def calculate(x: float, y: int) -> float: helps catch type errors"),
        
        ("Be aware of integer overflow", 
         "Python integers are arbitrary precision - no overflow, but watch memory")
    ]
    
    print("\n📚 NUMERIC BEST PRACTICES:")
    for practice, reason in best_practices:
        print(f"   ✓ {practice}")
        print(f"     → {reason}\n")


if __name__ == "__main__":
    demonstrate_integers()
    demonstrate_floats()
    demonstrate_type_conversion()
    demonstrate_enhanced_ecommerce_system()
    demonstrate_numeric_best_practices()
```

---

## 📝 Section 3: Strings – Working with Text

Strings are sequences of characters used to represent text. They're essential for customer names, product descriptions, addresses, and any human-readable information.

**SOLID Principle Applied: Interface Segregation** – Strings provide a rich interface of methods for text manipulation without exposing internal representation details.

**Design Pattern: Immutable Object Pattern** – Strings cannot be changed after creation; operations return new strings.

```python
"""
STRING DATA TYPE: WORKING WITH TEXT

This section covers string creation, manipulation, formatting,
and common operations for text processing.

SOLID Principle: Interface Segregation
- Strings provide focused methods for specific text operations
- Methods like .upper(), .lower(), .strip() each do one thing well

Design Pattern: Immutable Object Pattern
- Strings are immutable - operations return new strings
- Original strings remain unchanged, preventing side effects
"""

def demonstrate_string_basics():
    """
    Demonstrates fundamental string operations.
    
    Strings can be created with single quotes, double quotes,
    or triple quotes for multi-line text.
    """
    print("=" * 60)
    print("SECTION 3A: STRING BASICS")
    print("=" * 60)
    
    # STRING CREATION
    print("\n1. CREATING STRINGS")
    print("-" * 40)
    
    # Single quotes (most common)
    single_quoted = 'Hello, World!'
    
    # Double quotes (useful when string contains apostrophes)
    double_quoted = "It's a beautiful day"
    
    # Triple quotes (for multi-line strings)
    multi_line = """This string
spans multiple
lines"""
    
    # Empty string
    empty = ""
    
    print(f"Single quoted: {single_quoted}")
    print(f"Double quoted: {double_quoted}")
    print(f"Multi-line: {multi_line}")
    print(f"Empty string length: {len(empty)}")
    
    # STRING CONCATENATION
    print("\n2. STRING CONCATENATION")
    print("-" * 40)
    
    # Using + operator
    first_name = "Alice"
    last_name = "Chen"
    full_name = first_name + " " + last_name
    print(f"Concatenation with +: {full_name}")
    
    # Using join() method (more efficient for many strings)
    parts = ["Hello", "world", "from", "Python"]
    joined = " ".join(parts)
    print(f"Join with space: {joined}")
    
    # Using f-strings (Python 3.6+, recommended)
    age = 28
    introduction = f"My name is {full_name} and I am {age} years old."
    print(f"f-string: {introduction}")
    
    # STRING REPETITION
    print("\n3. STRING REPETITION")
    print("-" * 40)
    
    separator = "-" * 40
    print(f"Repetition: {separator}")
    
    # STRING INDEXING AND SLICING
    print("\n4. STRING INDEXING AND SLICING")
    print("-" * 40)
    
    text = "Python Programming"
    print(f"Original: '{text}'")
    print(f"First character (index 0): '{text[0]}'")
    print(f"Last character (index -1): '{text[-1]}'")
    print(f"First 6 characters: '{text[:6]}'")
    print(f"Characters 7-18: '{text[7:18]}'")
    print(f"Every other character: '{text[::2]}'")
    print(f"Reversed: '{text[::-1]}'")
    
    # STRING LENGTH
    print("\n5. STRING LENGTH")
    print("-" * 40)
    
    product_name = "Wireless Mouse"
    print(f"'{product_name}' has {len(product_name)} characters")


def demonstrate_string_methods():
    """
    Demonstrates common string methods for text manipulation.
    
    Strings have many built-in methods for common operations.
    Since strings are immutable, these methods always return new strings.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: STRING METHODS")
    print("=" * 60)
    
    # CASE CONVERSION
    print("\n1. CASE CONVERSION METHODS")
    print("-" * 40)
    
    text = "  Hello WORLD!  "
    print(f"Original: '{text}'")
    print(f".upper(): '{text.upper()}'")
    print(f".lower(): '{text.lower()}'")
    print(f".capitalize(): '{text.capitalize()}'")
    print(f".title(): '{text.title()}'")
    print(f".swapcase(): '{text.swapcase()}'")
    
    # WHITESPACE STRIPPING
    print("\n2. WHITESPACE STRIPPING")
    print("-" * 40)
    
    messy = "   extra spaces   \t\n"
    print(f"Original: '{messy}'")
    print(f".strip(): '{messy.strip()}'")  # Removes both ends
    print(f".lstrip(): '{messy.lstrip()}'")  # Removes left side
    print(f".rstrip(): '{messy.rstrip()}'")  # Removes right side
    
    # SEARCH AND REPLACE
    print("\n3. SEARCH AND REPLACE")
    print("-" * 40)
    
    sentence = "The quick brown fox jumps over the lazy dog"
    print(f"Original: '{sentence}'")
    print(f".find('fox'): {sentence.find('fox')}")  # Returns index or -1
    print(f".find('cat'): {sentence.find('cat')}")
    print(f".replace('fox', 'cat'): '{sentence.replace('fox', 'cat')}'")
    print(f".count('o'): {sentence.count('o')}")
    
    # BOOLEAN CHECKS
    print("\n4. BOOLEAN CHECK METHODS")
    print("-" * 40)
    
    test_strings = ["Python123", "python", "12345", "   ", "Hello!"]
    
    for s in test_strings:
        print(f"'{s}':")
        print(f"  isalpha(): {s.isalpha()}")  # Only letters?
        print(f"  isdigit(): {s.isdigit()}")  # Only digits?
        print(f"  isalnum(): {s.isalnum()}")  # Letters or digits?
        print(f"  isspace(): {s.isspace()}")  # Only whitespace?
        print(f"  islower(): {s.islower()}")  # All lowercase?
        print(f"  isupper(): {s.isupper()}")  # All uppercase?
    
    # SPLITTING AND JOINING
    print("\n5. SPLITTING AND JOINING")
    print("-" * 40)
    
    csv_data = "apple,banana,cherry,dates"
    print(f"CSV data: '{csv_data}'")
    
    # Split into list
    fruits = csv_data.split(",")
    print(f".split(','): {fruits}")
    
    # Split with max splits
    limited = csv_data.split(",", 2)
    print(f".split(',', 2): {limited}")
    
    # Split on whitespace
    words = "Python is awesome".split()
    print(f"Split on whitespace: {words}")
    
    # Join back together
    rejoined = " | ".join(fruits)
    print(f"Join with ' | ': '{rejoined}'")
    
    # START/END WITH
    print("\n6. START AND END CHECKS")
    print("-" * 40)
    
    filename = "document.pdf"
    print(f"Filename: '{filename}'")
    print(f".startswith('doc'): {filename.startswith('doc')}")
    print(f".startswith('file'): {filename.startswith('file')}")
    print(f".endswith('.pdf'): {filename.endswith('.pdf')}")
    print(f".endswith('.txt'): {filename.endswith('.txt')}")


def demonstrate_string_formatting():
    """
    Demonstrates different ways to format strings.
    
    String formatting inserts values into template strings.
    Modern Python offers multiple approaches, with f-strings being the preferred.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: STRING FORMATTING")
    print("=" * 60)
    
    # OLD STYLE (%) - Still works but not recommended for new code
    print("\n1. OLD STYLE (%) FORMATTING")
    print("-" * 40)
    
    name = "Alice"
    score = 95.5
    old_style = "Student %s scored %.1f%%" % (name, score)
    print(f"Old style: {old_style}")
    
    # FORMAT METHOD - More powerful but verbose
    print("\n2. .format() METHOD")
    print("-" * 40)
    
    # Positional arguments
    format1 = "{} scored {}".format(name, score)
    print(f"Positional: {format1}")
    
    # Named arguments
    format2 = "{name} scored {score:.1f}%".format(name=name, score=score)
    print(f"Named: {format2}")
    
    # F-STRINGS (Python 3.6+) - RECOMMENDED
    print("\n3. F-STRINGS (RECOMMENDED)")
    print("-" * 40)
    
    f_string = f"{name} scored {score:.1f}%"
    print(f"f-string: {f_string}")
    
    # F-string features
    print("\n4. F-STRING ADVANCED FEATURES")
    print("-" * 40)
    
    value = 1234.56789
    
    # Formatting numbers
    print(f"Decimal places: {value:.2f}")
    print(f"Thousands separator: {value:,.2f}")
    print(f"Percentage: {0.25:.1%}")
    print(f"Right-aligned (width 10): {name:>10}")
    print(f"Left-aligned (width 10): {name:<10}")
    print(f"Center-aligned (width 10): {name:^10}")
    
    # Expressions inside f-strings
    x, y = 10, 20
    print(f"Sum of {x} and {y} is {x + y}")
    print(f"Product: {x * y}")
    
    # Debugging with f-strings (Python 3.8+)
    print(f"{x=}, {y=}, {x + y=}")
    
    # MULTI-LINE F-STRINGS
    print("\n5. MULTI-LINE STRINGS")
    print("-" * 40)
    
    customer = {
        "name": "Bob Smith",
        "order_id": 10042,
        "total": 299.99
    }
    
    receipt = f"""
    ================ RECEIPT ================
    Customer: {customer['name']}
    Order ID: {customer['order_id']}
    Total: ${customer['total']:.2f}
    ==========================================
    """
    print(receipt)


def demonstrate_practical_string_use():
    """
    Demonstrates practical string processing in e-commerce context.
    
    This section shows how strings are used in real applications
    for data validation, formatting, and processing.
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: PRACTICAL STRING PROCESSING")
    print("=" * 60)
    
    # EMAIL VALIDATION
    print("\n1. EMAIL VALIDATION")
    print("-" * 40)
    
    def validate_email(email: str) -> tuple[bool, str]:
        """
        Validate email format.
        
        Args:
            email: Email address to validate
            
        Returns:
            Tuple of (is_valid, message)
        """
        if not email:
            return False, "Email cannot be empty"
        
        if "@" not in email:
            return False, "Email must contain @ symbol"
        
        local_part, domain = email.split("@", 1)
        
        if not local_part:
            return False, "Local part cannot be empty"
        
        if "." not in domain:
            return False, "Domain must contain a dot"
        
        if email.count("@") > 1:
            return False, "Email cannot have multiple @ symbols"
        
        return True, "Valid email"
    
    test_emails = [
        "alice@example.com",
        "bob@gmail",
        "invalid",
        "@missinglocal.com",
        "missingdomain@",
        "john.doe@company.co.uk"
    ]
    
    for email in test_emails:
        is_valid, message = validate_email(email)
        status = "✓" if is_valid else "✗"
        print(f"{status} {email:30} → {message}")
    
    # PHONE NUMBER FORMATTING
    print("\n2. PHONE NUMBER FORMATTING")
    print("-" * 40)
    
    def format_phone_number(phone: str) -> str:
        """
        Format phone number to standard display format.
        
        Removes non-digits and formats as (XXX) XXX-XXXX
        """
        # Remove all non-digit characters
        digits = ''.join(c for c in phone if c.isdigit())
        
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        elif len(digits) == 11 and digits[0] == '1':
            return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        else:
            return phone  # Return original if can't format
    
    test_phones = [
        "5551234567",
        "555-123-4567",
        "(555) 123-4567",
        "1-555-123-4567",
        "555.123.4567"
    ]
    
    for phone in test_phones:
        formatted = format_phone_number(phone)
        print(f"'{phone}' → '{formatted}'")
    
    # NAME PARSING
    print("\n3. NAME PARSING")
    print("-" * 40)
    
    def parse_full_name(full_name: str) -> dict:
        """
        Parse a full name into components.
        
        Handles various formats: "First Last", "Last, First", "First M. Last"
        """
        full_name = full_name.strip()
        
        # Check for "Last, First" format
        if "," in full_name:
            last, first = full_name.split(",", 1)
            return {
                "first_name": first.strip(),
                "last_name": last.strip(),
                "full_name": full_name
            }
        
        # Standard "First Last" format
        parts = full_name.split()
        
        if len(parts) == 1:
            return {
                "first_name": parts[0],
                "last_name": "",
                "full_name": full_name
            }
        elif len(parts) == 2:
            return {
                "first_name": parts[0],
                "last_name": parts[1],
                "full_name": full_name
            }
        else:
            # Middle name present
            return {
                "first_name": parts[0],
                "last_name": parts[-1],
                "middle_name": " ".join(parts[1:-1]),
                "full_name": full_name
            }
    
    test_names = [
        "Alice Chen",
        "Smith, Bob",
        "John A. Doe",
        "Marie",
        "Dr. Jane Smith"
    ]
    
    for name in test_names:
        parsed = parse_full_name(name)
        print(f"'{name}' → {parsed}")
    
    # ADDRESS STANDARDIZATION
    print("\n4. ADDRESS STANDARDIZATION")
    print("-" * 40)
    
    def standardize_address(address: str) -> dict:
        """
        Extract components from an address string.
        """
        address = address.strip().upper()
        
        # Common abbreviations
        abbreviations = {
            "STREET": "ST",
            "AVENUE": "AVE",
            "BOULEVARD": "BLVD",
            "ROAD": "RD",
            "DRIVE": "DR",
            "LANE": "LN",
            "COURT": "CT",
            "APARTMENT": "APT",
            "SUITE": "STE"
        }
        
        # Apply abbreviations
        for full, abbrev in abbreviations.items():
            address = address.replace(full, abbrev)
        
        return {
            "standardized": address,
            "has_zip": any(c.isdigit() for c in address[-10:]),
            "has_state": any(state in address for state in ["CA", "NY", "TX", "FL", "IL"])
        }
    
    addresses = [
        "123 Main Street",
        "456 Oak Avenue, Apt 4B",
        "789 Pine Boulevard",
        "321 Maple Drive"
    ]
    
    for addr in addresses:
        result = standardize_address(addr)
        print(f"'{addr}' → '{result['standardized']}'")
        print(f"  Has ZIP: {result['has_zip']}, Has State: {result['has_state']}")


def demonstrate_string_escape_sequences():
    """
    Demonstrates escape sequences in strings.
    
    Escape sequences allow including special characters in strings
    that would otherwise be interpreted differently.
    """
    print("\n" + "=" * 60)
    print("SECTION 3E: ESCAPE SEQUENCES")
    print("=" * 60)
    
    escape_sequences = [
        ("\\n", "Newline", "Line1\\nLine2"),
        ("\\t", "Tab", "Col1\\tCol2\\tCol3"),
        ("\\\\", "Backslash", "Path\\\\to\\\\file"),
        ("\\'", "Single quote", "It\\'s working"),
        ('\\"', "Double quote", 'She said \\"Hello\\"'),
        ("\\r", "Carriage return", "Overwrite\\rNew"),
    ]
    
    print("\nCommon escape sequences:")
    print("-" * 40)
    
    for seq, name, example in escape_sequences:
        # Show the escaped version
        escaped = eval(f"'{example}'")
        print(f"{seq:6} ({name:15}): {example} → {escaped}")
    
    # RAW STRINGS (ignore escape sequences)
    print("\n6. RAW STRINGS (r'...')")
    print("-" * 40)
    
    normal_path = "C:\\Users\\Name\\Documents"
    raw_path = r"C:\Users\Name\Documents"
    
    print(f"Normal string: {normal_path}")
    print(f"Raw string:    {raw_path}")
    print("Raw strings are great for file paths and regex patterns")


if __name__ == "__main__":
    demonstrate_string_basics()
    demonstrate_string_methods()
    demonstrate_string_formatting()
    demonstrate_practical_string_use()
    demonstrate_string_escape_sequences()
```

---

## 🎯 Section 4: Booleans – True/False Logic

Booleans represent truth values—either True or False. They're the foundation of decision-making in code.

**SOLID Principle Applied: Single Responsibility** – Boolean expressions evaluate exactly one condition or combination of conditions.

**Design Pattern: Flag Pattern** – Booleans act as flags controlling program flow.

```python
"""
BOOLEAN DATA TYPE: TRUE/FALSE LOGIC

This section covers boolean values, comparison operators,
and logical operators for building conditional logic.

SOLID Principle: Single Responsibility
- Each boolean expression evaluates one logical condition
- Complex logic is built from simple, focused conditions

Design Pattern: Flag Pattern
- Booleans serve as flags controlling program behavior
- Enable/disable features, track state, control flow
"""

def demonstrate_boolean_basics():
    """
    Demonstrates boolean values and comparison operators.
    
    Booleans have only two values: True and False.
    They are typically the result of comparison operations.
    """
    print("=" * 60)
    print("SECTION 4A: BOOLEAN BASICS")
    print("=" * 60)
    
    # BOOLEAN VALUES
    print("\n1. BOOLEAN VALUES")
    print("-" * 40)
    
    is_active = True
    is_deleted = False
    
    print(f"is_active = {is_active} (type: {type(is_active).__name__})")
    print(f"is_deleted = {is_deleted} (type: {type(is_deleted).__name__}")
    
    # COMPARISON OPERATORS
    print("\n2. COMPARISON OPERATORS")
    print("-" * 40)
    
    a = 10
    b = 20
    c = 10
    
    comparisons = [
        (f"{a} == {c}", a == c, "Equal to"),
        (f"{a} != {b}", a != b, "Not equal to"),
        (f"{a} < {b}", a < b, "Less than"),
        (f"{a} > {b}", a > b, "Greater than"),
        (f"{a} <= {c}", a <= c, "Less than or equal to"),
        (f"{b} >= {a}", b >= a, "Greater than or equal to"),
    ]
    
    for expr, result, name in comparisons:
        print(f"{expr:12} → {result:5} ({name})")
    
    # COMPARING STRINGS
    print("\n3. COMPARING STRINGS")
    print("-" * 40)
    
    print(f"'apple' == 'apple': {'apple' == 'apple'}")
    print(f"'apple' == 'Apple': {'apple' == 'Apple'} (case sensitive)")
    print(f"'apple' < 'banana': {'apple' < 'banana'} (lexicographical)")
    print(f"'Apple'.lower() == 'apple'.lower(): {'Apple'.lower() == 'apple'.lower()}")
    
    # COMPARING DIFFERENT TYPES
    print("\n4. COMPARING DIFFERENT TYPES")
    print("-" * 40)
    
    print(f"42 == '42': {42 == '42'} (different types, not equal)")
    print(f"42 == 42.0: {42 == 42.0} (int and float can be equal)")
    print(f"True == 1: {True == 1} (bool is subclass of int)")
    print(f"False == 0: {False == 0}")


def demonstrate_logical_operators():
    """
    Demonstrates logical operators for combining conditions.
    
    Logical operators (and, or, not) combine boolean expressions
    to create complex conditions.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: LOGICAL OPERATORS")
    print("=" * 60)
    
    # AND OPERATOR
    print("\n1. AND OPERATOR (both must be True)")
    print("-" * 40)
    
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"False and True: {False and True}")
    print(f"False and False: {False and False}")
    
    # OR OPERATOR
    print("\n2. OR OPERATOR (at least one must be True)")
    print("-" * 40)
    
    print(f"True or True: {True or True}")
    print(f"True or False: {True or False}")
    print(f"False or True: {False or True}")
    print(f"False or False: {False or False}")
    
    # NOT OPERATOR
    print("\n3. NOT OPERATOR (negation)")
    print("-" * 40)
    
    print(f"not True: {not True}")
    print(f"not False: {not False}")
    
    # PRACTICAL EXAMPLES
    print("\n4. PRACTICAL EXAMPLES")
    print("-" * 40)
    
    age = 25
    has_license = True
    has_insurance = False
    
    # Can drive if: has license AND (age >= 16) AND has insurance
    can_drive = has_license and age >= 16 and has_insurance
    print(f"Can drive: {can_drive}")
    
    # Can rent car if: age >= 21 OR (age >= 18 AND has_credit_card)
    age = 19
    has_credit_card = True
    can_rent = age >= 21 or (age >= 18 and has_credit_card)
    print(f"Age {age}, has credit card: {has_credit_card} → Can rent: {can_rent}")
    
    # SHORT-CIRCUIT EVALUATION
    print("\n5. SHORT-CIRCUIT EVALUATION")
    print("-" * 40)
    
    def expensive_check():
        print("  → Executing expensive_check()")
        return True
    
    # In AND, if first is False, second is NEVER evaluated
    print("False and expensive_check():")
    result = False and expensive_check()
    print(f"  Result: {result} (expensive_check never called)\n")
    
    # In OR, if first is True, second is NEVER evaluated
    print("True or expensive_check():")
    result = True or expensive_check()
    print(f"  Result: {result} (expensive_check never called)\n")
    
    # TRUTHY AND FALSY VALUES
    print("\n6. TRUTHY AND FALSY VALUES")
    print("-" * 40)
    
    # Values that evaluate to False in boolean context
    falsy_values = [
        False,           # Boolean False
        None,            # None type
        0,               # Integer zero
        0.0,             # Float zero
        "",              # Empty string
        [],              # Empty list
        {},              # Empty dictionary
        set(),           # Empty set
        tuple(),         # Empty tuple
    ]
    
    print("Falsy values (evaluate to False):")
    for val in falsy_values:
        print(f"  bool({repr(val)}) = {bool(val)}")
    
    # Most other values evaluate to True
    truthy_values = [
        True,            # Boolean True
        1,               # Non-zero integer
        3.14,            # Non-zero float
        "Hello",         # Non-empty string
        [1, 2, 3],       # Non-empty list
        {"key": "value"} # Non-empty dictionary
    ]
    
    print("\nTruthy values (evaluate to True):")
    for val in truthy_values:
        print(f"  bool({repr(val)}) = {bool(val)}")
    
    # Using truthiness for concise code
    print("\n7. USING TRUTHINESS FOR CONCISE CODE")
    print("-" * 40)
    
    name = "Alice"
    # Instead of: if name is not None and name != ""
    if name:
        print(f"Hello, {name}!")
    
    items = []
    # Instead of: if len(items) > 0
    if items:
        print(f"Found {len(items)} items")
    else:
        print("No items found")


def demonstrate_ecommerce_decision_logic():
    """
    Demonstrates boolean logic in e-commerce decision making.
    
    This section shows how booleans control business logic
    like discount eligibility, shipping calculations, and order approval.
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: E-COMMERCE DECISION LOGIC")
    print("=" * 60)
    
    class OrderEligibilityChecker:
        """
        Checks various eligibility conditions for orders.
        
        SOLID: Single Responsibility - Only handles eligibility checks
        Design Pattern: Specification Pattern - Encapsulates business rules
        """
        
        def __init__(self, order_total: float, customer_tier: str, 
                     items_in_cart: int, is_new_customer: bool,
                     has_coupon: bool, shipping_zip: str):
            """
            Initialize order data for eligibility checks.
            
            Args:
                order_total: Total order amount
                customer_tier: Customer loyalty tier (bronze, silver, gold, platinum)
                items_in_cart: Number of items in cart
                is_new_customer: Whether customer is new
                has_coupon: Whether customer has a coupon
                shipping_zip: Shipping ZIP code
            """
            self.order_total = order_total
            self.customer_tier = customer_tier
            self.items_in_cart = items_in_cart
            self.is_new_customer = is_new_customer
            self.has_coupon = has_coupon
            self.shipping_zip = shipping_zip
        
        def qualifies_for_free_shipping(self) -> bool:
            """
            Check if order qualifies for free shipping.
            
            Rules:
            - Order total > $50, OR
            - Customer is platinum tier, OR
            - Customer is gold tier AND order total > $25
            """
            high_value_order = self.order_total > 50
            platinum_tier = self.customer_tier == "platinum"
            gold_tier_with_minimum = self.customer_tier == "gold" and self.order_total > 25
            
            return high_value_order or platinum_tier or gold_tier_with_minimum
        
        def qualifies_for_discount(self) -> tuple[bool, str]:
            """
            Check if order qualifies for a discount.
            
            Returns:
                Tuple of (qualifies, reason)
            """
            # New customers get 10% off
            if self.is_new_customer:
                return True, "Welcome discount for new customers"
            
            # High volume orders get 5% off
            if self.items_in_cart >= 5:
                return True, "Bulk purchase discount"
            
            # High value orders get 8% off
            if self.order_total > 200:
                return True, "High value order discount"
            
            # Platinum customers always get 15% off
            if self.customer_tier == "platinum":
                return True, "Platinum tier benefit"
            
            # Coupon code present
            if self.has_coupon:
                return True, "Coupon code applied"
            
            return False, "No applicable discounts"
        
        def requires_signature(self) -> bool:
            """
            Check if order requires signature upon delivery.
            
            Rules:
            - Order total > $500, OR
            - Customer is new AND order total > $200
            """
            high_value = self.order_total > 500
            new_customer_high_value = self.is_new_customer and self.order_total > 200
            
            return high_value or new_customer_high_value
        
        def is_eligible_for_express_shipping(self) -> bool:
            """
            Check if express shipping is available.
            
            Rules:
            - Order before 2 PM, AND
            - Items in stock, AND
            - Not a remote ZIP code
            """
            # Simplified for demonstration
            is_before_cutoff = True  # Would check actual time
            items_in_stock = self.items_in_cart <= 10  # Simplified stock check
            is_remote_zip = self.shipping_zip.startswith("999")  # Remote ZIPs
            
            return is_before_cutoff and items_in_stock and not is_remote_zip
        
        def requires_manual_review(self) -> bool:
            """
            Check if order requires manual review for fraud prevention.
            
            Rules:
            - New customer AND order total > $500, OR
            - Multiple items of same expensive category, OR
            - Shipping to suspicious address
            """
            suspicious_new_customer = self.is_new_customer and self.order_total > 500
            suspicious_items = self.items_in_cart > 20  # Simplified
            suspicious_address = self.shipping_zip in ["00000", "12345"]  # Test ZIPs
            
            return suspicious_new_customer or suspicious_items or suspicious_address
    
    # Test the eligibility checker
    print("\n📋 ORDER ELIGIBILITY CHECKER")
    print("-" * 40)
    
    test_orders = [
        {"total": 45, "tier": "bronze", "items": 2, "new": False, "coupon": False, "zip": "90210"},
        {"total": 75, "tier": "bronze", "items": 3, "new": False, "coupon": False, "zip": "90210"},
        {"total": 30, "tier": "gold", "items": 1, "new": False, "coupon": False, "zip": "90210"},
        {"total": 600, "tier": "bronze", "items": 1, "new": True, "coupon": False, "zip": "90210"},
        {"total": 150, "tier": "platinum", "items": 2, "new": False, "coupon": True, "zip": "90210"},
    ]
    
    for i, order_data in enumerate(test_orders, 1):
        checker = OrderEligibilityChecker(
            order_total=order_data["total"],
            customer_tier=order_data["tier"],
            items_in_cart=order_data["items"],
            is_new_customer=order_data["new"],
            has_coupon=order_data["coupon"],
            shipping_zip=order_data["zip"]
        )
        
        print(f"\nOrder #{i}: ${order_data['total']}, {order_data['tier']} tier")
        print(f"  Free shipping: {checker.qualifies_for_free_shipping()}")
        
        discount_qualifies, discount_reason = checker.qualifies_for_discount()
        print(f"  Discount eligible: {discount_qualifies} ({discount_reason})")
        
        print(f"  Signature required: {checker.requires_signature()}")
        print(f"  Express available: {checker.is_eligible_for_express_shipping()}")
        print(f"  Manual review needed: {checker.requires_manual_review()}")


def demonstrate_boolean_patterns():
    """
    Demonstrates common boolean patterns and best practices.
    
    This section shows idiomatic ways to work with booleans
    and avoid common anti-patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 4D: BOOLEAN BEST PRACTICES")
    print("=" * 60)
    
    # ANTI-PATTERN 1: Redundant comparisons
    print("\n1. AVOID REDUNDANT COMPARISONS")
    print("-" * 40)
    
    is_active = True
    
    # Bad
    if is_active == True:
        print("Bad: if is_active == True")
    
    # Good
    if is_active:
        print("Good: if is_active")
    
    # Bad
    if is_active == False:
        print("This won't print")
    
    # Good
    if not is_active:
        print("Good: if not is_active")
    
    # ANTI-PATTERN 2: Using if-else for boolean assignment
    print("\n2. USE DIRECT BOOLEAN ASSIGNMENT")
    print("-" * 40)
    
    age = 18
    
    # Bad
    if age >= 18:
        can_vote = True
    else:
        can_vote = False
    print(f"Bad: can_vote = {can_vote}")
    
    # Good
    can_vote = age >= 18
    print(f"Good: can_vote = {can_vote}")
    
    # ANTI-PATTERN 3: Complex nested conditions
    print("\n3. FLATTEN NESTED CONDITIONS")
    print("-" * 40)
    
    def bad_nested_check(user):
        """Hard to read and maintain."""
        if user.get("is_authenticated"):
            if user.get("has_permission"):
                if user.get("is_active"):
                    if user.get("account_balance", 0) > 0:
                        return True
        return False
    
    def good_flat_check(user):
        """Clear, readable, each condition on its own line."""
        conditions = [
            user.get("is_authenticated"),
            user.get("has_permission"),
            user.get("is_active"),
            user.get("account_balance", 0) > 0
        ]
        return all(conditions)
    
    test_user = {
        "is_authenticated": True,
        "has_permission": True,
        "is_active": True,
        "account_balance": 100
    }
    
    print(f"Flat check result: {good_flat_check(test_user)}")
    
    # PATTERN: Guard clauses
    print("\n4. USE GUARD CLAUSES FOR EARLY RETURNS")
    print("-" * 40)
    
    def process_order(order_total, user_tier, has_coupon):
        """
        Process order with guard clauses.
        
        Guard clauses check invalid conditions first and return early.
        This reduces nesting and makes the happy path clear.
        """
        # Guard clauses (check failure conditions first)
        if order_total <= 0:
            return False, "Invalid order total"
        
        if user_tier not in ["bronze", "silver", "gold", "platinum"]:
            return False, "Invalid user tier"
        
        # Happy path (all checks passed)
        discount = 0
        if user_tier == "platinum":
            discount = 0.15
        elif has_coupon:
            discount = 0.10
        
        final_total = order_total * (1 - discount)
        return True, f"Order processed: ${final_total:.2f}"
    
    success, message = process_order(100, "gold", True)
    print(f"Result: {message}")
    
    # PATTERN: Boolean flags for state management
    print("\n5. BOOLEAN FLAGS FOR STATE MANAGEMENT")
    print("-" * 40)
    
    class OrderState:
        """
        Manages order state using boolean flags.
        
        Design Pattern: Flag Pattern - Each flag represents one aspect of state
        """
        
        def __init__(self):
            self.is_created = False
            self.is_paid = False
            self.is_shipped = False
            self.is_delivered = False
            self.is_cancelled = False
        
        def can_cancel(self) -> bool:
            """Order can be cancelled if not shipped or delivered."""
            return not self.is_shipped and not self.is_delivered
        
        def can_modify(self) -> bool:
            """Order can be modified if not paid, shipped, delivered, or cancelled."""
            return not any([self.is_paid, self.is_shipped, self.is_delivered, self.is_cancelled])
        
        def status(self) -> str:
            """Get human-readable order status."""
            if self.is_cancelled:
                return "Cancelled"
            if self.is_delivered:
                return "Delivered"
            if self.is_shipped:
                return "Shipped"
            if self.is_paid:
                return "Paid"
            if self.is_created:
                return "Created"
            return "Draft"
    
    order = OrderState()
    order.is_created = True
    order.is_paid = True
    
    print(f"Order status: {order.status()}")
    print(f"Can cancel: {order.can_cancel()}")
    print(f"Can modify: {order.can_modify()}")


if __name__ == "__main__":
    demonstrate_boolean_basics()
    demonstrate_logical_operators()
    demonstrate_ecommerce_decision_logic()
    demonstrate_boolean_patterns()
```

---

## 📊 Section 5: Input and Output – Talking to Users

Input and output operations allow programs to communicate with users—receiving data and displaying results.

**SOLID Principle Applied: Dependency Inversion** – High-level logic depends on input/output abstractions, not specific I/O mechanisms.

**Design Pattern: Adapter Pattern** – Input/output functions adapt between user interaction and program logic.

```python
"""
INPUT AND OUTPUT: TALKING TO USERS

This section covers getting user input and displaying output,
including formatting, validation, and error handling.

SOLID Principle: Dependency Inversion
- Business logic depends on I/O abstractions
- Easy to swap console I/O for GUI or web I/O

Design Pattern: Adapter Pattern
- Input functions adapt raw user input to typed values
- Output functions adapt data to user-readable format
"""

def demonstrate_basic_io():
    """
    Demonstrates basic input and output operations.
    
    print() displays output to the console.
    input() reads user input as a string.
    """
    print("=" * 60)
    print("SECTION 5A: BASIC INPUT/OUTPUT")
    print("=" * 60)
    
    # BASIC PRINT
    print("\n1. PRINT FUNCTION")
    print("-" * 40)
    
    # Single value
    print("Hello, World!")
    
    # Multiple values (automatically adds spaces)
    print("Hello", "World", "from", "Python")
    
    # Custom separator
    print("apple", "banana", "cherry", sep=", ")
    
    # Custom end (default is newline)
    print("Loading", end="...")
    print("Done!")
    
    # BASIC INPUT
    print("\n2. INPUT FUNCTION")
    print("-" * 40)
    
    # Simple input
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # INPUT ALWAYS RETURNS STRING
    print("\n3. INPUT RETURNS STRINGS")
    print("-" * 40)
    
    age_input = input("Enter your age: ")
    print(f"Type of input: {type(age_input).__name__}")
    print(f"Value: '{age_input}'")
    
    # Convert to integer
    age = int(age_input)
    print(f"As integer: {age}")
    
    # MULTI-LINE OUTPUT
    print("\n4. MULTI-LINE OUTPUT")
    print("-" * 40)
    
    # Using triple quotes
    banner = """
    ========================================
              WELCOME TO METROMAP
    ========================================
    """
    print(banner)
    
    # Using \n
    print("Line 1\nLine 2\nLine 3")


def demonstrate_input_validation():
    """
    Demonstrates validating and processing user input.
    
    User input is unpredictable. Always validate and handle errors.
    """
    print("\n" + "=" * 60)
    print("SECTION 5B: INPUT VALIDATION")
    print("=" * 60)
    
    # SIMPLE VALIDATION
    print("\n1. SIMPLE VALIDATION")
    print("-" * 40)
    
    def get_positive_integer(prompt: str) -> int:
        """
        Get a positive integer from user with validation.
        
        Keeps asking until valid input is provided.
        """
        while True:
            user_input = input(prompt)
            
            # Check if empty
            if not user_input.strip():
                print("  Input cannot be empty. Please try again.")
                continue
            
            # Check if numeric
            if not user_input.isdigit():
                print("  Please enter a positive number.")
                continue
            
            value = int(user_input)
            
            # Check if positive
            if value <= 0:
                print("  Please enter a number greater than 0.")
                continue
            
            return value
    
    # Demonstrate (commented out to not block demo)
    # quantity = get_positive_integer("Enter quantity: ")
    # print(f"Quantity set to: {quantity}")
    
    print("(Demonstration of get_positive_integer function - would run interactively)")
    
    # COMPLETE ORDER INPUT SYSTEM
    print("\n2. COMPLETE ORDER INPUT SYSTEM")
    print("-" * 40)
    
    class OrderInputHandler:
        """
        Handles user input for order creation with validation.
        
        SOLID: Single Responsibility - Only handles input collection and validation
        """
        
        @staticmethod
        def get_string(prompt: str, required: bool = True, min_length: int = 1) -> str:
            """Get validated string input."""
            while True:
                value = input(prompt).strip()
                
                if required and not value:
                    print("  This field is required.")
                    continue
                
                if value and len(value) < min_length:
                    print(f"  Must be at least {min_length} characters.")
                    continue
                
                return value
        
        @staticmethod
        def get_integer(prompt: str, min_value: int = None, max_value: int = None) -> int:
            """Get validated integer input."""
            while True:
                value_str = input(prompt).strip()
                
                if not value_str:
                    print("  Please enter a number.")
                    continue
                
                try:
                    value = int(value_str)
                except ValueError:
                    print("  Please enter a valid integer.")
                    continue
                
                if min_value is not None and value < min_value:
                    print(f"  Value must be at least {min_value}.")
                    continue
                
                if max_value is not None and value > max_value:
                    print(f"  Value must be at most {max_value}.")
                    continue
                
                return value
        
        @staticmethod
        def get_float(prompt: str, min_value: float = None, max_value: float = None) -> float:
            """Get validated float input."""
            while True:
                value_str = input(prompt).strip()
                
                if not value_str:
                    print("  Please enter a number.")
                    continue
                
                try:
                    value = float(value_str)
                except ValueError:
                    print("  Please enter a valid number.")
                    continue
                
                if min_value is not None and value < min_value:
                    print(f"  Value must be at least {min_value}.")
                    continue
                
                if max_value is not None and value > max_value:
                    print(f"  Value must be at most {max_value}.")
                    continue
                
                return value
        
        @staticmethod
        def get_yes_no(prompt: str, default: bool = None) -> bool:
            """Get yes/no confirmation."""
            prompt_display = f"{prompt} (y/n)"
            if default is True:
                prompt_display += " [Y/n]"
            elif default is False:
                prompt_display += " [y/N]"
            prompt_display += ": "
            
            while True:
                value = input(prompt_display).strip().lower()
                
                if not value and default is not None:
                    return default
                
                if value in ['y', 'yes']:
                    return True
                if value in ['n', 'no']:
                    return False
                
                print("  Please enter 'y' or 'n'.")
        
        def collect_order(self) -> dict:
            """
            Collect complete order information from user.
            
            Returns:
                Dictionary with validated order data
            """
            print("\n" + "=" * 40)
            print("ORDER ENTRY SYSTEM")
            print("=" * 40)
            
            # Customer information
            customer_name = self.get_string("Customer name: ", required=True, min_length=2)
            email = self.get_string("Email: ", required=True)
            
            # Product information
            product_name = self.get_string("Product name: ", required=True)
            quantity = self.get_integer("Quantity: ", min_value=1, max_value=100)
            price = self.get_float("Unit price: $", min_value=0.01)
            
            # Shipping information
            use_same_address = self.get_yes_no("Use same address for shipping?")
            
            if use_same_address:
                shipping_address = "Same as billing"
            else:
                shipping_address = self.get_string("Shipping address: ", required=True)
            
            # Gift options
            is_gift = self.get_yes_no("Is this a gift?")
            gift_message = ""
            if is_gift:
                gift_message = self.get_string("Gift message: ", required=False, min_length=0)
            
            # Calculate totals
            subtotal = quantity * price
            tax = subtotal * 0.08  # 8% tax
            total = subtotal + tax
            
            return {
                "customer_name": customer_name,
                "email": email,
                "product_name": product_name,
                "quantity": quantity,
                "price": price,
                "subtotal": subtotal,
                "tax": tax,
                "total": total,
                "shipping_address": shipping_address,
                "is_gift": is_gift,
                "gift_message": gift_message
            }
    
    # Demonstrate the order input system
    print("\n(OrderInputHandler class defined - ready for interactive use)")
    print("Example usage:")
    print("  handler = OrderInputHandler()")
    print("  order = handler.collect_order()")
    print("  print(order)")


def demonstrate_formatted_output():
    """
    Demonstrates formatted output for reports and receipts.
    
    Proper formatting makes output readable and professional.
    """
    print("\n" + "=" * 60)
    print("SECTION 5C: FORMATTED OUTPUT")
    print("=" * 60)
    
    # COLUMN ALIGNMENT
    print("\n1. COLUMN ALIGNMENT")
    print("-" * 40)
    
    products = [
        ("Laptop", 1299.99, 1),
        ("Mouse", 29.99, 2),
        ("Keyboard", 89.99, 1),
        ("Monitor", 349.99, 1),
    ]
    
    # Header
    print(f"{'Product':<20} {'Price':>10} {'Qty':>5} {'Total':>10}")
    print("-" * 50)
    
    # Rows
    grand_total = 0
    for name, price, qty in products:
        total = price * qty
        grand_total += total
        print(f"{name:<20} ${price:>9.2f} {qty:>5} ${total:>9.2f}")
    
    print("-" * 50)
    print(f"{'GRAND TOTAL':<20} {'':>10} {'':>5} ${grand_total:>9.2f}")
    
    # RECEIPT GENERATION
    print("\n2. RECEIPT GENERATION")
    print("-" * 40)
    
    def generate_receipt(order: dict) -> str:
        """
        Generate a formatted receipt from order data.
        """
        receipt_lines = []
        receipt_lines.append("=" * 50)
        receipt_lines.append(f"{'METROMAP MART':^50}")
        receipt_lines.append("=" * 50)
        receipt_lines.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        receipt_lines.append(f"Customer: {order.get('customer_name', 'N/A')}")
        receipt_lines.append("-" * 50)
        receipt_lines.append(f"{order.get('product_name', 'N/A')} x {order.get('quantity', 0)}")
        receipt_lines.append(f"  @ ${order.get('price', 0):.2f} each")
        receipt_lines.append("-" * 50)
        receipt_lines.append(f"{'Subtotal:':<20} ${order.get('subtotal', 0):>9.2f}")
        receipt_lines.append(f"{'Tax (8%):':<20} ${order.get('tax', 0):>9.2f}")
        receipt_lines.append(f"{'Total:':<20} ${order.get('total', 0):>9.2f}")
        receipt_lines.append("=" * 50)
        
        if order.get('is_gift'):
            receipt_lines.append("GIFT RECEIPT")
            if order.get('gift_message'):
                receipt_lines.append(f"Message: {order['gift_message']}")
            receipt_lines.append("=" * 50)
        
        receipt_lines.append("Thank you for shopping at Metromap Mart!")
        
        return "\n".join(receipt_lines)
    
    # Sample order
    sample_order = {
        "customer_name": "Alice Chen",
        "product_name": "UltraBook Pro",
        "quantity": 1,
        "price": 1299.99,
        "subtotal": 1299.99,
        "tax": 104.00,
        "total": 1403.99,
        "is_gift": False,
        "gift_message": ""
    }
    
    receipt = generate_receipt(sample_order)
    print(receipt)
    
    # PROGRESS INDICATORS
    print("\n3. PROGRESS INDICATORS")
    print("-" * 40)
    
    import time
    
    def show_progress(iterations: int, delay: float = 0.1):
        """
        Display a simple progress indicator.
        """
        print("Processing:", end=" ")
        
        for i in range(iterations):
            # Different progress indicators
            if i % 10 == 0:
                print(f"{i}%", end=" ", flush=True)
            else:
                print(".", end="", flush=True)
            
            time.sleep(delay)
        
        print(" Done!")
    
    print("Progress example:")
    # show_progress(50, 0.02)  # Uncomment to see animation
    print("(Progress animation would display here)")


def build_complete_checkout_system():
    """
    Complete checkout system integrating all I/O concepts.
    
    This is a working interactive checkout system that demonstrates
    input validation, output formatting, and business logic.
    """
    from datetime import datetime
    import time
    
    print("\n" + "=" * 60)
    print("SECTION 5D: COMPLETE CHECKOUT SYSTEM")
    print("=" * 60)
    
    class CheckoutSystem:
        """
        Complete interactive checkout system.
        
        SOLID Principles:
        - Single Responsibility: Each method handles one aspect of checkout
        - Dependency Inversion: Business logic depends on I/O abstractions
        
        Design Patterns:
        - Template Method: Checkout flow defined in process() method
        - Builder: Builds order incrementally from user input
        """
        
        def __init__(self):
            self.order = {}
            self.steps = [
                ("customer_info", self.get_customer_info),
                ("shipping_info", self.get_shipping_info),
                ("payment_info", self.get_payment_info),
                ("review_order", self.review_order),
                ("confirm_order", self.confirm_order)
            ]
        
        def display_header(self, title: str):
            """Display a formatted section header."""
            print("\n" + "=" * 50)
            print(f" {title:^48} ")
            print("=" * 50)
        
        def get_customer_info(self) -> dict:
            """Collect customer information."""
            self.display_header("CUSTOMER INFORMATION")
            
            name = input("Full name: ").strip()
            while not name:
                print("  Name is required.")
                name = input("Full name: ").strip()
            
            email = input("Email: ").strip()
            while "@" not in email or not email:
                print("  Please enter a valid email address.")
                email = input("Email: ").strip()
            
            phone = input("Phone number: ").strip()
            
            return {
                "name": name,
                "email": email,
                "phone": phone
            }
        
        def get_shipping_info(self) -> dict:
            """Collect shipping information."""
            self.display_header("SHIPPING INFORMATION")
            
            address = input("Street address: ").strip()
            while not address:
                print("  Address is required.")
                address = input("Street address: ").strip()
            
            city = input("City: ").strip()
            while not city:
                print("  City is required.")
                city = input("City: ").strip()
            
            state = input("State (2 letters): ").strip().upper()
            while len(state) != 2 or not state.isalpha():
                print("  Please enter a 2-letter state code.")
                state = input("State (2 letters): ").strip().upper()
            
            zip_code = input("ZIP code: ").strip()
            while not zip_code.isdigit() or len(zip_code) not in [5, 9]:
                print("  Please enter a valid ZIP code (5 or 9 digits).")
                zip_code = input("ZIP code: ").strip()
            
            # Shipping method
            print("\nShipping methods:")
            print("  1. Standard (5-7 business days) - $5.99")
            print("  2. Express (2-3 business days) - $12.99")
            print("  3. Overnight (1 business day) - $24.99")
            
            method_choice = input("Select shipping method (1-3): ").strip()
            while method_choice not in ["1", "2", "3"]:
                print("  Please select 1, 2, or 3.")
                method_choice = input("Select shipping method (1-3): ").strip()
            
            shipping_methods = {
                "1": {"name": "Standard", "days": "5-7", "cost": 5.99},
                "2": {"name": "Express", "days": "2-3", "cost": 12.99},
                "3": {"name": "Overnight", "days": "1", "cost": 24.99}
            }
            
            method = shipping_methods[method_choice]
            
            return {
                "address": address,
                "city": city,
                "state": state,
                "zip": zip_code,
                "shipping_method": method["name"],
                "shipping_days": method["days"],
                "shipping_cost": method["cost"]
            }
        
        def get_payment_info(self) -> dict:
            """Collect payment information."""
            self.display_header("PAYMENT INFORMATION")
            
            print("Payment methods:")
            print("  1. Credit Card")
            print("  2. PayPal")
            print("  3. Gift Card")
            
            method_choice = input("Select payment method (1-3): ").strip()
            while method_choice not in ["1", "2", "3"]:
                print("  Please select 1, 2, or 3.")
                method_choice = input("Select payment method (1-3): ").strip()
            
            payment_methods = {"1": "Credit Card", "2": "PayPal", "3": "Gift Card"}
            payment_method = payment_methods[method_choice]
            
            payment_info = {"method": payment_method}
            
            if payment_method == "Credit Card":
                card_number = input("Card number (last 4 digits only for demo): ").strip()
                payment_info["card_last4"] = card_number[-4:] if card_number else "****"
            
            return payment_info
        
        def review_order(self, collected_data: dict) -> bool:
            """Display order summary and get confirmation."""
            self.display_header("ORDER REVIEW")
            
            # Customer info
            print("\n📋 CUSTOMER INFORMATION:")
            print(f"   Name: {collected_data['customer_info']['name']}")
            print(f"   Email: {collected_data['customer_info']['email']}")
            print(f"   Phone: {collected_data['customer_info']['phone'] or 'Not provided'}")
            
            # Shipping info
            print("\n🚚 SHIPPING INFORMATION:")
            print(f"   Address: {collected_data['shipping_info']['address']}")
            print(f"   {collected_data['shipping_info']['city']}, {collected_data['shipping_info']['state']} {collected_data['shipping_info']['zip']}")
            print(f"   Method: {collected_data['shipping_info']['shipping_method']} ({collected_data['shipping_info']['shipping_days']} days)")
            print(f"   Cost: ${collected_data['shipping_info']['shipping_cost']:.2f}")
            
            # Payment info
            print("\n💳 PAYMENT INFORMATION:")
            print(f"   Method: {collected_data['payment_info']['method']}")
            if collected_data['payment_info'].get('card_last4'):
                print(f"   Card ending in: {collected_data['payment_info']['card_last4']}")
            
            # Order summary (simplified for demo)
            subtotal = 299.99
            shipping = collected_data['shipping_info']['shipping_cost']
            tax = subtotal * 0.08
            total = subtotal + shipping + tax
            
            print("\n💰 ORDER SUMMARY:")
            print(f"   Subtotal: ${subtotal:.2f}")
            print(f"   Shipping: ${shipping:.2f}")
            print(f"   Tax (8%): ${tax:.2f}")
            print(f"   TOTAL: ${total:.2f}")
            
            print("\n" + "-" * 50)
            confirm = input("Is this information correct? (y/n): ").strip().lower()
            
            return confirm in ['y', 'yes']
        
        def confirm_order(self, collected_data: dict) -> dict:
            """Process and confirm the order."""
            self.display_header("PROCESSING ORDER")
            
            # Simulate processing
            print("Processing payment", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print(" Done!")
            
            time.sleep(0.5)
            print("Generating receipt", end="")
            for _ in range(2):
                time.sleep(0.3)
                print(".", end="", flush=True)
            print(" Done!")
            
            # Generate order number
            order_number = f"MP-{datetime.now().strftime('%Y%m%d')}-{hash(str(collected_data)) % 10000:04d}"
            
            # Calculate totals
            subtotal = 299.99
            shipping = collected_data['shipping_info']['shipping_cost']
            tax = subtotal * 0.08
            total = subtotal + shipping + tax
            
            result = {
                "order_number": order_number,
                "customer": collected_data['customer_info']['name'],
                "shipping_address": f"{collected_data['shipping_info']['address']}, {collected_data['shipping_info']['city']}, {collected_data['shipping_info']['state']} {collected_data['shipping_info']['zip']}",
                "shipping_method": collected_data['shipping_info']['shipping_method'],
                "payment_method": collected_data['payment_info']['method'],
                "subtotal": subtotal,
                "shipping_cost": shipping,
                "tax": tax,
                "total": total,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return result
        
        def display_confirmation(self, result: dict):
            """Display order confirmation."""
            self.display_header("ORDER CONFIRMATION")
            
            print(f"\n✅ ORDER CONFIRMED!")
            print(f"\n📦 Order Number: {result['order_number']}")
            print(f"👤 Customer: {result['customer']}")
            print(f"🚚 Shipping: {result['shipping_method']}")
            print(f"💰 Total: ${result['total']:.2f}")
            print(f"\n📧 A confirmation email has been sent to your email address.")
            print(f"\nThank you for shopping at Metromap Mart!")
        
        def process(self) -> dict:
            """
            Run the complete checkout process.
            
            Returns:
                Order confirmation dictionary
            """
            collected_data = {}
            
            for step_name, step_func in self.steps:
                if step_name == "review_order":
                    # Special handling for review step
                    if not step_func(collected_data):
                        print("\n❌ Order cancelled. Please start over.")
                        return None
                elif step_name == "confirm_order":
                    result = step_func(collected_data)
                else:
                    # Collect data for this step
                    collected_data[step_name] = step_func()
            
            self.display_confirmation(result)
            return result
    
    # Run the checkout system
    print("\n🚀 STARTING CHECKOUT SYSTEM")
    print("-" * 40)
    print("This is an interactive demo. Follow the prompts to complete a checkout.")
    print("(Press Ctrl+C to skip the interactive demo)\n")
    
    try:
        checkout = CheckoutSystem()
        result = checkout.process()
        
        if result:
            print("\n" + "=" * 50)
            print(" INTERACTIVE DEMO COMPLETE ".center(50, "="))
            print("=" * 50)
    except KeyboardInterrupt:
        print("\n\nDemo skipped. The CheckoutSystem class is available for use.")


if __name__ == "__main__":
    from datetime import datetime
    
    demonstrate_basic_io()
    demonstrate_input_validation()
    demonstrate_formatted_output()
    build_complete_checkout_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Variables** – Named containers that store data. Follow naming conventions. Understand scope (local vs global).

- **Integers (int)** – Whole numbers for counting. Use for quantities, IDs, indices. Perfect for currency when stored as cents.

- **Floats (float)** – Decimal numbers for measurements. Be aware of precision limitations. Use Decimal for financial calculations.

- **Strings (str)** – Text data for names, addresses, descriptions. Immutable with rich method library. Use f-strings for formatting.

- **Booleans (bool)** – True/False values for decisions. Combine with logical operators (and, or, not). Use truthiness for concise code.

- **Type Conversion** – Convert between types with int(), float(), str(). Always validate user input before conversion.

- **Input/Output** – print() for output, input() for user input. Always validate and handle errors in user input.

- **SOLID Principles Applied** – Single Responsibility (each variable/function has one job), Interface Segregation (type-specific methods), Dependency Inversion (I/O abstractions).

- **Design Patterns Used** – Value Object (MonetaryAmount), Strategy (Discount strategies), Builder (Order building), Flag Pattern (Boolean state), Adapter Pattern (I/O functions).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: From Passenger to Driver

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 1 | 6 | 14% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **6** | **46** | **12%** |

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap: Reading the Map
4. Series 0, Story 4: The 2026 Python Metromap: Avoiding Derailments
5. Series 0, Story 5: The 2026 Python Metromap: From Passenger to Driver
6. Series A, Story 1: The 2026 Python Metromap: Variables & Data Types – The Rails of Python

**Next Story:** Series A, Story 2: The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets

---

## 📝 Your Invitation

You've laid the first rails. Now build something with what you've learned:

1. **Build a shopping cart** – Create variables for products, quantities, and prices. Calculate subtotals and totals.

2. **Create a user profile system** – Use strings for names and emails. Use booleans for subscription status.

3. **Build a discount calculator** – Use floats for percentages. Use comparison operators to check eligibility.

4. **Create an interactive order form** – Use input() to collect customer information. Validate all inputs.

5. **Generate formatted receipts** – Use f-strings and alignment to create professional-looking output.

**You've mastered variables and data types. Next stop: Collections!**

---

*Found this helpful? Clap, comment, and share what you built with variables and data types. Next stop: Collections!* 🚇