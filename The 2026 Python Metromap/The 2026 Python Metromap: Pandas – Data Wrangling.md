# The 2026 Python Metromap: Pandas – Data Wrangling

## Series G: Data Science & Visualization | Story 2 of 5

![The 2026 Python Metromap/images/Pandas – Data Wrangling](images/Pandas – Data Wrangling.png)

## 📖 Introduction

**Welcome to the second stop on the Data Science & Visualization Line.**

You've mastered NumPy—efficient numerical arrays, vectorized operations, and linear algebra. You can process millions of numbers, but real-world data isn't just numbers. It's messy, structured data with missing values, different types, labels, and hierarchies. That's where Pandas comes in.

Pandas is the Swiss Army knife of data analysis in Python. Built on top of NumPy, it provides two powerful data structures: Series (1D labeled arrays) and DataFrame (2D labeled tables). Pandas excels at reading, cleaning, transforming, aggregating, and joining data from various sources—CSV, Excel, SQL databases, JSON, and more. It's the essential tool for any data professional.

This story—**The 2026 Python Metromap: Pandas – Data Wrangling**—is your guide to mastering Pandas. We'll create and manipulate Series and DataFrames, handle missing data, filter and sort, group and aggregate, merge and join datasets. We'll build a complete sales analysis pipeline that cleans messy CSV data, analyzes multi-year trends, and generates business insights. We'll implement a customer segmentation system and a time series analysis tool.

**Let's wrangle some data.**

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

- 🔢 **The 2026 Python Metromap: NumPy – Numerical Computing** – Processing millions of sensor readings; matrix operations; statistical aggregates.

- 🐼 **The 2026 Python Metromap: Pandas – Data Wrangling** – Multi-year sales analysis; CSV cleaning; regional and product aggregation. **⬅️ YOU ARE HERE**

- 📈 **The 2026 Python Metromap: Matplotlib – Basic Plotting** – Stock price line charts; sales bar charts; market share pie charts. 🔜 *Up Next*

- 🎨 **The 2026 Python Metromap: Seaborn – Statistical Visualization** – Customer segmentation heatmaps; age distribution plots; feature correlation pair plots.

- 📊 **The 2026 Python Metromap: Real-World EDA Project** – End-to-end exploratory data analysis on COVID-19 data, housing prices, or e-commerce sales.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🐼 Section 1: Pandas Basics – Series and DataFrames

Series and DataFrame are the core data structures in Pandas, providing labeled data for efficient manipulation.

**SOLID Principle Applied: Single Responsibility** – Series handles 1D labeled data, DataFrame handles 2D labeled data.

**Design Pattern: Adapter Pattern** – Pandas adapts various data sources to a unified DataFrame interface.

```python
"""
PANDAS BASICS: SERIES AND DATAFRAMES

This section covers the fundamentals of Pandas Series and DataFrames.

SOLID Principle: Single Responsibility
- Series handles 1D labeled data
- DataFrame handles 2D labeled data

Design Pattern: Adapter Pattern
- Pandas adapts various data sources to a unified DataFrame interface
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def demonstrate_series():
    """
    Demonstrates Pandas Series (1D labeled array).
    
    Series are like dictionaries with ordered keys.
    """
    print("=" * 60)
    print("SECTION 1A: PANDAS SERIES")
    print("=" * 60)
    
    # CREATING SERIES
    print("\n1. CREATING SERIES")
    print("-" * 40)
    
    # From list
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(f"  From list:\n{s1}")
    
    # With custom index
    s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print(f"\n  With custom index:\n{s2}")
    
    # From dictionary
    s3 = pd.Series({'a': 10, 'b': 20, 'c': 30})
    print(f"\n  From dictionary:\n{s3}")
    
    # With default values
    s4 = pd.Series(5, index=range(5))
    print(f"\n  Constant value:\n{s4}")
    
    # SERIES ATTRIBUTES
    print("\n2. SERIES ATTRIBUTES")
    print("-" * 40)
    
    s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    print(f"  Series:\n{s}")
    print(f"  Values: {s.values}")
    print(f"  Index: {s.index}")
    print(f"  Shape: {s.shape}")
    print(f"  Size: {s.size}")
    print(f"  Data type: {s.dtype}")
    
    # ACCESSING SERIES DATA
    print("\n3. ACCESSING DATA")
    print("-" * 40)
    
    print(f"  s['c']: {s['c']}")
    print(f"  s[2]: {s[2]}")
    print(f"  s[['a', 'c', 'e']]:\n{s[['a', 'c', 'e']]}")
    print(f"  s[1:4]:\n{s[1:4]}")
    
    # VECTORIZED OPERATIONS
    print("\n4. VECTORIZED OPERATIONS")
    print("-" * 40)
    
    s = pd.Series([1, 2, 3, 4, 5])
    print(f"  Original: {s.values}")
    print(f"  s * 2: {s * 2}")
    print(f"  s ** 2: {s ** 2}")
    print(f"  s > 3: {s > 3}")
    print(f"  s[s > 3]: {s[s > 3]}")
    
    # SERIES METHODS
    print("\n5. SERIES METHODS")
    print("-" * 40)
    
    s = pd.Series([3, 1, 4, 1, 5, 9, 2, 6, 5])
    print(f"  Series: {s.values}")
    print(f"  sum: {s.sum()}")
    print(f"  mean: {s.mean():.2f}")
    print(f"  min: {s.min()}, max: {s.max()}")
    print(f"  std: {s.std():.2f}")
    print(f"  sorted: {s.sort_values().values}")
    print(f"  unique: {s.unique()}")
    print(f"  value_counts:\n{s.value_counts()}")


def demonstrate_dataframe_creation():
    """
    Demonstrates creating DataFrames from various sources.
    
    DataFrame is a 2D labeled data structure (like a spreadsheet or SQL table).
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: CREATING DATAFRAMES")
    print("=" * 60)
    
    # FROM DICTIONARY OF LISTS
    print("\n1. FROM DICTIONARY OF LISTS")
    print("-" * 40)
    
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [28, 35, 22, 31, 29],
        'city': ['NYC', 'LA', 'Chicago', 'NYC', 'Boston'],
        'salary': [75000, 85000, 65000, 95000, 70000]
    }
    df = pd.DataFrame(data)
    print(f"  DataFrame:\n{df}")
    
    # FROM LIST OF DICTIONARIES
    print("\n2. FROM LIST OF DICTIONARIES")
    print("-" * 40)
    
    data = [
        {'name': 'Alice', 'age': 28, 'city': 'NYC'},
        {'name': 'Bob', 'age': 35, 'city': 'LA'},
        {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}
    ]
    df = pd.DataFrame(data)
    print(f"  DataFrame:\n{df}")
    
    # FROM NUMPY ARRAY
    print("\n3. FROM NUMPY ARRAY")
    print("-" * 40)
    
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
    print(f"  DataFrame:\n{df}")
    
    # WITH CUSTOM INDEX
    print("\n4. WITH CUSTOM INDEX")
    print("-" * 40)
    
    df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])
    print(f"  DataFrame with custom index:\n{df}")
    
    # FROM CSV (simulated)
    print("\n5. FROM CSV (simulated)")
    print("-" * 40)
    
    csv_data = """name,age,city,salary
Alice,28,NYC,75000
Bob,35,LA,85000
Charlie,22,Chicago,65000
Diana,31,NYC,95000
Eve,29,Boston,70000
"""
    
    from io import StringIO
    df = pd.read_csv(StringIO(csv_data))
    print(f"  DataFrame from CSV:\n{df}")
    
    # DATAFRAME ATTRIBUTES
    print("\n6. DATAFRAME ATTRIBUTES")
    print("-" * 40)
    
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {df.columns.tolist()}")
    print(f"  Index: {df.index.tolist()}")
    print(f"  Data types:\n{df.dtypes}")
    print(f"  Info:\n{df.info()}")


def demonstrate_dataframe_operations():
    """
    Demonstrates basic DataFrame operations: viewing, selecting, filtering.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: DATAFRAME OPERATIONS")
    print("=" * 60)
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'],
        'age': [28, 35, 22, 31, 29, 42, 26],
        'department': ['Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales', 'Engineering', 'Marketing'],
        'salary': [75000, 85000, 65000, 95000, 70000, 120000, 68000],
        'years_experience': [5, 12, 2, 8, 4, 20, 3]
    })
    
    print(f"  Original DataFrame ({df.shape[0]} rows, {df.shape[1]} columns):")
    print(df)
    
    # VIEWING DATA
    print("\n1. VIEWING DATA")
    print("-" * 40)
    
    print(f"  head() - first 3 rows:\n{df.head(3)}")
    print(f"\n  tail() - last 3 rows:\n{df.tail(3)}")
    print(f"\n  sample() - random 2 rows:\n{df.sample(2)}")
    print(f"\n  describe() - statistics:\n{df.describe()}")
    
    # SELECTING COLUMNS
    print("\n2. SELECTING COLUMNS")
    print("-" * 40)
    
    print(f"  df['name'] (Series):\n{df['name']}")
    print(f"\n  df[['name', 'salary']] (DataFrame):\n{df[['name', 'salary']]}")
    
    # SELECTING ROWS (loc - by label, iloc - by position)
    print("\n3. SELECTING ROWS")
    print("-" * 40)
    
    print(f"  df.loc[2] (by label):\n{df.loc[2]}")
    print(f"\n  df.iloc[2] (by position):\n{df.iloc[2]}")
    print(f"\n  df.iloc[1:4]:\n{df.iloc[1:4]}")
    
    # SELECTING ROWS AND COLUMNS
    print("\n4. SELECTING ROWS AND COLUMNS")
    print("-" * 40)
    
    print(f"  df.loc[2:4, ['name', 'salary']]:\n{df.loc[2:4, ['name', 'salary']]}")
    print(f"\n  df.iloc[1:4, 0:3]:\n{df.iloc[1:4, 0:3]}")
    
    # BOOLEAN INDEXING (Filtering)
    print("\n5. FILTERING (Boolean Indexing)")
    print("-" * 40)
    
    mask = df['salary'] > 70000
    print(f"  Salary > 70000:\n{df[mask]}")
    
    mask = (df['department'] == 'Engineering') & (df['salary'] > 70000)
    print(f"\n  Engineering with salary > 70000:\n{df[mask]}")
    
    # isin() for multiple values
    mask = df['department'].isin(['Engineering', 'Sales'])
    print(f"\n  Engineering or Sales:\n{df[mask]}")
    
    # query() method (SQL-like)
    print(f"\n  query('salary > 80000'):\n{df.query('salary > 80000')}")
    
    # SORTING
    print("\n6. SORTING")
    print("-" * 40)
    
    print(f"  Sort by salary (ascending):\n{df.sort_values('salary')}")
    print(f"\n  Sort by salary (descending):\n{df.sort_values('salary', ascending=False)}")
    print(f"\n  Sort by multiple columns:\n{df.sort_values(['department', 'salary'], ascending=[True, False])}")


if __name__ == "__main__":
    demonstrate_series()
    demonstrate_dataframe_creation()
    demonstrate_dataframe_operations()
```

---

## 🧹 Section 2: Data Cleaning – Handling Missing Values and Duplicates

Real-world data is messy. Pandas provides powerful tools for cleaning and preparing data.

**SOLID Principle Applied: Single Responsibility** – Each cleaning operation handles one type of issue.

**Design Pattern: Pipeline Pattern** – Cleaning operations can be chained together.

```python
"""
DATA CLEANING: HANDLING MISSING VALUES AND DUPLICATES

This section covers cleaning messy data with Pandas.

SOLID Principle: Single Responsibility
- Each cleaning operation handles one type of issue

Design Pattern: Pipeline Pattern
- Cleaning operations can be chained together
"""

import pandas as pd
import numpy as np


def demonstrate_missing_values():
    """
    Demonstrates handling missing values (NaN/None).
    
    Common strategies: drop, fill, interpolate.
    """
    print("=" * 60)
    print("SECTION 2A: HANDLING MISSING VALUES")
    print("=" * 60)
    
    # Create data with missing values
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [28, np.nan, 22, 31, np.nan],
        'salary': [75000, 85000, np.nan, 95000, 70000],
        'city': ['NYC', 'LA', np.nan, 'NYC', 'Boston'],
        'bonus': [5000, np.nan, 3000, np.nan, 4000]
    })
    
    print("\n1. DETECTING MISSING VALUES")
    print("-" * 40)
    
    print(f"  Original DataFrame:\n{df}")
    print(f"\n  isnull():\n{df.isnull()}")
    print(f"\n  isnull().sum():\n{df.isnull().sum()}")
    print(f"\n  Percentage missing:\n{df.isnull().sum() / len(df) * 100}")
    
    # DROPPING MISSING VALUES
    print("\n2. DROPPING MISSING VALUES")
    print("-" * 40)
    
    print(f"  dropna() - drop any row with NaN:\n{df.dropna()}")
    print(f"\n  dropna(how='all') - drop rows where all are NaN:\n{df.dropna(how='all')}")
    print(f"\n  dropna(subset=['age', 'salary']) - drop NaN in specific columns:\n{df.dropna(subset=['age', 'salary'])}")
    print(f"\n  dropna(axis=1) - drop columns with NaN:\n{df.dropna(axis=1)}")
    
    # FILLING MISSING VALUES
    print("\n3. FILLING MISSING VALUES")
    print("-" * 40)
    
    # Fill with constant
    df_filled = df.copy()
    df_filled['age'] = df_filled['age'].fillna(df_filled['age'].mean())
    print(f"  Fill age with mean: {df_filled['age'].values}")
    
    df_filled = df.copy()
    df_filled['salary'] = df_filled['salary'].fillna(df_filled['salary'].median())
    print(f"  Fill salary with median: {df_filled['salary'].values}")
    
    df_filled = df.copy()
    df_filled['city'] = df_filled['city'].fillna('Unknown')
    print(f"  Fill city with 'Unknown': {df_filled['city'].values}")
    
    # Forward fill / backward fill
    df_filled = df.copy()
    df_filled['bonus'] = df_filled['bonus'].fillna(method='ffill')
    print(f"  Forward fill bonus: {df_filled['bonus'].values}")
    
    # INTERPOLATION
    print("\n4. INTERPOLATION")
    print("-" * 40)
    
    df_interp = pd.DataFrame({
        'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'y': [10, np.nan, np.nan, 40, np.nan, 60, np.nan, np.nan, 90, 100]
    })
    print(f"  Original:\n{df_interp}")
    print(f"\n  Linear interpolation:\n{df_interp.interpolate()}")
    
    # REPLACING VALUES
    print("\n5. REPLACING VALUES")
    print("-" * 40)
    
    df_replace = pd.DataFrame({
        'status': ['active', 'inactive', 'active', 'unknown', 'inactive', 'active'],
        'rating': [5, 3, 4, -1, 2, -999]
    })
    print(f"  Original:\n{df_replace}")
    
    df_replace['status'] = df_replace['status'].replace('unknown', 'pending')
    print(f"\n  Replace 'unknown' with 'pending':\n{df_replace}")
    
    df_replace['rating'] = df_replace['rating'].replace([-1, -999], np.nan)
    print(f"\n  Replace -1 and -999 with NaN:\n{df_replace}")


def demonstrate_duplicates():
    """
    Demonstrates handling duplicate data.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: HANDLING DUPLICATES")
    print("=" * 60)
    
    # Create data with duplicates
    df = pd.DataFrame({
        'id': [1, 2, 3, 1, 2, 4, 5, 3],
        'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Diana', 'Eve', 'Charlie'],
        'age': [28, 35, 22, 28, 35, 31, 29, 22],
        'city': ['NYC', 'LA', 'Chicago', 'NYC', 'LA', 'NYC', 'Boston', 'Chicago']
    })
    
    print("\n1. DETECTING DUPLICATES")
    print("-" * 40)
    
    print(f"  Original DataFrame:\n{df}")
    print(f"\n  duplicated():\n{df.duplicated()}")
    print(f"\n  duplicated().sum(): {df.duplicated().sum()}")
    
    # Duplicates based on subset
    print(f"\n  duplicated(subset=['name']):\n{df.duplicated(subset=['name'])}")
    print(f"\n  duplicated(subset=['name', 'age']):\n{df.duplicated(subset=['name', 'age'])}")
    
    # REMOVING DUPLICATES
    print("\n2. REMOVING DUPLICATES")
    print("-" * 40)
    
    print(f"  drop_duplicates():\n{df.drop_duplicates()}")
    print(f"\n  drop_duplicates(keep='first'):\n{df.drop_duplicates(keep='first')}")
    print(f"\n  drop_duplicates(keep='last'):\n{df.drop_duplicates(keep='last')}")
    print(f"\n  drop_duplicates(subset=['name']):\n{df.drop_duplicates(subset=['name'])}")
    
    # KEEPING FIRST AND LAST
    print("\n3. KEEPING FIRST AND LAST OCCURRENCES")
    print("-" * 40)
    
    print(f"  Original: {df['name'].values}")
    print(f"  keep='first': {df.drop_duplicates(subset=['name'], keep='first')['name'].values}")
    print(f"  keep='last': {df.drop_duplicates(subset=['name'], keep='last')['name'].values}")


def demonstrate_data_transformation():
    """
    Demonstrates data transformation: applying functions, mapping, and type conversion.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: DATA TRANSFORMATION")
    print("=" * 60)
    
    # Create sample data
    df = pd.DataFrame({
        'name': ['alice', 'BOB', 'Charlie', 'diana', 'EVE'],
        'salary': [75000, 85000, 65000, 95000, 70000],
        'bonus': [5000, 6000, 4500, 8000, 5500],
        'join_date': ['2020-01-15', '2019-06-20', '2021-03-10', '2018-11-05', '2022-02-28']
    })
    
    print("\n1. APPLYING FUNCTIONS")
    print("-" * 40)
    
    print(f"  Original:\n{df}")
    
    # String operations
    df['name'] = df['name'].str.capitalize()
    print(f"\n  Capitalized names:\n{df}")
    
    # Apply custom function
    df['total_comp'] = df['salary'] + df['bonus']
    print(f"\n  Added total_comp:\n{df}")
    
    # Apply with lambda
    df['salary_level'] = df['salary'].apply(lambda x: 'High' if x > 80000 else 'Medium' if x > 70000 else 'Low')
    print(f"\n  Salary level:\n{df[['name', 'salary', 'salary_level']]}")
    
    # map() for value mapping
    print("\n2. VALUE MAPPING (map())")
    print("-" * 40)
    
    df['gender'] = pd.Series(['F', 'M', 'M', 'F', 'F'])
    gender_map = {'F': 'Female', 'M': 'Male'}
    df['gender_full'] = df['gender'].map(gender_map)
    print(f"  Mapped gender:\n{df[['name', 'gender', 'gender_full']]}")
    
    # TYPE CONVERSION
    print("\n3. TYPE CONVERSION")
    print("-" * 40)
    
    print(f"  join_date type: {df['join_date'].dtype}")
    df['join_date'] = pd.to_datetime(df['join_date'])
    print(f"  After conversion: {df['join_date'].dtype}")
    
    # Extract date components
    df['join_year'] = df['join_date'].dt.year
    df['join_month'] = df['join_date'].dt.month
    print(f"\n  Date components:\n{df[['name', 'join_date', 'join_year', 'join_month']]}")
    
    # RENAMING COLUMNS
    print("\n4. RENAMING COLUMNS")
    print("-" * 40)
    
    df_renamed = df.rename(columns={
        'name': 'employee_name',
        'salary': 'base_salary',
        'bonus': 'annual_bonus'
    })
    print(f"  Renamed columns:\n{df_renamed.columns.tolist()}")
    
    # ADDING AND DROPPING COLUMNS
    print("\n5. ADDING AND DROPPING COLUMNS")
    print("-" * 40)
    
    df['years_at_company'] = 2024 - df['join_year']
    print(f"  Added years_at_company:\n{df[['name', 'join_year', 'years_at_company']]}")
    
    df_dropped = df.drop(['gender', 'gender_full'], axis=1)
    print(f"\n  Dropped columns: {df.columns.tolist()} → {df_dropped.columns.tolist()}")


def build_data_cleaning_pipeline():
    """
    Builds a complete data cleaning pipeline.
    
    Design Pattern: Pipeline Pattern - Chain cleaning operations
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: COMPLETE DATA CLEANING PIPELINE")
    print("=" * 60)
    
    # Create messy data
    messy_data = pd.DataFrame({
        'customer_id': [1, 2, 3, 1, 4, 5, 2, 6],
        'name': ['Alice', 'BOB', 'Charlie', 'Alice', '  Diana  ', 'eve', 'Bob', 'Frank'],
        'email': ['alice@example.com', 'bob@example', 'charlie@example.com', 
                  'alice@example.com', 'diana@example.com', 'eve@example.com', 
                  'bob@example.com', 'frank@example.com'],
        'age': [28, -5, 22, 28, 31, 29, 35, 250],
        'salary': [75000, 85000, None, 75000, 95000, 70000, 85000, 120000],
        'join_date': ['2020-01-15', 'invalid', '2021-03-10', '2020-01-15', 
                      '2018-11-05', '2022-02-28', '2019-06-20', '2023-01-10']
    })
    
    print("\n1. RAW MESSY DATA")
    print("-" * 40)
    print(messy_data)
    
    class DataCleaner:
        """Pipeline for cleaning messy data."""
        
        def __init__(self, df):
            self.df = df.copy()
            self.cleaning_log = []
        
        def remove_duplicates(self, subset=None):
            """Remove duplicate rows."""
            before = len(self.df)
            self.df = self.df.drop_duplicates(subset=subset)
            after = len(self.df)
            self.cleaning_log.append(f"Removed {before - after} duplicate rows")
            return self
        
        def clean_strings(self, columns):
            """Strip whitespace and standardize case."""
            for col in columns:
                if col in self.df.columns:
                    self.df[col] = self.df[col].str.strip()
                    if col == 'name':
                        self.df[col] = self.df[col].str.capitalize()
                    elif col == 'email':
                        self.df[col] = self.df[col].str.lower()
            self.cleaning_log.append(f"Cleaned string columns: {columns}")
            return self
        
        def fix_outliers(self, column, min_val, max_val, replacement='median'):
            """Fix outliers outside range."""
            mask = (self.df[column] < min_val) | (self.df[column] > max_val)
            outlier_count = mask.sum()
            
            if outlier_count > 0:
                if replacement == 'median':
                    replacement_value = self.df[column].median()
                elif replacement == 'mean':
                    replacement_value = self.df[column].mean()
                else:
                    replacement_value = replacement
                
                self.df.loc[mask, column] = replacement_value
                self.cleaning_log.append(f"Fixed {outlier_count} outliers in {column}")
            return self
        
        def handle_missing(self, column, strategy='median'):
            """Handle missing values."""
            missing_count = self.df[column].isna().sum()
            
            if missing_count > 0:
                if strategy == 'median':
                    fill_value = self.df[column].median()
                elif strategy == 'mean':
                    fill_value = self.df[column].mean()
                elif strategy == 'mode':
                    fill_value = self.df[column].mode()[0] if not self.df[column].mode().empty else None
                else:
                    fill_value = strategy
                
                self.df[column] = self.df[column].fillna(fill_value)
                self.cleaning_log.append(f"Filled {missing_count} missing values in {column}")
            return self
        
        def fix_dates(self, column, format='%Y-%m-%d'):
            """Fix invalid dates."""
            original = self.df[column].copy()
            self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
            invalid_count = original[~original.isna()].count() - self.df[column].notna().sum()
            if invalid_count > 0:
                self.cleaning_log.append(f"Fixed {invalid_count} invalid dates in {column}")
            return self
        
        def get_result(self):
            """Get cleaned DataFrame and cleaning log."""
            return self.df, self.cleaning_log
    
    # Run cleaning pipeline
    cleaner = DataCleaner(messy_data)
    cleaner.remove_duplicates(subset=['customer_id'])
    cleaner.clean_strings(['name', 'email'])
    cleaner.fix_outliers('age', min_val=0, max_val=120, replacement='median')
    cleaner.handle_missing('salary', strategy='median')
    cleaner.fix_dates('join_date')
    
    cleaned_df, log = cleaner.get_result()
    
    print("\n2. CLEANING LOG")
    print("-" * 40)
    for entry in log:
        print(f"  ✓ {entry}")
    
    print("\n3. CLEANED DATA")
    print("-" * 40)
    print(cleaned_df)
    
    print("\n4. DATA QUALITY REPORT")
    print("-" * 40)
    print(f"  Shape: {cleaned_df.shape}")
    print(f"  Missing values: {cleaned_df.isnull().sum().sum()}")
    print(f"  Duplicates: {cleaned_df.duplicated().sum()}")
    print(f"\n  Column info:")
    for col in cleaned_df.columns:
        print(f"    {col}: {cleaned_df[col].dtype}, unique: {cleaned_df[col].nunique()}")


if __name__ == "__main__":
    demonstrate_missing_values()
    demonstrate_duplicates()
    demonstrate_data_transformation()
    build_data_cleaning_pipeline()
```

---

## 📊 Section 3: Data Aggregation and Grouping

Grouping and aggregation are essential for summarizing data and extracting insights.

**SOLID Principle Applied: Single Responsibility** – Each aggregation operation has one purpose.

**Design Pattern: Strategy Pattern** – Different aggregation strategies (sum, mean, count, etc.).

```python
"""
DATA AGGREGATION AND GROUPING

This section covers grouping data and performing aggregations.

SOLID Principle: Single Responsibility
- Each aggregation operation has one purpose

Design Pattern: Strategy Pattern
- Different aggregation strategies (sum, mean, count, etc.)
"""

import pandas as pd
import numpy as np


def demonstrate_groupby_basics():
    """
    Demonstrates groupby operations for splitting data into groups.
    
    GroupBy follows the split-apply-combine pattern.
    """
    print("=" * 60)
    print("SECTION 3A: GROUPBY BASICS")
    print("=" * 60)
    
    # Create sample sales data
    sales_data = pd.DataFrame({
        'region': ['North', 'South', 'North', 'East', 'West', 'North', 'South', 'East'],
        'product': ['A', 'A', 'B', 'A', 'B', 'C', 'B', 'C'],
        'sales': [100, 150, 200, 120, 180, 90, 210, 130],
        'quantity': [5, 8, 10, 6, 9, 4, 11, 7],
        'profit': [20, 30, 40, 24, 36, 18, 42, 26]
    })
    
    print("\n1. SALES DATA")
    print("-" * 40)
    print(sales_data)
    
    # BASIC GROUPBY
    print("\n2. GROUP BY SINGLE COLUMN")
    print("-" * 40)
    
    # Group by region
    grouped = sales_data.groupby('region')
    print(f"  Groups: {grouped.groups.keys()}")
    
    print(f"\n  Region sales sum:\n{grouped['sales'].sum()}")
    print(f"\n  Region sales mean:\n{grouped['sales'].mean()}")
    print(f"\n  Region sales count:\n{grouped['sales'].count()}")
    
    # MULTIPLE AGGREGATIONS
    print("\n3. MULTIPLE AGGREGATIONS")
    print("-" * 40)
    
    # agg() with multiple functions
    result = grouped['sales'].agg(['sum', 'mean', 'min', 'max', 'std'])
    print(f"  Sales statistics by region:\n{result}")
    
    # Different aggregations for different columns
    result = grouped.agg({
        'sales': ['sum', 'mean'],
        'quantity': 'sum',
        'profit': 'mean'
    })
    print(f"\n  Multiple aggregations:\n{result}")
    
    # GROUP BY MULTIPLE COLUMNS
    print("\n4. GROUP BY MULTIPLE COLUMNS")
    print("-" * 40)
    
    grouped = sales_data.groupby(['region', 'product'])
    print(f"  Group by region and product:\n{grouped['sales'].sum()}")
    
    # Unstack to create pivot table
    pivot = grouped['sales'].sum().unstack()
    print(f"\n  Pivot table (unstacked):\n{pivot}")
    
    # CUSTOM AGGREGATION FUNCTIONS
    print("\n5. CUSTOM AGGREGATION FUNCTIONS")
    print("-" * 40)
    
    def range_func(x):
        return x.max() - x.min()
    
    def iqr_func(x):
        return x.quantile(0.75) - x.quantile(0.25)
    
    result = sales_data.groupby('region')['sales'].agg([
        ('sum', 'sum'),
        ('mean', 'mean'),
        ('range', range_func),
        ('iqr', iqr_func)
    ])
    print(f"  Custom aggregations:\n{result}")


def demonstrate_advanced_aggregation():
    """
    Demonstrates advanced aggregation techniques: transform, filter, and apply.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: ADVANCED AGGREGATION")
    print("=" * 60)
    
    # Create sample data
    df = pd.DataFrame({
        'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'value': [10, 15, 20, 25, 30, 35, 40, 45, 50],
        'score': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    })
    
    print("\n1. ORIGINAL DATA")
    print("-" * 40)
    print(df)
    
    # TRANSFORM (broadcast aggregated value back to original shape)
    print("\n2. TRANSFORM - Add group means to each row")
    print("-" * 40)
    
    df['group_mean'] = df.groupby('group')['value'].transform('mean')
    df['group_std'] = df.groupby('group')['value'].transform('std')
    print(f"  With group statistics:\n{df}")
    
    # Normalize within group
    df['normalized'] = (df['value'] - df['group_mean']) / df['group_std']
    print(f"\n  Normalized values:\n{df[['group', 'value', 'normalized']]}")
    
    # FILTER (keep groups that meet condition)
    print("\n3. FILTER - Keep groups with mean > 30")
    print("-" * 40)
    
    filtered = df.groupby('group').filter(lambda x: x['value'].mean() > 30)
    print(f"  Filtered groups:\n{filtered}")
    
    # APPLY (custom function on each group)
    print("\n4. APPLY - Custom function on each group")
    print("-" * 40)
    
    def group_summary(group):
        return pd.Series({
            'count': len(group),
            'sum': group['value'].sum(),
            'mean': group['value'].mean(),
            'range': group['value'].max() - group['value'].min()
        })
    
    summary = df.groupby('group').apply(group_summary)
    print(f"  Group summaries:\n{summary}")
    
    # WINDOW OPERATIONS (rolling, expanding)
    print("\n5. WINDOW OPERATIONS")
    print("-" * 40)
    
    # Create time series data
    ts = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30, freq='D'),
        'value': np.random.randn(30).cumsum() + 100
    })
    
    ts['rolling_7d'] = ts['value'].rolling(window=7).mean()
    ts['expanding_mean'] = ts['value'].expanding().mean()
    
    print(f"  Rolling 7-day average (last 5 rows):\n{ts.tail(5)}")


def build_sales_analysis_system():
    """
    Builds a complete sales analysis system with grouping and aggregation.
    
    Design Pattern: Pipeline Pattern - Analysis pipeline
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: SALES ANALYSIS SYSTEM")
    print("=" * 60)
    
    # Generate sample sales data
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
    n_records = 10000
    
    sales_data = pd.DataFrame({
        'date': np.random.choice(dates, n_records),
        'product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Desk'], n_records),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
        'quantity': np.random.randint(1, 10, n_records),
        'price': np.random.choice([999, 29, 89, 299, 399], n_records)
    })
    sales_data['revenue'] = sales_data['quantity'] * sales_data['price']
    sales_data['month'] = sales_data['date'].dt.month
    sales_data['quarter'] = sales_data['date'].dt.quarter
    
    print("\n1. SALES DATA OVERVIEW")
    print("-" * 40)
    print(f"  Records: {len(sales_data):,}")
    print(f"  Date range: {sales_data['date'].min().date()} to {sales_data['date'].max().date()}")
    print(f"  Total revenue: ${sales_data['revenue'].sum():,.2f}")
    
    # MONTHLY SALES
    print("\n2. MONTHLY SALES SUMMARY")
    print("-" * 40)
    
    monthly = sales_data.groupby('month').agg({
        'revenue': ['sum', 'mean', 'count'],
        'quantity': 'sum'
    }).round(2)
    print(f"  Monthly summary:\n{monthly}")
    
    # PRODUCT ANALYSIS
    print("\n3. PRODUCT PERFORMANCE")
    print("-" * 40)
    
    product_stats = sales_data.groupby('product').agg({
        'revenue': ['sum', 'mean'],
        'quantity': 'sum',
        'price': 'first'
    }).round(2)
    product_stats.columns = ['total_revenue', 'avg_revenue', 'total_quantity', 'unit_price']
    product_stats = product_stats.sort_values('total_revenue', ascending=False)
    print(f"  Product stats:\n{product_stats}")
    
    # REGION ANALYSIS
    print("\n4. REGION PERFORMANCE")
    print("-" * 40)
    
    region_stats = sales_data.groupby('region').agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).round(2)
    region_stats['revenue_percent'] = (region_stats['revenue'] / region_stats['revenue'].sum() * 100).round(1)
    region_stats = region_stats.sort_values('revenue', ascending=False)
    print(f"  Region stats:\n{region_stats}")
    
    # QUARTERLY PRODUCT ANALYSIS
    print("\n5. QUARTERLY PRODUCT ANALYSIS")
    print("-" * 40)
    
    quarterly_product = sales_data.groupby(['quarter', 'product'])['revenue'].sum().unstack()
    print(f"  Quarterly product revenue:\n{quarterly_product}")
    
    # BEST-SELLING PRODUCTS BY REGION
    print("\n6. BEST-SELLING PRODUCTS BY REGION")
    print("-" * 40)
    
    top_products = sales_data.groupby(['region', 'product'])['quantity'].sum().groupby('region').nlargest(1)
    print(f"  Top product by region:\n{top_products}")
    
    # CUSTOMER SEGMENTATION (based on purchase frequency)
    print("\n7. CUSTOMER SEGMENTATION")
    print("-" * 40)
    
    # Simulate customer purchases
    customers = pd.DataFrame({
        'customer_id': range(1, 1001),
        'purchase_count': np.random.poisson(5, 1000),
        'total_spent': np.random.exponential(500, 1000)
    })
    
    # Segment customers
    customers['segment'] = pd.cut(customers['total_spent'], 
                                   bins=[0, 100, 500, 1000, float('inf')],
                                   labels=['Bronze', 'Silver', 'Gold', 'Platinum'])
    
    segment_stats = customers.groupby('segment').agg({
        'customer_id': 'count',
        'total_spent': ['sum', 'mean']
    }).round(2)
    print(f"  Customer segments:\n{segment_stats}")
    
    # PIVOT TABLE
    print("\n8. PIVOT TABLE - Region × Product Revenue")
    print("-" * 40)
    
    pivot = pd.pivot_table(sales_data, 
                           values='revenue', 
                           index='region', 
                           columns='product', 
                           aggfunc='sum',
                           fill_value=0)
    print(f"  Pivot table:\n{pivot}")
    
    # CROSS TABULATION
    print("\n9. CROSS TABULATION - Region × Product Frequency")
    print("-" * 40)
    
    crosstab = pd.crosstab(sales_data['region'], sales_data['product'], normalize='index') * 100
    print(f"  Region product distribution (%):\n{crosstab.round(1)}")


if __name__ == "__main__":
    demonstrate_groupby_basics()
    demonstrate_advanced_aggregation()
    build_sales_analysis_system()
```

---

## 🔗 Section 4: Merging, Joining, and Concatenating Data

Combining multiple data sources is a common task in data analysis. Pandas provides powerful tools for merging, joining, and concatenating DataFrames.

**SOLID Principle Applied: Single Responsibility** – Each join operation has a specific purpose.

**Design Pattern: Adapter Pattern** – Merging adapts multiple data sources into one.

```python
"""
MERGING, JOINING, AND CONCATENATING DATA

This section covers combining multiple DataFrames.

SOLID Principle: Single Responsibility
- Each join operation has a specific purpose

Design Pattern: Adapter Pattern
- Merging adapts multiple data sources into one
"""

import pandas as pd
import numpy as np


def demonstrate_concatenation():
    """
    Demonstrates concatenating DataFrames vertically or horizontally.
    """
    print("=" * 60)
    print("SECTION 4A: CONCATENATION (CONCAT)")
    print("=" * 60)
    
    # Create sample DataFrames
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [28, 35, 22]
    })
    
    df2 = pd.DataFrame({
        'id': [4, 5, 6],
        'name': ['Diana', 'Eve', 'Frank'],
        'age': [31, 29, 42]
    })
    
    df3 = pd.DataFrame({
        'id': [7, 8, 9],
        'name': ['Grace', 'Henry', 'Ivy'],
        'age': [26, 38, 24]
    })
    
    print("\n1. VERTICAL CONCATENATION (stack rows)")
    print("-" * 40)
    
    print(f"  df1:\n{df1}")
    print(f"\n  df2:\n{df2}")
    
    combined = pd.concat([df1, df2], ignore_index=True)
    print(f"\n  Concatenated:\n{combined}")
    
    # Multiple DataFrames
    all_data = pd.concat([df1, df2, df3], ignore_index=True)
    print(f"\n  All three combined: {len(all_data)} rows")
    
    # HORIZONTAL CONCATENATION
    print("\n2. HORIZONTAL CONCATENATION (side by side)")
    print("-" * 40)
    
    df_contacts = pd.DataFrame({
        'id': [1, 2, 3],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
        'phone': ['555-0101', '555-0102', '555-0103']
    })
    
    combined_h = pd.concat([df1, df_contacts], axis=1)
    print(f"  Horizontal concatenation:\n{combined_h}")
    
    # WITH DIFFERENT INDEXES
    print("\n3. CONCATENATION WITH DIFFERENT INDEXES")
    print("-" * 40)
    
    df_a = pd.DataFrame({'value': [1, 2, 3]}, index=['a', 'b', 'c'])
    df_b = pd.DataFrame({'value': [4, 5, 6]}, index=['d', 'e', 'f'])
    df_c = pd.DataFrame({'other': [7, 8, 9]}, index=['a', 'b', 'g'])
    
    print(f"  df_a:\n{df_a}")
    print(f"\n  df_b:\n{df_b}")
    print(f"\n  df_c:\n{df_c}")
    
    # Outer join (union of indexes)
    outer = pd.concat([df_a, df_b, df_c], axis=0)
    print(f"\n  Outer join (axis=0):\n{outer}")
    
    # Inner join (intersection of indexes)
    inner = pd.concat([df_a, df_c], axis=1, join='inner')
    print(f"\n  Inner join (axis=1):\n{inner}")


def demonstrate_merging():
    """
    Demonstrates merging DataFrames (SQL-style joins).
    
    Merge types: inner, outer, left, right.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: MERGING (SQL-Style Joins)")
    print("=" * 60)
    
    # Create customer and order data
    customers = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'city': ['NYC', 'LA', 'Chicago', 'NYC', 'Boston']
    })
    
    orders = pd.DataFrame({
        'order_id': [101, 102, 103, 104, 105, 106],
        'customer_id': [1, 2, 1, 3, 4, 6],
        'amount': [250, 150, 300, 100, 450, 200],
        'date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20']
    })
    
    print("\n1. CUSTOMERS AND ORDERS")
    print("-" * 40)
    print(f"  Customers:\n{customers}")
    print(f"\n  Orders:\n{orders}")
    
    # INNER JOIN (only matching keys)
    print("\n2. INNER JOIN (only customers with orders)")
    print("-" * 40)
    
    inner = pd.merge(customers, orders, on='customer_id', how='inner')
    print(f"  Inner join:\n{inner}")
    
    # LEFT JOIN (all customers, matching orders)
    print("\n3. LEFT JOIN (all customers, orders if exist)")
    print("-" * 40)
    
    left = pd.merge(customers, orders, on='customer_id', how='left')
    print(f"  Left join:\n{left}")
    
    # RIGHT JOIN (all orders, matching customers)
    print("\n4. RIGHT JOIN (all orders, customers if exist)")
    print("-" * 40)
    
    right = pd.merge(customers, orders, on='customer_id', how='right')
    print(f"  Right join:\n{right}")
    
    # OUTER JOIN (all customers and all orders)
    print("\n5. OUTER JOIN (all customers and all orders)")
    print("-" * 40)
    
    outer = pd.merge(customers, orders, on='customer_id', how='outer')
    print(f"  Outer join:\n{outer}")
    
    # MERGING ON MULTIPLE KEYS
    print("\n6. MERGING ON MULTIPLE KEYS")
    print("-" * 40)
    
    inventory = pd.DataFrame({
        'product_id': [1, 1, 2, 2, 3],
        'warehouse': ['A', 'B', 'A', 'B', 'A'],
        'quantity': [100, 50, 200, 75, 150]
    })
    
    sales = pd.DataFrame({
        'product_id': [1, 1, 2, 3],
        'warehouse': ['A', 'B', 'A', 'A'],
        'sold': [30, 20, 50, 25]
    })
    
    print(f"  Inventory:\n{inventory}")
    print(f"\n  Sales:\n{sales}")
    
    merged = pd.merge(inventory, sales, on=['product_id', 'warehouse'], how='outer')
    print(f"\n  Merge on product_id and warehouse:\n{merged}")


def demonstrate_joining():
    """
    Demonstrates joining DataFrames using index.
    
    Join is similar to merge but uses indexes instead of columns.
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: JOINING (Using Index)")
    print("=" * 60)
    
    # Create DataFrames with meaningful indexes
    employees = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'department': ['Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales']
    }, index=[101, 102, 103, 104, 105])
    
    salaries = pd.DataFrame({
        'salary': [75000, 85000, 65000, 95000, 70000],
        'bonus': [5000, 6000, 4500, 8000, 5500]
    }, index=[101, 102, 103, 104, 105])
    
    print("\n1. EMPLOYEE DATA")
    print("-" * 40)
    print(f"  Employees:\n{employees}")
    print(f"\n  Salaries:\n{salaries}")
    
    # JOIN ON INDEX
    print("\n2. JOIN ON INDEX")
    print("-" * 40)
    
    joined = employees.join(salaries)
    print(f"  Join on index:\n{joined}")
    
    # DIFFERENT INDEXES
    print("\n3. JOIN WITH DIFFERENT INDEXES")
    print("-" * 40)
    
    performance = pd.DataFrame({
        'rating': [4.5, 4.2, 4.8, 4.1, 4.6]
    }, index=[101, 102, 104, 105, 106])
    
    print(f"  Performance:\n{performance}")
    
    left_join = employees.join(performance, how='left')
    right_join = employees.join(performance, how='right')
    outer_join = employees.join(performance, how='outer')
    
    print(f"\n  Left join:\n{left_join}")
    print(f"\n  Right join:\n{right_join}")
    print(f"\n  Outer join:\n{outer_join}")


def build_complete_data_integration():
    """
    Builds a complete data integration example combining multiple sources.
    
    Design Pattern: Pipeline Pattern - Data integration pipeline
    """
    print("\n" + "=" * 60)
    print("SECTION 4D: COMPLETE DATA INTEGRATION")
    print("=" * 60)
    
    # Source 1: Customer data (CSV)
    customers = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5, 6],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
        'email': ['alice@ex.com', 'bob@ex.com', 'charlie@ex.com', 
                  'diana@ex.com', 'eve@ex.com', 'frank@ex.com'],
        'join_date': ['2020-01-15', '2019-06-20', '2021-03-10', 
                      '2018-11-05', '2022-02-28', '2023-01-10']
    })
    
    # Source 2: Order data (Database)
    orders = pd.DataFrame({
        'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
        'customer_id': [1, 2, 1, 3, 4, 2, 5, 6],
        'order_date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18',
                       '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22'],
        'total': [250.00, 150.00, 300.00, 100.00, 450.00, 200.00, 350.00, 180.00]
    })
    
    # Source 3: Product data (API)
    order_items = pd.DataFrame({
        'order_id': [1001, 1001, 1002, 1003, 1003, 1004, 1005, 1006, 1007, 1008],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Mouse', 'Desk', 
                    'Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'quantity': [1, 2, 1, 1, 1, 1, 1, 3, 2, 1],
        'unit_price': [999.99, 29.99, 89.99, 299.99, 29.99, 399.99, 
                       999.99, 29.99, 89.99, 299.99]
    })
    
    # Source 4: Customer segmentation (Excel)
    segments = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5, 6],
        'segment': ['Gold', 'Silver', 'Bronze', 'Platinum', 'Silver', 'Bronze'],
        'tier': [1, 2, 3, 0, 2, 3]
    })
    
    print("\n1. DATA SOURCES")
    print("-" * 40)
    print(f"  Customers: {len(customers)} records")
    print(f"  Orders: {len(orders)} records")
    print(f"  Order Items: {len(order_items)} records")
    print(f"  Segments: {len(segments)} records")
    
    # Step 1: Merge orders with customers
    print("\n2. MERGING CUSTOMERS AND ORDERS")
    print("-" * 40)
    
    customer_orders = pd.merge(orders, customers, on='customer_id', how='left')
    print(f"  Customer-Orders: {len(customer_orders)} records")
    
    # Step 2: Merge with order items
    print("\n3. ADDING ORDER ITEMS")
    print("-" * 40)
    
    full_orders = pd.merge(customer_orders, order_items, on='order_id', how='left')
    full_orders['line_total'] = full_orders['quantity'] * full_orders['unit_price']
    print(f"  Full orders: {len(full_orders)} line items")
    
    # Step 3: Add customer segments
    print("\n4. ADDING CUSTOMER SEGMENTS")
    print("-" * 40)
    
    enriched = pd.merge(full_orders, segments, on='customer_id', how='left')
    print(f"  Enriched data: {len(enriched)} records")
    
    # Step 4: Calculate aggregations
    print("\n5. AGGREGATED INSIGHTS")
    print("-" * 40)
    
    # Customer lifetime value by segment
    clv = enriched.groupby('segment').agg({
        'customer_id': 'nunique',
        'line_total': ['sum', 'mean']
    }).round(2)
    print(f"  Customer Lifetime Value by Segment:\n{clv}")
    
    # Product performance by region (using customer city as region proxy)
    # Add city from customers
    enriched = pd.merge(enriched, customers[['customer_id', 'email']], on='customer_id', how='left')
    
    # Top products
    top_products = enriched.groupby('product').agg({
        'quantity': 'sum',
        'line_total': 'sum'
    }).sort_values('line_total', ascending=False)
    print(f"\n  Top Products:\n{top_products}")
    
    # Monthly revenue trend
    enriched['order_date'] = pd.to_datetime(enriched['order_date'])
    enriched['month'] = enriched['order_date'].dt.month
    monthly_revenue = enriched.groupby('month')['line_total'].sum()
    print(f"\n  Monthly Revenue:\n{monthly_revenue}")
    
    # Final integrated dataset
    print("\n6. FINAL INTEGRATED DATASET (Sample)")
    print("-" * 40)
    
    final_columns = ['order_id', 'customer_id', 'name', 'segment', 'order_date', 
                     'product', 'quantity', 'unit_price', 'line_total']
    print(enriched[final_columns].head(10))


if __name__ == "__main__":
    demonstrate_concatenation()
    demonstrate_merging()
    demonstrate_joining()
    build_complete_data_integration()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Series** – 1D labeled array. Created from lists, dicts, or scalars. Index labels for meaningful access.

- **DataFrame** – 2D labeled data structure (like spreadsheet). Columns can have different types. Created from dicts, lists, NumPy arrays, CSV, Excel, SQL.

- **Data Inspection** – `head()`, `tail()`, `sample()`, `info()`, `describe()`, `shape`, `columns`, `dtypes`.

- **Selecting Data** – `df['column']` (Series), `df[['col1', 'col2']]` (DataFrame), `df.loc[]` (label-based), `df.iloc[]` (position-based), boolean indexing.

- **Handling Missing Values** – `isnull()`, `dropna()`, `fillna()`, `interpolate()`. Replace with mean, median, mode, forward fill.

- **Duplicates** – `duplicated()`, `drop_duplicates()`. Keep first, last, or none.

- **Data Transformation** – `apply()`, `map()`, `replace()`, `astype()`, string methods (`str.upper()`, `str.strip()`).

- **GroupBy** – Split-apply-combine. `groupby()`, `agg()`, `transform()`, `filter()`, `apply()`. Multiple aggregation functions.

- **Pivot Tables** – `pivot_table()` for cross-tabulation. `crosstab()` for frequency tables.

- **Combining Data** – `concat()` (vertical/horizontal), `merge()` (SQL-style joins: inner, outer, left, right), `join()` (index-based).

- **SOLID Principles Applied** – Single Responsibility (each operation does one thing), Open/Closed (new aggregations can be added), Dependency Inversion (pipeline depends on DataFrame interface), Interface Segregation (clean method interfaces).

- **Design Patterns Used** – Adapter Pattern (data source adaptation), Pipeline Pattern (cleaning/analysis pipelines), Strategy Pattern (aggregation strategies), Factory Pattern (DataFrame creation), Iterator Pattern (groupby iteration).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: NumPy – Numerical Computing

- **📚 Series G Catalog:** Data Science & Visualization – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Matplotlib – Basic Plotting (Series G, Story 3)

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
| Series G | 5 | 2 | 3 | 40% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **42** | **10** | **81%** |

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

**Next Story:** Series G, Story 3: The 2026 Python Metromap: Matplotlib – Basic Plotting

---

## 📝 Your Invitation

You've mastered Pandas. Now build something with what you've learned:

1. **Build a data cleaning pipeline** – Create a reusable pipeline that handles missing values, outliers, duplicates, and type conversion.

2. **Create a sales dashboard** – Aggregate sales data by region, product, time period. Generate summary statistics.

3. **Build a customer segmentation system** – Use groupby and aggregation to segment customers by purchase behavior.

4. **Create a time series analysis tool** – Load time series data, resample, calculate rolling statistics.

5. **Build a data integration pipeline** – Merge data from multiple sources (CSV, Excel, API) into a unified dataset.

**You've mastered Pandas. Next stop: Matplotlib!**

---

*Found this helpful? Clap, comment, and share what you built with Pandas. Next stop: Matplotlib!* 🚇