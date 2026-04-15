# The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking

## Series F: Advanced Python Engineering | Story 6 of 6

![The 2026 Python Metromap/images/Type Hints and MyPy – Static Type Checking](images/Type Hints and MyPy – Static Type Checking.png)

## 📖 Introduction

**Welcome to the sixth and final stop on the Advanced Python Engineering Line.**

You've mastered decorators, generators, iterators, memory management, and testing. You can write efficient, reliable code and verify its correctness with tests. But there's one more practice that separates good Python code from great Python code: type hints.

Python is dynamically typed—variables can hold any type, and types are checked at runtime. This flexibility is powerful but can lead to bugs that only appear when specific code paths execute. Type hints (PEP 484) allow you to annotate your code with type information, and tools like MyPy can check these annotations statically, catching type errors before runtime.

This story—**The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking**—is your guide to type hints in Python. We'll learn the syntax for type annotations: variables, function parameters, return values. We'll explore complex types: `List`, `Dict`, `Optional`, `Union`, `Tuple`, `Any`. We'll use `Protocol` for duck typing, `TypedDict` for dictionaries, and `Final` for constants. We'll integrate MyPy into our development workflow. And we'll build a complete type-annotated application that catches bugs at development time.

**Let's annotate our types.**

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

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports.

- 📝 **The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking** – Large team codebase annotations; pre-runtime bug catching; automatic documentation. **⬅️ YOU ARE HERE**

### Series G: Data Science & Visualization (5 Stories) – Next Station

- 🔢 **The 2026 Python Metromap: NumPy – Numerical Computing** – Processing millions of sensor readings; matrix operations; statistical aggregates. 🔜 *Up Next*

- 🐼 **The 2026 Python Metromap: Pandas – Data Wrangling** – Multi-year sales analysis; CSV cleaning; regional and product aggregation.

- 📈 **The 2026 Python Metromap: Matplotlib – Basic Plotting** – Stock price line charts; sales bar charts; market share pie charts.

- 🎨 **The 2026 Python Metromap: Seaborn – Statistical Visualization** – Customer segmentation heatmaps; age distribution plots; feature correlation pair plots.

- 📊 **The 2026 Python Metromap: Real-World EDA Project** – End-to-end exploratory data analysis on COVID-19 data, housing prices, or e-commerce sales.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📝 Section 1: Type Hint Basics – Annotating Variables and Functions

Type hints allow you to specify the expected types of variables, function parameters, and return values.

**SOLID Principle Applied: Interface Segregation** – Type hints document the expected interface.

**Design Pattern: Specification Pattern** – Type hints specify what types are acceptable.

```python
"""
TYPE HINT BASICS: ANNOTATING VARIABLES AND FUNCTIONS

This section covers the fundamentals of type hints.

SOLID Principle: Interface Segregation
- Type hints document the expected interface

Design Pattern: Specification Pattern
- Type hints specify what types are acceptable
"""

from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable
from datetime import datetime, date


def demonstrate_basic_type_hints():
    """
    Demonstrates basic type hint syntax.
    
    Type hints are optional but improve code readability and enable static checking.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC TYPE HINTS")
    print("=" * 60)
    
    # VARIABLE TYPE HINTS
    print("\n1. VARIABLE TYPE HINTS")
    print("-" * 40)
    
    name: str = "Alice"
    age: int = 28
    price: float = 29.99
    is_active: bool = True
    items: List[str] = ["apple", "banana", "cherry"]
    scores: Dict[str, int] = {"Alice": 95, "Bob": 87}
    
    print(f"  name: {name} ({type(name).__name__})")
    print(f"  age: {age} ({type(age).__name__})")
    print(f"  price: {price} ({type(price).__name__})")
    print(f"  is_active: {is_active} ({type(is_active).__name__})")
    print(f"  items: {items} ({type(items).__name__})")
    print(f"  scores: {scores} ({type(scores).__name__})")
    
    # FUNCTION TYPE HINTS
    print("\n2. FUNCTION TYPE HINTS")
    print("-" * 40)
    
    def greet(name: str) -> str:
        """Greet a person."""
        return f"Hello, {name}!"
    
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b
    
    def process_items(items: List[str], prefix: str = "") -> List[str]:
        """Process list of strings."""
        return [f"{prefix}{item}" for item in items]
    
    result1: str = greet("Alice")
    result2: int = add(5, 3)
    result3: List[str] = process_items(["a", "b", "c"], "item_")
    
    print(f"  greet('Alice') -> {result1}")
    print(f"  add(5, 3) -> {result2}")
    print(f"  process_items -> {result3}")
    
    # MULTIPLE RETURN VALUES
    print("\n3. MULTIPLE RETURN VALUES")
    print("-" * 40)
    
    def get_min_max(numbers: List[int]) -> Tuple[int, int]:
        """Return min and max as tuple."""
        return min(numbers), max(numbers)
    
    min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2])
    print(f"  get_min_max([3,1,4,1,5,9,2]) -> ({min_val}, {max_val})")


def demonstrate_complex_types():
    """
    Demonstrates complex type hints: List, Dict, Tuple, Set, Optional, Union.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: COMPLEX TYPE HINTS")
    print("=" * 60)
    
    # LIST TYPES
    print("\n1. LIST TYPES")
    print("-" * 40)
    
    def process_strings(items: List[str]) -> List[int]:
        """Process list of strings to list of lengths."""
        return [len(item) for item in items]
    
    def get_first_element(items: List[int]) -> int:
        """Get first element of list."""
        return items[0] if items else 0
    
    strings: List[str] = ["hello", "world", "python"]
    lengths: List[int] = process_strings(strings)
    first: int = get_first_element(lengths)
    
    print(f"  strings: {strings}")
    print(f"  lengths: {lengths}")
    print(f"  first element: {first}")
    
    # DICTIONARY TYPES
    print("\n2. DICTIONARY TYPES")
    print("-" * 40)
    
    def get_user_info(user_id: int) -> Dict[str, Any]:
        """Get user information as dictionary."""
        return {
            "id": user_id,
            "name": f"User {user_id}",
            "email": f"user{user_id}@example.com"
        }
    
    def update_scores(scores: Dict[str, int], name: str, score: int) -> Dict[str, int]:
        """Update scores dictionary."""
        scores[name] = score
        return scores
    
    user: Dict[str, Any] = get_user_info(42)
    scores: Dict[str, int] = {"Alice": 95, "Bob": 87}
    updated: Dict[str, int] = update_scores(scores, "Charlie", 92)
    
    print(f"  user: {user}")
    print(f"  scores: {updated}")
    
    # TUPLE TYPES
    print("\n3. TUPLE TYPES")
    print("-" * 40)
    
    def get_coordinates() -> Tuple[float, float]:
        """Return (x, y) coordinates."""
        return (10.5, 20.3)
    
    def get_user_record() -> Tuple[int, str, str, bool]:
        """Return (id, name, email, active)."""
        return (1, "Alice", "alice@example.com", True)
    
    x, y = get_coordinates()
    user_id, name, email, active = get_user_record()
    
    print(f"  coordinates: ({x}, {y})")
    print(f"  user record: ({user_id}, {name}, {email}, {active})")
    
    # SET TYPES
    print("\n4. SET TYPES")
    print("-" * 40)
    
    def get_unique_items(items: List[str]) -> Set[str]:
        """Get unique items as set."""
        return set(items)
    
    def find_common(set1: Set[int], set2: Set[int]) -> Set[int]:
        """Find common elements between sets."""
        return set1 & set2
    
    unique: Set[str] = get_unique_items(["a", "b", "a", "c", "b", "d"])
    common: Set[int] = find_common({1, 2, 3, 4}, {3, 4, 5, 6})
    
    print(f"  unique items: {unique}")
    print(f"  common elements: {common}")
    
    # OPTIONAL TYPES (can be None)
    print("\n5. OPTIONAL TYPES")
    print("-" * 40)
    
    def find_user(user_id: int, users: Dict[int, str]) -> Optional[str]:
        """Find user by ID, return None if not found."""
        return users.get(user_id)
    
    def parse_date(date_str: str) -> Optional[date]:
        """Parse date string, return None if invalid."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return None
    
    users: Dict[int, str] = {1: "Alice", 2: "Bob"}
    user: Optional[str] = find_user(1, users)
    not_found: Optional[str] = find_user(99, users)
    parsed_date: Optional[date] = parse_date("2024-01-15")
    invalid_date: Optional[date] = parse_date("invalid")
    
    print(f"  find_user(1) -> {user}")
    print(f"  find_user(99) -> {not_found}")
    print(f"  parse_date('2024-01-15') -> {parsed_date}")
    print(f"  parse_date('invalid') -> {invalid_date}")
    
    # UNION TYPES (multiple possible types)
    print("\n6. UNION TYPES")
    print("-" * 40)
    
    def process_value(value: Union[int, str, float]) -> str:
        """Process value of multiple types."""
        if isinstance(value, int):
            return f"Integer: {value}"
        elif isinstance(value, str):
            return f"String: {value.upper()}"
        else:
            return f"Float: {value:.2f}"
    
    print(f"  process_value(42) -> {process_value(42)}")
    print(f"  process_value('hello') -> {process_value('hello')}")
    print(f"  process_value(3.14) -> {process_value(3.14)}")
    
    # ANY TYPE (opt-out of type checking)
    print("\n7. ANY TYPE (use sparingly)")
    print("-" * 40)
    
    def flexible_function(data: Any) -> Any:
        """Accepts and returns any type (bypasses type checking)."""
        return data
    
    result: Any = flexible_function(42)
    result2: Any = flexible_function("string")
    print("  Any type bypasses type checking - use only when necessary")


def demonstrate_callable_type_hints():
    """
    Demonstrates Callable type hints for functions and callbacks.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: CALLABLE TYPE HINTS")
    print("=" * 60)
    
    from typing import Callable
    
    # FUNCTION THAT TAKES A CALLBACK
    print("\n1. CALLBACK FUNCTIONS")
    print("-" * 40)
    
    def process_data(data: List[int], processor: Callable[[int], int]) -> List[int]:
        """Apply processor function to each element."""
        return [processor(x) for x in data]
    
    def double(x: int) -> int:
        return x * 2
    
    def square(x: int) -> int:
        return x ** 2
    
    numbers: List[int] = [1, 2, 3, 4, 5]
    doubled: List[int] = process_data(numbers, double)
    squared: List[int] = process_data(numbers, square)
    
    print(f"  Original: {numbers}")
    print(f"  Doubled: {doubled}")
    print(f"  Squared: {squared}")
    
    # FUNCTION THAT RETURNS A FUNCTION
    print("\n2. FUNCTION RETURNING FUNCTION")
    print("-" * 40)
    
    def make_multiplier(factor: int) -> Callable[[int], int]:
        """Return a function that multiplies by factor."""
        def multiplier(x: int) -> int:
            return x * factor
        return multiplier
    
    times_3: Callable[[int], int] = make_multiplier(3)
    result: int = times_3(5)
    
    print(f"  times_3(5) = {result}")
    
    # COMPLEX CALLABLE SIGNATURE
    print("\n3. COMPLEX CALLABLE SIGNATURE")
    print("-" * 40)
    
    def apply_operation(
        a: int, 
        b: int, 
        operation: Callable[[int, int], int]
    ) -> int:
        """Apply binary operation to two numbers."""
        return operation(a, b)
    
    add: Callable[[int, int], int] = lambda x, y: x + y
    multiply: Callable[[int, int], int] = lambda x, y: x * y
    
    print(f"  apply_operation(5, 3, add) = {apply_operation(5, 3, add)}")
    print(f"  apply_operation(5, 3, multiply) = {apply_operation(5, 3, multiply)}")


def demonstrate_type_hints_with_classes():
    """
    Demonstrates type hints in classes and methods.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: TYPE HINTS IN CLASSES")
    print("=" * 60)
    
    from typing import ClassVar, Optional, List
    
    class BankAccount:
        """Bank account with type hints."""
        
        # Class variable
        bank_name: ClassVar[str] = "Metromap Bank"
        interest_rate: ClassVar[float] = 0.02
        
        # Instance variables with type hints
        def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
            self.account_holder: str = account_holder
            self.balance: float = initial_balance
            self.transactions: List[float] = []
            self.is_active: bool = True
        
        def deposit(self, amount: float) -> float:
            """Deposit money."""
            if amount <= 0:
                raise ValueError("Amount must be positive")
            self.balance += amount
            self.transactions.append(amount)
            return self.balance
        
        def withdraw(self, amount: float) -> float:
            """Withdraw money."""
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            self.transactions.append(-amount)
            return self.balance
        
        def get_balance(self) -> float:
            """Get current balance."""
            return self.balance
        
        def get_transaction_count(self) -> int:
            """Get number of transactions."""
            return len(self.transactions)
        
        @classmethod
        def get_bank_info(cls) -> str:
            """Get bank information."""
            return f"{cls.bank_name} (interest: {cls.interest_rate * 100}%)"
        
        @staticmethod
        def validate_amount(amount: float) -> bool:
            """Validate transaction amount."""
            return amount > 0
    
    # Create account
    account: BankAccount = BankAccount("Alice Chen", 1000.00)
    account.deposit(500.00)
    account.withdraw(200.00)
    
    print(f"  Account holder: {account.account_holder}")
    print(f"  Balance: ${account.get_balance():.2f}")
    print(f"  Transactions: {account.get_transaction_count()}")
    print(f"  Bank info: {BankAccount.get_bank_info()}")
    print(f"  Amount valid: {BankAccount.validate_amount(100)}")


if __name__ == "__main__":
    demonstrate_basic_type_hints()
    demonstrate_complex_types()
    demonstrate_callable_type_hints()
    demonstrate_type_hints_with_classes()
```

---

## 🔧 Section 2: Advanced Type Hints – Protocols, TypedDict, and Final

Advanced type hints provide more precise type specifications for complex scenarios.

**SOLID Principle Applied: Liskov Substitution** – Protocols define structural subtyping.

**Design Pattern: Protocol Pattern** – Defines interfaces without inheritance.

```python
"""
ADVANCED TYPE HINTS: PROTOCOLS, TYPEDDICT, AND FINAL

This section covers advanced type hint features.

SOLID Principle: Liskov Substitution
- Protocols define structural subtyping

Design Pattern: Protocol Pattern
- Defines interfaces without inheritance
"""

from typing import Protocol, TypedDict, Final, Literal, TypeVar, Generic
from typing import List, Dict, Optional, Union, Any
from dataclasses import dataclass


def demonstrate_protocols():
    """
    Demonstrates Protocols for structural subtyping (duck typing).
    
    Protocols define required methods without inheritance.
    """
    print("=" * 60)
    print("SECTION 2A: PROTOCOLS (Structural Subtyping)")
    print("=" * 60)
    
    from typing import Protocol
    
    class Drawable(Protocol):
        """Protocol for drawable objects."""
        
        def draw(self) -> str:
            """Draw the object."""
            ...
        
        def get_position(self) -> tuple:
            """Get position as (x, y)."""
            ...
    
    class Circle:
        """Circle class (implements Drawable protocol implicitly)."""
        
        def __init__(self, x: float, y: float, radius: float):
            self.x = x
            self.y = y
            self.radius = radius
        
        def draw(self) -> str:
            return f"Drawing circle at ({self.x}, {self.y}) with radius {self.radius}"
        
        def get_position(self) -> tuple:
            return (self.x, self.y)
    
    class Rectangle:
        """Rectangle class (implements Drawable protocol implicitly)."""
        
        def __init__(self, x: float, y: float, width: float, height: float):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        
        def draw(self) -> str:
            return f"Drawing rectangle at ({self.x}, {self.y}) with size {self.width}x{self.height}"
        
        def get_position(self) -> tuple:
            return (self.x, self.y)
    
    # Function that accepts any Drawable (structural subtyping)
    def render(drawable: Drawable) -> None:
        """Render any drawable object."""
        print(f"  {drawable.draw()}")
        print(f"  Position: {drawable.get_position()}")
    
    circle = Circle(10, 20, 5)
    rectangle = Rectangle(30, 40, 15, 10)
    
    print("\n1. PROTOCOL IN ACTION")
    print("-" * 40)
    
    print("  Rendering circle:")
    render(circle)
    
    print("\n  Rendering rectangle:")
    render(rectangle)
    
    # PROTOCOL WITH MULTIPLE METHODS
    print("\n2. PROTOCOL WITH MULTIPLE METHODS")
    print("-" * 40)
    
    class Comparable(Protocol):
        """Protocol for comparable objects."""
        
        def __lt__(self, other: Any) -> bool:
            ...
        
        def __eq__(self, other: Any) -> bool:
            ...
    
    def find_min(items: List[Comparable]) -> Comparable:
        """Find minimum item (works with any comparable type)."""
        if not items:
            raise ValueError("Empty list")
        min_item = items[0]
        for item in items[1:]:
            if item < min_item:
                min_item = item
        return min_item
    
    # Works with ints (they implement __lt__ and __eq__)
    min_int: int = find_min([5, 2, 8, 1, 9])  # type: ignore
    print(f"  Minimum of [5,2,8,1,9] = {min_int}")
    
    # Works with strings
    min_str: str = find_min(["banana", "apple", "cherry"])  # type: ignore
    print(f"  Minimum of ['banana','apple','cherry'] = {min_str}")


def demonstrate_typed_dict():
    """
    Demonstrates TypedDict for structured dictionaries.
    
    TypedDict specifies the expected keys and value types for dictionaries.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: TYPEDDICT (Structured Dictionaries)")
    print("=" * 60)
    
    from typing import TypedDict
    
    class UserDict(TypedDict):
        """User dictionary structure."""
        id: int
        name: str
        email: str
        age: int
        is_active: bool
    
    class ProductDict(TypedDict):
        """Product dictionary structure."""
        sku: str
        name: str
        price: float
        in_stock: bool
        tags: List[str]
    
    # Create properly typed dictionaries
    user: UserDict = {
        "id": 1,
        "name": "Alice Chen",
        "email": "alice@example.com",
        "age": 28,
        "is_active": True
    }
    
    product: ProductDict = {
        "sku": "TECH-001",
        "name": "Laptop",
        "price": 999.99,
        "in_stock": True,
        "tags": ["electronics", "portable"]
    }
    
    print("\n1. TYPEDDICT EXAMPLES")
    print("-" * 40)
    
    def process_user(user: UserDict) -> str:
        """Process user dictionary."""
        return f"User {user['name']} ({user['email']}) is {'active' if user['is_active'] else 'inactive'}"
    
    def calculate_total(products: List[ProductDict]) -> float:
        """Calculate total price of products."""
        return sum(p["price"] for p in products)
    
    print(f"  User: {process_user(user)}")
    print(f"  Product: {product['name']} - ${product['price']}")
    
    # TOTAL (Optional) and NOT_REQUIRED
    print("\n2. OPTIONAL FIELDS IN TYPEDDICT")
    print("-" * 40)
    
    from typing import TypedDict, NotRequired
    
    class ConfigDict(TypedDict, total=False):
        """Configuration with optional fields."""
        host: str
        port: int
        debug: bool
        log_level: NotRequired[str]  # Python 3.11+
    
    # All fields are optional
    config1: ConfigDict = {}
    config2: ConfigDict = {"host": "localhost"}
    config3: ConfigDict = {"host": "localhost", "port": 8080, "debug": True}
    
    print(f"  Config 1: {config1}")
    print(f"  Config 2: {config2}")
    print(f"  Config 3: {config3}")


def demonstrate_final_and_literal():
    """
    Demonstrates Final for constants and Literal for specific values.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: FINAL AND LITERAL TYPES")
    print("=" * 60)
    
    from typing import Final, Literal
    
    # FINAL CONSTANTS (cannot be reassigned)
    print("\n1. FINAL (Constants)")
    print("-" * 40)
    
    MAX_RETRIES: Final[int] = 3
    DEFAULT_TIMEOUT: Final[float] = 30.0
    APP_NAME: Final[str] = "Metromap"
    
    print(f"  MAX_RETRIES = {MAX_RETRIES}")
    print(f"  DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")
    print(f"  APP_NAME = {APP_NAME}")
    
    # LITERAL TYPES (specific literal values)
    print("\n2. LITERAL (Specific Values)")
    print("-" * 40)
    
    from typing import Literal
    
    def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
        """Set log level to specific values only."""
        print(f"  Log level set to {level}")
    
    def http_status(code: Literal[200, 201, 400, 401, 404, 500]) -> str:
        """Get HTTP status message."""
        messages = {
            200: "OK",
            201: "Created",
            400: "Bad Request",
            401: "Unauthorized",
            404: "Not Found",
            500: "Internal Server Error"
        }
        return messages.get(code, "Unknown")
    
    set_log_level("INFO")
    # set_log_level("DEBUGGING")  # Type error - not allowed
    
    print(f"  HTTP 200: {http_status(200)}")
    print(f"  HTTP 404: {http_status(404)}")
    
    # LITERAL WITH MULTIPLE TYPES
    print("\n3. LITERAL WITH MULTIPLE TYPES")
    print("-" * 40)
    
    def parse_value(value: Literal["yes", "no", 1, 0, True, False]) -> bool:
        """Parse various literal values to boolean."""
        if value in ("yes", 1, True):
            return True
        return False
    
    print(f"  parse_value('yes') = {parse_value('yes')}")
    print(f"  parse_value(1) = {parse_value(1)}")
    print(f"  parse_value(True) = {parse_value(True)}")
    print(f"  parse_value('no') = {parse_value('no')}")


def demonstrate_generics():
    """
    Demonstrates Generics for type-parameterized classes and functions.
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: GENERICS (Type Parameters)")
    print("=" * 60)
    
    from typing import TypeVar, Generic
    
    T = TypeVar('T')
    K = TypeVar('K')
    V = TypeVar('V')
    
    # GENERIC CLASS
    print("\n1. GENERIC CLASS (Stack)")
    print("-" * 40)
    
    class Stack(Generic[T]):
        """Generic stack implementation."""
        
        def __init__(self) -> None:
            self._items: List[T] = []
        
        def push(self, item: T) -> None:
            self._items.append(item)
        
        def pop(self) -> T:
            if not self._items:
                raise IndexError("Stack is empty")
            return self._items.pop()
        
        def peek(self) -> T:
            if not self._items:
                raise IndexError("Stack is empty")
            return self._items[-1]
        
        def is_empty(self) -> bool:
            return len(self._items) == 0
        
        def __len__(self) -> int:
            return len(self._items)
    
    # Stack of integers
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"  Integer stack pop: {int_stack.pop()}")
    print(f"  Integer stack peek: {int_stack.peek()}")
    
    # Stack of strings
    str_stack: Stack[str] = Stack()
    str_stack.push("a")
    str_stack.push("b")
    str_stack.push("c")
    print(f"  String stack pop: {str_stack.pop()}")
    print(f"  String stack peek: {str_stack.peek()}")
    
    # GENERIC FUNCTION
    print("\n2. GENERIC FUNCTION")
    print("-" * 40)
    
    def first_element(items: List[T]) -> T:
        """Return first element of list."""
        if not items:
            raise ValueError("Empty list")
        return items[0]
    
    numbers: List[int] = [1, 2, 3]
    words: List[str] = ["a", "b", "c"]
    
    print(f"  first_element([1,2,3]) = {first_element(numbers)}")
    print(f"  first_element(['a','b','c']) = {first_element(words)}")
    
    # GENERIC WITH CONSTRAINTS
    print("\n3. GENERIC WITH CONSTRAINTS")
    print("-" * 40)
    
    Number = TypeVar('Number', int, float)
    
    def add_numbers(a: Number, b: Number) -> Number:
        """Add two numbers (int or float)."""
        return a + b  # type: ignore
    
    print(f"  add_numbers(5, 3) = {add_numbers(5, 3)}")
    print(f"  add_numbers(5.5, 3.2) = {add_numbers(5.5, 3.2)}")
    
    # GENERIC DICTIONARY
    print("\n4. GENERIC DICTIONARY")
    print("-" * 40)
    
    class BiMap(Generic[K, V]):
        """Bidirectional map."""
        
        def __init__(self) -> None:
            self._forward: Dict[K, V] = {}
            self._backward: Dict[V, K] = {}
        
        def put(self, key: K, value: V) -> None:
            self._forward[key] = value
            self._backward[value] = key
        
        def get_by_key(self, key: K) -> Optional[V]:
            return self._forward.get(key)
        
        def get_by_value(self, value: V) -> Optional[K]:
            return self._backward.get(value)
    
    bimap: BiMap[str, int] = BiMap()
    bimap.put("one", 1)
    bimap.put("two", 2)
    
    print(f"  get_by_key('one') = {bimap.get_by_key('one')}")
    print(f"  get_by_value(2) = {bimap.get_by_value(2)}")


if __name__ == "__main__":
    demonstrate_protocols()
    demonstrate_typed_dict()
    demonstrate_final_and_literal()
    demonstrate_generics()
```

---

## 🔍 Section 3: MyPy – Static Type Checking

MyPy checks your type hints statically, catching type errors before runtime.

**SOLID Principle Applied: Dependency Inversion** – MyPy checks that code adheres to type specifications.

**Design Pattern: Interpreter Pattern** – MyPy interprets type hints to validate code.

```python
"""
MYPY: STATIC TYPE CHECKING

This section covers using MyPy for static type checking.

SOLID Principle: Dependency Inversion
- MyPy checks that code adheres to type specifications

Design Pattern: Interpreter Pattern
- MyPy interprets type hints to validate code
"""

from typing import List, Dict, Optional, Union, Any, Callable
import sys


def demonstrate_mypy_concepts():
    """
    Demonstrates type errors that MyPy would catch.
    
    Note: These examples show code that would cause MyPy errors.
    The actual errors are shown in comments.
    """
    print("=" * 60)
    print("SECTION 3: MYPY – STATIC TYPE CHECKING")
    print("=" * 60)
    
    print("\n1. TYPE ERRORS MYPY CATCHES")
    print("-" * 40)
    
    print("""
    # Example 1: Wrong parameter type
    def greet(name: str) -> str:
        return f"Hello, {name}"
    
    # MyPy error: Argument 1 to "greet" has incompatible type "int"
    # greet(42)
    
    # Example 2: Wrong return type
    def get_count() -> int:
        return "five"  # MyPy error: Incompatible return value type
    
    # Example 3: Missing return
    def process(data: List[int]) -> int:
        if data:
            return data[0]
        # MyPy error: Missing return statement
    
    # Example 4: Wrong dictionary key type
    scores: Dict[str, int] = {}
    scores[42] = 100  # MyPy error: Invalid index type
    
    # Example 5: Optional not handled
    def find_user(user_id: int) -> Optional[str]:
        return None
    
    user = find_user(1)
    print(user.upper())  # MyPy error: Item "None" of "Optional[str]" has no attribute "upper"
    
    # Example 6: List type mismatch
    numbers: List[int] = [1, 2, 3]
    numbers.append("four")  # MyPy error: Argument 1 to "append" has incompatible type "str"
    """)
    
    print("\n2. MYPY CONFIGURATION (mypy.ini)")
    print("-" * 40)
    
    print("""
    # mypy.ini
    [mypy]
    python_version = 3.11
    warn_return_any = True
    warn_unused_configs = True
    disallow_untyped_defs = True
    disallow_any_unimported = True
    no_implicit_optional = True
    warn_redundant_casts = True
    warn_unused_ignores = True
    warn_no_return = True
    check_untyped_defs = True
    
    [mypy-requests]
    ignore_missing_imports = True
    """)
    
    print("\n3. RUNNING MYPY")
    print("-" * 40)
    
    print("""
    # Run on single file
    mypy script.py
    
    # Run on entire package
    mypy my_package/
    
    # Run with verbose output
    mypy -v script.py
    
    # Run with HTML report
    mypy --html-report ./mypy_html script.py
    
    # Run with strict mode
    mypy --strict script.py
    
    # Ignore missing imports
    mypy --ignore-missing-imports script.py
    """)


def demonstrate_type_ignore():
    """
    Demonstrates using # type: ignore to suppress MyPy errors.
    
    Use sparingly - only when you're sure the code is correct.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: TYPE IGNORE AND COMMENTS")
    print("=" * 60)
    
    print("\n1. SUPPRESSING ERRORS")
    print("-" * 40)
    
    print("""
    # Suppress error on specific line
    value: int = "string"  # type: ignore
    
    # Suppress specific error code
    value: int = "string"  # type: ignore[assignment]
    
    # Suppress whole block (with mypy >= 0.780)
    # mypy: ignore-errors
    problematic_code()
    # mypy: enable-errors
    """)
    
    print("\n2. TYPE COMMENTS (for older Python versions)")
    print("-" * 40)
    
    print("""
    # Before Python 3.6 (type hints as comments)
    def greet(name):
        # type: (str) -> str
        return f"Hello, {name}"
    
    # Multiple parameters
    def process(name, age, active):
        # type: (str, int, bool) -> Dict[str, Any]
        return {"name": name, "age": age, "active": active}
    """)


def demonstrate_type_checking_examples():
    """
    Demonstrates correct vs incorrect type usage.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: CORRECT VS INCORRECT EXAMPLES")
    print("=" * 60)
    
    from typing import Optional
    
    print("\n1. OPTIONAL HANDLING")
    print("-" * 40)
    
    def find_user(user_id: int) -> Optional[str]:
        """Find user by ID."""
        users = {1: "Alice", 2: "Bob"}
        return users.get(user_id)
    
    # BAD: Not handling None
    # user = find_user(3)
    # print(user.upper())  # Runtime error if None
    
    # GOOD: Handle None
    user = find_user(3)
    if user is not None:
        print(f"  Found user: {user.upper()}")
    else:
        print("  User not found")
    
    # GOOD: Use default value
    user = find_user(3) or "Unknown"
    print(f"  User: {user}")
    
    print("\n2. LIST TYPE CONSISTENCY")
    print("-" * 40)
    
    # GOOD: Consistent types
    numbers: List[int] = [1, 2, 3]
    numbers.append(4)
    print(f"  Numbers: {numbers}")
    
    # BAD: Mixed types in list (use Union if intentional)
    mixed: List[Union[int, str]] = [1, "two", 3]
    print(f"  Mixed: {mixed}")
    
    print("\n3. DICTIONARY KEY/VALUE TYPES")
    print("-" * 40)
    
    # GOOD: Consistent key/value types
    scores: Dict[str, int] = {"Alice": 95, "Bob": 87}
    scores["Charlie"] = 92
    print(f"  Scores: {scores}")
    
    # BAD: Wrong key type (would cause MyPy error)
    # scores[42] = 100
    
    print("\n4. FUNCTION OVERLOADING")
    print("-" * 40)
    
    from typing import overload
    
    @overload
    def process(value: int) -> int:
        ...
    
    @overload
    def process(value: str) -> str:
        ...
    
    def process(value: Union[int, str]) -> Union[int, str]:
        if isinstance(value, int):
            return value * 2
        else:
            return value.upper()
    
    print(f"  process(5) = {process(5)}")
    print(f"  process('hello') = {process('hello')}")


def build_type_annotated_application():
    """
    Builds a complete type-annotated application.
    
    This demonstrates best practices for using type hints in a real application.
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: TYPE-ANNOTATED APPLICATION")
    print("=" * 60)
    
    from typing import List, Dict, Optional, Tuple, Any
    from dataclasses import dataclass
    from datetime import datetime
    
    @dataclass
    class TodoItem:
        """Todo item with type annotations."""
        id: int
        title: str
        description: str
        completed: bool = False
        created_at: datetime = datetime.now()
        due_date: Optional[datetime] = None
        priority: int = 2  # 1=high, 2=medium, 3=low
    
    class TodoRepository:
        """Repository for todo items."""
        
        def __init__(self) -> None:
            self._items: Dict[int, TodoItem] = {}
            self._next_id: int = 1
        
        def add(self, title: str, description: str = "", 
                due_date: Optional[datetime] = None,
                priority: int = 2) -> TodoItem:
            """Add a new todo item."""
            item = TodoItem(
                id=self._next_id,
                title=title,
                description=description,
                due_date=due_date,
                priority=priority
            )
            self._items[item.id] = item
            self._next_id += 1
            return item
        
        def get(self, item_id: int) -> Optional[TodoItem]:
            """Get todo by ID."""
            return self._items.get(item_id)
        
        def update(self, item_id: int, **kwargs: Any) -> Optional[TodoItem]:
            """Update todo item."""
            item = self.get(item_id)
            if not item:
                return None
            
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            
            return item
        
        def delete(self, item_id: int) -> bool:
            """Delete todo item."""
            if item_id in self._items:
                del self._items[item_id]
                return True
            return False
        
        def get_all(self, include_completed: bool = False) -> List[TodoItem]:
            """Get all todos."""
            items = list(self._items.values())
            if not include_completed:
                items = [i for i in items if not i.completed]
            return sorted(items, key=lambda x: (x.priority, x.created_at))
        
        def get_by_priority(self, priority: int) -> List[TodoItem]:
            """Get todos by priority."""
            return [i for i in self._items.values() if i.priority == priority and not i.completed]
        
        def complete(self, item_id: int) -> Optional[TodoItem]:
            """Mark todo as completed."""
            return self.update(item_id, completed=True)
        
        def get_statistics(self) -> Dict[str, Any]:
            """Get todo statistics."""
            items = self._items.values()
            total = len(items)
            completed = sum(1 for i in items if i.completed)
            
            return {
                "total": total,
                "completed": completed,
                "pending": total - completed,
                "completion_rate": (completed / total * 100) if total > 0 else 0,
                "by_priority": {
                    priority: len(self.get_by_priority(priority))
                    for priority in [1, 2, 3]
                }
            }
    
    # Demonstrate the application
    repo = TodoRepository()
    
    print("\n1. CREATING TODOS")
    print("-" * 40)
    
    todo1 = repo.add("Learn Python", "Complete the Metromap course", priority=1)
    todo2 = repo.add("Write article", "Write about type hints", priority=2)
    todo3 = repo.add("Exercise", "30 minutes cardio", priority=3)
    
    print(f"  Created: {todo1.title} (ID: {todo1.id})")
    print(f"  Created: {todo2.title} (ID: {todo2.id})")
    print(f"  Created: {todo3.title} (ID: {todo3.id})")
    
    print("\n2. GETTING TODOS")
    print("-" * 40)
    
    todo = repo.get(1)
    if todo:
        print(f"  Todo 1: {todo.title} - Priority {todo.priority}")
    
    print("\n3. COMPLETING A TODO")
    print("-" * 40)
    
    repo.complete(1)
    print("  Todo 1 marked as completed")
    
    print("\n4. STATISTICS")
    print("-" * 40)
    
    stats = repo.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n5. TYPE-SAFE OPERATIONS")
    print("-" * 40)
    
    # This would be caught by MyPy:
    # repo.add(123, 456)  # Wrong parameter types
    
    # This works correctly:
    todo = repo.add("Correct usage", "String description", priority=2)
    print(f"  Created: {todo.title}")
    
    print("\n6. BENEFITS OF TYPE HINTS")
    print("-" * 40)
    
    print("""
    Benefits demonstrated:
    ✓ IDE autocomplete works better
    ✓ Catches bugs before runtime
    ✓ Self-documenting code
    ✓ Better refactoring support
    ✓ Acts as executable documentation
    ✓ Improves code readability
    """)


if __name__ == "__main__":
    demonstrate_mypy_concepts()
    demonstrate_type_ignore()
    demonstrate_type_checking_examples()
    build_type_annotated_application()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Basic Type Hints** – `name: str = "Alice"`, `def func(x: int) -> str:`. Optional but improve code quality.

- **Container Types** – `List[int]`, `Dict[str, int]`, `Tuple[int, str]`, `Set[float]`. Import from `typing`.

- **Optional and Union** – `Optional[str]` means `str or None`. `Union[int, str]` means `int or str`.

- **Callable Types** – `Callable[[int, int], int]` for functions. Great for callbacks and decorators.

- **Protocols** – Define interfaces without inheritance. Enables structural subtyping (duck typing with types).

- **TypedDict** – Specify structure of dictionaries. Keys and value types are defined.

- **Final and Literal** – `Final` for constants. `Literal["DEBUG", "INFO"]` for specific values.

- **Generics** – `TypeVar('T')` for type parameters. `Stack[T]` works with any type.

- **MyPy** – Static type checker. Catches type errors before runtime. `mypy script.py` to run.

- **Type Ignore** – `# type: ignore` suppresses errors. Use sparingly.

- **SOLID Principles Applied** – Interface Segregation (type hints document interfaces), Liskov Substitution (protocols enable structural subtyping), Dependency Inversion (MyPy checks adherence to types), Open/Closed (type hints don't change behavior).

- **Design Patterns Used** – Specification Pattern (type hints specify requirements), Protocol Pattern (structural interfaces), Interpreter Pattern (MyPy interprets hints), Generic Pattern (type-parameterized classes).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Testing & Debugging – pytest and unittest

- **📚 Series F Catalog:** Advanced Python Engineering – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: NumPy – Numerical Computing (Series G, Story 1)

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
| Series F | 6 | 6 | 0 | 100% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **40** | **12** | **77%** |

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
40. Series F, Story 6: The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking

**Next Story:** Series G, Story 1: The 2026 Python Metromap: NumPy – Numerical Computing

---

## 📝 Your Invitation

**Congratulations! You've completed the Advanced Python Engineering Line!**

You've mastered:
- Decorators (wrapping functions with behavior)
- Generators (memory-efficient lazy sequences)
- Iterators (custom iteration protocols)
- Memory Management (reference counting, GC, weak references)
- Testing & Debugging (unittest, pytest, pdb, mocking)
- Type Hints & MyPy (static type checking)

Now build something with what you've learned:

1. **Add type hints to an existing project** – Annotate all functions and classes, run MyPy.

2. **Set up a CI pipeline** – Run MyPy and pytest automatically on every commit.

3. **Create a generic repository** – Build a type-safe repository class using generics.

4. **Write a protocol** – Define a protocol for serializable objects and implement it in multiple classes.

5. **Use TypedDict for configuration** – Define strict configuration dictionaries with TypedDict.

**You've mastered Advanced Python Engineering. Next stop: Data Science & Visualization – NumPy!**

---

*Found this helpful? Clap, comment, and share what you annotated with type hints. Next stop: NumPy!* 🚇