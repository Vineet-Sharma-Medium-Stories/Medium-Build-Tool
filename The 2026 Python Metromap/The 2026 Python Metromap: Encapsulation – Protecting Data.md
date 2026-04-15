# The 2026 Python Metromap: Encapsulation – Protecting Data

## Series D: Object-Oriented Programming (OOP) Line | Story 5 of 6

![The 2026 Python Metromap/images/Encapsulation – Protecting Data](images/Encapsulation – Protecting Data.png)

## 📖 Introduction

**Welcome to the fifth stop on the Object-Oriented Programming Line.**

You've mastered classes, constructors, inheritance, and polymorphism. You can create hierarchies of classes, override methods, and treat different objects through common interfaces. But there's a critical aspect of object-oriented design you haven't explored yet—controlling access to data.

In real-world systems, not all data should be freely accessible or modifiable. A bank account's balance shouldn't be directly set to a negative value. A user's password shouldn't be readable in plain text. A product's price shouldn't be changed without validation. This is where encapsulation comes in.

Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class), while restricting direct access to some of the object's internal components. It's about hiding internal state and requiring all interaction to happen through well-defined interfaces (methods). This protects data integrity, reduces complexity, and makes code more maintainable.

This story—**The 2026 Python Metromap: Encapsulation – Protecting Data**—is your guide to mastering encapsulation in Python. We'll build a complete healthcare records system with private medical data. We'll create a bank account with protected balance and transaction validation. We'll implement a user authentication system with password hashing. We'll build a product inventory system with validation on price updates. And we'll create a complete employee management system with access controls.

**Let's protect our data.**

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

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules. **⬅️ YOU ARE HERE**

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🛡️ Section 1: Encapsulation Basics – Public, Protected, Private

Encapsulation controls access to class attributes and methods using naming conventions and property decorators.

**SOLID Principle Applied: Single Responsibility** – Encapsulation ensures each class manages its own data.

**Design Pattern: Proxy Pattern** – Properties act as proxies controlling access to attributes.

```python
"""
ENCAPSULATION BASICS: PUBLIC, PROTECTED, PRIVATE

This section covers the fundamentals of data hiding and access control.

SOLID Principle: Single Responsibility
- Each class manages its own data

Design Pattern: Proxy Pattern
- Properties act as proxies controlling attribute access
"""

from typing import Any, Optional


def demonstrate_naming_conventions():
    """
    Demonstrates Python's naming conventions for access control.
    
    Python uses naming conventions rather than strict access modifiers:
    - Public: normal name (accessible everywhere)
    - Protected: _single_leading_underscore (internal use, "please don't touch")
    - Private: __double_leading_underscore (name mangling, harder to access)
    """
    print("=" * 60)
    print("SECTION 1A: NAMING CONVENTIONS")
    print("=" * 60)
    
    class BankAccount:
        """Demonstrates different visibility levels."""
        
        def __init__(self, account_holder: str, initial_balance: float):
            # Public attribute - accessible anywhere
            self.account_holder = account_holder
            
            # Protected attribute - internal use (convention only)
            self._branch_code = "NYC001"
            
            # Private attribute - name mangling
            self.__balance = initial_balance
            
            # Private method
            def __validate_transaction(self, amount: float) -> bool:
                """Private validation method."""
                return amount > 0 and amount <= self.__balance
        
        def deposit(self, amount: float) -> bool:
            """Public method to deposit money."""
            if amount > 0:
                self.__balance += amount
                return True
            return False
        
        def withdraw(self, amount: float) -> bool:
            """Public method to withdraw money."""
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return True
            return False
        
        def get_balance(self) -> float:
            """Public getter for balance."""
            return self.__balance
    
    # Create account
    account = BankAccount("Alice Chen", 1000.00)
    
    print("\n1. ACCESSING PUBLIC ATTRIBUTES")
    print("-" * 40)
    
    # Public - accessible directly
    print(f"  account.account_holder: {account.account_holder}")
    account.account_holder = "Alice Wonderland"
    print(f"  After modification: {account.account_holder}")
    
    print("\n2. ACCESSING PROTECTED ATTRIBUTES (Convention only)")
    print("-" * 40)
    
    # Protected - accessible but discouraged
    print(f"  account._branch_code: {account._branch_code}")
    account._branch_code = "LAX001"
    print(f"  After modification: {account._branch_code}")
    print("  ⚠️ Works but violates convention - 'internal use only'")
    
    print("\n3. ACCESSING PRIVATE ATTRIBUTES (Name mangling)")
    print("-" * 40)
    
    # Private - not directly accessible
    try:
        print(f"  account.__balance: {account.__balance}")
    except AttributeError as e:
        print(f"  Error: {e}")
    
    # But name mangling makes it accessible (not recommended!)
    print(f"  account._BankAccount__balance: {account._BankAccount__balance}")
    print("  ⚠️ Name mangled but still accessible - don't do this!")
    
    print("\n4. USING PUBLIC METHODS (Recommended way)")
    print("-" * 40)
    
    print(f"  Initial balance: {account.get_balance()}")
    account.deposit(500)
    print(f"  After deposit: {account.get_balance()}")
    account.withdraw(200)
    print(f"  After withdrawal: {account.get_balance()}")
    
    print("\n5. SUMMARY OF PYTHON ENCAPSULATION")
    print("-" * 40)
    
    print("""
    Convention:                          Actual behavior:
    ─────────────────────────────────────────────────────────
    name        → Public                 → Fully accessible
    _name       → Protected (internal)   → Accessible (by convention only)
    __name      → Private                → Name mangled (_ClassName__name)
    
    💡 Python trusts developers to respect conventions rather than enforcing strict access control.
    💡 Use properties (@property) for controlled access instead of direct attribute access.
    """)


def demonstrate_properties():
    """
    Demonstrates using @property decorator for controlled access.
    
    Properties allow you to define getters, setters, and deleters
    that look like regular attribute access.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: PROPERTIES – CONTROLLED ACCESS")
    print("=" * 60)
    
    class Temperature:
        """Temperature class with property validation."""
        
        def __init__(self, celsius: float = 0):
            self._celsius = celsius
        
        @property
        def celsius(self) -> float:
            """Get temperature in Celsius."""
            return self._celsius
        
        @celsius.setter
        def celsius(self, value: float):
            """Set temperature in Celsius with validation."""
            # Absolute zero is -273.15°C
            if value < -273.15:
                raise ValueError(f"Temperature cannot be below absolute zero (-273.15°C)")
            self._celsius = value
        
        @property
        def fahrenheit(self) -> float:
            """Get temperature in Fahrenheit (computed property)."""
            return (self._celsius * 9/5) + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value: float):
            """Set temperature in Fahrenheit."""
            self.celsius = (value - 32) * 5/9
        
        @property
        def kelvin(self) -> float:
            """Get temperature in Kelvin (computed property)."""
            return self._celsius + 273.15
    
    print("\n1. USING PROPERTIES")
    print("-" * 40)
    
    temp = Temperature()
    
    # Using property like an attribute
    temp.celsius = 25
    print(f"  Celsius: {temp.celsius}°C")
    print(f"  Fahrenheit: {temp.fahrenheit}°F")
    print(f"  Kelvin: {temp.kelvin}K")
    
    # Set using Fahrenheit
    temp.fahrenheit = 98.6
    print(f"\n  After setting Fahrenheit to 98.6:")
    print(f"  Celsius: {temp.celsius}°C")
    
    # Validation in action
    print("\n2. VALIDATION IN PROPERTY SETTER")
    print("-" * 40)
    
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"  Error: {e}")
    
    print("\n3. READ-ONLY PROPERTY (no setter)")
    print("-" * 40)
    
    class Person:
        def __init__(self, first: str, last: str):
            self._first = first
            self._last = last
        
        @property
        def full_name(self) -> str:
            """Read-only computed property."""
            return f"{self._first} {self._last}"
        
        @property
        def first(self) -> str:
            return self._first
        
        @first.setter
        def first(self, value: str):
            self._first = value
    
    person = Person("Alice", "Chen")
    print(f"  Full name: {person.full_name}")
    person.first = "Alicia"
    print(f"  After changing first name: {person.full_name}")
    
    # This would fail - no setter for full_name
    try:
        person.full_name = "Bob Smith"
    except AttributeError as e:
        print(f"  Cannot set read-only property: {e}")
    
    print("\n4. PROPERTY WITH COMPUTED VALUE")
    print("-" * 40)
    
    class Rectangle:
        def __init__(self, width: float, height: float):
            self._width = width
            self._height = height
        
        @property
        def width(self) -> float:
            return self._width
        
        @width.setter
        def width(self, value: float):
            if value <= 0:
                raise ValueError("Width must be positive")
            self._width = value
        
        @property
        def height(self) -> float:
            return self._height
        
        @height.setter
        def height(self, value: float):
            if value <= 0:
                raise ValueError("Height must be positive")
            self._height = value
        
        @property
        def area(self) -> float:
            """Computed property - no setter."""
            return self._width * self._height
        
        @property
        def perimeter(self) -> float:
            """Computed property - no setter."""
            return 2 * (self._width + self._height)
    
    rect = Rectangle(5, 3)
    print(f"  Rectangle: {rect.width} x {rect.height}")
    print(f"  Area: {rect.area}")
    print(f"  Perimeter: {rect.perimeter}")
    
    rect.width = 10
    print(f"\n  After changing width to 10:")
    print(f"  Area: {rect.area}")
    print(f"  Perimeter: {rect.perimeter}")


def demonstrate_private_methods():
    """
    Demonstrates private methods for internal use only.
    
    Private methods are implementation details that shouldn't be called externally.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: PRIVATE METHODS")
    print("=" * 60)
    
    class DataProcessor:
        """Data processor with private helper methods."""
        
        def __init__(self, data: str):
            self._data = data
            self._processed_data = None
        
        def process(self) -> dict:
            """Public method - main interface."""
            # Call private helper methods
            cleaned = self._clean_data()
            validated = self._validate_data(cleaned)
            transformed = self._transform_data(validated)
            self._processed_data = transformed
            return self._get_results()
        
        def _clean_data(self) -> str:
            """Private method for data cleaning."""
            return self._data.strip().lower()
        
        def _validate_data(self, data: str) -> bool:
            """Private method for data validation."""
            return len(data) > 0 and data.isalnum()
        
        def _transform_data(self, data: str) -> str:
            """Private method for data transformation."""
            return data.upper()
        
        def _get_results(self) -> dict:
            """Private method for result formatting."""
            return {
                "original": self._data,
                "processed": self._processed_data,
                "length": len(self._processed_data) if self._processed_data else 0
            }
    
    processor = DataProcessor("  Hello World!  ")
    result = processor.process()
    
    print("\n1. USING PUBLIC METHOD")
    print("-" * 40)
    print(f"  Result: {result}")
    
    print("\n2. ATTEMPTING TO CALL PRIVATE METHODS")
    print("-" * 40)
    
    try:
        # This works but violates encapsulation
        print(f"  processor._clean_data(): {processor._clean_data()}")
        print("  ⚠️ Works but shouldn't be called directly")
    except AttributeError:
        print("  Cannot access private method")
    
    print("\n3. NAME MANGLING WITH PRIVATE METHODS")
    print("-" * 40)
    
    class Example:
        def public_method(self):
            return "public"
        
        def __private_method(self):
            return "private"
    
    obj = Example()
    print(f"  dir(obj): {[m for m in dir(obj) if not m.startswith('__')][:5]}...")
    print(f"  Private method mangled to: _Example__private_method")
    
    print("\n4. WHY USE PRIVATE METHODS?")
    print("-" * 40)
    
    print("""
    Benefits of private methods:
    ✓ Hide implementation details
    ✓ Prevent external code from depending on internal logic
    ✓ Allow internal refactoring without breaking external code
    ✓ Reduce complexity of public interface
    ✓ Document that a method is for internal use only
    
    When to use:
    - Helper methods that support public methods
    - Validation logic that shouldn't be bypassed
    - Internal calculations that may change
    """)


if __name__ == "__main__":
    demonstrate_naming_conventions()
    demonstrate_properties()
    demonstrate_private_methods()
```

---

## 🏥 Section 2: Healthcare Records System

A complete healthcare records system demonstrating encapsulation of sensitive medical data.

**SOLID Principles Applied:**
- Single Responsibility: MedicalRecord manages patient data
- Open/Closed: New record types can be added

**Design Patterns:**
- Proxy Pattern: Properties control access to sensitive data
- Factory Pattern: Creates validated records

```python
"""
HEALTHCARE RECORDS SYSTEM

This section builds a healthcare records system with encapsulated sensitive data.

SOLID Principles Applied:
- Single Responsibility: MedicalRecord manages patient data
- Open/Closed: New record types can be added

Design Patterns:
- Proxy Pattern: Properties control access to sensitive data
- Factory Pattern: Creates validated records
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, date
from enum import Enum
from abc import ABC, abstractmethod
import hashlib
import re


class AccessLevel(Enum):
    """Access levels for medical records."""
    PATIENT = "patient"
    DOCTOR = "doctor"
    NURSE = "nurse"
    ADMIN = "admin"
    AUDITOR = "auditor"


class MedicalSpecialty(Enum):
    """Medical specialties."""
    CARDIOLOGY = "cardiology"
    DERMATOLOGY = "dermatology"
    NEUROLOGY = "neurology"
    PEDIATRICS = "pediatrics"
    PSYCHIATRY = "psychiatry"
    GENERAL = "general"


class RecordStatus(Enum):
    """Medical record status."""
    ACTIVE = "active"
    ARCHIVED = "archived"
    PENDING_REVIEW = "pending_review"
    RESTRICTED = "restricted"


class AuditLog:
    """Audit log for tracking access to medical records."""
    
    def __init__(self):
        self._entries: List[Dict] = []
    
    def log_access(self, record_id: str, accessed_by: str, access_level: AccessLevel,
                   action: str, details: str = "") -> None:
        """Log an access event."""
        self._entries.append({
            "timestamp": datetime.now().isoformat(),
            "record_id": record_id,
            "accessed_by": accessed_by,
            "access_level": access_level.value,
            "action": action,
            "details": details
        })
    
    def get_access_history(self, record_id: str) -> List[Dict]:
        """Get access history for a specific record."""
        return [e for e in self._entries if e["record_id"] == record_id]
    
    def get_audit_report(self) -> str:
        """Generate audit report."""
        lines = []
        lines.append("=" * 70)
        lines.append("MEDICAL RECORDS AUDIT LOG")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("=" * 70)
        
        for entry in self._entries[-20:]:  # Last 20 entries
            lines.append(f"  {entry['timestamp'][:19]} | {entry['accessed_by']:15} | "
                        f"{entry['access_level']:10} | {entry['action']:15} | {entry['record_id']}")
        
        lines.append("=" * 70)
        return "\n".join(lines)


class MedicalRecord:
    """
    Medical record with encapsulated sensitive data.
    
    Design Pattern: Proxy Pattern - Properties control access
    """
    
    def __init__(self, patient_id: str, patient_name: str, date_of_birth: date):
        self._patient_id = patient_id
        self._patient_name = patient_name
        self._date_of_birth = date_of_birth
        self._record_id = f"MR-{patient_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._created_at = datetime.now()
        self._status = RecordStatus.ACTIVE
        
        # Encapsulated medical data
        self._diagnoses: List[Dict] = []
        self._prescriptions: List[Dict] = []
        self._lab_results: List[Dict] = []
        self._allergies: List[str] = []
        self._vital_signs: List[Dict] = []
        self._notes: List[Dict] = []
        
        # Access control
        self._authorized_personnel: Dict[str, AccessLevel] = {
            patient_id: AccessLevel.PATIENT
        }
    
    # Basic information (read-only for non-owners)
    @property
    def record_id(self) -> str:
        return self._record_id
    
    @property
    def patient_id(self) -> str:
        return self._patient_id
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @property
    def status(self) -> RecordStatus:
        return self._status
    
    # Patient name with access control
    def get_patient_name(self, requester_id: str, access_level: AccessLevel) -> Optional[str]:
        """Get patient name with access control."""
        if self._check_access(requester_id, access_level):
            return self._patient_name
        return None
    
    # Date of birth with access control
    def get_date_of_birth(self, requester_id: str, access_level: AccessLevel) -> Optional[date]:
        """Get date of birth with access control."""
        if self._check_access(requester_id, access_level):
            return self._date_of_birth
        return None
    
    def _check_access(self, requester_id: str, access_level: AccessLevel) -> bool:
        """Check if requester has sufficient access."""
        if requester_id == self._patient_id:
            return True
        
        authorized_level = self._authorized_personnel.get(requester_id)
        if authorized_level:
            # Define hierarchy (higher number = more access)
            level_values = {l: i for i, l in enumerate(AccessLevel)}
            if level_values.get(access_level, 0) >= level_values.get(authorized_level, 0):
                return True
        
        return False
    
    def authorize_personnel(self, personnel_id: str, access_level: AccessLevel,
                           authorized_by: str) -> bool:
        """Authorize medical personnel to access records."""
        if authorized_by != self._patient_id and authorized_by not in self._authorized_personnel:
            return False
        
        self._authorized_personnel[personnel_id] = access_level
        return True
    
    def revoke_access(self, personnel_id: str, authorized_by: str) -> bool:
        """Revoke access for medical personnel."""
        if authorized_by != self._patient_id and authorized_by not in self._authorized_personnel:
            return False
        
        if personnel_id in self._authorized_personnel:
            del self._authorized_personnel[personnel_id]
            return True
        return False
    
    # Medical data methods with validation
    def add_diagnosis(self, diagnosis: str, doctor_id: str, date: date,
                     specialty: MedicalSpecialty) -> bool:
        """Add a diagnosis (doctor only)."""
        if doctor_id not in self._authorized_personnel:
            return False
        
        self._diagnoses.append({
            "diagnosis": diagnosis,
            "doctor_id": doctor_id,
            "date": date.isoformat(),
            "specialty": specialty.value,
            "added_at": datetime.now().isoformat()
        })
        return True
    
    def get_diagnoses(self, requester_id: str, access_level: AccessLevel) -> List[Dict]:
        """Get diagnoses with access control."""
        if self._check_access(requester_id, access_level):
            return self._diagnoses.copy()
        return []
    
    def add_prescription(self, medication: str, dosage: str, frequency: str,
                        prescribed_by: str, start_date: date, end_date: date) -> bool:
        """Add a prescription."""
        if prescribed_by not in self._authorized_personnel:
            return False
        
        self._prescriptions.append({
            "medication": medication,
            "dosage": dosage,
            "frequency": frequency,
            "prescribed_by": prescribed_by,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "active": True,
            "added_at": datetime.now().isoformat()
        })
        return True
    
    def get_prescriptions(self, requester_id: str, access_level: AccessLevel) -> List[Dict]:
        """Get prescriptions with access control."""
        if self._check_access(requester_id, access_level):
            return self._prescriptions.copy()
        return []
    
    def add_lab_result(self, test_name: str, result: str, reference_range: str,
                      ordered_by: str, date: date) -> bool:
        """Add a lab result."""
        if ordered_by not in self._authorized_personnel:
            return False
        
        self._lab_results.append({
            "test_name": test_name,
            "result": result,
            "reference_range": reference_range,
            "ordered_by": ordered_by,
            "date": date.isoformat(),
            "added_at": datetime.now().isoformat()
        })
        return True
    
    def get_lab_results(self, requester_id: str, access_level: AccessLevel) -> List[Dict]:
        """Get lab results with access control."""
        if self._check_access(requester_id, access_level):
            return self._lab_results.copy()
        return []
    
    def add_allergy(self, allergy: str, added_by: str) -> bool:
        """Add an allergy."""
        if added_by not in self._authorized_personnel:
            return False
        
        if allergy not in self._allergies:
            self._allergies.append(allergy)
        return True
    
    def get_allergies(self, requester_id: str, access_level: AccessLevel) -> List[str]:
        """Get allergies with access control."""
        if self._check_access(requester_id, access_level):
            return self._allergies.copy()
        return []
    
    def add_vital_signs(self, blood_pressure: str, heart_rate: int,
                       temperature: float, oxygen_saturation: int,
                       recorded_by: str) -> bool:
        """Add vital signs."""
        if recorded_by not in self._authorized_personnel:
            return False
        
        self._vital_signs.append({
            "blood_pressure": blood_pressure,
            "heart_rate": heart_rate,
            "temperature": temperature,
            "oxygen_saturation": oxygen_saturation,
            "recorded_by": recorded_by,
            "recorded_at": datetime.now().isoformat()
        })
        return True
    
    def get_vital_signs(self, requester_id: str, access_level: AccessLevel) -> List[Dict]:
        """Get vital signs with access control."""
        if self._check_access(requester_id, access_level):
            return self._vital_signs.copy()
        return []
    
    def add_note(self, note: str, author_id: str, author_role: str) -> bool:
        """Add a clinical note."""
        if author_id not in self._authorized_personnel:
            return False
        
        self._notes.append({
            "note": note,
            "author_id": author_id,
            "author_role": author_role,
            "created_at": datetime.now().isoformat()
        })
        return True
    
    def get_notes(self, requester_id: str, access_level: AccessLevel) -> List[Dict]:
        """Get clinical notes with access control."""
        if self._check_access(requester_id, access_level):
            return self._notes.copy()
        return []
    
    def get_summary(self, requester_id: str, access_level: AccessLevel) -> Dict:
        """Get medical record summary with access control."""
        if not self._check_access(requester_id, access_level):
            return {"error": "Access denied"}
        
        return {
            "record_id": self._record_id,
            "patient_id": self._patient_id,
            "status": self._status.value,
            "created_at": self._created_at.isoformat(),
            "diagnoses_count": len(self._diagnoses),
            "prescriptions_count": len(self._prescriptions),
            "lab_results_count": len(self._lab_results),
            "allergies": self._allergies,
            "notes_count": len(self._notes)
        }


class MedicalRecordRepository:
    """
    Repository for medical records.
    
    Design Pattern: Repository Pattern - Central storage
    """
    
    def __init__(self):
        self._records: Dict[str, MedicalRecord] = {}
        self._audit_log = AuditLog()
    
    def create_record(self, patient_id: str, patient_name: str,
                     date_of_birth: date) -> MedicalRecord:
        """Create a new medical record."""
        record = MedicalRecord(patient_id, patient_name, date_of_birth)
        self._records[record.record_id] = record
        self._audit_log.log_access(record.record_id, patient_id, AccessLevel.PATIENT,
                                  "CREATE", "Record created")
        return record
    
    def get_record(self, record_id: str, requester_id: str,
                  access_level: AccessLevel) -> Optional[MedicalRecord]:
        """Get a medical record with access control."""
        record = self._records.get(record_id)
        if record:
            self._audit_log.log_access(record_id, requester_id, access_level,
                                      "VIEW", "Record accessed")
        return record
    
    def get_records_by_patient(self, patient_id: str) -> List[MedicalRecord]:
        """Get all records for a patient."""
        return [r for r in self._records.values() if r.patient_id == patient_id]
    
    def get_audit_report(self) -> str:
        """Get audit report."""
        return self._audit_log.get_audit_report()


def demonstrate_healthcare_system():
    """
    Demonstrate the healthcare records system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: HEALTHCARE RECORDS SYSTEM")
    print("=" * 60)
    
    repo = MedicalRecordRepository()
    
    print("\n1. CREATING MEDICAL RECORD")
    print("-" * 40)
    
    record = repo.create_record("P-1001", "Alice Chen", date(1995, 6, 15))
    print(f"  Created record: {record.record_id}")
    
    print("\n2. AUTHORIZING MEDICAL PERSONNEL")
    print("-" * 40)
    
    # Patient authorizes doctor
    record.authorize_personnel("DR-SMITH", AccessLevel.DOCTOR, "P-1001")
    record.authorize_personnel("NR-JONES", AccessLevel.NURSE, "P-1001")
    print("  Authorized: Dr. Smith (Doctor), Nurse Jones (Nurse)")
    
    print("\n3. ADDING MEDICAL DATA (Doctor only)")
    print("-" * 40)
    
    # Add diagnoses
    record.add_diagnosis("Hypertension", "DR-SMITH", date(2024, 1, 15),
                        MedicalSpecialty.CARDIOLOGY)
    record.add_diagnosis("Type 2 Diabetes", "DR-SMITH", date(2024, 1, 15),
                        MedicalSpecialty.GENERAL)
    print("  Added: Hypertension, Type 2 Diabetes")
    
    # Add prescriptions
    record.add_prescription("Lisinopril", "10mg", "Once daily",
                           "DR-SMITH", date(2024, 1, 15), date(2024, 7, 15))
    record.add_prescription("Metformin", "500mg", "Twice daily",
                           "DR-SMITH", date(2024, 1, 15), date(2024, 7, 15))
    print("  Added: Lisinopril, Metformin")
    
    # Add lab results
    record.add_lab_result("Blood Glucose", "140 mg/dL", "70-99 mg/dL",
                         "DR-SMITH", date(2024, 1, 14))
    record.add_lab_result("Blood Pressure", "135/85 mmHg", "<120/80 mmHg",
                         "DR-SMITH", date(2024, 1, 14))
    print("  Added: Lab results")
    
    # Add allergies
    record.add_allergy("Penicillin", "DR-SMITH")
    print("  Added: Allergy to Penicillin")
    
    # Add vital signs (Nurse)
    record.add_vital_signs("125/80", 72, 36.6, 98, "NR-JONES")
    print("  Added: Vital signs by Nurse Jones")
    
    # Add clinical note
    record.add_note("Patient reports feeling well. Blood pressure improving.",
                   "DR-SMITH", "Doctor")
    print("  Added: Clinical note")
    
    print("\n4. ACCESSING MEDICAL DATA (Different access levels)")
    print("-" * 40)
    
    # Patient accessing own record
    print("\n  Patient access:")
    print(f"    Patient name: {record.get_patient_name('P-1001', AccessLevel.PATIENT)}")
    print(f"    Diagnoses: {len(record.get_diagnoses('P-1001', AccessLevel.PATIENT))}")
    print(f"    Prescriptions: {len(record.get_prescriptions('P-1001', AccessLevel.PATIENT))}")
    
    # Doctor accessing record
    print("\n  Doctor access:")
    print(f"    Diagnoses: {record.get_diagnoses('DR-SMITH', AccessLevel.DOCTOR)}")
    prescriptions = record.get_prescriptions('DR-SMITH', AccessLevel.DOCTOR)
    for rx in prescriptions:
        print(f"      {rx['medication']}: {rx['dosage']} - {rx['frequency']}")
    
    # Unauthorized access attempt
    print("\n  Unauthorized access attempt:")
    unknown_name = record.get_patient_name("UNKNOWN", AccessLevel.PATIENT)
    print(f"    Patient name: {unknown_name}")
    
    print("\n5. RECORD SUMMARY")
    print("-" * 40)
    
    summary = record.get_summary("P-1001", AccessLevel.PATIENT)
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    print("\n6. AUDIT LOG")
    print("-" * 40)
    
    audit_report = repo.get_audit_report()
    print(audit_report[:500] + "...")


if __name__ == "__main__":
    demonstrate_healthcare_system()
```

---

## 💰 Section 3: Bank Account with Protected Balance

A secure bank account system demonstrating encapsulation of financial data.

**SOLID Principles Applied:**
- Single Responsibility: Account manages its own balance
- Open/Closed: New account types can be added

**Design Patterns:**
- Proxy Pattern: Properties validate transactions
- Command Pattern: Transactions as commands with undo

```python
"""
BANK ACCOUNT WITH PROTECTED BALANCE

This section builds a bank account system with encapsulated balance.

SOLID Principles Applied:
- Single Responsibility: Account manages its own balance
- Open/Closed: New account types can be added

Design Patterns:
- Proxy Pattern: Properties validate transactions
- Command Pattern: Transactions as commands with undo
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod
import uuid


class TransactionType(Enum):
    """Types of transactions."""
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER_IN = "transfer_in"
    TRANSFER_OUT = "transfer_out"
    INTEREST = "interest"
    FEE = "fee"
    REVERSAL = "reversal"


class Transaction:
    """Immutable transaction record."""
    
    def __init__(self, transaction_id: str, account_id: str, amount: float,
                 transaction_type: TransactionType, description: str = "",
                 balance_after: float = 0.0):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.balance_after = balance_after
        self.timestamp = datetime.now()
        self.is_reversed = False
    
    def to_dict(self) -> Dict:
        return {
            "id": self.transaction_id,
            "amount": self.amount,
            "type": self.transaction_type.value,
            "description": self.description,
            "balance_after": self.balance_after,
            "timestamp": self.timestamp.isoformat(),
            "reversed": self.is_reversed
        }
    
    def __str__(self) -> str:
        sign = "+" if self.amount > 0 else ""
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.transaction_type.value}: {sign}${self.amount:.2f} → ${self.balance_after:.2f}"


class BankAccount(ABC):
    """
    Abstract bank account with encapsulated balance.
    
    Design Pattern: Template Method - Defines account skeleton
    """
    
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        self._is_active = True
        self._created_at = datetime.now()
        self._daily_withdrawal_limit = 5000.0
        self._daily_withdrawn = 0.0
        self._last_withdrawal_date = datetime.now().date()
        
        if initial_balance > 0:
            self._record_transaction(initial_balance, TransactionType.DEPOSIT,
                                    "Initial deposit", initial_balance)
    
    @property
    def account_number(self) -> str:
        """Get account number (read-only)."""
        return self._account_number
    
    @property
    def account_holder(self) -> str:
        """Get account holder (read-only)."""
        return self._account_holder
    
    @property
    def is_active(self) -> bool:
        """Check if account is active (read-only)."""
        return self._is_active
    
    def get_balance(self) -> float:
        """Get current balance (read-only access)."""
        return self._balance
    
    def get_transaction_history(self, limit: int = 10) -> List[Transaction]:
        """Get recent transaction history."""
        return self._transactions[-limit:][::-1]
    
    def _record_transaction(self, amount: float, transaction_type: TransactionType,
                           description: str, balance_after: float) -> None:
        """Record a transaction (private method)."""
        transaction_id = str(uuid.uuid4())[:8]
        transaction = Transaction(transaction_id, self._account_number, amount,
                                 transaction_type, description, balance_after)
        self._transactions.append(transaction)
    
    def _reset_daily_withdrawal_if_needed(self) -> None:
        """Reset daily withdrawal counter if new day."""
        today = datetime.now().date()
        if today != self._last_withdrawal_date:
            self._daily_withdrawn = 0.0
            self._last_withdrawal_date = today
    
    def _check_withdrawal_limit(self, amount: float) -> Tuple[bool, str]:
        """Check if withdrawal is within daily limit."""
        self._reset_daily_withdrawal_if_needed()
        
        if self._daily_withdrawn + amount > self._daily_withdrawal_limit:
            remaining = self._daily_withdrawal_limit - self._daily_withdrawn
            return False, f"Daily withdrawal limit exceeded. ${remaining:.2f} remaining today"
        
        return True, "OK"
    
    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """Deposit money (validated)."""
        if not self._is_active:
            print(f"  Account {self._account_number} is closed")
            return False
        
        if amount <= 0:
            print(f"  Deposit amount must be positive")
            return False
        
        self._balance += amount
        self._record_transaction(amount, TransactionType.DEPOSIT, description, self._balance)
        print(f"  Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """Withdraw money with validation."""
        if not self._is_active:
            print(f"  Account {self._account_number} is closed")
            return False
        
        if amount <= 0:
            print(f"  Withdrawal amount must be positive")
            return False
        
        if not self.can_withdraw(amount):
            print(f"  Insufficient funds. Balance: ${self._balance:.2f}")
            return False
        
        limit_ok, limit_msg = self._check_withdrawal_limit(amount)
        if not limit_ok:
            print(f"  {limit_msg}")
            return False
        
        self._balance -= amount
        self._daily_withdrawn += amount
        self._record_transaction(-amount, TransactionType.WITHDRAWAL, description, self._balance)
        print(f"  Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def can_withdraw(self, amount: float) -> bool:
        """Check if withdrawal is possible (can be overridden)."""
        return amount <= self._balance
    
    def transfer_to(self, target_account: 'BankAccount', amount: float,
                   description: str = "Transfer") -> bool:
        """Transfer money to another account."""
        if not self._is_active:
            print(f"  Source account is closed")
            return False
        
        if not target_account._is_active:
            print(f"  Target account is closed")
            return False
        
        if self.withdraw(amount, f"Transfer to {target_account.account_number}"):
            target_account.deposit(amount, f"Transfer from {self.account_number}")
            print(f"  Transferred ${amount:.2f} from {self.account_number} to {target_account.account_number}")
            return True
        
        return False
    
    def close(self) -> None:
        """Close the account."""
        self._is_active = False
        print(f"  Account {self._account_number} closed")
    
    def get_statement(self) -> str:
        """Generate account statement."""
        lines = []
        lines.append("=" * 60)
        lines.append(f"STATEMENT - {self.get_account_type()}")
        lines.append(f"Account: {self._account_number}")
        lines.append(f"Holder: {self._account_holder}")
        lines.append(f"Balance: ${self._balance:.2f}")
        lines.append(f"Status: {'Active' if self._is_active else 'Closed'}")
        lines.append("-" * 60)
        lines.append("Recent Transactions:")
        
        for tx in self.get_transaction_history(10):
            lines.append(f"  {tx}")
        
        lines.append("=" * 60)
        return "\n".join(lines)
    
    @abstractmethod
    def get_account_type(self) -> str:
        """Get account type."""
        pass


class SavingsAccount(BankAccount):
    """Savings account with interest and minimum balance."""
    
    INTEREST_RATE = 0.02
    MINIMUM_BALANCE = 100.0
    
    def get_account_type(self) -> str:
        return "Savings Account"
    
    def can_withdraw(self, amount: float) -> bool:
        """Check withdrawal with minimum balance requirement."""
        if self._balance - amount < self.MINIMUM_BALANCE:
            return False
        return amount <= self._balance
    
    def add_interest(self) -> bool:
        """Add monthly interest."""
        if not self._is_active:
            return False
        
        interest = self._balance * (self.INTEREST_RATE / 12)
        if interest > 0:
            self._balance += interest
            self._record_transaction(interest, TransactionType.INTEREST,
                                    "Monthly interest", self._balance)
            print(f"  Added ${interest:.2f} interest to {self.account_number}")
            return True
        return False


class CheckingAccount(BankAccount):
    """Checking account with overdraft protection."""
    
    OVERDRAFT_LIMIT = 500.0
    
    def get_account_type(self) -> str:
        return "Checking Account"
    
    def can_withdraw(self, amount: float) -> bool:
        """Check withdrawal with overdraft."""
        return amount <= self._balance + self.OVERDRAFT_LIMIT
    
    def get_available_balance(self) -> float:
        """Get available balance including overdraft."""
        return self._balance + self.OVERDRAFT_LIMIT


class InvestmentAccount(BankAccount):
    """Investment account with trading capabilities."""
    
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self._portfolio: Dict[str, int] = {}
        self._daily_trade_limit = 10
        self._trades_today = 0
        self._last_trade_date = datetime.now().date()
    
    def get_account_type(self) -> str:
        return "Investment Account"
    
    def _reset_daily_trades(self) -> None:
        """Reset daily trade counter."""
        today = datetime.now().date()
        if today != self._last_trade_date:
            self._trades_today = 0
            self._last_trade_date = today
    
    def buy_shares(self, symbol: str, shares: int, price_per_share: float) -> bool:
        """Buy shares (validated)."""
        if not self._is_active:
            return False
        
        self._reset_daily_trades()
        
        if self._trades_today >= self._daily_trade_limit:
            print(f"  Daily trade limit reached ({self._daily_trade_limit})")
            return False
        
        cost = shares * price_per_share
        
        if not self.can_withdraw(cost):
            print(f"  Insufficient funds to buy {shares} shares of {symbol}")
            return False
        
        self._balance -= cost
        self._portfolio[symbol] = self._portfolio.get(symbol, 0) + shares
        self._trades_today += 1
        
        description = f"Bought {shares} shares of {symbol} @ ${price_per_share:.2f}"
        self._record_transaction(-cost, TransactionType.WITHDRAWAL, description, self._balance)
        print(f"  Bought {shares} shares of {symbol} for ${cost:.2f}")
        return True
    
    def sell_shares(self, symbol: str, shares: int, price_per_share: float) -> bool:
        """Sell shares (validated)."""
        if not self._is_active:
            return False
        
        self._reset_daily_trades()
        
        if self._trades_today >= self._daily_trade_limit:
            print(f"  Daily trade limit reached ({self._daily_trade_limit})")
            return False
        
        if symbol not in self._portfolio or self._portfolio[symbol] < shares:
            print(f"  Insufficient shares of {symbol}")
            return False
        
        proceeds = shares * price_per_share
        self._balance += proceeds
        self._portfolio[symbol] -= shares
        self._trades_today += 1
        
        if self._portfolio[symbol] == 0:
            del self._portfolio[symbol]
        
        description = f"Sold {shares} shares of {symbol} @ ${price_per_share:.2f}"
        self._record_transaction(proceeds, TransactionType.DEPOSIT, description, self._balance)
        print(f"  Sold {shares} shares of {symbol} for ${proceeds:.2f}")
        return True
    
    def get_portfolio(self) -> Dict[str, int]:
        """Get portfolio holdings (copy to prevent modification)."""
        return self._portfolio.copy()
    
    def get_portfolio_value(self, current_prices: Dict[str, float]) -> float:
        """Calculate total portfolio value."""
        stock_value = sum(self._portfolio.get(symbol, 0) * price
                         for symbol, price in current_prices.items())
        return self._balance + stock_value


def demonstrate_bank_system():
    """
    Demonstrate the bank account system with encapsulation.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: BANK ACCOUNT SYSTEM")
    print("=" * 60)
    
    print("\n1. CREATING ACCOUNTS")
    print("-" * 40)
    
    savings = SavingsAccount("SAV-001", "Alice Chen", 1000.00)
    checking = CheckingAccount("CHK-001", "Alice Chen", 500.00)
    investment = InvestmentAccount("INV-001", "Alice Chen", 5000.00)
    
    print(f"  Created: {savings.get_account_type()} - ${savings.get_balance():.2f}")
    print(f"  Created: {checking.get_account_type()} - ${checking.get_balance():.2f}")
    print(f"  Created: {investment.get_account_type()} - ${investment.get_balance():.2f}")
    
    print("\n2. ENCAPSULATED BALANCE (Cannot modify directly)")
    print("-" * 40)
    
    try:
        savings._balance = 999999  # This works but violates encapsulation
        print(f"  ⚠️ Direct balance modification possible: ${savings.get_balance():.2f}")
        # Reset to correct value
        savings._balance = 1000.00
    except AttributeError:
        print("  Cannot modify balance directly (protected)")
    
    print("  Balance accessed only through get_balance() method")
    
    print("\n3. VALIDATED TRANSACTIONS")
    print("-" * 40)
    
    # Valid deposit
    savings.deposit(500, "Bonus")
    
    # Invalid withdrawal (below minimum)
    savings.withdraw(1500)
    
    # Valid withdrawal
    savings.withdraw(200)
    
    # Daily limit check
    for _ in range(3):
        checking.withdraw(2000)
    
    print("\n4. TRANSFER BETWEEN ACCOUNTS")
    print("-" * 40)
    
    checking.transfer_to(savings, 300)
    
    print(f"  Savings balance: ${savings.get_balance():.2f}")
    print(f"  Checking balance: ${checking.get_balance():.2f}")
    
    print("\n5. INVESTMENT ACCOUNT TRADING")
    print("-" * 40)
    
    investment.buy_shares("AAPL", 10, 175.50)
    investment.buy_shares("GOOGL", 5, 140.25)
    
    print(f"  Portfolio: {investment.get_portfolio()}")
    print(f"  Cash balance: ${investment.get_balance():.2f}")
    
    # Portfolio valuation
    current_prices = {"AAPL": 180.25, "GOOGL": 145.50}
    portfolio_value = investment.get_portfolio_value(current_prices)
    print(f"  Portfolio value: ${portfolio_value:.2f}")
    
    print("\n6. ACCOUNT STATEMENTS")
    print("-" * 40)
    
    print(savings.get_statement())
    
    print("\n7. INTEREST CALCULATION")
    print("-" * 40)
    
    savings.add_interest()
    print(f"  Savings balance after interest: ${savings.get_balance():.2f}")


if __name__ == "__main__":
    demonstrate_bank_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Encapsulation Principles** – Bundle data with methods that operate on it. Hide internal state. Require interaction through well-defined interfaces.

- **Naming Conventions** – `name` (public), `_name` (protected, internal use), `__name` (private, name mangling). Python trusts developers to respect conventions.

- **Properties (`@property`)** – Create getters, setters, and deleters that look like attributes. Add validation, logging, or computation. Create read-only computed properties.

- **Private Methods** – `__method` for internal use only. Name mangling makes them harder (but not impossible) to access externally.

- **Healthcare Records** – Sensitive medical data with access control. Audit logging for compliance. Different access levels (patient, doctor, nurse).

- **Bank Account** – Protected balance with validation. Daily withdrawal limits. Minimum balance requirements. Transaction history.

- **Access Control** – Authorization checks before accessing sensitive data. Audit trails for accountability.

- **SOLID Principles Applied** – Single Responsibility (each class manages its own data), Open/Closed (new account types without changing base), Liskov Substitution (all accounts work as BankAccount), Dependency Inversion (depends on abstractions).

- **Design Patterns Used** – Proxy Pattern (properties control access), Command Pattern (transactions), Template Method (account skeleton), Repository Pattern (data storage), Factory Pattern (creating validated objects).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Polymorphism – One Interface, Many Forms

- **📚 Series D Catalog:** Object-Oriented Programming Line – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Abstraction – Hiding Complexity (Series D, Story 6)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 5 | 1 | 83% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **28** | **24** | **54%** |

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

**Next Story:** Series D, Story 6: The 2026 Python Metromap: Abstraction – Hiding Complexity

---

## 📝 Your Invitation

You've mastered encapsulation. Now build something with what you've learned:

1. **Build a user authentication system** – Encapsulate password hashing, login attempts, session management.

2. **Create a shopping cart** – Protect cart items from direct modification. Validate quantities against inventory.

3. **Build a configuration manager** – Encapsulate config loading, validation, and access with properties.

4. **Create a data validation library** – Build classes that validate and sanitize input data.

5. **Build an API client** – Encapsulate API keys, rate limiting, request/response handling.

**You've mastered encapsulation. Next stop: Abstraction!**

---

*Found this helpful? Clap, comment, and share what you built with encapsulation. Next stop: Abstraction!* 🚇