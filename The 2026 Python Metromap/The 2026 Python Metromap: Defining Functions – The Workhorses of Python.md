# The 2026 Python Metromap: Defining Functions – The Workhorses of Python

## Series B: Functions & Modules Yard | Story 1 of 6

![The 2026 Python Metromap/images/Defining Functions – The Workhorses of Python](images/Defining Functions – The Workhorses of Python.png)

## 📖 Introduction

**Welcome to the first stop on the Functions & Modules Yard Line.**

You've completed Foundations Station. You've mastered variables, collections, operators, control flow, loops, nested logic, and input/output. You can write programs that store data, make decisions, repeat operations, and talk to users. But as your programs grow, you'll notice something: you're writing the same code over and over.

That's where functions come in.

Functions are the workhorses of Python. They let you encapsulate reusable logic into named blocks that you can call whenever you need them. Instead of writing the same validation code ten times, you write it once in a function and call it ten times. Instead of copying and pasting calculation logic, you define a function and reuse it. Functions make your code DRY (Don't Repeat Yourself), organized, testable, and maintainable.

This story—**The 2026 Python Metromap: Defining Functions – The Workhorses of Python**—is your guide to creating and using functions. We'll build a complete payment processing module with validation, logging, and error handling functions. We'll create data validation functions that can be reused across multiple forms. We'll build a string processing utility library. And we'll implement a complete order processing system that demonstrates how functions organize complex business logic.

**Let's start building reusable code.**

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

- 🔧 **The 2026 Python Metromap: Defining Functions – The Workhorses of Python** – Payment processing module; validation functions; error handling. **⬅️ YOU ARE HERE**

- 📋 **The 2026 Python Metromap: Arguments – Positional, Keyword, and Default** – Flexible report generator for PDF, CSV, and JSON outputs. 🔜 *Up Next*

- 📤 **The 2026 Python Metromap: Return Values – Getting Results Back** – API response formatter; standardized success and error responses.

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines.

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver.

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔧 Section 1: Function Basics – Defining and Calling

A function is a reusable block of code that performs a specific task. You define it once with `def`, then call it whenever you need that behavior.

**SOLID Principle Applied: Single Responsibility** – Each function should do exactly one thing and do it well.

**Design Pattern: Command Pattern** – Functions encapsulate commands that can be executed on demand.

```python
"""
FUNCTION BASICS: DEFINING AND CALLING

This section covers the fundamentals of creating and using functions.

SOLID Principle: Single Responsibility
- Each function does exactly one thing

Design Pattern: Command Pattern
- Functions encapsulate commands that can be executed
"""

from typing import Any, Optional
import time


def demonstrate_function_basics():
    """
    Demonstrates basic function definition and calling.
    
    A function is defined with the 'def' keyword, followed by the
    function name, parentheses, and a colon. The body is indented.
    """
    print("=" * 60)
    print("SECTION 1A: FUNCTION BASICS")
    print("=" * 60)
    
    # SIMPLE FUNCTION (no parameters, no return)
    print("\n1. SIMPLE FUNCTION (no parameters, no return)")
    print("-" * 40)
    
    def greet():
        """Print a greeting message."""
        print("  Hello, welcome to Python functions!")
    
    # Call the function
    greet()
    greet()  # Can call multiple times
    
    # FUNCTION WITH PARAMETERS
    print("\n2. FUNCTION WITH PARAMETERS")
    print("-" * 40)
    
    def greet_person(name):
        """Greet a specific person."""
        print(f"  Hello, {name}!")
    
    greet_person("Alice")
    greet_person("Bob")
    greet_person("Charlie")
    
    # FUNCTION WITH MULTIPLE PARAMETERS
    print("\n3. FUNCTION WITH MULTIPLE PARAMETERS")
    print("-" * 40)
    
    def introduce(name, age, city):
        """Introduce a person with their details."""
        print(f"  {name} is {age} years old and lives in {city}.")
    
    introduce("Alice", 28, "New York")
    introduce("Bob", 35, "Los Angeles")
    
    # FUNCTION WITH RETURN VALUE
    print("\n4. FUNCTION WITH RETURN VALUE")
    print("-" * 40)
    
    def add(a, b):
        """Add two numbers and return the result."""
        result = a + b
        return result
    
    sum_result = add(5, 3)
    print(f"  add(5, 3) = {sum_result}")
    
    # Return value can be used directly
    print(f"  add(10, 20) = {add(10, 20)}")
    
    # FUNCTION WITH MULTIPLE RETURN VALUES (using tuples)
    print("\n5. FUNCTION WITH MULTIPLE RETURN VALUES")
    print("-" * 40)
    
    def get_min_max(numbers):
        """Return both minimum and maximum from a list."""
        if not numbers:
            return None, None
        return min(numbers), max(numbers)
    
    min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2])
    print(f"  Min: {min_val}, Max: {max_val}")
    
    # FUNCTION DOCSTRINGS (documentation)
    print("\n6. FUNCTION DOCSTRINGS")
    print("-" * 40)
    
    def calculate_area(length, width):
        """
        Calculate the area of a rectangle.
        
        Args:
            length: The length of the rectangle
            width: The width of the rectangle
            
        Returns:
            The area (length * width)
        """
        return length * width
    
    # Access docstring
    print(f"  Docstring: {calculate_area.__doc__}")
    print(f"  Help: {help(calculate_area)}")
    
    # FUNCTION WITH TYPE HINTS (annotations)
    print("\n7. FUNCTION WITH TYPE HINTS")
    print("-" * 40)
    
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    result = multiply(3.5, 2.0)
    print(f"  multiply(3.5, 2.0) = {result}")
    print(f"  Return type: {type(result).__name__}")
    
    # FUNCTION WITH DEFAULT ARGUMENTS (preview)
    print("\n8. FUNCTION WITH DEFAULT ARGUMENTS")
    print("-" * 40)
    
    def greet_with_title(name, title="Mr."):
        """Greet with optional title."""
        print(f"  Hello, {title} {name}!")
    
    greet_with_title("Smith")           # Uses default title
    greet_with_title("Smith", "Dr.")    # Overrides default
    
    # FUNCTION CALLING ANOTHER FUNCTION
    print("\n9. FUNCTION COMPOSITION")
    print("-" * 40)
    
    def square(x):
        """Square a number."""
        return x * x
    
    def sum_of_squares(a, b):
        """Calculate a² + b²."""
        return square(a) + square(b)
    
    result = sum_of_squares(3, 4)
    print(f"  sum_of_squares(3, 4) = {result} (3² + 4² = 9 + 16 = 25)")
    
    # EMPTY FUNCTION (using pass)
    print("\n10. EMPTY FUNCTION (placeholder)")
    print("-" * 40)
    
    def not_implemented_yet():
        """Placeholder for future implementation."""
        pass  # Does nothing, allows empty function
    
    not_implemented_yet()
    print("  Function with 'pass' - does nothing but is valid syntax")


def demonstrate_scope():
    """
    Demonstrates variable scope in functions.
    
    Variables defined inside a function are local to that function.
    Variables defined outside are global.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: VARIABLE SCOPE")
    print("=" * 60)
    
    # LOCAL VARIABLES
    print("\n1. LOCAL VARIABLES")
    print("-" * 40)
    
    def local_example():
        x = 10  # Local variable - only exists inside this function
        print(f"  Inside function: x = {x}")
    
    local_example()
    # print(x)  # This would cause NameError - x doesn't exist here
    
    print("  Local variables cannot be accessed outside their function")
    
    # GLOBAL VARIABLES
    print("\n2. GLOBAL VARIABLES")
    print("-" * 40)
    
    global_var = 100  # Global variable - accessible everywhere
    
    def read_global():
        """Functions can READ global variables."""
        print(f"  Reading global_var: {global_var}")
    
    def modify_global_bad():
        """This creates a LOCAL variable with the same name."""
        global_var = 200  # This is LOCAL, not modifying the global!
        print(f"  Inside modify_global_bad: global_var = {global_var}")
    
    def modify_global_good():
        """Use 'global' keyword to modify global variable."""
        global global_var
        global_var = 200
        print(f"  Inside modify_global_good: global_var = {global_var}")
    
    read_global()
    modify_global_bad()
    read_global()  # Still 100 - not changed!
    modify_global_good()
    read_global()  # Now 200 - changed!
    
    print("\n  ⚠️ Avoid modifying global variables when possible")
    print("     Use parameters and return values instead")
    
    # ENCLOSING SCOPE (for nested functions)
    print("\n3. ENCLOSING SCOPE (Nested functions)")
    print("-" * 40)
    
    def outer_function():
        """Outer function with its own variable."""
        outer_var = "I'm from outer"
        
        def inner_function():
            """Inner function can read outer variables."""
            print(f"  Inner function sees: {outer_var}")
        
        inner_function()
    
    outer_function()
    
    # NONLOCAL KEYWORD (modify enclosing variables)
    print("\n4. NONLOCAL KEYWORD")
    print("-" * 40)
    
    def counter():
        """Function that returns a counter function."""
        count = 0
        
        def increment():
            nonlocal count  # Allows modification of enclosing variable
            count += 1
            return count
        
        return increment
    
    my_counter = counter()
    print(f"  Count: {my_counter()}")
    print(f"  Count: {my_counter()}")
    print(f"  Count: {my_counter()}")
    
    # SCOPE RULES (LEGB)
    print("\n5. LEGB RULE (Local, Enclosing, Global, Built-in)")
    print("-" * 40)
    
    # Python looks for variables in this order:
    # 1. Local - inside the current function
    # 2. Enclosing - in outer functions (if nested)
    # 3. Global - at the module level
    # 4. Built-in - Python's built-in names (print, len, etc.)
    
    x = "global"
    
    def outer():
        x = "enclosing"
        
        def inner():
            x = "local"
            print(f"  Local x: {x}")
        
        inner()
        print(f"  Enclosing x: {x}")
    
    outer()
    print(f"  Global x: {x}")
    print(f"  Built-in len: {len([1, 2, 3])}")


def demonstrate_function_best_practices():
    """
    Demonstrates best practices for writing functions.
    
    Good functions are:
    - Small and focused (do one thing)
    - Have descriptive names
    - Have docstrings
    - Avoid side effects when possible
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: FUNCTION BEST PRACTICES")
    print("=" * 60)
    
    # BEST PRACTICE 1: Descriptive names
    print("\n1. USE DESCRIPTIVE NAMES")
    print("-" * 40)
    
    # Bad
    def f(x, y):
        return x + y
    
    # Good
    def calculate_total(price, tax):
        return price + tax
    
    print("  ✓ Function names should be verbs or verb phrases")
    print("  ✓ Names should describe what the function does")
    
    # BEST PRACTICE 2: Small and focused
    print("\n2. SINGLE RESPONSIBILITY (One thing per function)")
    print("-" * 40)
    
    # Bad - does too many things
    def process_order_bad(order):
        validate_order(order)
        calculate_total(order)
        apply_discount(order)
        process_payment(order)
        send_confirmation(order)
        update_inventory(order)
    
    # Good - each step is its own function
    def validate_order(order): pass
    def calculate_total(order): pass
    def apply_discount(order): pass
    def process_payment(order): pass
    def send_confirmation(order): pass
    def update_inventory(order): pass
    
    print("  ✓ Each function should do ONE thing")
    print("  ✓ Functions should be small (under 20-30 lines)")
    
    # BEST PRACTICE 3: Avoid side effects
    print("\n3. AVOID SIDE EFFECTS")
    print("-" * 40)
    
    # Bad - modifies input list
    def add_item_bad(cart, item):
        cart.append(item)  # Side effect!
        return len(cart)
    
    # Good - returns new list (pure function)
    def add_item_good(cart, item):
        new_cart = cart.copy()
        new_cart.append(item)
        return new_cart
    
    cart = ["apple", "banana"]
    result = add_item_good(cart, "cherry")
    print(f"  Original cart: {cart} (unchanged)")
    print(f"  New cart: {result}")
    
    # BEST PRACTICE 4: Use docstrings
    print("\n4. ALWAYS WRITE DOCSTRINGS")
    print("-" * 40)
    
    def celsius_to_fahrenheit(celsius):
        """
        Convert Celsius to Fahrenheit.
        
        Args:
            celsius: Temperature in Celsius
            
        Returns:
            Temperature in Fahrenheit
            
        Example:
            >>> celsius_to_fahrenheit(0)
            32.0
            >>> celsius_to_fahrenheit(100)
            212.0
        """
        return celsius * 9/5 + 32
    
    print(f"  Docstring: {celsius_to_fahrenheit.__doc__[:50]}...")
    
    # BEST PRACTICE 5: Use type hints
    print("\n5. USE TYPE HINTS")
    print("-" * 40)
    
    def divide(dividend: float, divisor: float) -> float:
        """Divide two numbers."""
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor
    
    print("  Type hints make code more readable and catch errors early")
    
    # BEST PRACTICE 6: Handle errors gracefully
    print("\n6. HANDLE ERRORS GRACEFULLY")
    print("-" * 40)
    
    def safe_divide(a, b):
        """
        Safely divide two numbers, returning None on error.
        """
        try:
            return a / b
        except ZeroDivisionError:
            print("  Warning: Division by zero")
            return None
        except TypeError:
            print("  Warning: Invalid types for division")
            return None
    
    print(f"  safe_divide(10, 2) = {safe_divide(10, 2)}")
    print(f"  safe_divide(10, 0) = {safe_divide(10, 0)}")
    print(f"  safe_divide(10, 'a') = {safe_divide(10, 'a')}")
    
    # BEST PRACTICE 7: Use constants for magic numbers
    print("\n7. USE CONSTANTS FOR MAGIC NUMBERS")
    print("-" * 40)
    
    # Bad
    def calculate_discount_bad(price):
        return price * 0.1  # What is 0.1?
    
    # Good
    DISCOUNT_RATE = 0.10
    
    def calculate_discount_good(price):
        """Calculate 10% discount."""
        return price * DISCOUNT_RATE
    
    print("  Named constants make code self-documenting")


def build_payment_processor():
    """
    Complete payment processing module using functions.
    
    This demonstrates a real-world payment processing system
    with validation, logging, and error handling functions.
    
    SOLID Principles Applied:
    - Single Responsibility: Each function has one purpose
    - Open/Closed: New payment methods can be added
    
    Design Patterns:
    - Command Pattern: Payment operations as functions
    - Factory Pattern: Creates payment processor instances
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: PAYMENT PROCESSING MODULE")
    print("=" * 60)
    
    from typing import Dict, Any, Tuple, Optional
    from datetime import datetime
    import re
    import random
    
    # ==========================================================================
    # VALIDATION FUNCTIONS
    # ==========================================================================
    
    def validate_credit_card(number: str) -> Tuple[bool, str]:
        """
        Validate credit card number using Luhn algorithm.
        
        Args:
            number: Credit card number as string
            
        Returns:
            Tuple of (is_valid, card_type)
        """
        # Remove spaces and dashes
        number = re.sub(r'[\s\-]', '', number)
        
        if not number.isdigit():
            return False, "Invalid: contains non-digits"
        
        if len(number) < 13 or len(number) > 19:
            return False, "Invalid: wrong length"
        
        # Detect card type
        card_patterns = {
            "Visa": r'^4[0-9]{12}(?:[0-9]{3})?$',
            "Mastercard": r'^5[1-5][0-9]{14}$|^2(?:2[2-9][0-9]{12}|[3-6][0-9]{13})$',
            "Amex": r'^3[47][0-9]{13}$',
            "Discover": r'^6(?:011|5[0-9]{2})[0-9]{12}$'
        }
        
        card_type = "Unknown"
        for name, pattern in card_patterns.items():
            if re.match(pattern, number):
                card_type = name
                break
        
        # Luhn algorithm check
        def luhn_check(card_num):
            total = 0
            reverse_digits = card_num[::-1]
            
            for i, digit in enumerate(reverse_digits):
                n = int(digit)
                if i % 2 == 1:  # Every other digit from the right
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n
            
            return total % 10 == 0
        
        if not luhn_check(number):
            return False, f"Invalid {card_type}: fails checksum"
        
        return True, card_type
    
    def validate_expiry_date(month: int, year: int) -> Tuple[bool, str]:
        """
        Validate credit card expiry date.
        
        Args:
            month: Expiry month (1-12)
            year: Expiry year (YYYY)
            
        Returns:
            Tuple of (is_valid, message)
        """
        if month < 1 or month > 12:
            return False, "Invalid month (must be 1-12)"
        
        if year < 2024 or year > 2040:
            return False, "Invalid year (must be 2024-2040)"
        
        now = datetime.now()
        if year < now.year or (year == now.year and month < now.month):
            return False, "Card has expired"
        
        return True, "Valid"
    
    def validate_cvv(cvv: str, card_type: str) -> Tuple[bool, str]:
        """
        Validate CVV code.
        
        Args:
            cvv: CVV code
            card_type: Type of card (for length validation)
            
        Returns:
            Tuple of (is_valid, message)
        """
        if not cvv.isdigit():
            return False, "CVV must contain only digits"
        
        expected_length = 4 if card_type == "Amex" else 3
        
        if len(cvv) != expected_length:
            return False, f"CVV must be {expected_length} digits for {card_type}"
        
        return True, "Valid"
    
    def validate_amount(amount: float) -> Tuple[bool, str]:
        """
        Validate payment amount.
        
        Args:
            amount: Payment amount
            
        Returns:
            Tuple of (is_valid, message)
        """
        if amount <= 0:
            return False, "Amount must be positive"
        
        if amount > 100000:
            return False, "Amount exceeds maximum ($100,000)"
        
        # Check for more than 2 decimal places
        if round(amount, 2) != amount:
            return False, "Amount cannot have more than 2 decimal places"
        
        return True, "Valid"
    
    # ==========================================================================
    # LOGGING FUNCTIONS
    # ==========================================================================
    
    LOG_LEVELS = {
        "INFO": 0,
        "WARNING": 1,
        "ERROR": 2,
        "DEBUG": 3
    }
    
    current_log_level = "INFO"
    transaction_log: List[Dict] = []
    
    def log_transaction(level: str, message: str, data: Optional[Dict] = None) -> None:
        """
        Log a transaction event.
        
        Args:
            level: Log level (INFO, WARNING, ERROR, DEBUG)
            message: Log message
            data: Optional additional data
        """
        if LOG_LEVELS.get(level, 0) < LOG_LEVELS.get(current_log_level, 0):
            return
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            "data": data or {}
        }
        transaction_log.append(log_entry)
        
        # Print to console for demo
        print(f"  [{level}] {message}")
    
    def get_transaction_log() -> List[Dict]:
        """Get the complete transaction log."""
        return transaction_log.copy()
    
    def clear_log() -> None:
        """Clear the transaction log."""
        transaction_log.clear()
        print("  Log cleared")
    
    # ==========================================================================
    # PAYMENT PROCESSING FUNCTIONS
    # ==========================================================================
    
    def process_credit_card_payment(
        card_number: str,
        expiry_month: int,
        expiry_year: int,
        cvv: str,
        amount: float,
        currency: str = "USD"
    ) -> Tuple[bool, str, Optional[str]]:
        """
        Process a credit card payment.
        
        Args:
            card_number: Credit card number
            expiry_month: Expiry month (1-12)
            expiry_year: Expiry year (YYYY)
            cvv: CVV code
            amount: Payment amount
            currency: Currency code (default USD)
            
        Returns:
            Tuple of (success, message, transaction_id)
        """
        log_transaction("INFO", f"Processing {currency} {amount:.2f} payment")
        
        # Validate amount
        amount_valid, amount_msg = validate_amount(amount)
        if not amount_valid:
            log_transaction("ERROR", f"Amount validation failed: {amount_msg}")
            return False, amount_msg, None
        
        # Validate card
        card_valid, card_type = validate_credit_card(card_number)
        if not card_valid:
            log_transaction("ERROR", f"Card validation failed: {card_type}")
            return False, card_type, None
        
        # Validate expiry
        expiry_valid, expiry_msg = validate_expiry_date(expiry_month, expiry_year)
        if not expiry_valid:
            log_transaction("ERROR", f"Expiry validation failed: {expiry_msg}")
            return False, expiry_msg, None
        
        # Validate CVV
        cvv_valid, cvv_msg = validate_cvv(cvv, card_type)
        if not cvv_valid:
            log_transaction("ERROR", f"CVV validation failed: {cvv_msg}")
            return False, cvv_msg, None
        
        # Simulate payment processing (in real system, call payment gateway)
        log_transaction("INFO", f"Contacting payment gateway for {card_type}...")
        
        # Simulate success/failure (95% success rate)
        import random
        if random.random() < 0.95:
            transaction_id = f"TXN-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            log_transaction("INFO", f"Payment successful! Transaction ID: {transaction_id}")
            return True, "Payment approved", transaction_id
        else:
            log_transaction("ERROR", "Payment declined by gateway")
            return False, "Payment declined", None
    
    def process_paypal_payment(
        email: str,
        amount: float,
        currency: str = "USD"
    ) -> Tuple[bool, str, Optional[str]]:
        """
        Process a PayPal payment.
        
        Args:
            email: PayPal account email
            amount: Payment amount
            currency: Currency code
            
        Returns:
            Tuple of (success, message, transaction_id)
        """
        log_transaction("INFO", f"Processing PayPal payment of {currency} {amount:.2f}")
        
        # Validate email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            log_transaction("ERROR", f"Invalid email format: {email}")
            return False, "Invalid email address", None
        
        # Validate amount
        amount_valid, amount_msg = validate_amount(amount)
        if not amount_valid:
            log_transaction("ERROR", f"Amount validation failed: {amount_msg}")
            return False, amount_msg, None
        
        # Simulate PayPal processing
        if random.random() < 0.95:
            transaction_id = f"PYPL-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            log_transaction("INFO", f"PayPal payment successful! Transaction ID: {transaction_id}")
            return True, "Payment approved", transaction_id
        else:
            log_transaction("ERROR", "PayPal payment failed")
            return False, "Payment failed", None
    
    def process_cash_payment(
        amount: float,
        cash_received: float,
        currency: str = "USD"
    ) -> Tuple[bool, str, Optional[float]]:
        """
        Process a cash payment.
        
        Args:
            amount: Amount due
            cash_received: Cash received from customer
            currency: Currency code
            
        Returns:
            Tuple of (success, message, change)
        """
        log_transaction("INFO", f"Processing cash payment of {currency} {amount:.2f}")
        
        if cash_received < amount:
            shortfall = amount - cash_received
            log_transaction("ERROR", f"Insufficient cash: short by {currency} {shortfall:.2f}")
            return False, f"Insufficient cash. Need {currency} {shortfall:.2f} more", None
        
        change = cash_received - amount
        log_transaction("INFO", f"Cash payment successful. Change: {currency} {change:.2f}")
        return True, "Payment complete", change
    
    # ==========================================================================
    # UTILITY FUNCTIONS
    # ==========================================================================
    
    def format_currency(amount: float, currency: str = "USD") -> str:
        """
        Format amount as currency string.
        
        Args:
            amount: Amount to format
            currency: Currency code
            
        Returns:
            Formatted currency string
        """
        symbols = {
            "USD": "$",
            "EUR": "€",
            "GBP": "£",
            "JPY": "¥",
            "CAD": "C$"
        }
        symbol = symbols.get(currency, currency)
        return f"{symbol}{amount:,.2f}"
    
    def calculate_tax(amount: float, tax_rate: float = 0.08) -> float:
        """
        Calculate tax amount.
        
        Args:
            amount: Pre-tax amount
            tax_rate: Tax rate (default 8%)
            
        Returns:
            Tax amount
        """
        return round(amount * tax_rate, 2)
    
    def calculate_total_with_tax(amount: float, tax_rate: float = 0.08) -> float:
        """
        Calculate total including tax.
        
        Args:
            amount: Pre-tax amount
            tax_rate: Tax rate
            
        Returns:
            Total with tax
        """
        return amount + calculate_tax(amount, tax_rate)
    
    # ==========================================================================
    # DEMONSTRATION
    # ==========================================================================
    
    print("\n💳 PAYMENT PROCESSING DEMONSTRATION")
    print("-" * 40)
    
    # Test credit card payment
    print("\n1. CREDIT CARD PAYMENT")
    print("-" * 40)
    
    success, message, transaction_id = process_credit_card_payment(
        card_number="4111111111111111",  # Test Visa number
        expiry_month=12,
        expiry_year=2026,
        cvv="123",
        amount=299.99
    )
    
    print(f"\n  Result: {'✅ SUCCESS' if success else '❌ FAILED'}")
    print(f"  Message: {message}")
    if transaction_id:
        print(f"  Transaction ID: {transaction_id}")
    
    # Test PayPal payment
    print("\n2. PAYPAL PAYMENT")
    print("-" * 40)
    
    success, message, transaction_id = process_paypal_payment(
        email="customer@example.com",
        amount=149.99
    )
    
    print(f"\n  Result: {'✅ SUCCESS' if success else '❌ FAILED'}")
    print(f"  Message: {message}")
    if transaction_id:
        print(f"  Transaction ID: {transaction_id}")
    
    # Test cash payment
    print("\n3. CASH PAYMENT")
    print("-" * 40)
    
    success, message, change = process_cash_payment(
        amount=89.99,
        cash_received=100.00
    )
    
    print(f"\n  Result: {'✅ SUCCESS' if success else '❌ FAILED'}")
    print(f"  Message: {message}")
    if change is not None:
        print(f"  Change: {format_currency(change)}")
    
    # Show transaction log
    print("\n4. TRANSACTION LOG")
    print("-" * 40)
    
    log = get_transaction_log()
    print(f"  Total log entries: {len(log)}")
    for entry in log[-5:]:  # Last 5 entries
        print(f"    {entry['timestamp'][11:19]} [{entry['level']}] {entry['message'][:50]}")
    
    # Utility functions demo
    print("\n5. UTILITY FUNCTIONS")
    print("-" * 40)
    
    subtotal = 100.00
    tax = calculate_tax(subtotal)
    total = calculate_total_with_tax(subtotal)
    
    print(f"  Subtotal: {format_currency(subtotal)}")
    print(f"  Tax (8%): {format_currency(tax)}")
    print(f"  Total: {format_currency(total)}")


if __name__ == "__main__":
    demonstrate_function_basics()
    demonstrate_scope()
    demonstrate_function_best_practices()
    build_payment_processor()
```

---

## 🔧 Section 2: Data Validation Functions

Reusable validation functions that can be used across multiple forms and data entry points.

**SOLID Principles Applied:**
- Single Responsibility: Each validation function validates one thing
- Open/Closed: New validation rules can be added

**Design Pattern: Strategy Pattern** – Validation strategies can be composed and reused

```python
"""
DATA VALIDATION FUNCTIONS

This section builds reusable validation functions for common data types.

SOLID Principles Applied:
- Single Responsibility: Each validator handles one data type
- Open/Closed: New validators can be added

Design Pattern: Strategy Pattern
- Validation strategies can be composed
"""

from typing import Any, Dict, List, Optional, Tuple, Callable
from datetime import datetime, date
import re


class ValidationResult:
    """
    Result of a validation operation.
    
    Encapsulates success/failure and error messages.
    """
    
    def __init__(self, is_valid: bool, errors: Optional[List[str]] = None):
        self.is_valid = is_valid
        self.errors = errors or []
    
    def add_error(self, error: str) -> 'ValidationResult':
        """Add an error message."""
        self.errors.append(error)
        self.is_valid = False
        return self
    
    def __bool__(self) -> bool:
        return self.is_valid
    
    def __str__(self) -> str:
        if self.is_valid:
            return "Valid"
        return f"Invalid: {', '.join(self.errors)}"


class Validators:
    """
    Collection of reusable validation functions.
    
    Design Pattern: Strategy Pattern - Each validator is a strategy
    """
    
    @staticmethod
    def required(value: Any, field_name: str = "Field") -> ValidationResult:
        """
        Validate that a value is not empty/None.
        
        Args:
            value: Value to validate
            field_name: Name of the field for error messages
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        if value is None:
            return result.add_error(f"{field_name} is required")
        
        if isinstance(value, str) and not value.strip():
            return result.add_error(f"{field_name} cannot be empty")
        
        if isinstance(value, (list, dict, set)) and len(value) == 0:
            return result.add_error(f"{field_name} cannot be empty")
        
        return result
    
    @staticmethod
    def min_length(value: str, min_len: int, field_name: str = "Field") -> ValidationResult:
        """
        Validate minimum string length.
        
        Args:
            value: String to validate
            min_len: Minimum required length
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        if len(value) < min_len:
            return result.add_error(f"{field_name} must be at least {min_len} characters")
        
        return result
    
    @staticmethod
    def max_length(value: str, max_len: int, field_name: str = "Field") -> ValidationResult:
        """
        Validate maximum string length.
        
        Args:
            value: String to validate
            max_len: Maximum allowed length
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        if len(value) > max_len:
            return result.add_error(f"{field_name} cannot exceed {max_len} characters")
        
        return result
    
    @staticmethod
    def pattern(value: str, pattern: str, field_name: str = "Field") -> ValidationResult:
        """
        Validate string against regex pattern.
        
        Args:
            value: String to validate
            pattern: Regular expression pattern
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        if not re.match(pattern, value):
            return result.add_error(f"{field_name} has invalid format")
        
        return result
    
    @staticmethod
    def email(value: str, field_name: str = "Email") -> ValidationResult:
        """
        Validate email address format.
        
        Args:
            value: Email address to validate
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        # Basic required check
        required_result = Validators.required(value, field_name)
        if not required_result.is_valid:
            return required_result
        
        # Email pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value):
            return result.add_error(f"{field_name} must be a valid email address")
        
        return result
    
    @staticmethod
    def phone(value: str, field_name: str = "Phone") -> ValidationResult:
        """
        Validate phone number format.
        
        Args:
            value: Phone number to validate
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        if not value:  # Phone is optional
            return result
        
        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)\.]', '', value)
        
        if not cleaned.isdigit():
            return result.add_error(f"{field_name} must contain only digits")
        
        if len(cleaned) < 10 or len(cleaned) > 15:
            return result.add_error(f"{field_name} must be 10-15 digits")
        
        return result
    
    @staticmethod
    def age(value: Any, min_age: int = 13, max_age: int = 120, field_name: str = "Age") -> ValidationResult:
        """
        Validate age.
        
        Args:
            value: Age value (can be int or string)
            min_age: Minimum allowed age
            max_age: Maximum allowed age
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        # Convert string to int if needed
        if isinstance(value, str):
            if not value.isdigit():
                return result.add_error(f"{field_name} must be a number")
            value = int(value)
        
        if not isinstance(value, (int, float)):
            return result.add_error(f"{field_name} must be a number")
        
        if value < min_age:
            return result.add_error(f"Must be at least {min_age} years old")
        
        if value > max_age:
            return result.add_error(f"{field_name} seems unrealistic")
        
        return result
    
    @staticmethod
    def range(value: Any, min_val: float, max_val: float, field_name: str = "Value") -> ValidationResult:
        """
        Validate numeric range.
        
        Args:
            value: Numeric value
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        try:
            num = float(value)
        except (ValueError, TypeError):
            return result.add_error(f"{field_name} must be a number")
        
        if num < min_val:
            return result.add_error(f"{field_name} must be at least {min_val}")
        
        if num > max_val:
            return result.add_error(f"{field_name} cannot exceed {max_val}")
        
        return result
    
    @staticmethod
    def one_of(value: Any, options: List[Any], field_name: str = "Field") -> ValidationResult:
        """
        Validate that value is one of the allowed options.
        
        Args:
            value: Value to validate
            options: List of allowed values
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        if value not in options:
            options_str = ", ".join(str(opt) for opt in options)
            return result.add_error(f"{field_name} must be one of: {options_str}")
        
        return result
    
    @staticmethod
    def date_format(value: str, fmt: str = "%Y-%m-%d", field_name: str = "Date") -> ValidationResult:
        """
        Validate date string format.
        
        Args:
            value: Date string to validate
            fmt: Expected date format
            field_name: Name of the field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        try:
            datetime.strptime(value, fmt)
        except ValueError:
            return result.add_error(f"{field_name} must be in format {fmt}")
        
        return result
    
    @staticmethod
    def compare(value1: Any, value2: Any, operator: str, field_name1: str, field_name2: str) -> ValidationResult:
        """
        Compare two values.
        
        Args:
            value1: First value
            value2: Second value
            operator: Comparison operator (==, !=, <, >, <=, >=)
            field_name1: Name of first field
            field_name2: Name of second field
            
        Returns:
            ValidationResult
        """
        result = ValidationResult(True)
        
        operators = {
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            "<": lambda a, b: a < b,
            ">": lambda a, b: a > b,
            "<=": lambda a, b: a <= b,
            ">=": lambda a, b: a >= b
        }
        
        if operator not in operators:
            return result.add_error(f"Unknown operator: {operator}")
        
        if not operators[operator](value1, value2):
            return result.add_error(f"{field_name1} must {operator} {field_name2}")
        
        return result


class FormValidator:
    """
    Validates complete forms with multiple fields.
    
    Design Pattern: Composite Pattern - Composes multiple validators
    """
    
    def __init__(self):
        self.rules: Dict[str, List[Tuple[Callable, str]]] = {}
    
    def add_rule(self, field_name: str, validator: Callable, error_message: Optional[str] = None) -> 'FormValidator':
        """
        Add a validation rule for a field.
        
        Args:
            field_name: Name of the field to validate
            validator: Validation function
            error_message: Custom error message (optional)
            
        Returns:
            Self for method chaining
        """
        if field_name not in self.rules:
            self.rules[field_name] = []
        
        self.rules[field_name].append((validator, error_message))
        return self
    
    def validate(self, data: Dict[str, Any]) -> ValidationResult:
        """
        Validate all fields against their rules.
        
        Args:
            data: Dictionary of field values
            
        Returns:
            ValidationResult with all errors
        """
        result = ValidationResult(True)
        
        for field_name, validators in self.rules.items():
            value = data.get(field_name)
            
            for validator, custom_message in validators:
                # Call validator with appropriate arguments
                if isinstance(validator, tuple):
                    # Validator with additional args
                    validation_result = validator[0](value, *validator[1:])
                else:
                    # Simple validator
                    validation_result = validator(value)
                
                if not validation_result.is_valid:
                    if custom_message:
                        result.add_error(custom_message)
                    else:
                        for error in validation_result.errors:
                            result.add_error(error)
        
        return result


def build_registration_form_validator() -> FormValidator:
    """
    Build a validator for a user registration form.
    
    Returns:
        Configured FormValidator instance
    """
    validator = FormValidator()
    
    # Username rules
    validator.add_rule(
        "username",
        lambda v: Validators.required(v, "Username"),
        "Username is required"
    )
    validator.add_rule(
        "username",
        lambda v: Validators.min_length(v, 3, "Username"),
        "Username must be at least 3 characters"
    )
    validator.add_rule(
        "username",
        lambda v: Validators.max_length(v, 20, "Username"),
        "Username cannot exceed 20 characters"
    )
    validator.add_rule(
        "username",
        lambda v: Validators.pattern(v, r'^[a-zA-Z0-9_]+$', "Username"),
        "Username can only contain letters, numbers, and underscore"
    )
    
    # Email rules
    validator.add_rule(
        "email",
        Validators.email,
        "Please enter a valid email address"
    )
    
    # Password rules
    validator.add_rule(
        "password",
        lambda v: Validators.required(v, "Password"),
        "Password is required"
    )
    validator.add_rule(
        "password",
        lambda v: Validators.min_length(v, 8, "Password"),
        "Password must be at least 8 characters"
    )
    
    # Age rules
    validator.add_rule(
        "age",
        lambda v: Validators.age(v, 13, 120, "Age"),
        "Must be at least 13 years old"
    )
    
    # Phone rules (optional)
    validator.add_rule(
        "phone",
        Validators.phone,
        "Please enter a valid phone number (10-15 digits)"
    )
    
    return validator


def run_validation_demo():
    """
    Demonstrate the validation functions.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: DATA VALIDATION FUNCTIONS")
    print("=" * 60)
    
    # Test individual validators
    print("\n1. INDIVIDUAL VALIDATOR TESTS")
    print("-" * 40)
    
    test_cases = [
        ("Email", Validators.email("alice@example.com"), "Valid email"),
        ("Email", Validators.email("invalid"), "Invalid email"),
        ("Age", Validators.age(25), "Valid age"),
        ("Age", Validators.age(12), "Too young"),
        ("Age", Validators.age(150), "Too old"),
        ("Phone", Validators.phone("555-123-4567"), "Valid phone"),
        ("Phone", Validators.phone("123"), "Invalid phone"),
    ]
    
    for name, result, expected_desc in test_cases:
        status = "✅" if result.is_valid else "❌"
        print(f"  {status} {name}: {expected_desc} → {result}")
    
    # Test form validator
    print("\n2. FORM VALIDATION DEMO")
    print("-" * 40)
    
    validator = build_registration_form_validator()
    
    # Test valid data
    valid_data = {
        "username": "alice_wonder",
        "email": "alice@example.com",
        "password": "SecurePass123",
        "age": 25,
        "phone": "555-123-4567"
    }
    
    result = validator.validate(valid_data)
    print(f"\n  Valid form data:")
    for key, value in valid_data.items():
        print(f"    {key}: {value}")
    print(f"  Validation result: {result}")
    
    # Test invalid data
    invalid_data = {
        "username": "a",  # Too short
        "email": "invalid",  # Invalid format
        "password": "weak",  # Too short
        "age": 12,  # Too young
        "phone": "123"  # Invalid phone
    }
    
    result = validator.validate(invalid_data)
    print(f"\n  Invalid form data:")
    for key, value in invalid_data.items():
        print(f"    {key}: {value}")
    print(f"  Validation result: {result}")
    if not result.is_valid:
        print("  Errors:")
        for error in result.errors:
            print(f"    ❌ {error}")


if __name__ == "__main__":
    run_validation_demo()
```

---

## 📝 Section 3: String Processing Utility Library

A collection of utility functions for string processing that can be reused across any project.

**SOLID Principles Applied:**
- Single Responsibility: Each utility does one thing
- Interface Segregation: Clean, focused interfaces

**Design Pattern: Utility Pattern** – Static methods that provide common functionality

```python
"""
STRING PROCESSING UTILITY LIBRARY

This section builds reusable string processing utilities.

SOLID Principles Applied:
- Single Responsibility: Each utility does one thing
- Interface Segregation: Clean, focused interfaces

Design Pattern: Utility Pattern
- Static methods providing common functionality
"""

from typing import List, Optional, Tuple
import re
import hashlib
import secrets
import string


class StringUtils:
    """
    Collection of string processing utility functions.
    
    All methods are static - no instance needed.
    """
    
    @staticmethod
    def is_empty(s: Optional[str]) -> bool:
        """
        Check if string is None, empty, or only whitespace.
        
        Args:
            s: String to check
            
        Returns:
            True if string is empty or whitespace
        """
        return s is None or not s.strip()
    
    @staticmethod
    def truncate(s: str, max_length: int, suffix: str = "...") -> str:
        """
        Truncate string to maximum length with suffix.
        
        Args:
            s: String to truncate
            max_length: Maximum length (including suffix)
            suffix: String to append when truncated
            
        Returns:
            Truncated string
        """
        if len(s) <= max_length:
            return s
        
        trunc_length = max_length - len(suffix)
        if trunc_length <= 0:
            return suffix
        
        return s[:trunc_length] + suffix
    
    @staticmethod
    def slugify(text: str) -> str:
        """
        Convert text to URL-friendly slug.
        
        Args:
            text: Text to slugify
            
        Returns:
            URL-friendly slug
        """
        # Convert to lowercase
        text = text.lower()
        
        # Replace spaces with hyphens
        text = re.sub(r'\s+', '-', text)
        
        # Remove special characters
        text = re.sub(r'[^a-z0-9\-]', '', text)
        
        # Remove multiple hyphens
        text = re.sub(r'-+', '-', text)
        
        # Strip hyphens from ends
        text = text.strip('-')
        
        return text
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """
        Extract all email addresses from text.
        
        Args:
            text: Text to search
            
        Returns:
            List of found email addresses
        """
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """
        Extract all URLs from text.
        
        Args:
            text: Text to search
            
        Returns:
            List of found URLs
        """
        pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/[-\w%!?=:@]+)*'
        return re.findall(pattern, text)
    
    @staticmethod
    def mask_email(email: str) -> str:
        """
        Mask email address for privacy.
        
        Args:
            email: Email address
            
        Returns:
            Masked email (e.g., a***e@example.com)
        """
        if "@" not in email:
            return email
        
        local, domain = email.split("@", 1)
        
        if len(local) <= 2:
            masked_local = local[0] + "***"
        else:
            masked_local = local[0] + "***" + local[-1]
        
        return f"{masked_local}@{domain}"
    
    @staticmethod
    def mask_phone(phone: str) -> str:
        """
        Mask phone number for privacy.
        
        Args:
            phone: Phone number
            
        Returns:
            Masked phone (e.g., ***-***-1234)
        """
        # Remove non-digits
        digits = re.sub(r'\D', '', phone)
        
        if len(digits) < 4:
            return "***"
        
        last4 = digits[-4:]
        return f"***-***-{last4}"
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate email address format.
        
        Args:
            email: Email address
            
        Returns:
            True if valid format
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """
        Validate phone number format.
        
        Args:
            phone: Phone number
            
        Returns:
            True if valid format
        """
        digits = re.sub(r'\D', '', phone)
        return 10 <= len(digits) <= 15
    
    @staticmethod
    def generate_random_string(length: int = 16, include_digits: bool = True) -> str:
        """
        Generate cryptographically random string.
        
        Args:
            length: Length of string
            include_digits: Whether to include digits
            
        Returns:
            Random string
        """
        chars = string.ascii_letters
        if include_digits:
            chars += string.digits
        
        return ''.join(secrets.choice(chars) for _ in range(length))
    
    @staticmethod
    def generate_token(length: int = 32) -> str:
        """
        Generate secure random token.
        
        Args:
            length: Token length in bytes
            
        Returns:
            Hexadecimal token
        """
        return secrets.token_hex(length)
    
    @staticmethod
    def hash_string(s: str, algorithm: str = "sha256") -> str:
        """
        Hash a string using specified algorithm.
        
        Args:
            s: String to hash
            algorithm: Hash algorithm (sha256, sha512, md5)
            
        Returns:
            Hexadecimal hash
        """
        hash_funcs = {
            "sha256": hashlib.sha256,
            "sha512": hashlib.sha512,
            "md5": hashlib.md5
        }
        
        if algorithm not in hash_funcs:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        return hash_funcs[algorithm](s.encode()).hexdigest()
    
    @staticmethod
    def capitalize_words(s: str) -> str:
        """
        Capitalize first letter of each word.
        
        Args:
            s: String to capitalize
            
        Returns:
            Capitalized string
        """
        return ' '.join(word.capitalize() for word in s.split())
    
    @staticmethod
    def reverse_words(s: str) -> str:
        """
        Reverse the order of words in a string.
        
        Args:
            s: String to reverse
            
        Returns:
            String with words reversed
        """
        return ' '.join(s.split()[::-1])
    
    @staticmethod
    def count_words(s: str) -> int:
        """
        Count number of words in string.
        
        Args:
            s: String to count
            
        Returns:
            Number of words
        """
        return len(s.split())
    
    @staticmethod
    def remove_duplicate_words(s: str) -> str:
        """
        Remove duplicate words while preserving order.
        
        Args:
            s: String to process
            
        Returns:
            String with duplicates removed
        """
        words = s.split()
        seen = set()
        result = []
        
        for word in words:
            if word.lower() not in seen:
                seen.add(word.lower())
                result.append(word)
        
        return ' '.join(result)
    
    @staticmethod
    def to_camel_case(s: str) -> str:
        """
        Convert snake_case to camelCase.
        
        Args:
            s: snake_case string
            
        Returns:
            camelCase string
        """
        parts = s.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    @staticmethod
    def to_snake_case(s: str) -> str:
        """
        Convert camelCase to snake_case.
        
        Args:
            s: camelCase string
            
        Returns:
            snake_case string
        """
        s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
    
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Check if string is a palindrome.
        
        Args:
            s: String to check
            
        Returns:
            True if palindrome
        """
        # Remove non-alphanumeric and convert to lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned == cleaned[::-1]


def run_string_utils_demo():
    """
    Demonstrate the string utility functions.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: STRING PROCESSING UTILITIES")
    print("=" * 60)
    
    utils = StringUtils
    
    # Demonstrate each utility
    print("\n1. BASIC UTILITIES")
    print("-" * 40)
    
    print(f"  is_empty(''): {utils.is_empty('')}")
    print(f"  is_empty('  '): {utils.is_empty('  ')}")
    print(f"  is_empty('hello'): {utils.is_empty('hello')}")
    
    long_text = "This is a very long string that needs to be truncated"
    print(f"  truncate('{long_text}', 20): '{utils.truncate(long_text, 20)}'")
    
    print(f"  slugify('Hello World!'): '{utils.slugify('Hello World!')}'")
    print(f"  slugify('Python Programming 101'): '{utils.slugify('Python Programming 101')}'")
    
    print("\n2. EXTRACTION")
    print("-" * 40)
    
    sample_text = "Contact alice@example.com or bob@company.co.uk. Visit https://python.org for more."
    print(f"  extract_emails('{sample_text}'): {utils.extract_emails(sample_text)}")
    print(f"  extract_urls('{sample_text}'): {utils.extract_urls(sample_text)}")
    
    print("\n3. MASKING (Privacy)")
    print("-" * 40)
    
    print(f"  mask_email('alice@example.com'): '{utils.mask_email('alice@example.com')}'")
    print(f"  mask_phone('555-123-4567'): '{utils.mask_phone('555-123-4567')}'")
    
    print("\n4. VALIDATION")
    print("-" * 40)
    
    print(f"  is_valid_email('alice@example.com'): {utils.is_valid_email('alice@example.com')}")
    print(f"  is_valid_email('invalid'): {utils.is_valid_email('invalid')}")
    print(f"  is_valid_phone('555-123-4567'): {utils.is_valid_phone('555-123-4567')}")
    
    print("\n5. GENERATION")
    print("-" * 40)
    
    print(f"  generate_random_string(16): '{utils.generate_random_string(16)}'")
    print(f"  generate_token(16): '{utils.generate_token(16)}'")
    print(f"  hash_string('password'): '{utils.hash_string('password')[:16]}...'")
    
    print("\n6. TRANSFORMATION")
    print("-" * 40)
    
    print(f"  capitalize_words('hello world python'): '{utils.capitalize_words('hello world python')}'")
    print(f"  reverse_words('hello world python'): '{utils.reverse_words('hello world python')}'")
    print(f"  count_words('The quick brown fox'): {utils.count_words('The quick brown fox')}")
    
    print(f"  to_camel_case('user_first_name'): '{utils.to_camel_case('user_first_name')}'")
    print(f"  to_snake_case('userFirstName'): '{utils.to_snake_case('userFirstName')}'")
    
    print(f"  is_palindrome('A man a plan a canal panama'): {utils.is_palindrome('A man a plan a canal panama')}")
    print(f"  is_palindrome('hello'): {utils.is_palindrome('hello')}")


if __name__ == "__main__":
    run_string_utils_demo()
```

---

## 🏭 Section 4: Complete Order Processing System

A complete order processing system that demonstrates how functions organize complex business logic.

**SOLID Principles Applied:**
- Single Responsibility: Each function handles one aspect of order processing
- Dependency Inversion: High-level functions depend on abstractions

**Design Pattern: Pipeline Pattern** – Order flows through processing stages

```python
"""
COMPLETE ORDER PROCESSING SYSTEM

This section builds a complete order processing system using functions
to organize complex business logic.

SOLID Principles Applied:
- Single Responsibility: Each function handles one aspect
- Dependency Inversion: High-level functions depend on abstractions

Design Pattern: Pipeline Pattern
- Order flows through processing stages
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import random


@dataclass
class OrderItem:
    """Individual item in an order."""
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
    phone: str


@dataclass
class Order:
    """Complete order with all details."""
    order_id: str
    customer: Customer
    items: List[OrderItem]
    subtotal: float
    discount_amount: float
    tax_amount: float
    shipping_cost: float
    total: float
    status: str
    created_at: datetime
    payment_method: Optional[str] = None
    tracking_number: Optional[str] = None


# ==========================================================================
# VALIDATION FUNCTIONS
# ==========================================================================

def validate_order_items(items: List[OrderItem]) -> Tuple[bool, str]:
    """
    Validate order items.
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not items:
        return False, "Order must contain at least one item"
    
    for item in items:
        if item.quantity <= 0:
            return False, f"Invalid quantity for {item.name}"
        
        if item.unit_price <= 0:
            return False, f"Invalid price for {item.name}"
    
    return True, ""


def validate_customer(customer: Customer) -> Tuple[bool, str]:
    """
    Validate customer information.
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not customer.name:
        return False, "Customer name is required"
    
    if not customer.email or "@" not in customer.email:
        return False, "Valid email is required"
    
    if not customer.address:
        return False, "Shipping address is required"
    
    if customer.tier not in ["bronze", "silver", "gold", "platinum"]:
        return False, f"Invalid customer tier: {customer.tier}"
    
    return True, ""


# ==========================================================================
# CALCULATION FUNCTIONS
# ==========================================================================

def calculate_subtotal(items: List[OrderItem]) -> float:
    """
    Calculate order subtotal.
    
    Args:
        items: List of order items
        
    Returns:
        Subtotal amount
    """
    return sum(item.subtotal() for item in items)


def calculate_discount(subtotal: float, customer_tier: str, has_coupon: bool = False) -> Tuple[float, str]:
    """
    Calculate discount based on customer tier and coupons.
    
    Args:
        subtotal: Order subtotal
        customer_tier: Customer loyalty tier
        has_coupon: Whether customer has a coupon
        
    Returns:
        Tuple of (discount_amount, discount_reason)
    """
    discount_percent = 0.0
    reason = ""
    
    # Tier-based discounts
    tier_discounts = {
        "bronze": 0.00,
        "silver": 0.05,
        "gold": 0.10,
        "platinum": 0.15
    }
    
    discount_percent = tier_discounts.get(customer_tier, 0.00)
    reason = f"{customer_tier.capitalize()} tier discount"
    
    # Additional coupon discount
    if has_coupon and subtotal >= 50:
        discount_percent += 0.10
        reason = f"{reason} + coupon discount"
    
    # Cap at 25% maximum discount
    discount_percent = min(discount_percent, 0.25)
    
    discount_amount = subtotal * discount_percent
    return round(discount_amount, 2), reason


def calculate_tax(subtotal: float, discount_amount: float, tax_rate: float = 0.08) -> float:
    """
    Calculate tax on discounted subtotal.
    
    Args:
        subtotal: Order subtotal
        discount_amount: Applied discount
        tax_rate: Tax rate (default 8%)
        
    Returns:
        Tax amount
    """
    taxable_amount = subtotal - discount_amount
    return round(taxable_amount * tax_rate, 2)


def calculate_shipping(subtotal: float, customer_tier: str, items_count: int) -> Tuple[float, str]:
    """
    Calculate shipping cost.
    
    Args:
        subtotal: Order subtotal
        customer_tier: Customer tier
        items_count: Number of items
        
    Returns:
        Tuple of (shipping_cost, shipping_method)
    """
    # Free shipping for high-value orders
    if subtotal >= 100:
        return 0.00, "Free Shipping"
    
    # Free shipping for platinum members
    if customer_tier == "platinum":
        return 0.00, "Free Shipping (Platinum)"
    
    # Standard shipping rates
    if subtotal >= 50:
        cost = 5.99
        method = "Standard Shipping"
    elif items_count <= 2:
        cost = 4.99
        method = "Economy Shipping"
    else:
        cost = 9.99
        method = "Standard Shipping"
    
    return cost, method


# ==========================================================================
# PROCESSING FUNCTIONS
# ==========================================================================

def create_order(customer: Customer, items: List[OrderItem], has_coupon: bool = False) -> Order:
    """
    Create a new order with all calculations.
    
    Args:
        customer: Customer placing the order
        items: Items in the order
        has_coupon: Whether customer has a coupon
        
    Returns:
        Complete Order object
    """
    # Generate order ID
    order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"
    
    # Calculate amounts
    subtotal = calculate_subtotal(items)
    discount_amount, discount_reason = calculate_discount(subtotal, customer.tier, has_coupon)
    tax_amount = calculate_tax(subtotal, discount_amount)
    shipping_cost, shipping_method = calculate_shipping(subtotal, customer.tier, len(items))
    total = subtotal - discount_amount + tax_amount + shipping_cost
    
    # Create order
    return Order(
        order_id=order_id,
        customer=customer,
        items=items,
        subtotal=round(subtotal, 2),
        discount_amount=discount_amount,
        tax_amount=tax_amount,
        shipping_cost=shipping_cost,
        total=round(total, 2),
        status="pending",
        created_at=datetime.now()
    )


def process_payment(order: Order, payment_method: str, payment_details: Dict) -> Tuple[bool, str, Optional[str]]:
    """
    Process payment for an order.
    
    Args:
        order: Order to process
        payment_method: Payment method (credit_card, paypal, cash)
        payment_details: Payment-specific details
        
    Returns:
        Tuple of (success, message, transaction_id)
    """
    if payment_method == "credit_card":
        # Simulate credit card processing
        card_number = payment_details.get("card_number", "")
        if len(card_number) >= 13 and "4111" in card_number:
            transaction_id = f"CC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return True, "Payment approved", transaction_id
        else:
            return False, "Card declined", None
    
    elif payment_method == "paypal":
        # Simulate PayPal processing
        email = payment_details.get("email", "")
        if "@" in email:
            transaction_id = f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return True, "PayPal payment successful", transaction_id
        else:
            return False, "Invalid PayPal account", None
    
    elif payment_method == "cash":
        # Cash payment
        cash_received = payment_details.get("cash_received", 0)
        if cash_received >= order.total:
            change = cash_received - order.total
            return True, f"Cash payment accepted. Change: ${change:.2f}", None
        else:
            shortfall = order.total - cash_received
            return False, f"Insufficient cash. Need ${shortfall:.2f} more", None
    
    else:
        return False, f"Unsupported payment method: {payment_method}", None


def update_inventory(order: Order) -> Tuple[bool, List[str]]:
    """
    Update inventory after order.
    
    Returns:
        Tuple of (success, out_of_stock_items)
    """
    out_of_stock = []
    
    for item in order.items:
        # Simulate inventory check
        if item.product_id.startswith("OUT"):
            out_of_stock.append(item.name)
    
    return len(out_of_stock) == 0, out_of_stock


def generate_tracking_number(order: Order) -> str:
    """
    Generate tracking number for shipping.
    
    Args:
        order: Order to ship
        
    Returns:
        Tracking number
    """
    return f"TRK-{order.order_id[-8:]}-{random.randint(1000, 9999)}"


def send_confirmation_email(order: Order) -> bool:
    """
    Send order confirmation email.
    
    Returns:
        True if sent successfully
    """
    # Simulate email sending
    print(f"  📧 Sending confirmation to {order.customer.email}...")
    return True


def process_order(customer: Customer, items: List[OrderItem], 
                  payment_method: str, payment_details: Dict,
                  has_coupon: bool = False) -> Dict[str, Any]:
    """
    Complete order processing pipeline.
    
    This function orchestrates all the steps of order processing.
    
    Args:
        customer: Customer information
        items: Order items
        payment_method: Payment method
        payment_details: Payment details
        has_coupon: Whether customer has coupon
        
    Returns:
        Dictionary with processing results
    """
    print("\n" + "=" * 50)
    print("ORDER PROCESSING PIPELINE")
    print("=" * 50)
    
    # Step 1: Validate
    print("\n1. VALIDATION")
    print("-" * 30)
    
    items_valid, items_error = validate_order_items(items)
    if not items_valid:
        return {"success": False, "error": items_error}
    print("  ✓ Items validated")
    
    customer_valid, customer_error = validate_customer(customer)
    if not customer_valid:
        return {"success": False, "error": customer_error}
    print("  ✓ Customer validated")
    
    # Step 2: Create order
    print("\n2. ORDER CREATION")
    print("-" * 30)
    
    order = create_order(customer, items, has_coupon)
    print(f"  Order ID: {order.order_id}")
    print(f"  Subtotal: ${order.subtotal:.2f}")
    if order.discount_amount > 0:
        print(f"  Discount: -${order.discount_amount:.2f}")
    print(f"  Tax: +${order.tax_amount:.2f}")
    print(f"  Shipping: +${order.shipping_cost:.2f}")
    print(f"  TOTAL: ${order.total:.2f}")
    
    # Step 3: Process payment
    print("\n3. PAYMENT PROCESSING")
    print("-" * 30)
    
    payment_success, payment_message, transaction_id = process_payment(order, payment_method, payment_details)
    if not payment_success:
        order.status = "payment_failed"
        return {"success": False, "error": payment_message, "order": order}
    print(f"  ✓ {payment_message}")
    if transaction_id:
        print(f"  Transaction ID: {transaction_id}")
    order.payment_method = payment_method
    
    # Step 4: Update inventory
    print("\n4. INVENTORY UPDATE")
    print("-" * 30)
    
    inventory_success, out_of_stock = update_inventory(order)
    if not inventory_success:
        order.status = "inventory_failed"
        return {"success": False, "error": f"Out of stock: {', '.join(out_of_stock)}", "order": order}
    print("  ✓ Inventory updated")
    
    # Step 5: Generate tracking
    print("\n5. SHIPPING")
    print("-" * 30)
    
    tracking_number = generate_tracking_number(order)
    order.tracking_number = tracking_number
    order.status = "shipped"
    print(f"  Tracking number: {tracking_number}")
    
    # Step 6: Send confirmation
    print("\n6. CONFIRMATION")
    print("-" * 30)
    
    send_confirmation_email(order)
    print("  ✓ Confirmation email sent")
    
    return {
        "success": True,
        "order": order,
        "message": f"Order {order.order_id} processed successfully",
        "tracking_number": tracking_number
    }


def run_order_processing_demo():
    """
    Demonstrate the complete order processing system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: COMPLETE ORDER PROCESSING SYSTEM")
    print("=" * 60)
    
    # Create test customer
    customer = Customer(
        id="CUST-001",
        name="Alice Chen",
        email="alice@example.com",
        tier="gold",
        address="123 Main St, New York, NY 10001",
        phone="555-123-4567"
    )
    
    # Create test items
    items = [
        OrderItem("P001", "Laptop", 1, 999.99),
        OrderItem("P002", "Mouse", 2, 29.99),
        OrderItem("P003", "USB Cable", 1, 19.99)
    ]
    
    # Test successful order
    print("\n📦 TEST CASE 1: SUCCESSFUL ORDER")
    print("-" * 40)
    
    result = process_order(
        customer=customer,
        items=items,
        payment_method="credit_card",
        payment_details={"card_number": "4111111111111111"},
        has_coupon=True
    )
    
    if result["success"]:
        order = result["order"]
        print(f"\n✅ SUCCESS: {result['message']}")
        print(f"   Order ID: {order.order_id}")
        print(f"   Status: {order.status}")
        print(f"   Total: ${order.total:.2f}")
        print(f"   Tracking: {order.tracking_number}")
    
    # Test failed payment
    print("\n📦 TEST CASE 2: FAILED PAYMENT")
    print("-" * 40)
    
    result = process_order(
        customer=customer,
        items=items,
        payment_method="credit_card",
        payment_details={"card_number": "1234"},
        has_coupon=False
    )
    
    if not result["success"]:
        print(f"\n❌ FAILED: {result['error']}")
    
    # Test out of stock
    print("\n📦 TEST CASE 3: OUT OF STOCK")
    print("-" * 40)
    
    out_of_stock_items = [
        OrderItem("OUT001", "Popular Item", 1, 49.99),
        OrderItem("P002", "Mouse", 1, 29.99)
    ]
    
    result = process_order(
        customer=customer,
        items=out_of_stock_items,
        payment_method="credit_card",
        payment_details={"card_number": "4111111111111111"},
        has_coupon=False
    )
    
    if not result["success"]:
        print(f"\n❌ FAILED: {result['error']}")


if __name__ == "__main__":
    run_order_processing_demo()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Function Basics** – Define with `def`, call by name. Functions encapsulate reusable logic.

- **Parameters and Arguments** – Functions can accept inputs. Multiple parameters, default values.

- **Return Values** – Functions return results with `return`. Can return multiple values as tuples.

- **Variable Scope** – Local variables exist only inside functions. Use `global` and `nonlocal` sparingly.

- **Best Practices** – Single responsibility, descriptive names, docstrings, type hints, error handling.

- **Payment Processor** – Validation, logging, and processing functions. Credit card, PayPal, cash payments.

- **Validation Functions** – Reusable validators for email, phone, age, ranges. Form validation composition.

- **String Utilities** – Truncation, slugify, extraction, masking, generation, transformation.

- **Order Processing** – Pipeline of functions: validate → calculate → payment → inventory → shipping → confirm.

- **SOLID Principles Applied** – Single Responsibility (each function does one thing), Open/Closed (extensible), Dependency Inversion (abstractions).

- **Design Patterns Used** – Command Pattern (functions as commands), Strategy Pattern (validation strategies), Utility Pattern (static methods), Pipeline Pattern (processing stages).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Arguments – Positional, Keyword, and Default (Series B, Story 2)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 1 | 5 | 17% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **13** | **39** | **25%** |

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

**Next Story:** Series B, Story 2: The 2026 Python Metromap: Arguments – Positional, Keyword, and Default

---

## 📝 Your Invitation

You've mastered defining functions. Now build something with what you've learned:

1. **Build a validation library** – Create reusable validators for common data types. Compose them for form validation.

2. **Create a string utility module** – Implement slugify, email masking, URL extraction, and hash functions.

3. **Build a payment processor** – Add support for more payment methods (crypto, gift cards, store credit).

4. **Create an order processing system** – Add more stages: fraud detection, tax calculation by region, international shipping.

5. **Build a report generator** – Create functions that generate PDF, CSV, and HTML reports from data.

**You've mastered defining functions. Next stop: Arguments!**

---

*Found this helpful? Clap, comment, and share what functions you built. Next stop: Arguments!* 🚇