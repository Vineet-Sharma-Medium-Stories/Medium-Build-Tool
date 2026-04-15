# The 2026 Python Metromap: Control Flow – if, elif, else

## Series A: Foundations Station | Story 4 of 7

![The 2026 Python Metromap/images/Control Flow – if, elif, else](images/Control Flow – if, elif, else.png)

## 📖 Introduction

**Welcome to the fourth stop on the Foundations Station Line.**

You've mastered variables, collections, and operators. You can store data, transform it, and compare values. But storing and transforming data is only useful if you can make decisions based on that data. Should this order get free shipping? Is this customer eligible for a discount? Which support team should handle this ticket?

Control flow is the branch in the tracks—the mechanism that lets your code choose different paths based on conditions. The if statement checks a condition and runs code only when that condition is True. elif (else if) checks additional conditions. else runs code when no conditions are met.

This story—**The 2026 Python Metromap: Control Flow – if, elif, else**—is your guide to decision-making in Python. We'll build a complete grade calculator that converts numeric scores to letter grades. We'll create a shipping cost estimator that handles multiple zones and weights. We'll build a customer support ticket routing system that directs issues to the right team. And we'll implement an order processing system with complex business rules.

**Let's make some decisions.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories)

- 🔧 **The 2026 Python Metromap: Variables & Data Types – The Rails of Python** – Integers, floats, strings, booleans; storing customer orders; type conversion; input/output operations.

- 🏗️ **The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets** – Shopping carts with lists; user profiles with dictionaries; analytics with sets; configuration with tuples.

- 📦 **The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More** – Building a discount engine; age verification; loan approval calculator.

- 🚦 **The 2026 Python Metromap: Control Flow – if, elif, else** – Grade calculator; shipping cost estimator; customer support ticket routing. **⬅️ YOU ARE HERE**

- 🔁 **The 2026 Python Metromap: Loops – for, while, break, continue** – Batch file processor; API retry mechanism; pagination system. 🔜 *Up Next*

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter.

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🚦 Section 1: The if Statement – Making Basic Decisions

The if statement is the foundation of control flow. It checks a condition and executes code only when that condition is True.

**SOLID Principle Applied: Single Responsibility** – Each if statement evaluates exactly one condition and executes one block of code.

**Design Pattern: Guard Clause Pattern** – if statements at the beginning of functions check for invalid conditions and return early.

```python
"""
THE IF STATEMENT: MAKING BASIC DECISIONS

This section covers the fundamental if statement and its syntax.

SOLID Principle: Single Responsibility
- Each if statement evaluates one condition

Design Pattern: Guard Clause Pattern
- Early returns for invalid conditions
"""

from typing import Any, Dict, List, Optional
from datetime import datetime


def demonstrate_if_basics():
    """
    Demonstrates basic if statement syntax and usage.
    
    The if statement checks a condition and executes the indented block
    only when the condition evaluates to True.
    """
    print("=" * 60)
    print("SECTION 1A: IF STATEMENT BASICS")
    print("=" * 60)
    
    # BASIC IF STATEMENT
    print("\n1. BASIC IF STATEMENT")
    print("-" * 40)
    
    temperature = 25
    
    if temperature > 20:
        print(f"  Temperature {temperature}°C is warm")
    
    # IF WITH FALSE CONDITION (nothing prints)
    temperature = 15
    if temperature > 20:
        print(f"  This won't print because {temperature} is not > 20")
    
    # IF WITH BOOLEAN
    print("\n2. IF WITH BOOLEAN VALUES")
    print("-" * 40)
    
    is_authenticated = True
    if is_authenticated:
        print("  User is authenticated - granting access")
    
    is_admin = False
    if is_admin:
        print("  This won't print because is_admin is False")
    
    # IF WITH COMPARISON OPERATORS
    print("\n3. IF WITH COMPARISON OPERATORS")
    print("-" * 40)
    
    age = 18
    
    if age >= 18:
        print(f"  Age {age} - eligible to vote")
    
    if age == 18:
        print(f"  Age {age} - exactly voting age")
    
    if age != 21:
        print(f"  Age {age} - not 21 yet")
    
    # IF WITH LOGICAL OPERATORS
    print("\n4. IF WITH LOGICAL OPERATORS")
    print("-" * 40)
    
    has_license = True
    has_insurance = True
    age = 25
    
    # AND - both must be True
    if has_license and has_insurance:
        print("  Can drive: has license AND insurance")
    
    # OR - at least one must be True
    is_member = False
    has_coupon = True
    
    if is_member or has_coupon:
        print("  Eligible for discount: member OR has coupon")
    
    # NOT - negates the condition
    is_blocked = False
    if not is_blocked:
        print("  User is not blocked - access granted")
    
    # IF WITH TRUTHY VALUES
    print("\n5. IF WITH TRUTHY VALUES")
    print("-" * 40)
    
    # Non-empty strings are truthy
    name = "Alice"
    if name:
        print(f"  Name provided: {name}")
    
    # Empty strings are falsy
    name = ""
    if not name:
        print("  No name provided")
    
    # Non-zero numbers are truthy
    quantity = 5
    if quantity:
        print(f"  Quantity: {quantity} items")
    
    # Zero is falsy
    quantity = 0
    if not quantity:
        print("  Quantity is zero")
    
    # Non-empty lists are truthy
    items = ["apple", "banana"]
    if items:
        print(f"  Cart has {len(items)} items")
    
    # Empty lists are falsy
    items = []
    if not items:
        print("  Cart is empty")
    
    # None is falsy
    user = None
    if user is None:
        print("  User not found")
    
    # IF STATEMENT INDENTATION (CRITICAL!)
    print("\n6. IF STATEMENT INDENTATION (IMPORTANT!)")
    print("-" * 40)
    
    score = 85
    
    if score >= 60:
        print("  This line is inside the if block")
        print("  This line is also inside the if block")
    print("  This line is OUTSIDE the if block (always runs)")
    
    # Indentation determines what code is conditional
    print("\n  Correct indentation is critical in Python!")
    print("  Use 4 spaces for each indentation level.")


def demonstrate_guard_clauses():
    """
    Demonstrates guard clauses for early returns.
    
    Guard clauses check invalid conditions at the beginning of functions
    and return early, reducing nesting and improving readability.
    
    Design Pattern: Guard Clause Pattern
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: GUARD CLAUSES")
    print("=" * 60)
    
    # WITHOUT GUARD CLAUSES (Nested and hard to read)
    print("\n1. WITHOUT GUARD CLAUSES (Bad)")
    print("-" * 40)
    
    def process_order_bad(order: Dict) -> str:
        """Process order with nested conditions."""
        if order:
            if order.get("items"):
                if order.get("payment_method"):
                    if order.get("shipping_address"):
                        return "Order processed"
                    else:
                        return "Missing shipping address"
                else:
                    return "Missing payment method"
            else:
                return "No items in order"
        else:
            return "No order provided"
    
    result = process_order_bad({"items": [1, 2], "payment_method": "card", "shipping_address": "123 Main St"})
    print(f"Result: {result}")
    
    # WITH GUARD CLAUSES (Clean and readable)
    print("\n2. WITH GUARD CLAUSES (Good)")
    print("-" * 40)
    
    def process_order_good(order: Dict) -> str:
        """Process order with guard clauses."""
        # Guard clauses - check invalid conditions first
        if not order:
            return "No order provided"
        
        if not order.get("items"):
            return "No items in order"
        
        if not order.get("payment_method"):
            return "Missing payment method"
        
        if not order.get("shipping_address"):
            return "Missing shipping address"
        
        # Happy path - all checks passed
        return "Order processed"
    
    result = process_order_good({"items": [1, 2], "payment_method": "card", "shipping_address": "123 Main St"})
    print(f"Result: {result}")
    
    # More guard clause examples
    print("\n3. MORE GUARD CLAUSE EXAMPLES")
    print("-" * 40)
    
    def calculate_discount(price: float, quantity: int, customer_tier: str) -> float:
        """
        Calculate discount with guard clauses.
        
        Guard clauses handle invalid inputs before business logic.
        """
        # Guard clauses - validate inputs
        if price <= 0:
            return 0.0
        
        if quantity <= 0:
            return 0.0
        
        if customer_tier not in ["bronze", "silver", "gold", "platinum"]:
            return 0.0
        
        # Business logic - only runs for valid inputs
        tier_discounts = {
            "bronze": 0.00,
            "silver": 0.05,
            "gold": 0.10,
            "platinum": 0.15
        }
        
        discount_rate = tier_discounts.get(customer_tier, 0.00)
        
        # Bulk discount for large quantities
        if quantity >= 10:
            discount_rate += 0.05
        
        # Maximum discount cap
        discount_rate = min(discount_rate, 0.25)
        
        return price * quantity * discount_rate
    
    # Test guard clauses
    test_cases = [
        (100, 2, "gold", "Valid order"),
        (-50, 2, "gold", "Invalid price"),
        (100, 0, "gold", "Invalid quantity"),
        (100, 2, "invalid", "Invalid tier"),
    ]
    
    for price, qty, tier, description in test_cases:
        discount = calculate_discount(price, qty, tier)
        print(f"  {description}: ${price} × {qty} ({tier}) → discount ${discount:.2f}")
    
    # REAL-WORLD: API Request Validation
    print("\n4. REAL-WORLD: API REQUEST VALIDATION")
    print("-" * 40)
    
    def validate_api_request(request: Dict) -> tuple:
        """
        Validate API request with guard clauses.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Required fields
        required_fields = ["user_id", "action", "timestamp"]
        
        for field in required_fields:
            if field not in request:
                return False, f"Missing required field: {field}"
        
        # Type validation
        if not isinstance(request["user_id"], str):
            return False, "user_id must be a string"
        
        if not isinstance(request["action"], str):
            return False, "action must be a string"
        
        # Value validation
        if len(request["user_id"]) < 3:
            return False, "user_id too short (minimum 3 characters)"
        
        valid_actions = ["create", "read", "update", "delete"]
        if request["action"] not in valid_actions:
            return False, f"Invalid action. Must be one of: {valid_actions}"
        
        # All validations passed
        return True, "Request valid"
    
    # Test requests
    test_requests = [
        {"user_id": "user123", "action": "read", "timestamp": "2024-01-01"},
        {"user_id": "a", "action": "read", "timestamp": "2024-01-01"},
        {"user_id": "user123", "action": "invalid", "timestamp": "2024-01-01"},
        {"user_id": "user123", "timestamp": "2024-01-01"},
    ]
    
    for req in test_requests:
        is_valid, message = validate_api_request(req)
        status = "✅" if is_valid else "❌"
        print(f"{status} {message}")


def build_temperature_advisor():
    """
    Builds a temperature-based clothing advisor using if statements.
    
    This demonstrates a real-world decision system that provides
    recommendations based on temperature conditions.
    
    SOLID Principles Applied:
    - Single Responsibility: Each condition handles one temperature range
    
    Design Pattern: Chain of Responsibility - Checks conditions in order
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: TEMPERATURE ADVISOR SYSTEM")
    print("=" * 60)
    
    from typing import Dict, List, Tuple
    
    class TemperatureAdvisor:
        """
        Provides clothing and activity recommendations based on temperature.
        
        Design Pattern: Chain of Responsibility - Checks temperature ranges in order
        """
        
        def __init__(self):
            # Define temperature thresholds and recommendations
            self.temperature_zones = [
                (-float('inf'), -10, "Extreme Cold", "🧥 Bundle up! Wear heavy coat, hat, gloves, scarf, and thermal layers. Limit outdoor exposure."),
                (-10, 0, "Very Cold", "🧣 Wear heavy coat, warm hat, gloves, and scarf. Consider thermal underwear."),
                (0, 10, "Cold", "🧥 Wear warm coat, hat, and gloves. A scarf is recommended."),
                (10, 15, "Cool", "🧥 Wear a jacket or light coat. Long sleeves recommended."),
                (15, 20, "Mild", "👕 Light jacket or sweater. Comfortable for outdoor activities."),
                (20, 25, "Warm", "👕 T-shirt weather. Light jacket for evenings."),
                (25, 30, "Hot", "🩳 Shorts and t-shirt. Wear sunscreen and stay hydrated."),
                (30, float('inf'), "Extreme Heat", "🩳 Light clothing only. Avoid midday sun. Stay indoors if possible.")
            ]
        
        def get_recommendation(self, temperature: float, unit: str = "C") -> Dict:
            """
            Get clothing and activity recommendations for a temperature.
            
            Args:
                temperature: Temperature value
                unit: Temperature unit ('C' for Celsius, 'F' for Fahrenheit)
                
            Returns:
                Dictionary with recommendations
            """
            # Convert Fahrenheit to Celsius if needed
            if unit.upper() == "F":
                celsius = (temperature - 32) * 5/9
            else:
                celsius = temperature
            
            # Find matching temperature zone
            for min_temp, max_temp, zone_name, advice in self.temperature_zones:
                if min_temp <= celsius < max_temp:
                    return {
                        "temperature_celsius": round(celsius, 1),
                        "temperature_fahrenheit": round(celsius * 9/5 + 32, 1),
                        "zone": zone_name,
                        "clothing_advice": advice,
                        "is_extreme": zone_name in ["Extreme Cold", "Extreme Heat"]
                    }
            
            # Fallback (should never reach here)
            return {
                "temperature_celsius": round(celsius, 1),
                "temperature_fahrenheit": round(celsius * 9/5 + 32, 1),
                "zone": "Unknown",
                "clothing_advice": "Check weather forecast for accurate information.",
                "is_extreme": False
            }
        
        def get_activity_suitability(self, temperature: float) -> Dict:
            """Get suitability ratings for various activities."""
            temp = temperature
            
            activities = {
                "Running": temp > 5 and temp < 25,
                "Swimming": temp > 20 and temp < 35,
                "Hiking": temp > 0 and temp < 30,
                "Skiing": temp < 5,
                "Cycling": temp > 5 and temp < 30,
                "Picnic": temp > 15 and temp < 28,
                "Beach": temp > 22 and temp < 35,
                "Camping": temp > 5 and temp < 25
            }
            
            return activities
    
    # DEMONSTRATION
    print("\n🌡️ DEMONSTRATION: TEMPERATURE ADVISOR")
    print("-" * 40)
    
    advisor = TemperatureAdvisor()
    
    # Test various temperatures
    test_temperatures = [-15, -5, 5, 12, 18, 22, 28, 35, 100]
    
    for temp in test_temperatures:
        print(f"\n{'='*40}")
        recommendation = advisor.get_recommendation(temp)
        
        print(f"Temperature: {recommendation['temperature_fahrenheit']:.1f}°F / {recommendation['temperature_celsius']:.1f}°C")
        print(f"Zone: {recommendation['zone']}")
        print(f"Advice: {recommendation['clothing_advice']}")
        
        if recommendation['is_extreme']:
            print("⚠️ EXTREME WEATHER ALERT: Take precautions!")
        
        # Show activity suitability
        activities = advisor.get_activity_suitability(temp)
        suitable = [act for act, suitable in activities.items() if suitable]
        if suitable:
            print(f"Suitable activities: {', '.join(suitable)}")


if __name__ == "__main__":
    demonstrate_if_basics()
    demonstrate_guard_clauses()
    build_temperature_advisor()
```

---

## 🔀 Section 2: The if-else Statement – Two Paths

The if-else statement provides two paths: one when the condition is True, another when it's False.

**SOLID Principle Applied: Open/Closed** – The if-else structure is closed for modification but open for extension with additional elif clauses.

**Design Pattern: Strategy Pattern** – Different code paths represent different strategies for handling conditions.

```python
"""
THE IF-ELSE STATEMENT: TWO PATHS

This section covers the if-else statement for binary decisions.

SOLID Principle: Open/Closed
- if-else structure can be extended with elif

Design Pattern: Strategy Pattern
- Different paths represent different strategies
"""

from typing import Dict, Any, Optional, Tuple
from datetime import datetime


def demonstrate_if_else():
    """
    Demonstrates if-else statement for binary decisions.
    
    if-else provides two execution paths: one for True, one for False.
    """
    print("=" * 60)
    print("SECTION 2A: IF-ELSE STATEMENT")
    print("=" * 60)
    
    # BASIC IF-ELSE
    print("\n1. BASIC IF-ELSE")
    print("-" * 40)
    
    age = 16
    
    if age >= 18:
        print(f"  Age {age}: Eligible to vote")
    else:
        print(f"  Age {age}: Not eligible to vote (need to be 18)")
    
    # IF-ELSE WITH COMPARISONS
    print("\n2. IF-ELSE WITH COMPARISONS")
    print("-" * 40)
    
    score = 65
    
    if score >= 60:
        print(f"  Score {score}: PASS")
    else:
        print(f"  Score {score}: FAIL")
    
    # IF-ELSE WITH LOGICAL OPERATORS
    print("\n3. IF-ELSE WITH LOGICAL OPERATORS")
    print("-" * 40)
    
    is_weekend = True
    is_holiday = False
    
    if is_weekend or is_holiday:
        print("  Day off! No work today.")
    else:
        print("  Regular work day")
    
    # IF-ELSE WITH TERNARY OPERATOR (Conditional Expression)
    print("\n4. TERNARY OPERATOR (Conditional Expression)")
    print("-" * 40)
    
    # Long form
    age = 20
    if age >= 18:
        status = "adult"
    else:
        status = "minor"
    print(f"  Long form: Age {age} → {status}")
    
    # Ternary operator (shorthand)
    status = "adult" if age >= 18 else "minor"
    print(f"  Ternary: Age {age} → {status}")
    
    # More ternary examples
    score = 85
    grade = "Pass" if score >= 60 else "Fail"
    print(f"  Score {score} → {grade}")
    
    # Nested ternary (use sparingly - can be hard to read)
    value = 0
    result = "positive" if value > 0 else "negative" if value < 0 else "zero"
    print(f"  Value {value} → {result}")
    
    # IF-ELSE FOR VALIDATION
    print("\n5. IF-ELSE FOR INPUT VALIDATION")
    print("-" * 40)
    
    def validate_age(age_str: str) -> Tuple[bool, Optional[int], str]:
        """Validate age input and return parsed age or error."""
        if not age_str:
            return False, None, "Age cannot be empty"
        
        if not age_str.isdigit():
            return False, None, "Age must be a number"
        
        age = int(age_str)
        
        if age < 0:
            return False, None, "Age cannot be negative"
        
        if age > 150:
            return False, None, "Age seems unrealistic (max 150)"
        
        return True, age, "Valid age"
    
    test_inputs = ["", "abc", "-5", "25", "200"]
    
    for input_str in test_inputs:
        is_valid, age, message = validate_age(input_str)
        if is_valid:
            print(f"  '{input_str}' → Valid: {message} (age={age})")
        else:
            print(f"  '{input_str}' → Invalid: {message}")
    
    # PRACTICAL: DISCOUNT ELIGIBILITY
    print("\n6. PRACTICAL: DISCOUNT ELIGIBILITY")
    print("-" * 40)
    
    def check_discount_eligibility(purchase_amount: float, is_member: bool, is_first_purchase: bool) -> Dict:
        """Determine discount eligibility and amount."""
        result = {
            "eligible": False,
            "discount_percent": 0,
            "message": ""
        }
        
        if is_first_purchase:
            result["eligible"] = True
            result["discount_percent"] = 15
            result["message"] = "Welcome discount!"
        elif is_member and purchase_amount >= 50:
            result["eligible"] = True
            result["discount_percent"] = 10
            result["message"] = "Member discount!"
        elif purchase_amount >= 100:
            result["eligible"] = True
            result["discount_percent"] = 5
            result["message"] = "Volume discount!"
        else:
            result["message"] = "No discount available"
        
        return result
    
    test_cases = [
        (25, False, False, "Small purchase, non-member"),
        (75, False, False, "Medium purchase, non-member"),
        (75, True, False, "Medium purchase, member"),
        (50, False, True, "First purchase"),
        (150, False, False, "Large purchase, non-member"),
    ]
    
    for amount, member, first, description in test_cases:
        result = check_discount_eligibility(amount, member, first)
        print(f"  {description}: ${amount} → {result['message']} ({result['discount_percent']}% off)")


def build_grade_calculator():
    """
    Complete grade calculator using if-elif-else statements.
    
    This demonstrates a real-world grading system that converts
    numeric scores to letter grades with plus/minus modifiers.
    
    SOLID Principles Applied:
    - Single Responsibility: Each grade range has one handler
    - Open/Closed: New grade ranges can be added
    
    Design Pattern: Chain of Responsibility - Checks grade ranges in order
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: GRADE CALCULATOR SYSTEM")
    print("=" * 60)
    
    from typing import Dict, List, Tuple, Optional
    from enum import Enum
    from dataclasses import dataclass
    
    class GradeScale(Enum):
        """Grading scale types."""
        STANDARD = "standard"      # 90-100 A, 80-89 B, etc.
        PASS_FAIL = "pass_fail"    # 60+ Pass, below 60 Fail
        LETTER_ONLY = "letter"     # A, B, C, D, F (no plus/minus)
    
    @dataclass
    class GradeResult:
        """Result of grade calculation."""
        numeric_score: float
        letter_grade: str
        grade_points: float
        is_passing: bool
        feedback: str
    
    class GradeCalculator:
        """
        Calculates letter grades from numeric scores.
        
        Design Pattern: Chain of Responsibility - Checks score ranges in order
        """
        
        def __init__(self, scale: GradeScale = GradeScale.STANDARD):
            self.scale = scale
        
        def calculate(self, score: float, max_score: float = 100.0) -> GradeResult:
            """
            Calculate grade from numeric score.
            
            Args:
                score: Student's score (points earned)
                max_score: Maximum possible score
                
            Returns:
                GradeResult with grade details
            """
            # Guard clauses
            if score < 0:
                return GradeResult(score, "INVALID", 0.0, False, "Score cannot be negative")
            
            if score > max_score:
                return GradeResult(score, "INVALID", 0.0, False, f"Score exceeds maximum ({max_score})")
            
            # Calculate percentage
            percentage = (score / max_score) * 100
            
            # Determine grade based on scale
            if self.scale == GradeScale.PASS_FAIL:
                return self._calculate_pass_fail(percentage, score, max_score)
            elif self.scale == GradeScale.LETTER_ONLY:
                return self._calculate_letter_only(percentage, score, max_score)
            else:
                return self._calculate_standard(percentage, score, max_score)
        
        def _calculate_standard(self, percentage: float, score: float, max_score: float) -> GradeResult:
            """Standard grading with plus/minus modifiers."""
            # Determine base letter grade
            if percentage >= 90:
                base_grade = "A"
                grade_points = 4.0
                feedback = "Excellent work!"
            elif percentage >= 80:
                base_grade = "B"
                grade_points = 3.0
                feedback = "Good work!"
            elif percentage >= 70:
                base_grade = "C"
                grade_points = 2.0
                feedback = "Satisfactory"
            elif percentage >= 60:
                base_grade = "D"
                grade_points = 1.0
                feedback = "Needs improvement"
            else:
                base_grade = "F"
                grade_points = 0.0
                feedback = "Failing. Please seek help."
            
            # Add plus/minus modifiers (except for F and A+ doesn't exist at most schools)
            if base_grade != "F" and base_grade != "A":
                # Get the last digit of percentage for plus/minus
                last_digit = percentage % 10
                
                if last_digit >= 7:
                    modifier = "+"
                    grade_points += 0.33
                elif last_digit <= 3:
                    modifier = "-"
                    grade_points -= 0.33
                else:
                    modifier = ""
            else:
                modifier = ""
            
            letter_grade = f"{base_grade}{modifier}"
            
            # Round grade points to 2 decimal places
            grade_points = round(grade_points, 2)
            
            return GradeResult(
                numeric_score=score,
                letter_grade=letter_grade,
                grade_points=grade_points,
                is_passing=percentage >= 60,
                feedback=feedback
            )
        
        def _calculate_pass_fail(self, percentage: float, score: float, max_score: float) -> GradeResult:
            """Pass/Fail grading."""
            is_passing = percentage >= 60
            return GradeResult(
                numeric_score=score,
                letter_grade="PASS" if is_passing else "FAIL",
                grade_points=1.0 if is_passing else 0.0,
                is_passing=is_passing,
                feedback="Pass" if is_passing else "Fail. Please retake the course."
            )
        
        def _calculate_letter_only(self, percentage: float, score: float, max_score: float) -> GradeResult:
            """Letter only grading (no plus/minus)."""
            if percentage >= 90:
                letter_grade = "A"
                grade_points = 4.0
                feedback = "Excellent!"
            elif percentage >= 80:
                letter_grade = "B"
                grade_points = 3.0
                feedback = "Good!"
            elif percentage >= 70:
                letter_grade = "C"
                grade_points = 2.0
                feedback = "Satisfactory"
            elif percentage >= 60:
                letter_grade = "D"
                grade_points = 1.0
                feedback = "Needs improvement"
            else:
                letter_grade = "F"
                grade_points = 0.0
                feedback = "Failing"
            
            return GradeResult(
                numeric_score=score,
                letter_grade=letter_grade,
                grade_points=grade_points,
                is_passing=percentage >= 60,
                feedback=feedback
            )
        
        def calculate_class_stats(self, grades: List[GradeResult]) -> Dict:
            """Calculate statistics for a list of grades."""
            if not grades:
                return {"error": "No grades provided"}
            
            numeric_scores = [g.numeric_score for g in grades]
            grade_points = [g.grade_points for g in grades]
            
            # Calculate statistics
            average_score = sum(numeric_scores) / len(numeric_scores)
            average_gpa = sum(grade_points) / len(grade_points)
            passing_count = sum(1 for g in grades if g.is_passing)
            
            # Grade distribution
            distribution = {}
            for grade in grades:
                # Get base letter (first character for A-F)
                base = grade.letter_grade[0] if grade.letter_grade[0] in "ABCDEF" else grade.letter_grade
                distribution[base] = distribution.get(base, 0) + 1
            
            return {
                "total_students": len(grades),
                "average_score": round(average_score, 1),
                "average_gpa": round(average_gpa, 2),
                "passing_rate": round((passing_count / len(grades)) * 100, 1),
                "grade_distribution": distribution,
                "highest_score": max(numeric_scores),
                "lowest_score": min(numeric_scores)
            }
    
    # DEMONSTRATION
    print("\n📊 DEMONSTRATION: GRADE CALCULATOR")
    print("-" * 40)
    
    calculator = GradeCalculator(GradeScale.STANDARD)
    
    # Test various scores
    test_scores = [98, 85, 77, 72, 68, 55, 42, 101, -5]
    
    print("\nINDIVIDUAL GRADE CALCULATIONS:")
    print("=" * 60)
    
    for score in test_scores:
        result = calculator.calculate(score)
        print(f"\nScore: {result.numeric_score}/100")
        print(f"  Letter Grade: {result.letter_grade}")
        print(f"  Grade Points: {result.grade_points}")
        print(f"  Passing: {result.is_passing}")
        print(f"  Feedback: {result.feedback}")
    
    # Class statistics
    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)
    
    class_grades = [
        calculator.calculate(95),
        calculator.calculate(87),
        calculator.calculate(78),
        calculator.calculate(92),
        calculator.calculate(64),
        calculator.calculate(71),
        calculator.calculate(88),
        calculator.calculate(55),
        calculator.calculate(93),
        calculator.calculate(81)
    ]
    
    stats = calculator.calculate_class_stats(class_grades)
    
    print(f"\nTotal Students: {stats['total_students']}")
    print(f"Average Score: {stats['average_score']}")
    print(f"Average GPA: {stats['average_gpa']}")
    print(f"Passing Rate: {stats['passing_rate']}%")
    print(f"Highest Score: {stats['highest_score']}")
    print(f"Lowest Score: {stats['lowest_score']}")
    
    print("\nGrade Distribution:")
    for grade, count in sorted(stats['grade_distribution'].items()):
        bar = "█" * count
        print(f"  {grade}: {bar} ({count} students)")
    
    # Compare grading scales
    print("\n" + "=" * 60)
    print("GRADING SCALE COMPARISON")
    print("=" * 60)
    
    score = 82
    
    for scale in GradeScale:
        calc = GradeCalculator(scale)
        result = calc.calculate(score)
        print(f"\n{scale.value.upper()}:")
        print(f"  Score: {result.numeric_score}/100")
        print(f"  Grade: {result.letter_grade}")
        print(f"  GPA: {result.grade_points}")
        print(f"  Feedback: {result.feedback}")


if __name__ == "__main__":
    demonstrate_if_else()
    build_grade_calculator()
```

---

## 🔀 Section 3: The if-elif-else Chain – Multiple Paths

The if-elif-else chain handles multiple mutually exclusive conditions. Each condition is checked in order until one is True.

**SOLID Principle Applied: Open/Closed** – New conditions can be added by adding new elif clauses without modifying existing ones.

**Design Pattern: Chain of Responsibility** – Each condition in the chain has a chance to handle the request.

```python
"""
THE IF-ELIF-ELSE CHAIN: MULTIPLE PATHS

This section covers if-elif-else chains for multiple conditions.

SOLID Principle: Open/Closed
- New conditions can be added with new elif clauses

Design Pattern: Chain of Responsibility
- Each condition in the chain has a chance to handle the request
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from datetime import datetime


def demonstrate_if_elif_else():
    """
    Demonstrates if-elif-else chains for multiple conditions.
    
    if-elif-else checks conditions in order until one is True.
    Only the first matching block executes.
    """
    print("=" * 60)
    print("SECTION 3A: IF-ELIF-ELSE CHAINS")
    print("=" * 60)
    
    # BASIC IF-ELIF-ELSE
    print("\n1. BASIC IF-ELIF-ELSE")
    print("-" * 40)
    
    score = 85
    
    if score >= 90:
        print(f"  Score {score}: A")
    elif score >= 80:
        print(f"  Score {score}: B")
    elif score >= 70:
        print(f"  Score {score}: C")
    elif score >= 60:
        print(f"  Score {score}: D")
    else:
        print(f"  Score {score}: F")
    
    # IMPORTANT: Order matters!
    print("\n2. ORDER MATTERS (Wrong Order)")
    print("-" * 40)
    
    # Wrong order - first condition catches everything
    score = 85
    
    if score >= 60:
        print(f"  Score {score}: D or better (but we wanted A/B/C/D logic)")
    elif score >= 70:
        print("  This will never run because first condition was True")
    
    # Correct order - most specific first
    print("\n  Always put most specific conditions first, general conditions last.")
    
    # MULTIPLE CONDITIONS PER BRANCH
    print("\n3. MULTIPLE CONDITIONS PER BRANCH")
    print("-" * 40)
    
    age = 25
    income = 50000
    credit_score = 720
    
    if age >= 18 and income >= 30000 and credit_score >= 650:
        print("  Approved for standard credit card")
    elif age >= 18 and income >= 20000 and credit_score >= 600:
        print("  Approved for secured credit card")
    elif age >= 18:
        print("  Conditional approval with co-signer required")
    else:
        print("  Not approved - must be 18 or older")
    
    # PRACTICAL: SHIPPING COST CALCULATOR
    print("\n4. PRACTICAL: SHIPPING COST CALCULATOR")
    print("-" * 40)
    
    def calculate_shipping(weight_kg: float, destination: str, is_express: bool = False) -> Dict:
        """Calculate shipping cost based on weight, destination, and speed."""
        # Base rates by destination
        if destination == "domestic":
            base_rate = 5.00
        elif destination == "international":
            base_rate = 20.00
        elif destination == "remote":
            base_rate = 35.00
        else:
            return {"error": f"Unknown destination: {destination}"}
        
        # Weight tiers
        if weight_kg <= 0.5:
            weight_multiplier = 1.0
        elif weight_kg <= 1.0:
            weight_multiplier = 1.5
        elif weight_kg <= 5.0:
            weight_multiplier = 2.5
        elif weight_kg <= 10.0:
            weight_multiplier = 4.0
        else:
            weight_multiplier = 6.0
        
        # Calculate base cost
        cost = base_rate * weight_multiplier
        
        # Express shipping multiplier
        if is_express:
            if destination == "domestic":
                cost *= 2.0
            else:
                cost *= 1.5
        
        # Free shipping for large orders (over $100 base cost)
        if cost >= 100:
            return {
                "weight_kg": weight_kg,
                "destination": destination,
                "is_express": is_express,
                "original_cost": round(cost, 2),
                "final_cost": 0.00,
                "message": "Free shipping applied!"
            }
        
        return {
            "weight_kg": weight_kg,
            "destination": destination,
            "is_express": is_express,
            "original_cost": round(cost, 2),
            "final_cost": round(cost, 2),
            "message": "Standard rate applied"
        }
    
    # Test shipping calculator
    test_shipments = [
        (0.3, "domestic", False),
        (2.0, "domestic", False),
        (0.5, "international", False),
        (3.0, "international", True),
        (12.0, "domestic", False),
        (25.0, "international", True),
    ]
    
    for weight, dest, express in test_shipments:
        result = calculate_shipping(weight, dest, express)
        if "error" in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  {weight}kg to {dest} (express={express}): ${result['final_cost']} - {result['message']}")


def build_shipping_estimator():
    """
    Complete shipping cost estimator with multiple zones and rules.
    
    This demonstrates a real-world shipping calculator with
    multiple tiers, zones, and special conditions.
    
    SOLID Principles Applied:
    - Single Responsibility: Each shipping rule is separate
    - Open/Closed: New zones and rules can be added
    
    Design Pattern: Chain of Responsibility - Checks conditions in order
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: SHIPPING ESTIMATOR SYSTEM")
    print("=" * 60)
    
    from typing import Dict, List, Optional, Tuple
    from dataclasses import dataclass
    from enum import Enum
    
    class ShippingZone(Enum):
        """Shipping zones with different rates."""
        LOCAL = "local"
        REGIONAL = "regional"
        NATIONAL = "national"
        INTERNATIONAL = "international"
        REMOTE = "remote"
    
    class ShippingSpeed(Enum):
        """Shipping speed options."""
        STANDARD = "standard"
        EXPEDITED = "expedited"
        EXPRESS = "express"
        OVERNIGHT = "overnight"
    
    @dataclass
    class ShippingEstimate:
        """Result of shipping cost calculation."""
        zone: ShippingZone
        speed: ShippingSpeed
        weight_kg: float
        base_cost: float
        fuel_surcharge: float
        handling_fee: float
        total_cost: float
        estimated_days: int
        is_eligible_for_free_shipping: bool
        notes: List[str]
    
    class ShippingEstimator:
        """
        Calculates shipping costs based on multiple factors.
        
        Design Pattern: Chain of Responsibility - Each zone has its own calculator
        """
        
        def __init__(self):
            # Zone rate tables (cost per kg)
            self.zone_rates = {
                ShippingZone.LOCAL: 2.50,
                ShippingZone.REGIONAL: 4.00,
                ShippingZone.NATIONAL: 6.50,
                ShippingZone.INTERNATIONAL: 15.00,
                ShippingZone.REMOTE: 25.00
            }
            
            # Speed multipliers
            self.speed_multipliers = {
                ShippingSpeed.STANDARD: 1.0,
                ShippingSpeed.EXPEDITED: 1.5,
                ShippingSpeed.EXPRESS: 2.0,
                ShippingSpeed.OVERNIGHT: 3.0
            }
            
            # Estimated delivery days by zone and speed
            self.delivery_days = {
                (ShippingZone.LOCAL, ShippingSpeed.STANDARD): 2,
                (ShippingZone.LOCAL, ShippingSpeed.EXPEDITED): 1,
                (ShippingZone.LOCAL, ShippingSpeed.EXPRESS): 1,
                (ShippingZone.LOCAL, ShippingSpeed.OVERNIGHT): 1,
                (ShippingZone.REGIONAL, ShippingSpeed.STANDARD): 3,
                (ShippingZone.REGIONAL, ShippingSpeed.EXPEDITED): 2,
                (ShippingZone.REGIONAL, ShippingSpeed.EXPRESS): 1,
                (ShippingZone.REGIONAL, ShippingSpeed.OVERNIGHT): 1,
                (ShippingZone.NATIONAL, ShippingSpeed.STANDARD): 5,
                (ShippingZone.NATIONAL, ShippingSpeed.EXPEDITED): 3,
                (ShippingZone.NATIONAL, ShippingSpeed.EXPRESS): 2,
                (ShippingZone.NATIONAL, ShippingSpeed.OVERNIGHT): 1,
                (ShippingZone.INTERNATIONAL, ShippingSpeed.STANDARD): 10,
                (ShippingZone.INTERNATIONAL, ShippingSpeed.EXPEDITED): 7,
                (ShippingZone.INTERNATIONAL, ShippingSpeed.EXPRESS): 5,
                (ShippingZone.INTERNATIONAL, ShippingSpeed.OVERNIGHT): 3,
                (ShippingZone.REMOTE, ShippingSpeed.STANDARD): 8,
                (ShippingZone.REMOTE, ShippingSpeed.EXPEDITED): 5,
                (ShippingZone.REMOTE, ShippingSpeed.EXPRESS): 3,
                (ShippingZone.REMOTE, ShippingSpeed.OVERNIGHT): 2,
            }
        
        def determine_zone(self, postal_code: str, country: str) -> ShippingZone:
            """
            Determine shipping zone based on postal code and country.
            
            Design Pattern: Strategy Pattern - Zone determination strategy
            """
            # Local (same city - simplified)
            if postal_code.startswith("902") and country == "US":
                return ShippingZone.LOCAL
            
            # Regional (same region - simplified)
            if postal_code.startswith("90") and country == "US":
                return ShippingZone.REGIONAL
            
            # National (same country)
            if country == "US":
                return ShippingZone.NATIONAL
            
            # Remote (hard-to-reach areas)
            remote_areas = ["99950", "96799", "96898"]
            if postal_code in remote_areas:
                return ShippingZone.REMOTE
            
            # International
            if country != "US":
                return ShippingZone.INTERNATIONAL
            
            return ShippingZone.NATIONAL
        
        def calculate_fuel_surcharge(self, base_cost: float, zone: ShippingZone) -> float:
            """Calculate fuel surcharge based on zone."""
            if zone == ShippingZone.INTERNATIONAL:
                return base_cost * 0.15
            elif zone == ShippingZone.REMOTE:
                return base_cost * 0.20
            elif zone == ShippingZone.NATIONAL:
                return base_cost * 0.10
            else:
                return base_cost * 0.05
        
        def calculate_handling_fee(self, weight_kg: float) -> float:
            """Calculate handling fee based on weight."""
            if weight_kg <= 1:
                return 1.00
            elif weight_kg <= 5:
                return 2.50
            elif weight_kg <= 20:
                return 5.00
            else:
                return 10.00
        
        def check_free_shipping_eligibility(self, subtotal: float, zone: ShippingZone, is_member: bool) -> bool:
            """Check if order qualifies for free shipping."""
            # Free shipping for members over $50
            if is_member and subtotal >= 50:
                return True
            
            # Free shipping for large orders
            if subtotal >= 100:
                return True
            
            # Free shipping for local and regional zones over $35
            if zone in [ShippingZone.LOCAL, ShippingZone.REGIONAL] and subtotal >= 35:
                return True
            
            return False
        
        def estimate(self, weight_kg: float, postal_code: str, country: str,
                    speed: ShippingSpeed = ShippingSpeed.STANDARD,
                    order_subtotal: float = 0, is_member: bool = False) -> ShippingEstimate:
            """
            Calculate shipping cost estimate.
            
            Args:
                weight_kg: Package weight in kilograms
                postal_code: Destination postal code
                country: Destination country
                speed: Shipping speed preference
                order_subtotal: Order subtotal (for free shipping calculation)
                is_member: Whether customer is a loyalty member
                
            Returns:
                ShippingEstimate with cost breakdown
            """
            # Guard clauses
            if weight_kg <= 0:
                weight_kg = 0.1  # Minimum weight
            
            # Determine zone
            zone = self.determine_zone(postal_code, country)
            
            # Calculate base cost
            rate_per_kg = self.zone_rates[zone]
            base_cost = rate_per_kg * weight_kg
            
            # Apply speed multiplier
            multiplier = self.speed_multipliers[speed]
            base_cost *= multiplier
            
            # Calculate additional fees
            fuel_surcharge = self.calculate_fuel_surcharge(base_cost, zone)
            handling_fee = self.calculate_handling_fee(weight_kg)
            
            # Calculate total before free shipping
            total_before_free = base_cost + fuel_surcharge + handling_fee
            
            # Check free shipping eligibility
            free_shipping = self.check_free_shipping_eligibility(order_subtotal, zone, is_member)
            
            # Apply free shipping if eligible
            if free_shipping:
                total_cost = 0
                notes = ["Free shipping applied!"]
            else:
                total_cost = total_before_free
                notes = []
            
            # Get estimated delivery days
            estimated_days = self.delivery_days.get((zone, speed), 5)
            
            return ShippingEstimate(
                zone=zone,
                speed=speed,
                weight_kg=weight_kg,
                base_cost=round(base_cost, 2),
                fuel_surcharge=round(fuel_surcharge, 2),
                handling_fee=round(handling_fee, 2),
                total_cost=round(total_cost, 2),
                estimated_days=estimated_days,
                is_eligible_for_free_shipping=free_shipping,
                notes=notes
            )
    
    # DEMONSTRATION
    print("\n📦 DEMONSTRATION: SHIPPING ESTIMATOR")
    print("-" * 40)
    
    estimator = ShippingEstimator()
    
    # Test scenarios
    test_scenarios = [
        {"weight": 1.5, "zip": "90210", "country": "US", "speed": ShippingSpeed.STANDARD, "subtotal": 0, "member": False, "desc": "Local, standard"},
        {"weight": 2.0, "zip": "90210", "country": "US", "speed": ShippingSpeed.EXPRESS, "subtotal": 0, "member": False, "desc": "Local, express"},
        {"weight": 3.0, "zip": "90210", "country": "US", "speed": ShippingSpeed.EXPRESS, "subtotal": 75, "member": False, "desc": "Local, express, $75 order"},
        {"weight": 5.0, "zip": "90210", "country": "US", "speed": ShippingSpeed.EXPRESS, "subtotal": 75, "member": True, "desc": "Local, express, $75, member"},
        {"weight": 2.5, "zip": "10001", "country": "US", "speed": ShippingSpeed.STANDARD, "subtotal": 0, "member": False, "desc": "National, standard"},
        {"weight": 1.0, "zip": "WC1A", "country": "UK", "speed": ShippingSpeed.STANDARD, "subtotal": 0, "member": False, "desc": "International, standard"},
        {"weight": 8.0, "zip": "99950", "country": "US", "speed": ShippingSpeed.STANDARD, "subtotal": 0, "member": False, "desc": "Remote, standard"},
    ]
    
    for scenario in test_scenarios:
        print(f"\n{'='*50}")
        print(f"Scenario: {scenario['desc']}")
        print(f"{'='*50}")
        
        estimate = estimator.estimate(
            weight_kg=scenario["weight"],
            postal_code=scenario["zip"],
            country=scenario["country"],
            speed=scenario["speed"],
            order_subtotal=scenario["subtotal"],
            is_member=scenario["member"]
        )
        
        print(f"Zone: {estimate.zone.value.upper()}")
        print(f"Weight: {estimate.weight_kg}kg")
        print(f"Speed: {estimate.speed.value.upper()}")
        print(f"\nCost Breakdown:")
        print(f"  Base Cost: ${estimate.base_cost}")
        print(f"  Fuel Surcharge: ${estimate.fuel_surcharge}")
        print(f"  Handling Fee: ${estimate.handling_fee}")
        print(f"  TOTAL: ${estimate.total_cost}")
        print(f"\nEstimated Delivery: {estimate.estimated_days} days")
        
        if estimate.notes:
            print(f"Notes: {', '.join(estimate.notes)}")


if __name__ == "__main__":
    demonstrate_if_elif_else()
    build_shipping_estimator()
```

---

## 🎫 Section 4: Customer Support Ticket Routing System

A complete customer support system that routes tickets based on priority, category, and customer tier using if-elif-else chains.

**SOLID Principles Applied:**
- Single Responsibility: Each routing rule has one purpose
- Open/Closed: New categories and priorities can be added
- Liskov Substitution: All ticket types follow same interface

**Design Patterns:**
- Chain of Responsibility: Ticket passes through routing rules
- Strategy Pattern: Different routing strategies for different ticket types
- Command Pattern: Each routing decision is encapsulated

```python
"""
CUSTOMER SUPPORT TICKET ROUTING SYSTEM

This section builds a complete customer support system using
if-elif-else chains for ticket routing and escalation.

SOLID Principles Applied:
- Single Responsibility: Each routing function has one purpose
- Open/Closed: New categories can be added without modifying existing code

Design Patterns:
- Chain of Responsibility: Ticket passes through routing rules
- Strategy Pattern: Different strategies for different ticket types
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict


class TicketPriority(Enum):
    """Ticket priority levels."""
    CRITICAL = 5
    HIGH = 4
    MEDIUM = 3
    LOW = 2
    TRIVIAL = 1


class TicketCategory(Enum):
    """Ticket categories."""
    TECHNICAL = "technical"
    BILLING = "billing"
    ACCOUNT = "account"
    PRODUCT = "product"
    SHIPPING = "shipping"
    FEATURE_REQUEST = "feature_request"
    COMPLAINT = "complaint"
    SECURITY = "security"
    GENERAL = "general"


class CustomerTier(Enum):
    """Customer loyalty tiers."""
    PLATINUM = 4
    GOLD = 3
    SILVER = 2
    BRONZE = 1
    BASIC = 0


@dataclass
class SupportTicket:
    """Represents a customer support ticket."""
    ticket_id: str
    customer_id: str
    customer_name: str
    customer_tier: CustomerTier
    priority: TicketPriority
    category: TicketCategory
    subject: str
    description: str
    created_at: datetime = field(default_factory=datetime.now)
    assigned_to: Optional[str] = None
    status: str = "open"
    escalation_count: int = 0
    tags: List[str] = field(default_factory=list)
    
    def age_hours(self) -> float:
        """Calculate ticket age in hours."""
        delta = datetime.now() - self.created_at
        return delta.total_seconds() / 3600


class RoutingRule:
    """Base class for routing rules."""
    
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority
    
    def applies(self, ticket: SupportTicket) -> bool:
        """Check if rule applies to ticket."""
        raise NotImplementedError
    
    def get_team(self) -> str:
        """Get team to route to."""
        raise NotImplementedError
    
    def get_sla_hours(self) -> int:
        """Get SLA response time in hours."""
        raise NotImplementedError


class CategoryRoutingRule(RoutingRule):
    """Route based on ticket category."""
    
    def __init__(self):
        super().__init__("Category Routing", priority=10)
    
    def applies(self, ticket: SupportTicket) -> bool:
        return True
    
    def get_team(self) -> str:
        return "General Support"
    
    def get_sla_hours(self) -> int:
        return 48


class PriorityRoutingRule(RoutingRule):
    """Route based on ticket priority."""
    
    def __init__(self):
        super().__init__("Priority Routing", priority=20)
    
    def applies(self, ticket: SupportTicket) -> bool:
        return ticket.priority in [TicketPriority.CRITICAL, TicketPriority.HIGH]
    
    def get_team(self) -> str:
        if ticket.priority == TicketPriority.CRITICAL:
            return "Emergency Response Team"
        return "Senior Support Team"
    
    def get_sla_hours(self) -> int:
        if ticket.priority == TicketPriority.CRITICAL:
            return 1
        return 4


class CustomerTierRoutingRule(RoutingRule):
    """Route based on customer tier."""
    
    def __init__(self):
        super().__init__("Customer Tier Routing", priority=30)
    
    def applies(self, ticket: SupportTicket) -> bool:
        return ticket.customer_tier in [CustomerTier.PLATINUM, CustomerTier.GOLD]
    
    def get_team(self) -> str:
        return "Premium Support Team"
    
    def get_sla_hours(self) -> int:
        if ticket.customer_tier == CustomerTier.PLATINUM:
            return 2
        return 8


class SecurityRoutingRule(RoutingRule):
    """Route security-related tickets."""
    
    def __init__(self):
        super().__init__("Security Routing", priority=40)
    
    def applies(self, ticket: SupportTicket) -> bool:
        return ticket.category == TicketCategory.SECURITY
    
    def get_team(self) -> str:
        return "Security Team"
    
    def get_sla_hours(self) -> int:
        return 1


class BillingRoutingRule(RoutingRule):
    """Route billing-related tickets."""
    
    def __init__(self):
        super().__init__("Billing Routing", priority=50)
    
    def applies(self, ticket: SupportTicket) -> bool:
        return ticket.category == TicketCategory.BILLING
    
    def get_team(self) -> str:
        return "Billing Team"
    
    def get_sla_hours(self) -> int:
        return 24


class TechnicalRoutingRule(RoutingRule):
    """Route technical tickets."""
    
    def __init__(self):
        super().__init__("Technical Routing", priority=60)
    
    def applies(self, ticket: SupportTicket) -> bool:
        return ticket.category == TicketCategory.TECHNICAL
    
    def get_team(self) -> str:
        return "Technical Support Team"
    
    def get_sla_hours(self) -> int:
        return 24


class SupportTicketRouter:
    """
    Routes support tickets to appropriate teams.
    
    Design Pattern: Chain of Responsibility - Ticket passes through rules
    """
    
    def __init__(self):
        self.rules = [
            SecurityRoutingRule(),
            PriorityRoutingRule(),
            CustomerTierRoutingRule(),
            BillingRoutingRule(),
            TechnicalRoutingRule(),
            CategoryRoutingRule()
        ]
    
    def route(self, ticket: SupportTicket) -> Dict[str, Any]:
        """
        Route ticket to appropriate team.
        
        Returns:
            Dictionary with routing decision
        """
        # Guard clauses for invalid tickets
        if not ticket.subject:
            return {"error": "Ticket must have a subject"}
        
        if not ticket.description:
            return {"error": "Ticket must have a description"}
        
        # Find best matching rule
        for rule in self.rules:
            if rule.applies(ticket):
                assigned_team = rule.get_team()
                sla_hours = rule.get_sla_hours()
                
                return {
                    "ticket_id": ticket.ticket_id,
                    "assigned_team": assigned_team,
                    "sla_hours": sla_hours,
                    "sla_deadline": (datetime.now() + timedelta(hours=sla_hours)).isoformat(),
                    "priority": ticket.priority.name,
                    "routing_reason": f"Matched rule: {rule.name}"
                }
        
        # Fallback routing
        return {
            "ticket_id": ticket.ticket_id,
            "assigned_team": "General Support",
            "sla_hours": 48,
            "sla_deadline": (datetime.now() + timedelta(hours=48)).isoformat(),
            "priority": ticket.priority.name,
            "routing_reason": "No specific rule matched"
        }
    
    def calculate_escalation(self, ticket: SupportTicket, hours_waiting: float) -> Dict[str, Any]:
        """
        Determine if ticket needs escalation based on wait time and priority.
        
        Returns:
            Escalation decision
        """
        # Priority-based escalation thresholds
        escalation_thresholds = {
            TicketPriority.CRITICAL: 0.5,   # 30 minutes
            TicketPriority.HIGH: 2,          # 2 hours
            TicketPriority.MEDIUM: 8,        # 8 hours
            TicketPriority.LOW: 24,          # 24 hours
            TicketPriority.TRIVIAL: 48       # 48 hours
        }
        
        threshold = escalation_thresholds.get(ticket.priority, 24)
        
        if hours_waiting >= threshold:
            # Determine escalation level
            if ticket.escalation_count == 0:
                level = "Level 1 - Team Lead"
            elif ticket.escalation_count == 1:
                level = "Level 2 - Department Manager"
            elif ticket.escalation_count == 2:
                level = "Level 3 - Director"
            else:
                level = "Level 4 - Executive"
            
            return {
                "needs_escalation": True,
                "hours_waiting": hours_waiting,
                "threshold": threshold,
                "escalation_level": level,
                "escalation_count": ticket.escalation_count + 1
            }
        
        return {
            "needs_escalation": False,
            "hours_waiting": hours_waiting,
            "threshold": threshold,
            "hours_until_escalation": round(threshold - hours_waiting, 1)
        }


class SupportTicketSystem:
    """
    Complete support ticket management system.
    
    SOLID: Single Responsibility - Manages ticket lifecycle
    
    Design Patterns:
    - Command Pattern: Ticket operations as commands
    - Observer Pattern: Notify teams on ticket assignment
    """
    
    def __init__(self):
        self.tickets: Dict[str, SupportTicket] = {}
        self.ticket_counter = 0
        self.router = SupportTicketRouter()
        self.team_queues: Dict[str, List[str]] = defaultdict(list)
        self.escalation_history: Dict[str, List[Dict]] = defaultdict(list)
    
    def create_ticket(self, customer_id: str, customer_name: str, customer_tier: CustomerTier,
                     category: TicketCategory, subject: str, description: str) -> SupportTicket:
        """Create a new support ticket."""
        self.ticket_counter += 1
        ticket_id = f"TKT-{self.ticket_counter:06d}"
        
        # Determine priority based on customer tier and category
        if category == TicketCategory.SECURITY:
            priority = TicketPriority.CRITICAL
        elif category == TicketCategory.COMPLAINT and customer_tier in [CustomerTier.PLATINUM, CustomerTier.GOLD]:
            priority = TicketPriority.HIGH
        elif customer_tier == CustomerTier.PLATINUM:
            priority = TicketPriority.HIGH
        elif customer_tier == CustomerTier.GOLD:
            priority = TicketPriority.MEDIUM
        else:
            priority = TicketPriority.LOW
        
        ticket = SupportTicket(
            ticket_id=ticket_id,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_tier=customer_tier,
            priority=priority,
            category=category,
            subject=subject,
            description=description
        )
        
        self.tickets[ticket_id] = ticket
        
        # Route the ticket
        routing_result = self.router.route(ticket)
        
        if "error" not in routing_result:
            ticket.assigned_to = routing_result["assigned_team"]
            self.team_queues[routing_result["assigned_team"]].append(ticket_id)
        
        return ticket
    
    def get_ticket_status(self, ticket_id: str) -> Dict[str, Any]:
        """Get detailed ticket status."""
        ticket = self.tickets.get(ticket_id)
        
        if not ticket:
            return {"error": f"Ticket {ticket_id} not found"}
        
        # Re-route to get latest routing
        routing = self.router.route(ticket)
        
        # Check escalation
        hours_waiting = ticket.age_hours()
        escalation = self.router.calculate_escalation(ticket, hours_waiting)
        
        return {
            "ticket_id": ticket.ticket_id,
            "customer": ticket.customer_name,
            "tier": ticket.customer_tier.name,
            "category": ticket.category.value,
            "priority": ticket.priority.name,
            "subject": ticket.subject,
            "status": ticket.status,
            "created_at": ticket.created_at.isoformat(),
            "age_hours": round(hours_waiting, 1),
            "assigned_team": ticket.assigned_to,
            "routing": routing,
            "escalation": escalation
        }
    
    def get_team_queue(self, team_name: str) -> List[Dict]:
        """Get all tickets in a team's queue."""
        ticket_ids = self.team_queues.get(team_name, [])
        tickets = []
        
        for ticket_id in ticket_ids:
            ticket = self.tickets.get(ticket_id)
            if ticket:
                tickets.append({
                    "ticket_id": ticket.ticket_id,
                    "customer": ticket.customer_name,
                    "priority": ticket.priority.name,
                    "subject": ticket.subject,
                    "age_hours": round(ticket.age_hours(), 1),
                    "status": ticket.status
                })
        
        # Sort by priority and age
        tickets.sort(key=lambda t: (t["age_hours"], -TicketPriority[t["priority"]].value), reverse=True)
        
        return tickets
    
    def get_system_metrics(self) -> Dict[str, Any]:
        """Get overall system metrics."""
        total_tickets = len(self.tickets)
        
        # Count by status
        by_status = defaultdict(int)
        for ticket in self.tickets.values():
            by_status[ticket.status] += 1
        
        # Count by priority
        by_priority = defaultdict(int)
        for ticket in self.tickets.values():
            by_priority[ticket.priority.name] += 1
        
        # Count by category
        by_category = defaultdict(int)
        for ticket in self.tickets.values():
            by_category[ticket.category.value] += 1
        
        # Calculate average response time (simplified)
        avg_age = sum(t.age_hours() for t in self.tickets.values()) / total_tickets if total_tickets > 0 else 0
        
        return {
            "total_tickets": total_tickets,
            "open_tickets": by_status.get("open", 0),
            "by_priority": dict(by_priority),
            "by_category": dict(by_category),
            "average_age_hours": round(avg_age, 1),
            "teams_with_queues": len(self.team_queues)
        }


def run_ticket_system_demo():
    """
    Complete demonstration of the support ticket system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: SUPPORT TICKET ROUTING SYSTEM")
    print("=" * 60)
    
    # Create ticket system
    system = SupportTicketSystem()
    
    # Create various tickets
    print("\n1. CREATING SUPPORT TICKETS")
    print("-" * 40)
    
    tickets_data = [
        ("CUST-001", "Alice Chen", CustomerTier.PLATINUM, TicketCategory.TECHNICAL,
         "Cannot login to dashboard", "Getting 500 error when trying to access dashboard"),
        
        ("CUST-002", "Bob Smith", CustomerTier.BASIC, TicketCategory.BILLING,
         "Incorrect charge on invoice", "Invoice #INV-123 shows $50 but should be $40"),
        
        ("CUST-003", "Charlie Brown", CustomerTier.GOLD, TicketCategory.SECURITY,
         "Suspicious account activity", "Received login attempt from unknown location"),
        
        ("CUST-004", "Diana Prince", CustomerTier.SILVER, TicketCategory.PRODUCT,
         "Product not working as described", "Wireless mouse stops working after 5 minutes"),
        
        ("CUST-005", "Eve Wilson", CustomerTier.BASIC, TicketCategory.SHIPPING,
         "Package not delivered", "Order #ORD-789 shows delivered but not received"),
        
        ("CUST-006", "Frank Castle", CustomerTier.PLATINUM, TicketCategory.COMPLAINT,
         "Very unhappy with service", "Third time contacting support for same issue")
    ]
    
    created_tickets = []
    for data in tickets_data:
        ticket = system.create_ticket(*data)
        created_tickets.append(ticket)
        print(f"  Created: {ticket.ticket_id} - {ticket.subject[:40]}... ({ticket.priority.name})")
    
    # Display ticket statuses
    print("\n2. TICKET STATUS AND ROUTING")
    print("-" * 40)
    
    for ticket in created_tickets[:3]:  # Show first 3 tickets
        status = system.get_ticket_status(ticket.ticket_id)
        print(f"\nTicket: {status['ticket_id']}")
        print(f"  Customer: {status['customer']} ({status['tier']})")
        print(f"  Priority: {status['priority']}")
        print(f"  Category: {status['category']}")
        print(f"  Assigned Team: {status['assigned_team']}")
        print(f"  SLA Deadline: {status['routing']['sla_deadline'][:16]}")
        print(f"  Age: {status['age_hours']} hours")
        
        if status['escalation']['needs_escalation']:
            print(f"  ⚠️ ESCALATION: {status['escalation']['escalation_level']}")
    
    # Show team queues
    print("\n3. TEAM QUEUES")
    print("-" * 40)
    
    teams = ["Security Team", "Premium Support Team", "Billing Team", "Technical Support Team"]
    
    for team in teams:
        queue = system.get_team_queue(team)
        if queue:
            print(f"\n{team} Queue ({len(queue)} tickets):")
            for ticket in queue[:3]:
                print(f"  {ticket['ticket_id']}: {ticket['subject'][:35]}... ({ticket['priority']}, {ticket['age_hours']}h)")
    
    # System metrics
    print("\n4. SYSTEM METRICS")
    print("-" * 40)
    
    metrics = system.get_system_metrics()
    print(f"Total Tickets: {metrics['total_tickets']}")
    print(f"Open Tickets: {metrics['open_tickets']}")
    print(f"Average Age: {metrics['average_age_hours']} hours")
    print(f"By Priority: {metrics['by_priority']}")
    print(f"By Category: {metrics['by_category']}")
    
    # Simulate time passing (for escalation demo)
    print("\n5. ESCALATION DEMONSTRATION")
    print("-" * 40)
    
    # Create an old ticket (simulate by setting created_at manually)
    old_ticket = SupportTicket(
        ticket_id="TKT-999999",
        customer_id="CUST-999",
        customer_name="Test User",
        customer_tier=CustomerTier.BASIC,
        priority=TicketPriority.HIGH,
        category=TicketCategory.TECHNICAL,
        subject="Urgent technical issue",
        description="System down",
        created_at=datetime.now() - timedelta(hours=3)
    )
    
    # Check escalation
    hours_waiting = old_ticket.age_hours()
    escalation = system.router.calculate_escalation(old_ticket, hours_waiting)
    
    print(f"Ticket: {old_ticket.ticket_id}")
    print(f"Priority: {old_ticket.priority.name}")
    print(f"Waiting: {hours_waiting} hours")
    
    if escalation['needs_escalation']:
        print(f"⚠️ ESCALATION NEEDED: {escalation['escalation_level']}")
    else:
        print(f"✓ Within SLA: {escalation['hours_until_escalation']} hours until escalation")


if __name__ == "__main__":
    run_ticket_system_demo()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **if Statement** – Execute code only when condition is True. Use guard clauses for early returns and input validation.

- **if-else Statement** – Two execution paths: one for True, one for False. Use ternary operator for simple conditional assignments.

- **if-elif-else Chain** – Multiple mutually exclusive conditions. Order matters—put most specific conditions first.

- **Grade Calculator** – Convert numeric scores to letter grades with plus/minus modifiers. Handle different grading scales.

- **Shipping Estimator** – Calculate costs based on weight, zone, and speed. Apply free shipping rules.

- **Support Ticket System** – Route tickets based on priority, category, and customer tier. Track escalations and SLAs.

- **SOLID Principles Applied** – Single Responsibility (each condition handles one case), Open/Closed (new conditions can be added), Liskov Substitution (consistent condition evaluation).

- **Design Patterns Used** – Guard Clause Pattern (early returns), Chain of Responsibility (if-elif chains), Strategy Pattern (different routing strategies), Command Pattern (encapsulated decisions).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Loops – for, while, break, continue

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 4 | 3 | 57% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **9** | **43** | **17%** |

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

**Next Story:** Series A, Story 5: The 2026 Python Metromap: Loops – for, while, break, continue

---

## 📝 Your Invitation

You've mastered control flow. Now build something with what you've learned:

1. **Build a grade calculator** – Convert numeric scores to letter grades. Add plus/minus modifiers. Handle different grading scales.

2. **Create a shipping calculator** – Calculate costs based on weight, zone, and speed. Add free shipping rules.

3. **Build a support ticket system** – Route tickets based on priority, category, and customer tier. Add escalation rules.

4. **Create a discount engine** – Use if-elif-else to apply different discount tiers based on purchase amount and customer status.

5. **Build an order processing system** – Use guard clauses for validation, then business logic for pricing and shipping.

**You've mastered control flow. Next stop: Loops!**

---

*Found this helpful? Clap, comment, and share what you built with control flow. Next stop: Loops!* 🚇