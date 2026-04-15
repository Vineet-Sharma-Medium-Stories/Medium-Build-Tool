# The 2026 Python Metromap: Abstraction – Hiding Complexity

## Series D: Object-Oriented Programming (OOP) Line | Story 6 of 6

![The 2026 Python Metromap/images/Abstraction – Hiding Complexity](images/Abstraction – Hiding Complexity.png)

## 📖 Introduction

**Welcome to the sixth and final stop on the Object-Oriented Programming Line.**

You've mastered classes, constructors, inheritance, polymorphism, and encapsulation. You can create hierarchies, treat objects through common interfaces, and protect internal data. But there's one more pillar of object-oriented programming that ties everything together—abstraction.

Abstraction is the concept of hiding complex implementation details and exposing only the essential features of an object. It's about creating simplified interfaces that let users interact with complex systems without needing to understand their inner workings. When you drive a car, you use the steering wheel and pedals—you don't need to understand the engine, transmission, or fuel injection system. That's abstraction.

In Python, abstraction is implemented using abstract base classes (ABCs) and abstract methods. Abstract methods are declared but contain no implementation—they define the interface that concrete subclasses must implement. This allows you to design flexible, extensible systems where the "what" is separated from the "how."

This story—**The 2026 Python Metromap: Abstraction – Hiding Complexity**—is your guide to mastering abstraction in Python. We'll build a complete email notification service with abstract base classes. We'll create a data storage system with multiple backends (file, database, cloud). We'll implement a payment gateway with different providers. And we'll build a complete report generation system with abstract report generators.

**Let's hide the complexity.**

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

- 🎭 **The 2026 Python Metromap: Polymorphism – One Interface, Many Forms** – Payment processing with CreditCard, PayPal, and Crypto implementations.

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules.

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations. **⬅️ YOU ARE HERE**

### Series E: File & Data Handling Line (5 Stories) – Next Station

- 📂 **The 2026 Python Metromap: File I/O – Reading & Writing** – Log file analyzer; server log parsing; error extraction; report generation. 🔜 *Up Next*

- 📊 **The 2026 Python Metromap: CSV & JSON Processing** – Sales data importer/exporter; vendor CSV integration; API JSON formatting.

- ⚠️ **The 2026 Python Metromap: Exception Handling – Graceful Failures** – Resilient web scraper; network error handling; request retries.

- 🔧 **The 2026 Python Metromap: Context Managers – The with Statement** – Database connection pool; automatic resource cleanup.

- 🗺️ **The 2026 Python Metromap: Working with Paths & Directories** – Automated backup system; file organization by date; log rotation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🎨 Section 1: Abstraction Basics – Abstract Base Classes

Abstraction hides implementation details and exposes only essential interfaces using abstract base classes (ABCs).

**SOLID Principle Applied: Dependency Inversion** – High-level modules depend on abstractions, not concrete implementations.

**Design Pattern: Template Method Pattern** – Abstract class defines algorithm skeleton, subclasses implement details.

```python
"""
ABSTRACTION BASICS: ABSTRACT BASE CLASSES

This section covers the fundamentals of abstraction using ABCs.

SOLID Principle: Dependency Inversion
- High-level modules depend on abstractions

Design Pattern: Template Method Pattern
- Abstract class defines skeleton, subclasses implement details
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import math


def demonstrate_abstract_base_classes():
    """
    Demonstrates abstract base classes and abstract methods.
    
    Abstract classes cannot be instantiated. They define interfaces
    that concrete subclasses must implement.
    """
    print("=" * 60)
    print("SECTION 1A: ABSTRACT BASE CLASSES")
    print("=" * 60)
    
    # ABSTRACT CLASS
    print("\n1. DEFINING AN ABSTRACT CLASS")
    print("-" * 40)
    
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
            """Concrete method (not abstract)."""
            return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"
    
    # Cannot instantiate abstract class
    try:
        shape = Shape()
    except TypeError as e:
        print(f"  Cannot instantiate abstract class: {e}")
    
    # CONCRETE SUBCLASSES
    print("\n2. CONCRETE SUBCLASSES (Implementing abstract methods)")
    print("-" * 40)
    
    class Circle(Shape):
        def __init__(self, radius: float):
            self.radius = radius
        
        def area(self) -> float:
            return math.pi * self.radius ** 2
        
        def perimeter(self) -> float:
            return 2 * math.pi * self.radius
    
    class Rectangle(Shape):
        def __init__(self, width: float, height: float):
            self.width = width
            self.height = height
        
        def area(self) -> float:
            return self.width * self.height
        
        def perimeter(self) -> float:
            return 2 * (self.width + self.height)
    
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    print(f"  Circle: {circle.describe()}")
    print(f"  Rectangle: {rectangle.describe()}")
    
    # ABSTRACT PROPERTIES
    print("\n3. ABSTRACT PROPERTIES")
    print("-" * 40)
    
    class Vehicle(ABC):
        @property
        @abstractmethod
        def make(self) -> str:
            pass
        
        @property
        @abstractmethod
        def model(self) -> str:
            pass
        
        @abstractmethod
        def start(self) -> str:
            pass
    
    class Car(Vehicle):
        def __init__(self, make: str, model: str):
            self._make = make
            self._model = model
        
        @property
        def make(self) -> str:
            return self._make
        
        @property
        def model(self) -> str:
            return self._model
        
        def start(self) -> str:
            return f"{self.make} {self.model} engine started"
    
    car = Car("Toyota", "Camry")
    print(f"  {car.start()}")
    
    # PARTIAL IMPLEMENTATION (still abstract)
    print("\n4. PARTIAL IMPLEMENTATION")
    print("-" * 40)
    
    class DataProcessor(ABC):
        @abstractmethod
        def extract(self) -> Any:
            pass
        
        @abstractmethod
        def transform(self, data: Any) -> Any:
            pass
        
        @abstractmethod
        def load(self, data: Any) -> bool:
            pass
        
        def process(self) -> bool:
            """Template method using abstract methods."""
            data = self.extract()
            transformed = self.transform(data)
            return self.load(transformed)
    
    class CSVProcessor(DataProcessor):
        def extract(self) -> Any:
            print("    Extracting from CSV...")
            return {"rows": [["name", "age"], ["Alice", 28], ["Bob", 35]]}
        
        def transform(self, data: Any) -> Any:
            print("    Transforming CSV data...")
            headers = data["rows"][0]
            rows = data["rows"][1:]
            return [dict(zip(headers, row)) for row in rows]
        
        def load(self, data: Any) -> bool:
            print(f"    Loading {len(data)} records...")
            return True
    
    processor = CSVProcessor()
    result = processor.process()
    print(f"  Processing result: {result}")


def demonstrate_abc_usage():
    """
    Demonstrates practical usage of abstract base classes.
    
    ABCs are useful for defining interfaces, plugin systems,
    and ensuring consistent implementation across subclasses.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: PRACTICAL ABC USAGE")
    print("=" * 60)
    
    # REGISTERING VIRTUAL SUBCLASSES
    print("\n1. VIRTUAL SUBCLASSES (register())")
    print("-" * 40)
    
    class Drawable(ABC):
        @abstractmethod
        def draw(self) -> str:
            pass
    
    # Regular class (not inheriting from Drawable)
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y
        
        def draw(self) -> str:
            return f"Drawing point at ({self.x}, {self.y})"
    
    # Register Point as virtual subclass of Drawable
    Drawable.register(Point)
    
    point = Point(10, 20)
    print(f"  Is Point a Drawable? {isinstance(point, Drawable)}")
    print(f"  {point.draw()}")
    
    # CHECKING FOR ABSTRACT METHODS
    print("\n2. CHECKING ABSTRACT METHODS")
    print("-" * 40)
    
    from abc import ABCMeta
    
    class Plugin(ABC):
        @abstractmethod
        def execute(self) -> None:
            pass
        
        @abstractmethod
        def get_name(self) -> str:
            pass
    
    # Check what methods need to be implemented
    print(f"  Abstract methods in Plugin: {Plugin.__abstractmethods__}")
    
    # CUSTOM ABC WITH VALIDATION
    print("\n3. CUSTOM ABC WITH VALIDATION")
    print("-" * 40)
    
    class Validatable(ABC):
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            # Check that subclass implements required methods
            required = {'validate', 'to_dict'}
            missing = required - set(dir(cls))
            if missing:
                raise TypeError(f"Class {cls.__name__} missing required methods: {missing}")
    
    class User(Validatable):
        def __init__(self, name: str, email: str):
            self.name = name
            self.email = email
        
        def validate(self) -> bool:
            return "@" in self.email and len(self.name) > 0
        
        def to_dict(self) -> Dict:
            return {"name": self.name, "email": self.email}
    
    user = User("Alice", "alice@example.com")
    print(f"  User valid: {user.validate()}")
    print(f"  User dict: {user.to_dict()}")
    
    # This would fail at class definition
    try:
        class BadUser(Validatable):
            def __init__(self, name: str):
                self.name = name
            # Missing validate() and to_dict()
    except TypeError as e:
        print(f"  Error: {e}")


def demonstrate_abstraction_vs_encapsulation():
    """
    Demonstrates the difference between abstraction and encapsulation.
    
    - Abstraction: Hides complexity, shows only essential features
    - Encapsulation: Hides data, requires method access
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: ABSTRACTION VS ENCAPSULATION")
    print("=" * 60)
    
    class CoffeeMachine(ABC):
        """
        Abstraction: Simple interface for making coffee.
        User doesn't need to know about water heating, grinding, etc.
        """
        
        @abstractmethod
        def make_coffee(self, type: str) -> str:
            """Make a cup of coffee (abstract interface)."""
            pass
        
        @abstractmethod
        def get_status(self) -> Dict:
            """Get machine status (abstract interface)."""
            pass
    
    class EspressoMachine(CoffeeMachine):
        """
        Concrete implementation with encapsulated complexity.
        """
        
        def __init__(self):
            # Encapsulated internal state
            self._water_level = 100
            self._bean_level = 100
            self._temperature = 20
            self._is_on = False
        
        def _heat_water(self) -> None:
            """Private method - internal complexity."""
            print("    Heating water to 93°C...")
            self._temperature = 93
        
        def _grind_beans(self) -> None:
            """Private method - internal complexity."""
            print("    Grinding beans...")
            self._bean_level -= 5
        
        def _pump_water(self) -> None:
            """Private method - internal complexity."""
            print("    Pumping water through coffee...")
            self._water_level -= 10
        
        def make_coffee(self, type: str) -> str:
            """Public interface - user doesn't see internal complexity."""
            if not self._is_on:
                return "Error: Machine is off"
            
            if self._water_level < 20:
                return "Error: Low water"
            
            if self._bean_level < 10:
                return "Error: Low beans"
            
            # Complex internal process hidden from user
            self._heat_water()
            self._grind_beans()
            self._pump_water()
            
            return f"Here's your {type} coffee! ☕"
        
        def turn_on(self) -> None:
            self._is_on = True
            print("  Machine turned on")
        
        def turn_off(self) -> None:
            self._is_on = False
            print("  Machine turned off")
        
        def get_status(self) -> Dict:
            """Simplified status interface."""
            return {
                "is_on": self._is_on,
                "water_level": self._water_level,
                "bean_level": self._bean_level,
                "temperature": self._temperature
            }
    
    machine = EspressoMachine()
    
    print("\n1. SIMPLE INTERFACE (Abstraction)")
    print("-" * 40)
    print("  User only needs to know: turn_on() and make_coffee()")
    
    machine.turn_on()
    result = machine.make_coffee("latte")
    print(f"  Result: {result}")
    
    print("\n2. ENCAPSULATED COMPLEXITY")
    print("-" * 40)
    print("  Internal state is hidden but accessible via interface:")
    status = machine.get_status()
    for key, value in status.items():
        print(f"    {key}: {value}")
    
    print("\n3. COMPARISON")
    print("-" * 40)
    print("""
    Abstraction (What):
        - Simplifies interface (make_coffee, get_status)
        - Hides how things work
        - Focuses on what the object does
    
    Encapsulation (How):
        - Protects internal data (_water_level, _bean_level)
        - Hides implementation details (_heat_water, _grind_beans)
        - Focuses on how the object works internally
    
    Both work together: Abstraction defines the interface,
    Encapsulation protects the implementation.
    """)


if __name__ == "__main__":
    demonstrate_abstract_base_classes()
    demonstrate_abc_usage()
    demonstrate_abstraction_vs_encapsulation()
```

---

## 📧 Section 2: Email Notification Service

A complete email notification service with abstract base classes for different providers.

**SOLID Principles Applied:**
- Dependency Inversion: High-level notification service depends on EmailProvider abstraction
- Open/Closed: New providers can be added without modifying existing code

**Design Patterns:**
- Strategy Pattern: Different email providers as strategies
- Factory Pattern: Creates appropriate provider

```python
"""
EMAIL NOTIFICATION SERVICE

This section builds an email notification service using abstraction.

SOLID Principles Applied:
- Dependency Inversion: Depends on EmailProvider abstraction
- Open/Closed: New providers can be added

Design Patterns:
- Strategy Pattern: Different email providers as strategies
- Factory Pattern: Creates appropriate provider
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from enum import Enum
import smtplib
import ssl
import json
import time
import random


class EmailPriority(Enum):
    """Email priority levels."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class EmailMessage:
    """Represents an email message (Value Object)."""
    
    def __init__(self, to_email: str, subject: str, body: str,
                 from_email: Optional[str] = None,
                 cc: Optional[List[str]] = None,
                 bcc: Optional[List[str]] = None,
                 priority: EmailPriority = EmailPriority.NORMAL,
                 attachments: Optional[List[str]] = None):
        self.to_email = to_email
        self.subject = subject
        self.body = body
        self.from_email = from_email or "noreply@metromap.com"
        self.cc = cc or []
        self.bcc = bcc or []
        self.priority = priority
        self.attachments = attachments or []
        self.timestamp = datetime.now()
        self.message_id = f"msg-{int(self.timestamp.timestamp())}-{random.randint(1000, 9999)}"
    
    def to_dict(self) -> Dict:
        return {
            "message_id": self.message_id,
            "to": self.to_email,
            "from": self.from_email,
            "subject": self.subject,
            "body": self.body[:100] + "..." if len(self.body) > 100 else self.body,
            "priority": self.priority.value,
            "timestamp": self.timestamp.isoformat()
        }


class EmailResult:
    """Result of sending an email."""
    
    def __init__(self, success: bool, message_id: str, details: str,
                 error: Optional[str] = None):
        self.success = success
        self.message_id = message_id
        self.details = details
        self.error = error
        self.timestamp = datetime.now()
    
    def __str__(self) -> str:
        status = "✅" if self.success else "❌"
        return f"{status} {self.message_id}: {self.details}"


class EmailProvider(ABC):
    """
    Abstract base class for email providers.
    
    SOLID: Dependency Inversion - High-level modules depend on this abstraction
    """
    
    @abstractmethod
    def send(self, message: EmailMessage) -> EmailResult:
        """Send an email message."""
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Get provider name."""
        pass
    
    @abstractmethod
    def get_status(self) -> Dict:
        """Get provider status."""
        pass


class SMTPProvider(EmailProvider):
    """SMTP email provider."""
    
    def __init__(self, smtp_server: str, port: int, username: str, password: str,
                 use_tls: bool = True):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self._sent_count = 0
        self._error_count = 0
    
    def get_provider_name(self) -> str:
        return f"SMTP ({self.smtp_server})"
    
    def get_status(self) -> Dict:
        return {
            "provider": "SMTP",
            "server": self.smtp_server,
            "port": self.port,
            "sent": self._sent_count,
            "errors": self._error_count,
            "uptime": "99.9%"
        }
    
    def send(self, message: EmailMessage) -> EmailResult:
        """Send email via SMTP."""
        try:
            # Simulate SMTP sending (would use real SMTP in production)
            print(f"    Connecting to {self.smtp_server}:{self.port}...")
            time.sleep(0.1)
            
            # Simulate success/failure
            if random.random() < 0.95:
                self._sent_count += 1
                return EmailResult(
                    True, message.message_id,
                    f"Email sent to {message.to_email} via SMTP"
                )
            else:
                self._error_count += 1
                return EmailResult(
                    False, message.message_id,
                    "Failed to send",
                    "SMTP connection timeout"
                )
        except Exception as e:
            self._error_count += 1
            return EmailResult(False, message.message_id, "Exception occurred", str(e))


class SendGridProvider(EmailProvider):
    """SendGrid API email provider."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._sent_count = 0
        self._error_count = 0
    
    def get_provider_name(self) -> str:
        return "SendGrid"
    
    def get_status(self) -> Dict:
        return {
            "provider": "SendGrid",
            "api_version": "v3",
            "sent": self._sent_count,
            "errors": self._error_count,
            "rate_limit": "100/second"
        }
    
    def send(self, message: EmailMessage) -> EmailResult:
        """Send email via SendGrid API."""
        try:
            print(f"    Calling SendGrid API...")
            time.sleep(0.08)
            
            if random.random() < 0.97:
                self._sent_count += 1
                return EmailResult(
                    True, message.message_id,
                    f"Email sent to {message.to_email} via SendGrid"
                )
            else:
                self._error_count += 1
                return EmailResult(
                    False, message.message_id,
                    "API rate limit exceeded",
                    "Rate limit reached"
                )
        except Exception as e:
            self._error_count += 1
            return EmailResult(False, message.message_id, "API error", str(e))


class MockProvider(EmailProvider):
    """Mock email provider for testing."""
    
    def __init__(self):
        self._sent_count = 0
        self._sent_emails: List[EmailMessage] = []
    
    def get_provider_name(self) -> str:
        return "Mock Provider"
    
    def get_status(self) -> Dict:
        return {
            "provider": "Mock",
            "sent": self._sent_count,
            "queued": len(self._sent_emails)
        }
    
    def send(self, message: EmailMessage) -> EmailResult:
        """Mock sending (always succeeds)."""
        self._sent_count += 1
        self._sent_emails.append(message)
        print(f"    [MOCK] Would send: {message.subject} to {message.to_email}")
        return EmailResult(
            True, message.message_id,
            f"[MOCK] Email would be sent to {message.to_email}"
        )
    
    def get_sent_emails(self) -> List[EmailMessage]:
        """Get all sent emails (for testing)."""
        return self._sent_emails.copy()


class EmailService:
    """
    Email service using abstraction.
    
    Design Pattern: Strategy Pattern - Pluggable email providers
    """
    
    def __init__(self, default_provider: Optional[EmailProvider] = None):
        self._default_provider = default_provider or MockProvider()
        self._providers: Dict[str, EmailProvider] = {
            self._default_provider.get_provider_name(): self._default_provider
        }
        self._history: List[EmailResult] = []
    
    def register_provider(self, provider: EmailProvider) -> None:
        """Register an email provider."""
        self._providers[provider.get_provider_name()] = provider
        print(f"  Registered provider: {provider.get_provider_name()}")
    
    def send_email(self, message: EmailMessage,
                  provider_name: Optional[str] = None) -> EmailResult:
        """Send an email using specified or default provider."""
        provider = self._providers.get(provider_name) if provider_name else self._default_provider
        
        if not provider:
            return EmailResult(False, message.message_id,
                              f"Provider '{provider_name}' not found",
                              "Provider not registered")
        
        print(f"\n  Sending email via {provider.get_provider_name()}...")
        result = provider.send(message)
        self._history.append(result)
        return result
    
    def send_batch(self, messages: List[EmailMessage],
                  provider_name: Optional[str] = None) -> List[EmailResult]:
        """Send multiple emails."""
        results = []
        for message in messages:
            results.append(self.send_email(message, provider_name))
        return results
    
    def get_statistics(self) -> Dict:
        """Get email service statistics."""
        total = len(self._history)
        successful = sum(1 for r in self._history if r.success)
        
        provider_stats = {}
        for name, provider in self._providers.items():
            provider_stats[name] = provider.get_status()
        
        return {
            "total_emails": total,
            "successful": successful,
            "failed": total - successful,
            "success_rate": (successful / total * 100) if total > 0 else 0,
            "providers": provider_stats
        }
    
    def get_history(self, limit: int = 20) -> List[EmailResult]:
        """Get recent email history."""
        return self._history[-limit:][::-1]


class EmailBuilder:
    """
    Builder for creating email messages.
    
    Design Pattern: Builder Pattern - Builds email incrementally
    """
    
    def __init__(self):
        self._to_email = None
        self._subject = None
        self._body = None
        self._from_email = None
        self._cc = []
        self._bcc = []
        self._priority = EmailPriority.NORMAL
        self._attachments = []
    
    def to(self, email: str) -> 'EmailBuilder':
        self._to_email = email
        return self
    
    def subject(self, subject: str) -> 'EmailBuilder':
        self._subject = subject
        return self
    
    def body(self, body: str) -> 'EmailBuilder':
        self._body = body
        return self
    
    def from_email(self, email: str) -> 'EmailBuilder':
        self._from_email = email
        return self
    
    def cc(self, email: str) -> 'EmailBuilder':
        self._cc.append(email)
        return self
    
    def bcc(self, email: str) -> 'EmailBuilder':
        self._bcc.append(email)
        return self
    
    def priority(self, priority: EmailPriority) -> 'EmailBuilder':
        self._priority = priority
        return self
    
    def attach(self, file_path: str) -> 'EmailBuilder':
        self._attachments.append(file_path)
        return self
    
    def build(self) -> EmailMessage:
        if not self._to_email or not self._subject or not self._body:
            raise ValueError("To, Subject, and Body are required")
        
        return EmailMessage(
            to_email=self._to_email,
            subject=self._subject,
            body=self._body,
            from_email=self._from_email,
            cc=self._cc,
            bcc=self._bcc,
            priority=self._priority,
            attachments=self._attachments
        )


def demonstrate_email_service():
    """
    Demonstrate the email notification service.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: EMAIL NOTIFICATION SERVICE")
    print("=" * 60)
    
    # Create email service with mock provider (for testing)
    service = EmailService(MockProvider())
    
    print("\n1. REGISTERING PROVIDERS")
    print("-" * 40)
    
    service.register_provider(SMTPProvider("smtp.gmail.com", 587, "user@gmail.com", "password"))
    service.register_provider(SendGridProvider("SG.api_key_12345"))
    
    print("\n2. BUILDING EMAILS (Builder Pattern)")
    print("-" * 40)
    
    email1 = (EmailBuilder()
              .to("alice@example.com")
              .subject("Welcome to Metromap!")
              .body("Thank you for joining our platform.\n\nBest regards,\nThe Metromap Team")
              .priority(EmailPriority.NORMAL)
              .build())
    
    email2 = (EmailBuilder()
              .to("bob@example.com")
              .subject("Your Order Confirmation")
              .body("Your order #ORD-12345 has been confirmed.\n\nTrack your order at: https://metromap.com/track/12345")
              .cc("support@metromap.com")
              .priority(EmailPriority.HIGH)
              .build())
    
    email3 = (EmailBuilder()
              .to("admin@metromap.com")
              .subject("URGENT: System Alert")
              .body("High CPU usage detected on production server.")
              .priority(EmailPriority.URGENT)
              .build())
    
    print(f"  Built {len([email1, email2, email3])} emails")
    
    print("\n3. SENDING EMAILS (Abstracted Interface)")
    print("-" * 40)
    
    # Send via default provider (Mock)
    result1 = service.send_email(email1)
    print(f"  {result1}")
    
    # Send via specific provider
    result2 = service.send_email(email2, "SendGrid")
    print(f"  {result2}")
    
    result3 = service.send_email(email3, "SMTP (smtp.gmail.com)")
    print(f"  {result3}")
    
    print("\n4. EMAIL SERVICE STATISTICS")
    print("-" * 40)
    
    stats = service.get_statistics()
    for key, value in stats.items():
        if key == "providers":
            print(f"  {key}:")
            for provider, provider_stats in value.items():
                print(f"    {provider}: {provider_stats}")
        else:
            print(f"  {key}: {value}")
    
    print("\n5. BATCH SENDING")
    print("-" * 40)
    
    batch_emails = [
        (EmailBuilder().to("user1@example.com").subject("Newsletter #1").body("Content 1").build()),
        (EmailBuilder().to("user2@example.com").subject("Newsletter #1").body("Content 2").build()),
        (EmailBuilder().to("user3@example.com").subject("Newsletter #1").body("Content 3").build())
    ]
    
    results = service.send_batch(batch_emails, "Mock Provider")
    print(f"  Batch results: {sum(1 for r in results if r.success)}/{len(results)} successful")
    
    print("\n6. ABSTRACTION BENEFITS")
    print("-" * 40)
    
    print("""
    Benefits demonstrated:
    ✓ EmailService works with any EmailProvider (SMTP, SendGrid, Mock)
    ✓ Adding new provider doesn't change existing code
    ✓ Complex email protocols hidden behind simple send() interface
    ✓ Easy testing with MockProvider
    ✓ Consistent interface across all providers
    """)


if __name__ == "__main__":
    demonstrate_email_service()
```

---

## 💾 Section 3: Data Storage Abstraction

A complete data storage system with abstract base classes for different storage backends.

**SOLID Principles Applied:**
- Dependency Inversion: High-level storage service depends on StorageBackend abstraction
- Open/Closed: New storage backends can be added

**Design Patterns:**
- Strategy Pattern: Different storage strategies
- Adapter Pattern: Adapts different storage APIs

```python
"""
DATA STORAGE ABSTRACTION

This section builds a data storage system with abstract backends.

SOLID Principles Applied:
- Dependency Inversion: Depends on StorageBackend abstraction
- Open/Closed: New storage backends can be added

Design Patterns:
- Strategy Pattern: Different storage strategies
- Adapter Pattern: Adapts different storage APIs
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import json
import os
import pickle
import sqlite3


class StorageBackend(ABC):
    """
    Abstract base class for storage backends.
    
    SOLID: Dependency Inversion - High-level modules depend on this abstraction
    """
    
    @abstractmethod
    def save(self, key: str, data: Any) -> bool:
        """Save data with the given key."""
        pass
    
    @abstractmethod
    def load(self, key: str) -> Optional[Any]:
        """Load data by key."""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete data by key."""
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        """Check if key exists."""
        pass
    
    @abstractmethod
    def list_keys(self) -> List[str]:
        """List all keys."""
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Clear all data."""
        pass


class FileStorageBackend(StorageBackend):
    """File-based storage backend."""
    
    def __init__(self, base_dir: str = "./storage"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)
        self._file_extension = ".json"
    
    def _get_file_path(self, key: str) -> str:
        """Get file path for a key."""
        # Sanitize key for filename
        safe_key = key.replace("/", "_").replace("\\", "_")
        return os.path.join(self.base_dir, f"{safe_key}{self._file_extension}")
    
    def save(self, key: str, data: Any) -> bool:
        """Save data to JSON file."""
        try:
            file_path = self._get_file_path(key)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"  Error saving {key}: {e}")
            return False
    
    def load(self, key: str) -> Optional[Any]:
        """Load data from JSON file."""
        try:
            file_path = self._get_file_path(key)
            if not os.path.exists(file_path):
                return None
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"  Error loading {key}: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """Delete file."""
        try:
            file_path = self._get_file_path(key)
            if os.path.exists(file_path):
                os.remove(file_path)
            return True
        except Exception as e:
            print(f"  Error deleting {key}: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """Check if file exists."""
        return os.path.exists(self._get_file_path(key))
    
    def list_keys(self) -> List[str]:
        """List all stored keys."""
        keys = []
        for filename in os.listdir(self.base_dir):
            if filename.endswith(self._file_extension):
                key = filename[:-len(self._file_extension)]
                keys.append(key)
        return keys
    
    def clear(self) -> None:
        """Delete all stored files."""
        for key in self.list_keys():
            self.delete(key)


class DictStorageBackend(StorageBackend):
    """In-memory dictionary storage backend."""
    
    def __init__(self):
        self._data: Dict[str, Any] = {}
    
    def save(self, key: str, data: Any) -> bool:
        self._data[key] = data
        return True
    
    def load(self, key: str) -> Optional[Any]:
        return self._data.get(key)
    
    def delete(self, key: str) -> bool:
        if key in self._data:
            del self._data[key]
            return True
        return False
    
    def exists(self, key: str) -> bool:
        return key in self._data
    
    def list_keys(self) -> List[str]:
        return list(self._data.keys())
    
    def clear(self) -> None:
        self._data.clear()


class SQLiteStorageBackend(StorageBackend):
    """SQLite database storage backend."""
    
    def __init__(self, db_path: str = "storage.db"):
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self) -> None:
        """Initialize database table."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS storage (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
    
    def save(self, key: str, data: Any) -> bool:
        """Save data to SQLite."""
        try:
            value = json.dumps(data, default=str)
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT OR REPLACE INTO storage (key, value, updated_at)
                    VALUES (?, ?, CURRENT_TIMESTAMP)
                """, (key, value))
            return True
        except Exception as e:
            print(f"  Error saving {key}: {e}")
            return False
    
    def load(self, key: str) -> Optional[Any]:
        """Load data from SQLite."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("SELECT value FROM storage WHERE key = ?", (key,))
                row = cursor.fetchone()
                if row:
                    return json.loads(row[0])
            return None
        except Exception as e:
            print(f"  Error loading {key}: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """Delete data from SQLite."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("DELETE FROM storage WHERE key = ?", (key,))
            return True
        except Exception as e:
            print(f"  Error deleting {key}: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """Check if key exists in SQLite."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("SELECT 1 FROM storage WHERE key = ?", (key,))
                return cursor.fetchone() is not None
        except Exception:
            return False
    
    def list_keys(self) -> List[str]:
        """List all keys from SQLite."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("SELECT key FROM storage")
                return [row[0] for row in cursor.fetchall()]
        except Exception:
            return []
    
    def clear(self) -> None:
        """Clear all data from SQLite."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("DELETE FROM storage")
        except Exception:
            pass


class StorageService:
    """
    Storage service using abstraction.
    
    Design Pattern: Strategy Pattern - Pluggable storage backends
    """
    
    def __init__(self, backend: Optional[StorageBackend] = None):
        self._backend = backend or DictStorageBackend()
        self._cache: Dict[str, Any] = {}
        self._cache_enabled = True
    
    def set_backend(self, backend: StorageBackend) -> None:
        """Change storage backend."""
        self._backend = backend
        print(f"  Backend changed to {backend.__class__.__name__}")
    
    def enable_cache(self, enabled: bool) -> None:
        """Enable or disable caching."""
        self._cache_enabled = enabled
        if not enabled:
            self._cache.clear()
    
    def save(self, key: str, data: Any) -> bool:
        """Save data (with optional cache)."""
        if self._cache_enabled:
            self._cache[key] = data
        return self._backend.save(key, data)
    
    def load(self, key: str) -> Optional[Any]:
        """Load data (with optional cache)."""
        if self._cache_enabled and key in self._cache:
            return self._cache[key]
        
        data = self._backend.load(key)
        if self._cache_enabled and data is not None:
            self._cache[key] = data
        return data
    
    def delete(self, key: str) -> bool:
        """Delete data."""
        if self._cache_enabled and key in self._cache:
            del self._cache[key]
        return self._backend.delete(key)
    
    def exists(self, key: str) -> bool:
        """Check if key exists."""
        if self._cache_enabled and key in self._cache:
            return True
        return self._backend.exists(key)
    
    def list_keys(self) -> List[str]:
        """List all keys."""
        return self._backend.list_keys()
    
    def clear(self) -> None:
        """Clear all data."""
        if self._cache_enabled:
            self._cache.clear()
        self._backend.clear()
    
    def get_stats(self) -> Dict:
        """Get storage statistics."""
        keys = self.list_keys()
        return {
            "backend": self._backend.__class__.__name__,
            "total_keys": len(keys),
            "cache_enabled": self._cache_enabled,
            "cache_size": len(self._cache) if self._cache_enabled else 0
        }


def demonstrate_storage_system():
    """
    Demonstrate the data storage abstraction.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: DATA STORAGE ABSTRACTION")
    print("=" * 60)
    
    print("\n1. CREATING STORAGE SERVICE")
    print("-" * 40)
    
    # Start with dict backend (in-memory)
    storage = StorageService(DictStorageBackend())
    print(f"  Initial backend: {storage._backend.__class__.__name__}")
    
    print("\n2. SAVING AND LOADING DATA")
    print("-" * 40)
    
    # Save user data
    user_data = {
        "id": 1,
        "name": "Alice Chen",
        "email": "alice@example.com",
        "preferences": {"theme": "dark", "language": "en"}
    }
    
    storage.save("user:alice", user_data)
    storage.save("user:bob", {"id": 2, "name": "Bob Smith", "email": "bob@example.com"})
    storage.save("settings:app", {"version": "1.0", "debug": True})
    
    print("  Saved 3 records")
    
    # Load data
    loaded = storage.load("user:alice")
    print(f"  Loaded user: {loaded['name']}")
    
    # Check existence
    print(f"  Exists 'user:alice': {storage.exists('user:alice')}")
    print(f"  Exists 'user:charlie': {storage.exists('user:charlie')}")
    
    print("\n3. LISTING KEYS")
    print("-" * 40)
    
    keys = storage.list_keys()
    print(f"  All keys: {keys}")
    
    print("\n4. SWITCHING BACKENDS (File Storage)")
    print("-" * 40)
    
    # Switch to file backend
    storage.set_backend(FileStorageBackend("./demo_storage"))
    
    # Save same data to file backend
    storage.save("user:alice", user_data)
    storage.save("user:bob", {"id": 2, "name": "Bob Smith", "email": "bob@example.com"})
    
    print("  Data saved to files")
    
    # Load from file backend
    loaded = storage.load("user:alice")
    print(f"  Loaded from file: {loaded['name']}")
    
    print("\n5. SQLITE BACKEND")
    print("-" * 40)
    
    storage.set_backend(SQLiteStorageBackend("demo_storage.db"))
    storage.save("product:laptop", {"name": "Laptop", "price": 999.99})
    storage.save("product:mouse", {"name": "Mouse", "price": 29.99})
    
    products = [storage.load(f"product:{p}") for p in ["laptop", "mouse"]]
    print(f"  Products from SQLite: {[p['name'] for p in products]}")
    
    print("\n6. CACHING DEMONSTRATION")
    print("-" * 40)
    
    # Revert to dict backend for cache demo
    storage.set_backend(DictStorageBackend())
    storage.enable_cache(True)
    
    # First load (cache miss)
    import time
    start = time.time()
    storage.save("test", {"data": "value"})
    data = storage.load("test")
    first_load = time.time() - start
    
    # Second load (cache hit)
    start = time.time()
    data = storage.load("test")
    second_load = time.time() - start
    
    print(f"  First load (cache miss): {first_load:.6f}s")
    print(f"  Second load (cache hit): {second_load:.6f}s")
    print(f"  Cache speedup: {first_load/second_load:.0f}x")
    
    print("\n7. STORAGE STATISTICS")
    print("-" * 40)
    
    stats = storage.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n8. CLEANUP")
    print("-" * 40)
    
    storage.clear()
    print(f"  After clear: {storage.list_keys()}")
    
    # Clean up demo files
    import shutil
    if os.path.exists("./demo_storage"):
        shutil.rmtree("./demo_storage")
    if os.path.exists("demo_storage.db"):
        os.remove("demo_storage.db")
    print("  Cleaned up demo files")


if __name__ == "__main__":
    demonstrate_storage_system()
```

---

## 📊 Section 4: Report Generation System

A complete report generation system with abstract report generators for different formats.

**SOLID Principles Applied:**
- Dependency Inversion: ReportService depends on ReportGenerator abstraction
- Open/Closed: New report formats can be added

**Design Patterns:**
- Strategy Pattern: Different report formats as strategies
- Template Method Pattern: Base report generator defines structure

```python
"""
REPORT GENERATION SYSTEM

This section builds a report generation system using abstraction.

SOLID Principles Applied:
- Dependency Inversion: Depends on ReportGenerator abstraction
- Open/Closed: New report formats can be added

Design Patterns:
- Strategy Pattern: Different report formats as strategies
- Template Method Pattern: Base report generator defines structure
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum
import json
import csv
from io import StringIO


class ReportFormat(Enum):
    """Report format types."""
    JSON = "json"
    CSV = "csv"
    HTML = "html"
    MARKDOWN = "markdown"
    TEXT = "text"


class ReportData:
    """Report data container."""
    
    def __init__(self, title: str, data: List[Dict], 
                 generated_at: datetime = None):
        self.title = title
        self.data = data
        self.generated_at = generated_at or datetime.now()
        self.metadata: Dict[str, Any] = {}
    
    def add_metadata(self, key: str, value: Any) -> 'ReportData':
        self.metadata[key] = value
        return self
    
    def get_headers(self) -> List[str]:
        if not self.data:
            return []
        return list(self.data[0].keys())


class ReportGenerator(ABC):
    """
    Abstract base class for report generators.
    
    SOLID: Dependency Inversion - High-level modules depend on this abstraction
    Design Pattern: Template Method - Defines report generation skeleton
    """
    
    @abstractmethod
    def get_format_name(self) -> str:
        """Get report format name."""
        pass
    
    @abstractmethod
    def get_file_extension(self) -> str:
        """Get file extension."""
        pass
    
    @abstractmethod
    def _generate_header(self, report: ReportData) -> str:
        """Generate report header (implementation specific)."""
        pass
    
    @abstractmethod
    def _generate_body(self, report: ReportData) -> str:
        """Generate report body (implementation specific)."""
        pass
    
    @abstractmethod
    def _generate_footer(self, report: ReportData) -> str:
        """Generate report footer (implementation specific)."""
        pass
    
    def generate(self, report: ReportData) -> str:
        """Generate complete report (template method)."""
        parts = [
            self._generate_header(report),
            self._generate_body(report),
            self._generate_footer(report)
        ]
        return "\n".join(parts)


class JSONReportGenerator(ReportGenerator):
    """JSON format report generator."""
    
    def get_format_name(self) -> str:
        return "JSON"
    
    def get_file_extension(self) -> str:
        return "json"
    
    def _generate_header(self, report: ReportData) -> str:
        return "{"  # JSON start
    
    def _generate_body(self, report: ReportData) -> str:
        output = {
            "title": report.title,
            "generated_at": report.generated_at.isoformat(),
            "metadata": report.metadata,
            "data": report.data,
            "record_count": len(report.data)
        }
        return json.dumps(output, indent=2, default=str)[1:-1]  # Remove outer braces
    
    def _generate_footer(self, report: ReportData) -> str:
        return "}"


class CSVReportGenerator(ReportGenerator):
    """CSV format report generator."""
    
    def get_format_name(self) -> str:
        return "CSV"
    
    def get_file_extension(self) -> str:
        return "csv"
    
    def _generate_header(self, report: ReportData) -> str:
        # CSV header is just the column headers
        if not report.data:
            return ""
        
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=report.get_headers())
        writer.writeheader()
        return output.getvalue().strip()
    
    def _generate_body(self, report: ReportData) -> str:
        if not report.data:
            return ""
        
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=report.get_headers())
        writer.writerows(report.data)
        return output.getvalue().strip()
    
    def _generate_footer(self, report: ReportData) -> str:
        return ""  # CSV has no footer


class HTMLReportGenerator(ReportGenerator):
    """HTML format report generator."""
    
    def get_format_name(self) -> str:
        return "HTML"
    
    def get_file_extension(self) -> str:
        return "html"
    
    def _generate_header(self, report: ReportData) -> str:
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{report.title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        .footer {{ margin-top: 20px; font-size: 12px; color: #666; }}
    </style>
</head>
<body>
    <h1>{report.title}</h1>
    <p>Generated: {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p>Records: {len(report.data)}</p>
"""
    
    def _generate_body(self, report: ReportData) -> str:
        if not report.data:
            return "    <p>No data available</p>\n"
        
        headers = report.get_headers()
        html = '    <table>\n        <tr>\n'
        for header in headers:
            html += f'            <th>{header}</th>\n'
        html += '        </tr>\n'
        
        for row in report.data:
            html += '        <tr>\n'
            for header in headers:
                value = row.get(header, '')
                html += f'            <td>{value}</td>\n'
            html += '        </tr>\n'
        
        html += '    </table>\n'
        return html
    
    def _generate_footer(self, report: ReportData) -> str:
        return f"""
    <div class="footer">
        Report generated by Metromap Report System
    </div>
</body>
</html>"""


class MarkdownReportGenerator(ReportGenerator):
    """Markdown format report generator."""
    
    def get_format_name(self) -> str:
        return "Markdown"
    
    def get_file_extension(self) -> str:
        return "md"
    
    def _generate_header(self, report: ReportData) -> str:
        return f"# {report.title}\n\n**Generated:** {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n**Records:** {len(report.data)}\n"
    
    def _generate_body(self, report: ReportData) -> str:
        if not report.data:
            return "\n*No data available*\n"
        
        headers = report.get_headers()
        md = "\n| " + " | ".join(headers) + " |\n"
        md += "|" + "|".join([" --- " for _ in headers]) + "|\n"
        
        for row in report.data:
            values = [str(row.get(h, '')) for h in headers]
            md += "| " + " | ".join(values) + " |\n"
        
        return md
    
    def _generate_footer(self, report: ReportData) -> str:
        return "\n\n---\n*Report generated by Metromap Report System*"


class TextReportGenerator(ReportGenerator):
    """Plain text format report generator."""
    
    def get_format_name(self) -> str:
        return "Text"
    
    def get_file_extension(self) -> str:
        return "txt"
    
    def _generate_header(self, report: ReportData) -> str:
        separator = "=" * 60
        return f"{separator}\n{report.title.center(60)}\n{separator}\nGenerated: {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}\nRecords: {len(report.data)}\n{'-' * 60}"
    
    def _generate_body(self, report: ReportData) -> str:
        if not report.data:
            return "\nNo data available"
        
        headers = report.get_headers()
        
        # Calculate column widths
        widths = {}
        for header in headers:
            widths[header] = len(header)
        
        for row in report.data:
            for header in headers:
                value = str(row.get(header, ''))
                widths[header] = max(widths[header], len(value))
        
        # Build table
        lines = []
        # Header row
        header_line = " | ".join(h.ljust(widths[h]) for h in headers)
        lines.append(header_line)
        lines.append("-" * len(header_line))
        
        # Data rows
        for row in report.data:
            row_line = " | ".join(str(row.get(h, '')).ljust(widths[h]) for h in headers)
            lines.append(row_line)
        
        return "\n" + "\n".join(lines)
    
    def _generate_footer(self, report: ReportData) -> str:
        return f"\n{'-' * 60}\nEnd of Report"


class ReportService:
    """
    Report generation service using abstraction.
    
    Design Pattern: Strategy Pattern - Pluggable report generators
    """
    
    def __init__(self):
        self._generators: Dict[str, ReportGenerator] = {
            "json": JSONReportGenerator(),
            "csv": CSVReportGenerator(),
            "html": HTMLReportGenerator(),
            "md": MarkdownReportGenerator(),
            "txt": TextReportGenerator()
        }
        self._history: List[Dict] = []
    
    def register_generator(self, name: str, generator: ReportGenerator) -> None:
        """Register a custom report generator."""
        self._generators[name] = generator
    
    def generate_report(self, report: ReportData, format_type: str) -> str:
        """Generate report in specified format."""
        if format_type not in self._generators:
            raise ValueError(f"Unknown format: {format_type}")
        
        generator = self._generators[format_type]
        content = generator.generate(report)
        
        self._history.append({
            "title": report.title,
            "format": format_type,
            "record_count": len(report.data),
            "generated_at": datetime.now().isoformat()
        })
        
        return content
    
    def save_report(self, report: ReportData, format_type: str, 
                   filename: Optional[str] = None) -> str:
        """Generate and save report to file."""
        content = self.generate_report(report, format_type)
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ext = self._generators[format_type].get_file_extension()
            filename = f"report_{timestamp}.{ext}"
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"  Report saved to: {filename}")
        return filename
    
    def get_available_formats(self) -> List[str]:
        """Get list of available formats."""
        return list(self._generators.keys())
    
    def get_history(self) -> List[Dict]:
        """Get report generation history."""
        return self._history.copy()


def demonstrate_report_system():
    """
    Demonstrate the report generation system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: REPORT GENERATION SYSTEM")
    print("=" * 60)
    
    # Create sample data
    print("\n1. CREATING REPORT DATA")
    print("-" * 40)
    
    sales_data = [
        {"product": "Laptop", "quantity": 5, "price": 999.99, "total": 4999.95},
        {"product": "Mouse", "quantity": 15, "price": 29.99, "total": 449.85},
        {"product": "Keyboard", "quantity": 8, "price": 89.99, "total": 719.92},
        {"product": "Monitor", "quantity": 3, "price": 299.99, "total": 899.97},
        {"product": "USB Cable", "quantity": 25, "price": 9.99, "total": 249.75}
    ]
    
    report = ReportData("Sales Report", sales_data)
    report.add_metadata("department", "Electronics")
    report.add_metadata("report_type", "monthly")
    
    print(f"  Title: {report.title}")
    print(f"  Records: {len(report.data)}")
    print(f"  Headers: {report.get_headers()}")
    
    service = ReportService()
    
    print("\n2. GENERATING DIFFERENT FORMATS")
    print("-" * 40)
    
    for fmt in service.get_available_formats():
        print(f"\n  {fmt.upper()} FORMAT:")
        content = service.generate_report(report, fmt)
        # Show first 200 characters
        preview = content[:200].replace('\n', ' ')
        print(f"    {preview}...")
    
    print("\n3. SAVING REPORTS TO FILES")
    print("-" * 40)
    
    service.save_report(report, "json", "sales_report.json")
    service.save_report(report, "csv", "sales_report.csv")
    service.save_report(report, "html", "sales_report.html")
    service.save_report(report, "md", "sales_report.md")
    service.save_report(report, "txt", "sales_report.txt")
    
    print("\n4. REPORT HISTORY")
    print("-" * 40)
    
    history = service.get_history()
    for entry in history:
        print(f"  {entry['generated_at'][:19]} - {entry['title']} ({entry['format']}) - {entry['record_count']} records")
    
    print("\n5. CUSTOM REPORT GENERATOR")
    print("-" * 40)
    
    class XMLReportGenerator(ReportGenerator):
        """Custom XML report generator."""
        
        def get_format_name(self) -> str:
            return "XML"
        
        def get_file_extension(self) -> str:
            return "xml"
        
        def _generate_header(self, report: ReportData) -> str:
            return f'<?xml version="1.0" encoding="UTF-8"?>\n<report title="{report.title}">'
        
        def _generate_body(self, report: ReportData) -> str:
            xml = f'\n    <generated_at>{report.generated_at.isoformat()}</generated_at>\n    <records>{len(report.data)}</records>\n    <data>'
            for row in report.data:
                xml += '\n        <record>'
                for key, value in row.items():
                    xml += f'\n            <{key}>{value}</{key}>'
                xml += '\n        </record>'
            xml += '\n    </data>'
            return xml
        
        def _generate_footer(self, report: ReportData) -> str:
            return '\n</report>'
    
    service.register_generator("xml", XMLReportGenerator())
    xml_content = service.generate_report(report, "xml")
    print(f"  XML Report length: {len(xml_content)} characters")
    print(f"  Preview: {xml_content[:150]}...")
    
    print("\n6. ABSTRACTION BENEFITS")
    print("-" * 40)
    
    print("""
    Benefits demonstrated:
    ✓ ReportService works with any ReportGenerator
    ✓ Adding new format (XML) didn't change existing code
    ✓ Complex report formatting hidden behind generate() interface
    ✓ Consistent interface across all formats
    ✓ Template method pattern ensures consistent report structure
    """)


if __name__ == "__main__":
    demonstrate_report_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Abstraction Basics** – Hide implementation details, expose only essential features. Use ABCs and abstract methods.

- **Abstract Base Classes (ABC)** – Cannot be instantiated. Define interfaces that subclasses must implement.

- **Abstract Methods** – `@abstractmethod` decorator. No implementation in base class. Subclasses must implement.

- **Template Method Pattern** – Base class defines algorithm skeleton. Subclasses implement specific steps.

- **Virtual Subclasses** – `register()` method allows classes to be recognized as subclasses without inheritance.

- **Dependency Inversion Principle** – High-level modules should depend on abstractions, not concrete implementations.

- **Email Service** – Abstract EmailProvider with SMTP, SendGrid, Mock implementations. Service works with any provider.

- **Storage System** – Abstract StorageBackend with File, Dict, SQLite implementations. Caching layer.

- **Report Generation** – Abstract ReportGenerator with JSON, CSV, HTML, Markdown, Text implementations. Template method pattern.

- **SOLID Principles Applied** – Dependency Inversion (depend on abstractions), Open/Closed (new providers/formats added), Liskov Substitution (all providers substitutable), Interface Segregation (clean interfaces), Single Responsibility (each generator handles one format).

- **Design Patterns Used** – Template Method Pattern (report generation skeleton), Strategy Pattern (pluggable providers/backends/generators), Adapter Pattern (adapts different APIs), Builder Pattern (email construction), Factory Pattern (creating providers).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Encapsulation – Protecting Data

- **📚 Series D Catalog:** Object-Oriented Programming Line – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: File I/O – Reading & Writing (Series E, Story 1)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **29** | **23** | **56%** |

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

**Next Story:** Series E, Story 1: The 2026 Python Metromap: File I/O – Reading & Writing

---

## 📝 Your Invitation

**Congratulations! You've completed the Object-Oriented Programming Line!**

You've mastered:
- Classes and Objects (blueprints and instances)
- Constructors (building objects with initial state)
- Inheritance (reusing parent classes)
- Polymorphism (one interface, many forms)
- Encapsulation (protecting data)
- Abstraction (hiding complexity)

Now build something with what you've learned:

1. **Build a plugin system** – Create an abstract Plugin class with register and execute methods.

2. **Create a data export system** – Abstract Exporter class with CSV, JSON, Excel, PDF implementations.

3. **Build a authentication system** – Abstract AuthProvider with OAuth, JWT, API Key implementations.

4. **Create a message queue system** – Abstract Queue with Redis, RabbitMQ, SQS implementations.

5. **Build a caching system** – Abstract Cache with Redis, Memcached, in-memory implementations.

**You've mastered Object-Oriented Programming. Next stop: File & Data Handling Line – File I/O!**

---

*Found this helpful? Clap, comment, and share what you built with abstraction. Next stop: File I/O!* 🚇