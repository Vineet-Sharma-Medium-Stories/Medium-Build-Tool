# The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale

## Series B: Functions & Modules Yard | Story 6 of 6

![The 2026 Python Metromap/images/Modules and Packages – Organizing Code at Scale](images/Modules and Packages – Organizing Code at Scale.png)

## 📖 Introduction

**Welcome to the sixth and final stop on the Functions & Modules Yard Line.**

You've mastered defining functions, passing arguments, returning values, using lambda functions, and recursion. You can write elegant, reusable code. But as your projects grow from a single file to dozens of files, you need a way to organize, structure, and share your code.

That's where modules and packages come in.

A module is simply a Python file containing code. A package is a collection of modules organized in directories. Together, they let you break large codebases into manageable pieces, reuse code across projects, and leverage Python's vast ecosystem of third-party libraries. Importing modules gives you access to thousands of pre-built solutions for everything from data science to web development.

This story—**The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale**—is your guide to structuring Python projects professionally. We'll build a complete reusable utility library with proper module organization. We'll create a package structure with `__init__.py` files, relative imports, and namespace packages. We'll learn to install and manage third-party packages with pip. And we'll build a complete data processing package that can be installed, imported, and used like any professional library.

**Let's organize our code.**

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

- 🔧 **The 2026 Python Metromap: Defining Functions – The Workhorses of Python** – Payment processing module; validation functions; error handling.

- 📋 **The 2026 Python Metromap: Arguments – Positional, Keyword, and Default** – Flexible report generator for PDF, CSV, and JSON outputs.

- 📤 **The 2026 Python Metromap: Return Values – Getting Results Back** – API response formatter; standardized success and error responses.

- ⚡ **The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful** – Sorting custom objects; filtering data streams; mapping pipelines.

- 🔄 **The 2026 Python Metromap: Recursion – Functions Calling Themselves** – Directory tree traversal; factorial calculations; Tower of Hanoi solver.

- 📦 **The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale** – Reusable utility library; multi-file project structure; publishing packages. **⬅️ YOU ARE HERE**

### Series C: Data Structures Express (5 Stories) – Next Station

- 📋 **The 2026 Python Metromap: Lists – Ordered & Mutable** – Todo application; playlist manager; undo/redo functionality. 🔜 *Up Next*

- 🔒 **The 2026 Python Metromap: Tuples – Immutable Collections** – GPS coordinates for delivery routes; database record representations; immutable configuration.

- 🔑 **The 2026 Python Metromap: Dictionaries – Key-Value Power** – User profile cache; product catalog; dependency injection container.

- 🎯 **The 2026 Python Metromap: Sets – Unique & Fast** – Duplicate removal; friend recommendation engine; common visitor detection.

- 📝 **The 2026 Python Metromap: Comprehensions – One-Line Power** – Data transformation pipelines; filtered iterations; nested structure creation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📦 Section 1: Understanding Modules – Single-File Organization

A module is a Python file containing functions, classes, and variables. The filename becomes the module name.

**SOLID Principle Applied: Single Responsibility** – Each module should have a clear, focused purpose.

**Design Pattern: Module Pattern** – Encapsulates related functionality in a single file.

```python
"""
UNDERSTANDING MODULES: SINGLE-FILE ORGANIZATION

This section covers the fundamentals of Python modules.

SOLID Principle: Single Responsibility
- Each module has a clear, focused purpose

Design Pattern: Module Pattern
- Encapsulates related functionality in a single file
"""

# This is a module file. In a real project, this would be in a separate .py file.
# For demonstration, we'll create simulated modules and show how to use them.

print("=" * 60)
print("SECTION 1A: WHAT ARE MODULES?")
print("=" * 60)


# Simulating a module called "string_utils.py"
class StringUtilsModule:
    """Simulated module content - would be in its own file."""
    
    def reverse_string(s: str) -> str:
        """Reverse a string."""
        return s[::-1]
    
    def capitalize_words(s: str) -> str:
        """Capitalize first letter of each word."""
        return ' '.join(word.capitalize() for word in s.split())
    
    def count_vowels(s: str) -> int:
        """Count vowels in a string."""
        return sum(1 for c in s.lower() if c in 'aeiou')
    
    def is_palindrome(s: str) -> bool:
        """Check if string is palindrome."""
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]


# Simulating a module called "math_utils.py"
class MathUtilsModule:
    """Simulated module content - would be in its own file."""
    
    def factorial(n: int) -> int:
        """Calculate factorial recursively."""
        if n <= 1:
            return 1
        return n * MathUtilsModule.factorial(n - 1)
    
    def is_prime(n: int) -> bool:
        """Check if number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def gcd(a: int, b: int) -> int:
        """Calculate greatest common divisor using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a


# DEMONSTRATION
print("\n1. MODULE CONCEPT")
print("-" * 40)

print("""
In a real Python project, you would organize code like this:

project/
├── string_utils.py    # Module 1
├── math_utils.py      # Module 2
└── main.py            # Main script

Inside string_utils.py:
    def reverse_string(s): ...
    def capitalize_words(s): ...
    def count_vowels(s): ...
    def is_palindrome(s): ...

Inside main.py:
    import string_utils
    result = string_utils.reverse_string("hello")
""")

print("\n2. IMPORTING MODULES (Syntax Examples)")
print("-" * 40)

print("""
# Import entire module
import string_utils
result = string_utils.reverse_string("hello")

# Import specific functions
from string_utils import reverse_string, capitalize_words
result = reverse_string("hello")

# Import with alias
import string_utils as su
result = su.reverse_string("hello")

# Import all (not recommended)
from string_utils import *
result = reverse_string("hello")
""")

print("\n3. SIMULATED MODULE USAGE")
print("-" * 40)

# Using our simulated modules
text = "Hello World"

print(f"  Original: '{text}'")
print(f"  reverse_string: '{StringUtilsModule.reverse_string(text)}'")
print(f"  capitalize_words: '{StringUtilsModule.capitalize_words(text)}'")
print(f"  count_vowels: {StringUtilsModule.count_vowels(text)}")
print(f"  is_palindrome: {StringUtilsModule.is_palindrome(text)}")

print(f"\n  factorial(5): {MathUtilsModule.factorial(5)}")
print(f"  is_prime(17): {MathUtilsModule.is_prime(17)}")
print(f"  gcd(48, 18): {MathUtilsModule.gcd(48, 18)}")


def demonstrate_module_search_path():
    """
    Demonstrates how Python finds modules.
    
    Python searches for modules in sys.path directories.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: MODULE SEARCH PATH")
    print("=" * 60)
    
    import sys
    
    print("\n1. PYTHON MODULE SEARCH PATH")
    print("-" * 40)
    
    print("Python searches for modules in this order:")
    for i, path in enumerate(sys.path[:5], 1):
        print(f"  {i}. {path}")
    if len(sys.path) > 5:
        print(f"  ... and {len(sys.path) - 5} more paths")
    
    print("\n2. ADDING CUSTOM PATHS")
    print("-" * 40)
    
    print("""
# Add a directory to the search path
import sys
sys.path.append('/path/to/my/modules')

# Now Python will also look in this directory for modules
import my_custom_module
""")
    
    print("\n3. CURRENT WORKING DIRECTORY")
    print("-" * 40)
    
    import os
    print(f"  Current working directory: {os.getcwd()}")
    print("  Python looks here first for modules!")
    
    print("\n4. MODULE CACHE")
    print("-" * 40)
    
    print("""
# Python caches imported modules in sys.modules
import sys
print(sys.modules.keys())

# Reload a module (useful during development)
import importlib
importlib.reload(my_module)
""")


def demonstrate_module_aliases():
    """
    Demonstrates module aliasing and selective imports.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: MODULE ALIASES AND SELECTIVE IMPORTS")
    print("=" * 60)
    
    # Simulated module with many functions
    class DataProcessor:
        """Simulated data processing module."""
        
        def clean_data(self, data): return data
        def normalize_data(self, data): return data
        def transform_data(self, data): return data
        def aggregate_data(self, data): return data
        def validate_data(self, data): return True
    
    print("\n1. SELECTIVE IMPORT (import specific items)")
    print("-" * 40)
    
    print("""
# Instead of importing the whole module:
import data_processor
processor = data_processor.DataProcessor()

# Import only what you need:
from data_processor import DataProcessor, clean_data, validate_data

# Benefits:
# - Clearer what functions are used
# - Shorter function names (no module prefix)
# - Smaller namespace footprint
""")
    
    print("\n2. MODULE ALIASING (renaming imports)")
    print("-" * 40)
    
    print("""
# Long module name:
import very_long_module_name_that_is_hard_to_type

# With alias:
import very_long_module_name_that_is_hard_to_type as vlm
result = vlm.some_function()

# Common conventions:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
""")
    
    print("\n3. AVOIDING NAMING CONFLICTS")
    print("-" * 40)
    
    print("""
# Two modules with same function name:
from module_a import process
from module_b import process  # Overwrites module_a.process!

# Solution 1: Use aliases
from module_a import process as process_a
from module_b import process as process_b

# Solution 2: Import modules instead
import module_a
import module_b
module_a.process()
module_b.process()
""")
    
    print("\n4. PACKAGE STRUCTURE PREVIEW")
    print("-" * 40)
    
    print("""
# Modules can be organized into packages (directories)
my_package/
├── __init__.py      # Makes directory a package
├── module_a.py
├── module_b.py
└── subpackage/
    ├── __init__.py
    └── module_c.py

# Import from package
import my_package.module_a
from my_package.subpackage import module_c
""")


if __name__ == "__main__":
    # This would normally be in a separate file
    print("\n" + "=" * 60)
    print("SECTION 1D: __name__ == '__main__' GUARD")
    print("=" * 60)
    
    print("""
# The if __name__ == '__main__': guard is used to:
# 1. Run code only when script is executed directly (not imported)
# 2. Allow module to be both imported AND run as script
# 3. Provide test/demo code for the module

# Example:
if __name__ == '__main__':
    # This code runs only when the file is run directly
    print("This module is being run directly")
    # Test the module functions here

# When imported, this code does NOT run
""")
    
    print("\n  This is a best practice for all Python modules!")
```

---

## 📁 Section 2: Creating Packages – Directory Organization

A package is a directory containing modules and a special `__init__.py` file.

**SOLID Principle Applied: Interface Segregation** – Packages expose clean public interfaces via `__init__.py`.

**Design Pattern: Facade Pattern** – `__init__.py` provides a simplified interface to the package.

```python
"""
CREATING PACKAGES: DIRECTORY ORGANIZATION

This section demonstrates creating and using Python packages.

SOLID Principle: Interface Segregation
- Packages expose clean public interfaces via __init__.py

Design Pattern: Facade Pattern
- __init__.py provides simplified interface to package
"""

import os
import sys
from pathlib import Path


def demonstrate_package_structure():
    """
    Demonstrates the structure of Python packages.
    """
    print("=" * 60)
    print("SECTION 2A: PACKAGE STRUCTURE")
    print("=" * 60)
    
    print("\n1. BASIC PACKAGE STRUCTURE")
    print("-" * 40)
    
    print("""
my_package/                    # Package directory
├── __init__.py               # Required - makes it a package
├── module_a.py               # Submodule
├── module_b.py               # Submodule
└── subpackage/               # Nested package
    ├── __init__.py
    └── module_c.py

# __init__.py can be empty or contain package initialization code
# It runs when the package is first imported
""")
    
    print("\n2. CREATING A SIMPLE PACKAGE (Simulated)")
    print("-" * 40)
    
    # Simulate package structure in memory
    class SimulatedPackage:
        """Simulates a package with multiple modules."""
        
        class __init__:
            """Package initialization."""
            __version__ = "1.0.0"
            __author__ = "Metromap"
            
            @staticmethod
            def info():
                return "This is the my_package package"
        
        class module_a:
            @staticmethod
            def function_a():
                return "Function A from module_a"
        
        class module_b:
            @staticmethod
            def function_b():
                return "Function B from module_b"
        
        class subpackage:
            class __init__:
                pass
            
            class module_c:
                @staticmethod
                def function_c():
                    return "Function C from subpackage.module_c"
    
    print("  Simulated package structure:")
    print("    my_package/")
    print("    ├── __init__.py")
    print("    ├── module_a.py")
    print("    ├── module_b.py")
    print("    └── subpackage/")
    print("        ├── __init__.py")
    print("        └── module_c.py")
    
    print("\n3. IMPORTING FROM PACKAGES")
    print("-" * 40)
    
    print("""
# Import entire package
import my_package
print(my_package.__version__)

# Import submodule
import my_package.module_a
my_package.module_a.function_a()

# Import specific function
from my_package.module_a import function_a
function_a()

# Import from subpackage
from my_package.subpackage import module_c
module_c.function_c()

# Import with alias
import my_package.module_a as ma
ma.function_a()
""")
    
    print("\n4. RELATIVE IMPORTS (Inside Package)")
    print("-" * 40)
    
    print("""
# Inside module_b.py, to import from module_a:

# Absolute import (recommended)
from my_package import module_a

# Relative import (within same package)
from . import module_a           # Current package
from ..subpackage import module_c  # Parent package then subpackage
from .subpackage import module_c   # Subpackage from current level

# Relative imports only work inside packages
""")


def demonstrate_init_py():
    """
    Demonstrates the role of __init__.py files.
    
    __init__.py controls what gets imported when the package is imported.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: __init__.py – Package Initialization")
    print("=" * 60)
    
    print("\n1. WHAT __init__.py CAN DO")
    print("-" * 40)
    
    print("""
# __init__.py can contain:

# 1. Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# 2. Package initialization code
import logging
logging.basicConfig(level=logging.INFO)

# 3. Define what gets exported with "from package import *"
__all__ = ['module_a', 'module_b']

# 4. Import submodules to make them available at package level
from .module_a import function_a
from .module_b import function_b

# 5. Create a simplified interface (Facade pattern)
from .module_a import clean_data
from .module_b import transform_data
from .module_c import aggregate_data

def process_data(data):
    return aggregate_data(transform_data(clean_data(data)))
""")
    
    print("\n2. CONTROLLING EXPORTS (__all__)")
    print("-" * 40)
    
    print("""
# __init__.py
__all__ = ['public_function', 'PublicClass']

def public_function():
    pass

def _private_function():
    pass  # Not exported

class PublicClass:
    pass

class _PrivateClass:
    pass  # Not exported

# When user does: from my_package import *
# Only public_function and PublicClass are imported
""")
    
    print("\n3. PACKAGE-LEVEL CONVENIENCE FUNCTIONS")
    print("-" * 40)
    
    print("""
# __init__.py can expose a simplified API
from .validators import validate_email, validate_phone
from .formatters import format_currency, format_date
from .parsers import parse_csv, parse_json

# User can then do:
from my_package import validate_email, format_currency

# Instead of:
from my_package.validators import validate_email
from my_package.formatters import format_currency
""")


def demonstrate_namespace_packages():
    """
    Demonstrates namespace packages (Python 3.3+).
    
    Namespace packages allow splitting a package across multiple directories.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: NAMESPACE PACKAGES")
    print("=" * 60)
    
    print("\n1. WHAT ARE NAMESPACE PACKAGES?")
    print("-" * 40)
    
    print("""
# Regular package: requires __init__.py in every directory
# Namespace package: works without __init__.py (Python 3.3+)

# Allows splitting a package across multiple locations:
# site-packages/company/team_a/__init__.py
# site-packages/company/team_b/__init__.py
# Both contribute to the same 'company' namespace package

# Use cases:
# - Large projects split across multiple repositories
# - Plugin systems where different packages contribute to the same namespace
# - Framework extensions
""")
    
    print("\n2. CREATING A NAMESPACE PACKAGE")
    print("-" * 40)
    
    print("""
# Directory structure (no __init__.py files needed):
company/
    team_a/
        module_a.py
    team_b/
        module_b.py

# Both directories are added to sys.path
# Python automatically merges them into a single 'company' namespace
""")
    
    print("\n3. WHEN TO USE REGULAR vs NAMESPACE PACKAGES")
    print("-" * 40)
    
    print("""
Regular Package:
- Single, cohesive project
- Need package initialization code
- Want to control exports via __all__
- Traditional, simpler to understand

Namespace Package:
- Distributed across multiple repositories
- Plugin architecture
- Large organization with multiple teams
- No package initialization needed
""")


if __name__ == "__main__":
    demonstrate_package_structure()
    demonstrate_init_py()
    demonstrate_namespace_packages()
```

---

## 🔧 Section 3: Building a Reusable Utility Package

Let's build a complete, reusable utility package with proper structure, documentation, and testing.

**SOLID Principles Applied:**
- Single Responsibility: Each module handles one category of utilities
- Interface Segregation: Clean public interfaces via __init__.py

**Design Patterns:**
- Facade Pattern: Simplified interface through __init__.py
- Factory Pattern: Creates utility objects

```python
"""
BUILDING A REUSABLE UTILITY PACKAGE

This section builds a complete utility package with proper structure.

SOLID Principles Applied:
- Single Responsibility: Each module handles one category
- Interface Segregation: Clean public interfaces

Design Patterns:
- Facade Pattern: Simplified interface through __init__.py
- Factory Pattern: Creates utility objects
"""

from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
from datetime import datetime
import re
import hashlib
import json
import os


# =============================================================================
# This would be in a file called: metromap_utils/__init__.py
# =============================================================================

"""
metromap_utils - A collection of reusable Python utilities.

This package provides common utilities for:
- String manipulation
- Data validation
- File handling
- Date formatting
- Hashing and security
"""

__version__ = "1.0.0"
__author__ = "Python Metromap"
__all__ = [
    'strings',
    'validators',
    'files',
    'dates',
    'security',
    'process_data',
    'validate_email',
    'format_currency',
    'hash_password'
]

# Import submodules to expose at package level
# In a real package, these would be in separate files


# =============================================================================
# This would be in a file called: metromap_utils/strings.py
# =============================================================================

class StringUtils:
    """String manipulation utilities."""
    
    @staticmethod
    def reverse(s: str) -> str:
        """Reverse a string."""
        return s[::-1]
    
    @staticmethod
    def capitalize_words(s: str) -> str:
        """Capitalize first letter of each word."""
        return ' '.join(word.capitalize() for word in s.split())
    
    @staticmethod
    def truncate(s: str, max_length: int, suffix: str = "...") -> str:
        """Truncate string to max length with suffix."""
        if len(s) <= max_length:
            return s
        return s[:max_length - len(suffix)] + suffix
    
    @staticmethod
    def slugify(text: str) -> str:
        """Convert text to URL-friendly slug."""
        text = text.lower()
        text = re.sub(r'[^a-z0-9]+', '-', text)
        return text.strip('-')
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """Extract email addresses from text."""
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)
    
    @staticmethod
    def mask_email(email: str) -> str:
        """Mask email for privacy (a***e@example.com)."""
        if '@' not in email:
            return email
        local, domain = email.split('@', 1)
        if len(local) <= 2:
            masked_local = local[0] + '***'
        else:
            masked_local = local[0] + '***' + local[-1]
        return f"{masked_local}@{domain}"


# =============================================================================
# This would be in a file called: metromap_utils/validators.py
# =============================================================================

class Validators:
    """Data validation utilities."""
    
    @staticmethod
    def is_email(email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_phone(phone: str) -> bool:
        """Validate phone number (US format)."""
        digits = re.sub(r'\D', '', phone)
        return 10 <= len(digits) <= 11
    
    @staticmethod
    def is_url(url: str) -> bool:
        """Validate URL format."""
        pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/[-\w%!?=:@]+)*'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def is_positive_number(value: Any) -> bool:
        """Check if value is a positive number."""
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_in_range(value: Any, min_val: float, max_val: float) -> bool:
        """Check if value is within range."""
        try:
            return min_val <= float(value) <= max_val
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def not_empty(value: Any) -> bool:
        """Check if value is not empty."""
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        if isinstance(value, (list, dict, set, tuple)):
            return len(value) > 0
        return True


# =============================================================================
# This would be in a file called: metromap_utils/files.py
# =============================================================================

class FileUtils:
    """File handling utilities."""
    
    @staticmethod
    def read_json(filepath: str) -> Dict:
        """Read JSON file and return dictionary."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def write_json(filepath: str, data: Dict, indent: int = 2) -> None:
        """Write dictionary to JSON file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent)
    
    @staticmethod
    def read_text(filepath: str) -> str:
        """Read text file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    @staticmethod
    def write_text(filepath: str, content: str) -> None:
        """Write text to file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    @staticmethod
    def get_file_size(filepath: str) -> int:
        """Get file size in bytes."""
        return os.path.getsize(filepath)
    
    @staticmethod
    def get_extension(filepath: str) -> str:
        """Get file extension."""
        return os.path.splitext(filepath)[1].lower()


# =============================================================================
# This would be in a file called: metromap_utils/dates.py
# =============================================================================

class DateUtils:
    """Date and time formatting utilities."""
    
    @staticmethod
    def format_date(date_obj: datetime, format_str: str = "%Y-%m-%d") -> str:
        """Format datetime object as string."""
        return date_obj.strftime(format_str)
    
    @staticmethod
    def parse_date(date_str: str, format_str: str = "%Y-%m-%d") -> datetime:
        """Parse date string to datetime."""
        return datetime.strptime(date_str, format_str)
    
    @staticmethod
    def get_age(birth_date: datetime) -> int:
        """Calculate age from birth date."""
        today = datetime.now()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    
    @staticmethod
    def is_weekend(date_obj: datetime) -> bool:
        """Check if date is weekend."""
        return date_obj.weekday() >= 5
    
    @staticmethod
    def get_days_between(date1: datetime, date2: datetime) -> int:
        """Get number of days between two dates."""
        return abs((date2 - date1).days)


# =============================================================================
# This would be in a file called: metromap_utils/security.py
# =============================================================================

class SecurityUtils:
    """Security and hashing utilities."""
    
    @staticmethod
    def hash_password(password: str, algorithm: str = "sha256") -> str:
        """Hash a password using specified algorithm."""
        hash_func = getattr(hashlib, algorithm)
        return hash_func(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Verify password against hash."""
        return SecurityUtils.hash_password(password) == hashed
    
    @staticmethod
    def generate_token(length: int = 32) -> str:
        """Generate secure random token."""
        import secrets
        return secrets.token_hex(length)
    
    @staticmethod
    def mask_sensitive(text: str, visible_start: int = 2, visible_end: int = 2) -> str:
        """Mask sensitive information (credit cards, SSNs)."""
        if len(text) <= visible_start + visible_end:
            return '*' * len(text)
        return text[:visible_start] + '*' * (len(text) - visible_start - visible_end) + text[-visible_end:]


# =============================================================================
# This would be in a file called: metromap_utils/__init__.py (continued)
# =============================================================================

# Create convenience instances
strings = StringUtils()
validators = Validators()
files = FileUtils()
dates = DateUtils()
security = SecurityUtils()

# Convenience functions (facade)
def process_data(data: Dict, operations: List[str]) -> Dict:
    """Process data through a series of operations."""
    result = data.copy()
    for op in operations:
        if op == "clean":
            result = {k: str(v).strip() for k, v in result.items()}
        elif op == "lowercase":
            result = {k: str(v).lower() for k, v in result.items()}
        elif op == "remove_nulls":
            result = {k: v for k, v in result.items() if v is not None}
    return result

def validate_email(email: str) -> bool:
    """Validate email address."""
    return validators.is_email(email)

def format_currency(amount: float, currency: str = "$") -> str:
    """Format amount as currency."""
    return f"{currency}{amount:,.2f}"

def hash_password(password: str) -> str:
    """Hash password for storage."""
    return security.hash_password(password)


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_utility_package():
    """
    Demonstrate using the complete utility package.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: REUSABLE UTILITY PACKAGE")
    print("=" * 60)
    
    print("\n📦 PACKAGE STRUCTURE")
    print("-" * 40)
    
    print("""
metromap_utils/
├── __init__.py          # Package initialization, exports
├── strings.py           # String manipulation utilities
├── validators.py        # Data validation utilities
├── files.py             # File handling utilities
├── dates.py             # Date formatting utilities
└── security.py          # Security and hashing utilities
""")
    
    print("\n1. USING STRING UTILITIES")
    print("-" * 40)
    
    text = "  hello world  "
    print(f"  Original: '{text}'")
    print(f"  strings.reverse: '{strings.reverse(text)}'")
    print(f"  strings.capitalize_words: '{strings.capitalize_words('hello world python')}'")
    print(f"  strings.truncate: '{strings.truncate('This is a very long string', 20)}'")
    print(f"  strings.slugify: '{strings.slugify('Hello World! This is Python.')}'")
    
    print("\n2. USING VALIDATORS")
    print("-" * 40)
    
    print(f"  is_email('alice@example.com'): {validators.is_email('alice@example.com')}")
    print(f"  is_email('invalid'): {validators.is_email('invalid')}")
    print(f"  is_phone('555-123-4567'): {validators.is_phone('555-123-4567')}")
    print(f"  is_url('https://python.org'): {validators.is_url('https://python.org')}")
    print(f"  is_positive_number(42): {validators.is_positive_number(42)}")
    print(f"  is_positive_number(-5): {validators.is_positive_number(-5)}")
    
    print("\n3. USING DATE UTILITIES")
    print("-" * 40)
    
    now = datetime.now()
    print(f"  Now: {now}")
    print(f"  format_date: {dates.format_date(now)}")
    print(f"  is_weekend: {dates.is_weekend(now)}")
    
    birth = datetime(1990, 6, 15)
    print(f"  Age for birth 1990-06-15: {dates.get_age(birth)}")
    
    print("\n4. USING SECURITY UTILITIES")
    print("-" * 40)
    
    password = "mySecretPassword123"
    hashed = security.hash_password(password)
    print(f"  Password: '{password}'")
    print(f"  Hashed: {hashed[:32]}...")
    print(f"  Verify correct: {security.verify_password(password, hashed)}")
    print(f"  Verify incorrect: {security.verify_password('wrong', hashed)}")
    print(f"  Generate token: {security.generate_token(16)}")
    print(f"  Mask credit card: {security.mask_sensitive('4111111111111111', 4, 4)}")
    
    print("\n5. USING FACADE FUNCTIONS (Simplified Interface)")
    print("-" * 40)
    
    print(f"  validate_email('alice@example.com'): {validate_email('alice@example.com')}")
    print(f"  format_currency(1234.56): {format_currency(1234.56)}")
    print(f"  format_currency(1234.56, '€'): {format_currency(1234.56, '€')}")
    
    sample_data = {"name": "  Alice  ", "email": "ALICE@EXAMPLE.COM", "age": None}
    processed = process_data(sample_data, ["clean", "lowercase", "remove_nulls"])
    print(f"  process_data: {sample_data} → {processed}")
    
    print("\n6. INSTALLING THE PACKAGE")
    print("-" * 40)
    
    print("""
# To install the package for development:
pip install -e .

# To install from PyPI (after publishing):
pip install metromap-utils

# To use in your code:
from metromap_utils import strings, validators, format_currency

result = strings.reverse("hello")
print(result)
""")


if __name__ == "__main__":
    demonstrate_utility_package()
```

---

## 📦 Section 4: Third-Party Packages – pip and PyPI

Python's ecosystem of third-party packages is one of its greatest strengths. pip is the package installer, and PyPI is the package repository.

**SOLID Principle Applied: Dependency Inversion** – Your code depends on abstractions provided by packages.

**Design Pattern: Dependency Injection** – Packages provide pre-built dependencies.

```python
"""
THIRD-PARTY PACKAGES: pip AND PyPI

This section covers installing and using third-party packages.

SOLID Principle: Dependency Inversion
- Your code depends on abstractions provided by packages

Design Pattern: Dependency Injection
- Packages provide pre-built dependencies
"""

import sys
import subprocess


def demonstrate_pip_basics():
    """
    Demonstrates basic pip commands.
    """
    print("=" * 60)
    print("SECTION 4A: pip BASICS")
    print("=" * 60)
    
    print("\n1. WHAT IS pip?")
    print("-" * 40)
    
    print("""
pip is the Python package installer.
- Downloads packages from PyPI (Python Package Index)
- Manages dependencies
- Installs and uninstalls packages
- Comes with Python 3.4+
""")
    
    print("\n2. COMMON pip COMMANDS")
    print("-" * 40)
    
    print("""
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install minimum version
pip install package_name>=1.0.0

# Install from requirements file
pip install -r requirements.txt

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package information
pip show package_name

# Freeze current environment (for requirements.txt)
pip freeze > requirements.txt
""")
    
    print("\n3. CHECKING pip VERSION")
    print("-" * 40)
    
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                               capture_output=True, text=True)
        print(f"  {result.stdout.strip()}")
    except Exception as e:
        print(f"  Could not run pip: {e}")
    
    print("\n4. LISTING INSTALLED PACKAGES")
    print("-" * 40)
    
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "list", "--format=freeze"], 
                               capture_output=True, text=True)
        packages = result.stdout.strip().split('\n')[:5]
        print("  First 5 installed packages:")
        for pkg in packages:
            if pkg:
                print(f"    {pkg}")
        if len(packages) > 5:
            print(f"    ... and {len(result.stdout.strip().split('\n')) - 5} more")
    except Exception as e:
        print(f"  Could not list packages: {e}")


def demonstrate_requirements_file():
    """
    Demonstrates requirements.txt and dependency management.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: requirements.txt")
    print("=" * 60)
    
    print("\n1. REQUIREMENTS.TXT FORMAT")
    print("-" * 40)
    
    print("""
# requirements.txt example:
requests==2.31.0          # Exact version
numpy>=1.24.0,<2.0.0      # Version range
pandas                    # Latest version
git+https://github.com/user/repo.git  # From GitHub
-e .                      # Editable install (development)
""")
    
    print("\n2. CREATING REQUIREMENTS.TXT")
    print("-" * 40)
    
    print("""
# Generate from current environment:
pip freeze > requirements.txt

# Generate only direct dependencies (using pip-tools):
pip install pip-tools
pip-compile requirements.in
""")
    
    print("\n3. SAMPLE REQUIREMENTS.TXT FOR DATA SCIENCE PROJECT")
    print("-" * 40)
    
    sample_requirements = """
# Data Science Project Dependencies
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.3.0
jupyter==1.0.0

# Development dependencies
pytest==7.4.0
black==23.7.0
mypy==1.4.0
"""
    print(sample_requirements)
    
    print("\n4. SEPARATING DEPENDENCIES")
    print("-" * 40)
    
    print("""
# requirements.txt - Production dependencies
numpy
pandas

# requirements-dev.txt - Development dependencies
-r requirements.txt
pytest
black
mypy

# Install with:
pip install -r requirements-dev.txt
""")


def demonstrate_virtual_environments():
    """
    Demonstrates virtual environment usage.
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: VIRTUAL ENVIRONMENTS")
    print("=" * 60)
    
    print("\n1. WHY VIRTUAL ENVIRONMENTS?")
    print("-" * 40)
    
    print("""
# Problem: Different projects need different package versions
Project A needs pandas 1.5.0
Project B needs pandas 2.0.0

# Solution: Isolated environments per project
Project A → env_a/ → pandas 1.5.0
Project B → env_b/ → pandas 2.0.0
""")
    
    print("\n2. CREATING A VIRTUAL ENVIRONMENT")
    print("-" * 40)
    
    print("""
# Using venv (built-in)
python -m venv myproject_env

# Using virtualenv (third-party, more features)
pip install virtualenv
virtualenv myproject_env

# Using conda (for Anaconda users)
conda create --name myproject_env python=3.11
""")
    
    print("\n3. ACTIVATING VIRTUAL ENVIRONMENT")
    print("-" * 40)
    
    print("""
# Windows:
myproject_env\\Scripts\\activate

# macOS/Linux:
source myproject_env/bin/activate

# After activation, you'll see (myproject_env) in your prompt
# pip install now installs into this environment only
""")
    
    print("\n4. DEACTIVATING")
    print("-" * 40)
    
    print("""
deactivate
""")
    
    print("\n5. USING pipenv (Alternative)")
    print("-" * 40)
    
    print("""
# Install pipenv
pip install pipenv

# Create environment and install dependencies
pipenv install requests

# Install dev dependencies
pipenv install --dev pytest

# Activate environment
pipenv shell

# Run a command in environment
pipenv run python script.py
""")


def demonstrate_popular_packages():
    """
    Demonstrates popular third-party packages by category.
    """
    print("\n" + "=" * 60)
    print("SECTION 4D: POPULAR THIRD-PARTY PACKAGES")
    print("=" * 60)
    
    categories = {
        "Data Science & Analysis": [
            ("numpy", "Numerical computing with arrays"),
            ("pandas", "Data manipulation and analysis"),
            ("scipy", "Scientific computing"),
            ("matplotlib", "Plotting and visualization"),
            ("seaborn", "Statistical data visualization"),
            ("scikit-learn", "Machine learning")
        ],
        "Web Development": [
            ("requests", "HTTP client library"),
            ("flask", "Micro web framework"),
            ("django", "Full-stack web framework"),
            ("fastapi", "Modern web API framework"),
            ("beautifulsoup4", "HTML/XML parsing")
        ],
        "Development Tools": [
            ("pytest", "Testing framework"),
            ("black", "Code formatter"),
            ("mypy", "Static type checker"),
            ("ruff", "Fast linter"),
            ("pre-commit", "Git hook manager")
        ],
        "Utilities": [
            ("click", "Command-line interface creation"),
            ("rich", "Rich text formatting in terminal"),
            ("tqdm", "Progress bars"),
            ("python-dotenv", "Environment variable management"),
            ("pydantic", "Data validation using type hints")
        ]
    }
    
    for category, packages in categories.items():
        print(f"\n📁 {category}")
        print("-" * 40)
        for name, description in packages:
            print(f"  {name:15} - {description}")


if __name__ == "__main__":
    demonstrate_pip_basics()
    demonstrate_requirements_file()
    demonstrate_virtual_environments()
    demonstrate_popular_packages()
```

---

## 🏭 Section 5: Complete Data Processing Package

A complete, production-ready data processing package that demonstrates professional package structure, testing, and documentation.

**SOLID Principles Applied:**
- Single Responsibility: Each module has one purpose
- Open/Closed: New processors can be added
- Dependency Inversion: Depends on abstractions

**Design Patterns:**
- Pipeline Pattern: Data flows through processors
- Factory Pattern: Creates processor instances
- Strategy Pattern: Different processing strategies

```python
"""
COMPLETE DATA PROCESSING PACKAGE

This section builds a complete, production-ready data processing package.

SOLID Principles Applied:
- Single Responsibility: Each module has one purpose
- Open/Closed: New processors can be added
- Dependency Inversion: Depends on abstractions

Design Patterns:
- Pipeline Pattern: Data flows through processors
- Factory Pattern: Creates processor instances
- Strategy Pattern: Different processing strategies
"""

from typing import List, Dict, Any, Optional, Callable, Union
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum
import csv
import json
from io import StringIO


# =============================================================================
# data_processor/exceptions.py
# =============================================================================

class DataProcessorError(Exception):
    """Base exception for data processor."""
    pass


class ValidationError(DataProcessorError):
    """Raised when data validation fails."""
    pass


class ProcessingError(DataProcessorError):
    """Raised when data processing fails."""
    pass


# =============================================================================
# data_processor/models.py
# =============================================================================

@dataclass
class DataRecord:
    """Represents a single data record."""
    data: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get value from data dictionary."""
        return self.data.get(key, default)
    
    def set(self, key: str, value: Any) -> 'DataRecord':
        """Set value in data dictionary."""
        self.data[key] = value
        return self


@dataclass
class ProcessingResult:
    """Result of data processing."""
    success: bool
    records_processed: int
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    processed_data: List[DataRecord] = field(default_factory=list)
    
    def summary(self) -> str:
        """Generate summary of processing result."""
        return f"Processed {self.records_processed} records. Success: {self.success}. Errors: {len(self.errors)}"


# =============================================================================
# data_processor/validators.py
# =============================================================================

class Validator(ABC):
    """Base class for data validators."""
    
    @abstractmethod
    def validate(self, record: DataRecord) -> Tuple[bool, Optional[str]]:
        """
        Validate a record.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        pass


class RequiredFieldValidator(Validator):
    """Validates that required fields are present."""
    
    def __init__(self, required_fields: List[str]):
        self.required_fields = required_fields
    
    def validate(self, record: DataRecord) -> Tuple[bool, Optional[str]]:
        for field in self.required_fields:
            if field not in record.data or record.data[field] is None:
                return False, f"Missing required field: {field}"
        return True, None


class TypeValidator(Validator):
    """Validates field types."""
    
    def __init__(self, field: str, expected_type: type):
        self.field = field
        self.expected_type = expected_type
    
    def validate(self, record: DataRecord) -> Tuple[bool, Optional[str]]:
        value = record.data.get(self.field)
        if value is not None and not isinstance(value, self.expected_type):
            return False, f"Field '{self.field}' should be {self.expected_type.__name__}, got {type(value).__name__}"
        return True, None


class RangeValidator(Validator):
    """Validates numeric range."""
    
    def __init__(self, field: str, min_val: Optional[float] = None, max_val: Optional[float] = None):
        self.field = field
        self.min_val = min_val
        self.max_val = max_val
    
    def validate(self, record: DataRecord) -> Tuple[bool, Optional[str]]:
        value = record.data.get(self.field)
        if value is None:
            return True, None
        
        try:
            num = float(value)
        except (ValueError, TypeError):
            return False, f"Field '{self.field}' is not numeric: {value}"
        
        if self.min_val is not None and num < self.min_val:
            return False, f"Field '{self.field}' is below minimum {self.min_val}: {num}"
        
        if self.max_val is not None and num > self.max_val:
            return False, f"Field '{self.field}' exceeds maximum {self.max_val}: {num}"
        
        return True, None


# =============================================================================
# data_processor/transformers.py
# =============================================================================

class Transformer(ABC):
    """Base class for data transformers."""
    
    @abstractmethod
    def transform(self, record: DataRecord) -> DataRecord:
        """Transform a record."""
        pass


class FieldMapper(Transformer):
    """Maps fields to new names."""
    
    def __init__(self, mapping: Dict[str, str]):
        self.mapping = mapping
    
    def transform(self, record: DataRecord) -> DataRecord:
        new_data = {}
        for key, value in record.data.items():
            new_key = self.mapping.get(key, key)
            new_data[new_key] = value
        record.data = new_data
        return record


class FieldCalculator(Transformer):
    """Adds computed fields."""
    
    def __init__(self, field_name: str, calculation: Callable[[Dict], Any]):
        self.field_name = field_name
        self.calculation = calculation
    
    def transform(self, record: DataRecord) -> DataRecord:
        value = self.calculation(record.data)
        record.data[self.field_name] = value
        return record


class StringCleaner(Transformer):
    """Cleans string fields."""
    
    def __init__(self, fields: Optional[List[str]] = None):
        self.fields = fields
    
    def transform(self, record: DataRecord) -> DataRecord:
        for key, value in record.data.items():
            if self.fields is None or key in self.fields:
                if isinstance(value, str):
                    record.data[key] = value.strip()
        return record


# =============================================================================
# data_processor/pipeline.py
# =============================================================================

class ProcessingPipeline:
    """
    Data processing pipeline.
    
    Design Pattern: Pipeline Pattern - Chains multiple processors
    """
    
    def __init__(self):
        self.validators: List[Validator] = []
        self.transformers: List[Transformer] = []
        self.error_on_validation_failure: bool = True
    
    def add_validator(self, validator: Validator) -> 'ProcessingPipeline':
        """Add a validator to the pipeline."""
        self.validators.append(validator)
        return self
    
    def add_transformer(self, transformer: Transformer) -> 'ProcessingPipeline':
        """Add a transformer to the pipeline."""
        self.transformers.append(transformer)
        return self
    
    def process_record(self, record: DataRecord) -> Tuple[bool, DataRecord, List[str]]:
        """
        Process a single record through the pipeline.
        
        Returns:
            Tuple of (success, processed_record, errors)
        """
        errors = []
        
        # Validation stage
        for validator in self.validators:
            is_valid, error = validator.validate(record)
            if not is_valid:
                errors.append(error)
                if self.error_on_validation_failure:
                    return False, record, errors
        
        # Transformation stage
        processed = record
        for transformer in self.transformers:
            processed = transformer.transform(processed)
        
        return len(errors) == 0, processed, errors
    
    def process_batch(self, records: List[DataRecord]) -> ProcessingResult:
        """
        Process a batch of records.
        
        Returns:
            ProcessingResult with statistics
        """
        processed_records = []
        errors = []
        warnings = []
        
        for record in records:
            success, processed, record_errors = self.process_record(record)
            if success:
                processed_records.append(processed)
            else:
                errors.extend(record_errors)
        
        return ProcessingResult(
            success=len(errors) == 0,
            records_processed=len(processed_records),
            errors=errors,
            warnings=warnings,
            processed_data=processed_records
        )


# =============================================================================
# data_processor/io.py
# =============================================================================

class DataReader(ABC):
    """Base class for data readers."""
    
    @abstractmethod
    def read(self, source: Any) -> List[DataRecord]:
        """Read data from source."""
        pass


class CSVReader(DataReader):
    """Reads CSV data."""
    
    def __init__(self, has_header: bool = True):
        self.has_header = has_header
    
    def read(self, source: Union[str, StringIO]) -> List[DataRecord]:
        records = []
        
        if isinstance(source, str):
            source = StringIO(source)
        
        reader = csv.DictReader(source) if self.has_header else csv.reader(source)
        
        if self.has_header:
            for row in reader:
                records.append(DataRecord(data=row))
        else:
            for row in reader:
                records.append(DataRecord(data={f"col_{i}": val for i, val in enumerate(row)}))
        
        return records


class JSONReader(DataReader):
    """Reads JSON data."""
    
    def read(self, source: Union[str, StringIO]) -> List[DataRecord]:
        if isinstance(source, str):
            data = json.loads(source)
        else:
            data = json.load(source)
        
        if isinstance(data, list):
            return [DataRecord(data=item) for item in data]
        elif isinstance(data, dict):
            return [DataRecord(data=data)]
        else:
            raise ValueError(f"Unsupported JSON type: {type(data)}")


class DataWriter(ABC):
    """Base class for data writers."""
    
    @abstractmethod
    def write(self, records: List[DataRecord], destination: Any) -> None:
        """Write data to destination."""
        pass


class CSVWriter(DataWriter):
    """Writes CSV data."""
    
    def __init__(self, fieldnames: Optional[List[str]] = None):
        self.fieldnames = fieldnames
    
    def write(self, records: List[DataRecord], destination: StringIO) -> None:
        if not records:
            return
        
        if not self.fieldnames:
            self.fieldnames = list(records[0].data.keys())
        
        writer = csv.DictWriter(destination, fieldnames=self.fieldnames)
        writer.writeheader()
        
        for record in records:
            writer.writerow(record.data)


class JSONWriter(DataWriter):
    """Writes JSON data."""
    
    def __init__(self, indent: int = 2):
        self.indent = indent
    
    def write(self, records: List[DataRecord], destination: StringIO) -> None:
        data = [record.data for record in records]
        json.dump(data, destination, indent=self.indent)


# =============================================================================
# data_processor/__init__.py
# =============================================================================

__version__ = "1.0.0"
__all__ = [
    'DataRecord',
    'ProcessingResult',
    'ProcessingPipeline',
    'Validator',
    'RequiredFieldValidator',
    'TypeValidator',
    'RangeValidator',
    'Transformer',
    'FieldMapper',
    'FieldCalculator',
    'StringCleaner',
    'DataReader',
    'CSVReader',
    'JSONReader',
    'DataWriter',
    'CSVWriter',
    'JSONWriter',
    'ValidationError',
    'ProcessingError'
]


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_data_processing_package():
    """
    Demonstrate the complete data processing package.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: COMPLETE DATA PROCESSING PACKAGE")
    print("=" * 60)
    
    print("\n📦 PACKAGE STRUCTURE")
    print("-" * 40)
    
    print("""
data_processor/
├── __init__.py          # Package exports
├── exceptions.py        # Custom exceptions
├── models.py            # Data models
├── validators.py        # Validation classes
├── transformers.py      # Transformation classes
├── pipeline.py          # Processing pipeline
└── io.py                # Input/output handlers
""")
    
    # Create sample data
    print("\n1. CREATING SAMPLE DATA")
    print("-" * 40)
    
    sample_csv = """name,age,email,score
Alice,25,alice@example.com,95
Bob,30,bob@example.com,87
Charlie,-5,invalid,92
Diana,28,diana@example.com,105
"""
    
    print("  Sample CSV data:")
    print(sample_csv)
    
    # Read data
    print("\n2. READING DATA")
    print("-" * 40)
    
    reader = CSVReader(has_header=True)
    records = reader.read(sample_csv)
    print(f"  Read {len(records)} records")
    for i, record in enumerate(records[:2], 1):
        print(f"    Record {i}: {record.data}")
    
    # Build processing pipeline
    print("\n3. BUILDING PROCESSING PIPELINE")
    print("-" * 40)
    
    pipeline = ProcessingPipeline()
    
    # Add validators
    pipeline.add_validator(RequiredFieldValidator(['name', 'age', 'email']))
    pipeline.add_validator(TypeValidator('age', int))
    pipeline.add_validator(RangeValidator('age', min_val=0, max_val=120))
    pipeline.add_validator(RangeValidator('score', min_val=0, max_val=100))
    
    # Add transformers
    pipeline.add_transformer(StringCleaner(['name', 'email']))
    pipeline.add_transformer(FieldCalculator('age_group', lambda d: 'adult' if d.get('age', 0) >= 18 else 'minor'))
    pipeline.add_transformer(FieldCalculator('grade', lambda d: 
        'A' if d.get('score', 0) >= 90 else
        'B' if d.get('score', 0) >= 80 else
        'C' if d.get('score', 0) >= 70 else
        'D' if d.get('score', 0) >= 60 else 'F'
    ))
    
    print("  Pipeline configured with:")
    print(f"    Validators: {len(pipeline.validators)}")
    print(f"    Transformers: {len(pipeline.transformers)}")
    
    # Process data
    print("\n4. PROCESSING DATA")
    print("-" * 40)
    
    result = pipeline.process_batch(records)
    
    print(f"  Processing Result:")
    print(f"    Success: {result.success}")
    print(f"    Records processed: {result.records_processed}")
    print(f"    Errors: {len(result.errors)}")
    
    if result.errors:
        print("\n  Errors:")
        for error in result.errors[:3]:
            print(f"    • {error}")
    
    print("\n  Processed Data:")
    for record in result.processed_data[:3]:
        print(f"    {record.data}")
    
    # Write processed data
    print("\n5. WRITING PROCESSED DATA")
    print("-" * 40)
    
    output = StringIO()
    writer = CSVWriter()
    writer.write(result.processed_data, output)
    
    print("  CSV Output:")
    print(output.getvalue())
    
    # JSON output
    print("\n6. JSON OUTPUT")
    print("-" * 40)
    
    json_output = StringIO()
    json_writer = JSONWriter(indent=2)
    json_writer.write(result.processed_data, json_output)
    
    print("  JSON Output (first 300 chars):")
    print(json_output.getvalue()[:300] + "...")
    
    print("\n7. PACKAGE USAGE SUMMARY")
    print("-" * 40)
    
    print("""
# Install the package
pip install data-processor

# Use in your code
from data_processor import (
    CSVReader, ProcessingPipeline,
    RequiredFieldValidator, RangeValidator,
    FieldCalculator, StringCleaner
)

# Create pipeline
pipeline = (ProcessingPipeline()
    .add_validator(RequiredFieldValidator(['name', 'email']))
    .add_validator(RangeValidator('age', 0, 120))
    .add_transformer(StringCleaner())
    .add_transformer(FieldCalculator('age_group', lambda d: 'adult' if d['age'] >= 18 else 'minor')))

# Process data
reader = CSVReader()
records = reader.read(csv_data)
result = pipeline.process_batch(records)
""")


if __name__ == "__main__":
    demonstrate_data_processing_package()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Modules** – Single Python files containing code. Filename becomes module name. Use `import` to access.

- **Packages** – Directories containing modules and `__init__.py`. Allow hierarchical organization.

- **`__init__.py`** – Package initialization file. Can set `__all__` to control exports. Provides facade pattern.

- **Import Syntax** – `import module`, `from module import function`, `import module as alias`.

- **`__name__ == '__main__'`** – Guard to run code only when script executed directly (not imported).

- **Module Search Path** – Python searches `sys.path` directories. Current directory first, then PYTHONPATH, then standard library.

- **Virtual Environments** – Isolated environments for different projects. `venv`, `virtualenv`, or `conda`.

- **pip** – Package installer. `pip install`, `pip freeze`, `pip list`. Requirements.txt for dependencies.

- **PyPI** – Python Package Index. Repository of thousands of third-party packages.

- **Utility Package** – Reusable package with string, validation, file, date, security utilities.

- **Data Processing Package** – Professional package with validators, transformers, pipeline pattern, I/O handlers.

- **SOLID Principles Applied** – Single Responsibility (each module has one purpose), Interface Segregation (clean public interfaces), Dependency Inversion (depends on abstractions), Open/Closed (new processors can be added).

- **Design Patterns Used** – Module Pattern (file-based organization), Facade Pattern (`__init__.py` simplification), Pipeline Pattern (data processing), Strategy Pattern (validators/transformers), Factory Pattern (reader/writer creation), Dependency Injection (third-party packages).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Recursion – Functions Calling Themselves

- **📚 Series B Catalog:** Functions & Modules Yard – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Lists – Ordered & Mutable (Series C, Story 1)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **18** | **34** | **35%** |

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

**Next Story:** Series C, Story 1: The 2026 Python Metromap: Lists – Ordered & Mutable

---

## 📝 Your Invitation

**Congratulations! You've completed Functions & Modules Yard!**

You've mastered:
- Defining functions with proper arguments and return values
- Lambda functions for simple operations
- Recursion for tree-like problems
- Modules and packages for organizing code

Now build something with what you've learned:

1. **Create your own utility package** – Build a package with string, validation, and date utilities. Publish it to a private repository.

2. **Build a data processing pipeline** – Create a package that reads CSV, validates records, transforms data, and writes JSON.

3. **Create a configuration management package** – Build a package that reads config from JSON/YAML, validates settings, and provides defaults.

4. **Package a previous project** – Take any project from Series A, organize it as a package, add `__init__.py`, and make it importable.

5. **Write and publish a package** – Create a simple package, write setup.py, and publish to Test PyPI.

**You've mastered Functions & Modules Yard. Next stop: Data Structures Express – Lists!**

---

*Found this helpful? Clap, comment, and share what package you built. Next stop: Lists!* 🚇