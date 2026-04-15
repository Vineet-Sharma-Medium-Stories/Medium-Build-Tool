# The 2026 Python Metromap: Exception Handling – Graceful Failures

## Series E: File & Data Handling Line | Story 3 of 5

![The 2026 Python Metromap/images/Exception Handling – Graceful Failures](images/Exception Handling – Graceful Failures.png)

## 📖 Introduction

**Welcome to the third stop on the File & Data Handling Line.**

You've mastered file I/O and structured data formats. You can read CSV files, parse JSON, and process complex data. But what happens when things go wrong? When a file doesn't exist, when network requests fail, when data is malformed, when a division by zero occurs? Your program crashes—unless you handle exceptions properly.

Exception handling is the art of anticipating and gracefully recovering from errors. Instead of crashing, your program can detect problems, log them, retry operations, fall back to alternative paths, and continue running. Proper exception handling separates normal program logic from error handling logic, making code more robust and maintainable.

This story—**The 2026 Python Metromap: Exception Handling – Graceful Failures**—is your guide to mastering exceptions in Python. We'll build a resilient web scraper that handles network errors, retries failed requests, and continues where it left off. We'll create a robust data processor that validates input, handles malformed data, and logs errors for later review. We'll implement a retry mechanism with exponential backoff. We'll build a transaction system with rollback on failure. And we'll create a complete application with comprehensive error handling, logging, and recovery.

**Let's fail gracefully.**

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

### Series E: File & Data Handling Line (5 Stories)

- 📂 **The 2026 Python Metromap: File I/O – Reading & Writing** – Log file analyzer; server log parsing; error extraction; report generation.

- 📊 **The 2026 Python Metromap: CSV & JSON Processing – Structured Data** – Sales data importer/exporter; vendor CSV integration; API JSON formatting.

- ⚠️ **The 2026 Python Metromap: Exception Handling – Graceful Failures** – Resilient web scraper; network error handling; request retries. **⬅️ YOU ARE HERE**

- 🔧 **The 2026 Python Metromap: Context Managers – The with Statement** – Database connection pool; automatic resource cleanup. 🔜 *Up Next*

- 🗺️ **The 2026 Python Metromap: Working with Paths & Directories** – Automated backup system; file organization by date; log rotation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## ⚠️ Section 1: Exception Basics – Try, Except, Else, Finally

Exceptions are errors detected during execution. Python's try-except blocks allow you to handle them gracefully.

**SOLID Principle Applied: Single Responsibility** – Each except block handles one type of error.

**Design Pattern: Guardian Pattern** – Exceptions guard against unexpected conditions.

```python
"""
EXCEPTION BASICS: TRY, EXCEPT, ELSE, FINALLY

This section covers the fundamentals of exception handling.

SOLID Principle: Single Responsibility
- Each except block handles one type of error

Design Pattern: Guardian Pattern
- Exceptions guard against unexpected conditions
"""

import sys
import traceback
from typing import Optional, Any


def demonstrate_try_except():
    """
    Demonstrates basic try-except blocks for error handling.
    
    Common exception types:
    - ValueError: Invalid value
    - TypeError: Wrong type
    - FileNotFoundError: File doesn't exist
    - KeyError: Dictionary key missing
    - IndexError: List index out of range
    - ZeroDivisionError: Division by zero
    - ConnectionError: Network failure
    """
    print("=" * 60)
    print("SECTION 1A: BASIC TRY-EXCEPT")
    print("=" * 60)
    
    # VALUE ERROR HANDLING
    print("\n1. HANDLING ValueError")
    print("-" * 40)
    
    def safe_convert_to_int(value: str) -> Optional[int]:
        """Safely convert string to integer."""
        try:
            return int(value)
        except ValueError:
            print(f"  Error: '{value}' is not a valid integer")
            return None
    
    print(f"  safe_convert_to_int('42'): {safe_convert_to_int('42')}")
    print(f"  safe_convert_to_int('abc'): {safe_convert_to_int('abc')}")
    
    # DIVISION BY ZERO
    print("\n2. HANDLING ZeroDivisionError")
    print("-" * 40)
    
    def safe_divide(a: float, b: float) -> Optional[float]:
        """Safely divide two numbers."""
        try:
            return a / b
        except ZeroDivisionError:
            print(f"  Error: Cannot divide {a} by zero")
            return None
    
    print(f"  safe_divide(10, 2): {safe_divide(10, 2)}")
    print(f"  safe_divide(10, 0): {safe_divide(10, 0)}")
    
    # FILE NOT FOUND
    print("\n3. HANDLING FileNotFoundError")
    print("-" * 40)
    
    def read_file_safely(filename: str) -> Optional[str]:
        """Safely read a file."""
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"  Error: File '{filename}' not found")
            return None
    
    print(f"  read_file_safely('existing.txt'): {read_file_safely('existing.txt')}")
    print(f"  read_file_safely('missing.txt'): {read_file_safely('missing.txt')}")
    
    # KEY ERROR
    print("\n4. HANDLING KeyError")
    print("-" * 40)
    
    def get_dict_value(data: dict, key: str, default=None):
        """Safely get value from dictionary."""
        try:
            return data[key]
        except KeyError:
            print(f"  Error: Key '{key}' not found")
            return default
    
    user = {"name": "Alice", "age": 28}
    print(f"  get_dict_value(user, 'name'): {get_dict_value(user, 'name')}")
    print(f"  get_dict_value(user, 'email'): {get_dict_value(user, 'email')}")
    
    # INDEX ERROR
    print("\n5. HANDLING IndexError")
    print("-" * 40)
    
    def safe_list_access(lst: list, index: int, default=None):
        """Safely access list element."""
        try:
            return lst[index]
        except IndexError:
            print(f"  Error: Index {index} out of range (length {len(lst)})")
            return default
    
    fruits = ["apple", "banana", "cherry"]
    print(f"  safe_list_access(fruits, 1): {safe_list_access(fruits, 1)}")
    print(f"  safe_list_access(fruits, 10): {safe_list_access(fruits, 10)}")
    
    # TYPE ERROR
    print("\n6. HANDLING TypeError")
    print("-" * 40)
    
    def add_numbers(a, b):
        """Add two numbers with type checking."""
        try:
            return a + b
        except TypeError:
            print(f"  Error: Cannot add {type(a).__name__} and {type(b).__name__}")
            return None
    
    print(f"  add_numbers(5, 3): {add_numbers(5, 3)}")
    print(f"  add_numbers('5', 3): {add_numbers('5', 3)}")
    
    # MULTIPLE EXCEPTIONS
    print("\n7. HANDLING MULTIPLE EXCEPTION TYPES")
    print("-" * 40)
    
    def robust_calculator(expression: str) -> Optional[float]:
        """Evaluate expression with multiple error handlers."""
        try:
            result = eval(expression)
            return float(result)
        except ZeroDivisionError:
            print("  Error: Division by zero")
            return None
        except ValueError:
            print("  Error: Invalid value")
            return None
        except SyntaxError:
            print("  Error: Invalid syntax")
            return None
        except Exception as e:
            print(f"  Unexpected error: {type(e).__name__}: {e}")
            return None
    
    print(f"  robust_calculator('10/2'): {robust_calculator('10/2')}")
    print(f"  robust_calculator('10/0'): {robust_calculator('10/0')}")
    print(f"  robust_calculator('10/abc'): {robust_calculator('10/abc')}")
    print(f"  robust_calculator('10//'): {robust_calculator('10//')}")


def demonstrate_else_finally():
    """
    Demonstrates else and finally clauses in exception handling.
    
    - else: Runs if no exception occurred
    - finally: Always runs (cleanup code)
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ELSE AND FINALLY CLAUSES")
    print("=" * 60)
    
    # USING ELSE
    print("\n1. USING ELSE (runs on success)")
    print("-" * 40)
    
    def process_file(filename: str) -> bool:
        """Process file with else clause."""
        try:
            with open(filename, 'r') as f:
                data = f.read()
        except FileNotFoundError:
            print(f"  File not found: {filename}")
            return False
        else:
            # This runs only if no exception occurred
            print(f"  Successfully read {len(data)} bytes from {filename}")
            return True
    
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("Hello, World!")
    
    process_file("test.txt")
    process_file("missing.txt")
    
    # USING FINALLY (always runs)
    print("\n2. USING FINALLY (cleanup code)")
    print("-" * 40)
    
    def divide_with_cleanup(a: float, b: float) -> Optional[float]:
        """Divide with cleanup in finally."""
        print(f"  Attempting to divide {a} by {b}")
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("  Error: Division by zero")
            return None
        finally:
            # This always runs, even if there's a return
            print("  Cleanup: Closing resources (always runs)")
    
    print(f"  Result: {divide_with_cleanup(10, 2)}")
    print(f"  Result: {divide_with_cleanup(10, 0)}")
    
    # RESOURCE CLEANUP WITH FINALLY
    print("\n3. RESOURCE CLEANUP EXAMPLE")
    print("-" * 40)
    
    class DatabaseConnection:
        """Mock database connection."""
        
        def __init__(self, name: str):
            self.name = name
            print(f"  Opening connection to {name}")
        
        def query(self, sql: str) -> list:
            """Execute a query."""
            if "error" in sql.lower():
                raise RuntimeError(f"Query failed: {sql}")
            return [{"id": 1, "name": "Alice"}]
        
        def close(self):
            """Close the connection."""
            print(f"  Closing connection to {self.name}")
    
    def execute_query(db_name: str, sql: str) -> Optional[list]:
        """Execute query with proper cleanup."""
        conn = DatabaseConnection(db_name)
        try:
            result = conn.query(sql)
            return result
        except RuntimeError as e:
            print(f"  Query error: {e}")
            return None
        finally:
            conn.close()
    
    print("\n  Successful query:")
    execute_query("prod_db", "SELECT * FROM users")
    
    print("\n  Failed query:")
    execute_query("prod_db", "SELECT error FROM users")


def demonstrate_raising_exceptions():
    """
    Demonstrates raising custom exceptions.
    
    Use 'raise' to trigger exceptions manually.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: RAISING EXCEPTIONS")
    print("=" * 60)
    
    # CUSTOM EXCEPTION CLASS
    print("\n1. CREATING CUSTOM EXCEPTIONS")
    print("-" * 40)
    
    class ValidationError(Exception):
        """Raised when validation fails."""
        pass
    
    class InsufficientFundsError(Exception):
        """Raised when account has insufficient funds."""
        def __init__(self, balance: float, requested: float):
            self.balance = balance
            self.requested = requested
            super().__init__(f"Insufficient funds: ${balance:.2f} available, ${requested:.2f} requested")
    
    class NegativeAmountError(ValueError):
        """Raised when amount is negative."""
        pass
    
    # USING CUSTOM EXCEPTIONS
    print("\n2. USING CUSTOM EXCEPTIONS")
    print("-" * 40)
    
    def validate_age(age: int) -> None:
        """Validate age with custom exception."""
        if age < 0:
            raise ValidationError(f"Age cannot be negative: {age}")
        if age > 150:
            raise ValidationError(f"Age seems unrealistic: {age}")
        print(f"  Age {age} is valid")
    
    def withdraw(account_balance: float, amount: float) -> float:
        """Withdraw money with custom exception."""
        if amount < 0:
            raise NegativeAmountError(f"Cannot withdraw negative amount: ${amount}")
        
        if amount > account_balance:
            raise InsufficientFundsError(account_balance, amount)
        
        new_balance = account_balance - amount
        print(f"  Withdrew ${amount:.2f}. New balance: ${new_balance:.2f}")
        return new_balance
    
    # Test validation
    print("\n  Testing validation:")
    try:
        validate_age(25)
        validate_age(-5)
    except ValidationError as e:
        print(f"    Caught: {e}")
    
    # Test withdrawal
    print("\n  Testing withdrawal:")
    balance = 100.00
    
    try:
        balance = withdraw(balance, 50.00)
        balance = withdraw(balance, 200.00)
    except NegativeAmountError as e:
        print(f"    Negative amount error: {e}")
    except InsufficientFundsError as e:
        print(f"    Insufficient funds: {e}")
    
    # RAISING WITH TRACEBACK
    print("\n3. RAISING FROM ANOTHER EXCEPTION")
    print("-" * 40)
    
    def process_data(data: dict) -> dict:
        """Process data with chained exceptions."""
        try:
            # Simulate an error
            result = data["value"] / data["divisor"]
            return {"result": result}
        except KeyError as e:
            raise ValidationError(f"Missing required field") from e
        except ZeroDivisionError as e:
            raise ValidationError(f"Division by zero") from e
    
    try:
        process_data({"value": 10})
    except ValidationError as e:
        print(f"  Caught: {e}")
        print(f"  Original cause: {e.__cause__}")


if __name__ == "__main__":
    demonstrate_try_except()
    demonstrate_else_finally()
    demonstrate_raising_exceptions()
```

---

## 🌐 Section 2: Resilient Web Scraper

A complete web scraper that handles network errors, retries failed requests, and continues where it left off.

**SOLID Principles Applied:**
- Single Responsibility: Each function handles one aspect of scraping
- Open/Closed: New error handling strategies can be added

**Design Patterns:**
- Retry Pattern: Automatic retry on failure
- Circuit Breaker Pattern: Stop retrying after too many failures

```python
"""
RESILIENT WEB SCRAPER

This section builds a web scraper that handles errors gracefully.

SOLID Principles Applied:
- Single Responsibility: Each function handles one aspect
- Open/Closed: New error handling strategies can be added

Design Patterns:
- Retry Pattern: Automatic retry on failure
- Circuit Breaker Pattern: Stop retrying after too many failures
"""

import time
import random
import json
from typing import List, Dict, Any, Optional, Callable
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
import hashlib


class ScraperStatus(Enum):
    """Scraper status."""
    OPERATIONAL = "operational"
    DEGRADED = "degraded"
    FAILED = "failed"


class RetryStrategy(Enum):
    """Retry backoff strategies."""
    FIXED = "fixed"
    LINEAR = "linear"
    EXPONENTIAL = "exponential"
    POLYNOMIAL = "polynomial"


@dataclass
class ScrapingResult:
    """Result of scraping a URL."""
    url: str
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    retry_count: int = 0
    duration_ms: float = 0
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict:
        return {
            "url": self.url,
            "success": self.success,
            "data": self.data[:200] + "..." if isinstance(self.data, str) and len(self.data) > 200 else self.data,
            "error": self.error,
            "status_code": self.status_code,
            "retry_count": self.retry_count,
            "duration_ms": self.duration_ms,
            "timestamp": self.timestamp.isoformat()
        }


class CircuitBreaker:
    """
    Circuit breaker to prevent repeated calls to failing services.
    
    Design Pattern: Circuit Breaker Pattern - Stops retrying after failures
    """
    
    def __init__(self, failure_threshold: int = 5, 
                 timeout_seconds: int = 60,
                 half_open_requests: int = 3):
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.half_open_requests = half_open_requests
        
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        self.half_open_successes = 0
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with circuit breaker protection."""
        if self.state == "OPEN":
            if time.time() - self.last_failure_time >= self.timeout_seconds:
                print(f"  Circuit breaker: Moving to HALF_OPEN state")
                self.state = "HALF_OPEN"
                self.half_open_successes = 0
            else:
                raise Exception(f"Circuit breaker is OPEN. Service unavailable.")
        
        try:
            result = func(*args, **kwargs)
            
            if self.state == "HALF_OPEN":
                self.half_open_successes += 1
                if self.half_open_successes >= self.half_open_requests:
                    print(f"  Circuit breaker: Moving to CLOSED state (recovered)")
                    self.state = "CLOSED"
                    self.failure_count = 0
            
            return result
            
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.state == "CLOSED" and self.failure_count >= self.failure_threshold:
                print(f"  Circuit breaker: Moving to OPEN state (after {self.failure_count} failures)")
                self.state = "OPEN"
            elif self.state == "HALF_OPEN":
                print(f"  Circuit breaker: Moving to OPEN state (test failed)")
                self.state = "OPEN"
            
            raise e
    
    def get_status(self) -> Dict:
        """Get circuit breaker status."""
        return {
            "state": self.state,
            "failure_count": self.failure_count,
            "last_failure": datetime.fromtimestamp(self.last_failure_time).isoformat() if self.last_failure_time else None,
            "timeout_remaining": max(0, self.timeout_seconds - (time.time() - self.last_failure_time)) if self.state == "OPEN" else 0
        }


class RetryHandler:
    """
    Handles retries with exponential backoff.
    
    Design Pattern: Retry Pattern - Automatic retry on failure
    """
    
    def __init__(self, max_retries: int = 3, 
                 base_delay: float = 1.0,
                 strategy: RetryStrategy = RetryStrategy.EXPONENTIAL,
                 retry_on_status_codes: List[int] = None,
                 retry_on_exceptions: List[type] = None):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.strategy = strategy
        self.retry_on_status_codes = retry_on_status_codes or [408, 429, 500, 502, 503, 504]
        self.retry_on_exceptions = retry_on_exceptions or [ConnectionError, TimeoutError]
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate delay for a given attempt."""
        if self.strategy == RetryStrategy.FIXED:
            delay = self.base_delay
        elif self.strategy == RetryStrategy.LINEAR:
            delay = self.base_delay * attempt
        elif self.strategy == RetryStrategy.POLYNOMIAL:
            delay = self.base_delay * (attempt ** 2)
        else:  # EXPONENTIAL
            delay = self.base_delay * (2 ** (attempt - 1))
        
        # Add jitter to prevent thundering herd
        jitter = random.uniform(0, delay * 0.1)
        return min(delay + jitter, 60)  # Cap at 60 seconds
    
    def _should_retry(self, attempt: int, exception: Exception = None, 
                      status_code: int = None) -> bool:
        """Determine if another retry should be attempted."""
        if attempt >= self.max_retries:
            return False
        
        if exception:
            for exc_type in self.retry_on_exceptions:
                if isinstance(exception, exc_type):
                    return True
        
        if status_code and status_code in self.retry_on_status_codes:
            return True
        
        return False
    
    def execute(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with retry logic."""
        last_exception = None
        last_status_code = None
        
        for attempt in range(1, self.max_retries + 1):
            try:
                result = func(*args, **kwargs)
                
                # Check if result indicates failure (for HTTP responses)
                if hasattr(result, 'status_code'):
                    if result.status_code >= 400:
                        last_status_code = result.status_code
                        if self._should_retry(attempt, status_code=last_status_code):
                            delay = self._calculate_delay(attempt)
                            print(f"    Retry {attempt}/{self.max_retries} after {delay:.1f}s (status {last_status_code})")
                            time.sleep(delay)
                            continue
                        else:
                            return result
                
                return result
                
            except Exception as e:
                last_exception = e
                if self._should_retry(attempt, exception=e):
                    delay = self._calculate_delay(attempt)
                    print(f"    Retry {attempt}/{self.max_retries} after {delay:.1f}s: {type(e).__name__}")
                    time.sleep(delay)
                else:
                    raise
        
        # All retries exhausted
        if last_exception:
            raise last_exception
        raise Exception(f"Request failed with status {last_status_code}")


class MockHTTPClient:
    """
    Mock HTTP client for demonstration.
    
    Simulates network requests with configurable success rates and delays.
    """
    
    def __init__(self, success_rate: float = 0.8, delay_ms: float = 50):
        self.success_rate = success_rate
        self.delay_ms = delay_ms
        self.call_count = 0
        self.failure_count = 0
    
    def get(self, url: str) -> Any:
        """Simulate HTTP GET request."""
        self.call_count += 1
        time.sleep(self.delay_ms / 1000)
        
        # Create response object
        class Response:
            def __init__(self, status_code, text):
                self.status_code = status_code
                self.text = text
            
            def json(self):
                import json
                return json.loads(self.text)
        
        # Simulate different responses based on URL
        if "/products" in url:
            return Response(200, json.dumps({
                "products": [
                    {"id": 1, "name": "Laptop", "price": 999},
                    {"id": 2, "name": "Mouse", "price": 29}
                ]
            }))
        
        elif "/product/" in url:
            product_id = url.split("/")[-1]
            
            # Simulate random failures
            if random.random() > self.success_rate:
                self.failure_count += 1
                return Response(500, "Internal Server Error")
            
            return Response(200, json.dumps({
                "id": int(product_id),
                "name": f"Product {product_id}",
                "price": random.randint(10, 1000)
            }))
        
        elif "/slow" in url:
            time.sleep(2)
            return Response(200, "Slow response")
        
        else:
            return Response(404, "Not Found")


class ResilientScraper:
    """
    Resilient web scraper with retry and circuit breaker.
    
    Design Pattern: Retry Pattern - Automatic retry on failure
    Design Pattern: Circuit Breaker Pattern - Stop retrying after failures
    """
    
    def __init__(self, client: Optional[MockHTTPClient] = None):
        self.client = client or MockHTTPClient()
        self.retry_handler = RetryHandler(max_retries=3, strategy=RetryStrategy.EXPONENTIAL)
        self.circuit_breaker = CircuitBreaker(failure_threshold=5, timeout_seconds=30)
        self.results: List[ScrapingResult] = []
        self.checkpoint_file = "scraper_checkpoint.json"
    
    def scrape_url(self, url: str) -> ScrapingResult:
        """Scrape a single URL with retry and circuit breaker."""
        start_time = time.time()
        retry_count = 0
        
        def make_request():
            nonlocal retry_count
            retry_count += 1
            return self.client.get(url)
        
        try:
            # Use circuit breaker to protect the service
            response = self.circuit_breaker.call(make_request)
            duration_ms = (time.time() - start_time) * 1000
            
            if response.status_code >= 400:
                result = ScrapingResult(
                    url=url,
                    success=False,
                    error=f"HTTP {response.status_code}",
                    status_code=response.status_code,
                    retry_count=retry_count - 1,
                    duration_ms=duration_ms
                )
            else:
                result = ScrapingResult(
                    url=url,
                    success=True,
                    data=response.json() if hasattr(response, 'json') else response.text,
                    status_code=response.status_code,
                    retry_count=retry_count - 1,
                    duration_ms=duration_ms
                )
        
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            result = ScrapingResult(
                url=url,
                success=False,
                error=str(e),
                retry_count=retry_count - 1,
                duration_ms=duration_ms
            )
        
        self.results.append(result)
        return result
    
    def scrape_batch(self, urls: List[str], checkpoint: bool = True) -> List[ScrapingResult]:
        """Scrape multiple URLs with checkpoint support."""
        results = []
        processed_urls = set()
        
        # Load checkpoint if exists
        if checkpoint:
            processed_urls = self._load_checkpoint()
        
        for i, url in enumerate(urls, 1):
            if url in processed_urls:
                print(f"  Skipping {url} (already processed)")
                continue
            
            print(f"  [{i}/{len(urls)}] Scraping {url}...")
            result = self.scrape_url(url)
            results.append(result)
            
            if result.success:
                print(f"    ✓ Success ({result.duration_ms:.0f}ms)")
            else:
                print(f"    ✗ Failed: {result.error}")
            
            # Save checkpoint
            if checkpoint:
                self._save_checkpoint(url)
            
            # Small delay between requests
            time.sleep(0.1)
        
        return results
    
    def _save_checkpoint(self, url: str) -> None:
        """Save checkpoint of processed URLs."""
        try:
            with open(self.checkpoint_file, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"processed_urls": []}
        
        if url not in data["processed_urls"]:
            data["processed_urls"].append(url)
            data["last_updated"] = datetime.now().isoformat()
        
        with open(self.checkpoint_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _load_checkpoint(self) -> set:
        """Load checkpoint of processed URLs."""
        try:
            with open(self.checkpoint_file, 'r') as f:
                data = json.load(f)
            return set(data.get("processed_urls", []))
        except (FileNotFoundError, json.JSONDecodeError):
            return set()
    
    def get_statistics(self) -> Dict:
        """Get scraping statistics."""
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        failed = total - successful
        
        return {
            "total_requests": total,
            "successful": successful,
            "failed": failed,
            "success_rate": (successful / total * 100) if total > 0 else 0,
            "average_duration_ms": sum(r.duration_ms for r in self.results) / total if total > 0 else 0,
            "circuit_breaker": self.circuit_breaker.get_status(),
            "checkpoint_file": self.checkpoint_file
        }
    
    def generate_report(self) -> str:
        """Generate scraping report."""
        stats = self.get_statistics()
        
        report = []
        report.append("=" * 60)
        report.append("WEB SCRAPING REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        report.append(f"\n📊 STATISTICS:")
        report.append(f"  Total Requests: {stats['total_requests']}")
        report.append(f"  Successful: {stats['successful']}")
        report.append(f"  Failed: {stats['failed']}")
        report.append(f"  Success Rate: {stats['success_rate']:.1f}%")
        report.append(f"  Average Duration: {stats['average_duration_ms']:.0f}ms")
        
        report.append(f"\n🔌 CIRCUIT BREAKER:")
        cb = stats['circuit_breaker']
        report.append(f"  State: {cb['state']}")
        report.append(f"  Failure Count: {cb['failure_count']}")
        if cb['timeout_remaining'] > 0:
            report.append(f"  Timeout Remaining: {cb['timeout_remaining']:.0f}s")
        
        report.append(f"\n❌ FAILED REQUESTS:")
        for r in self.results:
            if not r.success:
                report.append(f"  {r.url}: {r.error}")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)


def demonstrate_web_scraper():
    """
    Demonstrate the resilient web scraper.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: RESILIENT WEB SCRAPER")
    print("=" * 60)
    
    # Create scraper with low success rate to demonstrate retries
    client = MockHTTPClient(success_rate=0.6, delay_ms=20)
    scraper = ResilientScraper(client)
    
    print("\n1. SCRAPING SINGLE URL")
    print("-" * 40)
    
    result = scraper.scrape_url("https://api.example.com/products")
    print(f"  Success: {result.success}")
    if result.success:
        print(f"  Data: {result.data}")
    
    print("\n2. SCRAPING BATCH OF URLS")
    print("-" * 40)
    
    urls = [
        "https://api.example.com/products",
        "https://api.example.com/product/1",
        "https://api.example.com/product/2",
        "https://api.example.com/product/3",
        "https://api.example.com/product/4",
        "https://api.example.com/product/5",
        "https://api.example.com/error",
        "https://api.example.com/slow"
    ]
    
    results = scraper.scrape_batch(urls, checkpoint=False)
    
    print("\n3. SCRAPING STATISTICS")
    print("-" * 40)
    
    stats = scraper.get_statistics()
    for key, value in stats.items():
        if key == "circuit_breaker":
            print(f"  {key}:")
            for k, v in value.items():
                print(f"    {k}: {v}")
        else:
            print(f"  {key}: {value}")
    
    print("\n4. SCRAPING REPORT")
    print("-" * 40)
    
    report = scraper.generate_report()
    print(report)
    
    print("\n5. DEMONSTRATING RETRY LOGIC")
    print("-" * 40)
    
    # Create a client that fails first few times
    class FlakyClient(MockHTTPClient):
        def __init__(self):
            super().__init__(success_rate=1.0)
            self.attempt_count = {}
        
        def get(self, url: str):
            if url not in self.attempt_count:
                self.attempt_count[url] = 0
            self.attempt_count[url] += 1
            
            # Fail first 2 attempts for product/999
            if "/product/999" in url and self.attempt_count[url] <= 2:
                class ErrorResponse:
                    status_code = 500
                    text = "Internal Server Error"
                    def json(self):
                        return {}
                return ErrorResponse()
            
            return super().get(url)
    
    flaky_client = FlakyClient()
    flaky_scraper = ResilientScraper(flaky_client)
    
    result = flaky_scraper.scrape_url("https://api.example.com/product/999")
    print(f"  Final result: {'Success' if result.success else 'Failed'}")
    print(f"  Retry count: {result.retry_count}")
    
    # Clean up checkpoint
    import os
    if os.path.exists("scraper_checkpoint.json"):
        os.remove("scraper_checkpoint.json")
        print("\n  Cleaned up checkpoint file")


if __name__ == "__main__":
    demonstrate_web_scraper()
```

---

## 🔄 Section 3: Transaction System with Rollback

A transaction system that ensures data consistency with rollback on failure.

**SOLID Principles Applied:**
- Single Responsibility: Each operation is a separate transaction
- Open/Closed: New transaction types can be added

**Design Patterns:**
- Command Pattern: Transactions as commands with undo
- Memento Pattern: Save state for rollback

```python
"""
TRANSACTION SYSTEM WITH ROLLBACK

This section builds a transaction system that handles failures gracefully.

SOLID Principles Applied:
- Single Responsibility: Each operation is a separate transaction
- Open/Closed: New transaction types can be added

Design Patterns:
- Command Pattern: Transactions as commands with undo
- Memento Pattern: Save state for rollback
"""

from typing import List, Dict, Any, Optional, Callable, Tuple
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
import copy


class TransactionStatus(Enum):
    """Transaction status."""
    PENDING = "pending"
    COMMITTED = "committed"
    ROLLED_BACK = "rolled_back"
    FAILED = "failed"


@dataclass
class TransactionResult:
    """Result of a transaction."""
    success: bool
    message: str
    data: Any = None
    error: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "error": self.error,
            "timestamp": self.timestamp.isoformat()
        }


class Operation(Enum):
    """Database operations."""
    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"


class Database:
    """
    Simple in-memory database with transaction support.
    
    Design Pattern: Memento Pattern - Save state for rollback
    """
    
    def __init__(self):
        self.tables: Dict[str, Dict[int, Dict]] = {}
        self._initialize_tables()
        self._transaction_log: List[Dict] = []
    
    def _initialize_tables(self):
        """Initialize sample tables."""
        self.tables["users"] = {
            1: {"id": 1, "name": "Alice", "email": "alice@example.com", "balance": 1000},
            2: {"id": 2, "name": "Bob", "email": "bob@example.com", "balance": 500},
            3: {"id": 3, "name": "Charlie", "email": "charlie@example.com", "balance": 200}
        }
        
        self.tables["orders"] = {
            100: {"id": 100, "user_id": 1, "product": "Laptop", "amount": 999, "status": "pending"},
            101: {"id": 101, "user_id": 2, "product": "Mouse", "amount": 29, "status": "pending"}
        }
        
        self.tables["inventory"] = {
            "Laptop": {"product": "Laptop", "quantity": 10},
            "Mouse": {"product": "Mouse", "quantity": 50},
            "Keyboard": {"product": "Keyboard", "quantity": 25}
        }
    
    def get_table(self, table_name: str) -> Dict:
        """Get a table."""
        if table_name not in self.tables:
            raise KeyError(f"Table '{table_name}' does not exist")
        return self.tables[table_name]
    
    def insert(self, table_name: str, record: Dict) -> int:
        """Insert a record and return its ID."""
        table = self.get_table(table_name)
        
        # Generate new ID
        if table:
            new_id = max(table.keys()) + 1
        else:
            new_id = 1
        
        record["id"] = new_id
        table[new_id] = record
        
        self._log_transaction(Operation.INSERT, table_name, new_id, record)
        return new_id
    
    def update(self, table_name: str, record_id: int, updates: Dict) -> bool:
        """Update a record."""
        table = self.get_table(table_name)
        
        if record_id not in table:
            raise KeyError(f"Record {record_id} not found in {table_name}")
        
        # Save old state for potential rollback
        old_record = table[record_id].copy()
        table[record_id].update(updates)
        
        self._log_transaction(Operation.UPDATE, table_name, record_id, {
            "old": old_record,
            "new": table[record_id]
        })
        
        return True
    
    def delete(self, table_name: str, record_id: int) -> bool:
        """Delete a record."""
        table = self.get_table(table_name)
        
        if record_id not in table:
            raise KeyError(f"Record {record_id} not found in {table_name}")
        
        deleted = table.pop(record_id)
        
        self._log_transaction(Operation.DELETE, table_name, record_id, deleted)
        return True
    
    def get(self, table_name: str, record_id: int) -> Optional[Dict]:
        """Get a record by ID."""
        table = self.get_table(table_name)
        return table.get(record_id)
    
    def query(self, table_name: str, predicate: Callable) -> List[Dict]:
        """Query records matching predicate."""
        table = self.get_table(table_name)
        return [record for record in table.values() if predicate(record)]
    
    def _log_transaction(self, operation: Operation, table: str, 
                         record_id: int, data: Any) -> None:
        """Log a transaction for audit."""
        self._transaction_log.append({
            "timestamp": datetime.now().isoformat(),
            "operation": operation.value,
            "table": table,
            "record_id": record_id,
            "data": data
        })
    
    def get_transaction_log(self) -> List[Dict]:
        """Get transaction log."""
        return self._transaction_log.copy()
    
    def get_state(self) -> Dict:
        """Get current database state (for rollback)."""
        return copy.deepcopy(self.tables)
    
    def restore_state(self, state: Dict) -> None:
        """Restore database state (rollback)."""
        self.tables = copy.deepcopy(state)


class Transaction:
    """
    Represents a database transaction.
    
    Design Pattern: Command Pattern - Transaction as command with rollback
    """
    
    def __init__(self, db: Database):
        self.db = db
        self.operations: List[Tuple[str, str, int, Dict]] = []  # (operation, table, id, data)
        self.status = TransactionStatus.PENDING
        self.saved_state: Optional[Dict] = None
    
    def begin(self) -> None:
        """Begin transaction (save current state)."""
        self.saved_state = self.db.get_state()
        print("  Transaction started")
    
    def insert(self, table: str, record: Dict) -> int:
        """Insert a record within transaction."""
        record_id = self.db.insert(table, record)
        self.operations.append(("insert", table, record_id, record))
        return record_id
    
    def update(self, table: str, record_id: int, updates: Dict) -> None:
        """Update a record within transaction."""
        self.db.update(table, record_id, updates)
        self.operations.append(("update", table, record_id, updates))
    
    def delete(self, table: str, record_id: int) -> None:
        """Delete a record within transaction."""
        self.db.delete(table, record_id)
        self.operations.append(("delete", table, record_id, None))
    
    def commit(self) -> TransactionResult:
        """Commit the transaction."""
        try:
            # All operations already applied
            self.status = TransactionStatus.COMMITTED
            self.saved_state = None
            print(f"  Transaction committed ({len(self.operations)} operations)")
            return TransactionResult(True, "Transaction committed successfully", 
                                    {"operations": len(self.operations)})
        except Exception as e:
            return self.rollback(e)
    
    def rollback(self, error: Optional[Exception] = None) -> TransactionResult:
        """Rollback the transaction."""
        if self.saved_state:
            self.db.restore_state(self.saved_state)
            self.status = TransactionStatus.ROLLED_BACK
            error_msg = str(error) if error else "Manual rollback"
            print(f"  Transaction rolled back: {error_msg}")
            return TransactionResult(False, "Transaction rolled back", 
                                    error=error_msg)
        
        self.status = TransactionStatus.FAILED
        return TransactionResult(False, "Rollback failed - no saved state",
                                error="No saved state to restore")


class BankService:
    """
    Bank service with transaction support.
    
    Demonstrates using transactions for money transfers.
    """
    
    def __init__(self, db: Database):
        self.db = db
    
    def transfer_money(self, from_user_id: int, to_user_id: int, 
                       amount: float) -> TransactionResult:
        """Transfer money between accounts (transactional)."""
        tx = Transaction(self.db)
        
        try:
            tx.begin()
            
            # Get users
            from_user = self.db.get("users", from_user_id)
            to_user = self.db.get("users", to_user_id)
            
            if not from_user:
                raise ValueError(f"User {from_user_id} not found")
            if not to_user:
                raise ValueError(f"User {to_user_id} not found")
            
            # Check balance
            if from_user["balance"] < amount:
                raise ValueError(f"Insufficient funds: ${from_user['balance']:.2f}")
            
            # Perform transfer
            tx.update("users", from_user_id, {"balance": from_user["balance"] - amount})
            tx.update("users", to_user_id, {"balance": to_user["balance"] + amount})
            
            # Record transaction
            tx.insert("transactions", {
                "from_user": from_user_id,
                "to_user": to_user_id,
                "amount": amount,
                "timestamp": datetime.now().isoformat()
            })
            
            return tx.commit()
            
        except Exception as e:
            return tx.rollback(e)
    
    def place_order(self, user_id: int, product: str, quantity: int) -> TransactionResult:
        """Place an order (transactional)."""
        tx = Transaction(self.db)
        
        try:
            tx.begin()
            
            # Get user
            user = self.db.get("users", user_id)
            if not user:
                raise ValueError(f"User {user_id} not found")
            
            # Get product price (mock)
            product_prices = {"Laptop": 999, "Mouse": 29, "Keyboard": 89}
            price = product_prices.get(product)
            if not price:
                raise ValueError(f"Product {product} not found")
            
            total = price * quantity
            
            # Check inventory
            inventory = self.db.get("inventory", product)
            if not inventory or inventory["quantity"] < quantity:
                raise ValueError(f"Insufficient inventory for {product}")
            
            # Check balance
            if user["balance"] < total:
                raise ValueError(f"Insufficient funds: need ${total:.2f}, have ${user['balance']:.2f}")
            
            # Update balance
            tx.update("users", user_id, {"balance": user["balance"] - total})
            
            # Update inventory
            tx.update("inventory", product, {"quantity": inventory["quantity"] - quantity})
            
            # Create order
            order_id = tx.insert("orders", {
                "user_id": user_id,
                "product": product,
                "quantity": quantity,
                "amount": total,
                "status": "completed",
                "created_at": datetime.now().isoformat()
            })
            
            return tx.commit()
            
        except Exception as e:
            return tx.rollback(e)


def demonstrate_transaction_system():
    """
    Demonstrate the transaction system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: TRANSACTION SYSTEM WITH ROLLBACK")
    print("=" * 60)
    
    db = Database()
    bank = BankService(db)
    
    print("\n1. INITIAL DATABASE STATE")
    print("-" * 40)
    
    for user_id in [1, 2, 3]:
        user = db.get("users", user_id)
        print(f"  User {user_id}: {user['name']} - ${user['balance']:.2f}")
    
    print("\n2. SUCCESSFUL TRANSFER")
    print("-" * 40)
    
    result = bank.transfer_money(1, 2, 100.00)
    print(f"  Result: {result.message}")
    
    print("\n  Updated balances:")
    for user_id in [1, 2]:
        user = db.get("users", user_id)
        print(f"    User {user_id}: ${user['balance']:.2f}")
    
    print("\n3. FAILED TRANSFER (Insufficient funds)")
    print("-" * 40)
    
    result = bank.transfer_money(3, 1, 500.00)
    print(f"  Result: {result.message}")
    if result.error:
        print(f"  Error: {result.error}")
    
    print("\n  Balances unchanged:")
    for user_id in [1, 2, 3]:
        user = db.get("users", user_id)
        print(f"    User {user_id}: ${user['balance']:.2f}")
    
    print("\n4. PLACE ORDER (Successful)")
    print("-" * 40)
    
    result = bank.place_order(1, "Laptop", 1)
    print(f"  Result: {result.message}")
    
    # Show inventory
    inventory = db.get("inventory", "Laptop")
    print(f"  Laptop inventory: {inventory['quantity']}")
    
    user = db.get("users", 1)
    print(f"  User 1 balance: ${user['balance']:.2f}")
    
    print("\n5. PLACE ORDER (Failed - insufficient inventory)")
    print("-" * 40)
    
    result = bank.place_order(2, "Laptop", 20)
    print(f"  Result: {result.message}")
    
    # Show no changes
    inventory = db.get("inventory", "Laptop")
    print(f"  Laptop inventory unchanged: {inventory['quantity']}")
    
    print("\n6. TRANSACTION LOG")
    print("-" * 40)
    
    log = db.get_transaction_log()
    print(f"  Total transactions: {len(log)}")
    for entry in log[-5:]:
        print(f"    {entry['timestamp'][:19]} - {entry['operation']} - {entry['table']}")


if __name__ == "__main__":
    demonstrate_transaction_system()
```

---

## 📊 Section 4: Application with Comprehensive Error Handling

A complete application demonstrating comprehensive error handling, logging, and recovery.

**SOLID Principles Applied:**
- Single Responsibility: Each error handler has one purpose
- Dependency Inversion: Depends on logging abstraction

**Design Patterns:**
- Observer Pattern: Error handlers observe exceptions
- Chain of Responsibility: Multiple error handlers

```python
"""
APPLICATION WITH COMPREHENSIVE ERROR HANDLING

This section builds a complete application with error handling.

SOLID Principles Applied:
- Single Responsibility: Each error handler has one purpose
- Dependency Inversion: Depends on logging abstraction

Design Patterns:
- Observer Pattern: Error handlers observe exceptions
- Chain of Responsibility: Multiple error handlers
"""

import sys
import logging
import traceback
from typing import Dict, Any, Optional, Callable
from datetime import datetime
from enum import Enum
import json
import os


class ErrorSeverity(Enum):
    """Error severity levels."""
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class ApplicationError(Exception):
    """Base application exception."""
    
    def __init__(self, message: str, code: str = "APP_ERROR", 
                 severity: ErrorSeverity = ErrorSeverity.ERROR,
                 details: Optional[Dict] = None):
        super().__init__(message)
        self.code = code
        self.severity = severity
        self.details = details or {}
        self.timestamp = datetime.now()


class ConfigurationError(ApplicationError):
    """Configuration related errors."""
    pass


class DataValidationError(ApplicationError):
    """Data validation errors."""
    pass


class ServiceUnavailableError(ApplicationError):
    """Service unavailable errors."""
    pass


class ErrorHandler:
    """
    Centralized error handler with multiple strategies.
    
    Design Pattern: Chain of Responsibility - Multiple handlers
    """
    
    def __init__(self):
        self.handlers: List[Callable] = []
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('application.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def register_handler(self, handler: Callable) -> None:
        """Register an error handler."""
        self.handlers.append(handler)
    
    def handle(self, error: Exception, context: Optional[Dict] = None) -> Dict:
        """Handle an exception."""
        context = context or {}
        
        # Convert to ApplicationError if needed
        if not isinstance(error, ApplicationError):
            error = ApplicationError(
                str(error),
                code="UNKNOWN_ERROR",
                severity=ErrorSeverity.ERROR,
                details={"original_type": type(error).__name__}
            )
        
        # Log the error
        self._log_error(error, context)
        
        # Run registered handlers
        for handler in self.handlers:
            try:
                handler(error, context)
            except Exception as e:
                self.logger.error(f"Error handler failed: {e}")
        
        # Return error response
        return {
            "success": False,
            "error": {
                "code": error.code,
                "message": str(error),
                "severity": error.severity.value,
                "timestamp": error.timestamp.isoformat(),
                "details": error.details
            }
        }
    
    def _log_error(self, error: ApplicationError, context: Dict) -> None:
        """Log the error with appropriate level."""
        log_message = f"[{error.code}] {error}"
        if context:
            log_message += f" | Context: {json.dumps(context, default=str)}"
        
        if error.severity == ErrorSeverity.DEBUG:
            self.logger.debug(log_message)
        elif error.severity == ErrorSeverity.INFO:
            self.logger.info(log_message)
        elif error.severity == ErrorSeverity.WARNING:
            self.logger.warning(log_message)
        elif error.severity == ErrorSeverity.CRITICAL:
            self.logger.critical(log_message)
        else:
            self.logger.error(log_message)
        
        # Log traceback for critical errors
        if error.severity == ErrorSeverity.CRITICAL:
            self.logger.error(traceback.format_exc())


class DataProcessor:
    """
    Data processor with comprehensive error handling.
    """
    
    def __init__(self, error_handler: ErrorHandler):
        self.error_handler = error_handler
        self.processing_stats = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "errors": []
        }
    
    def validate_record(self, record: Dict) -> None:
        """Validate a data record."""
        required_fields = ["id", "name", "email", "age"]
        
        for field in required_fields:
            if field not in record:
                raise DataValidationError(
                    f"Missing required field: {field}",
                    code="MISSING_FIELD",
                    details={"field": field, "record": record}
                )
        
        if not isinstance(record["age"], (int, float)) or record["age"] < 0 or record["age"] > 150:
            raise DataValidationError(
                f"Invalid age: {record.get('age')}",
                code="INVALID_AGE",
                details={"age": record.get('age')}
            )
        
        if "@" not in record["email"]:
            raise DataValidationError(
                f"Invalid email: {record.get('email')}",
                code="INVALID_EMAIL",
                details={"email": record.get('email')}
            )
    
    def process_record(self, record: Dict) -> Dict:
        """Process a single record."""
        # Validate
        self.validate_record(record)
        
        # Transform
        processed = {
            "id": record["id"],
            "name": record["name"].strip().title(),
            "email": record["email"].lower().strip(),
            "age": int(record["age"]),
            "processed_at": datetime.now().isoformat()
        }
        
        # Add derived fields
        processed["age_group"] = (
            "senior" if processed["age"] >= 65 else
            "adult" if processed["age"] >= 18 else
            "minor"
        )
        
        return processed
    
    def process_batch(self, records: List[Dict]) -> List[Dict]:
        """Process a batch of records with error handling."""
        results = []
        
        for record in records:
            try:
                result = self.process_record(record)
                results.append(result)
                self.processing_stats["successful"] += 1
                
            except DataValidationError as e:
                self.processing_stats["failed"] += 1
                self.processing_stats["errors"].append({
                    "record": record,
                    "error": str(e),
                    "code": e.code
                })
                self.error_handler.handle(e, {"record": record})
                
            except Exception as e:
                self.processing_stats["failed"] += 1
                self.processing_stats["errors"].append({
                    "record": record,
                    "error": str(e)
                })
                self.error_handler.handle(e, {"record": record})
            
            finally:
                self.processing_stats["total_processed"] += 1
        
        return results
    
    def get_statistics(self) -> Dict:
        """Get processing statistics."""
        return {
            **self.processing_stats,
            "success_rate": (self.processing_stats["successful"] / 
                           max(self.processing_stats["total_processed"], 1)) * 100
        }


class ConfigManager:
    """Configuration manager with error handling."""
    
    def __init__(self, error_handler: ErrorHandler):
        self.error_handler = error_handler
        self.config = {}
    
    def load_from_file(self, filepath: str) -> bool:
        """Load configuration from file with error handling."""
        try:
            if not os.path.exists(filepath):
                raise ConfigurationError(
                    f"Config file not found: {filepath}",
                    code="CONFIG_NOT_FOUND",
                    severity=ErrorSeverity.CRITICAL
                )
            
            with open(filepath, 'r') as f:
                self.config = json.load(f)
            
            return True
            
        except json.JSONDecodeError as e:
            self.error_handler.handle(
                ConfigurationError(
                    f"Invalid JSON in config file: {e}",
                    code="CONFIG_INVALID_JSON",
                    severity=ErrorSeverity.ERROR,
                    details={"file": filepath, "error": str(e)}
                )
            )
            return False
        
        except Exception as e:
            self.error_handler.handle(e)
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        try:
            return self.config.get(key, default)
        except Exception as e:
            self.error_handler.handle(e)
            return default


class Application:
    """
    Complete application with comprehensive error handling.
    
    Design Pattern: Observer Pattern - Error handlers observe exceptions
    """
    
    def __init__(self):
        self.error_handler = ErrorHandler()
        self.processor = DataProcessor(self.error_handler)
        self.config = ConfigManager(self.error_handler)
        
        # Register custom error handlers
        self.error_handler.register_handler(self._email_on_critical_error)
        self.error_handler.register_handler(self._save_error_snapshot)
    
    def _email_on_critical_error(self, error: ApplicationError, context: Dict) -> None:
        """Send email on critical errors (simulated)."""
        if error.severity == ErrorSeverity.CRITICAL:
            print(f"  [SIMULATED] Sending critical error alert: {error.code} - {error}")
    
    def _save_error_snapshot(self, error: ApplicationError, context: Dict) -> None:
        """Save error snapshot to file."""
        snapshot = {
            "timestamp": datetime.now().isoformat(),
            "error": {
                "code": error.code,
                "message": str(error),
                "severity": error.severity.value,
                "details": error.details
            },
            "context": context
        }
        
        with open("error_snapshot.json", "w") as f:
            json.dump(snapshot, f, indent=2, default=str)
    
    def run(self) -> None:
        """Run the application."""
        print("\n" + "=" * 60)
        print("APPLICATION WITH ERROR HANDLING")
        print("=" * 60)
        
        # Load configuration
        print("\n1. LOADING CONFIGURATION")
        print("-" * 40)
        
        # Create config file
        with open("app_config.json", "w") as f:
            json.dump({
                "app_name": "Data Processor",
                "version": "1.0",
                "max_batch_size": 100
            }, f)
        
        if self.config.load_from_file("app_config.json"):
            print(f"  App name: {self.config.get('app_name')}")
            print(f"  Version: {self.config.get('version')}")
        
        # Process data
        print("\n2. PROCESSING DATA")
        print("-" * 40)
        
        sample_data = [
            {"id": 1, "name": "  alice  ", "email": "ALICE@EXAMPLE.COM", "age": 28},
            {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 35},
            {"id": 3, "name": "Charlie", "email": "invalid-email", "age": 22},
            {"id": 4, "name": "Diana", "email": "diana@example.com", "age": -5},
            {"id": 5, "name": "Eve", "email": "eve@example.com", "age": 200},
            {"id": 6, "name": "Frank", "email": "frank@example.com", "age": 42},
            {"id": 7, "name": "", "email": "grace@example.com", "age": 30},
            {"id": 8, "name": "Henry", "email": "henry@example.com", "age": 25},
        ]
        
        results = self.processor.process_batch(sample_data)
        
        print(f"\n  Processed {len(results)} records successfully")
        for record in results[:3]:
            print(f"    {record['id']}: {record['name']} ({record['age_group']})")
        
        # Show statistics
        print("\n3. PROCESSING STATISTICS")
        print("-" * 40)
        
        stats = self.processor.get_statistics()
        for key, value in stats.items():
            if key == "errors":
                print(f"  {key}: {len(value)} errors")
                for error in value[:3]:
                    print(f"    - {error['error']}")
            elif isinstance(value, float):
                print(f"  {key}: {value:.1f}")
            else:
                print(f"  {key}: {value}")
        
        # Error snapshot
        print("\n4. ERROR SNAPSHOT")
        print("-" * 40)
        
        if os.path.exists("error_snapshot.json"):
            with open("error_snapshot.json", "r") as f:
                snapshot = json.load(f)
            print(f"  Last error snapshot: {snapshot['timestamp']}")
            print(f"  Error code: {snapshot['error']['code']}")
        
        # Clean up
        for f in ["app_config.json", "error_snapshot.json", "application.log"]:
            if os.path.exists(f):
                os.remove(f)
        print("\n  Cleaned up files")


if __name__ == "__main__":
    app = Application()
    app.run()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Try-Except Blocks** – Catch and handle exceptions. Prevent crashes. Multiple except blocks for different error types.

- **Else Clause** – Runs only if no exception occurred. For code that should execute on success.

- **Finally Clause** – Always runs, even with return statements. For cleanup code (close files, release connections).

- **Raising Exceptions** – `raise` to trigger exceptions. Create custom exception classes for domain-specific errors.

- **Exception Chaining** – `raise NewError from original_error` preserves the cause chain.

- **Retry Pattern** – Automatic retry with exponential backoff. Circuit breaker to stop retrying after failures.

- **Transaction Pattern** – Begin, commit, rollback. Save state before operations, restore on failure.

- **Error Handler** – Centralized error handling. Multiple handlers for different severity levels.

- **SOLID Principles Applied** – Single Responsibility (each handler handles one error type), Open/Closed (new handlers can be added), Dependency Inversion (depends on abstractions), Interface Segregation (clean handler interfaces).

- **Design Patterns Used** – Retry Pattern (automatic retries), Circuit Breaker Pattern (stop after failures), Command Pattern (transactions with undo), Memento Pattern (state save/restore), Observer Pattern (error handlers), Chain of Responsibility (multiple handlers).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: CSV & JSON Processing – Structured Data

- **📚 Series E Catalog:** File & Data Handling Line – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Context Managers – The with Statement (Series E, Story 4)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 3 | 2 | 60% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **32** | **20** | **62%** |

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

**Next Story:** Series E, Story 4: The 2026 Python Metromap: Context Managers – The with Statement

---

## 📝 Your Invitation

You've mastered exception handling. Now build something with what you've learned:

1. **Build a resilient API client** – Add retry logic, circuit breaker, and timeout handling.

2. **Create a data validation pipeline** – Validate data, collect errors, generate reports.

3. **Build a transaction manager** – Support nested transactions, savepoints, two-phase commit.

4. **Create an error monitoring system** – Collect errors, send alerts, aggregate statistics.

5. **Build a fallback mechanism** – When primary service fails, use cached data or alternative service.

**You've mastered exception handling. Next stop: Context Managers!**

---

*Found this helpful? Clap, comment, and share what you built with exception handling. Next stop: Context Managers!* 🚇