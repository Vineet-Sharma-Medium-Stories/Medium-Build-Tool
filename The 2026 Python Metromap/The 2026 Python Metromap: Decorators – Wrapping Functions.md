# The 2026 Python Metromap: Decorators – Wrapping Functions

## Series F: Advanced Python Engineering | Story 1 of 6

![The 2026 Python Metromap/images/Decorators – Wrapping Functions](images/Decorators – Wrapping Functions.png)

## 📖 Introduction

**Welcome to the first stop on the Advanced Python Engineering Line.**

You've completed the File & Data Handling Line. You can read and write files, process CSV/JSON, handle exceptions, manage resources with context managers, and navigate file systems. But as your code becomes more sophisticated, you'll notice patterns—repeated boilerplate around functions: logging, timing, caching, authentication, retry logic. Writing this boilerplate repeatedly violates the DRY (Don't Repeat Yourself) principle.

That's where decorators come in.

Decorators are functions that modify the behavior of other functions. They wrap a function, adding functionality before, after, or around its execution, without changing the function's code. Decorators are used extensively in modern Python—for logging, timing, caching (`@lru_cache`), routing in web frameworks (`@app.route`), authentication (`@login_required`), and much more.

This story—**The 2026 Python Metromap: Decorators – Wrapping Functions**—is your guide to mastering decorators in Python. We'll start with function decorators, then class decorators, and decorators with arguments. We'll build a complete authentication system with `@login_required` and `@role_required` decorators. We'll create performance monitoring decorators (`@timer`, `@profile`). We'll implement retry logic with `@retry`. We'll build a caching system with `@cached`. And we'll create a complete web framework-style routing system.

**Let's wrap our functions.**

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

- 🎨 **The 2026 Python Metromap: Decorators – Wrapping Functions** – Authentication middleware; logging decorators; API retry logic. **⬅️ YOU ARE HERE**

- 🔄 **The 2026 Python Metromap: Generators – Memory-Efficient Loops** – Streaming large CSV files; paginated API responses; infinite data streams. 🔜 *Up Next*

- 🔁 **The 2026 Python Metromap: Iterators – Custom Looping** – Database paginator; file chunk reader; Fibonacci sequence iterator.

- 🧠 **The 2026 Python Metromap: Memory Management & Garbage Collection** – Optimizing a recommendation engine; memory profiling; leak fixing.

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports.

- 📝 **The 2026 Python Metromap: Type Hints & MyPy** – Large team codebase annotations; pre-runtime bug catching; automatic documentation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🎨 Section 1: Decorator Basics – Functions that Wrap Functions

Decorators are functions that take another function as an argument, add functionality, and return a new function.

**SOLID Principle Applied: Open/Closed** – Decorators add functionality without modifying existing code.

**Design Pattern: Decorator Pattern** – Wraps objects to add behavior dynamically.

```python
"""
DECORATOR BASICS: FUNCTIONS THAT WRAP FUNCTIONS

This section covers the fundamentals of decorators.

SOLID Principle: Open/Closed
- Decorators add functionality without modifying existing code

Design Pattern: Decorator Pattern
- Wraps objects to add behavior dynamically
"""

import time
import functools
from typing import Any, Callable


def demonstrate_basic_decorators():
    """
    Demonstrates basic decorator syntax and usage.
    
    A decorator is a function that takes a function and returns a function.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC DECORATORS")
    print("=" * 60)
    
    # SIMPLE DECORATOR
    print("\n1. SIMPLE DECORATOR (without @ syntax)")
    print("-" * 40)
    
    def logger(func):
        """Decorator that logs when function is called."""
        def wrapper(*args, **kwargs):
            print(f"  Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"  {func.__name__} returned {result}")
            return result
        return wrapper
    
    def add(a, b):
        return a + b
    
    # Manual decoration
    add_with_logging = logger(add)
    result = add_with_logging(3, 5)
    print(f"  Result: {result}")
    
    # DECORATOR WITH @ SYNTAX
    print("\n2. DECORATOR WITH @ SYNTAX")
    print("-" * 40)
    
    @logger
    def multiply(a, b):
        return a * b
    
    result = multiply(4, 5)
    print(f"  Result: {result}")
    
    # TIMING DECORATOR
    print("\n3. TIMING DECORATOR")
    print("-" * 40)
    
    def timer(func):
        """Decorator that measures execution time."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"  {func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper
    
    @timer
    def slow_function():
        time.sleep(0.1)
        return "Done"
    
    slow_function()
    
    # PRESERVING FUNCTION METADATA with functools.wraps
    print("\n4. PRESERVING FUNCTION METADATA (functools.wraps)")
    print("-" * 40)
    
    def bad_decorator(func):
        """Decorator without wraps."""
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    def good_decorator(func):
        """Decorator with wraps."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @bad_decorator
    def my_function():
        """This is my function docstring."""
        pass
    
    @good_decorator
    def my_function2():
        """This is my function docstring."""
        pass
    
    print(f"  Without wraps - name: {my_function.__name__}, doc: {my_function.__doc__}")
    print(f"  With wraps - name: {my_function2.__name__}, doc: {my_function2.__doc__}")
    
    # MULTIPLE DECORATORS (stacking)
    print("\n5. MULTIPLE DECORATORS (stacking)")
    print("-" * 40)
    
    @timer
    @logger
    def complex_operation(a, b):
        """Complex operation with multiple decorators."""
        time.sleep(0.05)
        return a ** b
    
    result = complex_operation(2, 10)
    print(f"  Result: {result}")


def demonstrate_decorators_with_arguments():
    """
    Demonstrates decorators that accept arguments.
    
    Decorators with arguments require an extra level of nesting.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: DECORATORS WITH ARGUMENTS")
    print("=" * 60)
    
    # DECORATOR WITH ARGUMENTS
    print("\n1. REPEAT DECORATOR (with argument)")
    print("-" * 40)
    
    def repeat(times: int):
        """Decorator that repeats a function multiple times."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"  Iteration {i + 1}/{times}")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    @repeat(times=3)
    def say_hello(name):
        return f"Hello, {name}!"
    
    results = say_hello("Alice")
    print(f"  Results: {results}")
    
    # DELAY DECORATOR
    print("\n2. DELAY DECORATOR")
    print("-" * 40)
    
    def delay(seconds: float):
        """Decorator that delays function execution."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"  Waiting {seconds} seconds...")
                time.sleep(seconds)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    @delay(0.5)
    def quick_message():
        return "This message was delayed"
    
    result = quick_message()
    print(f"  Result: {result}")
    
    # RETRY DECORATOR
    print("\n3. RETRY DECORATOR")
    print("-" * 40)
    
    def retry(max_attempts: int = 3, delay_seconds: float = 0.1):
        """Decorator that retries function on failure."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        if attempt < max_attempts:
                            print(f"  Attempt {attempt} failed, retrying in {delay_seconds}s...")
                            time.sleep(delay_seconds)
                raise last_exception
            return wrapper
        return decorator
    
    # Simulate flaky function
    attempt_count = 0
    
    @retry(max_attempts=3, delay_seconds=0.1)
    def flaky_function():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ConnectionError("Temporary failure")
        return "Success after retries"
    
    result = flaky_function()
    print(f"  Result: {result} (after {attempt_count} attempts)")
    
    # CONDITIONAL DECORATOR
    print("\n4. CONDITIONAL DECORATOR")
    print("-" * 40)
    
    def conditional(condition: bool):
        """Decorator that only applies if condition is True."""
        def decorator(func):
            if condition:
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    print(f"  Decorator applied to {func.__name__}")
                    return func(*args, **kwargs)
                return wrapper
            else:
                return func
        return decorator
    
    DEBUG_MODE = True
    
    @conditional(DEBUG_MODE)
    def debug_function():
        return "Debug output"
    
    @conditional(not DEBUG_MODE)
    def release_function():
        return "Release output"
    
    print(f"  debug_function: {debug_function()}")
    print(f"  release_function: {release_function()}")


def demonstrate_class_decorators():
    """
    Demonstrates decorators that work with classes and methods.
    
    Class decorators can modify classes; method decorators modify methods.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: CLASS AND METHOD DECORATORS")
    print("=" * 60)
    
    # CLASS DECORATOR
    print("\n1. CLASS DECORATOR")
    print("-" * 40)
    
    def add_repr(cls):
        """Class decorator that adds __repr__ method."""
        def __repr__(self):
            attrs = [f"{k}={v!r}" for k, v in self.__dict__.items()]
            return f"{cls.__name__}({', '.join(attrs)})"
        cls.__repr__ = __repr__
        return cls
    
    @add_repr
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    person = Person("Alice", 28)
    print(f"  Person with decorator: {person}")
    
    # METHOD DECORATOR
    print("\n2. METHOD DECORATOR")
    print("-" * 40)
    
    def log_method_calls(cls):
        """Class decorator that logs all method calls."""
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                setattr(cls, attr_name, logger(attr_value))
        return cls
    
    @log_method_calls
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def multiply(self, a, b):
            return a * b
    
    calc = Calculator()
    calc.add(5, 3)
    calc.multiply(4, 2)
    
    # STATIC METHOD DECORATOR
    print("\n3. STATIC METHOD DECORATOR (classmethod, staticmethod)")
    print("-" * 40)
    
    class MyClass:
        @staticmethod
        def static_method():
            return "Static method"
        
        @classmethod
        def class_method(cls):
            return f"Class method of {cls.__name__}"
    
    print(f"  Static method: {MyClass.static_method()}")
    print(f"  Class method: {MyClass.class_method()}")
    
    # PROPERTY DECORATOR
    print("\n4. PROPERTY DECORATOR")
    print("-" * 40)
    
    class Temperature:
        def __init__(self, celsius):
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Temperature below absolute zero")
            self._celsius = value
        
        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32
    
    temp = Temperature(25)
    print(f"  Celsius: {temp.celsius}")
    print(f"  Fahrenheit: {temp.fahrenheit}")
    temp.celsius = 30
    print(f"  After change: {temp.celsius}°C = {temp.fahrenheit}°F")


if __name__ == "__main__":
    demonstrate_basic_decorators()
    demonstrate_decorators_with_arguments()
    demonstrate_class_decorators()
```

---

## 🔐 Section 2: Authentication and Authorization Decorators

A complete authentication system using decorators for login and role-based access control.

**SOLID Principles Applied:**
- Open/Closed: Add security to functions without modifying them
- Single Responsibility: Decorators handle only auth concerns

**Design Patterns:**
- Decorator Pattern: Wraps functions with security checks
- Proxy Pattern: Decorators act as security proxies

```python
"""
AUTHENTICATION AND AUTHORIZATION DECORATORS

This section builds authentication decorators for access control.

SOLID Principles Applied:
- Open/Closed: Add security without modifying functions
- Single Responsibility: Decorators handle only auth concerns

Design Patterns:
- Decorator Pattern: Wraps functions with security checks
- Proxy Pattern: Decorators act as security proxies
"""

import functools
from typing import Dict, List, Optional, Callable, Any
from enum import Enum
from datetime import datetime, timedelta
import hashlib
import secrets


class UserRole(Enum):
    """User roles for authorization."""
    GUEST = "guest"
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"


class User:
    """User class for authentication."""
    
    def __init__(self, user_id: str, username: str, role: UserRole, 
                 password_hash: str, is_active: bool = True):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.password_hash = password_hash
        self.is_active = is_active
        self.last_login = None
        self.created_at = datetime.now()
        self.session_token: Optional[str] = None
        self.token_expiry: Optional[datetime] = None
    
    def authenticate(self, password: str) -> bool:
        """Authenticate user with password."""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()
    
    def create_session(self) -> str:
        """Create a new session token."""
        self.session_token = secrets.token_urlsafe(32)
        self.token_expiry = datetime.now() + timedelta(hours=24)
        return self.session_token
    
    def validate_session(self, token: str) -> bool:
        """Validate session token."""
        return (self.session_token == token and 
                self.token_expiry and 
                datetime.now() < self.token_expiry)
    
    def logout(self) -> None:
        """Invalidate session."""
        self.session_token = None
        self.token_expiry = None


class AuthManager:
    """
    Manages authentication and authorization.
    
    Design Pattern: Singleton Pattern - Single auth manager
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.users: Dict[str, User] = {}
        self._current_user: Optional[User] = None
        self._initialized = True
    
    def register_user(self, username: str, password: str, role: UserRole = UserRole.USER) -> User:
        """Register a new user."""
        if username in self.users:
            raise ValueError(f"User {username} already exists")
        
        user_id = f"user_{len(self.users) + 1}"
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        user = User(user_id, username, role, password_hash)
        self.users[username] = user
        return user
    
    def login(self, username: str, password: str) -> Optional[str]:
        """Login user and return session token."""
        user = self.users.get(username)
        if not user or not user.authenticate(password):
            return None
        
        if not user.is_active:
            return None
        
        user.last_login = datetime.now()
        token = user.create_session()
        self._current_user = user
        return token
    
    def logout(self) -> None:
        """Logout current user."""
        if self._current_user:
            self._current_user.logout()
            self._current_user = None
    
    def get_current_user(self) -> Optional[User]:
        """Get current authenticated user."""
        return self._current_user
    
    def validate_token(self, token: str) -> Optional[User]:
        """Validate session token and return user."""
        for user in self.users.values():
            if user.validate_session(token):
                self._current_user = user
                return user
        return None


# Global auth manager instance
_auth_manager = AuthManager()


def login_required(func: Callable) -> Callable:
    """
    Decorator that requires user to be logged in.
    
    Usage:
        @app.route('/dashboard')
        @login_required
        def dashboard():
            return "Welcome to dashboard"
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not _auth_manager.get_current_user():
            raise PermissionError("Login required")
        return func(*args, **kwargs)
    return wrapper


def role_required(*allowed_roles: UserRole) -> Callable:
    """
    Decorator that requires user to have one of the allowed roles.
    
    Usage:
        @app.route('/admin')
        @role_required(UserRole.ADMIN, UserRole.SUPER_ADMIN)
        def admin_panel():
            return "Admin panel"
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = _auth_manager.get_current_user()
            if not user:
                raise PermissionError("Login required")
            if user.role not in allowed_roles:
                raise PermissionError(
                    f"Role {user.role.value} not allowed. "
                    f"Required: {[r.value for r in allowed_roles]}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator


def permission_required(permission: str) -> Callable:
    """
    Decorator for fine-grained permissions.
    
    Usage:
        @permission_required('users.delete')
        def delete_user(user_id):
            pass
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = _auth_manager.get_current_user()
            if not user:
                raise PermissionError("Login required")
            
            # Permission mapping based on role
            role_permissions = {
                UserRole.GUEST: ['view_public'],
                UserRole.USER: ['view_public', 'edit_profile', 'view_own_data'],
                UserRole.MODERATOR: ['view_public', 'edit_profile', 'view_own_data',
                                    'view_users', 'edit_content'],
                UserRole.ADMIN: ['*'],  # All permissions
                UserRole.SUPER_ADMIN: ['*']
            }
            
            allowed = role_permissions.get(user.role, [])
            if '*' not in allowed and permission not in allowed:
                raise PermissionError(f"Permission '{permission}' denied")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def optional_auth(func: Callable) -> Callable:
    """
    Decorator that makes auth optional - sets user if available.
    
    Usage:
        @app.route('/profile')
        @optional_auth
        def profile(user=None):
            if user:
                return f"Profile of {user.username}"
            return "Please login to see your profile"
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = _auth_manager.get_current_user()
        return func(*args, **kwargs, user=user)
    return wrapper


def impersonate(user_role: UserRole):
    """
    Decorator for testing - impersonates a user role.
    
    Usage:
        @impersonate(UserRole.ADMIN)
        def test_admin_features():
            # Runs as admin
            pass
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Save original user
            original_user = _auth_manager.get_current_user()
            
            # Create temporary test user
            test_user = User(
                user_id="test_user",
                username="test",
                role=user_role,
                password_hash="",
                is_active=True
            )
            
            # Set as current user
            _auth_manager._current_user = test_user
            
            try:
                return func(*args, **kwargs)
            finally:
                # Restore original user
                _auth_manager._current_user = original_user
        return wrapper
    return decorator


def audit_log(action: str):
    """
    Decorator that logs user actions.
    
    Usage:
        @audit_log('user_deletion')
        def delete_user(user_id):
            pass
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = _auth_manager.get_current_user()
            username = user.username if user else "anonymous"
            
            print(f"  [AUDIT] {username} performed '{action}' at {datetime.now()}")
            
            result = func(*args, **kwargs)
            
            print(f"  [AUDIT] {action} completed")
            return result
        return wrapper
    return decorator


def demonstrate_auth_decorators():
    """
    Demonstrate authentication and authorization decorators.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: AUTHENTICATION AND AUTHORIZATION DECORATORS")
    print("=" * 60)
    
    # Register users
    print("\n1. REGISTERING USERS")
    print("-" * 40)
    
    auth = AuthManager()
    admin = auth.register_user("admin", "admin123", UserRole.ADMIN)
    moderator = auth.register_user("moderator", "mod123", UserRole.MODERATOR)
    regular_user = auth.register_user("alice", "pass123", UserRole.USER)
    
    print(f"  Registered: admin (admin), moderator, alice (user)")
    
    # Define protected functions
    print("\n2. DEFINING PROTECTED FUNCTIONS")
    print("-" * 40)
    
    @login_required
    def dashboard():
        return "Welcome to your dashboard!"
    
    @role_required(UserRole.ADMIN, UserRole.SUPER_ADMIN)
    def admin_panel():
        return "Admin panel - sensitive operations"
    
    @permission_required('users.delete')
    def delete_user(user_id: str):
        return f"Deleted user {user_id}"
    
    @optional_auth
    def profile_page(user=None):
        if user:
            return f"Profile of {user.username}"
        return "Please login to view your profile"
    
    @audit_log('view_admin_panel')
    @role_required(UserRole.ADMIN)
    def audited_admin_action():
        return "Admin action logged"
    
    print("  Functions defined with auth decorators")
    
    # Test without login
    print("\n3. TESTING WITHOUT LOGIN")
    print("-" * 40)
    
    try:
        result = dashboard()
    except PermissionError as e:
        print(f"  dashboard: {e}")
    
    try:
        result = profile_page()
    except Exception as e:
        print(f"  profile_page: {e}")
    else:
        print(f"  profile_page: {result}")
    
    # Test with regular user
    print("\n4. TESTING WITH REGULAR USER")
    print("-" * 40)
    
    token = auth.login("alice", "pass123")
    print(f"  Logged in as alice")
    
    try:
        result = dashboard()
        print(f"  dashboard: {result}")
    except PermissionError as e:
        print(f"  dashboard: {e}")
    
    try:
        result = admin_panel()
    except PermissionError as e:
        print(f"  admin_panel: {e}")
    
    try:
        result = delete_user("user123")
    except PermissionError as e:
        print(f"  delete_user: {e}")
    
    result = profile_page()
    print(f"  profile_page: {result}")
    
    # Test with admin
    print("\n5. TESTING WITH ADMIN")
    print("-" * 40)
    
    auth.logout()
    token = auth.login("admin", "admin123")
    print(f"  Logged in as admin")
    
    result = dashboard()
    print(f"  dashboard: {result}")
    
    result = admin_panel()
    print(f"  admin_panel: {result}")
    
    result = delete_user("user123")
    print(f"  delete_user: {result}")
    
    result = audited_admin_action()
    print(f"  audited_admin_action: {result}")
    
    # Test impersonation
    print("\n6. TESTING IMPERSONATION (for testing)")
    print("-" * 40)
    
    @impersonate(UserRole.ADMIN)
    def test_admin_function():
        user = auth.get_current_user()
        return f"Running as {user.username} ({user.role.value})"
    
    # Logout first
    auth.logout()
    result = test_admin_function()
    print(f"  {result}")
    
    # Verify original user not affected
    print(f"  Current user after impersonation: {auth.get_current_user()}")


if __name__ == "__main__":
    demonstrate_auth_decorators()
```

---

## ⏱️ Section 3: Performance Monitoring Decorators

Decorators for measuring and monitoring function performance.

**SOLID Principles Applied:**
- Open/Closed: Add monitoring without changing function logic
- Single Responsibility: Monitoring separated from business logic

**Design Patterns:**
- Decorator Pattern: Wraps functions with monitoring
- Observer Pattern: Notifies when thresholds exceeded

```python
"""
PERFORMANCE MONITORING DECORATORS

This section builds performance monitoring decorators.

SOLID Principles Applied:
- Open/Closed: Add monitoring without changing function logic
- Single Responsibility: Monitoring separated from business logic

Design Patterns:
- Decorator Pattern: Wraps functions with monitoring
- Observer Pattern: Notifies when thresholds exceeded
"""

import functools
import time
import threading
from typing import Dict, List, Optional, Callable, Any
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
import statistics


@dataclass
class PerformanceMetric:
    """Performance metric for a function."""
    name: str
    call_count: int = 0
    total_time: float = 0.0
    min_time: float = float('inf')
    max_time: float = 0.0
    errors: int = 0
    last_called: Optional[datetime] = None
    history: List[float] = field(default_factory=list)
    
    @property
    def avg_time(self) -> float:
        return self.total_time / self.call_count if self.call_count > 0 else 0.0
    
    @property
    def success_rate(self) -> float:
        total = self.call_count + self.errors
        return (self.call_count / total * 100) if total > 0 else 100.0


class MetricsCollector:
    """Collects performance metrics across functions."""
    
    def __init__(self):
        self.metrics: Dict[str, PerformanceMetric] = {}
        self.thresholds: Dict[str, float] = {}
        self.alert_callbacks: List[Callable] = []
    
    def record_call(self, func_name: str, duration: float, success: bool = True):
        """Record a function call."""
        if func_name not in self.metrics:
            self.metrics[func_name] = PerformanceMetric(name=func_name)
        
        metric = self.metrics[func_name]
        
        if success:
            metric.call_count += 1
            metric.total_time += duration
            metric.min_time = min(metric.min_time, duration)
            metric.max_time = max(metric.max_time, duration)
            metric.history.append(duration)
            # Keep last 100
            if len(metric.history) > 100:
                metric.history.pop(0)
        else:
            metric.errors += 1
        
        metric.last_called = datetime.now()
        
        # Check threshold
        if func_name in self.thresholds and duration > self.thresholds[func_name]:
            self._alert(func_name, duration, self.thresholds[func_name])
    
    def set_threshold(self, func_name: str, threshold_ms: float):
        """Set performance threshold for a function."""
        self.thresholds[func_name] = threshold_ms
    
    def add_alert_callback(self, callback: Callable):
        """Add callback for threshold alerts."""
        self.alert_callbacks.append(callback)
    
    def _alert(self, func_name: str, duration: float, threshold: float):
        """Trigger alert for threshold violation."""
        message = f"Performance alert: {func_name} took {duration:.2f}ms (threshold: {threshold:.0f}ms)"
        for callback in self.alert_callbacks:
            try:
                callback(message)
            except Exception:
                pass
    
    def get_stats(self, func_name: Optional[str] = None) -> Dict:
        """Get statistics for a function or all functions."""
        if func_name:
            metric = self.metrics.get(func_name)
            if metric:
                return {
                    "call_count": metric.call_count,
                    "avg_ms": round(metric.avg_time, 2),
                    "min_ms": round(metric.min_time, 2),
                    "max_ms": round(metric.max_time, 2),
                    "total_ms": round(metric.total_time, 2),
                    "errors": metric.errors,
                    "success_rate": round(metric.success_rate, 1),
                    "p95": self._percentile(metric.history, 95) if metric.history else 0
                }
            return {}
        
        return {name: self.get_stats(name) for name in self.metrics}
    
    def _percentile(self, data: List[float], percentile: float) -> float:
        """Calculate percentile of data."""
        if not data:
            return 0.0
        sorted_data = sorted(data)
        index = int(len(sorted_data) * percentile / 100)
        return sorted_data[min(index, len(sorted_data) - 1)]
    
    def reset(self):
        """Reset all metrics."""
        self.metrics.clear()


# Global metrics collector
_metrics = MetricsCollector()


def timer(func: Callable = None, *, name: Optional[str] = None, 
          threshold_ms: Optional[float] = None) -> Callable:
    """
    Decorator that measures function execution time.
    
    Usage:
        @timer
        def my_function():
            pass
        
        @timer(name="custom_name", threshold_ms=100)
        def slow_function():
            pass
    """
    def decorator(f):
        func_name = name or f.__name__
        
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            success = True
            try:
                result = f(*args, **kwargs)
                return result
            except Exception:
                success = False
                raise
            finally:
                duration = (time.perf_counter() - start) * 1000  # Convert to ms
                _metrics.record_call(func_name, duration, success)
        
        if threshold_ms:
            _metrics.set_threshold(func_name, threshold_ms)
        
        return wrapper
    
    if func is None:
        return decorator
    return decorator(func)


def profile(func: Callable = None, *, detailed: bool = False) -> Callable:
    """
    Decorator that provides detailed profiling information.
    
    Includes CPU time, memory usage, and call count.
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            import tracemalloc
            import resource
            
            # Start tracking
            start_time = time.perf_counter()
            start_cpu = time.process_time()
            
            if detailed:
                tracemalloc.start()
                start_memory = tracemalloc.get_traced_memory()[0]
            
            try:
                result = f(*args, **kwargs)
                return result
            finally:
                # Calculate metrics
                end_time = time.perf_counter()
                end_cpu = time.process_time()
                duration_ms = (end_time - start_time) * 1000
                cpu_ms = (end_cpu - start_cpu) * 1000
                
                print(f"\n  📊 Profile of {f.__name__}:")
                print(f"    Wall time: {duration_ms:.2f}ms")
                print(f"    CPU time: {cpu_ms:.2f}ms")
                
                if detailed:
                    current, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    print(f"    Memory peak: {peak / 1024:.2f}KB")
                    print(f"    Memory current: {current / 1024:.2f}KB")
                
                _metrics.record_call(f.__name__, duration_ms, True)
        
        return wrapper
    
    if func is None:
        return decorator
    return decorator(func)


def rate_limit(calls_per_second: float):
    """
    Decorator that rate-limits function calls.
    
    Usage:
        @rate_limit(calls_per_second=10)
        def api_call():
            pass
    """
    min_interval = 1.0 / calls_per_second
    last_called = {}
    lock = threading.Lock()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                now = time.time()
                key = func.__name__
                if key in last_called:
                    elapsed = now - last_called[key]
                    if elapsed < min_interval:
                        wait_time = min_interval - elapsed
                        time.sleep(wait_time)
                last_called[key] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator


def memoize(func: Callable = None, *, maxsize: int = 128) -> Callable:
    """
    Caching decorator (similar to functools.lru_cache).
    
    Caches function results based on arguments.
    """
    cache = {}
    cache_hits = 0
    cache_misses = 0
    
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            nonlocal cache_hits, cache_misses
            
            # Create cache key
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                cache_hits += 1
                return cache[key]
            
            cache_misses += 1
            result = f(*args, **kwargs)
            
            # Manage cache size
            if len(cache) >= maxsize:
                # Remove oldest (simplified)
                cache.pop(next(iter(cache)))
            
            cache[key] = result
            return result
        
        def cache_info():
            return {
                "hits": cache_hits,
                "misses": cache_misses,
                "size": len(cache),
                "maxsize": maxsize
            }
        
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache.clear
        return wrapper
    
    if func is None:
        return decorator
    return decorator(func)


def demonstrate_performance_decorators():
    """
    Demonstrate performance monitoring decorators.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: PERFORMANCE MONITORING DECORATORS")
    print("=" * 60)
    
    # Add alert callback
    def alert_handler(message):
        print(f"  🔔 ALERT: {message}")
    
    _metrics.add_alert_callback(alert_handler)
    
    print("\n1. TIMING DECORATOR")
    print("-" * 40)
    
    @timer
    def compute_fibonacci(n: int) -> int:
        """Compute Fibonacci number recursively."""
        if n <= 1:
            return n
        return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)
    
    result = compute_fibonacci(30)
    print(f"  Fibonacci(30) = {result}")
    
    print("\n2. THRESHOLD MONITORING")
    print("-" * 40)
    
    @timer(threshold_ms=50)
    def potentially_slow_function():
        time.sleep(0.08)  # 80ms - exceeds threshold
        return "Done"
    
    potentially_slow_function()
    
    print("\n3. DETAILED PROFILING")
    print("-" * 40)
    
    @profile(detailed=True)
    def memory_intensive():
        data = [i for i in range(100000)]
        return sum(data)
    
    result = memory_intensive()
    print(f"  Result: {result}")
    
    print("\n4. RATE LIMITING")
    print("-" * 40)
    
    @rate_limit(calls_per_second=2)
    def limited_function(x: int) -> int:
        return x * 2
    
    start = time.time()
    for i in range(5):
        result = limited_function(i)
        print(f"  Call {i+1}: {result}")
    elapsed = time.time() - start
    print(f"  5 calls took {elapsed:.2f}s (should be ~2.5s with rate limiting)")
    
    print("\n5. MEMOIZATION (Caching)")
    print("-" * 40)
    
    @memoize
    def expensive_computation(n: int) -> int:
        """Expensive computation with caching."""
        print(f"  Computing for n={n} (cache miss)")
        time.sleep(0.1)
        return n * n
    
    for n in [2, 2, 3, 2, 3, 4]:
        result = expensive_computation(n)
        print(f"  expensive_computation({n}) = {result}")
    
    info = expensive_computation.cache_info()
    print(f"\n  Cache info: {info}")
    
    print("\n6. PERFORMANCE STATISTICS")
    print("-" * 40)
    
    stats = _metrics.get_stats()
    for name, stat in stats.items():
        if stat:
            print(f"\n  {name}:")
            print(f"    Calls: {stat['call_count']}")
            print(f"    Avg: {stat['avg_ms']}ms")
            print(f"    Min: {stat['min_ms']}ms")
            print(f"    Max: {stat['max_ms']}ms")
            print(f"    P95: {stat['p95']}ms")
            print(f"    Success Rate: {stat['success_rate']}%")


if __name__ == "__main__":
    demonstrate_performance_decorators()
```

---

## 🏭 Section 4: Web Framework-Style Routing Decorators

A complete routing system inspired by Flask, demonstrating decorators for URL routing.

**SOLID Principles Applied:**
- Open/Closed: New routes can be added without modifying core
- Single Responsibility: Each decorator handles one aspect of routing

**Design Patterns:**
- Decorator Pattern: Route registration via decorators
- Registry Pattern: Central route registry
- Front Controller Pattern: Single entry point for all requests

```python
"""
WEB FRAMEWORK-STYLE ROUTING DECORATORS

This section builds a routing system inspired by Flask.

SOLID Principles Applied:
- Open/Closed: New routes added without modifying core
- Single Responsibility: Each decorator handles one aspect

Design Patterns:
- Decorator Pattern: Route registration via decorators
- Registry Pattern: Central route registry
- Front Controller Pattern: Single entry point
"""

import functools
import inspect
import re
from typing import Dict, List, Optional, Callable, Any, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import json


class HTTPMethod(Enum):
    """HTTP methods."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


@dataclass
class Route:
    """Route definition."""
    path: str
    methods: List[HTTPMethod]
    handler: Callable
    name: Optional[str] = None
    middleware: List[Callable] = field(default_factory=list)
    docstring: Optional[str] = None


class Router:
    """
    URL router with decorator support.
    
    Design Pattern: Registry Pattern - Central route registry
    """
    
    def __init__(self):
        self.routes: List[Route] = []
        self.before_request_handlers: List[Callable] = []
        self.after_request_handlers: List[Callable] = []
    
    def route(self, path: str, methods: List[HTTPMethod] = None, name: str = None):
        """
        Decorator for registering routes.
        
        Usage:
            @app.route('/users')
            def get_users():
                return {"users": []}
        """
        methods = methods or [HTTPMethod.GET]
        
        def decorator(handler: Callable) -> Callable:
            route = Route(
                path=path,
                methods=methods,
                handler=handler,
                name=name or handler.__name__,
                docstring=handler.__doc__
            )
            self.routes.append(route)
            
            @functools.wraps(handler)
            def wrapper(*args, **kwargs):
                return handler(*args, **kwargs)
            return wrapper
        
        return decorator
    
    def get(self, path: str, name: str = None):
        """Decorator for GET route."""
        return self.route(path, methods=[HTTPMethod.GET], name=name)
    
    def post(self, path: str, name: str = None):
        """Decorator for POST route."""
        return self.route(path, methods=[HTTPMethod.POST], name=name)
    
    def put(self, path: str, name: str = None):
        """Decorator for PUT route."""
        return self.route(path, methods=[HTTPMethod.PUT], name=name)
    
    def delete(self, path: str, name: str = None):
        """Decorator for DELETE route."""
        return self.route(path, methods=[HTTPMethod.DELETE], name=name)
    
    def before_request(self, handler: Callable) -> Callable:
        """Decorator for before-request handlers."""
        self.before_request_handlers.append(handler)
        return handler
    
    def after_request(self, handler: Callable) -> Callable:
        """Decorator for after-request handlers."""
        self.after_request_handlers.append(handler)
        return handler
    
    def _match_path(self, route_path: str, request_path: str) -> Tuple[bool, Dict]:
        """Match a route path against a request path."""
        # Convert route path to regex
        pattern = route_path
        param_names = []
        
        # Handle path parameters like /users/<user_id>
        def replace_param(match):
            param_names.append(match.group(1))
            return r'([^/]+)'
        
        pattern = re.sub(r'<(\w+)>', replace_param, pattern)
        pattern = f"^{pattern}$"
        
        match = re.match(pattern, request_path)
        if not match:
            return False, {}
        
        params = {name: value for name, value in zip(param_names, match.groups())}
        return True, params
    
    def find_route(self, path: str, method: HTTPMethod) -> Tuple[Optional[Route], Dict]:
        """Find route matching path and method."""
        for route in self.routes:
            if method in route.methods:
                matches, params = self._match_path(route.path, path)
                if matches:
                    return route, params
        return None, {}
    
    def dispatch(self, path: str, method: HTTPMethod, **extra_params) -> Any:
        """
        Dispatch request to appropriate handler.
        
        Returns:
            Response from handler
        """
        route, path_params = self.find_route(path, method)
        
        if not route:
            return {"error": "Not found", "status": 404}
        
        # Before request handlers
        for handler in self.before_request_handlers:
            handler()
        
        # Merge parameters
        kwargs = {**path_params, **extra_params}
        
        # Get parameter names from handler
        sig = inspect.signature(route.handler)
        
        # Filter kwargs to match handler parameters
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
        
        # Execute handler
        try:
            response = route.handler(**filtered_kwargs)
        except Exception as e:
            response = {"error": str(e), "status": 500}
        
        # After request handlers
        for handler in self.after_request_handlers:
            response = handler(response)
        
        return response


class App:
    """
    Web application with routing decorators.
    
    Design Pattern: Front Controller Pattern - Single entry point
    """
    
    def __init__(self, name: str):
        self.name = name
        self.router = Router()
        self.middleware: List[Callable] = []
    
    def route(self, path: str, methods: List[HTTPMethod] = None, name: str = None):
        """Route decorator."""
        return self.router.route(path, methods, name)
    
    def get(self, path: str, name: str = None):
        """GET route decorator."""
        return self.router.get(path, name)
    
    def post(self, path: str, name: str = None):
        """POST route decorator."""
        return self.router.post(path, name)
    
    def put(self, path: str, name: str = None):
        """PUT route decorator."""
        return self.router.put(path, name)
    
    def delete(self, path: str, name: str = None):
        """DELETE route decorator."""
        return self.router.delete(path, name)
    
    def before_request(self, handler: Callable) -> Callable:
        """Before request decorator."""
        return self.router.before_request(handler)
    
    def after_request(self, handler: Callable) -> Callable:
        """After request decorator."""
        return self.router.after_request(handler)
    
    def use(self, middleware: Callable):
        """Add middleware."""
        self.middleware.append(middleware)
        return self
    
    def handle_request(self, path: str, method: str, **kwargs) -> Any:
        """Handle an HTTP request."""
        http_method = HTTPMethod(method.upper())
        
        # Apply middleware
        request = {"path": path, "method": method, "params": kwargs}
        for middleware in self.middleware:
            request = middleware(request)
        
        response = self.router.dispatch(path, http_method, **kwargs)
        
        # Format response
        if isinstance(response, dict):
            response = json.dumps(response, default=str)
        
        return response
    
    def run(self, host: str = "localhost", port: int = 8000):
        """Run the application (simulated)."""
        print(f"\n  Starting {self.name} on http://{host}:{port}")
        print(f"  Registered routes:")
        for route in self.router.routes:
            methods = ", ".join(m.value for m in route.methods)
            print(f"    {methods:10} {route.path} → {route.name}")


def demonstrate_routing_system():
    """
    Demonstrate the routing decorator system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: WEB FRAMEWORK-STYLE ROUTING DECORATORS")
    print("=" * 60)
    
    # Create application
    app = App("Metromap API")
    
    print("\n1. DEFINING ROUTES WITH DECORATORS")
    print("-" * 40)
    
    # Define routes using decorators
    @app.get('/')
    def home():
        return {"message": "Welcome to Metromap API", "version": "1.0"}
    
    @app.get('/users')
    def get_users():
        return {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
    
    @app.get('/users/<user_id>')
    def get_user(user_id: int):
        return {"id": user_id, "name": f"User {user_id}"}
    
    @app.post('/users')
    def create_user(name: str, email: str):
        return {"id": 100, "name": name, "email": email, "created": True}
    
    @app.put('/users/<user_id>')
    def update_user(user_id: int, name: str = None, email: str = None):
        updates = {}
        if name:
            updates["name"] = name
        if email:
            updates["email"] = email
        return {"id": user_id, "updated": updates}
    
    @app.delete('/users/<user_id>')
    def delete_user(user_id: int):
        return {"deleted": user_id}
    
    print("  Routes defined")
    
    print("\n2. BEFORE AND AFTER REQUEST HANDLERS")
    print("-" * 40)
    
    @app.before_request
    def log_request():
        print("  📝 Before request handler executed")
    
    @app.after_request
    def add_timestamp(response):
        if isinstance(response, dict):
            response["timestamp"] = datetime.now().isoformat()
        return response
    
    print("  Added before/after request handlers")
    
    print("\n3. MIDDLEWARE")
    print("-" * 40)
    
    def logging_middleware(request):
        print(f"  🚀 Middleware: {request['method']} {request['path']}")
        return request
    
    app.use(logging_middleware)
    print("  Added logging middleware")
    
    print("\n4. HANDLING REQUESTS")
    print("-" * 40)
    
    # Simulate requests
    requests = [
        ("GET", "/"),
        ("GET", "/users"),
        ("GET", "/users/42"),
        ("POST", "/users", {"name": "Charlie", "email": "charlie@example.com"}),
        ("PUT", "/users/42", {"name": "Charles"}),
        ("DELETE", "/users/42"),
        ("GET", "/nonexistent")
    ]
    
    for method, path, *params in requests:
        print(f"\n  {method} {path}")
        kwargs = params[0] if params else {}
        response = app.handle_request(path, method, **kwargs)
        print(f"    Response: {response}")
    
    print("\n5. REGISTERED ROUTES")
    print("-" * 40)
    
    app.run()


if __name__ == "__main__":
    demonstrate_routing_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Decorator Basics** – Functions that wrap other functions. Use `@decorator` syntax. Preserve metadata with `functools.wraps`.

- **Decorators with Arguments** – Extra nesting level: `def decorator(arg): def wrapper(func): return func`. Use for configuration.

- **Stacking Decorators** – Multiple decorators applied bottom-up. Execution order: innermost first.

- **Class Decorators** – Modify or enhance classes. Add methods, track instances, apply mixins.

- **Authentication Decorators** – `@login_required`, `@role_required`, `@permission_required`. Add security without modifying functions.

- **Performance Decorators** – `@timer` (execution time), `@profile` (detailed metrics), `@rate_limit`, `@memoize` (caching).

- **Routing Decorators** – `@app.route`, `@app.get`, `@app.post`. Flask-style routing system. Path parameter extraction.

- **SOLID Principles Applied** – Open/Closed (add behavior without modification), Single Responsibility (decorators handle cross-cutting concerns), Dependency Inversion (depends on callable abstraction).

- **Design Patterns Used** – Decorator Pattern (wrapping functions), Proxy Pattern (access control), Observer Pattern (threshold alerts), Registry Pattern (route registration), Front Controller Pattern (single entry point).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Working with Paths & Directories

- **📚 Series F Catalog:** Advanced Python Engineering – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Generators – Memory-Efficient Loops (Series F, Story 2)

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
| Series F | 6 | 1 | 5 | 17% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **35** | **17** | **67%** |

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

**Next Story:** Series F, Story 2: The 2026 Python Metromap: Generators – Memory-Efficient Loops

---

## 📝 Your Invitation

You've mastered decorators. Now build something with what you've learned:

1. **Build a caching decorator** – Implement TTL-based cache, LRU eviction, persistent cache to disk.

2. **Create a validation decorator** – Validate function arguments against schema before execution.

3. **Build a transaction decorator** – Wrap database operations in a transaction with commit/rollback.

4. **Create a circuit breaker decorator** – Stop calling failing functions, reset after timeout.

5. **Build a deprecation decorator** – Mark functions as deprecated, log warnings, suggest alternatives.

**You've mastered decorators. Next stop: Generators!**

---

*Found this helpful? Clap, comment, and share what you built with decorators. Next stop: Generators!* 🚇