# The 2026 Python Metromap: Inheritance – Reusing Parent Classes

## Series D: Object-Oriented Programming (OOP) Line | Story 3 of 6

![The 2026 Python Metromap/images/Inheritance – Reusing Parent Classes](images/Inheritance – Reusing Parent Classes.png)

## 📖 Introduction

**Welcome to the third stop on the Object-Oriented Programming Line.**

You've mastered classes, objects, and constructors. You know how to create blueprints and initialize instances. But as your systems grow, you'll notice common patterns—multiple classes sharing similar attributes and methods. Writing the same code repeatedly violates the DRY (Don't Repeat Yourself) principle and makes maintenance difficult.

That's where inheritance comes in.

Inheritance allows a class (child) to inherit attributes and methods from another class (parent). The child class automatically gets everything the parent has, then can add its own specialized attributes and methods or override existing ones. Inheritance promotes code reuse, establishes relationships between classes, and enables polymorphic behavior.

This story—**The 2026 Python Metromap: Inheritance – Reusing Parent Classes**—is your guide to mastering inheritance in Python. We'll build a complete vehicle fleet management system with a base Vehicle class and specialized Car, Truck, and Motorcycle classes. We'll create an employee hierarchy with different employee types. We'll implement a payment processing system with various payment methods. And we'll build a complete shape library demonstrating method overriding and the super() function.

**Let's inherit.**

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

- 👪 **The 2026 Python Metromap: Inheritance – Reusing Parent Classes** – Vehicle fleet manager with Car, Truck, and Motorcycle classes. **⬅️ YOU ARE HERE**

- 🎭 **The 2026 Python Metromap: Polymorphism – One Interface, Many Forms** – Payment processing with CreditCard, PayPal, and Crypto implementations. 🔜 *Up Next*

- 🛡️ **The 2026 Python Metromap: Encapsulation – Protecting Data** – Healthcare records system; private attributes; validation rules.

- 🎨 **The 2026 Python Metromap: Abstraction – Hiding Complexity** – Email notification service; simplified interface for complex operations.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 👪 Section 1: Inheritance Basics – Parent and Child Classes

Inheritance allows a child class to inherit attributes and methods from a parent class, promoting code reuse and establishing hierarchical relationships.

**SOLID Principle Applied: Liskov Substitution** – Derived classes must be substitutable for their base classes.

**Design Pattern: Template Method Pattern** – Parent class defines the skeleton, children implement specifics.

```python
"""
INHERITANCE BASICS: PARENT AND CHILD CLASSES

This section covers the fundamentals of inheritance.

SOLID Principle: Liskov Substitution
- Derived classes must be substitutable for base classes

Design Pattern: Template Method Pattern
- Parent defines skeleton, children implement specifics
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import math


def demonstrate_basic_inheritance():
    """
    Demonstrates basic inheritance syntax and concepts.
    
    Child class inherits all attributes and methods from parent.
    """
    print("=" * 60)
    print("SECTION 1A: BASIC INHERITANCE")
    print("=" * 60)
    
    # PARENT CLASS
    print("\n1. PARENT CLASS (Animal)")
    print("-" * 40)
    
    class Animal:
        """Base class for all animals."""
        
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
            self.created_at = datetime.now()
        
        def speak(self) -> str:
            """Make the animal sound."""
            return "Some generic animal sound"
        
        def move(self) -> str:
            """How the animal moves."""
            return "The animal moves"
        
        def get_info(self) -> Dict:
            """Get animal information."""
            return {
                "name": self.name,
                "age": self.age,
                "type": "Animal"
            }
    
    # CHILD CLASS (inherits from Animal)
    print("\n2. CHILD CLASS (Dog inherits from Animal)")
    print("-" * 40)
    
    class Dog(Animal):
        """Dog class inheriting from Animal."""
        
        def speak(self) -> str:
            """Override the speak method."""
            return "Woof!"
        
        def move(self) -> str:
            """Override the move method."""
            return "The dog runs on four legs"
        
        def fetch(self) -> str:
            """Dog-specific method not in Animal."""
            return f"{self.name} fetches the ball!"
    
    # Create instances
    generic_animal = Animal("Unknown", 5)
    buddy = Dog("Buddy", 3)
    
    print(f"  Generic animal speaks: {generic_animal.speak()}")
    print(f"  Buddy speaks: {buddy.speak()}")
    print(f"  Buddy moves: {buddy.move()}")
    print(f"  Buddy fetches: {buddy.fetch()}")
    print(f"  Buddy info: {buddy.get_info()}")
    
    # Check inheritance relationships
    print("\n3. INHERITANCE RELATIONSHIPS")
    print("-" * 40)
    
    print(f"  Is buddy an Animal? {isinstance(buddy, Animal)}")
    print(f"  Is buddy a Dog? {isinstance(buddy, Dog)}")
    print(f"  Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")
    print(f"  Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")
    
    # MULTIPLE CHILDREN
    print("\n4. MULTIPLE CHILDREN (Cat and Bird)")
    print("-" * 40)
    
    class Cat(Animal):
        """Cat class inheriting from Animal."""
        
        def speak(self) -> str:
            return "Meow!"
        
        def move(self) -> str:
            return "The cat walks silently"
        
        def scratch(self) -> str:
            return f"{self.name} scratches the furniture!"
    
    class Bird(Animal):
        """Bird class inheriting from Animal."""
        
        def speak(self) -> str:
            return "Chirp!"
        
        def move(self) -> str:
            return "The bird flies through the air"
        
        def fly(self) -> str:
            return f"{self.name} soars through the sky!"
    
    whiskers = Cat("Whiskers", 2)
    tweety = Bird("Tweety", 1)
    
    print(f"  Cat: {whiskers.speak()}")
    print(f"  Bird: {tweety.speak()}")
    print(f"  Bird flies: {tweety.fly()}")


def demonstrate_method_override():
    """
    Demonstrates method overriding and the super() function.
    
    super() allows calling parent class methods from child classes.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: METHOD OVERRIDING AND super()")
    print("=" * 60)
    
    # WITHOUT super() - manually calling parent
    print("\n1. WITHOUT super() (Manual parent call)")
    print("-" * 40)
    
    class Vehicle:
        """Base Vehicle class."""
        
        def __init__(self, brand: str, model: str, year: int):
            print(f"  Vehicle.__init__ called for {brand} {model}")
            self.brand = brand
            self.model = model
            self.year = year
            self.is_running = False
        
        def start(self) -> str:
            self.is_running = True
            return "Vehicle engine started"
        
        def stop(self) -> str:
            self.is_running = False
            return "Vehicle engine stopped"
    
    class Car(Vehicle):
        """Car class - manually calls parent."""
        
        def __init__(self, brand: str, model: str, year: int, doors: int):
            print(f"  Car.__init__ called")
            # Manually call parent constructor
            Vehicle.__init__(self, brand, model, year)
            self.doors = doors
        
        def start(self) -> str:
            print("  Car.start called")
            return "Car engine started with a roar!"
    
    car = Car("Toyota", "Camry", 2024, 4)
    print(f"  Car start: {car.start()}")
    
    # WITH super() - recommended way
    print("\n2. WITH super() (Recommended)")
    print("-" * 40)
    
    class ElectricCar(Vehicle):
        """Electric Car class using super()."""
        
        def __init__(self, brand: str, model: str, year: int, battery_range: int):
            print(f"  ElectricCar.__init__ called")
            # super() automatically finds parent
            super().__init__(brand, model, year)
            self.battery_range = battery_range
        
        def start(self) -> str:
            # Call parent method then add behavior
            parent_result = super().start()
            return f"{parent_result} silently (electric motor)"
        
        def charge(self) -> str:
            return f"Charging battery ({self.battery_range} miles range)"
    
    tesla = ElectricCar("Tesla", "Model 3", 2024, 350)
    print(f"  Electric car start: {tesla.start()}")
    print(f"  Electric car charge: {tesla.charge()}")
    print(f"  Brand: {tesla.brand}, Model: {tesla.model}")
    
    # MULTILEVEL INHERITANCE
    print("\n3. MULTILEVEL INHERITANCE")
    print("-" * 40)
    
    class SportsCar(Car):
        """SportsCar inheriting from Car."""
        
        def __init__(self, brand: str, model: str, year: int, doors: int, top_speed: int):
            super().__init__(brand, model, year, doors)
            self.top_speed = top_speed
        
        def start(self) -> str:
            return f"Sports car roars to life! {self.top_speed} mph potential!"
        
        def turbo_boost(self) -> str:
            return f"Turbo boost engaged! {self.top_speed} mph!"
    
    ferrari = SportsCar("Ferrari", "488 GTB", 2024, 2, 205)
    print(f"  Sports car: {ferrari.start()}")
    print(f"  Turbo boost: {ferrari.turbo_boost()}")
    print(f"  Parent method via super: {super(SportsCar, ferrari).start()}")
    
    # METHOD RESOLUTION ORDER (MRO)
    print("\n4. METHOD RESOLUTION ORDER (MRO)")
    print("-" * 40)
    
    print(f"  SportsCar MRO: {[cls.__name__ for cls in SportsCar.__mro__]}")
    print("  Python looks for methods in this order")


def demonstrate_property_inheritance():
    """
    Demonstrates inheritance of properties and attributes.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: PROPERTY INHERITANCE")
    print("=" * 60)
    
    class Employee:
        """Base Employee class."""
        
        def __init__(self, name: str, salary: float):
            self._name = name
            self._salary = salary
        
        @property
        def name(self) -> str:
            return self._name
        
        @property
        def salary(self) -> float:
            return self._salary
        
        def calculate_bonus(self) -> float:
            """Calculate annual bonus."""
            return self._salary * 0.05
    
    class Manager(Employee):
        """Manager inherits from Employee."""
        
        def __init__(self, name: str, salary: float, team_size: int):
            super().__init__(name, salary)
            self.team_size = team_size
        
        def calculate_bonus(self) -> float:
            """Override bonus calculation for managers."""
            # Managers get higher bonus
            return self._salary * 0.10 + (self.team_size * 500)
        
        @property
        def team_info(self) -> str:
            return f"Manages team of {self.team_size} people"
    
    class Executive(Manager):
        """Executive inherits from Manager."""
        
        def __init__(self, name: str, salary: float, team_size: int, stock_options: int):
            super().__init__(name, salary, team_size)
            self.stock_options = stock_options
        
        def calculate_bonus(self) -> float:
            """Override bonus calculation for executives."""
            base_bonus = super().calculate_bonus()
            stock_bonus = self.stock_options * 10
            return base_bonus + stock_bonus
    
    # Create instances
    emp = Employee("Alice Chen", 75000)
    mgr = Manager("Bob Smith", 120000, 8)
    exec_officer = Executive("Carol Davis", 250000, 50, 10000)
    
    print(f"  Employee {emp.name}: bonus = ${emp.calculate_bonus():,.2f}")
    print(f"  Manager {mgr.name}: bonus = ${mgr.calculate_bonus():,.2f}")
    print(f"  Executive {exec_officer.name}: bonus = ${exec_officer.calculate_bonus():,.2f}")
    print(f"  Manager team info: {mgr.team_info}")


if __name__ == "__main__":
    demonstrate_basic_inheritance()
    demonstrate_method_override()
    demonstrate_property_inheritance()
```

---

## 🚗 Section 2: Vehicle Fleet Management System

A complete vehicle fleet management system with a base Vehicle class and specialized Car, Truck, and Motorcycle classes.

**SOLID Principles Applied:**
- Liskov Substitution: All vehicle types can be used interchangeably
- Open/Closed: New vehicle types can be added without modifying existing code

**Design Patterns:**
- Template Method Pattern: Base class defines common structure
- Factory Pattern: Creates different vehicle types

```python
"""
VEHICLE FLEET MANAGEMENT SYSTEM

This section builds a complete vehicle fleet management system using inheritance.

SOLID Principles Applied:
- Liskov Substitution: All vehicle types interchangeable
- Open/Closed: New vehicle types can be added

Design Patterns:
- Template Method Pattern: Base class defines common structure
- Factory Pattern: Creates different vehicle types
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod
import uuid


class FuelType(Enum):
    """Types of fuel."""
    GASOLINE = "gasoline"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"
    HYDROGEN = "hydrogen"


class TransmissionType(Enum):
    """Types of transmission."""
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    CVT = "cvt"
    DUAL_CLUTCH = "dual_clutch"


class VehicleStatus(Enum):
    """Vehicle status."""
    AVAILABLE = "available"
    RENTED = "rented"
    MAINTENANCE = "maintenance"
    RETIRED = "retired"


class Vehicle(ABC):
    """
    Abstract base class for all vehicles.
    
    SOLID: Liskov Substitution - All vehicles can be used as Vehicle
    Design Pattern: Template Method - Defines vehicle structure
    """
    
    def __init__(self, vin: str, make: str, model: str, year: int,
                 fuel_type: FuelType, transmission: TransmissionType,
                 rental_rate: float):
        """
        Initialize a vehicle.
        
        Args:
            vin: Vehicle Identification Number
            make: Manufacturer (e.g., Toyota, Ford)
            model: Model name (e.g., Camry, F-150)
            year: Manufacturing year
            fuel_type: Type of fuel
            transmission: Transmission type
            rental_rate: Daily rental rate
        """
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.rental_rate = rental_rate
        self.status = VehicleStatus.AVAILABLE
        self.mileage = 0
        self.last_maintenance = datetime.now()
        self.maintenance_history: List[Dict] = []
        self.rental_history: List[Dict] = []
    
    @abstractmethod
    def get_vehicle_type(self) -> str:
        """Return the type of vehicle."""
        pass
    
    @abstractmethod
    def get_max_passengers(self) -> int:
        """Return maximum number of passengers."""
        pass
    
    @abstractmethod
    def get_cargo_capacity(self) -> float:
        """Return cargo capacity in cubic feet."""
        pass
    
    def calculate_rental_cost(self, days: int) -> float:
        """Calculate rental cost for given days."""
        return self.rental_rate * days
    
    def rent(self, customer_id: str, days: int) -> Tuple[bool, str]:
        """Rent the vehicle."""
        if self.status != VehicleStatus.AVAILABLE:
            return False, f"Vehicle {self.vin} is not available"
        
        rental_id = str(uuid.uuid4())[:8]
        cost = self.calculate_rental_cost(days)
        
        self.status = VehicleStatus.RENTED
        self.rental_history.append({
            "rental_id": rental_id,
            "customer_id": customer_id,
            "start_date": datetime.now().isoformat(),
            "days": days,
            "cost": cost
        })
        
        return True, rental_id
    
    def return_vehicle(self, mileage_added: int) -> None:
        """Return the vehicle from rental."""
        if self.status != VehicleStatus.RENTED:
            raise ValueError(f"Vehicle {self.vin} is not rented")
        
        self.status = VehicleStatus.AVAILABLE
        self.mileage += mileage_added
        
        if self.rental_history:
            self.rental_history[-1]["end_date"] = datetime.now().isoformat()
            self.rental_history[-1]["mileage_added"] = mileage_added
    
    def schedule_maintenance(self) -> None:
        """Schedule vehicle for maintenance."""
        self.status = VehicleStatus.MAINTENANCE
        self.maintenance_history.append({
            "date": datetime.now().isoformat(),
            "mileage": self.mileage
        })
    
    def complete_maintenance(self) -> None:
        """Complete maintenance."""
        if self.status == VehicleStatus.MAINTENANCE:
            self.status = VehicleStatus.AVAILABLE
            self.last_maintenance = datetime.now()
    
    def needs_maintenance(self) -> bool:
        """Check if vehicle needs maintenance."""
        # Simplified: maintenance every 5000 miles
        if not self.maintenance_history:
            return self.mileage > 5000
        
        last_maintenance_mileage = self.maintenance_history[-1]["mileage"]
        return (self.mileage - last_maintenance_mileage) > 5000
    
    def to_dict(self) -> Dict:
        """Convert vehicle to dictionary."""
        return {
            "vin": self.vin,
            "type": self.get_vehicle_type(),
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "fuel_type": self.fuel_type.value,
            "transmission": self.transmission.value,
            "status": self.status.value,
            "mileage": self.mileage,
            "rental_rate": self.rental_rate,
            "max_passengers": self.get_max_passengers(),
            "cargo_capacity": self.get_cargo_capacity()
        }
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.get_vehicle_type()}) - ${self.rental_rate}/day"


class Car(Vehicle):
    """Car class inheriting from Vehicle."""
    
    def __init__(self, vin: str, make: str, model: str, year: int,
                 fuel_type: FuelType, transmission: TransmissionType,
                 rental_rate: float, doors: int, has_sunroof: bool = False):
        super().__init__(vin, make, model, year, fuel_type, transmission, rental_rate)
        self.doors = doors
        self.has_sunroof = has_sunroof
    
    def get_vehicle_type(self) -> str:
        return "Car"
    
    def get_max_passengers(self) -> int:
        return 5
    
    def get_cargo_capacity(self) -> float:
        return 15.0
    
    def __str__(self) -> str:
        base = super().__str__()
        sunroof = "with sunroof" if self.has_sunroof else ""
        return f"{base} - {self.doors} doors {sunroof}".strip()


class Truck(Vehicle):
    """Truck class inheriting from Vehicle."""
    
    def __init__(self, vin: str, make: str, model: str, year: int,
                 fuel_type: FuelType, transmission: TransmissionType,
                 rental_rate: float, payload_capacity: float, towing_capacity: float):
        super().__init__(vin, make, model, year, fuel_type, transmission, rental_rate)
        self.payload_capacity = payload_capacity
        self.towing_capacity = towing_capacity
    
    def get_vehicle_type(self) -> str:
        return "Truck"
    
    def get_max_passengers(self) -> int:
        return 3
    
    def get_cargo_capacity(self) -> float:
        return self.payload_capacity
    
    def __str__(self) -> str:
        return f"{super().__str__()} - {self.payload_capacity} lbs payload, {self.towing_capacity} lbs towing"


class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle."""
    
    def __init__(self, vin: str, make: str, model: str, year: int,
                 fuel_type: FuelType, transmission: TransmissionType,
                 rental_rate: float, engine_cc: int, has_sidecar: bool = False):
        super().__init__(vin, make, model, year, fuel_type, transmission, rental_rate)
        self.engine_cc = engine_cc
        self.has_sidecar = has_sidecar
    
    def get_vehicle_type(self) -> str:
        return "Motorcycle"
    
    def get_max_passengers(self) -> int:
        return 2 if self.has_sidecar else 1
    
    def get_cargo_capacity(self) -> float:
        return 5.0
    
    def __str__(self) -> str:
        sidecar = "with sidecar" if self.has_sidecar else ""
        return f"{super().__str__()} - {self.engine_cc}cc {sidecar}".strip()


class SUV(Vehicle):
    """SUV class inheriting from Vehicle."""
    
    def __init__(self, vin: str, make: str, model: str, year: int,
                 fuel_type: FuelType, transmission: TransmissionType,
                 rental_rate: float, seats: int, four_wheel_drive: bool = True):
        super().__init__(vin, make, model, year, fuel_type, transmission, rental_rate)
        self.seats = seats
        self.four_wheel_drive = four_wheel_drive
    
    def get_vehicle_type(self) -> str:
        return "SUV"
    
    def get_max_passengers(self) -> int:
        return self.seats
    
    def get_cargo_capacity(self) -> float:
        return 35.0
    
    def __str__(self) -> str:
        awd = "4WD" if self.four_wheel_drive else "2WD"
        return f"{super().__str__()} - {self.seats} seats, {awd}"


class ElectricVehicleMixin:
    """Mixin for electric vehicles."""
    
    def __init__(self, battery_capacity: float, charge_time_hours: float):
        self.battery_capacity = battery_capacity
        self.charge_time_hours = charge_time_hours
        self.battery_level = 100
    
    def charge(self, hours: float) -> str:
        """Charge the vehicle."""
        charge_added = (hours / self.charge_time_hours) * 100
        self.battery_level = min(100, self.battery_level + charge_added)
        return f"Charged {charge_added:.1f}%. Battery at {self.battery_level:.0f}%"
    
    def get_range(self) -> float:
        """Estimate range based on battery level."""
        return (self.battery_capacity * (self.battery_level / 100)) * 4  # Rough estimate


class ElectricCar(Car, ElectricVehicleMixin):
    """Electric Car combining Car and ElectricVehicleMixin."""
    
    def __init__(self, vin: str, make: str, model: str, year: int,
                 transmission: TransmissionType, rental_rate: float,
                 doors: int, battery_capacity: float, charge_time_hours: float,
                 has_sunroof: bool = False):
        # Initialize parent classes
        Car.__init__(self, vin, make, model, year, FuelType.ELECTRIC,
                     transmission, rental_rate, doors, has_sunroof)
        ElectricVehicleMixin.__init__(self, battery_capacity, charge_time_hours)
    
    def __str__(self) -> str:
        return f"{super().__str__()} - Electric, {self.battery_capacity}kWh battery"


class FleetManager:
    """
    Manages a fleet of vehicles.
    
    Design Pattern: Repository Pattern - Vehicle storage and retrieval
    """
    
    def __init__(self):
        self.vehicles: Dict[str, Vehicle] = {}
    
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the fleet."""
        self.vehicles[vehicle.vin] = vehicle
        print(f"  Added: {vehicle}")
    
    def get_vehicle(self, vin: str) -> Optional[Vehicle]:
        """Get vehicle by VIN."""
        return self.vehicles.get(vin)
    
    def get_available_vehicles(self) -> List[Vehicle]:
        """Get all available vehicles."""
        return [v for v in self.vehicles.values() if v.status == VehicleStatus.AVAILABLE]
    
    def get_vehicles_by_type(self, vehicle_type: str) -> List[Vehicle]:
        """Get vehicles by type."""
        return [v for v in self.vehicles.values() if v.get_vehicle_type() == vehicle_type]
    
    def rent_vehicle(self, vin: str, customer_id: str, days: int) -> Tuple[bool, str]:
        """Rent a vehicle by VIN."""
        vehicle = self.get_vehicle(vin)
        if not vehicle:
            return False, f"Vehicle {vin} not found"
        return vehicle.rent(customer_id, days)
    
    def return_vehicle(self, vin: str, mileage_added: int) -> bool:
        """Return a rented vehicle."""
        vehicle = self.get_vehicle(vin)
        if not vehicle:
            return False
        vehicle.return_vehicle(mileage_added)
        return True
    
    def get_fleet_statistics(self) -> Dict:
        """Get fleet statistics."""
        vehicles = self.vehicles.values()
        
        return {
            "total_vehicles": len(vehicles),
            "available": sum(1 for v in vehicles if v.status == VehicleStatus.AVAILABLE),
            "rented": sum(1 for v in vehicles if v.status == VehicleStatus.RENTED),
            "maintenance": sum(1 for v in vehicles if v.status == VehicleStatus.MAINTENANCE),
            "by_type": {
                vehicle_type: len(self.get_vehicles_by_type(vehicle_type))
                for vehicle_type in ["Car", "Truck", "Motorcycle", "SUV"]
            },
            "total_revenue": self._calculate_total_revenue()
        }
    
    def _calculate_total_revenue(self) -> float:
        """Calculate total revenue from all rentals."""
        total = 0.0
        for vehicle in self.vehicles.values():
            for rental in vehicle.rental_history:
                total += rental.get("cost", 0)
        return round(total, 2)
    
    def generate_fleet_report(self) -> str:
        """Generate a fleet report."""
        report = []
        report.append("=" * 60)
        report.append("FLEET MANAGEMENT REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        stats = self.get_fleet_statistics()
        report.append(f"\n📊 STATISTICS:")
        report.append(f"  Total Vehicles: {stats['total_vehicles']}")
        report.append(f"  Available: {stats['available']}")
        report.append(f"  Rented: {stats['rented']}")
        report.append(f"  Maintenance: {stats['maintenance']}")
        report.append(f"  Total Revenue: ${stats['total_revenue']:,.2f}")
        
        report.append(f"\n🚗 VEHICLES BY TYPE:")
        for vtype, count in stats['by_type'].items():
            if count > 0:
                report.append(f"  {vtype}: {count}")
        
        report.append(f"\n🔧 VEHICLES NEEDING MAINTENANCE:")
        for vehicle in self.vehicles.values():
            if vehicle.needs_maintenance():
                report.append(f"  {vehicle.make} {vehicle.model} - {vehicle.mileage} miles")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)


def demonstrate_fleet_system():
    """
    Demonstrate the vehicle fleet management system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: VEHICLE FLEET MANAGEMENT SYSTEM")
    print("=" * 60)
    
    fleet = FleetManager()
    
    print("\n1. ADDING VEHICLES TO FLEET")
    print("-" * 40)
    
    # Add cars
    car1 = Car("1HGCM82633A123456", "Honda", "Civic", 2023,
               FuelType.GASOLINE, TransmissionType.AUTOMATIC, 45.00, 4)
    car2 = Car("2FMDK3GC9DBA12345", "Ford", "Mustang", 2024,
               FuelType.GASOLINE, TransmissionType.MANUAL, 89.00, 2, True)
    
    # Add trucks
    truck1 = Truck("1FTFW1ET3EKE12345", "Ford", "F-150", 2023,
                   FuelType.GASOLINE, TransmissionType.AUTOMATIC, 95.00, 1500, 8000)
    
    # Add motorcycles
    bike1 = Motorcycle("JH2RC500XMK12345", "Honda", "CBR600RR", 2024,
                       FuelType.GASOLINE, TransmissionType.MANUAL, 65.00, 600)
    
    # Add SUV
    suv1 = SUV("5UXWX7C5XH0U12345", "BMW", "X5", 2024,
               FuelType.GASOLINE, TransmissionType.AUTOMATIC, 120.00, 7, True)
    
    # Add electric car
    ev1 = ElectricCar("1N4AZ1CP7JC123456", "Nissan", "Leaf", 2024,
                      TransmissionType.AUTOMATIC, 55.00, 4, 40.0, 8.0)
    
    for vehicle in [car1, car2, truck1, bike1, suv1, ev1]:
        fleet.add_vehicle(vehicle)
    
    print("\n2. FLEET STATISTICS")
    print("-" * 40)
    
    stats = fleet.get_fleet_statistics()
    for key, value in stats.items():
        if key == "by_type":
            print(f"  {key}:")
            for vtype, count in value.items():
                if count > 0:
                    print(f"    {vtype}: {count}")
        else:
            print(f"  {key}: {value}")
    
    print("\n3. RENTING A VEHICLE")
    print("-" * 40)
    
    success, rental_id = fleet.rent_vehicle(car1.vin, "CUST-001", 3)
    print(f"  Renting {car1.make} {car1.model}: {'Success' if success else 'Failed'}")
    if success:
        print(f"  Rental ID: {rental_id}")
        print(f"  Cost: ${car1.calculate_rental_cost(3):.2f}")
    
    print("\n4. AVAILABLE VEHICLES AFTER RENTAL")
    print("-" * 40)
    
    available = fleet.get_available_vehicles()
    print(f"  Available vehicles: {len(available)}")
    for v in available[:3]:
        print(f"    {v}")
    
    print("\n5. RETURNING VEHICLE")
    print("-" * 40)
    
    fleet.return_vehicle(car1.vin, 150)
    print(f"  Returned {car1.make} {car1.model} with 150 miles added")
    print(f"  Total mileage: {car1.mileage} miles")
    
    print("\n6. ELECTRIC VEHICLE FEATURES")
    print("-" * 40)
    
    print(f"  {ev1}")
    print(f"  Battery level: {ev1.battery_level}%")
    print(f"  Charging: {ev1.charge(4)}")
    print(f"  Estimated range: {ev1.get_range():.0f} miles")
    
    print("\n7. MAINTENANCE CHECK")
    print("-" * 40)
    
    # Add miles to trigger maintenance
    truck1.mileage = 6000
    if truck1.needs_maintenance():
        print(f"  {truck1.make} {truck1.model} needs maintenance!")
        truck1.schedule_maintenance()
        print(f"  Status: {truck1.status.value}")
    
    print("\n8. FLEET REPORT")
    print("-" * 40)
    
    report = fleet.generate_fleet_report()
    print(report)


if __name__ == "__main__":
    demonstrate_fleet_system()
```

---

## 🏢 Section 3: Employee Hierarchy System

A complete employee hierarchy demonstrating inheritance with different employee types, salary calculations, and benefits.

**SOLID Principles Applied:**
- Liskov Substitution: All employee types can be treated as Employee
- Open/Closed: New employee types can be added

**Design Patterns:**
- Template Method Pattern: Base class defines payroll calculation structure
- Composite Pattern: Department contains multiple employees

```python
"""
EMPLOYEE HIERARCHY SYSTEM

This section builds an employee hierarchy using inheritance.

SOLID Principles Applied:
- Liskov Substitution: All employee types can be treated as Employee
- Open/Closed: New employee types can be added

Design Patterns:
- Template Method Pattern: Base class defines payroll structure
- Composite Pattern: Department contains multiple employees
"""

from typing import List, Dict, Any, Optional
from datetime import datetime, date
from enum import Enum
from abc import ABC, abstractmethod
import uuid


class Department(Enum):
    """Company departments."""
    ENGINEERING = "Engineering"
    SALES = "Sales"
    MARKETING = "Marketing"
    HUMAN_RESOURCES = "Human Resources"
    FINANCE = "Finance"
    OPERATIONS = "Operations"


class Employee(ABC):
    """
    Abstract base class for all employees.
    
    SOLID: Liskov Substitution - All employees can be used as Employee
    """
    
    def __init__(self, employee_id: str, name: str, email: str,
                 department: Department, hire_date: date, base_salary: float):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.hire_date = hire_date
        self.base_salary = base_salary
        self.is_active = True
        self.performance_reviews: List[Dict] = []
    
    @abstractmethod
    def calculate_salary(self) -> float:
        """Calculate monthly salary including bonuses."""
        pass
    
    @abstractmethod
    def get_role(self) -> str:
        """Get employee role title."""
        pass
    
    def get_years_of_service(self) -> int:
        """Calculate years of service."""
        today = date.today()
        return today.year - self.hire_date.year
    
    def get_benefits(self) -> List[str]:
        """Get employee benefits."""
        benefits = ["Health Insurance", "Dental Insurance", "401(k)"]
        
        if self.get_years_of_service() >= 5:
            benefits.append("Extended Vacation")
        if self.get_years_of_service() >= 10:
            benefits.append("Sabbatical Leave")
        
        return benefits
    
    def add_performance_review(self, rating: int, comments: str) -> None:
        """Add a performance review."""
        self.performance_reviews.append({
            "date": datetime.now().isoformat(),
            "rating": rating,
            "comments": comments
        })
    
    def get_average_rating(self) -> float:
        """Calculate average performance rating."""
        if not self.performance_reviews:
            return 0.0
        ratings = [r["rating"] for r in self.performance_reviews]
        return sum(ratings) / len(ratings)
    
    def to_dict(self) -> Dict:
        """Convert employee to dictionary."""
        return {
            "id": self.employee_id,
            "name": self.name,
            "role": self.get_role(),
            "email": self.email,
            "department": self.department.value,
            "hire_date": self.hire_date.isoformat(),
            "years_of_service": self.get_years_of_service(),
            "salary": self.calculate_salary(),
            "benefits": self.get_benefits(),
            "active": self.is_active
        }
    
    def __str__(self) -> str:
        return f"{self.name} - {self.get_role()} ({self.department.value})"


class Engineer(Employee):
    """Engineer class inheriting from Employee."""
    
    def __init__(self, employee_id: str, name: str, email: str,
                 department: Department, hire_date: date, base_salary: float,
                 skill_level: int = 3, projects_completed: int = 0):
        super().__init__(employee_id, name, email, department, hire_date, base_salary)
        self.skill_level = skill_level  # 1-5
        self.projects_completed = projects_completed
    
    def get_role(self) -> str:
        levels = {1: "Junior", 2: "Mid", 3: "Senior", 4: "Lead", 5: "Principal"}
        return f"{levels.get(self.skill_level, 'Engineer')} Engineer"
    
    def calculate_salary(self) -> float:
        """Calculate salary with skill and project bonuses."""
        salary = self.base_salary
        
        # Skill level bonus
        salary += self.base_salary * (self.skill_level - 1) * 0.05
        
        # Project completion bonus
        project_bonus = self.projects_completed * 500
        salary += project_bonus
        
        return round(salary, 2)
    
    def complete_project(self) -> None:
        """Record a completed project."""
        self.projects_completed += 1
        print(f"  {self.name} completed project #{self.projects_completed}")


class SalesPerson(Employee):
    """SalesPerson class inheriting from Employee."""
    
    def __init__(self, employee_id: str, name: str, email: str,
                 department: Department, hire_date: date, base_salary: float,
                 commission_rate: float = 0.05, sales_volume: float = 0):
        super().__init__(employee_id, name, email, department, hire_date, base_salary)
        self.commission_rate = commission_rate
        self.sales_volume = sales_volume
    
    def get_role(self) -> str:
        return "Sales Representative"
    
    def calculate_salary(self) -> float:
        """Calculate salary with commission."""
        commission = self.sales_volume * self.commission_rate
        return round(self.base_salary + commission, 2)
    
    def add_sale(self, amount: float) -> None:
        """Record a sale."""
        self.sales_volume += amount
        print(f"  {self.name} made a sale of ${amount:,.2f}")


class Manager(Employee):
    """Manager class inheriting from Employee."""
    
    def __init__(self, employee_id: str, name: str, email: str,
                 department: Department, hire_date: date, base_salary: float,
                 team_size: int = 0, management_bonus: float = 0.10):
        super().__init__(employee_id, name, email, department, hire_date, base_salary)
        self.team_size = team_size
        self.management_bonus = management_bonus
    
    def get_role(self) -> str:
        return "Manager"
    
    def calculate_salary(self) -> float:
        """Calculate salary with management bonus."""
        bonus = self.base_salary * self.management_bonus
        team_bonus = self.team_size * 1000
        return round(self.base_salary + bonus + team_bonus, 2)
    
    def hire_employee(self) -> None:
        """Hire a new team member."""
        self.team_size += 1
        print(f"  {self.name} hired a new employee. Team size: {self.team_size}")


class Executive(Manager):
    """Executive class inheriting from Manager."""
    
    def __init__(self, employee_id: str, name: str, email: str,
                 department: Department, hire_date: date, base_salary: float,
                 team_size: int, stock_options: int, executive_bonus: float = 0.25):
        super().__init__(employee_id, name, email, department, hire_date,
                        base_salary, team_size)
        self.stock_options = stock_options
        self.executive_bonus = executive_bonus
    
    def get_role(self) -> str:
        return "Executive"
    
    def calculate_salary(self) -> float:
        """Calculate salary with executive bonus."""
        base = super().calculate_salary()
        bonus = self.base_salary * self.executive_bonus
        return round(base + bonus, 2)
    
    def get_benefits(self) -> List[str]:
        """Get executive benefits (additional)."""
        benefits = super().get_benefits()
        benefits.append("Company Car")
        benefits.append("Stock Options")
        return benefits


class DepartmentManager:
    """
    Manages employees within a department.
    
    Design Pattern: Composite Pattern - Department contains employees
    """
    
    def __init__(self, department: Department):
        self.department = department
        self.employees: List[Employee] = []
    
    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the department."""
        if employee.department != self.department:
            raise ValueError(f"Employee belongs to {employee.department.value}")
        self.employees.append(employee)
        print(f"  Added {employee.name} to {self.department.value}")
    
    def get_total_salary_expense(self) -> float:
        """Calculate total salary expense for the department."""
        return sum(e.calculate_salary() for e in self.employees)
    
    def get_employee_by_role(self, role: str) -> List[Employee]:
        """Get employees by role."""
        return [e for e in self.employees if e.get_role() == role]
    
    def get_average_salary(self) -> float:
        """Calculate average salary."""
        if not self.employees:
            return 0.0
        return self.get_total_salary_expense() / len(self.employees)
    
    def generate_department_report(self) -> str:
        """Generate department report."""
        report = []
        report.append(f"\n{'='*50}")
        report.append(f"DEPARTMENT: {self.department.value}")
        report.append(f"{'='*50}")
        report.append(f"Total Employees: {len(self.employees)}")
        report.append(f"Total Salary Expense: ${self.get_total_salary_expense():,.2f}")
        report.append(f"Average Salary: ${self.get_average_salary():,.2f}")
        
        report.append(f"\nEMPLOYEES:")
        for emp in self.employees:
            report.append(f"  {emp.name} ({emp.get_role()}) - ${emp.calculate_salary():,.2f}")
        
        return "\n".join(report)


def demonstrate_employee_system():
    """
    Demonstrate the employee hierarchy system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: EMPLOYEE HIERARCHY SYSTEM")
    print("=" * 60)
    
    # Create departments
    eng_dept = DepartmentManager(Department.ENGINEERING)
    sales_dept = DepartmentManager(Department.SALES)
    
    print("\n1. CREATING EMPLOYEES")
    print("-" * 40)
    
    # Create engineers
    alice = Engineer("EMP-001", "Alice Chen", "alice@metromap.com",
                     Department.ENGINEERING, date(2022, 6, 15), 85000, 4, 8)
    bob = Engineer("EMP-002", "Bob Smith", "bob@metromap.com",
                   Department.ENGINEERING, date(2023, 1, 10), 75000, 3, 3)
    
    # Create sales person
    carol = SalesPerson("EMP-003", "Carol Davis", "carol@metromap.com",
                        Department.SALES, date(2021, 3, 20), 65000, 0.08, 150000)
    
    # Create manager
    david = Manager("EMP-004", "David Wilson", "david@metromap.com",
                    Department.ENGINEERING, date(2018, 8, 1), 120000, 5)
    
    # Create executive
    emma = Executive("EMP-005", "Emma Brown", "emma@metromap.com",
                     Department.ENGINEERING, date(2015, 2, 10), 200000, 20, 10000)
    
    # Add to departments
    eng_dept.add_employee(alice)
    eng_dept.add_employee(bob)
    eng_dept.add_employee(david)
    eng_dept.add_employee(emma)
    sales_dept.add_employee(carol)
    
    print("\n2. EMPLOYEE DETAILS")
    print("-" * 40)
    
    for emp in [alice, bob, carol, david, emma]:
        print(f"\n  {emp.name} ({emp.get_role()}):")
        print(f"    Salary: ${emp.calculate_salary():,.2f}")
        print(f"    Years of service: {emp.get_years_of_service()}")
        print(f"    Benefits: {', '.join(emp.get_benefits())}")
    
    print("\n3. PERFORMANCE REVIEWS")
    print("-" * 40)
    
    alice.add_performance_review(5, "Excellent project delivery")
    alice.add_performance_review(4, "Good technical leadership")
    bob.add_performance_review(3, "Meets expectations")
    
    print(f"  Alice's avg rating: {alice.get_average_rating():.1f}")
    print(f"  Bob's avg rating: {bob.get_average_rating():.1f}")
    
    print("\n4. BUSINESS ACTIVITIES")
    print("-" * 40)
    
    alice.complete_project()
    bob.complete_project()
    carol.add_sale(50000)
    david.hire_employee()
    
    print("\n5. UPDATED SALARIES")
    print("-" * 40)
    
    print(f"  Alice's new salary: ${alice.calculate_salary():,.2f}")
    print(f"  Bob's new salary: ${bob.calculate_salary():,.2f}")
    print(f"  Carol's new salary: ${carol.calculate_salary():,.2f}")
    print(f"  David's new salary: ${david.calculate_salary():,.2f}")
    
    print("\n6. DEPARTMENT REPORTS")
    print("-" * 40)
    
    print(eng_dept.generate_department_report())
    print(sales_dept.generate_department_report())
    
    print("\n7. COMPANY-WIDE STATISTICS")
    print("-" * 40)
    
    all_employees = eng_dept.employees + sales_dept.employees
    total_salary = sum(e.calculate_salary() for e in all_employees)
    
    print(f"  Total Employees: {len(all_employees)}")
    print(f"  Total Salary Expense: ${total_salary:,.2f}")
    print(f"  Average Salary: ${total_salary / len(all_employees):,.2f}")


if __name__ == "__main__":
    demonstrate_employee_system()
```

---

## 🏦 Section 4: Payment Processing System

A payment processing system demonstrating inheritance with different payment methods.

**SOLID Principles Applied:**
- Liskov Substitution: All payment methods can be processed uniformly
- Open/Closed: New payment methods can be added

**Design Patterns:**
- Strategy Pattern: Different payment strategies
- Factory Pattern: Creates payment processors

```python
"""
PAYMENT PROCESSING SYSTEM

This section builds a payment processing system using inheritance.

SOLID Principles Applied:
- Liskov Substitution: All payment methods can be processed uniformly
- Open/Closed: New payment methods can be added

Design Patterns:
- Strategy Pattern: Different payment strategies
- Factory Pattern: Creates payment processors
"""

from typing import Dict, Any, Optional, Tuple
from datetime import datetime
from abc import ABC, abstractmethod
import uuid
import re
import random


class PaymentResult:
    """Result of a payment transaction."""
    
    def __init__(self, success: bool, transaction_id: str, message: str, 
                 amount: float, timestamp: datetime = None):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
        self.amount = amount
        self.timestamp = timestamp or datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "success": self.success,
            "transaction_id": self.transaction_id,
            "message": self.message,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __str__(self) -> str:
        status = "✅ SUCCESS" if self.success else "❌ FAILED"
        return f"{status}: {self.message} (ID: {self.transaction_id})"


class PaymentMethod(ABC):
    """
    Abstract base class for payment methods.
    
    SOLID: Liskov Substitution - All payment methods can be processed uniformly
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
    
    def get_fee(self, amount: float) -> float:
        """Calculate transaction fee."""
        return 0.0


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
        # Check card number (simple validation)
        if not self.card_number or len(self.card_number) < 13:
            return False, "Invalid card number length"
        
        if not self.card_number.isdigit():
            return False, "Card number must contain only digits"
        
        # Check expiry
        current_year = datetime.now().year
        current_month = datetime.now().month
        
        if self.expiry_year < current_year or \
           (self.expiry_year == current_year and self.expiry_month < current_month):
            return False, "Card has expired"
        
        if self.expiry_year > current_year + 10:
            return False, "Invalid expiry year"
        
        # Check CVV
        if not self.cvv.isdigit() or len(self.cvv) not in [3, 4]:
            return False, "Invalid CVV"
        
        return True, "Valid"
    
    def get_fee(self, amount: float) -> float:
        """Calculate credit card processing fee."""
        return amount * 0.029 + 0.30  # 2.9% + $0.30
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process credit card payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        # Simulate payment processing (95% success)
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
        return amount * 0.034 + 0.30  # 3.4% + $0.30
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process PayPal payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        # Simulate payment processing
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
        return amount * 0.01  # 1% fee
    
    def process_payment(self, amount: float, currency: str = "USD") -> PaymentResult:
        """Process cryptocurrency payment."""
        is_valid, message = self.validate()
        if not is_valid:
            return PaymentResult(False, "", message, amount)
        
        # Simulate crypto payment
        if random.random() < 0.97:
            transaction_id = f"CRYPTO-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            fee = self.get_fee(amount)
            return PaymentResult(True, transaction_id,
                               f"Crypto payment confirmed. Fee: ${fee:.2f}", amount)
        else:
            return PaymentResult(False, "", "Transaction failed - network error", amount)


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
        
        # Simulate bank transfer
        if random.random() < 0.98:
            transaction_id = f"BT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            fee = self.get_fee(amount)
            return PaymentResult(True, transaction_id,
                               f"Bank transfer initiated. Fee: ${fee:.2f}", amount)
        else:
            return PaymentResult(False, "", "Bank transfer failed", amount)


class PaymentProcessor:
    """
    Payment processor that handles different payment methods.
    
    Design Pattern: Strategy Pattern - Different payment strategies
    """
    
    def __init__(self):
        self.transaction_history: List[PaymentResult] = []
    
    def process_payment(self, payment_method: PaymentMethod, amount: float, 
                       currency: str = "USD") -> PaymentResult:
        """Process a payment using the given method."""
        print(f"  Processing ${amount:.2f} via {payment_method.method_name}...")
        
        result = payment_method.process_payment(amount, currency)
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
            lines.append(f"  {tx.timestamp.strftime('%Y-%m-%d %H:%M:%S')}: ${tx.amount:.2f} - {tx.message}")
        
        lines.append("-" * 60)
        lines.append(f"Total Processed: ${self.get_total_processed():,.2f}")
        lines.append(f"Success Rate: {self.get_success_rate():.1f}%")
        lines.append("=" * 60)
        
        return "\n".join(lines)


def demonstrate_payment_system():
    """
    Demonstrate the payment processing system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: PAYMENT PROCESSING SYSTEM")
    print("=" * 60)
    
    processor = PaymentProcessor()
    
    print("\n1. CREDIT CARD PAYMENT")
    print("-" * 40)
    
    cc = CreditCard("4111111111111111", 12, 2026, "123")
    result = processor.process_payment(cc, 299.99)
    print(f"  {result}")
    
    print("\n2. PAYPAL PAYMENT")
    print("-" * 40)
    
    pp = PayPal("customer@example.com")
    result = processor.process_payment(pp, 149.99)
    print(f"  {result}")
    
    print("\n3. CRYPTO PAYMENT")
    print("-" * 40)
    
    crypto = CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "BTC")
    result = processor.process_payment(crypto, 89.99)
    print(f"  {result}")
    
    print("\n4. BANK TRANSFER")
    print("-" * 40)
    
    bank = BankTransfer("12345678", "123456789", "Alice Chen")
    result = processor.process_payment(bank, 500.00)
    print(f"  {result}")
    
    print("\n5. INVALID PAYMENT ATTEMPT")
    print("-" * 40)
    
    invalid_cc = CreditCard("1234", 1, 2020, "12")
    result = processor.process_payment(invalid_cc, 100.00)
    print(f"  {result}")
    
    print("\n6. PAYMENT STATISTICS")
    print("-" * 40)
    
    print(f"  Total Processed: ${processor.get_total_processed():,.2f}")
    print(f"  Success Rate: {processor.get_success_rate():.1f}%")
    
    print("\n7. TRANSACTION HISTORY")
    print("-" * 40)
    
    print(processor.get_transaction_summary())
    
    print("\n8. FEE COMPARISON")
    print("-" * 40)
    
    amount = 100.00
    methods = [
        ("Credit Card", CreditCard("4111111111111111", 12, 2026, "123")),
        ("PayPal", PayPal("user@example.com")),
        ("Crypto", CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")),
        ("Bank Transfer", BankTransfer("12345678", "123456789", "Test"))
    ]
    
    for name, method in methods:
        fee = method.get_fee(amount)
        print(f"  {name}: ${fee:.2f} fee on ${amount:.2f}")


if __name__ == "__main__":
    demonstrate_payment_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Inheritance Basics** – Child class inherits from parent using `class Child(Parent):`. Gets all parent attributes and methods.

- **Method Overriding** – Child can override parent methods by defining same name. Use `super()` to call parent method.

- **super() Function** – Calls parent class methods. Essential for proper constructor chaining. Avoids hardcoding parent class names.

- **Multiple Inheritance** – Class can inherit from multiple parents. Python uses Method Resolution Order (MRO) to determine method lookup.

- **Abstract Base Classes (ABC)** – Use `ABC` and `@abstractmethod` to create interfaces. Cannot instantiate abstract classes.

- **Liskov Substitution Principle** – Derived classes must be substitutable for base classes. All vehicles can be used as Vehicle.

- **Open/Closed Principle** – Classes open for extension, closed for modification. New vehicle types don't require changes to existing code.

- **Vehicle Fleet System** – Base Vehicle class with Car, Truck, Motorcycle, SUV, ElectricCar. Fleet management with rentals and maintenance.

- **Employee Hierarchy** – Base Employee with Engineer, SalesPerson, Manager, Executive. Salary calculation with different formulas.

- **Payment Processing** – Base PaymentMethod with CreditCard, PayPal, CryptoPayment, BankTransfer. Different fee structures.

- **Design Patterns Used** – Template Method Pattern (base class defines structure), Strategy Pattern (payment strategies), Factory Pattern (creating objects), Composite Pattern (department contains employees), Repository Pattern (fleet storage).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Constructor – Building Objects

- **📚 Series D Catalog:** Object-Oriented Programming Line – View all 6 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Polymorphism – One Interface, Many Forms (Series D, Story 4)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 3 | 3 | 50% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **26** | **26** | **50%** |

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

**Next Story:** Series D, Story 4: The 2026 Python Metromap: Polymorphism – One Interface, Many Forms

---

## 📝 Your Invitation

You've mastered inheritance. Now build something with what you've learned:

1. **Build a shape library** – Create Shape base class with Circle, Rectangle, Triangle. Calculate area and perimeter.

2. **Create a media player hierarchy** – MediaPlayer base with AudioPlayer, VideoPlayer, StreamingPlayer.

3. **Build a document system** – Document base with TextDocument, Spreadsheet, Presentation. Save, load, export methods.

4. **Create a game character system** – Character base with Warrior, Mage, Archer, Healer. Attack, defend, special abilities.

5. **Build a notification system** – Notifier base with EmailNotifier, SMSNotifier, PushNotifier.

**You've mastered inheritance. Next stop: Polymorphism!**

---

*Found this helpful? Clap, comment, and share what you built with inheritance. Next stop: Polymorphism!* 🚇