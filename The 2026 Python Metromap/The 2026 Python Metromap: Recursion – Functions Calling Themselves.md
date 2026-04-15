# The 2026 Python Metromap: Recursion – Functions Calling Themselves

## Series B: Functions & Modules Yard | Story 5 of 6

![The 2026 Python Metromap/images/Recursion – Functions Calling Themselves](images/Recursion – Functions Calling Themselves.png)

## 📖 Introduction

**Welcome to the fifth stop on the Functions & Modules Yard Line.**

You've mastered defining functions, passing arguments, returning values, and using lambda functions. But there's a special kind of function that calls itself—a recursive function. At first, this seems impossible or dangerous. How can a function call itself without causing an infinite loop?

Recursion is a powerful technique where a function solves a problem by breaking it down into smaller, identical subproblems. Each recursive call works on a smaller piece of the original problem until it reaches a base case—the simplest possible version that can be solved directly. Recursion is especially elegant for problems with recursive structure: directory trees, nested data, mathematical sequences, and divide-and-conquer algorithms.

This story—**The 2026 Python Metromap: Recursion – Functions Calling Themselves**—is your guide to thinking recursively. We'll start with the classic factorial example, then explore practical applications: traversing directory trees, navigating nested data structures, implementing recursive search algorithms, solving the Tower of Hanoi puzzle, and building a complete file system analyzer that recursively processes directories.

**Let's call ourselves.**

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

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines.

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver. **⬅️ YOU ARE HERE**

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔄 Section 1: Recursion Basics – The Factorial Example

Recursion is a function that calls itself. Every recursive function needs two essential parts: a base case (stopping condition) and a recursive case (where the function calls itself with a smaller input).

**SOLID Principle Applied: Single Responsibility** – Each recursive call handles one level of the problem.

**Design Pattern: Template Method Pattern** – The recursive structure defines the algorithm skeleton.

```python
"""
RECURSION BASICS: THE FACTORIAL EXAMPLE

This section covers the fundamentals of recursive functions.

SOLID Principle: Single Responsibility
- Each recursive call handles one level of the problem

Design Pattern: Template Method Pattern
- Recursive structure defines algorithm skeleton
"""

from typing import List, Any, Optional
import sys


def demonstrate_factorial():
    """
    Demonstrates recursion with the classic factorial example.
    
    Factorial: n! = n × (n-1) × (n-2) × ... × 1
    Base case: 0! = 1, 1! = 1
    Recursive case: n! = n × (n-1)!
    """
    print("=" * 60)
    print("SECTION 1A: FACTORIAL - THE CLASSIC EXAMPLE")
    print("=" * 60)
    
    # RECURSIVE FACTORIAL
    print("\n1. RECURSIVE FACTORIAL")
    print("-" * 40)
    
    def factorial_recursive(n: int) -> int:
        """
        Calculate factorial using recursion.
        
        Args:
            n: Non-negative integer
            
        Returns:
            n! (n factorial)
        """
        # Base case: stop recursion
        if n <= 1:
            print(f"    Base case: factorial({n}) = 1")
            return 1
        
        # Recursive case: call self with smaller input
        print(f"    factorial({n}) = {n} × factorial({n-1})")
        result = n * factorial_recursive(n - 1)
        print(f"    factorial({n}) = {result}")
        return result
    
    result = factorial_recursive(5)
    print(f"\n  factorial(5) = {result}")
    
    # VISUALIZING THE CALL STACK
    print("\n2. VISUALIZING THE CALL STACK")
    print("-" * 40)
    
    def factorial_with_trace(n: int, depth: int = 0) -> int:
        """Factorial with call stack visualization."""
        indent = "  " * depth
        print(f"{indent}→ factorial({n}) called")
        
        if n <= 1:
            print(f"{indent}← factorial({n}) returns 1")
            return 1
        
        result = n * factorial_with_trace(n - 1, depth + 1)
        print(f"{indent}← factorial({n}) returns {result}")
        return result
    
    print("  Call stack visualization:")
    factorial_with_trace(4)
    
    # ITERATIVE VERSION (for comparison)
    print("\n3. ITERATIVE FACTORIAL (vs Recursive)")
    print("-" * 40)
    
    def factorial_iterative(n: int) -> int:
        """Calculate factorial using iteration."""
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    print(f"  Recursive factorial(5) = {factorial_recursive(5)}")
    print(f"  Iterative factorial(5) = {factorial_iterative(5)}")
    print("\n  Recursive: Elegant but uses more memory (call stack)")
    print("  Iterative: More efficient but less elegant")


def demonstrate_recursion_components():
    """
    Demonstrates the essential components of recursion.
    
    Every recursive function needs:
    1. Base case(s) - when to stop
    2. Recursive case(s) - how to break down the problem
    3. Progress toward base case - each call gets closer to stopping
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ESSENTIAL RECURSION COMPONENTS")
    print("=" * 60)
    
    # COUNTDOWN EXAMPLE
    print("\n1. COUNTDOWN - Simple Recursion")
    print("-" * 40)
    
    def countdown(n: int) -> None:
        """Count down from n to 1."""
        if n <= 0:
            print("  Blast off! 🚀")
            return
        
        print(f"  {n}...")
        countdown(n - 1)
    
    countdown(5)
    
    # SUM OF NUMBERS
    print("\n2. SUM OF NUMBERS")
    print("-" * 40)
    
    def sum_range(n: int) -> int:
        """
        Sum all numbers from 1 to n.
        
        Base case: sum_range(1) = 1
        Recursive case: sum_range(n) = n + sum_range(n-1)
        """
        if n <= 1:
            return n
        return n + sum_range(n - 1)
    
    print(f"  sum_range(10) = {sum_range(10)}")
    print(f"  sum_range(100) = {sum_range(100)}")
    
    # POWER FUNCTION
    print("\n3. POWER FUNCTION (Exponentiation)")
    print("-" * 40)
    
    def power(base: int, exponent: int) -> int:
        """
        Calculate base raised to exponent using recursion.
        
        Base case: power(base, 0) = 1
        Recursive case: power(base, n) = base × power(base, n-1)
        """
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        return base * power(base, exponent - 1)
    
    print(f"  power(2, 0) = {power(2, 0)}")
    print(f"  power(2, 1) = {power(2, 1)}")
    print(f"  power(2, 5) = {power(2, 5)}")
    print(f"  power(3, 4) = {power(3, 4)}")
    
    # FIBONACCI SEQUENCE
    print("\n4. FIBONACCI SEQUENCE")
    print("-" * 40)
    
    def fibonacci(n: int) -> int:
        """
        Calculate nth Fibonacci number.
        
        Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
        Base cases: fib(0) = 0, fib(1) = 1
        Recursive case: fib(n) = fib(n-1) + fib(n-2)
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print("  First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"    fib({i}) = {fibonacci(i)}")
    
    # MEMOIZED FIBONACCI (Optimization)
    print("\n5. MEMOIZED FIBONACCI (with caching)")
    print("-" * 40)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fibonacci_memoized(n: int) -> int:
        """Fibonacci with memoization for performance."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    
    import time
    
    n = 35
    start = time.time()
    result1 = fibonacci(n)
    time1 = time.time() - start
    
    start = time.time()
    result2 = fibonacci_memoized(n)
    time2 = time.time() - start
    
    print(f"  fibonacci({n}) = {result1} (took {time1:.4f}s)")
    print(f"  fibonacci_memoized({n}) = {result2} (took {time2:.4f}s)")
    print("  ⚠️ Without memoization, Fibonacci is O(2^n) - very slow!")
    
    # RECURSION LIMIT
    print("\n6. PYTHON RECURSION LIMIT")
    print("-" * 40)
    
    print(f"  Default recursion limit: {sys.getrecursionlimit()}")
    
    def deep_recursion(n: int) -> int:
        """Function that recurses deeply."""
        if n <= 0:
            return 0
        return 1 + deep_recursion(n - 1)
    
    try:
        result = deep_recursion(1500)
        print(f"  deep_recursion(1500) succeeded")
    except RecursionError as e:
        print(f"  RecursionError: {e}")
    
    print("\n  To increase recursion limit:")
    print("  sys.setrecursionlimit(10000)")
    print("  ⚠️ Be careful - very deep recursion can cause stack overflow")


def demonstrate_tail_recursion():
    """
    Demonstrates tail recursion concept.
    
    Tail recursion is when the recursive call is the last operation.
    Python doesn't optimize tail recursion, but understanding the concept is valuable.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: TAIL RECURSION")
    print("=" * 60)
    
    # NON-TAIL RECURSIVE (needs to multiply after returning)
    print("\n1. NON-TAIL RECURSIVE FACTORIAL")
    print("-" * 40)
    
    def factorial_non_tail(n: int) -> int:
        """Standard factorial - not tail recursive."""
        if n <= 1:
            return 1
        # Multiplication happens AFTER the recursive call returns
        return n * factorial_non_tail(n - 1)
    
    # TAIL RECURSIVE (uses accumulator)
    print("\n2. TAIL RECURSIVE FACTORIAL")
    print("-" * 40)
    
    def factorial_tail(n: int, accumulator: int = 1) -> int:
        """
        Tail recursive factorial.
        
        The recursive call is the LAST operation.
        Args:
            n: Number to calculate factorial for
            accumulator: Running product (default 1)
        """
        if n <= 1:
            return accumulator
        # Recursive call is the last operation
        return factorial_tail(n - 1, n * accumulator)
    
    print(f"  factorial_non_tail(5) = {factorial_non_tail(5)}")
    print(f"  factorial_tail(5) = {factorial_tail(5)}")
    
    # TAIL RECURSIVE SUM
    print("\n3. TAIL RECURSIVE SUM")
    print("-" * 40)
    
    def sum_tail(n: int, accumulator: int = 0) -> int:
        """Tail recursive sum of numbers 1 to n."""
        if n <= 0:
            return accumulator
        return sum_tail(n - 1, accumulator + n)
    
    print(f"  sum_tail(10) = {sum_tail(10)}")
    print(f"  sum_tail(100) = {sum_tail(100)}")
    
    # WHY TAIL RECURSION MATTERS (in languages that optimize it)
    print("\n4. WHY TAIL RECURSION?")
    print("-" * 40)
    
    print("""
    In languages with tail call optimization (TCO):
    - Tail recursive functions use O(1) stack space
    - No risk of stack overflow for deep recursion
    - Can be as efficient as loops
    
    In Python:
    - No tail call optimization (by design)
    - Tail recursion doesn't provide stack benefits
    - Use iteration or memoization instead
    - Consider converting recursion to iteration for deep problems
    """)


if __name__ == "__main__":
    demonstrate_factorial()
    demonstrate_recursion_components()
    demonstrate_tail_recursion()
```

---

## 🌳 Section 2: Recursive Data Traversal – Trees and Directories

Recursion is perfect for traversing tree-like data structures, such as file systems, nested dictionaries, and hierarchical data.

**SOLID Principle Applied: Open/Closed** – New traversal operations can be added without modifying the structure.

**Design Pattern: Composite Pattern** – Recursion handles nested structures uniformly.

```python
"""
RECURSIVE DATA TRAVERSAL: TREES AND DIRECTORIES

This section demonstrates using recursion to traverse hierarchical data.

SOLID Principle: Open/Closed
- New traversal operations can be added

Design Pattern: Composite Pattern
- Recursion handles nested structures uniformly
"""

from typing import List, Dict, Any, Optional, Callable
from pathlib import Path
import os


def demonstrate_directory_traversal():
    """
    Demonstrates recursive directory traversal.
    
    File systems are naturally recursive: directories contain files and subdirectories.
    """
    print("=" * 60)
    print("SECTION 2A: DIRECTORY TRAVERSAL")
    print("=" * 60)
    
    # CREATE SAMPLE DIRECTORY STRUCTURE (in memory for demo)
    print("\n1. RECURSIVE DIRECTORY LISTING")
    print("-" * 40)
    
    # Simulated file system structure
    sample_fs = {
        "name": "project",
        "type": "directory",
        "children": [
            {
                "name": "src",
                "type": "directory",
                "children": [
                    {"name": "main.py", "type": "file", "size": 1024},
                    {"name": "utils.py", "type": "file", "size": 512},
                    {
                        "name": "modules",
                        "type": "directory",
                        "children": [
                            {"name": "auth.py", "type": "file", "size": 2048},
                            {"name": "database.py", "type": "file", "size": 3072}
                        ]
                    }
                ]
            },
            {
                "name": "tests",
                "type": "directory",
                "children": [
                    {"name": "test_main.py", "type": "file", "size": 768},
                    {"name": "test_utils.py", "type": "file", "size": 640}
                ]
            },
            {"name": "README.md", "type": "file", "size": 256},
            {"name": "setup.py", "type": "file", "size": 128}
        ]
    }
    
    def list_files_recursive(node: Dict, indent: str = "") -> None:
        """
        Recursively list all files in a directory tree.
        
        Args:
            node: Current directory or file node
            indent: Indentation string for pretty printing
        """
        if node["type"] == "file":
            print(f"{indent}📄 {node['name']} ({node['size']} bytes)")
        else:
            print(f"{indent}📁 {node['name']}/")
            for child in node.get("children", []):
                list_files_recursive(child, indent + "  ")
    
    print("  File system structure:")
    list_files_recursive(sample_fs)
    
    # COUNT FILES RECURSIVELY
    print("\n2. COUNTING FILES RECURSIVELY")
    print("-" * 40)
    
    def count_files(node: Dict) -> int:
        """Recursively count all files in a directory tree."""
        if node["type"] == "file":
            return 1
        
        total = 0
        for child in node.get("children", []):
            total += count_files(child)
        return total
    
    def count_files_by_extension(node: Dict, extension: str) -> int:
        """Count files with specific extension recursively."""
        if node["type"] == "file":
            return 1 if node["name"].endswith(extension) else 0
        
        total = 0
        for child in node.get("children", []):
            total += count_files_by_extension(child, extension)
        return total
    
    file_count = count_files(sample_fs)
    py_count = count_files_by_extension(sample_fs, ".py")
    md_count = count_files_by_extension(sample_fs, ".md")
    
    print(f"  Total files: {file_count}")
    print(f"  Python files: {py_count}")
    print(f"  Markdown files: {md_count}")
    
    # FIND LARGEST FILE
    print("\n3. FINDING LARGEST FILE RECURSIVELY")
    print("-" * 40)
    
    def find_largest_file(node: Dict) -> Optional[Dict]:
        """Find the largest file in a directory tree."""
        if node["type"] == "file":
            return node
        
        largest = None
        largest_size = -1
        
        for child in node.get("children", []):
            candidate = find_largest_file(child)
            if candidate and candidate.get("size", 0) > largest_size:
                largest = candidate
                largest_size = candidate.get("size", 0)
        
        return largest
    
    largest = find_largest_file(sample_fs)
    if largest:
        print(f"  Largest file: {largest['name']} ({largest['size']} bytes)")
    
    # COLLECT ALL PYTHON FILES
    print("\n4. COLLECTING ALL PYTHON FILES")
    print("-" * 40)
    
    def collect_files_by_extension(node: Dict, extension: str, result: List[str]) -> None:
        """Collect all files with specific extension into a list."""
        if node["type"] == "file":
            if node["name"].endswith(extension):
                result.append(node["name"])
        else:
            for child in node.get("children", []):
                collect_files_by_extension(child, extension, result)
    
    py_files = []
    collect_files_by_extension(sample_fs, ".py", py_files)
    print(f"  Python files: {py_files}")
    
    # CALCULATE TOTAL SIZE
    print("\n5. CALCULATING TOTAL DIRECTORY SIZE")
    print("-" * 40)
    
    def calculate_total_size(node: Dict) -> int:
        """Calculate total size of all files in a directory tree."""
        if node["type"] == "file":
            return node.get("size", 0)
        
        total = 0
        for child in node.get("children", []):
            total += calculate_total_size(child)
        return total
    
    total_size = calculate_total_size(sample_fs)
    print(f"  Total directory size: {total_size} bytes")
    
    # GENERATE DIRECTORY TREE STRING
    print("\n6. GENERATING DIRECTORY TREE STRING")
    print("-" * 40)
    
    def generate_tree_string(node: Dict, prefix: str = "", is_last: bool = True) -> str:
        """Generate a tree string representation (like 'tree' command)."""
        if node["type"] == "file":
            return f"{prefix}{'└── ' if is_last else '├── '}{node['name']}\n"
        
        result = f"{prefix}{'└── ' if is_last else '├── '}{node['name']}/\n"
        
        children = node.get("children", [])
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            result += generate_tree_string(child, new_prefix, is_last_child)
        
        return result
    
    tree_string = generate_tree_string(sample_fs)
    print("  Directory tree:")
    print(tree_string)


def demonstrate_nested_data_traversal():
    """
    Demonstrates traversing nested dictionaries and lists recursively.
    
    JSON data, configuration files, and API responses are often nested.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: NESTED DATA TRAVERSAL")
    print("=" * 60)
    
    # SAMPLE NESTED DATA (like JSON from an API)
    print("\n1. NESTED DATA STRUCTURE")
    print("-" * 40)
    
    nested_data = {
        "user": {
            "name": "Alice",
            "profile": {
                "age": 28,
                "address": {
                    "street": "123 Main St",
                    "city": "New York",
                    "zip": "10001"
                },
                "preferences": {
                    "theme": "dark",
                    "notifications": True
                }
            },
            "orders": [
                {"id": 1, "total": 299.99, "items": ["laptop", "mouse"]},
                {"id": 2, "total": 89.99, "items": ["keyboard"]}
            ]
        }
    }
    
    def print_nested(obj: Any, indent: str = "") -> None:
        """Recursively print nested data structure."""
        if isinstance(obj, dict):
            for key, value in obj.items():
                print(f"{indent}{key}:")
                print_nested(value, indent + "  ")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                print(f"{indent}[{i}]:")
                print_nested(item, indent + "  ")
        else:
            print(f"{indent}  {obj}")
    
    print("  Nested data structure:")
    print_nested(nested_data)
    
    # SEARCH FOR KEY RECURSIVELY
    print("\n2. SEARCHING FOR KEYS RECURSIVELY")
    print("-" * 40)
    
    def find_key(obj: Any, target_key: str, path: str = "") -> List[str]:
        """
        Find all paths to a specific key in nested data.
        
        Args:
            obj: Current object (dict, list, or primitive)
            target_key: Key to search for
            path: Current path (for tracking)
            
        Returns:
            List of paths where the key exists
        """
        results = []
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_path = f"{path}.{key}" if path else key
                if key == target_key:
                    results.append(current_path)
                results.extend(find_key(value, target_key, current_path))
        
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                current_path = f"{path}[{i}]"
                results.extend(find_key(item, target_key, current_path))
        
        return results
    
    paths = find_key(nested_data, "city")
    print(f"  Paths to 'city': {paths}")
    
    # GET VALUE BY PATH
    print("\n3. GETTING VALUE BY PATH RECURSIVELY")
    print("-" * 40)
    
    def get_value_by_path(obj: Any, path: str) -> Optional[Any]:
        """
        Get value from nested data using dot notation path.
        
        Args:
            obj: Current object
            path: Dot-separated path (e.g., "user.profile.address.city")
            
        Returns:
            Value at path, or None if not found
        """
        if not path:
            return obj
        
        parts = path.split(".", 1)
        key = parts[0]
        remaining = parts[1] if len(parts) > 1 else ""
        
        if isinstance(obj, dict) and key in obj:
            return get_value_by_path(obj[key], remaining)
        elif isinstance(obj, list) and key.isdigit():
            idx = int(key)
            if 0 <= idx < len(obj):
                return get_value_by_path(obj[idx], remaining)
        
        return None
    
    city = get_value_by_path(nested_data, "user.profile.address.city")
    print(f"  user.profile.address.city = {city}")
    
    theme = get_value_by_path(nested_data, "user.profile.preferences.theme")
    print(f"  user.profile.preferences.theme = {theme}")
    
    # TRANSFORM NESTED DATA
    print("\n4. TRANSFORMING NESTED DATA RECURSIVELY")
    print("-" * 40)
    
    def transform_strings(obj: Any, transform_func: Callable) -> Any:
        """
        Recursively transform all strings in nested data.
        
        Args:
            obj: Current object
            transform_func: Function to apply to strings
            
        Returns:
            Transformed object (new copy)
        """
        if isinstance(obj, dict):
            return {k: transform_strings(v, transform_func) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [transform_strings(item, transform_func) for item in obj]
        elif isinstance(obj, str):
            return transform_func(obj)
        else:
            return obj
    
    transformed = transform_strings(nested_data, lambda s: s.upper())
    
    print("  After transforming all strings to uppercase:")
    print(f"    user.name: {transformed['user']['name']}")
    print(f"    user.profile.address.city: {transformed['user']['profile']['address']['city']}")
    
    # COLLECT ALL VALUES OF A SPECIFIC TYPE
    print("\n5. COLLECTING ALL STRINGS")
    print("-" * 40)
    
    def collect_strings(obj: Any, result: List[str]) -> None:
        """Recursively collect all string values."""
        if isinstance(obj, dict):
            for value in obj.values():
                collect_strings(value, result)
        elif isinstance(obj, list):
            for item in obj:
                collect_strings(item, result)
        elif isinstance(obj, str):
            result.append(obj)
    
    all_strings = []
    collect_strings(nested_data, all_strings)
    print(f"  All string values: {all_strings}")


if __name__ == "__main__":
    demonstrate_directory_traversal()
    demonstrate_nested_data_traversal()
```

---

## 🔍 Section 3: Recursive Search Algorithms

Recursion is excellent for search algorithms that divide the problem space, like binary search.

**SOLID Principle Applied: Dependency Inversion** – Search algorithms depend on the comparison abstraction.

**Design Pattern: Divide and Conquer** – Problems are split into smaller subproblems.

```python
"""
RECURSIVE SEARCH ALGORITHMS

This section demonstrates recursive search algorithms like binary search.

SOLID Principle: Dependency Inversion
- Search algorithms depend on comparison abstraction

Design Pattern: Divide and Conquer
- Problems are split into smaller subproblems
"""

from typing import List, Any, Optional, Callable, TypeVar
import math

T = TypeVar('T')


def demonstrate_binary_search():
    """
    Demonstrates recursive binary search.
    
    Binary search is O(log n) - much faster than linear search for sorted data.
    """
    print("=" * 60)
    print("SECTION 3A: BINARY SEARCH")
    print("=" * 60)
    
    # RECURSIVE BINARY SEARCH
    print("\n1. RECURSIVE BINARY SEARCH")
    print("-" * 40)
    
    def binary_search(arr: List[T], target: T, left: int = 0, right: int = None) -> int:
        """
        Recursive binary search for target in sorted array.
        
        Args:
            arr: Sorted list to search
            target: Value to find
            left: Left boundary index
            right: Right boundary index
            
        Returns:
            Index of target, or -1 if not found
        """
        if right is None:
            right = len(arr) - 1
        
        # Base case: target not found
        if left > right:
            return -1
        
        # Find middle index
        mid = (left + right) // 2
        
        # Check if target is at middle
        if arr[mid] == target:
            return mid
        
        # Recursive case: search left or right half
        if target < arr[mid]:
            return binary_search(arr, target, left, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, right)
    
    # Test binary search
    sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print(f"  Array: {sorted_numbers}")
    
    for target in [7, 13, 20]:
        index = binary_search(sorted_numbers, target)
        if index != -1:
            print(f"  Found {target} at index {index}")
        else:
            print(f"  {target} not found")
    
    # BINARY SEARCH WITH VISUALIZATION
    print("\n2. BINARY SEARCH WITH VISUALIZATION")
    print("-" * 40)
    
    def binary_search_visual(arr: List[int], target: int, left: int = 0, right: int = None, depth: int = 0) -> int:
        """Binary search with call visualization."""
        if right is None:
            right = len(arr) - 1
        
        indent = "  " * depth
        print(f"{indent}Searching in {arr[left:right+1]} for {target}")
        
        if left > right:
            print(f"{indent}  Not found!")
            return -1
        
        mid = (left + right) // 2
        print(f"{indent}  Mid = {mid}, value = {arr[mid]}")
        
        if arr[mid] == target:
            print(f"{indent}  Found {target} at index {mid}!")
            return mid
        
        if target < arr[mid]:
            print(f"{indent}  {target} < {arr[mid]}, searching left half")
            return binary_search_visual(arr, target, left, mid - 1, depth + 1)
        else:
            print(f"{indent}  {target} > {arr[mid]}, searching right half")
            return binary_search_visual(arr, target, mid + 1, right, depth + 1)
    
    binary_search_visual(sorted_numbers, 13, 0, len(sorted_numbers) - 1)
    
    # SEARCH IN STRING LIST
    print("\n3. BINARY SEARCH IN STRING LIST")
    print("-" * 40)
    
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    
    def binary_search_strings(arr: List[str], target: str, left: int = 0, right: int = None) -> int:
        """Binary search for strings (case-insensitive)."""
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        # Case-insensitive comparison
        mid_val = arr[mid].lower()
        target_lower = target.lower()
        
        if mid_val == target_lower:
            return mid
        
        if target_lower < mid_val:
            return binary_search_strings(arr, target, left, mid - 1)
        else:
            return binary_search_strings(arr, target, mid + 1, right)
    
    print(f"  Words: {words}")
    
    for target in ["cherry", "fig", "mango"]:
        index = binary_search_strings(words, target)
        if index != -1:
            print(f"  Found '{target}' at index {index}")
        else:
            print(f"  '{target}' not found")


def demonstrate_recursive_search_patterns():
    """
    Demonstrates other recursive search patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: OTHER RECURSIVE SEARCH PATTERNS")
    print("=" * 60)
    
    # FIND MAXIMUM RECURSIVELY
    print("\n1. FIND MAXIMUM RECURSIVELY")
    print("-" * 40)
    
    def find_max(arr: List[int], left: int = 0, right: int = None) -> int:
        """Recursively find maximum element."""
        if right is None:
            right = len(arr) - 1
        
        # Base case: single element
        if left == right:
            return arr[left]
        
        # Divide and conquer
        mid = (left + right) // 2
        left_max = find_max(arr, left, mid)
        right_max = find_max(arr, mid + 1, right)
        
        return max(left_max, right_max)
    
    numbers = [3, 8, 2, 10, 5, 7, 1, 9, 4, 6]
    print(f"  Array: {numbers}")
    print(f"  Maximum: {find_max(numbers)}")
    
    # BINARY SEARCH FOR INSERTION POINT
    print("\n2. BINARY SEARCH FOR INSERTION POINT")
    print("-" * 40)
    
    def find_insertion_point(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """
        Find index where target should be inserted to maintain sorted order.
        
        Returns:
            Index where target should be inserted
        """
        if right is None:
            right = len(arr)
        
        if left >= right:
            return left
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if target < arr[mid]:
            return find_insertion_point(arr, target, left, mid)
        else:
            return find_insertion_point(arr, target, mid + 1, right)
    
    sorted_arr = [1, 3, 5, 7, 9]
    print(f"  Sorted array: {sorted_arr}")
    
    for target in [4, 6, 0, 10]:
        pos = find_insertion_point(sorted_arr, target)
        print(f"  Insert {target} at index {pos}")
    
    # FIND FIRST OCCURRENCE (for duplicates)
    print("\n3. FIND FIRST OCCURRENCE IN SORTED ARRAY")
    print("-" * 40)
    
    def find_first_occurrence(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """Find first occurrence of target (for arrays with duplicates)."""
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Check if this is the first occurrence
            if mid == 0 or arr[mid - 1] != target:
                return mid
            # Search left half for earlier occurrence
            return find_first_occurrence(arr, target, left, mid - 1)
        
        if target < arr[mid]:
            return find_first_occurrence(arr, target, left, mid - 1)
        else:
            return find_first_occurrence(arr, target, mid + 1, right)
    
    duplicates = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5]
    print(f"  Array with duplicates: {duplicates}")
    
    for target in [2, 3, 5]:
        index = find_first_occurrence(duplicates, target)
        print(f"  First occurrence of {target}: index {index}")
    
    # FIND LAST OCCURRENCE
    print("\n4. FIND LAST OCCURRENCE")
    print("-" * 40)
    
    def find_last_occurrence(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """Find last occurrence of target in sorted array with duplicates."""
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Check if this is the last occurrence
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            # Search right half for later occurrence
            return find_last_occurrence(arr, target, mid + 1, right)
        
        if target < arr[mid]:
            return find_last_occurrence(arr, target, left, mid - 1)
        else:
            return find_last_occurrence(arr, target, mid + 1, right)
    
    for target in [2, 3, 5]:
        first = find_first_occurrence(duplicates, target)
        last = find_last_occurrence(duplicates, target)
        print(f"  {target}: first at {first}, last at {last}, count = {last - first + 1}")


if __name__ == "__main__":
    demonstrate_binary_search()
    demonstrate_recursive_search_patterns()
```

---

## 🏛️ Section 4: Tower of Hanoi – Classic Recursive Problem

The Tower of Hanoi is a classic recursive puzzle that demonstrates the elegance of recursion.

**SOLID Principle Applied: Single Responsibility** – Each recursive call handles moving one disk.

**Design Pattern: Divide and Conquer** – The problem is split into smaller subproblems.

```python
"""
TOWER OF HANOI: CLASSIC RECURSIVE PROBLEM

This section solves the Tower of Hanoi puzzle using recursion.

SOLID Principle: Single Responsibility
- Each recursive call handles moving one disk

Design Pattern: Divide and Conquer
- Problem split into smaller subproblems
"""

from typing import List, Tuple
import time


def demonstrate_tower_of_hanoi():
    """
    Demonstrates the Tower of Hanoi solution using recursion.
    
    The puzzle: Move all disks from source peg to target peg using auxiliary peg.
    Rules:
    1. Only one disk can be moved at a time
    2. A larger disk cannot be placed on top of a smaller disk
    """
    print("=" * 60)
    print("SECTION 4: TOWER OF HANOI")
    print("=" * 60)
    
    # BASIC TOWER OF HANOI
    print("\n1. BASIC TOWER OF HANOI SOLUTION")
    print("-" * 40)
    
    def hanoi(n: int, source: str, target: str, auxiliary: str) -> List[str]:
        """
        Solve Tower of Hanoi puzzle.
        
        Args:
            n: Number of disks
            source: Source peg name
            target: Target peg name
            auxiliary: Auxiliary peg name
            
        Returns:
            List of moves as strings
        """
        moves = []
        
        if n == 1:
            # Base case: move single disk directly
            moves.append(f"Move disk 1 from {source} to {target}")
        else:
            # Step 1: Move n-1 disks from source to auxiliary
            moves.extend(hanoi(n - 1, source, auxiliary, target))
            
            # Step 2: Move largest disk from source to target
            moves.append(f"Move disk {n} from {source} to {target}")
            
            # Step 3: Move n-1 disks from auxiliary to target
            moves.extend(hanoi(n - 1, auxiliary, target, source))
        
        return moves
    
    # Solve for 3 disks
    print("  Solution for 3 disks:")
    moves = hanoi(3, "A", "C", "B")
    for move in moves:
        print(f"    {move}")
    
    print(f"\n  Total moves for 3 disks: {len(moves)}")
    
    # TOWER OF HANOI WITH VISUALIZATION
    print("\n2. TOWER OF HANOI WITH STATE VISUALIZATION")
    print("-" * 40)
    
    class HanoiVisualizer:
        """Visualizes the Tower of Hanoi state after each move."""
        
        def __init__(self, n: int, peg_names: Tuple[str, str, str] = ('A', 'B', 'C')):
            self.n = n
            self.peg_names = peg_names
            self.pegs = {name: list(range(n, 0, -1)) for name in peg_names}
            self.move_count = 0
        
        def display(self) -> None:
            """Display current state of all pegs."""
            print(f"\n  After move {self.move_count}:")
            for peg_name in self.peg_names:
                disks = self.pegs[peg_name]
                if disks:
                    print(f"    {peg_name}: {disks}")
                else:
                    print(f"    {peg_name}: []")
            print()
        
        def move_disk(self, source: str, target: str) -> None:
            """Move top disk from source to target."""
            if not self.pegs[source]:
                raise ValueError(f"No disk on peg {source}")
            
            disk = self.pegs[source].pop()
            
            if self.pegs[target] and disk > self.pegs[target][-1]:
                raise ValueError(f"Cannot place disk {disk} on smaller disk {self.pegs[target][-1]}")
            
            self.pegs[target].append(disk)
            self.move_count += 1
        
        def solve(self, n: int, source: str, target: str, auxiliary: str) -> None:
            """Solve Hanoi with visualization."""
            if n == 1:
                self.move_disk(source, target)
                self.display()
            else:
                self.solve(n - 1, source, auxiliary, target)
                self.move_disk(source, target)
                self.display()
                self.solve(n - 1, auxiliary, target, source)
    
    print("  Visualizing 3-disk solution:")
    visualizer = HanoiVisualizer(3)
    visualizer.display()
    visualizer.solve(3, 'A', 'C', 'B')
    
    # COUNTING MOVES
    print("\n3. MINIMUM MOVES FORMULA")
    print("-" * 40)
    
    def minimum_moves(n: int) -> int:
        """Calculate minimum moves required for n disks."""
        # Formula: moves = 2^n - 1
        return (1 << n) - 1  # Bit shift for 2^n
    
    print("  Minimum moves for different disk counts:")
    for n in range(1, 11):
        moves = minimum_moves(n)
        print(f"    {n} disk(s): {moves} moves")
    
    # ITERATIVE SOLUTION (for comparison)
    print("\n4. ITERATIVE TOWER OF HANOI")
    print("-" * 40)
    
    def hanoi_iterative(n: int, source: str, target: str, auxiliary: str) -> List[str]:
        """
        Iterative solution using stack (simulates recursion).
        
        This is more complex but avoids recursion depth issues.
        """
        moves = []
        stack = [(n, source, target, auxiliary, False)]
        
        while stack:
            n, src, tgt, aux, processed = stack.pop()
            
            if n == 1:
                moves.append(f"Move disk 1 from {src} to {tgt}")
            elif not processed:
                # Push in reverse order for correct execution
                stack.append((n, src, tgt, aux, True))
                stack.append((n - 1, aux, tgt, src, False))
                stack.append((1, src, tgt, aux, False))
                stack.append((n - 1, src, aux, tgt, False))
        
        return moves
    
    print("  Iterative solution (same result, no recursion):")
    iter_moves = hanoi_iterative(3, "A", "C", "B")
    for move in iter_moves[:5]:
        print(f"    {move}")
    print(f"    ... {len(iter_moves)} moves total")
    
    # RECURSION DEPTH FOR HANOI
    print("\n5. RECURSION DEPTH ANALYSIS")
    print("-" * 40)
    
    def hanoi_depth(n: int, depth: int = 0) -> int:
        """Calculate maximum recursion depth for n disks."""
        if n == 1:
            return depth + 1
        return max(hanoi_depth(n - 1, depth + 1), hanoi_depth(n - 1, depth + 1))
    
    for n in range(1, 11):
        max_depth = hanoi_depth(n)
        moves = minimum_moves(n)
        print(f"  {n} disks: max depth = {max_depth}, moves = {moves:,}")
    
    print("\n  Note: Maximum recursion depth = number of disks + 1")
    print("  This is efficient! Depth doesn't grow exponentially like moves.")


if __name__ == "__main__":
    demonstrate_tower_of_hanoi()
```

---

## 📁 Section 5: Complete File System Analyzer

A complete file system analyzer that uses recursion to scan directories, analyze file types, and generate reports.

**SOLID Principles Applied:**
- Single Responsibility: Each function handles one analysis aspect
- Open/Closed: New analysis types can be added

**Design Patterns:**
- Composite Pattern: Treats files and directories uniformly
- Visitor Pattern: Different analysis operations on the structure
- Iterator Pattern: Recursive iteration through the tree

```python
"""
COMPLETE FILE SYSTEM ANALYZER

This section builds a complete file system analyzer using recursion.

SOLID Principles Applied:
- Single Responsibility: Each function handles one analysis aspect
- Open/Closed: New analysis types can be added

Design Patterns:
- Composite Pattern: Files and directories treated uniformly
- Visitor Pattern: Different analysis operations
- Iterator Pattern: Recursive iteration through tree
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
import os
import hashlib
from collections import defaultdict


@dataclass
class FileInfo:
    """Information about a file."""
    path: str
    name: str
    size: int
    extension: str
    modified_time: datetime
    created_time: datetime
    hash: Optional[str] = None


@dataclass
class DirectoryInfo:
    """Information about a directory."""
    path: str
    name: str
    files: List[FileInfo] = field(default_factory=list)
    subdirectories: List['DirectoryInfo'] = field(default_factory=list)
    
    def total_size(self) -> int:
        """Calculate total size of all files in directory (recursive)."""
        size = sum(f.size for f in self.files)
        for subdir in self.subdirectories:
            size += subdir.total_size()
        return size
    
    def file_count(self) -> int:
        """Count total number of files (recursive)."""
        count = len(self.files)
        for subdir in self.subdirectories:
            count += subdir.file_count()
        return count
    
    def directory_count(self) -> int:
        """Count total number of subdirectories (recursive)."""
        count = len(self.subdirectories)
        for subdir in self.subdirectories:
            count += subdir.directory_count()
        return count


class FileSystemAnalyzer:
    """
    Recursively analyzes file system structure.
    
    Design Pattern: Composite Pattern - Files and directories treated uniformly
    """
    
    def __init__(self, root_path: str):
        self.root_path = Path(root_path).resolve()
        self.root_info: Optional[DirectoryInfo] = None
    
    def scan(self) -> DirectoryInfo:
        """
        Recursively scan directory structure.
        
        Returns:
            DirectoryInfo containing complete structure
        """
        self.root_info = self._scan_directory(self.root_path)
        return self.root_info
    
    def _scan_directory(self, path: Path) -> DirectoryInfo:
        """
        Recursively scan a single directory.
        
        Args:
            path: Path to scan
            
        Returns:
            DirectoryInfo for this directory
        """
        dir_info = DirectoryInfo(
            path=str(path),
            name=path.name
        )
        
        try:
            for item in path.iterdir():
                if item.is_file():
                    file_info = self._get_file_info(item)
                    dir_info.files.append(file_info)
                elif item.is_dir():
                    subdir_info = self._scan_directory(item)
                    dir_info.subdirectories.append(subdir_info)
        except PermissionError:
            print(f"  Permission denied: {path}")
        except OSError as e:
            print(f"  Error accessing {path}: {e}")
        
        return dir_info
    
    def _get_file_info(self, path: Path) -> FileInfo:
        """
        Get information about a single file.
        
        Args:
            path: Path to file
            
        Returns:
            FileInfo object
        """
        stat = path.stat()
        
        return FileInfo(
            path=str(path),
            name=path.name,
            size=stat.st_size,
            extension=path.suffix.lower(),
            modified_time=datetime.fromtimestamp(stat.st_mtime),
            created_time=datetime.fromtimestamp(stat.st_ctime)
        )
    
    def calculate_file_hash(self, file_path: str, algorithm: str = "md5") -> str:
        """
        Calculate hash of a file (useful for finding duplicates).
        
        Args:
            file_path: Path to file
            algorithm: Hash algorithm (md5, sha1, sha256)
            
        Returns:
            Hexadecimal hash string
        """
        hash_func = getattr(hashlib, algorithm)()
        
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_func.update(chunk)
        
        return hash_func.hexdigest()
    
    def find_duplicate_files(self, directory_info: Optional[DirectoryInfo] = None) -> Dict[str, List[str]]:
        """
        Find duplicate files by size and hash.
        
        Args:
            directory_info: Starting directory (defaults to root)
            
        Returns:
            Dictionary mapping hash to list of file paths
        """
        if directory_info is None:
            directory_info = self.root_info
        
        if not directory_info:
            return {}
        
        # Group by size first (quick filter)
        size_groups: Dict[int, List[FileInfo]] = defaultdict(list)
        
        def collect_files(info: DirectoryInfo):
            for file in info.files:
                size_groups[file.size].append(file)
            for subdir in info.subdirectories:
                collect_files(subdir)
        
        collect_files(directory_info)
        
        # Find duplicates by hash within each size group
        duplicates: Dict[str, List[str]] = {}
        
        for size, files in size_groups.items():
            if len(files) < 2:
                continue
            
            hash_groups: Dict[str, List[str]] = defaultdict(list)
            
            for file in files:
                file_hash = self.calculate_file_hash(file.path)
                hash_groups[file_hash].append(file.path)
            
            for file_hash, paths in hash_groups.items():
                if len(paths) > 1:
                    duplicates[file_hash] = paths
        
        return duplicates
    
    def get_extension_statistics(self, directory_info: Optional[DirectoryInfo] = None) -> Dict[str, Dict]:
        """
        Get statistics by file extension.
        
        Returns:
            Dictionary with extension as key, stats as value
        """
        if directory_info is None:
            directory_info = self.root_info
        
        if not directory_info:
            return {}
        
        ext_stats: Dict[str, Dict] = defaultdict(lambda: {"count": 0, "total_size": 0})
        
        def collect_stats(info: DirectoryInfo):
            for file in info.files:
                ext = file.extension if file.extension else "no_extension"
                ext_stats[ext]["count"] += 1
                ext_stats[ext]["total_size"] += file.size
            for subdir in info.subdirectories:
                collect_stats(subdir)
        
        collect_stats(directory_info)
        
        return dict(ext_stats)
    
    def get_largest_files(self, n: int = 10, directory_info: Optional[DirectoryInfo] = None) -> List[FileInfo]:
        """
        Get the n largest files in the directory tree.
        
        Args:
            n: Number of largest files to return
            directory_info: Starting directory
            
        Returns:
            List of largest FileInfo objects
        """
        if directory_info is None:
            directory_info = self.root_info
        
        if not directory_info:
            return []
        
        all_files = []
        
        def collect_files(info: DirectoryInfo):
            all_files.extend(info.files)
            for subdir in info.subdirectories:
                collect_files(subdir)
        
        collect_files(directory_info)
        all_files.sort(key=lambda f: f.size, reverse=True)
        
        return all_files[:n]
    
    def get_newest_files(self, n: int = 10, directory_info: Optional[DirectoryInfo] = None) -> List[FileInfo]:
        """
        Get the n newest files (by modified time).
        
        Args:
            n: Number of newest files to return
            directory_info: Starting directory
            
        Returns:
            List of newest FileInfo objects
        """
        if directory_info is None:
            directory_info = self.root_info
        
        if not directory_info:
            return []
        
        all_files = []
        
        def collect_files(info: DirectoryInfo):
            all_files.extend(info.files)
            for subdir in info.subdirectories:
                collect_files(subdir)
        
        collect_files(directory_info)
        all_files.sort(key=lambda f: f.modified_time, reverse=True)
        
        return all_files[:n]
    
    def generate_report(self) -> str:
        """
        Generate a complete report of the file system analysis.
        
        Returns:
            Formatted report string
        """
        if not self.root_info:
            return "No scan data available. Run scan() first."
        
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append(f"FILE SYSTEM ANALYSIS REPORT")
        report_lines.append(f"Root: {self.root_path}")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        # Basic statistics
        total_size = self.root_info.total_size()
        total_files = self.root_info.file_count()
        total_dirs = self.root_info.directory_count()
        
        report_lines.append(f"\n📊 BASIC STATISTICS:")
        report_lines.append(f"  Total Directories: {total_dirs:,}")
        report_lines.append(f"  Total Files: {total_files:,}")
        report_lines.append(f"  Total Size: {self._format_size(total_size)}")
        
        # Extension statistics
        ext_stats = self.get_extension_statistics()
        if ext_stats:
            report_lines.append(f"\n📁 FILE TYPE DISTRIBUTION:")
            sorted_exts = sorted(ext_stats.items(), key=lambda x: x[1]["count"], reverse=True)
            for ext, stats in sorted_exts[:10]:
                report_lines.append(f"  {ext or 'no extension':15} : {stats['count']:6} files, {self._format_size(stats['total_size'])}")
        
        # Largest files
        largest = self.get_largest_files(10)
        if largest:
            report_lines.append(f"\n💾 LARGEST FILES:")
            for i, file in enumerate(largest, 1):
                report_lines.append(f"  {i:2}. {self._format_size(file.size):>10} - {file.name}")
        
        # Newest files
        newest = self.get_newest_files(10)
        if newest:
            report_lines.append(f"\n🕒 NEWEST FILES:")
            for i, file in enumerate(newest, 1):
                report_lines.append(f"  {i:2}. {file.modified_time.strftime('%Y-%m-%d')} - {file.name}")
        
        # Duplicate files
        duplicates = self.find_duplicate_files()
        if duplicates:
            duplicate_count = sum(len(paths) for paths in duplicates.values())
            duplicate_files = len(duplicates)
            report_lines.append(f"\n🔄 DUPLICATE FILES:")
            report_lines.append(f"  Found {duplicate_files} sets of duplicates ({duplicate_count} total files)")
        
        report_lines.append("\n" + "=" * 60)
        
        return "\n".join(report_lines)
    
    def _format_size(self, size: int) -> str:
        """Format size in bytes to human-readable string."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"
    
    def print_tree(self, directory_info: Optional[DirectoryInfo] = None, prefix: str = "", is_last: bool = True) -> None:
        """
        Print directory tree structure.
        
        Args:
            directory_info: Starting directory (defaults to root)
            prefix: Prefix for tree lines
            is_last: Whether this is the last item in parent
        """
        if directory_info is None:
            directory_info = self.root_info
        
        if not directory_info:
            return
        
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{directory_info.name}/")
        
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        children = directory_info.files + directory_info.subdirectories
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            
            if isinstance(child, FileInfo):
                size_str = self._format_size(child.size)
                connector_child = "└── " if is_last_child else "├── "
                print(f"{new_prefix}{connector_child}{child.name} ({size_str})")
            else:
                self.print_tree(child, new_prefix, is_last_child)


def demonstrate_file_analyzer():
    """
    Demonstrate the file system analyzer.
    
    Note: This creates a temporary directory structure for demonstration.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: FILE SYSTEM ANALYZER")
    print("=" * 60)
    
    import tempfile
    import time
    
    # Create temporary directory structure for demonstration
    print("\n📁 CREATING SAMPLE DIRECTORY STRUCTURE")
    print("-" * 40)
    
    temp_dir = tempfile.mkdtemp()
    print(f"  Created temp directory: {temp_dir}")
    
    # Create sample files
    def create_sample_file(path: str, size_kb: int = 1):
        """Create a sample file with specified size."""
        with open(path, 'w') as f:
            f.write("X" * (size_kb * 1024))
    
    # Create nested structure
    src_dir = os.path.join(temp_dir, "src")
    os.makedirs(src_dir)
    create_sample_file(os.path.join(src_dir, "main.py"), 5)
    create_sample_file(os.path.join(src_dir, "utils.py"), 3)
    
    modules_dir = os.path.join(src_dir, "modules")
    os.makedirs(modules_dir)
    create_sample_file(os.path.join(modules_dir, "auth.py"), 8)
    create_sample_file(os.path.join(modules_dir, "database.py"), 12)
    
    tests_dir = os.path.join(temp_dir, "tests")
    os.makedirs(tests_dir)
    create_sample_file(os.path.join(tests_dir, "test_main.py"), 4)
    create_sample_file(os.path.join(tests_dir, "test_utils.py"), 3)
    
    # Create duplicate file
    create_sample_file(os.path.join(temp_dir, "README.md"), 2)
    create_sample_file(os.path.join(tests_dir, "README copy.md"), 2)
    
    # Create config file
    create_sample_file(os.path.join(temp_dir, "config.json"), 1)
    
    print("  Sample files created:")
    print("    src/main.py, src/utils.py")
    print("    src/modules/auth.py, src/modules/database.py")
    print("    tests/test_main.py, tests/test_utils.py, tests/README copy.md")
    print("    README.md, config.json")
    
    # Run analyzer
    print("\n🔍 ANALYZING FILE SYSTEM")
    print("-" * 40)
    
    analyzer = FileSystemAnalyzer(temp_dir)
    analyzer.scan()
    
    # Print tree
    print("\n  Directory tree:")
    analyzer.print_tree()
    
    # Generate report
    report = analyzer.generate_report()
    print(report)
    
    # Clean up
    import shutil
    shutil.rmtree(temp_dir)
    print(f"\n  Cleaned up temp directory: {temp_dir}")


if __name__ == "__main__":
    demonstrate_file_analyzer()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Recursion Basics** – Function that calls itself. Requires base case (stopping condition) and recursive case (calls self with smaller input).

- **Factorial** – Classic example: n! = n × (n-1)!. Base case: 0! = 1, 1! = 1.

- **Fibonacci** – fib(n) = fib(n-1) + fib(n-2). Without memoization, O(2^n) time complexity.

- **Recursion Limit** – Python default is 1000. Can increase with `sys.setrecursionlimit()` but be careful.

- **Tail Recursion** – Recursive call is last operation. Python doesn't optimize it; use iteration instead.

- **Directory Traversal** – Recursively walk through file system. Process files and subdirectories uniformly.

- **Nested Data Traversal** – Recursively navigate JSON-like structures. Find keys, get values by path.

- **Binary Search** – O(log n) search in sorted arrays. Divide and conquer approach.

- **Tower of Hanoi** – Classic recursive puzzle. Moves = 2^n - 1. Recursion depth = n + 1.

- **File System Analyzer** – Complete tool using recursion: scan directories, find duplicates, generate reports.

- **SOLID Principles Applied** – Single Responsibility (each recursive function handles one level), Open/Closed (new traversal operations can be added), Dependency Inversion (depends on abstractions).

- **Design Patterns Used** – Composite Pattern (files and directories treated uniformly), Divide and Conquer (problem splitting), Visitor Pattern (different analysis operations), Iterator Pattern (recursive iteration).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful

- **📚 Series B Catalog:** Functions & Modules Yard – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale (Series B, Story 6)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 5 | 1 | 83% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **17** | **35** | **33%** |

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

**Next Story:** Series B, Story 6: The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale

---

## 📝 Your Invitation

You've mastered recursion. Now build something with what you've learned:

1. **Build a directory tree visualizer** – Create a command-line tool that displays directory structure like the `tree` command.

2. **Create a JSON path finder** – Implement a function that finds all paths to a specific key in nested JSON data.

3. **Build a duplicate file finder** – Scan directories, group files by size, then by hash to find duplicates.

4. **Create a recursive search utility** – Implement find and replace across all files in a directory tree.

5. **Solve more recursive puzzles** – Try implementing the Sieve of Eratosthenes, Merge Sort, or Quick Sort recursively.

**You've mastered recursion. Next stop: Modules & Packages!**

---

*Found this helpful? Clap, comment, and share what you built with recursion. Next stop: Modules & Packages!* 🚇