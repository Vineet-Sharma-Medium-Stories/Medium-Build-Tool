# The 2026 Python Metromap: Memory Management & Garbage Collection

## Series F: Advanced Python Engineering | Story 4 of 6

![The 2026 Python Metromap/images/Memory Management and Garbage Collection](images/Memory Management and Garbage Collection.png)

## 📖 Introduction

**Welcome to the fourth stop on the Advanced Python Engineering Line.**

You've mastered decorators, generators, and iterators. You can write elegant, efficient code that processes data lazily and reuses logic. But as your applications grow, you'll encounter a different kind of challenge—memory usage. Programs that leak memory crash. Programs that allocate inefficiently become slow. Understanding how Python manages memory is essential for building robust, production-ready applications.

Python handles memory automatically through reference counting and garbage collection. Every object has a reference count; when it drops to zero, the memory is freed. But circular references (objects referencing each other) can cause memory leaks. Python's garbage collector detects and cleans up these cycles. Understanding these mechanisms helps you write memory-efficient code and debug memory issues.

This story—**The 2026 Python Metromap: Memory Management & Garbage Collection**—is your guide to Python memory management. We'll explore reference counting, weak references, and the garbage collector. We'll build memory profiling tools to track allocations. We'll implement an object pool to reuse objects and reduce allocations. We'll create a memory-efficient cache with weak references. We'll build a memory leak detector. And we'll optimize a recommendation engine that was consuming too much RAM.

**Let's manage memory.**

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

- 🧠 **The 2026 Python Metromap: Memory Management & Garbage Collection** – Optimizing a recommendation engine; memory profiling; leak fixing. **⬅️ YOU ARE HERE**

- ✅ **The 2026 Python Metromap: Testing & Debugging – pytest and unittest** – CI/CD pipeline; unit tests; integration tests; coverage reports. 🔜 *Up Next*

- 📝 **The 2026 Python Metromap: Type Hints & MyPy** – Large team codebase annotations; pre-runtime bug catching; automatic documentation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🧠 Section 1: Reference Counting and Garbage Collection

Python uses reference counting for memory management, with a cycle detector for circular references.

**SOLID Principle Applied: Single Responsibility** – Each object manages its own reference count.

**Design Pattern: RAII (Resource Acquisition Is Initialization)** – Objects clean up when reference count reaches zero.

```python
"""
REFERENCE COUNTING AND GARBAGE COLLECTION

This section covers Python's memory management fundamentals.

SOLID Principle: Single Responsibility
- Each object manages its own reference count

Design Pattern: RAII (Resource Acquisition Is Initialization)
- Objects clean up when reference count reaches zero
"""

import sys
import gc
import weakref
from typing import Any, Dict, List, Optional


def demonstrate_reference_counting():
    """
    Demonstrates how reference counting works.
    
    Every object tracks how many references point to it.
    When count reaches zero, memory is freed.
    """
    print("=" * 60)
    print("SECTION 1A: REFERENCE COUNTING")
    print("=" * 60)
    
    # BASIC REFERENCE COUNTING
    print("\n1. BASIC REFERENCE COUNTING")
    print("-" * 40)
    
    # Create object
    x = [1, 2, 3]
    print(f"  x = {x}")
    print(f"  Reference count: {sys.getrefcount(x) - 1}")  # Subtract 1 for getrefcount itself
    
    # Add another reference
    y = x
    print(f"  y = x")
    print(f"  Reference count: {sys.getrefcount(x) - 1}")
    
    # Add to list
    z = [x]
    print(f"  z = [x]")
    print(f"  Reference count: {sys.getrefcount(x) - 1}")
    
    # Remove references
    del y
    print(f"  del y")
    print(f"  Reference count: {sys.getrefcount(x) - 1}")
    
    del z
    print(f"  del z")
    print(f"  Reference count: {sys.getrefcount(x) - 1}")
    
    # OBJECT DESTRUCTION
    print("\n2. OBJECT DESTRUCTION (__del__)")
    print("-" * 40)
    
    class TrackedObject:
        """Object that logs its lifecycle."""
        
        def __init__(self, name: str):
            self.name = name
            print(f"  {name} created")
        
        def __del__(self):
            print(f"  {self.name} destroyed")
    
    obj = TrackedObject("temp")
    print(f"  Reference count: {sys.getrefcount(obj) - 1}")
    
    obj2 = obj
    print(f"  After second reference: {sys.getrefcount(obj) - 1}")
    
    del obj
    print(f"  After deleting first reference: {sys.getrefcount(obj2) - 1}")
    
    del obj2
    print("  After deleting last reference - object destroyed")
    
    # REFERENCE COUNT LIMITATIONS
    print("\n3. REFERENCE COUNTING LIMITATIONS (Circular References)")
    print("-" * 40)
    
    class Node:
        """Node that can reference other nodes."""
        
        def __init__(self, name: str):
            self.name = name
            self.ref = None
            print(f"  {name} created")
        
        def __del__(self):
            print(f"  {self.name} destroyed")
    
    # Create circular reference
    a = Node("A")
    b = Node("B")
    a.ref = b
    b.ref = a
    print(f"  Created circular reference: A -> B -> A")
    print(f"  Reference count of A: {sys.getrefcount(a) - 1}")
    print(f"  Reference count of B: {sys.getrefcount(b) - 1}")
    
    # Delete references
    del a
    del b
    print("  Deleted A and B references")
    print("  ⚠️ Objects still exist due to circular reference!")
    
    # Force garbage collection
    print("\n  Forcing garbage collection...")
    collected = gc.collect()
    print(f"  Garbage collector collected {collected} objects")


def demonstrate_garbage_collection():
    """
    Demonstrates Python's garbage collector for cyclic references.
    
    The garbage collector detects and cleans up circular references.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: GARBAGE COLLECTION")
    print("=" * 60)
    
    # GARBAGE COLLECTOR INTERFACE
    print("\n1. GARBAGE COLLECTOR INTERFACE")
    print("-" * 40)
    
    print(f"  GC enabled: {gc.isenabled()}")
    print(f"  GC thresholds: {gc.get_threshold()}")
    print(f"  GC debug flags: {gc.get_debug()}")
    
    # MANUAL GC CONTROL
    print("\n2. MANUAL GC CONTROL")
    print("-" * 40)
    
    # Disable GC (for performance-critical sections)
    gc.disable()
    print("  GC disabled")
    
    # Re-enable GC
    gc.enable()
    print("  GC re-enabled")
    
    # Get GC stats
    print(f"  GC stats: {gc.get_stats()}")
    
    # GARBAGE COLLECTION WITH DEBUGGING
    print("\n3. GC DEBUGGING")
    print("-" * 40)
    
    class LeakyObject:
        """Object that can create cycles."""
        
        def __init__(self, name: str):
            self.name = name
            self.circular_ref = None
        
        def __repr__(self):
            return f"LeakyObject({self.name})"
    
    # Enable GC debugging
    gc.set_debug(gc.DEBUG_LEAK)
    
    # Create cycles
    obj1 = LeakyObject("X")
    obj2 = LeakyObject("Y")
    obj1.circular_ref = obj2
    obj2.circular_ref = obj1
    
    # Delete references
    del obj1
    del obj2
    
    # Collect garbage (will print debug info)
    collected = gc.collect()
    print(f"  Collected {collected} objects")
    
    # Disable debugging
    gc.set_debug(0)
    
    # GARBAGE COLLECTOR GENERATIONS
    print("\n4. GC GENERATIONS")
    print("-" * 40)
    
    # Python uses three generations for garbage collection
    # Generation 0: newest objects
    # Generation 1: survived one collection
    # Generation 2: oldest objects
    
    print(f"  Generation 0 count: {gc.get_count()[0]}")
    print(f"  Generation 1 count: {gc.get_count()[1]}")
    print(f"  Generation 2 count: {gc.get_count()[2]}")
    
    # Force collection of specific generation
    print("\n  Forcing generation 0 collection...")
    gc.collect(0)
    
    print("\n  Forcing full collection...")
    gc.collect()
    
    # GET GARBAGE
    print("\n5. GETTING GARBAGE OBJECTS")
    print("-" * 40)
    
    # Create some garbage
    garbage = []
    for i in range(5):
        obj = LeakyObject(f"Garbage_{i}")
        garbage.append(obj)
    
    # Delete reference to list
    del garbage
    
    # Collect and see what's garbage
    gc.collect()
    garbage_objects = gc.garbage
    print(f"  Objects in gc.garbage: {len(garbage_objects)}")
    
    # REFERENCE CYCLES WITH FINALIZERS
    print("\n6. REFERENCE CYCLES WITH __del__")
    print("-" * 40)
    
    class FinalizedNode:
        """Node with finalizer that prevents GC of cycles."""
        
        def __init__(self, name: str):
            self.name = name
            self.ref = None
        
        def __del__(self):
            print(f"  {self.name} finalized")
    
    # Objects with __del__ in cycles are not collected automatically
    a = FinalizedNode("A")
    b = FinalizedNode("B")
    a.ref = b
    b.ref = a
    
    del a
    del b
    
    print("  Attempting to collect cycle with __del__...")
    collected = gc.collect()
    print(f"  Collected {collected} objects")
    print("  ⚠️ Objects with __del__ in cycles are not collected automatically!")
    
    # Clean up
    gc.collect()


def demonstrate_weak_references():
    """
    Demonstrates weak references for breaking cycles.
    
    Weak references don't increase reference count, allowing objects to be collected.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: WEAK REFERENCES")
    print("=" * 60)
    
    # WEAK REFERENCE BASICS
    print("\n1. WEAK REFERENCE BASICS")
    print("-" * 40)
    
    class Data:
        def __init__(self, value: str):
            self.value = value
        
        def __del__(self):
            print(f"  Data({self.value}) destroyed")
    
    obj = Data("important")
    weak_obj = weakref.ref(obj)
    
    print(f"  Weak reference: {weak_obj}")
    print(f"  Weak reference returns: {weak_obj()}")
    
    del obj
    print(f"  After deleting object, weak reference returns: {weak_obj()}")
    
    # WEAK VALUE DICTIONARY
    print("\n2. WEAKVALUE DICTIONARY (auto-cleaning)")
    print("-" * 40)
    
    from weakref import WeakValueDictionary
    
    cache = WeakValueDictionary()
    
    obj1 = Data("cached1")
    obj2 = Data("cached2")
    
    cache["key1"] = obj1
    cache["key2"] = obj2
    
    print(f"  Cache size: {len(cache)}")
    print(f"  Cache keys: {list(cache.keys())}")
    
    del obj1
    print(f"  After deleting obj1, cache size: {len(cache)}")
    print(f"  Cache keys: {list(cache.keys())}")
    
    # WEAK KEY DICTIONARY
    print("\n3. WEAKKEYDICTIONARY")
    print("-" * 40)
    
    from weakref import WeakKeyDictionary
    
    key_cache = WeakKeyDictionary()
    
    key1 = Data("key1")
    key2 = Data("key2")
    
    key_cache[key1] = "value1"
    key_cache[key2] = "value2"
    
    print(f"  Cache size: {len(key_cache)}")
    
    del key1
    print(f"  After deleting key1, cache size: {len(key_cache)}")
    
    # WEAK SET
    print("\n4. WEAKSET")
    print("-" * 40)
    
    from weakref import WeakSet
    
    weak_set = WeakSet()
    
    item1 = Data("set_item1")
    item2 = Data("set_item2")
    
    weak_set.add(item1)
    weak_set.add(item2)
    
    print(f"  WeakSet size: {len(weak_set)}")
    
    del item1
    print(f"  After deleting item1, size: {len(weak_set)}")
    
    # PRACTICAL: CACHE WITH WEAK REFERENCES
    print("\n5. PRACTICAL: WEAK REFERENCE CACHE")
    print("-" * 40)
    
    class ExpensiveObject:
        """Object that's expensive to create."""
        
        _instances = WeakValueDictionary()
        
        def __new__(cls, key: str):
            # Return cached instance if exists
            if key in cls._instances:
                print(f"  Returning cached instance for {key}")
                return cls._instances[key]
            
            print(f"  Creating new instance for {key}")
            instance = super().__new__(cls)
            cls._instances[key] = instance
            return instance
        
        def __init__(self, key: str):
            self.key = key
            self.data = f"Expensive data for {key}"
        
        def __del__(self):
            print(f"  ExpensiveObject({self.key}) destroyed")
    
    # Create instances
    obj_a = ExpensiveObject("A")
    obj_b = ExpensiveObject("B")
    obj_c = ExpensiveObject("A")  # Returns cached instance
    
    print(f"  obj_a is obj_c: {obj_a is obj_c}")
    
    del obj_a
    del obj_c
    print("  Deleted references to A")
    
    # Create again - will create new instance
    obj_d = ExpensiveObject("A")
    print(f"  obj_d created: {obj_d.key}")
    
    # BREAKING CYCLES WITH WEAK REFERENCES
    print("\n6. BREAKING CYCLES WITH WEAKREF")
    print("-" * 40)
    
    class TreeNode:
        """Tree node using weakref for parent reference."""
        
        def __init__(self, name: str):
            self.name = name
            self.children = []
            self._parent = None
        
        @property
        def parent(self):
            return self._parent() if self._parent else None
        
        @parent.setter
        def parent(self, node):
            self._parent = weakref.ref(node) if node else None
        
        def add_child(self, child):
            child.parent = self
            self.children.append(child)
        
        def __del__(self):
            print(f"  TreeNode({self.name}) destroyed")
    
    root = TreeNode("root")
    child = TreeNode("child")
    root.add_child(child)
    
    print("  Created root -> child relationship (weakref for parent)")
    print("  Deleting root...")
    del root
    print("  After deleting root, child should also be collected")
    
    # Force GC
    gc.collect()


if __name__ == "__main__":
    demonstrate_reference_counting()
    demonstrate_garbage_collection()
    demonstrate_weak_references()
```

---

## 📊 Section 2: Memory Profiling Tools

Tools and techniques for profiling memory usage and finding leaks.

**SOLID Principles Applied:**
- Single Responsibility: Each profiler measures one aspect of memory
- Open/Closed: New profiling strategies can be added

**Design Patterns:**
- Decorator Pattern: Wrap functions with memory profiling
- Observer Pattern: Monitor memory usage over time

```python
"""
MEMORY PROFILING TOOLS

This section builds memory profiling tools for tracking allocations.

SOLID Principles Applied:
- Single Responsibility: Each profiler measures one aspect
- Open/Closed: New profiling strategies can be added

Design Patterns:
- Decorator Pattern: Wrap functions with memory profiling
- Observer Pattern: Monitor memory usage over time
"""

import tracemalloc
import time
import functools
from typing import Dict, List, Any, Callable, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import linecache
import os


@dataclass
class MemorySnapshot:
    """Memory snapshot at a point in time."""
    timestamp: float
    current_mb: float
    peak_mb: float
    diff_mb: float = 0.0


class MemoryProfiler:
    """
    Profiles memory usage of code blocks.
    
    Design Pattern: Decorator Pattern - Wraps code with profiling
    """
    
    def __init__(self):
        self.snapshots: List[MemorySnapshot] = []
        self.tracemalloc_started = False
    
    def start(self) -> None:
        """Start memory tracking."""
        tracemalloc.start()
        self.tracemalloc_started = True
        self._take_snapshot("start")
    
    def stop(self) -> Dict:
        """Stop memory tracking and return statistics."""
        if self.tracemalloc_started:
            self._take_snapshot("stop")
            tracemalloc.stop()
            self.tracemalloc_started = False
        
        return self.get_statistics()
    
    def _take_snapshot(self, label: str = "") -> None:
        """Take a memory snapshot."""
        current, peak = tracemalloc.get_traced_memory()
        current_mb = current / (1024 * 1024)
        peak_mb = peak / (1024 * 1024)
        
        diff = 0.0
        if self.snapshots:
            diff = current_mb - self.snapshots[-1].current_mb
        
        self.snapshots.append(MemorySnapshot(
            timestamp=time.time(),
            current_mb=current_mb,
            peak_mb=peak_mb,
            diff_mb=diff
        ))
    
    def get_statistics(self) -> Dict:
        """Get memory statistics."""
        if not self.snapshots:
            return {}
        
        start = self.snapshots[0]
        end = self.snapshots[-1]
        
        return {
            "start_mb": round(start.current_mb, 2),
            "end_mb": round(end.current_mb, 2),
            "peak_mb": round(max(s.peak_mb for s in self.snapshots), 2),
            "delta_mb": round(end.current_mb - start.current_mb, 2),
            "snapshots": len(self.snapshots)
        }
    
    def get_top_allocations(self, limit: int = 10) -> List[Dict]:
        """Get top memory allocations by line."""
        if not self.tracemalloc_started:
            return []
        
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        
        result = []
        for stat in top_stats[:limit]:
            frame = stat.traceback[0]
            filename = os.path.basename(frame.filename)
            result.append({
                "file": filename,
                "line": frame.lineno,
                "size_mb": stat.size / (1024 * 1024),
                "count": stat.count,
                "code": linecache.getline(frame.filename, frame.lineno).strip()
            })
        
        return result
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


def memory_profile(func: Callable = None, *, detailed: bool = False):
    """
    Decorator that profiles memory usage of a function.
    
    Usage:
        @memory_profile
        def my_function():
            pass
        
        @memory_profile(detailed=True)
        def detailed_function():
            pass
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            profiler = MemoryProfiler()
            profiler.start()
            
            try:
                result = f(*args, **kwargs)
                return result
            finally:
                stats = profiler.stop()
                print(f"\n  📊 Memory profile for {f.__name__}:")
                print(f"    Start: {stats['start_mb']:.2f} MB")
                print(f"    End: {stats['end_mb']:.2f} MB")
                print(f"    Peak: {stats['peak_mb']:.2f} MB")
                print(f"    Delta: {stats['delta_mb']:.2f} MB")
                
                if detailed:
                    print(f"\n  Top allocations:")
                    top = profiler.get_top_allocations(5)
                    for alloc in top:
                        print(f"    {alloc['file']}:{alloc['line']} - {alloc['size_mb']:.2f} MB ({alloc['count']} allocations)")
                        if alloc['code']:
                            print(f"      {alloc['code']}")
        
        return wrapper
    
    if func is None:
        return decorator
    return decorator(func)


class MemoryTracker:
    """
    Tracks memory usage over time.
    
    Design Pattern: Observer Pattern - Monitors memory at intervals
    """
    
    def __init__(self, interval_seconds: float = 1.0):
        self.interval = interval_seconds
        self.running = False
        self.readings: List[Dict] = []
        self._start_time = None
    
    def start(self) -> None:
        """Start tracking memory."""
        self.running = True
        self._start_time = time.time()
        self._track()
    
    def _track(self) -> None:
        """Track memory at intervals."""
        import threading
        
        def track_loop():
            while self.running:
                import psutil
                process = psutil.Process()
                memory_info = process.memory_info()
                
                self.readings.append({
                    "timestamp": time.time() - self._start_time,
                    "rss_mb": memory_info.rss / (1024 * 1024),
                    "vms_mb": memory_info.vms / (1024 * 1024),
                    "percent": process.memory_percent()
                })
                
                time.sleep(self.interval)
        
        thread = threading.Thread(target=track_loop, daemon=True)
        thread.start()
    
    def stop(self) -> Dict:
        """Stop tracking and return statistics."""
        self.running = False
        
        if not self.readings:
            return {}
        
        rss_values = [r["rss_mb"] for r in self.readings]
        
        return {
            "duration_seconds": self.readings[-1]["timestamp"],
            "samples": len(self.readings),
            "min_rss_mb": min(rss_values),
            "max_rss_mb": max(rss_values),
            "avg_rss_mb": sum(rss_values) / len(rss_values),
            "final_rss_mb": rss_values[-1],
            "readings": self.readings
        }
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


class LeakDetector:
    """
    Detects memory leaks by comparing snapshots.
    
    Design Pattern: Observer Pattern - Compares memory states
    """
    
    def __init__(self):
        self.snapshots = []
    
    def take_snapshot(self, label: str = "") -> None:
        """Take a memory snapshot."""
        snapshot = tracemalloc.take_snapshot()
        self.snapshots.append({
            "label": label,
            "snapshot": snapshot,
            "timestamp": time.time()
        })
    
    def compare(self, snapshot1_idx: int = 0, snapshot2_idx: int = -1) -> Dict:
        """Compare two snapshots for leaks."""
        if len(self.snapshots) < 2:
            return {"error": "Need at least two snapshots"}
        
        snap1 = self.snapshots[snapshot1_idx]["snapshot"]
        snap2 = self.snapshots[snapshot2_idx]["snapshot"]
        
        # Compare snapshots
        diff = snap2.compare_to(snap1, 'lineno')
        
        # Filter for allocations that grew
        growing = [stat for stat in diff if stat.size_diff > 0]
        
        return {
            "total_leaked_mb": sum(stat.size_diff for stat in growing) / (1024 * 1024),
            "total_traces": len(growing),
            "top_leaks": [
                {
                    "size_mb": stat.size_diff / (1024 * 1024),
                    "count": stat.count_diff,
                    "file": os.path.basename(stat.traceback[0].filename),
                    "line": stat.traceback[0].lineno
                }
                for stat in growing[:10]
            ]
        }


def demonstrate_memory_profiling():
    """
    Demonstrate memory profiling tools.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: MEMORY PROFILING TOOLS")
    print("=" * 60)
    
    # BASIC PROFILER
    print("\n1. BASIC MEMORY PROFILER")
    print("-" * 40)
    
    profiler = MemoryProfiler()
    profiler.start()
    
    # Allocate some memory
    data = [i for i in range(1000000)]
    time.sleep(0.1)
    
    stats = profiler.stop()
    print(f"  Memory usage:")
    print(f"    Start: {stats['start_mb']:.2f} MB")
    print(f"    End: {stats['end_mb']:.2f} MB")
    print(f"    Peak: {stats['peak_mb']:.2f} MB")
    print(f"    Delta: {stats['delta_mb']:.2f} MB")
    
    # DECORATOR PROFILING
    print("\n2. DECORATOR MEMORY PROFILING")
    print("-" * 40)
    
    @memory_profile
    def create_large_list(size: int) -> List:
        """Create a large list."""
        return [i for i in range(size)]
    
    @memory_profile(detailed=True)
    def create_with_leak(size: int) -> List:
        """Create list and simulate leak."""
        leak = []
        for i in range(size):
            leak.append(i)
            if i % 100000 == 0:
                time.sleep(0.01)
        return leak
    
    result = create_large_list(500000)
    result2 = create_with_leak(300000)
    
    # CONTEXT MANAGER PROFILING
    print("\n3. CONTEXT MANAGER PROFILING")
    print("-" * 40)
    
    with MemoryProfiler() as profiler:
        large_data = [i ** 2 for i in range(200000)]
        time.sleep(0.05)
    
    stats = profiler.get_statistics()
    print(f"  Context manager stats:")
    print(f"    Peak: {stats['peak_mb']:.2f} MB")
    print(f"    Delta: {stats['delta_mb']:.2f} MB")
    
    # TOP ALLOCATIONS
    print("\n4. TOP MEMORY ALLOCATIONS")
    print("-" * 40)
    
    tracemalloc.start()
    
    # Create various objects
    list1 = [i for i in range(100000)]
    dict1 = {i: i**2 for i in range(50000)}
    list2 = [str(i) for i in range(80000)]
    
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("  Top 5 allocations by line:")
    for stat in top_stats[:5]:
        frame = stat.traceback[0]
        filename = os.path.basename(frame.filename)
        print(f"    {filename}:{frame.lineno} - {stat.size / (1024*1024):.2f} MB ({stat.count} allocations)")
    
    tracemalloc.stop()
    
    # LEAK DETECTION
    print("\n5. LEAK DETECTION")
    print("-" * 40)
    
    tracemalloc.start()
    detector = LeakDetector()
    
    detector.take_snapshot("before")
    
    # Simulate memory leak
    leaked_data = []
    for i in range(1000):
        leaked_data.append([j for j in range(100)])
        if i % 200 == 0:
            time.sleep(0.01)
    
    detector.take_snapshot("after")
    
    leak_report = detector.compare(0, 1)
    print(f"  Potential memory leak detected:")
    print(f"    Total leaked: {leak_report['total_leaked_mb']:.2f} MB")
    print(f"    Leak traces: {leak_report['total_traces']}")
    
    if leak_report['top_leaks']:
        print("    Top leaks:")
        for leak in leak_report['top_leaks'][:3]:
            print(f"      {leak['file']}:{leak['line']} - {leak['size_mb']:.2f} MB")
    
    tracemalloc.stop()
    
    # MEMORY TRACKER
    print("\n6. MEMORY TRACKER OVER TIME")
    print("-" * 40)
    
    print("  Tracking memory for 2 seconds...")
    with MemoryTracker(interval_seconds=0.5) as tracker:
        # Simulate memory growth
        data = []
        for i in range(5):
            data.extend([j for j in range(100000)])
            time.sleep(0.3)
    
    stats = tracker.stop()
    print(f"  Tracking results:")
    print(f"    Duration: {stats['duration_seconds']:.1f}s")
    print(f"    Samples: {stats['samples']}")
    print(f"    Min RSS: {stats['min_rss_mb']:.1f} MB")
    print(f"    Max RSS: {stats['max_rss_mb']:.1f} MB")
    print(f"    Final RSS: {stats['final_rss_mb']:.1f} MB")


if __name__ == "__main__":
    demonstrate_memory_profiling()
```

---

## 🗄️ Section 3: Object Pool for Reuse

An object pool that reuses objects to reduce memory allocations and garbage collection.

**SOLID Principles Applied:**
- Single Responsibility: Pool manages object lifecycle
- Open/Closed: New poolable types can be added

**Design Patterns:**
- Pool Pattern: Reuses expensive objects
- Factory Pattern: Creates objects when pool is empty

```python
"""
OBJECT POOL FOR REUSE

This section builds an object pool to reduce memory allocations.

SOLID Principles Applied:
- Single Responsibility: Pool manages object lifecycle
- Open/Closed: New poolable types can be added

Design Patterns:
- Pool Pattern: Reuses expensive objects
- Factory Pattern: Creates objects when pool is empty
"""

from typing import TypeVar, Generic, List, Callable, Optional, Any
from dataclasses import dataclass, field
import time
import weakref
from collections import deque


T = TypeVar('T')


class ObjectPool(Generic[T]):
    """
    Generic object pool for reusing objects.
    
    Design Pattern: Pool Pattern - Reuses expensive objects
    """
    
    def __init__(self, creator: Callable[[], T], resetter: Optional[Callable[[T], None]] = None,
                 max_size: int = 100, initial_size: int = 0):
        """
        Initialize object pool.
        
        Args:
            creator: Function that creates new objects
            resetter: Function that resets object to initial state
            max_size: Maximum pool size
            initial_size: Initial number of objects to create
        """
        self.creator = creator
        self.resetter = resetter or (lambda x: None)
        self.max_size = max_size
        self._pool: deque = deque()
        self._active_count = 0
        self._total_created = 0
        self._total_acquired = 0
        self._total_released = 0
        
        # Pre-create initial objects
        for _ in range(initial_size):
            self._pool.append(self._create())
    
    def _create(self) -> T:
        """Create a new object."""
        self._total_created += 1
        return self.creator()
    
    def acquire(self) -> T:
        """Acquire an object from the pool."""
        self._total_acquired += 1
        self._active_count += 1
        
        if self._pool:
            obj = self._pool.popleft()
            return obj
        
        # Pool empty, create new
        return self._create()
    
    def release(self, obj: T) -> None:
        """Release an object back to the pool."""
        self._active_count -= 1
        self._total_released += 1
        
        # Reset object state
        self.resetter(obj)
        
        # Return to pool if space available
        if len(self._pool) < self.max_size:
            self._pool.append(obj)
        # Otherwise, let object be garbage collected
    
    def __enter__(self):
        return self.acquire()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cannot release in __exit__ without the object
        pass
    
    def get_stats(self) -> dict:
        """Get pool statistics."""
        return {
            "pool_size": len(self._pool),
            "active_count": self._active_count,
            "total_created": self._total_created,
            "total_acquired": self._total_acquired,
            "total_released": self._total_released,
            "reuse_rate": (self._total_acquired - self._total_created) / max(self._total_acquired, 1) * 100
        }


class PooledObject:
    """Base class for poolable objects."""
    
    def reset(self) -> None:
        """Reset object to initial state."""
        pass


class DatabaseConnection:
    """
    Simulated database connection with pooling.
    
    Design Pattern: Pool Pattern - Connection reuse
    """
    
    def __init__(self, conn_id: int):
        self.conn_id = conn_id
        self.in_use = False
        self.query_count = 0
    
    def execute(self, query: str) -> str:
        """Execute a query."""
        if not self.in_use:
            raise RuntimeError("Connection not acquired")
        
        self.query_count += 1
        time.sleep(0.01)  # Simulate query
        return f"Result from {self.conn_id}: {query[:20]}..."
    
    def reset(self) -> None:
        """Reset connection state."""
        self.in_use = False
        # Keep query count for stats
        # But reset other state
    
    def __repr__(self):
        return f"DBConn({self.conn_id}, queries={self.query_count})"


class ConnectionPool:
    """
    Connection pool for database connections.
    
    Design Pattern: Pool Pattern - Connection reuse
    """
    
    def __init__(self, min_connections: int = 2, max_connections: int = 10):
        self.min_connections = min_connections
        self.max_connections = max_connections
        self._pool: deque = deque()
        self._active: dict = {}
        self._next_id = 1
        
        # Create initial connections
        for _ in range(min_connections):
            self._create_connection()
    
    def _create_connection(self) -> DatabaseConnection:
        """Create a new connection."""
        conn = DatabaseConnection(self._next_id)
        self._next_id += 1
        self._pool.append(conn)
        return conn
    
    def acquire(self) -> DatabaseConnection:
        """Acquire a connection."""
        if not self._pool:
            if len(self._active) < self.max_connections:
                self._create_connection()
            else:
                raise RuntimeError("No available connections")
        
        conn = self._pool.popleft()
        conn.in_use = True
        self._active[id(conn)] = conn
        return conn
    
    def release(self, conn: DatabaseConnection) -> None:
        """Release a connection."""
        conn.reset()
        conn.in_use = False
        del self._active[id(conn)]
        
        # Keep pool at min size
        if len(self._pool) < self.min_connections:
            self._pool.append(conn)
        # Otherwise, let connection be garbage collected
    
    def __enter__(self):
        return self.acquire()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Would need to pass connection to release
        pass
    
    def get_stats(self) -> dict:
        """Get pool statistics."""
        return {
            "pool_size": len(self._pool),
            "active_connections": len(self._active),
            "total_connections": self._next_id - 1,
            "min_connections": self.min_connections,
            "max_connections": self.max_connections
        }


class ConnectionContext:
    """Context manager for connection acquisition."""
    
    def __init__(self, pool: ConnectionPool):
        self.pool = pool
        self.connection = None
    
    def __enter__(self):
        self.connection = self.pool.acquire()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.pool.release(self.connection)


class ObjectPoolManager:
    """
    Manages multiple object pools.
    
    Design Pattern: Factory Pattern - Creates and manages pools
    """
    
    def __init__(self):
        self.pools: dict = {}
    
    def get_pool(self, name: str, creator: Callable, resetter: Callable = None,
                 max_size: int = 100) -> ObjectPool:
        """Get or create an object pool."""
        if name not in self.pools:
            self.pools[name] = ObjectPool(creator, resetter, max_size)
        return self.pools[name]
    
    def get_stats(self) -> dict:
        """Get statistics for all pools."""
        return {name: pool.get_stats() for name, pool in self.pools.items()}


class MemoryEfficientList:
    """
    Memory-efficient list that uses object pooling for elements.
    
    Design Pattern: Pool Pattern - Reuses element objects
    """
    
    def __init__(self, element_pool: ObjectPool):
        self.element_pool = element_pool
        self._elements = []
    
    def append(self, value: Any) -> None:
        """Append a value using pooled element."""
        element = self.element_pool.acquire()
        element.value = value
        self._elements.append(element)
    
    def __iter__(self):
        return (elem.value for elem in self._elements)
    
    def __len__(self):
        return len(self._elements)
    
    def clear(self) -> None:
        """Clear the list and release elements back to pool."""
        for elem in self._elements:
            self.element_pool.release(elem)
        self._elements.clear()


class PooledElement:
    """Element that can be pooled."""
    
    def __init__(self):
        self.value = None
        self.in_use = False
    
    def reset(self):
        self.value = None
        self.in_use = False


def demonstrate_object_pool():
    """
    Demonstrate object pool implementation.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: OBJECT POOL FOR REUSE")
    print("=" * 60)
    
    # BASIC OBJECT POOL
    print("\n1. BASIC OBJECT POOL")
    print("-" * 40)
    
    def create_list():
        return []
    
    def reset_list(lst):
        lst.clear()
    
    pool = ObjectPool(create_list, reset_list, max_size=5, initial_size=3)
    
    print(f"  Initial pool stats: {pool.get_stats()}")
    
    # Acquire objects
    list1 = pool.acquire()
    list2 = pool.acquire()
    list3 = pool.acquire()
    list4 = pool.acquire()  # Creates new since pool empty
    
    list1.append(1)
    list2.append(2)
    list3.append(3)
    
    print(f"  After acquiring 4 objects: {pool.get_stats()}")
    
    # Release objects
    pool.release(list1)
    pool.release(list2)
    
    print(f"  After releasing 2 objects: {pool.get_stats()}")
    
    # Acquire again (reuses released objects)
    list5 = pool.acquire()
    list6 = pool.acquire()
    
    print(f"  After re-acquiring: {pool.get_stats()}")
    print(f"  List5 contents (should be empty after reset): {list5}")
    
    # DATABASE CONNECTION POOL
    print("\n2. DATABASE CONNECTION POOL")
    print("-" * 40)
    
    conn_pool = ConnectionPool(min_connections=2, max_connections=5)
    print(f"  Initial pool: {conn_pool.get_stats()}")
    
    # Simulate concurrent connections
    connections = []
    for i in range(4):
        conn = conn_pool.acquire()
        connections.append(conn)
        print(f"  Acquired connection {conn.conn_id}")
    
    print(f"  After acquiring 4: {conn_pool.get_stats()}")
    
    # Release some
    for conn in connections[:2]:
        conn_pool.release(conn)
        print(f"  Released connection {conn.conn_id}")
    
    print(f"  After releasing 2: {conn_pool.get_stats()}")
    
    # Use context manager
    print("\n  Using context manager:")
    with ConnectionContext(conn_pool) as conn:
        result = conn.execute("SELECT * FROM users")
        print(f"    {result}")
    
    # PERFORMANCE COMPARISON
    print("\n3. PERFORMANCE: WITH POOL VS WITHOUT POOL")
    print("-" * 40)
    
    import time
    
    # Without pool
    start = time.time()
    for _ in range(100):
        conn = DatabaseConnection(0)
        conn.execute("SELECT")
        # Connection discarded (garbage collected)
    without_pool = time.time() - start
    
    # With pool
    pool = ConnectionPool(min_connections=5, max_connections=5)
    start = time.time()
    for _ in range(100):
        with ConnectionContext(pool) as conn:
            conn.execute("SELECT")
    with_pool = time.time() - start
    
    print(f"  Without pool: {without_pool:.3f}s")
    print(f"  With pool: {with_pool:.3f}s")
    print(f"  Speedup: {without_pool / with_pool:.1f}x")
    
    # POOL MANAGER
    print("\n4. OBJECT POOL MANAGER")
    print("-" * 40)
    
    manager = ObjectPoolManager()
    
    # Register pools
    list_pool = manager.get_pool("lists", create_list, reset_list, max_size=10)
    dict_pool = manager.get_pool("dicts", dict, lambda d: d.clear(), max_size=10)
    
    # Use pools
    lst = list_pool.acquire()
    lst.append(1)
    lst.append(2)
    print(f"  List from pool: {lst}")
    list_pool.release(lst)
    
    dct = dict_pool.acquire()
    dct["key"] = "value"
    print(f"  Dict from pool: {dct}")
    dict_pool.release(dct)
    
    print(f"  Manager stats: {manager.get_stats()}")
    
    # MEMORY EFFICIENT LIST
    print("\n5. MEMORY-EFFICIENT LIST WITH POOLING")
    print("-" * 40)
    
    element_pool = ObjectPool(PooledElement, lambda e: e.reset(), max_size=50)
    efficient_list = MemoryEfficientList(element_pool)
    
    for i in range(20):
        efficient_list.append(i)
    
    print(f"  List length: {len(efficient_list)}")
    print(f"  Element pool stats: {element_pool.get_stats()}")
    
    efficient_list.clear()
    print(f"  After clear, element pool: {element_pool.get_stats()}")
    print("  Elements returned to pool for reuse!")


if __name__ == "__main__":
    demonstrate_object_pool()
```

---

## 🔄 Section 4: Memory-Efficient Cache with Weak References

A cache that uses weak references to prevent memory leaks while still providing caching benefits.

**SOLID Principles Applied:**
- Single Responsibility: Cache manages storage, weak references prevent leaks
- Open/Closed: New eviction policies can be added

**Design Patterns:**
- Proxy Pattern: Cache proxies access to values
- Observer Pattern: Notifies when values are evicted

```python
"""
MEMORY-EFFICIENT CACHE WITH WEAK REFERENCES

This section builds a cache using weak references to prevent leaks.

SOLID Principles Applied:
- Single Responsibility: Cache manages storage
- Open/Closed: New eviction policies can be added

Design Patterns:
- Proxy Pattern: Cache proxies access to values
- Observer Pattern: Notifies when values are evicted
"""

import weakref
import time
from typing import Dict, Any, Optional, Callable, List
from collections import OrderedDict
from dataclasses import dataclass, field
import threading


@dataclass
class CacheEntry:
    """Cache entry with metadata."""
    key: Any
    value: Any
    size: int = 1
    access_count: int = 0
    created_at: float = field(default_factory=time.time)
    last_access: float = field(default_factory=time.time)


class WeakValueCache:
    """
    Cache that holds weak references to values.
    
    Values are garbage collected when no other references exist.
    
    Design Pattern: Proxy Pattern - Caches values weakly
    """
    
    def __init__(self):
        self._cache: Dict[Any, weakref.ref] = {}
        self._stats = {"hits": 0, "misses": 0, "evictions": 0}
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache."""
        if key in self._cache:
            value = self._cache[key]()
            if value is not None:
                self._stats["hits"] += 1
                return value
            else:
                # Value was garbage collected
                del self._cache[key]
                self._stats["evictions"] += 1
        
        self._stats["misses"] += 1
        return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put value into cache."""
        self._cache[key] = weakref.ref(value)
    
    def remove(self, key: Any) -> None:
        """Remove key from cache."""
        if key in self._cache:
            del self._cache[key]
    
    def clear(self) -> None:
        """Clear the cache."""
        self._cache.clear()
    
    def get_stats(self) -> dict:
        """Get cache statistics."""
        total = self._stats["hits"] + self._stats["misses"]
        return {
            "size": len(self._cache),
            "hits": self._stats["hits"],
            "misses": self._stats["misses"],
            "hit_rate": (self._stats["hits"] / total * 100) if total > 0 else 0,
            "evictions": self._stats["evictions"]
        }
    
    def __contains__(self, key: Any) -> bool:
        return key in self._cache


class LRUCache:
    """
    LRU cache with size limit and eviction.
    
    Design Pattern: Proxy Pattern - Caches values with eviction
    """
    
    def __init__(self, max_size: int = 100, max_memory_mb: float = None):
        self.max_size = max_size
        self.max_memory_mb = max_memory_mb
        self._cache: OrderedDict = OrderedDict()
        self._stats = {"hits": 0, "misses": 0, "evictions": 0}
        self._current_memory_mb = 0.0
        self._lock = threading.Lock()
    
    def _estimate_size(self, value: Any) -> int:
        """Estimate memory size of value."""
        import sys
        return sys.getsizeof(value)
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache."""
        with self._lock:
            if key in self._cache:
                # Move to end (most recently used)
                value = self._cache.pop(key)
                self._cache[key] = value
                self._stats["hits"] += 1
                return value
        
        self._stats["misses"] += 1
        return None
    
    def put(self, key: Any, value: Any) -> bool:
        """Put value into cache."""
        size = self._estimate_size(value)
        size_mb = size / (1024 * 1024)
        
        with self._lock:
            # Remove if already exists
            if key in self._cache:
                old_size = self._estimate_size(self._cache[key])
                self._current_memory_mb -= old_size / (1024 * 1024)
                del self._cache[key]
            
            # Evict while over capacity
            while (len(self._cache) >= self.max_size or 
                   (self.max_memory_mb and self._current_memory_mb + size_mb > self.max_memory_mb)):
                if not self._cache:
                    break
                # Remove least recently used
                evicted_key, evicted_value = self._cache.popitem(last=False)
                evicted_size = self._estimate_size(evicted_value)
                self._current_memory_mb -= evicted_size / (1024 * 1024)
                self._stats["evictions"] += 1
            
            # Add new value
            self._cache[key] = value
            self._current_memory_mb += size_mb
        
        return True
    
    def remove(self, key: Any) -> None:
        """Remove key from cache."""
        with self._lock:
            if key in self._cache:
                size = self._estimate_size(self._cache[key])
                self._current_memory_mb -= size / (1024 * 1024)
                del self._cache[key]
    
    def clear(self) -> None:
        """Clear the cache."""
        with self._lock:
            self._cache.clear()
            self._current_memory_mb = 0.0
    
    def get_stats(self) -> dict:
        """Get cache statistics."""
        total = self._stats["hits"] + self._stats["misses"]
        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "memory_mb": round(self._current_memory_mb, 2),
            "max_memory_mb": self.max_memory_mb,
            "hits": self._stats["hits"],
            "misses": self._stats["misses"],
            "hit_rate": (self._stats["hits"] / total * 100) if total > 0 else 0,
            "evictions": self._stats["evictions"]
        }


class TTLCache:
    """
    Time-To-Live cache with expiration.
    
    Design Pattern: Proxy Pattern - Caches values with expiration
    """
    
    def __init__(self, ttl_seconds: int = 300, max_size: int = 1000):
        self.ttl = ttl_seconds
        self.max_size = max_size
        self._cache: Dict[Any, CacheEntry] = {}
        self._stats = {"hits": 0, "misses": 0, "expired": 0}
    
    def _is_expired(self, entry: CacheEntry) -> bool:
        """Check if entry has expired."""
        return time.time() - entry.last_access > self.ttl
    
    def _clean_expired(self) -> None:
        """Remove expired entries."""
        expired_keys = [k for k, v in self._cache.items() if self._is_expired(v)]
        for key in expired_keys:
            del self._cache[key]
            self._stats["expired"] += 1
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache."""
        self._clean_expired()
        
        if key in self._cache:
            entry = self._cache[key]
            if not self._is_expired(entry):
                entry.access_count += 1
                entry.last_access = time.time()
                self._stats["hits"] += 1
                return entry.value
            else:
                del self._cache[key]
                self._stats["expired"] += 1
        
        self._stats["misses"] += 1
        return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put value into cache."""
        self._clean_expired()
        
        # Evict if at capacity
        if len(self._cache) >= self.max_size:
            # Remove least accessed
            min_key = min(self._cache.keys(), key=lambda k: self._cache[k].access_count)
            del self._cache[min_key]
        
        self._cache[key] = CacheEntry(key=key, value=value)
    
    def remove(self, key: Any) -> None:
        """Remove key from cache."""
        if key in self._cache:
            del self._cache[key]
    
    def clear(self) -> None:
        """Clear the cache."""
        self._cache.clear()
    
    def get_stats(self) -> dict:
        """Get cache statistics."""
        total = self._stats["hits"] + self._stats["misses"]
        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "ttl_seconds": self.ttl,
            "hits": self._stats["hits"],
            "misses": self._stats["misses"],
            "hit_rate": (self._stats["hits"] / total * 100) if total > 0 else 0,
            "expired": self._stats["expired"]
        }


class CacheFactory:
    """
    Factory for creating different cache types.
    
    Design Pattern: Factory Pattern - Creates cache instances
    """
    
    @staticmethod
    def weak_value() -> WeakValueCache:
        """Create weak value cache."""
        return WeakValueCache()
    
    @staticmethod
    def lru(max_size: int = 100, max_memory_mb: float = None) -> LRUCache:
        """Create LRU cache."""
        return LRUCache(max_size, max_memory_mb)
    
    @staticmethod
    def ttl(ttl_seconds: int = 300, max_size: int = 1000) -> TTLCache:
        """Create TTL cache."""
        return TTLCache(ttl_seconds, max_size)


def demonstrate_memory_efficient_cache():
    """
    Demonstrate memory-efficient caches.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: MEMORY-EFFICIENT CACHE")
    print("=" * 60)
    
    # WEAK VALUE CACHE
    print("\n1. WEAK VALUE CACHE (Auto cleanup)")
    print("-" * 40)
    
    cache = CacheFactory.weak_value()
    
    class Data:
        def __init__(self, value):
            self.value = value
        
        def __del__(self):
            print(f"    Data({self.value}) garbage collected")
    
    # Add data to cache
    data1 = Data("important")
    data2 = Data("also_important")
    
    cache.put("key1", data1)
    cache.put("key2", data2)
    
    print(f"  Cache size: {cache.get_stats()['size']}")
    print(f"  Get key1: {cache.get('key1') is not None}")
    
    # Delete reference to data1
    del data1
    print("  Deleted reference to data1")
    
    # Force garbage collection
    import gc
    gc.collect()
    
    print(f"  Cache size after GC: {cache.get_stats()['size']}")
    print(f"  Get key1: {cache.get('key1') is not None}")
    
    # LRU CACHE
    print("\n2. LRU CACHE (Size limited)")
    print("-" * 40)
    
    lru = CacheFactory.lru(max_size=3)
    
    for i in range(5):
        lru.put(f"key{i}", f"value{i}")
        print(f"  Added key{i}, cache size: {lru.get_stats()['size']}")
    
    print(f"  Cache keys: {list(lru._cache.keys())}")
    print(f"  Get key0: {lru.get('key0')} (should be None - evicted)")
    print(f"  Get key4: {lru.get('key4')}")
    
    # LRU with memory limit
    print("\n3. LRU CACHE WITH MEMORY LIMIT")
    print("-" * 40)
    
    mem_lru = CacheFactory.lru(max_size=10, max_memory_mb=1.0)
    
    # Add large objects
    for i in range(5):
        large_data = list(range(100000))  # ~800KB each
        mem_lru.put(f"large_{i}", large_data)
        stats = mem_lru.get_stats()
        print(f"  Added large_{i}, memory: {stats['memory_mb']:.2f} MB, size: {stats['size']}")
    
    # TTL CACHE
    print("\n4. TTL CACHE (Time-based expiration)")
    print("-" * 40)
    
    ttl_cache = CacheFactory.ttl(ttl_seconds=2, max_size=10)
    
    ttl_cache.put("temp", "temporary value")
    print(f"  Added value with 2 second TTL")
    print(f"  Immediate get: {ttl_cache.get('temp')}")
    
    time.sleep(3)
    print(f"  After 3 seconds: {ttl_cache.get('temp')}")
    print(f"  Cache stats: {ttl_cache.get_stats()}")
    
    # CACHE PERFORMANCE COMPARISON
    print("\n5. CACHE PERFORMANCE COMPARISON")
    print("-" * 40)
    
    import time
    
    def expensive_computation(n: int) -> int:
        """Simulate expensive computation."""
        time.sleep(0.001)
        return n * n
    
    # Without cache
    start = time.time()
    results_no_cache = [expensive_computation(i % 10) for i in range(1000)]
    no_cache_time = time.time() - start
    
    # With LRU cache
    cache = CacheFactory.lru(max_size=10)
    start = time.time()
    results_cached = []
    for i in range(1000):
        key = i % 10
        value = cache.get(key)
        if value is None:
            value = expensive_computation(key)
            cache.put(key, value)
        results_cached.append(value)
    cached_time = time.time() - start
    
    print(f"  Without cache: {no_cache_time:.3f}s")
    print(f"  With cache: {cached_time:.3f}s")
    print(f"  Speedup: {no_cache_time / cached_time:.1f}x")
    print(f"  Cache stats: {cache.get_stats()}")
    
    # REAL-WORLD: API RESPONSE CACHING
    print("\n6. REAL-WORLD: API RESPONSE CACHING")
    print("-" * 40)
    
    class APIClient:
        def __init__(self):
            self.cache = CacheFactory.ttl(ttl_seconds=30, max_size=100)
            self.call_count = 0
        
        def get_user(self, user_id: int) -> dict:
            cache_key = f"user_{user_id}"
            
            # Check cache
            cached = self.cache.get(cache_key)
            if cached:
                return {"source": "cache", "data": cached}
            
            # Simulate API call
            self.call_count += 1
            time.sleep(0.02)
            user_data = {"id": user_id, "name": f"User {user_id}"}
            
            # Store in cache
            self.cache.put(cache_key, user_data)
            return {"source": "api", "data": user_data}
        
        def get_stats(self):
            return {
                "api_calls": self.call_count,
                "cache_stats": self.cache.get_stats()
            }
    
    api = APIClient()
    
    # First request (cache miss)
    result = api.get_user(1)
    print(f"  First request: {result['source']}")
    
    # Second request (cache hit)
    result = api.get_user(1)
    print(f"  Second request: {result['source']}")
    
    # Wait for expiration
    time.sleep(31)
    result = api.get_user(1)
    print(f"  After TTL expiration: {result['source']}")
    
    stats = api.get_stats()
    print(f"\n  API Stats:")
    print(f"    API calls: {stats['api_calls']}")
    print(f"    Cache hits: {stats['cache_stats']['hits']}")
    print(f"    Cache hit rate: {stats['cache_stats']['hit_rate']:.1f}%")


if __name__ == "__main__":
    demonstrate_memory_efficient_cache()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Reference Counting** – Each object tracks how many references point to it. When count reaches zero, memory is freed. Use `sys.getrefcount()` to inspect.

- **Garbage Collection** – Detects and cleans circular references. Three generations (0, 1, 2). Use `gc.collect()` to force collection.

- **Weak References** – Don't increase reference count. Use `weakref.ref`, `WeakValueDictionary`, `WeakKeyDictionary`, `WeakSet`. Perfect for caches and parent pointers.

- **Memory Profiling** – `tracemalloc` tracks memory allocations. Compare snapshots to find leaks. Profile function memory usage with decorators.

- **Object Pool** – Reuse expensive objects to reduce allocations. Database connections, thread pools, buffer pools.

- **LRU Cache** – Evicts least recently used items. Size and memory limits. High hit rate for repeated access patterns.

- **TTL Cache** – Items expire after time-to-live. Perfect for API responses, session data.

- **Weak Value Cache** – Values are garbage collected when no other references exist. Auto-cleanup, no memory leaks.

- **SOLID Principles Applied** – Single Responsibility (each cache has one eviction policy), Open/Closed (new cache types can be added), Dependency Inversion (caches depend on abstractions), Interface Segregation (clean cache interfaces).

- **Design Patterns Used** – RAII (resource cleanup), Pool Pattern (object reuse), Proxy Pattern (cache access), Factory Pattern (cache creation), Observer Pattern (eviction notifications), Decorator Pattern (profiling).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Iterators – Custom Looping

- **📚 Series F Catalog:** Advanced Python Engineering – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Testing & Debugging – pytest and unittest (Series F, Story 5)

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
| Series F | 6 | 4 | 2 | 67% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **38** | **14** | **73%** |

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

**Next Story:** Series F, Story 5: The 2026 Python Metromap: Testing & Debugging – pytest and unittest

---

## 📝 Your Invitation

You've mastered memory management. Now build something with what you've learned:

1. **Build a memory profiler** – Create a decorator that tracks memory usage of functions and generates reports.

2. **Create a weak reference cache** – Build a cache that automatically removes entries when objects are garbage collected.

3. **Implement an object pool** – Create a pool for database connections, thread pools, or buffer pools.

4. **Build a memory-efficient data structure** – Implement a linked list or tree that uses weak references to prevent cycles.

5. **Create a memory leak detector** – Build a tool that runs functions and reports if memory usage grows over time.

**You've mastered memory management. Next stop: Testing & Debugging!**

---

*Found this helpful? Clap, comment, and share what you built with memory management. Next stop: Testing & Debugging!* 🚇