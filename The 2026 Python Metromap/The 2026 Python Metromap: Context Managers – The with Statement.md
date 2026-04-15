# The 2026 Python Metromap: Context Managers – The with Statement

## Series E: File & Data Handling Line | Story 4 of 5

![The 2026 Python Metromap/images/Context Managers – The with Statement](images/Context Managers – The with Statement.png)

## 📖 Introduction

**Welcome to the fourth stop on the File & Data Handling Line.**

You've mastered file I/O, CSV/JSON processing, and exception handling. You know how to read files, parse data, and handle errors gracefully. But there's a pattern you've been using without fully understanding: the `with` statement. Every time you open a file with `with open(...) as f`, you're using a context manager.

Context managers are Python's elegant solution for resource management. They guarantee that resources are properly acquired and released, even when exceptions occur. Files are closed, database connections are released, locks are unlocked—automatically and reliably. The `with` statement provides a clean, readable syntax for this pattern.

This story—**The 2026 Python Metromap: Context Managers – The with Statement**—is your guide to mastering context managers in Python. We'll explore the built-in context managers for files, locks, and temporary directories. We'll learn to create our own context managers using classes and the `contextlib` module. We'll build a database connection pool with automatic cleanup. We'll create a timing context manager for performance measurement. We'll implement a transaction context manager for database operations. And we'll build a complete resource management system.

**Let's manage contexts.**

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

- ⚠️ **The 2026 Python Metromap: Exception Handling – Graceful Failures** – Resilient web scraper; network error handling; request retries.

- 🔧 **The 2026 Python Metromap: Context Managers – The with Statement** – Database connection pool; automatic resource cleanup. **⬅️ YOU ARE HERE**

- 🗺️ **The 2026 Python Metromap: Working with Paths & Directories** – Automated backup system; file organization by date; log rotation. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔧 Section 1: Context Manager Basics – The with Statement

The `with` statement provides a clean way to manage resources by automatically calling setup and cleanup code.

**SOLID Principle Applied: Single Responsibility** – Context managers handle resource acquisition and release.

**Design Pattern: RAII (Resource Acquisition Is Initialization)** – Resources are acquired in initialization and released in finalization.

```python
"""
CONTEXT MANAGER BASICS: THE WITH STATEMENT

This section covers the fundamentals of context managers.

SOLID Principle: Single Responsibility
- Context managers handle resource acquisition and release

Design Pattern: RAII (Resource Acquisition Is Initialization)
- Resources acquired in initialization, released in finalization
"""

import time
import threading
from typing import Any, Optional


def demonstrate_file_context_manager():
    """
    Demonstrates using the built-in file context manager.
    
    The with statement ensures files are closed even if exceptions occur.
    """
    print("=" * 60)
    print("SECTION 1A: FILE CONTEXT MANAGER")
    print("=" * 60)
    
    # WITHOUT CONTEXT MANAGER (Manual cleanup)
    print("\n1. WITHOUT CONTEXT MANAGER (Error-prone)")
    print("-" * 40)
    
    f = None
    try:
        f = open("manual.txt", "w")
        f.write("Hello, World!")
        # What if exception occurs here? File might not be closed!
    finally:
        if f:
            f.close()
    print("  Manual file handling with try-finally")
    
    # WITH CONTEXT MANAGER (Automatic cleanup)
    print("\n2. WITH CONTEXT MANAGER (Clean and safe)")
    print("-" * 40)
    
    with open("auto.txt", "w") as f:
        f.write("Hello, World!")
        # File automatically closed when block exits
    print("  File automatically closed")
    
    # MULTIPLE FILES
    print("\n3. MANAGING MULTIPLE FILES")
    print("-" * 40)
    
    with open("source.txt", "w") as src, open("dest.txt", "w") as dst:
        src.write("Source content")
        dst.write("Destination content")
    print("  Both files managed in one with statement")
    
    # READING FILES
    print("\n4. READING FILES WITH CONTEXT MANAGER")
    print("-" * 40)
    
    with open("source.txt", "r") as f:
        content = f.read()
    print(f"  File content: {content}")
    
    # EXCEPTION HANDLING
    print("\n5. EXCEPTION HANDLING WITH CONTEXT MANAGER")
    print("-" * 40)
    
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"  Caught exception: {e}")
        print("  File was never opened, so nothing to close")
    
    # Clean up
    import os
    for f in ["manual.txt", "auto.txt", "source.txt", "dest.txt"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up test files")


def demonstrate_lock_context_manager():
    """
    Demonstrates using threading locks with context manager.
    
    The lock context manager ensures locks are always released.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: LOCK CONTEXT MANAGER")
    print("=" * 60)
    
    # WITHOUT CONTEXT MANAGER
    print("\n1. WITHOUT CONTEXT MANAGER (Manual lock management)")
    print("-" * 40)
    
    lock = threading.Lock()
    shared_counter = 0
    
    def increment_manual():
        global shared_counter
        lock.acquire()
        try:
            # Critical section
            local = shared_counter
            time.sleep(0.001)  # Simulate work
            shared_counter = local + 1
        finally:
            lock.release()  # Must remember to release!
    
    print("  Manual lock with try-finally (error-prone)")
    
    # WITH CONTEXT MANAGER
    print("\n2. WITH CONTEXT MANAGER (Automatic lock management)")
    print("-" * 40)
    
    shared_counter = 0
    
    def increment_auto():
        global shared_counter
        with lock:  # Automatically acquires and releases
            local = shared_counter
            time.sleep(0.001)
            shared_counter = local + 1
    
    # Run increments
    threads = []
    for _ in range(10):
        t = threading.Thread(target=increment_auto)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"  Final counter: {shared_counter} (expected 10)")
    
    # RLOCK (Reentrant Lock)
    print("\n3. REENTRANT LOCK (RLock)")
    print("-" * 40)
    
    rlock = threading.RLock()
    
    def recursive_function(n: int):
        with rlock:
            if n > 0:
                recursive_function(n - 1)
    
    recursive_function(5)
    print("  RLock allows same thread to acquire lock multiple times")


def demonstrate_other_builtin_context_managers():
    """
    Demonstrates other built-in context managers.
    
    - decimal.localcontext: Temporary decimal precision
    - redirect_stdout: Redirect print output
    - TemporaryDirectory: Automatic cleanup
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: OTHER BUILT-IN CONTEXT MANAGERS")
    print("=" * 60)
    
    # DECIMAL CONTEXT
    print("\n1. DECIMAL CONTEXT (temporary precision)")
    print("-" * 40)
    
    from decimal import Decimal, localcontext
    
    with localcontext() as ctx:
        ctx.prec = 3  # 3-digit precision
        result = Decimal('1') / Decimal('7')
        print(f"  With precision 3: {result}")
    
    # Outside context, precision returns to default
    result = Decimal('1') / Decimal('7')
    print(f"  Default precision: {result}")
    
    # REDIRECT STDOUT
    print("\n2. REDIRECT STDOUT (capture print output)")
    print("-" * 40)
    
    from io import StringIO
    import sys
    
    captured_output = StringIO()
    
    with redirect_stdout(captured_output):
        print("This goes to captured output")
        print("This also goes to captured output")
    
    print(f"  Captured output: {captured_output.getvalue().strip()}")
    
    # TEMPORARY DIRECTORY
    print("\n3. TEMPORARY DIRECTORY (auto-cleanup)")
    print("-" * 40)
    
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"  Created temp directory: {tmpdir}")
        # Directory automatically deleted after block
    print("  Temp directory automatically deleted")
    
    # SUPPRESS EXCEPTIONS
    print("\n4. SUPPRESS EXCEPTIONS (ignore specific exceptions)")
    print("-" * 40)
    
    from contextlib import suppress
    
    with suppress(FileNotFoundError):
        open("nonexistent.txt", "r")
        print("  This line is not executed")
    print("  Exception was suppressed, program continues")
    
    # NULL CONTEXT MANAGER (do nothing)
    print("\n5. NULL CONTEXT MANAGER (conditional execution)")
    print("-" * 40)
    
    from contextlib import nullcontext
    
    debug_mode = False
    with (open("debug.log", "w") if debug_mode else nullcontext()) as f:
        # If debug_mode, f is file; otherwise, f is None
        if f:
            f.write("Debug information")
    print("  nullcontext used for conditional context managers")


def demonstrate_context_manager_without_with():
    """
    Demonstrates manual context manager usage.
    
    Context managers can be used manually, but with is preferred.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: MANUAL CONTEXT MANAGER USAGE")
    print("=" * 60)
    
    # Manual context manager usage (for rare cases)
    print("\n1. MANUAL CONTEXT MANAGER (without 'with')")
    print("-" * 40)
    
    f = open("manual_context.txt", "w")
    print(f"  File opened: {f}")
    
    # Use the file
    f.write("Content")
    
    # Manually close
    f.close()
    print("  File manually closed")
    
    # Manual context manager with __enter__ and __exit__
    print("\n2. MANUAL __enter__ AND __exit__ CALLS")
    print("-" * 40)
    
    f = open("manual_enter_exit.txt", "w")
    f.__enter__()  # Acquire resource
    try:
        f.write("Content")
    finally:
        f.__exit__(None, None, None)  # Release resource
    print("  Manually called __enter__ and __exit__")
    
    # Clean up
    import os
    for f in ["manual_context.txt", "manual_enter_exit.txt"]:
        if os.path.exists(f):
            os.remove(f)


def redirect_stdout(target):
    """Helper for stdout redirection (simplified)."""
    import sys
    from contextlib import contextmanager
    
    @contextmanager
    def stdout_redirector(stream):
        old_stdout = sys.stdout
        sys.stdout = stream
        try:
            yield
        finally:
            sys.stdout = old_stdout
    
    return stdout_redirector(target)


if __name__ == "__main__":
    demonstrate_file_context_manager()
    demonstrate_lock_context_manager()
    demonstrate_other_builtin_context_managers()
    demonstrate_context_manager_without_with()
```

---

## 🔧 Section 2: Creating Custom Context Managers

You can create your own context managers using classes (with `__enter__` and `__exit__`) or the `@contextmanager` decorator.

**SOLID Principles Applied:**
- Single Responsibility: Each context manager handles one resource type
- Open/Closed: New context managers can be created without modifying existing code

**Design Patterns:**
- Factory Pattern: `@contextmanager` creates context managers
- Template Method Pattern: `__enter__` and `__exit__` define the template

```python
"""
CREATING CUSTOM CONTEXT MANAGERS

This section covers creating custom context managers.

SOLID Principles Applied:
- Single Responsibility: Each context manager handles one resource type
- Open/Closed: New context managers can be created

Design Patterns:
- Factory Pattern: @contextmanager creates context managers
- Template Method Pattern: __enter__ and __exit__ define the template
"""

import time
from contextlib import contextmanager
from typing import Any, Optional, Generator


def demonstrate_class_based_context_manager():
    """
    Demonstrates creating context managers using classes.
    
    Class-based context managers implement __enter__ and __exit__ methods.
    """
    print("=" * 60)
    print("SECTION 2A: CLASS-BASED CONTEXT MANAGERS")
    print("=" * 60)
    
    # SIMPLE TIMER CONTEXT MANAGER
    print("\n1. TIMER CONTEXT MANAGER")
    print("-" * 40)
    
    class Timer:
        """Context manager for measuring execution time."""
        
        def __enter__(self):
            self.start = time.time()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.time()
            self.duration = self.end - self.start
            print(f"  Duration: {self.duration:.4f} seconds")
            # Return False to propagate exceptions
            return False
        
        def elapsed(self):
            """Get elapsed time without exiting."""
            return time.time() - self.start
    
    # Use the timer
    with Timer() as timer:
        time.sleep(0.5)
        print(f"  Elapsed inside: {timer.elapsed():.3f}s")
    
    # FILE CONTEXT MANAGER (custom)
    print("\n2. CUSTOM FILE CONTEXT MANAGER")
    print("-" * 40)
    
    class ManagedFile:
        """Custom file context manager."""
        
        def __init__(self, filename: str, mode: str = 'r'):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
            # Log if exception occurred
            if exc_type:
                print(f"  Exception: {exc_type.__name__}: {exc_val}")
            return False  # Propagate exception
    
    with ManagedFile("test.txt", "w") as f:
        f.write("Hello, Context Manager!")
    print("  File written and closed automatically")
    
    # CONNECTION CONTEXT MANAGER
    print("\n3. DATABASE CONNECTION CONTEXT MANAGER")
    print("-" * 40)
    
    class DatabaseConnection:
        """Mock database connection with context manager."""
        
        def __init__(self, connection_string: str):
            self.connection_string = connection_string
            self.connected = False
        
        def __enter__(self):
            print(f"  Connecting to {self.connection_string}...")
            self.connected = True
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"  Disconnecting from {self.connection_string}...")
            self.connected = False
            if exc_type:
                print(f"  Exception during transaction: {exc_val}")
                # Rollback would happen here
            return False
        
        def query(self, sql: str) -> list:
            """Execute a query."""
            if not self.connected:
                raise RuntimeError("Not connected to database")
            print(f"  Executing: {sql}")
            return [{"id": 1, "name": "Alice"}]
    
    with DatabaseConnection("postgresql://localhost/mydb") as db:
        results = db.query("SELECT * FROM users")
        print(f"  Query results: {results}")
    
    # CONTEXT MANAGER THAT SUPPRESSES EXCEPTIONS
    print("\n4. EXCEPTION SUPPRESSING CONTEXT MANAGER")
    print("-" * 40)
    
    class Suppressor:
        """Context manager that suppresses specified exceptions."""
        
        def __init__(self, *exceptions):
            self.exceptions = exceptions
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type and issubclass(exc_type, self.exceptions):
                print(f"  Suppressed: {exc_type.__name__}: {exc_val}")
                return True  # Exception handled
            return False
    
    with Suppressor(ValueError, TypeError):
        int("not a number")
        print("  This line is not executed")
    print("  ValueError was suppressed")
    
    # CONTEXT MANAGER WITH STATE
    print("\n5. CONTEXT MANAGER WITH STATE TRACKING")
    print("-" * 40)
    
    class Indenter:
        """Context manager for indented printing."""
        
        def __init__(self):
            self.level = 0
        
        def __enter__(self):
            self.level += 1
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.level -= 1
            return False
        
        def print(self, message: str):
            """Print with current indentation."""
            print("  " * self.level + message)
    
    with Indenter() as indent:
        indent.print("Level 1")
        with indent:
            indent.print("Level 2")
            with indent:
                indent.print("Level 3")
        indent.print("Back to level 1")


def demonstrate_decorator_based_context_manager():
    """
    Demonstrates creating context managers using the @contextmanager decorator.
    
    The @contextmanager decorator turns a generator function into a context manager.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: DECORATOR-BASED CONTEXT MANAGERS")
    print("=" * 60)
    
    # TIMER USING DECORATOR
    print("\n1. TIMER CONTEXT MANAGER (decorator style)")
    print("-" * 40)
    
    @contextmanager
    def timer(name: str = "Operation"):
        """Context manager for timing operations."""
        print(f"  Starting {name}...")
        start = time.time()
        try:
            yield
        finally:
            duration = time.time() - start
            print(f"  {name} completed in {duration:.3f}s")
    
    with timer("Data Processing"):
        time.sleep(0.5)
    
    # TEMPORARY ATTRIBUTE CONTEXT MANAGER
    print("\n2. TEMPORARY ATTRIBUTE CONTEXT MANAGER")
    print("-" * 40)
    
    @contextmanager
    def temporary_attribute(obj, name: str, value: Any):
        """Temporarily set an attribute."""
        old_value = getattr(obj, name, None)
        setattr(obj, name, value)
        try:
            yield
        finally:
            if old_value is not None:
                setattr(obj, name, old_value)
            else:
                delattr(obj, name)
    
    class Config:
        debug = False
    
    config = Config()
    print(f"  Initial debug: {config.debug}")
    
    with temporary_attribute(config, "debug", True):
        print(f"  Inside context: {config.debug}")
    
    print(f"  After context: {config.debug}")
    
    # TEMPORARY DIRECTORY CONTEXT MANAGER
    print("\n3. TEMPORARY DIRECTORY (custom)")
    print("-" * 40)
    
    import tempfile
    import shutil
    import os
    
    @contextmanager
    def temporary_directory():
        """Create a temporary directory that auto-deletes."""
        dirpath = tempfile.mkdtemp()
        print(f"  Created: {dirpath}")
        try:
            yield dirpath
        finally:
            shutil.rmtree(dirpath)
            print(f"  Deleted: {dirpath}")
    
    with temporary_directory() as tmpdir:
        # Create a file in the temp directory
        filepath = os.path.join(tmpdir, "test.txt")
        with open(filepath, "w") as f:
            f.write("Temporary content")
        print(f"  Created file in {tmpdir}")
    print("  Directory auto-deleted")
    
    # REDIRECT STDOUT CONTEXT MANAGER
    print("\n4. REDIRECT STDOUT CONTEXT MANAGER")
    print("-" * 40)
    
    import sys
    from io import StringIO
    
    @contextmanager
    def capture_output():
        """Capture stdout and stderr."""
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        stdout_capture = StringIO()
        stderr_capture = StringIO()
        sys.stdout = stdout_capture
        sys.stderr = stderr_capture
        try:
            yield stdout_capture, stderr_capture
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
    
    with capture_output() as (out, err):
        print("This is captured")
        import sys
        sys.stderr.write("This is error captured\n")
    
    print(f"  Captured stdout: {out.getvalue().strip()}")
    print(f"  Captured stderr: {err.getvalue().strip()}")
    
    # NESTED CONTEXT MANAGERS
    print("\n5. NESTING CONTEXT MANAGERS")
    print("-" * 40)
    
    @contextmanager
    def prefix_text(prefix: str):
        """Add prefix to all printed text."""
        print(f"{prefix}Entering context")
        try:
            yield
        finally:
            print(f"{prefix}Exiting context")
    
    with prefix_text(">> "), timer("Nested operation"):
        print("  Inside nested contexts")
        time.sleep(0.1)


def demonstrate_error_handling_in_context_managers():
    """
    Demonstrates error handling within context managers.
    
    Context managers can handle, log, or propagate exceptions.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: ERROR HANDLING IN CONTEXT MANAGERS")
    print("=" * 60)
    
    # CONTEXT MANAGER THAT LOGS EXCEPTIONS
    print("\n1. EXCEPTION LOGGING CONTEXT MANAGER")
    print("-" * 40)
    
    @contextmanager
    def log_exceptions(logger_name: str = "context"):
        """Log any exceptions that occur."""
        try:
            yield
        except Exception as e:
            print(f"  [ERROR] {logger_name}: {type(e).__name__}: {e}")
            raise  # Re-raise after logging
    
    try:
        with log_exceptions("test_operation"):
            print("  Inside context")
            raise ValueError("Something went wrong")
    except ValueError:
        print("  Exception propagated after logging")
    
    # CONTEXT MANAGER THAT RETRIES ON FAILURE
    print("\n2. RETRY CONTEXT MANAGER")
    print("-" * 40)
    
    @contextmanager
    def retry_on_failure(max_retries: int = 3, delay: float = 0.1):
        """Retry the block if it fails."""
        attempts = 0
        while True:
            attempts += 1
            try:
                yield
                break  # Success, exit retry loop
            except Exception as e:
                if attempts >= max_retries:
                    print(f"  Failed after {max_retries} attempts: {e}")
                    raise
                print(f"  Attempt {attempts} failed, retrying in {delay}s...")
                time.sleep(delay)
    
    # Simulate flaky operation
    attempt_count = 0
    
    def flaky_operation():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ConnectionError("Temporary failure")
        return "Success"
    
    with retry_on_failure(max_retries=3):
        result = flaky_operation()
        print(f"  Operation succeeded: {result}")
    
    # CONTEXT MANAGER WITH ROLLBACK
    print("\n3. TRANSACTION WITH ROLLBACK CONTEXT MANAGER")
    print("-" * 40)
    
    class Transaction:
        """Simple transaction with rollback on error."""
        
        def __init__(self):
            self.changes = []
            self.committed = False
        
        def add_change(self, change: str):
            self.changes.append(change)
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                print(f"  Rolling back {len(self.changes)} changes")
                self.changes.clear()
                return False
            else:
                self.committed = True
                print(f"  Committed {len(self.changes)} changes")
                return False
    
    with Transaction() as tx:
        tx.add_change("Update user 1")
        tx.add_change("Update user 2")
        # No exception, transaction commits
    print(f"  Transaction committed: {tx.committed}")
    
    try:
        with Transaction() as tx:
            tx.add_change("Update user 1")
            raise ValueError("Something went wrong")
    except ValueError:
        print("  Transaction rolled back due to exception")
        print(f"  Changes after rollback: {tx.changes}")


if __name__ == "__main__":
    demonstrate_class_based_context_manager()
    demonstrate_decorator_based_context_manager()
    demonstrate_error_handling_in_context_managers()
```

---

## 🗄️ Section 3: Database Connection Pool

A complete database connection pool that uses context managers for automatic connection management.

**SOLID Principles Applied:**
- Single Responsibility: Pool manages connections, connections execute queries
- Dependency Inversion: Depends on connection abstraction

**Design Patterns:**
- Pool Pattern: Reuses expensive connections
- Proxy Pattern: Context manager proxies connection operations

```python
"""
DATABASE CONNECTION POOL

This section builds a database connection pool with context managers.

SOLID Principles Applied:
- Single Responsibility: Pool manages connections
- Dependency Inversion: Depends on connection abstraction

Design Patterns:
- Pool Pattern: Reuses expensive connections
- Proxy Pattern: Context manager proxies connection operations
"""

import time
import threading
import queue
from typing import Any, Dict, List, Optional, Callable
from contextlib import contextmanager
from datetime import datetime
import random


class DatabaseConnection:
    """
    Simulated database connection.
    
    Design Pattern: Proxy Pattern - Wraps actual connection
    """
    
    def __init__(self, conn_id: int, connection_string: str):
        self.conn_id = conn_id
        self.connection_string = connection_string
        self.in_use = False
        self.created_at = datetime.now()
        self.last_used = None
        self.transaction_active = False
    
    def connect(self) -> None:
        """Simulate connecting to database."""
        time.sleep(0.01)  # Simulate connection overhead
        print(f"  Connection {self.conn_id} established")
    
    def disconnect(self) -> None:
        """Simulate disconnecting from database."""
        time.sleep(0.005)
        print(f"  Connection {self.conn_id} closed")
    
    def execute(self, query: str, params: Optional[Dict] = None) -> List[Dict]:
        """Execute a query."""
        if not self.in_use:
            raise RuntimeError("Connection not acquired")
        
        self.last_used = datetime.now()
        
        # Simulate query execution
        time.sleep(0.02)
        
        # Simulate different results based on query
        if "SELECT" in query.upper():
            return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        elif "INSERT" in query.upper():
            return [{"affected_rows": 1}]
        elif "UPDATE" in query.upper():
            return [{"affected_rows": 1}]
        else:
            return []
    
    def begin_transaction(self) -> None:
        """Begin a database transaction."""
        self.transaction_active = True
        print(f"  Connection {self.conn_id}: BEGIN TRANSACTION")
    
    def commit(self) -> None:
        """Commit the current transaction."""
        self.transaction_active = False
        print(f"  Connection {self.conn_id}: COMMIT")
    
    def rollback(self) -> None:
        """Rollback the current transaction."""
        self.transaction_active = False
        print(f"  Connection {self.conn_id}: ROLLBACK")
    
    def __repr__(self) -> str:
        return f"DBConn({self.conn_id}, in_use={self.in_use})"


class ConnectionPool:
    """
    Database connection pool with context manager support.
    
    Design Pattern: Pool Pattern - Reuses connections
    """
    
    def __init__(self, connection_string: str, min_size: int = 2, max_size: int = 10):
        self.connection_string = connection_string
        self.min_size = min_size
        self.max_size = max_size
        
        self._pool: queue.Queue = queue.Queue()
        self._active_connections: Dict[int, DatabaseConnection] = {}
        self._lock = threading.Lock()
        self._next_conn_id = 1
        
        self._initialize_pool()
    
    def _initialize_pool(self) -> None:
        """Initialize the connection pool with minimum connections."""
        for _ in range(self.min_size):
            conn = self._create_connection()
            self._pool.put(conn)
        print(f"  Connection pool initialized with {self.min_size} connections")
    
    def _create_connection(self) -> DatabaseConnection:
        """Create a new database connection."""
        with self._lock:
            conn_id = self._next_conn_id
            self._next_conn_id += 1
        
        conn = DatabaseConnection(conn_id, self.connection_string)
        conn.connect()
        return conn
    
    def acquire(self, timeout: float = 30.0) -> Optional[DatabaseConnection]:
        """
        Acquire a connection from the pool.
        
        Args:
            timeout: Maximum time to wait for a connection
            
        Returns:
            DatabaseConnection or None if timeout
        """
        start_time = time.time()
        
        while True:
            try:
                # Try to get a connection from the pool
                conn = self._pool.get(timeout=1.0)
                
                # Check if connection is still valid (simulated)
                if random.random() < 0.05:  # 5% chance of stale connection
                    print(f"  Connection {conn.conn_id} was stale, reconnecting...")
                    conn.disconnect()
                    conn.connect()
                
                conn.in_use = True
                print(f"  Acquired connection {conn.conn_id}")
                return conn
                
            except queue.Empty:
                # No connections available, try to create a new one
                with self._lock:
                    if len(self._active_connections) < self.max_size:
                        conn = self._create_connection()
                        conn.in_use = True
                        self._active_connections[conn.conn_id] = conn
                        print(f"  Created new connection {conn.conn_id} (pool expanded)")
                        return conn
                
                # Check timeout
                if time.time() - start_time > timeout:
                    raise TimeoutError(f"Could not acquire connection within {timeout}s")
                
                print(f"  Waiting for connection...")
    
    def release(self, conn: DatabaseConnection) -> None:
        """Release a connection back to the pool."""
        conn.in_use = False
        conn.transaction_active = False
        self._pool.put(conn)
        print(f"  Released connection {conn.conn_id} back to pool")
    
    @contextmanager
    def get_connection(self):
        """
        Context manager for acquiring and releasing connections.
        
        Usage:
            with pool.get_connection() as conn:
                conn.execute("SELECT * FROM users")
        """
        conn = self.acquire()
        try:
            yield conn
        finally:
            self.release(conn)
    
    @contextmanager
    def transaction(self):
        """
        Context manager for database transactions.
        
        Usage:
            with pool.transaction() as conn:
                conn.execute("UPDATE users SET balance = balance - 100 WHERE id = 1")
                conn.execute("UPDATE users SET balance = balance + 100 WHERE id = 2")
        """
        conn = self.acquire()
        try:
            conn.begin_transaction()
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"  Transaction rolled back due to: {e}")
            raise
        finally:
            self.release(conn)
    
    def close_all(self) -> None:
        """Close all connections in the pool."""
        # Close connections in the queue
        while not self._pool.empty():
            try:
                conn = self._pool.get_nowait()
                conn.disconnect()
            except queue.Empty:
                break
        
        # Close active connections
        for conn in self._active_connections.values():
            conn.disconnect()
        
        self._active_connections.clear()
        print("  All connections closed")
    
    def get_stats(self) -> Dict:
        """Get pool statistics."""
        return {
            "pool_size": self._pool.qsize(),
            "active_connections": len(self._active_connections),
            "min_size": self.min_size,
            "max_size": self.max_size,
            "connection_string": self.connection_string
        }


class Repository:
    """
    Data repository using the connection pool.
    
    Demonstrates using context managers for database operations.
    """
    
    def __init__(self, pool: ConnectionPool):
        self.pool = pool
    
    def find_user(self, user_id: int) -> Optional[Dict]:
        """Find a user by ID."""
        with self.pool.get_connection() as conn:
            results = conn.execute(f"SELECT * FROM users WHERE id = {user_id}")
            return results[0] if results else None
    
    def transfer_money(self, from_user: int, to_user: int, amount: float) -> bool:
        """Transfer money between users (transactional)."""
        try:
            with self.pool.transaction() as conn:
                # Check balances
                from_balance = conn.execute(f"SELECT balance FROM users WHERE id = {from_user}")
                if not from_balance or from_balance[0]["balance"] < amount:
                    raise ValueError(f"Insufficient funds for user {from_user}")
                
                # Perform transfer
                conn.execute(f"UPDATE users SET balance = balance - {amount} WHERE id = {from_user}")
                conn.execute(f"UPDATE users SET balance = balance + {amount} WHERE id = {to_user}")
                
                # Record transaction
                conn.execute(f"INSERT INTO transactions (from_user, to_user, amount) VALUES ({from_user}, {to_user}, {amount})")
                
                return True
        except Exception as e:
            print(f"  Transfer failed: {e}")
            return False


def demonstrate_connection_pool():
    """
    Demonstrate the database connection pool.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: DATABASE CONNECTION POOL")
    print("=" * 60)
    
    # Create connection pool
    print("\n1. INITIALIZING CONNECTION POOL")
    print("-" * 40)
    
    pool = ConnectionPool("postgresql://localhost/mydb", min_size=2, max_size=5)
    stats = pool.get_stats()
    print(f"  Pool stats: {stats}")
    
    # Simple connection usage
    print("\n2. USING CONNECTION CONTEXT MANAGER")
    print("-" * 40)
    
    with pool.get_connection() as conn:
        results = conn.execute("SELECT * FROM users")
        print(f"  Query returned {len(results)} rows")
    
    # Concurrent connection usage
    print("\n3. CONCURRENT CONNECTION USAGE")
    print("-" * 40)
    
    import concurrent.futures
    
    def worker(worker_id: int):
        with pool.get_connection() as conn:
            time.sleep(0.05)  # Simulate work
            return f"Worker {worker_id} used connection {conn.conn_id}"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(worker, i) for i in range(8)]
        for future in concurrent.futures.as_completed(futures):
            print(f"  {future.result()}")
    
    # Transaction example
    print("\n4. TRANSACTION CONTEXT MANAGER")
    print("-" * 40)
    
    # Simulate accounts
    class Account:
        def __init__(self, id: int, balance: float):
            self.id = id
            self.balance = balance
    
    # Override execute for demo
    original_execute = DatabaseConnection.execute
    
    def mock_execute(self, query: str, params=None):
        if "balance -" in query:
            # Simulate balance update
            pass
        return original_execute(self, query, params)
    
    DatabaseConnection.execute = mock_execute
    
    print("  Transfer attempt (successful):")
    try:
        with pool.transaction() as conn:
            conn.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
            conn.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
        print("  Transfer completed successfully")
    except Exception as e:
        print(f"  Transfer failed: {e}")
    
    print("\n  Transfer attempt (with rollback):")
    try:
        with pool.transaction() as conn:
            conn.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
            raise ValueError("Insufficient funds")
            conn.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    except ValueError:
        print("  Transfer rolled back due to error")
    
    # Pool statistics
    print("\n5. POOL STATISTICS")
    print("-" * 40)
    
    stats = pool.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Clean up
    print("\n6. CLOSING POOL")
    print("-" * 40)
    
    pool.close_all()


if __name__ == "__main__":
    demonstrate_connection_pool()
```

---

## ⏱️ Section 4: Performance Measurement and Profiling

A complete performance measurement system using context managers.

**SOLID Principles Applied:**
- Single Responsibility: Each context manager measures one aspect
- Open/Closed: New measurement types can be added

**Design Patterns:**
- Decorator Pattern: Context managers wrap code blocks
- Observer Pattern: Notify when thresholds exceeded

```python
"""
PERFORMANCE MEASUREMENT AND PROFILING

This section builds performance measurement tools using context managers.

SOLID Principles Applied:
- Single Responsibility: Each context manager measures one aspect
- Open/Closed: New measurement types can be added

Design Patterns:
- Decorator Pattern: Context managers wrap code blocks
- Observer Pattern: Notify when thresholds exceeded
"""

import time
import functools
import threading
from typing import Dict, List, Optional, Callable, Any
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict


@dataclass
class Measurement:
    """Single measurement result."""
    name: str
    duration_ms: float
    start_time: datetime
    end_time: datetime
    success: bool = True
    error: Optional[str] = None
    metadata: Dict = field(default_factory=dict)


@dataclass
class Statistics:
    """Statistics for a metric."""
    count: int = 0
    total_ms: float = 0.0
    min_ms: float = float('inf')
    max_ms: float = 0.0
    errors: int = 0
    
    @property
    def avg_ms(self) -> float:
        return self.total_ms / self.count if self.count > 0 else 0.0
    
    @property
    def success_rate(self) -> float:
        return ((self.count - self.errors) / self.count * 100) if self.count > 0 else 100.0


class MetricsCollector:
    """
    Collects and analyzes performance metrics.
    
    Design Pattern: Observer Pattern - Observes measurements
    """
    
    def __init__(self):
        self.measurements: List[Measurement] = []
        self._statistics: Dict[str, Statistics] = defaultdict(Statistics)
        self._thresholds: Dict[str, float] = {}
    
    def add_measurement(self, measurement: Measurement) -> None:
        """Add a measurement."""
        self.measurements.append(measurement)
        
        stats = self._statistics[measurement.name]
        stats.count += 1
        stats.total_ms += measurement.duration_ms
        stats.min_ms = min(stats.min_ms, measurement.duration_ms)
        stats.max_ms = max(stats.max_ms, measurement.duration_ms)
        if not measurement.success:
            stats.errors += 1
        
        # Check threshold
        if measurement.name in self._thresholds:
            if measurement.duration_ms > self._thresholds[measurement.name]:
                print(f"  ⚠️ Threshold exceeded: {measurement.name} took {measurement.duration_ms:.2f}ms (threshold: {self._thresholds[measurement.name]}ms)")
    
    def set_threshold(self, name: str, threshold_ms: float) -> None:
        """Set a performance threshold."""
        self._thresholds[name] = threshold_ms
    
    def get_statistics(self, name: Optional[str] = None) -> Dict:
        """Get statistics for a metric or all metrics."""
        if name:
            stats = self._statistics.get(name)
            if stats:
                return {
                    "count": stats.count,
                    "avg_ms": round(stats.avg_ms, 2),
                    "min_ms": round(stats.min_ms, 2),
                    "max_ms": round(stats.max_ms, 2),
                    "total_ms": round(stats.total_ms, 2),
                    "errors": stats.errors,
                    "success_rate": round(stats.success_rate, 1)
                }
            return {}
        
        return {
            name: {
                "count": stats.count,
                "avg_ms": round(stats.avg_ms, 2),
                "min_ms": round(stats.min_ms, 2),
                "max_ms": round(stats.max_ms, 2),
                "success_rate": round(stats.success_rate, 1)
            }
            for name, stats in self._statistics.items()
        }
    
    def get_recent_measurements(self, limit: int = 10) -> List[Measurement]:
        """Get recent measurements."""
        return self.measurements[-limit:][::-1]
    
    def reset(self) -> None:
        """Reset all statistics."""
        self.measurements.clear()
        self._statistics.clear()
    
    def generate_report(self) -> str:
        """Generate a performance report."""
        report = []
        report.append("=" * 60)
        report.append("PERFORMANCE REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        for name, stats in self._statistics.items():
            report.append(f"\n📊 {name}:")
            report.append(f"  Count: {stats.count}")
            report.append(f"  Average: {stats.avg_ms:.2f}ms")
            report.append(f"  Min: {stats.min_ms:.2f}ms")
            report.append(f"  Max: {stats.max_ms:.2f}ms")
            report.append(f"  Success Rate: {stats.success_rate:.1f}%")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)


# Global metrics collector
_metrics = MetricsCollector()


@contextmanager
def measure(name: str, **metadata):
    """
    Context manager for measuring execution time.
    
    Usage:
        with measure("database_query"):
            result = db.query("SELECT * FROM users")
    """
    start = time.time()
    start_dt = datetime.now()
    success = True
    error = None
    
    try:
        yield
    except Exception as e:
        success = False
        error = str(e)
        raise
    finally:
        duration_ms = (time.time() - start) * 1000
        measurement = Measurement(
            name=name,
            duration_ms=duration_ms,
            start_time=start_dt,
            end_time=datetime.now(),
            success=success,
            error=error,
            metadata=metadata
        )
        _metrics.add_measurement(measurement)


def timed(threshold_ms: Optional[float] = None):
    """
    Decorator for timing functions.
    
    Usage:
        @timed(threshold_ms=100)
        def slow_function():
            time.sleep(0.5)
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = f"{func.__module__}.{func.__qualname__}"
            with measure(func_name):
                return func(*args, **kwargs)
        
        if threshold_ms:
            _metrics.set_threshold(func.__name__, threshold_ms)
        
        return wrapper
    return decorator


@contextmanager
def profile(name: str, detailed: bool = False):
    """
    Advanced profiling context manager.
    
    Provides detailed timing breakdown and memory usage.
    """
    import tracemalloc
    
    start_time = time.time()
    start_cpu = time.process_time()
    
    if detailed:
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[0]
    
    try:
        yield
    finally:
        end_time = time.time()
        end_cpu = time.process_time()
        
        duration_ms = (end_time - start_time) * 1000
        cpu_ms = (end_cpu - start_cpu) * 1000
        
        print(f"\n  📈 Profile: {name}")
        print(f"    Wall time: {duration_ms:.2f}ms")
        print(f"    CPU time: {cpu_ms:.2f}ms")
        
        if detailed:
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"    Memory peak: {peak / 1024:.2f}KB")
            print(f"    Memory current: {current / 1024:.2f}KB")
        
        # Add to metrics
        measurement = Measurement(
            name=f"profile_{name}",
            duration_ms=duration_ms,
            start_time=datetime.now(),
            end_time=datetime.now(),
            metadata={"cpu_ms": cpu_ms}
        )
        _metrics.add_measurement(measurement)


@contextmanager
def batch_measure(batch_name: str):
    """
    Context manager for measuring batch operations.
    
    Tracks individual operations within a batch.
    """
    operations = []
    start_time = time.time()
    
    class BatchRecorder:
        def record(self, op_name: str):
            return measure(f"{batch_name}.{op_name}")
    
    recorder = BatchRecorder()
    
    try:
        yield recorder
    finally:
        total_ms = (time.time() - start_time) * 1000
        print(f"  Batch '{batch_name}' total: {total_ms:.2f}ms")


def get_metrics() -> MetricsCollector:
    """Get the global metrics collector."""
    return _metrics


def demonstrate_performance_measurement():
    """
    Demonstrate performance measurement tools.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: PERFORMANCE MEASUREMENT")
    print("=" * 60)
    
    # Basic timing
    print("\n1. BASIC TIMING WITH CONTEXT MANAGER")
    print("-" * 40)
    
    with measure("sleep_operation"):
        time.sleep(0.1)
    
    # Decorator-based timing
    print("\n2. DECORATOR-BASED TIMING")
    print("-" * 40)
    
    @timed()
    def process_data(size: int):
        """Simulate data processing."""
        time.sleep(size / 1000)
        return f"Processed {size} items"
    
    result = process_data(50)
    print(f"  Result: {result}")
    
    # Threshold monitoring
    print("\n3. THRESHOLD MONITORING")
    print("-" * 40)
    
    _metrics.set_threshold("slow_function", 50)
    
    @timed(threshold_ms=50)
    def slow_function():
        time.sleep(0.1)
    
    slow_function()
    
    # Detailed profiling
    print("\n4. DETAILED PROFILING")
    print("-" * 40)
    
    with profile("complex_operation", detailed=True):
        # Simulate memory allocation
        data = [i for i in range(10000)]
        time.sleep(0.05)
        result = sum(data)
    
    # Batch measurement
    print("\n5. BATCH MEASUREMENT")
    print("-" * 40)
    
    with batch_measure("data_pipeline") as batch:
        with batch.record("extract"):
            time.sleep(0.02)
        with batch.record("transform"):
            time.sleep(0.03)
        with batch.record("load"):
            time.sleep(0.01)
    
    # Statistics
    print("\n6. PERFORMANCE STATISTICS")
    print("-" * 40)
    
    stats = _metrics.get_statistics()
    for name, stat in stats.items():
        print(f"  {name}:")
        print(f"    Count: {stat['count']}")
        print(f"    Avg: {stat['avg_ms']}ms")
        print(f"    Min: {stat['min_ms']}ms")
        print(f"    Max: {stat['max_ms']}ms")
        print(f"    Success Rate: {stat['success_rate']}%")
    
    # Full report
    print("\n7. PERFORMANCE REPORT")
    print("-" * 40)
    
    report = _metrics.generate_report()
    print(report)
    
    # Real-world example: API endpoint timing
    print("\n8. REAL-WORLD EXAMPLE: API ENDPOINT")
    print("-" * 40)
    
    class APIHandler:
        @timed()
        def get_users(self):
            time.sleep(0.02)
            return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        
        @timed()
        def get_orders(self, user_id: int):
            time.sleep(0.03)
            return [{"id": 101, "amount": 99.99}]
        
        def handle_request(self, endpoint: str):
            with measure(f"api_{endpoint}"):
                if endpoint == "/users":
                    return self.get_users()
                elif endpoint == "/orders":
                    return self.get_orders(1)
    
    api = APIHandler()
    api.handle_request("/users")
    api.handle_request("/orders")
    
    print("\n  API Statistics:")
    api_stats = _metrics.get_statistics()
    for name, stat in api_stats.items():
        if name.startswith("api_") or name.startswith("APIHandler"):
            print(f"    {name}: {stat['avg_ms']}ms avg ({stat['count']} calls)")


if __name__ == "__main__":
    demonstrate_performance_measurement()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Context Manager Basics** – `with` statement manages resources. `__enter__` acquires, `__exit__` releases.

- **Built-in Context Managers** – Files, locks (`threading.Lock`), decimal context, temporary directory, suppress exceptions.

- **Class-based Context Managers** – Implement `__enter__` and `__exit__` methods. Return value from `__enter__` is available via `as`.

- **Decorator-based Context Managers** – `@contextmanager` turns generator into context manager. `yield` separates setup and cleanup.

- **Error Handling** – `__exit__` receives exception info. Return `True` to suppress, `False` to propagate.

- **Connection Pool** – Reuses expensive database connections. Context manager for acquire/release. Transaction context manager with commit/rollback.

- **Performance Measurement** – Measure execution time, CPU time, memory usage. Set thresholds, generate reports.

- **SOLID Principles Applied** – Single Responsibility (each context manager handles one resource), Open/Closed (new context managers can be created), Dependency Inversion (depends on abstractions).

- **Design Patterns Used** – RAII (Resource Acquisition Is Initialization), Pool Pattern (connection reuse), Proxy Pattern (connection wrapper), Decorator Pattern (timing decorator), Observer Pattern (threshold monitoring).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Exception Handling – Graceful Failures

- **📚 Series E Catalog:** File & Data Handling Line – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Working with Paths & Directories (Series E, Story 5)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 4 | 1 | 80% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **33** | **19** | **63%** |

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

**Next Story:** Series E, Story 5: The 2026 Python Metromap: Working with Paths & Directories

---

## 📝 Your Invitation

You've mastered context managers. Now build something with what you've learned:

1. **Build a Redis connection pool** – Create a connection pool for Redis with context managers.

2. **Create a file lock context manager** – Prevent concurrent file access across processes.

3. **Build a change directory context manager** – Temporarily change working directory, restore on exit.

4. **Create a environment variable context manager** – Temporarily set environment variables.

5. **Build a timeout context manager** – Raise exception if code block takes too long.

**You've mastered context managers. Next stop: Working with Paths & Directories!**

---

*Found this helpful? Clap, comment, and share what you built with context managers. Next stop: Paths & Directories!* 🚇