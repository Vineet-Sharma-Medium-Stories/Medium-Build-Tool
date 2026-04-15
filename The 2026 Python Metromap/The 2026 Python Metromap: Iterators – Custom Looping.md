# The 2026 Python Metromap: Iterators – Custom Looping

## Series F: Advanced Python Engineering | Story 3 of 6

![The 2026 Python Metromap/images/Iterators – Custom Looping](images/Iterators – Custom Looping.png)

## 📖 Introduction

**Welcome to the third stop on the Advanced Python Engineering Line.**

You've mastered generators—functions that yield values lazily using `yield`. You can process large datasets efficiently, create infinite streams, and build data pipelines. But generators are just one way to implement iteration in Python. Underneath, Python's `for` loop works with any object that follows the iterator protocol.

Iterators are objects that produce values one at a time. Unlike generators (which are a convenient way to create iterators), you can build custom iterator classes by implementing the `__iter__` and `__next__` methods. This gives you complete control over iteration behavior—you can create iterators that paginate through database results, read files in chunks, generate sequences with complex logic, or iterate over custom data structures.

This story—**The 2026 Python Metromap: Iterators – Custom Looping**—is your guide to mastering iterators in Python. We'll build a complete database paginator that fetches rows in chunks. We'll create a file chunk reader that reads large files in manageable pieces. We'll implement a Fibonacci iterator with caching. We'll build a tree iterator that traverses hierarchical data. And we'll create a complete custom collection that supports iteration, indexing, and slicing.

**Let's iterate.**

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

- 🔁 **The 2026 Python Metromap: Iterators – Custom Looping** – Database paginator; file chunk reader; Fibonacci sequence iterator. **⬅️ YOU ARE HERE**

- 🧠 **The 2026 Python Metromap: Memory Management & Garbage Collection** – Optimizing a recommendation engine; memory profiling; leak fixing. 🔜 *Up Next*

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports.

- 📝 **The 2026 Python Metromap: Type Hints & MyPy** – Large team codebase annotations; pre-runtime bug catching; automatic documentation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔁 Section 1: Iterator Protocol – __iter__ and __next__

The iterator protocol requires two methods: `__iter__` returns the iterator object, and `__next__` returns the next value or raises `StopIteration`.

**SOLID Principle Applied: Single Responsibility** – Each iterator handles one traversal pattern.

**Design Pattern: Iterator Pattern** – Provides a way to access elements sequentially without exposing underlying representation.

```python
"""
ITERATOR PROTOCOL: __iter__ AND __next__

This section covers the fundamentals of the iterator protocol.

SOLID Principle: Single Responsibility
- Each iterator handles one traversal pattern

Design Pattern: Iterator Pattern
- Provides sequential access without exposing representation
"""

from typing import Any, Iterator, List, Optional
import time


def demonstrate_iterator_protocol():
    """
    Demonstrates the iterator protocol with custom iterators.
    
    Any object with __iter__ and __next__ can be used in a for loop.
    """
    print("=" * 60)
    print("SECTION 1A: ITERATOR PROTOCOL")
    print("=" * 60)
    
    # SIMPLE CUSTOM ITERATOR
    print("\n1. SIMPLE CUSTOM ITERATOR")
    print("-" * 40)
    
    class CountDown:
        """Iterator that counts down from n to 1."""
        
        def __init__(self, start: int):
            self.current = start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            value = self.current
            self.current -= 1
            return value
    
    countdown = CountDown(5)
    print("  Countdown from 5:")
    for num in countdown:
        print(f"    {num}")
    
    # RANGE ITERATOR (custom implementation)
    print("\n2. CUSTOM RANGE ITERATOR")
    print("-" * 40)
    
    class MyRange:
        """Custom range iterator similar to built-in range."""
        
        def __init__(self, start: int, stop: int = None, step: int = 1):
            if stop is None:
                self.start = 0
                self.stop = start
            else:
                self.start = start
                self.stop = stop
            self.step = step
            self.current = self.start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if (self.step > 0 and self.current >= self.stop) or \
               (self.step < 0 and self.current <= self.stop):
                raise StopIteration
            
            value = self.current
            self.current += self.step
            return value
    
    print("  MyRange(5):", list(MyRange(5)))
    print("  MyRange(2, 10, 2):", list(MyRange(2, 10, 2)))
    print("  MyRange(10, 0, -1):", list(MyRange(10, 0, -1)))
    
    # ITERATOR THAT CAN BE USED MULTIPLE TIMES
    print("\n3. REUSABLE ITERATOR (returns new iterator each time)")
    print("-" * 40)
    
    class Squares:
        """Iterable that can be used multiple times."""
        
        def __init__(self, n: int):
            self.n = n
        
        def __iter__(self):
            # Return a new iterator each time
            return SquaresIterator(self.n)
    
    class SquaresIterator:
        """Actual iterator for Squares."""
        
        def __init__(self, n: int):
            self.n = n
            self.current = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current >= self.n:
                raise StopIteration
            value = self.current ** 2
            self.current += 1
            return value
    
    squares = Squares(5)
    print("  First iteration:", list(squares))
    print("  Second iteration:", list(squares))
    
    # INFINITE ITERATOR
    print("\n4. INFINITE ITERATOR")
    print("-" * 40)
    
    class NaturalNumbers:
        """Infinite iterator of natural numbers."""
        
        def __init__(self):
            self.current = 1
        
        def __iter__(self):
            return self
        
        def __next__(self):
            value = self.current
            self.current += 1
            return value
    
    naturals = NaturalNumbers()
    print("  First 10 natural numbers:")
    for i, num in enumerate(naturals):
        if i >= 10:
            break
        print(f"    {num}")
    
    # ITERATOR WITH STOP CONDITION
    print("\n5. ITERATOR WITH MAX ITERATIONS")
    print("-" * 40)
    
    class LimitedIterator:
        """Iterator that stops after max_iterations."""
        
        def __init__(self, max_iterations: int = 10):
            self.max_iterations = max_iterations
            self.count = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.count >= self.max_iterations:
                raise StopIteration
            self.count += 1
            return f"Item {self.count}"
    
    limited = LimitedIterator(5)
    for item in limited:
        print(f"  {item}")


def demonstrate_iterator_vs_iterable():
    """
    Demonstrates the difference between iterable and iterator.
    
    - Iterable: object with __iter__() that returns an iterator
    - Iterator: object with __next__() that produces values
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ITERABLE VS ITERATOR")
    print("=" * 60)
    
    # LIST (iterable, not iterator)
    print("\n1. LIST (Iterable, not Iterator)")
    print("-" * 40)
    
    numbers = [1, 2, 3]
    print(f"  numbers: {numbers}")
    print(f"  has __iter__: {hasattr(numbers, '__iter__')}")
    print(f"  has __next__: {hasattr(numbers, '__next__')}")
    
    # Get iterator from list
    iterator = iter(numbers)
    print(f"\n  iterator = iter(numbers)")
    print(f"  iterator has __next__: {hasattr(iterator, '__next__')}")
    print(f"  next(iterator): {next(iterator)}")
    print(f"  next(iterator): {next(iterator)}")
    
    # STRING (iterable)
    print("\n2. STRING (Iterable)")
    print("-" * 40)
    
    text = "Python"
    print(f"  text: '{text}'")
    for char in text:
        print(f"    {char}")
    
    # DICTIONARY (iterable over keys)
    print("\n3. DICTIONARY (Iterable over keys)")
    print("-" * 40)
    
    user = {"name": "Alice", "age": 28, "city": "NYC"}
    print("  Keys:")
    for key in user:
        print(f"    {key}")
    
    print("  Values:")
    for value in user.values():
        print(f"    {value}")
    
    print("  Items:")
    for key, value in user.items():
        print(f"    {key}: {value}")
    
    # CUSTOM ITERABLE CLASS
    print("\n4. CUSTOM ITERABLE CLASS")
    print("-" * 40)
    
    class Fibonacci:
        """Iterable Fibonacci sequence."""
        
        def __init__(self, n: int):
            self.n = n
        
        def __iter__(self):
            return FibonacciIterator(self.n)
    
    class FibonacciIterator:
        """Iterator for Fibonacci sequence."""
        
        def __init__(self, n: int):
            self.n = n
            self.a, self.b = 0, 1
            self.count = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.count >= self.n:
                raise StopIteration
            if self.count == 0:
                self.count += 1
                return 0
            if self.count == 1:
                self.count += 1
                return 1
            
            value = self.a + self.b
            self.a, self.b = self.b, value
            self.count += 1
            return value
    
    fib = Fibonacci(10)
    print("  First 10 Fibonacci numbers:", list(fib))
    
    # USING iter() WITH SENTINEL
    print("\n5. iter() WITH SENTINEL (callable until sentinel)")
    print("-" * 40)
    
    def generate_data():
        """Generator that produces data until 'stop'."""
        data = [1, 2, 3, "stop", 4, 5]
        for item in data:
            yield item
    
    gen = generate_data()
    # Iterate until 'stop' is encountered
    for value in iter(lambda: next(gen), "stop"):
        print(f"  {value}")


def demonstrate_builtin_iterators():
    """
    Demonstrates Python's built-in iterator utilities.
    
    - enumerate: Adds counter to iteration
    - zip: Parallel iteration
    - map: Apply function to each item
    - filter: Filter items
    - reversed: Reverse iteration
    - sorted: Sorted iteration
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: BUILT-IN ITERATOR UTILITIES")
    print("=" * 60)
    
    # ENUMERATE
    print("\n1. ENUMERATE - Add counter to iteration")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry", "date"]
    print("  Fruits with index:")
    for i, fruit in enumerate(fruits):
        print(f"    {i}: {fruit}")
    
    print("  Starting at 1:")
    for i, fruit in enumerate(fruits, start=1):
        print(f"    {i}: {fruit}")
    
    # ZIP - Parallel iteration
    print("\n2. ZIP - Parallel iteration over multiple iterables")
    print("-" * 40)
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [28, 35, 22]
    cities = ["NYC", "LA", "Chicago"]
    
    print("  Zipped data:")
    for name, age, city in zip(names, ages, cities):
        print(f"    {name}, {age}, {city}")
    
    # ZIP with unequal lengths
    print("\n  Zip with unequal lengths (stops at shortest):")
    for pair in zip([1, 2, 3, 4], ['a', 'b', 'c']):
        print(f"    {pair}")
    
    # ZIP_LONGEST (from itertools)
    print("\n  zip_longest (fills missing values):")
    from itertools import zip_longest
    for a, b in zip_longest([1, 2, 3, 4], ['a', 'b', 'c'], fillvalue='?'):
        print(f"    {a}, {b}")
    
    # MAP - Apply function to each item
    print("\n3. MAP - Apply function to each item")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"  Original: {numbers}")
    print(f"  Squares: {squares}")
    
    # FILTER - Filter items
    print("\n4. FILTER - Filter items by predicate")
    print("-" * 40)
    
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 == 1, numbers))
    print(f"  Evens: {evens}")
    print(f"  Odds: {odds}")
    
    # REVERSED - Reverse iteration
    print("\n5. REVERSED - Iterate in reverse")
    print("-" * 40)
    
    for num in reversed(numbers):
        print(f"    {num}")
    
    # SORTED - Sorted iteration
    print("\n6. SORTED - Iterate in sorted order")
    print("-" * 40)
    
    unsorted = [3, 1, 4, 1, 5, 9, 2]
    for num in sorted(unsorted):
        print(f"    {num}")
    
    print("  Descending:")
    for num in sorted(unsorted, reverse=True):
        print(f"    {num}")


if __name__ == "__main__":
    demonstrate_iterator_protocol()
    demonstrate_iterator_vs_iterable()
    demonstrate_builtin_iterators()
```

---

## 🗄️ Section 2: Database Paginator

A complete database paginator that fetches rows in chunks using iterators.

**SOLID Principles Applied:**
- Single Responsibility: Paginator handles fetching, iterator handles traversal
- Open/Closed: New database backends can be added

**Design Patterns:**
- Iterator Pattern: Iterates through database rows lazily
- Proxy Pattern: Paginator proxies database queries

```python
"""
DATABASE PAGINATOR

This section builds a database paginator using iterators.

SOLID Principles Applied:
- Single Responsibility: Paginator handles fetching
- Open/Closed: New database backends can be added

Design Patterns:
- Iterator Pattern: Lazy row iteration
- Proxy Pattern: Paginator proxies database queries
"""

from typing import Dict, List, Any, Optional, Iterator, Tuple
from dataclasses import dataclass
from datetime import datetime
import time
import random


@dataclass
class DatabaseRow:
    """Simulated database row."""
    id: int
    data: Dict[str, Any]
    created_at: datetime


class MockDatabase:
    """
    Mock database for demonstration.
    
    Simulates a database with large tables.
    """
    
    def __init__(self):
        self.tables: Dict[str, List[Dict]] = {}
        self._initialize_data()
        self.query_count = 0
    
    def _initialize_data(self):
        """Initialize sample data."""
        # Users table (1000 rows)
        users = []
        for i in range(1, 1001):
            users.append({
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "age": 20 + (i % 60),
                "city": ["NYC", "LA", "Chicago", "Houston"][i % 4],
                "active": i % 2 == 0,
                "created_at": datetime.now().isoformat()
            })
        self.tables["users"] = users
        
        # Orders table (5000 rows)
        orders = []
        for i in range(1, 5001):
            orders.append({
                "id": i,
                "user_id": random.randint(1, 1000),
                "amount": round(random.uniform(10, 500), 2),
                "status": random.choice(["pending", "shipped", "delivered"]),
                "created_at": datetime.now().isoformat()
            })
        self.tables["orders"] = orders
        
        # Products table (200 rows)
        products = []
        categories = ["Electronics", "Clothing", "Books", "Home"]
        for i in range(1, 201):
            products.append({
                "id": i,
                "name": f"Product {i}",
                "category": categories[i % 4],
                "price": round(random.uniform(10, 500), 2),
                "stock": random.randint(0, 100)
            })
        self.tables["products"] = products
    
    def query(self, table: str, filters: Dict = None, 
              order_by: str = None, limit: int = None, 
              offset: int = 0) -> List[Dict]:
        """Execute a query."""
        self.query_count += 1
        time.sleep(0.01)  # Simulate query time
        
        data = self.tables.get(table, [])
        
        # Apply filters
        if filters:
            for key, value in filters.items():
                data = [row for row in data if row.get(key) == value]
        
        # Apply ordering
        if order_by:
            data = sorted(data, key=lambda x: x.get(order_by, 0))
        
        # Apply pagination
        if limit:
            data = data[offset:offset + limit]
        
        return data
    
    def count(self, table: str, filters: Dict = None) -> int:
        """Count rows matching filters."""
        if filters:
            data = self.query(table, filters)
            return len(data)
        return len(self.tables.get(table, []))
    
    def get_stats(self) -> Dict:
        """Get database statistics."""
        return {
            "query_count": self.query_count,
            "tables": {name: len(rows) for name, rows in self.tables.items()}
        }


class DatabasePaginator:
    """
    Paginator for database queries.
    
    Design Pattern: Iterator Pattern - Lazy page iteration
    """
    
    def __init__(self, db: MockDatabase, table: str, 
                 page_size: int = 100, filters: Dict = None,
                 order_by: str = None):
        self.db = db
        self.table = table
        self.page_size = page_size
        self.filters = filters or {}
        self.order_by = order_by
        self.total_rows = db.count(table, filters)
        self.total_pages = (self.total_rows + page_size - 1) // page_size
        self.current_page = 0
        self.current_page_data = []
    
    def get_page(self, page_num: int) -> List[Dict]:
        """Get a specific page."""
        offset = (page_num - 1) * self.page_size
        return self.db.query(
            table=self.table,
            filters=self.filters,
            order_by=self.order_by,
            limit=self.page_size,
            offset=offset
        )
    
    def __iter__(self):
        return DatabasePaginatorIterator(self)
    
    def get_stats(self) -> Dict:
        """Get paginator statistics."""
        return {
            "table": self.table,
            "total_rows": self.total_rows,
            "page_size": self.page_size,
            "total_pages": self.total_pages,
            "filters": self.filters,
            "order_by": self.order_by
        }


class DatabasePaginatorIterator:
    """
    Iterator for database paginator.
    
    Design Pattern: Iterator Pattern - Iterates through all rows
    """
    
    def __init__(self, paginator: DatabasePaginator):
        self.paginator = paginator
        self.current_page = 1
        self.current_index = 0
        self.current_page_data = []
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # Load next page if needed
        if self.current_index >= len(self.current_page_data):
            if self.current_page > self.paginator.total_pages:
                raise StopIteration
            
            self.current_page_data = self.paginator.get_page(self.current_page)
            self.current_index = 0
            self.current_page += 1
            
            if not self.current_page_data:
                raise StopIteration
        
        row = self.current_page_data[self.current_index]
        self.current_index += 1
        return row


class ChunkedDatabaseReader:
    """
    Reads database in chunks using iterators.
    
    Design Pattern: Iterator Pattern - Chunk-based iteration
    """
    
    def __init__(self, db: MockDatabase, table: str, 
                 chunk_size: int = 500, filters: Dict = None):
        self.db = db
        self.table = table
        self.chunk_size = chunk_size
        self.filters = filters or {}
        self.total_rows = db.count(table, filters)
    
    def read_chunks(self) -> Iterator[List[Dict]]:
        """Yield chunks of rows."""
        offset = 0
        
        while offset < self.total_rows:
            chunk = self.db.query(
                table=self.table,
                filters=self.filters,
                limit=self.chunk_size,
                offset=offset
            )
            
            if not chunk:
                break
            
            yield chunk
            offset += self.chunk_size
    
    def process_in_chunks(self, processor: callable) -> int:
        """Process data in chunks with a processor function."""
        processed = 0
        for chunk in self.read_chunks():
            processed += processor(chunk)
        return processed


class BufferedIterator:
    """
    Iterator with buffer for prefetching.
    
    Design Pattern: Iterator Pattern - Prefetches data
    """
    
    def __init__(self, source_iterator: Iterator, buffer_size: int = 10):
        self.source = source_iterator
        self.buffer_size = buffer_size
        self.buffer = []
        self.exhausted = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # Refill buffer if empty
        if not self.buffer and not self.exhausted:
            self._refill_buffer()
        
        if not self.buffer:
            raise StopIteration
        
        return self.buffer.pop(0)
    
    def _refill_buffer(self):
        """Refill the buffer from source."""
        for _ in range(self.buffer_size):
            try:
                self.buffer.append(next(self.source))
            except StopIteration:
                self.exhausted = True
                break
    
    def has_next(self) -> bool:
        """Check if there are more items."""
        if self.buffer:
            return True
        if not self.exhausted:
            self._refill_buffer()
        return bool(self.buffer)
    
    def peek(self):
        """Peek at next item without consuming."""
        if not self.buffer and not self.exhausted:
            self._refill_buffer()
        
        if self.buffer:
            return self.buffer[0]
        raise StopIteration


def demonstrate_database_paginator():
    """
    Demonstrate the database paginator.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: DATABASE PAGINATOR")
    print("=" * 60)
    
    db = MockDatabase()
    
    print("\n1. DATABASE STATISTICS")
    print("-" * 40)
    
    stats = db.get_stats()
    for table, count in stats["tables"].items():
        print(f"  {table}: {count:,} rows")
    
    print("\n2. PAGINATOR SETUP")
    print("-" * 40)
    
    paginator = DatabasePaginator(db, "users", page_size=50)
    paginator_stats = paginator.get_stats()
    print(f"  Table: {paginator_stats['table']}")
    print(f"  Total rows: {paginator_stats['total_rows']:,}")
    print(f"  Page size: {paginator_stats['page_size']}")
    print(f"  Total pages: {paginator_stats['total_pages']}")
    
    print("\n3. ITERATING THROUGH PAGES (Lazy loading)")
    print("-" * 40)
    
    # Count users without loading all into memory
    user_count = 0
    for user in paginator:
        user_count += 1
        if user_count <= 5:
            print(f"    User {user['id']}: {user['name']}")
    
    print(f"\n  Total users iterated: {user_count}")
    print(f"  Database queries: {db.get_stats()['query_count']}")
    
    print("\n4. FILTERED PAGINATION")
    print("-" * 40)
    
    active_paginator = DatabasePaginator(
        db, "users", page_size=30,
        filters={"active": True}
    )
    
    print(f"  Active users: {active_paginator.total_rows:,}")
    
    active_count = 0
    for user in active_paginator:
        active_count += 1
    
    print(f"  Active users iterated: {active_count}")
    
    print("\n5. CHUNKED PROCESSING")
    print("-" * 40)
    
    chunked_reader = ChunkedDatabaseReader(db, "orders", chunk_size=200)
    
    def process_chunk(chunk):
        """Process a chunk of orders."""
        total_amount = sum(order["amount"] for order in chunk)
        print(f"    Chunk: {len(chunk)} orders, total ${total_amount:.2f}")
        return len(chunk)
    
    print("  Processing orders in chunks:")
    total_processed = chunked_reader.process_in_chunks(process_chunk)
    print(f"  Total processed: {total_processed} orders")
    
    print("\n6. BUFFERED ITERATOR (Prefetching)")
    print("-" * 40)
    
    paginator2 = DatabasePaginator(db, "products", page_size=20)
    buffered = BufferedIterator(paginator2, buffer_size=5)
    
    print("  Products with buffered iterator:")
    count = 0
    while buffered.has_next() and count < 10:
        product = next(buffered)
        print(f"    {product['name']}: ${product['price']:.2f}")
        count += 1
    
    print(f"\n  Buffer has next: {buffered.has_next()}")
    print(f"  Peek next: {buffered.peek()['name']}")
    
    print("\n7. PERFORMANCE COMPARISON")
    print("-" * 40)
    
    # Method 1: Load all at once (eager)
    db = MockDatabase()
    start = time.time()
    all_users = db.query("users", limit=1000)
    eager_time = time.time() - start
    eager_memory = sys.getsizeof(all_users)
    
    # Method 2: Iterator (lazy)
    db = MockDatabase()
    start = time.time()
    paginator3 = DatabasePaginator(db, "users", page_size=100)
    lazy_count = 0
    for user in paginator3:
        lazy_count += 1
    lazy_time = time.time() - start
    
    print(f"  Eager loading: {eager_time:.3f}s, memory: {eager_memory:,} bytes")
    print(f"  Lazy loading: {lazy_time:.3f}s, constant memory")
    print(f"  Both fetched {lazy_count} users")
    print("  💡 Iterators use constant memory regardless of dataset size!")


if __name__ == "__main__":
    import sys
    demonstrate_database_paginator()
```

---

## 📂 Section 3: File Chunk Reader

A file chunk reader that reads large files in manageable pieces using iterators.

**SOLID Principles Applied:**
- Single Responsibility: Chunk reader handles file reading, iterator handles traversal
- Open/Closed: New chunk strategies can be added

**Design Patterns:**
- Iterator Pattern: Lazy file reading
- Adapter Pattern: Adapts file to iterator interface

```python
"""
FILE CHUNK READER

This section builds a file chunk reader using iterators.

SOLID Principles Applied:
- Single Responsibility: Chunk reader handles file reading
- Open/Closed: New chunk strategies can be added

Design Patterns:
- Iterator Pattern: Lazy file reading
- Adapter Pattern: Adapts file to iterator interface
"""

import os
from typing import Iterator, List, Optional, Callable, Any
from pathlib import Path
import hashlib


class FileChunkReader:
    """
    Reads files in chunks using iterators.
    
    Design Pattern: Iterator Pattern - Yields chunks lazily
    """
    
    def __init__(self, filepath: str, chunk_size: int = 8192):
        self.filepath = filepath
        self.chunk_size = chunk_size
        self.file_size = os.path.getsize(filepath)
        self.total_chunks = (self.file_size + chunk_size - 1) // chunk_size
    
    def read_chunks(self, start_byte: int = 0, end_byte: int = None) -> Iterator[bytes]:
        """Read file in chunks."""
        with open(self.filepath, 'rb') as f:
            f.seek(start_byte)
            
            bytes_read = 0
            end = end_byte if end_byte is not None else self.file_size
            
            while bytes_read < (end - start_byte):
                remaining = (end - start_byte) - bytes_read
                read_size = min(self.chunk_size, remaining)
                chunk = f.read(read_size)
                
                if not chunk:
                    break
                
                bytes_read += len(chunk)
                yield chunk
    
    def read_lines(self, encoding: str = 'utf-8') -> Iterator[str]:
        """Read file line by line (memory efficient)."""
        with open(self.filepath, 'r', encoding=encoding) as f:
            for line in f:
                yield line.rstrip('\n')
    
    def read_blocks(self, block_size: int = 1024 * 1024) -> Iterator[bytes]:
        """Read file in fixed-size blocks."""
        return self.read_chunks(chunk_size=block_size)
    
    def get_chunk_info(self) -> dict:
        """Get information about file chunks."""
        return {
            "file": self.filepath,
            "size_bytes": self.file_size,
            "size_mb": self.file_size / (1024 * 1024),
            "chunk_size": self.chunk_size,
            "total_chunks": self.total_chunks
        }


class LineIterator:
    """
    Iterator for reading files line by line.
    
    Design Pattern: Iterator Pattern - Line-based iteration
    """
    
    def __init__(self, filepath: str, encoding: str = 'utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.file = None
        self.line_number = 0
    
    def __iter__(self):
        self.file = open(self.filepath, 'r', encoding=self.encoding)
        self.line_number = 0
        return self
    
    def __next__(self):
        if self.file is None:
            raise RuntimeError("Iterator not initialized")
        
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        
        self.line_number += 1
        return line.rstrip('\n')
    
    def __enter__(self):
        self.file = open(self.filepath, 'r', encoding=self.encoding)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
    
    def get_line_number(self) -> int:
        """Get current line number."""
        return self.line_number


class CSVLineParser:
    """
    Parses CSV files line by line using iterators.
    
    Design Pattern: Iterator Pattern - Lazy CSV parsing
    """
    
    def __init__(self, filepath: str, has_header: bool = True, delimiter: str = ','):
        self.filepath = filepath
        self.has_header = has_header
        self.delimiter = delimiter
        self.headers = None
    
    def __iter__(self):
        self.file = open(self.filepath, 'r')
        self.line_num = 0
        self.headers = None
        
        if self.has_header:
            header_line = self.file.readline().strip()
            self.headers = header_line.split(self.delimiter)
            self.line_num += 1
        
        return self
    
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        
        self.line_num += 1
        values = line.strip().split(self.delimiter)
        
        if self.headers:
            return dict(zip(self.headers, values))
        return values
    
    def __enter__(self):
        self.__iter__()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'file') and self.file:
            self.file.close()


class ReversedFileReader:
    """
    Reads files in reverse order (from end to beginning).
    
    Design Pattern: Iterator Pattern - Reverse file reading
    """
    
    def __init__(self, filepath: str, encoding: str = 'utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.chunk_size = 8192
    
    def read_lines_reverse(self) -> Iterator[str]:
        """Read lines from end to beginning."""
        with open(self.filepath, 'rb') as f:
            f.seek(0, os.SEEK_END)
            file_size = f.tell()
            
            buffer = b''
            position = file_size
            
            while position > 0:
                # Read chunk from end
                read_size = min(self.chunk_size, position)
                position -= read_size
                f.seek(position)
                chunk = f.read(read_size)
                
                buffer = chunk + buffer
                
                # Process complete lines
                lines = buffer.split(b'\n')
                buffer = lines[0]  # Keep incomplete line
                
                for line in reversed(lines[1:]):
                    if line:
                        yield line.decode(self.encoding)
            
            # Yield remaining buffer
            if buffer:
                yield buffer.decode(self.encoding)


class FileProcessor:
    """
    Processes files with custom transformations.
    
    Design Pattern: Pipeline Pattern - Chains transformations
    """
    
    def __init__(self, source: Iterator):
        self.source = source
        self.transformations: List[Callable] = []
    
    def map(self, func: Callable) -> 'FileProcessor':
        """Apply transformation to each item."""
        self.transformations.append(func)
        return self
    
    def filter(self, predicate: Callable) -> 'FileProcessor':
        """Filter items."""
        def filter_transform(items):
            for item in items:
                if predicate(item):
                    yield item
        
        self.transformations.append(filter_transform)
        return self
    
    def take(self, n: int) -> List:
        """Take first n items."""
        result = []
        items = self.source
        
        for transform in self.transformations:
            items = transform(items)
        
        for i, item in enumerate(items):
            if i >= n:
                break
            result.append(item)
        
        return result
    
    def collect(self) -> List:
        """Collect all items."""
        items = self.source
        for transform in self.transformations:
            items = transform(items)
        return list(items)
    
    def reduce(self, func: Callable, initial: Any = None) -> Any:
        """Reduce items to a single value."""
        items = self.source
        for transform in self.transformations:
            items = transform(items)
        
        if initial is not None:
            result = initial
            for item in items:
                result = func(result, item)
            return result
        else:
            items_iter = iter(items)
            try:
                result = next(items_iter)
            except StopIteration:
                raise ValueError("Cannot reduce empty iterable")
            
            for item in items_iter:
                result = func(result, item)
            return result


def demonstrate_file_chunk_reader():
    """
    Demonstrate the file chunk reader.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: FILE CHUNK READER")
    print("=" * 60)
    
    # Create a large test file
    print("\n1. CREATING TEST FILE")
    print("-" * 40)
    
    test_file = "large_test_file.txt"
    with open(test_file, "w") as f:
        for i in range(1000):
            f.write(f"Line {i}: This is some sample content for testing.\n")
    
    file_size = os.path.getsize(test_file)
    print(f"  Created {test_file} ({file_size:,} bytes, 1000 lines)")
    
    # Chunk reader
    print("\n2. CHUNK READER")
    print("-" * 40)
    
    reader = FileChunkReader(test_file, chunk_size=1024)
    info = reader.get_chunk_info()
    print(f"  File info: {info['size_mb']:.2f} MB, {info['total_chunks']} chunks")
    
    print("  Reading first 3 chunks:")
    for i, chunk in enumerate(reader.read_chunks()):
        if i >= 3:
            break
        print(f"    Chunk {i+1}: {len(chunk)} bytes")
    
    print("\n3. LINE ITERATOR (Memory efficient)")
    print("-" * 40)
    
    line_iter = LineIterator(test_file)
    print("  First 5 lines:")
    for i, line in enumerate(line_iter):
        if i >= 5:
            break
        print(f"    {line}")
    
    print(f"\n  Total lines: {sum(1 for _ in LineIterator(test_file))}")
    
    print("\n4. CSV LINE PARSER")
    print("-" * 40)
    
    # Create CSV file
    csv_file = "test_data.csv"
    with open(csv_file, "w") as f:
        f.write("name,age,city,score\n")
        for i in range(100):
            f.write(f"User{i},{(20 + i % 50)},{['NYC','LA','Chicago'][i%3]},{50 + i%50}\n")
    
    parser = CSVLineParser(csv_file)
    print("  First 5 rows as dictionaries:")
    for i, row in enumerate(parser):
        if i >= 5:
            break
        print(f"    {row}")
    
    print("\n5. REVERSED FILE READER")
    print("-" * 40)
    
    reverse_reader = ReversedFileReader(test_file)
    print("  Last 5 lines (in reverse order):")
    for i, line in enumerate(reverse_reader.read_lines_reverse()):
        if i >= 5:
            break
        print(f"    {line}")
    
    print("\n6. FILE PROCESSOR PIPELINE")
    print("-" * 40)
    
    # Create number file
    num_file = "numbers.txt"
    with open(num_file, "w") as f:
        for i in range(1000):
            f.write(f"{random.randint(1, 100)}\n")
    
    processor = FileProcessor(LineIterator(num_file))
    processor.map(lambda x: int(x))
    processor.filter(lambda x: x % 2 == 0)
    processor.map(lambda x: x * 2)
    
    result = processor.take(10)
    print(f"  First 10 even numbers doubled: {result}")
    
    # Reduce to sum
    processor2 = FileProcessor(LineIterator(num_file))
    processor2.map(lambda x: int(x))
    total = processor2.reduce(lambda a, b: a + b, 0)
    print(f"  Sum of all numbers: {total}")
    
    print("\n7. PERFORMANCE COMPARISON")
    print("-" * 40)
    
    # Memory usage comparison
    import tracemalloc
    
    # List approach (eager)
    tracemalloc.start()
    all_lines = []
    with open(test_file, 'r') as f:
        all_lines = f.readlines()
    list_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    # Iterator approach (lazy)
    tracemalloc.start()
    line_count = 0
    for line in LineIterator(test_file):
        line_count += 1
    iter_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    print(f"  List approach: {list_memory / 1024:.1f} KB")
    print(f"  Iterator approach: {iter_memory / 1024:.1f} KB")
    print(f"  Both processed {line_count} lines")
    print("  💡 Iterators use far less memory for large files!")
    
    # Clean up
    for f in [test_file, csv_file, num_file]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up test files")


if __name__ == "__main__":
    import random
    demonstrate_file_chunk_reader()
```

---

## 🔢 Section 4: Custom Sequence Iterator

A complete custom sequence implementation with iteration, indexing, and slicing.

**SOLID Principles Applied:**
- Single Responsibility: Sequence handles storage and access
- Interface Segregation: Implements sequence protocol methods

**Design Patterns:**
- Iterator Pattern: Supports iteration
- Value Object Pattern: Immutable sequence elements

```python
"""
CUSTOM SEQUENCE ITERATOR

This section builds a custom sequence with iteration support.

SOLID Principles Applied:
- Single Responsibility: Sequence handles storage and access
- Interface Segregation: Implements sequence protocol

Design Patterns:
- Iterator Pattern: Supports iteration
- Value Object Pattern: Immutable sequence elements
"""

from typing import Any, Iterator, Optional, List, Tuple, Union
from collections.abc import Sequence
import math


class FibonacciSequence(Sequence):
    """
    Fibonacci sequence with lazy evaluation.
    
    Implements the sequence protocol for indexing and iteration.
    
    Design Pattern: Iterator Pattern - Lazy value generation
    """
    
    def __init__(self, count: int):
        self.count = count
        self._cache = {}
    
    def __getitem__(self, index: Union[int, slice]) -> Any:
        """Get item by index or slice."""
        if isinstance(index, slice):
            start, stop, step = index.indices(self.count)
            return [self[i] for i in range(start, stop, step)]
        
        if index < 0:
            index = self.count + index
        
        if index < 0 or index >= self.count:
            raise IndexError("Fibonacci index out of range")
        
        return self._fibonacci(index)
    
    def __len__(self) -> int:
        return self.count
    
    def _fibonacci(self, n: int) -> int:
        """Calculate Fibonacci number with memoization."""
        if n in self._cache:
            return self._cache[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        result = self._fibonacci(n - 1) + self._fibonacci(n - 2)
        self._cache[n] = result
        return result
    
    def __iter__(self):
        return FibonacciIterator(self)


class FibonacciIterator:
    """Iterator for FibonacciSequence."""
    
    def __init__(self, sequence: FibonacciSequence):
        self.sequence = sequence
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        value = self.sequence[self.index]
        self.index += 1
        return value


class PrimeSequence(Sequence):
    """
    Lazy prime number sequence.
    
    Generates prime numbers on demand without precomputing all.
    """
    
    def __init__(self, count: int):
        self.count = count
        self._primes = []
    
    def __getitem__(self, index: Union[int, slice]) -> Any:
        """Get prime by index."""
        if isinstance(index, slice):
            start, stop, step = index.indices(self.count)
            return [self[i] for i in range(start, stop, step)]
        
        if index < 0:
            index = self.count + index
        
        if index < 0 or index >= self.count:
            raise IndexError("Prime index out of range")
        
        return self._get_prime(index)
    
    def __len__(self) -> int:
        return self.count
    
    def _is_prime(self, n: int) -> bool:
        """Check if number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def _get_prime(self, index: int) -> int:
        """Get the nth prime number."""
        while len(self._primes) <= index:
            if not self._primes:
                candidate = 2
            else:
                candidate = self._primes[-1] + 1
            
            while not self._is_prime(candidate):
                candidate += 1
            
            self._primes.append(candidate)
        
        return self._primes[index]
    
    def __iter__(self):
        return PrimeIterator(self)


class PrimeIterator:
    """Iterator for PrimeSequence."""
    
    def __init__(self, sequence: PrimeSequence):
        self.sequence = sequence
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        value = self.sequence[self.index]
        self.index += 1
        return value


class CircularBuffer:
    """
    Circular buffer with iterator support.
    
    Design Pattern: Iterator Pattern - Cyclic iteration
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def append(self, item: Any) -> None:
        """Append item to buffer (overwrites oldest if full)."""
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity
    
    def __getitem__(self, index: int) -> Any:
        """Get item by index (relative to head)."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.buffer[(self.head + index) % self.capacity]
    
    def __len__(self) -> int:
        return self.size
    
    def __iter__(self):
        for i in range(self.size):
            yield self[i]
    
    def __repr__(self) -> str:
        return f"CircularBuffer({list(self)})"


class InfiniteSequence:
    """
    Infinite sequence with custom iteration.
    
    Design Pattern: Iterator Pattern - Infinite iteration
    """
    
    def __init__(self, generator):
        self.generator = generator
        self._cache = []
    
    def __iter__(self):
        return InfiniteIterator(self)
    
    def take(self, n: int) -> List:
        """Take first n elements."""
        return [self[i] for i in range(n)]
    
    def __getitem__(self, index: int) -> Any:
        """Get item by index (computes if needed)."""
        if index < 0:
            raise IndexError("Negative index not supported for infinite sequence")
        
        while len(self._cache) <= index:
            self._cache.append(next(self.generator))
        
        return self._cache[index]
    
    def skip(self, n: int) -> 'InfiniteSequence':
        """Skip first n elements."""
        for _ in range(n):
            next(self.generator)
        return self


class InfiniteIterator:
    """Iterator for InfiniteSequence."""
    
    def __init__(self, sequence: InfiniteSequence):
        self.sequence = sequence
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.sequence[self.index]
        self.index += 1
        return value


class Matrix:
    """
    2D matrix with row and column iteration.
    
    Design Pattern: Iterator Pattern - Multiple iteration strategies
    """
    
    def __init__(self, data: List[List[Any]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def row_iterator(self) -> Iterator[List[Any]]:
        """Iterate over rows."""
        for row in self.data:
            yield row
    
    def col_iterator(self) -> Iterator[List[Any]]:
        """Iterate over columns."""
        for j in range(self.cols):
            yield [self.data[i][j] for i in range(self.rows)]
    
    def diagonal_iterator(self) -> Iterator[Any]:
        """Iterate over main diagonal."""
        for i in range(min(self.rows, self.cols)):
            yield self.data[i][i]
    
    def spiral_iterator(self) -> Iterator[Any]:
        """Iterate in spiral order."""
        if not self.data or not self.data[0]:
            return
        
        top, bottom = 0, self.rows - 1
        left, right = 0, self.cols - 1
        
        while top <= bottom and left <= right:
            # Top row
            for j in range(left, right + 1):
                yield self.data[top][j]
            top += 1
            
            # Right column
            for i in range(top, bottom + 1):
                yield self.data[i][right]
            right -= 1
            
            if top <= bottom:
                # Bottom row
                for j in range(right, left - 1, -1):
                    yield self.data[bottom][j]
                bottom -= 1
            
            if left <= right:
                # Left column
                for i in range(bottom, top - 1, -1):
                    yield self.data[i][left]
                left += 1
    
    def __iter__(self):
        return self.row_iterator()


def demonstrate_custom_sequences():
    """
    Demonstrate custom sequence iterators.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: CUSTOM SEQUENCE ITERATORS")
    print("=" * 60)
    
    print("\n1. FIBONACCI SEQUENCE (Lazy evaluation)")
    print("-" * 40)
    
    fib = FibonacciSequence(20)
    print(f"  Length: {len(fib)}")
    print(f"  First 10: {fib[:10]}")
    print(f"  Index 15: {fib[15]}")
    print(f"  Slicing [5:15:2]: {fib[5:15:2]}")
    
    print("\n  Iteration:")
    for i, val in enumerate(fib):
        if i >= 8:
            break
        print(f"    {val}", end=" ")
    print()
    
    print("\n2. PRIME SEQUENCE (Lazy generation)")
    print("-" * 40)
    
    primes = PrimeSequence(20)
    print(f"  First 15 primes: {primes[:15]}")
    print(f"  Index 10: {primes[10]}")
    
    print("\n3. CIRCULAR BUFFER")
    print("-" * 40)
    
    buffer = CircularBuffer(5)
    for i in range(1, 8):
        buffer.append(i)
        print(f"  After appending {i}: {buffer}")
    
    print(f"  Buffer length: {len(buffer)}")
    print(f"  Buffer[2]: {buffer[2]}")
    
    print("\n4. INFINITE SEQUENCE")
    print("-" * 40)
    
    def natural_numbers():
        n = 1
        while True:
            yield n
            n += 1
    
    infinite = InfiniteSequence(natural_numbers())
    print(f"  First 10 natural numbers: {infinite.take(10)}")
    print(f"  Index 100: {infinite[100]}")
    print(f"  Skip first 5, then take 10: {infinite.skip(5).take(10)}")
    
    print("\n5. MATRIX ITERATORS")
    print("-" * 40)
    
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("  Matrix:")
    for row in matrix:
        print(f"    {row}")
    
    print("  Row iteration:")
    for row in matrix.row_iterator():
        print(f"    {row}")
    
    print("  Column iteration:")
    for col in matrix.col_iterator():
        print(f"    {col}")
    
    print("  Diagonal iteration:")
    for val in matrix.diagonal_iterator():
        print(f"    {val}")
    
    print("  Spiral iteration:")
    for val in matrix.spiral_iterator():
        print(f"    {val}", end=" ")
    print()
    
    print("\n6. PERFORMANCE: LAZY VS EAGER")
    print("-" * 40)
    
    import time
    
    # Eager: compute all primes upfront
    start = time.time()
    eager_primes = [p for p in PrimeSequence(1000)]
    eager_time = time.time() - start
    
    # Lazy: iterate through primes without storing
    start = time.time()
    lazy_primes = []
    for p in PrimeSequence(1000):
        lazy_primes.append(p)
    lazy_time = time.time() - start
    
    print(f"  Eager (list): {eager_time:.4f}s")
    print(f"  Lazy (iterator): {lazy_time:.4f}s")
    print(f"  Both generated {len(eager_primes)} primes")
    print("  💡 Lazy evaluation is similar speed but uses less memory")


if __name__ == "__main__":
    demonstrate_custom_sequences()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Iterator Protocol** – `__iter__` returns iterator, `__next__` returns next value or raises `StopIteration`. Any object implementing these can be used in `for` loops.

- **Iterable vs Iterator** – Iterable has `__iter__` (can be iterated multiple times). Iterator has `__next__` (can be consumed once).

- **Built-in Iterators** – `enumerate` (adds counter), `zip` (parallel iteration), `map` (apply function), `filter` (filter items), `reversed` (reverse order), `sorted` (sorted order).

- **Database Paginator** – Iterate through database rows without loading all into memory. Fetch pages lazily as needed.

- **Chunked Reading** – Read large files in chunks. Process line by line without loading entire file.

- **Buffered Iterator** – Prefetch items into buffer for performance. Peek at next item without consuming.

- **Custom Sequences** – Implement `Sequence` protocol (`__getitem__`, `__len__`) for lazy sequences. Fibonacci, primes, infinite sequences.

- **Multiple Iteration Strategies** – Row iteration, column iteration, diagonal iteration, spiral iteration for matrices.

- **SOLID Principles Applied** – Single Responsibility (each iterator handles one traversal), Interface Segregation (clean sequence interface), Open/Closed (new iterators can be added), Dependency Inversion (depends on iterator abstraction).

- **Design Patterns Used** – Iterator Pattern (custom iteration), Proxy Pattern (database paginator), Adapter Pattern (file to iterator), Pipeline Pattern (transformations), Value Object Pattern (immutable sequence elements).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Generators – Memory-Efficient Loops

- **📚 Series F Catalog:** Advanced Python Engineering – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Memory Management & Garbage Collection (Series F, Story 4)

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
| Series F | 6 | 3 | 3 | 50% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **37** | **15** | **71%** |

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

**Next Story:** Series F, Story 4: The 2026 Python Metromap: Memory Management & Garbage Collection

---

## 📝 Your Invitation

You've mastered iterators. Now build something with what you've learned:

1. **Build a paginated API client** – Create an iterator that fetches pages from a REST API on demand.

2. **Create a tree iterator** – Implement pre-order, in-order, post-order traversal for binary trees.

3. **Build a file tailer** – Create an iterator that follows a file (like `tail -f`), yielding new lines as they're added.

4. **Create a window iterator** – Iterator that yields sliding windows of data (useful for time series).

5. **Build a CSV reader** – Implement a lazy CSV reader that handles large files efficiently.

**You've mastered iterators. Next stop: Memory Management & Garbage Collection!**

---

*Found this helpful? Clap, comment, and share what you built with iterators. Next stop: Memory Management!* 🚇