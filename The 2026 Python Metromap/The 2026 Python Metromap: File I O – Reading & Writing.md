# The 2026 Python Metromap: File I/O – Reading & Writing

## Series E: File & Data Handling Line | Story 1 of 5

![The 2026 Python Metromap/images/File IO – Reading and Writing](images/File IO – Reading and Writing.png)

## 📖 Introduction

**Welcome to the first stop on the File & Data Handling Line.**

You've mastered the Object-Oriented Programming Line. You can create classes, hierarchies, and complex systems that model real-world entities. But all that data exists only in memory—it disappears when the program ends. To persist data, share it between applications, or process large datasets, you need to work with files.

File I/O (Input/Output) is how your Python programs interact with the file system—reading from files, writing to files, and managing file resources. Whether you're processing log files, reading configuration, saving user data, or generating reports, file I/O is essential. Understanding how to efficiently read, write, and manage files is a fundamental skill for any Python developer.

This story—**The 2026 Python Metromap: File I/O – Reading & Writing**—is your guide to mastering file operations in Python. We'll build a complete log file analyzer that reads server logs, extracts errors, and generates reports. We'll create a configuration manager that reads and writes settings. We'll build a data backup system that copies and archives files. We'll implement a file splitter/merger for large files. And we'll create a complete text file processor with line-by-line processing.

**Let's read and write.**

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

- 📂 **The 2026 Python Metromap: File I/O – Reading & Writing** – Log file analyzer; server log parsing; error extraction; report generation. **⬅️ YOU ARE HERE**

- 📊 **The 2026 Python Metromap: CSV & JSON Processing** – Sales data importer/exporter; vendor CSV integration; API JSON formatting. 🔜 *Up Next*

- ⚠️ **The 2026 Python Metromap: Exception Handling – Graceful Failures** – Resilient web scraper; network error handling; request retries.

- 🔧 **The 2026 Python Metromap: Context Managers – The with Statement** – Database connection pool; automatic resource cleanup.

- 🗺️ **The 2026 Python Metromap: Working with Paths & Directories** – Automated backup system; file organization by date; log rotation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📂 Section 1: File I/O Basics – Opening, Reading, Writing, Closing

File operations in Python use the `open()` function, which returns a file object with methods for reading and writing.

**SOLID Principle Applied: Single Responsibility** – Each file operation method has one purpose.

**Design Pattern: Resource Acquisition Is Initialization (RAII)** – Files are resources that should be properly closed.

```python
"""
FILE I/O BASICS: OPENING, READING, WRITING, CLOSING

This section covers the fundamentals of file operations.

SOLID Principle: Single Responsibility
- Each file operation method has one purpose

Design Pattern: RAII (Resource Acquisition Is Initialization)
- Files are resources that should be properly closed
"""

import os
from typing import List, Optional, Iterator
from datetime import datetime


def demonstrate_file_modes():
    """
    Demonstrates different file opening modes.
    
    Common modes:
    - 'r': Read (default)
    - 'w': Write (overwrites existing)
    - 'a': Append (adds to end)
    - 'x': Exclusive creation (fails if exists)
    - 'b': Binary mode
    - 't': Text mode (default)
    - '+': Read and write
    """
    print("=" * 60)
    print("SECTION 1A: FILE OPENING MODES")
    print("=" * 60)
    
    # WRITE MODE ('w') - Creates or overwrites
    print("\n1. WRITE MODE ('w')")
    print("-" * 40)
    
    with open("demo_write.txt", "w") as f:
        f.write("Hello, World!\n")
        f.write("This is line 2\n")
        f.write("This is line 3\n")
    print("  Created demo_write.txt with 3 lines")
    
    # APPEND MODE ('a') - Adds to end
    print("\n2. APPEND MODE ('a')")
    print("-" * 40)
    
    with open("demo_append.txt", "a") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
    print("  Created demo_append.txt with 2 lines")
    
    with open("demo_append.txt", "a") as f:
        f.write("Line 3 (appended)\n")
    print("  Appended line 3 to demo_append.txt")
    
    # READ MODE ('r') - Reads existing file
    print("\n3. READ MODE ('r')")
    print("-" * 40)
    
    with open("demo_write.txt", "r") as f:
        content = f.read()
    print(f"  Content of demo_write.txt:\n{content}")
    
    # READ AND WRITE MODE ('r+')
    print("\n4. READ AND WRITE MODE ('r+')")
    print("-" * 40)
    
    with open("demo_rw.txt", "w") as f:
        f.write("Original content\n")
    
    with open("demo_rw.txt", "r+") as f:
        content = f.read()
        f.write("Added content at end\n")
    print("  Read and wrote to demo_rw.txt")
    
    # EXCLUSIVE CREATION MODE ('x') - Fails if file exists
    print("\n5. EXCLUSIVE CREATION MODE ('x')")
    print("-" * 40)
    
    try:
        with open("demo_new.txt", "x") as f:
            f.write("New file created")
        print("  Created new file with 'x' mode")
        
        # This will fail
        with open("demo_new.txt", "x") as f:
            f.write("This won't work")
    except FileExistsError as e:
        print(f"  Error: {e}")
    
    # BINARY MODE ('rb', 'wb')
    print("\n6. BINARY MODE ('rb', 'wb')")
    print("-" * 40)
    
    data = b"Binary data \x00\x01\x02\x03"
    with open("demo_binary.bin", "wb") as f:
        f.write(data)
    print(f"  Wrote {len(data)} bytes to binary file")
    
    with open("demo_binary.bin", "rb") as f:
        read_data = f.read()
    print(f"  Read {len(read_data)} bytes from binary file")
    print(f"  Data matches: {data == read_data}")
    
    # Clean up
    print("\n  Cleaning up demo files...")
    for f in ["demo_write.txt", "demo_append.txt", "demo_rw.txt", 
              "demo_new.txt", "demo_binary.bin"]:
        if os.path.exists(f):
            os.remove(f)
    print("  Cleanup complete")


def demonstrate_reading_methods():
    """
    Demonstrates different ways to read files.
    
    Methods:
    - read(): Read entire file
    - readline(): Read one line
    - readlines(): Read all lines into list
    - iteration: Iterate line by line (memory efficient)
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: READING METHODS")
    print("=" * 60)
    
    # Create a sample file
    sample_content = """Line 1: First line
Line 2: Second line with some content
Line 3: Third line
Line 4: Fourth line
Line 5: Fifth and final line
"""
    with open("sample.txt", "w") as f:
        f.write(sample_content)
    
    print("\n1. read() - Entire file as string")
    print("-" * 40)
    
    with open("sample.txt", "r") as f:
        content = f.read()
    print(f"  Length: {len(content)} characters")
    print(f"  Preview: {content[:50]}...")
    
    print("\n2. read(size) - Read specific number of characters")
    print("-" * 40)
    
    with open("sample.txt", "r") as f:
        chunk1 = f.read(10)
        chunk2 = f.read(10)
        chunk3 = f.read(10)
    print(f"  Chunk 1: '{chunk1}'")
    print(f"  Chunk 2: '{chunk2}'")
    print(f"  Chunk 3: '{chunk3}'")
    
    print("\n3. readline() - Read one line at a time")
    print("-" * 40)
    
    with open("sample.txt", "r") as f:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
    print(f"  Line 1: {line1.rstrip()}")
    print(f"  Line 2: {line2.rstrip()}")
    print(f"  Line 3: {line3.rstrip()}")
    
    print("\n4. readlines() - All lines as list")
    print("-" * 40)
    
    with open("sample.txt", "r") as f:
        lines = f.readlines()
    print(f"  Number of lines: {len(lines)}")
    print(f"  First line: {lines[0].rstrip()}")
    
    print("\n5. Iteration - Memory efficient (best for large files)")
    print("-" * 40)
    
    line_count = 0
    with open("sample.txt", "r") as f:
        for line in f:
            line_count += 1
    print(f"  Iterated through {line_count} lines")
    
    print("\n6. seek() and tell() - Moving file pointer")
    print("-" * 40)
    
    with open("sample.txt", "r") as f:
        print(f"  Initial position: {f.tell()}")
        f.read(5)
        print(f"  After reading 5 chars: {f.tell()}")
        f.seek(0)
        print(f"  After seek(0): {f.tell()}")
        f.seek(10)
        print(f"  After seek(10): {f.tell()}")
    
    # Clean up
    os.remove("sample.txt")
    print("\n  Cleaned up sample.txt")


def demonstrate_writing_methods():
    """
    Demonstrates different ways to write to files.
    
    Methods:
    - write(): Write string
    - writelines(): Write list of strings
    - print() with file parameter
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: WRITING METHODS")
    print("=" * 60)
    
    print("\n1. write() - Write string")
    print("-" * 40)
    
    with open("write_demo.txt", "w") as f:
        f.write("First line\n")
        f.write("Second line\n")
        f.write("Third line\n")
    print("  Wrote 3 lines using write()")
    
    print("\n2. writelines() - Write list of strings")
    print("-" * 40)
    
    lines = ["Line A\n", "Line B\n", "Line C\n"]
    with open("writelines_demo.txt", "w") as f:
        f.writelines(lines)
    print(f"  Wrote {len(lines)} lines using writelines()")
    
    print("\n3. print() with file parameter")
    print("-" * 40)
    
    with open("print_demo.txt", "w") as f:
        print("First line", file=f)
        print("Second line", file=f)
        print("Third line", file=f)
    print("  Wrote 3 lines using print()")
    
    print("\n4. Writing different data types (must convert to string)")
    print("-" * 40)
    
    data = {
        "name": "Alice",
        "age": 28,
        "active": True,
        "scores": [95, 87, 92]
    }
    
    with open("data_demo.txt", "w") as f:
        f.write(f"Name: {data['name']}\n")
        f.write(f"Age: {data['age']}\n")
        f.write(f"Active: {data['active']}\n")
        f.write(f"Scores: {', '.join(map(str, data['scores']))}\n")
    print("  Wrote dictionary data to file")
    
    # Read back to verify
    with open("data_demo.txt", "r") as f:
        content = f.read()
    print(f"  Content:\n{content}")
    
    # Clean up
    for f in ["write_demo.txt", "writelines_demo.txt", "print_demo.txt", "data_demo.txt"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


def demonstrate_file_encoding():
    """
    Demonstrates working with different file encodings.
    
    Common encodings:
    - utf-8: Universal (default)
    - ascii: Basic English
    - latin-1: Western European
    - cp1252: Windows default
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: FILE ENCODINGS")
    print("=" * 60)
    
    # UTF-8 (default, supports all Unicode)
    print("\n1. UTF-8 ENCODING")
    print("-" * 40)
    
    utf8_text = "Hello, 世界, こんにちは, 안녕하세요"
    with open("utf8_demo.txt", "w", encoding="utf-8") as f:
        f.write(utf8_text)
    print(f"  Wrote UTF-8 text: {utf8_text[:30]}...")
    
    with open("utf8_demo.txt", "r", encoding="utf-8") as f:
        read_text = f.read()
    print(f"  Read back: {read_text[:30]}...")
    print(f"  Matches: {utf8_text == read_text}")
    
    # ASCII (only basic English)
    print("\n2. ASCII ENCODING (Limited)")
    print("-" * 40)
    
    ascii_text = "Hello World! 123"
    with open("ascii_demo.txt", "w", encoding="ascii") as f:
        f.write(ascii_text)
    print(f"  Wrote ASCII text: {ascii_text}")
    
    try:
        with open("ascii_demo.txt", "w", encoding="ascii") as f:
            f.write("Hello 世界")  # This will fail
    except UnicodeEncodeError as e:
        print(f"  Error writing non-ASCII: {e}")
    
    # Specifying encoding when reading
    print("\n3. SPECIFYING ENCODING WHEN READING")
    print("-" * 40)
    
    with open("utf8_demo.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(f"  Read UTF-8 file correctly: {content[:20]}...")
    
    # Error handling
    print("\n4. ENCODING ERROR HANDLING")
    print("-" * 40)
    
    # Create file with different encoding
    with open("mixed_encoding.txt", "wb") as f:
        f.write(b"Hello \xff World")
    
    try:
        with open("mixed_encoding.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError as e:
        print(f"  Error: {e}")
    
    # Use error handling
    with open("mixed_encoding.txt", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    print(f"  With errors='ignore': '{content}'")
    
    with open("mixed_encoding.txt", "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    print(f"  With errors='replace': '{content}'")
    
    # Clean up
    for f in ["utf8_demo.txt", "ascii_demo.txt", "mixed_encoding.txt"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_file_modes()
    demonstrate_reading_methods()
    demonstrate_writing_methods()
    demonstrate_file_encoding()
```

---

## 📊 Section 2: Log File Analyzer

A complete log file analyzer that reads server logs, extracts errors, and generates reports.

**SOLID Principles Applied:**
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New log patterns can be added

**Design Patterns:**
- Iterator Pattern: Processes log lines one by one
- Strategy Pattern: Different log parsing strategies

```python
"""
LOG FILE ANALYZER

This section builds a complete log file analyzer.

SOLID Principles Applied:
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New log patterns can be added

Design Patterns:
- Iterator Pattern: Processes log lines one by one
- Strategy Pattern: Different log parsing strategies
"""

import os
import re
from typing import List, Dict, Any, Optional, Iterator, Tuple
from datetime import datetime
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from enum import Enum


class LogLevel(Enum):
    """Log severity levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class LogEntry:
    """Represents a single log entry."""
    raw: str
    timestamp: Optional[datetime] = None
    level: Optional[LogLevel] = None
    message: str = ""
    source: str = ""
    line_number: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def is_error(self) -> bool:
        return self.level in [LogLevel.ERROR, LogLevel.CRITICAL]
    
    def is_warning(self) -> bool:
        return self.level == LogLevel.WARNING


class LogParser:
    """
    Parses log files line by line.
    
    Design Pattern: Iterator Pattern - Iterates through log lines
    """
    
    # Common log patterns
    PATTERNS = {
        # Apache/Nginx common log format
        'common': re.compile(
            r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
            r'"(?P<method>\S+) (?P<path>\S+) \S+" '
            r'(?P<status>\d+) (?P<size>\d+)'
        ),
        # Syslog format
        'syslog': re.compile(
            r'(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+'
            r'(?P<host>\S+)\s+(?P<process>[^\[]+)\[?\d*\]?:?\s*(?P<message>.*)'
        ),
        # Python logging format
        'python': re.compile(
            r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+'
            r'(?P<level>[A-Z]+)\s+(?P<module>\S+)\s+(?P<message>.*)'
        ),
        # Generic with timestamp and level
        'generic': re.compile(
            r'(?P<timestamp>\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})?\s*'
            r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)?\s*'
            r'(?P<message>.*)'
        )
    }
    
    @classmethod
    def parse_line(cls, line: str, line_num: int) -> LogEntry:
        """Parse a single log line."""
        entry = LogEntry(raw=line.rstrip(), line_number=line_num)
        
        # Try each pattern
        for pattern_name, pattern in cls.PATTERNS.items():
            match = pattern.search(line)
            if match:
                groups = match.groupdict()
                
                # Parse timestamp
                if groups.get('timestamp'):
                    try:
                        # Try common timestamp formats
                        for fmt in [
                            "%d/%b/%Y:%H:%M:%S %z",
                            "%Y-%m-%d %H:%M:%S,%f",
                            "%b %d %H:%M:%S",
                            "%Y-%m-%d %H:%M:%S"
                        ]:
                            try:
                                entry.timestamp = datetime.strptime(groups['timestamp'], fmt)
                                break
                            except ValueError:
                                continue
                    except Exception:
                        pass
                
                # Parse log level
                if groups.get('level'):
                    try:
                        entry.level = LogLevel(groups['level'].upper())
                    except ValueError:
                        pass
                
                # Parse message
                if groups.get('message'):
                    entry.message = groups['message']
                elif groups.get('path'):
                    entry.message = f"{groups.get('method', '')} {groups.get('path', '')}"
                
                # Store all metadata
                entry.metadata = {k: v for k, v in groups.items() if v}
                break
        
        # If no pattern matched, use raw line as message
        if not entry.message:
            entry.message = line.strip()
        
        # Try to extract level from message if not found
        if not entry.level:
            for level in LogLevel:
                if level.value in line.upper():
                    entry.level = level
                    break
        
        return entry
    
    @classmethod
    def parse_file(cls, filepath: str) -> Iterator[LogEntry]:
        """Parse a log file and yield entries."""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                yield cls.parse_line(line, line_num)


class LogAnalyzer:
    """
    Analyzes log files and generates reports.
    
    Design Pattern: Strategy Pattern - Different analysis strategies
    """
    
    def __init__(self):
        self.entries: List[LogEntry] = []
        self.stats: Dict[str, Any] = {}
    
    def analyze_file(self, filepath: str) -> None:
        """Analyze a log file."""
        self.entries = list(LogParser.parse_file(filepath))
        self._calculate_statistics()
    
    def analyze_files(self, filepaths: List[str]) -> None:
        """Analyze multiple log files."""
        all_entries = []
        for filepath in filepaths:
            all_entries.extend(LogParser.parse_file(filepath))
        self.entries = all_entries
        self._calculate_statistics()
    
    def _calculate_statistics(self) -> None:
        """Calculate statistics from log entries."""
        if not self.entries:
            self.stats = {}
            return
        
        # Basic counts
        total = len(self.entries)
        errors = sum(1 for e in self.entries if e.is_error())
        warnings = sum(1 for e in self.entries if e.is_warning())
        
        # Level distribution
        level_counts = Counter()
        for entry in self.entries:
            if entry.level:
                level_counts[entry.level.value] += 1
        
        # Hourly distribution
        hourly = defaultdict(int)
        for entry in self.entries:
            if entry.timestamp:
                hourly[entry.timestamp.hour] += 1
        
        # Top error messages
        error_messages = Counter()
        for entry in self.entries:
            if entry.is_error() and entry.message:
                # Truncate long messages for grouping
                msg = entry.message[:100]
                error_messages[msg] += 1
        
        # Source/IP distribution
        sources = Counter()
        for entry in self.entries:
            source = entry.metadata.get('ip') or entry.metadata.get('host') or entry.source
            if source:
                sources[source] += 1
        
        self.stats = {
            "total_entries": total,
            "error_count": errors,
            "warning_count": warnings,
            "error_rate": (errors / total * 100) if total > 0 else 0,
            "level_distribution": dict(level_counts),
            "hourly_distribution": dict(hourly),
            "top_errors": error_messages.most_common(10),
            "top_sources": sources.most_common(10),
            "time_range": self._get_time_range()
        }
    
    def _get_time_range(self) -> Optional[Dict]:
        """Get time range of logs."""
        timestamps = [e.timestamp for e in self.entries if e.timestamp]
        if not timestamps:
            return None
        
        return {
            "start": min(timestamps).isoformat(),
            "end": max(timestamps).isoformat(),
            "duration_hours": (max(timestamps) - min(timestamps)).total_seconds() / 3600
        }
    
    def get_errors(self) -> List[LogEntry]:
        """Get all error and critical entries."""
        return [e for e in self.entries if e.is_error()]
    
    def get_warnings(self) -> List[LogEntry]:
        """Get all warning entries."""
        return [e for e in self.entries if e.is_warning()]
    
    def search(self, pattern: str) -> List[LogEntry]:
        """Search for pattern in log messages."""
        pattern_lower = pattern.lower()
        return [e for e in self.entries if pattern_lower in e.message.lower()]
    
    def filter_by_level(self, level: LogLevel) -> List[LogEntry]:
        """Filter entries by log level."""
        return [e for e in self.entries if e.level == level]
    
    def filter_by_time(self, start: datetime, end: datetime) -> List[LogEntry]:
        """Filter entries by time range."""
        return [e for e in self.entries if e.timestamp and start <= e.timestamp <= end]
    
    def generate_report(self) -> str:
        """Generate a detailed analysis report."""
        if not self.entries:
            return "No log data to analyze"
        
        report = []
        report.append("=" * 70)
        report.append("LOG ANALYSIS REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 70)
        
        # Summary
        report.append("\n📊 SUMMARY STATISTICS:")
        report.append(f"  Total entries: {self.stats['total_entries']:,}")
        report.append(f"  Errors: {self.stats['error_count']:,}")
        report.append(f"  Warnings: {self.stats['warning_count']:,}")
        report.append(f"  Error rate: {self.stats['error_rate']:.2f}%")
        
        if self.stats.get('time_range'):
            tr = self.stats['time_range']
            report.append(f"  Time range: {tr['start']} to {tr['end']}")
            report.append(f"  Duration: {tr['duration_hours']:.1f} hours")
        
        # Level distribution
        report.append("\n📈 LOG LEVEL DISTRIBUTION:")
        for level, count in sorted(self.stats['level_distribution'].items()):
            bar_length = min(40, int(count / self.stats['total_entries'] * 40))
            bar = "█" * bar_length + "░" * (40 - bar_length)
            percentage = (count / self.stats['total_entries']) * 100
            report.append(f"  {level:8}: {bar} {percentage:5.1f}% ({count:,})")
        
        # Hourly distribution
        if self.stats['hourly_distribution']:
            report.append("\n🕐 HOURLY DISTRIBUTION:")
            max_count = max(self.stats['hourly_distribution'].values())
            for hour in range(24):
                count = self.stats['hourly_distribution'].get(hour, 0)
                bar_length = int((count / max_count) * 30) if max_count > 0 else 0
                bar = "█" * bar_length
                report.append(f"  {hour:02d}:00 {bar} {count}")
        
        # Top errors
        if self.stats['top_errors']:
            report.append("\n❌ TOP ERROR MESSAGES:")
            for i, (msg, count) in enumerate(self.stats['top_errors'][:5], 1):
                report.append(f"  {i}. [{count}] {msg[:60]}...")
        
        # Top sources
        if self.stats['top_sources']:
            report.append("\n🌐 TOP SOURCES (IP/Host):")
            for i, (source, count) in enumerate(self.stats['top_sources'][:5], 1):
                report.append(f"  {i}. {source}: {count} requests")
        
        report.append("\n" + "=" * 70)
        return "\n".join(report)
    
    def export_errors(self, output_file: str) -> None:
        """Export errors to a file."""
        errors = self.get_errors()
        with open(output_file, 'w') as f:
            f.write(f"ERROR LOG EXPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total errors: {len(errors)}\n")
            f.write("=" * 50 + "\n\n")
            
            for error in errors:
                f.write(f"[Line {error.line_number}] ")
                if error.timestamp:
                    f.write(f"{error.timestamp.strftime('%Y-%m-%d %H:%M:%S')} ")
                f.write(f"{error.level.value if error.level else 'UNKNOWN'}\n")
                f.write(f"  {error.message}\n")
                f.write("-" * 40 + "\n")
        
        print(f"  Exported {len(errors)} errors to {output_file}")


def demonstrate_log_analyzer():
    """
    Demonstrate the log file analyzer.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: LOG FILE ANALYZER")
    print("=" * 60)
    
    # Create a sample log file
    sample_log = """2024-01-15 10:23:45,123 INFO main.py Application started
2024-01-15 10:23:46,456 INFO database.py Connected to database
2024-01-15 10:24:12,789 WARNING api.py Slow response: 2.5s
2024-01-15 10:25:33,012 ERROR auth.py Authentication failed for user 'alice'
2024-01-15 10:26:01,345 CRITICAL payment.py Payment gateway timeout
2024-01-15 10:27:44,678 INFO api.py GET /api/users 200 OK
2024-01-15 10:28:22,901 ERROR database.py Connection pool exhausted
2024-01-15 10:29:15,234 INFO api.py POST /api/orders 201 Created
2024-01-15 10:30:03,567 WARNING cache.py Cache miss for key 'user:123'
2024-01-15 10:31:47,890 ERROR payment.py Invalid card number
2024-01-15 10:32:59,123 INFO main.py Shutdown signal received
"""
    
    with open("sample.log", "w") as f:
        f.write(sample_log)
    print("  Created sample.log")
    
    # Analyze the log
    analyzer = LogAnalyzer()
    analyzer.analyze_file("sample.log")
    
    # Generate report
    print("\n1. ANALYSIS REPORT")
    print("-" * 40)
    report = analyzer.generate_report()
    print(report)
    
    # Export errors
    print("\n2. EXPORTING ERRORS")
    print("-" * 40)
    analyzer.export_errors("errors.txt")
    
    # Search functionality
    print("\n3. SEARCHING LOGS")
    print("-" * 40)
    
    results = analyzer.search("payment")
    print(f"  Found {len(results)} entries containing 'payment':")
    for entry in results[:3]:
        print(f"    [{entry.level.value if entry.level else '?'}] {entry.message[:50]}")
    
    # Filter by level
    print("\n4. FILTERING BY LEVEL")
    print("-" * 40)
    
    errors = analyzer.filter_by_level(LogLevel.ERROR)
    print(f"  ERROR entries: {len(errors)}")
    for error in errors[:3]:
        print(f"    {error.message[:60]}")
    
    # Clean up
    os.remove("sample.log")
    if os.path.exists("errors.txt"):
        os.remove("errors.txt")
    print("\n  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_log_analyzer()
```

---

## 🔧 Section 3: Configuration Manager

A complete configuration manager that reads and writes settings files.

**SOLID Principles Applied:**
- Single Responsibility: Configuration manager handles file I/O
- Dependency Inversion: Depends on file abstraction

**Design Patterns:**
- Singleton Pattern: Single configuration instance
- Builder Pattern: Builds configuration from multiple sources

```python
"""
CONFIGURATION MANAGER

This section builds a configuration manager that reads and writes settings.

SOLID Principles Applied:
- Single Responsibility: Configuration manager handles file I/O
- Dependency Inversion: Depends on file abstraction

Design Patterns:
- Singleton Pattern: Single configuration instance
- Builder Pattern: Builds configuration from multiple sources
"""

import os
import json
from typing import Dict, Any, Optional, List
from pathlib import Path
from datetime import datetime
import configparser


class ConfigFormat:
    """Supported configuration formats."""
    JSON = "json"
    INI = "ini"
    ENV = "env"


class ConfigValue:
    """Configuration value with metadata."""
    
    def __init__(self, value: Any, source: str = "default", 
                 description: str = "", required: bool = False):
        self.value = value
        self.source = source
        self.description = description
        self.required = required
        self.updated_at = datetime.now()
    
    def __repr__(self):
        return f"ConfigValue({self.value}, source={self.source})"


class ConfigurationManager:
    """
    Manages application configuration with file I/O.
    
    Design Pattern: Singleton Pattern - Single config instance
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
        
        self._config: Dict[str, ConfigValue] = {}
        self._file_paths: List[str] = []
        self._initialized = True
    
    def set_defaults(self, defaults: Dict[str, Any]) -> 'ConfigurationManager':
        """Set default configuration values."""
        for key, value in defaults.items():
            if key not in self._config:
                self._config[key] = ConfigValue(value, source="default")
        return self
    
    def load_from_json(self, filepath: str, required: bool = False) -> 'ConfigurationManager':
        """Load configuration from JSON file."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            for key, value in data.items():
                if key in self._config:
                    # Update existing
                    self._config[key].value = value
                    self._config[key].source = filepath
                    self._config[key].updated_at = datetime.now()
                else:
                    # Add new
                    self._config[key] = ConfigValue(value, source=filepath)
            
            self._file_paths.append(filepath)
            print(f"  Loaded config from {filepath}")
        except FileNotFoundError:
            if required:
                raise FileNotFoundError(f"Required config file not found: {filepath}")
            print(f"  Warning: Config file not found: {filepath}")
        except json.JSONDecodeError as e:
            print(f"  Error parsing {filepath}: {e}")
        
        return self
    
    def load_from_ini(self, filepath: str, section: str = "DEFAULT", required: bool = False) -> 'ConfigurationManager':
        """Load configuration from INI file."""
        try:
            config = configparser.ConfigParser()
            config.read(filepath)
            
            if section not in config:
                if required:
                    raise KeyError(f"Section '{section}' not found in {filepath}")
                return self
            
            for key, value in config[section].items():
                # Try to convert to appropriate type
                try:
                    # Try int
                    converted = int(value)
                except ValueError:
                    try:
                        # Try float
                        converted = float(value)
                    except ValueError:
                        # Try bool
                        if value.lower() in ('true', 'yes', 'on', '1'):
                            converted = True
                        elif value.lower() in ('false', 'no', 'off', '0'):
                            converted = False
                        else:
                            converted = value
                
                if key in self._config:
                    self._config[key].value = converted
                    self._config[key].source = filepath
                    self._config[key].updated_at = datetime.now()
                else:
                    self._config[key] = ConfigValue(converted, source=filepath)
            
            self._file_paths.append(filepath)
            print(f"  Loaded config from {filepath} [{section}]")
        except FileNotFoundError:
            if required:
                raise
            print(f"  Warning: Config file not found: {filepath}")
        
        return self
    
    def load_from_env(self, prefix: str = "APP_") -> 'ConfigurationManager':
        """Load configuration from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                
                # Try to convert value
                try:
                    converted = int(value)
                except ValueError:
                    try:
                        converted = float(value)
                    except ValueError:
                        if value.lower() in ('true', 'yes', 'on', '1'):
                            converted = True
                        elif value.lower() in ('false', 'no', 'off', '0'):
                            converted = False
                        else:
                            converted = value
                
                if config_key in self._config:
                    self._config[config_key].value = converted
                    self._config[config_key].source = "env"
                    self._config[config_key].updated_at = datetime.now()
                else:
                    self._config[config_key] = ConfigValue(converted, source="env")
        
        print(f"  Loaded {len([k for k in os.environ if k.startswith(prefix)])} env variables")
        return self
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        if key in self._config:
            return self._config[key].value
        return default
    
    def get_string(self, key: str, default: str = "") -> str:
        """Get string value."""
        value = self.get(key, default)
        return str(value) if value is not None else default
    
    def get_int(self, key: str, default: int = 0) -> int:
        """Get integer value."""
        value = self.get(key, default)
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def get_float(self, key: str, default: float = 0.0) -> float:
        """Get float value."""
        value = self.get(key, default)
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    def get_bool(self, key: str, default: bool = False) -> bool:
        """Get boolean value."""
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', 'yes', 'on', '1')
        return bool(value)
    
    def set(self, key: str, value: Any, source: str = "runtime") -> 'ConfigurationManager':
        """Set configuration value."""
        if key in self._config:
            self._config[key].value = value
            self._config[key].source = source
            self._config[key].updated_at = datetime.now()
        else:
            self._config[key] = ConfigValue(value, source=source)
        return self
    
    def save_to_json(self, filepath: str) -> None:
        """Save current configuration to JSON file."""
        data = {key: cfg.value for key, cfg in self._config.items()}
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        print(f"  Saved configuration to {filepath}")
    
    def save_to_ini(self, filepath: str, section: str = "DEFAULT") -> None:
        """Save current configuration to INI file."""
        config = configparser.ConfigParser()
        config[section] = {key: str(cfg.value) for key, cfg in self._config.items()}
        
        with open(filepath, 'w') as f:
            config.write(f)
        print(f"  Saved configuration to {filepath} [{section}]")
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration values."""
        return {key: cfg.value for key, cfg in self._config.items()}
    
    def get_with_metadata(self) -> Dict[str, Dict]:
        """Get all configuration values with metadata."""
        return {
            key: {
                "value": cfg.value,
                "source": cfg.source,
                "updated_at": cfg.updated_at.isoformat(),
                "description": cfg.description
            }
            for key, cfg in self._config.items()
        }
    
    def validate_required(self) -> List[str]:
        """Check for missing required configuration."""
        missing = []
        for key, cfg in self._config.items():
            if cfg.required and cfg.value is None:
                missing.append(key)
        return missing
    
    def reload(self) -> 'ConfigurationManager':
        """Reload configuration from files."""
        # Save current sources
        sources = set()
        for cfg in self._config.values():
            if cfg.source not in ["default", "runtime", "env"]:
                sources.add(cfg.source)
        
        # Reload from files
        for source in sources:
            if source.endswith('.json'):
                self.load_from_json(source)
            elif source.endswith('.ini'):
                self.load_from_ini(source)
        
        return self
    
    def get_source_report(self) -> str:
        """Generate configuration source report."""
        report = []
        report.append("=" * 50)
        report.append("CONFIGURATION SOURCE REPORT")
        report.append("=" * 50)
        
        for key, cfg in sorted(self._config.items()):
            report.append(f"  {key}: {cfg.value} [{cfg.source}]")
        
        report.append("=" * 50)
        return "\n".join(report)


def demonstrate_config_manager():
    """
    Demonstrate the configuration manager.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: CONFIGURATION MANAGER")
    print("=" * 60)
    
    # Create sample config files
    json_config = {
        "app_name": "Metromap App",
        "version": "1.0.0",
        "debug": True,
        "port": 8080,
        "max_connections": 100
    }
    
    with open("config.json", "w") as f:
        json.dump(json_config, f, indent=2)
    print("  Created config.json")
    
    # INI config
    with open("config.ini", "w") as f:
        f.write("""[DEFAULT]
database_host = localhost
database_port = 5432
database_name = metromap
log_level = INFO
cache_enabled = true
""")
    print("  Created config.ini")
    
    # Set environment variable
    os.environ["APP_API_KEY"] = "secret-key-12345"
    
    # Create configuration manager
    config = ConfigurationManager()
    
    print("\n1. LOADING CONFIGURATION FROM MULTIPLE SOURCES")
    print("-" * 40)
    
    config.set_defaults({
        "app_name": "Default App",
        "version": "0.0.0",
        "debug": False,
        "port": 3000
    })
    
    config.load_from_json("config.json")
    config.load_from_ini("config.ini")
    config.load_from_env("APP_")
    
    print("\n2. ACCESSING CONFIGURATION VALUES")
    print("-" * 40)
    
    print(f"  app_name: {config.get('app_name')}")
    print(f"  version: {config.get('version')}")
    print(f"  debug: {config.get('debug')}")
    print(f"  port: {config.get_int('port')}")
    print(f"  database_host: {config.get('database_host')}")
    print(f"  database_port: {config.get_int('database_port')}")
    print(f"  api_key: {config.get('api_key')}")
    print(f"  log_level: {config.get('log_level', 'INFO')}")
    
    print("\n3. TYPED GETTERS")
    print("-" * 40)
    
    print(f"  port as int: {config.get_int('port')}")
    print(f"  debug as bool: {config.get_bool('debug')}")
    print(f"  cache_enabled as bool: {config.get_bool('cache_enabled')}")
    
    print("\n4. SETTING RUNTIME VALUES")
    print("-" * 40)
    
    config.set("max_retries", 3)
    config.set("timeout", 30)
    config.set("feature_flag_x", True)
    print("  Set runtime values: max_retries, timeout, feature_flag_x")
    
    print("\n5. CONFIGURATION SOURCE REPORT")
    print("-" * 40)
    
    report = config.get_source_report()
    print(report)
    
    print("\n6. SAVING CONFIGURATION")
    print("-" * 40)
    
    config.save_to_json("config_export.json")
    config.save_to_ini("config_export.ini")
    
    print("\n7. ALL CONFIGURATION VALUES")
    print("-" * 40)
    
    all_config = config.get_all()
    for key, value in all_config.items():
        print(f"  {key}: {value}")
    
    # Clean up
    for f in ["config.json", "config.ini", "config_export.json", "config_export.ini"]:
        if os.path.exists(f):
            os.remove(f)
    del os.environ["APP_API_KEY"]
    print("\n  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_config_manager()
```

---

## 📁 Section 4: File Splitter and Merger

A utility for splitting large files into smaller chunks and merging them back together.

**SOLID Principles Applied:**
- Single Responsibility: Split and merge functions have distinct purposes
- Open/Closed: New chunking strategies can be added

**Design Patterns:**
- Iterator Pattern: Processes file in chunks
- Builder Pattern: Builds merged file from chunks

```python
"""
FILE SPLITTER AND MERGER

This section builds utilities for splitting and merging files.

SOLID Principles Applied:
- Single Responsibility: Split and merge have distinct purposes
- Open/Closed: New chunking strategies can be added

Design Patterns:
- Iterator Pattern: Processes file in chunks
- Builder Pattern: Builds merged file from chunks
"""

import os
import hashlib
from typing import List, Optional, Iterator, Tuple
from pathlib import Path
from datetime import datetime


class FileSplitter:
    """
    Splits large files into smaller chunks.
    
    Design Pattern: Iterator Pattern - Iterates through file chunks
    """
    
    def __init__(self, chunk_size: int = 1024 * 1024):  # 1MB default
        self.chunk_size = chunk_size
    
    def split(self, filepath: str, output_dir: str = None) -> List[str]:
        """
        Split a file into chunks.
        
        Args:
            filepath: Path to file to split
            output_dir: Directory for chunks (default: same as file)
            
        Returns:
            List of chunk file paths
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        file_size = os.path.getsize(filepath)
        num_chunks = (file_size + self.chunk_size - 1) // self.chunk_size
        
        if output_dir is None:
            output_dir = os.path.dirname(filepath)
        
        os.makedirs(output_dir, exist_ok=True)
        
        base_name = os.path.basename(filepath)
        name, ext = os.path.splitext(base_name)
        
        chunk_files = []
        
        with open(filepath, 'rb') as f:
            for i in range(num_chunks):
                chunk_data = f.read(self.chunk_size)
                chunk_name = f"{name}.part{i+1:04d}{ext}"
                chunk_path = os.path.join(output_dir, chunk_name)
                
                with open(chunk_path, 'wb') as chunk_file:
                    chunk_file.write(chunk_data)
                
                chunk_files.append(chunk_path)
                print(f"  Created chunk {i+1}/{num_chunks}: {chunk_name}")
        
        # Create manifest file
        manifest_path = os.path.join(output_dir, f"{name}.manifest.txt")
        with open(manifest_path, 'w') as f:
            f.write(f"original_file={filepath}\n")
            f.write(f"original_size={file_size}\n")
            f.write(f"chunk_size={self.chunk_size}\n")
            f.write(f"num_chunks={num_chunks}\n")
            f.write(f"created_at={datetime.now().isoformat()}\n")
            f.write("chunks=\n")
            for chunk in chunk_files:
                chunk_name = os.path.basename(chunk)
                with open(chunk, 'rb') as cf:
                    chunk_hash = hashlib.md5(cf.read()).hexdigest()
                f.write(f"  {chunk_name}:{chunk_hash}\n")
        
        print(f"  Created manifest: {manifest_path}")
        return chunk_files


class FileMerger:
    """
    Merges file chunks back into original file.
    
    Design Pattern: Builder Pattern - Builds file from chunks
    """
    
    def __init__(self):
        self.verified_chunks: List[str] = []
    
    def merge(self, manifest_path: str, output_file: Optional[str] = None) -> str:
        """
        Merge chunks using manifest file.
        
        Args:
            manifest_path: Path to manifest file
            output_file: Output file path (optional)
            
        Returns:
            Path to merged file
        """
        if not os.path.exists(manifest_path):
            raise FileNotFoundError(f"Manifest not found: {manifest_path}")
        
        # Parse manifest
        manifest = self._parse_manifest(manifest_path)
        
        # Verify chunks
        if not self._verify_chunks(manifest):
            raise ValueError("Chunk verification failed")
        
        # Determine output file
        if output_file is None:
            output_file = manifest['original_file']
        
        # Merge chunks
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
        
        with open(output_file, 'wb') as out_f:
            for chunk_path in self.verified_chunks:
                with open(chunk_path, 'rb') as chunk_f:
                    out_f.write(chunk_f.read())
        
        # Verify final file size
        merged_size = os.path.getsize(output_file)
        if merged_size != manifest['original_size']:
            raise ValueError(f"Size mismatch: expected {manifest['original_size']}, got {merged_size}")
        
        print(f"  Merged {len(self.verified_chunks)} chunks into {output_file}")
        return output_file
    
    def _parse_manifest(self, manifest_path: str) -> dict:
        """Parse manifest file."""
        manifest = {}
        chunks = []
        
        with open(manifest_path, 'r') as f:
            lines = f.readlines()
        
        in_chunks = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if line == "chunks=":
                in_chunks = True
                continue
            
            if in_chunks:
                if ':' in line:
                    chunk_name, chunk_hash = line.split(':', 1)
                    chunks.append({
                        'name': chunk_name.strip(),
                        'hash': chunk_hash.strip(),
                        'path': os.path.join(os.path.dirname(manifest_path), chunk_name.strip())
                    })
            else:
                if '=' in line:
                    key, value = line.split('=', 1)
                    manifest[key.strip()] = value.strip()
        
        manifest['chunks'] = chunks
        return manifest
    
    def _verify_chunks(self, manifest: dict) -> bool:
        """Verify chunk integrity using hashes."""
        self.verified_chunks = []
        
        for chunk in manifest['chunks']:
            chunk_path = chunk['path']
            expected_hash = chunk['hash']
            
            if not os.path.exists(chunk_path):
                print(f"  Missing chunk: {chunk['name']}")
                return False
            
            with open(chunk_path, 'rb') as f:
                actual_hash = hashlib.md5(f.read()).hexdigest()
            
            if actual_hash != expected_hash:
                print(f"  Hash mismatch for {chunk['name']}")
                return False
            
            self.verified_chunks.append(chunk_path)
        
        print(f"  Verified {len(self.verified_chunks)} chunks")
        return True


class FileProcessor:
    """
    High-level file processing utilities.
    
    Design Pattern: Facade Pattern - Simplified interface for file operations
    """
    
    @staticmethod
    def get_file_info(filepath: str) -> dict:
        """Get detailed file information."""
        stat = os.stat(filepath)
        return {
            "path": filepath,
            "name": os.path.basename(filepath),
            "size_bytes": stat.st_size,
            "size_mb": stat.st_size / (1024 * 1024),
            "size_gb": stat.st_size / (1024 * 1024 * 1024),
            "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "is_file": os.path.isfile(filepath),
            "is_dir": os.path.isdir(filepath)
        }
    
    @staticmethod
    def calculate_hash(filepath: str, algorithm: str = "md5") -> str:
        """Calculate file hash."""
        hash_func = getattr(hashlib, algorithm)()
        
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hash_func.update(chunk)
        
        return hash_func.hexdigest()
    
    @staticmethod
    def compare_files(file1: str, file2: str) -> bool:
        """Compare two files for equality."""
        if os.path.getsize(file1) != os.path.getsize(file2):
            return False
        
        hash1 = FileProcessor.calculate_hash(file1)
        hash2 = FileProcessor.calculate_hash(file2)
        
        return hash1 == hash2


def demonstrate_splitter_merger():
    """
    Demonstrate the file splitter and merger.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: FILE SPLITTER AND MERGER")
    print("=" * 60)
    
    # Create a sample file
    sample_content = "Hello, World!\n" * 1000  # ~18KB
    with open("sample_large.txt", "w") as f:
        f.write(sample_content)
    
    file_info = FileProcessor.get_file_info("sample_large.txt")
    print(f"\n1. ORIGINAL FILE INFO")
    print("-" * 40)
    print(f"  Name: {file_info['name']}")
    print(f"  Size: {file_info['size_bytes']} bytes ({file_info['size_mb']:.2f} MB)")
    
    # Split the file
    print("\n2. SPLITTING FILE INTO CHUNKS")
    print("-" * 40)
    
    splitter = FileSplitter(chunk_size=4096)  # 4KB chunks
    chunks = splitter.split("sample_large.txt", "chunks")
    
    print(f"\n  Created {len(chunks)} chunks in 'chunks/' directory")
    
    # List chunks
    print("\n3. CHUNK LIST")
    print("-" * 40)
    for i, chunk in enumerate(chunks[:5], 1):
        size = os.path.getsize(chunk)
        print(f"  {os.path.basename(chunk)}: {size} bytes")
    if len(chunks) > 5:
        print(f"  ... and {len(chunks) - 5} more")
    
    # Verify hash of original
    print("\n4. FILE HASH VERIFICATION")
    print("-" * 40)
    
    original_hash = FileProcessor.calculate_hash("sample_large.txt")
    print(f"  Original file hash: {original_hash[:16]}...")
    
    # Merge chunks back
    print("\n5. MERGING CHUNKS BACK")
    print("-" * 40)
    
    merger = FileMerger()
    merged_file = merger.merge("chunks/sample_large.manifest.txt", "sample_restored.txt")
    
    # Compare files
    print("\n6. VERIFYING RESTORED FILE")
    print("-" * 40)
    
    restored_hash = FileProcessor.calculate_hash("sample_restored.txt")
    print(f"  Restored file hash: {restored_hash[:16]}...")
    
    are_equal = FileProcessor.compare_files("sample_large.txt", "sample_restored.txt")
    print(f"  Files are identical: {are_equal}")
    
    # Clean up
    print("\n7. CLEANING UP")
    print("-" * 40)
    
    os.remove("sample_large.txt")
    os.remove("sample_restored.txt")
    
    import shutil
    if os.path.exists("chunks"):
        shutil.rmtree("chunks")
    
    print("  Removed test files and chunks")


if __name__ == "__main__":
    demonstrate_splitter_merger()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **File Modes** – `'r'` (read), `'w'` (write, overwrite), `'a'` (append), `'x'` (exclusive create), `'b'` (binary), `'+'` (read/write).

- **Reading Methods** – `read()` (entire file), `readline()` (one line), `readlines()` (all lines), iteration (memory efficient).

- **Writing Methods** – `write()` (string), `writelines()` (list of strings), `print(..., file=f)`.

- **File Encoding** – UTF-8 (default, universal), ASCII (basic English). Handle errors with `errors='ignore'` or `errors='replace'`.

- **Context Managers** – `with open(...) as f:` automatically closes files, even on errors.

- **Log File Analyzer** – Parse log lines, extract levels, generate reports. Search and filter capabilities.

- **Configuration Manager** – Load from JSON, INI, environment variables. Priority: env > file > default.

- **File Splitter/Merger** – Split large files into chunks. Verify integrity with hashes. Reconstruct original.

- **SOLID Principles Applied** – Single Responsibility (each function has one purpose), Open/Closed (new log patterns can be added), Dependency Inversion (depends on file abstractions).

- **Design Patterns Used** – RAII (resource management), Iterator Pattern (line-by-line processing), Strategy Pattern (parsing strategies), Singleton Pattern (configuration manager), Builder Pattern (file merging), Facade Pattern (file utilities).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Abstraction – Hiding Complexity

- **📚 Series E Catalog:** File & Data Handling Line – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: CSV & JSON Processing (Series E, Story 2)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 1 | 4 | 20% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **30** | **22** | **58%** |

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

**Next Story:** Series E, Story 2: The 2026 Python Metromap: CSV & JSON Processing

---

## 📝 Your Invitation

You've mastered file I/O. Now build something with what you've learned:

1. **Build a log monitoring system** – Watch log files in real-time, send alerts on errors.

2. **Create a configuration manager** – Support YAML, TOML formats. Add encryption for sensitive values.

3. **Build a file encryption tool** – Encrypt/decrypt files using symmetric encryption.

4. **Create a backup system** – Copy files, create archives, verify integrity.

5. **Build a text file processor** – Search and replace across multiple files, line-by-line processing.

**You've mastered file I/O. Next stop: CSV & JSON Processing!**

---

*Found this helpful? Clap, comment, and share what you built with file I/O. Next stop: CSV & JSON Processing!* 🚇