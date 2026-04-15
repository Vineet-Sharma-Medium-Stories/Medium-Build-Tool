# The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More

## Series A: Foundations Station | Story 3 of 7

![The 2026 Python Metromap/images/Operators – Arithmetic, Comparison, Logical, and More](images/Operators – Arithmetic, Comparison, Logical, and More.png)

## 📖 Introduction

**Welcome to the third stop on the Foundations Station Line.**

You've mastered variables and data types. You can store numbers, text, and collections. You can build shopping carts, user profiles, and analytics systems. But storing data is only half the story. The real power comes from transforming that data—calculating totals, comparing values, making decisions, and combining conditions.

Operators are the tools that transform data. Arithmetic operators calculate totals and discounts. Comparison operators check if a price is within budget. Logical operators combine multiple conditions. Assignment operators update values efficiently. Membership operators check if an item exists in a collection.

This story—**The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More**—is your guide to every operator in Python. We'll build a complete discount engine that calculates prices with multiple discount tiers. We'll create an age verification system for a restricted website. We'll build a loan approval calculator that evaluates multiple criteria. And we'll implement a shopping cart with complex pricing rules.

**Let's transform some data.**

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

- 📦 **The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More** – Building a discount engine; age verification; loan approval calculator. **⬅️ YOU ARE HERE**

- 🚦 **The 2026 Python Metromap: Control Flow – if, elif, else** – Grade calculator; shipping cost estimator; customer support ticket routing. 🔜 *Up Next*

- 🔁 **The 2026 Python Metromap: Loops – for, while, break, continue** – Batch file processor; API retry mechanism; pagination system.

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter.

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## ➕ Section 1: Arithmetic Operators – Doing the Math

Arithmetic operators perform mathematical calculations on numbers. They're essential for calculating totals, discounts, taxes, and any numerical transformation.

**SOLID Principle Applied: Single Responsibility** – Each arithmetic operator performs exactly one mathematical operation.

**Design Pattern: Interpreter Pattern** – Arithmetic operators form a mini-language for mathematical expressions.

```python
"""
ARITHMETIC OPERATORS: DOING THE MATH

This section covers all arithmetic operators in Python:
+, -, *, /, //, %, **

SOLID Principle: Single Responsibility
- Each operator performs one mathematical operation

Design Pattern: Interpreter Pattern
- Operators form a mini-language for expressions
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import Union, List, Dict, Any
import math


def demonstrate_basic_arithmetic():
    """
    Demonstrates fundamental arithmetic operations.
    
    Covers addition, subtraction, multiplication, division,
    floor division, modulus, and exponentiation.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC ARITHMETIC OPERATORS")
    print("=" * 60)
    
    # ADDITION (+)
    print("\n1. ADDITION (+)")
    print("-" * 40)
    
    a, b = 15, 27
    print(f"{a} + {b} = {a + b}")
    
    # String concatenation (addition for strings)
    first = "Hello"
    second = "World"
    print(f"'{first}' + ' ' + '{second}' = '{first + ' ' + second}'")
    
    # List concatenation
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"{list1} + {list2} = {list1 + list2}")
    
    # SUBTRACTION (-)
    print("\n2. SUBTRACTION (-)")
    print("-" * 40)
    
    a, b = 100, 37
    print(f"{a} - {b} = {a - b}")
    print(f"{b} - {a} = {b - a} (negative result)")
    
    # MULTIPLICATION (*)
    print("\n3. MULTIPLICATION (*)")
    print("-" * 40)
    
    a, b = 12, 8
    print(f"{a} * {b} = {a * b}")
    
    # String repetition
    star = "*"
    print(f"'{star}' * 10 = '{star * 10}'")
    
    # List repetition
    items = [1, 2]
    print(f"{items} * 3 = {items * 3}")
    
    # DIVISION (/) - Always returns float
    print("\n4. DIVISION (/)")
    print("-" * 40)
    
    a, b = 15, 4
    print(f"{a} / {b} = {a / b} (float result)")
    print(f"10 / 3 = {10 / 3}")
    print(f"10 / 2 = {10 / 2} (still float: {10 / 2} is 5.0, not 5)")
    
    # FLOOR DIVISION (//) - Integer division, rounds down
    print("\n5. FLOOR DIVISION (//)")
    print("-" * 40)
    
    a, b = 15, 4
    print(f"{a} // {b} = {a // b} (integer result, floors down)")
    print(f"10 // 3 = {10 // 3}")
    print(f"10 // 2 = {10 // 2}")
    
    # Negative numbers with floor division (rounds DOWN, not toward zero)
    print(f"-10 // 3 = {-10 // 3} (rounds down to -4, not -3)")
    
    # MODULUS (%) - Remainder after division
    print("\n6. MODULUS (%) - Remainder")
    print("-" * 40)
    
    a, b = 17, 5
    print(f"{a} % {b} = {a % b} (remainder when {a} divided by {b})")
    
    # Check if number is even or odd
    numbers = [1, 2, 3, 4, 5, 6]
    for n in numbers:
        is_even = n % 2 == 0
        print(f"{n} is {'even' if is_even else 'odd'} (remainder: {n % 2})")
    
    # Check if number is divisible
    print(f"Is 15 divisible by 3? {15 % 3 == 0}")
    print(f"Is 16 divisible by 3? {16 % 3 == 0}")
    
    # EXPONENTIATION (**) - Power
    print("\n7. EXPONENTIATION (**) - Power")
    print("-" * 40)
    
    base, exponent = 2, 3
    print(f"{base} ** {exponent} = {base ** exponent} (2³ = 8)")
    print(f"10 ** 2 = {10 ** 2} (10² = 100)")
    print(f"2 ** 10 = {2 ** 10} (2¹⁰ = 1024)")
    print(f"9 ** 0.5 = {9 ** 0.5} (square root = 3.0)")
    
    # OPERATOR PRECEDENCE (PEMDAS)
    print("\n8. OPERATOR PRECEDENCE (PEMDAS)")
    print("-" * 40)
    
    print("Python follows standard mathematical precedence:")
    print("  Parentheses → Exponents → Multiplication/Division → Addition/Subtraction")
    
    expression1 = 2 + 3 * 4
    expression2 = (2 + 3) * 4
    print(f"2 + 3 * 4 = {expression1} (multiplication first)")
    print(f"(2 + 3) * 4 = {expression2} (parentheses override)")
    
    expression3 = 2 ** 3 * 2
    expression4 = 2 ** (3 * 2)
    print(f"2 ** 3 * 2 = {expression3} (exponent then multiplication)")
    print(f"2 ** (3 * 2) = {expression4} (parentheses change order)")


def demonstrate_arithmetic_with_different_types():
    """
    Demonstrates arithmetic with integers, floats, and decimals.
    
    Shows type conversion rules and precision considerations.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ARITHMETIC WITH DIFFERENT TYPES")
    print("=" * 60)
    
    # INT AND FLOAT MIXING
    print("\n1. INTEGERS AND FLOATS")
    print("-" * 40)
    
    int_val = 10
    float_val = 3.5
    
    print(f"int {int_val} + float {float_val} = {int_val + float_val} (result is float)")
    print(f"int {int_val} * float {float_val} = {int_val * float_val} (result is float)")
    print(f"type(int + float): {type(int_val + float_val).__name__}")
    
    # PRECISION ISSUES WITH FLOATS
    print("\n2. FLOATING POINT PRECISION (Important!)")
    print("-" * 40)
    
    print("Floats have precision limitations due to binary representation:")
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"Is 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
    
    # Solutions for precision
    print("\nSolutions for financial calculations:")
    
    # Method 1: Use integers (cents)
    cents = 10 + 20
    dollars = cents / 100
    print(f"Method 1 (cents): 10¢ + 20¢ = {cents}¢ = ${dollars:.2f}")
    
    # Method 2: Use Decimal module
    from decimal import Decimal
    d1 = Decimal('0.1')
    d2 = Decimal('0.2')
    d3 = d1 + d2
    print(f"Method 2 (Decimal): {d1} + {d2} = {d3} == 0.3? {d3 == Decimal('0.3')}")
    
    # Method 3: Use rounding
    rounded = round(0.1 + 0.2, 10)
    print(f"Method 3 (rounding): round(0.1 + 0.2, 10) = {rounded}")
    
    # PRACTICAL USE: PRICE CALCULATION
    print("\n3. PRACTICAL: PRICE CALCULATION")
    print("-" * 40)
    
    def calculate_price(price: float, quantity: int, tax_rate: float, discount_percent: float) -> Dict[str, float]:
        """
        Calculate final price with tax and discount.
        
        Args:
            price: Unit price
            quantity: Number of items
            tax_rate: Tax rate (e.g., 0.08 for 8%)
            discount_percent: Discount percentage (e.g., 10 for 10%)
            
        Returns:
            Dictionary with calculation breakdown
        """
        subtotal = price * quantity
        discount_amount = subtotal * (discount_percent / 100)
        after_discount = subtotal - discount_amount
        tax_amount = after_discount * tax_rate
        total = after_discount + tax_amount
        
        return {
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "after_discount": round(after_discount, 2),
            "tax_amount": round(tax_amount, 2),
            "total": round(total, 2)
        }
    
    result = calculate_price(price=29.99, quantity=3, tax_rate=0.08, discount_percent=10)
    print(f"Price: $29.99 × 3 = ${result['subtotal']:.2f}")
    print(f"10% discount: -${result['discount_amount']:.2f}")
    print(f"After discount: ${result['after_discount']:.2f}")
    print(f"Tax (8%): ${result['tax_amount']:.2f}")
    print(f"TOTAL: ${result['total']:.2f}")


def demonstrate_special_arithmetic_operations():
    """
    Demonstrates advanced arithmetic operations.
    
    Includes divmod, pow, abs, and mathematical functions.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: SPECIAL ARITHMETIC OPERATIONS")
    print("=" * 60)
    
    # DIVMOD - Returns both quotient and remainder
    print("\n1. divmod() - Quotient and Remainder")
    print("-" * 40)
    
    a, b = 17, 5
    quotient, remainder = divmod(a, b)
    print(f"divmod({a}, {b}) = ({quotient}, {remainder})")
    print(f"Check: {quotient} × {b} + {remainder} = {quotient * b + remainder} (should equal {a})")
    
    # Practical use: Converting seconds to minutes and seconds
    total_seconds = 125
    minutes, seconds = divmod(total_seconds, 60)
    print(f"{total_seconds} seconds = {minutes} minutes and {seconds} seconds")
    
    # POW with modulus (for cryptography)
    print("\n2. pow() with Three Arguments")
    print("-" * 40)
    
    base, exponent, modulus = 2, 10, 1000
    result = pow(base, exponent, modulus)
    print(f"pow({base}, {exponent}, {modulus}) = {result}")
    print(f"This is equivalent to ({base}^{exponent}) % {modulus} = {result}")
    
    # ABSOLUTE VALUE
    print("\n3. abs() - Absolute Value")
    print("-" * 40)
    
    negatives = [-10, -3.14, -1000]
    for n in negatives:
        print(f"abs({n}) = {abs(n)}")
    
    # Distance between points
    def distance(x1, y1, x2, y2) -> float:
        """Calculate Euclidean distance between two points."""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    dist = distance(0, 0, 3, 4)
    print(f"Distance between (0,0) and (3,4): {dist}")
    
    # ROUNDING
    print("\n4. round() - Rounding Numbers")
    print("-" * 40)
    
    pi = 3.14159265359
    print(f"pi = {pi}")
    print(f"round(pi, 0) = {round(pi, 0)}")
    print(f"round(pi, 1) = {round(pi, 1)}")
    print(f"round(pi, 2) = {round(pi, 2)}")
    print(f"round(pi, 4) = {round(pi, 4)}")
    
    # Rounding to nearest integer
    for value in [2.3, 2.5, 2.7, 3.5]:
        print(f"round({value}) = {round(value)}")
    
    # MATH MODULE FUNCTIONS
    print("\n5. Math Module Functions")
    print("-" * 40)
    
    import math
    
    print(f"math.floor(3.7) = {math.floor(3.7)} (rounds down)")
    print(f"math.ceil(3.2) = {math.ceil(3.2)} (rounds up)")
    print(f"math.trunc(3.7) = {math.trunc(3.7)} (removes decimal)")
    
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.sin(math.pi/2) = {math.sin(math.pi/2)}")
    print(f"math.log(100, 10) = {math.log(100, 10)}")
    
    # PRACTICAL: SHIPPING COST CALCULATOR
    print("\n6. PRACTICAL: SHIPPING COST CALCULATOR")
    print("-" * 40)
    
    class ShippingCalculator:
        """
        Calculates shipping costs based on weight and distance.
        
        Design Pattern: Strategy Pattern - Different pricing strategies
        """
        
        def __init__(self, base_rate: float = 5.0):
            self.base_rate = base_rate
        
        def calculate(self, weight_kg: float, distance_km: float, is_express: bool = False) -> Dict[str, Any]:
            """
            Calculate shipping cost.
            
            Args:
                weight_kg: Package weight in kilograms
                distance_km: Shipping distance in kilometers
                is_express: Whether express shipping is requested
                
            Returns:
                Dictionary with calculation breakdown
            """
            # Weight factor (heavier costs more)
            weight_factor = math.ceil(weight_kg)  # Round up to nearest kg
            weight_cost = self.base_rate * weight_factor
            
            # Distance factor (farther costs more)
            distance_cost = distance_km * 0.10  # $0.10 per km
            
            # Base total
            subtotal = weight_cost + distance_cost
            
            # Express multiplier
            express_multiplier = 1.5 if is_express else 1.0
            total = subtotal * express_multiplier
            
            # Apply bulk discount for heavy packages over long distances
            bulk_discount = 0
            if weight_kg > 20 and distance_km > 500:
                bulk_discount = total * 0.10  # 10% discount
                total -= bulk_discount
            
            return {
                "weight_kg": weight_kg,
                "distance_km": distance_km,
                "weight_cost": round(weight_cost, 2),
                "distance_cost": round(distance_cost, 2),
                "subtotal": round(subtotal, 2),
                "express_multiplier": express_multiplier,
                "bulk_discount": round(bulk_discount, 2),
                "total": round(total, 2)
            }
    
    calculator = ShippingCalculator(base_rate=5.0)
    
    # Standard shipping
    result = calculator.calculate(weight_kg=5.5, distance_km=150)
    print(f"Standard shipping for 5.5kg, 150km:")
    print(f"  Weight cost: ${result['weight_cost']}")
    print(f"  Distance cost: ${result['distance_cost']}")
    print(f"  Total: ${result['total']}")
    
    # Express shipping
    result = calculator.calculate(weight_kg=5.5, distance_km=150, is_express=True)
    print(f"\nExpress shipping (same package): ${result['total']}")
    
    # Heavy package with bulk discount
    result = calculator.calculate(weight_kg=25, distance_km=600)
    print(f"\nHeavy package (25kg, 600km):")
    print(f"  Subtotal: ${result['subtotal']}")
    print(f"  Bulk discount: -${result['bulk_discount']}")
    print(f"  Total: ${result['total']}")


if __name__ == "__main__":
    demonstrate_basic_arithmetic()
    demonstrate_arithmetic_with_different_types()
    demonstrate_special_arithmetic_operations()
```

---

## ⚖️ Section 2: Comparison Operators – Making Comparisons

Comparison operators compare values and return boolean results (True or False). They're essential for decision-making in code.

**SOLID Principle Applied: Dependency Inversion** – Comparison operators work with any comparable type through consistent interfaces.

**Design Pattern: Strategy Pattern** – Different comparison strategies for different data types.

```python
"""
COMPARISON OPERATORS: MAKING COMPARISONS

This section covers all comparison operators:
==, !=, <, >, <=, >=

SOLID Principle: Dependency Inversion
- Operators work with any comparable type

Design Pattern: Strategy Pattern
- Different strategies for different types
"""

from typing import Any, List, Dict, Tuple
from datetime import datetime, date


def demonstrate_basic_comparisons():
    """
    Demonstrates fundamental comparison operations.
    
    Comparison operators return boolean (True/False) results.
    They can be used with numbers, strings, dates, and custom objects.
    """
    print("=" * 60)
    print("SECTION 2A: BASIC COMPARISON OPERATORS")
    print("=" * 60)
    
    # EQUAL TO (==)
    print("\n1. EQUAL TO (==)")
    print("-" * 40)
    
    print(f"5 == 5: {5 == 5}")
    print(f"5 == 3: {5 == 3}")
    print(f"'hello' == 'hello': {'hello' == 'hello'}")
    print(f"'hello' == 'Hello': {'hello' == 'Hello'} (case sensitive)")
    print(f"5 == 5.0: {5 == 5.0} (different numeric types)")
    
    # NOT EQUAL TO (!=)
    print("\n2. NOT EQUAL TO (!=)")
    print("-" * 40)
    
    print(f"5 != 3: {5 != 3}")
    print(f"5 != 5: {5 != 5}")
    print(f"'apple' != 'orange': {'apple' != 'orange'}")
    
    # LESS THAN (<)
    print("\n3. LESS THAN (<)")
    print("-" * 40)
    
    print(f"3 < 5: {3 < 5}")
    print(f"5 < 3: {5 < 3}")
    print(f"10 < 10: {10 < 10}")
    
    # LESS THAN OR EQUAL TO (<=)
    print("\n4. LESS THAN OR EQUAL TO (<=)")
    print("-" * 40)
    
    print(f"3 <= 5: {3 <= 5}")
    print(f"5 <= 5: {5 <= 5}")
    print(f"6 <= 5: {6 <= 5}")
    
    # GREATER THAN (>)
    print("\n5. GREATER THAN (>)")
    print("-" * 40)
    
    print(f"5 > 3: {5 > 3}")
    print(f"3 > 5: {3 > 5}")
    print(f"10 > 10: {10 > 10}")
    
    # GREATER THAN OR EQUAL TO (>=)
    print("\n6. GREATER THAN OR EQUAL TO (>=)")
    print("-" * 40)
    
    print(f"5 >= 3: {5 >= 3}")
    print(f"5 >= 5: {5 >= 5}")
    print(f"3 >= 5: {3 >= 5}")
    
    # COMPARING STRINGS (Lexicographical order)
    print("\n7. COMPARING STRINGS")
    print("-" * 40)
    
    print(f"'apple' < 'banana': {'apple' < 'banana'} (a comes before b)")
    print(f"'apple' > 'Apple': {'apple' > 'Apple'} (lowercase > uppercase in ASCII)")
    print(f"'car' < 'cat': {'car' < 'cat'} (compare character by character)")
    print(f"'abc' < 'abcd': {'abc' < 'abcd'} (shorter string is less if prefix matches)")
    
    # COMPARING LISTS (Lexicographical order)
    print("\n8. COMPARING LISTS")
    print("-" * 40)
    
    print(f"[1, 2, 3] == [1, 2, 3]: {[1, 2, 3] == [1, 2, 3]}")
    print(f"[1, 2, 3] < [1, 2, 4]: {[1, 2, 3] < [1, 2, 4]}")
    print(f"[1, 2] < [1, 2, 3]: {[1, 2] < [1, 2, 3]}")


def demonstrate_chaining_comparisons():
    """
    Demonstrates chaining multiple comparisons.
    
    Python allows chaining comparisons like `a < b < c`
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: CHAINING COMPARISONS")
    print("=" * 60)
    
    # BASIC CHAINING
    print("\n1. BASIC CHAINING")
    print("-" * 40)
    
    x = 5
    print(f"x = {x}")
    print(f"1 < x < 10: {1 < x < 10} (equivalent to 1 < x and x < 10)")
    print(f"1 < x < 5: {1 < x < 5}")
    
    # MULTIPLE CHAINS
    print("\n2. MULTIPLE COMPARISONS")
    print("-" * 40)
    
    a, b, c, d = 5, 10, 15, 20
    print(f"a={a}, b={b}, c={c}, d={d}")
    print(f"a < b < c < d: {a < b < c < d}")
    print(f"a < b > c < d: {a < b > c < d} (mixed operators allowed)")
    
    # WITH EQUALITY
    print("\n3. CHAINING WITH EQUALITY")
    print("-" * 40)
    
    x = 10
    print(f"x = {x}")
    print(f"5 <= x <= 15: {5 <= x <= 15}")
    print(f"5 < x == 10: {5 < x == 10}")
    
    # PRACTICAL: VALIDATING RANGES
    print("\n4. PRACTICAL: RANGE VALIDATION")
    print("-" * 40)
    
    def validate_age(age: int) -> bool:
        """Check if age is valid (between 0 and 150)."""
        return 0 <= age <= 150
    
    def validate_grade(score: float) -> str:
        """Convert numeric score to letter grade."""
        if 90 <= score <= 100:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        elif 0 <= score < 60:
            return "F"
        else:
            return "Invalid"
    
    test_ages = [-5, 25, 200]
    for age in test_ages:
        print(f"Age {age} is valid: {validate_age(age)}")
    
    test_scores = [95, 85, 75, 65, 55, 105]
    for score in test_scores:
        print(f"Score {score} → Grade: {validate_grade(score)}")


def compare_different_types():
    """
    Demonstrates comparing values of different types.
    
    Some comparisons work, others raise TypeError.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: COMPARING DIFFERENT TYPES")
    print("=" * 60)
    
    # NUMERIC TYPES
    print("\n1. NUMERIC TYPES")
    print("-" * 40)
    
    print(f"5 == 5.0: {5 == 5.0} (int and float)")
    print(f"5 < 5.5: {5 < 5.5}")
    print(f"10 > 9.99: {10 > 9.99}")
    
    # BOOLEAN (True/False are 1/0)
    print("\n2. BOOLEAN COMPARISONS")
    print("-" * 40)
    
    print(f"True == 1: {True == 1}")
    print(f"False == 0: {False == 0}")
    print(f"True < 2: {True < 2}")
    print(f"True > False: {True > False}")
    
    # None comparisons
    print("\n3. NONE COMPARISONS")
    print("-" * 40)
    
    print(f"None == None: {None == None}")
    print(f"None is None: {None is None} (use 'is' for None)")
    print(f"None == 0: {None == 0} (not equal)")
    print(f"None == False: {None == False} (not equal)")
    
    # Type mismatches (raise TypeError)
    print("\n4. TYPE MISMATCHES (Raise TypeError)")
    print("-" * 40)
    
    # This would raise TypeError:
    # print("5" < 10)  # TypeError: '<' not supported between 'str' and 'int'
    
    print("String and number comparisons raise TypeError:")
    print("  '5' < 10  → TypeError")
    print("  Convert first: int('5') < 10 → works")
    
    # COMPARING DATES
    print("\n5. COMPARING DATES")
    print("-" * 40)
    
    today = date.today()
    tomorrow = date.today().replace(day=today.day + 1) if today.day < 28 else today
    yesterday = date.today().replace(day=today.day - 1) if today.day > 1 else today
    
    print(f"Today: {today}")
    print(f"Tomorrow: {tomorrow}")
    print(f"Yesterday: {yesterday}")
    print(f"Today < Tomorrow: {today < tomorrow}")
    print(f"Yesterday < Today: {yesterday < today}")
    print(f"Today == Today: {today == today}")


def build_loan_approval_system():
    """
    Complete loan approval system using comparison operators.
    
    This demonstrates a real-world system that evaluates loan applications
    based on multiple criteria using comparison operators.
    
    SOLID Principles Applied:
    - Single Responsibility: Each rule is a separate function
    - Open/Closed: New rules can be added without modifying existing code
    
    Design Patterns:
    - Specification Pattern: Business rules as specifications
    - Composite Pattern: Combine multiple rules
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: LOAN APPROVAL SYSTEM")
    print("=" * 60)
    
    from typing import List, Dict, Any, Tuple, Optional
    from dataclasses import dataclass
    from datetime import datetime, timedelta
    
    @dataclass
    class LoanApplication:
        """Represents a loan application."""
        applicant_name: str
        age: int
        annual_income: float
        credit_score: int
        loan_amount: float
        loan_term_months: int
        existing_debt: float
        employment_years: float
        has_collateral: bool
        application_date: datetime = None
        
        def __post_init__(self):
            if self.application_date is None:
                self.application_date = datetime.now()
        
        def debt_to_income_ratio(self) -> float:
            """Calculate debt-to-income ratio."""
            return self.existing_debt / self.annual_income if self.annual_income > 0 else float('inf')
        
        def loan_to_income_ratio(self) -> float:
            """Calculate loan-to-income ratio."""
            return self.loan_amount / self.annual_income if self.annual_income > 0 else float('inf')
    
    class LoanRule:
        """
        Base class for loan approval rules.
        
        Design Pattern: Specification Pattern - Each rule is a specification
        """
        
        def __init__(self, name: str, description: str):
            self.name = name
            self.description = description
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            """
            Evaluate the rule against an application.
            
            Returns:
                Tuple of (passed, message)
            """
            raise NotImplementedError
    
    class AgeRule(LoanRule):
        """Age must be between 18 and 80."""
        
        def __init__(self):
            super().__init__("Age Rule", "Applicant must be between 18 and 80 years old")
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            passed = 18 <= application.age <= 80
            message = f"Age {application.age}: {'PASS' if passed else 'FAIL'} (requires 18-80)"
            return passed, message
    
    class CreditScoreRule(LoanRule):
        """Credit score must be above minimum threshold."""
        
        def __init__(self, min_score: int = 620):
            super().__init__("Credit Score Rule", f"Credit score must be at least {min_score}")
            self.min_score = min_score
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            passed = application.credit_score >= self.min_score
            message = f"Credit score {application.credit_score}: {'PASS' if passed else 'FAIL'} (requires ≥{self.min_score})"
            return passed, message
    
    class IncomeRule(LoanRule):
        """Annual income must be sufficient for loan amount."""
        
        def __init__(self, max_loan_to_income: float = 0.5):
            super().__init__("Income Rule", f"Loan amount cannot exceed {max_loan_to_income * 100}% of annual income")
            self.max_ratio = max_loan_to_income
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            ratio = application.loan_to_income_ratio()
            passed = ratio <= self.max_ratio
            message = f"Loan-to-income ratio {ratio:.1%}: {'PASS' if passed else 'FAIL'} (requires ≤{self.max_ratio:.0%})"
            return passed, message
    
    class DebtToIncomeRule(LoanRule):
        """Debt-to-income ratio must be below threshold."""
        
        def __init__(self, max_ratio: float = 0.43):
            super().__init__("Debt-to-Income Rule", f"Debt-to-income ratio must be below {max_ratio:.0%}")
            self.max_ratio = max_ratio
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            ratio = application.debt_to_income_ratio()
            passed = ratio <= self.max_ratio
            message = f"Debt-to-income ratio {ratio:.1%}: {'PASS' if passed else 'FAIL'} (requires ≤{self.max_ratio:.0%})"
            return passed, message
    
    class EmploymentRule(LoanRule):
        """Employment history must be sufficient."""
        
        def __init__(self, min_years: float = 1.0):
            super().__init__("Employment Rule", f"Must be employed for at least {min_years} years")
            self.min_years = min_years
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            passed = application.employment_years >= self.min_years
            message = f"Employment years {application.employment_years}: {'PASS' if passed else 'FAIL'} (requires ≥{self.min_years})"
            return passed, message
    
    class LoanAmountRule(LoanRule):
        """Loan amount must be within reasonable bounds."""
        
        def __init__(self, min_amount: float = 1000, max_amount: float = 500000):
            super().__init__("Loan Amount Rule", f"Loan amount must be between ${min_amount:,.0f} and ${max_amount:,.0f}")
            self.min_amount = min_amount
            self.max_amount = max_amount
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            passed = self.min_amount <= application.loan_amount <= self.max_amount
            message = f"Loan amount ${application.loan_amount:,.0f}: {'PASS' if passed else 'FAIL'} (requires ${self.min_amount:,.0f}-${self.max_amount:,.0f})"
            return passed, message
    
    class PaymentToIncomeRule(LoanRule):
        """Monthly payment must be affordable relative to income."""
        
        def __init__(self, max_payment_to_income: float = 0.36):
            super().__init__("Payment-to-Income Rule", f"Monthly payment cannot exceed {max_payment_to_income:.0%} of monthly income")
            self.max_ratio = max_payment_to_income
        
        def calculate_monthly_payment(self, application: LoanApplication) -> float:
            """Calculate monthly payment using simple interest formula."""
            monthly_rate = 0.05 / 12  # Assume 5% annual interest rate
            numerator = application.loan_amount * monthly_rate * (1 + monthly_rate) ** application.loan_term_months
            denominator = (1 + monthly_rate) ** application.loan_term_months - 1
            return numerator / denominator if denominator != 0 else float('inf')
        
        def evaluate(self, application: LoanApplication) -> Tuple[bool, str]:
            monthly_income = application.annual_income / 12
            monthly_payment = self.calculate_monthly_payment(application)
            ratio = monthly_payment / monthly_income if monthly_income > 0 else float('inf')
            passed = ratio <= self.max_ratio
            message = f"Payment-to-income ratio {ratio:.1%}: {'PASS' if passed else 'FAIL'} (requires ≤{self.max_ratio:.0%})"
            return passed, message
    
    class LoanApprover:
        """
        Evaluates loan applications against all rules.
        
        Design Pattern: Composite Pattern - Combines multiple rules
        """
        
        def __init__(self):
            self.rules: List[LoanRule] = []
        
        def add_rule(self, rule: LoanRule) -> 'LoanApprover':
            """Add a rule to the approval process."""
            self.rules.append(rule)
            return self
        
        def evaluate(self, application: LoanApplication) -> Dict[str, Any]:
            """
            Evaluate application against all rules.
            
            Returns:
                Dictionary with evaluation results
            """
            results = []
            all_passed = True
            
            for rule in self.rules:
                passed, message = rule.evaluate(application)
                results.append({
                    "rule": rule.name,
                    "description": rule.description,
                    "passed": passed,
                    "message": message
                })
                if not passed:
                    all_passed = False
            
            # Calculate final decision
            if all_passed:
                decision = "APPROVED"
                reason = "All criteria satisfied"
            else:
                decision = "DENIED"
                failed_rules = [r["rule"] for r in results if not r["passed"]]
                reason = f"Failed rules: {', '.join(failed_rules)}"
            
            # Calculate suggested loan terms if denied
            suggested_terms = None
            if not all_passed:
                suggested_terms = self._suggest_terms(application, results)
            
            return {
                "applicant": application.applicant_name,
                "decision": decision,
                "reason": reason,
                "rule_results": results,
                "suggested_terms": suggested_terms
            }
        
        def _suggest_terms(self, application: LoanApplication, results: List[Dict]) -> Optional[Dict]:
            """Suggest modified terms if application is denied."""
            suggestions = {}
            
            # Check income ratio
            for result in results:
                if result["rule"] == "Income Rule" and not result["passed"]:
                    max_loan = application.annual_income * 0.5
                    suggestions["max_loan_amount"] = round(max_loan, 2)
                
                if result["rule"] == "Debt-to-Income Rule" and not result["passed"]:
                    max_debt = application.annual_income * 0.43
                    suggestions["max_total_debt"] = round(max_debt, 2)
            
            return suggestions if suggestions else None
    
    # DEMONSTRATION
    print("\n📋 DEMONSTRATION: LOAN APPROVAL SYSTEM")
    print("-" * 40)
    
    # Create approver with all rules
    approver = LoanApprover()
    approver.add_rule(AgeRule())
    approver.add_rule(CreditScoreRule(min_score=650))
    approver.add_rule(IncomeRule(max_loan_to_income=0.5))
    approver.add_rule(DebtToIncomeRule(max_ratio=0.43))
    approver.add_rule(EmploymentRule(min_years=1.0))
    approver.add_rule(LoanAmountRule(min_amount=1000, max_amount=500000))
    approver.add_rule(PaymentToIncomeRule(max_payment_to_income=0.36))
    
    # Test applications
    print("\n1. EVALUATING LOAN APPLICATIONS")
    print("-" * 40)
    
    applications = [
        LoanApplication(
            applicant_name="Alice Chen",
            age=32,
            annual_income=85000,
            credit_score=720,
            loan_amount=25000,
            loan_term_months=36,
            existing_debt=15000,
            employment_years=5.5,
            has_collateral=False
        ),
        LoanApplication(
            applicant_name="Bob Smith",
            age=22,
            annual_income=35000,
            credit_score=610,
            loan_amount=30000,
            loan_term_months=48,
            existing_debt=20000,
            employment_years=0.5,
            has_collateral=False
        ),
        LoanApplication(
            applicant_name="Carol Davis",
            age=45,
            annual_income=120000,
            credit_score=780,
            loan_amount=100000,
            loan_term_months=60,
            existing_debt=25000,
            employment_years=12.0,
            has_collateral=True
        ),
        LoanApplication(
            applicant_name="David Brown",
            age=65,
            annual_income=50000,
            credit_score=680,
            loan_amount=40000,
            loan_term_months=36,
            existing_debt=30000,
            employment_years=20.0,
            has_collateral=False
        )
    ]
    
    for app in applications:
        print(f"\n{'='*50}")
        print(f"APPLICANT: {app.applicant_name}")
        print(f"{'='*50}")
        print(f"Age: {app.age}")
        print(f"Annual Income: ${app.annual_income:,.2f}")
        print(f"Credit Score: {app.credit_score}")
        print(f"Loan Amount: ${app.loan_amount:,.2f}")
        print(f"Existing Debt: ${app.existing_debt:,.2f}")
        print(f"Employment: {app.employment_years} years")
        
        result = approver.evaluate(app)
        
        print(f"\nDECISION: {result['decision']}")
        print(f"Reason: {result['reason']}")
        
        if result['suggested_terms']:
            print("\nSUGGESTED TERMS:")
            for key, value in result['suggested_terms'].items():
                print(f"  {key}: ${value:,.2f}")
        
        print("\nRULE RESULTS:")
        for rule_result in result['rule_results']:
            status = "✅" if rule_result['passed'] else "❌"
            print(f"  {status} {rule_result['message']}")


if __name__ == "__main__":
    demonstrate_basic_comparisons()
    demonstrate_chaining_comparisons()
    compare_different_types()
    build_loan_approval_system()
```

---

## 🔗 Section 3: Logical Operators – Combining Conditions

Logical operators (and, or, not) combine boolean expressions to create complex conditions. They're essential for decision-making logic.

**SOLID Principle Applied: Interface Segregation** – Each logical operator serves a distinct purpose: conjunction, disjunction, or negation.

**Design Pattern: Composite Pattern** – Logical operators combine simpler conditions into complex expressions.

```python
"""
LOGICAL OPERATORS: COMBINING CONDITIONS

This section covers logical operators:
and, or, not

SOLID Principle: Interface Segregation
- Each operator has a distinct purpose

Design Pattern: Composite Pattern
- Combine simple conditions into complex expressions
"""

from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass


def demonstrate_logical_operators():
    """
    Demonstrates basic logical operators.
    
    and: True only if both operands are True
    or: True if at least one operand is True
    not: Negates the boolean value
    """
    print("=" * 60)
    print("SECTION 3A: BASIC LOGICAL OPERATORS")
    print("=" * 60)
    
    # AND OPERATOR
    print("\n1. AND OPERATOR (and)")
    print("-" * 40)
    
    truth_table = [
        (True, True, True and True),
        (True, False, True and False),
        (False, True, False and True),
        (False, False, False and False)
    ]
    
    print("Truth table for AND:")
    for a, b, result in truth_table:
        print(f"  {a} and {b} = {result}")
    
    # OR OPERATOR
    print("\n2. OR OPERATOR (or)")
    print("-" * 40)
    
    truth_table = [
        (True, True, True or True),
        (True, False, True or False),
        (False, True, False or True),
        (False, False, False or False)
    ]
    
    print("Truth table for OR:")
    for a, b, result in truth_table:
        print(f"  {a} or {b} = {result}")
    
    # NOT OPERATOR
    print("\n3. NOT OPERATOR (not)")
    print("-" * 40)
    
    print(f"not True = {not True}")
    print(f"not False = {not False}")
    
    # PRACTICAL EXAMPLES
    print("\n4. PRACTICAL EXAMPLES")
    print("-" * 40)
    
    age = 25
    has_license = True
    has_insurance = True
    
    # Can drive if: has license AND has insurance
    can_drive = has_license and has_insurance
    print(f"Has license: {has_license}, Has insurance: {has_insurance}")
    print(f"Can drive: {can_drive}")
    
    # Can rent car if: age >= 21 OR (age >= 18 AND has_credit_card)
    age = 19
    has_credit_card = True
    can_rent = age >= 21 or (age >= 18 and has_credit_card)
    print(f"\nAge: {age}, Has credit card: {has_credit_card}")
    print(f"Can rent car: {can_rent}")
    
    # Discount eligibility: NOT a new customer AND (purchase > $100 OR member)
    is_new_customer = False
    purchase_amount = 150
    is_member = False
    
    qualifies = not is_new_customer and (purchase_amount > 100 or is_member)
    print(f"\nNew customer: {is_new_customer}, Purchase: ${purchase_amount}, Member: {is_member}")
    print(f"Qualifies for discount: {qualifies}")


def demonstrate_short_circuit_evaluation():
    """
    Demonstrates short-circuit evaluation in logical operators.
    
    Python stops evaluating as soon as the result is determined.
    This can be used for efficient and safe condition checking.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: SHORT-CIRCUIT EVALUATION")
    print("=" * 60)
    
    # AND SHORT-CIRCUIT (stops at first False)
    print("\n1. AND SHORT-CIRCUIT")
    print("-" * 40)
    
    def expensive_check_1():
        print("  → expensive_check_1() executed")
        return True
    
    def expensive_check_2():
        print("  → expensive_check_2() executed")
        return False
    
    def expensive_check_3():
        print("  → expensive_check_3() executed")
        return True
    
    print("Evaluating: expensive_check_1() and expensive_check_2() and expensive_check_3()")
    result = expensive_check_1() and expensive_check_2() and expensive_check_3()
    print(f"Result: {result}")
    print("Note: expensive_check_3() was NEVER called because AND already had a False")
    
    # OR SHORT-CIRCUIT (stops at first True)
    print("\n2. OR SHORT-CIRCUIT")
    print("-" * 40)
    
    print("Evaluating: expensive_check_2() or expensive_check_1() or expensive_check_3()")
    result = expensive_check_2() or expensive_check_1() or expensive_check_3()
    print(f"Result: {result}")
    print("Note: expensive_check_3() was NEVER called because OR already had a True")
    
    # PRACTICAL USE: Safe attribute access
    print("\n3. PRACTICAL: SAFE ATTRIBUTE ACCESS")
    print("-" * 40)
    
    class User:
        def __init__(self, name: str, profile: Optional[Dict] = None):
            self.name = name
            self.profile = profile
    
    users = [
        User("Alice", {"age": 28, "city": "NYC"}),
        User("Bob", None),
        User("Charlie", {"age": 35, "city": "LA"})
    ]
    
    for user in users:
        # Safe way to access nested attribute
        age = user.profile and user.profile.get("age")
        print(f"{user.name}: age = {age if age is not None else 'unknown'}")
    
    # PRACTICAL: Default values with OR
    print("\n4. PRACTICAL: DEFAULT VALUES")
    print("-" * 40)
    
    def get_display_name(user: Dict) -> str:
        """Get display name with fallback."""
        return user.get("nickname") or user.get("name") or "Anonymous User"
    
    test_users = [
        {"name": "Alice", "nickname": "Ally"},
        {"name": "Bob"},
        {},
        {"nickname": ""}
    ]
    
    for user in test_users:
        display = get_display_name(user)
        print(f"User: {user} → Display: {display}")


def demonstrate_truthiness():
    """
    Demonstrates truthy and falsy values in Python.
    
    Many values evaluate to True or False in boolean context.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: TRUTHY AND FALSY VALUES")
    print("=" * 60)
    
    # FALSY VALUES
    print("\n1. FALSY VALUES (evaluate to False)")
    print("-" * 40)
    
    falsy_values = [
        False,
        None,
        0,
        0.0,
        "",
        [],
        (),
        {},
        set(),
        range(0)
    ]
    
    for value in falsy_values:
        print(f"  bool({repr(value):15}) = {bool(value)}")
    
    # TRUTHY VALUES
    print("\n2. TRUTHY VALUES (evaluate to True)")
    print("-" * 40)
    
    truthy_values = [
        True,
        1,
        -1,
        3.14,
        "Hello",
        "False",
        [1, 2],
        (1, 2),
        {"key": "value"},
        {1, 2, 3}
    ]
    
    for value in truthy_values:
        print(f"  bool({repr(value)[:20]:20}) = {bool(value)}")
    
    # USING TRUTHINESS IN CONDITIONS
    print("\n3. USING TRUTHINESS FOR CONCISE CODE")
    print("-" * 40)
    
    # Instead of: if name is not None and name != ""
    def greet(name):
        if name:  # Truthy check
            print(f"Hello, {name}!")
        else:
            print("Hello, anonymous!")
    
    greet("Alice")
    greet("")
    greet(None)
    
    # Instead of: if len(items) > 0
    def process_items(items):
        if items:  # Truthy check for non-empty list
            print(f"Processing {len(items)} items")
        else:
            print("No items to process")
    
    process_items([1, 2, 3])
    process_items([])


def build_discount_engine():
    """
    Complete discount engine using logical and comparison operators.
    
    This demonstrates a real-world system that calculates discounts
    based on multiple conditions using operators.
    
    SOLID Principles Applied:
    - Single Responsibility: Each discount rule is separate
    - Open/Closed: New discount rules can be added
    
    Design Patterns:
    - Strategy Pattern: Different discount strategies
    - Chain of Responsibility: Multiple discount checks
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: DISCOUNT ENGINE")
    print("=" * 60)
    
    from typing import List, Dict, Any, Optional, Tuple
    from enum import Enum
    from datetime import datetime, timedelta
    
    class CustomerTier(Enum):
        """Customer loyalty tiers."""
        BRONZE = "bronze"
        SILVER = "silver"
        GOLD = "gold"
        PLATINUM = "platinum"
    
    class DiscountType(Enum):
        """Types of discounts."""
        PERCENTAGE = "percentage"
        FIXED_AMOUNT = "fixed_amount"
        FREE_SHIPPING = "free_shipping"
    
    @dataclass
    class Discount:
        """Represents a discount applied to an order."""
        type: DiscountType
        name: str
        value: float  # Percentage or fixed amount
        description: str
    
    @dataclass
    class Order:
        """Represents a customer order."""
        customer_id: str
        customer_tier: CustomerTier
        subtotal: float
        items_count: int
        is_first_purchase: bool
        has_coupon: bool
        coupon_code: Optional[str] = None
        order_date: datetime = None
        
        def __post_init__(self):
            if self.order_date is None:
                self.order_date = datetime.now()
    
    class DiscountRule:
        """
        Base class for discount rules.
        
        Design Pattern: Strategy Pattern - Encapsulates discount logic
        """
        
        def __init__(self, name: str, priority: int = 0):
            self.name = name
            self.priority = priority
        
        def applies(self, order: Order) -> bool:
            """Check if this discount applies to the order."""
            raise NotImplementedError
        
        def calculate(self, order: Order) -> Optional[Discount]:
            """Calculate the discount if applicable."""
            raise NotImplementedError
    
    class TierDiscountRule(DiscountRule):
        """Discount based on customer loyalty tier."""
        
        def __init__(self):
            super().__init__("Tier Discount", priority=10)
        
        def applies(self, order: Order) -> bool:
            return True  # Applies to all orders
        
        def calculate(self, order: Order) -> Optional[Discount]:
            tier_discounts = {
                CustomerTier.BRONZE: 0,
                CustomerTier.SILVER: 5,
                CustomerTier.GOLD: 10,
                CustomerTier.PLATINUM: 15
            }
            
            discount_percent = tier_discounts.get(order.customer_tier, 0)
            
            if discount_percent > 0:
                return Discount(
                    type=DiscountType.PERCENTAGE,
                    name=self.name,
                    value=discount_percent,
                    description=f"{discount_percent}% off for {order.customer_tier.value} members"
                )
            return None
    
    class BulkPurchaseRule(DiscountRule):
        """Discount for purchasing many items."""
        
        def __init__(self, min_items: int = 5, discount_percent: int = 10):
            super().__init__("Bulk Purchase Discount", priority=20)
            self.min_items = min_items
            self.discount_percent = discount_percent
        
        def applies(self, order: Order) -> bool:
            return order.items_count >= self.min_items
        
        def calculate(self, order: Order) -> Optional[Discount]:
            return Discount(
                type=DiscountType.PERCENTAGE,
                name=self.name,
                value=self.discount_percent,
                description=f"{self.discount_percent}% off for buying {self.min_items}+ items"
            )
    
    class HighValueRule(DiscountRule):
        """Discount for high-value orders."""
        
        def __init__(self, min_amount: float = 200, discount_percent: int = 15):
            super().__init__("High Value Discount", priority=30)
            self.min_amount = min_amount
            self.discount_percent = discount_percent
        
        def applies(self, order: Order) -> bool:
            return order.subtotal >= self.min_amount
        
        def calculate(self, order: Order) -> Optional[Discount]:
            return Discount(
                type=DiscountType.PERCENTAGE,
                name=self.name,
                value=self.discount_percent,
                description=f"{self.discount_percent}% off for orders over ${self.min_amount:.0f}"
            )
    
    class FirstPurchaseRule(DiscountRule):
        """Welcome discount for first-time customers."""
        
        def __init__(self, discount_percent: int = 10):
            super().__init__("Welcome Discount", priority=40)
            self.discount_percent = discount_percent
        
        def applies(self, order: Order) -> bool:
            return order.is_first_purchase
        
        def calculate(self, order: Order) -> Optional[Discount]:
            return Discount(
                type=DiscountType.PERCENTAGE,
                name=self.name,
                value=self.discount_percent,
                description=f"{self.discount_percent}% off your first purchase!"
            )
    
    class CouponRule(DiscountRule):
        """Discount from coupon code."""
        
        def __init__(self):
            super().__init__("Coupon Discount", priority=5)
            self.coupons = {
                "SAVE20": {"type": "percentage", "value": 20},
                "SAVE10": {"type": "percentage", "value": 10},
                "FREESHIP": {"type": "free_shipping", "value": 0}
            }
        
        def applies(self, order: Order) -> bool:
            return order.has_coupon and order.coupon_code in self.coupons
        
        def calculate(self, order: Order) -> Optional[Discount]:
            if not self.applies(order):
                return None
            
            coupon = self.coupons[order.coupon_code]
            
            if coupon["type"] == "percentage":
                return Discount(
                    type=DiscountType.PERCENTAGE,
                    name=self.name,
                    value=coupon["value"],
                    description=f"Coupon {order.coupon_code}: {coupon['value']}% off"
                )
            elif coupon["type"] == "free_shipping":
                return Discount(
                    type=DiscountType.FREE_SHIPPING,
                    name=self.name,
                    value=0,
                    description=f"Coupon {order.coupon_code}: Free shipping"
                )
            
            return None
    
    class DiscountEngine:
        """
        Calculates best available discount for an order.
        
        Design Pattern: Chain of Responsibility - Tries each rule in priority order
        """
        
        def __init__(self):
            self.rules: List[DiscountRule] = []
        
        def add_rule(self, rule: DiscountRule) -> 'DiscountEngine':
            """Add a discount rule."""
            self.rules.append(rule)
            return self
        
        def calculate_best_discount(self, order: Order) -> Tuple[Optional[Discount], float]:
            """
            Calculate the best applicable discount.
            
            Returns:
                Tuple of (best_discount, discounted_amount)
            """
            applicable_discounts = []
            
            for rule in sorted(self.rules, key=lambda r: r.priority):
                if rule.applies(order):
                    discount = rule.calculate(order)
                    if discount:
                        applicable_discounts.append(discount)
            
            if not applicable_discounts:
                return None, order.subtotal
            
            # For simplicity, take the largest percentage discount
            # In production, would need more sophisticated combination logic
            best_discount = max(
                applicable_discounts,
                key=lambda d: d.value if d.type == DiscountType.PERCENTAGE else 0
            )
            
            if best_discount.type == DiscountType.PERCENTAGE:
                discount_amount = order.subtotal * (best_discount.value / 100)
                final_amount = order.subtotal - discount_amount
            else:
                discount_amount = 0
                final_amount = order.subtotal
            
            return best_discount, final_amount
    
    # DEMONSTRATION
    print("\n🛒 DEMONSTRATION: DISCOUNT ENGINE")
    print("-" * 40)
    
    # Create discount engine with all rules
    engine = DiscountEngine()
    engine.add_rule(TierDiscountRule())
    engine.add_rule(BulkPurchaseRule(min_items=5, discount_percent=10))
    engine.add_rule(HighValueRule(min_amount=200, discount_percent=15))
    engine.add_rule(FirstPurchaseRule(discount_percent=10))
    engine.add_rule(CouponRule())
    
    # Test orders
    test_orders = [
        Order(
            customer_id="CUST-001",
            customer_tier=CustomerTier.BRONZE,
            subtotal=75.00,
            items_count=2,
            is_first_purchase=False,
            has_coupon=False
        ),
        Order(
            customer_id="CUST-002",
            customer_tier=CustomerTier.GOLD,
            subtotal=150.00,
            items_count=6,
            is_first_purchase=False,
            has_coupon=False
        ),
        Order(
            customer_id="CUST-003",
            customer_tier=CustomerTier.SILVER,
            subtotal=250.00,
            items_count=3,
            is_first_purchase=False,
            has_coupon=False
        ),
        Order(
            customer_id="CUST-004",
            customer_tier=CustomerTier.BRONZE,
            subtotal=45.00,
            items_count=1,
            is_first_purchase=True,
            has_coupon=False
        ),
        Order(
            customer_id="CUST-005",
            customer_tier=CustomerTier.BRONZE,
            subtotal=120.00,
            items_count=2,
            is_first_purchase=False,
            has_coupon=True,
            coupon_code="SAVE20"
        )
    ]
    
    print("\nDISCOUNT CALCULATIONS:")
    print("=" * 60)
    
    for order in test_orders:
        print(f"\nOrder for {order.customer_tier.value.upper()} tier customer")
        print(f"  Subtotal: ${order.subtotal:.2f}")
        print(f"  Items: {order.items_count}")
        print(f"  First purchase: {order.is_first_purchase}")
        print(f"  Has coupon: {order.has_coupon} ({order.coupon_code if order.has_coupon else 'N/A'})")
        
        discount, final_amount = engine.calculate_best_discount(order)
        
        if discount:
            print(f"\n  ✓ Applied: {discount.description}")
            if discount.type == DiscountType.PERCENTAGE:
                discount_amount = order.subtotal * (discount.value / 100)
                print(f"    Discount amount: ${discount_amount:.2f}")
        else:
            print(f"\n  No discount applicable")
        
        print(f"  Final total: ${final_amount:.2f}")
        print("-" * 40)


if __name__ == "__main__":
    demonstrate_logical_operators()
    demonstrate_short_circuit_evaluation()
    demonstrate_truthiness()
    build_discount_engine()
```

---

## 📝 Section 4: Assignment and Membership Operators

Assignment operators update variable values efficiently. Membership operators check if a value exists in a collection.

**SOLID Principle Applied: Single Responsibility** – Each assignment operator performs one specific update operation.

**Design Pattern: Command Pattern** – Assignment operators are commands that modify variable state.

```python
"""
ASSIGNMENT AND MEMBERSHIP OPERATORS

This section covers:
- Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
- Membership operators: in, not in

SOLID Principle: Single Responsibility
- Each operator performs one specific operation

Design Pattern: Command Pattern
- Assignment operators modify variable state
"""

from typing import List, Any


def demonstrate_assignment_operators():
    """
    Demonstrates assignment and augmented assignment operators.
    
    Augmented assignment operators combine an operation with assignment.
    """
    print("=" * 60)
    print("SECTION 4A: ASSIGNMENT OPERATORS")
    print("=" * 60)
    
    # BASIC ASSIGNMENT (=)
    print("\n1. BASIC ASSIGNMENT (=)")
    print("-" * 40)
    
    x = 10
    name = "Alice"
    numbers = [1, 2, 3]
    
    print(f"x = {x}")
    print(f"name = '{name}'")
    print(f"numbers = {numbers}")
    
    # AUGMENTED ASSIGNMENT
    print("\n2. AUGMENTED ASSIGNMENT OPERATORS")
    print("-" * 40)
    
    # Addition assignment (+=)
    counter = 0
    print(f"counter = {counter}")
    counter += 5
    print(f"counter += 5 → {counter}")
    counter += 3
    print(f"counter += 3 → {counter}")
    
    # Subtraction assignment (-=)
    value = 100
    print(f"\nvalue = {value}")
    value -= 25
    print(f"value -= 25 → {value}")
    value -= 10
    print(f"value -= 10 → {value}")
    
    # Multiplication assignment (*=)
    product = 5
    print(f"\nproduct = {product}")
    product *= 4
    print(f"product *= 4 → {product}")
    product *= 2
    print(f"product *= 2 → {product}")
    
    # Division assignment (/=)
    quotient = 100
    print(f"\nquotient = {quotient}")
    quotient /= 4
    print(f"quotient /= 4 → {quotient}")
    
    # Floor division assignment (//=)
    floor_div = 17
    print(f"\nfloor_div = {floor_div}")
    floor_div //= 5
    print(f"floor_div //= 5 → {floor_div}")
    
    # Modulus assignment (%=)
    remainder = 17
    print(f"\nremainder = {remainder}")
    remainder %= 5
    print(f"remainder %= 5 → {remainder}")
    
    # Exponentiation assignment (**=)
    power = 2
    print(f"\npower = {power}")
    power **= 10
    print(f"power **= 10 → {power}")
    
    # STRING AND LIST AUGMENTED ASSIGNMENT
    print("\n3. AUGMENTED ASSIGNMENT WITH STRINGS AND LISTS")
    print("-" * 40)
    
    # String concatenation
    message = "Hello"
    print(f"message = '{message}'")
    message += " World"
    print(f"message += ' World' → '{message}'")
    message += "!"
    print(f"message += '!' → '{message}'")
    
    # List extension
    cart = ["apple", "banana"]
    print(f"cart = {cart}")
    cart += ["cherry", "date"]
    print(f"cart += ['cherry', 'date'] → {cart}")
    
    # PRACTICAL USE: ACCUMULATORS
    print("\n4. PRACTICAL: ACCUMULATORS")
    print("-" * 40)
    
    # Summing numbers
    total = 0
    prices = [29.99, 49.99, 19.99, 99.99]
    
    for price in prices:
        total += price
        print(f"  Added ${price:.2f}, running total: ${total:.2f}")
    
    # Building a string
    words = ["Python", "is", "awesome", "and", "powerful"]
    sentence = ""
    
    for word in words:
        sentence += word + " "
    
    print(f"\nBuilt sentence: '{sentence.strip()}'")
    
    # Counting occurrences
    text = "abracadabra"
    char_counts = {}
    
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    print(f"Character counts: {char_counts}")


def demonstrate_membership_operators():
    """
    Demonstrates membership operators (in, not in).
    
    Check if a value exists in a sequence or collection.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: MEMBERSHIP OPERATORS")
    print("=" * 60)
    
    # STRING MEMBERSHIP
    print("\n1. STRING MEMBERSHIP")
    print("-" * 40)
    
    text = "The quick brown fox jumps over the lazy dog"
    
    print(f"Text: '{text}'")
    print(f"'quick' in text: {'quick' in text}")
    print(f"'slow' in text: {'slow' in text}")
    print(f"'fox' not in text: {'fox' not in text}")
    print(f"'cat' not in text: {'cat' not in text}")
    
    # Check if string starts with prefix
    print(f"text.startswith('The'): {text.startswith('The')}")
    
    # Check if string ends with suffix
    print(f"text.endswith('dog'): {text.endswith('dog')}")
    
    # LIST MEMBERSHIP
    print("\n2. LIST MEMBERSHIP")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry", "date"]
    
    print(f"Fruits: {fruits}")
    print(f"'banana' in fruits: {'banana' in fruits}")
    print(f"'grape' in fruits: {'grape' in fruits}")
    print(f"'apple' not in fruits: {'apple' not in fruits}")
    
    # DICTIONARY MEMBERSHIP
    print("\n3. DICTIONARY MEMBERSHIP")
    print("-" * 40)
    
    user = {
        "name": "Alice",
        "age": 28,
        "email": "alice@example.com"
    }
    
    print(f"User dict: {user}")
    print(f"'name' in user: {'name' in user} (checks keys)")
    print(f"'age' in user: {'age' in user}")
    print(f"'phone' in user: {'phone' in user}")
    print(f"'Alice' in user.values(): {'Alice' in user.values()}")
    
    # SET MEMBERSHIP (O(1) - very fast!)
    print("\n4. SET MEMBERSHIP (O(1) performance)")
    print("-" * 40)
    
    valid_ids = {1001, 1002, 1003, 1004, 1005}
    
    test_ids = [1001, 1006, 1003, 1007]
    
    for test_id in test_ids:
        is_valid = test_id in valid_ids
        print(f"ID {test_id} is valid: {is_valid}")
    
    # TUPLE MEMBERSHIP
    print("\n5. TUPLE MEMBERSHIP")
    print("-" * 40)
    
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    print(f"'Wednesday' in days: {'Wednesday' in days}")
    print(f"'Funday' in days: {'Funday' in days}")
    
    # PRACTICAL USE CASES
    print("\n6. PRACTICAL USE CASES")
    print("-" * 40)
    
    # Email validation
    def is_valid_email(email: str) -> bool:
        """Check if email has basic valid format."""
        return "@" in email and "." in email.split("@")[-1]
    
    emails = ["alice@example.com", "bob@gmail", "invalid", "charlie@company.co.uk"]
    
    for email in emails:
        valid = is_valid_email(email)
        print(f"'{email}' is {'valid' if valid else 'invalid'}")
    
    # Category filter
    allowed_categories = {"electronics", "books", "clothing", "toys"}
    
    def can_ship_product(category: str) -> bool:
        """Check if product category can be shipped."""
        return category in allowed_categories
    
    products = [
        ("Laptop", "electronics"),
        ("Novel", "books"),
        ("Perishable Food", "food"),
        ("Action Figure", "toys")
    ]
    
    for product, category in products:
        shippable = can_ship_product(category)
        print(f"{product} ({category}): {'can ship' if shippable else 'cannot ship'}")
    
    # Permission checking
    user_permissions = {"read", "write", "delete"}
    
    def has_permission(user_perms: set, required_perms: set) -> bool:
        """Check if user has all required permissions."""
        return required_perms.issubset(user_perms)
    
    required = {"read", "write"}
    print(f"\nUser permissions: {user_permissions}")
    print(f"Required: {required}")
    print(f"Has all required permissions: {has_permission(user_permissions, required)}")


def build_age_verification_system():
    """
    Complete age verification system using comparison and logical operators.
    
    This demonstrates a real-world system for verifying user age
    and determining access to age-restricted content.
    
    SOLID Principles Applied:
    - Single Responsibility: Each verification rule is separate
    - Open/Closed: New verification rules can be added
    
    Design Patterns:
    - Specification Pattern: Age verification rules
    - Composite Pattern: Combine multiple verification methods
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: AGE VERIFICATION SYSTEM")
    print("=" * 60)
    
    from typing import List, Dict, Any, Tuple, Optional
    from datetime import datetime, date
    from enum import Enum
    from dataclasses import dataclass
    
    class ContentRating(Enum):
        """Content rating categories."""
        G = "General Audience"
        PG = "Parental Guidance"
        PG13 = "Parents Strongly Cautioned"
        R = "Restricted"
        NC17 = "Adults Only"
    
    @dataclass
    class User:
        """Represents a user attempting to access content."""
        user_id: str
        name: str
        birth_date: date
        country: str
        has_parental_consent: bool = False
        is_verified: bool = False
    
    class AgeVerificationRule:
        """Base class for age verification rules."""
        
        def __init__(self, name: str):
            self.name = name
        
        def verify(self, user: User, content_rating: ContentRating) -> Tuple[bool, str]:
            """Verify if user meets age requirements."""
            raise NotImplementedError
    
    class MinimumAgeRule(AgeVerificationRule):
        """Verify user meets minimum age requirement."""
        
        def __init__(self):
            super().__init__("Minimum Age Rule")
        
        def get_minimum_age(self, rating: ContentRating) -> int:
            """Get minimum age required for content rating."""
            age_requirements = {
                ContentRating.G: 0,
                ContentRating.PG: 8,
                ContentRating.PG13: 13,
                ContentRating.R: 17,
                ContentRating.NC17: 18
            }
            return age_requirements.get(rating, 18)
        
        def calculate_age(self, birth_date: date) -> int:
            """Calculate age from birth date."""
            today = date.today()
            age = today.year - birth_date.year
            # Adjust if birthday hasn't occurred this year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            return age
        
        def verify(self, user: User, content_rating: ContentRating) -> Tuple[bool, str]:
            min_age = self.get_minimum_age(content_rating)
            user_age = self.calculate_age(user.birth_date)
            
            if min_age == 0:
                return True, "No age restriction"
            
            passed = user_age >= min_age
            message = f"Age {user_age} ≥ {min_age}: {'PASS' if passed else 'FAIL'}"
            return passed, message
    
    class ParentalConsentRule(AgeVerificationRule):
        """Allow younger users with parental consent."""
        
        def __init__(self):
            super().__init__("Parental Consent Rule")
        
        def verify(self, user: User, content_rating: ContentRating) -> Tuple[bool, str]:
            # PG-13 content may be allowed with parental consent for 13-17 year olds
            if content_rating == ContentRating.PG13 and user.has_parental_consent:
                return True, "Access granted with parental consent"
            
            # R content may be allowed with parental consent for 15-17 year olds
            if content_rating == ContentRating.R and user.has_parental_consent:
                return True, "Access granted with parental consent"
            
            return False, "Parental consent not applicable or insufficient"
    
    class CountrySpecificRule(AgeVerificationRule):
        """Handle country-specific age requirements."""
        
        def __init__(self):
            super().__init__("Country Specific Rule")
        
        def get_country_age(self, country: str, rating: ContentRating) -> Optional[int]:
            """Get country-specific age requirement."""
            # Different countries have different age requirements
            country_rules = {
                "US": {ContentRating.R: 17, ContentRating.NC17: 18},
                "UK": {ContentRating.R: 18, ContentRating.NC17: 18},
                "Germany": {ContentRating.R: 18, ContentRating.NC17: 18},
                "Japan": {ContentRating.R: 18, ContentRating.NC17: 18}
            }
            
            return country_rules.get(country, {}).get(rating)
        
        def verify(self, user: User, content_rating: ContentRating) -> Tuple[bool, str]:
            country_age = self.get_country_age(user.country, content_rating)
            
            if country_age is None:
                return True, "No country-specific restriction"
            
            from datetime import date
            user_age = date.today().year - user.birth_date.year
            
            passed = user_age >= country_age
            message = f"Country {user.country} requires age {country_age}: {'PASS' if passed else 'FAIL'}"
            return passed, message
    
    class VerifiedAccountRule(AgeVerificationRule):
        """Require verified account for restricted content."""
        
        def __init__(self):
            super().__init__("Verified Account Rule")
        
        def verify(self, user: User, content_rating: ContentRating) -> Tuple[bool, str]:
            # R and NC-17 content require verified accounts
            if content_rating in [ContentRating.R, ContentRating.NC17]:
                passed = user.is_verified
                message = f"Account verified: {'PASS' if passed else 'FAIL'} (required for restricted content)"
                return passed, message
            
            return True, "Verification not required"
    
    class AgeVerifier:
        """
        Complete age verification system.
        
        Design Pattern: Chain of Responsibility - Runs all verification rules
        """
        
        def __init__(self):
            self.rules: List[AgeVerificationRule] = [
                MinimumAgeRule(),
                ParentalConsentRule(),
                CountrySpecificRule(),
                VerifiedAccountRule()
            ]
        
        def verify_access(self, user: User, content_rating: ContentRating) -> Dict[str, Any]:
            """
            Verify if user can access content.
            
            Returns:
                Dictionary with verification results
            """
            results = []
            all_passed = True
            final_message = ""
            
            for rule in self.rules:
                passed, message = rule.verify(user, content_rating)
                results.append({
                    "rule": rule.name,
                    "passed": passed,
                    "message": message
                })
                
                if not passed:
                    all_passed = False
                    final_message = message
            
            return {
                "user": user.name,
                "content_rating": content_rating.value,
                "access_granted": all_passed,
                "message": "Access granted" if all_passed else f"Access denied: {final_message}",
                "rule_results": results
            }
    
    # DEMONSTRATION
    print("\n🔞 DEMONSTRATION: AGE VERIFICATION SYSTEM")
    print("-" * 40)
    
    verifier = AgeVerifier()
    
    # Test users
    test_users = [
        User(
            user_id="USER-001",
            name="Alice (16, US, verified)",
            birth_date=date(2010, 3, 15),
            country="US",
            has_parental_consent=True,
            is_verified=True
        ),
        User(
            user_id="USER-002",
            name="Bob (16, US, not verified)",
            birth_date=date(2010, 3, 15),
            country="US",
            has_parental_consent=False,
            is_verified=False
        ),
        User(
            user_id="USER-003",
            name="Charlie (25, US, verified)",
            birth_date=date(1999, 6, 20),
            country="US",
            has_parental_consent=False,
            is_verified=True
        ),
        User(
            user_id="USER-004",
            name="Diana (17, UK, verified)",
            birth_date=date(2009, 8, 10),
            country="UK",
            has_parental_consent=False,
            is_verified=True
        )
    ]
    
    content_ratings = [ContentRating.G, ContentRating.PG13, ContentRating.R, ContentRating.NC17]
    
    for user in test_users:
        print(f"\n{'='*50}")
        print(f"USER: {user.name}")
        print(f"  Age: {AgeVerificationRule().calculate_age(user.birth_date)}")
        print(f"  Country: {user.country}")
        print(f"  Verified: {user.is_verified}")
        print(f"  Parental Consent: {user.has_parental_consent}")
        print(f"{'='*50}")
        
        for rating in content_ratings:
            result = verifier.verify_access(user, rating)
            status = "✅" if result["access_granted"] else "❌"
            print(f"{status} {rating.value}: {result['message']}")


if __name__ == "__main__":
    demonstrate_assignment_operators()
    demonstrate_membership_operators()
    build_age_verification_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Arithmetic Operators** – +, -, *, /, //, %, **. Calculate totals, discounts, and mathematical transformations. Use floor division (//) for integer division. Use modulus (%) for remainders and even/odd checks.

- **Comparison Operators** – ==, !=, <, >, <=, >=. Compare values and return boolean results. Chain comparisons for range checks (a < b < c). Compare strings lexicographically.

- **Logical Operators** – and, or, not. Combine boolean expressions. Short-circuit evaluation stops early when result is determined. Use truthiness for concise condition checks.

- **Assignment Operators** – =, +=, -=, *=, /=, //=, %=, **=. Update variables efficiently. Use augmented assignment for accumulators and counters.

- **Membership Operators** – in, not in. Check if value exists in collections. O(1) for sets and dicts. O(n) for lists and tuples.

- **SOLID Principles Applied** – Single Responsibility (each operator does one thing), Interface Segregation (distinct operator types), Dependency Inversion (operators work with any type).

- **Design Patterns Used** – Interpreter Pattern (arithmetic expressions), Strategy Pattern (comparison and discount strategies), Composite Pattern (logical combinations), Specification Pattern (verification rules), Chain of Responsibility (multiple rule evaluation).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Control Flow – if, elif, else

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 3 | 4 | 43% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **8** | **44** | **15%** |

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap: Reading the Map
4. Series 0, Story 4: The 2026 Python Metromap: Avoiding Derailments
5. Series 0, Story 5: The 2026 Python Metromap: From Passenger to Driver
6. Series A, Story 1: The 2026 Python Metromap: Variables & Data Types – The Rails of Python
7. Series A, Story 2: The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets
8. Series A, Story 3: The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More

**Next Story:** Series A, Story 4: The 2026 Python Metromap: Control Flow – if, elif, else

---

## 📝 Your Invitation

You've mastered operators. Now build something with what you've learned:

1. **Build a discount calculator** – Use arithmetic operators to calculate percentage discounts. Use comparison operators for tiered discounts. Use logical operators for combining conditions.

2. **Create a loan eligibility checker** – Use comparison operators for age, income, and credit score checks. Use logical operators to combine multiple criteria.

3. **Build an age verification system** – Use comparison operators for age checks. Use membership operators for allowed countries. Use logical operators for consent rules.

4. **Create a price calculator** – Use arithmetic operators for subtotals, taxes, and totals. Use augmented assignment for accumulators.

5. **Build a shopping cart with discounts** – Combine all operator types to create a complete pricing engine.

**You've mastered operators. Next stop: Control Flow!**

---

*Found this helpful? Clap, comment, and share what you built with operators. Next stop: Control Flow!* 🚇