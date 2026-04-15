# The 2026 Python Metromap: Automation with os and sys

## Series H: Web Development & Automation | Story 3 of 5

![The 2026 Python Metromap/images/Automation with os and sys](images/Automation with os and sys.png)

## 📖 Introduction

**Welcome to the third stop on the Web Development & Automation Line.**

You've mastered Flask and Django—building web applications and APIs. But not all automation happens over HTTP. Sometimes you need to automate tasks on your own computer: organizing files, cleaning directories, renaming batches, monitoring system resources, and managing processes.

The `os` and `sys` modules are Python's gateway to the operating system. They provide functions for interacting with the file system, environment variables, command-line arguments, process management, and system information. With these tools, you can write scripts that automate repetitive tasks, manage files across directories, and interact with the underlying operating system.

This story—**The 2026 Python Metromap: Automation with os and sys**—is your guide to system-level automation. We'll build a complete file organizer that sorts files by type, date, and size. We'll create a batch file renamer with pattern matching. We'll build a disk usage analyzer and cleanup tool. We'll implement a process monitor and resource tracker. And we'll create a comprehensive backup automation system.

**Let's automate.**

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
### Series F: Advanced Python Engineering (6 Stories) – COMPLETED
### Series G: Data Science & Visualization (5 Stories) – COMPLETED

### Series H: Web Development & Automation (5 Stories)

- 🌶️ **The 2026 Python Metromap: Flask – Building Web APIs** – URL shortener service; REST endpoints; database storage; redirect logic.

- 🎸 **The 2026 Python Metromap: Django – Full-Stack Web Apps** – Blog platform; user authentication; admin panel; comments system; search functionality.

- 🤖 **The 2026 Python Metromap: Automation with os and sys** – File organizer script; type-based sorting; file renaming; temp directory cleaning. **⬅️ YOU ARE HERE**

- 🕸️ **The 2026 Python Metromap: Web Scraping with BeautifulSoup** – Price monitoring bot; multi-site product tracking; price drop alerts. 🔜 *Up Next*

- ⏰ **The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler** – Daily report emailer; weekly backup system; cron-style job scheduler.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🤖 Section 1: os Module Basics – File System Operations

The `os` module provides functions for interacting with the operating system, including file and directory operations.

**SOLID Principle Applied: Single Responsibility** – Each os function performs one system operation.

**Design Pattern: Facade Pattern** – os module provides simplified interface to system calls.

```python
"""
OS MODULE BASICS: FILE SYSTEM OPERATIONS

This section covers the fundamentals of the os module.

SOLID Principle: Single Responsibility
- Each os function performs one system operation

Design Pattern: Facade Pattern
- os module provides simplified interface to system calls
"""

import os
import sys
import stat
import shutil
from datetime import datetime
from pathlib import Path


def demonstrate_os_basics():
    """
    Demonstrates basic os module functions for file system operations.
    """
    print("=" * 60)
    print("SECTION 1A: OS MODULE BASICS")
    print("=" * 60)
    
    # CURRENT WORKING DIRECTORY
    print("\n1. CURRENT WORKING DIRECTORY")
    print("-" * 40)
    
    cwd = os.getcwd()
    print(f"  Current directory: {cwd}")
    
    # Change directory (commented to avoid changing actual working dir)
    # os.chdir('/tmp')
    # print(f"  Changed to: {os.getcwd()}")
    
    # LIST DIRECTORY CONTENTS
    print("\n2. LISTING DIRECTORY CONTENTS")
    print("-" * 40)
    
    # Create a test directory
    test_dir = "os_test_dir"
    os.makedirs(test_dir, exist_ok=True)
    
    # Create some test files
    for i in range(3):
        with open(os.path.join(test_dir, f"file_{i}.txt"), "w") as f:
            f.write(f"Test file {i}")
    
    os.makedirs(os.path.join(test_dir, "subdir"), exist_ok=True)
    
    # List contents
    contents = os.listdir(test_dir)
    print(f"  Contents of '{test_dir}': {contents}")
    
    # PATH OPERATIONS
    print("\n3. PATH OPERATIONS")
    print("-" * 40)
    
    path = os.path.join(test_dir, "subdir", "nested.txt")
    print(f"  Joined path: {path}")
    print(f"  Dirname: {os.path.dirname(path)}")
    print(f"  Basename: {os.path.basename(path)}")
    print(f"  Split: {os.path.split(path)}")
    print(f"  Splitext: {os.path.splitext(path)}")
    print(f"  Absolute path: {os.path.abspath(path)}")
    
    # FILE INFORMATION
    print("\n4. FILE INFORMATION")
    print("-" * 40)
    
    test_file = os.path.join(test_dir, "file_0.txt")
    file_stat = os.stat(test_file)
    
    print(f"  File: {test_file}")
    print(f"  Size: {file_stat.st_size} bytes")
    print(f"  Permissions: {oct(file_stat.st_mode)[-3:]}")
    print(f"  Created: {datetime.fromtimestamp(file_stat.st_ctime)}")
    print(f"  Modified: {datetime.fromtimestamp(file_stat.st_mtime)}")
    print(f"  Accessed: {datetime.fromtimestamp(file_stat.st_atime)}")
    
    # CHECKING EXISTENCE
    print("\n5. CHECKING EXISTENCE")
    print("-" * 40)
    
    print(f"  Exists: {os.path.exists(test_file)}")
    print(f"  Is file: {os.path.isfile(test_file)}")
    print(f"  Is directory: {os.path.isdir(test_file)}")
    print(f"  Is link: {os.path.islink(test_file)}")
    print(f"  Is absolute: {os.path.isabs(test_file)}")
    
    # FILE PERMISSIONS
    print("\n6. FILE PERMISSIONS")
    print("-" * 40)
    
    print(f"  Readable: {os.access(test_file, os.R_OK)}")
    print(f"  Writable: {os.access(test_file, os.W_OK)}")
    print(f"  Executable: {os.access(test_file, os.X_OK)}")
    
    # RENAME AND REMOVE
    print("\n7. RENAME AND REMOVE")
    print("-" * 40)
    
    rename_from = os.path.join(test_dir, "temp.txt")
    rename_to = os.path.join(test_dir, "renamed.txt")
    
    with open(rename_from, "w") as f:
        f.write("Temporary content")
    
    print(f"  Created: {rename_from}")
    os.rename(rename_from, rename_to)
    print(f"  Renamed to: {rename_to}")
    os.remove(rename_to)
    print(f"  Removed: {rename_to}")
    
    # CREATE AND REMOVE DIRECTORIES
    print("\n8. CREATE AND REMOVE DIRECTORIES")
    print("-" * 40)
    
    new_dir = os.path.join(test_dir, "new_folder")
    os.mkdir(new_dir)
    print(f"  Created directory: {new_dir}")
    os.rmdir(new_dir)
    print(f"  Removed directory: {new_dir}")
    
    # RECURSIVE DIRECTORY OPERATIONS
    print("\n9. RECURSIVE DIRECTORY OPERATIONS")
    print("-" * 40)
    
    nested_dir = os.path.join(test_dir, "parent", "child", "grandchild")
    os.makedirs(nested_dir, exist_ok=True)
    print(f"  Created nested directories: {nested_dir}")
    
    # Walk through directory tree
    print("\n  Walking directory tree:")
    for root, dirs, files in os.walk(test_dir):
        level = root.replace(test_dir, '').count(os.sep)
        indent = '  ' * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = '  ' * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
    
    # ENVIRONMENT VARIABLES
    print("\n10. ENVIRONMENT VARIABLES")
    print("-" * 40)
    
    print(f"  PATH: {os.environ.get('PATH', 'Not set')[:50]}...")
    print(f"  HOME: {os.environ.get('HOME', 'Not set')}")
    print(f"  USER: {os.environ.get('USER', 'Not set')}")
    
    # Set environment variable (only affects current process)
    os.environ['TEST_VAR'] = 'test_value'
    print(f"  TEST_VAR: {os.environ.get('TEST_VAR')}")
    
    # PROCESS INFORMATION
    print("\n11. PROCESS INFORMATION")
    print("-" * 40)
    
    print(f"  Process ID: {os.getpid()}")
    print(f"  Parent PID: {os.getppid()}")
    print(f"  Process group: {os.getpgrp()}")
    
    # Clean up
    print("\n12. CLEANING UP")
    print("-" * 40)
    
    shutil.rmtree(test_dir)
    print(f"  Removed test directory: {test_dir}")


def demonstrate_os_walk():
    """
    Demonstrates recursive directory traversal with os.walk.
    
    os.walk generates file names in a directory tree.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: RECURSIVE DIRECTORY TRAVERSAL (os.walk)")
    print("=" * 60)
    
    # Create a nested directory structure for demonstration
    test_root = "walk_test"
    os.makedirs(test_root, exist_ok=True)
    
    # Create files and subdirectories
    structure = {
        "file1.txt": "Content 1",
        "file2.log": "Log content",
        "subdir1": {
            "file3.txt": "Content 3",
            "file4.py": "print('Hello')",
            "subsubdir": {
                "file5.json": '{"key": "value"}'
            }
        },
        "subdir2": {
            "file6.md": "# Markdown",
            "data.csv": "1,2,3"
        }
    }
    
    def create_structure(base, struct):
        for name, content in struct.items():
            path = os.path.join(base, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, 'w') as f:
                    f.write(content)
    
    create_structure(test_root, structure)
    
    print("\n1. BASIC os.walk()")
    print("-" * 40)
    
    for root, dirs, files in os.walk(test_root):
        level = root.replace(test_root, '').count(os.sep)
        indent = '  ' * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"{indent}  {file}")
    
    # COLLECT ALL FILES
    print("\n2. COLLECTING ALL FILES")
    print("-" * 40)
    
    all_files = []
    for root, dirs, files in os.walk(test_root):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)
    
    print(f"  Total files found: {len(all_files)}")
    for f in all_files:
        print(f"    {f}")
    
    # FILTER BY EXTENSION
    print("\n3. FILTERING BY EXTENSION")
    print("-" * 40)
    
    txt_files = []
    for root, dirs, files in os.walk(test_root):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    
    print(f"  Text files: {txt_files}")
    
    # FIND LARGEST FILE
    print("\n4. FINDING LARGEST FILE")
    print("-" * 40)
    
    largest_file = None
    largest_size = 0
    
    for root, dirs, files in os.walk(test_root):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            if size > largest_size:
                largest_size = size
                largest_file = file_path
    
    print(f"  Largest file: {largest_file} ({largest_size} bytes)")
    
    # CALCULATE TOTAL SIZE
    print("\n5. CALCULATING TOTAL SIZE")
    print("-" * 40)
    
    total_size = 0
    for root, dirs, files in os.walk(test_root):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    
    print(f"  Total size: {total_size} bytes ({total_size / 1024:.2f} KB)")
    
    # DELETE ALL .log FILES
    print("\n6. DELETING FILES BY PATTERN")
    print("-" * 40)
    
    log_files = []
    for root, dirs, files in os.walk(test_root):
        for file in files:
            if file.endswith('.log'):
                log_path = os.path.join(root, file)
                log_files.append(log_path)
                # os.remove(log_path)  # Uncomment to actually delete
                print(f"  Would delete: {log_path}")
    
    print(f"  Found {len(log_files)} log files")
    
    # MODIFYING WALK BEHAVIOR (pruning directories)
    print("\n7. PRUNING DIRECTORIES DURING WALK")
    print("-" * 40)
    
    print("  Skipping 'subdir2' directory:")
    for root, dirs, files in os.walk(test_root):
        # Modify dirs in-place to skip certain directories
        if 'subdir2' in dirs:
            dirs.remove('subdir2')
        
        level = root.replace(test_root, '').count(os.sep)
        indent = '  ' * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"{indent}  {file}")
    
    # Clean up
    print("\n8. CLEANING UP")
    print("-" * 40)
    
    shutil.rmtree(test_root)
    print(f"  Removed test directory: {test_root}")


def demonstrate_os_environ():
    """
    Demonstrates working with environment variables.
    
    Environment variables are key-value pairs that affect process behavior.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: ENVIRONMENT VARIABLES")
    print("=" * 60)
    
    # GET ENVIRONMENT VARIABLES
    print("\n1. GETTING ENVIRONMENT VARIABLES")
    print("-" * 40)
    
    # Get with default
    home = os.environ.get('HOME', '/home/user')
    print(f"  HOME: {home}")
    
    # Get with exception if not found
    try:
        path = os.environ['PATH']
        print(f"  PATH: {path[:80]}...")
    except KeyError:
        print("  PATH not found")
    
    # Check if variable exists
    print(f"  Has HOME: {'HOME' in os.environ}")
    
    # LIST ALL ENVIRONMENT VARIABLES
    print("\n2. LISTING ENVIRONMENT VARIABLES")
    print("-" * 40)
    
    important_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'LANG', 'PYTHONPATH']
    for var in important_vars:
        if var in os.environ:
            print(f"  {var}: {os.environ[var][:60]}...")
    
    # SETTING ENVIRONMENT VARIABLES
    print("\n3. SETTING ENVIRONMENT VARIABLES")
    print("-" * 40)
    
    # Set for current process only
    os.environ['MY_APP_CONFIG'] = 'production'
    print(f"  MY_APP_CONFIG: {os.environ.get('MY_APP_CONFIG')}")
    
    # Update multiple
    os.environ.update({
        'APP_DEBUG': 'false',
        'APP_PORT': '8080',
        'APP_NAME': 'Metromap'
    })
    
    for key, value in os.environ.items():
        if key.startswith('APP_'):
            print(f"  {key}: {value}")
    
    # ENVIRONMENT VARIABLES FOR SUBPROCESSES
    print("\n4. ENVIRONMENT VARIABLES IN SUBPROCESSES")
    print("-" * 40)
    
    import subprocess
    
    # Subprocess inherits environment
    result = subprocess.run(
        ['python', '-c', 'import os; print(os.environ.get("MY_APP_CONFIG", "Not set"))'],
        capture_output=True, text=True
    )
    print(f"  Subprocess output: {result.stdout.strip()}")
    
    # Passing custom environment
    custom_env = os.environ.copy()
    custom_env['CUSTOM_VAR'] = 'custom_value'
    
    result = subprocess.run(
        ['python', '-c', 'import os; print(os.environ.get("CUSTOM_VAR", "Not set"))'],
        env=custom_env, capture_output=True, text=True
    )
    print(f"  With custom env: {result.stdout.strip()}")
    
    # PRACTICAL: LOADING CONFIGURATION
    print("\n5. PRACTICAL: LOADING CONFIGURATION FROM ENV")
    print("-" * 40)
    
    class Config:
        """Configuration loaded from environment variables."""
        
        @classmethod
        def load(cls):
            cls.DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
            cls.PORT = int(os.environ.get('PORT', 8000))
            cls.HOST = os.environ.get('HOST', '0.0.0.0')
            cls.DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
            cls.SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
            cls.API_KEY = os.environ.get('API_KEY')
    
    # Set test values
    os.environ['DEBUG'] = 'true'
    os.environ['PORT'] = '5000'
    
    Config.load()
    print(f"  DEBUG: {Config.DEBUG}")
    print(f"  PORT: {Config.PORT}")
    print(f"  HOST: {Config.HOST}")
    
    # Clean up test variables
    del os.environ['MY_APP_CONFIG']
    del os.environ['APP_DEBUG']
    del os.environ['APP_PORT']
    del os.environ['APP_NAME']
    del os.environ['DEBUG']
    del os.environ['PORT']


if __name__ == "__main__":
    demonstrate_os_basics()
    demonstrate_os_walk()
    demonstrate_os_environ()
```

---

## 📂 Section 2: File Organizer System

A complete file organizer that automatically sorts files by type, date, size, and custom rules.

**SOLID Principles Applied:**
- Single Responsibility: Each organizer rule handles one file type
- Open/Closed: New organization rules can be added

**Design Patterns:**
- Strategy Pattern: Different organization strategies
- Chain of Responsibility: Rules applied in order

```python
"""
FILE ORGANIZER SYSTEM

This section builds a complete file organizer for automatic file sorting.

SOLID Principles Applied:
- Single Responsibility: Each organizer rule handles one file type
- Open/Closed: New organization rules can be added

Design Patterns:
- Strategy Pattern: Different organization strategies
- Chain of Responsibility: Rules applied in order
"""

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Callable
import mimetypes
import hashlib
import argparse


class FileRule:
    """Rule for organizing files."""
    
    def __init__(self, pattern: str, destination: str, priority: int = 10):
        self.pattern = pattern
        self.destination = destination
        self.priority = priority
    
    def matches(self, filename: str) -> bool:
        """Check if file matches this rule."""
        return filename.lower().endswith(self.pattern.lower())


class FileOrganizer:
    """
    Organizes files based on rules.
    
    Design Pattern: Chain of Responsibility - Rules applied in priority order
    """
    
    # Default rules by file type
    DEFAULT_RULES = [
        # Images
        FileRule('.jpg', 'Images', 10),
        FileRule('.jpeg', 'Images', 10),
        FileRule('.png', 'Images', 10),
        FileRule('.gif', 'Images', 10),
        FileRule('.bmp', 'Images', 10),
        FileRule('.svg', 'Images', 10),
        FileRule('.webp', 'Images', 10),
        
        # Documents
        FileRule('.pdf', 'Documents', 10),
        FileRule('.doc', 'Documents', 10),
        FileRule('.docx', 'Documents', 10),
        FileRule('.txt', 'Documents', 10),
        FileRule('.md', 'Documents', 10),
        FileRule('.rtf', 'Documents', 10),
        FileRule('.odt', 'Documents', 10),
        
        # Spreadsheets
        FileRule('.xls', 'Spreadsheets', 10),
        FileRule('.xlsx', 'Spreadsheets', 10),
        FileRule('.csv', 'Spreadsheets', 10),
        FileRule('.ods', 'Spreadsheets', 10),
        
        # Presentations
        FileRule('.ppt', 'Presentations', 10),
        FileRule('.pptx', 'Presentations', 10),
        FileRule('.odp', 'Presentations', 10),
        
        # Archives
        FileRule('.zip', 'Archives', 10),
        FileRule('.tar', 'Archives', 10),
        FileRule('.gz', 'Archives', 10),
        FileRule('.bz2', 'Archives', 10),
        FileRule('.rar', 'Archives', 10),
        FileRule('.7z', 'Archives', 10),
        
        # Audio
        FileRule('.mp3', 'Audio', 10),
        FileRule('.wav', 'Audio', 10),
        FileRule('.flac', 'Audio', 10),
        FileRule('.aac', 'Audio', 10),
        FileRule('.ogg', 'Audio', 10),
        FileRule('.m4a', 'Audio', 10),
        
        # Video
        FileRule('.mp4', 'Video', 10),
        FileRule('.avi', 'Video', 10),
        FileRule('.mov', 'Video', 10),
        FileRule('.mkv', 'Video', 10),
        FileRule('.wmv', 'Video', 10),
        FileRule('.flv', 'Video', 10),
        
        # Code
        FileRule('.py', 'Code', 10),
        FileRule('.js', 'Code', 10),
        FileRule('.html', 'Code', 10),
        FileRule('.css', 'Code', 10),
        FileRule('.json', 'Code', 10),
        FileRule('.xml', 'Code', 10),
        FileRule('.yaml', 'Code', 10),
        FileRule('.yml', 'Code', 10),
        FileRule('.sh', 'Scripts', 10),
        
        # Executables
        FileRule('.exe', 'Executables', 10),
        FileRule('.msi', 'Executables', 10),
        FileRule('.app', 'Applications', 10),
        FileRule('.deb', 'Packages', 10),
        FileRule('.rpm', 'Packages', 10),
        
        # Default
        FileRule('', 'Other', 0),
    ]
    
    def __init__(self, rules: Optional[List[FileRule]] = None):
        self.rules = rules or self.DEFAULT_RULES.copy()
        self._sort_rules()
    
    def _sort_rules(self):
        """Sort rules by priority (higher priority first)."""
        self.rules.sort(key=lambda r: r.priority, reverse=True)
    
    def add_rule(self, rule: FileRule) -> 'FileOrganizer':
        """Add a custom organization rule."""
        self.rules.append(rule)
        self._sort_rules()
        return self
    
    def get_destination(self, filename: str) -> str:
        """Get destination folder for a file."""
        for rule in self.rules:
            if rule.matches(filename):
                return rule.destination
        return "Other"
    
    def organize(self, source_dir: str, dest_root: Optional[str] = None,
                 organize_by_date: bool = False, dry_run: bool = True) -> Dict:
        """
        Organize files in a directory.
        
        Args:
            source_dir: Directory to organize
            dest_root: Root directory for organized files
            organize_by_date: Whether to create date subfolders
            dry_run: If True, only simulate (don't move files)
            
        Returns:
            Dictionary with organization statistics
        """
        source_dir = Path(source_dir).resolve()
        if not source_dir.exists():
            raise FileNotFoundError(f"Directory not found: {source_dir}")
        
        if dest_root is None:
            dest_root = source_dir
        
        dest_root = Path(dest_root).resolve()
        
        organized: Dict[str, List[Path]] = {}
        stats = {
            "total_files": 0,
            "moved": 0,
            "errors": 0,
            "skipped": 0,
            "by_destination": {}
        }
        
        for item in source_dir.iterdir():
            if not item.is_file():
                continue
            
            stats["total_files"] += 1
            
            # Skip hidden files
            if item.name.startswith('.'):
                stats["skipped"] += 1
                print(f"  Skipping hidden file: {item.name}")
                continue
            
            # Determine destination
            dest_folder = self.get_destination(item.name)
            
            if organize_by_date:
                mod_time = datetime.fromtimestamp(item.stat().st_mtime)
                date_folder = mod_time.strftime("%Y/%m")
                dest_folder = os.path.join(dest_folder, date_folder)
            
            # Create destination path
            dest_path = dest_root / dest_folder / item.name
            
            # Record organization
            if dest_folder not in organized:
                organized[dest_folder] = []
                stats["by_destination"][dest_folder] = 0
            
            organized[dest_folder].append(item)
            stats["by_destination"][dest_folder] += 1
            
            if not dry_run:
                try:
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Handle duplicate names
                    counter = 1
                    original_dest = dest_path
                    while dest_path.exists():
                        stem = original_dest.stem
                        suffix = original_dest.suffix
                        dest_path = original_dest.parent / f"{stem}_{counter}{suffix}"
                        counter += 1
                    
                    shutil.move(str(item), str(dest_path))
                    stats["moved"] += 1
                    print(f"  Moved: {item.name} → {dest_folder}/")
                except Exception as e:
                    stats["errors"] += 1
                    print(f"  Error moving {item.name}: {e}")
            else:
                print(f"  [DRY RUN] Would move: {item.name} → {dest_folder}/")
        
        return organized, stats


class FileCleaner:
    """
    Cleans up empty directories and temporary files.
    
    Design Pattern: Strategy Pattern - Different cleanup strategies
    """
    
    def __init__(self):
        self.temp_extensions = ['.tmp', '.temp', '.cache', '.log', '.bak', '.swp']
        self.temp_names = ['Thumbs.db', '.DS_Store', 'desktop.ini']
    
    def clean_empty_dirs(self, root_dir: str, dry_run: bool = True) -> int:
        """Remove empty directories recursively."""
        root_dir = Path(root_dir).resolve()
        deleted = 0
        
        # Process from bottom up
        for dir_path in sorted(root_dir.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if dir_path.is_dir() and not any(dir_path.iterdir()):
                if not dry_run:
                    dir_path.rmdir()
                deleted += 1
                print(f"  {'[DRY RUN] ' if dry_run else ''}Removed empty dir: {dir_path}")
        
        return deleted
    
    def clean_temp_files(self, root_dir: str, dry_run: bool = True) -> int:
        """Remove temporary files."""
        root_dir = Path(root_dir).resolve()
        deleted = 0
        
        for file_path in root_dir.rglob("*"):
            if file_path.is_file():
                should_delete = False
                
                # Check by extension
                if file_path.suffix.lower() in self.temp_extensions:
                    should_delete = True
                
                # Check by name
                if file_path.name in self.temp_names:
                    should_delete = True
                
                if should_delete:
                    if not dry_run:
                        file_path.unlink()
                    deleted += 1
                    print(f"  {'[DRY RUN] ' if dry_run else ''}Removed temp file: {file_path.name}")
        
        return deleted
    
    def clean_duplicates(self, root_dir: str, dry_run: bool = True) -> int:
        """Remove duplicate files (same content)."""
        from collections import defaultdict
        
        root_dir = Path(root_dir).resolve()
        hash_map = defaultdict(list)
        deleted = 0
        
        # Group files by size first (quick filter)
        size_groups = defaultdict(list)
        for file_path in root_dir.rglob("*"):
            if file_path.is_file():
                size_groups[file_path.stat().st_size].append(file_path)
        
        # Check duplicates by hash
        for size, files in size_groups.items():
            if len(files) < 2:
                continue
            
            for file_path in files:
                hash_md5 = hashlib.md5()
                with open(file_path, 'rb') as f:
                    for chunk in iter(lambda: f.read(4096), b''):
                        hash_md5.update(chunk)
                file_hash = hash_md5.hexdigest()
                hash_map[file_hash].append(file_path)
        
        # Delete duplicates (keep first, delete others)
        for file_hash, file_paths in hash_map.items():
            if len(file_paths) > 1:
                # Keep the first file by modification time (most recent)
                file_paths.sort(key=lambda p: p.stat().st_mtime, reverse=True)
                for file_path in file_paths[1:]:
                    if not dry_run:
                        file_path.unlink()
                    deleted += 1
                    print(f"  {'[DRY RUN] ' if dry_run else ''}Removed duplicate: {file_path.name}")
        
        return deleted
    
    def clean_old_files(self, root_dir: str, days_old: int = 30, dry_run: bool = True) -> int:
        """Remove files older than specified days."""
        root_dir = Path(root_dir).resolve()
        cutoff = datetime.now().timestamp() - (days_old * 24 * 60 * 60)
        deleted = 0
        
        for file_path in root_dir.rglob("*"):
            if file_path.is_file() and file_path.stat().st_mtime < cutoff:
                if not dry_run:
                    file_path.unlink()
                deleted += 1
                print(f"  {'[DRY RUN] ' if dry_run else ''}Removed old file: {file_path.name}")
        
        return deleted


class BatchRenamer:
    """
    Batch file renamer with pattern matching.
    
    Design Pattern: Command Pattern - Rename operations as commands
    """
    
    def __init__(self, directory: str):
        self.directory = Path(directory).resolve()
    
    def rename_by_pattern(self, pattern: str, replacement: str, 
                         extension: Optional[str] = None,
                         dry_run: bool = True) -> List[Tuple[Path, Path]]:
        """
        Rename files matching pattern.
        
        Args:
            pattern: Pattern to replace
            replacement: Replacement text
            extension: Optional file extension filter
            dry_run: If True, only simulate
            
        Returns:
            List of (original, new) path tuples
        """
        changes = []
        
        for file_path in self.directory.iterdir():
            if not file_path.is_file():
                continue
            
            if extension and file_path.suffix != extension:
                continue
            
            if pattern in file_path.name:
                new_name = file_path.name.replace(pattern, replacement)
                new_path = file_path.parent / new_name
                
                changes.append((file_path, new_path))
                
                if not dry_run:
                    file_path.rename(new_path)
                    print(f"  Renamed: {file_path.name} → {new_name}")
                else:
                    print(f"  [DRY RUN] Would rename: {file_path.name} → {new_name}")
        
        return changes
    
    def rename_sequential(self, prefix: str, start: int = 1, 
                          extension: Optional[str] = None,
                          dry_run: bool = True) -> List[Tuple[Path, Path]]:
        """
        Rename files sequentially.
        
        Args:
            prefix: Prefix for new names
            start: Starting number
            extension: Optional file extension filter
            dry_run: If True, only simulate
            
        Returns:
            List of (original, new) path tuples
        """
        changes = []
        files = []
        
        for file_path in self.directory.iterdir():
            if not file_path.is_file():
                continue
            
            if extension and file_path.suffix != extension:
                continue
            
            # Sort by modification time
            files.append(file_path)
        
        files.sort(key=lambda p: p.stat().st_mtime)
        
        for i, file_path in enumerate(files, start):
            new_name = f"{prefix}_{i:03d}{file_path.suffix}"
            new_path = file_path.parent / new_name
            
            changes.append((file_path, new_path))
            
            if not dry_run:
                file_path.rename(new_path)
                print(f"  Renamed: {file_path.name} → {new_name}")
            else:
                print(f"  [DRY RUN] Would rename: {file_path.name} → {new_name}")
        
        return changes
    
    def add_prefix_suffix(self, prefix: str = "", suffix: str = "",
                          extension: Optional[str] = None,
                          dry_run: bool = True) -> List[Tuple[Path, Path]]:
        """Add prefix or suffix to filenames."""
        changes = []
        
        for file_path in self.directory.iterdir():
            if not file_path.is_file():
                continue
            
            if extension and file_path.suffix != extension:
                continue
            
            stem = file_path.stem
            new_name = f"{prefix}{stem}{suffix}{file_path.suffix}"
            new_path = file_path.parent / new_name
            
            if new_name != file_path.name:
                changes.append((file_path, new_path))
                
                if not dry_run:
                    file_path.rename(new_path)
                    print(f"  Renamed: {file_path.name} → {new_name}")
                else:
                    print(f"  [DRY RUN] Would rename: {file_path.name} → {new_name}")
        
        return changes


def demonstrate_file_organizer():
    """
    Demonstrate the file organizer system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: FILE ORGANIZER SYSTEM")
    print("=" * 60)
    
    import tempfile
    import shutil
    
    # Create messy directory
    temp_dir = tempfile.mkdtemp()
    messy_dir = Path(temp_dir) / "messy"
    messy_dir.mkdir()
    
    print("\n1. CREATING MESSY DIRECTORY")
    print("-" * 40)
    
    # Create various files
    files = [
        ("document.pdf", "PDF content"),
        ("image.jpg", "Image content"),
        ("spreadsheet.xlsx", "Excel content"),
        ("script.py", "print('Hello')"),
        ("archive.zip", "Zip content"),
        ("song.mp3", "Audio content"),
        ("video.mp4", "Video content"),
        ("readme.txt", "Text content"),
        ("data.json", '{"key": "value"}'),
        ("temp.tmp", "Temporary file"),
        ("backup.bak", "Backup file"),
        ("duplicate1.txt", "Same content"),
        ("duplicate2.txt", "Same content"),
        ("duplicate3.txt", "Same content"),
        (".hidden", "Hidden file"),
    ]
    
    for filename, content in files:
        (messy_dir / filename).write_text(content)
    
    print(f"  Created {len(files)} files in {messy_dir}")
    
    # Show before
    print("\n  Before organization:")
    for f in sorted(messy_dir.iterdir()):
        print(f"    {f.name}")
    
    # Organize by type
    print("\n2. ORGANIZING BY TYPE (Dry Run)")
    print("-" * 40)
    
    organizer = FileOrganizer()
    organized, stats = organizer.organize(str(messy_dir), dry_run=True)
    
    print(f"\n  Would organize {stats['total_files']} files into {len(organized)} folders:")
    for folder, files_list in sorted(organized.items()):
        print(f"    {folder}/ ({len(files_list)} files)")
    
    # Actually organize
    print("\n3. ORGANIZING BY TYPE (Actual)")
    print("-" * 40)
    
    organizer.organize(str(messy_dir), dry_run=False)
    
    # Show after
    print("\n  After organization:")
    for item in sorted(messy_dir.iterdir()):
        if item.is_dir():
            print(f"    📁 {item.name}/")
            for f in sorted(item.iterdir()):
                print(f"      📄 {f.name}")
    
    # Clean up duplicates
    print("\n4. CLEANING DUPLICATES")
    print("-" * 40)
    
    cleaner = FileCleaner()
    duplicates_removed = cleaner.clean_duplicates(str(messy_dir), dry_run=False)
    print(f"  Removed {duplicates_removed} duplicate files")
    
    # Clean temp files
    print("\n5. CLEANING TEMPORARY FILES")
    print("-" * 40)
    
    temps_removed = cleaner.clean_temp_files(str(messy_dir), dry_run=False)
    print(f"  Removed {temps_removed} temporary files")
    
    # Clean empty directories
    print("\n6. CLEANING EMPTY DIRECTORIES")
    print("-" * 40)
    
    empty_dirs = cleaner.clean_empty_dirs(str(messy_dir), dry_run=False)
    print(f"  Removed {empty_dirs} empty directories")
    
    # Batch renaming
    print("\n7. BATCH RENAMING")
    print("-" * 40)
    
    # Create files for renaming
    rename_dir = Path(temp_dir) / "rename_test"
    rename_dir.mkdir()
    
    for i in range(5):
        (rename_dir / f"old_file_{i}.txt").write_text(f"Content {i}")
    
    print(f"  Created 5 files in {rename_dir}")
    
    renamer = BatchRenamer(str(rename_dir))
    renamer.rename_by_pattern("old_", "new_", dry_run=False)
    
    print("\n  After renaming:")
    for f in rename_dir.iterdir():
        print(f"    {f.name}")
    
    # Clean up
    shutil.rmtree(temp_dir)
    print("\n  Cleaned up temp directory")


if __name__ == "__main__":
    demonstrate_file_organizer()
```

---

## 💾 Section 3: System Information and Process Management

Monitor system resources, CPU, memory, disk usage, and manage processes.

**SOLID Principles Applied:**
- Single Responsibility: Each monitoring function tracks one resource
- Dependency Inversion: Depends on OS abstractions

**Design Patterns:**
- Observer Pattern: Monitor system state over time
- Singleton Pattern: Single system monitor instance

```python
"""
SYSTEM INFORMATION AND PROCESS MANAGEMENT

This section covers monitoring system resources and managing processes.

SOLID Principles Applied:
- Single Responsibility: Each monitoring function tracks one resource
- Dependency Inversion: Depends on OS abstractions

Design Patterns:
- Observer Pattern: Monitor system state over time
- Singleton Pattern: Single system monitor instance
"""

import os
import sys
import platform
import psutil
import time
import signal
import subprocess
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import threading


@dataclass
class SystemStats:
    """System statistics snapshot."""
    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    memory_used_gb: float
    memory_total_gb: float
    disk_percent: float
    disk_used_gb: float
    disk_free_gb: float
    network_sent_mb: float
    network_recv_mb: float
    processes: int


class SystemMonitor:
    """
    Monitors system resources.
    
    Design Pattern: Singleton Pattern - Single monitor instance
    Design Pattern: Observer Pattern - Collects system metrics
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
        
        self.history: List[SystemStats] = []
        self._running = False
        self._monitor_thread = None
        self._initialized = True
    
    def get_system_info(self) -> Dict:
        """Get detailed system information."""
        return {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": sys.version,
            "python_implementation": platform.python_implementation(),
        }
    
    def get_cpu_info(self) -> Dict:
        """Get CPU information."""
        return {
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "max_frequency": psutil.cpu_freq().max if psutil.cpu_freq() else None,
            "current_frequency": psutil.cpu_freq().current if psutil.cpu_freq() else None,
            "percent_per_core": psutil.cpu_percent(percpu=True),
            "total_percent": psutil.cpu_percent(),
        }
    
    def get_memory_info(self) -> Dict:
        """Get memory information."""
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        return {
            "total_gb": memory.total / (1024**3),
            "available_gb": memory.available / (1024**3),
            "used_gb": memory.used / (1024**3),
            "percent": memory.percent,
            "swap_total_gb": swap.total / (1024**3),
            "swap_used_gb": swap.used / (1024**3),
            "swap_percent": swap.percent,
        }
    
    def get_disk_info(self) -> List[Dict]:
        """Get disk partition information."""
        disks = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disks.append({
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "fstype": partition.fstype,
                    "total_gb": usage.total / (1024**3),
                    "used_gb": usage.used / (1024**3),
                    "free_gb": usage.free / (1024**3),
                    "percent": usage.percent,
                })
            except PermissionError:
                continue
        
        return disks
    
    def get_network_info(self) -> Dict:
        """Get network information."""
        net_io = psutil.net_io_counters()
        return {
            "bytes_sent_mb": net_io.bytes_sent / (1024**2),
            "bytes_recv_mb": net_io.bytes_recv / (1024**2),
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv,
            "errin": net_io.errin,
            "errout": net_io.errout,
            "dropin": net_io.dropin,
            "dropout": net_io.dropout,
        }
    
    def get_process_list(self, sort_by: str = 'cpu') -> List[Dict]:
        """Get list of running processes."""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 
                                          'status', 'create_time', 'username']):
            try:
                info = proc.info
                processes.append({
                    "pid": info['pid'],
                    "name": info['name'],
                    "cpu_percent": info['cpu_percent'],
                    "memory_percent": info['memory_percent'],
                    "status": info['status'],
                    "username": info['username'],
                    "created": datetime.fromtimestamp(info['create_time']).strftime('%Y-%m-%d %H:%M:%S'),
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Sort processes
        if sort_by == 'cpu':
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        elif sort_by == 'memory':
            processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        
        return processes
    
    def take_snapshot(self) -> SystemStats:
        """Take a system statistics snapshot."""
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        
        stats = SystemStats(
            timestamp=datetime.now(),
            cpu_percent=cpu,
            memory_percent=memory.percent,
            memory_used_gb=memory.used / (1024**3),
            memory_total_gb=memory.total / (1024**3),
            disk_percent=disk.percent,
            disk_used_gb=disk.used / (1024**3),
            disk_free_gb=disk.free / (1024**3),
            network_sent_mb=net.bytes_sent / (1024**2),
            network_recv_mb=net.bytes_recv / (1024**2),
            processes=len(psutil.pids())
        )
        
        self.history.append(stats)
        
        # Keep only last 100 snapshots
        if len(self.history) > 100:
            self.history.pop(0)
        
        return stats
    
    def start_monitoring(self, interval_seconds: float = 5.0):
        """Start background monitoring."""
        if self._running:
            return
        
        self._running = True
        
        def monitor_loop():
            while self._running:
                self.take_snapshot()
                time.sleep(interval_seconds)
        
        self._monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        self._monitor_thread.start()
        print(f"  Started monitoring (interval: {interval_seconds}s)")
    
    def stop_monitoring(self):
        """Stop background monitoring."""
        self._running = False
        if self._monitor_thread:
            self._monitor_thread.join(timeout=2)
        print("  Stopped monitoring")
    
    def get_average_stats(self, last_n: int = 10) -> Dict:
        """Get average statistics from recent snapshots."""
        if not self.history:
            return {}
        
        recent = self.history[-last_n:]
        
        return {
            "avg_cpu_percent": sum(s.cpu_percent for s in recent) / len(recent),
            "avg_memory_percent": sum(s.memory_percent for s in recent) / len(recent),
            "avg_disk_percent": sum(s.disk_percent for s in recent) / len(recent),
            "peak_cpu_percent": max(s.cpu_percent for s in recent),
            "peak_memory_percent": max(s.memory_percent for s in recent),
            "avg_processes": sum(s.processes for s in recent) / len(recent),
        }
    
    def generate_report(self) -> str:
        """Generate a system report."""
        report = []
        report.append("=" * 60)
        report.append("SYSTEM REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        # System info
        sys_info = self.get_system_info()
        report.append("\n📋 SYSTEM INFORMATION:")
        report.append(f"  System: {sys_info['system']} {sys_info['release']}")
        report.append(f"  Node: {sys_info['node']}")
        report.append(f"  Machine: {sys_info['machine']}")
        report.append(f"  Python: {sys_info['python_version'][:50]}")
        
        # CPU info
        cpu_info = self.get_cpu_info()
        report.append("\n🖥️  CPU INFORMATION:")
        report.append(f"  Physical cores: {cpu_info['physical_cores']}")
        report.append(f"  Logical cores: {cpu_info['total_cores']}")
        report.append(f"  Current usage: {cpu_info['total_percent']:.1f}%")
        
        # Memory info
        mem_info = self.get_memory_info()
        report.append("\n💾 MEMORY INFORMATION:")
        report.append(f"  Total: {mem_info['total_gb']:.2f} GB")
        report.append(f"  Used: {mem_info['used_gb']:.2f} GB ({mem_info['percent']:.1f}%)")
        report.append(f"  Available: {mem_info['available_gb']:.2f} GB")
        
        # Disk info
        report.append("\n💿 DISK INFORMATION:")
        for disk in self.get_disk_info():
            report.append(f"  {disk['device']} ({disk['mountpoint']}):")
            report.append(f"    Total: {disk['total_gb']:.2f} GB")
            report.append(f"    Used: {disk['used_gb']:.2f} GB ({disk['percent']:.1f}%)")
            report.append(f"    Free: {disk['free_gb']:.2f} GB")
        
        # Network info
        net_info = self.get_network_info()
        report.append("\n🌐 NETWORK INFORMATION:")
        report.append(f"  Data sent: {net_info['bytes_sent_mb']:.2f} MB")
        report.append(f"  Data received: {net_info['bytes_recv_mb']:.2f} MB")
        
        # Top processes
        report.append("\n📊 TOP PROCESSES BY CPU:")
        for proc in self.get_process_list(sort_by='cpu')[:5]:
            report.append(f"  {proc['pid']:6} {proc['name']:20} CPU: {proc['cpu_percent']:5.1f}%  MEM: {proc['memory_percent']:5.1f}%")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)


class ProcessManager:
    """
    Manages system processes.
    
    Design Pattern: Command Pattern - Process operations as commands
    """
    
    @staticmethod
    def get_process_info(pid: int) -> Optional[Dict]:
        """Get information about a specific process."""
        try:
            proc = psutil.Process(pid)
            return {
                "pid": pid,
                "name": proc.name(),
                "exe": proc.exe(),
                "cwd": proc.cwd(),
                "status": proc.status(),
                "username": proc.username(),
                "cpu_percent": proc.cpu_percent(),
                "memory_percent": proc.memory_percent(),
                "memory_rss_mb": proc.memory_info().rss / (1024**2),
                "memory_vms_mb": proc.memory_info().vms / (1024**2),
                "connections": len(proc.connections()),
                "threads": proc.num_threads(),
                "create_time": datetime.fromtimestamp(proc.create_time()).strftime('%Y-%m-%d %H:%M:%S'),
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return None
    
    @staticmethod
    def kill_process(pid: int, force: bool = False) -> bool:
        """Terminate a process."""
        try:
            proc = psutil.Process(pid)
            if force:
                proc.kill()
            else:
                proc.terminate()
            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
    
    @staticmethod
    def get_process_tree(pid: int) -> List[Dict]:
        """Get process tree for a given PID."""
        tree = []
        
        try:
            proc = psutil.Process(pid)
            tree.append({
                "pid": proc.pid,
                "name": proc.name(),
                "children": []
            })
            
            for child in proc.children(recursive=True):
                tree.append({
                    "pid": child.pid,
                    "name": child.name(),
                    "parent": child.ppid(),
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        
        return tree
    
    @staticmethod
    def find_processes_by_name(name: str) -> List[Dict]:
        """Find processes by name."""
        results = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] and name.lower() in proc.info['name'].lower():
                    results.append({
                        "pid": proc.info['pid'],
                        "name": proc.info['name'],
                        "cmdline": ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else '',
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return results


def demonstrate_system_monitor():
    """
    Demonstrate system monitoring capabilities.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: SYSTEM MONITORING")
    print("=" * 60)
    
    monitor = SystemMonitor()
    
    print("\n1. SYSTEM INFORMATION")
    print("-" * 40)
    
    sys_info = monitor.get_system_info()
    for key, value in sys_info.items():
        print(f"  {key}: {value}")
    
    print("\n2. CPU INFORMATION")
    print("-" * 40)
    
    cpu_info = monitor.get_cpu_info()
    print(f"  Physical cores: {cpu_info['physical_cores']}")
    print(f"  Logical cores: {cpu_info['total_cores']}")
    print(f"  Current usage: {cpu_info['total_percent']:.1f}%")
    print(f"  Per-core usage: {cpu_info['percent_per_core']}")
    
    print("\n3. MEMORY INFORMATION")
    print("-" * 40)
    
    mem_info = monitor.get_memory_info()
    print(f"  Total: {mem_info['total_gb']:.2f} GB")
    print(f"  Used: {mem_info['used_gb']:.2f} GB ({mem_info['percent']:.1f}%)")
    print(f"  Available: {mem_info['available_gb']:.2f} GB")
    
    print("\n4. DISK INFORMATION")
    print("-" * 40)
    
    for disk in monitor.get_disk_info():
        print(f"  {disk['device']} ({disk['mountpoint']}):")
        print(f"    Total: {disk['total_gb']:.2f} GB")
        print(f"    Used: {disk['used_gb']:.2f} GB ({disk['percent']:.1f}%)")
        print(f"    Free: {disk['free_gb']:.2f} GB")
    
    print("\n5. TOP PROCESSES")
    print("-" * 40)
    
    for proc in monitor.get_process_list(sort_by='cpu')[:10]:
        print(f"  PID {proc['pid']:6} {proc['name']:20} CPU: {proc['cpu_percent']:5.1f}%  MEM: {proc['memory_percent']:5.1f}%")
    
    print("\n6. TAKING SYSTEM SNAPSHOT")
    print("-" * 40)
    
    snapshot = monitor.take_snapshot()
    print(f"  CPU: {snapshot.cpu_percent:.1f}%")
    print(f"  Memory: {snapshot.memory_percent:.1f}%")
    print(f"  Disk: {snapshot.disk_percent:.1f}%")
    print(f"  Processes: {snapshot.processes}")
    
    print("\n7. PROCESS DETAILS")
    print("-" * 40)
    
    # Get current Python process
    current_pid = os.getpid()
    proc_info = ProcessManager.get_process_info(current_pid)
    
    if proc_info:
        print(f"  PID: {proc_info['pid']}")
        print(f"  Name: {proc_info['name']}")
        print(f"  Status: {proc_info['status']}")
        print(f"  Memory: {proc_info['memory_rss_mb']:.2f} MB")
        print(f"  Threads: {proc_info['threads']}")
    
    print("\n8. COMPLETE SYSTEM REPORT")
    print("-" * 40)
    
    report = monitor.generate_report()
    print(report[:500] + "...")


if __name__ == "__main__":
    demonstrate_system_monitor()
```

---

## 🔄 Section 4: Backup Automation System

A complete backup automation system that copies files, creates archives, and rotates old backups.

**SOLID Principles Applied:**
- Single Responsibility: Each backup function handles one aspect
- Open/Closed: New backup strategies can be added

**Design Patterns:**
- Command Pattern: Backup operations as commands
- Strategy Pattern: Different backup strategies

```python
"""
BACKUP AUTOMATION SYSTEM

This section builds a complete backup automation system.

SOLID Principles Applied:
- Single Responsibility: Each backup function handles one aspect
- Open/Closed: New backup strategies can be added

Design Patterns:
- Command Pattern: Backup operations as commands
- Strategy Pattern: Different backup strategies
"""

import os
import sys
import shutil
import zipfile
import tarfile
import hashlib
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
import argparse
import glob


@dataclass
class BackupFile:
    """Information about a backed-up file."""
    source: str
    destination: str
    size: int
    hash: str
    modified: datetime


@dataclass
class BackupManifest:
    """Manifest for a backup."""
    backup_id: str
    created_at: datetime
    source_root: str
    destination_root: str
    file_count: int
    total_size: int
    compression: str
    files: List[Dict] = field(default_factory=list)


class BackupManager:
    """
    Manages backups of directories.
    
    Design Pattern: Command Pattern - Backup operations as commands
    """
    
    def __init__(self, backup_root: str):
        self.backup_root = Path(backup_root)
        self.backup_root.mkdir(parents=True, exist_ok=True)
        self.manifests: Dict[str, BackupManifest] = {}
        self._load_manifests()
    
    def _load_manifests(self):
        """Load existing backup manifests."""
        manifest_file = self.backup_root / "backups.json"
        if manifest_file.exists():
            try:
                with open(manifest_file, 'r') as f:
                    data = json.load(f)
                    for backup_id, info in data.items():
                        self.manifests[backup_id] = BackupManifest(
                            backup_id=backup_id,
                            created_at=datetime.fromisoformat(info['created_at']),
                            source_root=info['source_root'],
                            destination_root=info['destination_root'],
                            file_count=info['file_count'],
                            total_size=info['total_size'],
                            compression=info['compression']
                        )
            except (json.JSONDecodeError, KeyError):
                pass
    
    def _save_manifests(self):
        """Save backup manifests."""
        manifest_file = self.backup_root / "backups.json"
        data = {}
        for backup_id, manifest in self.manifests.items():
            data[backup_id] = {
                "created_at": manifest.created_at.isoformat(),
                "source_root": manifest.source_root,
                "destination_root": manifest.destination_root,
                "file_count": manifest.file_count,
                "total_size": manifest.total_size,
                "compression": manifest.compression
            }
        with open(manifest_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _get_file_hash(self, file_path: Path) -> str:
        """Calculate file hash for change detection."""
        hash_md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _should_backup(self, file_path: Path, last_manifest: Optional[BackupManifest]) -> bool:
        """Determine if file should be backed up."""
        if not last_manifest:
            return True
        
        # Check if file was in last backup
        for backed_file in last_manifest.files:
            if backed_file['source'] == str(file_path):
                current_hash = self._get_file_hash(file_path)
                return current_hash != backed_file['hash']
        
        return True
    
    def backup(self, source_dir: str, incremental: bool = False,
               compression: str = 'none', previous_backup_id: Optional[str] = None) -> str:
        """
        Perform a backup of a directory.
        
        Args:
            source_dir: Directory to back up
            incremental: Whether to perform incremental backup
            compression: Compression type (none, zip, tar.gz)
            previous_backup_id: Previous backup ID for incremental
            
        Returns:
            Backup ID
        """
        source_dir = Path(source_dir).resolve()
        if not source_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {source_dir}")
        
        # Generate backup ID
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_id = f"backup_{timestamp}"
        
        # Get previous manifest if needed
        previous_manifest = None
        if incremental and previous_backup_id:
            previous_manifest = self.manifests.get(previous_backup_id)
        
        # Create backup directory
        backup_path = self.backup_root / backup_id
        backup_path.mkdir(parents=True)
        
        # Collect and copy files
        backed_files = []
        total_size = 0
        file_count = 0
        
        print(f"\n  Backing up: {source_dir}")
        
        for file_path in source_dir.rglob("*"):
            if file_path.is_file():
                should_backup = self._should_backup(file_path, previous_manifest)
                
                if should_backup or not incremental:
                    rel_path = file_path.relative_to(source_dir)
                    dest_path = backup_path / rel_path
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    shutil.copy2(file_path, dest_path)
                    
                    stat = file_path.stat()
                    backed_files.append({
                        "source": str(file_path),
                        "destination": str(dest_path),
                        "size": stat.st_size,
                        "hash": self._get_file_hash(file_path),
                        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
                    total_size += stat.st_size
                    file_count += 1
                    print(f"    Copied: {rel_path}")
        
        # Create archive if compression requested
        final_path = backup_path
        if compression != 'none':
            archive_name = f"{backup_id}.{compression}"
            archive_path = self.backup_root / archive_name
            
            if compression == 'zip':
                with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                    for file in backup_path.rglob("*"):
                        if file.is_file():
                            zf.write(file, file.relative_to(backup_path))
            elif compression == 'tar.gz':
                with tarfile.open(archive_path, 'w:gz') as tf:
                    tf.add(backup_path, arcname=backup_id)
            
            # Remove original directory after archiving
            shutil.rmtree(backup_path)
            final_path = archive_path
        
        # Create manifest
        manifest = BackupManifest(
            backup_id=backup_id,
            created_at=datetime.now(),
            source_root=str(source_dir),
            destination_root=str(final_path),
            file_count=file_count,
            total_size=total_size,
            compression=compression,
            files=backed_files
        )
        
        self.manifests[backup_id] = manifest
        self._save_manifests()
        
        print(f"\n  Backup {backup_id} completed: {file_count} files, {total_size / 1024:.1f} KB")
        return backup_id
    
    def restore(self, backup_id: str, target_dir: str) -> int:
        """Restore a backup to a target directory."""
        manifest = self.manifests.get(backup_id)
        if not manifest:
            raise ValueError(f"Backup {backup_id} not found")
        
        target_dir = Path(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
        
        source_path = Path(manifest.destination_root)
        
        # Extract if compressed
        if manifest.compression != 'none':
            import tempfile
            with tempfile.TemporaryDirectory() as tmpdir:
                extract_path = Path(tmpdir)
                
                if manifest.compression == 'zip':
                    with zipfile.ZipFile(source_path, 'r') as zf:
                        zf.extractall(extract_path)
                elif manifest.compression == 'tar.gz':
                    with tarfile.open(source_path, 'r:gz') as tf:
                        tf.extractall(extract_path)
                
                # Copy extracted files to target
                extracted_dir = extract_path / manifest.backup_id
                if extracted_dir.exists():
                    for item in extracted_dir.rglob("*"):
                        if item.is_file():
                            rel_path = item.relative_to(extracted_dir)
                            dest = target_dir / rel_path
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(item, dest)
        else:
            # Copy directly from backup directory
            for item in source_path.rglob("*"):
                if item.is_file():
                    rel_path = item.relative_to(source_path)
                    dest = target_dir / rel_path
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest)
        
        print(f"  Restored {manifest.file_count} files to {target_dir}")
        return manifest.file_count
    
    def list_backups(self) -> List[Dict]:
        """List all backups."""
        backups = []
        for manifest in sorted(self.manifests.values(), key=lambda m: m.created_at, reverse=True):
            backups.append({
                "id": manifest.backup_id,
                "created": manifest.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "files": manifest.file_count,
                "size_kb": round(manifest.total_size / 1024, 1),
                "compression": manifest.compression
            })
        return backups
    
    def delete_old_backups(self, keep_days: int = 30) -> int:
        """Delete backups older than keep_days."""
        cutoff = datetime.now() - timedelta(days=keep_days)
        deleted = 0
        
        for backup_id, manifest in list(self.manifests.items()):
            if manifest.created_at < cutoff:
                # Delete backup files
                backup_path = Path(manifest.destination_root)
                if backup_path.exists():
                    if backup_path.is_dir():
                        shutil.rmtree(backup_path)
                    else:
                        backup_path.unlink()
                
                del self.manifests[backup_id]
                deleted += 1
        
        self._save_manifests()
        print(f"  Deleted {deleted} old backups")
        return deleted
    
    def get_backup_size(self) -> int:
        """Get total size of all backups."""
        total = 0
        for manifest in self.manifests.values():
            total += manifest.total_size
        return total


class FileSync:
    """
    Synchronizes files between directories.
    
    Design Pattern: Command Pattern - Sync operations as commands
    """
    
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir).resolve()
        self.target_dir = Path(target_dir).resolve()
    
    def sync(self, dry_run: bool = True, delete: bool = False) -> Dict:
        """
        Synchronize source to target.
        
        Args:
            dry_run: If True, only simulate
            delete: If True, delete files in target not in source
            
        Returns:
            Statistics dictionary
        """
        stats = {
            "copied": 0,
            "updated": 0,
            "deleted": 0,
            "errors": 0
        }
        
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source not found: {self.source_dir}")
        
        self.target_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy/update files from source to target
        for source_file in self.source_dir.rglob("*"):
            if source_file.is_file():
                rel_path = source_file.relative_to(self.source_dir)
                target_file = self.target_dir / rel_path
                
                if not target_file.exists():
                    # New file
                    if not dry_run:
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source_file, target_file)
                    stats["copied"] += 1
                    print(f"  {'[DRY RUN] ' if dry_run else ''}Copy: {rel_path}")
                
                elif source_file.stat().st_mtime > target_file.stat().st_mtime:
                    # Updated file
                    if not dry_run:
                        shutil.copy2(source_file, target_file)
                    stats["updated"] += 1
                    print(f"  {'[DRY RUN] ' if dry_run else ''}Update: {rel_path}")
        
        # Delete files in target not in source
        if delete:
            for target_file in self.target_dir.rglob("*"):
                if target_file.is_file():
                    rel_path = target_file.relative_to(self.target_dir)
                    source_file = self.source_dir / rel_path
                    
                    if not source_file.exists():
                        if not dry_run:
                            target_file.unlink()
                        stats["deleted"] += 1
                        print(f"  {'[DRY RUN] ' if dry_run else ''}Delete: {rel_path}")
        
        return stats


def demonstrate_backup_system():
    """
    Demonstrate the backup automation system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: BACKUP AUTOMATION SYSTEM")
    print("=" * 60)
    
    import tempfile
    import shutil
    
    # Create test directory
    temp_dir = tempfile.mkdtemp()
    source_dir = Path(temp_dir) / "source"
    backup_root = Path(temp_dir) / "backups"
    
    source_dir.mkdir()
    
    print("\n1. CREATING SAMPLE FILES")
    print("-" * 40)
    
    # Create files
    (source_dir / "file1.txt").write_text("Content of file 1")
    (source_dir / "file2.txt").write_text("Content of file 2")
    
    subdir = source_dir / "subdir"
    subdir.mkdir()
    (subdir / "file3.txt").write_text("Content of file 3")
    (subdir / "config.json").write_text('{"key": "value"}')
    
    print(f"  Created source directory: {source_dir}")
    
    # Create backup manager
    backup_mgr = BackupManager(str(backup_root))
    
    print("\n2. FULL BACKUP")
    print("-" * 40)
    
    backup_id = backup_mgr.backup(str(source_dir))
    print(f"  Created backup: {backup_id}")
    
    print("\n3. MODIFYING FILES")
    print("-" * 40)
    
    # Modify a file
    (source_dir / "file1.txt").write_text("Modified content")
    print("  Modified file1.txt")
    
    # Add a new file
    (source_dir / "file4.txt").write_text("New file")
    print("  Added file4.txt")
    
    print("\n4. INCREMENTAL BACKUP")
    print("-" * 40)
    
    backup_id2 = backup_mgr.backup(str(source_dir), incremental=True, previous_backup_id=backup_id)
    print(f"  Created incremental backup: {backup_id2}")
    
    print("\n5. LISTING BACKUPS")
    print("-" * 40)
    
    backups = backup_mgr.list_backups()
    for backup in backups:
        print(f"  {backup['id']}: {backup['created']}, {backup['files']} files, {backup['size_kb']} KB")
    
    print("\n6. RESTORING BACKUP")
    print("-" * 40)
    
    restore_dir = Path(temp_dir) / "restore"
    files_restored = backup_mgr.restore(backup_id, str(restore_dir))
    print(f"  Restored {files_restored} files to {restore_dir}")
    
    print("\n7. FILE SYNCHRONIZATION")
    print("-" * 40)
    
    sync_source = source_dir
    sync_target = Path(temp_dir) / "sync_target"
    
    syncer = FileSync(str(sync_source), str(sync_target))
    stats = syncer.sync(dry_run=False)
    
    print(f"  Sync results: {stats['copied']} copied, {stats['updated']} updated")
    
    print("\n8. BACKUP SIZE AND CLEANUP")
    print("-" * 40)
    
    total_size = backup_mgr.get_backup_size()
    print(f"  Total backup size: {total_size / 1024:.1f} KB")
    
    # Clean up
    shutil.rmtree(temp_dir)
    print("\n  Cleaned up temp directory")


if __name__ == "__main__":
    demonstrate_backup_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **os Module** – File system operations: `getcwd()`, `listdir()`, `mkdir()`, `rename()`, `remove()`, `walk()`, `environ`.

- **Path Operations** – `os.path.join()`, `os.path.exists()`, `os.path.isfile()`, `os.path.isdir()`, `os.path.getsize()`, `os.path.getmtime()`.

- **os.walk()** – Recursive directory traversal. Generate file paths, filter by extension, find largest files, calculate total size.

- **Environment Variables** – `os.environ` dictionary. Get, set, check existence. Load configuration from environment.

- **File Organizer** – Sort files by type, date, size. Custom rules, duplicate detection, temp file cleanup, batch renaming.

- **System Monitoring** – `psutil` for CPU, memory, disk, network, processes. Real-time monitoring, system snapshots, process management.

- **Process Management** – List processes, get process info, kill processes, find by name, process tree.

- **Backup Automation** – Full and incremental backups. Compression (ZIP, TAR). Manifest tracking, restore, rotation, file synchronization.

- **SOLID Principles Applied** – Single Responsibility (each function has one purpose), Open/Closed (new rules can be added), Dependency Inversion (depends on OS abstractions), Interface Segregation (clean module interfaces).

- **Design Patterns Used** – Facade Pattern (os module interface), Strategy Pattern (organization strategies), Chain of Responsibility (file rules), Command Pattern (backup operations), Observer Pattern (system monitoring), Singleton Pattern (monitor instance).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Django – Full-Stack Web Apps

- **📚 Series H Catalog:** Web Development & Automation – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Web Scraping with BeautifulSoup (Series H, Story 4)

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
| Series G | 5 | 5 | 0 | 100% |
| Series H | 5 | 3 | 2 | 60% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **48** | **4** | **92%** |

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
41. Series G, Story 1: The 2026 Python Metromap: NumPy – Numerical Computing
42. Series G, Story 2: The 2026 Python Metromap: Pandas – Data Wrangling
43. Series G, Story 3: The 2026 Python Metromap: Matplotlib – Basic Plotting
44. Series G, Story 4: The 2026 Python Metromap: Seaborn – Statistical Visualization
45. Series G, Story 5: The 2026 Python Metromap: Real-World EDA Project
46. Series H, Story 1: The 2026 Python Metromap: Flask – Building Web APIs
47. Series H, Story 2: The 2026 Python Metromap: Django – Full-Stack Web Apps
48. Series H, Story 3: The 2026 Python Metromap: Automation with os and sys

**Next Story:** Series H, Story 4: The 2026 Python Metromap: Web Scraping with BeautifulSoup

---

## 📝 Your Invitation

You've mastered system automation. Now build something with what you've learned:

1. **Build a download organizer** – Automatically sort downloaded files into folders by type.

2. **Create a system health monitor** – Build a dashboard showing CPU, memory, disk usage with alerts.

3. **Build a log rotator** – Automatically archive and compress old log files.

4. **Create a photo organizer** – Organize photos by date taken using EXIF data.

5. **Build a disk cleanup tool** – Find and delete duplicate files, temp files, and old downloads.

**You've mastered system automation. Next stop: Web Scraping with BeautifulSoup!**

---

*Found this helpful? Clap, comment, and share what you automated. Next stop: Web Scraping!* 🚇