# The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users

## Series A: Foundations Station | Story 7 of 7

![The 2026 Python Metromap/images/Input Output and Type Casting – Talking to Users](images/Input Output and Type Casting – Talking to Users.png)

## 📖 Introduction

**Welcome to the seventh and final stop on the Foundations Station Line.**

You've mastered variables, collections, operators, control flow, loops, and nested logic. You can store data, transform it, make decisions, repeat operations, and validate complex structures. But all of this power is useless if your program can't communicate with the outside world.

Input and output are the bridges between your code and reality. The `print()` function displays results, status messages, and prompts. The `input()` function receives data from users. Type casting converts between data types—turning the string "42" into the integer 42, or formatting numbers for display.

This story—**The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users**—is your guide to making your programs interactive. We'll build a complete CLI calculator that handles user input, validates it, performs calculations, and formats output. We'll create a user registration system with comprehensive validation. We'll build an interactive quiz system that tracks scores and provides feedback. And we'll implement a complete point-of-sale terminal that integrates everything you've learned.

**Let's start the conversation.**

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

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter.

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system. **⬅️ YOU ARE HERE**

### Series B: Functions & Modules Yard (6 Stories) – Next Station

- 🔧 **The 2026 Python Metromap: Defining Functions – The Workhorses of Python** – Payment processing module; validation functions; error handling. 🔜 *Up Next*

- 📋 **The 2026 Python Metromap: Arguments – Positional, Keyword, and Default** – Flexible report generator for PDF, CSV, and JSON outputs.

- 📤 **The 2026 Python Metromap: Return Values – Getting Results Back** – API response formatter; standardized success and error responses.

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines.

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver.

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📥 Section 1: Basic Input and Output – print() and input()

The `print()` function sends output to the console. The `input()` function reads user input as a string.

**SOLID Principle Applied: Single Responsibility** – Each I/O function has one clear purpose: print displays, input collects.

**Design Pattern: Adapter Pattern** – I/O functions adapt between user interaction and program logic.

```python
"""
BASIC INPUT AND OUTPUT: print() AND input()

This section covers the fundamental I/O functions in Python.

SOLID Principle: Single Responsibility
- print() displays output
- input() collects user input

Design Pattern: Adapter Pattern
- I/O functions adapt between user and program
"""

from typing import Any, List, Optional
import time


def demonstrate_print_basics():
    """
    Demonstrates the print() function and its parameters.
    
    print() can handle multiple arguments, custom separators,
    and custom endings.
    """
    print("=" * 60)
    print("SECTION 1A: PRINT() FUNCTION")
    print("=" * 60)
    
    # BASIC PRINT
    print("\n1. BASIC PRINT")
    print("-" * 40)
    
    print("Hello, World!")
    print(42)
    print(3.14159)
    print(True)
    
    # MULTIPLE ARGUMENTS
    print("\n2. MULTIPLE ARGUMENTS")
    print("-" * 40)
    
    # Print multiple values (automatically adds spaces)
    print("Hello", "World", "from", "Python")
    
    # Mixing types
    name = "Alice"
    age = 28
    print("Name:", name, "Age:", age)
    
    # SEPARATOR PARAMETER (sep)
    print("\n3. SEPARATOR PARAMETER (sep)")
    print("-" * 40)
    
    # Default separator (space)
    print("apple", "banana", "cherry")
    
    # Custom separator
    print("apple", "banana", "cherry", sep=", ")
    print("apple", "banana", "cherry", sep=" | ")
    print("apple", "banana", "cherry", sep="\n")
    
    # CSV format
    print("name,age,city", "Alice,28,NYC", "Bob,35,LA", sep="\n")
    
    # END PARAMETER (end)
    print("\n4. END PARAMETER (end)")
    print("-" * 40)
    
    # Default end (newline)
    print("First line")
    print("Second line")
    
    # Custom end
    print("Loading", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(" Done!")
    
    # No newline
    print("Same line ", end="")
    print("continues here")
    
    # FILE PARAMETER (write to file)
    print("\n5. FILE PARAMETER (writing to file)")
    print("-" * 40)
    
    with open("output.txt", "w") as f:
        print("This goes to a file", file=f)
        print("Another line in the file", file=f)
    
    print("Text written to output.txt")
    
    # FLUSH PARAMETER (force output)
    print("\n6. FLUSH PARAMETER")
    print("-" * 40)
    
    for i in range(3):
        print(f"Progress: {i}/3", end="\r", flush=True)
        time.sleep(0.5)
    print("Progress: Complete!    ")
    
    # FORMATTED PRINTING
    print("\n7. FORMATTED PRINTING")
    print("-" * 40)
    
    # f-strings (recommended)
    name = "Alice"
    score = 95.5
    print(f"Student {name} scored {score:.1f}%")
    
    # .format() method
    print("Student {} scored {:.1f}%".format(name, score))
    
    # % formatting (old style)
    print("Student %s scored %.1f%%" % (name, score))
    
    # Alignment
    print(f"{'Left':<10} {'Center':^10} {'Right':>10}")
    print(f"{'apple':<10} {'banana':^10} {'cherry':>10}")
    
    # PRETTY PRINTING
    print("\n8. PRETTY PRINTING")
    print("-" * 40)
    
    data = {
        "name": "Alice Chen",
        "age": 28,
        "email": "alice@example.com",
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY"
        }
    }
    
    # Simple print
    print("Simple:", data)
    
    # Pretty print with pprint
    import pprint
    print("\nPretty print:")
    pprint.pprint(data, indent=2, width=40)


def demonstrate_input_basics():
    """
    Demonstrates the input() function for collecting user input.
    
    input() always returns a string. Values must be converted
    to appropriate types using type casting.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: INPUT() FUNCTION")
    print("=" * 60)
    
    # Simulated inputs for demonstration (since real input would pause)
    simulated_responses = ["Alice", "28", "alice@example.com", "100"]
    response_index = 0
    
    def simulate_input(prompt: str) -> str:
        """Simulate user input for demonstration purposes."""
        nonlocal response_index
        response = simulated_responses[response_index % len(simulated_responses)]
        response_index += 1
        print(f"{prompt}{response} (simulated)")
        return response
    
    print("\n(Using simulated input for demonstration)")
    print("-" * 40)
    
    # BASIC INPUT
    print("\n1. BASIC INPUT")
    print("-" * 40)
    
    name = simulate_input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # INPUT ALWAYS RETURNS STRING
    print("\n2. INPUT RETURNS STRING")
    print("-" * 40)
    
    age_str = simulate_input("Enter your age: ")
    print(f"Type of input: {type(age_str).__name__}")
    print(f"Value: '{age_str}'")
    
    # Must convert for numeric operations
    age = int(age_str)
    next_age = age + 1
    print(f"Next year you will be {next_age}")
    
    # INPUT WITH VALIDATION LOOP
    print("\n3. INPUT WITH VALIDATION LOOP")
    print("-" * 40)
    
    # Simulate multiple attempts
    simulated_ages = ["abc", "-5", "25"]
    age_index = 0
    
    def simulate_validated_input(prompt: str) -> str:
        nonlocal age_index
        response = simulated_ages[age_index]
        age_index += 1
        print(f"{prompt}{response}")
        return response
    
    age = None
    attempts = 0
    
    while age is None and attempts < len(simulated_ages):
        user_input = simulate_validated_input("Enter your age: ")
        attempts += 1
        
        if not user_input.isdigit():
            print(f"  Invalid: '{user_input}' is not a number")
            continue
        
        age_value = int(user_input)
        
        if age_value < 0 or age_value > 120:
            print(f"  Invalid: Age must be between 0 and 120")
            continue
        
        age = age_value
        print(f"  Valid age: {age}")
    
    # MULTIPLE INPUTS
    print("\n4. MULTIPLE INPUTS")
    print("-" * 40)
    
    print("Enter three numbers separated by spaces:")
    simulated_numbers = "10 20 30"
    print(f"  {simulated_numbers}")
    
    # Split input into multiple values
    values = simulated_numbers.split()
    if len(values) >= 3:
        a, b, c = map(int, values[:3])
        print(f"Sum: {a + b + c}")
    
    # SECURE INPUT (password)
    print("\n5. SECURE INPUT (password simulation)")
    print("-" * 40)
    
    import getpass
    
    print("(getpass hides input in real terminals)")
    # In real code: password = getpass.getpass("Enter password: ")
    # For demo, we'll simulate
    password = "secret123"
    print(f"Password entered (simulated): {'*' * len(password)}")


def demonstrate_type_casting():
    """
    Demonstrates converting between data types (type casting).
    
    Type casting converts a value from one type to another.
    Common conversions: int(), float(), str(), bool(), list(), dict()
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: TYPE CASTING")
    print("=" * 60)
    
    # STRING TO INTEGER
    print("\n1. STRING TO INTEGER (int())")
    print("-" * 40)
    
    str_num = "42"
    int_num = int(str_num)
    print(f"'{str_num}' → {int_num} (type: {type(int_num).__name__})")
    
    # String with decimal converts to int (truncates)
    str_decimal = "3.14"
    try:
        int_decimal = int(float(str_decimal))  # Must go through float first
        print(f"'{str_decimal}' → {int_decimal} (via float)")
    except ValueError:
        print(f"'{str_decimal}' cannot convert directly to int")
    
    # STRING TO FLOAT
    print("\n2. STRING TO FLOAT (float())")
    print("-" * 40)
    
    str_float = "3.14159"
    float_num = float(str_float)
    print(f"'{str_float}' → {float_num} (type: {type(float_num).__name__})")
    
    str_int = "42"
    float_from_int = float(str_int)
    print(f"'{str_int}' → {float_from_int} (type: {type(float_from_int).__name__})")
    
    # NUMBER TO STRING
    print("\n3. NUMBER TO STRING (str())")
    print("-" * 40)
    
    num = 12345
    str_num = str(num)
    print(f"{num} → '{str_num}' (type: {type(str_num).__name__})")
    
    price = 29.99
    str_price = str(price)
    print(f"{price} → '{str_price}'")
    
    # BOOLEAN CONVERSIONS
    print("\n4. BOOLEAN CONVERSIONS (bool())")
    print("-" * 40)
    
    # Falsy values become False
    falsy_values = [0, 0.0, "", [], {}, None, False]
    for val in falsy_values:
        print(f"bool({repr(val)}) = {bool(val)}")
    
    # Truthy values become True
    truthy_values = [1, -1, 3.14, "Hello", [1, 2], {"key": "value"}, True]
    for val in truthy_values:
        print(f"bool({repr(val)}) = {bool(val)}")
    
    # LIST CONVERSIONS
    print("\n5. LIST CONVERSIONS (list(), tuple(), set())")
    print("-" * 40)
    
    # String to list of characters
    word = "Python"
    char_list = list(word)
    print(f"list('{word}') = {char_list}")
    
    # String to tuple
    char_tuple = tuple(word)
    print(f"tuple('{word}') = {char_tuple}")
    
    # List to set (removes duplicates)
    dup_list = [1, 2, 2, 3, 3, 3, 4]
    unique_set = set(dup_list)
    print(f"set({dup_list}) = {unique_set}")
    
    # Range to list
    range_list = list(range(5))
    print(f"list(range(5)) = {range_list}")
    
    # DICTIONARY CONVERSIONS
    print("\n6. DICTIONARY CONVERSIONS (dict())")
    print("-" * 40)
    
    # List of tuples to dict
    pairs = [("name", "Alice"), ("age", 28), ("city", "NYC")]
    dict_from_pairs = dict(pairs)
    print(f"dict({pairs}) = {dict_from_pairs}")
    
    # Two lists to dict using zip
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    dict_from_lists = dict(zip(keys, values))
    print(f"dict(zip({keys}, {values})) = {dict_from_lists}")
    
    # SAFE TYPE CASTING
    print("\n7. SAFE TYPE CASTING (with error handling)")
    print("-" * 40)
    
    def safe_int_convert(value: Any, default: int = 0) -> int:
        """Safely convert to int, returning default on failure."""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    test_values = ["42", "3.14", "abc", None, [1, 2]]
    for val in test_values:
        result = safe_int_convert(val)
        print(f"safe_int_convert({repr(val)}) = {result}")
    
    # PRACTICAL: FORM VALIDATION
    print("\n8. PRACTICAL: FORM DATA CONVERSION")
    print("-" * 40)
    
    # Simulated form data (all strings from input)
    form_data = {
        "name": "Alice Chen",
        "age": "28",
        "height": "5.6",
        "is_student": "yes",
        "courses": "Python,Data Science,Web Dev"
    }
    
    print("Raw form data (all strings):")
    for key, value in form_data.items():
        print(f"  {key}: '{value}' ({type(value).__name__})")
    
    # Convert to appropriate types
    converted_data = {
        "name": form_data["name"],  # stays string
        "age": int(form_data["age"]),  # convert to int
        "height": float(form_data["height"]),  # convert to float
        "is_student": form_data["is_student"].lower() == "yes",  # convert to bool
        "courses": [c.strip() for c in form_data["courses"].split(",")]  # convert to list
    }
    
    print("\nConverted data (appropriate types):")
    for key, value in converted_data.items():
        print(f"  {key}: {value} ({type(value).__name__})")


if __name__ == "__main__":
    demonstrate_print_basics()
    demonstrate_input_basics()
    demonstrate_type_casting()
```

---

## 🧮 Section 2: Building a CLI Calculator

A complete command-line calculator that handles user input, validates it, performs calculations, and formats output.

**SOLID Principles Applied:**
- Single Responsibility: Each operation is a separate function
- Open/Closed: New operations can be added without modifying existing code

**Design Patterns:**
- Command Pattern: Each operation is a command
- Strategy Pattern: Different calculation strategies

```python
"""
CLI CALCULATOR: COMPLETE COMMAND-LINE CALCULATOR

This section builds a complete calculator that handles user input,
validates it, performs calculations, and formats output.

SOLID Principles Applied:
- Single Responsibility: Each operation has its own function
- Open/Closed: New operations can be added

Design Patterns:
- Command Pattern: Each operation is a command
- Strategy Pattern: Different calculation strategies
"""

from typing import Dict, List, Tuple, Optional, Callable
from enum import Enum
import math
import re


class Operation(Enum):
    """Supported calculator operations."""
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "^"
    MODULUS = "%"
    SQUARE_ROOT = "sqrt"
    FACTORIAL = "fact"
    PERCENTAGE = "% of"


class Calculator:
    """
    Complete CLI calculator with multiple operations.
    
    Design Pattern: Command Pattern - Each operation is a command
    """
    
    def __init__(self):
        """Initialize calculator with operation history."""
        self.history: List[Dict] = []
        self.memory: float = 0.0
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> Tuple[float, str]:
        """Divide a by b with error handling."""
        if b == 0:
            return 0.0, "Error: Division by zero"
        return a / b, "success"
    
    def power(self, base: float, exponent: float) -> float:
        """Raise base to exponent power."""
        return base ** exponent
    
    def modulus(self, a: float, b: float) -> float:
        """Calculate remainder of a divided by b."""
        if b == 0:
            return 0.0
        return a % b
    
    def square_root(self, a: float) -> Tuple[float, str]:
        """Calculate square root with error handling."""
        if a < 0:
            return 0.0, "Error: Cannot take square root of negative number"
        return math.sqrt(a), "success"
    
    def factorial(self, n: int) -> Tuple[int, str]:
        """Calculate factorial with error handling."""
        if n < 0:
            return 0, "Error: Factorial not defined for negative numbers"
        if not isinstance(n, int) and n != int(n):
            return 0, "Error: Factorial only defined for integers"
        
        n = int(n)
        if n > 20:
            return 0, "Error: Number too large (max 20)"
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result, "success"
    
    def percentage(self, value: float, percent: float) -> float:
        """Calculate percentage of a value."""
        return value * (percent / 100)
    
    def evaluate_expression(self, expression: str) -> Tuple[float, str]:
        """
        Evaluate a mathematical expression safely.
        
        Uses a safe subset of operations (no eval of arbitrary code).
        """
        # Clean the expression
        expression = expression.strip().replace(" ", "")
        
        # Check for basic operations
        patterns = [
            (r'^(\d+\.?\d*)\+(\d+\.?\d*)$', self.add),
            (r'^(\d+\.?\d*)-(\d+\.?\d*)$', self.subtract),
            (r'^(\d+\.?\d*)\*(\d+\.?\d*)$', self.multiply),
            (r'^(\d+\.?\d*)/(\d+\.?\d*)$', self.divide),
            (r'^(\d+\.?\d*)\^(\d+\.?\d*)$', self.power),
            (r'^(\d+\.?\d*)%(\d+\.?\d*)$', self.modulus),
            (r'^sqrt\((\d+\.?\d*)\)$', lambda x, _: self.square_root(x)),
            (r'^fact\((\d+)\)$', lambda x, _: self.factorial(int(x))),
        ]
        
        for pattern, operation in patterns:
            match = re.match(pattern, expression)
            if match:
                if pattern.startswith(r'^sqrt') or pattern.startswith(r'^fact'):
                    result, error = operation(float(match.group(1)), None)
                    if error != "success":
                        return 0.0, error
                    return result, "success"
                else:
                    a, b = float(match.group(1)), float(match.group(2))
                    if operation == self.divide:
                        result, error = operation(a, b)
                        if error != "success":
                            return 0.0, error
                        return result, "success"
                    else:
                        return operation(a, b), "success"
        
        return 0.0, f"Error: Invalid expression '{expression}'"
    
    def add_to_history(self, operation: str, inputs: List, result: float) -> None:
        """Add calculation to history."""
        self.history.append({
            "operation": operation,
            "inputs": inputs,
            "result": result,
            "timestamp": __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        # Keep only last 20 items
        if len(self.history) > 20:
            self.history.pop(0)
    
    def show_history(self) -> str:
        """Format and return calculation history."""
        if not self.history:
            return "No calculations yet."
        
        lines = ["\n" + "=" * 50, "CALCULATION HISTORY", "=" * 50]
        
        for i, entry in enumerate(reversed(self.history[-10:]), 1):
            if entry["operation"] == "expression":
                lines.append(f"{i}. {entry['inputs'][0]} = {entry['result']}")
            else:
                lines.append(f"{i}. {entry['operation']} {entry['inputs']} = {entry['result']}")
            lines.append(f"   ({entry['timestamp']})")
        
        lines.append("=" * 50)
        return "\n".join(lines)
    
    def memory_store(self, value: float) -> None:
        """Store value in memory."""
        self.memory = value
        print(f"  Memory stored: {value}")
    
    def memory_recall(self) -> float:
        """Recall value from memory."""
        return self.memory
    
    def memory_clear(self) -> None:
        """Clear memory."""
        self.memory = 0.0
        print("  Memory cleared")
    
    def memory_add(self, value: float) -> None:
        """Add to memory."""
        self.memory += value
        print(f"  Memory updated: {self.memory}")
    
    def memory_subtract(self, value: float) -> None:
        """Subtract from memory."""
        self.memory -= value
        print(f"  Memory updated: {self.memory}")


class CalculatorCLI:
    """
    Command-line interface for the calculator.
    
    Design Pattern: Command Pattern - CLI commands mapped to calculator methods
    """
    
    def __init__(self):
        self.calc = Calculator()
        self.running = True
        
        # Command mapping
        self.commands: Dict[str, Callable] = {
            "help": self.show_help,
            "h": self.show_help,
            "quit": self.quit,
            "q": self.quit,
            "exit": self.quit,
            "history": self.show_history,
            "mem": self.show_memory,
            "mem_store": self.memory_store,
            "ms": self.memory_store,
            "mem_recall": self.memory_recall,
            "mr": self.memory_recall,
            "mem_clear": self.memory_clear,
            "mc": self.memory_clear,
            "mem_add": self.memory_add,
            "m+": self.memory_add,
            "mem_sub": self.memory_subtract,
            "m-": self.memory_subtract,
            "clear": self.clear_screen,
            "cls": self.clear_screen
        }
    
    def show_help(self) -> None:
        """Display help information."""
        help_text = """
╔══════════════════════════════════════════════════════════════╗
║                     CALCULATOR HELP                          ║
╠══════════════════════════════════════════════════════════════╣
║ BASIC OPERATIONS:                                            ║
║   2 + 3        Addition                                      ║
║   10 - 4       Subtraction                                   ║
║   6 * 7        Multiplication                                ║
║   15 / 3       Division                                      ║
║   2 ^ 5        Power (2 to the 5th = 32)                     ║
║   17 % 5       Modulus (remainder = 2)                       ║
║                                                              ║
║ ADVANCED OPERATIONS:                                         ║
║   sqrt(16)     Square root (result = 4)                      ║
║   fact(5)      Factorial (5! = 120)                          ║
║   100 % of 25  25% of 100 = 25                               ║
║                                                              ║
║ MEMORY OPERATIONS:                                           ║
║   ms 100       Store 100 in memory                           ║
║   mr           Recall memory value                           ║
║   m+ 50        Add 50 to memory                              ║
║   m- 25        Subtract 25 from memory                       ║
║   mc           Clear memory                                  ║
║                                                              ║
║ OTHER COMMANDS:                                              ║
║   history      Show calculation history                      ║
║   clear / cls  Clear screen                                  ║
║   help / h     Show this help                                ║
║   quit / q / exit  Exit calculator                           ║
╚══════════════════════════════════════════════════════════════╝
"""
        print(help_text)
    
    def show_history(self) -> None:
        """Display calculation history."""
        print(self.calc.show_history())
    
    def show_memory(self) -> None:
        """Display current memory value."""
        print(f"  Memory: {self.calc.memory}")
    
    def memory_store(self, value_str: str = "") -> None:
        """Store value in memory."""
        if not value_str:
            value_str = input("  Enter value to store: ")
        try:
            value = float(value_str)
            self.calc.memory_store(value)
        except ValueError:
            print("  Invalid number")
    
    def memory_recall(self) -> None:
        """Recall memory value."""
        value = self.calc.memory_recall()
        print(f"  Recalled: {value}")
    
    def memory_add(self, value_str: str = "") -> None:
        """Add to memory."""
        if not value_str:
            value_str = input("  Enter value to add: ")
        try:
            value = float(value_str)
            self.calc.memory_add(value)
        except ValueError:
            print("  Invalid number")
    
    def memory_subtract(self, value_str: str = "") -> None:
        """Subtract from memory."""
        if not value_str:
            value_str = input("  Enter value to subtract: ")
        try:
            value = float(value_str)
            self.calc.memory_subtract(value)
        except ValueError:
            print("  Invalid number")
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show_header()
    
    def show_header(self) -> None:
        """Display calculator header."""
        print("\n" + "=" * 50)
        print("        PYTHON CALCULATOR - METROMAP EDITION")
        print("=" * 50)
        print("Type 'help' for commands, 'quit' to exit\n")
    
    def quit(self) -> None:
        """Exit the calculator."""
        self.running = False
        print("\nThank you for using Python Calculator!")
        print("Goodbye! 👋\n")
    
    def process_operation(self, user_input: str) -> None:
        """Process a calculation operation."""
        user_input = user_input.strip()
        
        # Check for percentage operation
        if " % of " in user_input:
            parts = user_input.split(" % of ")
            if len(parts) == 2:
                try:
                    percent = float(parts[0])
                    value = float(parts[1])
                    result = self.calc.percentage(value, percent)
                    print(f"  {percent}% of {value} = {result}")
                    self.calc.add_to_history(f"{percent}% of {value}", [percent, value], result)
                    return
                except ValueError:
                    print("  Invalid numbers")
                    return
        
        # Evaluate expression
        result, error = self.calc.evaluate_expression(user_input)
        
        if error != "success":
            print(f"  {error}")
        else:
            # Format result (remove .0 for integers)
            if result == int(result):
                display_result = int(result)
            else:
                display_result = round(result, 6)
            print(f"  = {display_result}")
            self.calc.add_to_history("expression", [user_input], result)
    
    def run(self) -> None:
        """Run the calculator CLI main loop."""
        self.show_header()
        
        while self.running:
            try:
                user_input = input(">>> ").strip()
                
                if not user_input:
                    continue
                
                # Check if it's a command
                parts = user_input.split()
                command = parts[0].lower()
                
                if command in self.commands:
                    # Command with optional argument
                    args = " ".join(parts[1:]) if len(parts) > 1 else ""
                    if args:
                        self.commands[command](args)
                    else:
                        self.commands[command]()
                else:
                    # Treat as calculation
                    self.process_operation(user_input)
                    
            except KeyboardInterrupt:
                print("\n\nUse 'quit' to exit")
            except Exception as e:
                print(f"  Error: {e}")


def run_calculator_demo():
    """
    Demonstrate the calculator (non-interactive demo).
    """
    print("\n" + "=" * 60)
    print("SECTION 2: CLI CALCULATOR DEMONSTRATION")
    print("=" * 60)
    
    calc = Calculator()
    
    print("\n📊 CALCULATOR OPERATIONS DEMO")
    print("-" * 40)
    
    # Demonstrate operations
    test_cases = [
        ("2 + 3", calc.evaluate_expression("2+3")),
        ("10 - 4", calc.evaluate_expression("10-4")),
        ("6 * 7", calc.evaluate_expression("6*7")),
        ("15 / 3", calc.evaluate_expression("15/3")),
        ("10 / 0", calc.evaluate_expression("10/0")),
        ("2 ^ 5", calc.evaluate_expression("2^5")),
        ("17 % 5", calc.evaluate_expression("17%5")),
        ("sqrt(16)", calc.evaluate_expression("sqrt(16)")),
        ("sqrt(-4)", calc.evaluate_expression("sqrt(-4)")),
        ("fact(5)", calc.evaluate_expression("fact(5)")),
        ("100 % of 25", (calc.percentage(25, 100), "success"))
    ]
    
    for description, (result, error) in test_cases:
        if error != "success":
            print(f"  {description:15} → {error}")
        else:
            # Format result
            if isinstance(result, float) and result == int(result):
                display = int(result)
            else:
                display = round(result, 6) if isinstance(result, float) else result
            print(f"  {description:15} = {display}")
            calc.add_to_history(description.split()[0], description.split()[1:], result)
    
    # Show history
    print(calc.show_history())
    
    print("\n💡 To run the interactive calculator:")
    print("   calc_cli = CalculatorCLI()")
    print("   calc_cli.run()")


if __name__ == "__main__":
    run_calculator_demo()
```

---

## 📝 Section 3: User Registration System

A complete user registration system with comprehensive input validation, type conversion, and formatted output.

**SOLID Principles Applied:**
- Single Responsibility: Each validation rule is separate
- Open/Closed: New fields can be added without modifying existing validation

**Design Patterns:**
- Builder Pattern: Builds user object incrementally
- Factory Pattern: Creates validated user objects

```python
"""
USER REGISTRATION SYSTEM

This section builds a complete user registration system with
comprehensive input validation and type conversion.

SOLID Principles Applied:
- Single Responsibility: Each validation function has one purpose
- Open/Closed: New fields can be added

Design Patterns:
- Builder Pattern: Builds user incrementally
- Factory Pattern: Creates validated user objects
"""

from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime
import re
import hashlib


@dataclass
class User:
    """Represents a registered user."""
    username: str
    email: str
    password_hash: str
    full_name: str
    age: int
    phone: str
    address: str
    newsletter_opt_in: bool
    registered_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary for storage."""
        return {
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "age": self.age,
            "phone": self.phone,
            "address": self.address,
            "newsletter_opt_in": self.newsletter_opt_in,
            "registered_at": self.registered_at.isoformat(),
            "is_active": self.is_active
        }
    
    def get_display_name(self) -> str:
        """Get display name (first name or username)."""
        first_name = self.full_name.split()[0] if self.full_name else self.username
        return first_name


class Validator:
    """
    Validation functions for user input.
    
    Design Pattern: Strategy Pattern - Different validation strategies
    """
    
    @staticmethod
    def validate_username(username: str) -> Tuple[bool, str]:
        """
        Validate username.
        
        Rules:
        - 3-20 characters
        - Letters, numbers, underscore only
        - Must start with letter
        """
        if not username:
            return False, "Username is required"
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if len(username) > 20:
            return False, "Username must be at most 20 characters"
        
        if not username[0].isalpha():
            return False, "Username must start with a letter"
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscore"
        
        return True, "Valid"
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """
        Validate email address.
        
        Rules:
        - Must contain @
        - Must contain domain with dot
        """
        if not email:
            return False, "Email is required"
        
        if "@" not in email:
            return False, "Email must contain @ symbol"
        
        local_part, domain = email.split("@", 1)
        
        if not local_part:
            return False, "Email local part cannot be empty"
        
        if "." not in domain:
            return False, "Email domain must contain a dot"
        
        if email.count("@") > 1:
            return False, "Email cannot have multiple @ symbols"
        
        # More comprehensive regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False, "Invalid email format"
        
        return True, "Valid"
    
    @staticmethod
    def validate_password(password: str, confirm: str) -> Tuple[bool, str]:
        """
        Validate password.
        
        Rules:
        - Minimum 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character
        - Passwords match
        """
        if not password:
            return False, "Password is required"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        if not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter"
        
        if not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter"
        
        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one digit"
        
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            return False, "Password must contain at least one special character"
        
        if password != confirm:
            return False, "Passwords do not match"
        
        return True, "Valid"
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """
        Validate full name.
        
        Rules:
        - Not empty
        - At least 2 characters
        - Letters, spaces, hyphens, apostrophes only
        """
        if not name:
            return False, "Name is required"
        
        if len(name) < 2:
            return False, "Name must be at least 2 characters"
        
        if len(name) > 100:
            return False, "Name must be at most 100 characters"
        
        if not re.match(r"^[a-zA-Z\s\-']+$", name):
            return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
        
        return True, "Valid"
    
    @staticmethod
    def validate_age(age_str: str) -> Tuple[bool, int, str]:
        """
        Validate age.
        
        Rules:
        - Must be a number
        - Between 13 and 120
        """
        if not age_str:
            return False, 0, "Age is required"
        
        if not age_str.isdigit():
            return False, 0, "Age must be a number"
        
        age = int(age_str)
        
        if age < 13:
            return False, age, "Must be at least 13 years old"
        
        if age > 120:
            return False, age, "Invalid age"
        
        return True, age, "Valid"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """
        Validate phone number.
        
        Rules:
        - Optional (can be empty)
        - If provided, must be valid format
        """
        if not phone:
            return True, "Optional"
        
        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
        
        if not cleaned.isdigit():
            return False, "Phone number can only contain digits, spaces, hyphens, parentheses, and dots"
        
        if len(cleaned) < 10 or len(cleaned) > 15:
            return False, "Phone number must be 10-15 digits"
        
        return True, "Valid"
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()


class RegistrationForm:
    """
    User registration form with validation.
    
    Design Pattern: Builder Pattern - Builds user incrementally
    """
    
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.errors: Dict[str, str] = {}
        self.validator = Validator()
    
    def get_input(self, prompt: str, field_name: str, 
                  validator_func: callable, 
                  required: bool = True,
                  sensitive: bool = False) -> Optional[str]:
        """
        Get and validate user input.
        
        Args:
            prompt: Prompt to display
            field_name: Name of field for error tracking
            validator_func: Function to validate input
            required: Whether field is required
            sensitive: Whether to hide input (for passwords)
        """
        max_attempts = 3
        attempts = 0
        
        while attempts < max_attempts:
            if sensitive:
                # In real code, use getpass
                value = input(f"{prompt} ")
            else:
                value = input(f"{prompt} ").strip()
            
            if not value and not required:
                self.data[field_name] = None
                return value
            
            if not value and required:
                print(f"  ⚠️ {field_name.replace('_', ' ').title()} is required")
                attempts += 1
                continue
            
            if validator_func:
                if field_name == "password":
                    # Special handling for password confirmation
                    confirm = input("Confirm password: ")
                    is_valid, message = validator_func(value, confirm)
                elif field_name == "age":
                    is_valid, converted, message = validator_func(value)
                    if is_valid:
                        self.data[field_name] = converted
                        return value
                else:
                    is_valid, message = validator_func(value)
                    if is_valid:
                        self.data[field_name] = value
                        return value
                
                print(f"  ⚠️ {message}")
                attempts += 1
            else:
                self.data[field_name] = value
                return value
        
        raise ValueError(f"Too many invalid attempts for {field_name}")
    
    def collect_user_data(self) -> Dict[str, Any]:
        """Collect all user data through interactive prompts."""
        print("\n" + "=" * 50)
        print("        USER REGISTRATION FORM")
        print("=" * 50)
        print("Please enter the following information:\n")
        
        # Collect each field with validation
        self.get_input("Username:", "username", self.validator.validate_username)
        self.get_input("Email:", "email", self.validator.validate_email)
        self.get_input("Password:", "password", self.validator.validate_password, sensitive=True)
        self.get_input("Full Name:", "full_name", self.validator.validate_name)
        self.get_input("Age:", "age", self.validator.validate_age)
        self.get_input("Phone (optional):", "phone", self.validator.validate_phone, required=False)
        self.get_input("Address:", "address", None)
        
        # Newsletter opt-in (yes/no)
        newsletter = input("Subscribe to newsletter? (y/n): ").strip().lower()
        self.data["newsletter_opt_in"] = newsletter in ["y", "yes"]
        
        return self.data
    
    def create_user(self) -> User:
        """Create a User object from validated data."""
        return User(
            username=self.data["username"],
            email=self.data["email"],
            password_hash=self.validator.hash_password(self.data["password"]),
            full_name=self.data["full_name"],
            age=self.data["age"],
            phone=self.data.get("phone", ""),
            address=self.data.get("address", ""),
            newsletter_opt_in=self.data.get("newsletter_opt_in", False)
        )
    
    def display_confirmation(self, user: User) -> None:
        """Display registration confirmation."""
        print("\n" + "=" * 50)
        print("        REGISTRATION SUCCESSFUL!")
        print("=" * 50)
        print(f"\nWelcome, {user.get_display_name()}!")
        print(f"\nYour account has been created with:")
        print(f"  Username: {user.username}")
        print(f"  Email: {user.email}")
        print(f"  Newsletter: {'Yes' if user.newsletter_opt_in else 'No'}")
        print(f"\nA confirmation email has been sent to {user.email}")
        print("=" * 50)


class UserDatabase:
    """
    Simulated user database for registration system.
    
    Design Pattern: Repository Pattern - User storage and retrieval
    """
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.emails: Dict[str, str] = {}
    
    def username_exists(self, username: str) -> bool:
        """Check if username already exists."""
        return username in self.users
    
    def email_exists(self, email: str) -> bool:
        """Check if email already exists."""
        return email in self.emails
    
    def add_user(self, user: User) -> bool:
        """Add user to database."""
        if self.username_exists(user.username):
            print(f"  Error: Username '{user.username}' already exists")
            return False
        
        if self.email_exists(user.email):
            print(f"  Error: Email '{user.email}' already registered")
            return False
        
        self.users[user.username] = user
        self.emails[user.email] = user.username
        return True
    
    def get_user(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.users.get(username)
    
    def authenticate(self, username: str, password: str) -> Tuple[bool, Optional[User]]:
        """Authenticate user with username and password."""
        user = self.get_user(username)
        if not user:
            return False, None
        
        password_hash = Validator.hash_password(password)
        if user.password_hash == password_hash:
            return True, user
        
        return False, None


def run_registration_demo():
    """
    Demonstrate the user registration system.
    
    Uses simulated input for demonstration purposes.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: USER REGISTRATION SYSTEM")
    print("=" * 60)
    
    # Simulated registration data
    simulated_data = {
        "username": "alice_wonder",
        "email": "alice@example.com",
        "password": "SecurePass123!",
        "confirm": "SecurePass123!",
        "full_name": "Alice Wonderland",
        "age": "25",
        "phone": "555-123-4567",
        "address": "123 Wonderland Lane",
        "newsletter": "y"
    }
    
    data_index = 0
    simulated_keys = list(simulated_data.keys())
    
    def simulate_input(prompt: str) -> str:
        nonlocal data_index
        key = simulated_keys[data_index % len(simulated_keys)]
        value = str(simulated_data.get(key, ""))
        data_index += 1
        print(f"{prompt}{value} (simulated)")
        return value
    
    # Save original input
    original_input = __builtins__.input
    __builtins__.input = simulate_input
    
    try:
        print("\n📝 REGISTRATION DEMO (Using simulated input)")
        print("-" * 40)
        
        # Run registration
        form = RegistrationForm()
        form.collect_user_data()
        
        # Check for existing user (simulated)
        db = UserDatabase()
        
        if db.username_exists(form.data["username"]):
            print(f"\n  Error: Username '{form.data['username']}' already taken")
        elif db.email_exists(form.data["email"]):
            print(f"\n  Error: Email '{form.data['email']}' already registered")
        else:
            user = form.create_user()
            db.add_user(user)
            form.display_confirmation(user)
            
            # Show user data
            print("\n📊 USER DATA (stored):")
            for key, value in user.to_dict().items():
                if key != "password_hash":
                    print(f"  {key}: {value}")
    
    finally:
        # Restore original input
        __builtins__.input = original_input
    
    print("\n💡 To run the interactive registration system:")
    print("   form = RegistrationForm()")
    print("   form.collect_user_data()")
    print("   user = form.create_user()")


if __name__ == "__main__":
    run_registration_demo()
```

---

## 🎮 Section 4: Interactive Quiz System

A complete interactive quiz system that presents questions, collects answers, validates input, and provides scores.

**SOLID Principles Applied:**
- Single Responsibility: Each component has one purpose
- Open/Closed: New question types can be added

**Design Patterns:**
- Iterator Pattern: Iterates through questions
- Command Pattern: Each answer is processed as a command

```python
"""
INTERACTIVE QUIZ SYSTEM

This section builds a complete quiz system with multiple question types,
score tracking, and formatted results.

SOLID Principles Applied:
- Single Responsibility: Each component has one purpose
- Open/Closed: New question types can be added

Design Patterns:
- Iterator Pattern: Iterates through questions
- Command Pattern: Each answer processed as command
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import random


class QuestionType(Enum):
    """Types of quiz questions."""
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    NUMERIC = "numeric"
    TEXT = "text"


@dataclass
class Question:
    """Represents a quiz question."""
    text: str
    question_type: QuestionType
    correct_answer: Any
    options: Optional[List[str]] = None
    points: int = 1
    explanation: Optional[str] = None
    
    def __post_init__(self):
        """Validate question based on type."""
        if self.question_type == QuestionType.MULTIPLE_CHOICE:
            if not self.options or len(self.options) < 2:
                raise ValueError("Multiple choice questions need options")
        
        if self.question_type == QuestionType.TRUE_FALSE:
            self.options = ["True", "False"]
            if isinstance(self.correct_answer, str):
                self.correct_answer = self.correct_answer.lower() == "true"
    
    def check_answer(self, user_answer: Any) -> bool:
        """Check if user answer is correct."""
        if self.question_type == QuestionType.NUMERIC:
            try:
                return float(user_answer) == float(self.correct_answer)
            except ValueError:
                return False
        elif self.question_type == QuestionType.TEXT:
            return user_answer.strip().lower() == str(self.correct_answer).lower()
        elif self.question_type == QuestionType.TRUE_FALSE:
            if isinstance(user_answer, str):
                user_answer = user_answer.lower() in ["true", "t", "yes", "y"]
            return user_answer == self.correct_answer
        else:  # Multiple choice
            return str(user_answer).strip().lower() == str(self.correct_answer).lower()
    
    def format_for_display(self) -> str:
        """Format question for display."""
        text = f"\n📝 {self.text} (Points: {self.points})"
        
        if self.question_type == QuestionType.MULTIPLE_CHOICE and self.options:
            text += "\n"
            for i, option in enumerate(self.options, 1):
                text += f"\n  {i}. {option}"
            text += "\n\nEnter the number of your answer: "
        elif self.question_type == QuestionType.TRUE_FALSE:
            text += "\n  1. True\n  2. False\n\nEnter 1 or 2: "
        elif self.question_type == QuestionType.NUMERIC:
            text += "\n\nEnter your numeric answer: "
        else:
            text += "\n\nEnter your answer: "
        
        return text


@dataclass
class QuizResult:
    """Result of a quiz attempt."""
    quiz_name: str
    score: int
    total_points: int
    percentage: float
    answers: List[Dict] = field(default_factory=list)
    
    def get_grade(self) -> str:
        """Get letter grade based on percentage."""
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 80:
            return "B"
        elif self.percentage >= 70:
            return "C"
        elif self.percentage >= 60:
            return "D"
        else:
            return "F"
    
    def is_passing(self) -> bool:
        """Check if quiz was passed."""
        return self.percentage >= 70


class Quiz:
    """
    Interactive quiz system.
    
    Design Pattern: Iterator Pattern - Iterates through questions
    """
    
    def __init__(self, name: str, questions: List[Question]):
        self.name = name
        self.questions = questions
        self.current_question_index = 0
        self.answers: List[Dict] = []
        self.score = 0
        self.total_points = sum(q.points for q in questions)
    
    def run(self) -> QuizResult:
        """Run the complete quiz."""
        print("\n" + "=" * 50)
        print(f"        QUIZ: {self.name}")
        print("=" * 50)
        print(f"\nThis quiz has {len(self.questions)} questions")
        print(f"Total points: {self.total_points}")
        print("\nGood luck!\n")
        
        input("Press Enter to start...")
        
        for question in self.questions:
            self.ask_question(question)
        
        return self.get_results()
    
    def ask_question(self, question: Question) -> None:
        """Present a single question and collect answer."""
        print("\n" + "-" * 40)
        
        # Display question
        print(question.format_for_display(), end="")
        
        # Get answer with validation
        max_attempts = 2
        attempts = 0
        
        while attempts < max_attempts:
            user_answer = input().strip()
            
            # Convert answer based on question type
            if question.question_type == QuestionType.MULTIPLE_CHOICE:
                if user_answer.isdigit():
                    idx = int(user_answer) - 1
                    if 0 <= idx < len(question.options):
                        user_answer = question.options[idx]
                    else:
                        print(f"  Invalid choice. Please enter 1-{len(question.options)}")
                        attempts += 1
                        continue
                else:
                    # Allow direct text answer
                    pass
            
            elif question.question_type == QuestionType.TRUE_FALSE:
                if user_answer in ["1", "True", "true", "t"]:
                    user_answer = True
                elif user_answer in ["2", "False", "false", "f"]:
                    user_answer = False
                else:
                    print("  Invalid choice. Please enter 1 (True) or 2 (False)")
                    attempts += 1
                    continue
            
            elif question.question_type == QuestionType.NUMERIC:
                try:
                    user_answer = float(user_answer)
                except ValueError:
                    print("  Please enter a number")
                    attempts += 1
                    continue
            
            # Check answer
            is_correct = question.check_answer(user_answer)
            points_earned = question.points if is_correct else 0
            
            if is_correct:
                self.score += points_earned
                print(f"\n  ✅ Correct! (+{points_earned} points)")
            else:
                correct_display = question.correct_answer
                if question.question_type == QuestionType.MULTIPLE_CHOICE:
                    # Find the correct option text
                    pass
                print(f"\n  ❌ Incorrect. The correct answer is: {correct_display}")
            
            if question.explanation:
                print(f"  📚 Explanation: {question.explanation}")
            
            # Store answer
            self.answers.append({
                "question": question.text,
                "user_answer": user_answer,
                "correct_answer": question.correct_answer,
                "is_correct": is_correct,
                "points_earned": points_earned,
                "points_possible": question.points
            })
            
            break
        
        else:
            print("  No more attempts. Moving to next question.")
            self.answers.append({
                "question": question.text,
                "user_answer": None,
                "correct_answer": question.correct_answer,
                "is_correct": False,
                "points_earned": 0,
                "points_possible": question.points
            })
    
    def get_results(self) -> QuizResult:
        """Calculate and display quiz results."""
        percentage = (self.score / self.total_points) * 100 if self.total_points > 0 else 0
        
        print("\n" + "=" * 50)
        print("        QUIZ RESULTS")
        print("=" * 50)
        print(f"\nQuiz: {self.name}")
        print(f"Score: {self.score} / {self.total_points}")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Grade: {QuizResult('', 0, 0, 0).get_grade() if hasattr(QuizResult('', 0, 0, 0), 'get_grade') else self._get_grade(percentage)}")
        
        if percentage >= 70:
            print("\n  🎉 Congratulations! You passed!")
        else:
            print("\n  📚 Keep studying and try again!")
        
        # Show detailed results
        print("\n" + "-" * 40)
        print("DETAILED RESULTS:")
        print("-" * 40)
        
        for i, answer in enumerate(self.answers, 1):
            status = "✅" if answer["is_correct"] else "❌"
            print(f"\n{status} Question {i}: {answer['question'][:50]}...")
            print(f"   Your answer: {answer['user_answer']}")
            if not answer["is_correct"]:
                print(f"   Correct answer: {answer['correct_answer']}")
            print(f"   Points: {answer['points_earned']}/{answer['points_possible']}")
        
        return QuizResult(
            quiz_name=self.name,
            score=self.score,
            total_points=self.total_points,
            percentage=percentage,
            answers=self.answers
        )
    
    def _get_grade(self, percentage: float) -> str:
        """Get letter grade."""
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"


class QuizBank:
    """
    Repository of pre-defined quizzes.
    
    Design Pattern: Repository Pattern - Stores and provides quizzes
    """
    
    @staticmethod
    def get_python_basics_quiz() -> Quiz:
        """Get Python basics quiz."""
        questions = [
            Question(
                text="What is the correct way to create a variable in Python?",
                question_type=QuestionType.MULTIPLE_CHOICE,
                correct_answer="variable = 5",
                options=["var 5", "variable = 5", "5 = variable", "let variable = 5"],
                points=1,
                explanation="Python uses the assignment operator (=) with variable name on the left."
            ),
            Question(
                text="Which data type is immutable?",
                question_type=QuestionType.MULTIPLE_CHOICE,
                correct_answer="tuple",
                options=["list", "dict", "tuple", "set"],
                points=1,
                explanation="Tuples cannot be changed after creation, making them immutable."
            ),
            Question(
                text="What does the 'len()' function do?",
                question_type=QuestionType.MULTIPLE_CHOICE,
                correct_answer="Returns the length of a sequence",
                options=["Converts to lowercase", "Returns the length of a sequence", "Creates a new list", "Removes duplicates"],
                points=1,
                explanation="len() returns the number of items in a container like a list, string, or tuple."
            ),
            Question(
                text="Python uses indentation to define code blocks.",
                question_type=QuestionType.TRUE_FALSE,
                correct_answer=True,
                points=1,
                explanation="Unlike languages that use braces, Python uses indentation (usually 4 spaces) to define blocks."
            ),
            Question(
                text="What is the result of 10 // 3?",
                question_type=QuestionType.NUMERIC,
                correct_answer=3,
                points=1,
                explanation="// is floor division - it returns the integer quotient, rounding down."
            )
        ]
        
        return Quiz("Python Basics", questions)
    
    @staticmethod
    def get_programming_quiz() -> Quiz:
        """Get general programming quiz."""
        questions = [
            Question(
                text="What does 'IDE' stand for?",
                question_type=QuestionType.MULTIPLE_CHOICE,
                correct_answer="Integrated Development Environment",
                options=["Integrated Data Entry", "Integrated Development Environment", "Internal Debugging Engine", "Interactive Display Editor"],
                points=1,
                explanation="IDE stands for Integrated Development Environment, software that provides tools for programming."
            ),
            Question(
                text="What is a variable?",
                question_type=QuestionType.TEXT,
                correct_answer="a named storage location",
                points=1,
                explanation="A variable is a named location in memory that stores a value."
            ),
            Question(
                text="A loop that never ends is called an infinite loop.",
                question_type=QuestionType.TRUE_FALSE,
                correct_answer=True,
                points=1,
                explanation="An infinite loop occurs when the loop condition never becomes false."
            ),
            Question(
                text="What is the time complexity of binary search?",
                question_type=QuestionType.MULTIPLE_CHOICE,
                correct_answer="O(log n)",
                options=["O(1)", "O(n)", "O(log n)", "O(n²)"],
                points=1,
                explanation="Binary search repeatedly divides the search space in half, giving O(log n) complexity."
            )
        ]
        
        return Quiz("Programming Fundamentals", questions)


def run_quiz_demo():
    """
    Demonstrate the interactive quiz system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: INTERACTIVE QUIZ SYSTEM")
    print("=" * 60)
    
    # Get available quizzes
    quiz_bank = QuizBank()
    quizzes = [
        ("Python Basics", quiz_bank.get_python_basics_quiz()),
        ("Programming Fundamentals", quiz_bank.get_programming_quiz())
    ]
    
    print("\n📚 AVAILABLE QUIZZES")
    print("-" * 40)
    for i, (name, _) in enumerate(quizzes, 1):
        print(f"  {i}. {name}")
    
    # For demo, run the first quiz with simulated answers
    print("\n" + "-" * 40)
    print("Running Python Basics Quiz (with simulated answers)")
    print("-" * 40)
    
    # Simulate answers for demonstration
    simulated_answers = ["2", "3", "2", "1", "3"]
    answer_index = 0
    
    original_input = __builtins__.input
    
    def simulate_quiz_input(prompt):
        nonlocal answer_index
        if "Press Enter to start" in prompt:
            return ""
        if answer_index < len(simulated_answers):
            answer = simulated_answers[answer_index]
            answer_index += 1
            print(f"{answer} (simulated)")
            return answer
        return ""
    
    try:
        __builtins__.input = simulate_quiz_input
        quiz = quiz_bank.get_python_basics_quiz()
        result = quiz.run()
        
        print("\n" + "=" * 50)
        print("QUIZ COMPLETED!")
        print("=" * 50)
        
    finally:
        __builtins__.input = original_input
    
    print("\n💡 To run an interactive quiz:")
    print("   quiz = QuizBank.get_python_basics_quiz()")
    print("   result = quiz.run()")
    print("   print(f'Your score: {result.percentage:.1f}%')")


if __name__ == "__main__":
    run_quiz_demo()
```

---

## 🏪 Section 5: Complete Point of Sale (POS) Terminal

A complete point-of-sale terminal that integrates everything learned in Foundations Station.

**SOLID Principles Applied:**
- Single Responsibility: Each component has one purpose
- Dependency Inversion: Depends on abstractions

**Design Patterns:**
- Command Pattern: POS commands
- Builder Pattern: Builds order incrementally
- Singleton Pattern: Single POS instance

```python
"""
COMPLETE POINT OF SALE (POS) TERMINAL

This section builds a complete POS terminal integrating all
Foundations Station concepts.

SOLID Principles Applied:
- Single Responsibility: Each component has one purpose
- Dependency Inversion: Depends on abstractions

Design Patterns:
- Command Pattern: POS commands
- Builder Pattern: Builds order incrementally
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class Product:
    """Product in the inventory."""
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
    """Item in shopping cart."""
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


@dataclass
class Order:
    """Customer order."""
    order_id: str
    items: List[CartItem]
    subtotal: float
    tax: float
    discount: float
    total: float
    payment_method: str
    status: str
    timestamp: datetime
    
    def to_dict(self) -> Dict:
        """Convert order to dictionary."""
        return {
            "order_id": self.order_id,
            "items": [
                {
                    "sku": item.product.sku,
                    "name": item.product.name,
                    "quantity": item.quantity,
                    "price": item.product.price,
                    "subtotal": item.subtotal()
                }
                for item in self.items
            ],
            "subtotal": self.subtotal,
            "tax": self.tax,
            "discount": self.discount,
            "total": self.total,
            "payment_method": self.payment_method,
            "status": self.status,
            "timestamp": self.timestamp.isoformat()
        }


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
            ("P002", "Mouse", 29.99, "Electronics", 0.08),
            ("P003", "Keyboard", 89.99, "Electronics", 0.08),
            ("P004", "Monitor", 299.99, "Electronics", 0.08),
            ("P005", "Notebook", 4.99, "Stationery", 0.05),
            ("P006", "Pen", 1.99, "Stationery", 0.05),
            ("P007", "Backpack", 49.99, "Accessories", 0.07),
            ("P008", "Water Bottle", 19.99, "Accessories", 0.07)
        ]
        
        for sku, name, price, category, tax_rate in sample_products:
            self.products[sku] = Product(sku, name, price, category, tax_rate)
    
    def get_product(self, sku: str) -> Optional[Product]:
        """Get product by SKU."""
        return self.products.get(sku)
    
    def search_products(self, query: str) -> List[Product]:
        """Search products by name or SKU."""
        query_lower = query.lower()
        results = []
        for product in self.products.values():
            if query_lower in product.name.lower() or query_lower in product.sku.lower():
                results.append(product)
        return results
    
    def list_all(self) -> List[Product]:
        """List all products."""
        return list(self.products.values())


class ShoppingCart:
    """
    Shopping cart management.
    
    Design Pattern: Builder Pattern - Builds order incrementally
    """
    
    def __init__(self):
        self.items: List[CartItem] = []
        self.discount_code: Optional[str] = None
        self.discount_percent: float = 0.0
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add item to cart."""
        # Check if already in cart
        for item in self.items:
            if item.product.sku == product.sku:
                item.quantity += quantity
                print(f"  Updated {product.name}: {item.quantity} total")
                return
        
        self.items.append(CartItem(product, quantity))
        print(f"  Added {quantity}x {product.name}")
    
    def remove_item(self, sku: str) -> None:
        """Remove item from cart."""
        original_count = len(self.items)
        self.items = [item for item in self.items if item.product.sku != sku]
        if len(self.items) < original_count:
            print(f"  Removed product {sku}")
        else:
            print(f"  Product {sku} not found")
    
    def update_quantity(self, sku: str, quantity: int) -> None:
        """Update item quantity."""
        if quantity <= 0:
            self.remove_item(sku)
            return
        
        for item in self.items:
            if item.product.sku == sku:
                item.quantity = quantity
                print(f"  Updated quantity to {quantity}")
                return
        
        print(f"  Product {sku} not found")
    
    def apply_discount(self, code: str, percent: float) -> None:
        """Apply discount to cart."""
        self.discount_code = code
        self.discount_percent = percent
        print(f"  Applied {percent}% discount with code: {code}")
    
    def subtotal(self) -> float:
        """Calculate subtotal."""
        return sum(item.subtotal() for item in self.items)
    
    def discount_amount(self) -> float:
        """Calculate discount amount."""
        return self.subtotal() * (self.discount_percent / 100)
    
    def tax(self) -> float:
        """Calculate total tax."""
        taxable_subtotal = self.subtotal() - self.discount_amount()
        return sum(item.product.tax_rate for item in self.items) / len(self.items) * taxable_subtotal if self.items else 0
    
    def total(self) -> float:
        """Calculate final total."""
        return self.subtotal() - self.discount_amount() + self.tax()
    
    def item_count(self) -> int:
        """Get total number of items."""
        return sum(item.quantity for item in self.items)
    
    def is_empty(self) -> bool:
        """Check if cart is empty."""
        return len(self.items) == 0
    
    def clear(self) -> None:
        """Clear the cart."""
        self.items.clear()
        self.discount_code = None
        self.discount_percent = 0.0
    
    def display(self) -> None:
        """Display cart contents."""
        if self.is_empty():
            print("\n  Cart is empty")
            return
        
        print("\n" + "-" * 40)
        print("CART CONTENTS:")
        print("-" * 40)
        
        for item in self.items:
            print(f"  {item.quantity}x {item.product.name}")
            print(f"     @ ${item.product.price:.2f} = ${item.subtotal():.2f}")
        
        print("-" * 40)
        print(f"  Subtotal: ${self.subtotal():.2f}")
        if self.discount_percent > 0:
            print(f"  Discount ({self.discount_percent}%): -${self.discount_amount():.2f}")
        print(f"  Tax: ${self.tax():.2f}")
        print(f"  TOTAL: ${self.total():.2f}")
        print("-" * 40)


class POSTerminal:
    """
    Complete Point of Sale Terminal.
    
    Design Pattern: Command Pattern - POS commands
    """
    
    def __init__(self):
        self.inventory = Inventory()
        self.cart = ShoppingCart()
        self.orders: List[Order] = []
        self.order_counter = 1000
        self.running = True
    
    def display_menu(self) -> None:
        """Display main menu."""
        print("\n" + "=" * 50)
        print("        POINT OF SALE TERMINAL")
        print("=" * 50)
        print("\n1. Browse Products")
        print("2. Search Products")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Update Cart")
        print("6. Apply Discount")
        print("7. Checkout")
        print("8. View Orders")
        print("9. Help")
        print("0. Exit")
        print("-" * 50)
    
    def browse_products(self) -> None:
        """Display all products."""
        print("\n" + "-" * 40)
        print("PRODUCT CATALOG:")
        print("-" * 40)
        print(f"{'SKU':<8} {'Name':<20} {'Price':<10} {'Category':<12}")
        print("-" * 50)
        
        for product in self.inventory.list_all():
            print(f"{product.sku:<8} {product.name:<20} ${product.price:<9.2f} {product.category:<12}")
        print("-" * 50)
    
    def search_products(self) -> None:
        """Search for products."""
        query = input("\nEnter search term: ").strip()
        if not query:
            print("  Please enter a search term")
            return
        
        results = self.inventory.search_products(query)
        
        if not results:
            print(f"  No products found matching '{query}'")
            return
        
        print(f"\nFound {len(results)} products:")
        print("-" * 40)
        for product in results:
            print(f"  {product.sku}: {product.name} - ${product.price:.2f}")
    
    def add_to_cart(self) -> None:
        """Add product to cart."""
        sku = input("\nEnter product SKU: ").strip().upper()
        product = self.inventory.get_product(sku)
        
        if not product:
            print(f"  Product '{sku}' not found")
            return
        
        quantity_str = input("Enter quantity (default 1): ").strip()
        quantity = int(quantity_str) if quantity_str.isdigit() else 1
        
        if quantity <= 0:
            print("  Quantity must be positive")
            return
        
        self.cart.add_item(product, quantity)
    
    def view_cart(self) -> None:
        """Display current cart."""
        self.cart.display()
    
    def update_cart(self) -> None:
        """Update cart items."""
        if self.cart.is_empty():
            print("  Cart is empty")
            return
        
        self.cart.display()
        print("\nUpdate options:")
        print("  1. Remove item")
        print("  2. Change quantity")
        print("  3. Clear cart")
        print("  0. Cancel")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            sku = input("Enter SKU to remove: ").strip().upper()
            self.cart.remove_item(sku)
        elif choice == "2":
            sku = input("Enter SKU to update: ").strip().upper()
            quantity_str = input("Enter new quantity: ").strip()
            if quantity_str.isdigit():
                self.cart.update_quantity(sku, int(quantity_str))
            else:
                print("  Invalid quantity")
        elif choice == "3":
            confirm = input("Clear entire cart? (y/n): ").strip().lower()
            if confirm == "y":
                self.cart.clear()
                print("  Cart cleared")
        elif choice == "0":
            return
        else:
            print("  Invalid option")
    
    def apply_discount(self) -> None:
        """Apply discount to cart."""
        if self.cart.is_empty():
            print("  Cart is empty. Add items first.")
            return
        
        code = input("\nEnter discount code: ").strip().upper()
        
        # Simple discount validation
        valid_codes = {
            "SAVE10": 10,
            "SAVE20": 20,
            "WELCOME": 15,
            "FLASH": 25
        }
        
        if code not in valid_codes:
            print(f"  Invalid discount code: {code}")
            return
        
        percent = valid_codes[code]
        self.cart.apply_discount(code, percent)
    
    def checkout(self) -> None:
        """Process checkout."""
        if self.cart.is_empty():
            print("  Cannot checkout: Cart is empty")
            return
        
        print("\n" + "=" * 50)
        print("        CHECKOUT")
        print("=" * 50)
        
        self.cart.display()
        
        print("\nPayment methods:")
        print("  1. Credit Card")
        print("  2. Debit Card")
        print("  3. Cash")
        print("  4. Gift Card")
        
        payment_choice = input("\nSelect payment method: ").strip()
        payment_methods = {"1": "Credit Card", "2": "Debit Card", "3": "Cash", "4": "Gift Card"}
        
        if payment_choice not in payment_methods:
            print("  Invalid payment method")
            return
        
        payment_method = payment_methods[payment_choice]
        total = self.cart.total()
        
        print(f"\nTotal due: ${total:.2f}")
        
        if payment_method == "Cash":
            cash_str = input("Enter cash amount: ").strip()
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
        
        # Create order
        self.order_counter += 1
        order = Order(
            order_id=f"ORD-{self.order_counter}",
            items=self.cart.items.copy(),
            subtotal=self.cart.subtotal(),
            tax=self.cart.tax(),
            discount=self.cart.discount_amount(),
            total=total,
            payment_method=payment_method,
            status="completed",
            timestamp=datetime.now()
        )
        
        self.orders.append(order)
        
        # Print receipt
        self.print_receipt(order)
        
        # Clear cart
        self.cart.clear()
        
        print("\n  ✅ Checkout complete! Thank you for shopping!")
    
    def print_receipt(self, order: Order) -> None:
        """Print order receipt."""
        print("\n" + "=" * 50)
        print("        RECEIPT")
        print("=" * 50)
        print(f"Order #: {order.order_id}")
        print(f"Date: {order.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
        
        for item in order.items:
            print(f"{item.quantity}x {item.product.name}")
            print(f"  ${item.product.price:.2f} each = ${item.subtotal():.2f}")
        
        print("-" * 50)
        print(f"Subtotal: ${order.subtotal:.2f}")
        if order.discount > 0:
            print(f"Discount: -${order.discount:.2f}")
        print(f"Tax: ${order.tax:.2f}")
        print(f"TOTAL: ${order.total:.2f}")
        print(f"Payment: {order.payment_method}")
        print("=" * 50)
    
    def view_orders(self) -> None:
        """View order history."""
        if not self.orders:
            print("\n  No orders yet")
            return
        
        print("\n" + "-" * 40)
        print("ORDER HISTORY:")
        print("-" * 40)
        
        for order in reversed(self.orders[-10:]):
            print(f"\n  {order.order_id} - {order.timestamp.strftime('%Y-%m-%d %H:%M')}")
            print(f"    Items: {len(order.items)}")
            print(f"    Total: ${order.total:.2f}")
            print(f"    Status: {order.status}")
    
    def show_help(self) -> None:
        """Display help information."""
        help_text = """
╔══════════════════════════════════════════════════════════════╗
║                    POS TERMINAL HELP                         ║
╠══════════════════════════════════════════════════════════════╣
║ 1. Browse Products - View all available products             ║
║ 2. Search Products - Find products by name or SKU            ║
║ 3. Add to Cart - Add a product by SKU and quantity           ║
║ 4. View Cart - Display current cart contents                 ║
║ 5. Update Cart - Remove items or change quantities           ║
║ 6. Apply Discount - Enter discount code for savings          ║
║ 7. Checkout - Complete purchase and print receipt            ║
║ 8. View Orders - See order history                           ║
║ 9. Help - Show this help                                     ║
║ 0. Exit - Close the POS terminal                             ║
╚══════════════════════════════════════════════════════════════╝
"""
        print(help_text)
    
    def run(self) -> None:
        """Run the POS terminal main loop."""
        print("\n" + "=" * 60)
        print("    WELCOME TO METROMAP POINT OF SALE")
        print("=" * 60)
        
        while self.running:
            self.display_menu()
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self.browse_products()
            elif choice == "2":
                self.search_products()
            elif choice == "3":
                self.add_to_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.update_cart()
            elif choice == "6":
                self.apply_discount()
            elif choice == "7":
                self.checkout()
            elif choice == "8":
                self.view_orders()
            elif choice == "9":
                self.show_help()
            elif choice == "0":
                print("\nThank you for using Metromap POS!")
                print("Goodbye! 👋")
                self.running = False
            else:
                print("  Invalid choice. Enter 0-9")
            
            if self.running:
                input("\nPress Enter to continue...")


def run_pos_demo():
    """
    Run a quick demonstration of the POS terminal.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: POINT OF SALE TERMINAL")
    print("=" * 60)
    
    pos = POSTerminal()
    
    # Quick demo - show features without full interaction
    print("\n📦 POS TERMINAL FEATURES")
    print("-" * 40)
    
    print("\n1. Inventory loaded:")
    for product in pos.inventory.list_all()[:5]:
        print(f"   {product.sku}: {product.name} - ${product.price:.2f}")
    print("   ...")
    
    print("\n2. Shopping cart operations:")
    product = pos.inventory.get_product("P001")
    pos.cart.add_item(product, 1)
    product = pos.inventory.get_product("P002")
    pos.cart.add_item(product, 2)
    pos.cart.display()
    
    print("\n3. Discount application:")
    pos.cart.apply_discount("SAVE10", 10)
    pos.cart.display()
    
    print("\n💡 To run the full interactive POS:")
    print("   pos = POSTerminal()")
    print("   pos.run()")


if __name__ == "__main__":
    run_pos_demo()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **print() Function** – Display output with custom separators (sep), endings (end), and file output. Use f-strings for formatted output.

- **input() Function** – Collect user input as strings. Always validate and convert input before use.

- **Type Casting** – Convert between types: int(), float(), str(), bool(), list(), dict(). Handle conversion errors with try-except.

- **CLI Calculator** – Build interactive calculator with memory, history, and multiple operations. Validate numeric input.

- **User Registration** – Comprehensive validation for username, email, password, age, phone. Hash passwords for security.

- **Interactive Quiz** – Multiple question types (multiple choice, true/false, numeric, text). Track scores and provide feedback.

- **Point of Sale Terminal** – Complete POS with inventory, cart, discounts, checkout, receipts, and order history.

- **SOLID Principles Applied** – Single Responsibility (each function has one purpose), Open/Closed (extensible), Dependency Inversion (abstractions).

- **Design Patterns Used** – Adapter Pattern (I/O functions), Command Pattern (calculator/POS commands), Builder Pattern (order building), Repository Pattern (data storage), Iterator Pattern (quiz questions).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Nested Logic – Conditions Inside Loops

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Defining Functions – The Workhorses of Python (Series B, Story 1)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **12** | **40** | **23%** |

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

**Next Story:** Series B, Story 1: The 2026 Python Metromap: Defining Functions – The Workhorses of Python

---

## 📝 Your Invitation

**Congratulations! You've completed Foundations Station!**

You've mastered the core building blocks of Python:
- Variables and Data Types
- Collections (Lists, Tuples, Dicts, Sets)
- Operators (Arithmetic, Comparison, Logical, Assignment, Membership)
- Control Flow (if, elif, else)
- Loops (for, while, break, continue)
- Nested Logic (Conditions inside loops, nested loops)
- Input/Output and Type Casting

Now build something with what you've learned:

1. **Build a calculator** – Add more operations (trigonometry, logarithms). Add a graphical interface.

2. **Create a registration system** – Add password strength meter. Send confirmation emails.

3. **Build a quiz system** – Load questions from JSON files. Add timers and leaderboards.

4. **Create a POS terminal** – Add barcode scanning. Integrate with payment gateways.

5. **Build a data entry system** – Create forms for any data. Export to CSV/JSON.

**You've mastered Foundations Station. Next stop: Functions & Modules Yard!**

---

*Found this helpful? Clap, comment, and share what you built. Next stop: Functions!* 🚇