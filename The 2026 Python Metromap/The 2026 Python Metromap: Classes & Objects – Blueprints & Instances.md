# The 2026 Python Metromap: Classes & Objects – Blueprints & Instances

## Series D: Object-Oriented Programming (OOP) Line | Story 1 of 6

![The 2026 Python Metromap/images/Classes and Objects – Blueprints and Instances](images/Classes and Objects – Blueprints and Instances.png)

## 📖 Introduction

**Welcome to the first stop on the Object-Oriented Programming Line.**

You've mastered variables, functions, modules, and data structures. You can write code that stores data, makes decisions, repeats operations, and transforms collections. But as your programs grow larger and more complex, you need a way to model real-world entities—customers, orders, products, bank accounts—as cohesive units that bundle data with the operations that act on that data.

That's where classes and objects come in.

A class is a blueprint—a template that defines the structure and behavior of objects. An object is an instance of a class—a concrete entity with its own specific data. Object-oriented programming (OOP) lets you model real-world relationships, hide complexity, reuse code through inheritance, and write programs that are easier to understand, maintain, and extend.

This story—**The 2026 Python Metromap: Classes & Objects – Blueprints & Instances**—is your guide to the fundamentals of object-oriented programming in Python. We'll build a complete bank account system with deposits, withdrawals, and balance checking. We'll create a customer management system with multiple accounts. We'll implement a product catalog with classes for different product types. And we'll build a complete order processing system that demonstrates how classes model real-world business entities.

**Let's blueprint our code.**

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

- 🏗️ **The 2026 Python Metromap: Classes & Objects – Blueprints & Instances** – Bank account system; deposit and withdrawal methods; customer management. **⬅️ YOU ARE HERE**

- 🔧 **The 2026 Python Metromap: Constructor – Building Objects** – Employee onboarding system; automatic attribute initialization. 🔜 *Up Next*

- 👪 **The 2026 Python Metromap: Inheritance – Reusing Parent Classes** – Vehicle fleet manager with Car, Truck, and Motorcycle classes.

- 🎭 **The 2026 Python Metromap: Polymorphism – One Interface, Many Forms** – Payment processing with CreditCard, PayPal, and Crypto implementations.

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules.

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🏗️ Section 1: Class Fundamentals – Defining Blueprints

A class is a blueprint for creating objects. It defines the attributes (data) and methods (behaviors) that objects of that class will have.

**SOLID Principle Applied: Single Responsibility** – Each class should have one clear purpose and responsibility.

**Design Pattern: Factory Pattern** – Classes act as factories for creating object instances.

```python
"""
CLASS FUNDAMENTALS: DEFINING BLUEPRINTS

This section covers the basics of defining and using classes.

SOLID Principle: Single Responsibility
- Each class should have one clear purpose

Design Pattern: Factory Pattern
- Classes act as factories for creating object instances
"""

from typing import Any, Dict, List, Optional
from datetime import datetime
import random


def demonstrate_class_basics():
    """
    Demonstrates basic class definition and object creation.
    
    A class is defined using the 'class' keyword.
    Objects are created by calling the class like a function.
    """
    print("=" * 60)
    print("SECTION 1A: CLASS BASICS")
    print("=" * 60)
    
    # DEFINING A SIMPLE CLASS
    print("\n1. DEFINING A SIMPLE CLASS")
    print("-" * 40)
    
    class Dog:
        """A simple Dog class."""
        
        # Class attribute (shared by all instances)
        species = "Canis familiaris"
        
        # Instance method
        def bark(self):
            """Make the dog bark."""
            return "Woof!"
        
        def sit(self):
            """Make the dog sit."""
            return "The dog sits."
    
    # CREATING OBJECTS (INSTANCES)
    print("\n2. CREATING OBJECTS")
    print("-" * 40)
    
    buddy = Dog()
    max_dog = Dog()
    
    print(f"  buddy: {buddy}")
    print(f"  max_dog: {max_dog}")
    print(f"  Are they the same object? {buddy is max_dog}")
    
    # ACCESSING CLASS ATTRIBUTES
    print("\n3. ACCESSING CLASS ATTRIBUTES")
    print("-" * 40)
    
    print(f"  Dog.species: {Dog.species}")
    print(f"  buddy.species: {buddy.species}")
    print(f"  max_dog.species: {max_dog.species}")
    
    # CALLING METHODS
    print("\n4. CALLING METHODS")
    print("-" * 40)
    
    print(f"  buddy.bark(): {buddy.bark()}")
    print(f"  max_dog.sit(): {max_dog.sit()}")
    
    # ADDING INSTANCE ATTRIBUTES
    print("\n5. ADDING INSTANCE ATTRIBUTES")
    print("-" * 40)
    
    buddy.name = "Buddy"
    buddy.age = 3
    max_dog.name = "Max"
    max_dog.age = 5
    
    print(f"  buddy.name: {buddy.name}, buddy.age: {buddy.age}")
    print(f"  max_dog.name: {max_dog.name}, max_dog.age: {max_dog.age}")
    
    # IMPORTANT: Instance attributes are separate
    buddy.color = "brown"
    # max_dog does NOT have a 'color' attribute
    print(f"  buddy.color: {buddy.color}")
    
    # Check if attribute exists
    if hasattr(max_dog, 'color'):
        print("  max_dog has color")
    else:
        print("  max_dog does NOT have color")


def demonstrate_class_with_methods():
    """
    Demonstrates classes with multiple methods and self parameter.
    
    The 'self' parameter refers to the instance calling the method.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: CLASSES WITH METHODS")
    print("=" * 60)
    
    class BankAccount:
        """
        A simple bank account class.
        
        Design Principle: Single Responsibility - Manages a single account
        """
        
        def __init__(self, account_holder: str, initial_balance: float = 0.0):
            """
            Initialize a new bank account.
            
            Args:
                account_holder: Name of the account holder
                initial_balance: Starting balance (default 0)
            """
            self.account_holder = account_holder
            self.balance = initial_balance
            self.transaction_count = 0
            self.is_active = True
        
        def deposit(self, amount: float) -> float:
            """
            Deposit money into the account.
            
            Args:
                amount: Amount to deposit
                
            Returns:
                New balance
            """
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            
            self.balance += amount
            self.transaction_count += 1
            print(f"  Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return self.balance
        
        def withdraw(self, amount: float) -> float:
            """
            Withdraw money from the account.
            
            Args:
                amount: Amount to withdraw
                
            Returns:
                New balance
            """
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            
            if amount > self.balance:
                raise ValueError(f"Insufficient funds. Balance: ${self.balance:.2f}")
            
            self.balance -= amount
            self.transaction_count += 1
            print(f"  Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            return self.balance
        
        def get_balance(self) -> float:
            """Get current balance."""
            return self.balance
        
        def get_account_info(self) -> Dict:
            """Get account information."""
            return {
                "holder": self.account_holder,
                "balance": self.balance,
                "transactions": self.transaction_count,
                "active": self.is_active
            }
        
        def close_account(self) -> None:
            """Close the account."""
            self.is_active = False
            print(f"  Account for {self.account_holder} has been closed")
    
    # CREATE ACCOUNTS
    print("\n1. CREATING BANK ACCOUNTS")
    print("-" * 40)
    
    alice_account = BankAccount("Alice Chen", 1000.00)
    bob_account = BankAccount("Bob Smith", 500.00)
    
    print(f"  Alice's account: {alice_account.get_account_info()}")
    print(f"  Bob's account: {bob_account.get_account_info()}")
    
    # PERFORM TRANSACTIONS
    print("\n2. PERFORMING TRANSACTIONS")
    print("-" * 40)
    
    alice_account.deposit(250.00)
    alice_account.withdraw(100.00)
    bob_account.deposit(50.00)
    
    # TRY INVALID WITHDRAWAL
    print("\n3. HANDLING INVALID OPERATIONS")
    print("-" * 40)
    
    try:
        bob_account.withdraw(1000.00)
    except ValueError as e:
        print(f"  Error: {e}")
    
    # CLOSE ACCOUNT
    print("\n4. CLOSING ACCOUNT")
    print("-" * 40)
    
    alice_account.close_account()
    print(f"  Alice's account active: {alice_account.is_active}")
    
    # ACCOUNT SUMMARY
    print("\n5. ACCOUNT SUMMARIES")
    print("-" * 40)
    
    for account in [alice_account, bob_account]:
        info = account.get_account_info()
        print(f"  {info['holder']}: ${info['balance']:.2f} ({info['transactions']} transactions)")


def demonstrate_class_attributes_vs_instance_attributes():
    """
    Demonstrates the difference between class attributes and instance attributes.
    
    Class attributes are shared across all instances.
    Instance attributes are unique to each instance.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: CLASS VS INSTANCE ATTRIBUTES")
    print("=" * 60)
    
    class Employee:
        """
        Employee class demonstrating class vs instance attributes.
        
        Design Principle: Single Responsibility - Represents an employee
        """
        
        # Class attributes (shared by all instances)
        company = "Metromap Technologies"
        employee_count = 0
        raise_percentage = 0.05  # 5% annual raise
        
        def __init__(self, name: str, salary: float):
            """Initialize an employee."""
            # Instance attributes (unique to each instance)
            self.name = name
            self.salary = salary
            self.employee_id = Employee.employee_count + 1
            
            # Update class attribute
            Employee.employee_count += 1
        
        def give_raise(self) -> float:
            """Give the employee a raise."""
            raise_amount = self.salary * Employee.raise_percentage
            self.salary += raise_amount
            return self.salary
        
        def get_info(self) -> Dict:
            """Get employee information."""
            return {
                "id": self.employee_id,
                "name": self.name,
                "salary": self.salary,
                "company": Employee.company
            }
        
        @classmethod
        def set_raise_percentage(cls, percentage: float) -> None:
            """Set the raise percentage for all employees."""
            cls.raise_percentage = percentage
            print(f"  Raise percentage updated to {percentage * 100}%")
        
        @classmethod
        def get_employee_count(cls) -> int:
            """Get total number of employees."""
            return cls.employee_count
        
        @staticmethod
        def is_weekend(day: str) -> bool:
            """Check if a day is a weekend (static method)."""
            return day.lower() in ['saturday', 'sunday']
    
    # CREATE EMPLOYEES
    print("\n1. CREATING EMPLOYEES")
    print("-" * 40)
    
    alice = Employee("Alice Chen", 75000)
    bob = Employee("Bob Smith", 68000)
    charlie = Employee("Charlie Brown", 82000)
    
    print(f"  Total employees: {Employee.get_employee_count()}")
    print(f"  Alice's ID: {alice.employee_id}")
    print(f"  Bob's ID: {bob.employee_id}")
    print(f"  Charlie's ID: {charlie.employee_id}")
    
    # CLASS ATTRIBUTES ARE SHARED
    print("\n2. CLASS ATTRIBUTES ARE SHARED")
    print("-" * 40)
    
    print(f"  Alice's company: {alice.company}")
    print(f"  Bob's company: {bob.company}")
    print(f"  Employee.company: {Employee.company}")
    
    # CHANGING CLASS ATTRIBUTE AFFECTS ALL
    print("\n3. CHANGING CLASS ATTRIBUTE")
    print("-" * 40)
    
    Employee.company = "Metromap Global"
    print(f"  Alice's company after change: {alice.company}")
    print(f"  Bob's company after change: {bob.company}")
    
    # INSTANCE ATTRIBUTES ARE SEPARATE
    print("\n4. INSTANCE ATTRIBUTES ARE SEPARATE")
    print("-" * 40)
    
    print(f"  Alice's salary: ${alice.salary:,.2f}")
    print(f"  Bob's salary: ${bob.salary:,.2f}")
    alice.give_raise()
    print(f"  Alice's salary after raise: ${alice.salary:,.2f}")
    print(f"  Bob's salary unchanged: ${bob.salary:,.2f}")
    
    # CLASS METHODS
    print("\n5. CLASS METHODS")
    print("-" * 40)
    
    Employee.set_raise_percentage(0.07)  # 7% raise
    alice.give_raise()
    bob.give_raise()
    print(f"  Alice's salary after 7% raise: ${alice.salary:,.2f}")
    print(f"  Bob's salary after 7% raise: ${bob.salary:,.2f}")
    
    # STATIC METHODS
    print("\n6. STATIC METHODS")
    print("-" * 40)
    
    print(f"  Is Monday a weekend? {Employee.is_weekend('Monday')}")
    print(f"  Is Saturday a weekend? {Employee.is_weekend('Saturday')}")
    
    # FINAL SUMMARY
    print("\n7. EMPLOYEE SUMMARIES")
    print("-" * 40)
    
    for emp in [alice, bob, charlie]:
        info = emp.get_info()
        print(f"  Employee {info['id']}: {info['name']} - ${info['salary']:,.2f} ({info['company']})")


def demonstrate_method_types():
    """
    Demonstrates the three types of methods in Python classes.
    
    - Instance methods: operate on instance data (self)
    - Class methods: operate on class data (cls)
    - Static methods: utility functions related to the class
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: METHOD TYPES")
    print("=" * 60)
    
    class Calculator:
        """
        Calculator demonstrating different method types.
        
        Design Pattern: Utility Pattern - Provides calculation utilities
        """
        
        # Class constant
        PI = 3.14159
        
        def __init__(self, precision: int = 2):
            """Initialize calculator with precision."""
            self.precision = precision
        
        # Instance method (uses self)
        def add(self, a: float, b: float) -> float:
            """Add two numbers (instance method)."""
            result = a + b
            return round(result, self.precision)
        
        def multiply(self, a: float, b: float) -> float:
            """Multiply two numbers (instance method)."""
            result = a * b
            return round(result, self.precision)
        
        # Class method (uses cls)
        @classmethod
        def circle_area(cls, radius: float) -> float:
            """Calculate circle area (class method)."""
            return cls.PI * radius ** 2
        
        @classmethod
        def circle_circumference(cls, radius: float) -> float:
            """Calculate circle circumference (class method)."""
            return 2 * cls.PI * radius
        
        # Static method (no self or cls)
        @staticmethod
        def is_even(number: int) -> bool:
            """Check if number is even (static method)."""
            return number % 2 == 0
        
        @staticmethod
        def is_prime(number: int) -> bool:
            """Check if number is prime (static method)."""
            if number < 2:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True
    
    # INSTANCE METHODS
    print("\n1. INSTANCE METHODS (use self)")
    print("-" * 40)
    
    calc = Calculator(precision=3)
    print(f"  calc.add(10.1234, 5.6789) = {calc.add(10.1234, 5.6789)}")
    print(f"  calc.multiply(3.14159, 2.0) = {calc.multiply(3.14159, 2.0)}")
    
    # Different instances can have different state
    calc2 = Calculator(precision=0)
    print(f"  calc2.add(10.1234, 5.6789) = {calc2.add(10.1234, 5.6789)}")
    
    # CLASS METHODS (use cls)
    print("\n2. CLASS METHODS (use cls)")
    print("-" * 40)
    
    print(f"  Calculator.circle_area(5) = {Calculator.circle_area(5):.2f}")
    print(f"  Calculator.circle_circumference(5) = {Calculator.circle_circumference(5):.2f}")
    
    # STATIC METHODS (no self or cls)
    print("\n3. STATIC METHODS (no self or cls)")
    print("-" * 40)
    
    print(f"  Calculator.is_even(4) = {Calculator.is_even(4)}")
    print(f"  Calculator.is_even(7) = {Calculator.is_even(7)}")
    print(f"  Calculator.is_prime(17) = {Calculator.is_prime(17)}")
    print(f"  Calculator.is_prime(20) = {Calculator.is_prime(20)}")
    
    # WHEN TO USE EACH
    print("\n4. WHEN TO USE EACH METHOD TYPE")
    print("-" * 40)
    
    print("""
    Instance Methods:
        - Need to access or modify instance-specific data
        - Most common method type
        - First parameter is 'self'
    
    Class Methods:
        - Need to access or modify class-level data
        - Alternative constructors
        - First parameter is 'cls'
        - Decorated with @classmethod
    
    Static Methods:
        - Utility functions related to the class
        - Don't need access to instance or class data
        - No special first parameter
        - Decorated with @staticmethod
    """)


if __name__ == "__main__":
    demonstrate_class_basics()
    demonstrate_class_with_methods()
    demonstrate_class_attributes_vs_instance_attributes()
    demonstrate_method_types()
```

---

## 🏦 Section 2: Building a Complete Bank Account System

A complete bank account system with multiple account types, transaction history, and interest calculation.

**SOLID Principles Applied:**
- Single Responsibility: Each class has one responsibility
- Open/Closed: New account types can be added

**Design Patterns:**
- Command Pattern: Transactions as commands
- Memento Pattern: Transaction history for undo/redo

```python
"""
BUILDING A COMPLETE BANK ACCOUNT SYSTEM

This section builds a complete bank account system with multiple account types.

SOLID Principles Applied:
- Single Responsibility: Each class has one responsibility
- Open/Closed: New account types can be added

Design Patterns:
- Command Pattern: Transactions as commands
- Memento Pattern: Transaction history for undo/redo
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum
import uuid


class TransactionType(Enum):
    """Types of transactions."""
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER_IN = "transfer_in"
    TRANSFER_OUT = "transfer_out"
    INTEREST = "interest"
    FEE = "fee"


class Transaction:
    """
    Represents a single transaction.
    
    Design Pattern: Command Pattern - Transaction as command
    """
    
    def __init__(self, transaction_id: str, account_id: str, amount: float,
                 transaction_type: TransactionType, description: str = ""):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.timestamp = datetime.now()
        self.is_reversed = False
    
    def to_dict(self) -> Dict:
        """Convert transaction to dictionary."""
        return {
            "id": self.transaction_id,
            "account_id": self.account_id,
            "amount": self.amount,
            "type": self.transaction_type.value,
            "description": self.description,
            "timestamp": self.timestamp.isoformat(),
            "is_reversed": self.is_reversed
        }
    
    def __str__(self) -> str:
        sign = "+" if self.amount > 0 else ""
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.transaction_type.value}: {sign}${self.amount:.2f} - {self.description}"


class Account(ABC):
    """
    Abstract base class for all account types.
    
    SOLID: Liskov Substitution - All account types can be used interchangeably
    Design Pattern: Template Method - Defines account skeleton
    """
    
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance
        self.transactions: List[Transaction] = []
        self.created_at = datetime.now()
        self.is_active = True
        
        # Record initial deposit if any
        if initial_balance > 0:
            self._record_transaction(initial_balance, TransactionType.DEPOSIT, "Initial deposit")
    
    @abstractmethod
    def get_account_type(self) -> str:
        """Return the account type name."""
        pass
    
    @abstractmethod
    def calculate_interest(self) -> float:
        """Calculate interest for this account."""
        pass
    
    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """Deposit money into the account."""
        if not self.is_active:
            print(f"  Account {self.account_number} is closed")
            return False
        
        if amount <= 0:
            print(f"  Deposit amount must be positive")
            return False
        
        self._balance += amount
        self._record_transaction(amount, TransactionType.DEPOSIT, description)
        print(f"  Deposited ${amount:.2f} to {self.get_account_type()} {self.account_number}")
        return True
    
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """Withdraw money from the account."""
        if not self.is_active:
            print(f"  Account {self.account_number} is closed")
            return False
        
        if amount <= 0:
            print(f"  Withdrawal amount must be positive")
            return False
        
        if not self.can_withdraw(amount):
            print(f"  Insufficient funds. Balance: ${self._balance:.2f}")
            return False
        
        self._balance -= amount
        self._record_transaction(-amount, TransactionType.WITHDRAWAL, description)
        print(f"  Withdrew ${amount:.2f} from {self.get_account_type()} {self.account_number}")
        return True
    
    def can_withdraw(self, amount: float) -> bool:
        """Check if withdrawal is allowed."""
        return amount <= self._balance
    
    def get_balance(self) -> float:
        """Get current balance."""
        return self._balance
    
    def _record_transaction(self, amount: float, transaction_type: TransactionType, description: str) -> None:
        """Record a transaction."""
        transaction_id = str(uuid.uuid4())[:8]
        transaction = Transaction(transaction_id, self.account_number, amount, transaction_type, description)
        self.transactions.append(transaction)
    
    def get_transaction_history(self, limit: int = 10) -> List[Transaction]:
        """Get recent transaction history."""
        return self.transactions[-limit:][::-1]
    
    def get_statement(self) -> str:
        """Generate account statement."""
        lines = []
        lines.append("=" * 60)
        lines.append(f"STATEMENT - {self.get_account_type()}")
        lines.append(f"Account: {self.account_number}")
        lines.append(f"Holder: {self.account_holder}")
        lines.append(f"Balance: ${self._balance:.2f}")
        lines.append(f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("-" * 60)
        lines.append("Recent Transactions:")
        
        for tx in self.get_transaction_history(10):
            lines.append(f"  {tx}")
        
        lines.append("=" * 60)
        return "\n".join(lines)
    
    def close(self) -> None:
        """Close the account."""
        self.is_active = False
        print(f"  Account {self.account_number} has been closed")
    
    def to_dict(self) -> Dict:
        """Convert account to dictionary."""
        return {
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "account_type": self.get_account_type(),
            "balance": self._balance,
            "created_at": self.created_at.isoformat(),
            "is_active": self.is_active,
            "transactions": [t.to_dict() for t in self.transactions]
        }


class SavingsAccount(Account):
    """
    Savings account with interest and minimum balance requirement.
    
    SOLID: Liskov Substitution - Can be used anywhere Account is expected
    """
    
    INTEREST_RATE = 0.02  # 2% annual interest
    MINIMUM_BALANCE = 100.0
    
    def get_account_type(self) -> str:
        return "Savings Account"
    
    def can_withdraw(self, amount: float) -> bool:
        """Check if withdrawal would violate minimum balance."""
        if self._balance - amount < self.MINIMUM_BALANCE:
            return False
        return amount <= self._balance
    
    def calculate_interest(self) -> float:
        """Calculate monthly interest."""
        interest = self._balance * (self.INTEREST_RATE / 12)
        return round(interest, 2)
    
    def add_interest(self) -> bool:
        """Add interest to the account."""
        interest = self.calculate_interest()
        if interest > 0:
            self._balance += interest
            self._record_transaction(interest, TransactionType.INTEREST, "Monthly interest")
            print(f"  Added ${interest:.2f} interest to {self.account_number}")
            return True
        return False


class CheckingAccount(Account):
    """
    Checking account with overdraft protection.
    
    SOLID: Liskov Substitution - Can be used anywhere Account is expected
    """
    
    OVERDRAFT_LIMIT = 500.0
    MONTHLY_FEE = 5.0
    
    def get_account_type(self) -> str:
        return "Checking Account"
    
    def can_withdraw(self, amount: float) -> bool:
        """Check if withdrawal is within overdraft limit."""
        return amount <= self._balance + self.OVERDRAFT_LIMIT
    
    def calculate_interest(self) -> float:
        """Checking accounts typically don't earn interest."""
        return 0.0
    
    def apply_monthly_fee(self) -> bool:
        """Apply monthly maintenance fee."""
        if self._balance >= 1000:  # Fee waived for high balance
            return False
        
        self._balance -= self.MONTHLY_FEE
        self._record_transaction(-self.MONTHLY_FEE, TransactionType.FEE, "Monthly maintenance fee")
        print(f"  Applied ${self.MONTHLY_FEE:.2f} fee to {self.account_number}")
        return True


class InvestmentAccount(Account):
    """
    Investment account with portfolio tracking.
    
    SOLID: Liskov Substitution - Can be used anywhere Account is expected
    """
    
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.portfolio: Dict[str, int] = {}  # symbol -> shares
    
    def get_account_type(self) -> str:
        return "Investment Account"
    
    def calculate_interest(self) -> float:
        """Investment accounts don't earn interest directly."""
        return 0.0
    
    def buy_shares(self, symbol: str, shares: int, price_per_share: float) -> bool:
        """Buy shares of a stock."""
        cost = shares * price_per_share
        
        if not self.can_withdraw(cost):
            print(f"  Insufficient funds to buy {shares} shares of {symbol}")
            return False
        
        self._balance -= cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares
        
        description = f"Bought {shares} shares of {symbol} @ ${price_per_share:.2f}"
        self._record_transaction(-cost, TransactionType.WITHDRAWAL, description)
        print(f"  Bought {shares} shares of {symbol} for ${cost:.2f}")
        return True
    
    def sell_shares(self, symbol: str, shares: int, price_per_share: float) -> bool:
        """Sell shares of a stock."""
        if symbol not in self.portfolio or self.portfolio[symbol] < shares:
            print(f"  Insufficient shares of {symbol}")
            return False
        
        proceeds = shares * price_per_share
        self._balance += proceeds
        self.portfolio[symbol] -= shares
        
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
        
        description = f"Sold {shares} shares of {symbol} @ ${price_per_share:.2f}"
        self._record_transaction(proceeds, TransactionType.DEPOSIT, description)
        print(f"  Sold {shares} shares of {symbol} for ${proceeds:.2f}")
        return True
    
    def get_portfolio_value(self, current_prices: Dict[str, float]) -> float:
        """Calculate total portfolio value."""
        stock_value = sum(self.portfolio.get(symbol, 0) * price 
                         for symbol, price in current_prices.items())
        return self._balance + stock_value


class Bank:
    """
    Bank that manages multiple accounts.
    
    Design Pattern: Facade Pattern - Simplified interface to account management
    """
    
    def __init__(self, name: str):
        self.name = name
        self.accounts: Dict[str, Account] = {}
        self.customers: Dict[str, List[str]] = {}  # customer_id -> list of account_numbers
    
    def create_account(self, account_type: str, customer_id: str, 
                       account_holder: str, initial_deposit: float = 0.0) -> Optional[str]:
        """Create a new account."""
        account_number = f"{account_type[:3].upper()}{random.randint(10000, 99999)}"
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, account_holder, initial_deposit)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_number, account_holder, initial_deposit)
        elif account_type.lower() == "investment":
            account = InvestmentAccount(account_number, account_holder, initial_deposit)
        else:
            print(f"  Unknown account type: {account_type}")
            return None
        
        self.accounts[account_number] = account
        
        if customer_id not in self.customers:
            self.customers[customer_id] = []
        self.customers[customer_id].append(account_number)
        
        print(f"  Created {account.get_account_type()} {account_number} for {account_holder}")
        return account_number
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """Get account by number."""
        return self.accounts.get(account_number)
    
    def transfer(self, from_account: str, to_account: str, amount: float) -> bool:
        """Transfer money between accounts."""
        source = self.get_account(from_account)
        dest = self.get_account(to_account)
        
        if not source:
            print(f"  Source account {from_account} not found")
            return False
        
        if not dest:
            print(f"  Destination account {to_account} not found")
            return False
        
        if not source.withdraw(amount, f"Transfer to {to_account}"):
            return False
        
        dest.deposit(amount, f"Transfer from {from_account}")
        print(f"  Transferred ${amount:.2f} from {from_account} to {to_account}")
        return True
    
    def get_customer_accounts(self, customer_id: str) -> List[Account]:
        """Get all accounts for a customer."""
        account_numbers = self.customers.get(customer_id, [])
        return [self.accounts[acc] for acc in account_numbers if acc in self.accounts]
    
    def print_customer_summary(self, customer_id: str) -> None:
        """Print summary of customer's accounts."""
        accounts = self.get_customer_accounts(customer_id)
        
        print(f"\n{'='*50}")
        print(f"CUSTOMER SUMMARY: {customer_id}")
        print(f"{'='*50}")
        
        total_balance = 0.0
        for account in accounts:
            print(f"\n{account.get_account_type()}: {account.account_number}")
            print(f"  Balance: ${account.get_balance():.2f}")
            total_balance += account.get_balance()
        
        print(f"\n{'='*50}")
        print(f"TOTAL BALANCE: ${total_balance:.2f}")
        print(f"{'='*50}\n")
    
    def process_monthly_maintenance(self) -> None:
        """Process monthly tasks for all accounts."""
        print(f"\n📅 Monthly Maintenance for {self.name}")
        print("-" * 40)
        
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CheckingAccount):
                account.apply_monthly_fee()
        
        print("  Monthly maintenance complete")


def demonstrate_bank_system():
    """
    Demonstrate the complete bank account system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: COMPLETE BANK ACCOUNT SYSTEM")
    print("=" * 60)
    
    import random
    
    # Create bank
    bank = Bank("Metromap National Bank")
    
    print("\n1. CREATING ACCOUNTS")
    print("-" * 40)
    
    customer_id = "CUST-001"
    
    savings = bank.create_account("savings", customer_id, "Alice Chen", 1000.00)
    checking = bank.create_account("checking", customer_id, "Alice Chen", 500.00)
    investment = bank.create_account("investment", customer_id, "Alice Chen", 5000.00)
    
    # Get account objects
    savings_acc = bank.get_account(savings)
    checking_acc = bank.get_account(checking)
    investment_acc = bank.get_account(investment)
    
    print("\n2. PERFORMING TRANSACTIONS")
    print("-" * 40)
    
    # Savings account operations
    savings_acc.deposit(200.00, "Birthday gift")
    savings_acc.withdraw(150.00, "ATM withdrawal")
    
    # Checking account operations
    checking_acc.deposit(1000.00, "Paycheck")
    checking_acc.withdraw(1200.00, "Rent payment")  # Tests overdraft
    
    # Transfer between accounts
    bank.transfer(savings, checking, 300.00)
    
    # Investment account operations
    investment_acc.buy_shares("AAPL", 10, 175.50)
    investment_acc.buy_shares("GOOGL", 5, 140.25)
    
    print("\n3. ACCOUNT STATEMENTS")
    print("-" * 40)
    
    print(savings_acc.get_statement())
    
    print("\n4. PORTFOLIO VALUE")
    print("-" * 40)
    
    current_prices = {"AAPL": 180.25, "GOOGL": 145.50}
    portfolio_value = investment_acc.get_portfolio_value(current_prices)
    print(f"  Portfolio value: ${portfolio_value:.2f}")
    print(f"  Cash balance: ${investment_acc.get_balance():.2f}")
    print(f"  Stock value: ${portfolio_value - investment_acc.get_balance():.2f}")
    
    print("\n5. CUSTOMER SUMMARY")
    print("-" * 40)
    
    bank.print_customer_summary(customer_id)
    
    print("\n6. MONTHLY MAINTENANCE")
    print("-" * 40)
    
    bank.process_monthly_maintenance()
    
    print("\n7. FINAL BALANCES")
    print("-" * 40)
    
    for account in [savings_acc, checking_acc, investment_acc]:
        print(f"  {account.get_account_type()}: ${account.get_balance():.2f}")


if __name__ == "__main__":
    demonstrate_bank_system()
```

---

## 🏭 Section 3: Product Management System

A complete product management system with categories, inventory tracking, and pricing rules.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of product management
- Open/Closed: New product types can be added

**Design Patterns:**
- Factory Pattern: Creates different product types
- Observer Pattern: Notifies when inventory changes

```python
"""
PRODUCT MANAGEMENT SYSTEM

This section builds a product management system with categories and inventory.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New product types can be added

Design Patterns:
- Factory Pattern: Creates different product types
- Observer Pattern: Notifies when inventory changes
"""

from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid


class ProductCategory(Enum):
    """Product categories."""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"
    FOOD = "food"
    TOYS = "toys"
    SPORTS = "sports"


class ProductStatus(Enum):
    """Product status."""
    ACTIVE = "active"
    DISCONTINUED = "discontinued"
    OUT_OF_STOCK = "out_of_stock"
    COMING_SOON = "coming_soon"


@dataclass
class Price:
    """Value object for price."""
    amount: float
    currency: str = "USD"
    
    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Price cannot be negative")
    
    def __str__(self) -> str:
        symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
        symbol = symbols.get(self.currency, self.currency)
        return f"{symbol}{self.amount:.2f}"
    
    def apply_discount(self, discount_percent: float) -> 'Price':
        """Apply percentage discount."""
        new_amount = self.amount * (1 - discount_percent / 100)
        return Price(round(new_amount, 2), self.currency)


class Product:
    """
    Base Product class.
    
    SOLID: Single Responsibility - Represents a product
    """
    
    def __init__(self, sku: str, name: str, category: ProductCategory, 
                 price: Price, description: str = ""):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.created_at = datetime.now()
        self.status = ProductStatus.ACTIVE
        self.tags: List[str] = []
        self.metadata: Dict[str, Any] = {}
        self._observers: List[Callable] = []
    
    def attach_observer(self, observer: Callable) -> None:
        """Attach an observer for price/inventory changes."""
        self._observers.append(observer)
    
    def _notify_observers(self, event: str, data: Any) -> None:
        """Notify all observers of an event."""
        for observer in self._observers:
            observer(self.sku, event, data)
    
    def update_price(self, new_price: Price) -> None:
        """Update product price."""
        old_price = self.price
        self.price = new_price
        self._notify_observers("price_change", {"old": str(old_price), "new": str(new_price)})
        print(f"  Price updated for {self.name}: {old_price} → {new_price}")
    
    def update_status(self, new_status: ProductStatus) -> None:
        """Update product status."""
        self.status = new_status
        self._notify_observers("status_change", {"new_status": new_status.value})
        print(f"  Status updated for {self.name}: {new_status.value}")
    
    def add_tag(self, tag: str) -> None:
        """Add a tag to the product."""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        return {
            "sku": self.sku,
            "name": self.name,
            "category": self.category.value,
            "price": str(self.price),
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "status": self.status.value,
            "tags": self.tags,
            "metadata": self.metadata
        }
    
    def __str__(self) -> str:
        return f"{self.name} ({self.sku}) - {self.price} [{self.status.value}]"


class InventoryItem:
    """
    Represents inventory for a product.
    
    Design Pattern: Observer Pattern - Notifies when stock changes
    """
    
    def __init__(self, product: Product, quantity: int = 0, reorder_point: int = 10):
        self.product = product
        self.quantity = quantity
        self.reorder_point = reorder_point
        self.reserved_quantity = 0
        self.last_restocked = datetime.now()
        
        # Attach observer to product for price/status changes
        product.attach_observer(self._on_product_event)
    
    @property
    def available_quantity(self) -> int:
        """Get available quantity (not reserved)."""
        return self.quantity - self.reserved_quantity
    
    def _on_product_event(self, sku: str, event: str, data: Any) -> None:
        """Handle product events."""
        print(f"  Inventory notified: {sku} - {event}: {data}")
    
    def restock(self, quantity: int) -> None:
        """Add inventory."""
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        
        self.quantity += quantity
        self.last_restocked = datetime.now()
        print(f"  Restocked {self.product.name}: +{quantity} (now {self.quantity})")
    
    def reserve(self, quantity: int) -> bool:
        """Reserve inventory for an order."""
        if quantity > self.available_quantity:
            return False
        
        self.reserved_quantity += quantity
        print(f"  Reserved {quantity} of {self.product.name}")
        return True
    
    def release_reservation(self, quantity: int) -> None:
        """Release reserved inventory."""
        self.reserved_quantity = max(0, self.reserved_quantity - quantity)
        print(f"  Released reservation of {quantity} for {self.product.name}")
    
    def fulfill(self, quantity: int) -> bool:
        """Fulfill an order (remove from inventory)."""
        if quantity > self.available_quantity:
            return False
        
        self.quantity -= quantity
        self.reserved_quantity = max(0, self.reserved_quantity - quantity)
        print(f"  Fulfilled {quantity} of {self.product.name}")
        
        # Check if reorder needed
        if self.quantity <= self.reorder_point:
            print(f"  ⚠️ Reorder alert: {self.product.name} stock low ({self.quantity} left)")
        
        return True
    
    def get_status(self) -> Dict:
        """Get inventory status."""
        return {
            "sku": self.product.sku,
            "name": self.product.name,
            "quantity": self.quantity,
            "available": self.available_quantity,
            "reserved": self.reserved_quantity,
            "reorder_point": self.reorder_point,
            "needs_reorder": self.quantity <= self.reorder_point
        }


class ProductCatalog:
    """
    Product catalog with inventory management.
    
    Design Pattern: Repository Pattern - Central product storage
    """
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.inventory: Dict[str, InventoryItem] = {}
        self.category_index: Dict[ProductCategory, List[str]] = {}
    
    def add_product(self, product: Product, initial_quantity: int = 0) -> None:
        """Add a product to the catalog."""
        if product.sku in self.products:
            raise ValueError(f"Product {product.sku} already exists")
        
        self.products[product.sku] = product
        self.inventory[product.sku] = InventoryItem(product, initial_quantity)
        
        # Update category index
        if product.category not in self.category_index:
            self.category_index[product.category] = []
        self.category_index[product.category].append(product.sku)
        
        print(f"  Added product: {product}")
    
    def get_product(self, sku: str) -> Optional[Product]:
        """Get product by SKU."""
        return self.products.get(sku)
    
    def get_inventory(self, sku: str) -> Optional[InventoryItem]:
        """Get inventory for a product."""
        return self.inventory.get(sku)
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a category."""
        skus = self.category_index.get(category, [])
        return [self.products[sku] for sku in skus if sku in self.products]
    
    def search_products(self, query: str) -> List[Product]:
        """Search products by name or description."""
        query_lower = query.lower()
        results = []
        for product in self.products.values():
            if query_lower in product.name.lower() or query_lower in product.description.lower():
                results.append(product)
        return results
    
    def apply_category_discount(self, category: ProductCategory, discount_percent: float) -> None:
        """Apply discount to all products in a category."""
        for product in self.get_products_by_category(category):
            new_price = product.price.apply_discount(discount_percent)
            product.update_price(new_price)
        print(f"  Applied {discount_percent}% discount to {category.value} category")
    
    def get_low_stock_products(self, threshold: int = 10) -> List[Dict]:
        """Get products with low stock."""
        low_stock = []
        for sku, inventory in self.inventory.items():
            if inventory.quantity <= threshold:
                product = self.products[sku]
                low_stock.append({
                    "sku": sku,
                    "name": product.name,
                    "quantity": inventory.quantity,
                    "threshold": threshold
                })
        return low_stock
    
    def get_catalog_summary(self) -> Dict:
        """Get catalog summary statistics."""
        total_value = sum(inv.quantity * prod.price.amount 
                         for sku, inv in self.inventory.items()
                         for prod in [self.products[sku]])
        
        return {
            "total_products": len(self.products),
            "total_inventory_value": round(total_value, 2),
            "categories": len(self.category_index),
            "low_stock_count": len(self.get_low_stock_products()),
            "active_products": sum(1 for p in self.products.values() if p.status == ProductStatus.ACTIVE)
        }


class ShoppingCart:
    """
    Shopping cart for customer orders.
    
    Design Pattern: Builder Pattern - Builds order incrementally
    """
    
    def __init__(self, catalog: ProductCatalog):
        self.catalog = catalog
        self.items: Dict[str, int] = {}  # sku -> quantity
        self.reservations: Dict[str, int] = {}  # sku -> reserved quantity
    
    def add_item(self, sku: str, quantity: int = 1) -> bool:
        """Add item to cart."""
        product = self.catalog.get_product(sku)
        if not product:
            print(f"  Product {sku} not found")
            return False
        
        inventory = self.catalog.get_inventory(sku)
        if not inventory or inventory.available_quantity < quantity:
            print(f"  Insufficient stock for {product.name}")
            return False
        
        self.items[sku] = self.items.get(sku, 0) + quantity
        print(f"  Added {quantity}x {product.name} to cart")
        return True
    
    def remove_item(self, sku: str, quantity: int = None) -> bool:
        """Remove item from cart."""
        if sku not in self.items:
            print(f"  Product {sku} not in cart")
            return False
        
        if quantity is None or quantity >= self.items[sku]:
            del self.items[sku]
        else:
            self.items[sku] -= quantity
        
        print(f"  Removed {sku} from cart")
        return True
    
    def get_subtotal(self) -> Price:
        """Calculate cart subtotal."""
        total = 0.0
        for sku, qty in self.items.items():
            product = self.catalog.get_product(sku)
            if product:
                total += product.price.amount * qty
        return Price(round(total, 2))
    
    def reserve_inventory(self) -> bool:
        """Reserve inventory for items in cart."""
        for sku, qty in self.items.items():
            inventory = self.catalog.get_inventory(sku)
            if not inventory or not inventory.reserve(qty):
                return False
            self.reservations[sku] = qty
        return True
    
    def release_reservations(self) -> None:
        """Release all reservations."""
        for sku, qty in self.reservations.items():
            inventory = self.catalog.get_inventory(sku)
            if inventory:
                inventory.release_reservation(qty)
        self.reservations.clear()
    
    def clear(self) -> None:
        """Clear the cart."""
        self.items.clear()
        self.release_reservations()
    
    def get_summary(self) -> Dict:
        """Get cart summary."""
        items_detail = []
        for sku, qty in self.items.items():
            product = self.catalog.get_product(sku)
            if product:
                items_detail.append({
                    "sku": sku,
                    "name": product.name,
                    "quantity": qty,
                    "unit_price": str(product.price),
                    "total": str(Price(product.price.amount * qty))
                })
        
        return {
            "items": items_detail,
            "item_count": sum(self.items.values()),
            "unique_items": len(self.items),
            "subtotal": str(self.get_subtotal())
        }
    
    def display(self) -> None:
        """Display cart contents."""
        if not self.items:
            print("\n  Cart is empty")
            return
        
        print("\n" + "-" * 50)
        print("SHOPPING CART")
        print("-" * 50)
        
        for sku, qty in self.items.items():
            product = self.catalog.get_product(sku)
            if product:
                print(f"  {qty}x {product.name} @ {product.price} = {Price(product.price.amount * qty)}")
        
        print("-" * 50)
        print(f"  Subtotal: {self.get_subtotal()}")
        print("-" * 50)


def demonstrate_product_system():
    """
    Demonstrate the product management system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: PRODUCT MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Create catalog
    catalog = ProductCatalog()
    
    print("\n1. ADDING PRODUCTS")
    print("-" * 40)
    
    # Create products
    laptop = Product("TECH-001", "UltraBook Pro", ProductCategory.ELECTRONICS, Price(1299.99))
    laptop.description = "High-performance laptop for professionals"
    laptop.add_tag("premium")
    laptop.add_tag("portable")
    
    mouse = Product("TECH-002", "Wireless Mouse", ProductCategory.ELECTRONICS, Price(29.99))
    mouse.add_tag("wireless")
    mouse.add_tag("ergonomic")
    
    notebook = Product("OFF-001", "Premium Notebook", ProductCategory.BOOKS, Price(4.99))
    
    catalog.add_product(laptop, 10)
    catalog.add_product(mouse, 50)
    catalog.add_product(notebook, 100)
    
    print("\n2. PRODUCT CATALOG")
    print("-" * 40)
    
    for product in catalog.products.values():
        inv = catalog.get_inventory(product.sku)
        print(f"  {product} - Stock: {inv.quantity}")
    
    print("\n3. SHOPPING CART")
    print("-" * 40)
    
    cart = ShoppingCart(catalog)
    cart.add_item("TECH-001", 1)
    cart.add_item("TECH-002", 2)
    cart.add_item("OFF-001", 3)
    
    cart.display()
    
    print("\n4. RESERVE INVENTORY")
    print("-" * 40)
    
    if cart.reserve_inventory():
        print("  Inventory reserved successfully")
        for sku, qty in cart.reservations.items():
            inv = catalog.get_inventory(sku)
            print(f"    {sku}: {qty} reserved (available: {inv.available_quantity})")
    
    print("\n5. FULFILL ORDER")
    print("-" * 40)
    
    for sku, qty in cart.items.items():
        inv = catalog.get_inventory(sku)
        inv.fulfill(qty)
    
    cart.clear()
    print("  Order fulfilled, cart cleared")
    
    print("\n6. CATALOG SUMMARY")
    print("-" * 40)
    
    summary = catalog.get_catalog_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    print("\n7. CATEGORY DISCOUNT")
    print("-" * 40)
    
    catalog.apply_category_discount(ProductCategory.ELECTRONICS, 10)
    
    print(f"\n  New laptop price: {laptop.price}")
    print(f"  New mouse price: {mouse.price}")
    
    print("\n8. LOW STOCK ALERT")
    print("-" * 40)
    
    low_stock = catalog.get_low_stock_products(15)
    for item in low_stock:
        print(f"  ⚠️ {item['name']}: only {item['quantity']} left (threshold: {item['threshold']})")


if __name__ == "__main__":
    demonstrate_product_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Class Definition** – `class ClassName:` creates a blueprint. Contains attributes (data) and methods (behaviors).

- **Object Creation** – `obj = ClassName()` creates an instance. Each instance has its own data.

- **Instance Methods** – Take `self` parameter. Access and modify instance attributes.

- **Class Attributes** – Shared across all instances. Defined at class level. Access via `ClassName.attribute`.

- **Instance Attributes** – Unique to each instance. Created in `__init__` or added later.

- **Class Methods** – Use `@classmethod` decorator. Take `cls` parameter. Access/modify class state.

- **Static Methods** – Use `@staticmethod` decorator. No `self` or `cls`. Utility functions related to class.

- **Bank Account System** – Multiple account types (Savings, Checking, Investment). Transaction history. Interest calculation.

- **Product Management** – Product catalog with categories. Inventory tracking with reservations. Shopping cart.

- **SOLID Principles Applied** – Single Responsibility (each class has one purpose), Liskov Substitution (subclasses work where parent expected), Open/Closed (new types can be added), Interface Segregation (clean interfaces), Dependency Inversion (depends on abstractions).

- **Design Patterns Used** – Factory Pattern (creating objects), Command Pattern (transactions), Observer Pattern (inventory notifications), Repository Pattern (product storage), Builder Pattern (cart building), Template Method (account skeleton), Value Object Pattern (Price), Facade Pattern (Bank interface).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Comprehensions – One-Line Power

- **📚 Series D Catalog:** Object-Oriented Programming Line – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Constructor – Building Objects (Series D, Story 2)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 1 | 5 | 17% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **24** | **28** | **46%** |

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

**Next Story:** Series D, Story 2: The 2026 Python Metromap: Constructor – Building Objects

---

## 📝 Your Invitation

You've mastered classes and objects. Now build something with what you've learned:

1. **Build a library system** – Create classes for Book, Member, Loan. Track due dates, calculate fines, manage reservations.

2. **Create a vehicle registration system** – Classes for Vehicle, Owner, Registration. Track VIN, plate numbers, expiration dates.

3. **Build a restaurant ordering system** – Classes for MenuItem, Order, Table. Calculate totals, track order status, manage seating.

4. **Create a task management system** – Classes for Task, Project, Assignment. Track priorities, deadlines, completion status.

5. **Build a hotel reservation system** – Classes for Room, Guest, Reservation. Check availability, calculate rates, manage check-in/out.

**You've mastered classes and objects. Next stop: Constructors!**

---

*Found this helpful? Clap, comment, and share what classes you built. Next stop: Constructors!* 🚇