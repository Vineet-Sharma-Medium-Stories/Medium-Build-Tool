# The 2026 Python Metromap: Testing & Debugging – pytest and unittest

## Series F: Advanced Python Engineering | Story 5 of 6

![The 2026 Python Metromap/images/Testing and Debugging – pytest and unittest](images/Testing and Debugging – pytest and unittest.png)

## 📖 Introduction

**Welcome to the fifth stop on the Advanced Python Engineering Line.**

You've mastered decorators, generators, iterators, and memory management. You can write efficient, elegant code that handles large datasets and manages resources properly. But how do you know your code works correctly? How do you ensure that changes don't break existing functionality? How do you debug when things go wrong?

Testing and debugging are essential practices for building reliable software. Tests verify that your code behaves as expected, catch regressions before they reach production, and serve as living documentation. Debugging helps you understand why tests fail and fix the underlying issues. Together, they form the foundation of professional software development.

This story—**The 2026 Python Metromap: Testing & Debugging – pytest and unittest**—is your guide to testing and debugging Python code. We'll explore the built-in `unittest` framework and the more modern `pytest`. We'll write unit tests, integration tests, and end-to-end tests. We'll use fixtures, mocking, and parametrization. We'll debug with print statements, logging, the Python debugger (pdb), and breakpoints. We'll build a complete CI/CD pipeline with automated testing. And we'll create a test coverage reporting system.

**Let's test and debug.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories) – COMPLETED
### Series B: Functions & Modules Yard (6 Stories) – COMPLETED
### Series C: Data Structures Express (5 Stories) – COMPLETED
### Series D: Object-Oriented Programming (OOP) Line (6 Stories) – COMPLETED
### Series E: File & Data Handling Line (5 Stories) – COMPLETED

### Series F: Advanced Python Engineering (6 Stories)

- 🎨 **The 2026 Python Metromap: Decorators – Wrapping Functions** – Authentication middleware; logging decorators; API retry logic.

- 🔄 **The 2026 Python Metromap: Generators – Memory-Efficient Loops** – Streaming large CSV files; paginated API responses; infinite data streams.

- 🔁 **The 2026 Python Metromap: Iterators – Custom Looping** – Database paginator; file chunk reader; Fibonacci sequence iterator.

- 🧠 **The 2026 Python Metromap: Memory Management & Garbage Collection** – Optimizing a recommendation engine; memory profiling; leak fixing.

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports. **⬅️ YOU ARE HERE**

- 📝 **The 2026 Python Metromap: Type Hints & MyPy** – Large team codebase annotations; pre-runtime bug catching; automatic documentation. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## ✅ Section 1: unittest – Python's Built-in Testing Framework

The `unittest` module provides a testing framework inspired by JUnit, with test cases, assertions, and test discovery.

**SOLID Principle Applied: Single Responsibility** – Each test method tests one specific behavior.

**Design Pattern: Command Pattern** – Test cases are commands that can be run individually or in suites.

```python
"""
UNITTEST: PYTHON'S BUILT-IN TESTING FRAMEWORK

This section covers the unittest module for writing tests.

SOLID Principle: Single Responsibility
- Each test method tests one specific behavior

Design Pattern: Command Pattern
- Test cases are commands that can be run individually
"""

import unittest
import sys
from io import StringIO
from datetime import datetime, date
import math


# =============================================================================
# CODE TO TEST
# =============================================================================

class Calculator:
    """Simple calculator for demonstration."""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


class BankAccount:
    """Bank account for demonstration."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        
        if initial_balance > 0:
            self._record_transaction("deposit", initial_balance)
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self._record_transaction("deposit", amount)
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record_transaction("withdrawal", amount)
        return self.balance
    
    def _record_transaction(self, type, amount):
        self.transactions.append({
            "type": type,
            "amount": amount,
            "balance": self.balance,
            "timestamp": datetime.now()
        })
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_count(self):
        return len(self.transactions)


class UserValidator:
    """Validates user data."""
    
    @staticmethod
    def validate_email(email):
        if not email:
            return False
        return "@" in email and "." in email.split("@")[-1]
    
    @staticmethod
    def validate_age(age):
        if not isinstance(age, (int, float)):
            return False
        return 0 <= age <= 150
    
    @staticmethod
    def validate_username(username):
        if not username or len(username) < 3:
            return False
        return username.isalnum()


# =============================================================================
# UNIT TESTS
# =============================================================================

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures - runs before each test."""
        self.calc = Calculator()
        print(f"  Setting up Calculator test")
    
    def tearDown(self):
        """Clean up after tests - runs after each test."""
        print(f"  Tearing down Calculator test")
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test exponentiation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
    
    def test_factorial(self):
        """Test factorial."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
    
    def test_factorial_negative(self):
        """Test factorial with negative number."""
        with self.assertRaises(ValueError):
            self.calc.factorial(-5)


class TestBankAccount(unittest.TestCase):
    """Test cases for BankAccount class."""
    
    def setUp(self):
        self.account = BankAccount("Alice", 1000)
    
    def test_initial_balance(self):
        """Test initial balance is set correctly."""
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_deposit(self):
        """Test deposit increases balance."""
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)
    
    def test_deposit_negative(self):
        """Test deposit with negative amount raises error."""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_withdraw(self):
        """Test withdrawal decreases balance."""
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds."""
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
    
    def test_transaction_record(self):
        """Test transactions are recorded."""
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_transaction_count(), 3)  # Initial deposit + 2
        self.assertEqual(self.account.transactions[0]["type"], "deposit")
        self.assertEqual(self.account.transactions[0]["amount"], 1000)


class TestUserValidator(unittest.TestCase):
    """Test cases for UserValidator."""
    
    def test_validate_email_valid(self):
        """Test valid email addresses."""
        self.assertTrue(UserValidator.validate_email("user@example.com"))
        self.assertTrue(UserValidator.validate_email("name.last@domain.co.uk"))
    
    def test_validate_email_invalid(self):
        """Test invalid email addresses."""
        self.assertFalse(UserValidator.validate_email(""))
        self.assertFalse(UserValidator.validate_email("invalid"))
        self.assertFalse(UserValidator.validate_email("missing@domain"))
    
    def test_validate_age_valid(self):
        """Test valid ages."""
        self.assertTrue(UserValidator.validate_age(25))
        self.assertTrue(UserValidator.validate_age(0))
        self.assertTrue(UserValidator.validate_age(150))
    
    def test_validate_age_invalid(self):
        """Test invalid ages."""
        self.assertFalse(UserValidator.validate_age(-5))
        self.assertFalse(UserValidator.validate_age(200))
        self.assertFalse(UserValidator.validate_age("twenty"))
    
    def test_validate_username_valid(self):
        """Test valid usernames."""
        self.assertTrue(UserValidator.validate_username("alice123"))
        self.assertTrue(UserValidator.validate_username("BobTheBuilder"))
    
    def test_validate_username_invalid(self):
        """Test invalid usernames."""
        self.assertFalse(UserValidator.validate_username(""))
        self.assertFalse(UserValidator.validate_username("ab"))  # Too short
        self.assertFalse(UserValidator.validate_username("user@name"))  # Special chars


# =============================================================================
# TEST SUITE
# =============================================================================

def create_test_suite():
    """Create a test suite with specific tests."""
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTest(TestCalculator('test_add'))
    suite.addTest(TestCalculator('test_divide'))
    suite.addTest(TestBankAccount('test_deposit'))
    suite.addTest(TestBankAccount('test_withdraw'))
    
    return suite


def run_tests():
    """Run all tests."""
    # Create test loader
    loader = unittest.TestLoader()
    
    # Create test suite from test classes
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccount))
    suite.addTests(loader.loadTestsFromTestCase(TestUserValidator))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


def demonstrate_unittest():
    """
    Demonstrate the unittest framework.
    """
    print("\n" + "=" * 60)
    print("SECTION 1: UNITTEST FRAMEWORK")
    print("=" * 60)
    
    print("\n1. TEST CLASS STRUCTURE")
    print("-" * 40)
    
    print("""
    class TestCalculator(unittest.TestCase):
        def setUp(self):
            # Runs before each test
            self.calc = Calculator()
        
        def tearDown(self):
            # Runs after each test
            pass
        
        def test_add(self):
            # Test method (must start with 'test_')
            self.assertEqual(self.calc.add(2, 3), 5)
        
        def test_divide_by_zero(self):
            # Test exception
            with self.assertRaises(ValueError):
                self.calc.divide(10, 0)
    """)
    
    print("\n2. COMMON ASSERTIONS")
    print("-" * 40)
    
    print("""
    Assertion Methods:
    - assertEqual(a, b)          a == b
    - assertNotEqual(a, b)       a != b
    - assertTrue(x)              bool(x) is True
    - assertFalse(x)             bool(x) is False
    - assertIs(a, b)             a is b
    - assertIsNot(a, b)          a is not b
    - assertIsNone(x)            x is None
    - assertIsNotNone(x)         x is not None
    - assertIn(a, b)             a in b
    - assertNotIn(a, b)          a not in b
    - assertIsInstance(a, b)     isinstance(a, b)
    - assertRaises(Exc, func)    func raises Exc
    """)
    
    print("\n3. RUNNING TESTS")
    print("-" * 40)
    
    # Run tests and capture output
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=1)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    runner.run(suite)
    
    output = stream.getvalue()
    print("  Test output preview:")
    for line in output.split('\n')[:5]:
        if line.strip():
            print(f"    {line}")
    
    print("\n4. TEST DISCOVERY")
    print("-" * 40)
    
    print("""
    # Discover and run all tests in directory
    python -m unittest discover
    
    # Discover tests in specific directory
    python -m unittest discover -s tests
    
    # Discover tests matching pattern
    python -m unittest discover -p "test_*.py"
    
    # Run specific test file
    python -m unittest test_calculator.py
    
    # Run specific test class
    python -m unittest test_calculator.TestCalculator
    
    # Run specific test method
    python -m unittest test_calculator.TestCalculator.test_add
    """)


if __name__ == "__main__":
    demonstrate_unittest()
    
    # Run the actual tests (commented to avoid output in demo)
    # result = run_tests()
    # print(f"\n  Tests run: {result.testsRun}")
    # print(f"  Failures: {len(result.failures)}")
    # print(f"  Errors: {len(result.errors)}")
```

---

## 🧪 Section 2: pytest – Modern Python Testing

pytest is a more modern, feature-rich testing framework with simpler syntax, fixtures, and powerful plugins.

**SOLID Principles Applied:**
- Single Responsibility: Each test function tests one behavior
- Dependency Inversion: Fixtures provide dependencies

**Design Patterns:**
- Fixture Pattern: Provides test context and data
- Parametrization Pattern: Runs same test with different inputs

```python
"""
PYTEST: MODERN PYTHON TESTING

This section covers pytest, a more modern testing framework.

SOLID Principles Applied:
- Single Responsibility: Each test tests one behavior
- Dependency Inversion: Fixtures provide dependencies

Design Patterns:
- Fixture Pattern: Provides test context and data
- Parametrization Pattern: Runs tests with different inputs
"""

import pytest
from typing import List, Dict, Any
from datetime import datetime, timedelta
import tempfile
import json
import os


# =============================================================================
# CODE TO TEST
# =============================================================================

class TaskManager:
    """Task manager for demonstration."""
    
    def __init__(self):
        self.tasks: List[Dict] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "", priority: int = 2) -> int:
        """Add a task and return its ID."""
        if not title:
            raise ValueError("Task title cannot be empty")
        if priority not in [1, 2, 3]:
            raise ValueError("Priority must be 1, 2, or 3")
        
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now()
        }
        self.tasks.append(task)
        self.next_id += 1
        return task["id"]
    
    def get_task(self, task_id: int) -> Dict:
        """Get task by ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise ValueError(f"Task {task_id} not found")
    
    def complete_task(self, task_id: int) -> None:
        """Mark task as completed."""
        task = self.get_task(task_id)
        task["completed"] = True
    
    def get_pending_tasks(self) -> List[Dict]:
        """Get all pending tasks."""
        return [t for t in self.tasks if not t["completed"]]
    
    def get_tasks_by_priority(self, priority: int) -> List[Dict]:
        """Get tasks by priority."""
        return [t for t in self.tasks if t["priority"] == priority]
    
    def save_to_file(self, filepath: str) -> None:
        """Save tasks to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.tasks, f, indent=2, default=str)
    
    def load_from_file(self, filepath: str) -> None:
        """Load tasks from JSON file."""
        with open(filepath, 'r') as f:
            self.tasks = json.load(f)
            if self.tasks:
                self.next_id = max(t["id"] for t in self.tasks) + 1


class DataProcessor:
    """Data processing utility."""
    
    @staticmethod
    def filter_evens(numbers: List[int]) -> List[int]:
        """Filter even numbers."""
        return [n for n in numbers if n % 2 == 0]
    
    @staticmethod
    def square_numbers(numbers: List[int]) -> List[int]:
        """Square all numbers."""
        return [n ** 2 for n in numbers]
    
    @staticmethod
    def calculate_average(numbers: List[int]) -> float:
        """Calculate average of numbers."""
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)


# =============================================================================
# PYTEST TESTS
# =============================================================================

class TestTaskManager:
    """Test cases for TaskManager using pytest style."""
    
    @pytest.fixture
    def task_manager(self):
        """Fixture providing a TaskManager instance."""
        tm = TaskManager()
        tm.add_task("Test Task 1", "Description 1", 1)
        tm.add_task("Test Task 2", "Description 2", 2)
        return tm
    
    @pytest.fixture
    def populated_manager(self):
        """Fixture with pre-populated tasks."""
        tm = TaskManager()
        tm.add_task("High Priority", priority=1)
        tm.add_task("Medium Priority", priority=2)
        tm.add_task("Low Priority", priority=3)
        tm.add_task("Another High", priority=1)
        return tm
    
    def test_add_task(self, task_manager):
        """Test adding a task."""
        task_id = task_manager.add_task("New Task", "Description", 3)
        assert task_id == 3
        task = task_manager.get_task(task_id)
        assert task["title"] == "New Task"
        assert task["priority"] == 3
        assert not task["completed"]
    
    def test_add_task_empty_title(self, task_manager):
        """Test adding task with empty title raises error."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            task_manager.add_task("")
    
    def test_add_task_invalid_priority(self, task_manager):
        """Test adding task with invalid priority."""
        with pytest.raises(ValueError):
            task_manager.add_task("Task", priority=5)
    
    def test_get_task(self, task_manager):
        """Test getting task by ID."""
        task = task_manager.get_task(1)
        assert task["title"] == "Test Task 1"
        assert task["description"] == "Description 1"
    
    def test_get_task_not_found(self, task_manager):
        """Test getting non-existent task."""
        with pytest.raises(ValueError, match="Task 999 not found"):
            task_manager.get_task(999)
    
    def test_complete_task(self, task_manager):
        """Test completing a task."""
        task_manager.complete_task(1)
        task = task_manager.get_task(1)
        assert task["completed"]
    
    def test_get_pending_tasks(self, task_manager):
        """Test getting pending tasks."""
        pending = task_manager.get_pending_tasks()
        assert len(pending) == 2
        
        task_manager.complete_task(1)
        pending = task_manager.get_pending_tasks()
        assert len(pending) == 1
        assert pending[0]["id"] == 2
    
    def test_get_tasks_by_priority(self, populated_manager):
        """Test filtering tasks by priority."""
        high_priority = populated_manager.get_tasks_by_priority(1)
        assert len(high_priority) == 2
        
        medium_priority = populated_manager.get_tasks_by_priority(2)
        assert len(medium_priority) == 1
    
    @pytest.mark.parametrize("title,priority,expected", [
        ("Task 1", 1, True),
        ("Task 2", 2, True),
        ("Task 3", 3, True),
    ])
    def test_add_multiple_tasks(self, task_manager, title, priority, expected):
        """Test adding multiple tasks with parametrization."""
        task_id = task_manager.add_task(title, priority=priority)
        assert task_id > 0
        task = task_manager.get_task(task_id)
        assert task["title"] == title
        assert task["priority"] == priority
    
    def test_save_and_load(self, task_manager):
        """Test saving and loading tasks to file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            # Save tasks
            task_manager.save_to_file(temp_file)
            
            # Create new manager and load
            new_manager = TaskManager()
            new_manager.load_from_file(temp_file)
            
            assert len(new_manager.tasks) == 2
            assert new_manager.get_task(1)["title"] == "Test Task 1"
        finally:
            os.unlink(temp_file)


class TestDataProcessor:
    """Test cases for DataProcessor."""
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2, 3, 4, 5], [2, 4]),
        ([], []),
        ([1, 3, 5], []),
        ([2, 4, 6], [2, 4, 6]),
    ])
    def test_filter_evens(self, input_list, expected):
        """Test filtering even numbers with parametrization."""
        assert DataProcessor.filter_evens(input_list) == expected
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2, 3], [1, 4, 9]),
        ([], []),
        ([-1, -2], [1, 4]),
    ])
    def test_square_numbers(self, input_list, expected):
        """Test squaring numbers."""
        assert DataProcessor.square_numbers(input_list) == expected
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20, 30], 20.0),
        ([], 0.0),
        ([5], 5.0),
    ])
    def test_calculate_average(self, input_list, expected):
        """Test average calculation."""
        assert DataProcessor.calculate_average(input_list) == expected
    
    def test_chained_operations(self):
        """Test chaining multiple operations."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Chain: filter evens → square → average
        evens = DataProcessor.filter_evens(data)
        squares = DataProcessor.square_numbers(evens)
        average = DataProcessor.calculate_average(squares)
        
        assert average == 44.0  # (4 + 16 + 36 + 64 + 100) / 5 = 44


# =============================================================================
# FIXTURE TYPES
# =============================================================================

@pytest.fixture(scope="function")
def function_scope_fixture():
    """Runs once per test function."""
    print("\n  Function scope fixture setup")
    yield "function_data"
    print("  Function scope fixture teardown")


@pytest.fixture(scope="module")
def module_scope_fixture():
    """Runs once per test module."""
    print("\n  Module scope fixture setup")
    yield "module_data"
    print("  Module scope fixture teardown")


@pytest.fixture(scope="session")
def session_scope_fixture():
    """Runs once per test session."""
    print("\n  Session scope fixture setup")
    yield "session_data"
    print("  Session scope fixture teardown")


@pytest.fixture
def sample_data():
    """Provide sample test data."""
    return {
        "names": ["Alice", "Bob", "Charlie"],
        "ages": [28, 35, 22],
        "cities": ["NYC", "LA", "Chicago"]
    }


def test_fixture_example(sample_data):
    """Test using fixture data."""
    assert len(sample_data["names"]) == 3
    assert sample_data["ages"][0] == 28


# =============================================================================
# MARKERS AND SKIPS
# =============================================================================

@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow."""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    """Test that is skipped."""
    assert False


@pytest.mark.skipif(True, reason="Condition met")
def test_conditional_skip():
    """Test skipped conditionally."""
    assert True


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_pytest():
    """
    Demonstrate pytest features.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: PYTEST FRAMEWORK")
    print("=" * 60)
    
    print("\n1. SIMPLE TEST SYNTAX")
    print("-" * 40)
    
    print("""
    # pytest uses plain assert statements
    def test_addition():
        assert 2 + 2 == 4
        assert 2 + 2 != 5
    
    # No need for unittest.TestCase or self.assertEqual
    """)
    
    print("\n2. FIXTURES")
    print("-" * 40)
    
    print("""
    @pytest.fixture
    def database_connection():
        # Setup
        conn = create_connection()
        yield conn  # Provide to test
        # Teardown
        conn.close()
    
    def test_query(database_connection):
        result = database_connection.query("SELECT * FROM users")
        assert len(result) > 0
    """)
    
    print("\n3. PARAMETRIZATION")
    print("-" * 40)
    
    print("""
    @pytest.mark.parametrize("input,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
    ])
    def test_double(input, expected):
        assert input * 2 == expected
    
    # Runs the test 3 times with different values
    """)
    
    print("\n4. MARKERS")
    print("-" * 40)
    
    print("""
    @pytest.mark.slow
    def test_slow_operation():
        # Test that takes a long time
        pass
    
    @pytest.mark.skip(reason="Not implemented")
    def test_not_ready():
        pass
    
    # Run only slow tests: pytest -m slow
    # Skip slow tests: pytest -m "not slow"
    """)
    
    print("\n5. RUNNING PYTEST")
    print("-" * 40)
    
    print("""
    # Run all tests
    pytest
    
    # Run specific file
    pytest test_calculator.py
    
    # Run specific test
    pytest test_calculator.py::TestCalculator::test_add
    
    # Run with verbose output
    pytest -v
    
    # Run with print output
    pytest -s
    
    # Run with coverage
    pytest --cov=my_module
    
    # Run with failing on first error
    pytest -x
    """)


if __name__ == "__main__":
    demonstrate_pytest()
    
    # To run the actual tests, you would use:
    # pytest test_file.py -v
```

---

## 🐛 Section 3: Debugging Techniques – pdb and breakpoint()

Debugging helps you understand why code isn't working as expected. Python provides built-in debugger (pdb) and the `breakpoint()` function.

**SOLID Principle Applied: Single Responsibility** – Each debugging tool has a specific purpose.

**Design Pattern: Observer Pattern** – Debugger observes program execution.

```python
"""
DEBUGGING TECHNIQUES: PDB AND BREAKPOINT()

This section covers debugging techniques using pdb and breakpoint().

SOLID Principle: Single Responsibility
- Each debugging tool has a specific purpose

Design Pattern: Observer Pattern
- Debugger observes program execution
"""

import pdb
import sys
from typing import List, Dict, Any


# =============================================================================
# CODE WITH BUGS FOR DEBUGGING
# =============================================================================

class ShoppingCart:
    """Shopping cart with intentional bugs for debugging."""
    
    def __init__(self):
        self.items = []
        self.discount = 0
    
    def add_item(self, name: str, price: float, quantity: int = 1):
        """Add item to cart."""
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "subtotal": price * quantity
        })
    
    def calculate_subtotal(self):
        """Calculate subtotal (BUG: sum of prices, not subtotals)."""
        # BUG: Should sum item["subtotal"], not item["price"]
        return sum(item["price"] for item in self.items)
    
    def apply_discount(self, percent: float):
        """Apply discount percentage."""
        self.discount = percent / 100
    
    def calculate_total(self):
        """Calculate total with discount (BUG: applies discount incorrectly)."""
        subtotal = self.calculate_subtotal()
        # BUG: Should subtract discount, not multiply
        return subtotal * (1 - self.discount)
    
    def get_item_count(self):
        """Get total number of items (BUG: counts items, not quantity)."""
        # BUG: Should sum quantities, not count items
        return len(self.items)


class BuggyFunction:
    """Function with bugs for debugging practice."""
    
    @staticmethod
    def find_duplicates(items: List) -> List:
        """Find duplicates in list (BUG: returns all items, not just duplicates)."""
        seen = set()
        duplicates = []
        for item in items:
            if item in seen:
                duplicates.append(item)
            else:
                seen.add(item)
        return duplicates  # This actually works correctly
    
    @staticmethod
    def reverse_string(s: str) -> str:
        """Reverse string (BUG: off-by-one)."""
        # BUG: Should be range(len(s)-1, -1, -1) or s[::-1]
        result = ""
        for i in range(len(s), -1, -1):
            result += s[i]
        return result
    
    @staticmethod
    def divide_list(numbers: List[int], divisor: int) -> List[float]:
        """Divide all numbers by divisor (BUG: division by zero)."""
        # BUG: No check for divisor == 0
        return [n / divisor for n in numbers]


# =============================================================================
# DEBUGGING DEMONSTRATION
# =============================================================================

def demonstrate_breakpoint():
    """
    Demonstrates using breakpoint() for debugging.
    
    breakpoint() is Python 3.7+ and respects PYTHONBREAKPOINT environment variable.
    """
    print("\n" + "=" * 60)
    print("SECTION 3A: USING breakpoint()")
    print("=" * 60)
    
    print("\n1. breakpoint() BASICS")
    print("-" * 40)
    
    print("""
    # Insert breakpoint in code
    def buggy_function(x):
        result = x * 2
        breakpoint()  # Execution pauses here
        return result
    
    # When breakpoint is hit, you enter the debugger:
    # (Pdb) p x          - print variable x
    # (Pdb) p result     - print variable result
    # (Pdb) n            - next line
    # (Pdb) c            - continue execution
    # (Pdb) q            - quit
    """)
    
    print("\n2. DEBUGGING SHOPPING CART")
    print("-" * 40)
    
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99, 1)
    cart.add_item("Mouse", 29.99, 2)
    cart.add_item("Keyboard", 89.99, 1)
    
    print("  Cart created with items")
    print(f"  Item count (buggy): {cart.get_item_count()}")  # Should be 4, not 3
    print(f"  Subtotal (buggy): ${cart.calculate_subtotal():.2f}")  # Should be sum of subtotals
    
    # Uncomment to debug:
    # breakpoint()
    
    cart.apply_discount(10)
    print(f"  Total with 10% discount (buggy): ${cart.calculate_total():.2f}")
    
    print("\n  To debug this code, add breakpoint() and inspect variables:")
    print("    (Pdb) p cart.items")
    print("    (Pdb) p [item['subtotal'] for item in cart.items]")
    print("    (Pdb) p sum(item['price'] for item in cart.items)")
    print("    (Pdb) p sum(item['subtotal'] for item in cart.items)")


def demonstrate_pdb_commands():
    """
    Demonstrates common pdb commands.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: PDB COMMANDS")
    print("=" * 60)
    
    print("\n1. NAVIGATION COMMANDS")
    print("-" * 40)
    
    print("""
    Command    | Description
    -----------|------------------------------------------
    n (next)   | Execute next line (step over)
    s (step)   | Execute next line (step into functions)
    c (cont)   | Continue execution until next breakpoint
    r (return) | Continue until current function returns
    q (quit)   | Quit debugger
    """)
    
    print("\n2. INSPECTION COMMANDS")
    print("-" * 40)
    
    print("""
    Command     | Description
    ------------|------------------------------------------
    p expr      | Print value of expression
    pp expr     | Pretty-print value of expression
    l (list)    | Show current line and context
    w (where)   | Print stack trace
    up          | Move up stack frame
    down        | Move down stack frame
    """)
    
    print("\n3. BREAKPOINT COMMANDS")
    print("-" * 40)
    
    print("""
    Command              | Description
    ---------------------|------------------------------------------
    b (break)            | Set breakpoint at current line
    b 42                 | Set breakpoint at line 42
    b function_name      | Set breakpoint at function
    tbreak               | Temporary breakpoint
    cl (clear)           | Clear breakpoints
    disable              | Disable breakpoint
    enable               | Enable breakpoint
    """)
    
    print("\n4. CONDITIONAL BREAKPOINTS")
    print("-" * 40)
    
    print("""
    # Break when i == 10
    b 42, i == 10
    
    # Break when x > 100
    b calculate_total, subtotal > 1000
    
    # Break when exception occurs
    b, ZeroDivisionError
    """)
    
    print("\n5. POST-MORTEM DEBUGGING")
    print("-" * 40)
    
    print("""
    import pdb
    import traceback
    
    try:
        buggy_function()
    except Exception:
        traceback.print_exc()
        pdb.post_mortem()
    
    # This starts debugger at the point of exception
    """)


def demonstrate_debugging_scenarios():
    """
    Demonstrates debugging different types of bugs.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: DEBUGGING SCENARIOS")
    print("=" * 60)
    
    # SCENARIO 1: Off-by-one error
    print("\n1. OFF-BY-ONE ERROR")
    print("-" * 40)
    
    buggy = BuggyFunction()
    try:
        result = buggy.reverse_string("Python")
        print(f"  reverse_string('Python') = '{result}'")
        print("  (Expected: 'nohtyP')")
    except IndexError as e:
        print(f"  Error: {e}")
        print("  Off-by-one: range(len(s), -1, -1) goes out of bounds")
        print("  Fix: range(len(s)-1, -1, -1) or use s[::-1]")
    
    # SCENARIO 2: Division by zero
    print("\n2. DIVISION BY ZERO")
    print("-" * 40)
    
    try:
        result = buggy.divide_list([10, 20, 30], 0)
        print(f"  Result: {result}")
    except ZeroDivisionError as e:
        print(f"  Error: {e}")
        print("  Fix: Add check for divisor == 0")
    
    # SCENARIO 3: Logic error
    print("\n3. LOGIC ERROR (Wrong calculation)")
    print("-" * 40)
    
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99, 1)
    cart.add_item("Mouse", 29.99, 2)
    
    print(f"  Items in cart: {cart.items}")
    print(f"  get_item_count() returns: {cart.get_item_count()}")  # Returns 2
    print(f"  Expected: 3 (1 laptop + 2 mice)")
    print("  Bug: Counting items, not quantities")
    print("  Fix: sum(item['quantity'] for item in self.items)")
    
    print("\n  calculate_subtotal() returns: ${cart.calculate_subtotal():.2f}")
    actual_subtotal = 999.99 + 29.99 + 29.99
    print(f"  Expected: ${actual_subtotal:.2f}")
    print("  Bug: Summing price instead of subtotal")
    print("  Fix: sum(item['subtotal'] for item in self.items)")


def demonstrate_logging_for_debugging():
    """
    Demonstrates using logging instead of print for debugging.
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: LOGGING FOR DEBUGGING")
    print("=" * 60)
    
    import logging
    
    print("\n1. LOGGING LEVELS")
    print("-" * 40)
    
    print("""
    logging.DEBUG    - Detailed information for debugging
    logging.INFO     - Confirmation that things are working
    logging.WARNING  - Indication of potential problem
    logging.ERROR    - Error that prevented function execution
    logging.CRITICAL - Serious error that may stop program
    """)
    
    print("\n2. CONFIGURING LOGGING")
    print("-" * 40)
    
    print("""
    import logging
    
    # Basic configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    
    # Get logger
    logger = logging.getLogger(__name__)
    
    # Use logger
    logger.debug("Variable x = %s", x)
    logger.info("Processing started")
    logger.warning("Low disk space")
    logger.error("Failed to connect")
    """)
    
    print("\n3. LOGGING EXAMPLE")
    print("-" * 40)
    
    # Configure logging for demo
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)
    
    def process_order(order_id, items):
        logger.debug(f"Processing order {order_id} with {len(items)} items")
        
        total = 0
        for item in items:
            logger.debug(f"  Processing item: {item}")
            total += item.get("price", 0) * item.get("quantity", 0)
        
        logger.info(f"Order {order_id} total: ${total:.2f}")
        
        if total > 1000:
            logger.warning(f"High value order: ${total:.2f}")
        
        return total
    
    # Simulate processing
    order = {
        "id": 12345,
        "items": [
            {"name": "Laptop", "price": 999.99, "quantity": 1},
            {"name": "Mouse", "price": 29.99, "quantity": 2}
        ]
    }
    
    print("  Logging output:")
    process_order(order["id"], order["items"])


def demonstrate_interactive_debugging():
    """
    Demonstrates interactive debugging with a working example.
    
    This function contains a breakpoint that will activate when run interactively.
    """
    print("\n" + "=" * 60)
    print("SECTION 3E: INTERACTIVE DEBUGGING EXAMPLE")
    print("=" * 60)
    
    print("""
    To run this example interactively, uncomment the breakpoint() and run:
    python -m pdb script.py
    
    Or run normally with breakpoint():
    python script.py
    """)
    
    def calculate_average_with_debug(numbers):
        """Calculate average with debug point."""
        total = 0
        count = 0
        
        for i, n in enumerate(numbers):
            total += n
            count += 1
            # breakpoint()  # Uncomment to debug
            print(f"  After {i}: total={total}, count={count}")
        
        if count == 0:
            return 0
        return total / count
    
    numbers = [10, 20, 30, 40, 50]
    result = calculate_average_with_debug(numbers)
    print(f"  Average of {numbers} = {result}")
    
    print("\n  Debugging commands to try:")
    print("    (Pdb) p numbers")
    print("    (Pdb) p total")
    print("    (Pdb) p count")
    print("    (Pdb) n  # next line")
    print("    (Pdb) c  # continue")


if __name__ == "__main__":
    demonstrate_breakpoint()
    demonstrate_pdb_commands()
    demonstrate_debugging_scenarios()
    demonstrate_logging_for_debugging()
    demonstrate_interactive_debugging()
```

---

## 🔄 Section 4: Mocking and Patching for Tests

Mocking replaces real objects with test doubles to isolate the code being tested.

**SOLID Principles Applied:**
- Dependency Inversion: Tests depend on abstractions
- Liskov Substitution: Mocks can substitute real objects

**Design Patterns:**
- Mock Object Pattern: Simulates real objects
- Test Double Pattern: Replaces dependencies in tests

```python
"""
MOCKING AND PATCHING FOR TESTS

This section covers mocking and patching in tests.

SOLID Principles Applied:
- Dependency Inversion: Tests depend on abstractions
- Liskov Substitution: Mocks can substitute real objects

Design Patterns:
- Mock Object Pattern: Simulates real objects
- Test Double Pattern: Replaces dependencies in tests
"""

from unittest.mock import Mock, patch, MagicMock, PropertyMock
import pytest
import requests
from datetime import datetime
import json


# =============================================================================
# CODE TO TEST WITH EXTERNAL DEPENDENCIES
# =============================================================================

class WeatherService:
    """Weather service that calls external API."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.weather.com/v1"
    
    def get_temperature(self, city: str) -> float:
        """Get current temperature for a city."""
        url = f"{self.base_url}/current"
        params = {"city": city, "apikey": self.api_key}
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")
        
        data = response.json()
        return data["temperature"]
    
    def get_forecast(self, city: str, days: int) -> list:
        """Get weather forecast."""
        url = f"{self.base_url}/forecast"
        params = {"city": city, "days": days, "apikey": self.api_key}
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")
        
        data = response.json()
        return data["forecast"]


class EmailService:
    """Email service that sends emails."""
    
    def __init__(self, smtp_server: str):
        self.smtp_server = smtp_server
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send an email."""
        # In reality, would use SMTP
        print(f"Sending email to {to}: {subject}")
        return True


class UserService:
    """User service with dependencies."""
    
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
        self.users = {}
    
    def register_user(self, email: str, name: str) -> int:
        """Register a new user."""
        user_id = len(self.users) + 1
        self.users[user_id] = {"email": email, "name": name, "active": True}
        
        # Send welcome email
        self.email_service.send_email(
            to=email,
            subject="Welcome!",
            body=f"Hello {name}, welcome to our platform!"
        )
        
        return user_id
    
    def deactivate_user(self, user_id: int) -> bool:
        """Deactivate a user."""
        if user_id not in self.users:
            return False
        
        self.users[user_id]["active"] = False
        
        # Send notification
        user = self.users[user_id]
        self.email_service.send_email(
            to=user["email"],
            subject="Account Deactivated",
            body=f"Your account has been deactivated."
        )
        
        return True


class Database:
    """Database class to mock."""
    
    def query(self, sql: str) -> list:
        """Execute query."""
        # In reality, would connect to database
        return []
    
    def insert(self, table: str, data: dict) -> int:
        """Insert record."""
        return 1


# =============================================================================
# TESTS WITH MOCKS
# =============================================================================

class TestWeatherService:
    """Test WeatherService with mocked requests."""
    
    def test_get_temperature_success(self):
        """Test successful temperature retrieval."""
        # Create mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"temperature": 22.5}
        
        # Patch requests.get
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock_response
            
            service = WeatherService("test_api_key")
            temp = service.get_temperature("London")
            
            assert temp == 22.5
            mock_get.assert_called_once()
    
    def test_get_temperature_api_error(self):
        """Test API error handling."""
        mock_response = Mock()
        mock_response.status_code = 500
        
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock_response
            
            service = WeatherService("test_api_key")
            
            with pytest.raises(Exception, match="API error: 500"):
                service.get_temperature("London")
    
    def test_get_forecast(self):
        """Test forecast retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "forecast": [{"day": "Monday", "temp": 20}, {"day": "Tuesday", "temp": 22}]
        }
        
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock_response
            
            service = WeatherService("test_api_key")
            forecast = service.get_forecast("Paris", 2)
            
            assert len(forecast) == 2
            assert forecast[0]["day"] == "Monday"


class TestUserService:
    """Test UserService with mocked EmailService."""
    
    def test_register_user_sends_email(self):
        """Test user registration sends welcome email."""
        # Create mock email service
        mock_email = Mock(spec=EmailService)
        
        service = UserService(mock_email)
        user_id = service.register_user("test@example.com", "Test User")
        
        assert user_id == 1
        mock_email.send_email.assert_called_once()
        call_args = mock_email.send_email.call_args[1]
        assert call_args["to"] == "test@example.com"
        assert "Welcome" in call_args["subject"]
    
    def test_deactivate_user_sends_email(self):
        """Test user deactivation sends notification."""
        mock_email = Mock(spec=EmailService)
        
        service = UserService(mock_email)
        service.register_user("test@example.com", "Test User")
        mock_email.reset_mock()
        
        result = service.deactivate_user(1)
        
        assert result is True
        mock_email.send_email.assert_called_once()
    
    def test_deactivate_nonexistent_user(self):
        """Test deactivating non-existent user."""
        mock_email = Mock(spec=EmailService)
        
        service = UserService(mock_email)
        result = service.deactivate_user(999)
        
        assert result is False
        mock_email.send_email.assert_not_called()


class TestMockingPatterns:
    """Demonstrate different mocking patterns."""
    
    def test_mock_return_value(self):
        """Test setting return value."""
        mock_obj = Mock()
        mock_obj.calculate.return_value = 42
        
        assert mock_obj.calculate() == 42
    
    def test_mock_side_effect(self):
        """Test setting side effects."""
        mock_obj = Mock()
        mock_obj.process.side_effect = [1, 2, 3, Exception("Error")]
        
        assert mock_obj.process() == 1
        assert mock_obj.process() == 2
        assert mock_obj.process() == 3
        
        with pytest.raises(Exception, match="Error"):
            mock_obj.process()
    
    def test_mock_side_effect_function(self):
        """Test side effect as function."""
        def custom_effect(x):
            return x * 2
        
        mock_obj = Mock()
        mock_obj.transform.side_effect = custom_effect
        
        assert mock_obj.transform(5) == 10
        assert mock_obj.transform(10) == 20
    
    def test_mock_attributes(self):
        """Test mocking attributes."""
        mock_obj = Mock()
        mock_obj.name = "Test Object"
        mock_obj.value = 100
        
        assert mock_obj.name == "Test Object"
        assert mock_obj.value == 100
    
    def test_property_mock(self):
        """Test mocking properties."""
        mock_obj = Mock()
        type(mock_obj).temperature = PropertyMock(return_value=25.5)
        
        assert mock_obj.temperature == 25.5
    
    def test_assert_called_with(self):
        """Test asserting call arguments."""
        mock_func = Mock()
        mock_func(1, 2, key="value")
        
        mock_func.assert_called_once_with(1, 2, key="value")
    
    def test_assert_call_count(self):
        """Test asserting call count."""
        mock_func = Mock()
        mock_func()
        mock_func()
        
        assert mock_func.call_count == 2
        mock_func.assert_called()
    
    def test_mock_patch_multiple(self):
        """Test patching multiple objects."""
        with patch('module.function1') as mock1, patch('module.function2') as mock2:
            mock1.return_value = 10
            mock2.return_value = 20
            
            # Use mocked functions
            pass
    
    def test_patch_object(self):
        """Test patching object methods."""
        service = WeatherService("key")
        
        with patch.object(service, 'get_temperature', return_value=15.0):
            temp = service.get_temperature("Berlin")
            assert temp == 15.0
    
    @patch('module.ClassName')
    def test_patch_decorator(self, MockClass):
        """Test patching with decorator."""
        instance = MockClass.return_value
        instance.method.return_value = "mocked"
        
        # Test code here
        pass


class TestPatchContextManager:
    """Test patching as context manager."""
    
    def test_patch_context(self):
        """Test using patch as context manager."""
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, 0)
            
            now = datetime.now()
            assert now.year == 2024
            assert now.month == 1
    
    def test_patch_with_autospec(self):
        """Test patching with autospec."""
        mock_email = Mock(spec=EmailService)
        
        # This will fail if method doesn't exist
        # mock_email.nonexistent_method()  # Would raise AttributeError


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_mocking():
    """
    Demonstrate mocking concepts.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: MOCKING AND PATCHING")
    print("=" * 60)
    
    print("\n1. WHY MOCK?")
    print("-" * 40)
    
    print("""
    Benefits of mocking:
    ✓ Isolate code being tested
    ✓ Avoid external dependencies (API, database, network)
    ✓ Control test environment
    ✓ Test error conditions
    ✓ Speed up tests
    """)
    
    print("\n2. BASIC MOCK USAGE")
    print("-" * 40)
    
    mock_obj = Mock()
    mock_obj.method.return_value = 42
    print(f"  mock_obj.method() = {mock_obj.method()}")
    
    print("\n3. MOCKING REQUESTS")
    print("-" * 40)
    
    print("""
    # Mock HTTP requests
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        response = requests.get("https://api.example.com")
        assert response.json() == {"data": "test"}
    """)
    
    print("\n4. MOCKING CLASSES")
    print("-" * 40)
    
    print("""
    # Mock entire class
    with patch('my_module.Database') as MockDatabase:
        mock_db = MockDatabase.return_value
        mock_db.query.return_value = [{"id": 1, "name": "Test"}]
        
        service = UserService(mock_db)
        users = service.get_users()
        assert len(users) == 1
    """)
    
    print("\n5. MOCKING PROPERTIES")
    print("-" * 40)
    
    print("""
    # Mock property
    mock_obj = Mock()
    type(mock_obj).temperature = PropertyMock(return_value=25.5)
    assert mock_obj.temperature == 25.5
    """)
    
    print("\n6. ASSERTING CALLS")
    print("-" * 40)
    
    mock_func = Mock()
    mock_func(1, 2, 3)
    mock_func.assert_called_once_with(1, 2, 3)
    print("  Assertions passed!")


if __name__ == "__main__":
    demonstrate_mocking()
    
    # To run the actual tests with pytest:
    # pytest test_file.py -v
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **unittest Framework** – Python's built-in testing framework. TestCase class, setUp/tearDown, assertions (assertEqual, assertRaises, etc.). Test discovery with `python -m unittest discover`.

- **pytest Framework** – Modern, more concise testing. Plain assert statements. Fixtures for setup/teardown. Parametrization for multiple test cases. Markers for categorizing tests.

- **Common Assertions** – Equality, truthiness, exceptions, containment, type checking. pytest gives better error messages.

- **Fixtures** – Provide test context and data. Scope options: function, class, module, session. Yield for teardown.

- **Parametrization** – `@pytest.mark.parametrize` runs same test with different inputs. Reduces code duplication.

- **Debugging with pdb** – `breakpoint()` or `pdb.set_trace()`. Commands: n (next), s (step), c (continue), p (print), l (list), q (quit).

- **Logging for Debugging** – Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Better than print statements for production debugging.

- **Mocking** – Replace real objects with test doubles. `Mock`, `patch`, `MagicMock`. Control return values and side effects.

- **Patching** – `patch` as decorator, context manager, or function. `patch.object` for specific methods.

- **SOLID Principles Applied** – Single Responsibility (each test tests one behavior), Dependency Inversion (tests depend on abstractions via mocks), Liskov Substitution (mocks substitute real objects), Open/Closed (new tests can be added without changing existing ones).

- **Design Patterns Used** – Command Pattern (test cases), Fixture Pattern (test setup), Mock Object Pattern (test doubles), Observer Pattern (debugger observing execution).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Memory Management & Garbage Collection

- **📚 Series F Catalog:** Advanced Python Engineering – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Type Hints & MyPy (Series F, Story 6)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 5 | 0 | 100% |
| Series F | 6 | 5 | 1 | 83% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **39** | **13** | **75%** |

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
21. Series C, Story 3: The 2026 Python Metromap: Dictionaries – Key-Value Power
22. Series C, Story 4: The 2026 Python Metromap: Sets – Unique & Fast
23. Series C, Story 5: The 2026 Python Metromap: Comprehensions – One-Line Power
24. Series D, Story 1: The 2026 Python Metromap: Classes & Objects – Blueprints & Instances
25. Series D, Story 2: The 2026 Python Metromap: Constructor – Building Objects
26. Series D, Story 3: The 2026 Python Metromap: Inheritance – Reusing Parent Classes
27. Series D, Story 4: The 2026 Python Metromap: Polymorphism – One Interface, Many Forms
28. Series D, Story 5: The 2026 Python Metromap: Encapsulation – Protecting Data
29. Series D, Story 6: The 2026 Python Metromap: Abstraction – Hiding Complexity
30. Series E, Story 1: The 2026 Python Metromap: File I/O – Reading & Writing
31. Series E, Story 2: The 2026 Python Metromap: CSV & JSON Processing – Structured Data
32. Series E, Story 3: The 2026 Python Metromap: Exception Handling – Graceful Failures
33. Series E, Story 4: The 2026 Python Metromap: Context Managers – The with Statement
34. Series E, Story 5: The 2026 Python Metromap: Working with Paths & Directories
35. Series F, Story 1: The 2026 Python Metromap: Decorators – Wrapping Functions
36. Series F, Story 2: The 2026 Python Metromap: Generators – Memory-Efficient Loops
37. Series F, Story 3: The 2026 Python Metromap: Iterators – Custom Looping
38. Series F, Story 4: The 2026 Python Metromap: Memory Management & Garbage Collection
39. Series F, Story 5: The 2026 Python Metromap: Testing & Debugging – pytest and unittest

**Next Story:** Series F, Story 6: The 2026 Python Metromap: Type Hints & MyPy

---

## 📝 Your Invitation

You've mastered testing and debugging. Now build something with what you've learned:

1. **Write unit tests for a project** – Take any previous project and write comprehensive tests using pytest.

2. **Set up CI/CD** – Configure GitHub Actions or GitLab CI to run tests automatically on every commit.

3. **Add test coverage reporting** – Use pytest-cov to measure coverage and aim for >80%.

4. **Practice debugging** – Introduce bugs intentionally and use pdb to find and fix them.

5. **Mock external APIs** – Write tests for code that calls external services using mock and patch.

**You've mastered testing and debugging. Next stop: Type Hints & MyPy!**

---

*Found this helpful? Clap, comment, and share what you tested. Next stop: Type Hints & MyPy!* 🚇