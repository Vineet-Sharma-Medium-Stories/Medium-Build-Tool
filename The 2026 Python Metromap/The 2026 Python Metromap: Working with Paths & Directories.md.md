# The 2026 Python Metromap: Working with Paths & Directories

## Series E: File & Data Handling Line | Story 5 of 5

![The 2026 Python Metromap/images/Working with Paths and Directories](images/Working with Paths and Directories.png)

## 📖 Introduction

**Welcome to the fifth and final stop on the File & Data Handling Line.**

You've mastered file I/O, structured data, exception handling, and context managers. You can read and write files, process CSV and JSON, handle errors gracefully, and manage resources with context managers. But there's a fundamental skill that ties it all together—working with file paths and directories.

File paths are how you locate files on your system. Directories organize files into hierarchies. Managing paths across different operating systems (Windows, macOS, Linux) can be challenging—Windows uses backslashes, while Unix uses forward slashes. Hardcoding paths leads to brittle code that breaks when moved. Python's `pathlib` module provides an elegant, object-oriented way to handle paths that works across all platforms.

This story—**The 2026 Python Metromap: Working with Paths & Directories**—is your guide to mastering file system operations. We'll build a complete automated backup system that copies files, creates archives, and rotates old backups. We'll create a file organizer that sorts files by type, date, or name. We'll implement a disk usage analyzer that recursively calculates directory sizes. We'll build a file synchronization tool that mirrors directories. And we'll create a comprehensive file system watcher that monitors changes.

**Let's navigate the file system.**

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

- 📂 **The 2026 Python Metromap: File I/O – Reading & Writing** – Log file analyzer; server log parsing; error extraction; report generation.

- 📊 **The 2026 Python Metromap: CSV & JSON Processing – Structured Data** – Sales data importer/exporter; vendor CSV integration; API JSON formatting.

- ⚠️ **The 2026 Python Metromap: Exception Handling – Graceful Failures** – Resilient web scraper; network error handling; request retries.

- 🔧 **The 2026 Python Metromap: Context Managers – The with Statement** – Database connection pool; automatic resource cleanup.

- 🗺️ **The 2026 Python Metromap: Working with Paths & Directories** – Automated backup system; file organization by date; log rotation. **⬅️ YOU ARE HERE**

### Series F: Advanced Python Engineering (6 Stories) – Next Station

- 🎨 **The 2026 Python Metromap: Decorators – Wrapping Functions** – Authentication middleware; logging decorators; API retry logic. 🔜 *Up Next*

- 🔄 **The 2026 Python Metromap: Generators – Memory-Efficient Loops** – Streaming large CSV files; paginated API responses; infinite data streams.

- 🔁 **The 2026 Python Metromap: Iterators – Custom Looping** – Database paginator; file chunk reader; Fibonacci sequence iterator.

- 🧠 **The 2026 Python Metromap: Memory Management & Garbage Collection** – Optimizing a recommendation engine; memory profiling; leak fixing.

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports.

- 📝 **The 2026 Python Metromap: Type Hints & MyPy** – Large team codebase annotations; pre-runtime bug catching; automatic documentation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🗺️ Section 1: Path Basics – pathlib Fundamentals

The `pathlib` module provides an object-oriented interface for working with file system paths across all operating systems.

**SOLID Principle Applied: Single Responsibility** – Path objects represent file system locations.

**Design Pattern: Value Object Pattern** – Paths are immutable value objects.

```python
"""
PATH BASICS: PATHLIB FUNDAMENTALS

This section covers the basics of working with paths using pathlib.

SOLID Principle: Single Responsibility
- Path objects represent file system locations

Design Pattern: Value Object Pattern
- Paths are immutable value objects
"""

from pathlib import Path
import os
import tempfile
from datetime import datetime


def demonstrate_path_creation():
    """
    Demonstrates creating and manipulating Path objects.
    
    Path objects work across Windows, macOS, and Linux.
    """
    print("=" * 60)
    print("SECTION 1A: CREATING AND MANIPULATING PATHS")
    print("=" * 60)
    
    # CREATING PATHS
    print("\n1. CREATING PATH OBJECTS")
    print("-" * 40)
    
    # Current directory
    current = Path.cwd()
    print(f"  Current directory: {current}")
    
    # Home directory
    home = Path.home()
    print(f"  Home directory: {home}")
    
    # From string (platform independent!)
    path1 = Path("data", "files", "document.txt")
    print(f"  Path from parts: {path1}")
    
    # Absolute path
    abs_path = Path("/usr/local/bin")
    print(f"  Absolute path: {abs_path}")
    
    # Path joining (uses correct separator for platform)
    print("\n2. JOINING PATHS (Platform Independent)")
    print("-" * 40)
    
    base = Path("project")
    subdir = base / "src" / "main.py"
    print(f"  Using / operator: {subdir}")
    
    # joinpath method
    joined = base.joinpath("tests", "test_main.py")
    print(f"  Using joinpath: {joined}")
    
    # PARTS OF A PATH
    print("\n3. DECOMPOSING PATHS")
    print("-" * 40)
    
    path = Path("/home/user/documents/report.pdf")
    print(f"  Full path: {path}")
    print(f"  Parent: {path.parent}")
    print(f"  Name: {path.name}")
    print(f"  Stem (name without extension): {path.stem}")
    print(f"  Suffix (extension): {path.suffix}")
    print(f"  Parts: {path.parts}")
    print(f"  Anchor: {path.anchor}")
    
    # MULTIPLE PARENTS
    print("\n4. NAVIGATING PARENTS")
    print("-" * 40)
    
    print(f"  Parent: {path.parent}")
    print(f"  Parent.parent: {path.parent.parent}")
    print(f"  Parents list: {list(path.parents)}")
    
    # RESOLVING PATHS
    print("\n5. RESOLVING PATHS (Absolute, normalized)")
    print("-" * 40)
    
    relative = Path("docs/../src/main.py")
    print(f"  Relative path: {relative}")
    print(f"  Resolved (normalized): {relative.resolve()}")
    
    # Absolute path
    print(f"  Absolute: {relative.absolute()}")
    
    # RELATIVE TO
    print("\n6. RELATIVE PATHS")
    print("-" * 40)
    
    base = Path("/home/user/project")
    target = Path("/home/user/project/src/main.py")
    print(f"  Base: {base}")
    print(f"  Target: {target}")
    print(f"  Relative to base: {target.relative_to(base)}")
    
    # CHANGING NAMES
    print("\n7. MODIFYING PATHS (Creates new Path objects)")
    print("-" * 40)
    
    original = Path("document.txt")
    print(f"  Original: {original}")
    print(f"  With new name: {original.with_name("report.pdf")}")
    print(f"  With new suffix: {original.with_suffix(".md")}")
    print(f"  With new stem: {Path(original.stem + "_v2")}{original.suffix}")


def demonstrate_path_properties_and_checks():
    """
    Demonstrates checking path properties and existence.
    
    Path objects can check if files/directories exist, their types, etc.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: PATH PROPERTIES AND CHECKS")
    print("=" * 60)
    
    # Create temporary files for demonstration
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        
        # Create a file
        file_path = base / "test_file.txt"
        file_path.write_text("Hello, World!")
        
        # Create a directory
        dir_path = base / "test_dir"
        dir_path.mkdir()
        
        # Create a symlink (if supported)
        symlink_path = base / "test_link.txt"
        try:
            symlink_path.symlink_to(file_path)
            has_symlink = True
        except (NotImplementedError, OSError):
            has_symlink = False
        
        print("\n1. EXISTENCE CHECKS")
        print("-" * 40)
        
        print(f"  File exists: {file_path.exists()}")
        print(f"  Directory exists: {dir_path.exists()}")
        print(f"  Non-existent: {base / "nonexistent.txt"} exists? {(base / "nonexistent.txt").exists()}")
        
        print("\n2. TYPE CHECKS")
        print("-" * 40)
        
        print(f"  Is file: {file_path.is_file()}")
        print(f"  Is directory: {file_path.is_dir()}")
        print(f"  Is file (dir): {dir_path.is_file()}")
        print(f"  Is directory (dir): {dir_path.is_dir()}")
        
        if has_symlink:
            print(f"\n  Is symlink: {symlink_path.is_symlink()}")
            print(f"  Symlink target: {symlink_path.resolve()}")
        
        print("\n3. FILE INFORMATION")
        print("-" * 40)
        
        stat = file_path.stat()
        print(f"  Size: {stat.st_size} bytes")
        print(f"  Created: {datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Modified: {datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Accessed: {datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n4. PERMISSIONS")
        print("-" * 40)
        
        print(f"  Readable: {os.access(file_path, os.R_OK)}")
        print(f"  Writable: {os.access(file_path, os.W_OK)}")
        print(f"  Executable: {os.access(file_path, os.X_OK)}")
        
        print("\n5. GLOBBING (Pattern matching)")
        print("-" * 40)
        
        # Create some files for globbing
        (base / "file1.txt").write_text("")
        (base / "file2.txt").write_text("")
        (base / "file3.csv").write_text("")
        (base / "subdir").mkdir()
        (base / "subdir" / "nested.txt").write_text("")
        
        print(f"  All .txt files: {list(base.glob("*.txt"))}")
        print(f"  All files: {list(base.glob("*"))}")
        print(f"  Recursive .txt: {list(base.rglob("*.txt"))}")
        
        print("\n6. DIRECTORY CONTENTS")
        print("-" * 40)
        
        print(f"  Iterating directory:")
        for item in base.iterdir():
            print(f"    {item.name} ({'dir' if item.is_dir() else 'file'})")


def demonstrate_path_operations():
    """
    Demonstrates file and directory operations using pathlib.
    
    Create, rename, delete files and directories.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: FILE AND DIRECTORY OPERATIONS")
    print("=" * 60)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        
        print("\n1. CREATING DIRECTORIES")
        print("-" * 40)
        
        # Create single directory
        new_dir = base / "new_folder"
        new_dir.mkdir()
        print(f"  Created: {new_dir}")
        
        # Create nested directories (parents=True)
        nested = base / "parent" / "child" / "grandchild"
        nested.mkdir(parents=True)
        print(f"  Created nested: {nested}")
        
        # mkdir with exist_ok (no error if exists)
        nested.mkdir(parents=True, exist_ok=True)
        print(f"  mkdir with exist_ok (no error)")
        
        print("\n2. CREATING AND WRITING FILES")
        print("-" * 40)
        
        # Write text
        file_path = base / "sample.txt"
        file_path.write_text("Hello, World!\nSecond line")
        print(f"  Wrote text to {file_path}")
        
        # Read text
        content = file_path.read_text()
        print(f"  Read content: {content}")
        
        # Write bytes
        binary_path = base / "sample.bin"
        binary_path.write_bytes(b'Binary data \x00\x01')
        print(f"  Wrote binary to {binary_path}")
        
        # Append to file
        with file_path.open('a') as f:
            f.write("\nThird line")
        print(f"  Appended to file")
        
        print("\n3. RENAMING AND MOVING")
        print("-" * 40)
        
        # Rename
        renamed = base / "renamed.txt"
        file_path.rename(renamed)
        print(f"  Renamed: {file_path} → {renamed}")
        
        # Move to different directory
        dest_dir = base / "moved"
        dest_dir.mkdir()
        moved = renamed.replace(dest_dir / "moved.txt")
        print(f"  Moved: {renamed} → {moved}")
        
        print("\n4. COPYING (using shutil)")
        print("-" * 40)
        
        import shutil
        copy_path = base / "copy.txt"
        shutil.copy2(moved, copy_path)
        print(f"  Copied: {moved} → {copy_path}")
        
        print("\n5. DELETING")
        print("-" * 40)
        
        # Delete file
        copy_path.unlink()
        print(f"  Deleted file: {copy_path}")
        
        # Delete empty directory
        empty_dir = base / "empty"
        empty_dir.mkdir()
        empty_dir.rmdir()
        print(f"  Deleted empty directory: {empty_dir}")
        
        # Delete directory with contents
        shutil.rmtree(nested.parent)
        print(f"  Deleted directory tree: {nested.parent}")
        
        print("\n6. TOUCH (Create empty file / update timestamp)")
        print("-" * 40)
        
        touch_file = base / "touched.txt"
        touch_file.touch()
        print(f"  Created empty file: {touch_file}")
        
        # Update timestamp
        time.sleep(1)
        touch_file.touch()
        print(f"  Updated timestamp")


if __name__ == "__main__":
    demonstrate_path_creation()
    demonstrate_path_properties_and_checks()
    demonstrate_path_operations()
```

---

## 💾 Section 2: Automated Backup System

A complete automated backup system that copies files, creates archives, and rotates old backups.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of backup
- Open/Closed: New backup strategies can be added

**Design Patterns:**
- Strategy Pattern: Different backup strategies
- Command Pattern: Backup operations as commands

```python
"""
AUTOMATED BACKUP SYSTEM

This section builds a complete automated backup system.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New backup strategies can be added

Design Patterns:
- Strategy Pattern: Different backup strategies
- Command Pattern: Backup operations as commands
"""

import shutil
import zipfile
import tarfile
import hashlib
from pathlib import Path
from typing import List, Dict, Optional, Set, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import json
import time


class BackupStrategy(Enum):
    """Backup strategies."""
    FULL = "full"
    INCREMENTAL = "incremental"
    DIFFERENTIAL = "differential"


class CompressionType(Enum):
    """Compression types."""
    NONE = "none"
    ZIP = "zip"
    TAR_GZ = "tar.gz"
    TAR_BZ2 = "tar.bz2"


@dataclass
class BackupFile:
    """Information about a backed-up file."""
    source_path: str
    dest_path: str
    size: int
    hash: str
    modified_time: datetime
    backed_up_at: datetime


@dataclass
class BackupManifest:
    """Manifest for a backup."""
    backup_id: str
    backup_type: BackupStrategy
    created_at: datetime
    source_root: str
    destination_root: str
    compression: CompressionType
    files: List[BackupFile] = field(default_factory=list)
    total_size: int = 0
    file_count: int = 0
    parent_backup_id: Optional[str] = None


class FileHasher:
    """Utility for calculating file hashes."""
    
    @staticmethod
    def md5(file_path: Path) -> str:
        """Calculate MD5 hash of a file."""
        hash_md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    @staticmethod
    def sha256(file_path: Path) -> str:
        """Calculate SHA256 hash of a file."""
        hash_sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()


class BackupManager:
    """
    Manages backups of directories.
    
    Design Pattern: Strategy Pattern - Different backup strategies
    """
    
    def __init__(self, backup_root: Path):
        self.backup_root = Path(backup_root)
        self.backup_root.mkdir(parents=True, exist_ok=True)
        self.manifests: Dict[str, BackupManifest] = {}
        self._load_manifests()
    
    def _load_manifests(self):
        """Load existing backup manifests."""
        manifest_file = self.backup_root / "backups.json"
        if manifest_file.exists():
            with open(manifest_file, 'r') as f:
                data = json.load(f)
                # Would parse into manifests (simplified)
    
    def _save_manifests(self):
        """Save backup manifests."""
        manifest_file = self.backup_root / "backups.json"
        data = {}
        for backup_id, manifest in self.manifests.items():
            data[backup_id] = {
                "backup_id": manifest.backup_id,
                "backup_type": manifest.backup_type.value,
                "created_at": manifest.created_at.isoformat(),
                "source_root": manifest.source_root,
                "file_count": manifest.file_count,
                "total_size": manifest.total_size
            }
        with open(manifest_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _get_backup_path(self, backup_id: str) -> Path:
        """Get the path for a backup."""
        return self.backup_root / backup_id
    
    def _get_file_hash(self, file_path: Path) -> str:
        """Get file hash for change detection."""
        return FileHasher.md5(file_path)
    
    def _get_file_state(self, file_path: Path) -> Dict:
        """Get current state of a file."""
        stat = file_path.stat()
        return {
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime),
            "hash": self._get_file_hash(file_path)
        }
    
    def _should_backup(self, file_path: Path, last_manifest: Optional[BackupManifest]) -> bool:
        """Determine if file should be backed up."""
        if not last_manifest:
            return True
        
        # Find file in last backup
        for backed_file in last_manifest.files:
            if Path(backed_file.source_path) == file_path:
                current_state = self._get_file_state(file_path)
                return current_state["hash"] != backed_file.hash
        
        return True
    
    def backup(self, source_dir: Path, strategy: BackupStrategy = BackupStrategy.FULL,
               compression: CompressionType = CompressionType.NONE,
               previous_backup_id: Optional[str] = None) -> str:
        """
        Perform a backup of a directory.
        
        Args:
            source_dir: Directory to back up
            strategy: Full, incremental, or differential
            compression: Compression type
            previous_backup_id: Previous backup ID (for incremental/differential)
            
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
        if strategy != BackupStrategy.FULL and previous_backup_id:
            previous_manifest = self.manifests.get(previous_backup_id)
        
        # Create backup directory
        backup_path = self._get_backup_path(backup_id)
        backup_path.mkdir(parents=True)
        
        # Collect files to back up
        files_to_backup = []
        manifest_files = []
        total_size = 0
        
        for file_path in source_dir.rglob("*"):
            if file_path.is_file():
                should_backup = self._should_backup(file_path, previous_manifest)
                if should_backup:
                    files_to_backup.append(file_path)
                
                # Always include in manifest (even if not backed up for incremental)
                rel_path = file_path.relative_to(source_dir)
                manifest_files.append((file_path, rel_path, should_backup))
        
        # Copy files
        backed_files = []
        for file_path, rel_path, backed in files_to_backup:
            dest_path = backup_path / rel_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            if backed:
                shutil.copy2(file_path, dest_path)
                stat = file_path.stat()
                backed_files.append(BackupFile(
                    source_path=str(file_path),
                    dest_path=str(dest_path),
                    size=stat.st_size,
                    hash=self._get_file_hash(file_path),
                    modified_time=datetime.fromtimestamp(stat.st_mtime),
                    backed_up_at=datetime.now()
                ))
                total_size += stat.st_size
        
        # Create archive if compression requested
        final_path = backup_path
        if compression != CompressionType.NONE:
            archive_name = f"{backup_id}.{compression.value}"
            archive_path = self.backup_root / archive_name
            
            if compression == CompressionType.ZIP:
                with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                    for file in backup_path.rglob("*"):
                        if file.is_file():
                            zf.write(file, file.relative_to(backup_path))
            elif compression == CompressionType.TAR_GZ:
                with tarfile.open(archive_path, 'w:gz') as tf:
                    tf.add(backup_path, arcname=backup_id)
            
            # Remove original directory after archiving
            shutil.rmtree(backup_path)
            final_path = archive_path
        
        # Create manifest
        manifest = BackupManifest(
            backup_id=backup_id,
            backup_type=strategy,
            created_at=datetime.now(),
            source_root=str(source_dir),
            destination_root=str(final_path),
            compression=compression,
            files=backed_files,
            total_size=total_size,
            file_count=len(backed_files),
            parent_backup_id=previous_backup_id
        )
        
        self.manifests[backup_id] = manifest
        self._save_manifests()
        
        print(f"  Backup {backup_id} completed: {len(backed_files)} files, {total_size / 1024:.1f} KB")
        return backup_id
    
    def restore(self, backup_id: str, target_dir: Path) -> int:
        """Restore a backup to a target directory."""
        manifest = self.manifests.get(backup_id)
        if not manifest:
            raise ValueError(f"Backup {backup_id} not found")
        
        target_dir = Path(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
        
        source_path = Path(manifest.destination_root)
        
        # Extract if compressed
        if manifest.compression != CompressionType.NONE:
            import tempfile
            with tempfile.TemporaryDirectory() as tmpdir:
                extract_path = Path(tmpdir)
                
                if manifest.compression == CompressionType.ZIP:
                    with zipfile.ZipFile(source_path, 'r') as zf:
                        zf.extractall(extract_path)
                elif manifest.compression in [CompressionType.TAR_GZ, CompressionType.TAR_BZ2]:
                    mode = 'r:gz' if manifest.compression == CompressionType.TAR_GZ else 'r:bz2'
                    with tarfile.open(source_path, mode) as tf:
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
        
        print(f"  Restored {backup_id} to {target_dir}")
        return manifest.file_count
    
    def list_backups(self) -> List[Dict]:
        """List all backups."""
        backups = []
        for manifest in sorted(self.manifests.values(), key=lambda m: m.created_at, reverse=True):
            backups.append({
                "id": manifest.backup_id,
                "type": manifest.backup_type.value,
                "created": manifest.created_at.isoformat(),
                "files": manifest.file_count,
                "size_kb": round(manifest.total_size / 1024, 1)
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


def demonstrate_backup_system():
    """
    Demonstrate the automated backup system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: AUTOMATED BACKUP SYSTEM")
    print("=" * 60)
    
    import tempfile
    import shutil
    
    # Create sample directory structure
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
    print(f"  Files: file1.txt, file2.txt, subdir/file3.txt, subdir/config.json")
    
    # Create backup manager
    backup_mgr = BackupManager(backup_root)
    
    print("\n2. FULL BACKUP")
    print("-" * 40)
    
    backup_id = backup_mgr.backup(source_dir, strategy=BackupStrategy.FULL)
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
    
    backup_id2 = backup_mgr.backup(source_dir, strategy=BackupStrategy.INCREMENTAL,
                                   previous_backup_id=backup_id)
    print(f"  Created incremental backup: {backup_id2}")
    
    print("\n5. LISTING BACKUPS")
    print("-" * 40)
    
    backups = backup_mgr.list_backups()
    for backup in backups:
        print(f"  {backup['id']}: {backup['type']}, {backup['files']} files, {backup['size_kb']} KB")
    
    print("\n6. RESTORING BACKUP")
    print("-" * 40)
    
    restore_dir = Path(temp_dir) / "restore"
    files_restored = backup_mgr.restore(backup_id, restore_dir)
    print(f"  Restored {files_restored} files to {restore_dir}")
    
    # Verify restored files
    print("\n  Restored files:")
    for file in restore_dir.rglob("*"):
        if file.is_file():
            print(f"    {file.relative_to(restore_dir)}")
    
    print("\n7. DELETING OLD BACKUPS")
    print("-" * 40)
    
    # Create a fake old backup (modify timestamp in manifest)
    old_manifest = BackupManifest(
        backup_id="old_backup",
        backup_type=BackupStrategy.FULL,
        created_at=datetime.now() - timedelta(days=100),
        source_root=str(source_dir),
        destination_root=str(backup_root / "old"),
        compression=CompressionType.NONE
    )
    backup_mgr.manifests["old_backup"] = old_manifest
    
    deleted = backup_mgr.delete_old_backups(keep_days=30)
    print(f"  Deleted {deleted} backup(s)")
    
    # Clean up
    shutil.rmtree(temp_dir)
    print("\n  Cleaned up temp directory")


if __name__ == "__main__":
    demonstrate_backup_system()
```

---

## 📂 Section 3: File Organizer

A file organizer that automatically sorts files by type, date, or custom rules.

**SOLID Principles Applied:**
- Single Responsibility: Each organizer rule handles one file type
- Open/Closed: New organization rules can be added

**Design Patterns:**
- Strategy Pattern: Different organization strategies
- Chain of Responsibility: Rules applied in order

```python
"""
FILE ORGANIZER

This section builds a file organizer for automatic file sorting.

SOLID Principles Applied:
- Single Responsibility: Each organizer rule handles one file type
- Open/Closed: New organization rules can be added

Design Patterns:
- Strategy Pattern: Different organization strategies
- Chain of Responsibility: Rules applied in order
"""

from pathlib import Path
from typing import Dict, List, Optional, Callable, Tuple
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum
import shutil
import mimetypes


class OrganizationMode(Enum):
    """File organization modes."""
    BY_TYPE = "by_type"
    BY_DATE = "by_date"
    BY_SIZE = "by_size"
    BY_NAME = "by_name"
    CUSTOM = "custom"


@dataclass
class FileRule:
    """Rule for organizing files."""
    pattern: str  # File extension or pattern
    destination: str  # Destination folder name
    priority: int = 0
    condition: Optional[Callable[[Path], bool]] = None
    
    def matches(self, file_path: Path) -> bool:
        """Check if file matches this rule."""
        if self.condition:
            return self.condition(file_path)
        
        # Check by extension
        return file_path.suffix.lower() == self.pattern.lower()


class FileOrganizer:
    """
    Organizes files based on rules.
    
    Design Pattern: Chain of Responsibility - Rules applied in priority order
    """
    
    # Default rules by file type
    DEFAULT_RULES = [
        # Images
        FileRule(".jpg", "Images", 10),
        FileRule(".jpeg", "Images", 10),
        FileRule(".png", "Images", 10),
        FileRule(".gif", "Images", 10),
        FileRule(".bmp", "Images", 10),
        FileRule(".svg", "Images", 10),
        
        # Documents
        FileRule(".pdf", "Documents", 10),
        FileRule(".doc", "Documents", 10),
        FileRule(".docx", "Documents", 10),
        FileRule(".txt", "Documents", 10),
        FileRule(".md", "Documents", 10),
        FileRule(".rtf", "Documents", 10),
        
        # Spreadsheets
        FileRule(".xls", "Spreadsheets", 10),
        FileRule(".xlsx", "Spreadsheets", 10),
        FileRule(".csv", "Spreadsheets", 10),
        
        # Presentations
        FileRule(".ppt", "Presentations", 10),
        FileRule(".pptx", "Presentations", 10),
        
        # Archives
        FileRule(".zip", "Archives", 10),
        FileRule(".tar", "Archives", 10),
        FileRule(".gz", "Archives", 10),
        FileRule(".rar", "Archives", 10),
        FileRule(".7z", "Archives", 10),
        
        # Audio
        FileRule(".mp3", "Audio", 10),
        FileRule(".wav", "Audio", 10),
        FileRule(".flac", "Audio", 10),
        FileRule(".aac", "Audio", 10),
        
        # Video
        FileRule(".mp4", "Video", 10),
        FileRule(".avi", "Video", 10),
        FileRule(".mov", "Video", 10),
        FileRule(".mkv", "Video", 10),
        FileRule(".wmv", "Video", 10),
        
        # Code
        FileRule(".py", "Code", 10),
        FileRule(".js", "Code", 10),
        FileRule(".html", "Code", 10),
        FileRule(".css", "Code", 10),
        FileRule(".json", "Code", 10),
        FileRule(".xml", "Code", 10),
        FileRule(".yaml", "Code", 10),
        FileRule(".yml", "Code", 10),
        
        # Executables
        FileRule(".exe", "Executables", 10),
        FileRule(".msi", "Executables", 10),
        FileRule(".sh", "Scripts", 10),
        FileRule(".bat", "Scripts", 10),
        
        # Default
        FileRule("", "Other", 0),
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
    
    def get_destination(self, file_path: Path) -> str:
        """Get destination folder for a file."""
        for rule in self.rules:
            if rule.matches(file_path):
                return rule.destination
        return "Other"
    
    def organize(self, source_dir: Path, dest_root: Optional[Path] = None,
                 mode: OrganizationMode = OrganizationMode.BY_TYPE,
                 dry_run: bool = True) -> Dict[str, List[Path]]:
        """
        Organize files in a directory.
        
        Args:
            source_dir: Directory to organize
            dest_root: Root directory for organized files (default: same as source)
            mode: Organization mode
            dry_run: If True, only simulate (don't move files)
            
        Returns:
            Dictionary mapping destination folders to lists of files
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
            "by_destination": {}
        }
        
        for file_path in source_dir.rglob("*"):
            if not file_path.is_file():
                continue
            
            stats["total_files"] += 1
            
            # Determine destination
            if mode == OrganizationMode.BY_TYPE:
                dest_folder = self.get_destination(file_path)
            elif mode == OrganizationMode.BY_DATE:
                mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                dest_folder = mod_time.strftime("%Y/%m")
            elif mode == OrganizationMode.BY_SIZE:
                size = file_path.stat().st_size
                if size < 1024:
                    dest_folder = "tiny_1KB"
                elif size < 1024 * 1024:
                    dest_folder = "small_1MB"
                elif size < 10 * 1024 * 1024:
                    dest_folder = "medium_10MB"
                elif size < 100 * 1024 * 1024:
                    dest_folder = "large_100MB"
                else:
                    dest_folder = "huge"
            elif mode == OrganizationMode.BY_NAME:
                first_char = file_path.name[0].lower()
                if first_char.isalpha():
                    dest_folder = first_char.upper()
                else:
                    dest_folder = "0-9"
            else:  # CUSTOM
                dest_folder = self.get_destination(file_path)
            
            # Create destination path
            dest_path = dest_root / dest_folder / file_path.name
            
            # Record organization
            if dest_folder not in organized:
                organized[dest_folder] = []
                stats["by_destination"][dest_folder] = 0
            
            organized[dest_folder].append(file_path)
            stats["by_destination"][dest_folder] += 1
            
            if not dry_run:
                try:
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Handle duplicate names
                    if dest_path.exists():
                        stem = dest_path.stem
                        suffix = dest_path.suffix
                        counter = 1
                        while dest_path.exists():
                            dest_path = dest_path.parent / f"{stem}_{counter}{suffix}"
                            counter += 1
                    
                    shutil.move(str(file_path), str(dest_path))
                    stats["moved"] += 1
                    print(f"  Moved: {file_path.name} → {dest_folder}/")
                except Exception as e:
                    stats["errors"] += 1
                    print(f"  Error moving {file_path.name}: {e}")
        
        return organized, stats


class FileCleaner:
    """
    Cleans up empty directories and temporary files.
    
    Design Pattern: Strategy Pattern - Different cleanup strategies
    """
    
    def __init__(self):
        self.temp_patterns = [".tmp", ".temp", "~", ".cache", ".log"]
    
    def clean_empty_dirs(self, root_dir: Path, dry_run: bool = True) -> int:
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
    
    def clean_temp_files(self, root_dir: Path, dry_run: bool = True) -> int:
        """Remove temporary files."""
        root_dir = Path(root_dir).resolve()
        deleted = 0
        
        for file_path in root_dir.rglob("*"):
            if file_path.is_file():
                should_delete = False
                
                # Check by extension
                if file_path.suffix.lower() in self.temp_patterns:
                    should_delete = True
                
                # Check for backup files
                if file_path.name.endswith(".bak") or file_path.name.endswith(".backup"):
                    should_delete = True
                
                if should_delete:
                    if not dry_run:
                        file_path.unlink()
                    deleted += 1
                    print(f"  {'[DRY RUN] ' if dry_run else ''}Removed temp file: {file_path.name}")
        
        return deleted
    
    def clean_duplicates(self, root_dir: Path, dry_run: bool = True) -> int:
        """Remove duplicate files (same content)."""
        from collections import defaultdict
        import hashlib
        
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
                # Keep the first file, delete the rest
                for file_path in file_paths[1:]:
                    if not dry_run:
                        file_path.unlink()
                    deleted += 1
                    print(f"  {'[DRY RUN] ' if dry_run else ''}Removed duplicate: {file_path.name}")
        
        return deleted


def demonstrate_file_organizer():
    """
    Demonstrate the file organizer.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: FILE ORGANIZER")
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
    organized, stats = organizer.organize(messy_dir, mode=OrganizationMode.BY_TYPE, dry_run=True)
    
    print(f"\n  Would organize into {len(organized)} folders:")
    for folder, files_list in sorted(organized.items()):
        print(f"    {folder}/ ({len(files_list)} files)")
    
    # Actually organize
    print("\n3. ORGANIZING BY TYPE (Actual)")
    print("-" * 40)
    
    organizer.organize(messy_dir, mode=OrganizationMode.BY_TYPE, dry_run=False)
    
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
    duplicates_removed = cleaner.clean_duplicates(messy_dir, dry_run=False)
    print(f"  Removed {duplicates_removed} duplicate files")
    
    # Clean temp files
    print("\n5. CLEANING TEMPORARY FILES")
    print("-" * 40)
    
    temps_removed = cleaner.clean_temp_files(messy_dir, dry_run=False)
    print(f"  Removed {temps_removed} temporary files")
    
    # Clean empty directories
    print("\n6. CLEANING EMPTY DIRECTORIES")
    print("-" * 40)
    
    empty_dirs = cleaner.clean_empty_dirs(messy_dir, dry_run=False)
    print(f"  Removed {empty_dirs} empty directories")
    
    # Final state
    print("\n  Final directory structure:")
    for item in sorted(messy_dir.iterdir()):
        if item.is_dir():
            print(f"    📁 {item.name}/")
        else:
            print(f"    📄 {item.name}")
    
    # Clean up
    shutil.rmtree(temp_dir)
    print("\n  Cleaned up temp directory")


if __name__ == "__main__":
    demonstrate_file_organizer()
```

---

## 📊 Section 4: Disk Usage Analyzer

A disk usage analyzer that recursively calculates directory sizes and identifies space hogs.

**SOLID Principles Applied:**
- Single Responsibility: Each analyzer function has one purpose
- Open/Closed: New analysis types can be added

**Design Patterns:**
- Iterator Pattern: Recursively iterates through directories
- Visitor Pattern: Visits each file/directory to collect data

```python
"""
DISK USAGE ANALYZER

This section builds a disk usage analyzer for finding space hogs.

SOLID Principles Applied:
- Single Responsibility: Each analyzer function has one purpose
- Open/Closed: New analysis types can be added

Design Patterns:
- Iterator Pattern: Recursively iterates through directories
- Visitor Pattern: Visits each file/directory to collect data
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict
import os


@dataclass
class FileInfo:
    """Information about a file."""
    path: Path
    size: int
    modified: datetime
    extension: str
    
    @property
    def size_mb(self) -> float:
        return self.size / (1024 * 1024)
    
    @property
    def size_gb(self) -> float:
        return self.size / (1024 * 1024 * 1024)


@dataclass
class DirectoryInfo:
    """Information about a directory."""
    path: Path
    size: int = 0
    file_count: int = 0
    dir_count: int = 0
    children: List['DirectoryInfo'] = field(default_factory=list)
    files: List[FileInfo] = field(default_factory=list)
    
    @property
    def size_mb(self) -> float:
        return self.size / (1024 * 1024)
    
    @property
    def size_gb(self) -> float:
        return self.size / (1024 * 1024 * 1024)


class DiskUsageAnalyzer:
    """
    Analyzes disk usage recursively.
    
    Design Pattern: Iterator Pattern - Recursively traverses directories
    """
    
    def __init__(self, root_path: Path):
        self.root_path = Path(root_path).resolve()
        self.root_info: Optional[DirectoryInfo] = None
    
    def analyze(self) -> DirectoryInfo:
        """Analyze disk usage starting from root."""
        self.root_info = self._analyze_directory(self.root_path)
        return self.root_info
    
    def _analyze_directory(self, path: Path) -> DirectoryInfo:
        """Recursively analyze a directory."""
        dir_info = DirectoryInfo(path=path)
        
        try:
            for item in path.iterdir():
                if item.is_file():
                    try:
                        stat = item.stat()
                        file_info = FileInfo(
                            path=item,
                            size=stat.st_size,
                            modified=datetime.fromtimestamp(stat.st_mtime),
                            extension=item.suffix.lower()
                        )
                        dir_info.files.append(file_info)
                        dir_info.size += stat.st_size
                        dir_info.file_count += 1
                    except (OSError, PermissionError):
                        pass
                
                elif item.is_dir():
                    sub_info = self._analyze_directory(item)
                    dir_info.children.append(sub_info)
                    dir_info.size += sub_info.size
                    dir_info.file_count += sub_info.file_count
                    dir_info.dir_count += 1 + sub_info.dir_count
        
        except (OSError, PermissionError):
            pass
        
        return dir_info
    
    def get_largest_files(self, n: int = 10) -> List[FileInfo]:
        """Get the n largest files."""
        all_files = []
        
        def collect_files(info: DirectoryInfo):
            all_files.extend(info.files)
            for child in info.children:
                collect_files(child)
        
        if self.root_info:
            collect_files(self.root_info)
        
        all_files.sort(key=lambda f: f.size, reverse=True)
        return all_files[:n]
    
    def get_largest_directories(self, n: int = 10) -> List[DirectoryInfo]:
        """Get the n largest directories."""
        all_dirs = []
        
        def collect_dirs(info: DirectoryInfo):
            all_dirs.append(info)
            for child in info.children:
                collect_dirs(child)
        
        if self.root_info:
            collect_dirs(self.root_info)
        
        all_dirs.sort(key=lambda d: d.size, reverse=True)
        return all_dirs[:n]
    
    def get_extension_breakdown(self) -> Dict[str, Dict]:
        """Get breakdown by file extension."""
        extension_stats: Dict[str, Dict] = defaultdict(lambda: {"count": 0, "size": 0})
        
        def collect_extensions(info: DirectoryInfo):
            for file in info.files:
                ext = file.extension if file.extension else "no_extension"
                extension_stats[ext]["count"] += 1
                extension_stats[ext]["size"] += file.size
            for child in info.children:
                collect_extensions(child)
        
        if self.root_info:
            collect_extensions(self.root_info)
        
        return dict(extension_stats)
    
    def get_age_breakdown(self) -> Dict[str, Dict]:
        """Get breakdown by file age."""
        now = datetime.now()
        age_groups = {
            "today": {"max_days": 1, "count": 0, "size": 0},
            "this_week": {"max_days": 7, "count": 0, "size": 0},
            "this_month": {"max_days": 30, "count": 0, "size": 0},
            "this_year": {"max_days": 365, "count": 0, "size": 0},
            "older": {"max_days": float('inf'), "count": 0, "size": 0}
        }
        
        def collect_ages(info: DirectoryInfo):
            for file in info.files:
                days_old = (now - file.modified).days
                
                if days_old <= 1:
                    age_groups["today"]["count"] += 1
                    age_groups["today"]["size"] += file.size
                elif days_old <= 7:
                    age_groups["this_week"]["count"] += 1
                    age_groups["this_week"]["size"] += file.size
                elif days_old <= 30:
                    age_groups["this_month"]["count"] += 1
                    age_groups["this_month"]["size"] += file.size
                elif days_old <= 365:
                    age_groups["this_year"]["count"] += 1
                    age_groups["this_year"]["size"] += file.size
                else:
                    age_groups["older"]["count"] += 1
                    age_groups["older"]["size"] += file.size
            
            for child in info.children:
                collect_ages(child)
        
        if self.root_info:
            collect_ages(self.root_info)
        
        return age_groups
    
    def get_size_breakdown(self) -> Dict[str, Dict]:
        """Get breakdown by file size."""
        size_groups = {
            "tiny_1KB": {"max_bytes": 1024, "count": 0, "size": 0},
            "small_1MB": {"max_bytes": 1024 * 1024, "count": 0, "size": 0},
            "medium_10MB": {"max_bytes": 10 * 1024 * 1024, "count": 0, "size": 0},
            "large_100MB": {"max_bytes": 100 * 1024 * 1024, "count": 0, "size": 0},
            "huge_1GB": {"max_bytes": 1024 * 1024 * 1024, "count": 0, "size": 0},
            "enormous": {"max_bytes": float('inf'), "count": 0, "size": 0}
        }
        
        def collect_sizes(info: DirectoryInfo):
            for file in info.files:
                if file.size < 1024:
                    size_groups["tiny_1KB"]["count"] += 1
                    size_groups["tiny_1KB"]["size"] += file.size
                elif file.size < 1024 * 1024:
                    size_groups["small_1MB"]["count"] += 1
                    size_groups["small_1MB"]["size"] += file.size
                elif file.size < 10 * 1024 * 1024:
                    size_groups["medium_10MB"]["count"] += 1
                    size_groups["medium_10MB"]["size"] += file.size
                elif file.size < 100 * 1024 * 1024:
                    size_groups["large_100MB"]["count"] += 1
                    size_groups["large_100MB"]["size"] += file.size
                elif file.size < 1024 * 1024 * 1024:
                    size_groups["huge_1GB"]["count"] += 1
                    size_groups["huge_1GB"]["size"] += file.size
                else:
                    size_groups["enormous"]["count"] += 1
                    size_groups["enormous"]["size"] += file.size
            
            for child in info.children:
                collect_sizes(child)
        
        if self.root_info:
            collect_sizes(self.root_info)
        
        return size_groups
    
    def generate_report(self) -> str:
        """Generate a disk usage report."""
        if not self.root_info:
            return "No analysis data. Run analyze() first."
        
        report = []
        report.append("=" * 60)
        report.append("DISK USAGE ANALYSIS REPORT")
        report.append(f"Root: {self.root_path}")
        report.append(f"Analyzed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        # Summary
        total_size_gb = self.root_info.size_gb
        total_files = self.root_info.file_count
        total_dirs = self.root_info.dir_count
        
        report.append(f"\n📊 SUMMARY:")
        report.append(f"  Total Size: {total_size_gb:.2f} GB")
        report.append(f"  Total Files: {total_files:,}")
        report.append(f"  Total Directories: {total_dirs:,}")
        
        # Largest directories
        report.append(f"\n📁 LARGEST DIRECTORIES:")
        for i, dir_info in enumerate(self.get_largest_directories(10), 1):
            percent = (dir_info.size / self.root_info.size) * 100 if self.root_info.size > 0 else 0
            report.append(f"  {i:2}. {dir_info.path.name}: {dir_info.size_mb:.1f} MB ({percent:.1f}%)")
        
        # Largest files
        report.append(f"\n📄 LARGEST FILES:")
        for i, file_info in enumerate(self.get_largest_files(10), 1):
            report.append(f"  {i:2}. {file_info.path.name}: {file_info.size_mb:.1f} MB")
        
        # Extension breakdown
        report.append(f"\n📑 EXTENSION BREAKDOWN:")
        ext_stats = self.get_extension_breakdown()
        sorted_exts = sorted(ext_stats.items(), key=lambda x: x[1]["size"], reverse=True)
        for ext, stats in sorted_exts[:10]:
            size_mb = stats["size"] / (1024 * 1024)
            report.append(f"  {ext or 'no extension'}: {stats['count']} files, {size_mb:.1f} MB")
        
        # Age breakdown
        report.append(f"\n🕒 AGE BREAKDOWN:")
        age_stats = self.get_age_breakdown()
        for age, stats in age_stats.items():
            if stats["count"] > 0:
                size_mb = stats["size"] / (1024 * 1024)
                report.append(f"  {age}: {stats['count']} files, {size_mb:.1f} MB")
        
        # Size breakdown
        report.append(f"\n📏 SIZE BREAKDOWN:")
        size_stats = self.get_size_breakdown()
        for size_group, stats in size_stats.items():
            if stats["count"] > 0:
                size_mb = stats["size"] / (1024 * 1024)
                report.append(f"  {size_group}: {stats['count']} files, {size_mb:.1f} MB")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)
    
    def print_tree(self, info: Optional[DirectoryInfo] = None, prefix: str = "", is_last: bool = True):
        """Print directory tree with sizes."""
        if info is None:
            info = self.root_info
        
        if not info:
            return
        
        connector = "└── " if is_last else "├── "
        size_str = self._format_size(info.size)
        print(f"{prefix}{connector}{info.path.name} ({size_str})")
        
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        # Print files first
        children = info.files + info.children
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            
            if isinstance(child, FileInfo):
                connector_child = "└── " if is_last_child else "├── "
                size_str = self._format_size(child.size)
                print(f"{new_prefix}{connector_child}{child.path.name} ({size_str})")
            else:
                self.print_tree(child, new_prefix, is_last_child)
    
    def _format_size(self, size: int) -> str:
        """Format size in human-readable format."""
        if size < 1024:
            return f"{size} B"
        elif size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"
        elif size < 1024 * 1024 * 1024:
            return f"{size / (1024 * 1024):.1f} MB"
        else:
            return f"{size / (1024 * 1024 * 1024):.2f} GB"


def demonstrate_disk_analyzer():
    """
    Demonstrate the disk usage analyzer.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: DISK USAGE ANALYZER")
    print("=" * 60)
    
    import tempfile
    import shutil
    
    # Create a sample directory structure
    temp_dir = tempfile.mkdtemp()
    root = Path(temp_dir) / "test_data"
    root.mkdir()
    
    print("\n1. CREATING SAMPLE DIRECTORY STRUCTURE")
    print("-" * 40)
    
    # Create files of various sizes
    def create_file(path: Path, size_kb: int):
        with open(path, 'w') as f:
            f.write("X" * (size_kb * 1024))
    
    # Documents
    docs = root / "documents"
    docs.mkdir()
    create_file(docs / "resume.pdf", 500)
    create_file(docs / "report.docx", 200)
    create_file(docs / "spreadsheet.xlsx", 300)
    
    # Images
    images = root / "images"
    images.mkdir()
    create_file(images / "photo1.jpg", 1500)
    create_file(images / "photo2.jpg", 1200)
    create_file(images / "photo3.png", 800)
    
    # Videos
    videos = root / "videos"
    videos.mkdir()
    create_file(videos / "movie1.mp4", 50000)
    create_file(videos / "movie2.mp4", 35000)
    
    # Archives
    archives = root / "archives"
    archives.mkdir()
    create_file(archives / "backup1.zip", 10000)
    create_file(archives / "backup2.zip", 8000)
    
    # Code
    code = root / "code"
    code.mkdir()
    create_file(code / "main.py", 50)
    create_file(code / "utils.py", 30)
    create_file(code / "data.json", 10)
    
    # Deeply nested
    nested = root / "a" / "b" / "c" / "d"
    nested.mkdir(parents=True)
    create_file(nested / "deep_file.txt", 100)
    
    print(f"  Created test directory: {root}")
    
    # Analyze
    print("\n2. ANALYZING DISK USAGE")
    print("-" * 40)
    
    analyzer = DiskUsageAnalyzer(root)
    analyzer.analyze()
    
    # Print tree
    print("\n  Directory tree:")
    analyzer.print_tree()
    
    # Generate report
    print("\n3. DISK USAGE REPORT")
    print("-" * 40)
    
    report = analyzer.generate_report()
    print(report)
    
    # Specific queries
    print("\n4. LARGEST FILES")
    print("-" * 40)
    
    largest_files = analyzer.get_largest_files(5)
    for i, f in enumerate(largest_files, 1):
        print(f"  {i}. {f.path.relative_to(root)}: {f.size_mb:.1f} MB")
    
    print("\n5. EXTENSION BREAKDOWN")
    print("-" * 40)
    
    ext_stats = analyzer.get_extension_breakdown()
    for ext, stats in sorted(ext_stats.items(), key=lambda x: x[1]["size"], reverse=True):
        size_mb = stats["size"] / (1024 * 1024)
        print(f"  {ext}: {stats['count']} files, {size_mb:.1f} MB")
    
    # Clean up
    shutil.rmtree(temp_dir)
    print("\n  Cleaned up temp directory")


if __name__ == "__main__":
    demonstrate_disk_analyzer()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **pathlib Basics** – Object-oriented path handling. Works across Windows, macOS, Linux. Use `/` operator for joining paths.

- **Path Operations** – `Path.cwd()`, `Path.home()`, `path.parent`, `path.name`, `path.stem`, `path.suffix`, `path.parts`.

- **File Operations** – `path.exists()`, `path.is_file()`, `path.is_dir()`, `path.stat()`, `path.glob()`, `path.rglob()`.

- **File I/O with pathlib** – `path.read_text()`, `path.write_text()`, `path.read_bytes()`, `path.write_bytes()`.

- **Directory Operations** – `path.mkdir()`, `path.rmdir()`, `path.iterdir()`, `shutil.rmtree()`.

- **Backup System** – Full, incremental, differential backups. Compression (ZIP, TAR). Manifest tracking, rotation.

- **File Organizer** – Sort by type, date, size, name. Custom rules, duplicate detection, temp file cleanup.

- **Disk Analyzer** – Recursive size calculation. Largest files/directories. Extension, age, size breakdowns.

- **SOLID Principles Applied** – Single Responsibility (each class handles one aspect), Open/Closed (new rules can be added), Dependency Inversion (depends on abstractions), Interface Segregation (clean interfaces).

- **Design Patterns Used** – Strategy Pattern (organization strategies), Command Pattern (backup operations), Chain of Responsibility (file rules), Iterator Pattern (recursive traversal), Visitor Pattern (collecting data), Value Object Pattern (immutable paths).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Context Managers – The with Statement

- **📚 Series E Catalog:** File & Data Handling Line – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Decorators – Wrapping Functions (Series F, Story 1)

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
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **34** | **18** | **65%** |

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

**Next Story:** Series F, Story 1: The 2026 Python Metromap: Decorators – Wrapping Functions

---

## 📝 Your Invitation

**Congratulations! You've completed the File & Data Handling Line!**

You've mastered:
- File I/O (reading, writing, encoding)
- CSV and JSON processing
- Exception handling and graceful failures
- Context managers for resource management
- Paths and directories with pathlib

Now build something with what you've learned:

1. **Build a log rotation system** – Automatically rotate log files when they exceed size limits.

2. **Create a file synchronization tool** – Sync directories between locations, detect changes.

3. **Build a duplicate file finder** – Find and manage duplicate files across directories.

4. **Create a media organizer** – Organize photos by date taken, videos by resolution.

5. **Build a disk cleanup tool** – Find and delete temporary files, empty directories, old logs.

**You've mastered File & Data Handling. Next stop: Advanced Python Engineering – Decorators!**

---

*Found this helpful? Clap, comment, and share what you built with paths and directories. Next stop: Decorators!* 🚇