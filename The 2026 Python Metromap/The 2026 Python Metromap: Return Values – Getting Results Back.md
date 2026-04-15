# The 2026 Python Metromap: Return Values – Getting Results Back

## Series B: Functions & Modules Yard | Story 3 of 6

![The 2026 Python Metromap/images/Return Values – Getting Results Back](images/Return Values – Getting Results Back.png)

## 📖 Introduction

**Welcome to the third stop on the Functions & Modules Yard Line.**

You've mastered defining functions and passing arguments. You know how to send data into functions. But what about getting data out? A function that calculates a value is useless if you can't use that result elsewhere in your code.

Return values are how functions communicate results back to the caller. The `return` statement ends function execution and sends a value back. Functions can return single values, multiple values as tuples, complex objects, or even nothing at all. The way you structure return values determines how reusable and testable your functions become.

This story—**The 2026 Python Metromap: Return Values – Getting Results Back**—is your guide to mastering function returns. We'll build a complete API response formatter that standardizes success and error responses. We'll create a data validation system that returns detailed results with error messages. We'll implement a result pattern for handling operations that can fail. And we'll build a complete order processing system with structured return values.

**Let's get results back.**

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

- 📤 **The 2026 Python Metromap: Return Values – Getting Results Back** – API response formatter; standardized success and error responses. **⬅️ YOU ARE HERE**

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines. 🔜 *Up Next*

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver.

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📤 Section 1: Return Statement Basics

The `return` statement exits a function and optionally sends a value back to the caller.

**SOLID Principle Applied: Single Responsibility** – Functions should return results without side effects.

**Design Pattern: Command Pattern** – Return values are the result of executing a command.

```python
"""
RETURN STATEMENT BASICS

This section covers the fundamentals of returning values from functions.

SOLID Principle: Single Responsibility
- Functions return results without side effects

Design Pattern: Command Pattern
- Return values are command execution results
"""

from typing import Any, Optional, Tuple, List, Dict
from datetime import datetime
import random


def demonstrate_return_basics():
    """
    Demonstrates basic return statement syntax and usage.
    
    The return statement ends function execution and sends a value back.
    """
    print("=" * 60)
    print("SECTION 1A: RETURN STATEMENT BASICS")
    print("=" * 60)
    
    # NO RETURN (returns None implicitly)
    print("\n1. NO RETURN STATEMENT (returns None)")
    print("-" * 40)
    
    def greet(name):
        print(f"  Hello, {name}!")
        # No return statement
    
    result = greet("Alice")
    print(f"  Return value: {result} (type: {type(result).__name__})")
    
    # SINGLE RETURN VALUE
    print("\n2. SINGLE RETURN VALUE")
    print("-" * 40)
    
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b
    
    result = add(5, 3)
    print(f"  add(5, 3) = {result} (type: {type(result).__name__})")
    
    # RETURN STOPS FUNCTION EXECUTION
    print("\n3. RETURN STOPS FUNCTION EXECUTION")
    print("-" * 40)
    
    def early_return(value):
        print("  Start of function")
        
        if value < 0:
            print("  Negative value - returning early")
            return "Error: Negative value"
        
        print("  Processing positive value")
        result = value * 2
        print("  End of function")
        return result
    
    print("  Calling with positive value:")
    result1 = early_return(10)
    print(f"  Result: {result1}")
    
    print("\n  Calling with negative value:")
    result2 = early_return(-5)
    print(f"  Result: {result2}")
    
    # RETURN WITH EXPRESSION
    print("\n4. RETURN WITH EXPRESSION")
    print("-" * 40)
    
    def calculate_discount(price, discount_percent):
        """Return calculated discount (expression directly)."""
        return price * discount_percent / 100
    
    discount = calculate_discount(100, 15)
    print(f"  Discount on $100 at 15%: ${discount:.2f}")
    
    # RETURNING FROM LOOPS
    print("\n5. RETURNING FROM LOOPS")
    print("-" * 40)
    
    def find_first_even(numbers):
        """Return first even number found, or None."""
        for num in numbers:
            if num % 2 == 0:
                return num  # Exit function immediately
        return None  # No even number found
    
    numbers = [1, 3, 5, 8, 10, 13]
    result = find_first_even(numbers)
    print(f"  First even in {numbers}: {result}")
    
    # RETURN FROM CONDITIONAL
    print("\n6. RETURN FROM CONDITIONAL")
    print("-" * 40)
    
    def get_status_code(status):
        """Return different values based on condition."""
        if status == "success":
            return 200
        elif status == "created":
            return 201
        elif status == "bad_request":
            return 400
        elif status == "unauthorized":
            return 401
        elif status == "not_found":
            return 404
        else:
            return 500
    
    print(f"  success → {get_status_code('success')}")
    print(f"  not_found → {get_status_code('not_found')}")
    print(f"  unknown → {get_status_code('unknown')}")


def demonstrate_multiple_return_values():
    """
    Demonstrates returning multiple values using tuples.
    
    Python allows returning multiple values packed into a tuple.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: MULTIPLE RETURN VALUES")
    print("=" * 60)
    
    # BASIC MULTIPLE RETURNS
    print("\n1. RETURNING MULTIPLE VALUES (as tuple)")
    print("-" * 40)
    
    def get_min_max(numbers):
        """Return both minimum and maximum values."""
        if not numbers:
            return None, None
        return min(numbers), max(numbers)
    
    result = get_min_max([3, 1, 4, 1, 5, 9, 2])
    print(f"  Return value: {result} (type: {type(result).__name__})")
    
    # UNPACKING RETURN VALUES
    print("\n2. UNPACKING MULTIPLE RETURNS")
    print("-" * 40)
    
    min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2])
    print(f"  Unpacked: min={min_val}, max={max_val}")
    
    # FUNCTION WITH 3+ RETURN VALUES
    print("\n3. FUNCTION WITH MULTIPLE RETURN VALUES")
    print("-" * 40)
    
    def analyze_list(numbers):
        """Return multiple statistics about a list."""
        if not numbers:
            return 0, 0, 0, 0, 0
        
        total = sum(numbers)
        count = len(numbers)
        mean = total / count
        minimum = min(numbers)
        maximum = max(numbers)
        
        return count, total, mean, minimum, maximum
    
    stats = analyze_list([10, 20, 30, 40, 50])
    print(f"  Return tuple: {stats}")
    
    count, total, mean, min_val, max_val = analyze_list([10, 20, 30, 40, 50])
    print(f"  Unpacked: count={count}, total={total}, mean={mean:.1f}, min={min_val}, max={max_val}")
    
    # PRACTICAL: DIVMOD
    print("\n4. PRACTICAL: divmod() - Built-in multiple return")
    print("-" * 40)
    
    quotient, remainder = divmod(17, 5)
    print(f"  divmod(17, 5) = ({quotient}, {remainder})")
    print(f"  Check: {quotient} × 5 + {remainder} = {quotient * 5 + remainder}")
    
    # PRACTICAL: ENUMERATE
    print("\n5. PRACTICAL: enumerate() - Returns index-value pairs")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # PRACTICAL: DATETIME COMPONENTS
    print("\n6. PRACTICAL: Returning date components")
    print("-" * 40)
    
    def get_date_components(date_obj=None):
        """Return year, month, day as separate values."""
        if date_obj is None:
            date_obj = datetime.now()
        
        return date_obj.year, date_obj.month, date_obj.day
    
    year, month, day = get_date_components()
    print(f"  Today: {year}-{month}-{day}")
    
    # IGNORING SOME RETURN VALUES
    print("\n7. IGNORING UNUSED RETURN VALUES")
    print("-" * 40)
    
    # Use underscore for values to ignore
    _, total, mean, _, _ = analyze_list([10, 20, 30, 40, 50])
    print(f"  Total: {total}, Mean: {mean:.1f} (ignored count, min, max)")


def demonstrate_returning_complex_objects():
    """
    Demonstrates returning dictionaries, lists, and custom objects.
    
    Complex return values make functions more expressive and maintainable.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: RETURNING COMPLEX OBJECTS")
    print("=" * 60)
    
    # RETURNING DICTIONARIES
    print("\n1. RETURNING DICTIONARIES (self-documenting)")
    print("-" * 40)
    
    def analyze_user_data(users):
        """Return comprehensive user analytics as a dictionary."""
        if not users:
            return {
                "count": 0,
                "average_age": 0,
                "unique_cities": [],
                "active_count": 0
            }
        
        ages = [u.get("age", 0) for u in users]
        cities = {u.get("city") for u in users if u.get("city")}
        active = [u for u in users if u.get("is_active", False)]
        
        return {
            "count": len(users),
            "average_age": sum(ages) / len(ages) if ages else 0,
            "unique_cities": list(cities),
            "active_count": len(active),
            "active_percentage": (len(active) / len(users)) * 100
        }
    
    sample_users = [
        {"name": "Alice", "age": 28, "city": "NYC", "is_active": True},
        {"name": "Bob", "age": 35, "city": "LA", "is_active": True},
        {"name": "Charlie", "age": 42, "city": "NYC", "is_active": False}
    ]
    
    result = analyze_user_data(sample_users)
    print(f"  Analysis result:")
    for key, value in result.items():
        print(f"    {key}: {value}")
    
    # RETURNING LISTS
    print("\n2. RETURNING LISTS")
    print("-" * 40)
    
    def get_active_users(users):
        """Return list of active user names."""
        return [u["name"] for u in users if u.get("is_active", False)]
    
    active = get_active_users(sample_users)
    print(f"  Active users: {active}")
    
    # RETURNING CUSTOM OBJECTS (using dataclass)
    print("\n3. RETURNING CUSTOM OBJECTS (dataclass)")
    print("-" * 40)
    
    from dataclasses import dataclass
    
    @dataclass
    class ValidationResult:
        """Result of a validation operation."""
        is_valid: bool
        errors: List[str]
        warnings: List[str]
        validated_data: Optional[Dict] = None
        
        def __bool__(self):
            return self.is_valid
        
        def to_dict(self):
            return {
                "is_valid": self.is_valid,
                "errors": self.errors,
                "warnings": self.warnings,
                "validated_data": self.validated_data
            }
    
    def validate_user_data(data):
        """Validate user data and return rich result object."""
        errors = []
        warnings = []
        validated = {}
        
        # Validate name
        name = data.get("name", "")
        if not name:
            errors.append("Name is required")
        elif len(name) < 2:
            errors.append("Name must be at least 2 characters")
        else:
            validated["name"] = name.strip().title()
        
        # Validate age
        age = data.get("age")
        if age is None:
            errors.append("Age is required")
        elif not isinstance(age, (int, float)):
            errors.append("Age must be a number")
        elif age < 13:
            errors.append("Must be at least 13 years old")
        elif age > 120:
            warnings.append("Age seems unusually high")
            validated["age"] = age
        else:
            validated["age"] = age
        
        # Validate email
        email = data.get("email", "")
        if email and "@" not in email:
            errors.append("Invalid email format")
        elif email:
            validated["email"] = email
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            validated_data=validated if not errors else None
        )
    
    # Test validation
    test_data = {"name": "alice", "age": 150, "email": "invalid"}
    result = validate_user_data(test_data)
    
    print(f"  Input: {test_data}")
    print(f"  Is valid: {result.is_valid}")
    print(f"  Errors: {result.errors}")
    print(f"  Warnings: {result.warnings}")
    print(f"  Validated: {result.validated_data}")
    
    # RETURNING NONE
    print("\n4. RETURNING None (indicating no result)")
    print("-" * 40)
    
    def find_user_by_id(user_id, users):
        """Return user if found, None otherwise."""
        for user in users:
            if user.get("id") == user_id:
                return user
        return None
    
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    
    user = find_user_by_id(1, users)
    print(f"  find_user_by_id(1): {user}")
    
    user = find_user_by_id(99, users)
    print(f"  find_user_by_id(99): {user}")
    
    # Check for None
    if user is None:
        print("  User not found - handle appropriately")


def demonstrate_return_early_patterns():
    """
    Demonstrates early return patterns for cleaner code.
    
    Early returns reduce nesting and improve readability.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: EARLY RETURN PATTERNS")
    print("=" * 60)
    
    # WITHOUT EARLY RETURNS (Nested)
    print("\n1. WITHOUT EARLY RETURNS (Hard to read)")
    print("-" * 40)
    
    def process_order_bad(order):
        """Process order with nested conditions."""
        if order:
            if order.get("items"):
                if order.get("payment"):
                    if order.get("shipping"):
                        return "Order processed"
                    else:
                        return "Missing shipping"
                else:
                    return "Missing payment"
            else:
                return "No items"
        else:
            return "No order"
    
    result = process_order_bad({"items": [1], "payment": "card", "shipping": "address"})
    print(f"  Result: {result}")
    
    # WITH EARLY RETURNS (Clean)
    print("\n2. WITH EARLY RETURNS (Guard clauses)")
    print("-" * 40)
    
    def process_order_good(order):
        """Process order with guard clauses (early returns)."""
        if not order:
            return "No order"
        
        if not order.get("items"):
            return "No items"
        
        if not order.get("payment"):
            return "Missing payment"
        
        if not order.get("shipping"):
            return "Missing shipping"
        
        # All validations passed
        return "Order processed"
    
    result = process_order_good({"items": [1], "payment": "card", "shipping": "address"})
    print(f"  Result: {result}")
    
    # VALIDATION WITH EARLY RETURNS
    print("\n3. VALIDATION WITH EARLY RETURNS")
    print("-" * 40)
    
    def validate_registration(username, email, password, age):
        """Validate registration with early returns."""
        if not username or len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if "@" not in email:
            return False, "Invalid email address"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        if age < 13:
            return False, "Must be at least 13 years old"
        
        return True, "Registration valid"
    
    is_valid, message = validate_registration("alice", "alice@example.com", "password123", 25)
    print(f"  Valid registration: {is_valid} - {message}")
    
    is_valid, message = validate_registration("a", "invalid", "short", 10)
    print(f"  Invalid registration: {is_valid} - {message}")
    
    # CALCULATION WITH EARLY RETURN FOR EDGE CASES
    print("\n4. CALCULATION WITH EARLY RETURN")
    print("-" * 40)
    
    def calculate_average(numbers):
        """Calculate average with early return for empty list."""
        if not numbers:
            return 0.0
        
        return sum(numbers) / len(numbers)
    
    print(f"  average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")
    print(f"  average([]) = {calculate_average([])}")
    
    # RECURSIVE WITH EARLY RETURN (base case)
    print("\n5. RECURSIVE WITH EARLY RETURN")
    print("-" * 40)
    
    def factorial(n):
        """Calculate factorial with early return for base case."""
        if n <= 1:
            return 1
        
        return n * factorial(n - 1)
    
    print(f"  factorial(5) = {factorial(5)}")


if __name__ == "__main__":
    demonstrate_return_basics()
    demonstrate_multiple_return_values()
    demonstrate_returning_complex_objects()
    demonstrate_return_early_patterns()
```

---

## 🎯 Section 2: Result Pattern for Error Handling

The Result pattern provides a clean way to handle operations that can succeed or fail without using exceptions.

**SOLID Principle Applied: Single Responsibility** – Result objects separate success from error handling.

**Design Pattern: Result Pattern** – Encapsulates success/failure in a container object.

```python
"""
RESULT PATTERN FOR ERROR HANDLING

This section covers the Result pattern for handling operations
that can succeed or fail without using exceptions.

SOLID Principle: Single Responsibility
- Result objects separate success from error handling

Design Pattern: Result Pattern
- Encapsulates success/failure in a container
"""

from typing import TypeVar, Generic, Optional, Callable, Any, List, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

T = TypeVar('T')
E = TypeVar('E')


class Result(Generic[T, E]):
    """
    Result type representing either success (Ok) or failure (Err).
    
    This pattern is common in functional programming and provides
    explicit error handling without exceptions.
    """
    
    def __init__(self, is_ok: bool, value: Optional[T] = None, error: Optional[E] = None):
        self._is_ok = is_ok
        self._value = value
        self._error = error
    
    @classmethod
    def ok(cls, value: T) -> 'Result[T, E]':
        """Create a successful result."""
        return cls(True, value=value)
    
    @classmethod
    def err(cls, error: E) -> 'Result[T, E]':
        """Create a failed result."""
        return cls(False, error=error)
    
    def is_ok(self) -> bool:
        """Return True if result is successful."""
        return self._is_ok
    
    def is_err(self) -> bool:
        """Return True if result is failed."""
        return not self._is_ok
    
    def ok(self) -> Optional[T]:
        """Get the success value (or None if error)."""
        return self._value if self._is_ok else None
    
    def err(self) -> Optional[E]:
        """Get the error value (or None if success)."""
        return self._error if not self._is_ok else None
    
    def unwrap(self) -> T:
        """
        Get the success value or raise an exception.
        
        Use only when you're sure the result is Ok.
        """
        if self._is_ok:
            return self._value
        raise ValueError(f"Called unwrap on error result: {self._error}")
    
    def unwrap_or(self, default: T) -> T:
        """Get success value or return default."""
        return self._value if self._is_ok else default
    
    def unwrap_or_else(self, fallback: Callable[[E], T]) -> T:
        """Get success value or compute from error."""
        if self._is_ok:
            return self._value
        return fallback(self._error)
    
    def map(self, func: Callable[[T], Any]) -> 'Result[Any, E]':
        """Apply function to success value, preserving error."""
        if self._is_ok:
            return Result.ok(func(self._value))
        return Result.err(self._error)
    
    def map_err(self, func: Callable[[E], Any]) -> 'Result[T, Any]':
        """Apply function to error value."""
        if self._is_ok:
            return Result.ok(self._value)
        return Result.err(func(self._error))
    
    def and_then(self, func: Callable[[T], 'Result[Any, E]']) -> 'Result[Any, E]':
        """Apply function that returns a Result."""
        if self._is_ok:
            return func(self._value)
        return Result.err(self._error)
    
    def __repr__(self) -> str:
        if self._is_ok:
            return f"Ok({self._value})"
        return f"Err({self._error})"
    
    def __bool__(self) -> bool:
        return self._is_ok


@dataclass
class ValidationError:
    """Structured validation error."""
    field: str
    message: str
    code: str
    value: Any = None


@dataclass
class BusinessError:
    """Structured business error."""
    code: str
    message: str
    details: Optional[Dict] = None


def demonstrate_result_pattern():
    """
    Demonstrates the Result pattern for explicit error handling.
    """
    print("=" * 60)
    print("SECTION 2A: RESULT PATTERN BASICS")
    print("=" * 60)
    
    # CREATING RESULTS
    print("\n1. CREATING OK AND ERR RESULTS")
    print("-" * 40)
    
    success = Result.ok(42)
    failure = Result.err("Something went wrong")
    
    print(f"  Success: {success}")
    print(f"  Failure: {failure}")
    print(f"  success.is_ok(): {success.is_ok()}")
    print(f"  failure.is_err(): {failure.is_err()}")
    
    # ACCESSING VALUES
    print("\n2. ACCESSING VALUES SAFELY")
    print("-" * 40)
    
    value = success.ok()
    error = failure.err()
    
    print(f"  success.ok(): {value}")
    print(f"  failure.err(): {error}")
    
    # UNWRAPPING (with risk)
    print("\n3. UNWRAPPING VALUES")
    print("-" * 40)
    
    try:
        unwrapped = success.unwrap()
        print(f"  success.unwrap(): {unwrapped}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    try:
        unwrapped = failure.unwrap()
        print(f"  failure.unwrap(): {unwrapped}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    # UNWRAP_OR (safe with default)
    print("\n4. UNWRAP_OR (safe with default)")
    print("-" * 40)
    
    print(f"  success.unwrap_or(0): {success.unwrap_or(0)}")
    print(f"  failure.unwrap_or(0): {failure.unwrap_or(0)}")
    
    # MAPPING
    print("\n5. MAPPING OVER RESULTS")
    print("-" * 40)
    
    doubled = success.map(lambda x: x * 2)
    print(f"  success.map(lambda x: x * 2): {doubled}")
    
    # AND_THEN (chaining operations)
    print("\n6. CHAINING WITH AND_THEN")
    print("-" * 40)
    
    def divide(a: int, b: int) -> Result[int, str]:
        """Divide two numbers, returning Result."""
        if b == 0:
            return Result.err("Division by zero")
        return Result.ok(a // b)
    
    result = (Result.ok(10)
              .and_then(lambda x: divide(x, 2))
              .and_then(lambda x: divide(x, 5)))
    
    print(f"  Chain 10 / 2 / 5: {result}")
    
    result = (Result.ok(10)
              .and_then(lambda x: divide(x, 0))
              .and_then(lambda x: divide(x, 5)))
    
    print(f"  Chain with division by zero: {result}")


def demonstrate_result_validation():
    """
    Demonstrates using Result pattern for data validation.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: RESULT PATTERN FOR VALIDATION")
    print("=" * 60)
    
    def validate_username(username: str) -> Result[str, List[ValidationError]]:
        """Validate username, returning Result."""
        errors = []
        
        if not username:
            errors.append(ValidationError(
                field="username",
                message="Username is required",
                code="REQUIRED"
            ))
        elif len(username) < 3:
            errors.append(ValidationError(
                field="username",
                message="Username must be at least 3 characters",
                code="TOO_SHORT",
                value=username
            ))
        elif len(username) > 20:
            errors.append(ValidationError(
                field="username",
                message="Username cannot exceed 20 characters",
                code="TOO_LONG",
                value=username
            ))
        elif not username[0].isalpha():
            errors.append(ValidationError(
                field="username",
                message="Username must start with a letter",
                code="INVALID_START",
                value=username
            ))
        
        if errors:
            return Result.err(errors)
        
        return Result.ok(username)
    
    def validate_email(email: str) -> Result[str, List[ValidationError]]:
        """Validate email, returning Result."""
        errors = []
        
        if not email:
            errors.append(ValidationError(
                field="email",
                message="Email is required",
                code="REQUIRED"
            ))
        elif "@" not in email:
            errors.append(ValidationError(
                field="email",
                message="Email must contain @ symbol",
                code="INVALID_FORMAT",
                value=email
            ))
        elif email.count("@") > 1:
            errors.append(ValidationError(
                field="email",
                message="Email cannot have multiple @ symbols",
                code="INVALID_FORMAT",
                value=email
            ))
        
        if errors:
            return Result.err(errors)
        
        return Result.ok(email)
    
    def validate_age(age: int) -> Result[int, List[ValidationError]]:
        """Validate age, returning Result."""
        errors = []
        
        if age < 13:
            errors.append(ValidationError(
                field="age",
                message="Must be at least 13 years old",
                code="TOO_YOUNG",
                value=age
            ))
        elif age > 120:
            errors.append(ValidationError(
                field="age",
                message="Age seems unrealistic",
                code="TOO_OLD",
                value=age
            ))
        
        if errors:
            return Result.err(errors)
        
        return Result.ok(age)
    
    def validate_user(name: str, email: str, age: int) -> Result[Dict, List[ValidationError]]:
        """
        Validate complete user using Result chaining.
        """
        all_errors = []
        
        # Validate each field
        name_result = validate_username(name)
        if name_result.is_err():
            all_errors.extend(name_result.err())
        
        email_result = validate_email(email)
        if email_result.is_err():
            all_errors.extend(email_result.err())
        
        age_result = validate_age(age)
        if age_result.is_err():
            all_errors.extend(age_result.err())
        
        if all_errors:
            return Result.err(all_errors)
        
        return Result.ok({
            "username": name_result.ok(),
            "email": email_result.ok(),
            "age": age_result.ok()
        })
    
    # TEST VALIDATION
    print("\n1. VALIDATING VALID USER")
    print("-" * 40)
    
    result = validate_user("alice_wonder", "alice@example.com", 25)
    
    if result.is_ok():
        print(f"  ✅ Valid: {result.ok()}")
    else:
        print(f"  ❌ Errors: {result.err()}")
    
    print("\n2. VALIDATING INVALID USER")
    print("-" * 40)
    
    result = validate_user("a", "invalid", 10)
    
    if result.is_ok():
        print(f"  ✅ Valid: {result.ok()}")
    else:
        print(f"  ❌ Errors:")
        for error in result.err():
            print(f"    - {error.field}: {error.message} (code: {error.code})")
    
    print("\n3. USING RESULT IN BUSINESS LOGIC")
    print("-" * 40)
    
    def register_user(name: str, email: str, age: int) -> Result[Dict, List[ValidationError]]:
        """Register user with validation."""
        # Validate first
        validation = validate_user(name, email, age)
        if validation.is_err():
            return Result.err(validation.err())
        
        # Simulate user creation
        user_data = validation.ok()
        user_data["id"] = 1001
        user_data["registered_at"] = datetime.now().isoformat()
        
        return Result.ok(user_data)
    
    # Successful registration
    result = register_user("alice", "alice@example.com", 25)
    if result.is_ok():
        print(f"  ✅ Registration successful: {result.ok()['username']}")
        print(f"     User ID: {result.ok()['id']}")
    
    # Failed registration
    result = register_user("a", "invalid", 10)
    if result.is_err():
        print(f"  ❌ Registration failed:")
        for error in result.err():
            print(f"     - {error.field}: {error.message}")


def demonstrate_business_result():
    """
    Demonstrates using Result pattern for business operations.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: RESULT PATTERN FOR BUSINESS LOGIC")
    print("=" * 60)
    
    from dataclasses import dataclass
    from typing import Optional
    
    @dataclass
    class User:
        """User entity."""
        id: int
        name: str
        email: str
        balance: float
    
    @dataclass
    class Order:
        """Order entity."""
        id: str
        user_id: int
        amount: float
        status: str
    
    class AccountService:
        """Account service with Result-based operations."""
        
        def __init__(self):
            self.users = {
                1: User(1, "Alice", "alice@example.com", 1000.00),
                2: User(2, "Bob", "bob@example.com", 500.00),
                3: User(3, "Charlie", "charlie@example.com", 100.00)
            }
            self.orders = []
            self.next_order_id = 1000
        
        def get_user(self, user_id: int) -> Result[User, BusinessError]:
            """Get user by ID."""
            user = self.users.get(user_id)
            if not user:
                return Result.err(BusinessError(
                    code="USER_NOT_FOUND",
                    message=f"User with ID {user_id} not found"
                ))
            return Result.ok(user)
        
        def check_balance(self, user: User, amount: float) -> Result[float, BusinessError]:
            """Check if user has sufficient balance."""
            if amount <= 0:
                return Result.err(BusinessError(
                    code="INVALID_AMOUNT",
                    message=f"Amount must be positive: {amount}"
                ))
            
            if user.balance < amount:
                return Result.err(BusinessError(
                    code="INSUFFICIENT_FUNDS",
                    message=f"Insufficient funds. Balance: ${user.balance:.2f}, Required: ${amount:.2f}"
                ))
            
            return Result.ok(user.balance - amount)
        
        def process_payment(self, user: User, amount: float) -> Result[float, BusinessError]:
            """Process payment and return new balance."""
            # Check balance first
            check_result = self.check_balance(user, amount)
            if check_result.is_err():
                return Result.err(check_result.err())
            
            # Process payment
            new_balance = user.balance - amount
            user.balance = new_balance
            
            return Result.ok(new_balance)
        
        def create_order(self, user_id: int, amount: float) -> Result[Order, BusinessError]:
            """Create an order for a user."""
            # Get user
            user_result = self.get_user(user_id)
            if user_result.is_err():
                return Result.err(user_result.err())
            
            user = user_result.ok()
            
            # Process payment
            payment_result = self.process_payment(user, amount)
            if payment_result.is_err():
                return Result.err(payment_result.err())
            
            # Create order
            order_id = f"ORD-{self.next_order_id}"
            self.next_order_id += 1
            
            order = Order(
                id=order_id,
                user_id=user_id,
                amount=amount,
                status="completed"
            )
            self.orders.append(order)
            
            return Result.ok(order)
        
        def transfer_funds(self, from_user_id: int, to_user_id: int, amount: float) -> Result[Dict, BusinessError]:
            """Transfer funds between users."""
            # Get source user
            from_result = self.get_user(from_user_id)
            if from_result.is_err():
                return Result.err(from_result.err())
            
            # Get destination user
            to_result = self.get_user(to_user_id)
            if to_result.is_err():
                return Result.err(to_result.err())
            
            from_user = from_result.ok()
            to_user = to_result.ok()
            
            # Process withdrawal
            withdraw_result = self.process_payment(from_user, amount)
            if withdraw_result.is_err():
                return Result.err(withdraw_result.err())
            
            # Process deposit
            to_user.balance += amount
            
            return Result.ok({
                "from_user": from_user.id,
                "to_user": to_user.id,
                "amount": amount,
                "from_balance": from_user.balance,
                "to_balance": to_user.balance
            })
    
    # DEMONSTRATION
    print("\n💰 ACCOUNT SERVICE DEMONSTRATION")
    print("-" * 40)
    
    service = AccountService()
    
    # Successful order creation
    print("\n1. CREATING ORDER (SUCCESSFUL)")
    print("-" * 30)
    
    result = service.create_order(user_id=1, amount=150.00)
    
    if result.is_ok():
        order = result.ok()
        print(f"  ✅ Order created: {order.id}")
        print(f"     Amount: ${order.amount:.2f}")
        print(f"     Status: {order.status}")
        print(f"     New balance for user 1: ${service.users[1].balance:.2f}")
    else:
        error = result.err()
        print(f"  ❌ Failed: {error.code} - {error.message}")
    
    # Failed order (insufficient funds)
    print("\n2. CREATING ORDER (INSUFFICIENT FUNDS)")
    print("-" * 30)
    
    result = service.create_order(user_id=3, amount=200.00)
    
    if result.is_ok():
        order = result.ok()
        print(f"  ✅ Order created: {order.id}")
    else:
        error = result.err()
        print(f"  ❌ Failed: {error.code} - {error.message}")
    
    # Failed order (user not found)
    print("\n3. CREATING ORDER (USER NOT FOUND)")
    print("-" * 30)
    
    result = service.create_order(user_id=99, amount=50.00)
    
    if result.is_ok():
        order = result.ok()
        print(f"  ✅ Order created: {order.id}")
    else:
        error = result.err()
        print(f"  ❌ Failed: {error.code} - {error.message}")
    
    # Transfer funds
    print("\n4. TRANSFER FUNDS")
    print("-" * 30)
    
    print(f"  Before transfer:")
    print(f"    User 1 balance: ${service.users[1].balance:.2f}")
    print(f"    User 2 balance: ${service.users[2].balance:.2f}")
    
    result = service.transfer_funds(from_user_id=1, to_user_id=2, amount=100.00)
    
    if result.is_ok():
        transfer = result.ok()
        print(f"  ✅ Transfer successful: ${transfer['amount']:.2f}")
        print(f"  After transfer:")
        print(f"    User 1 balance: ${transfer['from_balance']:.2f}")
        print(f"    User 2 balance: ${transfer['to_balance']:.2f}")
    else:
        error = result.err()
        print(f"  ❌ Transfer failed: {error.code} - {error.message}")


if __name__ == "__main__":
    demonstrate_result_pattern()
    demonstrate_result_validation()
    demonstrate_business_result()
```

---

## 📊 Section 3: API Response Formatter

A complete API response formatter that standardizes success and error responses across an application.

**SOLID Principles Applied:**
- Single Responsibility: Each formatter handles one response type
- Open/Closed: New response types can be added

**Design Patterns:**
- Factory Pattern: Creates response objects
- Builder Pattern: Builds responses incrementally

```python
"""
API RESPONSE FORMATTER

This section builds a complete API response formatter that standardizes
success and error responses across an application.

SOLID Principles Applied:
- Single Responsibility: Each formatter handles one response type
- Open/Closed: New response types can be added

Design Patterns:
- Factory Pattern: Creates response objects
- Builder Pattern: Builds responses incrementally
"""

from typing import Dict, Any, Optional, List, Union, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
import uuid


class ResponseStatus(Enum):
    """API response status types."""
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class APIResponse:
    """
    Standardized API response format.
    
    All API responses follow this structure for consistency.
    """
    status: ResponseStatus
    message: str
    data: Optional[Any] = None
    errors: Optional[List[Dict]] = None
    warnings: Optional[List[str]] = None
    meta: Optional[Dict] = None
    request_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        """Convert response to dictionary."""
        result = {
            "status": self.status.value,
            "message": self.message,
            "request_id": self.request_id,
            "timestamp": self.timestamp
        }
        
        if self.data is not None:
            result["data"] = self.data
        
        if self.errors:
            result["errors"] = self.errors
        
        if self.warnings:
            result["warnings"] = self.warnings
        
        if self.meta:
            result["meta"] = self.meta
        
        return result
    
    def to_json(self, indent: int = 2) -> str:
        """Convert response to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)
    
    def __str__(self) -> str:
        return self.to_json()


class ResponseBuilder:
    """
    Builder for creating API responses.
    
    Design Pattern: Builder Pattern - Builds responses incrementally
    """
    
    def __init__(self):
        self._status = ResponseStatus.SUCCESS
        self._message = ""
        self._data = None
        self._errors = []
        self._warnings = []
        self._meta = {}
    
    def success(self, message: str) -> 'ResponseBuilder':
        """Set response as success."""
        self._status = ResponseStatus.SUCCESS
        self._message = message
        return self
    
    def error(self, message: str) -> 'ResponseBuilder':
        """Set response as error."""
        self._status = ResponseStatus.ERROR
        self._message = message
        return self
    
    def warning(self, message: str) -> 'ResponseBuilder':
        """Set response as warning."""
        self._status = ResponseStatus.WARNING
        self._message = message
        return self
    
    def info(self, message: str) -> 'ResponseBuilder':
        """Set response as info."""
        self._status = ResponseStatus.INFO
        self._message = message
        return self
    
    def data(self, data: Any) -> 'ResponseBuilder':
        """Add data to response."""
        self._data = data
        return self
    
    def add_error(self, error: Union[str, Dict]) -> 'ResponseBuilder':
        """Add an error to response."""
        if isinstance(error, str):
            self._errors.append({"message": error})
        else:
            self._errors.append(error)
        return self
    
    def add_warning(self, warning: str) -> 'ResponseBuilder':
        """Add a warning to response."""
        self._warnings.append(warning)
        return self
    
    def meta(self, key: str, value: Any) -> 'ResponseBuilder':
        """Add metadata to response."""
        self._meta[key] = value
        return self
    
    def pagination(self, page: int, per_page: int, total: int) -> 'ResponseBuilder':
        """Add pagination metadata."""
        total_pages = (total + per_page - 1) // per_page if per_page > 0 else 0
        
        self._meta["pagination"] = {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_previous": page > 1
        }
        return self
    
    def build(self) -> APIResponse:
        """Build the final APIResponse object."""
        return APIResponse(
            status=self._status,
            message=self._message,
            data=self._data,
            errors=self._errors if self._errors else None,
            warnings=self._warnings if self._warnings else None,
            meta=self._meta if self._meta else None
        )


class APIResponseFactory:
    """
    Factory for creating common API responses.
    
    Design Pattern: Factory Pattern - Creates standard responses
    """
    
    @staticmethod
    def ok(data: Any = None, message: str = "Operation successful") -> APIResponse:
        """Create a standard success response."""
        return ResponseBuilder().success(message).data(data).build()
    
    @staticmethod
    def created(data: Any = None, message: str = "Resource created successfully") -> APIResponse:
        """Create a creation success response."""
        return ResponseBuilder().success(message).data(data).meta("created", True).build()
    
    @staticmethod
    def deleted(message: str = "Resource deleted successfully") -> APIResponse:
        """Create a deletion success response."""
        return ResponseBuilder().success(message).meta("deleted", True).build()
    
    @staticmethod
    def bad_request(message: str = "Bad request", errors: Optional[List] = None) -> APIResponse:
        """Create a bad request error response."""
        builder = ResponseBuilder().error(message)
        if errors:
            for error in errors:
                builder.add_error(error)
        return builder.build()
    
    @staticmethod
    def unauthorized(message: str = "Unauthorized access") -> APIResponse:
        """Create an unauthorized error response."""
        return ResponseBuilder().error(message).meta("code", "UNAUTHORIZED").build()
    
    @staticmethod
    def forbidden(message: str = "Access forbidden") -> APIResponse:
        """Create a forbidden error response."""
        return ResponseBuilder().error(message).meta("code", "FORBIDDEN").build()
    
    @staticmethod
    def not_found(resource: str = "Resource") -> APIResponse:
        """Create a not found error response."""
        return ResponseBuilder().error(f"{resource} not found").meta("code", "NOT_FOUND").build()
    
    @staticmethod
    def conflict(message: str = "Resource conflict") -> APIResponse:
        """Create a conflict error response."""
        return ResponseBuilder().error(message).meta("code", "CONFLICT").build()
    
    @staticmethod
    def validation_error(errors: List[Dict]) -> APIResponse:
        """Create a validation error response."""
        builder = ResponseBuilder().error("Validation failed")
        for error in errors:
            builder.add_error(error)
        return builder.meta("code", "VALIDATION_ERROR").build()
    
    @staticmethod
    def internal_error(message: str = "Internal server error") -> APIResponse:
        """Create an internal server error response."""
        return ResponseBuilder().error(message).meta("code", "INTERNAL_ERROR").build()
    
    @staticmethod
    def paginated(data: List, page: int, per_page: int, total: int, message: str = "Success") -> APIResponse:
        """Create a paginated success response."""
        return (ResponseBuilder()
                .success(message)
                .data(data)
                .pagination(page, per_page, total)
                .build())


class ErrorCodes:
    """Standard error codes for the application."""
    
    VALIDATION_ERROR = "VALIDATION_ERROR"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    AUTHORIZATION_ERROR = "AUTHORIZATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    CONFLICT = "CONFLICT"
    RATE_LIMIT = "RATE_LIMIT"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    BUSINESS_RULE_VIOLATION = "BUSINESS_RULE_VIOLATION"


def demonstrate_api_response_formatter():
    """
    Demonstrate the API response formatter with examples.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: API RESPONSE FORMATTER")
    print("=" * 60)
    
    # SUCCESS RESPONSES
    print("\n1. SUCCESS RESPONSES")
    print("-" * 40)
    
    # Simple success
    response = APIResponseFactory.ok({"user": {"id": 1, "name": "Alice"}})
    print(f"  OK Response: {response.to_json()[:100]}...")
    
    # Created response
    response = APIResponseFactory.created({"id": 100, "name": "New User"})
    print(f"  Created Response: {response.to_json()[:100]}...")
    
    # Paginated response
    data = [{"id": i, "name": f"User {i}"} for i in range(1, 26)]
    response = APIResponseFactory.paginated(data[:10], page=1, per_page=10, total=25)
    print(f"  Paginated Response: {response.to_json()[:150]}...")
    
    # ERROR RESPONSES
    print("\n2. ERROR RESPONSES")
    print("-" * 40)
    
    # Bad request
    response = APIResponseFactory.bad_request("Invalid input", ["Email is required", "Password too short"])
    print(f"  Bad Request: {response.to_json()[:150]}...")
    
    # Not found
    response = APIResponseFactory.not_found("User")
    print(f"  Not Found: {response.to_json()}")
    
    # Validation error
    errors = [
        {"field": "email", "message": "Invalid email format", "code": "INVALID_EMAIL"},
        {"field": "age", "message": "Must be at least 13", "code": "TOO_YOUNG"}
    ]
    response = APIResponseFactory.validation_error(errors)
    print(f"  Validation Error: {response.to_json()}")
    
    # USING RESPONSE BUILDER
    print("\n3. USING RESPONSE BUILDER (Custom responses)")
    print("-" * 40)
    
    response = (ResponseBuilder()
                .warning("Rate limit approaching")
                .data({"remaining": 950, "limit": 1000})
                .add_warning("50 requests remaining this hour")
                .meta("reset_time", "2024-01-01T00:00:00Z")
                .build())
    
    print(f"  Warning Response: {response.to_json()}")
    
    # COMPLETE API HANDLER EXAMPLE
    print("\n4. COMPLETE API HANDLER EXAMPLE")
    print("-" * 40)
    
    class UserAPIHandler:
        """Example API handler using response formatter."""
        
        def __init__(self):
            self.users = {
                1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
                2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
            }
        
        def get_user(self, user_id: int) -> APIResponse:
            """Get user by ID."""
            user = self.users.get(user_id)
            if not user:
                return APIResponseFactory.not_found(f"User {user_id}")
            
            return APIResponseFactory.ok(user)
        
        def create_user(self, data: Dict) -> APIResponse:
            """Create a new user."""
            # Validation
            errors = []
            if not data.get("name"):
                errors.append({"field": "name", "message": "Name is required"})
            if not data.get("email"):
                errors.append({"field": "email", "message": "Email is required"})
            elif "@" not in data["email"]:
                errors.append({"field": "email", "message": "Invalid email format"})
            
            if errors:
                return APIResponseFactory.validation_error(errors)
            
            # Check for duplicate email
            for user in self.users.values():
                if user["email"] == data["email"]:
                    return APIResponseFactory.conflict("Email already exists")
            
            # Create user
            new_id = max(self.users.keys()) + 1
            new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
            self.users[new_id] = new_user
            
            return APIResponseFactory.created(new_user)
        
        def list_users(self, page: int = 1, per_page: int = 10) -> APIResponse:
            """List users with pagination."""
            users_list = list(self.users.values())
            total = len(users_list)
            
            start = (page - 1) * per_page
            end = start + per_page
            paginated_users = users_list[start:end]
            
            return APIResponseFactory.paginated(paginated_users, page, per_page, total)
    
    # Test the API handler
    handler = UserAPIHandler()
    
    print("  GET /users/1:")
    response = handler.get_user(1)
    print(f"    {response.to_json()}")
    
    print("\n  GET /users/99:")
    response = handler.get_user(99)
    print(f"    {response.to_json()}")
    
    print("\n  POST /users (valid):")
    response = handler.create_user({"name": "Charlie", "email": "charlie@example.com"})
    print(f"    {response.to_json()}")
    
    print("\n  POST /users (invalid):")
    response = handler.create_user({"name": ""})
    print(f"    {response.to_json()}")
    
    print("\n  GET /users (paginated):")
    response = handler.list_users(page=1, per_page=10)
    data = response.to_dict()
    print(f"    Total: {data['meta']['pagination']['total']}")
    print(f"    Page: {data['meta']['pagination']['page']}")


if __name__ == "__main__":
    demonstrate_api_response_formatter()
```

---

## 🏭 Section 4: Complete Order Processing with Structured Returns

A complete order processing system demonstrating structured return values using the Result pattern and API response formatter.

**SOLID Principles Applied:**
- Single Responsibility: Each processing step has one responsibility
- Dependency Inversion: Depends on abstractions (Result, APIResponse)

**Design Patterns:**
- Pipeline Pattern: Order flows through processing stages
- Result Pattern: Explicit success/failure handling

```python
"""
COMPLETE ORDER PROCESSING WITH STRUCTURED RETURNS

This section builds a complete order processing system using
structured return values and the Result pattern.

SOLID Principles Applied:
- Single Responsibility: Each processing step has one responsibility
- Dependency Inversion: Depends on abstractions

Design Patterns:
- Pipeline Pattern: Order flows through processing stages
- Result Pattern: Explicit success/failure handling
"""

from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import random
import uuid


class OrderStatus(Enum):
    """Order status values."""
    PENDING = "pending"
    VALIDATED = "validated"
    PAYMENT_PROCESSED = "payment_processed"
    INVENTORY_RESERVED = "inventory_reserved"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    FAILED = "failed"


@dataclass
class OrderItem:
    """Individual order item."""
    product_id: str
    name: str
    quantity: int
    unit_price: float
    
    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Customer:
    """Customer information."""
    id: str
    name: str
    email: str
    tier: str  # bronze, silver, gold, platinum
    address: str


@dataclass
class Order:
    """Complete order with all details."""
    order_id: str
    customer: Customer
    items: List[OrderItem]
    subtotal: float
    discount: float
    tax: float
    shipping: float
    total: float
    status: OrderStatus
    created_at: datetime
    payment_transaction_id: Optional[str] = None
    tracking_number: Optional[str] = None
    errors: List[str] = field(default_factory=list)


class OrderError:
    """Structured order processing errors."""
    
    def __init__(self, code: str, message: str, step: str, details: Optional[Dict] = None):
        self.code = code
        self.message = message
        self.step = step
        self.details = details or {}
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "code": self.code,
            "message": self.message,
            "step": self.step,
            "details": self.details,
            "timestamp": self.timestamp.isoformat()
        }


class OrderResult:
    """
    Result of order processing operation.
    
    Design Pattern: Result Pattern - Encapsulates success/failure
    """
    
    def __init__(self, success: bool, order: Optional[Order] = None, error: Optional[OrderError] = None):
        self.success = success
        self.order = order
        self.error = error
    
    @classmethod
    def success(cls, order: Order) -> 'OrderResult':
        return cls(True, order=order)
    
    @classmethod
    def failure(cls, error: OrderError) -> 'OrderResult':
        return cls(False, error=error)
    
    def is_success(self) -> bool:
        return self.success
    
    def is_failure(self) -> bool:
        return not self.success
    
    def get_order(self) -> Optional[Order]:
        return self.order
    
    def get_error(self) -> Optional[OrderError]:
        return self.error
    
    def to_response(self) -> Dict:
        """Convert to API response format."""
        if self.success:
            return {
                "success": True,
                "order_id": self.order.order_id,
                "status": self.order.status.value,
                "total": self.order.total,
                "message": f"Order {self.order.order_id} processed successfully"
            }
        else:
            return {
                "success": False,
                "error": self.error.to_dict(),
                "message": self.error.message
            }


class OrderCalculator:
    """
    Order calculation service.
    
    Design Pattern: Strategy Pattern - Different calculation strategies
    """
    
    @staticmethod
    def calculate_subtotal(items: List[OrderItem]) -> float:
        """Calculate order subtotal."""
        return sum(item.subtotal() for item in items)
    
    @staticmethod
    def calculate_discount(subtotal: float, customer_tier: str, coupon_code: Optional[str] = None) -> Tuple[float, str]:
        """Calculate discount based on tier and coupon."""
        # Tier discounts
        tier_discounts = {
            "bronze": 0.00,
            "silver": 0.05,
            "gold": 0.10,
            "platinum": 0.15
        }
        
        discount_percent = tier_discounts.get(customer_tier, 0.00)
        reason = f"{customer_tier.capitalize()} tier discount"
        
        # Coupon discount
        if coupon_code:
            coupon_discounts = {
                "SAVE10": 0.10,
                "SAVE20": 0.20,
                "WELCOME": 0.15
            }
            if coupon_code in coupon_discounts:
                discount_percent += coupon_discounts[coupon_code]
                reason += f" + coupon {coupon_code}"
        
        # Cap at 25%
        discount_percent = min(discount_percent, 0.25)
        discount_amount = subtotal * discount_percent
        
        return round(discount_amount, 2), reason
    
    @staticmethod
    def calculate_tax(subtotal: float, discount: float, tax_rate: float = 0.08) -> float:
        """Calculate tax on discounted subtotal."""
        taxable = subtotal - discount
        return round(taxable * tax_rate, 2)
    
    @staticmethod
    def calculate_shipping(subtotal: float, items_count: int, customer_tier: str) -> Tuple[float, str]:
        """Calculate shipping cost."""
        # Free shipping conditions
        if subtotal >= 100:
            return 0.00, "Free shipping (order over $100)"
        
        if customer_tier == "platinum":
            return 0.00, "Free shipping (platinum member)"
        
        # Standard rates
        if items_count <= 2:
            return 5.99, "Standard shipping"
        elif items_count <= 5:
            return 8.99, "Standard shipping"
        else:
            return 12.99, "Express shipping"


class OrderValidator:
    """
    Order validation service.
    
    Design Pattern: Chain of Responsibility - Multiple validation steps
    """
    
    @staticmethod
    def validate_items(items: List[OrderItem]) -> Optional[OrderError]:
        """Validate order items."""
        if not items:
            return OrderError(
                code="EMPTY_ORDER",
                message="Order must contain at least one item",
                step="validation"
            )
        
        for item in items:
            if item.quantity <= 0:
                return OrderError(
                    code="INVALID_QUANTITY",
                    message=f"Invalid quantity for {item.name}: {item.quantity}",
                    step="validation",
                    details={"product": item.product_id, "quantity": item.quantity}
                )
            
            if item.unit_price <= 0:
                return OrderError(
                    code="INVALID_PRICE",
                    message=f"Invalid price for {item.name}: ${item.unit_price}",
                    step="validation",
                    details={"product": item.product_id, "price": item.unit_price}
                )
        
        return None
    
    @staticmethod
    def validate_customer(customer: Customer) -> Optional[OrderError]:
        """Validate customer information."""
        if not customer.name:
            return OrderError(
                code="INVALID_CUSTOMER",
                message="Customer name is required",
                step="validation"
            )
        
        if not customer.email or "@" not in customer.email:
            return OrderError(
                code="INVALID_EMAIL",
                message=f"Invalid email address: {customer.email}",
                step="validation"
            )
        
        if not customer.address:
            return OrderError(
                code="NO_ADDRESS",
                message="Shipping address is required",
                step="validation"
            )
        
        return None


class PaymentService:
    """
    Payment processing service.
    
    Design Pattern: Adapter Pattern - Adapts payment gateway
    """
    
    @staticmethod
    def process_payment(order_id: str, amount: float, payment_method: str) -> Tuple[bool, Optional[str], Optional[OrderError]]:
        """
        Process payment for order.
        
        Returns:
            Tuple of (success, transaction_id, error)
        """
        # Simulate payment processing
        if payment_method not in ["credit_card", "paypal", "cash"]:
            return False, None, OrderError(
                code="INVALID_PAYMENT_METHOD",
                message=f"Unsupported payment method: {payment_method}",
                step="payment",
                details={"method": payment_method}
            )
        
        # Simulate success/failure (95% success)
        if random.random() < 0.95:
            transaction_id = f"TXN-{uuid.uuid4().hex[:12].upper()}"
            return True, transaction_id, None
        else:
            return False, None, OrderError(
                code="PAYMENT_DECLINED",
                message="Payment was declined. Please try another payment method.",
                step="payment"
            )


class InventoryService:
    """
    Inventory management service.
    """
    
    def __init__(self):
        # Simulated inventory
        self.inventory = {
            "PROD-001": {"name": "Laptop", "stock": 10},
            "PROD-002": {"name": "Mouse", "stock": 50},
            "PROD-003": {"name": "Keyboard", "stock": 25},
            "PROD-004": {"name": "Monitor", "stock": 5},
            "PROD-005": {"name": "USB Cable", "stock": 100}
        }
    
    def reserve_inventory(self, items: List[OrderItem]) -> Tuple[bool, Optional[OrderError]]:
        """
        Reserve inventory for order items.
        
        Returns:
            Tuple of (success, error)
        """
        out_of_stock = []
        
        for item in items:
            if item.product_id in self.inventory:
                if self.inventory[item.product_id]["stock"] < item.quantity:
                    out_of_stock.append({
                        "product": item.product_id,
                        "name": item.name,
                        "requested": item.quantity,
                        "available": self.inventory[item.product_id]["stock"]
                    })
            else:
                out_of_stock.append({
                    "product": item.product_id,
                    "name": item.name,
                    "requested": item.quantity,
                    "available": 0
                })
        
        if out_of_stock:
            return False, OrderError(
                code="OUT_OF_STOCK",
                message="Some items are out of stock",
                step="inventory",
                details={"out_of_stock": out_of_stock}
            )
        
        # Reserve inventory (decrease stock)
        for item in items:
            self.inventory[item.product_id]["stock"] -= item.quantity
        
        return True, None


class ShippingService:
    """
    Shipping service.
    """
    
    @staticmethod
    def create_shipment(order_id: str, address: str, items: List[OrderItem]) -> Tuple[bool, Optional[str], Optional[OrderError]]:
        """
        Create shipment for order.
        
        Returns:
            Tuple of (success, tracking_number, error)
        """
        # Simulate shipment creation
        tracking_number = f"TRK-{uuid.uuid4().hex[:8].upper()}"
        
        # Simulate success (98% success)
        if random.random() < 0.98:
            return True, tracking_number, None
        else:
            return False, None, OrderError(
                code="SHIPPING_FAILED",
                message="Unable to create shipment. Please contact support.",
                step="shipping"
            )


class OrderProcessor:
    """
    Complete order processing pipeline.
    
    Design Pattern: Pipeline Pattern - Order flows through processing stages
    """
    
    def __init__(self):
        self.calculator = OrderCalculator()
        self.validator = OrderValidator()
        self.payment_service = PaymentService()
        self.inventory_service = InventoryService()
        self.shipping_service = ShippingService()
        self.order_counter = 1000
    
    def process_order(
        self,
        customer: Customer,
        items: List[OrderItem],
        payment_method: str,
        coupon_code: Optional[str] = None
    ) -> OrderResult:
        """
        Process an order through all stages.
        
        Each stage returns a structured result, allowing
        graceful failure handling.
        """
        # Generate order ID
        self.order_counter += 1
        order_id = f"ORD-{self.order_counter}"
        
        # STAGE 1: Validation
        item_error = self.validator.validate_items(items)
        if item_error:
            return OrderResult.failure(item_error)
        
        customer_error = self.validator.validate_customer(customer)
        if customer_error:
            return OrderResult.failure(customer_error)
        
        # STAGE 2: Calculate amounts
        subtotal = self.calculator.calculate_subtotal(items)
        discount, discount_reason = self.calculator.calculate_discount(subtotal, customer.tier, coupon_code)
        tax = self.calculator.calculate_tax(subtotal, discount)
        shipping, shipping_method = self.calculator.calculate_shipping(subtotal, len(items), customer.tier)
        total = subtotal - discount + tax + shipping
        
        # Create order object
        order = Order(
            order_id=order_id,
            customer=customer,
            items=items,
            subtotal=round(subtotal, 2),
            discount=discount,
            tax=tax,
            shipping=shipping,
            total=round(total, 2),
            status=OrderStatus.PENDING,
            created_at=datetime.now()
        )
        
        # STAGE 3: Reserve inventory
        inventory_success, inventory_error = self.inventory_service.reserve_inventory(items)
        if not inventory_success:
            order.status = OrderStatus.FAILED
            order.errors.append(inventory_error.message)
            return OrderResult.failure(inventory_error)
        
        order.status = OrderStatus.INVENTORY_RESERVED
        
        # STAGE 4: Process payment
        payment_success, transaction_id, payment_error = self.payment_service.process_payment(
            order_id, total, payment_method
        )
        
        if not payment_success:
            order.status = OrderStatus.FAILED
            order.errors.append(payment_error.message)
            return OrderResult.failure(payment_error)
        
        order.payment_transaction_id = transaction_id
        order.status = OrderStatus.PAYMENT_PROCESSED
        
        # STAGE 5: Create shipment
        shipping_success, tracking_number, shipping_error = self.shipping_service.create_shipment(
            order_id, customer.address, items
        )
        
        if not shipping_success:
            order.status = OrderStatus.FAILED
            order.errors.append(shipping_error.message)
            return OrderResult.failure(shipping_error)
        
        order.tracking_number = tracking_number
        order.status = OrderStatus.SHIPPED
        
        return OrderResult.success(order)


def demonstrate_order_processing():
    """
    Demonstrate the complete order processing system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: COMPLETE ORDER PROCESSING")
    print("=" * 60)
    
    processor = OrderProcessor()
    
    # Create test customer
    customer = Customer(
        id="CUST-001",
        name="Alice Chen",
        email="alice@example.com",
        tier="gold",
        address="123 Main St, New York, NY 10001"
    )
    
    # Create test items
    items = [
        OrderItem("PROD-001", "Laptop", 1, 999.99),
        OrderItem("PROD-002", "Mouse", 2, 29.99),
        OrderItem("PROD-003", "Keyboard", 1, 89.99)
    ]
    
    print("\n1. PROCESSING SUCCESSFUL ORDER")
    print("-" * 40)
    
    result = processor.process_order(
        customer=customer,
        items=items,
        payment_method="credit_card",
        coupon_code="SAVE10"
    )
    
    print(f"  Result: {'✅ SUCCESS' if result.is_success() else '❌ FAILED'}")
    
    if result.is_success():
        order = result.get_order()
        print(f"  Order ID: {order.order_id}")
        print(f"  Status: {order.status.value}")
        print(f"  Subtotal: ${order.subtotal:.2f}")
        print(f"  Discount: -${order.discount:.2f}")
        print(f"  Tax: +${order.tax:.2f}")
        print(f"  Shipping: +${order.shipping:.2f}")
        print(f"  Total: ${order.total:.2f}")
        print(f"  Tracking: {order.tracking_number}")
    
    print("\n2. PROCESSING ORDER WITH OUT OF STOCK ITEM")
    print("-" * 40)
    
    items_with_out_of_stock = [
        OrderItem("PROD-004", "Monitor", 10, 299.99),  # Only 5 in stock
        OrderItem("PROD-002", "Mouse", 1, 29.99)
    ]
    
    result = processor.process_order(
        customer=customer,
        items=items_with_out_of_stock,
        payment_method="credit_card"
    )
    
    print(f"  Result: {'✅ SUCCESS' if result.is_success() else '❌ FAILED'}")
    
    if result.is_failure():
        error = result.get_error()
        print(f"  Error Code: {error.code}")
        print(f"  Error Message: {error.message}")
        print(f"  Failed at: {error.step}")
        if error.details:
            print(f"  Details: {error.details}")
    
    print("\n3. PROCESSING ORDER WITH INVALID PAYMENT")
    print("-" * 40)
    
    # Force payment failure by using invalid method
    result = processor.process_order(
        customer=customer,
        items=items,
        payment_method="invalid_method"
    )
    
    print(f"  Result: {'✅ SUCCESS' if result.is_success() else '❌ FAILED'}")
    
    if result.is_failure():
        error = result.get_error()
        print(f"  Error Code: {error.code}")
        print(f"  Error Message: {error.message}")
        print(f"  Failed at: {error.step}")
    
    print("\n4. PROCESSING ORDER WITH EMPTY CART")
    print("-" * 40)
    
    result = processor.process_order(
        customer=customer,
        items=[],
        payment_method="credit_card"
    )
    
    print(f"  Result: {'✅ SUCCESS' if result.is_success() else '❌ FAILED'}")
    
    if result.is_failure():
        error = result.get_error()
        print(f"  Error Code: {error.code}")
        print(f"  Error Message: {error.message}")
    
    # API Response conversion
    print("\n5. CONVERTING TO API RESPONSE")
    print("-" * 40)
    
    result = processor.process_order(
        customer=customer,
        items=items,
        payment_method="credit_card",
        coupon_code="SAVE10"
    )
    
    api_response = result.to_response()
    print(f"  API Response: {api_response}")


if __name__ == "__main__":
    demonstrate_order_processing()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Return Statement** – Exits function and returns value. Returns None if no return specified.

- **Single Return Values** – Functions can return any type: int, str, bool, list, dict, objects.

- **Multiple Return Values** – Return multiple values as tuples. Unpack with `a, b = func()`.

- **Complex Return Objects** – Dictionaries and dataclasses make return values self-documenting.

- **Early Returns** – Guard clauses reduce nesting and improve readability. Check invalid conditions first.

- **Result Pattern** – Encapsulate success/failure in container. Explicit error handling without exceptions.

- **Validation Results** – Return detailed validation errors with field names and codes.

- **API Response Formatter** – Standardize success and error responses. Builder pattern for flexible construction.

- **Order Processing** – Complete pipeline with structured returns at each stage. Graceful failure handling.

- **SOLID Principles Applied** – Single Responsibility (each function returns one type of result), Open/Closed (new result types can be added), Dependency Inversion (depends on Result abstraction).

- **Design Patterns Used** – Result Pattern (explicit success/failure), Builder Pattern (response construction), Factory Pattern (standard responses), Pipeline Pattern (processing stages), Chain of Responsibility (validation chain).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Arguments – Positional, Keyword, and Default

- **📚 Series B Catalog:** Functions & Modules Yard – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful (Series B, Story 4)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 3 | 3 | 50% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **15** | **37** | **29%** |

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

**Next Story:** Series B, Story 4: The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful

---

## 📝 Your Invitation

You've mastered return values. Now build something with what you've learned:

1. **Build a Result class** – Implement map, and_then, unwrap_or methods. Use it for database operations.

2. **Create an API response formatter** – Add more response types (accepted, no_content, see_other). Add rate limiting headers.

3. **Build a validation library** – Return structured validation results with field-level errors. Compose validators.

4. **Create an order processing system** – Add more stages (fraud detection, tax calculation by region). Use Result pattern throughout.

5. **Build a data fetching service** – Return Result types for API calls, database queries, file operations.

**You've mastered return values. Next stop: Lambda Functions!**

---

*Found this helpful? Clap, comment, and share what you built with structured returns. Next stop: Lambda Functions!* 🚇