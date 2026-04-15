# The 2026 Python Metromap: Generators – Memory-Efficient Loops

## Series F: Advanced Python Engineering | Story 2 of 6

![The 2026 Python Metromap/images/Generators – Memory-Efficient Loops](images/Generators – Memory-Efficient Loops.png)

## 📖 Introduction

**Welcome to the second stop on the Advanced Python Engineering Line.**

You've mastered decorators—wrapping functions to add behavior without modifying code. You can add logging, timing, authentication, and caching with simple `@decorator` syntax. But there's another advanced pattern that transforms how you handle data: generators.

Generators are functions that produce values one at a time, on demand, rather than computing all values at once and storing them in memory. They're perfect for processing large datasets that don't fit in memory, streaming data from APIs, generating infinite sequences, and building efficient data pipelines.

This story—**The 2026 Python Metromap: Generators – Memory-Efficient Loops**—is your guide to mastering generators in Python. We'll start with generator functions using `yield`. We'll explore generator expressions for concise generation. We'll build a complete CSV streaming processor that handles files larger than RAM. We'll create an infinite data stream generator for real-time analytics. We'll implement a paginated API client that lazily fetches pages. And we'll build a complete data pipeline that chains multiple generators together.

**Let's generate efficiently.**

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

- 🔄 **The 2026 Python Metromap: Generators – Memory-Efficient Loops** – Streaming large CSV files; paginated API responses; infinite data streams. **⬅️ YOU ARE HERE**

- 🔁 **The 2026 Python Metromap: Iterators – Custom Looping** – Database paginator; file chunk reader; Fibonacci sequence iterator. 🔜 *Up Next*

- 🧠 **The 2026 Python Metromap: Memory Management & Garbage Collection** – Optimizing a recommendation engine; memory profiling; leak fixing.

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports.

- 📝 **The 2026 Python Metromap: Type Hints & MyPy** – Large team codebase annotations; pre-runtime bug catching; automatic documentation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔄 Section 1: Generator Basics – The yield Keyword

Generators are functions that use `yield` instead of `return`. They produce values lazily, one at a time, preserving state between calls.

**SOLID Principle Applied: Single Responsibility** – Generators produce one value at a time on demand.

**Design Pattern: Iterator Pattern** – Generators implement the iterator protocol automatically.

```python
"""
GENERATOR BASICS: THE yield KEYWORD

This section covers the fundamentals of generator functions.

SOLID Principle: Single Responsibility
- Generators produce one value at a time on demand

Design Pattern: Iterator Pattern
- Generators implement the iterator protocol automatically
"""

import time
import sys
from typing import Generator, List, Any


def demonstrate_basic_generators():
    """
    Demonstrates basic generator functions using yield.
    
    A generator function returns a generator object that can be iterated.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC GENERATORS")
    print("=" * 60)
    
    # SIMPLE GENERATOR
    print("\n1. SIMPLE GENERATOR FUNCTION")
    print("-" * 40)
    
    def count_up_to(n: int) -> Generator[int, None, None]:
        """Generator that counts from 1 to n."""
        i = 1
        while i <= n:
            yield i
            i += 1
    
    # Create generator object
    counter = count_up_to(5)
    print(f"  Generator object: {counter}")
    print(f"  Type: {type(counter).__name__}")
    
    # Iterate using next()
    print(f"  next(counter): {next(counter)}")
    print(f"  next(counter): {next(counter)}")
    print(f"  next(counter): {next(counter)}")
    
    # Iterate using for loop
    print("\n  Iterating with for loop:")
    for num in count_up_to(3):
        print(f"    {num}")
    
    # MEMORY EFFICIENCY DEMONSTRATION
    print("\n2. MEMORY EFFICIENCY (vs list)")
    print("-" * 40)
    
    def list_squares(n: int) -> List[int]:
        """Returns list of squares (uses memory for all)."""
        result = []
        for i in range(n):
            result.append(i ** 2)
        return result
    
    def generator_squares(n: int) -> Generator[int, None, None]:
        """Generator of squares (produces one at a time)."""
        for i in range(n):
            yield i ** 2
    
    n = 1000000
    list_size = sys.getsizeof(list_squares(1000))  # Just for comparison
    gen = generator_squares(1000)
    gen_size = sys.getsizeof(gen)
    
    print(f"  List memory: {list_size:,} bytes for 1,000 items")
    print(f"  Generator memory: {gen_size:,} bytes (constant)")
    print("  💡 Generators use O(1) memory regardless of sequence length")
    
    # GENERATOR WITH MULTIPLE YIELDS
    print("\n3. GENERATOR WITH MULTIPLE YIELDS")
    print("-" * 40)
    
    def multi_yield():
        """Generator with multiple yield statements."""
        print("  Starting generator")
        yield 1
        print("  After first yield")
        yield 2
        print("  After second yield")
        yield 3
        print("  Generator finished")
    
    gen = multi_yield()
    print(f"  next(): {next(gen)}")
    print(f"  next(): {next(gen)}")
    print(f"  next(): {next(gen)}")
    
    # GENERATOR EXPRESSIONS
    print("\n4. GENERATOR EXPRESSIONS (tuple comprehension)")
    print("-" * 40)
    
    # List comprehension (eager)
    squares_list = [x ** 2 for x in range(10)]
    print(f"  List comprehension: {squares_list} (uses memory)")
    
    # Generator expression (lazy)
    squares_gen = (x ** 2 for x in range(10))
    print(f"  Generator expression: {squares_gen}")
    print(f"  Convert to list: {list(squares_gen)}")
    
    # MEMORY COMPARISON: LIST COMPREHENSION VS GENERATOR
    print("\n5. MEMORY COMPARISON (Large data)")
    print("-" * 40)
    
    import tracemalloc
    
    # List comprehension
    tracemalloc.start()
    large_list = [i for i in range(1000000)]
    list_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    # Generator expression
    tracemalloc.start()
    large_gen = (i for i in range(1000000))
    gen_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    print(f"  List memory: {list_memory / 1024:.1f} KB")
    print(f"  Generator memory: {gen_memory / 1024:.1f} KB")
    print(f"  Generator is {list_memory / max(gen_memory, 1):.0f}x more memory efficient!")


def demonstrate_generator_protocol():
    """
    Demonstrates the generator protocol: send(), throw(), close().
    
    Generators support bidirectional communication and exception handling.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: GENERATOR PROTOCOL (send, throw, close)")
    print("=" * 60)
    
    # GENERATOR WITH send()
    print("\n1. send() - Sending values into generator")
    print("-" * 40)
    
    def accumulator() -> Generator[int, int, str]:
        """Generator that accumulates sent values."""
        total = 0
        while True:
            value = yield total
            if value is None:
                break
            total += value
        return f"Total: {total}"
    
    acc = accumulator()
    
    # Prime the generator (first next() to reach yield)
    print(f"  First next(): {next(acc)}")
    
    # Send values
    print(f"  send(10): {acc.send(10)}")
    print(f"  send(20): {acc.send(20)}")
    print(f"  send(30): {acc.send(30)}")
    
    try:
        acc.send(None)  # Stop the generator
    except StopIteration as e:
        print(f"  Generator returned: {e.value}")
    
    # GENERATOR WITH throw()
    print("\n2. throw() - Raising exception inside generator")
    print("-" * 40)
    
    def safe_divide() -> Generator[float, float, None]:
        """Generator that divides numbers safely."""
        while True:
            try:
                numerator = yield
                denominator = yield
                result = numerator / denominator
                yield result
            except ZeroDivisionError:
                yield float('inf')
            except ValueError:
                yield 0.0
    
    divider = safe_divide()
    next(divider)  # Prime
    
    print(f"  Send numerator 10: {divider.send(10)}")
    print(f"  Send denominator 2: {divider.send(2)}")
    print(f"  Result: {next(divider)}")
    
    # Reset
    next(divider)
    print(f"  Send numerator 10: {divider.send(10)}")
    print(f"  Send denominator 0: {divider.send(0)}")
    print(f"  Result (inf): {next(divider)}")
    
    # GENERATOR WITH close()
    print("\n3. close() - Stopping generator")
    print("-" * 40)
    
    def infinite_counter() -> Generator[int, None, None]:
        """Infinite counter generator."""
        i = 0
        try:
            while True:
                yield i
                i += 1
        finally:
            print("  Generator cleaned up")
    
    counter = infinite_counter()
    print(f"  First: {next(counter)}")
    print(f"  Second: {next(counter)}")
    print(f"  Third: {next(counter)}")
    counter.close()
    
    # GENERATOR WITH yield from (delegation)
    print("\n4. yield from - Delegating to subgenerator")
    print("-" * 40)
    
    def subgen():
        """Subgenerator."""
        yield 1
        yield 2
        yield 3
    
    def delegator():
        """Generator that delegates to subgenerator."""
        yield "Start"
        yield from subgen()
        yield "End"
    
    for value in delegator():
        print(f"  {value}")
    
    # RECURSIVE GENERATOR (yield from for recursion)
    print("\n5. RECURSIVE GENERATOR with yield from")
    print("-" * 40)
    
    def flatten(nested_list: List) -> Generator[Any, None, None]:
        """Flatten nested lists recursively."""
        for item in nested_list:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    
    nested = [1, [2, 3], [4, [5, 6]], 7]
    flattened = list(flatten(nested))
    print(f"  Nested: {nested}")
    print(f"  Flattened: {flattened}")


def demonstrate_practical_generators():
    """
    Demonstrates practical use cases for generators.
    
    - Reading large files line by line
    - Generating infinite sequences
    - Lazy evaluation pipelines
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: PRACTICAL GENERATORS")
    print("=" * 60)
    
    # READING LARGE FILES LINE BY LINE
    print("\n1. READING LARGE FILES (memory efficient)")
    print("-" * 40)
    
    # Create a large file
    with open("large_file.txt", "w") as f:
        for i in range(1000):
            f.write(f"Line {i}: This is some content\n")
    print("  Created large_file.txt with 1000 lines")
    
    def read_large_file(filepath: str) -> Generator[str, None, None]:
        """Generator that reads file line by line."""
        with open(filepath, 'r') as f:
            for line in f:
                yield line.strip()
    
    # Process only first 5 lines
    print("  Reading first 5 lines:")
    for i, line in enumerate(read_large_file("large_file.txt")):
        if i >= 5:
            break
        print(f"    {line}")
    
    # INFINITE SEQUENCES
    print("\n2. INFINITE SEQUENCES (Fibonacci)")
    print("-" * 40)
    
    def fibonacci() -> Generator[int, None, None]:
        """Generate infinite Fibonacci sequence."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    fib = fibonacci()
    print("  First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"    {next(fib)}")
    
    # PRIME NUMBER GENERATOR
    print("\n3. PRIME NUMBER GENERATOR")
    print("-" * 40)
    
    def primes() -> Generator[int, None, None]:
        """Generate prime numbers infinitely."""
        yield 2
        n = 3
        while True:
            is_prime = True
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n
            n += 2
    
    prime_gen = primes()
    print("  First 10 primes:")
    for i in range(10):
        print(f"    {next(prime_gen)}")
    
    # LAZY EVALUATION PIPELINE
    print("\n4. LAZY EVALUATION PIPELINE")
    print("-" * 40)
    
    def numbers(start: int = 0) -> Generator[int, None, None]:
        """Infinite number generator."""
        n = start
        while True:
            yield n
            n += 1
    
    def filter_even(source: Generator) -> Generator:
        """Filter even numbers."""
        for value in source:
            if value % 2 == 0:
                yield value
    
    def square(source: Generator) -> Generator:
        """Square numbers."""
        for value in source:
            yield value ** 2
    
    def take(n: int, source: Generator) -> List:
        """Take first n items from generator."""
        result = []
        for i, value in enumerate(source):
            if i >= n:
                break
            result.append(value)
        return result
    
    # Pipeline: numbers → filter_even → square → take(10)
    pipeline = take(10, square(filter_even(numbers())))
    print(f"  First 10 even squares: {pipeline}")
    
    # CHAINING GENERATORS
    print("\n5. CHAINING GENERATORS (data pipeline)")
    print("-" * 40)
    
    def read_logs() -> Generator[str, None, None]:
        """Simulate reading log entries."""
        logs = [
            "2024-01-15 ERROR Failed to connect",
            "2024-01-15 INFO User logged in",
            "2024-01-15 ERROR Timeout occurred",
            "2024-01-15 WARNING High memory usage"
        ]
        for log in logs:
            yield log
    
    def filter_errors(source: Generator) -> Generator:
        """Filter only error logs."""
        for log in source:
            if "ERROR" in log:
                yield log
    
    def extract_message(source: Generator) -> Generator:
        """Extract error message."""
        for log in source:
            parts = log.split(" ", 2)
            if len(parts) >= 3:
                yield parts[2]
    
    errors = extract_message(filter_errors(read_logs()))
    print("  Error messages:")
    for error in errors:
        print(f"    {error}")
    
    import os
    os.remove("large_file.txt")
    print("\n  Cleaned up test file")


if __name__ == "__main__":
    demonstrate_basic_generators()
    demonstrate_generator_protocol()
    demonstrate_practical_generators()
```

---

## 📊 Section 2: CSV Streaming Processor

A complete CSV streaming processor that handles files larger than RAM using generators.

**SOLID Principles Applied:**
- Single Responsibility: Each generator handles one transformation
- Dependency Inversion: Pipeline depends on generator abstraction

**Design Patterns:**
- Pipeline Pattern: Data flows through generator stages
- Lazy Loading Pattern: Data loaded on demand

```python
"""
CSV STREAMING PROCESSOR

This section builds a CSV streaming processor using generators.

SOLID Principles Applied:
- Single Responsibility: Each generator handles one transformation
- Dependency Inversion: Pipeline depends on generator abstraction

Design Patterns:
- Pipeline Pattern: Data flows through generator stages
- Lazy Loading Pattern: Data loaded on demand
"""

import csv
import io
from typing import Dict, List, Any, Generator, Optional, Callable
from datetime import datetime
import os


class CSVStreamReader:
    """
    Streaming CSV reader using generators.
    
    Reads CSV files row by row without loading entire file into memory.
    """
    
    def __init__(self, filepath: str, chunk_size: int = 8192):
        self.filepath = filepath
        self.chunk_size = chunk_size
    
    def read_rows(self) -> Generator[Dict[str, Any], None, None]:
        """
        Read CSV rows as dictionaries, one at a time.
        
        Yields:
            Dictionary representing one CSV row
        """
        with open(self.filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row
    
    def read_chunks(self) -> Generator[List[Dict], None, None]:
        """
        Read CSV in chunks (batches of rows).
        
        Yields:
            List of dictionaries (chunk of rows)
        """
        chunk = []
        for row in self.read_rows():
            chunk.append(row)
            if len(chunk) >= self.chunk_size:
                yield chunk
                chunk = []
        
        if chunk:
            yield chunk
    
    def read_filtered(self, predicate: Callable[[Dict], bool]) -> Generator[Dict, None, None]:
        """
        Read and filter rows on the fly.
        
        Args:
            predicate: Function that returns True for rows to keep
            
        Yields:
            Filtered rows
        """
        for row in self.read_rows():
            if predicate(row):
                yield row


class CSVTransformPipeline:
    """
    CSV transformation pipeline using generators.
    
    Design Pattern: Pipeline Pattern - Data flows through stages
    """
    
    def __init__(self):
        self.stages: List[Callable] = []
    
    def add_stage(self, stage: Callable) -> 'CSVTransformPipeline':
        """Add a transformation stage to the pipeline."""
        self.stages.append(stage)
        return self
    
    def process(self, source: Generator) -> Generator:
        """Process data through all pipeline stages."""
        result = source
        for stage in self.stages:
            result = stage(result)
        return result


class CSVTransformers:
    """Collection of CSV transformation functions."""
    
    @staticmethod
    def convert_types(type_map: Dict[str, type]) -> Callable:
        """Convert field types in each row."""
        def transformer(source: Generator) -> Generator:
            for row in source:
                for field, field_type in type_map.items():
                    if field in row and row[field]:
                        try:
                            if field_type == int:
                                row[field] = int(float(row[field]))
                            elif field_type == float:
                                row[field] = float(row[field])
                            elif field_type == bool:
                                row[field] = row[field].lower() in ('true', 'yes', '1')
                        except (ValueError, TypeError):
                            pass
                yield row
        return transformer
    
    @staticmethod
    def select_fields(fields: List[str]) -> Callable:
        """Select only specified fields."""
        def transformer(source: Generator) -> Generator:
            for row in source:
                yield {k: v for k, v in row.items() if k in fields}
        return transformer
    
    @staticmethod
    def add_computed_field(field_name: str, compute: Callable) -> Callable:
        """Add a computed field to each row."""
        def transformer(source: Generator) -> Generator:
            for row in source:
                row[field_name] = compute(row)
                yield row
        return transformer
    
    @staticmethod
    def filter_rows(predicate: Callable[[Dict], bool]) -> Callable:
        """Filter rows based on predicate."""
        def transformer(source: Generator) -> Generator:
            for row in source:
                if predicate(row):
                    yield row
        return transformer
    
    @staticmethod
    def clean_strings(fields: List[str] = None) -> Callable:
        """Clean string fields (strip whitespace)."""
        def transformer(source: Generator) -> Generator:
            for row in source:
                for key, value in row.items():
                    if fields is None or key in fields:
                        if isinstance(value, str):
                            row[key] = value.strip()
                yield row
        return transformer


class CSVStreamWriter:
    """
    Streaming CSV writer using generators.
    
    Writes CSV rows one at a time without buffering entire dataset.
    """
    
    def __init__(self, filepath: str, fieldnames: List[str] = None):
        self.filepath = filepath
        self.fieldnames = fieldnames
        self._first_row = True
    
    def write_rows(self, rows: Generator) -> int:
        """
        Write rows from a generator to CSV file.
        
        Args:
            rows: Generator yielding dictionaries
            
        Returns:
            Number of rows written
        """
        count = 0
        first_row = True
        
        with open(self.filepath, 'w', newline='') as f:
            writer = None
            
            for row in rows:
                if first_row:
                    if not self.fieldnames:
                        self.fieldnames = list(row.keys())
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                    writer.writeheader()
                    first_row = False
                
                writer.writerow(row)
                count += 1
        
        return count
    
    def write_chunked(self, chunks: Generator, chunk_size: int = 1000) -> int:
        """
        Write chunks of rows to CSV file.
        
        Args:
            chunks: Generator yielding lists of rows
            chunk_size: Size of each chunk
            
        Returns:
            Number of rows written
        """
        total = 0
        first_chunk = True
        
        with open(self.filepath, 'w', newline='') as f:
            writer = None
            
            for chunk in chunks:
                if first_chunk and chunk:
                    if not self.fieldnames:
                        self.fieldnames = list(chunk[0].keys())
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                    writer.writeheader()
                    first_chunk = False
                
                if writer:
                    writer.writerows(chunk)
                    total += len(chunk)
        
        return total


def demonstrate_csv_streaming():
    """
    Demonstrate the CSV streaming processor.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: CSV STREAMING PROCESSOR")
    print("=" * 60)
    
    # Create large sample CSV
    print("\n1. CREATING LARGE SAMPLE CSV")
    print("-" * 40)
    
    sample_data = []
    for i in range(1000):
        sample_data.append({
            "id": i,
            "name": f"User {i}",
            "email": f"user{i}@example.com",
            "age": 20 + (i % 50),
            "city": ["NYC", "LA", "Chicago", "Houston"][i % 4],
            "active": i % 2 == 0,
            "score": 50 + (i % 50)
        })
    
    with open("large_data.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sample_data[0].keys())
        writer.writeheader()
        writer.writerows(sample_data)
    
    print(f"  Created large_data.csv with {len(sample_data)} rows")
    
    # Streaming reader
    print("\n2. STREAMING CSV READER")
    print("-" * 40)
    
    reader = CSVStreamReader("large_data.csv")
    
    print("  Reading first 5 rows:")
    for i, row in enumerate(reader.read_rows()):
        if i >= 5:
            break
        print(f"    {row['id']}: {row['name']} ({row['city']})")
    
    print(f"\n  Total rows in file: {sum(1 for _ in reader.read_rows())}")
    
    # Filtered reading
    print("\n3. FILTERED READING (on the fly)")
    print("-" * 40)
    
    def is_active(row):
        return row['active'] == 'True' or row['active'] == True
    
    active_count = 0
    for row in reader.read_filtered(is_active):
        active_count += 1
    
    print(f"  Active users: {active_count}")
    
    # Chunked reading
    print("\n4. CHUNKED READING")
    print("-" * 40)
    
    chunk_reader = CSVStreamReader("large_data.csv", chunk_size=100)
    chunk_count = 0
    for chunk in chunk_reader.read_chunks():
        chunk_count += 1
        print(f"  Chunk {chunk_count}: {len(chunk)} rows")
    
    # Transformation pipeline
    print("\n5. TRANSFORMATION PIPELINE")
    print("-" * 40)
    
    pipeline = CSVTransformPipeline()
    pipeline.add_stage(CSVTransformers.clean_strings(["name", "email", "city"]))
    pipeline.add_stage(CSVTransformers.convert_types({
        "id": int,
        "age": int,
        "score": int,
        "active": bool
    }))
    pipeline.add_stage(CSVTransformers.add_computed_field("age_group", 
        lambda r: "senior" if r.get("age", 0) >= 60 else "adult" if r.get("age", 0) >= 18 else "minor"))
    pipeline.add_stage(CSVTransformers.add_computed_field("score_level",
        lambda r: "high" if r.get("score", 0) >= 80 else "medium" if r.get("score", 0) >= 60 else "low"))
    pipeline.add_stage(CSVTransformers.filter_rows(lambda r: r.get("active", False)))
    pipeline.add_stage(CSVTransformers.select_fields(["id", "name", "age_group", "score_level", "city"]))
    
    print("  Pipeline configured with:")
    print("    - String cleaning")
    print("    - Type conversion")
    print("    - Computed fields (age_group, score_level)")
    print("    - Filter (active only)")
    print("    - Field selection")
    
    # Process through pipeline
    source = reader.read_rows()
    processed = pipeline.process(source)
    
    print("\n  Processed data (first 5 rows):")
    for i, row in enumerate(processed):
        if i >= 5:
            break
        print(f"    {row}")
    
    # Count processed rows
    source = reader.read_rows()
    processed = pipeline.process(source)
    count = sum(1 for _ in processed)
    print(f"\n  Total processed rows: {count}")
    
    # Streaming write
    print("\n6. STREAMING CSV WRITE")
    print("-" * 40)
    
    source = reader.read_rows()
    processed = pipeline.process(source)
    
    writer = CSVStreamWriter("processed_data.csv")
    rows_written = writer.write_rows(processed)
    print(f"  Wrote {rows_written} rows to processed_data.csv")
    
    # Verify output
    with open("processed_data.csv", "r") as f:
        print(f"  Output preview:")
        for i, line in enumerate(f):
            if i >= 5:
                break
            print(f"    {line.strip()}")
    
    # Clean up
    for f in ["large_data.csv", "processed_data.csv"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up files")


if __name__ == "__main__":
    demonstrate_csv_streaming()
```

---

## 🌊 Section 3: Infinite Data Stream Generator

A system for generating and processing infinite data streams using generators.

**SOLID Principles Applied:**
- Single Responsibility: Each generator produces one type of data
- Open/Closed: New data sources can be added

**Design Patterns:**
- Observer Pattern: Stream consumers observe data
- Producer-Consumer Pattern: Generators produce, consumers process

```python
"""
INFINITE DATA STREAM GENERATOR

This section builds infinite data stream generators.

SOLID Principles Applied:
- Single Responsibility: Each generator produces one type
- Open/Closed: New data sources can be added

Design Patterns:
- Observer Pattern: Stream consumers observe data
- Producer-Consumer Pattern: Generators produce, consumers process
"""

import time
import random
import threading
from typing import Generator, Dict, Any, Callable, List, Optional
from datetime import datetime
from dataclasses import dataclass
from collections import deque
import math


@dataclass
class DataPoint:
    """Data point in a stream."""
    timestamp: datetime
    value: float
    source: str
    metadata: Dict[str, Any]


class DataStreamGenerator:
    """
    Generates infinite data streams.
    
    Design Pattern: Producer Pattern - Produces data continuously
    """
    
    @staticmethod
    def sine_wave(frequency: float = 1.0, amplitude: float = 1.0, 
                  offset: float = 0.0, sample_rate: float = 10.0) -> Generator[DataPoint, None, None]:
        """
        Generate sine wave data stream.
        
        Args:
            frequency: Frequency in Hz
            amplitude: Amplitude of wave
            offset: Vertical offset
            sample_rate: Samples per second
        """
        t = 0.0
        while True:
            value = amplitude * math.sin(2 * math.pi * frequency * t) + offset
            yield DataPoint(
                timestamp=datetime.now(),
                value=value,
                source="sine_wave",
                metadata={"frequency": frequency, "amplitude": amplitude}
            )
            t += 1.0 / sample_rate
            time.sleep(1.0 / sample_rate)
    
    @staticmethod
    def random_walk(initial: float = 0.0, step_size: float = 1.0,
                    sample_rate: float = 10.0) -> Generator[DataPoint, None, None]:
        """
        Generate random walk data stream.
        
        Args:
            initial: Starting value
            step_size: Maximum step size
            sample_rate: Samples per second
        """
        value = initial
        while True:
            value += random.uniform(-step_size, step_size)
            yield DataPoint(
                timestamp=datetime.now(),
                value=value,
                source="random_walk",
                metadata={"step_size": step_size}
            )
            time.sleep(1.0 / sample_rate)
    
    @staticmethod
    def sensor_data(sensor_id: str, base_value: float = 50.0,
                    noise_level: float = 5.0, sample_rate: float = 5.0) -> Generator[DataPoint, None, None]:
        """
        Simulate sensor data with noise.
        
        Args:
            sensor_id: Sensor identifier
            base_value: Base reading value
            noise_level: Random noise amplitude
            sample_rate: Samples per second
        """
        while True:
            value = base_value + random.uniform(-noise_level, noise_level)
            yield DataPoint(
                timestamp=datetime.now(),
                value=value,
                source=f"sensor_{sensor_id}",
                metadata={"base_value": base_value, "noise_level": noise_level}
            )
            time.sleep(1.0 / sample_rate)
    
    @staticmethod
    def stock_price(symbol: str, initial_price: float = 100.0,
                    volatility: float = 0.02, sample_rate: float = 1.0) -> Generator[DataPoint, None, None]:
        """
        Simulate stock price data (geometric Brownian motion).
        
        Args:
            symbol: Stock symbol
            initial_price: Starting price
            volatility: Price volatility
            sample_rate: Samples per second
        """
        price = initial_price
        while True:
            # Random walk with log-normal distribution
            change = random.gauss(0, volatility)
            price *= (1 + change)
            
            yield DataPoint(
                timestamp=datetime.now(),
                value=price,
                source=f"stock_{symbol}",
                metadata={"symbol": symbol, "volatility": volatility}
            )
            time.sleep(1.0 / sample_rate)


class StreamProcessor:
    """
    Processes data streams with windowing and aggregation.
    
    Design Pattern: Consumer Pattern - Consumes and processes data
    """
    
    def __init__(self, window_size: int = 10):
        self.window_size = window_size
        self.buffer: deque = deque(maxlen=window_size)
        self.callbacks: List[Callable] = []
    
    def add_callback(self, callback: Callable) -> 'StreamProcessor':
        """Add callback for processed data."""
        self.callbacks.append(callback)
        return self
    
    def process(self, stream: Generator[DataPoint, None, None]) -> Generator[Dict, None, None]:
        """
        Process stream with sliding window.
        
        Yields:
            Window statistics
        """
        for point in stream:
            self.buffer.append(point.value)
            
            if len(self.buffer) == self.window_size:
                stats = {
                    "timestamp": point.timestamp,
                    "source": point.source,
                    "mean": sum(self.buffer) / self.window_size,
                    "min": min(self.buffer),
                    "max": max(self.buffer),
                    "std": self._std_dev(self.buffer),
                    "window_size": self.window_size
                }
                
                for callback in self.callbacks:
                    callback(stats)
                
                yield stats
    
    def _std_dev(self, data: deque) -> float:
        """Calculate standard deviation."""
        if len(data) < 2:
            return 0.0
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
        return math.sqrt(variance)


class AlertSystem:
    """
    Alert system for stream monitoring.
    
    Design Pattern: Observer Pattern - Observes stream for conditions
    """
    
    def __init__(self):
        self.rules: List[Dict] = []
        self.alerts: List[Dict] = []
    
    def add_rule(self, condition: Callable[[Dict], bool], message: str) -> 'AlertSystem':
        """Add an alert rule."""
        self.rules.append({"condition": condition, "message": message})
        return self
    
    def check(self, data: Dict) -> None:
        """Check data against all rules."""
        for rule in self.rules:
            if rule["condition"](data):
                alert = {
                    "timestamp": datetime.now(),
                    "message": rule["message"],
                    "data": data
                }
                self.alerts.append(alert)
                print(f"  🚨 ALERT: {rule['message']}")
    
    def get_alerts(self, last_n: int = None) -> List[Dict]:
        """Get recent alerts."""
        if last_n:
            return self.alerts[-last_n:]
        return self.alerts


class StreamRecorder:
    """
    Records stream data to memory or file.
    
    Design Pattern: Observer Pattern - Observes and stores data
    """
    
    def __init__(self, max_records: int = 1000):
        self.records: List[DataPoint] = []
        self.max_records = max_records
    
    def record(self, point: DataPoint) -> None:
        """Record a data point."""
        self.records.append(point)
        if len(self.records) > self.max_records:
            self.records.pop(0)
    
    def get_recent(self, n: int = 100) -> List[DataPoint]:
        """Get recent records."""
        return self.records[-n:]
    
    def get_statistics(self) -> Dict:
        """Get statistics of recorded data."""
        if not self.records:
            return {"count": 0}
        
        values = [r.value for r in self.records]
        return {
            "count": len(self.records),
            "min": min(values),
            "max": max(values),
            "mean": sum(values) / len(values),
            "source_counts": self._count_by_source()
        }
    
    def _count_by_source(self) -> Dict:
        """Count records by source."""
        counts = {}
        for record in self.records:
            counts[record.source] = counts.get(record.source, 0) + 1
        return counts


class StreamVisualizer:
    """
    Simple ASCII visualization for data streams.
    
    Design Pattern: Observer Pattern - Visualizes data
    """
    
    def __init__(self, width: int = 50, height: int = 20):
        self.width = width
        self.height = height
        self.data_buffer: deque = deque(maxlen=width)
        self.min_value = float('inf')
        self.max_value = float('-inf')
    
    def update(self, value: float) -> None:
        """Update visualization with new value."""
        self.data_buffer.append(value)
        self.min_value = min(self.min_value, value)
        self.max_value = max(self.max_value, value)
    
    def display(self) -> None:
        """Display ASCII chart."""
        if not self.data_buffer:
            return
        
        # Clear screen (simplified)
        print("\033[2J\033[H", end="")
        
        # Calculate scaling
        value_range = self.max_value - self.min_value
        if value_range == 0:
            value_range = 1
        
        # Draw chart
        for y in range(self.height, 0, -1):
            level = self.min_value + (y / self.height) * value_range
            line = []
            for x, value in enumerate(self.data_buffer):
                if value >= level:
                    line.append("█")
                else:
                    line.append(" ")
            print("".join(line))
        
        # Draw axis
        print("-" * self.width)
        print(f"Min: {self.min_value:.2f} | Max: {self.max_value:.2f}")


def demonstrate_stream_generation():
    """
    Demonstrate infinite data stream generation and processing.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: INFINITE DATA STREAM GENERATOR")
    print("=" * 60)
    
    print("\n1. GENERATING DATA STREAMS")
    print("-" * 40)
    
    # Sine wave generator
    print("  Sine wave stream (5 samples):")
    sine_gen = DataStreamGenerator.sine_wave(frequency=0.5, amplitude=2, sample_rate=5)
    for i, point in enumerate(sine_gen):
        if i >= 5:
            break
        print(f"    {point.timestamp.strftime('%H:%M:%S.%f')[:-3]}: {point.value:.3f}")
    
    # Random walk generator
    print("\n  Random walk stream (5 samples):")
    walk_gen = DataStreamGenerator.random_walk(initial=0, step_size=1, sample_rate=5)
    for i, point in enumerate(walk_gen):
        if i >= 5:
            break
        print(f"    {point.timestamp.strftime('%H:%M:%S.%f')[:-3]}: {point.value:.3f}")
    
    print("\n2. STREAM PROCESSING (Moving Window)")
    print("-" * 40)
    
    # Create processor
    processor = StreamProcessor(window_size=5)
    
    # Add callback for alerting
    def on_stats(stats):
        if stats['mean'] > 1.5:
            print(f"    🔔 Mean exceeded threshold: {stats['mean']:.3f}")
    
    processor.add_callback(on_stats)
    
    # Process stream
    stream = DataStreamGenerator.sine_wave(frequency=0.5, amplitude=2, sample_rate=5)
    print("  Processing sine wave (showing window stats):")
    for i, stats in enumerate(processor.process(stream)):
        if i >= 10:
            break
        print(f"    Window {i+1}: mean={stats['mean']:.3f}, min={stats['min']:.3f}, max={stats['max']:.3f}")
    
    print("\n3. ALERT SYSTEM")
    print("-" * 40)
    
    alert_system = AlertSystem()
    alert_system.add_rule(lambda s: s['max'] > 1.8, "High value detected!")
    alert_system.add_rule(lambda s: s['min'] < -1.8, "Low value detected!")
    alert_system.add_rule(lambda s: s['std'] > 0.5, "High volatility detected!")
    
    processor2 = StreamProcessor(window_size=5)
    stream2 = DataStreamGenerator.sine_wave(frequency=0.5, amplitude=2, sample_rate=5)
    
    print("  Monitoring stream for conditions:")
    for i, stats in enumerate(processor2.process(stream2)):
        alert_system.check(stats)
        if i >= 15:
            break
    
    alerts = alert_system.get_alerts()
    print(f"  Total alerts: {len(alerts)}")
    
    print("\n4. STREAM RECORDING")
    print("-" * 40)
    
    recorder = StreamRecorder(max_records=20)
    stream3 = DataStreamGenerator.sensor_data("temp", base_value=72, noise_level=3, sample_rate=4)
    
    for i, point in enumerate(stream3):
        recorder.record(point)
        if i >= 15:
            break
    
    stats = recorder.get_statistics()
    print(f"  Recorded {stats['count']} data points")
    print(f"  Temperature range: {stats['min']:.1f}°F - {stats['max']:.1f}°F")
    print(f"  Average: {stats['mean']:.1f}°F")
    
    print("\n5. MULTIPLE STREAMS (Producer-Consumer)")
    print("-" * 40)
    
    class StreamManager:
        """Manages multiple streams."""
        
        def __init__(self):
            self.streams: List[Generator] = []
            self.consumers: List[Callable] = []
        
        def add_stream(self, stream: Generator) -> 'StreamManager':
            self.streams.append(stream)
            return self
        
        def add_consumer(self, consumer: Callable) -> 'StreamManager':
            self.consumers.append(consumer)
            return self
        
        def run(self, duration_seconds: float = 2.0):
            """Run all streams for specified duration."""
            start_time = time.time()
            
            while time.time() - start_time < duration_seconds:
                for stream in self.streams:
                    try:
                        data = next(stream)
                        for consumer in self.consumers:
                            consumer(data)
                    except StopIteration:
                        pass
                
                time.sleep(0.01)  # Small delay
    
    # Create multiple streams
    manager = StreamManager()
    manager.add_stream(DataStreamGenerator.sensor_data("temp", 72, 2, 5))
    manager.add_stream(DataStreamGenerator.sensor_data("humidity", 45, 3, 5))
    manager.add_stream(DataStreamGenerator.random_walk(0, 0.5, 5))
    
    # Simple consumer
    def print_data(point: DataPoint):
        print(f"    {point.source}: {point.value:.2f}")
    
    manager.add_consumer(print_data)
    
    print("  Running multiple streams for 2 seconds:")
    manager.run(2.0)
    
    print("\n6. VISUALIZATION (ASCII)")
    print("-" * 40)
    print("  (Simplified visualization - would display in real terminal)")
    print("  Visualizer would show real-time ASCII chart of stream data")


if __name__ == "__main__":
    demonstrate_stream_generation()
```

---

## 🔌 Section 4: Paginated API Client

A complete API client that uses generators to lazily fetch paginated results.

**SOLID Principles Applied:**
- Single Responsibility: Each generator handles one pagination strategy
- Dependency Inversion: Client depends on generator abstraction

**Design Patterns:**
- Iterator Pattern: Iterates through pages lazily
- Lazy Loading Pattern: Fetches pages on demand

```python
"""
PAGINATED API CLIENT

This section builds an API client that uses generators for pagination.

SOLID Principles Applied:
- Single Responsibility: Each generator handles one pagination strategy
- Dependency Inversion: Client depends on generator abstraction

Design Patterns:
- Iterator Pattern: Iterates through pages lazily
- Lazy Loading Pattern: Fetches pages on demand
"""

import time
import json
import random
from typing import Dict, List, Any, Generator, Optional, Callable
from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class PaginationType(Enum):
    """Types of pagination."""
    OFFSET = "offset"
    CURSOR = "cursor"
    PAGE_NUMBER = "page_number"


@dataclass
class APIResponse:
    """API response wrapper."""
    data: Any
    next_cursor: Optional[str] = None
    has_more: bool = False
    total: Optional[int] = None
    page: Optional[int] = None


class MockAPIClient:
    """
    Mock API client for demonstration.
    
    Simulates paginated API endpoints.
    """
    
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url
        self.call_count = 0
    
    def get_users(self, page: int = 1, page_size: int = 10, cursor: str = None) -> APIResponse:
        """Get users with pagination."""
        self.call_count += 1
        time.sleep(0.05)  # Simulate network delay
        
        # Generate users
        start = (page - 1) * page_size if page else 0
        if cursor:
            start = int(cursor) if cursor.isdigit() else 0
        
        users = []
        for i in range(start, start + page_size):
            users.append({
                "id": i + 1,
                "name": f"User {i + 1}",
                "email": f"user{i + 1}@example.com",
                "created_at": datetime.now().isoformat()
            })
        
        total = 100
        has_more = (start + page_size) < total
        
        return APIResponse(
            data=users,
            next_cursor=str(start + page_size) if has_more else None,
            has_more=has_more,
            total=total,
            page=page
        )
    
    def get_orders(self, user_id: int, limit: int = 20, offset: int = 0) -> APIResponse:
        """Get orders for a user."""
        self.call_count += 1
        time.sleep(0.03)
        
        # Generate orders
        orders = []
        for i in range(offset, min(offset + limit, 100)):
            orders.append({
                "id": i + 1,
                "user_id": user_id,
                "amount": random.uniform(10, 500),
                "status": random.choice(["pending", "shipped", "delivered"])
            })
        
        has_more = (offset + limit) < 100
        
        return APIResponse(
            data=orders,
            has_more=has_more,
            total=100
        )
    
    def get_products(self, category: str = None, cursor: str = None) -> APIResponse:
        """Get products with cursor pagination."""
        self.call_count += 1
        time.sleep(0.04)
        
        # Simulate cursor-based pagination
        products = {
            "electronics": [
                {"id": "e1", "name": "Laptop", "price": 999},
                {"id": "e2", "name": "Phone", "price": 699},
                {"id": "e3", "name": "Tablet", "price": 399}
            ],
            "books": [
                {"id": "b1", "name": "Python Book", "price": 49},
                {"id": "b2", "name": "Data Science", "price": 59},
                {"id": "b3", "name": "AI Guide", "price": 69}
            ]
        }
        
        data = products.get(category, products["electronics"])
        
        return APIResponse(
            data=data,
            has_more=False
        )
    
    def get_stats(self) -> Dict:
        """Get API call statistics."""
        return {"total_calls": self.call_count}


class PaginatedIterator:
    """
    Iterator for paginated API endpoints.
    
    Design Pattern: Iterator Pattern - Lazy page iteration
    """
    
    def __init__(self, client: MockAPIClient, endpoint: str, **params):
        self.client = client
        self.endpoint = endpoint
        self.params = params
        self.page = 1
        self.cursor = None
        self.has_more = True
        self.total_fetched = 0
        self.current_page_data = []
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # Get next page if needed
        if self.current_index >= len(self.current_page_data):
            if not self.has_more:
                raise StopIteration
            
            self._fetch_next_page()
            
            if not self.current_page_data:
                raise StopIteration
            
            self.current_index = 0
        
        item = self.current_page_data[self.current_index]
        self.current_index += 1
        self.total_fetched += 1
        return item
    
    def _fetch_next_page(self):
        """Fetch the next page of results."""
        if self.endpoint == "users":
            response = self.client.get_users(page=self.page, **self.params)
            self.current_page_data = response.data
            self.has_more = response.has_more
            self.page += 1
        
        elif self.endpoint == "orders":
            offset = self.total_fetched
            response = self.client.get_orders(offset=offset, **self.params)
            self.current_page_data = response.data
            self.has_more = response.has_more
        
        elif self.endpoint == "products":
            response = self.client.get_products(**self.params)
            self.current_page_data = response.data
            self.has_more = False
    
    def get_stats(self) -> Dict:
        """Get iteration statistics."""
        return {
            "total_fetched": self.total_fetched,
            "pages_loaded": self.page - 1,
            "has_more": self.has_more
        }


def paginate_offset(client: MockAPIClient, endpoint: str, 
                    page_size: int = 10, **params) -> Generator[Dict, None, None]:
    """
    Generator for offset-based pagination.
    
    Yields:
        Items one by one, fetching pages as needed.
    """
    page = 1
    has_more = True
    
    while has_more:
        if endpoint == "users":
            response = client.get_users(page=page, page_size=page_size, **params)
        elif endpoint == "orders":
            offset = (page - 1) * page_size
            response = client.get_orders(offset=offset, limit=page_size, **params)
        else:
            break
        
        for item in response.data:
            yield item
        
        has_more = response.has_more
        page += 1
        
        # Small delay between pages
        time.sleep(0.01)


def paginate_cursor(client: MockAPIClient, endpoint: str, 
                    **params) -> Generator[Dict, None, None]:
    """
    Generator for cursor-based pagination.
    
    Yields:
        Items one by one, fetching pages as needed.
    """
    cursor = None
    has_more = True
    
    while has_more:
        if endpoint == "products":
            response = client.get_products(cursor=cursor, **params)
        else:
            break
        
        for item in response.data:
            yield item
        
        cursor = response.next_cursor
        has_more = response.has_more and cursor is not None


class APIPipeline:
    """
    API data pipeline with transformations.
    
    Design Pattern: Pipeline Pattern - Chains transformations
    """
    
    def __init__(self, source: Generator):
        self.source = source
        self.transformations: List[Callable] = []
    
    def map(self, func: Callable) -> 'APIPipeline':
        """Apply transformation to each item."""
        self.transformations.append(func)
        return self
    
    def filter(self, predicate: Callable) -> 'APIPipeline':
        """Filter items."""
        def filter_transform(items):
            for item in items:
                if predicate(item):
                    yield item
        
        self.transformations.append(filter_transform)
        return self
    
    def take(self, n: int) -> List:
        """Take first n items and execute pipeline."""
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
        """Collect all items (use with caution for large datasets)."""
        items = self.source
        for transform in self.transformations:
            items = transform(items)
        return list(items)


def demonstrate_paginated_client():
    """
    Demonstrate the paginated API client.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: PAGINATED API CLIENT")
    print("=" * 60)
    
    client = MockAPIClient()
    
    print("\n1. MANUAL PAGINATION (Offset-based)")
    print("-" * 40)
    
    # Fetch first 2 pages of users
    print("  Users (first 2 pages):")
    page1 = client.get_users(page=1, page_size=5)
    for user in page1.data:
        print(f"    {user['id']}: {user['name']}")
    
    page2 = client.get_users(page=2, page_size=5)
    for user in page2.data:
        print(f"    {user['id']}: {user['name']}")
    
    print(f"\n  API calls: {client.get_stats()['total_calls']}")
    
    print("\n2. GENERATOR-BASED PAGINATION (Lazy loading)")
    print("-" * 40)
    
    # Reset call count
    client = MockAPIClient()
    
    user_gen = paginate_offset(client, "users", page_size=10)
    
    print("  Fetching first 15 users lazily:")
    for i, user in enumerate(user_gen):
        if i >= 15:
            break
        print(f"    {user['id']}: {user['name']}")
    
    print(f"\n  API calls made: {client.get_stats()['total_calls']}")
    
    print("\n3. PAGINATED ITERATOR (Object-oriented)")
    print("-" * 40)
    
    client = MockAPIClient()
    user_iter = PaginatedIterator(client, "users", page_size=15)
    
    print("  First 20 users from iterator:")
    for i, user in enumerate(user_iter):
        if i >= 20:
            break
        print(f"    {user['id']}: {user['name']}")
    
    stats = user_iter.get_stats()
    print(f"\n  Iterator stats: {stats}")
    print(f"  API calls: {client.get_stats()['total_calls']}")
    
    print("\n4. DATA PIPELINE WITH TRANSFORMATIONS")
    print("-" * 40)
    
    client = MockAPIClient()
    user_gen = paginate_offset(client, "users", page_size=20)
    
    pipeline = APIPipeline(user_gen)
    pipeline.filter(lambda u: u['id'] % 2 == 0)  # Even IDs only
    pipeline.map(lambda u: {**u, 'name_upper': u['name'].upper()})
    pipeline.map(lambda u: {**u, 'is_even': True})
    
    results = pipeline.take(10)
    print("  Processed users (even IDs, uppercase names):")
    for user in results:
        print(f"    {user['id']}: {user['name_upper']}")
    
    print("\n5. CURSOR-BASED PAGINATION")
    print("-" * 40)
    
    client = MockAPIClient()
    product_gen = paginate_cursor(client, "products", category="electronics")
    
    print("  Products:")
    for product in product_gen:
        print(f"    {product['name']}: ${product['price']}")
    
    print("\n6. ORDER PAGINATION WITH FILTERING")
    print("-" * 40)
    
    client = MockAPIClient()
    order_gen = paginate_offset(client, "orders", page_size=15, user_id=1)
    
    # Pipeline for orders
    pipeline = APIPipeline(order_gen)
    pipeline.filter(lambda o: o['status'] == 'delivered')
    pipeline.map(lambda o: {**o, 'amount_with_tax': round(o['amount'] * 1.08, 2)})
    
    delivered_orders = pipeline.take(10)
    print(f"  Delivered orders for user 1:")
    for order in delivered_orders:
        print(f"    Order {order['id']}: ${order['amount']:.2f} + tax = ${order['amount_with_tax']:.2f}")
    
    print("\n7. PERFORMANCE COMPARISON")
    print("-" * 40)
    
    # Eager loading (load all at once)
    client = MockAPIClient()
    start = time.time()
    
    all_users = []
    page = 1
    has_more = True
    while has_more:
        response = client.get_users(page=page, page_size=50)
        all_users.extend(response.data)
        has_more = response.has_more
        page += 1
    
    eager_time = time.time() - start
    eager_calls = client.get_stats()['total_calls']
    
    # Lazy loading (generator)
    client = MockAPIClient()
    start = time.time()
    
    user_gen = paginate_offset(client, "users", page_size=50)
    lazy_users = []
    for user in user_gen:
        lazy_users.append(user)
    
    lazy_time = time.time() - start
    lazy_calls = client.get_stats()['total_calls']
    
    print(f"  Eager loading: {eager_time:.2f}s, {eager_calls} API calls")
    print(f"  Lazy loading: {lazy_time:.2f}s, {lazy_calls} API calls")
    print(f"  Both fetched {len(all_users)} users")
    print("  💡 Lazy loading is faster for partial consumption")


if __name__ == "__main__":
    demonstrate_paginated_client()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Generator Functions** – Use `yield` instead of `return`. Preserve state between calls. Produce values lazily.

- **Memory Efficiency** – Generators use O(1) memory regardless of sequence length. Perfect for large datasets.

- **Generator Expressions** – `(expr for item in iterable)` – lazy version of list comprehension.

- **Generator Protocol** – `send()` sends values into generator. `throw()` raises exceptions. `close()` stops generator.

- **`yield from`** – Delegate to subgenerator. Flatten nested structures. Chain generators.

- **Infinite Sequences** – Generators can produce infinite streams (Fibonacci, primes, random walks).

- **CSV Streaming** – Process CSV files row by row. Transform pipeline with multiple stages. Filter, map, aggregate.

- **Data Streams** – Real-time data generation (sine wave, random walk, sensor data). Window processing, alerts.

- **Paginated API** – Lazy fetch pages. Offset and cursor pagination. API pipeline with transformations.

- **SOLID Principles Applied** – Single Responsibility (each generator does one thing), Dependency Inversion (pipelines depend on generators), Open/Closed (new transformations can be added).

- **Design Patterns Used** – Iterator Pattern (lazy iteration), Pipeline Pattern (data flow), Producer-Consumer Pattern (stream generation), Observer Pattern (alerts, recording), Lazy Loading Pattern (on-demand fetching).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Decorators – Wrapping Functions

- **📚 Series F Catalog:** Advanced Python Engineering – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Iterators – Custom Looping (Series F, Story 3)

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
| Series F | 6 | 2 | 4 | 33% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **36** | **16** | **69%** |

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

**Next Story:** Series F, Story 3: The 2026 Python Metromap: Iterators – Custom Looping

---

## 📝 Your Invitation

You've mastered generators. Now build something with what you've learned:

1. **Build a log file tailer** – Generator that yields new lines as they're added to a file (like `tail -f`).

2. **Create a data sampler** – Generator that samples every Nth item from a stream.

3. **Build a rate limiter** – Generator that limits the rate of data production.

4. **Create a data deduplicator** – Generator that removes consecutive duplicates from a stream.

5. **Build a moving average calculator** – Generator that yields running average of last N values.

**You've mastered generators. Next stop: Iterators!**

---

*Found this helpful? Clap, comment, and share what you built with generators. Next stop: Iterators!* 🚇