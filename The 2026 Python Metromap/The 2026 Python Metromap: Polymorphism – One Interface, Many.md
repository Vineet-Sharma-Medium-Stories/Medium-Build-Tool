# The 2026 Python Metromap: Polymorphism – One Interface, Many Forms

## Series D: Object-Oriented Programming (OOP) Line | Story 4 of 6

![The 2026 Python Metromap/images/Polymorphism – One Interface, Many Forms](images/Polymorphism – One Interface, Many Forms.png)

## 📖 Introduction

**Welcome to the fourth stop on the Object-Oriented Programming Line.**

You've mastered classes, constructors, and inheritance. You know how to create hierarchies where child classes inherit from parents. But inheritance alone doesn't unlock the full power of object-oriented programming. The real magic happens when you treat different objects through a common interface—that's polymorphism.

Polymorphism (from Greek "many forms") allows objects of different classes to be treated as objects of a common superclass. The same method call can behave differently depending on the actual type of the object. This enables you to write flexible, extensible code that works with a family of related types without knowing their specific classes.

This story—**The 2026 Python Metromap: Polymorphism – One Interface, Many Forms**—is your guide to mastering polymorphism in Python. We'll build a complete payment processing system where different payment methods (CreditCard, PayPal, Crypto) all implement the same `process_payment` method. We'll create a shape calculator where Circle, Rectangle, and Triangle all respond to `area()` and `perimeter()`. We'll build a notification system with Email, SMS, and Push notifications. And we'll create a complete plugin architecture that demonstrates dynamic polymorphism.

**Let's embrace many forms.**

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

- 🔧 **The 2026 Python Metromap: Constructor – Building Objects** – Employee onboarding system; automatic attribute initialization.

- 👪 **The 2026 Python Metromap: Inheritance – Reusing Parent Classes** – Vehicle fleet manager with Car, Truck, and Motorcycle classes.

- 🎭 **The 2026 Python Metromap: Polymorphism – One Interface, Many Forms** – Payment processing with CreditCard, PayPal, and Crypto implementations. **⬅️ YOU ARE HERE**

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules. 🔜 *Up Next*

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🎭 Section 1: Polymorphism Basics – Many Forms, One Interface

Polymorphism allows different classes to have methods with the same name but different implementations, enabling code to work with objects of various types through a common interface.

**SOLID Principle Applied: Liskov Substitution** – Objects of derived classes must be substitutable for objects of the base class.

**Design Pattern: Strategy Pattern** – Different behaviors encapsulated in different classes with a common interface.

```python
"""
POLYMORPHISM BASICS: MANY FORMS, ONE INTERFACE

This section covers the fundamentals of polymorphism.

SOLID Principle: Liskov Substitution
- Objects of derived classes must be substitutable for base class

Design Pattern: Strategy Pattern
- Different behaviors with common interface
"""

from typing import List, Any
from abc import ABC, abstractmethod
import math


def demonstrate_basic_polymorphism():
    """
    Demonstrates basic polymorphism with animal sounds.
    
    Different animals implement the same method differently.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC POLYMORPHISM")
    print("=" * 60)
    
    # DIFFERENT CLASSES, SAME METHOD NAME
    print("\n1. ANIMAL SOUNDS – Same method, different behaviors")
    print("-" * 40)
    
    class Animal:
        """Base animal class."""
        
        def __init__(self, name: str):
            self.name = name
        
        def make_sound(self) -> str:
            """Make animal sound (to be overridden)."""
            return "Some generic sound"
        
        def move(self) -> str:
            """How the animal moves."""
            return "The animal moves"
    
    class Dog(Animal):
        def make_sound(self) -> str:
            return "Woof! Woof!"
        
        def move(self) -> str:
            return "The dog runs on four legs"
    
    class Cat(Animal):
        def make_sound(self) -> str:
            return "Meow!"
        
        def move(self) -> str:
            return "The cat walks silently"
    
    class Bird(Animal):
        def make_sound(self) -> str:
            return "Chirp! Chirp!"
        
        def move(self) -> str:
            return "The bird flies through the air"
    
    # Polymorphism in action
    animals: List[Animal] = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Tweety")
    ]
    
    for animal in animals:
        print(f"  {animal.name} says: {animal.make_sound()}")
        print(f"    {animal.move()}")
    
    # POLYMORPHIC FUNCTION
    print("\n2. POLYMORPHIC FUNCTION – Works with any Animal")
    print("-" * 40)
    
    def animal_show(animal: Animal) -> None:
        """Function that works with any Animal type."""
        print(f"  {animal.name} performs: {animal.make_sound()}")
    
    animal_show(Dog("Rex"))
    animal_show(Cat("Luna"))
    animal_show(Bird("Sunny"))
    
    # DUCK TYPING (Python's approach to polymorphism)
    print("\n3. DUCK TYPING – "If it walks like a duck and quacks like a duck...")
    print("-" * 40)
    
    class Duck:
        def make_sound(self) -> str:
            return "Quack! Quack!"
        
        def move(self) -> str:
            return "The duck waddles"
    
    class Person:
        def make_sound(self) -> str:
            return "Hello there!"
        
        def move(self) -> str:
            return "The person walks on two legs"
    
    # Python doesn't require inheritance – just the right methods
    def process_creature(creature):
        """Works with any object that has make_sound() and move()."""
        print(f"  Sound: {creature.make_sound()}")
        print(f"  Movement: {creature.move()}")
    
    print("  Duck (no inheritance from Animal):")
    process_creature(Duck())
    print("  Person (no inheritance from Animal):")
    process_creature(Person())
    
    print("\n  💡 Python uses duck typing – if it has the method, it works!")


def demonstrate_polymorphism_with_shapes():
    """
    Demonstrates polymorphism with geometric shapes.
    
    All shapes implement area() and perimeter() differently.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: POLYMORPHISM WITH SHAPES")
    print("=" * 60)
    
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        """Abstract base class for all shapes."""
        
        @abstractmethod
        def area(self) -> float:
            """Calculate area of the shape."""
            pass
        
        @abstractmethod
        def perimeter(self) -> float:
            """Calculate perimeter of the shape."""
            pass
        
        def describe(self) -> str:
            """Describe the shape (uses polymorphic methods)."""
            return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"
    
    class Circle(Shape):
        def __init__(self, radius: float):
            self.radius = radius
        
        def area(self) -> float:
            return math.pi * self.radius ** 2
        
        def perimeter(self) -> float:
            return 2 * math.pi * self.radius
        
        def __str__(self) -> str:
            return f"Circle(r={self.radius})"
    
    class Rectangle(Shape):
        def __init__(self, width: float, height: float):
            self.width = width
            self.height = height
        
        def area(self) -> float:
            return self.width * self.height
        
        def perimeter(self) -> float:
            return 2 * (self.width + self.height)
        
        def __str__(self) -> str:
            return f"Rectangle({self.width}×{self.height})"
    
    class Triangle(Shape):
        def __init__(self, a: float, b: float, c: float):
            self.a = a
            self.b = b
            self.c = c
        
        def area(self) -> float:
            # Heron's formula
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        
        def perimeter(self) -> float:
            return self.a + self.b + self.c
        
        def __str__(self) -> str:
            return f"Triangle({self.a},{self.b},{self.c})"
    
    class Square(Rectangle):
        def __init__(self, side: float):
            super().__init__(side, side)
        
        def __str__(self) -> str:
            return f"Square(side={self.width})"
    
    # Polymorphic collection
    shapes: List[Shape] = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Square(4)
    ]
    
    print("\n1. POLYMORPHIC SHAPE COLLECTION")
    print("-" * 40)
    
    for shape in shapes:
        print(f"  {shape}: {shape.describe()}")
    
    # Polymorphic function
    print("\n2. POLYMORPHIC FUNCTION – calculate_total_area")
    print("-" * 40)
    
    def calculate_total_area(shapes: List[Shape]) -> float:
        """Calculate total area of any collection of shapes."""
        return sum(shape.area() for shape in shapes)
    
    total = calculate_total_area(shapes)
    print(f"  Total area of all shapes: {total:.2f}")
    
    # Sorting polymorphic objects
    print("\n3. SORTING POLYMORPHIC OBJECTS")
    print("-" * 40)
    
    shapes_by_area = sorted(shapes, key=lambda s: s.area())
    print("  Shapes sorted by area:")
    for shape in shapes_by_area:
        print(f"    {shape}: area = {shape.area():.2f}")
    
    shapes_by_perimeter = sorted(shapes, key=lambda s: s.perimeter(), reverse=True)
    print("\n  Shapes sorted by perimeter (largest first):")
    for shape in shapes_by_perimeter:
        print(f"    {shape}: perimeter = {shape.perimeter():.2f}")


def demonstrate_duck_typing():
    """
    Demonstrates Python's duck typing approach to polymorphism.
    
    Duck typing: "If it walks like a duck and quacks like a duck, it's a duck."
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: DUCK TYPING – Python's Dynamic Polymorphism")
    print("=" * 60)
    
    # COMPLETELY UNRELATED CLASSES with same method names
    print("\n1. UNRELATED CLASSES with same interface")
    print("-" * 40)
    
    class Airplane:
        def start(self) -> str:
            return "Airplane engines roaring to life"
        
        def stop(self) -> str:
            return "Airplane engines shutting down"
        
        def get_status(self) -> str:
            return "Airplane ready for takeoff"
    
    class Car:
        def start(self) -> str:
            return "Car engine starting with a vroom"
        
        def stop(self) -> str:
            return "Car engine turning off"
        
        def get_status(self) -> str:
            return "Car ready to drive"
    
    class Boat:
        def start(self) -> str:
            return "Boat motor sputtering to life"
        
        def stop(self) -> str:
            return "Boat motor winding down"
        
        def get_status(self) -> str:
            return "Boat ready to sail"
    
    # Polymorphic function works with ANY object that has the required methods
    def operate_vehicle(vehicle):
        """Works with any object that has start(), stop(), and get_status()."""
        print(f"  Starting: {vehicle.start()}")
        print(f"  Status: {vehicle.get_status()}")
        print(f"  Stopping: {vehicle.stop()}")
    
    print("  Operating Airplane:")
    operate_vehicle(Airplane())
    print("\n  Operating Car:")
    operate_vehicle(Car())
    print("\n  Operating Boat:")
    operate_vehicle(Boat())
    
    # PRACTICAL: DATA PROCESSING WITH DUCK TYPING
    print("\n2. PRACTICAL: DATA PROCESSING PIPELINE")
    print("-" * 40)
    
    class CSVProcessor:
        def process(self, data: str) -> List[List[str]]:
            """Process CSV data."""
            lines = data.strip().split('\n')
            return [line.split(',') for line in lines]
        
        def get_format(self) -> str:
            return "CSV"
    
    class JSONProcessor:
        def process(self, data: str) -> dict:
            """Process JSON data."""
            import json
            return json.loads(data)
        
        def get_format(self) -> str:
            return "JSON"
    
    class XMLProcessor:
        def process(self, data: str) -> str:
            """Process XML data (simplified)."""
            # In reality, would parse XML
            return f"Parsed XML: {data[:50]}..."
        
        def get_format(self) -> str:
            return "XML"
    
    def process_data(processor, data: str):
        """Polymorphic data processing."""
        print(f"  Processing {processor.get_format()} data...")
        result = processor.process(data)
        print(f"  Result type: {type(result).__name__}")
        return result
    
    csv_data = "name,age\nAlice,28\nBob,35"
    json_data = '{"name": "Alice", "age": 28}'
    xml_data = '<person><name>Alice</name><age>28</age></person>'
    
    process_data(CSVProcessor(), csv_data)
    process_data(JSONProcessor(), json_data)
    process_data(XMLProcessor(), xml_data)


if __name__ == "__main__":
    demonstrate_basic_polymorphism()
    demonstrate_polymorphism_with_shapes()
    demonstrate_duck_typing()
```

---

## 💳 Section 2: Payment Processing System

A complete payment processing system demonstrating polymorphism with different payment methods.

**SOLID Principles Applied:**
- Liskov Substitution: All payment methods can be processed uniformly
- Open/Closed: New payment methods can be added without modifying existing code

**Design Patterns:**
- Strategy Pattern: Different payment strategies with common interface
- Factory Pattern: Creates appropriate payment method

```python
"""
PAYMENT PROCESSING SYSTEM

This section builds a payment processing system using polymorphism.

SOLID Principles Applied:
- Liskov Substitution: All payment methods processed uniformly
- Open/Closed: New payment methods can be added

Design Patterns:
- Strategy Pattern: Different payment strategies with common interface
- Factory Pattern: Creates appropriate payment method
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum
import uuid
import re
import random


class PaymentStatus(Enum):
    """Payment status."""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class PaymentResult:
    """Result of a payment transaction."""
    
    def __init__(self, success: bool, transaction_id: str, message: str,
                 amount: float, status: PaymentStatus = None):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
        self.amount = amount
        self.status = status or (PaymentStatus.COMPLETED if success else PaymentStatus.FAILED)
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "success": self.success,
            "transaction_id": self.transaction_id,
            "message": self.message,
            "amount": self.amount,
            "status": self.status.value,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __str__(self) -> str:
        status_icon = "✅" if self.success else "❌"
        return f"{status_icon} {self.message} (ID: {self.transaction_id})"


class PaymentMethod(ABC):
    """
    Abstract base class for all payment methods.
    
    SOLID: Liskov Substitution - All payment methods can be used as PaymentMethod
    """
    
    def __init__(self, method_name: str):
        self.method_name = method_name
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process a payment."""
        pass
    
    @abstractmethod
    def validate(self) -> Tuple[bool, str]:
        """Validate payment method details."""
        pass
    
    @abstractmethod
    def get_fee(self, amount: float) -> float:
        """Calculate transaction fee."""
        pass
    
    def refund(self, transaction_id: str, amount: float) -> PaymentResult:
        """Refund a payment."""
        # Base implementation - can be overridden
        return PaymentResult(True, f"REF-{transaction_id}",
                            f"Refund of ${amount:.2f} processed", amount, PaymentStatus.REFUNDED)


class CreditCard(PaymentMethod):
    """Credit card payment method."""
    
    def __init__(self, card_number: str, expiry_month: int, expiry_year: int, cvv: str):
        super().__init__("Credit Card")
        self.card_number = card_number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.cvv = cvv
        self.card_type = self._detect_card_type()
    
    def _detect_card_type(self) -> str:
        """Detect card type from number."""
        first_digit = self.card_number[0]
        if first_digit == '4':
            return "Visa"
        elif first_digit == '5':
            return "Mastercard"
        elif first_digit == '3':
            return "American Express"
        elif first_digit == '6':
            return "Discover"
        return "Unknown"
    
    def validate(self) -> Tuple[bool, str]:
        """Validate credit card details."""
        if not self.card_number or len(self.card_number) < 13:
            return False, "Invalid card number length"
        
        if not self.card_number.isdigit():
            return False, "Card number must contain only digits"
        
        # Luhn algorithm (simplified check)
        if not self._luhn_check():
            return False, "Invalid card number"
        
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        if self.expiry_year < current_year or \
           (self.expiry_year == current_year and self.expiry_month < current_month):
            return False, "Card has expired"
        
        if self.expiry_year > current_year + 10:
            return False, "Invalid expiry year"
        
        if not self.cvv.isdigit() or len(self.cvv) not in [3, 4]:
            return False, "Invalid CVV"
        
        return True, "Valid"
    
    def _luhn_check(self) -> bool:
        """Perform Luhn algorithm check."""
        digits = [int(d) for d in self.card_number[::-1]]
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0
    
    def get_fee(self, amount: float) -> float:
        """Calculate credit card processing fee."""
        return amount * 0.029 + 0.30
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process credit card payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        # Simulate payment processing
        if random.random() < 0.95:
            transaction_id = f"CC-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            fee = self.get_fee(amount)
            return PaymentResult(True, transaction_id,
                               f"Payment approved. Fee: ${fee:.2f}", amount)
        else:
            return PaymentResult(False, "", "Payment declined by bank", amount)


class PayPal(PaymentMethod):
    """PayPal payment method."""
    
    def __init__(self, email: str):
        super().__init__("PayPal")
        self.email = email
    
    def validate(self) -> Tuple[bool, str]:
        """Validate PayPal email."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, self.email):
            return False, "Invalid email address"
        return True, "Valid"
    
    def get_fee(self, amount: float) -> float:
        """Calculate PayPal processing fee."""
        return amount * 0.034 + 0.30
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process PayPal payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        if random.random() < 0.93:
            transaction_id = f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            fee = self.get_fee(amount)
            return PaymentResult(True, transaction_id,
                               f"PayPal payment successful. Fee: ${fee:.2f}", amount)
        else:
            return PaymentResult(False, "", "PayPal payment failed", amount)


class CryptoPayment(PaymentMethod):
    """Cryptocurrency payment method."""
    
    def __init__(self, wallet_address: str, crypto_type: str = "BTC"):
        super().__init__("Cryptocurrency")
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type
    
    def validate(self) -> Tuple[bool, str]:
        """Validate wallet address."""
        if not self.wallet_address or len(self.wallet_address) < 26:
            return False, "Invalid wallet address"
        return True, "Valid"
    
    def get_fee(self, amount: float) -> float:
        """Calculate crypto transaction fee."""
        return amount * 0.01
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process cryptocurrency payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        if random.random() < 0.97:
            transaction_id = f"CRYPTO-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            fee = self.get_fee(amount)
            return PaymentResult(True, transaction_id,
                               f"Crypto payment confirmed. Fee: ${fee:.2f}", amount)
        else:
            return PaymentResult(False, "", "Transaction failed - network error", amount)
    
    def refund(self, transaction_id: str, amount: float) -> PaymentResult:
        """Crypto refunds are more complex."""
        return PaymentResult(False, "", "Crypto refunds not supported", amount)


class BankTransfer(PaymentMethod):
    """Bank transfer payment method."""
    
    def __init__(self, account_number: str, routing_number: str, account_name: str):
        super().__init__("Bank Transfer")
        self.account_number = account_number
        self.routing_number = routing_number
        self.account_name = account_name
    
    def validate(self) -> Tuple[bool, str]:
        """Validate bank account details."""
        if not self.account_number or len(self.account_number) < 8:
            return False, "Invalid account number"
        if not self.routing_number or len(self.routing_number) != 9:
            return False, "Invalid routing number"
        if not self.routing_number.isdigit():
            return False, "Routing number must be digits"
        if not self.account_name:
            return False, "Account name required"
        return True, "Valid"
    
    def get_fee(self, amount: float) -> float:
        """Calculate bank transfer fee."""
        return 0.0 if amount > 1000 else 5.00
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process bank transfer."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        if random.random() < 0.98:
            transaction_id = f"BT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            fee = self.get_fee(amount)
            return PaymentResult(True, transaction_id,
                               f"Bank transfer initiated. Fee: ${fee:.2f}", amount)
        else:
            return PaymentResult(False, "", "Bank transfer failed", amount)


class GiftCard(PaymentMethod):
    """Gift card payment method."""
    
    def __init__(self, card_number: str, pin: str, balance: float):
        super().__init__("Gift Card")
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    
    def validate(self) -> Tuple[bool, str]:
        """Validate gift card."""
        if not self.card_number or len(self.card_number) < 10:
            return False, "Invalid card number"
        if not self.pin or len(self.pin) < 4:
            return False, "Invalid PIN"
        if self.balance <= 0:
            return False, "Card has no balance"
        return True, "Valid"
    
    def get_fee(self, amount: float) -> float:
        """Gift cards have no fees."""
        return 0.0
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process gift card payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        if amount > self.balance:
            return PaymentResult(False, "", f"Insufficient balance. Available: ${self.balance:.2f}", amount)
        
        transaction_id = f"GC-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
        self.balance -= amount
        return PaymentResult(True, transaction_id,
                           f"Gift card payment successful. Remaining balance: ${self.balance:.2f}", amount)


class PaymentProcessor:
    """
    Payment processor that handles different payment methods polymorphically.
    
    Design Pattern: Strategy Pattern - Different payment strategies
    """
    
    def __init__(self):
        self.transaction_history: List[PaymentResult] = []
        self.payment_methods: Dict[str, PaymentMethod] = {}
    
    def register_method(self, name: str, method: PaymentMethod) -> None:
        """Register a payment method."""
        self.payment_methods[name] = method
        print(f"  Registered payment method: {name}")
    
    def process_payment(self, method_name: str, amount: float,
                       currency: str = "USD") -> PaymentResult:
        """Process a payment using a registered method."""
        if method_name not in self.payment_methods:
            return PaymentResult(False, "", f"Payment method '{method_name}' not found", amount)
        
        method = self.payment_methods[method_name]
        print(f"\n  Processing ${amount:.2f} via {method.method_name}...")
        
        result = method.process_payment(amount, currency)
        self.transaction_history.append(result)
        
        return result
    
    def get_total_processed(self) -> float:
        """Get total amount processed successfully."""
        return sum(t.amount for t in self.transaction_history if t.success)
    
    def get_success_rate(self) -> float:
        """Calculate success rate percentage."""
        if not self.transaction_history:
            return 0.0
        successful = sum(1 for t in self.transaction_history if t.success)
        return (successful / len(self.transaction_history)) * 100
    
    def get_transaction_summary(self) -> str:
        """Get transaction summary."""
        lines = []
        lines.append("=" * 60)
        lines.append("TRANSACTION HISTORY")
        lines.append("=" * 60)
        
        for tx in self.transaction_history[-10:]:
            status = "✅" if tx.success else "❌"
            lines.append(f"  {status} ${tx.amount:>8.2f} - {tx.message[:40]}")
        
        lines.append("-" * 60)
        lines.append(f"Total Processed: ${self.get_total_processed():,.2f}")
        lines.append(f"Success Rate: {self.get_success_rate():.1f}%")
        lines.append(f"Total Transactions: {len(self.transaction_history)}")
        lines.append("=" * 60)
        
        return "\n".join(lines)
    
    def get_payment_stats(self) -> Dict[str, Any]:
        """Get payment statistics by method."""
        stats = {}
        for method_name, method in self.payment_methods.items():
            method_tx = [t for t in self.transaction_history 
                        if "via" in t.message and method_name in t.message]
            stats[method_name] = {
                "total_attempts": len(method_tx),
                "successful": sum(1 for t in method_tx if t.success),
                "total_amount": sum(t.amount for t in method_tx if t.success)
            }
        return stats


class PaymentMethodFactory:
    """
    Factory for creating payment methods.
    
    Design Pattern: Factory Pattern - Creates appropriate payment method
    """
    
    @staticmethod
    def create_credit_card(card_number: str, expiry_month: int,
                          expiry_year: int, cvv: str) -> CreditCard:
        return CreditCard(card_number, expiry_month, expiry_year, cvv)
    
    @staticmethod
    def create_paypal(email: str) -> PayPal:
        return PayPal(email)
    
    @staticmethod
    def create_crypto(wallet_address: str, crypto_type: str = "BTC") -> CryptoPayment:
        return CryptoPayment(wallet_address, crypto_type)
    
    @staticmethod
    def create_bank_transfer(account_number: str, routing_number: str,
                            account_name: str) -> BankTransfer:
        return BankTransfer(account_number, routing_number, account_name)
    
    @staticmethod
    def create_gift_card(card_number: str, pin: str, balance: float) -> GiftCard:
        return GiftCard(card_number, pin, balance)


def demonstrate_payment_system():
    """
    Demonstrate the polymorphic payment processing system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: PAYMENT PROCESSING SYSTEM")
    print("=" * 60)
    
    processor = PaymentProcessor()
    factory = PaymentMethodFactory()
    
    print("\n1. REGISTERING PAYMENT METHODS")
    print("-" * 40)
    
    # Register different payment methods
    processor.register_method("credit_card", 
                             factory.create_credit_card("4111111111111111", 12, 2026, "123"))
    processor.register_method("paypal",
                             factory.create_paypal("customer@example.com"))
    processor.register_method("crypto",
                             factory.create_crypto("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    processor.register_method("bank_transfer",
                             factory.create_bank_transfer("12345678", "123456789", "Alice Chen"))
    processor.register_method("gift_card",
                             factory.create_gift_card("GC-1234567890", "1234", 100.00))
    
    print("\n2. PROCESSING PAYMENTS (Polymorphic)")
    print("-" * 40)
    
    # Process payments using different methods - same interface!
    payments = [
        ("credit_card", 299.99),
        ("paypal", 149.99),
        ("crypto", 89.99),
        ("bank_transfer", 500.00),
        ("gift_card", 75.00),
        ("credit_card", 45.50),
        ("paypal", 199.99)
    ]
    
    for method, amount in payments:
        result = processor.process_payment(method, amount)
        print(f"    {result}")
    
    print("\n3. PAYMENT STATISTICS")
    print("-" * 40)
    
    stats = processor.get_payment_stats()
    for method, data in stats.items():
        print(f"  {method}:")
        print(f"    Attempts: {data['total_attempts']}")
        print(f"    Successful: {data['successful']}")
        print(f"    Total Amount: ${data['total_amount']:,.2f}")
    
    print("\n4. TRANSACTION SUMMARY")
    print("-" * 40)
    
    print(processor.get_transaction_summary())
    
    print("\n5. FEE COMPARISON (Polymorphic fee calculation)")
    print("-" * 40)
    
    amount = 100.00
    for method_name, method in processor.payment_methods.items():
        fee = method.get_fee(amount)
        print(f"  {method_name}: ${fee:.2f} fee on ${amount:.2f}")
    
    print("\n6. POLYMORPHIC REFUNDS")
    print("-" * 40)
    
    # Different refund behaviors for different methods
    for method_name, method in processor.payment_methods.items():
        result = method.refund("TEST-123", 50.00)
        print(f"  {method_name}: {result.message}")


if __name__ == "__main__":
    demonstrate_payment_system()
```

---

## 📢 Section 3: Notification System

A polymorphic notification system supporting multiple delivery channels.

**SOLID Principles Applied:**
- Liskov Substitution: All notifiers can be used interchangeably
- Interface Segregation: Clean, focused interface for notifications

**Design Patterns:**
- Strategy Pattern: Different notification strategies
- Observer Pattern: Notify multiple recipients

```python
"""
NOTIFICATION SYSTEM

This section builds a polymorphic notification system.

SOLID Principles Applied:
- Liskov Substitution: All notifiers interchangeable
- Interface Segregation: Clean notification interface

Design Patterns:
- Strategy Pattern: Different notification strategies
- Observer Pattern: Notify multiple recipients
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum
import time
import random


class NotificationPriority(Enum):
    """Notification priority levels."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class NotificationResult:
    """Result of sending a notification."""
    
    def __init__(self, success: bool, channel: str, recipient: str,
                 message: str, error: Optional[str] = None):
        self.success = success
        self.channel = channel
        self.recipient = recipient
        self.message = message
        self.error = error
        self.timestamp = datetime.now()
    
    def __str__(self) -> str:
        status = "✅" if self.success else "❌"
        return f"{status} {self.channel} → {self.recipient}: {self.message[:50]}"


class Notifier(ABC):
    """
    Abstract base class for all notifiers.
    
    SOLID: Liskov Substitution - All notifiers can be used as Notifier
    """
    
    def __init__(self, name: str):
        self.name = name
        self.history: List[NotificationResult] = []
    
    @abstractmethod
    def send(self, recipient: str, subject: str, body: str,
             priority: NotificationPriority = NotificationPriority.NORMAL) -> NotificationResult:
        """Send a notification."""
        pass
    
    @abstractmethod
    def get_channel_type(self) -> str:
        """Get the channel type."""
        pass
    
    def get_history(self, limit: int = 10) -> List[NotificationResult]:
        """Get recent notification history."""
        return self.history[-limit:][::-1]
    
    def _record_result(self, result: NotificationResult) -> None:
        """Record a notification result."""
        self.history.append(result)
    
    def get_success_rate(self) -> float:
        """Calculate success rate."""
        if not self.history:
            return 100.0
        successful = sum(1 for r in self.history if r.success)
        return (successful / len(self.history)) * 100


class EmailNotifier(Notifier):
    """Email notification channel."""
    
    def __init__(self, smtp_server: str = "smtp.gmail.com"):
        super().__init__("Email")
        self.smtp_server = smtp_server
    
    def get_channel_type(self) -> str:
        return "Email"
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def send(self, recipient: str, subject: str, body: str,
             priority: NotificationPriority = NotificationPriority.NORMAL) -> NotificationResult:
        """Send an email notification."""
        if not self._validate_email(recipient):
            result = NotificationResult(False, self.name, recipient, "Invalid email address",
                                       "Email format validation failed")
            self._record_result(result)
            return result
        
        # Simulate email sending
        time.sleep(0.05)  # Simulate network delay
        
        # 95% success rate
        if random.random() < 0.95:
            result = NotificationResult(True, self.name, recipient,
                                       f"Email sent: '{subject}'")
        else:
            result = NotificationResult(False, self.name, recipient,
                                       "Failed to send email", "SMTP connection error")
        
        self._record_result(result)
        return result


class SMSNotifier(Notifier):
    """SMS notification channel."""
    
    def __init__(self, api_key: str = "test-api-key"):
        super().__init__("SMS")
        self.api_key = api_key
    
    def get_channel_type(self) -> str:
        return "SMS"
    
    def _validate_phone(self, phone: str) -> bool:
        """Validate phone number."""
        digits = ''.join(c for c in phone if c.isdigit())
        return 10 <= len(digits) <= 15
    
    def send(self, recipient: str, subject: str, body: str,
             priority: NotificationPriority = NotificationPriority.NORMAL) -> NotificationResult:
        """Send an SMS notification."""
        if not self._validate_phone(recipient):
            result = NotificationResult(False, self.name, recipient,
                                       "Invalid phone number", "Phone validation failed")
            self._record_result(result)
            return result
        
        # SMS has character limit
        if len(body) > 160:
            body = body[:157] + "..."
        
        time.sleep(0.03)  # Simulate API call
        
        if random.random() < 0.92:
            result = NotificationResult(True, self.name, recipient,
                                       f"SMS sent: {body[:50]}...")
        else:
            result = NotificationResult(False, self.name, recipient,
                                       "Failed to send SMS", "Carrier network error")
        
        self._record_result(result)
        return result


class PushNotifier(Notifier):
    """Push notification channel."""
    
    def __init__(self, app_id: str = "mobile-app"):
        super().__init__("Push Notification")
        self.app_id = app_id
    
    def get_channel_type(self) -> str:
        return "Push"
    
    def send(self, recipient: str, subject: str, body: str,
             priority: NotificationPriority = NotificationPriority.NORMAL) -> NotificationResult:
        """Send a push notification."""
        # Push notifications use device tokens
        if not recipient or len(recipient) < 10:
            result = NotificationResult(False, self.name, recipient,
                                       "Invalid device token", "Token validation failed")
            self._record_result(result)
            return result
        
        time.sleep(0.02)
        
        if random.random() < 0.98:
            result = NotificationResult(True, self.name, recipient,
                                       f"Push notification sent: {subject}")
        else:
            result = NotificationResult(False, self.name, recipient,
                                       "Failed to send push", "APNS connection error")
        
        self._record_result(result)
        return result


class SlackNotifier(Notifier):
    """Slack notification channel."""
    
    def __init__(self, webhook_url: str = "https://hooks.slack.com/..."):
        super().__init__("Slack")
        self.webhook_url = webhook_url
    
    def get_channel_type(self) -> str:
        return "Slack"
    
    def send(self, recipient: str, subject: str, body: str,
             priority: NotificationPriority = NotificationPriority.NORMAL) -> NotificationResult:
        """Send a Slack notification."""
        # Slack uses channel/webhook, recipient is channel name
        time.sleep(0.04)
        
        if random.random() < 0.96:
            result = NotificationResult(True, self.name, f"#{recipient}",
                                       f"Slack message sent to #{recipient}")
        else:
            result = NotificationResult(False, self.name, f"#{recipient}",
                                       "Failed to send Slack message", "API rate limit")
        
        self._record_result(result)
        return result


class NotificationService:
    """
    Notification service that manages multiple notifiers.
    
    Design Pattern: Strategy Pattern - Different notification strategies
    """
    
    def __init__(self):
        self.notifiers: Dict[str, Notifier] = {}
    
    def register_notifier(self, name: str, notifier: Notifier) -> None:
        """Register a notifier."""
        self.notifiers[name] = notifier
        print(f"  Registered notifier: {name}")
    
    def send_notification(self, notifier_name: str, recipient: str,
                         subject: str, body: str,
                         priority: NotificationPriority = NotificationPriority.NORMAL) -> NotificationResult:
        """Send a notification using a specific notifier."""
        if notifier_name not in self.notifiers:
            return NotificationResult(False, notifier_name, recipient,
                                     f"Notifier '{notifier_name}' not found")
        
        notifier = self.notifiers[notifier_name]
        return notifier.send(recipient, subject, body, priority)
    
    def broadcast(self, recipients: Dict[str, str], subject: str, body: str,
                  priority: NotificationPriority = NotificationPriority.NORMAL) -> List[NotificationResult]:
        """
        Broadcast to multiple recipients using different notifiers.
        
        Args:
            recipients: Dictionary mapping notifier_name to recipient
            subject: Notification subject
            body: Notification body
            priority: Priority level
            
        Returns:
            List of notification results
        """
        results = []
        for notifier_name, recipient in recipients.items():
            result = self.send_notification(notifier_name, recipient, subject, body, priority)
            results.append(result)
        return results
    
    def get_all_statistics(self) -> Dict[str, Any]:
        """Get statistics for all notifiers."""
        stats = {}
        for name, notifier in self.notifiers.items():
            stats[name] = {
                "channel": notifier.get_channel_type(),
                "total_sent": len(notifier.history),
                "success_rate": notifier.get_success_rate()
            }
        return stats


def demonstrate_notification_system():
    """
    Demonstrate the polymorphic notification system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: NOTIFICATION SYSTEM")
    print("=" * 60)
    
    service = NotificationService()
    
    print("\n1. REGISTERING NOTIFIERS")
    print("-" * 40)
    
    service.register_notifier("email", EmailNotifier())
    service.register_notifier("sms", SMSNotifier())
    service.register_notifier("push", PushNotifier())
    service.register_notifier("slack", SlackNotifier())
    
    print("\n2. SENDING NOTIFICATIONS (Polymorphic)")
    print("-" * 40)
    
    # Same interface, different implementations
    notifications = [
        ("email", "alice@example.com", "Welcome!", "Thanks for joining!"),
        ("sms", "+1-555-123-4567", "Alert", "Your order has shipped!"),
        ("push", "device_token_12345", "New Message", "You have a new message"),
        ("slack", "general", "Deployment", "New version deployed to production")
    ]
    
    for notifier, recipient, subject, body in notifications:
        result = service.send_notification(notifier, recipient, subject, body)
        print(f"  {result}")
    
    print("\n3. BROADCAST TO MULTIPLE CHANNELS")
    print("-" * 40)
    
    recipients = {
        "email": "admin@example.com",
        "slack": "alerts",
        "sms": "+1-555-999-8888"
    }
    
    results = service.broadcast(recipients, "System Alert", "High CPU usage detected",
                               NotificationPriority.HIGH)
    
    for result in results:
        print(f"  {result}")
    
    print("\n4. NOTIFIER STATISTICS")
    print("-" * 40)
    
    stats = service.get_all_statistics()
    for name, data in stats.items():
        print(f"  {name}:")
        print(f"    Channel: {data['channel']}")
        print(f"    Total Sent: {data['total_sent']}")
        print(f"    Success Rate: {data['success_rate']:.1f}%")
    
    print("\n5. NOTIFICATION HISTORY (Polymorphic)")
    print("-" * 40)
    
    for name, notifier in service.notifiers.items():
        history = notifier.get_history(3)
        if history:
            print(f"\n  {name} recent notifications:")
            for result in history:
                print(f"    {result}")
    
    print("\n6. PRIORITY-BASED ROUTING")
    print("-" * 40)
    
    # Different priorities could route to different channels
    def send_priority_notification(service: NotificationService, recipient: str,
                                   subject: str, body: str, priority: NotificationPriority):
        """Send notification based on priority."""
        if priority == NotificationPriority.URGENT:
            # Send via multiple channels for urgent
            recipients = {
                "email": recipient,
                "sms": "+1-555-123-4567",
                "slack": "urgent-alerts"
            }
            return service.broadcast(recipients, f"URGENT: {subject}", body, priority)
        elif priority == NotificationPriority.HIGH:
            return [service.send_notification("email", recipient, subject, body, priority)]
        else:
            return [service.send_notification("email", recipient, subject, body, priority)]
    
    result = send_priority_notification(service, "user@example.com",
                                       "Security Alert", "Unusual login detected",
                                       NotificationPriority.URGENT)
    print(f"  Urgent notification sent via {len(result)} channels")


if __name__ == "__main__":
    demonstrate_notification_system()
```

---

## 🔌 Section 4: Plugin Architecture

A complete plugin architecture demonstrating dynamic polymorphism where plugins are loaded and executed at runtime.

**SOLID Principles Applied:**
- Open/Closed: New plugins can be added without modifying core
- Dependency Inversion: Core depends on plugin interfaces

**Design Patterns:**
- Strategy Pattern: Different plugin strategies
- Factory Pattern: Creates plugin instances
- Chain of Responsibility: Multiple plugins can process data

```python
"""
PLUGIN ARCHITECTURE

This section builds a plugin architecture demonstrating dynamic polymorphism.

SOLID Principles Applied:
- Open/Closed: New plugins added without modifying core
- Dependency Inversion: Core depends on plugin interfaces

Design Patterns:
- Strategy Pattern: Different plugin strategies
- Factory Pattern: Creates plugin instances
- Chain of Responsibility: Multiple plugins process data
"""

from typing import List, Dict, Any, Optional, Callable
from abc import ABC, abstractmethod
from datetime import datetime
import importlib
import inspect
import os


class Plugin(ABC):
    """
    Abstract base class for all plugins.
    
    SOLID: Dependency Inversion - Core depends on this abstraction
    """
    
    @abstractmethod
    def get_name(self) -> str:
        """Get plugin name."""
        pass
    
    @abstractmethod
    def get_version(self) -> str:
        """Get plugin version."""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Get plugin description."""
        pass
    
    @abstractmethod
    def execute(self, data: Any, context: Dict[str, Any]) -> Any:
        """Execute the plugin."""
        pass


class TextProcessorPlugin(Plugin):
    """Plugin for processing text."""
    
    def get_name(self) -> str:
        return "Text Processor"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_description(self) -> str:
        return "Processes text data (uppercase, lowercase, title case)"
    
    def execute(self, data: Any, context: Dict[str, Any]) -> Any:
        """Process text data."""
        if not isinstance(data, str):
            raise ValueError("TextProcessorPlugin requires string input")
        
        operation = context.get("operation", "uppercase")
        
        if operation == "uppercase":
            return data.upper()
        elif operation == "lowercase":
            return data.lower()
        elif operation == "title":
            return data.title()
        elif operation == "reverse":
            return data[::-1]
        else:
            return data


class DataFilterPlugin(Plugin):
    """Plugin for filtering data."""
    
    def get_name(self) -> str:
        return "Data Filter"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_description(self) -> str:
        return "Filters data based on criteria"
    
    def execute(self, data: Any, context: Dict[str, Any]) -> Any:
        """Filter data."""
        if not isinstance(data, list):
            raise ValueError("DataFilterPlugin requires list input")
        
        min_value = context.get("min_value")
        max_value = context.get("max_value")
        field = context.get("field")
        
        if field:
            # Filter list of dicts by field value
            filtered = []
            for item in data:
                if isinstance(item, dict) and field in item:
                    value = item[field]
                    if min_value is not None and value < min_value:
                        continue
                    if max_value is not None and value > max_value:
                        continue
                    filtered.append(item)
            return filtered
        else:
            # Filter list of numbers
            filtered = [x for x in data if isinstance(x, (int, float))]
            if min_value is not None:
                filtered = [x for x in filtered if x >= min_value]
            if max_value is not None:
                filtered = [x for x in filtered if x <= max_value]
            return filtered


class StatsCalculatorPlugin(Plugin):
    """Plugin for statistical calculations."""
    
    def get_name(self) -> str:
        return "Stats Calculator"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_description(self) -> str:
        return "Calculates statistics (sum, average, min, max)"
    
    def execute(self, data: Any, context: Dict[str, Any]) -> Any:
        """Calculate statistics."""
        if not isinstance(data, (list, tuple)):
            raise ValueError("StatsCalculatorPlugin requires list or tuple input")
        
        numeric_data = [x for x in data if isinstance(x, (int, float))]
        
        if not numeric_data:
            return {"error": "No numeric data found"}
        
        operation = context.get("operation", "all")
        
        if operation == "sum":
            return sum(numeric_data)
        elif operation == "avg":
            return sum(numeric_data) / len(numeric_data)
        elif operation == "min":
            return min(numeric_data)
        elif operation == "max":
            return max(numeric_data)
        elif operation == "count":
            return len(numeric_data)
        else:
            return {
                "sum": sum(numeric_data),
                "avg": sum(numeric_data) / len(numeric_data),
                "min": min(numeric_data),
                "max": max(numeric_data),
                "count": len(numeric_data)
            }


class FormatterPlugin(Plugin):
    """Plugin for formatting output."""
    
    def get_name(self) -> str:
        return "Formatter"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_description(self) -> str:
        return "Formats output (JSON, CSV, table)"
    
    def execute(self, data: Any, context: Dict[str, Any]) -> Any:
        """Format data."""
        format_type = context.get("format", "json")
        
        if format_type == "json":
            import json
            return json.dumps(data, indent=2, default=str)
        elif format_type == "csv" and isinstance(data, list) and data:
            if isinstance(data[0], dict):
                import csv
                from io import StringIO
                output = StringIO()
                writer = csv.DictWriter(output, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                return output.getvalue()
        elif format_type == "table" and isinstance(data, list) and data:
            if isinstance(data[0], dict):
                headers = list(data[0].keys())
                rows = [[str(item.get(h, "")) for h in headers] for item in data]
                # Calculate column widths
                widths = [max(len(h), max((len(row[i]) for row in rows), default=0)) 
                         for i, h in enumerate(headers)]
                
                # Build table
                result = []
                result.append("+" + "+".join("-" * (w + 2) for w in widths) + "+")
                result.append("|" + "|".join(f" {h:<{w}} " for h, w in zip(headers, widths)) + "|")
                result.append("+" + "+".join("-" * (w + 2) for w in widths) + "+")
                for row in rows:
                    result.append("|" + "|".join(f" {row[i]:<{w}} " for i, w in enumerate(widths)) + "|")
                result.append("+" + "+".join("-" * (w + 2) for w in widths) + "+")
                return "\n".join(result)
        
        return str(data)


class ValidationPlugin(Plugin):
    """Plugin for data validation."""
    
    def get_name(self) -> str:
        return "Data Validator"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_description(self) -> str:
        return "Validates data against rules"
    
    def execute(self, data: Any, context: Dict[str, Any]) -> Any:
        """Validate data."""
        rules = context.get("rules", {})
        errors = []
        
        for field, rule in rules.items():
            value = data.get(field) if isinstance(data, dict) else None
            
            if rule.get("required") and value is None:
                errors.append(f"{field} is required")
            
            if value is not None:
                if "min" in rule and value < rule["min"]:
                    errors.append(f"{field} must be at least {rule['min']}")
                if "max" in rule and value > rule["max"]:
                    errors.append(f"{field} must be at most {rule['max']}")
                if "type" in rule and not isinstance(value, rule["type"]):
                    errors.append(f"{field} must be of type {rule['type'].__name__}")
        
        return {"valid": len(errors) == 0, "errors": errors}


class PluginManager:
    """
    Manages and executes plugins.
    
    Design Pattern: Strategy Pattern - Pluggable strategies
    Design Pattern: Registry Pattern - Central plugin registry
    """
    
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
        self.plugin_chain: List[str] = []
    
    def register_plugin(self, plugin: Plugin) -> None:
        """Register a plugin."""
        self.plugins[plugin.get_name()] = plugin
        print(f"  Registered plugin: {plugin.get_name()} v{plugin.get_version()}")
    
    def unregister_plugin(self, plugin_name: str) -> bool:
        """Unregister a plugin."""
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            if plugin_name in self.plugin_chain:
                self.plugin_chain.remove(plugin_name)
            return True
        return False
    
    def execute_plugin(self, plugin_name: str, data: Any,
                      context: Optional[Dict] = None) -> Any:
        """Execute a single plugin."""
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin '{plugin_name}' not found")
        
        plugin = self.plugins[plugin_name]
        context = context or {}
        
        print(f"  Executing: {plugin.get_name()} - {plugin.get_description()}")
        start_time = datetime.now()
        
        result = plugin.execute(data, context)
        
        elapsed = (datetime.now() - start_time).total_seconds() * 1000
        print(f"    Completed in {elapsed:.2f}ms")
        
        return result
    
    def execute_chain(self, data: Any, context: Optional[Dict] = None) -> Any:
        """Execute plugins in chain order."""
        context = context or {}
        result = data
        
        for plugin_name in self.plugin_chain:
            result = self.execute_plugin(plugin_name, result, context)
        
        return result
    
    def set_plugin_chain(self, plugin_names: List[str]) -> None:
        """Set the order of plugin execution."""
        for name in plugin_names:
            if name not in self.plugins:
                raise ValueError(f"Plugin '{name}' not registered")
        self.plugin_chain = plugin_names
        print(f"  Plugin chain set: {' → '.join(plugin_names)}")
    
    def list_plugins(self) -> List[Dict]:
        """List all registered plugins."""
        return [
            {
                "name": p.get_name(),
                "version": p.get_version(),
                "description": p.get_description()
            }
            for p in self.plugins.values()
        ]
    
    def get_plugin_info(self, plugin_name: str) -> Optional[Dict]:
        """Get plugin information."""
        if plugin_name in self.plugins:
            p = self.plugins[plugin_name]
            return {
                "name": p.get_name(),
                "version": p.get_version(),
                "description": p.get_description(),
                "methods": [m for m in dir(p) if not m.startswith("_") and callable(getattr(p, m))]
            }
        return None


def demonstrate_plugin_architecture():
    """
    Demonstrate the plugin architecture.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: PLUGIN ARCHITECTURE")
    print("=" * 60)
    
    manager = PluginManager()
    
    print("\n1. REGISTERING PLUGINS")
    print("-" * 40)
    
    manager.register_plugin(TextProcessorPlugin())
    manager.register_plugin(DataFilterPlugin())
    manager.register_plugin(StatsCalculatorPlugin())
    manager.register_plugin(FormatterPlugin())
    manager.register_plugin(ValidationPlugin())
    
    print("\n2. LISTING REGISTERED PLUGINS")
    print("-" * 40)
    
    for plugin_info in manager.list_plugins():
        print(f"  📦 {plugin_info['name']} v{plugin_info['version']}")
        print(f"     {plugin_info['description']}")
    
    print("\n3. SINGLE PLUGIN EXECUTION")
    print("-" * 40)
    
    # Text processing
    result = manager.execute_plugin("Text Processor", "hello world", {"operation": "uppercase"})
    print(f"  Text Processor result: {result}")
    
    # Data filtering
    data = [10, 25, 30, 45, 50, 65, 70, 85, 90]
    result = manager.execute_plugin("Data Filter", data, {"min_value": 30, "max_value": 70})
    print(f"  Data Filter result: {result}")
    
    # Statistics
    result = manager.execute_plugin("Stats Calculator", data, {"operation": "all"})
    print(f"  Stats Calculator result: {result}")
    
    print("\n4. PLUGIN CHAIN EXECUTION")
    print("-" * 40)
    
    # Set up a processing pipeline
    manager.set_plugin_chain(["Data Filter", "Stats Calculator", "Formatter"])
    
    raw_data = [5, 12, 23, 35, 48, 52, 67, 71, 84, 93]
    print(f"  Raw data: {raw_data}")
    
    result = manager.execute_chain(raw_data, {
        "min_value": 20,
        "max_value": 80,
        "operation": "all",
        "format": "json"
    })
    
    print(f"\n  Pipeline result:")
    print(f"  {result[:200]}..." if len(str(result)) > 200 else f"  {result}")
    
    print("\n5. DATA VALIDATION PLUGIN")
    print("-" * 40)
    
    validation_rules = {
        "name": {"required": True, "type": str},
        "age": {"required": True, "type": int, "min": 18, "max": 120},
        "email": {"required": True, "type": str}
    }
    
    valid_data = {"name": "Alice", "age": 25, "email": "alice@example.com"}
    invalid_data = {"name": "Bob", "age": 15}  # Missing email, age too low
    
    result = manager.execute_plugin("Data Validator", valid_data, {"rules": validation_rules})
    print(f"  Valid data: {result}")
    
    result = manager.execute_plugin("Data Validator", invalid_data, {"rules": validation_rules})
    print(f"  Invalid data: {result}")
    
    print("\n6. PLUGIN INFORMATION")
    print("-" * 40)
    
    info = manager.get_plugin_info("Stats Calculator")
    if info:
        print(f"  {info['name']} v{info['version']}")
        print(f"  Description: {info['description']}")
        print(f"  Methods: {', '.join(info['methods'][:5])}...")
    
    print("\n7. DYNAMIC PLUGIN REGISTRATION (Runtime)")
    print("-" * 40)
    
    # Create a custom plugin on the fly
    class ReverseStringPlugin(Plugin):
        def get_name(self) -> str:
            return "String Reverser"
        
        def get_version(self) -> str:
            return "1.0.0"
        
        def get_description(self) -> str:
            return "Reverses a string"
        
        def execute(self, data: Any, context: Dict[str, Any]) -> Any:
            if isinstance(data, str):
                return data[::-1]
            return data
    
    manager.register_plugin(ReverseStringPlugin())
    result = manager.execute_plugin("String Reverser", "Python Programming")
    print(f"  String Reverser result: {result}")


if __name__ == "__main__":
    demonstrate_plugin_architecture()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Polymorphism Basics** – Different classes implement the same method differently. Objects of different types can be treated uniformly through a common interface.

- **Duck Typing** – Python's approach to polymorphism. "If it walks like a duck and quacks like a duck, it's a duck." Objects don't need to inherit from a common base class—they just need the required methods.

- **Liskov Substitution Principle** – Objects of derived classes must be substitutable for objects of the base class. Code that works with a base class should work with any derived class.

- **Open/Closed Principle** – Classes open for extension, closed for modification. New functionality can be added by creating new classes, not changing existing ones.

- **Payment Processing** – Different payment methods (CreditCard, PayPal, Crypto, BankTransfer, GiftCard) all implement `process_payment()` with different logic. Same interface, different implementations.

- **Shape Calculator** – Circle, Rectangle, Triangle, Square all implement `area()` and `perimeter()` with different formulas. Polymorphic collection processing.

- **Notification System** – Email, SMS, Push, Slack notifications all implement `send()` with different delivery mechanisms. Broadcast to multiple channels.

- **Plugin Architecture** – Dynamic polymorphism where plugins are registered and executed at runtime. Chain of Responsibility pattern for processing pipelines.

- **SOLID Principles Applied** – Liskov Substitution (all subclasses substitutable), Open/Closed (new payment methods added without changes), Dependency Inversion (core depends on abstractions), Interface Segregation (clean plugin interfaces).

- **Design Patterns Used** – Strategy Pattern (payment strategies), Factory Pattern (payment method creation), Observer Pattern (notifications), Chain of Responsibility (plugin chain), Registry Pattern (plugin management).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Inheritance – Reusing Parent Classes

- **📚 Series D Catalog:** Object-Oriented Programming Line – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Encapsulation – Protecting Data (Series D, Story 5)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 4 | 2 | 67% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **27** | **25** | **52%** |

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

**Next Story:** Series D, Story 5: The 2026 Python Metromap: Encapsulation – Protecting Data

---

## 📝 Your Invitation

You've mastered polymorphism. Now build something with what you've learned:

1. **Build a shape calculator** – Create Shape base class with Circle, Rectangle, Triangle. Calculate total area of mixed shape collections.

2. **Create a payment system** – Implement different payment methods with polymorphic `process_payment()`.

3. **Build a notification service** – Create Email, SMS, Push, Slack notifiers with polymorphic `send()`.

4. **Create a data export system** – Implement JSON, CSV, XML, Excel exporters with polymorphic `export()`.

5. **Build a plugin system** – Create an architecture where plugins can be loaded dynamically at runtime.

**You've mastered polymorphism. Next stop: Encapsulation!**

---

*Found this helpful? Clap, comment, and share what you built with polymorphism. Next stop: Encapsulation!* 🚇