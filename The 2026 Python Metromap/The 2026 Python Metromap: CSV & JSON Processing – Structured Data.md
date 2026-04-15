# The 2026 Python Metromap: CSV & JSON Processing – Structured Data

## Series E: File & Data Handling Line | Story 2 of 5

![The 2026 Python Metromap/images/CSV and JSON Processing – Structured Data](images/CSV and JSON Processing – Structured Data.png)

## 📖 Introduction

**Welcome to the second stop on the File & Data Handling Line.**

You've mastered basic file I/O—reading and writing text files, processing logs, and managing configurations. But most real-world data isn't stored in simple text files. It's structured: CSV files from spreadsheets, JSON data from APIs, XML from legacy systems. To work with this data effectively, you need specialized tools.

CSV (Comma-Separated Values) is the universal format for tabular data—spreadsheets, database exports, and data analysis. JSON (JavaScript Object Notation) is the lingua franca of web APIs—nested, flexible, and human-readable. Mastering both formats is essential for data processing, API integration, and modern application development.

This story—**The 2026 Python Metromap: CSV & JSON Processing – Structured Data**—is your guide to working with structured data formats. We'll build a complete sales data importer that reads CSV files, validates data, and generates reports. We'll create an API client that sends and receives JSON. We'll build a data converter that transforms between CSV and JSON. We'll implement a nested JSON parser for complex API responses. And we'll create a complete ETL (Extract, Transform, Load) pipeline.

**Let's structure our data.**

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

- 📊 **The 2026 Python Metromap: CSV & JSON Processing – Structured Data** – Sales data importer/exporter; vendor CSV integration; API JSON formatting. **⬅️ YOU ARE HERE**

- ⚠️ **The 2026 Python Metromap: Exception Handling – Graceful Failures** – Resilient web scraper; network error handling; request retries. 🔜 *Up Next*

- 🔧 **The 2026 Python Metromap: Context Managers – The with Statement** – Database connection pool; automatic resource cleanup.

- 🗺️ **The 2026 Python Metromap: Working with Paths & Directories** – Automated backup system; file organization by date; log rotation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📊 Section 1: CSV Processing – Reading and Writing Tabular Data

CSV (Comma-Separated Values) is the standard format for tabular data. Python's `csv` module provides robust reading and writing capabilities.

**SOLID Principle Applied: Single Responsibility** – Each CSV operation has a specific purpose.

**Design Pattern: Iterator Pattern** – CSV reader iterates through rows without loading entire file.

```python
"""
CSV PROCESSING: READING AND WRITING TABULAR DATA

This section covers reading and writing CSV files.

SOLID Principle: Single Responsibility
- Each CSV operation has a specific purpose

Design Pattern: Iterator Pattern
- CSV reader iterates through rows efficiently
"""

import csv
from typing import List, Dict, Any, Optional, Iterator
from datetime import datetime
from io import StringIO
import os


def demonstrate_csv_reading():
    """
    Demonstrates different ways to read CSV files.
    
    Methods:
    - csv.reader: Returns lists
    - csv.DictReader: Returns dictionaries with headers
    """
    print("=" * 60)
    print("SECTION 1A: READING CSV FILES")
    print("=" * 60)
    
    # Create sample CSV file
    sample_csv = """name,age,city,salary
Alice Chen,28,New York,75000
Bob Smith,35,Los Angeles,85000
Charlie Brown,22,Chicago,65000
Diana Prince,31,New York,95000
Eve Wilson,29,Boston,70000
"""
    
    with open("employees.csv", "w") as f:
        f.write(sample_csv)
    print("  Created employees.csv")
    
    # METHOD 1: csv.reader (returns lists)
    print("\n1. csv.reader() - Rows as lists")
    print("-" * 40)
    
    with open("employees.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)  # Get header row
        print(f"  Headers: {headers}")
        
        for row in reader:
            print(f"  Row: {row}")
    
    # METHOD 2: csv.DictReader (returns dictionaries)
    print("\n2. csv.DictReader() - Rows as dictionaries")
    print("-" * 40)
    
    with open("employees.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"  {row['name']}: {row['age']} years old, from {row['city']}")
    
    # METHOD 3: Reading with custom delimiter
    print("\n3. CUSTOM DELIMITER (e.g., tab-separated)")
    print("-" * 40)
    
    tsv_data = "name\tage\tcity\nAlice\t28\tNYC\nBob\t35\tLA"
    with open("data.tsv", "w") as f:
        f.write(tsv_data)
    
    with open("data.tsv", "r") as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            print(f"  {row['name']} - {row['city']}")
    
    # METHOD 4: Reading specific columns
    print("\n4. READING SPECIFIC COLUMNS")
    print("-" * 40)
    
    with open("employees.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"  {row['name']} earns ${row['salary']}")
    
    # METHOD 5: Handling missing values
    print("\n5. HANDLING MISSING VALUES")
    print("-" * 40)
    
    messy_csv = """name,age,city
Alice,28,NYC
Bob,,LA
Charlie,35,
"""
    
    with open("messy.csv", "w") as f:
        f.write(messy_csv)
    
    with open("messy.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            age = row['age'] if row['age'] else "Unknown"
            city = row['city'] if row['city'] else "Unknown"
            print(f"  {row['name']}: Age {age}, City {city}")
    
    # Clean up
    for f in ["employees.csv", "data.tsv", "messy.csv"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


def demonstrate_csv_writing():
    """
    Demonstrates different ways to write CSV files.
    
    Methods:
    - csv.writer: Write lists
    - csv.DictWriter: Write dictionaries
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: WRITING CSV FILES")
    print("=" * 60)
    
    # METHOD 1: csv.writer (write lists)
    print("\n1. csv.writer() - Writing lists")
    print("-" * 40)
    
    data = [
        ["Product", "Price", "Quantity"],
        ["Laptop", 999.99, 5],
        ["Mouse", 29.99, 15],
        ["Keyboard", 89.99, 8]
    ]
    
    with open("products.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("  Wrote products.csv with 4 rows")
    
    # METHOD 2: csv.DictWriter (write dictionaries)
    print("\n2. csv.DictWriter() - Writing dictionaries")
    print("-" * 40)
    
    employees = [
        {"name": "Alice", "department": "Engineering", "salary": 95000},
        {"name": "Bob", "department": "Sales", "salary": 75000},
        {"name": "Charlie", "department": "Marketing", "salary": 68000}
    ]
    
    with open("employees_out.csv", "w", newline='') as f:
        fieldnames = ["name", "department", "salary"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(employees)
    print("  Wrote employees_out.csv with 3 records")
    
    # METHOD 3: Custom delimiter
    print("\n3. CUSTOM DELIMITER (pipe-separated)")
    print("-" * 40)
    
    with open("products_pipe.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(["ID", "Name", "Price"])
        writer.writerow([1, "Laptop", 999.99])
        writer.writerow([2, "Mouse", 29.99])
    print("  Wrote pipe-delimited CSV")
    
    # METHOD 4: Quote handling
    print("\n4. QUOTE HANDLING")
    print("-" * 40)
    
    data_with_quotes = [
        ["Description", "Value"],
        ['Contains "quotes"', 123],
        ['Contains, comma', 456]
    ]
    
    with open("quoted.csv", "w", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data_with_quotes)
    print("  Wrote CSV with all fields quoted")
    
    # METHOD 5: Appending to existing CSV
    print("\n5. APPENDING TO CSV")
    print("-" * 40)
    
    with open("products.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Monitor", 299.99, 3])
    print("  Appended new row to products.csv")
    
    # Verify
    with open("products.csv", "r") as f:
        content = f.read()
    print(f"  Final content:\n{content}")
    
    # Clean up
    for f in ["products.csv", "employees_out.csv", "products_pipe.csv", "quoted.csv"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


def build_sales_data_processor():
    """
    Complete sales data processor that reads CSV, validates, and generates reports.
    
    SOLID: Single Responsibility - Each function handles one aspect
    Design Pattern: Pipeline Pattern - Data flows through processing stages
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: SALES DATA PROCESSOR")
    print("=" * 60)
    
    from typing import Tuple
    from collections import defaultdict
    
    class SalesRecord:
        """Represents a sales record."""
        
        def __init__(self, date: str, product: str, quantity: int, price: float, region: str):
            self.date = date
            self.product = product
            self.quantity = quantity
            self.price = price
            self.region = region
            self.total = quantity * price
        
        @classmethod
        def from_dict(cls, data: Dict) -> 'SalesRecord':
            """Create from dictionary (from CSV)."""
            return cls(
                date=data['date'],
                product=data['product'],
                quantity=int(data['quantity']),
                price=float(data['price']),
                region=data['region']
            )
        
        def to_dict(self) -> Dict:
            return {
                "date": self.date,
                "product": self.product,
                "quantity": self.quantity,
                "price": self.price,
                "region": self.region,
                "total": self.total
            }
    
    class SalesDataProcessor:
        """
        Processes sales data from CSV.
        
        Design Pattern: Pipeline Pattern - Data flows through stages
        """
        
        def __init__(self):
            self.records: List[SalesRecord] = []
            self.errors: List[Tuple[int, str]] = []
        
        def load_from_csv(self, filepath: str) -> 'SalesDataProcessor':
            """Load sales data from CSV file."""
            self.records = []
            self.errors = []
            
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                
                for line_num, row in enumerate(reader, start=2):
                    try:
                        # Validate required fields
                        required = ['date', 'product', 'quantity', 'price', 'region']
                        missing = [f for f in required if not row.get(f)]
                        if missing:
                            raise ValueError(f"Missing fields: {missing}")
                        
                        # Validate data types
                        try:
                            quantity = int(row['quantity'])
                            if quantity <= 0:
                                raise ValueError(f"Quantity must be positive: {quantity}")
                        except ValueError:
                            raise ValueError(f"Invalid quantity: {row['quantity']}")
                        
                        try:
                            price = float(row['price'])
                            if price <= 0:
                                raise ValueError(f"Price must be positive: {price}")
                        except ValueError:
                            raise ValueError(f"Invalid price: {row['price']}")
                        
                        record = SalesRecord.from_dict(row)
                        self.records.append(record)
                        
                    except Exception as e:
                        self.errors.append((line_num, str(e)))
            
            print(f"  Loaded {len(self.records)} records with {len(self.errors)} errors")
            return self
        
        def validate(self) -> 'SalesDataProcessor':
            """Validate loaded data."""
            # Check for duplicates
            seen = set()
            duplicates = []
            for record in self.records:
                key = (record.date, record.product, record.region)
                if key in seen:
                    duplicates.append(key)
                seen.add(key)
            
            if duplicates:
                print(f"  Warning: Found {len(duplicates)} duplicate entries")
            
            return self
        
        def filter_by_region(self, region: str) -> List[SalesRecord]:
            """Filter records by region."""
            return [r for r in self.records if r.region == region]
        
        def filter_by_product(self, product: str) -> List[SalesRecord]:
            """Filter records by product."""
            return [r for r in self.records if r.product == product]
        
        def filter_by_date_range(self, start_date: str, end_date: str) -> List[SalesRecord]:
            """Filter records by date range."""
            return [r for r in self.records if start_date <= r.date <= end_date]
        
        def get_summary(self) -> Dict:
            """Get sales summary statistics."""
            if not self.records:
                return {"error": "No data"}
            
            total_revenue = sum(r.total for r in self.records)
            total_quantity = sum(r.quantity for r in self.records)
            
            # Product summary
            product_revenue = defaultdict(float)
            product_quantity = defaultdict(int)
            for r in self.records:
                product_revenue[r.product] += r.total
                product_quantity[r.product] += r.quantity
            
            # Region summary
            region_revenue = defaultdict(float)
            for r in self.records:
                region_revenue[r.region] += r.total
            
            # Daily summary
            daily_revenue = defaultdict(float)
            for r in self.records:
                daily_revenue[r.date] += r.total
            
            return {
                "total_records": len(self.records),
                "total_revenue": round(total_revenue, 2),
                "total_quantity": total_quantity,
                "average_order_value": round(total_revenue / len(self.records), 2),
                "product_summary": {
                    product: {
                        "revenue": round(revenue, 2),
                        "quantity": product_quantity[product]
                    }
                    for product, revenue in product_revenue.items()
                },
                "region_summary": {
                    region: round(revenue, 2) for region, revenue in region_revenue.items()
                },
                "top_product": max(product_revenue.items(), key=lambda x: x[1])[0] if product_revenue else None,
                "top_region": max(region_revenue.items(), key=lambda x: x[1])[0] if region_revenue else None,
                "daily_revenue": {date: round(rev, 2) for date, rev in daily_revenue.items()}
            }
        
        def export_to_csv(self, output_file: str, records: List[SalesRecord] = None) -> None:
            """Export records to CSV."""
            if records is None:
                records = self.records
            
            with open(output_file, 'w', newline='') as f:
                if records:
                    writer = csv.DictWriter(f, fieldnames=records[0].to_dict().keys())
                    writer.writeheader()
                    for record in records:
                        writer.writerow(record.to_dict())
            
            print(f"  Exported {len(records)} records to {output_file}")
        
        def generate_report(self) -> str:
            """Generate a sales report."""
            summary = self.get_summary()
            
            report = []
            report.append("=" * 60)
            report.append("SALES DATA REPORT")
            report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report.append("=" * 60)
            
            report.append(f"\n📊 OVERALL STATISTICS:")
            report.append(f"  Total Records: {summary['total_records']:,}")
            report.append(f"  Total Revenue: ${summary['total_revenue']:,.2f}")
            report.append(f"  Total Quantity: {summary['total_quantity']:,}")
            report.append(f"  Average Order: ${summary['average_order_value']:.2f}")
            
            report.append(f"\n🏆 TOP PERFORMERS:")
            report.append(f"  Top Product: {summary['top_product']}")
            report.append(f"  Top Region: {summary['top_region']}")
            
            report.append(f"\n📦 PRODUCT BREAKDOWN:")
            for product, data in summary['product_summary'].items():
                report.append(f"  {product}: ${data['revenue']:,.2f} ({data['quantity']} units)")
            
            report.append(f"\n📍 REGION BREAKDOWN:")
            for region, revenue in summary['region_summary'].items():
                report.append(f"  {region}: ${revenue:,.2f}")
            
            report.append("\n" + "=" * 60)
            return "\n".join(report)
    
    # Create sample sales data
    sales_csv = """date,product,quantity,price,region
2024-01-01,Laptop,2,999.99,North
2024-01-02,Mouse,5,29.99,South
2024-01-03,Laptop,1,999.99,East
2024-01-04,Keyboard,3,89.99,West
2024-01-05,Mouse,10,29.99,North
2024-01-06,Monitor,2,299.99,South
2024-01-07,Laptop,1,999.99,West
2024-01-08,Keyboard,2,89.99,North
2024-01-09,Mouse,8,29.99,East
2024-01-10,Monitor,3,299.99,North
"""
    
    with open("sales_data.csv", "w") as f:
        f.write(sales_csv)
    print("  Created sales_data.csv")
    
    # Process data
    processor = SalesDataProcessor()
    processor.load_from_csv("sales_data.csv").validate()
    
    # Generate report
    print("\n1. SALES REPORT")
    print("-" * 40)
    report = processor.generate_report()
    print(report)
    
    # Filter by region
    print("\n2. FILTERED DATA (North Region)")
    print("-" * 40)
    north_sales = processor.filter_by_region("North")
    print(f"  North region sales: {len(north_sales)} records")
    for record in north_sales[:3]:
        print(f"    {record.date}: {record.quantity}x {record.product} = ${record.total:.2f}")
    
    # Export filtered data
    print("\n3. EXPORTING FILTERED DATA")
    print("-" * 40)
    processor.export_to_csv("north_sales.csv", north_sales)
    
    # Summary statistics
    print("\n4. SUMMARY STATISTICS")
    print("-" * 40)
    summary = processor.get_summary()
    print(f"  Total Revenue: ${summary['total_revenue']:,.2f}")
    print(f"  Top Product: {summary['top_product']}")
    print(f"  Top Region: {summary['top_region']}")
    
    # Clean up
    for f in ["sales_data.csv", "north_sales.csv"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_csv_reading()
    demonstrate_csv_writing()
    build_sales_data_processor()
```

---

## 🔄 Section 2: JSON Processing – Nested Data Structures

JSON (JavaScript Object Notation) is the standard format for web APIs and configuration files, supporting nested structures.

**SOLID Principle Applied: Single Responsibility** – Each JSON operation has a specific purpose.

**Design Pattern: Adapter Pattern** – JSON adapts Python objects to/from text format.

```python
"""
JSON PROCESSING: NESTED DATA STRUCTURES

This section covers reading and writing JSON files.

SOLID Principle: Single Responsibility
- Each JSON operation has a specific purpose

Design Pattern: Adapter Pattern
- JSON adapts Python objects to/from text format
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime, date
from decimal import Decimal
import os


def demonstrate_json_basics():
    """
    Demonstrates basic JSON serialization and deserialization.
    
    Methods:
    - json.dumps(): Convert Python object to JSON string
    - json.loads(): Convert JSON string to Python object
    - json.dump(): Write JSON to file
    - json.load(): Read JSON from file
    """
    print("=" * 60)
    print("SECTION 2A: JSON BASICS")
    print("=" * 60)
    
    # Python object
    data = {
        "name": "Alice Chen",
        "age": 28,
        "email": "alice@example.com",
        "is_active": True,
        "scores": [95, 87, 92],
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zip": "10001"
        },
        "preferences": {
            "theme": "dark",
            "notifications": True
        }
    }
    
    print("\n1. PYTHON TO JSON (serialization)")
    print("-" * 40)
    
    # Convert to JSON string
    json_string = json.dumps(data, indent=2)
    print(f"  JSON string (first 200 chars):\n{json_string[:200]}...")
    
    print("\n2. JSON TO PYTHON (deserialization)")
    print("-" * 40)
    
    # Convert back to Python
    restored = json.loads(json_string)
    print(f"  Restored type: {type(restored).__name__}")
    print(f"  Restored name: {restored['name']}")
    print(f"  Restored scores: {restored['scores']}")
    
    print("\n3. WRITING JSON TO FILE")
    print("-" * 40)
    
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("  Wrote user_data.json")
    
    print("\n4. READING JSON FROM FILE")
    print("-" * 40)
    
    with open("user_data.json", "r") as f:
        loaded = json.load(f)
    print(f"  Loaded user: {loaded['name']} from file")
    
    # Clean up
    if os.path.exists("user_data.json"):
        os.remove("user_data.json")
    print("\n  Cleaned up demo files")


def demonstrate_json_custom_serialization():
    """
    Demonstrates custom serialization for non-standard types.
    
    JSON supports: dict, list, str, int, float, bool, None
    Custom types need conversion (datetime, Decimal, date, etc.)
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: CUSTOM JSON SERIALIZATION")
    print("=" * 60)
    
    class CustomEncoder(json.JSONEncoder):
        """Custom JSON encoder for non-standard types."""
        
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, date):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return float(obj)
            if hasattr(obj, '__dict__'):
                return obj.__dict__
            return super().default(obj)
    
    # Data with non-standard types
    data = {
        "name": "Alice",
        "created_at": datetime.now(),
        "birth_date": date(1995, 6, 15),
        "price": Decimal("99.99"),
        "tags": ["python", "json", "demo"]
    }
    
    print("\n1. WITHOUT CUSTOM ENCODER (fails)")
    print("-" * 40)
    
    try:
        json.dumps(data)
    except TypeError as e:
        print(f"  Error: {e}")
    
    print("\n2. WITH CUSTOM ENCODER")
    print("-" * 40)
    
    json_string = json.dumps(data, cls=CustomEncoder, indent=2)
    print(f"  Serialized:\n{json_string}")
    
    print("\n3. DECODING BACK (with custom parsing)")
    print("-" * 40)
    
    def custom_decoder(dict_obj):
        """Custom decoder to restore datetime objects."""
        for key, value in dict_obj.items():
            if key in ['created_at', 'birth_date'] and isinstance(value, str):
                try:
                    dict_obj[key] = datetime.fromisoformat(value)
                except ValueError:
                    pass
        return dict_obj
    
    restored = json.loads(json_string, object_hook=custom_decoder)
    print(f"  Restored created_at type: {type(restored['created_at']).__name__}")
    print(f"  Restored birth_date type: {type(restored['birth_date']).__name__}")
    print(f"  Restored price type: {type(restored['price']).__name__}")
    
    print("\n4. USING default AND object_hook PARAMETERS")
    print("-" * 40)
    
    # Simpler approach for common types
    def json_serializer(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Type {type(obj)} not serializable")
    
    json_string = json.dumps(data, default=json_serializer, indent=2)
    print(f"  Serialized with default parameter:\n{json_string[:150]}...")


def build_api_client():
    """
    Builds an API client that sends and receives JSON.
    
    SOLID: Dependency Inversion - Depends on JSON abstraction
    Design Pattern: Adapter Pattern - Adapts Python to API calls
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: API CLIENT WITH JSON")
    print("=" * 60)
    
    import requests
    from typing import Optional, Tuple
    
    class APIClient:
        """
        API client that communicates via JSON.
        
        Design Pattern: Adapter Pattern - Adapts Python to HTTP/JSON
        """
        
        def __init__(self, base_url: str, api_key: Optional[str] = None):
            self.base_url = base_url.rstrip('/')
            self.api_key = api_key
            self.session = requests.Session()
            
            if api_key:
                self.session.headers.update({"Authorization": f"Bearer {api_key}"})
            self.session.headers.update({"Content-Type": "application/json"})
        
        def _request(self, method: str, endpoint: str, data: Dict = None) -> Tuple[int, Dict]:
            """Make an HTTP request and parse JSON response."""
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            
            try:
                if method == "GET":
                    response = self.session.get(url)
                elif method == "POST":
                    response = self.session.post(url, json=data)
                elif method == "PUT":
                    response = self.session.put(url, json=data)
                elif method == "DELETE":
                    response = self.session.delete(url)
                else:
                    raise ValueError(f"Unsupported method: {method}")
                
                # Try to parse JSON response
                try:
                    response_data = response.json()
                except json.JSONDecodeError:
                    response_data = {"message": response.text}
                
                return response.status_code, response_data
                
            except requests.exceptions.RequestException as e:
                return 500, {"error": str(e)}
        
        def get(self, endpoint: str, **params) -> Tuple[int, Dict]:
            """GET request with query parameters."""
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            try:
                response = self.session.get(url, params=params)
                return response.status_code, response.json() if response.text else {}
            except Exception as e:
                return 500, {"error": str(e)}
        
        def post(self, endpoint: str, data: Dict) -> Tuple[int, Dict]:
            """POST request with JSON body."""
            return self._request("POST", endpoint, data)
        
        def put(self, endpoint: str, data: Dict) -> Tuple[int, Dict]:
            """PUT request with JSON body."""
            return self._request("PUT", endpoint, data)
        
        def delete(self, endpoint: str) -> Tuple[int, Dict]:
            """DELETE request."""
            return self._request("DELETE", endpoint)
    
    # Simulated API server (for demonstration)
    class MockAPIServer:
        """Mock API server for demonstration."""
        
        def __init__(self):
            self.users = {
                1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
                2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
            }
            self.next_id = 3
        
        def handle_request(self, method: str, path: str, data: Dict = None) -> Tuple[int, Dict]:
            """Handle mock API request."""
            if path == "/users" and method == "GET":
                return 200, {"users": list(self.users.values()), "total": len(self.users)}
            
            elif path.startswith("/users/") and method == "GET":
                try:
                    user_id = int(path.split("/")[-1])
                    user = self.users.get(user_id)
                    if user:
                        return 200, user
                    return 404, {"error": "User not found"}
                except ValueError:
                    return 400, {"error": "Invalid user ID"}
            
            elif path == "/users" and method == "POST":
                new_user = {
                    "id": self.next_id,
                    "name": data.get("name"),
                    "email": data.get("email")
                }
                self.users[self.next_id] = new_user
                self.next_id += 1
                return 201, new_user
            
            elif path.startswith("/users/") and method == "PUT":
                try:
                    user_id = int(path.split("/")[-1])
                    if user_id in self.users:
                        self.users[user_id].update(data)
                        return 200, self.users[user_id]
                    return 404, {"error": "User not found"}
                except ValueError:
                    return 400, {"error": "Invalid user ID"}
            
            elif path.startswith("/users/") and method == "DELETE":
                try:
                    user_id = int(path.split("/")[-1])
                    if user_id in self.users:
                        deleted = self.users.pop(user_id)
                        return 200, {"deleted": deleted}
                    return 404, {"error": "User not found"}
                except ValueError:
                    return 400, {"error": "Invalid user ID"}
            
            return 404, {"error": "Not found"}
    
    # Demonstration
    print("\n1. API CLIENT DEMONSTRATION")
    print("-" * 40)
    
    # Use mock server (in production, use real URL)
    mock_server = MockAPIServer()
    
    # Create client (would connect to real API)
    client = APIClient("https://api.example.com/v1")
    
    # Simulate API calls using mock
    print("\n  GET /users:")
    status, data = mock_server.handle_request("GET", "/users")
    print(f"    Status: {status}")
    print(f"    Response: {json.dumps(data, indent=2)[:150]}...")
    
    print("\n  POST /users (create):")
    new_user = {"name": "Charlie", "email": "charlie@example.com"}
    status, data = mock_server.handle_request("POST", "/users", new_user)
    print(f"    Status: {status}")
    print(f"    Created user: {data}")
    
    print("\n  GET /users/1:")
    status, data = mock_server.handle_request("GET", "/users/1")
    print(f"    User: {data}")
    
    print("\n  PUT /users/1 (update):")
    update = {"name": "Alicia"}
    status, data = mock_server.handle_request("PUT", "/users/1", update)
    print(f"    Updated: {data}")
    
    print("\n  DELETE /users/2:")
    status, data = mock_server.handle_request("DELETE", "/users/2")
    print(f"    Deleted: {data.get('deleted', {}).get('name')}")
    
    print("\n2. JSON PAYLOAD EXAMPLES")
    print("-" * 40)
    
    # Request payload
    request_payload = {
        "user": {
            "name": "New User",
            "email": "new@example.com",
            "profile": {
                "age": 30,
                "city": "Boston"
            }
        },
        "metadata": {
            "source": "api_client",
            "version": "1.0"
        }
    }
    
    print("  Request JSON:")
    print(f"    {json.dumps(request_payload, indent=2)[:200]}...")
    
    # Response payload
    response_payload = {
        "status": "success",
        "data": {
            "id": 100,
            "name": "New User",
            "created_at": datetime.now().isoformat()
        },
        "meta": {
            "request_id": "req_12345",
            "processing_time_ms": 45
        }
    }
    
    print("\n  Response JSON:")
    print(f"    {json.dumps(response_payload, indent=2)[:200]}...")
    
    print("\n3. BEST PRACTICES FOR API JSON")
    print("-" * 40)
    
    print("""
    ✅ Use consistent field naming (snake_case or camelCase)
    ✅ Include metadata (request_id, timestamp, version)
    ✅ Use standard HTTP status codes
    ✅ Return structured errors: {"error": {"code": "...", "message": "..."}}
    ✅ Validate JSON schema on both sides
    ✅ Handle missing fields gracefully
    ✅ Use datetime.isoformat() for timestamps
    """)


if __name__ == "__main__":
    demonstrate_json_basics()
    demonstrate_json_custom_serialization()
    build_api_client()
```

---

## 🔄 Section 3: CSV-JSON Converter

A utility for converting between CSV and JSON formats with validation and transformation.

**SOLID Principles Applied:**
- Single Responsibility: Converter handles one conversion direction
- Open/Closed: New conversion options can be added

**Design Patterns:**
- Adapter Pattern: Adapts between CSV and JSON
- Builder Pattern: Builds conversion configuration

```python
"""
CSV-JSON CONVERTER

This section builds utilities for converting between CSV and JSON.

SOLID Principles Applied:
- Single Responsibility: Converter handles one conversion direction
- Open/Closed: New conversion options can be added

Design Patterns:
- Adapter Pattern: Adapts between CSV and JSON
- Builder Pattern: Builds conversion configuration
"""

import csv
import json
import os
from typing import List, Dict, Any, Optional, Callable
from io import StringIO
from datetime import datetime


class ConverterConfig:
    """Configuration for CSV-JSON conversion."""
    
    def __init__(self):
        self.delimiter = ','
        self.encoding = 'utf-8'
        self.has_header = True
        self.preserve_order = False
        self.null_value = None
        self.transformers: Dict[str, Callable] = {}
        self.include_fields: Optional[List[str]] = None
        self.exclude_fields: Optional[List[str]] = None
    
    def set_delimiter(self, delimiter: str) -> 'ConverterConfig':
        self.delimiter = delimiter
        return self
    
    def set_encoding(self, encoding: str) -> 'ConverterConfig':
        self.encoding = encoding
        return self
    
    def set_header(self, has_header: bool) -> 'ConverterConfig':
        self.has_header = has_header
        return self
    
    def add_transformer(self, field: str, transformer: Callable) -> 'ConverterConfig':
        self.transformers[field] = transformer
        return self
    
    def include(self, fields: List[str]) -> 'ConverterConfig':
        self.include_fields = fields
        return self
    
    def exclude(self, fields: List[str]) -> 'ConverterConfig':
        self.exclude_fields = fields
        return self


class CSVToJSONConverter:
    """
    Converts CSV files to JSON format.
    
    Design Pattern: Adapter Pattern - Adapts CSV to JSON
    """
    
    def __init__(self, config: Optional[ConverterConfig] = None):
        self.config = config or ConverterConfig()
    
    def convert_file(self, input_file: str, output_file: str) -> None:
        """Convert CSV file to JSON file."""
        data = self.read_csv(input_file)
        
        with open(output_file, 'w', encoding=self.config.encoding) as f:
            if self.config.preserve_order:
                json.dump(data, f, indent=2)
            else:
                json.dump(data, f, indent=2, sort_keys=True)
        
        print(f"  Converted {input_file} → {output_file} ({len(data)} records)")
    
    def read_csv(self, filepath: str) -> List[Dict]:
        """Read CSV file and convert to list of dictionaries."""
        records = []
        
        with open(filepath, 'r', encoding=self.config.encoding) as f:
            if self.config.has_header:
                reader = csv.DictReader(f, delimiter=self.config.delimiter)
                for row in reader:
                    record = self._process_row(row)
                    if record:
                        records.append(record)
            else:
                reader = csv.reader(f, delimiter=self.config.delimiter)
                for row_num, row in enumerate(reader):
                    record = {f"col_{i}": self._transform_value(val, f"col_{i}")
                             for i, val in enumerate(row)}
                    if record:
                        records.append(record)
        
        return records
    
    def _process_row(self, row: Dict) -> Optional[Dict]:
        """Process a single CSV row."""
        record = {}
        
        for key, value in row.items():
            # Skip if field excluded
            if self.config.exclude_fields and key in self.config.exclude_fields:
                continue
            
            # Skip if field not included
            if self.config.include_fields and key not in self.config.include_fields:
                continue
            
            # Apply transformer
            if key in self.config.transformers:
                value = self.config.transformers[key](value)
            
            # Handle null values
            if value == '' and self.config.null_value is not None:
                value = self.config.null_value
            
            record[key] = value
        
        return record if record else None
    
    def _transform_value(self, value: str, field: str) -> Any:
        """Transform value based on field type hints."""
        # Try to detect type
        if value == '':
            return value
        
        # Try integer
        try:
            if value.isdigit():
                return int(value)
        except (ValueError, AttributeError):
            pass
        
        # Try float
        try:
            if '.' in value:
                return float(value)
        except (ValueError, AttributeError):
            pass
        
        # Try boolean
        if value.lower() in ('true', 'yes', 'on', '1'):
            return True
        if value.lower() in ('false', 'no', 'off', '0'):
            return False
        
        return value


class JSONToCSVConverter:
    """
    Converts JSON files to CSV format.
    
    Design Pattern: Adapter Pattern - Adapts JSON to CSV
    """
    
    def __init__(self, config: Optional[ConverterConfig] = None):
        self.config = config or ConverterConfig()
    
    def convert_file(self, input_file: str, output_file: str) -> None:
        """Convert JSON file to CSV file."""
        with open(input_file, 'r', encoding=self.config.encoding) as f:
            data = json.load(f)
        
        if not data:
            print("  No data to convert")
            return
        
        if isinstance(data, dict):
            data = [data]
        
        self.write_csv(data, output_file)
        print(f"  Converted {input_file} → {output_file} ({len(data)} records)")
    
    def write_csv(self, data: List[Dict], output_file: str) -> None:
        """Write list of dictionaries to CSV file."""
        if not data:
            return
        
        # Get all field names
        fieldnames = set()
        for record in data:
            fieldnames.update(record.keys())
        
        fieldnames = sorted(fieldnames) if not self.config.preserve_order else list(fieldnames)
        
        # Apply field filtering
        if self.config.include_fields:
            fieldnames = [f for f in fieldnames if f in self.config.include_fields]
        if self.config.exclude_fields:
            fieldnames = [f for f in fieldnames if f not in self.config.exclude_fields]
        
        with open(output_file, 'w', newline='', encoding=self.config.encoding) as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=self.config.delimiter)
            writer.writeheader()
            
            for record in data:
                # Transform values
                row = {}
                for field in fieldnames:
                    value = record.get(field, '')
                    if field in self.config.transformers:
                        value = self.config.transformers[field](value)
                    row[field] = value
                
                writer.writerow(row)


class DataTransformer:
    """Collection of common data transformers."""
    
    @staticmethod
    def to_int(value: str) -> int:
        try:
            return int(float(value)) if value else 0
        except (ValueError, TypeError):
            return 0
    
    @staticmethod
    def to_float(value: str) -> float:
        try:
            return float(value) if value else 0.0
        except (ValueError, TypeError):
            return 0.0
    
    @staticmethod
    def to_bool(value: str) -> bool:
        if isinstance(value, bool):
            return value
        return str(value).lower() in ('true', 'yes', 'on', '1')
    
    @staticmethod
    def to_date(value: str) -> str:
        """Parse and reformat date to ISO format."""
        try:
            # Try common formats
            for fmt in ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y%m%d"]:
                try:
                    dt = datetime.strptime(value, fmt)
                    return dt.strftime("%Y-%m-%d")
                except ValueError:
                    continue
            return value
        except Exception:
            return value
    
    @staticmethod
    def uppercase(value: str) -> str:
        return str(value).upper()
    
    @staticmethod
    def lowercase(value: str) -> str:
        return str(value).lower()
    
    @staticmethod
    def capitalize(value: str) -> str:
        return str(value).capitalize()
    
    @staticmethod
    def strip(value: str) -> str:
        return str(value).strip()


def demonstrate_converter():
    """
    Demonstrate CSV-JSON conversion.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: CSV-JSON CONVERTER")
    print("=" * 60)
    
    # Create sample CSV
    csv_data = """id,name,email,age,active,joined_date
1,Alice Chen,alice@example.com,28,true,2023-01-15
2,Bob Smith,bob@example.com,35,false,2023-02-20
3,Charlie Brown,charlie@example.com,22,true,2023-03-10
4,Diana Prince,diana@example.com,31,true,2023-04-05
5,Eve Wilson,eve@example.com,29,false,2023-05-12
"""
    
    with open("sample.csv", "w") as f:
        f.write(csv_data)
    print("  Created sample.csv")
    
    print("\n1. CSV TO JSON CONVERSION")
    print("-" * 40)
    
    config = ConverterConfig()
    config.add_transformer("age", DataTransformer.to_int)
    config.add_transformer("active", DataTransformer.to_bool)
    
    converter = CSVToJSONConverter(config)
    converter.convert_file("sample.csv", "output.json")
    
    # Show JSON output
    with open("output.json", "r") as f:
        json_data = json.load(f)
    print(f"\n  JSON output (first record):")
    print(f"    {json.dumps(json_data[0], indent=2)}")
    
    print("\n2. JSON TO CSV CONVERSION")
    print("-" * 40)
    
    # Modify JSON data
    json_data.append({
        "id": 6,
        "name": "Frank Miller",
        "email": "frank@example.com",
        "age": 40,
        "active": True,
        "joined_date": "2023-06-18"
    })
    
    with open("modified.json", "w") as f:
        json.dump(json_data, f, indent=2)
    
    config2 = ConverterConfig()
    config2.add_transformer("name", DataTransformer.uppercase)
    config2.add_transformer("email", DataTransformer.lowercase)
    
    json_to_csv = JSONToCSVConverter(config2)
    json_to_csv.convert_file("modified.json", "restored.csv")
    
    # Show restored CSV
    with open("restored.csv", "r") as f:
        print(f"\n  Restored CSV:")
        print(f"    {f.read()[:200]}...")
    
    print("\n3. FIELD SELECTION AND FILTERING")
    print("-" * 40)
    
    config3 = ConverterConfig()
    config3.include(["name", "email", "active"])
    config3.add_transformer("name", DataTransformer.capitalize)
    
    converter2 = CSVToJSONConverter(config3)
    converter2.convert_file("sample.csv", "filtered.json")
    
    with open("filtered.json", "r") as f:
        filtered = json.load(f)
    print(f"  Filtered output (only name, email, active):")
    for record in filtered:
        print(f"    {record}")
    
    print("\n4. CUSTOM DELIMITER")
    print("-" * 40)
    
    # Create pipe-delimited file
    pipe_data = """id|name|city
1|Alice|New York
2|Bob|Los Angeles
3|Charlie|Chicago
"""
    
    with open("pipe_data.txt", "w") as f:
        f.write(pipe_data)
    
    config4 = ConverterConfig()
    config4.set_delimiter('|')
    
    converter3 = CSVToJSONConverter(config4)
    converter3.convert_file("pipe_data.txt", "pipe_output.json")
    
    with open("pipe_output.json", "r") as f:
        pipe_json = json.load(f)
    print(f"  Converted pipe-delimited file to JSON:")
    for record in pipe_json:
        print(f"    {record}")
    
    # Clean up
    for f in ["sample.csv", "output.json", "modified.json", "restored.csv", 
              "filtered.json", "pipe_data.txt", "pipe_output.json"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_converter()
```

---

## 🏭 Section 4: Complete ETL Pipeline

A complete ETL (Extract, Transform, Load) pipeline for data processing.

**SOLID Principles Applied:**
- Single Responsibility: Each stage has one purpose
- Dependency Inversion: Stages depend on abstractions

**Design Patterns:**
- Pipeline Pattern: Data flows through stages
- Strategy Pattern: Pluggable transformations

```python
"""
COMPLETE ETL PIPELINE

This section builds a complete ETL (Extract, Transform, Load) pipeline.

SOLID Principles Applied:
- Single Responsibility: Each stage has one purpose
- Dependency Inversion: Stages depend on abstractions

Design Patterns:
- Pipeline Pattern: Data flows through stages
- Strategy Pattern: Pluggable transformations
"""

import csv
import json
import os
from typing import List, Dict, Any, Optional, Callable, Iterator
from datetime import datetime
from abc import ABC, abstractmethod
import hashlib


class ExtractStage(ABC):
    """Abstract base class for data extraction."""
    
    @abstractmethod
    def extract(self, source: str) -> Iterator[Dict]:
        """Extract data from source."""
        pass


class TransformStage(ABC):
    """Abstract base class for data transformation."""
    
    @abstractmethod
    def transform(self, data: Iterator[Dict]) -> Iterator[Dict]:
        """Transform extracted data."""
        pass


class LoadStage(ABC):
    """Abstract base class for data loading."""
    
    @abstractmethod
    def load(self, data: Iterator[Dict], destination: str) -> Dict:
        """Load transformed data to destination."""
        pass


class CSVExtractor(ExtractStage):
    """Extract data from CSV files."""
    
    def __init__(self, delimiter: str = ',', has_header: bool = True):
        self.delimiter = delimiter
        self.has_header = has_header
    
    def extract(self, source: str) -> Iterator[Dict]:
        """Extract CSV data row by row."""
        with open(source, 'r') as f:
            if self.has_header:
                reader = csv.DictReader(f, delimiter=self.delimiter)
                for row in reader:
                    yield row
            else:
                reader = csv.reader(f, delimiter=self.delimiter)
                for row_num, row in enumerate(reader):
                    yield {f"col_{i}": val for i, val in enumerate(row)}


class JSONExtractor(ExtractStage):
    """Extract data from JSON files."""
    
    def extract(self, source: str) -> Iterator[Dict]:
        """Extract JSON data."""
        with open(source, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            for item in data:
                yield item
        elif isinstance(data, dict):
            yield data
        else:
            raise ValueError(f"Unsupported JSON type: {type(data)}")


class DataCleaner(TransformStage):
    """Clean and validate data."""
    
    def __init__(self, required_fields: List[str] = None, 
                 remove_nulls: bool = True,
                 strip_strings: bool = True):
        self.required_fields = required_fields or []
        self.remove_nulls = remove_nulls
        self.strip_strings = strip_strings
    
    def transform(self, data: Iterator[Dict]) -> Iterator[Dict]:
        """Clean each record."""
        for record in data:
            # Check required fields
            if self.required_fields:
                missing = [f for f in self.required_fields if not record.get(f)]
                if missing:
                    continue
            
            # Strip strings
            if self.strip_strings:
                for key, value in record.items():
                    if isinstance(value, str):
                        record[key] = value.strip()
            
            # Remove null values
            if self.remove_nulls:
                record = {k: v for k, v in record.items() if v is not None and v != ''}
            
            yield record


class TypeConverter(TransformStage):
    """Convert field types."""
    
    def __init__(self, type_map: Dict[str, Callable]):
        self.type_map = type_map
    
    def transform(self, data: Iterator[Dict]) -> Iterator[Dict]:
        """Convert types for each record."""
        for record in data:
            for field, converter in self.type_map.items():
                if field in record and record[field] is not None:
                    try:
                        record[field] = converter(record[field])
                    except (ValueError, TypeError):
                        pass
            yield record


class FieldMapper(TransformStage):
    """Rename or select fields."""
    
    def __init__(self, field_map: Dict[str, str] = None, 
                 select: List[str] = None,
                 exclude: List[str] = None):
        self.field_map = field_map or {}
        self.select = select
        self.exclude = exclude
    
    def transform(self, data: Iterator[Dict]) -> Iterator[Dict]:
        """Map and filter fields."""
        for record in data:
            # Apply field mapping
            for old_name, new_name in self.field_map.items():
                if old_name in record:
                    record[new_name] = record.pop(old_name)
            
            # Select fields
            if self.select:
                record = {k: v for k, v in record.items() if k in self.select}
            
            # Exclude fields
            if self.exclude:
                record = {k: v for k, v in record.items() if k not in self.exclude}
            
            yield record


class FieldCalculator(TransformStage):
    """Add computed fields."""
    
    def __init__(self, calculations: Dict[str, Callable]):
        self.calculations = calculations
    
    def transform(self, data: Iterator[Dict]) -> Iterator[Dict]:
        """Add computed fields."""
        for record in data:
            for field_name, calculator in self.calculations.items():
                try:
                    record[field_name] = calculator(record)
                except Exception:
                    record[field_name] = None
            yield record


class CSVLoader(LoadStage):
    """Load data to CSV file."""
    
    def __init__(self, delimiter: str = ','):
        self.delimiter = delimiter
    
    def load(self, data: Iterator[Dict], destination: str) -> Dict:
        """Load data to CSV."""
        records = list(data)
        
        if not records:
            return {"loaded": 0, "error": "No data to load"}
        
        fieldnames = set()
        for record in records:
            fieldnames.update(record.keys())
        fieldnames = sorted(fieldnames)
        
        with open(destination, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(records)
        
        return {
            "loaded": len(records),
            "destination": destination,
            "fields": len(fieldnames)
        }


class JSONLoader(LoadStage):
    """Load data to JSON file."""
    
    def __init__(self, indent: int = 2):
        self.indent = indent
    
    def load(self, data: Iterator[Dict], destination: str) -> Dict:
        """Load data to JSON."""
        records = list(data)
        
        with open(destination, 'w') as f:
            json.dump(records, f, indent=self.indent, default=str)
        
        return {
            "loaded": len(records),
            "destination": destination,
            "size_bytes": os.path.getsize(destination)
        }


class ETLPipeline:
    """
    Complete ETL pipeline.
    
    Design Pattern: Pipeline Pattern - Data flows through stages
    """
    
    def __init__(self):
        self.extractors: Dict[str, ExtractStage] = {
            'csv': CSVExtractor(),
            'json': JSONExtractor()
        }
        self.transformations: List[TransformStage] = []
        self.loaders: Dict[str, LoadStage] = {
            'csv': CSVLoader(),
            'json': JSONLoader()
        }
    
    def add_transformation(self, transformation: TransformStage) -> 'ETLPipeline':
        """Add a transformation stage."""
        self.transformations.append(transformation)
        return self
    
    def run(self, source: str, source_format: str, 
            destination: str, dest_format: str) -> Dict:
        """Run the ETL pipeline."""
        print(f"\n  ETL Pipeline: {source} → {destination}")
        
        # Extract
        extractor = self.extractors.get(source_format)
        if not extractor:
            raise ValueError(f"Unsupported source format: {source_format}")
        
        print(f"  Extracting from {source_format.upper()}...")
        data = extractor.extract(source)
        
        # Transform
        for transformation in self.transformations:
            print(f"  Applying {transformation.__class__.__name__}...")
            data = transformation.transform(data)
        
        # Load
        loader = self.loaders.get(dest_format)
        if not loader:
            raise ValueError(f"Unsupported destination format: {dest_format}")
        
        print(f"  Loading to {dest_format.upper()}...")
        result = loader.load(data, destination)
        
        return result


def demonstrate_etl_pipeline():
    """
    Demonstrate the complete ETL pipeline.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: COMPLETE ETL PIPELINE")
    print("=" * 60)
    
    # Create source CSV
    source_csv = """user_id,name,email,age,registration_date,active
1001,Alice Chen,alice@example.com,28,2023-01-15,true
1002,Bob Smith,bob@example.com,35,2023-02-20,false
1003,Charlie Brown,charlie@example.com,22,2023-03-10,true
1004,Diana Prince,diana@example.com,31,2023-04-05,true
1005,Eve Wilson,eve@example.com,29,2023-05-12,false
"""
    
    with open("source_data.csv", "w") as f:
        f.write(source_csv)
    print("  Created source_data.csv")
    
    print("\n1. BUILDING ETL PIPELINE")
    print("-" * 40)
    
    pipeline = ETLPipeline()
    
    # Add transformations
    pipeline.add_transformation(DataCleaner(required_fields=["user_id", "email"]))
    pipeline.add_transformation(TypeConverter({
        "age": int,
        "active": lambda x: str(x).lower() in ('true', 'yes', '1')
    }))
    pipeline.add_transformation(FieldMapper({
        "user_id": "id",
        "registration_date": "joined_at"
    }))
    pipeline.add_transformation(FieldCalculator({
        "age_group": lambda r: "senior" if r.get("age", 0) > 60 else "adult" if r.get("age", 0) > 18 else "minor",
        "email_domain": lambda r: r.get("email", "").split("@")[-1] if "@" in r.get("email", "") else ""
    }))
    
    print("  Pipeline configured with:")
    print("    - Data cleaning")
    print("    - Type conversion")
    print("    - Field mapping")
    print("    - Computed fields")
    
    # Run pipeline to JSON
    print("\n2. RUNNING PIPELINE (CSV → JSON)")
    print("-" * 40)
    
    result = pipeline.run("source_data.csv", "csv", "output.json", "json")
    print(f"\n  Result: {result}")
    
    # Show output JSON
    with open("output.json", "r") as f:
        output_data = json.load(f)
    print(f"\n  Transformed JSON output:")
    for record in output_data:
        print(f"    {record}")
    
    # Run pipeline to CSV
    print("\n3. RUNNING PIPELINE (CSV → CSV)")
    print("-" * 40)
    
    # Create a new pipeline without some transformations for CSV output
    pipeline2 = ETLPipeline()
    pipeline2.add_transformation(DataCleaner(required_fields=["user_id"]))
    pipeline2.add_transformation(TypeConverter({"age": int}))
    pipeline2.add_transformation(FieldMapper({"user_id": "id"}))
    
    result2 = pipeline2.run("source_data.csv", "csv", "cleaned_data.csv", "csv")
    print(f"\n  Result: {result2}")
    
    # Show output CSV
    with open("cleaned_data.csv", "r") as f:
        print(f"\n  Cleaned CSV output:")
        print(f"    {f.read()}")
    
    # Clean up
    for f in ["source_data.csv", "output.json", "cleaned_data.csv"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_etl_pipeline()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **CSV Reading** – `csv.reader` (lists), `csv.DictReader` (dictionaries). Handle headers, custom delimiters, missing values.

- **CSV Writing** – `csv.writer` (lists), `csv.DictWriter` (dictionaries). Control quoting with `quoting=csv.QUOTE_ALL`.

- **JSON Serialization** – `json.dumps()` (string), `json.dump()` (file). Custom encoders for datetime, Decimal.

- **JSON Deserialization** – `json.loads()` (string), `json.load()` (file). `object_hook` for custom type restoration.

- **CSV-JSON Converter** – Bidirectional conversion. Field selection, type conversion, data cleaning.

- **ETL Pipeline** – Extract (CSV/JSON), Transform (clean, convert, map, calculate), Load (CSV/JSON).

- **Sales Data Processor** – Load CSV, validate, filter, aggregate, generate reports, export filtered data.

- **API Client** – Send/receive JSON. Handle requests, responses, errors.

- **SOLID Principles Applied** – Single Responsibility (each converter does one job), Open/Closed (new formats can be added), Dependency Inversion (stages depend on abstractions), Interface Segregation (clean stage interfaces).

- **Design Patterns Used** – Iterator Pattern (row-by-row processing), Adapter Pattern (CSV/JSON adaptation), Pipeline Pattern (ETL stages), Strategy Pattern (pluggable transformations), Builder Pattern (converter configuration).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: File I/O – Reading & Writing

- **📚 Series E Catalog:** File & Data Handling Line – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Exception Handling – Graceful Failures (Series E, Story 3)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 2 | 3 | 40% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **31** | **21** | **60%** |

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

**Next Story:** Series E, Story 3: The 2026 Python Metromap: Exception Handling – Graceful Failures

---

## 📝 Your Invitation

You've mastered CSV and JSON processing. Now build something with what you've learned:

1. **Build a data migration tool** – Migrate data between CSV, JSON, XML, and database formats.

2. **Create a data validator** – Validate CSV files against JSON schemas, report errors.

3. **Build an API data sync** – Extract data from REST API (JSON), transform, load to CSV.

4. **Create a report generator** – Generate CSV reports from JSON data with formatting.

5. **Build a data anonymizer** – Anonymize sensitive fields in CSV/JSON files.

**You've mastered CSV & JSON processing. Next stop: Exception Handling!**

---

*Found this helpful? Clap, comment, and share what you built with CSV and JSON. Next stop: Exception Handling!* 🚇