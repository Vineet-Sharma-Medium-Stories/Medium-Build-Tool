# The 2026 Python Metromap: Loops – for, while, break, continue

## Series A: Foundations Station | Story 5 of 7

![The 2026 Python Metromap/images/Loops – for, while, break, continue](images/Loops – for, while, break, continue.png)

## 📖 Introduction

**Welcome to the fifth stop on the Foundations Station Line.**

You've mastered variables, collections, operators, and control flow. You can store data, transform it, compare values, and make decisions. But what happens when you need to repeat an operation—processing every item in a list, retrying a failed network request, or paginating through thousands of records?

That's where loops come in.

Loops are the engines of repetition. The for loop iterates over sequences—lists, strings, dictionaries, ranges. The while loop repeats as long as a condition remains True. Break exits a loop early. Continue skips to the next iteration. Together, they automate repetitive tasks and process data at scale.

This story—**The 2026 Python Metromap: Loops – for, while, break, continue**—is your guide to iteration in Python. We'll build a batch file processor that handles thousands of files. We'll create an API retry mechanism with exponential backoff. We'll implement a pagination system for large datasets. And we'll build a complete order processing system that validates, processes, and reports on bulk orders.

**Let's start the repetition.**

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

- 🔁 **The 2026 Python Metromap: Loops – for, while, break, continue** – Batch file processor; API retry mechanism; pagination system. **⬅️ YOU ARE HERE**

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter. 🔜 *Up Next*

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔁 Section 1: The for Loop – Iterating Over Sequences

The for loop iterates over any iterable object—lists, tuples, strings, dictionaries, ranges, and more.

**SOLID Principle Applied: Single Responsibility** – Each for loop has one clear iteration purpose.

**Design Pattern: Iterator Pattern** – The for loop uses Python's iterator protocol to traverse collections.

```python
"""
THE FOR LOOP: ITERATING OVER SEQUENCES

This section covers the for loop and its various applications.

SOLID Principle: Single Responsibility
- Each for loop has one clear iteration purpose

Design Pattern: Iterator Pattern
- Uses Python's iterator protocol to traverse collections
"""

from typing import List, Dict, Any, Tuple
from datetime import datetime
import time


def demonstrate_for_loop_basics():
    """
    Demonstrates basic for loop syntax and usage.
    
    The for loop iterates over each item in a sequence.
    """
    print("=" * 60)
    print("SECTION 1A: FOR LOOP BASICS")
    print("=" * 60)
    
    # ITERATING OVER LISTS
    print("\n1. ITERATING OVER LISTS")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("Fruits list:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # ITERATING OVER STRINGS
    print("\n2. ITERATING OVER STRINGS")
    print("-" * 40)
    
    word = "Python"
    print(f"Characters in '{word}':")
    for char in word:
        print(f"  '{char}'")
    
    # ITERATING OVER TUPLES
    print("\n3. ITERATING OVER TUPLES")
    print("-" * 40)
    
    coordinates = [(10, 20), (30, 40), (50, 60)]
    
    for x, y in coordinates:
        print(f"  Point: ({x}, {y})")
    
    # ITERATING OVER DICTIONARIES
    print("\n4. ITERATING OVER DICTIONARIES")
    print("-" * 40)
    
    user = {"name": "Alice", "age": 28, "email": "alice@example.com", "tier": "gold"}
    
    print("Iterating over keys:")
    for key in user:
        print(f"  {key}: {user[key]}")
    
    print("\nIterating over items (key-value pairs):")
    for key, value in user.items():
        print(f"  {key} = {value}")
    
    print("\nIterating over values only:")
    for value in user.values():
        print(f"  {value}")
    
    # USING RANGE
    print("\n5. USING RANGE()")
    print("-" * 40)
    
    print("range(5) - numbers 0 to 4:")
    for i in range(5):
        print(f"  {i}")
    
    print("\nrange(2, 8) - numbers 2 to 7:")
    for i in range(2, 8):
        print(f"  {i}")
    
    print("\nrange(1, 10, 2) - odd numbers:")
    for i in range(1, 10, 2):
        print(f"  {i}")
    
    print("\nrange(10, 0, -1) - countdown:")
    for i in range(10, 0, -1):
        print(f"  {i}")
    
    # USING ENUMERATE
    print("\n6. USING ENUMERATE() - Get index and value")
    print("-" * 40)
    
    colors = ["red", "green", "blue", "yellow"]
    
    print("With index:")
    for index, color in enumerate(colors):
        print(f"  {index}: {color}")
    
    print("\nWith custom start index:")
    for index, color in enumerate(colors, start=1):
        print(f"  {index}: {color}")
    
    # USING ZIP - Iterate over multiple sequences in parallel
    print("\n7. USING ZIP() - Parallel iteration")
    print("-" * 40)
    
    names = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [95, 87, 92, 88]
    grades = ["A", "B", "A", "B"]
    
    print("Student data:")
    for name, score, grade in zip(names, scores, grades):
        print(f"  {name}: {score} ({grade})")
    
    # NESTED FOR LOOPS
    print("\n8. NESTED FOR LOOPS")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matrix (3x3):")
    for row in matrix:
        for value in row:
            print(f"  {value}", end=" ")
        print()  # New line after each row


def demonstrate_for_loop_patterns():
    """
    Demonstrates common for loop patterns and best practices.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: FOR LOOP PATTERNS")
    print("=" * 60)
    
    # ACCUMULATOR PATTERN (Summing)
    print("\n1. ACCUMULATOR PATTERN")
    print("-" * 40)
    
    numbers = [10, 20, 30, 40, 50]
    total = 0
    
    for num in numbers:
        total += num
        print(f"  Added {num}, running total: {total}")
    
    print(f"\nFinal total: {total}")
    
    # FILTERING PATTERN
    print("\n2. FILTERING PATTERN")
    print("-" * 40)
    
    scores = [85, 92, 78, 65, 95, 88, 72, 91]
    passing_scores = []
    
    for score in scores:
        if score >= 70:
            passing_scores.append(score)
            print(f"  {score} - PASS")
        else:
            print(f"  {score} - FAIL")
    
    print(f"\nPassing scores: {passing_scores}")
    print(f"Pass rate: {len(passing_scores)}/{len(scores)} = {len(passing_scores)/len(scores)*100:.1f}%")
    
    # TRANSFORMATION PATTERN
    print("\n3. TRANSFORMATION PATTERN")
    print("-" * 40)
    
    prices = [10.99, 25.50, 8.75, 12.00, 30.25]
    discounted_prices = []
    
    print("Original prices:")
    for price in prices:
        print(f"  ${price:.2f}")
    
    for price in prices:
        discounted = price * 0.9  # 10% off
        discounted_prices.append(discounted)
    
    print("\nDiscounted prices (10% off):")
    for price in discounted_prices:
        print(f"  ${price:.2f}")
    
    # SEARCHING PATTERN
    print("\n4. SEARCHING PATTERN")
    print("-" * 40)
    
    products = [
        {"id": 101, "name": "Laptop", "price": 999},
        {"id": 102, "name": "Mouse", "price": 25},
        {"id": 103, "name": "Keyboard", "price": 75},
        {"id": 104, "name": "Monitor", "price": 299}
    ]
    
    search_id = 103
    found_product = None
    
    for product in products:
        if product["id"] == search_id:
            found_product = product
            break  # Exit loop once found
    
    if found_product:
        print(f"Found product: {found_product['name']} - ${found_product['price']}")
    else:
        print(f"Product with ID {search_id} not found")
    
    # MAPPING PATTERN
    print("\n5. MAPPING PATTERN")
    print("-" * 40)
    
    names = ["alice", "bob", "charlie", "diana"]
    capitalized_names = []
    
    for name in names:
        capitalized_names.append(name.capitalize())
    
    print(f"Original: {names}")
    print(f"Capitalized: {capitalized_names}")
    
    # COMPREHENSION EQUIVALENTS (Preview)
    print("\n6. LIST COMPREHENSION EQUIVALENTS")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Traditional loop
    squares_loop = []
    for n in numbers:
        squares_loop.append(n ** 2)
    
    # List comprehension
    squares_comp = [n ** 2 for n in numbers]
    
    print(f"Loop result: {squares_loop}")
    print(f"Comprehension result: {squares_comp}")
    
    # Traditional loop with condition
    evens_loop = []
    for n in numbers:
        if n % 2 == 0:
            evens_loop.append(n)
    
    # List comprehension with condition
    evens_comp = [n for n in numbers if n % 2 == 0]
    
    print(f"Even numbers (loop): {evens_loop}")
    print(f"Even numbers (comprehension): {evens_comp}")


def build_batch_processor():
    """
    Complete batch file processing system using for loops.
    
    This demonstrates a real-world system that processes
    thousands of files with progress tracking and error handling.
    
    SOLID Principles Applied:
    - Single Responsibility: Each processing function has one purpose
    - Open/Closed: New file types can be added
    
    Design Patterns:
    - Iterator Pattern: Iterates through file collections
    - Template Method: Processing workflow defined in steps
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: BATCH FILE PROCESSOR")
    print("=" * 60)
    
    from typing import List, Dict, Any, Optional, Callable
    from dataclasses import dataclass, field
    from enum import Enum
    import random
    import time
    
    class FileStatus(Enum):
        """Status of file processing."""
        PENDING = "pending"
        PROCESSING = "processing"
        SUCCESS = "success"
        FAILED = "failed"
        SKIPPED = "skipped"
    
    class FileType(Enum):
        """Supported file types."""
        CSV = "csv"
        JSON = "json"
        XML = "xml"
        TXT = "txt"
        LOG = "log"
        IMAGE = "image"
    
    @dataclass
    class ProcessedFile:
        """Result of processing a single file."""
        filename: str
        file_type: FileType
        size_bytes: int
        status: FileStatus
        processing_time_ms: float
        error_message: Optional[str] = None
        records_processed: int = 0
    
    @dataclass
    class BatchResult:
        """Result of processing a batch of files."""
        total_files: int
        successful: int
        failed: int
        skipped: int
        total_records: int
        total_processing_time_ms: float
        files: List[ProcessedFile] = field(default_factory=list)
        errors: List[str] = field(default_factory=list)
        
        def success_rate(self) -> float:
            """Calculate success rate percentage."""
            if self.total_files == 0:
                return 0.0
            return (self.successful / self.total_files) * 100
        
        def summary(self) -> str:
            """Generate summary report."""
            return f"""
            ========================================
            BATCH PROCESSING SUMMARY
            ========================================
            Total Files: {self.total_files}
            Successful: {self.successful}
            Failed: {self.failed}
            Skipped: {self.skipped}
            Success Rate: {self.success_rate():.1f}%
            Total Records: {self.total_records}
            Total Time: {self.total_processing_time_ms:.0f}ms
            ========================================
            """
    
    class FileProcessor:
        """
        Processes files of various types.
        
        Design Pattern: Strategy Pattern - Different strategies for different file types
        """
        
        def __init__(self):
            # Register processors for different file types
            self.processors: Dict[FileType, Callable] = {
                FileType.CSV: self._process_csv,
                FileType.JSON: self._process_json,
                FileType.TXT: self._process_txt,
                FileType.LOG: self._process_log
            }
        
        def _process_csv(self, filename: str, content: str) -> int:
            """Simulate CSV processing."""
            # Simulate processing time based on content length
            time.sleep(0.01 * (len(content) / 1000))
            # Count rows (simulated)
            rows = content.count('\n')
            return max(1, rows)
        
        def _process_json(self, filename: str, content: str) -> int:
            """Simulate JSON processing."""
            time.sleep(0.008 * (len(content) / 1000))
            # Count objects (simulated)
            objects = content.count('{')
            return max(1, objects)
        
        def _process_txt(self, filename: str, content: str) -> int:
            """Simulate text file processing."""
            time.sleep(0.005 * (len(content) / 1000))
            # Count words (simulated)
            words = len(content.split())
            return max(1, words)
        
        def _process_log(self, filename: str, content: str) -> int:
            """Simulate log file processing."""
            time.sleep(0.015 * (len(content) / 1000))
            # Count log entries (simulated)
            entries = content.count('\n')
            return max(1, entries)
        
        def process(self, filename: str, file_type: FileType, content: str) -> Tuple[bool, int, str]:
            """
            Process a file and return results.
            
            Returns:
                Tuple of (success, records_processed, error_message)
            """
            try:
                processor = self.processors.get(file_type)
                if not processor:
                    return False, 0, f"Unsupported file type: {file_type.value}"
                
                records = processor(filename, content)
                return True, records, ""
            except Exception as e:
                return False, 0, str(e)
    
    class BatchProcessor:
        """
        Processes batches of files with progress tracking.
        
        Design Pattern: Iterator Pattern - Iterates through file queue
        """
        
        def __init__(self, processor: FileProcessor):
            self.processor = processor
            self.progress_callback: Optional[Callable] = None
        
        def set_progress_callback(self, callback: Callable) -> None:
            """Set callback for progress updates."""
            self.progress_callback = callback
        
        def process_batch(self, files: List[Dict[str, Any]], 
                         max_concurrent: int = 1,
                         retry_failed: bool = True) -> BatchResult:
            """
            Process a batch of files.
            
            Args:
                files: List of file metadata dictionaries
                max_concurrent: Maximum concurrent processes (simulated)
                retry_failed: Whether to retry failed files
                
            Returns:
                BatchResult with processing statistics
            """
            results = []
            total_records = 0
            total_time = 0
            errors = []
            
            total_files = len(files)
            
            print(f"\n📁 Starting batch processing of {total_files} files...")
            print("-" * 50)
            
            for idx, file_info in enumerate(files, 1):
                # Progress update
                if self.progress_callback:
                    self.progress_callback(idx, total_files, file_info["filename"])
                else:
                    print(f"  [{idx}/{total_files}] Processing: {file_info['filename']}")
                
                # Determine file type
                extension = file_info["filename"].split('.')[-1].lower()
                file_type_map = {
                    "csv": FileType.CSV,
                    "json": FileType.JSON,
                    "txt": FileType.TXT,
                    "log": FileType.LOG
                }
                file_type = file_type_map.get(extension, FileType.TXT)
                
                # Skip very large files
                if file_info.get("size_bytes", 0) > 10 * 1024 * 1024:  # 10MB
                    results.append(ProcessedFile(
                        filename=file_info["filename"],
                        file_type=file_type,
                        size_bytes=file_info["size_bytes"],
                        status=FileStatus.SKIPPED,
                        processing_time_ms=0,
                        error_message="File too large (>10MB)"
                    ))
                    continue
                
                # Process with retry logic
                start_time = time.time()
                success = False
                records = 0
                error_msg = ""
                
                for attempt in range(3 if retry_failed else 1):
                    success, records, error_msg = self.processor.process(
                        file_info["filename"],
                        file_type,
                        file_info.get("content", "")
                    )
                    
                    if success:
                        break
                    
                    if attempt < 2:
                        wait_time = (attempt + 1) * 0.5
                        time.sleep(wait_time)  # Exponential backoff
                
                processing_time = (time.time() - start_time) * 1000  # Convert to ms
                total_time += processing_time
                
                if success:
                    total_records += records
                    status = FileStatus.SUCCESS
                    print(f"    ✅ SUCCESS - {records} records in {processing_time:.0f}ms")
                else:
                    status = FileStatus.FAILED
                    errors.append(f"{file_info['filename']}: {error_msg}")
                    print(f"    ❌ FAILED - {error_msg}")
                
                results.append(ProcessedFile(
                    filename=file_info["filename"],
                    file_type=file_type,
                    size_bytes=file_info["size_bytes"],
                    status=status,
                    processing_time_ms=processing_time,
                    error_message=error_msg if not success else None,
                    records_processed=records if success else 0
                ))
            
            # Compile results
            successful = sum(1 for r in results if r.status == FileStatus.SUCCESS)
            failed = sum(1 for r in results if r.status == FileStatus.FAILED)
            skipped = sum(1 for r in results if r.status == FileStatus.SKIPPED)
            
            return BatchResult(
                total_files=total_files,
                successful=successful,
                failed=failed,
                skipped=skipped,
                total_records=total_records,
                total_processing_time_ms=total_time,
                files=results,
                errors=errors
            )
    
    # DEMONSTRATION
    print("\n📁 DEMONSTRATION: BATCH FILE PROCESSOR")
    print("-" * 40)
    
    # Create sample files
    sample_files = [
        {"filename": "sales_jan.csv", "size_bytes": 1024, "content": "date,amount\n2024-01-01,100\n2024-01-02,150\n2024-01-03,200"},
        {"filename": "sales_feb.csv", "size_bytes": 2048, "content": "date,amount\n2024-02-01,120\n2024-02-02,180"},
        {"filename": "config.json", "size_bytes": 512, "content": '{"setting1": "value1", "setting2": "value2"}'},
        {"filename": "app.log", "size_bytes": 4096, "content": "ERROR: Connection failed\nINFO: Retry attempt 1\nSUCCESS: Connected"},
        {"filename": "large_file.csv", "size_bytes": 15 * 1024 * 1024, "content": ""},  # 15MB - will be skipped
        {"filename": "unsupported.xyz", "size_bytes": 100, "content": "test content"}
    ]
    
    # Create processor
    file_processor = FileProcessor()
    batch_processor = BatchProcessor(file_processor)
    
    # Define progress callback
    def show_progress(current, total, filename):
        percent = (current / total) * 100
        bar_length = 30
        filled = int(bar_length * current / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\r  Progress: [{bar}] {percent:.1f}% - {filename}", end="", flush=True)
    
    batch_processor.set_progress_callback(show_progress)
    
    # Process batch
    result = batch_processor.process_batch(sample_files, retry_failed=True)
    
    print("\n" + result.summary())
    
    # Show failed files details
    if result.failed > 0:
        print("\nFAILED FILES DETAILS:")
        for file_result in result.files:
            if file_result.status == FileStatus.FAILED:
                print(f"  ❌ {file_result.filename}: {file_result.error_message}")
    
    # Show successful files summary
    successful_files = [f for f in result.files if f.status == FileStatus.SUCCESS]
    if successful_files:
        print(f"\nSUCCESSFUL FILES ({len(successful_files)}):")
        for f in successful_files:
            print(f"  ✅ {f.filename}: {f.records_processed} records, {f.processing_time_ms:.0f}ms")


if __name__ == "__main__":
    demonstrate_for_loop_basics()
    demonstrate_for_loop_patterns()
    build_batch_processor()
```

---

## 🔄 Section 2: The while Loop – Repeating Until a Condition Changes

The while loop repeats as long as a condition remains True. It's perfect for situations where you don't know how many iterations you need.

**SOLID Principle Applied: Single Responsibility** – Each while loop has one clear termination condition.

**Design Pattern: State Pattern** – The loop continues while the state meets the condition.

```python
"""
THE WHILE LOOP: REPEATING UNTIL A CONDITION CHANGES

This section covers the while loop and its applications.

SOLID Principle: Single Responsibility
- Each while loop has one clear termination condition

Design Pattern: State Pattern
- Loop continues while state meets condition
"""

from typing import List, Dict, Any, Optional, Tuple
import random
import time


def demonstrate_while_loop_basics():
    """
    Demonstrates basic while loop syntax and usage.
    
    The while loop continues as long as the condition is True.
    Must ensure the condition eventually becomes False (avoid infinite loops).
    """
    print("=" * 60)
    print("SECTION 2A: WHILE LOOP BASICS")
    print("=" * 60)
    
    # BASIC WHILE LOOP
    print("\n1. BASIC WHILE LOOP")
    print("-" * 40)
    
    count = 1
    while count <= 5:
        print(f"  Iteration {count}")
        count += 1
    
    print(f"  Loop ended. Count is now {count}")
    
    # COUNTDOWN
    print("\n2. COUNTDOWN")
    print("-" * 40)
    
    timer = 5
    print("  Launching in:")
    while timer > 0:
        print(f"    {timer}...")
        timer -= 1
        time.sleep(0.3)
    print("    LIFT OFF! 🚀")
    
    # SUM UNTIL LIMIT
    print("\n3. SUMMING UNTIL LIMIT")
    print("-" * 40)
    
    total = 0
    number = 1
    
    while total + number <= 100:
        total += number
        print(f"  Added {number}, total: {total}")
        number += 1
    
    print(f"\n  Final total: {total}")
    print(f"  Next number {number} would exceed 100")
    
    # WHILE WITH USER INPUT
    print("\n4. WHILE WITH USER INPUT")
    print("-" * 40)
    
    # Simulated user input (would use input() in real code)
    simulated_responses = ["yes", "no", "yes", "quit"]
    response_index = 0
    
    user_response = "yes"
    print("  (Simulated user input for demonstration)")
    
    while user_response != "quit":
        user_response = simulated_responses[response_index]
        response_index += 1
        print(f"  User said: {user_response}")
        
        if user_response == "yes":
            print("    Continuing...")
        elif user_response == "no":
            print("    Asking again...")
    
    print("  Loop ended. Goodbye!")
    
    # INFINITE LOOP WITH BREAK (Must have exit condition!)
    print("\n5. INFINITE LOOP WITH BREAK")
    print("-" * 40)
    
    attempts = 0
    max_attempts = 3
    
    while True:  # Infinite loop - must break out
        attempts += 1
        print(f"  Attempt {attempts}")
        
        if attempts >= max_attempts:
            print("  Max attempts reached. Breaking out.")
            break
        
        if random.random() > 0.7:  # 30% success chance
            print("  Success! Breaking out.")
            break
    
    print("  Loop exited.")


def demonstrate_while_loop_patterns():
    """
    Demonstrates common while loop patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: WHILE LOOP PATTERNS")
    print("=" * 60)
    
    # VALIDATION LOOP
    print("\n1. VALIDATION LOOP (Keep asking until valid)")
    print("-" * 40)
    
    # Simulated validation
    print("  (Simulated input validation)")
    
    valid_options = ["yes", "no", "maybe"]
    simulated_inputs = ["maybe", "yeah", "y", "yes"]
    input_index = 0
    
    user_input = None
    while user_input not in valid_options:
        user_input = simulated_inputs[input_index]
        input_index += 1
        print(f"  User entered: '{user_input}'")
        
        if user_input not in valid_options:
            print(f"    Invalid! Please enter {', '.join(valid_options)}")
    
    print(f"  Valid input received: {user_input}")
    
    # RETRY LOOP (with timeout)
    print("\n2. RETRY LOOP (with timeout)")
    print("-" * 40)
    
    max_retries = 5
    retry_count = 0
    success = False
    
    print("  Attempting to connect to server...")
    
    while retry_count < max_retries and not success:
        retry_count += 1
        wait_time = 2 ** retry_count  # Exponential backoff
        print(f"    Attempt {retry_count}/{max_retries}")
        
        # Simulate connection (70% success after retry)
        if random.random() > (0.3 * retry_count):
            success = True
            print(f"    ✅ Connected successfully!")
        else:
            if retry_count < max_retries:
                print(f"    ❌ Failed. Waiting {wait_time}s before retry...")
                time.sleep(0.2)  # Reduced for demo
    
    if not success:
        print("  ❌ Failed to connect after all retries")
    
    # GAME LOOP
    print("\n3. GAME LOOP")
    print("-" * 40)
    
    secret_number = random.randint(1, 20)
    guess_count = 0
    max_guesses = 5
    
    print("  Guess the number (1-20)!")
    
    # Simulated guesses
    simulated_guesses = [15, 8, 12, 10, 10]
    guess_index = 0
    
    while guess_count < max_guesses:
        guess = simulated_guesses[guess_index]
        guess_index += 1
        guess_count += 1
        
        print(f"    Guess {guess_count}: {guess}")
        
        if guess == secret_number:
            print(f"    🎉 Correct! The number was {secret_number}")
            print(f"    You got it in {guess_count} guesses!")
            break
        elif guess < secret_number:
            print(f"    Too low!")
        else:
            print(f"    Too high!")
    
    if guess_count == max_guesses and guess != secret_number:
        print(f"  Game over! The number was {secret_number}")
    
    # CONSUMER-PRODUCER PATTERN
    print("\n4. CONSUMER-PRODUCER PATTERN")
    print("-" * 40)
    
    # Simulated queue processing
    task_queue = ["task1", "task2", "task3", "task4", "task5"]
    processed = []
    
    print("  Processing task queue:")
    
    while task_queue:
        task = task_queue.pop(0)  # Remove first item
        print(f"    Processing: {task}")
        processed.append(task)
        time.sleep(0.1)
    
    print(f"  All tasks processed. Completed: {len(processed)} tasks")
    
    # FIND FIRST MATCH
    print("\n5. FIND FIRST MATCH")
    print("-" * 40)
    
    data = [10, 23, 45, 67, 89, 12, 34, 56, 78]
    target = 67
    index = 0
    found_index = -1
    
    while index < len(data):
        if data[index] == target:
            found_index = index
            break
        index += 1
    
    if found_index >= 0:
        print(f"  Found {target} at index {found_index}")
    else:
        print(f"  {target} not found in list")


def build_retry_mechanism():
    """
    Complete API retry mechanism with exponential backoff.
    
    This demonstrates a real-world system that retries failed
    API calls with increasing delays between attempts.
    
    SOLID Principles Applied:
    - Single Responsibility: Retry logic separated from business logic
    - Open/Closed: New retry strategies can be added
    
    Design Patterns:
    - Retry Pattern: Automatic retry on failure
    - Circuit Breaker Pattern: Stop retrying after too many failures
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: API RETRY MECHANISM")
    print("=" * 60)
    
    from typing import Callable, Any, Optional, Tuple
    from dataclasses import dataclass
    from enum import Enum
    import requests  # Mocked for demonstration
    
    class RetryStrategy(Enum):
        """Retry backoff strategies."""
        FIXED = "fixed"          # Same delay each time
        LINEAR = "linear"        # Delay increases linearly
        EXPONENTIAL = "exponential"  # Delay doubles each time
        POLYNOMIAL = "polynomial"    # Delay increases by power
    
    @dataclass
    class RetryConfig:
        """Configuration for retry behavior."""
        max_retries: int = 3
        base_delay_seconds: float = 1.0
        strategy: RetryStrategy = RetryStrategy.EXPONENTIAL
        max_delay_seconds: float = 30.0
        retry_on_status_codes: List[int] = None
        retry_on_exceptions: List[type] = None
        
        def __post_init__(self):
            if self.retry_on_status_codes is None:
                self.retry_on_status_codes = [408, 429, 500, 502, 503, 504]
            if self.retry_on_exceptions is None:
                self.retry_on_exceptions = [ConnectionError, TimeoutError]
    
    @dataclass
    class RetryResult:
        """Result of a retry operation."""
        success: bool
        result: Any
        attempts: int
        total_time_seconds: float
        final_error: Optional[str] = None
        retry_history: List[Dict] = None
        
        def __post_init__(self):
            if self.retry_history is None:
                self.retry_history = []
    
    class RetryExecutor:
        """
        Executes operations with automatic retry logic.
        
        Design Pattern: Retry Pattern - Automatic retry on failure
        Design Pattern: Circuit Breaker Pattern - Prevents endless retries
        """
        
        def __init__(self, config: Optional[RetryConfig] = None):
            self.config = config or RetryConfig()
            self.circuit_open = False
            self.failure_count = 0
            self.last_failure_time = 0
        
        def _calculate_delay(self, attempt: int) -> float:
            """Calculate delay for a given attempt number."""
            if self.config.strategy == RetryStrategy.FIXED:
                delay = self.config.base_delay_seconds
            elif self.config.strategy == RetryStrategy.LINEAR:
                delay = self.config.base_delay_seconds * attempt
            elif self.config.strategy == RetryStrategy.POLYNOMIAL:
                delay = self.config.base_delay_seconds * (attempt ** 2)
            else:  # EXPONENTIAL
                delay = self.config.base_delay_seconds * (2 ** (attempt - 1))
            
            return min(delay, self.config.max_delay_seconds)
        
        def _should_retry(self, attempt: int, exception: Exception = None, 
                         status_code: int = None) -> bool:
            """Determine if another retry should be attempted."""
            if attempt >= self.config.max_retries:
                return False
            
            if exception:
                for exc_type in self.config.retry_on_exceptions:
                    if isinstance(exception, exc_type):
                        return True
            
            if status_code and status_code in self.config.retry_on_status_codes:
                return True
            
            return False
        
        def execute(self, func: Callable, *args, **kwargs) -> RetryResult:
            """
            Execute a function with automatic retry.
            
            Args:
                func: Function to execute
                *args, **kwargs: Arguments to pass to function
                
            Returns:
                RetryResult with execution details
            """
            start_time = time.time()
            retry_history = []
            last_exception = None
            
            for attempt in range(1, self.config.max_retries + 1):
                try:
                    # Execute the function
                    result = func(*args, **kwargs)
                    
                    # Check if result indicates failure (for API responses)
                    status_code = None
                    if hasattr(result, 'status_code'):
                        status_code = result.status_code
                        if status_code >= 400:
                            raise Exception(f"HTTP {status_code}: {result.text if hasattr(result, 'text') else 'Error'}")
                    
                    # Success!
                    total_time = time.time() - start_time
                    return RetryResult(
                        success=True,
                        result=result,
                        attempts=attempt,
                        total_time_seconds=total_time,
                        retry_history=retry_history
                    )
                    
                except Exception as e:
                    last_exception = e
                    status_code = getattr(e, 'response', None)
                    status_code = status_code.status_code if status_code else None
                    
                    retry_history.append({
                        "attempt": attempt,
                        "error": str(e),
                        "delay": self._calculate_delay(attempt) if attempt < self.config.max_retries else 0
                    })
                    
                    print(f"    Attempt {attempt} failed: {str(e)[:50]}")
                    
                    if self._should_retry(attempt, e, status_code):
                        delay = self._calculate_delay(attempt)
                        print(f"    Retrying in {delay:.1f}s...")
                        time.sleep(delay)
                    else:
                        break
            
            total_time = time.time() - start_time
            return RetryResult(
                success=False,
                result=None,
                attempts=self.config.max_retries,
                total_time_seconds=total_time,
                final_error=str(last_exception) if last_exception else "Unknown error",
                retry_history=retry_history
            )
    
    # DEMONSTRATION
    print("\n🌐 DEMONSTRATION: API RETRY MECHANISM")
    print("-" * 40)
    
    # Simulate different API behaviors
    def unstable_api(success_rate: float = 0.5, delay: float = 0.1):
        """Simulate an unstable API endpoint."""
        time.sleep(delay)
        if random.random() < success_rate:
            return {"status": "success", "data": "API response data"}
        else:
            raise ConnectionError("Connection timeout")
    
    def flaky_api(fail_count: int = 2):
        """Simulate an API that fails first N times."""
        if not hasattr(flaky_api, "call_count"):
            flaky_api.call_count = 0
        
        flaky_api.call_count += 1
        
        if flaky_api.call_count <= fail_count:
            raise TimeoutError(f"Request timeout (attempt {flaky_api.call_count})")
        
        return {"status": "success", "data": "API response after retries"}
    
    # Reset counter
    flaky_api.call_count = 0
    
    # Test different retry strategies
    print("\n1. TESTING UNSTABLE API (50% success rate)")
    print("-" * 40)
    
    configs = [
        ("Fixed (1s)", RetryConfig(max_retries=3, strategy=RetryStrategy.FIXED, base_delay_seconds=0.5)),
        ("Linear (1s,2s,3s)", RetryConfig(max_retries=3, strategy=RetryStrategy.LINEAR, base_delay_seconds=0.5)),
        ("Exponential (1s,2s,4s)", RetryConfig(max_retries=3, strategy=RetryStrategy.EXPONENTIAL, base_delay_seconds=0.5))
    ]
    
    for strategy_name, config in configs:
        print(f"\n  Strategy: {strategy_name}")
        executor = RetryExecutor(config)
        result = executor.execute(lambda: unstable_api(success_rate=0.6, delay=0.05))
        
        if result.success:
            print(f"    ✅ SUCCESS after {result.attempts} attempts ({result.total_time_seconds:.2f}s)")
        else:
            print(f"    ❌ FAILED after {result.attempts} attempts")
    
    # Test flaky API (fails first 2 times)
    print("\n2. TESTING FLAKY API (fails first 2 attempts)")
    print("-" * 40)
    
    # Reset counter
    flaky_api.call_count = 0
    
    executor = RetryExecutor(RetryConfig(max_retries=3, strategy=RetryStrategy.EXPONENTIAL, base_delay_seconds=0.3))
    result = executor.execute(flaky_api)
    
    if result.success:
        print(f"  ✅ SUCCESS after {result.attempts} attempts")
        for history in result.retry_history:
            print(f"    Attempt {history['attempt']}: {history['error'][:40]}...")
    else:
        print(f"  ❌ FAILED after {result.attempts} attempts")
    
    # Test always-failing API
    print("\n3. TESTING ALWAYS-FAILING API")
    print("-" * 40)
    
    def always_fail():
        raise ConnectionError("Network unreachable")
    
    executor = RetryExecutor(RetryConfig(max_retries=3, strategy=RetryStrategy.EXPONENTIAL, base_delay_seconds=0.2))
    result = executor.execute(always_fail)
    
    print(f"  Result: {'SUCCESS' if result.success else 'FAILED'}")
    print(f"  Attempts: {result.attempts}")
    print(f"  Total time: {result.total_time_seconds:.2f}s")
    print(f"  Final error: {result.final_error}")
    
    # RECOMMENDATIONS
    print("\n📚 RETRY BEST PRACTICES")
    print("-" * 40)
    
    recommendations = [
        "✓ Always set a maximum retry limit (3-5 is typical)",
        "✓ Use exponential backoff for distributed systems",
        "✓ Only retry idempotent operations (safe to repeat)",
        "✓ Log retry attempts for debugging",
        "✓ Consider circuit breaker for sustained failures",
        "✓ Different errors deserve different retry strategies"
    ]
    
    for rec in recommendations:
        print(f"  {rec}")


if __name__ == "__main__":
    demonstrate_while_loop_basics()
    demonstrate_while_loop_patterns()
    build_retry_mechanism()
```

---

## 🛑 Section 3: Break, Continue, and Else in Loops

Break exits a loop immediately. Continue skips to the next iteration. Else runs after normal loop completion (not after break).

**SOLID Principle Applied: Single Responsibility** – Each control statement has one clear purpose.

**Design Pattern: Guard Clause Pattern** – Continue acts as a guard clause within loops.

```python
"""
BREAK, CONTINUE, AND ELSE IN LOOPS

This section covers loop control statements.

SOLID Principle: Single Responsibility
- break: exit loop immediately
- continue: skip to next iteration
- else: run after normal completion

Design Pattern: Guard Clause Pattern
- continue acts as guard clause within loops
"""

from typing import List, Dict, Any, Optional
import random
import time


def demonstrate_break():
    """
    Demonstrates the break statement.
    
    break exits the innermost loop immediately.
    """
    print("=" * 60)
    print("SECTION 3A: BREAK STATEMENT")
    print("=" * 60)
    
    # BREAK ON CONDITION
    print("\n1. BREAK ON CONDITION")
    print("-" * 40)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Searching for first even number:")
    for num in numbers:
        print(f"  Checking {num}")
        if num % 2 == 0:
            print(f"    Found even number: {num}")
            break
    
    # BREAK IN WHILE LOOP
    print("\n2. BREAK IN WHILE LOOP")
    print("-" * 40)
    
    secret = random.randint(1, 10)
    guesses = [5, 7, 3, 8, 2]  # Simulated guesses
    guess_index = 0
    
    print(f"Secret number (simulated): {secret}")
    
    while guess_index < len(guesses):
        guess = guesses[guess_index]
        guess_index += 1
        print(f"  Guess {guess_index}: {guess}")
        
        if guess == secret:
            print(f"    ✓ Correct! Found at guess {guess_index}")
            break
        else:
            print(f"    ✗ Wrong")
    
    # BREAK IN NESTED LOOPS
    print("\n3. BREAK IN NESTED LOOPS")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    target = 11
    found = False
    
    print(f"Searching for {target} in matrix:")
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            print(f"  Checking [{row_idx}][{col_idx}] = {value}")
            if value == target:
                print(f"    ✓ Found at position ({row_idx}, {col_idx})")
                found = True
                break  # Breaks inner loop only
        if found:
            break  # Breaks outer loop
    
    # PRACTICAL: FIND FIRST VALID ITEM
    print("\n4. PRACTICAL: FIND FIRST VALID ITEM")
    print("-" * 40)
    
    def find_first_valid(items: List, validator_func) -> Optional[Any]:
        """Find first item that passes validation."""
        for item in items:
            if validator_func(item):
                return item
        return None
    
    products = [
        {"name": "A", "price": 5, "in_stock": False},
        {"name": "B", "price": 15, "in_stock": True},
        {"name": "C", "price": 25, "in_stock": True},
        {"name": "D", "price": 8, "in_stock": False}
    ]
    
    def in_stock_and_affordable(product):
        return product["in_stock"] and product["price"] < 20
    
    result = find_first_valid(products, in_stock_and_affordable)
    
    if result:
        print(f"Found: {result['name']} - ${result['price']}")
    else:
        print("No matching product found")


def demonstrate_continue():
    """
    Demonstrates the continue statement.
    
    continue skips the rest of the current iteration and moves to the next.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: CONTINUE STATEMENT")
    print("=" * 60)
    
    # SKIP EVEN NUMBERS
    print("\n1. SKIP EVEN NUMBERS")
    print("-" * 40)
    
    print("Odd numbers only:")
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(f"  {i}")
    
    # FILTER VALID ITEMS
    print("\n2. FILTER VALID ITEMS")
    print("-" * 40)
    
    user_inputs = ["alice", "", "bob", None, "charlie", "  ", "diana"]
    
    print(f"Raw inputs: {user_inputs}")
    print("Processing valid inputs:")
    
    valid_count = 0
    for inp in user_inputs:
        if not inp or not inp.strip():
            print(f"  Skipping invalid input: '{inp}'")
            continue
        
        valid_count += 1
        print(f"  Processing: '{inp.strip()}'")
    
    print(f"Processed {valid_count} valid inputs")
    
    # CONTINUE IN WHILE LOOP
    print("\n3. CONTINUE IN WHILE LOOP")
    print("-" * 40)
    
    numbers = [1, 2, -3, 4, -5, 6, -7, 8, 9, -10]
    index = 0
    sum_positive = 0
    
    print(f"Numbers: {numbers}")
    
    while index < len(numbers):
        num = numbers[index]
        index += 1
        
        if num < 0:
            print(f"  Skipping negative: {num}")
            continue
        
        sum_positive += num
        print(f"  Added {num}, sum: {sum_positive}")
    
    print(f"Sum of positive numbers: {sum_positive}")
    
    # PRACTICAL: PROCESSING WITH EXCEPTIONS
    print("\n4. PRACTICAL: DATA CLEANING")
    print("-" * 40)
    
    data_rows = [
        {"id": 1, "value": 100, "valid": True},
        {"id": 2, "value": None, "valid": True},
        {"id": 3, "value": 250, "valid": False},
        {"id": 4, "value": 300, "valid": True},
        {"id": 5, "value": "error", "valid": True}
    ]
    
    print("Cleaning data:")
    cleaned_data = []
    
    for row in data_rows:
        # Skip if not valid
        if not row["valid"]:
            print(f"  Skipping row {row['id']}: not valid")
            continue
        
        # Skip if value is None
        if row["value"] is None:
            print(f"  Skipping row {row['id']}: value is None")
            continue
        
        # Skip if value is not numeric
        if not isinstance(row["value"], (int, float)):
            print(f"  Skipping row {row['id']}: value is not numeric")
            continue
        
        cleaned_data.append(row)
        print(f"  Row {row['id']} accepted: {row['value']}")
    
    print(f"Accepted {len(cleaned_data)} of {len(data_rows)} rows")


def demonstrate_loop_else():
    """
    Demonstrates the else clause in loops.
    
    else runs after normal loop completion (when break was NOT encountered).
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: ELSE IN LOOPS")
    print("=" * 60)
    
    # ELSE WITH FOR LOOP (NO BREAK)
    print("\n1. ELSE WITH FOR LOOP (No break)")
    print("-" * 40)
    
    for i in range(5):
        print(f"  Iteration {i}")
    else:
        print("  Loop completed normally (no break encountered)")
    
    # ELSE WITH FOR LOOP (WITH BREAK)
    print("\n2. ELSE WITH FOR LOOP (With break)")
    print("-" * 40)
    
    for i in range(5):
        print(f"  Iteration {i}")
        if i == 3:
            print("    Break encountered!")
            break
    else:
        print("  This else block will NOT run because break occurred")
    
    print("  Loop exited")
    
    # PRACTICAL: SEARCH WITH ELSE
    print("\n3. PRACTICAL: SEARCH WITH ELSE")
    print("-" * 40)
    
    def find_item(items, target):
        """Search for item, with else indicating not found."""
        for item in items:
            if item == target:
                print(f"  Found {target}!")
                return True
        else:
            print(f"  {target} not found in list")
            return False
    
    fruits = ["apple", "banana", "cherry", "date"]
    
    find_item(fruits, "cherry")
    find_item(fruits, "grape")
    
    # PRACTICAL: PRIME NUMBER CHECKER
    print("\n4. PRACTICAL: PRIME NUMBER CHECKER")
    print("-" * 40)
    
    def is_prime(n: int) -> bool:
        """Check if a number is prime using for-else."""
        if n < 2:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"  {n} is divisible by {i}")
                return False
        else:
            print(f"  {n} has no divisors found")
            return True
    
    test_numbers = [2, 7, 12, 17, 25, 29]
    
    for num in test_numbers:
        result = is_prime(num)
        print(f"  {num} is prime: {result}\n")
    
    # PRACTICAL: CONNECTION ATTEMPT
    print("\n5. PRACTICAL: CONNECTION ATTEMPT WITH RETRY")
    print("-" * 40)
    
    def attempt_connection(max_attempts: int = 3) -> bool:
        """Attempt connection with retry logic using for-else."""
        for attempt in range(1, max_attempts + 1):
            print(f"  Attempt {attempt}...")
            
            # Simulate connection (70% success on first, higher on retry)
            success_rate = 0.7 + (attempt - 1) * 0.15
            if random.random() < success_rate:
                print(f"    ✅ Connected on attempt {attempt}")
                return True
            else:
                print(f"    ❌ Failed")
        
        else:
            print(f"  Failed to connect after {max_attempts} attempts")
            return False
    
    attempt_connection(3)


def build_pagination_system():
    """
    Complete pagination system using loops.
    
    This demonstrates a real-world system that paginates through
    large datasets, fetching and processing pages until completion.
    
    SOLID Principles Applied:
    - Single Responsibility: Pagination logic separated from data fetching
    - Open/Closed: New data sources can be added
    
    Design Patterns:
    - Iterator Pattern: Iterates through pages
    - Lazy Loading Pattern: Fetches pages on demand
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: PAGINATION SYSTEM")
    print("=" * 60)
    
    from typing import List, Dict, Any, Optional, Iterator
    from dataclasses import dataclass, field
    from datetime import datetime
    
    @dataclass
    class Page:
        """Represents a single page of data."""
        number: int
        items: List[Dict]
        has_next: bool
        total_items: Optional[int] = None
        fetch_time_ms: float = 0
    
    @dataclass
    class PaginationResult:
        """Result of paginated data fetch."""
        total_pages: int
        total_items: int
        items: List[Dict]
        fetch_time_seconds: float
        pages_processed: List[int] = field(default_factory=list)
    
    class DataSource:
        """
        Simulated data source with pagination API.
        
        Design Pattern: Repository Pattern - Data access abstraction
        """
        
        def __init__(self, total_items: int = 1000, items_per_page: int = 50):
            self.total_items = total_items
            self.items_per_page = items_per_page
            self.total_pages = (total_items + items_per_page - 1) // items_per_page
            self.call_count = 0
        
        def fetch_page(self, page_number: int, page_size: int = None) -> Page:
            """
            Fetch a specific page from the data source.
            
            Args:
                page_number: Page number (1-indexed)
                page_size: Items per page (uses default if not specified)
                
            Returns:
                Page object with items and metadata
            """
            self.call_count += 1
            page_size = page_size or self.items_per_page
            
            # Simulate network delay
            time.sleep(0.05)  # 50ms per page
            
            # Calculate start and end indices
            start_idx = (page_number - 1) * page_size
            end_idx = min(start_idx + page_size, self.total_items)
            
            # Generate items for this page
            items = []
            for i in range(start_idx, end_idx):
                items.append({
                    "id": i + 1,
                    "name": f"Item {i + 1}",
                    "value": (i + 1) * 10,
                    "timestamp": datetime.now().isoformat()
                })
            
            has_next = end_idx < self.total_items
            
            return Page(
                number=page_number,
                items=items,
                has_next=has_next,
                total_items=self.total_items,
                fetch_time_ms=0  # Would be actual time in production
            )
        
        def get_total_items(self) -> int:
            """Get total number of items available."""
            return self.total_items
        
        def get_total_pages(self, page_size: int = None) -> int:
            """Get total number of pages."""
            page_size = page_size or self.items_per_page
            return (self.total_items + page_size - 1) // page_size
    
    class Paginator:
        """
        Handles paginated data fetching and processing.
        
        Design Pattern: Iterator Pattern - Iterates through pages
        Design Pattern: Lazy Loading - Fetches pages only when needed
        """
        
        def __init__(self, data_source: DataSource, page_size: int = 50):
            self.data_source = data_source
            self.page_size = page_size
            self.total_pages = data_source.get_total_pages(page_size)
        
        def fetch_all(self, progress_callback: Optional[Callable] = None) -> PaginationResult:
            """
            Fetch all pages using a for loop.
            
            Args:
                progress_callback: Optional callback for progress updates
                
            Returns:
                PaginationResult with all items
            """
            start_time = time.time()
            all_items = []
            pages_processed = []
            
            print(f"\n📄 Fetching {self.total_pages} pages ({self.page_size} items/page)...")
            
            for page_num in range(1, self.total_pages + 1):
                # Progress update
                if progress_callback:
                    progress_callback(page_num, self.total_pages)
                else:
                    percent = (page_num / self.total_pages) * 100
                    print(f"  Page {page_num}/{self.total_pages} ({percent:.0f}%)", end="\r", flush=True)
                
                # Fetch page
                page = self.data_source.fetch_page(page_num, self.page_size)
                all_items.extend(page.items)
                pages_processed.append(page_num)
            
            total_time = time.time() - start_time
            
            print(f"\n  ✅ Fetched {len(all_items)} items in {total_time:.2f}s")
            
            return PaginationResult(
                total_pages=self.total_pages,
                total_items=len(all_items),
                items=all_items,
                fetch_time_seconds=total_time,
                pages_processed=pages_processed
            )
        
        def fetch_until_condition(self, condition: Callable) -> PaginationResult:
            """
            Fetch pages until a condition is met (using while loop).
            
            Args:
                condition: Function that takes an item and returns True to stop
                
            Returns:
                PaginationResult with items up to condition
            """
            start_time = time.time()
            all_items = []
            pages_processed = []
            page_num = 1
            
            print(f"\n🔍 Fetching pages until condition met...")
            
            while True:
                print(f"  Fetching page {page_num}...")
                page = self.data_source.fetch_page(page_num, self.page_size)
                all_items.extend(page.items)
                pages_processed.append(page_num)
                
                # Check condition on each item
                for item in page.items:
                    if condition(item):
                        print(f"  ✅ Condition met at item {item['id']}")
                        total_time = time.time() - start_time
                        return PaginationResult(
                            total_pages=page_num,
                            total_items=len(all_items),
                            items=all_items,
                            fetch_time_seconds=total_time,
                            pages_processed=pages_processed
                        )
                
                if not page.has_next:
                    break
                
                page_num += 1
            
            total_time = time.time() - start_time
            print(f"  Completed all pages, condition never met")
            
            return PaginationResult(
                total_pages=page_num,
                total_items=len(all_items),
                items=all_items,
                fetch_time_seconds=total_time,
                pages_processed=pages_processed
            )
        
        def process_batches(self, batch_size: int, processor: Callable) -> Dict:
            """
            Process data in batches (nested loops).
            
            Args:
                batch_size: Number of items per batch
                processor: Function to process each batch
                
            Returns:
                Processing statistics
            """
            start_time = time.time()
            batches_processed = 0
            items_processed = 0
            
            print(f"\n⚙️ Processing data in batches of {batch_size}...")
            
            for page_num in range(1, self.total_pages + 1):
                page = self.data_source.fetch_page(page_num, self.page_size)
                
                # Process items in batches within the page
                for i in range(0, len(page.items), batch_size):
                    batch = page.items[i:i + batch_size]
                    processor(batch)
                    batches_processed += 1
                    items_processed += len(batch)
                    
                    print(f"  Batch {batches_processed}: processed {items_processed} items", end="\r")
            
            total_time = time.time() - start_time
            
            return {
                "batches_processed": batches_processed,
                "items_processed": items_processed,
                "total_time_seconds": total_time,
                "avg_batch_time_ms": (total_time / batches_processed) * 1000 if batches_processed > 0 else 0
            }
    
    # DEMONSTRATION
    print("\n📊 DEMONSTRATION: PAGINATION SYSTEM")
    print("-" * 40)
    
    # Create data source with 247 items (5 pages of 50, last page has 47)
    data_source = DataSource(total_items=247, items_per_page=50)
    paginator = Paginator(data_source, page_size=50)
    
    # 1. Fetch all pages
    print("\n1. FETCHING ALL PAGES")
    print("-" * 40)
    
    def show_progress(current, total):
        percent = (current / total) * 100
        bar_length = 30
        filled = int(bar_length * current / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\r  Progress: [{bar}] {percent:.0f}%", end="", flush=True)
    
    result = paginator.fetch_all(progress_callback=show_progress)
    print(f"\n  Total items: {result.total_items}")
    print(f"  Total pages: {result.total_pages}")
    print(f"  Fetch time: {result.fetch_time_seconds:.2f}s")
    print(f"  API calls: {data_source.call_count}")
    
    # 2. Fetch until condition
    print("\n2. FETCHING UNTIL CONDITION")
    print("-" * 40)
    
    # Reset call count
    data_source.call_count = 0
    
    def stop_when_id_over_100(item):
        return item["id"] > 100
    
    result = paginator.fetch_until_condition(stop_when_id_over_100)
    print(f"  Items fetched: {result.total_items}")
    print(f"  Pages processed: {result.pages_processed}")
    print(f"  API calls: {data_source.call_count}")
    
    # 3. Process in batches
    print("\n3. PROCESSING IN BATCHES")
    print("-" * 40)
    
    # Reset call count
    data_source.call_count = 0
    
    def process_batch(batch):
        """Simulate processing a batch of items."""
        time.sleep(0.01)  # Simulate processing time
    
    stats = paginator.process_batches(batch_size=10, processor=process_batch)
    print(f"\n  Batches: {stats['batches_processed']}")
    print(f"  Items: {stats['items_processed']}")
    print(f"  Total time: {stats['total_time_seconds']:.2f}s")
    print(f"  Avg batch time: {stats['avg_batch_time_ms']:.1f}ms")
    
    # SUMMARY
    print("\n📚 PAGINATION BEST PRACTICES")
    print("-" * 40)
    
    practices = [
        "✓ Always use page size limits to prevent memory issues",
        "✓ Implement lazy loading for large datasets",
        "✓ Use progress callbacks for long-running operations",
        "✓ Cache fetched pages when appropriate",
        "✓ Handle network errors with retry logic",
        "✓ Consider infinite scroll vs traditional pagination"
    ]
    
    for practice in practices:
        print(f"  {practice}")


if __name__ == "__main__":
    demonstrate_break()
    demonstrate_continue()
    demonstrate_loop_else()
    build_pagination_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **for Loop** – Iterates over sequences (lists, strings, dicts, ranges). Use enumerate() for index-value pairs. Use zip() for parallel iteration.

- **while Loop** – Repeats while condition is True. Perfect for unknown iteration counts. Must ensure condition eventually becomes False.

- **break** – Exits loop immediately. Use with for-else pattern to detect if loop completed normally.

- **continue** – Skips to next iteration. Acts as guard clause within loops. Use to filter invalid items.

- **else in Loops** – Runs after normal loop completion (no break). Perfect for search operations.

- **Batch Processing** – Process thousands of files with progress tracking. Use retry logic for transient failures.

- **Retry Mechanism** – Exponential backoff for API calls. Different strategies for different failure types.

- **Pagination** – Handle large datasets by fetching pages. Lazy loading prevents memory issues.

- **SOLID Principles Applied** – Single Responsibility (each loop has one purpose), Open/Closed (new iteration strategies can be added).

- **Design Patterns Used** – Iterator Pattern (for loops), Retry Pattern (API retries), Circuit Breaker Pattern (prevent endless retries), Lazy Loading Pattern (pagination).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Control Flow – if, elif, else

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Nested Logic – Conditions Inside Loops

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 5 | 2 | 71% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **10** | **42** | **19%** |

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

**Next Story:** Series A, Story 6: The 2026 Python Metromap: Nested Logic – Conditions Inside Loops

---

## 📝 Your Invitation

You've mastered loops. Now build something with what you've learned:

1. **Build a batch processor** – Process a list of files with progress tracking. Add retry logic for failed files.

2. **Create an API retry mechanism** – Implement exponential backoff. Test with simulated flaky APIs.

3. **Build a pagination system** – Fetch data from a simulated API page by page. Add lazy loading.

4. **Create a data validator** – Use loops to validate records. Use continue to skip invalid records.

5. **Build a search system** – Use for-else to indicate when items aren't found. Add break on first match.

**You've mastered loops. Next stop: Nested Logic!**

---

*Found this helpful? Clap, comment, and share what you built with loops. Next stop: Nested Logic!* 🚇