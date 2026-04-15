# The 2026 Python Metromap: Constructor – Building Objects

## Series D: Object-Oriented Programming (OOP) Line | Story 2 of 6

![The 2026 Python Metromap/images/Constructor – Building Objects](images/Constructor – Building Objects.png)

## 📖 Introduction

**Welcome to the second stop on the Object-Oriented Programming Line.**

You've mastered classes and objects. You know how to define blueprints and create instances. But every time you create an object, you manually set its attributes after creation. Wouldn't it be better to initialize objects with their initial state automatically when they're created?

That's where constructors come in.

The constructor is a special method called `__init__` that runs automatically when you create a new object. It initializes the object's attributes, sets up initial state, and can perform any setup logic needed before the object is used. Constructors ensure that every object starts in a valid, consistent state—no more creating objects and then setting attributes separately.

This story—**The 2026 Python Metromap: Constructor – Building Objects**—is your guide to mastering the `__init__` method. We'll build a complete employee onboarding system that initializes employees with proper attributes. We'll create a configuration system with validation in the constructor. We'll implement multiple constructors using class methods. We'll build a complete order system with complex initialization logic. And we'll create a data validation framework that ensures objects are always created correctly.

**Let's build better objects.**

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

### Series D: Object-Oriented Programming (OOP) Line (6 Stories)

- 🏗️ **The 2026 Python Metromap: Classes & Objects – Blueprints & Instances** – Bank account system; deposit and withdrawal methods; customer management.

- 🔧 **The 2026 Python Metromap: Constructor – Building Objects** – Employee onboarding system; automatic attribute initialization. **⬅️ YOU ARE HERE**

- 👪 **The 2026 Python Metromap: Inheritance – Reusing Parent Classes** – Vehicle fleet manager with Car, Truck, and Motorcycle classes. 🔜 *Up Next*

- 🎭 **The 2026 Python Metromap: Polymorphism – One Interface, Many Forms** – Payment processing with CreditCard, PayPal, and Crypto implementations.

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules.

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔧 Section 1: The __init__ Constructor – Initializing Objects

The `__init__` method is called automatically when an object is created. It initializes the object's attributes and sets up initial state.

**SOLID Principle Applied: Single Responsibility** – The constructor should only initialize the object, not perform complex business logic.

**Design Pattern: Builder Pattern** – Constructors build objects with required initial state.

```python
"""
THE __init__ CONSTRUCTOR: INITIALIZING OBJECTS

This section covers the __init__ method and object initialization.

SOLID Principle: Single Responsibility
- Constructors should only initialize objects

Design Pattern: Builder Pattern
- Constructors build objects with required state
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import uuid


def demonstrate_constructor_basics():
    """
    Demonstrates basic __init__ constructor usage.
    
    The __init__ method runs automatically when an object is created.
    """
    print("=" * 60)
    print("SECTION 1A: __init__ CONSTRUCTOR BASICS")
    print("=" * 60)
    
    # SIMPLE CONSTRUCTOR
    print("\n1. SIMPLE CONSTRUCTOR")
    print("-" * 40)
    
    class Person:
        """Simple Person class with constructor."""
        
        def __init__(self, name: str, age: int):
            """Initialize a new Person."""
            print(f"  Creating Person: {name}")
            self.name = name
            self.age = age
            self.created_at = datetime.now()
        
        def introduce(self):
            """Introduce the person."""
            return f"Hello, I'm {self.name}, age {self.age}"
    
    # Creating objects automatically calls __init__
    alice = Person("Alice", 28)
    bob = Person("Bob", 35)
    
    print(f"  Alice: {alice.introduce()}")
    print(f"  Bob: {bob.introduce()}")
    print(f"  Alice created at: {alice.created_at.strftime('%H:%M:%S')}")
    
    # CONSTRUCTOR WITH DEFAULT VALUES
    print("\n2. CONSTRUCTOR WITH DEFAULT VALUES")
    print("-" * 40)
    
    class Product:
        """Product with default values in constructor."""
        
        def __init__(self, name: str, price: float, category: str = "General", in_stock: bool = True):
            self.name = name
            self.price = price
            self.category = category
            self.in_stock = in_stock
            self.sku = f"SKU-{uuid.uuid4().hex[:8].upper()}"
        
        def __str__(self):
            stock = "✓" if self.in_stock else "✗"
            return f"{self.name}: ${self.price:.2f} [{self.category}] {stock}"
    
    laptop = Product("Laptop", 999.99, "Electronics")
    mouse = Product("Mouse", 29.99)  # Uses default category
    notebook = Product("Notebook", 4.99, "Stationery", True)
    
    print(f"  {laptop}")
    print(f"  {mouse}")
    print(f"  {notebook}")
    
    # CONSTRUCTOR WITH VALIDATION
    print("\n3. CONSTRUCTOR WITH VALIDATION")
    print("-" * 40)
    
    class BankAccount:
        """Bank account with validation in constructor."""
        
        def __init__(self, account_holder: str, initial_balance: float = 0.0):
            # Validation
            if not account_holder or len(account_holder) < 2:
                raise ValueError("Account holder name must be at least 2 characters")
            
            if initial_balance < 0:
                raise ValueError("Initial balance cannot be negative")
            
            self.account_holder = account_holder
            self.balance = initial_balance
            self.account_number = f"ACC-{uuid.uuid4().hex[:8].upper()}"
            self.transactions = []
            
            if initial_balance > 0:
                self._record_transaction(initial_balance, "Initial deposit")
        
        def _record_transaction(self, amount: float, description: str):
            self.transactions.append({
                "amount": amount,
                "description": description,
                "timestamp": datetime.now()
            })
        
        def __str__(self):
            return f"Account {self.account_number}: {self.account_holder} - ${self.balance:.2f}"
    
    try:
        valid_account = BankAccount("Alice Chen", 1000)
        print(f"  Created: {valid_account}")
        
        invalid_name = BankAccount("A", 100)  # Too short
    except ValueError as e:
        print(f"  Error creating account: {e}")
    
    try:
        invalid_balance = BankAccount("Bob Smith", -50)  # Negative balance
    except ValueError as e:
        print(f"  Error creating account: {e}")


def demonstrate_constructor_vs_methods():
    """
    Demonstrates the difference between constructor and regular methods.
    
    Constructor runs once at creation; methods can be called multiple times.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: CONSTRUCTOR VS REGULAR METHODS")
    print("=" * 60)
    
    class Counter:
        """Counter demonstrating constructor vs method execution."""
        
        def __init__(self, start: int = 0):
            """Constructor - runs once when object is created."""
            print(f"  __init__ called: initializing counter to {start}")
            self.count = start
            self.initialized_at = datetime.now()
        
        def increment(self, amount: int = 1):
            """Regular method - can be called multiple times."""
            print(f"  increment({amount}) called")
            self.count += amount
            return self.count
        
        def decrement(self, amount: int = 1):
            """Regular method - can be called multiple times."""
            print(f"  decrement({amount}) called")
            self.count -= amount
            return self.count
    
    # Constructor runs automatically
    print("\n  Creating counter:")
    counter = Counter(10)
    
    # Methods can be called many times
    print("\n  Calling methods:")
    counter.increment(5)
    counter.increment(3)
    counter.decrement(2)
    print(f"  Final count: {counter.count}")
    
    # Constructor runs ONCE per object
    print("\n  Creating another counter:")
    another = Counter(100)
    print(f"  Another counter count: {another.count}")
    
    # IMPORTANT: Constructor vs __new__
    print("\n4. __init__ VS __new__")
    print("-" * 40)
    
    class Example:
        def __new__(cls, *args, **kwargs):
            print(f"  __new__ called (creates the object)")
            instance = super().__new__(cls)
            return instance
        
        def __init__(self, value):
            print(f"  __init__ called (initializes the object)")
            self.value = value
    
    obj = Example(42)
    print(f"  Object created with value: {obj.value}")
    
    print("\n  __new__ creates the object; __init__ initializes it")
    print("  You rarely need to override __new__ - use __init__ instead")


def demonstrate_constructor_with_complex_initialization():
    """
    Demonstrates complex initialization logic in constructors.
    
    Constructors can compute derived attributes and set up relationships.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: COMPLEX INITIALIZATION")
    print("=" * 60)
    
    class Order:
        """Order with complex initialization logic."""
        
        def __init__(self, customer_name: str, items: List[Tuple[str, float, int]]):
            """
            Initialize an order with items.
            
            Args:
                customer_name: Name of the customer
                items: List of (product_name, unit_price, quantity)
            """
            self.order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            self.customer_name = customer_name
            self.created_at = datetime.now()
            self.status = "pending"
            
            # Initialize items
            self.items = []
            for name, price, qty in items:
                self.items.append({
                    "name": name,
                    "price": price,
                    "quantity": qty,
                    "subtotal": price * qty
                })
            
            # Calculate derived values
            self.subtotal = sum(item["subtotal"] for item in self.items)
            self.tax = round(self.subtotal * 0.08, 2)
            self.total = self.subtotal + self.tax
            
            # Apply discount logic
            if self.subtotal > 500:
                self.discount = round(self.subtotal * 0.10, 2)
                self.total -= self.discount
                self.discount_applied = "10% off"
            else:
                self.discount = 0
                self.discount_applied = None
            
            # Generate tracking number if needed
            if self.total > 100:
                self.tracking_number = f"TRK-{uuid.uuid4().hex[:8].upper()}"
            else:
                self.tracking_number = None
        
        def get_summary(self) -> Dict:
            """Get order summary."""
            return {
                "order_id": self.order_id,
                "customer": self.customer_name,
                "created_at": self.created_at.isoformat(),
                "status": self.status,
                "subtotal": self.subtotal,
                "discount": self.discount,
                "discount_applied": self.discount_applied,
                "tax": self.tax,
                "total": self.total,
                "tracking_number": self.tracking_number,
                "item_count": len(self.items)
            }
        
        def __str__(self):
            return f"Order {self.order_id}: {self.customer_name} - ${self.total:.2f}"
    
    # Create orders with different values
    print("\n1. SMALL ORDER")
    print("-" * 40)
    
    small_order = Order("Alice Chen", [
        ("Mouse", 29.99, 1),
        ("Keyboard", 75.00, 1)
    ])
    
    print(f"  {small_order}")
    print(f"  Subtotal: ${small_order.subtotal:.2f}")
    print(f"  Tax: ${small_order.tax:.2f}")
    print(f"  Total: ${small_order.total:.2f}")
    print(f"  Tracking: {small_order.tracking_number}")
    
    print("\n2. LARGE ORDER (with discount and tracking)")
    print("-" * 40)
    
    large_order = Order("Bob Smith", [
        ("Laptop", 999.99, 1),
        ("Monitor", 299.99, 1),
        ("Mouse", 29.99, 2)
    ])
    
    print(f"  {large_order}")
    print(f"  Subtotal: ${large_order.subtotal:.2f}")
    print(f"  Discount: ${large_order.discount:.2f} ({large_order.discount_applied})")
    print(f"  Tax: ${large_order.tax:.2f}")
    print(f"  Total: ${large_order.total:.2f}")
    print(f"  Tracking: {large_order.tracking_number}")


if __name__ == "__main__":
    demonstrate_constructor_basics()
    demonstrate_constructor_vs_methods()
    demonstrate_constructor_with_complex_initialization()
```

---

## 🏢 Section 2: Employee Onboarding System

A complete employee onboarding system demonstrating constructors with validation, derived attributes, and complex initialization.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of employee management
- Open/Closed: New employee types can be added

**Design Patterns:**
- Factory Pattern: Creates employees with proper initialization
- Builder Pattern: Builds employee profiles incrementally

```python
"""
EMPLOYEE ONBOARDING SYSTEM

This section builds a complete employee onboarding system using constructors.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New employee types can be added

Design Patterns:
- Factory Pattern: Creates employees with proper initialization
- Builder Pattern: Builds employee profiles incrementally
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, date
from enum import Enum
from dataclasses import dataclass
import uuid
import re


class Department(Enum):
    """Company departments."""
    ENGINEERING = "Engineering"
    SALES = "Sales"
    MARKETING = "Marketing"
    HUMAN_RESOURCES = "Human Resources"
    FINANCE = "Finance"
    OPERATIONS = "Operations"


class EmploymentType(Enum):
    """Types of employment."""
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"
    CONTRACT = "Contract"
    INTERN = "Intern"


class EmployeeLevel(Enum):
    """Employee seniority levels."""
    ENTRY = 1
    JUNIOR = 2
    MID = 3
    SENIOR = 4
    LEAD = 5
    MANAGER = 6
    DIRECTOR = 7
    EXECUTIVE = 8


@dataclass
class Address:
    """Value object for employee address."""
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"
    
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
    
    def to_dict(self) -> Dict:
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip": self.zip_code,
            "country": self.country
        }


@dataclass
class ContactInfo:
    """Value object for contact information."""
    email: str
    phone: str
    emergency_contact_name: str
    emergency_contact_phone: str
    
    def __post_init__(self):
        self._validate_email()
        self._validate_phone()
    
    def _validate_email(self):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, self.email):
            raise ValueError(f"Invalid email: {self.email}")
    
    def _validate_phone(self):
        """Validate phone number."""
        digits = re.sub(r'\D', '', self.phone)
        if len(digits) < 10:
            raise ValueError(f"Invalid phone: {self.phone}")
    
    def to_dict(self) -> Dict:
        return {
            "email": self.email,
            "phone": self.phone,
            "emergency_contact": self.emergency_contact_name,
            "emergency_phone": self.emergency_contact_phone
        }


class Employee:
    """
    Employee class with comprehensive constructor validation.
    
    SOLID: Single Responsibility - Represents an employee
    """
    
    def __init__(self, first_name: str, last_name: str, email: str,
                 department: Department, employment_type: EmploymentType,
                 start_date: date, salary: float, address: Address,
                 contact: ContactInfo, level: EmployeeLevel = EmployeeLevel.ENTRY):
        """
        Initialize a new employee with validation.
        
        Args:
            first_name: Employee's first name
            last_name: Employee's last name
            email: Work email address
            department: Department assignment
            employment_type: Full-time, part-time, etc.
            start_date: Date of employment
            salary: Annual salary
            address: Physical address
            contact: Contact information
            level: Seniority level (default ENTRY)
        """
        # Basic validation
        self._validate_name(first_name, "First name")
        self._validate_name(last_name, "Last name")
        self._validate_salary(salary)
        
        self.employee_id = f"EMP-{uuid.uuid4().hex[:8].upper()}"
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department = department
        self.employment_type = employment_type
        self.start_date = start_date
        self.salary = salary
        self.address = address
        self.contact = contact
        self.level = level
        self.is_active = True
        self.created_at = datetime.now()
        
        # Derived attributes
        self.full_name = f"{first_name} {last_name}"
        self.years_of_service = self._calculate_years_of_service()
        self.pay_frequency = self._determine_pay_frequency()
        
        # Initialize empty collections
        self.dependents: List[Dict] = []
        self.performance_reviews: List[Dict] = []
        self.time_off_requests: List[Dict] = []
    
    def _validate_name(self, name: str, field: str) -> None:
        """Validate name fields."""
        if not name or len(name) < 2:
            raise ValueError(f"{field} must be at least 2 characters")
        if not name.replace(" ", "").replace("-", "").isalpha():
            raise ValueError(f"{field} can only contain letters, spaces, and hyphens")
    
    def _validate_salary(self, salary: float) -> None:
        """Validate salary."""
        if salary <= 0:
            raise ValueError("Salary must be positive")
        
        if self.employment_type == EmploymentType.FULL_TIME and salary < 30000:
            raise ValueError("Full-time salary must be at least $30,000")
        
        if self.employment_type == EmploymentType.INTERN and salary > 60000:
            raise ValueError("Intern salary seems too high")
    
    def _calculate_years_of_service(self) -> float:
        """Calculate years of service based on start date."""
        today = date.today()
        days = (today - self.start_date).days
        return round(days / 365.25, 1)
    
    def _determine_pay_frequency(self) -> str:
        """Determine pay frequency based on employment type."""
        if self.employment_type == EmploymentType.FULL_TIME:
            return "Bi-weekly"
        elif self.employment_type == EmploymentType.PART_TIME:
            return "Weekly"
        elif self.employment_type == EmploymentType.CONTRACT:
            return "Monthly"
        else:
            return "Bi-weekly"
    
    def get_yearly_compensation(self) -> float:
        """Calculate total yearly compensation including benefits."""
        # Base salary
        total = self.salary
        
        # Bonus based on level
        bonus_percent = {1: 0, 2: 5, 3: 10, 4: 15, 5: 20, 6: 25, 7: 35, 8: 50}
        bonus = self.salary * (bonus_percent.get(self.level.value, 0) / 100)
        total += bonus
        
        # Years of service bonus
        service_bonus = self.salary * min(0.10, self.years_of_service * 0.01)
        total += service_bonus
        
        return round(total, 2)
    
    def promote(self, new_level: EmployeeLevel, new_salary: Optional[float] = None) -> None:
        """Promote the employee."""
        if new_level.value <= self.level.value:
            raise ValueError(f"New level must be higher than current ({self.level.name})")
        
        self.level = new_level
        
        if new_salary:
            self._validate_salary(new_salary)
            self.salary = new_salary
        
        self.performance_reviews.append({
            "type": "promotion",
            "new_level": new_level.name,
            "new_salary": self.salary,
            "date": datetime.now().isoformat()
        })
        
        print(f"  {self.full_name} promoted to {new_level.name}")
    
    def add_dependent(self, name: str, relationship: str, birth_date: date) -> None:
        """Add a dependent to the employee's record."""
        self.dependents.append({
            "name": name,
            "relationship": relationship,
            "birth_date": birth_date.isoformat(),
            "added_at": datetime.now().isoformat()
        })
    
    def request_time_off(self, start_date: date, end_date: date, reason: str) -> str:
        """Request time off."""
        request_id = f"TO-{uuid.uuid4().hex[:6].upper()}"
        days = (end_date - start_date).days + 1
        
        self.time_off_requests.append({
            "id": request_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "days": days,
            "reason": reason,
            "status": "pending",
            "requested_at": datetime.now().isoformat()
        })
        
        return request_id
    
    def approve_time_off(self, request_id: str) -> bool:
        """Approve a time off request."""
        for request in self.time_off_requests:
            if request["id"] == request_id and request["status"] == "pending":
                request["status"] = "approved"
                request["approved_at"] = datetime.now().isoformat()
                return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert employee to dictionary."""
        return {
            "employee_id": self.employee_id,
            "full_name": self.full_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "department": self.department.value,
            "employment_type": self.employment_type.value,
            "level": self.level.name,
            "start_date": self.start_date.isoformat(),
            "salary": self.salary,
            "years_of_service": self.years_of_service,
            "address": self.address.to_dict(),
            "contact": self.contact.to_dict(),
            "is_active": self.is_active,
            "dependents": self.dependents,
            "performance_reviews": self.performance_reviews[-5:]
        }
    
    def get_summary(self) -> str:
        """Get employee summary."""
        return f"""
        ========================================
        EMPLOYEE SUMMARY
        ========================================
        ID: {self.employee_id}
        Name: {self.full_name}
        Department: {self.department.value}
        Level: {self.level.name}
        Employment: {self.employment_type.value}
        Start Date: {self.start_date.strftime('%Y-%m-%d')}
        Years of Service: {self.years_of_service}
        Salary: ${self.salary:,.2f}
        Total Compensation: ${self.get_yearly_compensation():,.2f}
        Status: {'Active' if self.is_active else 'Inactive'}
        ========================================
        """
    
    def __str__(self) -> str:
        return f"{self.full_name} - {self.department.value} ({self.level.name})"


class EmployeeOnboarding:
    """
    Manages the employee onboarding process.
    
    Design Pattern: Builder Pattern - Builds employee profiles step by step
    """
    
    def __init__(self):
        self.employees: Dict[str, Employee] = {}
    
    def onboard_employee(self, first_name: str, last_name: str, email: str,
                         department: Department, employment_type: EmploymentType,
                         start_date: date, salary: float,
                         street: str, city: str, state: str, zip_code: str,
                         phone: str, emergency_name: str, emergency_phone: str,
                         level: EmployeeLevel = EmployeeLevel.ENTRY) -> Employee:
        """
        Onboard a new employee with all required information.
        
        Returns:
            Created Employee object
        """
        # Create address
        address = Address(street, city, state, zip_code)
        
        # Create contact info
        contact = ContactInfo(email, phone, emergency_name, emergency_phone)
        
        # Create employee (constructor handles validation)
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            employment_type=employment_type,
            start_date=start_date,
            salary=salary,
            address=address,
            contact=contact,
            level=level
        )
        
        self.employees[employee.employee_id] = employee
        print(f"  ✅ Onboarded: {employee.full_name} ({employee.employee_id})")
        
        return employee
    
    def get_employee(self, employee_id: str) -> Optional[Employee]:
        """Get employee by ID."""
        return self.employees.get(employee_id)
    
    def get_employees_by_department(self, department: Department) -> List[Employee]:
        """Get all employees in a department."""
        return [e for e in self.employees.values() if e.department == department]
    
    def get_employees_by_level(self, level: EmployeeLevel) -> List[Employee]:
        """Get all employees at a specific level."""
        return [e for e in self.employees.values() if e.level == level]
    
    def get_employees_hiring_anniversary(self, month: int) -> List[Employee]:
        """Get employees with hiring anniversary in given month."""
        return [e for e in self.employees.values() if e.start_date.month == month]
    
    def generate_org_chart(self) -> Dict:
        """Generate organizational chart."""
        org_chart = {}
        for dept in Department:
            employees = self.get_employees_by_department(dept)
            if employees:
                org_chart[dept.value] = [
                    {
                        "name": e.full_name,
                        "level": e.level.name,
                        "id": e.employee_id
                    }
                    for e in sorted(employees, key=lambda x: x.level.value, reverse=True)
                ]
        return org_chart
    
    def get_statistics(self) -> Dict:
        """Get employee statistics."""
        employees = self.employees.values()
        
        if not employees:
            return {"total": 0}
        
        total_salary = sum(e.salary for e in employees)
        avg_salary = total_salary / len(employees)
        
        return {
            "total_employees": len(employees),
            "active_employees": sum(1 for e in employees if e.is_active),
            "departments": len(set(e.department for e in employees)),
            "total_salary": round(total_salary, 2),
            "average_salary": round(avg_salary, 2),
            "by_department": {
                dept.value: len(self.get_employees_by_department(dept))
                for dept in Department
            },
            "by_level": {
                level.name: len(self.get_employees_by_level(level))
                for level in EmployeeLevel
            }
        }


def demonstrate_onboarding_system():
    """
    Demonstrate the employee onboarding system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: EMPLOYEE ONBOARDING SYSTEM")
    print("=" * 60)
    
    onboarding = EmployeeOnboarding()
    
    print("\n1. ONBOARDING EMPLOYEES")
    print("-" * 40)
    
    # Onboard employees
    alice = onboarding.onboard_employee(
        first_name="Alice", last_name="Chen", email="alice.chen@metromap.com",
        department=Department.ENGINEERING, employment_type=EmploymentType.FULL_TIME,
        start_date=date(2023, 6, 15), salary=95000,
        street="123 Tech Lane", city="San Francisco", state="CA", zip_code="94105",
        phone="555-0101", emergency_name="Bob Chen", emergency_phone="555-0102",
        level=EmployeeLevel.SENIOR
    )
    
    bob = onboarding.onboard_employee(
        first_name="Bob", last_name="Smith", email="bob.smith@metromap.com",
        department=Department.SALES, employment_type=EmploymentType.FULL_TIME,
        start_date=date(2024, 1, 10), salary=75000,
        street="456 Market St", city="San Francisco", state="CA", zip_code="94105",
        phone="555-0201", emergency_name="Jane Smith", emergency_phone="555-0202",
        level=EmployeeLevel.JUNIOR
    )
    
    charlie = onboarding.onboard_employee(
        first_name="Charlie", last_name="Brown", email="charlie.brown@metromap.com",
        department=Department.ENGINEERING, employment_type=EmploymentType.INTERN,
        start_date=date(2024, 6, 1), salary=45000,
        street="789 Innovation Dr", city="San Francisco", state="CA", zip_code="94105",
        phone="555-0301", emergency_name="Diana Brown", emergency_phone="555-0302",
        level=EmployeeLevel.ENTRY
    )
    
    print("\n2. EMPLOYEE SUMMARIES")
    print("-" * 40)
    
    for emp in [alice, bob, charlie]:
        print(emp.get_summary())
    
    print("\n3. PROMOTIONS AND UPDATES")
    print("-" * 40)
    
    # Promote Alice
    alice.promote(EmployeeLevel.LEAD, 120000)
    print(f"  Alice's new salary: ${alice.salary:,.2f}")
    print(f"  Alice's new compensation: ${alice.get_yearly_compensation():,.2f}")
    
    # Add dependent for Alice
    alice.add_dependent("Emma Chen", "Daughter", date(2020, 5, 10))
    print(f"  Added dependent for Alice")
    
    print("\n4. TIME OFF REQUEST")
    print("-" * 40)
    
    request_id = bob.request_time_off(
        start_date=date(2024, 7, 15),
        end_date=date(2024, 7, 22),
        reason="Vacation"
    )
    print(f"  Time off request created: {request_id}")
    
    bob.approve_time_off(request_id)
    print(f"  Time off request approved")
    
    print("\n5. ORGANIZATIONAL CHART")
    print("-" * 40)
    
    org_chart = onboarding.generate_org_chart()
    for dept, employees in org_chart.items():
        print(f"\n  {dept}:")
        for emp in employees:
            print(f"    {emp['level']}: {emp['name']}")
    
    print("\n6. EMPLOYEE STATISTICS")
    print("-" * 40)
    
    stats = onboarding.get_statistics()
    for key, value in stats.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for k, v in value.items():
                if v > 0:
                    print(f"    {k}: {v}")
        else:
            print(f"  {key}: {value}")
    
    print("\n7. DEPARTMENT ROSTER")
    print("-" * 40)
    
    eng_employees = onboarding.get_employees_by_department(Department.ENGINEERING)
    print(f"  Engineering Department ({len(eng_employees)} employees):")
    for emp in eng_employees:
        print(f"    {emp.full_name} - {emp.level.name}")


if __name__ == "__main__":
    demonstrate_onboarding_system()
```

---

## 🏭 Section 3: Multiple Constructors with Class Methods

Python doesn't support multiple constructors directly, but you can create alternative constructors using class methods.

**SOLID Principle Applied: Single Responsibility** – Each constructor method handles one way of creating objects.

**Design Pattern: Factory Method Pattern** – Class methods act as alternative constructors.

```python
"""
MULTIPLE CONSTRUCTORS WITH CLASS METHODS

This section demonstrates alternative constructors using class methods.

SOLID Principle: Single Responsibility
- Each constructor handles one creation method

Design Pattern: Factory Method Pattern
- Class methods act as alternative constructors
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, date
import json
import csv
from io import StringIO


class Product:
    """
    Product with multiple constructors.
    
    Design Pattern: Factory Method Pattern - Multiple creation methods
    """
    
    def __init__(self, sku: str, name: str, price: float, category: str, in_stock: bool = True):
        self.sku = sku
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        self.created_at = datetime.now()
    
    # Standard constructor
    @classmethod
    def create(cls, sku: str, name: str, price: float, category: str, in_stock: bool = True) -> 'Product':
        """Standard constructor (same as __init__)."""
        return cls(sku, name, price, category, in_stock)
    
    # Alternative constructor from dictionary
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create Product from dictionary."""
        return cls(
            sku=data['sku'],
            name=data['name'],
            price=data['price'],
            category=data['category'],
            in_stock=data.get('in_stock', True)
        )
    
    # Alternative constructor from CSV row
    @classmethod
    def from_csv_row(cls, row: List[str]) -> 'Product':
        """Create Product from CSV row."""
        return cls(
            sku=row[0],
            name=row[1],
            price=float(row[2]),
            category=row[3],
            in_stock=row[4].lower() == 'true'
        )
    
    # Alternative constructor from JSON string
    @classmethod
    def from_json(cls, json_str: str) -> 'Product':
        """Create Product from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    # Alternative constructor with discount
    @classmethod
    def create_with_discount(cls, sku: str, name: str, base_price: float, 
                             category: str, discount_percent: float) -> 'Product':
        """Create product with discount applied."""
        discounted_price = base_price * (1 - discount_percent / 100)
        return cls(sku, name, round(discounted_price, 2), category)
    
    # Alternative constructor for premium products
    @classmethod
    def create_premium(cls, sku: str, name: str, price: float) -> 'Product':
        """Create a premium product."""
        return cls(sku, name, price, "Premium", True)
    
    def __str__(self) -> str:
        return f"{self.sku}: {self.name} - ${self.price:.2f} [{self.category}]"


class DateRange:
    """
    Date range with multiple constructors.
    
    Design Pattern: Factory Method Pattern - Multiple creation methods
    """
    
    def __init__(self, start_date: date, end_date: date):
        if start_date > end_date:
            raise ValueError("Start date must be before end date")
        self.start_date = start_date
        self.end_date = end_date
    
    @classmethod
    def from_strings(cls, start_str: str, end_str: str, format_str: str = "%Y-%m-%d") -> 'DateRange':
        """Create DateRange from date strings."""
        start = datetime.strptime(start_str, format_str).date()
        end = datetime.strptime(end_str, format_str).date()
        return cls(start, end)
    
    @classmethod
    def from_days(cls, start_date: date, days: int) -> 'DateRange':
        """Create DateRange from start date and number of days."""
        end_date = start_date + timedelta(days=days)
        return cls(start_date, end_date)
    
    @classmethod
    def this_week(cls) -> 'DateRange':
        """Create DateRange for current week."""
        today = date.today()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return cls(start, end)
    
    @classmethod
    def this_month(cls) -> 'DateRange':
        """Create DateRange for current month."""
        today = date.today()
        start = date(today.year, today.month, 1)
        if today.month == 12:
            end = date(today.year + 1, 1, 1) - timedelta(days=1)
        else:
            end = date(today.year, today.month + 1, 1) - timedelta(days=1)
        return cls(start, end)
    
    @classmethod
    def last_n_days(cls, n: int) -> 'DateRange':
        """Create DateRange for last N days."""
        end = date.today()
        start = end - timedelta(days=n - 1)
        return cls(start, end)
    
    def __str__(self) -> str:
        return f"{self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}"


class Config:
    """
    Configuration with multiple constructors.
    
    Design Pattern: Factory Method Pattern - Multiple creation methods
    """
    
    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        self.loaded_at = datetime.now()
    
    @classmethod
    def from_dict(cls, settings: Dict) -> 'Config':
        """Create Config from dictionary."""
        return cls(settings)
    
    @classmethod
    def from_json_file(cls, filepath: str) -> 'Config':
        """Create Config from JSON file."""
        with open(filepath, 'r') as f:
            settings = json.load(f)
        return cls(settings)
    
    @classmethod
    def from_env_vars(cls, prefix: str = "APP_") -> 'Config':
        """Create Config from environment variables."""
        import os
        settings = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                settings[key[len(prefix):].lower()] = value
        return cls(settings)
    
    @classmethod
    def default(cls) -> 'Config':
        """Create default configuration."""
        default_settings = {
            "debug": False,
            "host": "localhost",
            "port": 8080,
            "log_level": "INFO",
            "max_connections": 100
        }
        return cls(default_settings)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self.settings.get(key, default)
    
    def __str__(self) -> str:
        return f"Config({len(self.settings)} settings, loaded at {self.loaded_at.strftime('%H:%M:%S')})"


def demonstrate_multiple_constructors():
    """
    Demonstrate multiple constructor patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: MULTIPLE CONSTRUCTORS")
    print("=" * 60)
    
    # PRODUCT EXAMPLES
    print("\n1. PRODUCT MULTIPLE CONSTRUCTORS")
    print("-" * 40)
    
    # Standard constructor
    product1 = Product("P001", "Laptop", 999.99, "Electronics")
    print(f"  Standard: {product1}")
    
    # From dictionary
    product2 = Product.from_dict({
        "sku": "P002",
        "name": "Mouse",
        "price": 29.99,
        "category": "Electronics",
        "in_stock": True
    })
    print(f"  From dict: {product2}")
    
    # From CSV row
    csv_row = ["P003", "Keyboard", "89.99", "Electronics", "true"]
    product3 = Product.from_csv_row(csv_row)
    print(f"  From CSV: {product3}")
    
    # From JSON
    json_str = '{"sku": "P004", "name": "Monitor", "price": 299.99, "category": "Electronics"}'
    product4 = Product.from_json(json_str)
    print(f"  From JSON: {product4}")
    
    # With discount
    product5 = Product.create_with_discount("P005", "Premium Laptop", 1500.00, "Electronics", 15)
    print(f"  With discount: {product5}")
    
    # Premium product
    product6 = Product.create_premium("P006", "Ultra Premium", 2500.00)
    print(f"  Premium: {product6}")
    
    # DATE RANGE EXAMPLES
    print("\n2. DATE RANGE MULTIPLE CONSTRUCTORS")
    print("-" * 40)
    
    from datetime import timedelta
    
    # From strings
    range1 = DateRange.from_strings("2024-01-01", "2024-01-31")
    print(f"  From strings: {range1}")
    
    # From days
    range2 = DateRange.from_days(date(2024, 6, 1), 7)
    print(f"  From days: {range2}")
    
    # This week
    range3 = DateRange.this_week()
    print(f"  This week: {range3}")
    
    # This month
    range4 = DateRange.this_month()
    print(f"  This month: {range4}")
    
    # Last N days
    range5 = DateRange.last_n_days(30)
    print(f"  Last 30 days: {range5}")
    
    # CONFIGURATION EXAMPLES
    print("\n3. CONFIGURATION MULTIPLE CONSTRUCTORS")
    print("-" * 40)
    
    # Default config
    config1 = Config.default()
    print(f"  Default: {config1}")
    print(f"    debug: {config1.get('debug')}")
    print(f"    port: {config1.get('port')}")
    
    # From dict
    config2 = Config.from_dict({
        "debug": True,
        "host": "192.168.1.100",
        "port": 9090
    })
    print(f"  From dict: {config2}")
    
    # ADVANTAGES OF MULTIPLE CONSTRUCTORS
    print("\n4. ADVANTAGES OF MULTIPLE CONSTRUCTORS")
    print("-" * 40)
    
    print("""
    Benefits:
    ✓ Flexible object creation from different data sources
    ✓ Clear intent (method names describe the creation method)
    ✓ Encapsulates conversion logic
    ✓ Makes code more readable and maintainable
    ✓ Allows default configurations
    
    Common use cases:
    - Creating objects from database records
    - Parsing API responses
    - Reading configuration files
    - Creating test fixtures
    - Providing sensible defaults
    """)


if __name__ == "__main__":
    from datetime import timedelta
    demonstrate_multiple_constructors()
```

---

## 🏛️ Section 4: Complete Order Management System

A complete order management system demonstrating constructors with validation, derived data, and relationships between objects.

**SOLID Principles Applied:**
- Single Responsibility: Each class has one purpose
- Dependency Inversion: Depends on abstractions

**Design Patterns:**
- Factory Pattern: Creates orders with validation
- Builder Pattern: Builds complex orders

```python
"""
COMPLETE ORDER MANAGEMENT SYSTEM

This section builds a complete order management system with constructors.

SOLID Principles Applied:
- Single Responsibility: Each class has one purpose
- Dependency Inversion: Depends on abstractions

Design Patterns:
- Factory Pattern: Creates orders with validation
- Builder Pattern: Builds complex orders
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, date
from enum import Enum
from dataclasses import dataclass
import uuid
import random


class OrderStatus(Enum):
    """Order status values."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class PaymentMethod(Enum):
    """Payment methods."""
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"


class ShippingMethod(Enum):
    """Shipping methods."""
    STANDARD = "standard"
    EXPEDITED = "expedited"
    EXPRESS = "express"
    OVERNIGHT = "overnight"


@dataclass
class Address:
    """Shipping address value object."""
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"
    
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
    
    def validate(self) -> Tuple[bool, List[str]]:
        """Validate address."""
        errors = []
        if not self.street:
            errors.append("Street is required")
        if not self.city:
            errors.append("City is required")
        if len(self.state) != 2:
            errors.append("State must be 2-letter code")
        if not self.zip_code or not self.zip_code.isdigit():
            errors.append("ZIP code must contain only digits")
        return len(errors) == 0, errors


@dataclass
class OrderItem:
    """Item in an order."""
    product_id: str
    product_name: str
    quantity: int
    unit_price: float
    
    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price
    
    def to_dict(self) -> Dict:
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.subtotal
        }


class Order:
    """
    Order class with comprehensive constructor validation.
    
    SOLID: Single Responsibility - Manages a single order
    """
    
    def __init__(self, customer_id: str, customer_name: str, customer_email: str,
                 items: List[OrderItem], shipping_address: Address,
                 payment_method: PaymentMethod, shipping_method: ShippingMethod = ShippingMethod.STANDARD):
        """
        Initialize a new order with validation.
        
        Args:
            customer_id: Unique customer identifier
            customer_name: Customer's full name
            customer_email: Customer's email address
            items: List of order items
            shipping_address: Shipping destination
            payment_method: How customer will pay
            shipping_method: Shipping speed preference
        """
        # Validate inputs
        self._validate_customer(customer_name, customer_email)
        self._validate_items(items)
        self._validate_address(shipping_address)
        
        # Initialize order
        self.order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.items = items
        self.shipping_address = shipping_address
        self.payment_method = payment_method
        self.shipping_method = shipping_method
        self.created_at = datetime.now()
        self.status = OrderStatus.PENDING
        self.payment_status = "pending"
        self.tracking_number = None
        
        # Calculate financials
        self.subtotal = sum(item.subtotal for item in items)
        self.shipping_cost = self._calculate_shipping()
        self.tax = round(self.subtotal * 0.08, 2)
        self.discount = self._calculate_discount()
        self.total = self.subtotal + self.shipping_cost + self.tax - self.discount
        
        # Apply free shipping if eligible
        if self._is_eligible_for_free_shipping():
            self.shipping_cost = 0
            self.total -= self.shipping_cost
        
        # Round to 2 decimals
        self.subtotal = round(self.subtotal, 2)
        self.shipping_cost = round(self.shipping_cost, 2)
        self.tax = round(self.tax, 2)
        self.discount = round(self.discount, 2)
        self.total = round(self.total, 2)
    
    def _validate_customer(self, name: str, email: str) -> None:
        """Validate customer information."""
        if not name or len(name) < 2:
            raise ValueError("Customer name must be at least 2 characters")
        if '@' not in email or '.' not in email:
            raise ValueError("Invalid email address")
    
    def _validate_items(self, items: List[OrderItem]) -> None:
        """Validate order items."""
        if not items:
            raise ValueError("Order must contain at least one item")
        for item in items:
            if item.quantity <= 0:
                raise ValueError(f"Invalid quantity for {item.product_name}")
            if item.unit_price <= 0:
                raise ValueError(f"Invalid price for {item.product_name}")
    
    def _validate_address(self, address: Address) -> None:
        """Validate shipping address."""
        is_valid, errors = address.validate()
        if not is_valid:
            raise ValueError(f"Invalid address: {', '.join(errors)}")
    
    def _calculate_shipping(self) -> float:
        """Calculate shipping cost based on items and method."""
        base_cost = 5.99
        
        # Weight factor (simplified - based on item count)
        item_count = sum(item.quantity for item in self.items)
        weight_factor = max(1, item_count // 3)
        
        # Method multiplier
        method_multipliers = {
            ShippingMethod.STANDARD: 1.0,
            ShippingMethod.EXPEDITED: 1.5,
            ShippingMethod.EXPRESS: 2.0,
            ShippingMethod.OVERNIGHT: 3.0
        }
        
        cost = base_cost * weight_factor * method_multipliers.get(self.shipping_method, 1.0)
        return min(cost, 50.0)  # Cap at $50
    
    def _calculate_discount(self) -> float:
        """Calculate applicable discounts."""
        discount = 0.0
        
        # Volume discount
        item_count = sum(item.quantity for item in self.items)
        if item_count >= 10:
            discount += self.subtotal * 0.10
        elif item_count >= 5:
            discount += self.subtotal * 0.05
        
        # High-value order discount
        if self.subtotal >= 500:
            discount += self.subtotal * 0.05
        
        return min(discount, self.subtotal * 0.20)  # Max 20% discount
    
    def _is_eligible_for_free_shipping(self) -> bool:
        """Check if order qualifies for free shipping."""
        return self.subtotal >= 100 or self.shipping_method == ShippingMethod.EXPRESS
    
    def confirm(self) -> bool:
        """Confirm the order."""
        if self.status != OrderStatus.PENDING:
            return False
        
        self.status = OrderStatus.CONFIRMED
        print(f"  Order {self.order_id} confirmed")
        return True
    
    def process_payment(self) -> bool:
        """Process payment for the order."""
        if self.status not in [OrderStatus.PENDING, OrderStatus.CONFIRMED]:
            return False
        
        # Simulate payment processing
        success = random.random() < 0.95
        
        if success:
            self.payment_status = "paid"
            self.status = OrderStatus.PROCESSING
            print(f"  Payment processed for order {self.order_id}")
        else:
            self.payment_status = "failed"
            print(f"  Payment failed for order {self.order_id}")
        
        return success
    
    def ship(self, tracking_number: str) -> bool:
        """Mark order as shipped."""
        if self.status != OrderStatus.PROCESSING:
            return False
        
        self.status = OrderStatus.SHIPPED
        self.tracking_number = tracking_number
        print(f"  Order {self.order_id} shipped. Tracking: {tracking_number}")
        return True
    
    def deliver(self) -> bool:
        """Mark order as delivered."""
        if self.status != OrderStatus.SHIPPED:
            return False
        
        self.status = OrderStatus.DELIVERED
        print(f"  Order {self.order_id} delivered")
        return True
    
    def cancel(self) -> bool:
        """Cancel the order."""
        if self.status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
            return False
        
        self.status = OrderStatus.CANCELLED
        print(f"  Order {self.order_id} cancelled")
        return True
    
    def get_summary(self) -> Dict:
        """Get order summary."""
        return {
            "order_id": self.order_id,
            "customer": self.customer_name,
            "created_at": self.created_at.isoformat(),
            "status": self.status.value,
            "payment_status": self.payment_status,
            "items_count": sum(item.quantity for item in self.items),
            "unique_items": len(self.items),
            "subtotal": self.subtotal,
            "shipping": self.shipping_cost,
            "tax": self.tax,
            "discount": self.discount,
            "total": self.total,
            "tracking_number": self.tracking_number,
            "shipping_address": str(self.shipping_address),
            "shipping_method": self.shipping_method.value
        }
    
    def generate_invoice(self) -> str:
        """Generate invoice as string."""
        invoice = []
        invoice.append("=" * 60)
        invoice.append(f"INVOICE - {self.order_id}")
        invoice.append("=" * 60)
        invoice.append(f"Customer: {self.customer_name}")
        invoice.append(f"Email: {self.customer_email}")
        invoice.append(f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        invoice.append(f"Status: {self.status.value}")
        invoice.append("-" * 60)
        invoice.append("ITEMS:")
        
        for item in self.items:
            invoice.append(f"  {item.quantity}x {item.product_name} @ ${item.unit_price:.2f} = ${item.subtotal:.2f}")
        
        invoice.append("-" * 60)
        invoice.append(f"Subtotal: ${self.subtotal:.2f}")
        invoice.append(f"Shipping: ${self.shipping_cost:.2f}")
        invoice.append(f"Tax: ${self.tax:.2f}")
        
        if self.discount > 0:
            invoice.append(f"Discount: -${self.discount:.2f}")
        
        invoice.append("-" * 60)
        invoice.append(f"TOTAL: ${self.total:.2f}")
        invoice.append("=" * 60)
        
        return "\n".join(invoice)
    
    def __str__(self) -> str:
        return f"Order {self.order_id}: {self.customer_name} - ${self.total:.2f} ({self.status.value})"


class OrderBuilder:
    """
    Builder for creating complex orders.
    
    Design Pattern: Builder Pattern - Builds orders incrementally
    """
    
    def __init__(self):
        self.customer_id = None
        self.customer_name = None
        self.customer_email = None
        self.items = []
        self.shipping_address = None
        self.payment_method = PaymentMethod.CREDIT_CARD
        self.shipping_method = ShippingMethod.STANDARD
    
    def set_customer(self, customer_id: str, name: str, email: str) -> 'OrderBuilder':
        """Set customer information."""
        self.customer_id = customer_id
        self.customer_name = name
        self.customer_email = email
        return self
    
    def add_item(self, product_id: str, product_name: str, quantity: int, unit_price: float) -> 'OrderBuilder':
        """Add an item to the order."""
        self.items.append(OrderItem(product_id, product_name, quantity, unit_price))
        return self
    
    def set_shipping_address(self, street: str, city: str, state: str, zip_code: str) -> 'OrderBuilder':
        """Set shipping address."""
        self.shipping_address = Address(street, city, state, zip_code)
        return self
    
    def set_payment_method(self, method: PaymentMethod) -> 'OrderBuilder':
        """Set payment method."""
        self.payment_method = method
        return self
    
    def set_shipping_method(self, method: ShippingMethod) -> 'OrderBuilder':
        """Set shipping method."""
        self.shipping_method = method
        return self
    
    def build(self) -> Order:
        """Build and return the order."""
        if not self.customer_id or not self.customer_name:
            raise ValueError("Customer information required")
        
        if not self.items:
            raise ValueError("At least one item required")
        
        if not self.shipping_address:
            raise ValueError("Shipping address required")
        
        return Order(
            customer_id=self.customer_id,
            customer_name=self.customer_name,
            customer_email=self.customer_email,
            items=self.items,
            shipping_address=self.shipping_address,
            payment_method=self.payment_method,
            shipping_method=self.shipping_method
        )


class OrderManager:
    """
    Manages multiple orders.
    
    Design Pattern: Repository Pattern - Order storage and retrieval
    """
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}
    
    def create_order(self, builder: OrderBuilder) -> Order:
        """Create an order using the builder."""
        order = builder.build()
        self.orders[order.order_id] = order
        return order
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Get order by ID."""
        return self.orders.get(order_id)
    
    def get_orders_by_customer(self, customer_id: str) -> List[Order]:
        """Get all orders for a customer."""
        return [o for o in self.orders.values() if o.customer_id == customer_id]
    
    def get_orders_by_status(self, status: OrderStatus) -> List[Order]:
        """Get orders by status."""
        return [o for o in self.orders.values() if o.status == status]
    
    def get_recent_orders(self, days: int = 7) -> List[Order]:
        """Get orders from last N days."""
        cutoff = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        from datetime import timedelta
        cutoff -= timedelta(days=days)
        return [o for o in self.orders.values() if o.created_at >= cutoff]
    
    def get_statistics(self) -> Dict:
        """Get order statistics."""
        orders = self.orders.values()
        
        if not orders:
            return {"total_orders": 0}
        
        total_revenue = sum(o.total for o in orders if o.status != OrderStatus.CANCELLED)
        
        return {
            "total_orders": len(orders),
            "total_revenue": round(total_revenue, 2),
            "average_order_value": round(total_revenue / len(orders), 2) if orders else 0,
            "by_status": {
                status.value: len(self.get_orders_by_status(status))
                for status in OrderStatus
            },
            "recent_orders_7d": len(self.get_recent_orders(7))
        }


def demonstrate_order_system():
    """
    Demonstrate the complete order management system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: COMPLETE ORDER MANAGEMENT SYSTEM")
    print("=" * 60)
    
    manager = OrderManager()
    
    print("\n1. CREATING ORDERS WITH BUILDER")
    print("-" * 40)
    
    # Order 1: Small order
    builder1 = OrderBuilder()
    order1 = (builder1
              .set_customer("CUST-001", "Alice Chen", "alice@example.com")
              .add_item("PROD-001", "Wireless Mouse", 2, 29.99)
              .add_item("PROD-002", "USB Cable", 1, 19.99)
              .set_shipping_address("123 Main St", "New York", "NY", "10001")
              .set_payment_method(PaymentMethod.CREDIT_CARD)
              .build())
    
    manager.create_order(builder1)
    print(f"  Created: {order1}")
    
    # Order 2: Large order with discount
    builder2 = OrderBuilder()
    order2 = (builder2
              .set_customer("CUST-002", "Bob Smith", "bob@example.com")
              .add_item("PROD-003", "Laptop", 1, 999.99)
              .add_item("PROD-004", "Monitor", 1, 299.99)
              .add_item("PROD-001", "Wireless Mouse", 3, 29.99)
              .set_shipping_address("456 Oak Ave", "Los Angeles", "CA", "90210")
              .set_payment_method(PaymentMethod.PAYPAL)
              .set_shipping_method(ShippingMethod.EXPRESS)
              .build())
    
    manager.create_order(builder2)
    print(f"  Created: {order2}")
    
    # Order 3: Small single item
    builder3 = OrderBuilder()
    order3 = (builder3
              .set_customer("CUST-001", "Alice Chen", "alice@example.com")
              .add_item("PROD-005", "Notebook", 5, 4.99)
              .set_shipping_address("123 Main St", "New York", "NY", "10001")
              .set_payment_method(PaymentMethod.DEBIT_CARD)
              .build())
    
    manager.create_order(builder3)
    print(f"  Created: {order3}")
    
    print("\n2. ORDER DETAILS")
    print("-" * 40)
    
    for order in [order1, order2, order3]:
        summary = order.get_summary()
        print(f"\n  Order {summary['order_id']}:")
        print(f"    Customer: {summary['customer']}")
        print(f"    Items: {summary['items_count']} items")
        print(f"    Subtotal: ${summary['subtotal']:.2f}")
        print(f"    Shipping: ${summary['shipping']:.2f}")
        print(f"    Discount: ${summary['discount']:.2f}")
        print(f"    Total: ${summary['total']:.2f}")
        print(f"    Status: {summary['status']}")
    
    print("\n3. PROCESSING ORDERS")
    print("-" * 40)
    
    # Process order2 (large order)
    order2.confirm()
    order2.process_payment()
    order2.ship("TRK-123456789")
    order2.deliver()
    
    print("\n4. INVOICE GENERATION")
    print("-" * 40)
    
    print(order2.generate_invoice())
    
    print("\n5. ORDER STATISTICS")
    print("-" * 40)
    
    stats = manager.get_statistics()
    for key, value in stats.items():
        if key == "by_status":
            print(f"  {key}:")
            for status, count in value.items():
                if count > 0:
                    print(f"    {status}: {count}")
        else:
            print(f"  {key}: {value}")
    
    print("\n6. CUSTOMER ORDER HISTORY")
    print("-" * 40)
    
    alice_orders = manager.get_orders_by_customer("CUST-001")
    print(f"  Alice's orders ({len(alice_orders)}):")
    for order in alice_orders:
        print(f"    {order.order_id}: ${order.total:.2f} ({order.status.value})")


if __name__ == "__main__":
    demonstrate_order_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **__init__ Constructor** – Special method called when object is created. Initializes attributes and sets up initial state.

- **Constructor Validation** – Validate inputs before creating object. Raise ValueError for invalid data.

- **Default Values** – Constructor parameters can have defaults. Makes object creation flexible.

- **Derived Attributes** – Calculate attributes in constructor based on inputs (subtotal, tax, total).

- **__new__ vs __init__** – __new__ creates the object, __init__ initializes it. Use __init__ for most cases.

- **Multiple Constructors** – Python doesn't support multiple __init__ methods. Use class methods as alternative constructors.

- **Class Method Constructors** – `@classmethod` decorator. `from_dict`, `from_json`, `from_csv` patterns.

- **Builder Pattern** – Separate object construction from representation. Build complex objects step by step.

- **Employee Onboarding** – Constructor with validation, derived attributes, and relationships.

- **Order Management** – Complex constructor calculating shipping, tax, discount. Builder for flexible creation.

- **SOLID Principles Applied** – Single Responsibility (constructor only initializes), Dependency Inversion (depends on value objects), Open/Closed (new creation methods via class methods).

- **Design Patterns Used** – Builder Pattern (order construction), Factory Method Pattern (alternative constructors), Value Object Pattern (Address, ContactInfo), Repository Pattern (order storage), Template Method (order lifecycle).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Classes & Objects – Blueprints & Instances

- **📚 Series D Catalog:** Object-Oriented Programming Line – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Inheritance – Reusing Parent Classes (Series D, Story 3)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 2 | 4 | 33% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **25** | **27** | **48%** |

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

**Next Story:** Series D, Story 3: The 2026 Python Metromap: Inheritance – Reusing Parent Classes

---

## 📝 Your Invitation

You've mastered constructors. Now build something with what you've learned:

1. **Build a product catalog** – Create Product class with constructors from dict, CSV, JSON. Add validation for price and SKU.

2. **Create a user registration system** – User class with constructor validation for email, password strength, age verification.

3. **Build a booking system** – Appointment class with constructor that validates time slots and checks for conflicts.

4. **Create a configuration system** – Config class with constructors from file, environment variables, defaults.

5. **Build a data import system** – Create classes that can be constructed from multiple data sources (database, API, file).

**You've mastered constructors. Next stop: Inheritance!**

---

*Found this helpful? Clap, comment, and share what you built with constructors. Next stop: Inheritance!* 🚇