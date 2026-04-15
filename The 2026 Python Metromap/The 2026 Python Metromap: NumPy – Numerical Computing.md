# The 2026 Python Metromap: NumPy – Numerical Computing

## Series G: Data Science & Visualization | Story 1 of 5

![The 2026 Python Metromap/images/NumPy – Numerical Computing](images/NumPy – Numerical Computing.png)

## 📖 Introduction

**Welcome to the first stop on the Data Science & Visualization Line.**

You've completed the Advanced Python Engineering Line. You've mastered decorators, generators, iterators, memory management, testing, and type hints. You can write robust, efficient, production-ready code. But there's a whole new world of Python that powers data science, machine learning, and scientific computing—and it starts with NumPy.

NumPy (Numerical Python) is the foundation of the entire Python data science ecosystem. It provides the ndarray—a powerful N-dimensional array object that is faster and more memory-efficient than Python lists. NumPy arrays enable vectorized operations, broadcasting, and linear algebra that are essential for data analysis, machine learning, and scientific computing. Pandas, Matplotlib, Scikit-learn, and TensorFlow all build on NumPy.

This story—**The 2026 Python Metromap: NumPy – Numerical Computing**—is your guide to mastering NumPy. We'll create and manipulate ndarrays, perform vectorized operations, use broadcasting, and apply linear algebra. We'll process millions of sensor readings, perform matrix operations for image processing, and calculate statistical aggregates. We'll build a complete data analysis pipeline using NumPy.

**Let's compute numerically.**

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

### Series G: Data Science & Visualization (5 Stories)

- 🔢 **The 2026 Python Metromap: NumPy – Numerical Computing** – Processing millions of sensor readings; matrix operations; statistical aggregates. **⬅️ YOU ARE HERE**

- 🐼 **The 2026 Python Metromap: Pandas – Data Wrangling** – Multi-year sales analysis; CSV cleaning; regional and product aggregation. 🔜 *Up Next*

- 📈 **The 2026 Python Metromap: Matplotlib – Basic Plotting** – Stock price line charts; sales bar charts; market share pie charts.

- 🎨 **The 2026 Python Metromap: Seaborn – Statistical Visualization** – Customer segmentation heatmaps; age distribution plots; feature correlation pair plots.

- 📊 **The 2026 Python Metromap: Real-World EDA Project** – End-to-end exploratory data analysis on COVID-19 data, housing prices, or e-commerce sales.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔢 Section 1: NumPy Basics – Creating and Understanding ndarrays

The ndarray (N-dimensional array) is NumPy's core data structure—more efficient than Python lists for numerical operations.

**SOLID Principle Applied: Single Responsibility** – ndarrays handle numerical data storage and operations.

**Design Pattern: Flyweight Pattern** – NumPy arrays store data contiguously in memory for efficiency.

```python
"""
NUMPY BASICS: CREATING AND UNDERSTANDING NDARRAYS

This section covers creating and manipulating NumPy arrays.

SOLID Principle: Single Responsibility
- ndarrays handle numerical data storage and operations

Design Pattern: Flyweight Pattern
- NumPy arrays store data contiguously in memory for efficiency
"""

import numpy as np
import time
import sys


def demonstrate_array_creation():
    """
    Demonstrates different ways to create NumPy arrays.
    
    NumPy arrays are homogeneous (all elements same type) and fixed-size.
    """
    print("=" * 60)
    print("SECTION 1A: CREATING NUMPY ARRAYS")
    print("=" * 60)
    
    # FROM PYTHON LISTS
    print("\n1. CREATING FROM PYTHON LISTS")
    print("-" * 40)
    
    # 1D array
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"  1D array: {arr1d}")
    print(f"  Shape: {arr1d.shape}, Dimensions: {arr1d.ndim}, Type: {arr1d.dtype}")
    
    # 2D array (matrix)
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n  2D array:\n{arr2d}")
    print(f"  Shape: {arr2d.shape}, Dimensions: {arr2d.ndim}")
    
    # 3D array
    arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"\n  3D array shape: {arr3d.shape}")
    
    # ARRAY CREATION FUNCTIONS
    print("\n2. ARRAY CREATION FUNCTIONS")
    print("-" * 40)
    
    # Zeros
    zeros = np.zeros((3, 4))
    print(f"  zeros((3,4)):\n{zeros}")
    
    # Ones
    ones = np.ones((2, 3))
    print(f"\n  ones((2,3)):\n{ones}")
    
    # Identity matrix
    identity = np.eye(4)
    print(f"\n  eye(4):\n{identity}")
    
    # Constant value
    constants = np.full((2, 3), 7)
    print(f"\n  full((2,3), 7):\n{constants}")
    
    # Range
    range_arr = np.arange(0, 10, 2)
    print(f"\n  arange(0, 10, 2): {range_arr}")
    
    # Linspace (evenly spaced)
    linspace_arr = np.linspace(0, 1, 5)
    print(f"  linspace(0, 1, 5): {linspace_arr}")
    
    # Random arrays
    random_arr = np.random.random((3, 3))
    print(f"\n  random.random((3,3)):\n{random_arr[:2,:2]}...")
    
    random_normal = np.random.randn(2, 4)
    print(f"  randn(2,4): {random_normal}")
    
    random_integers = np.random.randint(1, 10, size=(3, 3))
    print(f"  randint(1,10, size=(3,3)):\n{random_integers}")
    
    # MEMORY EFFICIENCY
    print("\n3. MEMORY EFFICIENCY (NumPy vs Python List)")
    print("-" * 40)
    
    py_list = list(range(1000))
    np_array = np.arange(1000)
    
    list_size = sys.getsizeof(py_list) + sum(sys.getsizeof(i) for i in py_list)
    array_size = np_array.nbytes
    
    print(f"  Python list memory: {list_size:,} bytes")
    print(f"  NumPy array memory: {array_size:,} bytes")
    print(f"  NumPy is {list_size / array_size:.1f}x more memory efficient!")
    
    # DATA TYPES
    print("\n4. NUMPY DATA TYPES")
    print("-" * 40)
    
    int_arr = np.array([1, 2, 3], dtype=np.int32)
    float_arr = np.array([1, 2, 3], dtype=np.float64)
    complex_arr = np.array([1+2j, 3+4j], dtype=np.complex128)
    bool_arr = np.array([True, False, True], dtype=np.bool_)
    
    print(f"  int32: {int_arr.dtype}")
    print(f"  float64: {float_arr.dtype}")
    print(f"  complex128: {complex_arr.dtype}")
    print(f"  bool: {bool_arr.dtype}")
    
    # Changing dtype
    arr = np.array([1, 2, 3, 4])
    float_arr = arr.astype(np.float64)
    print(f"  Converted: {arr.dtype} → {float_arr.dtype}")


def demonstrate_array_attributes_and_operations():
    """
    Demonstrates array attributes and basic operations.
    
    NumPy arrays support vectorized operations (no loops needed).
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ARRAY ATTRIBUTES AND OPERATIONS")
    print("=" * 60)
    
    # ARRAY ATTRIBUTES
    print("\n1. ARRAY ATTRIBUTES")
    print("-" * 40)
    
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    print(f"  Array:\n{arr}")
    print(f"  Shape: {arr.shape}")
    print(f"  Size (total elements): {arr.size}")
    print(f"  Dimensions (ndim): {arr.ndim}")
    print(f"  Data type: {arr.dtype}")
    print(f"  Item size (bytes): {arr.itemsize}")
    print(f"  Total bytes: {arr.nbytes}")
    
    # VECTORIZED OPERATIONS
    print("\n2. VECTORIZED OPERATIONS (No loops needed!)")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5])
    
    # Arithmetic operations
    print(f"  Original: {arr}")
    print(f"  arr + 10: {arr + 10}")
    print(f"  arr * 2: {arr * 2}")
    print(f"  arr ** 2: {arr ** 2}")
    print(f"  np.sqrt(arr): {np.sqrt(arr)}")
    print(f"  np.sin(arr): {np.sin(arr)}")
    
    # OPERATIONS BETWEEN ARRAYS
    print("\n3. OPERATIONS BETWEEN ARRAYS")
    print("-" * 40)
    
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    
    print(f"  a: {a}")
    print(f"  b: {b}")
    print(f"  a + b: {a + b}")
    print(f"  a * b: {a * b}")
    print(f"  a @ b (dot product): {a @ b}")
    print(f"  np.dot(a, b): {np.dot(a, b)}")
    
    # COMPARISON OPERATIONS
    print("\n4. COMPARISON OPERATIONS")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  arr > 3: {arr > 3}")
    print(f"  arr == 3: {arr == 3}")
    print(f"  (arr > 2) & (arr < 5): {(arr > 2) & (arr < 5)}")
    
    # UNIVERSAL FUNCTIONS (ufuncs)
    print("\n5. UNIVERSAL FUNCTIONS (ufuncs)")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5])
    
    print(f"  np.exp(arr): {np.exp(arr)}")
    print(f"  np.log(arr): {np.log(arr)}")
    print(f"  np.log10(arr): {np.log10(arr)}")
    print(f"  np.maximum(arr, 3): {np.maximum(arr, 3)}")
    print(f"  np.minimum(arr, 3): {np.minimum(arr, 3)}")


def demonstrate_performance_comparison():
    """
    Demonstrates the performance advantage of NumPy over Python lists.
    
    Vectorized operations are significantly faster than Python loops.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: PERFORMANCE COMPARISON")
    print("=" * 60)
    
    size = 10_000_000
    
    print(f"\n1. PERFORMANCE: VECTORIZED VS LOOP (size={size:,})")
    print("-" * 40)
    
    # Python list with loop
    py_list = list(range(size))
    start = time.time()
    py_result = [x ** 2 for x in py_list]
    py_time = time.time() - start
    
    # NumPy array with vectorized operation
    np_array = np.arange(size)
    start = time.time()
    np_result = np_array ** 2
    np_time = time.time() - start
    
    print(f"  Python loop: {py_time:.4f} seconds")
    print(f"  NumPy vectorized: {np_time:.4f} seconds")
    print(f"  NumPy is {py_time / np_time:.1f}x faster!")
    
    print("\n2. PERFORMANCE: MATH OPERATIONS")
    print("-" * 40)
    
    size = 1_000_000
    np_array = np.random.randn(size)
    py_list = np_array.tolist()
    
    # Sum
    start = time.time()
    py_sum = sum(py_list)
    py_sum_time = time.time() - start
    
    start = time.time()
    np_sum = np.sum(np_array)
    np_sum_time = time.time() - start
    
    print(f"  Sum - Python: {py_sum_time:.4f}s, NumPy: {np_sum_time:.4f}s")
    print(f"  NumPy is {py_sum_time / np_sum_time:.1f}x faster")
    
    # Mean
    start = time.time()
    py_mean = sum(py_list) / len(py_list)
    py_mean_time = time.time() - start
    
    start = time.time()
    np_mean = np.mean(np_array)
    np_mean_time = time.time() - start
    
    print(f"  Mean - Python: {py_mean_time:.4f}s, NumPy: {np_mean_time:.4f}s")
    print(f"  NumPy is {py_mean_time / np_mean_time:.1f}x faster")


def demonstrate_shape_manipulation():
    """
    Demonstrates reshaping, flattening, and transposing arrays.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: SHAPE MANIPULATION")
    print("=" * 60)
    
    arr = np.arange(12)
    print(f"\n1. ORIGINAL ARRAY")
    print("-" * 40)
    print(f"  arr: {arr}")
    print(f"  shape: {arr.shape}")
    
    # RESHAPE
    print("\n2. RESHAPE")
    print("-" * 40)
    
    arr_2d = arr.reshape(3, 4)
    print(f"  reshape(3,4):\n{arr_2d}")
    
    arr_2d_other = arr.reshape(2, 6)
    print(f"\n  reshape(2,6):\n{arr_2d_other}")
    
    # -1 for automatic dimension
    arr_auto = arr.reshape(2, -1)
    print(f"\n  reshape(2, -1):\n{arr_auto}")
    
    # FLATTEN
    print("\n3. FLATTEN")
    print("-" * 40)
    
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"  Original matrix:\n{matrix}")
    print(f"  ravel(): {matrix.ravel()} (returns view)")
    print(f"  flatten(): {matrix.flatten()} (returns copy)")
    
    # TRANSPOSE
    print("\n4. TRANSPOSE")
    print("-" * 40)
    
    print(f"  Original:\n{matrix}")
    print(f"  transpose():\n{matrix.T}")
    print(f"  transpose() shape: {matrix.T.shape}")
    
    # RESIZE (modifies array)
    print("\n5. RESIZE (modifies original)")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"  Original: {arr}")
    arr.resize(2, 3)
    print(f"  After resize(2,3):\n{arr}")


if __name__ == "__main__":
    demonstrate_array_creation()
    demonstrate_array_attributes_and_operations()
    demonstrate_performance_comparison()
    demonstrate_shape_manipulation()
```

---

## 🔄 Section 2: Indexing and Slicing – Accessing Array Elements

NumPy provides powerful indexing and slicing capabilities similar to Python lists, but extended for multi-dimensional arrays.

**SOLID Principle Applied: Single Responsibility** – Indexing operations access data without modification.

**Design Pattern: Iterator Pattern** – Fancy indexing creates new arrays from selected elements.

```python
"""
INDEXING AND SLICING: ACCESSING ARRAY ELEMENTS

This section covers indexing, slicing, and advanced indexing in NumPy.

SOLID Principle: Single Responsibility
- Indexing operations access data without modification

Design Pattern: Iterator Pattern
- Fancy indexing creates new arrays from selected elements
"""

import numpy as np


def demonstrate_basic_indexing_and_slicing():
    """
    Demonstrates basic indexing and slicing (similar to Python lists).
    """
    print("=" * 60)
    print("SECTION 2A: BASIC INDEXING AND SLICING")
    print("=" * 60)
    
    # 1D ARRAY INDEXING
    print("\n1. 1D ARRAY INDEXING")
    print("-" * 40)
    
    arr = np.array([10, 20, 30, 40, 50])
    print(f"  arr: {arr}")
    print(f"  arr[0]: {arr[0]}")
    print(f"  arr[-1]: {arr[-1]}")
    print(f"  arr[2]: {arr[2]}")
    
    # 1D SLICING
    print("\n2. 1D SLICING")
    print("-" * 40)
    
    print(f"  arr[:3]: {arr[:3]}")
    print(f"  arr[2:]: {arr[2:]}")
    print(f"  arr[1:4]: {arr[1:4]}")
    print(f"  arr[::2]: {arr[::2]}")
    print(f"  arr[::-1]: {arr[::-1]}")
    
    # 2D ARRAY INDEXING
    print("\n3. 2D ARRAY INDEXING")
    print("-" * 40)
    
    matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(f"  Matrix:\n{matrix}")
    print(f"  matrix[0, 2]: {matrix[0, 2]}")
    print(f"  matrix[1, 3]: {matrix[1, 3]}")
    print(f"  matrix[2, 0]: {matrix[2, 0]}")
    
    # 2D SLICING
    print("\n4. 2D SLICING")
    print("-" * 40)
    
    print(f"  matrix[0:2, 1:3]:\n{matrix[0:2, 1:3]}")
    print(f"  matrix[:, 1:3]:\n{matrix[:, 1:3]}")
    print(f"  matrix[1:, :2]:\n{matrix[1:, :2]}")
    print(f"  matrix[:, ::2]:\n{matrix[:, ::2]}")
    
    # MODIFYING WITH SLICING
    print("\n5. MODIFYING WITH SLICING")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  Before: {arr}")
    arr[1:4] = 99
    print(f"  After arr[1:4] = 99: {arr}")
    
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n  Matrix before:\n{matrix}")
    matrix[0, :] = [10, 11, 12]
    print(f"  After matrix[0, :] = [10,11,12]:\n{matrix}")
    matrix[:, 1] = 99
    print(f"  After matrix[:, 1] = 99:\n{matrix}")


def demonstrate_fancy_indexing():
    """
    Demonstrates fancy indexing (indexing with integer arrays).
    
    Fancy indexing creates a copy, not a view.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: FANCY INDEXING")
    print("=" * 60)
    
    # 1D FANCY INDEXING
    print("\n1. 1D FANCY INDEXING")
    print("-" * 40)
    
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    print(f"  arr: {arr}")
    
    indices = [1, 3, 5]
    print(f"  arr[[1, 3, 5]]: {arr[indices]}")
    
    # Using array of indices
    idx = np.array([0, 2, 4, 6])
    print(f"  arr[idx]: {arr[idx]}")
    
    # Using negative indices
    print(f"  arr[[-1, -2, -3]]: {arr[[-1, -2, -3]]}")
    
    # 2D FANCY INDEXING
    print("\n2. 2D FANCY INDEXING")
    print("-" * 40)
    
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print(f"  Matrix:\n{matrix}")
    
    # Select specific rows
    print(f"  matrix[[0, 2, 3]]:\n{matrix[[0, 2, 3]]}")
    
    # Select specific rows and columns
    print(f"  matrix[[0, 2], [1, 2]]: {matrix[[0, 2], [1, 2]]}")
    
    # Using meshgrid for rectangular selection
    rows = np.array([0, 2])
    cols = np.array([1, 2])
    print(f"  rows={rows}, cols={cols}")
    print(f"  matrix[rows[:, np.newaxis], cols]:\n{matrix[rows[:, np.newaxis], cols]}")
    
    # COMBINING SLICES AND FANCY INDEXING
    print("\n3. COMBINING SLICES AND FANCY INDEXING")
    print("-" * 40)
    
    print(f"  matrix[1:3, [0, 2]]:\n{matrix[1:3, [0, 2]]}")
    print(f"  matrix[[0, 2], 1:3]:\n{matrix[[0, 2], 1:3]}")


def demonstrate_boolean_indexing():
    """
    Demonstrates boolean (mask) indexing for conditional selection.
    
    Boolean indexing creates a copy of selected elements.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: BOOLEAN INDEXING")
    print("=" * 60)
    
    # 1D BOOLEAN INDEXING
    print("\n1. 1D BOOLEAN INDEXING")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"  arr: {arr}")
    
    mask = arr > 5
    print(f"  mask (arr > 5): {mask}")
    print(f"  arr[mask]: {arr[mask]}")
    
    # Combined conditions
    mask2 = (arr > 3) & (arr < 8)
    print(f"  mask ((arr > 3) & (arr < 8)): {mask2}")
    print(f"  arr[mask2]: {arr[mask2]}")
    
    # Direct condition
    print(f"  arr[arr % 2 == 0]: {arr[arr % 2 == 0]}")
    print(f"  arr[arr % 2 == 1]: {arr[arr % 2 == 1]}")
    
    # 2D BOOLEAN INDEXING
    print("\n2. 2D BOOLEAN INDEXING")
    print("-" * 40)
    
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"  Matrix:\n{matrix}")
    
    mask = matrix > 5
    print(f"  mask (matrix > 5):\n{mask}")
    print(f"  matrix[mask]: {matrix[mask]}")
    
    # Row-wise conditions
    row_mask = matrix.sum(axis=1) > 15
    print(f"  row_mask (sum > 15): {row_mask}")
    print(f"  matrix[row_mask]:\n{matrix[row_mask]}")
    
    # PRACTICAL: DATA FILTERING
    print("\n3. PRACTICAL: DATA FILTERING")
    print("-" * 40)
    
    # Sensor data with outliers
    sensor_data = np.array([22.5, 23.1, 21.8, 999.9, 22.3, 22.7, -999, 22.9])
    print(f"  Raw sensor data: {sensor_data}")
    
    # Remove outliers
    valid_mask = (sensor_data > -100) & (sensor_data < 100)
    cleaned_data = sensor_data[valid_mask]
    print(f"  Valid mask: {valid_mask}")
    print(f"  Cleaned data: {cleaned_data}")
    
    # Replace outliers with mean
    mean_value = np.mean(cleaned_data)
    sensor_data[~valid_mask] = mean_value
    print(f"  After replacing outliers: {sensor_data}")


def demonstrate_advanced_indexing_techniques():
    """
    Demonstrates advanced indexing techniques like take, choose, and where.
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: ADVANCED INDEXING TECHNIQUES")
    print("=" * 60)
    
    # np.where (conditional selection)
    print("\n1. np.where() - Conditional selection")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # Replace values based on condition
    result = np.where(arr > 5, 1, 0)
    print(f"  arr: {arr}")
    print(f"  np.where(arr > 5, 1, 0): {result}")
    
    # Replace with different values
    result = np.where(arr % 2 == 0, "even", "odd")
    print(f"  np.where(arr % 2 == 0, 'even', 'odd'): {result}")
    
    # np.take (take elements at indices)
    print("\n2. np.take() - Take elements at indices")
    print("-" * 40)
    
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    indices = [0, 2, 4, 6]
    print(f"  arr: {arr}")
    print(f"  indices: {indices}")
    print(f"  np.take(arr, indices): {np.take(arr, indices)}")
    
    # np.choose (choose from multiple arrays)
    print("\n3. np.choose() - Choose from multiple arrays")
    print("-" * 40)
    
    choices = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
    selector = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2]).reshape(3, 3)
    result = np.choose(selector, choices)
    print(f"  choices: {choices}")
    print(f"  selector:\n{selector}")
    print(f"  result:\n{result}")
    
    # np.extract (extract elements where condition is True)
    print("\n4. np.extract() - Extract where condition is True")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    condition = arr % 3 == 0
    extracted = np.extract(condition, arr)
    print(f"  arr: {arr}")
    print(f"  condition (arr % 3 == 0): {condition}")
    print(f"  np.extract(condition, arr): {extracted}")


if __name__ == "__main__":
    demonstrate_basic_indexing_and_slicing()
    demonstrate_fancy_indexing()
    demonstrate_boolean_indexing()
    demonstrate_advanced_indexing_techniques()
```

---

## 📊 Section 3: Array Operations – Math, Statistics, and Linear Algebra

NumPy provides a comprehensive set of mathematical, statistical, and linear algebra operations.

**SOLID Principle Applied: Single Responsibility** – Each function performs one mathematical operation.

**Design Pattern: Strategy Pattern** – Different reduction strategies (sum, mean, std, etc.).

```python
"""
ARRAY OPERATIONS: MATH, STATISTICS, AND LINEAR ALGEBRA

This section covers mathematical, statistical, and linear algebra operations.

SOLID Principle: Single Responsibility
- Each function performs one mathematical operation

Design Pattern: Strategy Pattern
- Different reduction strategies (sum, mean, std, etc.)
"""

import numpy as np


def demonstrate_aggregation_functions():
    """
    Demonstrates aggregation functions (sum, mean, min, max, etc.).
    
    Aggregation functions reduce the array to a single value or along an axis.
    """
    print("=" * 60)
    print("SECTION 3A: AGGREGATION FUNCTIONS")
    print("=" * 60)
    
    # 1D ARRAY AGGREGATIONS
    print("\n1. 1D ARRAY AGGREGATIONS")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"  arr: {arr}")
    print(f"  sum: {np.sum(arr)}")
    print(f"  mean: {np.mean(arr):.2f}")
    print(f"  median: {np.median(arr):.2f}")
    print(f"  min: {np.min(arr)}")
    print(f"  max: {np.max(arr)}")
    print(f"  std (standard deviation): {np.std(arr):.2f}")
    print(f"  var (variance): {np.var(arr):.2f}")
    
    # 2D ARRAY AGGREGATIONS
    print("\n2. 2D ARRAY AGGREGATIONS (with axis)")
    print("-" * 40)
    
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"  Matrix:\n{matrix}")
    
    # Axis=0 (column-wise)
    print(f"\n  sum(axis=0): {np.sum(matrix, axis=0)} (column sums)")
    print(f"  mean(axis=0): {np.mean(matrix, axis=0)} (column means)")
    print(f"  min(axis=0): {np.min(matrix, axis=0)} (column mins)")
    
    # Axis=1 (row-wise)
    print(f"\n  sum(axis=1): {np.sum(matrix, axis=1)} (row sums)")
    print(f"  mean(axis=1): {np.mean(matrix, axis=1)} (row means)")
    print(f"  min(axis=1): {np.min(matrix, axis=1)} (row mins)")
    
    # CUMULATIVE OPERATIONS
    print("\n3. CUMULATIVE OPERATIONS")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  arr: {arr}")
    print(f"  cumsum (cumulative sum): {np.cumsum(arr)}")
    print(f"  cumprod (cumulative product): {np.cumprod(arr)}")
    
    # PERCENTILES
    print("\n4. PERCENTILES")
    print("-" * 40)
    
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100])
    print(f"  data: {data}")
    print(f"  25th percentile: {np.percentile(data, 25)}")
    print(f"  50th percentile (median): {np.percentile(data, 50)}")
    print(f"  75th percentile: {np.percentile(data, 75)}")
    print(f"  90th percentile: {np.percentile(data, 90)}")


def demonstrate_broadcasting():
    """
    Demonstrates broadcasting - NumPy's ability to operate on arrays of different shapes.
    
    Broadcasting allows operations between arrays of different sizes.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: BROADCASTING")
    print("=" * 60)
    
    # SCALAR BROADCASTING
    print("\n1. SCALAR BROADCASTING")
    print("-" * 40)
    
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  arr: {arr}")
    print(f"  arr + 10: {arr + 10}")
    print(f"  arr * 2: {arr * 2}")
    print(f"  arr ** 2: {arr ** 2}")
    
    # VECTOR BROADCASTING
    print("\n2. VECTOR BROADCASTING")
    print("-" * 40)
    
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    vector = np.array([10, 20, 30])
    print(f"  Matrix:\n{matrix}")
    print(f"  Vector: {vector}")
    print(f"  matrix + vector:\n{matrix + vector}")
    
    # MATRIX BROADCASTING
    print("\n3. MATRIX BROADCASTING")
    print("-" * 40)
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[10], [20]])
    print(f"  A:\n{A}")
    print(f"  B:\n{B}")
    print(f"  A + B:\n{A + B}")
    
    # PRACTICAL: NORMALIZING DATA
    print("\n4. PRACTICAL: NORMALIZING DATA")
    print("-" * 40)
    
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"  Original data:\n{data}")
    
    # Subtract mean and divide by std (standardization)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized = (data - mean) / std
    print(f"  Column means: {mean}")
    print(f"  Column stds: {std}")
    print(f"  Normalized (Z-score):\n{normalized}")
    print(f"  Normalized mean: {np.mean(normalized, axis=0)}")
    print(f"  Normalized std: {np.std(normalized, axis=0)}")


def demonstrate_linear_algebra():
    """
    Demonstrates linear algebra operations with NumPy.
    
    NumPy provides matrix multiplication, dot product, inverse, determinant, eigenvalues.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: LINEAR ALGEBRA")
    print("=" * 60)
    
    # MATRIX MULTIPLICATION
    print("\n1. MATRIX MULTIPLICATION")
    print("-" * 40)
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"  A:\n{A}")
    print(f"  B:\n{B}")
    print(f"  A @ B:\n{A @ B}")
    print(f"  np.dot(A, B):\n{np.dot(A, B)}")
    print(f"  A.dot(B):\n{A.dot(B)}")
    
    # VECTOR DOT PRODUCT
    print("\n2. VECTOR DOT PRODUCT")
    print("-" * 40)
    
    v = np.array([1, 2, 3])
    w = np.array([4, 5, 6])
    print(f"  v: {v}")
    print(f"  w: {w}")
    print(f"  v @ w: {v @ w}")
    print(f"  np.dot(v, w): {np.dot(v, w)}")
    
    # MATRIX INVERSE
    print("\n3. MATRIX INVERSE")
    print("-" * 40)
    
    A = np.array([[1, 2], [3, 4]])
    A_inv = np.linalg.inv(A)
    print(f"  A:\n{A}")
    print(f"  A_inv:\n{A_inv}")
    print(f"  A @ A_inv:\n{A @ A_inv}")
    
    # DETERMINANT
    print("\n4. DETERMINANT")
    print("-" * 40)
    
    A = np.array([[1, 2], [3, 4]])
    det = np.linalg.det(A)
    print(f"  A:\n{A}")
    print(f"  determinant: {det:.2f}")
    
    # EIGENVALUES AND EIGENVECTORS
    print("\n5. EIGENVALUES AND EIGENVECTORS")
    print("-" * 40)
    
    A = np.array([[4, 2], [1, 3]])
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"  A:\n{A}")
    print(f"  Eigenvalues: {eigenvalues}")
    print(f"  Eigenvectors:\n{eigenvectors}")
    
    # SOLVING LINEAR SYSTEMS
    print("\n6. SOLVING LINEAR SYSTEMS (Ax = b)")
    print("-" * 40)
    
    # 2x + y = 5
    # x + 2y = 4
    A = np.array([[2, 1], [1, 2]])
    b = np.array([5, 4])
    x = np.linalg.solve(A, b)
    print(f"  A:\n{A}")
    print(f"  b: {b}")
    print(f"  Solution x: {x}")
    print(f"  Verification: A @ x = {A @ x}")


def demonstrate_statistical_operations():
    """
    Demonstrates advanced statistical operations with NumPy.
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: STATISTICAL OPERATIONS")
    print("=" * 60)
    
    # Generate random data
    np.random.seed(42)
    data = np.random.normal(loc=100, scale=15, size=1000)
    
    print("\n1. DESCRIPTIVE STATISTICS")
    print("-" * 40)
    
    print(f"  Mean: {np.mean(data):.2f}")
    print(f"  Median: {np.median(data):.2f}")
    print(f"  Std: {np.std(data):.2f}")
    print(f"  Variance: {np.var(data):.2f}")
    print(f"  Min: {np.min(data):.2f}")
    print(f"  Max: {np.max(data):.2f}")
    print(f"  Range: {np.ptp(data):.2f}")
    
    # CORRELATION
    print("\n2. CORRELATION")
    print("-" * 40)
    
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    z = np.array([5, 4, 3, 2, 1])
    
    print(f"  x: {x}, y: {y}, z: {z}")
    print(f"  Correlation x-y: {np.corrcoef(x, y)[0, 1]:.3f}")
    print(f"  Correlation x-z: {np.corrcoef(x, z)[0, 1]:.3f}")
    
    # COVARIANCE
    print("\n3. COVARIANCE")
    print("-" * 40)
    
    cov_matrix = np.cov(x, y)
    print(f"  Covariance matrix:\n{cov_matrix}")
    
    # HISTOGRAM
    print("\n4. HISTOGRAM")
    print("-" * 40)
    
    hist, bin_edges = np.histogram(data, bins=10)
    print(f"  Histogram bins: {len(hist)}")
    print(f"  Bin edges: {bin_edges[:3]}...{bin_edges[-3:]}")
    print(f"  Counts: {hist[:3]}...{hist[-3:]}")
    
    # UNIQUE VALUES
    print("\n5. UNIQUE VALUES")
    print("-" * 40)
    
    arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    unique, counts = np.unique(arr, return_counts=True)
    print(f"  arr: {arr}")
    print(f"  Unique values: {unique}")
    print(f"  Counts: {counts}")


if __name__ == "__main__":
    demonstrate_aggregation_functions()
    demonstrate_broadcasting()
    demonstrate_linear_algebra()
    demonstrate_statistical_operations()
```

---

## 🔬 Section 4: Practical Data Analysis with NumPy

Complete practical examples of using NumPy for real-world data analysis.

**SOLID Principles Applied:**
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New analysis types can be added

**Design Patterns:**
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different normalization strategies

```python
"""
PRACTICAL DATA ANALYSIS WITH NUMPY

This section applies NumPy to real-world data analysis problems.

SOLID Principles Applied:
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New analysis types can be added

Design Patterns:
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different normalization strategies
"""

import numpy as np
import time
from datetime import datetime, timedelta


def generate_sensor_data():
    """
    Generates simulated sensor data for analysis.
    
    Creates temperature, humidity, and pressure readings over time.
    """
    print("=" * 60)
    print("SECTION 4A: GENERATING SENSOR DATA")
    print("=" * 60)
    
    # Simulate 30 days of hourly readings
    hours = 30 * 24
    timestamps = np.arange(hours)
    
    # Temperature: sinusoidal pattern with daily cycle + noise
    temp_base = 20 + 5 * np.sin(2 * np.pi * timestamps / 24)  # Daily cycle
    temp_noise = np.random.normal(0, 2, hours)
    temperature = temp_base + temp_noise
    
    # Humidity: inverse relationship with temperature + noise
    humidity_base = 60 - 15 * np.sin(2 * np.pi * timestamps / 24)
    humidity_noise = np.random.normal(0, 5, hours)
    humidity = np.clip(humidity_base + humidity_noise, 0, 100)
    
    # Pressure: slow variation + noise
    pressure_base = 1013 + 5 * np.sin(2 * np.pi * timestamps / (24 * 7))  # Weekly cycle
    pressure_noise = np.random.normal(0, 3, hours)
    pressure = pressure_base + pressure_noise
    
    print(f"\n  Generated {hours} hours of sensor data")
    print(f"  Temperature range: {np.min(temperature):.1f}°C - {np.max(temperature):.1f}°C")
    print(f"  Humidity range: {np.min(humidity):.1f}% - {np.max(humidity):.1f}%")
    print(f"  Pressure range: {np.min(pressure):.1f} hPa - {np.max(pressure):.1f} hPa")
    
    return {
        "timestamps": timestamps,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    }


def analyze_sensor_data(data):
    """
    Analyzes sensor data to find patterns and anomalies.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: ANALYZING SENSOR DATA")
    print("=" * 60)
    
    temp = data["temperature"]
    humidity = data["humidity"]
    pressure = data["pressure"]
    
    # BASIC STATISTICS
    print("\n1. BASIC STATISTICS")
    print("-" * 40)
    
    print(f"  Temperature - Mean: {np.mean(temp):.2f}°C, Std: {np.std(temp):.2f}°C")
    print(f"  Humidity - Mean: {np.mean(humidity):.2f}%, Std: {np.std(humidity):.2f}%")
    print(f"  Pressure - Mean: {np.mean(pressure):.2f} hPa, Std: {np.std(pressure):.2f} hPa")
    
    # ANOMALY DETECTION (3-sigma rule)
    print("\n2. ANOMALY DETECTION (3-sigma)")
    print("-" * 40)
    
    temp_mean, temp_std = np.mean(temp), np.std(temp)
    temp_anomalies = np.abs(temp - temp_mean) > 3 * temp_std
    print(f"  Temperature anomalies: {np.sum(temp_anomalies)} readings")
    
    humidity_mean, humidity_std = np.mean(humidity), np.std(humidity)
    humidity_anomalies = np.abs(humidity - humidity_mean) > 3 * humidity_std
    print(f"  Humidity anomalies: {np.sum(humidity_anomalies)} readings")
    
    # CORRELATION ANALYSIS
    print("\n3. CORRELATION ANALYSIS")
    print("-" * 40)
    
    temp_humidity_corr = np.corrcoef(temp, humidity)[0, 1]
    temp_pressure_corr = np.corrcoef(temp, pressure)[0, 1]
    humidity_pressure_corr = np.corrcoef(humidity, pressure)[0, 1]
    
    print(f"  Temperature-Humidity correlation: {temp_humidity_corr:.3f}")
    print(f"  Temperature-Pressure correlation: {temp_pressure_corr:.3f}")
    print(f"  Humidity-Pressure correlation: {humidity_pressure_corr:.3f}")
    
    # DAILY AGGREGATION
    print("\n4. DAILY AGGREGATION")
    print("-" * 40)
    
    # Reshape to days (24 hours per day)
    days = len(temp) // 24
    temp_daily = temp[:days*24].reshape(days, 24)
    
    daily_means = np.mean(temp_daily, axis=1)
    daily_mins = np.min(temp_daily, axis=1)
    daily_maxs = np.max(temp_daily, axis=1)
    
    print(f"  Daily temperature - Mean: {np.mean(daily_means):.1f}°C")
    print(f"  Daily temperature - Min: {np.min(daily_mins):.1f}°C")
    print(f"  Daily temperature - Max: {np.max(daily_maxs):.1f}°C")
    
    # PEAK DETECTION
    print("\n5. PEAK DETECTION")
    print("-" * 40)
    
    # Find peaks (local maxima)
    from scipy.signal import find_peaks
    
    peaks, properties = find_peaks(temp, distance=24, prominence=2)
    print(f"  Temperature peaks detected: {len(peaks)}")
    print(f"  Peak temperatures: {temp[peaks][:5]}...")
    
    # TREND ANALYSIS (moving average)
    print("\n6. TREND ANALYSIS (Moving Average)")
    print("-" * 40)
    
    window = 24 * 7  # 7-day moving average
    temp_ma = np.convolve(temp, np.ones(window)/window, mode='valid')
    
    print(f"  Original temperature range: {np.min(temp):.1f} - {np.max(temp):.1f}°C")
    print(f"  Moving average range: {np.min(temp_ma):.1f} - {np.max(temp_ma):.1f}°C")
    print(f"  Trend direction: {'Increasing' if temp_ma[-1] > temp_ma[0] else 'Decreasing'}")


def process_image_data():
    """
    Demonstrates image processing with NumPy.
    
    Images are just 3D arrays (height, width, channels).
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: IMAGE PROCESSING WITH NUMPY")
    print("=" * 60)
    
    # Create a synthetic image (100x100 RGB)
    print("\n1. CREATING SYNTHETIC IMAGE")
    print("-" * 40)
    
    height, width = 100, 100
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Add a red square in the center
    center_y, center_x = height // 2, width // 2
    size = 30
    image[center_y-size:center_y+size, center_x-size:center_x+size, 0] = 255
    
    # Add a green circle
    y, x = np.ogrid[:height, :width]
    mask = (x - center_x) ** 2 + (y - center_y) ** 2 < size ** 2
    image[mask, 1] = 255
    
    print(f"  Image shape: {image.shape}")
    print(f"  Image dtype: {image.dtype}")
    print(f"  Image min: {image.min()}, max: {image.max()}")
    
    # BRIGHTNESS ADJUSTMENT
    print("\n2. BRIGHTNESS ADJUSTMENT")
    print("-" * 40)
    
    # Increase brightness
    bright = np.clip(image.astype(np.int16) + 50, 0, 255).astype(np.uint8)
    print(f"  Brightness increased by 50")
    
    # Decrease brightness
    dark = np.clip(image.astype(np.int16) - 50, 0, 255).astype(np.uint8)
    print(f"  Brightness decreased by 50")
    
    # COLOR TRANSFORMATION (Grayscale)
    print("\n3. GRAYSCALE CONVERSION")
    print("-" * 40)
    
    # Weighted average for grayscale
    grayscale = (0.2989 * image[:, :, 0] + 
                 0.5870 * image[:, :, 1] + 
                 0.1140 * image[:, :, 2]).astype(np.uint8)
    print(f"  Grayscale shape: {grayscale.shape}")
    print(f"  Grayscale range: {grayscale.min()} - {grayscale.max()}")
    
    # FLIP AND ROTATE
    print("\n4. FLIP AND ROTATE")
    print("-" * 40)
    
    flipped_h = np.flip(image, axis=1)  # Horizontal flip
    flipped_v = np.flip(image, axis=0)  # Vertical flip
    rotated = np.rot90(image, k=1)      # Rotate 90 degrees
    
    print(f"  Original shape: {image.shape}")
    print(f"  Horizontal flip shape: {flipped_h.shape}")
    print(f"  Vertical flip shape: {flipped_v.shape}")
    print(f"  Rotated shape: {rotated.shape}")
    
    # IMAGE FILTERING (Blur)
    print("\n5. IMAGE FILTERING (Simple Blur)")
    print("-" * 40)
    
    # Simple 3x3 averaging filter
    kernel = np.ones((3, 3, 1)) / 9
    
    # Apply filter (simplified - would use convolution in practice)
    blurred = np.zeros_like(image)
    for c in range(3):
        blurred[1:-1, 1:-1, c] = (
            image[0:-2, 0:-2, c] + image[0:-2, 1:-1, c] + image[0:-2, 2:, c] +
            image[1:-1, 0:-2, c] + image[1:-1, 1:-1, c] + image[1:-1, 2:, c] +
            image[2:, 0:-2, c] + image[2:, 1:-1, c] + image[2:, 2:, c]
        ) / 9
    
    print(f"  Blurred image shape: {blurred.shape}")


def analyze_financial_data():
    """
    Demonstrates financial data analysis with NumPy.
    
    Calculates returns, volatility, and moving averages.
    """
    print("\n" + "=" * 60)
    print("SECTION 4D: FINANCIAL DATA ANALYSIS")
    print("=" * 60)
    
    # Generate simulated stock price data
    np.random.seed(42)
    days = 252  # One trading year
    initial_price = 100
    daily_returns = np.random.normal(0.0005, 0.02, days)  # 0.05% mean, 2% volatility
    
    # Calculate price path
    price = initial_price * np.exp(np.cumsum(daily_returns))
    
    print("\n1. STOCK PRICE STATISTICS")
    print("-" * 40)
    
    print(f"  Initial price: ${initial_price:.2f}")
    print(f"  Final price: ${price[-1]:.2f}")
    print(f"  Total return: {(price[-1] / initial_price - 1) * 100:.1f}%")
    print(f"  Max price: ${np.max(price):.2f}")
    print(f"  Min price: ${np.min(price):.2f}")
    print(f"  Price volatility (daily): {np.std(daily_returns) * 100:.2f}%")
    print(f"  Price volatility (annual): {np.std(daily_returns) * np.sqrt(252) * 100:.2f}%")
    
    # MOVING AVERAGES
    print("\n2. MOVING AVERAGES")
    print("-" * 40)
    
    window = 20
    ma_20 = np.convolve(price, np.ones(window)/window, mode='valid')
    ma_50 = np.convolve(price, np.ones(50)/50, mode='valid')
    
    print(f"  Current price: ${price[-1]:.2f}")
    print(f"  20-day MA: ${ma_20[-1]:.2f}")
    print(f"  50-day MA: ${ma_50[-1]:.2f}")
    print(f"  Signal: {'BUY' if ma_20[-1] > ma_50[-1] else 'SELL'}")
    
    # MAXIMUM DRAWDOWN
    print("\n3. MAXIMUM DRAWDOWN")
    print("-" * 40)
    
    running_max = np.maximum.accumulate(price)
    drawdown = (price - running_max) / running_max * 100
    max_drawdown = np.min(drawdown)
    
    print(f"  Maximum drawdown: {max_drawdown:.1f}%")
    print(f"  Days to recover: {np.argmax(price > running_max[np.argmin(drawdown)]) - np.argmin(drawdown)}")
    
    # MONTHLY RETURNS
    print("\n4. MONTHLY RETURNS")
    print("-" * 40)
    
    # Reshape to months (21 trading days per month)
    months = len(price) // 21
    monthly_prices = price[:months*21].reshape(months, 21)
    monthly_returns = (monthly_prices[:, -1] / monthly_prices[:, 0] - 1) * 100
    
    print(f"  Best month: {np.max(monthly_returns):.1f}%")
    print(f"  Worst month: {np.min(monthly_returns):.1f}%")
    print(f"  Average monthly return: {np.mean(monthly_returns):.1f}%")
    print(f"  Positive months: {np.sum(monthly_returns > 0)}/{months}")
    
    # RISK METRICS
    print("\n5. RISK METRICS")
    print("-" * 40)
    
    # Value at Risk (VaR) at 95% confidence
    var_95 = np.percentile(daily_returns, 5)
    print(f"  Daily VaR (95%): {var_95 * 100:.2f}%")
    
    # Conditional VaR (Expected Shortfall)
    cvar_95 = np.mean(daily_returns[daily_returns <= var_95])
    print(f"  Daily CVaR (95%): {cvar_95 * 100:.2f}%")


def build_complete_analysis_pipeline():
    """
    Builds a complete data analysis pipeline using NumPy.
    
    Design Pattern: Pipeline Pattern - Data flows through analysis stages
    """
    print("\n" + "=" * 60)
    print("SECTION 4E: COMPLETE ANALYSIS PIPELINE")
    print("=" * 60)
    
    class DataPipeline:
        """Complete data analysis pipeline."""
        
        def __init__(self):
            self.stages = []
        
        def add_stage(self, name, func):
            self.stages.append({"name": name, "func": func})
            return self
        
        def run(self, data):
            results = {}
            current_data = data
            
            for stage in self.stages:
                print(f"\n  Running: {stage['name']}")
                start = time.time()
                current_data, stage_result = stage['func'](current_data)
                elapsed = time.time() - start
                
                if stage_result is not None:
                    results[stage['name']] = stage_result
                
                print(f"    Completed in {elapsed:.3f}s")
            
            return current_data, results
    
    # Define pipeline stages
    def load_data(data):
        """Load and prepare data."""
        # Generate sample data
        np.random.seed(42)
        n_samples = 10000
        data = {
            "values": np.random.randn(n_samples) * 10 + 50,
            "labels": np.random.choice(["A", "B", "C"], n_samples)
        }
        print(f"    Loaded {n_samples} samples")
        return data, {"n_samples": n_samples}
    
    def clean_data(data):
        """Clean data (remove outliers)."""
        values = data["values"]
        labels = data["labels"]
        
        # Remove outliers beyond 3 sigma
        mean, std = np.mean(values), np.std(values)
        mask = np.abs(values - mean) <= 3 * std
        
        cleaned_values = values[mask]
        cleaned_labels = labels[mask]
        
        removed = len(values) - len(cleaned_values)
        print(f"    Removed {removed} outliers")
        
        return {"values": cleaned_values, "labels": cleaned_labels}, {"removed": removed}
    
    def normalize_data(data):
        """Normalize data to [0, 1] range."""
        values = data["values"]
        min_val, max_val = np.min(values), np.max(values)
        normalized = (values - min_val) / (max_val - min_val)
        
        print(f"    Normalized range: [{np.min(normalized):.3f}, {np.max(normalized):.3f}]")
        
        return {"values": normalized, "labels": data["labels"]}, {"min": min_val, "max": max_val}
    
    def analyze_data(data):
        """Perform statistical analysis."""
        values = data["values"]
        labels = data["labels"]
        
        stats = {
            "mean": np.mean(values),
            "median": np.median(values),
            "std": np.std(values),
            "min": np.min(values),
            "max": np.max(values),
            "percentiles": {
                "25": np.percentile(values, 25),
                "50": np.percentile(values, 50),
                "75": np.percentile(values, 75),
                "90": np.percentile(values, 90),
                "95": np.percentile(values, 95),
                "99": np.percentile(values, 99)
            }
        }
        
        # Statistics by label
        unique_labels = np.unique(labels)
        by_label = {}
        for label in unique_labels:
            label_values = values[labels == label]
            by_label[label] = {
                "count": len(label_values),
                "mean": np.mean(label_values),
                "std": np.std(label_values)
            }
        stats["by_label"] = by_label
        
        print(f"    Mean: {stats['mean']:.3f}, Std: {stats['std']:.3f}")
        
        return data, stats
    
    # Build and run pipeline
    pipeline = DataPipeline()
    pipeline.add_stage("Load Data", load_data)
    pipeline.add_stage("Clean Data", clean_data)
    pipeline.add_stage("Normalize", normalize_data)
    pipeline.add_stage("Analyze", analyze_data)
    
    print("\n  Running analysis pipeline...")
    final_data, results = pipeline.run(None)
    
    print("\n  FINAL RESULTS:")
    for stage, result in results.items():
        print(f"\n  {stage}:")
        if isinstance(result, dict):
            for key, value in result.items():
                if isinstance(value, dict):
                    print(f"    {key}:")
                    for k, v in value.items():
                        print(f"      {k}: {v}")
                else:
                    print(f"    {key}: {value}")


if __name__ == "__main__":
    sensor_data = generate_sensor_data()
    analyze_sensor_data(sensor_data)
    process_image_data()
    analyze_financial_data()
    build_complete_analysis_pipeline()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **ndarray Basics** – Homogeneous, fixed-size arrays. Created from lists or using functions: `zeros()`, `ones()`, `eye()`, `arange()`, `linspace()`, `random()`.

- **Array Attributes** – `shape`, `ndim`, `size`, `dtype`, `nbytes`. More memory efficient than Python lists.

- **Vectorized Operations** – Operations apply to entire arrays without loops. Much faster than Python loops (10-100x).

- **Indexing and Slicing** – Similar to Python lists but extended for multiple dimensions. Fancy indexing with integer arrays. Boolean indexing with masks.

- **Broadcasting** – Operations between arrays of different shapes. Enables efficient element-wise operations.

- **Aggregation Functions** – `sum()`, `mean()`, `median()`, `min()`, `max()`, `std()`, `var()`, `percentile()`. Axis parameter for row/column operations.

- **Linear Algebra** – Matrix multiplication (`@`), `dot()`, `inv()`, `det()`, `eig()`, `solve()`.

- **Practical Applications** – Sensor data analysis (anomaly detection, correlation, trend analysis). Image processing (brightness, grayscale, flip, rotate, blur). Financial analysis (returns, volatility, drawdown, VaR).

- **SOLID Principles Applied** – Single Responsibility (each function does one analysis), Open/Closed (pipeline stages can be added), Dependency Inversion (pipeline depends on function interfaces), Interface Segregation (clean function signatures).

- **Design Patterns Used** – Pipeline Pattern (analysis stages), Strategy Pattern (normalization strategies), Iterator Pattern (array indexing), Factory Pattern (array creation), Flyweight Pattern (memory-efficient storage).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking

- **📚 Series G Catalog:** Data Science & Visualization – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Pandas – Data Wrangling (Series G, Story 2)

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
| Series G | 5 | 1 | 4 | 20% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **41** | **11** | **79%** |

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

**Next Story:** Series G, Story 2: The 2026 Python Metromap: Pandas – Data Wrangling

---

## 📝 Your Invitation

You've mastered NumPy. Now build something with what you've learned:

1. **Build a data normalizer** – Create functions to normalize data using min-max, z-score, and robust scaling.

2. **Create a moving average crossover strategy** – Implement a trading strategy using NumPy for backtesting.

3. **Build an image processor** – Implement brightness, contrast, saturation adjustments using NumPy.

4. **Create a statistical summary tool** – Build a function that computes comprehensive statistics for any dataset.

5. **Build a signal processing pipeline** – Implement filters (low-pass, high-pass) using NumPy.

**You've mastered NumPy. Next stop: Pandas!**

---

*Found this helpful? Clap, comment, and share what you built with NumPy. Next stop: Pandas!* 🚇