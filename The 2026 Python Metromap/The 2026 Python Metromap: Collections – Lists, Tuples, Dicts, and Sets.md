# The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets

## Series A: Foundations Station | Story 2 of 7

![The 2026 Python Metromap/images/Collections – Lists, Tuples, Dicts, and Sets](images/Collections – Lists, Tuples, Dicts, and Sets.png)

## 📖 Introduction

**Welcome to the second stop on the Foundations Station Line.**

You've mastered variables and data types. You can store a customer name, a product price, and an order status. But real-world applications aren't built from single values—they're built from collections of data.

A shopping cart isn't one item—it's a list of items. An employee record isn't one field—it's a dictionary of attributes. GPS coordinates aren't changeable—they're a tuple. Unique website visitors aren't duplicates—they're a set.

This story—**The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets**—is your journey into Python's four powerhouse data structures. We'll build real things: a shopping cart system with lists, a user profile system with dictionaries, a unique visitor tracker with sets, and an immutable configuration manager with tuples.

**Let's load the data.**

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

- 🏗️ **The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets** – Shopping carts with lists; user profiles with dictionaries; analytics with sets; configuration with tuples. **⬅️ YOU ARE HERE**

- 📦 **The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More** – Building a discount engine; age verification; loan approval calculator. 🔜 *Up Next*

- 🚦 **The 2026 Python Metromap: Control Flow – if, elif, else** – Grade calculator; shipping cost estimator; customer support ticket routing.

- 🔁 **The 2026 Python Metromap: Loops – for, while, break, continue** – Batch file processor; API retry mechanism; pagination system.

- 🧩 **The 2026 Python Metromap: Nested Logic – Conditions Inside Loops** – Sudoku validator; student grade matrix; multi-condition search filter.

- 📥📤 **The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users** – CLI calculator; user registration form; interactive quiz system.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📋 Section 1: Lists – Ordered and Mutable Sequences

Lists are ordered, mutable collections that can hold any type of data. They're perfect for sequences that change over time—like a shopping cart or a playlist.

**SOLID Principle Applied: Single Responsibility** – A list has one job: maintain an ordered sequence of items. Methods like append(), remove(), and sort() each do one thing well.

**Design Pattern: Collection Pattern** – Lists provide a standard interface for accessing, modifying, and iterating over grouped data.

```python
"""
LISTS: ORDERED AND MUTABLE SEQUENCES

This section covers list creation, manipulation, and common operations.
Lists are the most versatile data structure in Python.

SOLID Principle: Single Responsibility
- Lists maintain ordered sequences
- Each list method performs one specific operation

Design Pattern: Collection Pattern
- Provides uniform interface for grouped data
- Supports iteration, indexing, and modification
"""

from typing import List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import copy


def demonstrate_list_basics():
    """
    Demonstrates fundamental list operations.
    
    Lists are created with square brackets [] or list() constructor.
    They maintain order and allow duplicate values.
    """
    print("=" * 60)
    print("SECTION 1A: LIST BASICS")
    print("=" * 60)
    
    # LIST CREATION
    print("\n1. CREATING LISTS")
    print("-" * 40)
    
    # Empty list
    empty_list = []
    empty_list_constructor = list()
    print(f"Empty list: {empty_list}")
    print(f"Empty list constructor: {empty_list_constructor}")
    
    # List with initial values
    fruits = ["apple", "banana", "cherry", "date"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    
    print(f"Fruits: {fruits}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    
    # List from range
    range_list = list(range(5))  # [0, 1, 2, 3, 4]
    print(f"From range: {range_list}")
    
    # List from string
    char_list = list("Python")
    print(f"From string: {char_list}")
    
    # ACCESSING ELEMENTS
    print("\n2. ACCESSING ELEMENTS")
    print("-" * 40)
    
    colors = ["red", "green", "blue", "yellow", "purple"]
    print(f"Colors: {colors}")
    
    # Positive indexing (0-based)
    print(f"First element (index 0): {colors[0]}")
    print(f"Second element (index 1): {colors[1]}")
    print(f"Third element (index 2): {colors[2]}")
    
    # Negative indexing (from end)
    print(f"Last element (index -1): {colors[-1]}")
    print(f"Second last (index -2): {colors[-2]}")
    
    # MODIFYING ELEMENTS
    print("\n3. MODIFYING ELEMENTS")
    print("-" * 40)
    
    # Change element by index
    colors[1] = "emerald"
    print(f"After modifying index 1: {colors}")
    
    # SLICING
    print("\n4. SLICING LISTS")
    print("-" * 40)
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original: {numbers}")
    
    # Slicing syntax: list[start:end:step]
    print(f"First 3 elements [0:3]: {numbers[0:3]}")
    print(f"Elements 3-6 [3:7]: {numbers[3:7]}")
    print(f"Last 3 elements [-3:]: {numbers[-3:]}")
    print(f"Every other element [::2]: {numbers[::2]}")
    print(f"Reversed [::-1]: {numbers[::-1]}")
    
    # Slicing creates a SHALLOW copy
    original = [1, 2, 3]
    sliced_copy = original[:]
    sliced_copy[0] = 99
    print(f"Original after slice modification: {original} (unchanged)")
    print(f"Slice copy: {sliced_copy}")


def demonstrate_list_methods():
    """
    Demonstrates list methods for adding, removing, and searching.
    
    Lists have many built-in methods that modify the list in-place.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: LIST METHODS")
    print("=" * 60)
    
    # ADDING ELEMENTS
    print("\n1. ADDING ELEMENTS")
    print("-" * 40)
    
    shopping_list = []
    print(f"Start: {shopping_list}")
    
    # append() - adds to end
    shopping_list.append("milk")
    print(f"After append('milk'): {shopping_list}")
    
    shopping_list.append("eggs")
    shopping_list.append("bread")
    print(f"After more appends: {shopping_list}")
    
    # insert() - adds at specific position
    shopping_list.insert(1, "butter")
    print(f"After insert(1, 'butter'): {shopping_list}")
    
    # extend() - adds multiple elements
    shopping_list.extend(["cheese", "yogurt"])
    print(f"After extend(): {shopping_list}")
    
    # REMOVING ELEMENTS
    print("\n2. REMOVING ELEMENTS")
    print("-" * 40)
    
    # remove() - removes first occurrence by value
    shopping_list.remove("eggs")
    print(f"After remove('eggs'): {shopping_list}")
    
    # pop() - removes and returns by index (default last)
    removed = shopping_list.pop()
    print(f"After pop(): removed '{removed}', list: {shopping_list}")
    
    removed = shopping_list.pop(0)
    print(f"After pop(0): removed '{removed}', list: {shopping_list}")
    
    # clear() - removes all elements
    temp_list = [1, 2, 3]
    temp_list.clear()
    print(f"After clear(): {temp_list}")
    
    # SEARCHING AND COUNTING
    print("\n3. SEARCHING AND COUNTING")
    print("-" * 40)
    
    items = ["apple", "banana", "apple", "cherry", "apple", "date"]
    print(f"Items: {items}")
    
    # index() - finds first occurrence (raises ValueError if not found)
    print(f"Index of 'banana': {items.index('banana')}")
    print(f"Index of 'apple' starting from 1: {items.index('apple', 1)}")
    
    # count() - counts occurrences
    print(f"Count of 'apple': {items.count('apple')}")
    print(f"Count of 'grape': {items.count('grape')}")
    
    # in operator (membership testing)
    print(f"'cherry' in items: {'cherry' in items}")
    print(f"'grape' in items: {'grape' in items}")
    
    # SORTING AND REVERSING
    print("\n4. SORTING AND REVERSING")
    print("-" * 40)
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"Original: {numbers}")
    
    # sort() - sorts in-place (modifies original)
    numbers.sort()
    print(f"After sort(): {numbers}")
    
    # sort descending
    numbers.sort(reverse=True)
    print(f"After sort(reverse=True): {numbers}")
    
    # reverse() - reverses in-place
    letters = ["a", "b", "c", "d"]
    letters.reverse()
    print(f"After reverse(): {letters}")
    
    # sorted() function - returns new sorted list
    original = [3, 1, 4, 1, 5]
    sorted_new = sorted(original)
    print(f"Original unchanged: {original}")
    print(f"New sorted list: {sorted_new}")
    
    # LIST COPYING (Important!)
    print("\n5. LIST COPYING (SHALLOW VS DEEP)")
    print("-" * 40)
    
    # Method 1: Assignment (does NOT copy - both reference same list)
    original = [1, 2, [3, 4]]
    assignment_copy = original
    assignment_copy[0] = 99
    print(f"Original after assignment modification: {original} (changed!)")
    
    # Reset
    original = [1, 2, [3, 4]]
    
    # Method 2: Slice copy (shallow copy)
    slice_copy = original[:]
    slice_copy[0] = 99
    slice_copy[2][0] = 999  # Modifies nested list in BOTH!
    print(f"Original after shallow copy: {original}")
    print(f"Shallow copy: {slice_copy}")
    
    # Method 3: copy() method (shallow copy)
    original = [1, 2, [3, 4]]
    copy_method = original.copy()
    copy_method[0] = 99
    print(f"Original after .copy(): {original}")
    
    # Method 4: deep copy (copies nested structures)
    import copy
    original = [1, 2, [3, 4]]
    deep_copy = copy.deepcopy(original)
    deep_copy[2][0] = 999
    print(f"Original after deep copy: {original} (unchanged)")
    print(f"Deep copy: {deep_copy}")


def demonstrate_list_comprehensions():
    """
    Demonstrates list comprehensions for concise list creation.
    
    List comprehensions provide a concise way to create lists
    from existing iterables with optional filtering.
    
    Design Pattern: Comprehension Pattern - Declarative list construction
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: LIST COMPREHENSIONS")
    print("=" * 60)
    
    # BASIC COMPREHENSION
    print("\n1. BASIC COMPREHENSION")
    print("-" * 40)
    
    # Traditional loop
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print(f"Loop squares: {squares}")
    
    # List comprehension
    squares_comp = [x ** 2 for x in range(10)]
    print(f"Comprehension squares: {squares_comp}")
    
    # WITH CONDITIONAL FILTERING
    print("\n2. WITH CONDITIONAL FILTERING")
    print("-" * 40)
    
    # Even numbers only
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers: {evens}")
    
    # Odd numbers squared
    odd_squares = [x ** 2 for x in range(10) if x % 2 == 1]
    print(f"Odd squares: {odd_squares}")
    
    # WITH IF-ELSE
    print("\n3. WITH IF-ELSE (TERNARY)")
    print("-" * 40)
    
    # Label numbers as even or odd
    labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
    print(f"Number labels: {labels}")
    
    # NESTED COMPREHENSIONS
    print("\n4. NESTED COMPREHENSIONS")
    print("-" * 40)
    
    # Flatten a matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Original matrix: {matrix}")
    print(f"Flattened: {flattened}")
    
    # Create coordinate pairs
    coordinates = [(x, y) for x in range(3) for y in range(3)]
    print(f"Coordinate pairs: {coordinates}")
    
    # PRACTICAL EXAMPLES
    print("\n5. PRACTICAL EXAMPLES")
    print("-" * 40)
    
    # Extract prices from product list
    products = [
        {"name": "Laptop", "price": 999},
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 75}
    ]
    prices = [p["price"] for p in products]
    print(f"Product prices: {prices}")
    
    # Filter expensive products
    expensive = [p["name"] for p in products if p["price"] > 50]
    print(f"Products over $50: {expensive}")
    
    # String manipulation
    words = ["hello", "world", "python", "code"]
    upper_words = [word.upper() for word in words]
    print(f"Uppercase words: {upper_words}")
    
    # Multiple conditions
    numbers = list(range(20))
    special = [n for n in numbers if n % 2 == 0 and n % 3 == 0]
    print(f"Numbers divisible by 2 AND 3: {special}")


def build_shopping_cart_system():
    """
    Complete shopping cart system using lists.
    
    This demonstrates a production-ready shopping cart with
    items, quantities, prices, and total calculations.
    
    SOLID Principles Applied:
    - Single Responsibility: Each class has one purpose
    - Open/Closed: Cart operations can be extended
    
    Design Patterns:
    - Collection Pattern: Cart maintains list of items
    - Builder Pattern: Add items incrementally
    - Iterator Pattern: Iterate through cart items
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: SHOPPING CART SYSTEM")
    print("=" * 60)
    
    @dataclass
    class CartItem:
        """
        Represents a single item in the shopping cart.
        
        SOLID: Single Responsibility - Only represents an item
        """
        product_id: str
        name: str
        price: float
        quantity: int
        
        def subtotal(self) -> float:
            """Calculate line item subtotal."""
            return self.price * self.quantity
        
        def __str__(self) -> str:
            return f"{self.quantity}x {self.name} @ ${self.price:.2f} = ${self.subtotal():.2f}"
    
    class ShoppingCart:
        """
        Complete shopping cart implementation.
        
        SOLID: 
        - Single Responsibility: Manages cart operations
        - Open/Closed: Extensible with new features
        
        Design Patterns:
        - Collection Pattern: List-based storage
        - Iterator Pattern: Iterable cart items
        """
        
        def __init__(self):
            """Initialize empty cart."""
            self._items: List[CartItem] = []
            self._discount_code: Optional[str] = None
            self._discount_percent: float = 0.0
        
        # CORE CART OPERATIONS
        def add_item(self, product_id: str, name: str, price: float, quantity: int = 1) -> 'ShoppingCart':
            """
            Add an item to the cart.
            
            If item already exists, updates quantity instead of duplicating.
            
            Args:
                product_id: Unique product identifier
                name: Product name
                price: Unit price
                quantity: Number of units
                
            Returns:
                Self for method chaining (Builder pattern)
            """
            if quantity <= 0:
                raise ValueError(f"Quantity must be positive, got {quantity}")
            
            # Check if item already in cart
            for item in self._items:
                if item.product_id == product_id:
                    # Update existing item quantity
                    item.quantity += quantity
                    print(f"  Updated {name}: {item.quantity} total")
                    return self
            
            # Add new item
            new_item = CartItem(product_id, name, price, quantity)
            self._items.append(new_item)
            print(f"  Added {quantity}x {name} (${price:.2f} each)")
            return self
        
        def remove_item(self, product_id: str) -> 'ShoppingCart':
            """
            Remove an item completely from the cart.
            
            Args:
                product_id: Product identifier to remove
                
            Returns:
                Self for method chaining
            """
            original_length = len(self._items)
            self._items = [item for item in self._items if item.product_id != product_id]
            
            if len(self._items) < original_length:
                print(f"  Removed product {product_id}")
            else:
                print(f"  Product {product_id} not found in cart")
            
            return self
        
        def update_quantity(self, product_id: str, quantity: int) -> 'ShoppingCart':
            """
            Update quantity of an existing item.
            
            Args:
                product_id: Product identifier
                quantity: New quantity (0 or negative removes item)
                
            Returns:
                Self for method chaining
            """
            if quantity <= 0:
                return self.remove_item(product_id)
            
            for item in self._items:
                if item.product_id == product_id:
                    item.quantity = quantity
                    print(f"  Updated {item.name} to quantity {quantity}")
                    return self
            
            print(f"  Product {product_id} not found")
            return self
        
        # DISCOUNT OPERATIONS
        def apply_discount(self, code: str, percent: float) -> 'ShoppingCart':
            """
            Apply a discount code to the cart.
            
            Args:
                code: Discount code
                percent: Discount percentage (e.g., 10 for 10% off)
                
            Returns:
                Self for method chaining
            """
            if not 0 < percent <= 100:
                raise ValueError(f"Discount percent must be between 0 and 100, got {percent}")
            
            self._discount_code = code
            self._discount_percent = percent
            print(f"  Applied {percent}% discount with code: {code}")
            return self
        
        def remove_discount(self) -> 'ShoppingCart':
            """Remove any applied discount."""
            self._discount_code = None
            self._discount_percent = 0.0
            print("  Discount removed")
            return self
        
        # CALCULATION METHODS
        def item_count(self) -> int:
            """Get total number of items (sum of quantities)."""
            return sum(item.quantity for item in self._items)
        
        def unique_items_count(self) -> int:
            """Get number of unique products in cart."""
            return len(self._items)
        
        def subtotal(self) -> float:
            """Calculate subtotal before discounts and tax."""
            return sum(item.subtotal() for item in self._items)
        
        def discount_amount(self) -> float:
            """Calculate discount amount."""
            return self.subtotal() * (self._discount_percent / 100)
        
        def subtotal_after_discount(self) -> float:
            """Calculate subtotal after discount."""
            return self.subtotal() - self.discount_amount()
        
        def tax_amount(self, tax_rate: float = 0.08) -> float:
            """Calculate tax amount."""
            return self.subtotal_after_discount() * tax_rate
        
        def total(self, tax_rate: float = 0.08) -> float:
            """Calculate final total including tax."""
            return self.subtotal_after_discount() + self.tax_amount(tax_rate)
        
        # UTILITY METHODS
        def is_empty(self) -> bool:
            """Check if cart is empty."""
            return len(self._items) == 0
        
        def clear(self) -> 'ShoppingCart':
            """Remove all items from cart."""
            self._items.clear()
            self._discount_code = None
            self._discount_percent = 0.0
            print("  Cart cleared")
            return self
        
        def get_items(self) -> List[CartItem]:
            """Get copy of cart items (prevents external modification)."""
            return self._items.copy()
        
        # DISPLAY METHODS
        def __str__(self) -> str:
            """Printable cart summary."""
            if self.is_empty():
                return "🛒 Cart is empty"
            
            lines = ["\n" + "=" * 50, "🛒 SHOPPING CART", "=" * 50]
            
            for item in self._items:
                lines.append(f"  {item}")
            
            lines.append("-" * 50)
            lines.append(f"  Subtotal: ${self.subtotal():.2f}")
            
            if self._discount_percent > 0:
                lines.append(f"  Discount ({self._discount_percent}%): -${self.discount_amount():.2f}")
                lines.append(f"  After discount: ${self.subtotal_after_discount():.2f}")
            
            lines.append(f"  Tax (8%): ${self.tax_amount():.2f}")
            lines.append(f"  TOTAL: ${self.total():.2f}")
            lines.append("=" * 50)
            
            return "\n".join(lines)
        
        def generate_receipt(self) -> str:
            """
            Generate a formatted receipt for printing.
            
            Returns:
                Receipt string suitable for printing or email
            """
            receipt_lines = []
            receipt_lines.append("=" * 50)
            receipt_lines.append(f"{'METROMAP MART':^50}")
            receipt_lines.append(f"{'RECEIPT':^50}")
            receipt_lines.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S'):^50}")
            receipt_lines.append("=" * 50)
            receipt_lines.append("")
            
            for item in self._items:
                receipt_lines.append(f"{item.name:<30} x{item.quantity:>2}  ${item.subtotal():>8.2f}")
            
            receipt_lines.append("")
            receipt_lines.append("-" * 50)
            receipt_lines.append(f"{'Subtotal':<40} ${self.subtotal():>8.2f}")
            
            if self._discount_percent > 0:
                receipt_lines.append(f"{'Discount':<40} -${self.discount_amount():>7.2f}")
            
            receipt_lines.append(f"{'Tax (8%)':<40} ${self.tax_amount():>8.2f}")
            receipt_lines.append("-" * 50)
            receipt_lines.append(f"{'TOTAL':<40} ${self.total():>8.2f}")
            receipt_lines.append("=" * 50)
            receipt_lines.append("Thank you for shopping at Metromap Mart!")
            receipt_lines.append("=" * 50)
            
            return "\n".join(receipt_lines)
        
        def checkout(self, payment_method: str, amount_paid: float) -> dict:
            """
            Process checkout and return order summary.
            
            Args:
                payment_method: Payment method (credit_card, paypal, etc.)
                amount_paid: Amount paid by customer
                
            Returns:
                Dictionary with order details
            """
            if self.is_empty():
                raise ValueError("Cannot checkout empty cart")
            
            total_due = self.total()
            
            if amount_paid < total_due:
                raise ValueError(f"Insufficient payment. Due: ${total_due:.2f}, Paid: ${amount_paid:.2f}")
            
            change = amount_paid - total_due
            
            order_summary = {
                "order_id": f"MP-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "timestamp": datetime.now().isoformat(),
                "items": [(item.name, item.quantity, item.price, item.subtotal()) for item in self._items],
                "subtotal": self.subtotal(),
                "discount_percent": self._discount_percent,
                "discount_amount": self.discount_amount(),
                "tax": self.tax_amount(),
                "total": total_due,
                "payment_method": payment_method,
                "amount_paid": amount_paid,
                "change": change,
                "status": "completed"
            }
            
            # Clear cart after successful checkout
            self.clear()
            
            return order_summary
    
    # DEMONSTRATION
    print("\n📦 DEMONSTRATION: SHOPPING CART SYSTEM")
    print("-" * 40)
    
    # Create cart using Builder pattern (method chaining)
    cart = ShoppingCart()
    
    # Add items
    print("\n1. ADDING ITEMS TO CART")
    print("-" * 40)
    cart.add_item("PROD-001", "Laptop", 999.99, 1)
    cart.add_item("PROD-002", "Wireless Mouse", 29.99, 2)
    cart.add_item("PROD-003", "USB-C Cable", 19.99, 1)
    cart.add_item("PROD-004", "Laptop Stand", 49.99, 1)
    
    # Display cart
    print(cart)
    
    # Update quantities
    print("\n2. UPDATING QUANTITIES")
    print("-" * 40)
    cart.update_quantity("PROD-002", 3)
    cart.update_quantity("PROD-003", 2)
    
    print(cart)
    
    # Apply discount
    print("\n3. APPLYING DISCOUNT")
    print("-" * 40)
    cart.apply_discount("SAVE10", 10)
    
    print(cart)
    
    # Remove an item
    print("\n4. REMOVING ITEM")
    print("-" * 40)
    cart.remove_item("PROD-004")
    
    print(cart)
    
    # Generate receipt
    print("\n5. GENERATING RECEIPT")
    print("-" * 40)
    receipt = cart.generate_receipt()
    print(receipt)
    
    # Checkout
    print("\n6. CHECKOUT")
    print("-" * 40)
    try:
        total = cart.total()
        order = cart.checkout("credit_card", total)
        print(f"✅ Order completed! Order ID: {order['order_id']}")
        print(f"   Total paid: ${order['amount_paid']:.2f}")
        print(f"   Change: ${order['change']:.2f}")
    except ValueError as e:
        print(f"❌ Checkout failed: {e}")
    
    # Verify cart is empty after checkout
    print(f"\nCart after checkout: {cart}")
    
    # CART STATISTICS
    print("\n7. CART STATISTICS")
    print("-" * 40)
    
    # Create a new cart for demonstration
    demo_cart = ShoppingCart()
    demo_cart.add_item("A", "Product A", 10, 5)
    demo_cart.add_item("B", "Product B", 20, 3)
    demo_cart.add_item("C", "Product C", 30, 2)
    
    print(f"Unique items: {demo_cart.unique_items_count()}")
    print(f"Total quantity: {demo_cart.item_count()}")
    print(f"Average price: ${demo_cart.subtotal() / demo_cart.item_count():.2f}")


if __name__ == "__main__":
    demonstrate_list_basics()
    demonstrate_list_methods()
    demonstrate_list_comprehensions()
    build_shopping_cart_system()
```

---

## 🔒 Section 2: Tuples – Immutable Sequences

Tuples are ordered, immutable collections. Once created, they cannot be changed. This makes them perfect for fixed data like coordinates, configuration, or database records.

**SOLID Principle Applied: Interface Segregation** – Tuples provide a minimal interface for fixed data—no modification methods, only access methods.

**Design Pattern: Value Object Pattern** – Tuples are immutable value objects; equality is based on content, not identity.

```python
"""
TUPLES: IMMUTABLE SEQUENCES

This section covers tuple creation, unpacking, and use cases.
Tuples are immutable - they cannot be changed after creation.

SOLID Principle: Interface Segregation
- Tuples provide only read-only operations
- No methods that modify the tuple

Design Pattern: Value Object Pattern
- Immutable by design
- Equality based on content, not identity
"""

from typing import Tuple, Any, Dict, List
from collections import namedtuple


def demonstrate_tuple_basics():
    """
    Demonstrates fundamental tuple operations.
    
    Tuples are created with parentheses () or tuple() constructor.
    They maintain order but cannot be modified.
    """
    print("=" * 60)
    print("SECTION 2A: TUPLE BASICS")
    print("=" * 60)
    
    # TUPLE CREATION
    print("\n1. CREATING TUPLES")
    print("-" * 40)
    
    # Empty tuple
    empty_tuple = ()
    empty_tuple_constructor = tuple()
    print(f"Empty tuple: {empty_tuple}")
    
    # Tuple with values
    coordinates = (10, 20)
    rgb = (255, 128, 0)
    mixed = (1, "hello", 3.14, True)
    
    print(f"Coordinates: {coordinates}")
    print(f"RGB color: {rgb}")
    print(f"Mixed types: {mixed}")
    
    # Single-element tuple (note the comma!)
    single_element = (42,)  # Without comma, it's just the number 42
    not_a_tuple = (42)
    print(f"Single-element tuple: {single_element} (type: {type(single_element).__name__})")
    print(f"Not a tuple: {not_a_tuple} (type: {type(not_a_tuple).__name__})")
    
    # Tuple without parentheses (tuple packing)
    packed = 1, 2, 3
    print(f"Packed tuple: {packed}")
    
    # From list
    from_list = tuple([1, 2, 3])
    print(f"From list: {from_list}")
    
    # ACCESSING ELEMENTS
    print("\n2. ACCESSING ELEMENTS")
    print("-" * 40)
    
    colors = ("red", "green", "blue", "yellow")
    print(f"Colors: {colors}")
    
    # Indexing (same as lists)
    print(f"First element: {colors[0]}")
    print(f"Last element: {colors[-1]}")
    
    # Slicing (returns new tuple)
    print(f"First 2 elements: {colors[:2]}")
    print(f"Every other: {colors[::2]}")
    
    # IMMUTABILITY DEMONSTRATION
    print("\n3. IMMUTABILITY (Cannot modify)")
    print("-" * 40)
    
    point = (10, 20)
    print(f"Original tuple: {point}")
    
    # This would raise TypeError:
    # point[0] = 99  # TypeError: 'tuple' object does not support item assignment
    
    print("Tuples cannot be modified after creation")
    print("  • Cannot add elements")
    print("  • Cannot remove elements")
    print("  • Cannot change elements")
    
    # TUPLE METHODS
    print("\n4. TUPLE METHODS")
    print("-" * 40)
    
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"Numbers: {numbers}")
    
    # count() - occurrences of a value
    print(f"Count of 2: {numbers.count(2)}")
    
    # index() - first occurrence
    print(f"Index of 3: {numbers.index(3)}")
    print(f"Index of 2 starting from index 2: {numbers.index(2, 2)}")
    
    # MEMBERSHIP TESTING
    print("\n5. MEMBERSHIP TESTING")
    print("-" * 40)
    
    fruits = ("apple", "banana", "cherry")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'grape' in fruits: {'grape' in fruits}")
    print(f"'banana' not in fruits: {'banana' not in fruits}")


def demonstrate_tuple_unpacking():
    """
    Demonstrates tuple unpacking for elegant variable assignment.
    
    Tuple unpacking is one of Python's most elegant features.
    It allows assigning multiple variables at once.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: TUPLE UNPACKING")
    print("=" * 60)
    
    # BASIC UNPACKING
    print("\n1. BASIC UNPACKING")
    print("-" * 40)
    
    # Unpack tuple into variables
    point = (10, 20)
    x, y = point
    print(f"Point: {point}")
    print(f"x = {x}, y = {y}")
    
    # Unpack from function return
    def get_coordinates():
        return (100, 200)
    
    x, y = get_coordinates()
    print(f"From function: x={x}, y={y}")
    
    # SWAPPING VARIABLES (Elegant!)
    print("\n2. SWAPPING VARIABLES")
    print("-" * 40)
    
    a, b = 5, 10
    print(f"Before swap: a={a}, b={b}")
    
    a, b = b, a  # Swap using tuple unpacking
    print(f"After swap: a={a}, b={b}")
    
    # UNPACKING WITH ASTERISK (Extended unpacking)
    print("\n3. EXTENDED UNPACKING (*)")
    print("-" * 40)
    
    numbers = (1, 2, 3, 4, 5)
    
    # Capture first, rest
    first, *rest = numbers
    print(f"First: {first}, Rest: {rest}")
    
    # Capture last, rest
    *rest, last = numbers
    print(f"Rest: {rest}, Last: {last}")
    
    # Capture first, middle, last
    first, *middle, last = numbers
    print(f"First: {first}, Middle: {middle}, Last: {last}")
    
    # UNPACKING NESTED TUPLES
    print("\n4. UNPACKING NESTED TUPLES")
    print("-" * 40)
    
    nested = ((1, 2), (3, 4), (5, 6))
    
    for a, b in nested:
        print(f"a={a}, b={b}")
    
    # Deep unpacking
    data = ("Alice", 28, ("New York", "NY"))
    name, age, (city, state) = data
    print(f"Name: {name}, Age: {age}, City: {city}, State: {state}")
    
    # PRACTICAL USE CASES
    print("\n5. PRACTICAL USE CASES")
    print("-" * 40)
    
    # Iterating over dictionary items
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    for name, score in scores.items():
        print(f"{name}: {score}")
    
    # Enumerate gives index-value pairs
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    
    # Zip combines iterables
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")


def demonstrate_named_tuples():
    """
    Demonstrates namedtuple for self-documenting tuples.
    
    Named tuples give field names to tuple elements,
    making code more readable and self-documenting.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: NAMED TUPLES")
    print("=" * 60)
    
    # CREATING NAMED TUPLES
    print("\n1. CREATING NAMED TUPLES")
    print("-" * 40)
    
    from collections import namedtuple
    
    # Define a named tuple type
    Point = namedtuple('Point', ['x', 'y'])
    RGB = namedtuple('RGB', ['red', 'green', 'blue'])
    Person = namedtuple('Person', ['name', 'age', 'city'])
    
    # Create instances
    p = Point(10, 20)
    color = RGB(255, 128, 0)
    person = Person("Alice", 28, "New York")
    
    print(f"Point: {p}")
    print(f"Color: {color}")
    print(f"Person: {person}")
    
    # ACCESSING FIELDS
    print("\n2. ACCESSING FIELDS")
    print("-" * 40)
    
    # By index (tuple-style)
    print(f"Point[0]: {p[0]}, Point[1]: {p[1]}")
    
    # By name (self-documenting!)
    print(f"Point.x: {p.x}, Point.y: {p.y}")
    print(f"RGB.red: {color.red}, RGB.blue: {color.blue}")
    print(f"Person.name: {person.name}, Person.age: {person.age}")
    
    # NAMED TUPLE METHODS
    print("\n3. NAMED TUPLE METHODS")
    print("-" * 40)
    
    # _asdict() - convert to dictionary
    as_dict = person._asdict()
    print(f"Person as dict: {as_dict}")
    
    # _replace() - create new instance with replaced fields
    older_person = person._replace(age=29)
    print(f"Original: {person}")
    print(f"Modified: {older_person}")
    
    # _fields - get field names
    print(f"Point fields: {Point._fields}")
    print(f"Person fields: {Person._fields}")
    
    # PRACTICAL USE CASE: DATA RECORDS
    print("\n4. PRACTICAL USE CASE: DATA RECORDS")
    print("-" * 40)
    
    # Define record types
    Product = namedtuple('Product', ['sku', 'name', 'price', 'in_stock'])
    Order = namedtuple('Order', ['order_id', 'customer', 'products', 'total'])
    
    # Create product records
    products = [
        Product("TECH-001", "Laptop", 999.99, True),
        Product("TECH-002", "Mouse", 29.99, True),
        Product("TECH-003", "Keyboard", 89.99, False),
    ]
    
    print("Product catalog:")
    for product in products:
        stock_status = "In stock" if product.in_stock else "Out of stock"
        print(f"  {product.sku}: {product.name} - ${product.price} ({stock_status})")
    
    # WHY USE NAMED TUPLES?
    print("\n5. WHY USE NAMED TUPLES?")
    print("-" * 40)
    
    advantages = [
        "✓ More readable than regular tuples (field names document intent)",
        "✓ More memory efficient than classes (no __dict__ per instance)",
        "✓ Immutable by default (prevents accidental modification)",
        "✓ Can be used anywhere a tuple can be used",
        "✓ Support field access by name AND by index",
        "✓ Automatic string representation"
    ]
    
    for advantage in advantages:
        print(advantage)


def build_configuration_system():
    """
    Complete configuration system using tuples for immutable settings.
    
    This demonstrates using tuples for fixed configuration data,
    database connection settings, and API endpoints.
    
    SOLID Principles Applied:
    - Single Responsibility: Configuration is separate from business logic
    - Interface Segregation: Read-only access to config values
    
    Design Patterns:
    - Value Object Pattern: Immutable configuration values
    - Singleton Pattern: Single source of truth for config
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: CONFIGURATION SYSTEM")
    print("=" * 60)
    
    from typing import Tuple, Dict, Any, Optional
    from collections import namedtuple
    
    # Define configuration using named tuples
    DatabaseConfig = namedtuple('DatabaseConfig', [
        'host', 'port', 'database', 'user', 'password', 'pool_size', 'timeout'
    ])
    
    APIConfig = namedtuple('APIConfig', [
        'base_url', 'version', 'timeout', 'max_retries', 'rate_limit'
    ])
    
    FeatureFlags = namedtuple('FeatureFlags', [
        'dark_mode', 'beta_features', 'analytics', 'debug_mode', 'cache_enabled'
    ])
    
    class ConfigurationManager:
        """
        Centralized configuration management.
        
        All configuration is immutable and accessible via properties.
        
        Design Pattern: Singleton Pattern - Single configuration instance
        """
        
        # Database configuration (immutable)
        DATABASE = DatabaseConfig(
            host="localhost",
            port=5432,
            database="metromap_db",
            user="app_user",
            password="secure_password_here",
            pool_size=10,
            timeout=30
        )
        
        # API configuration (immutable)
        API = APIConfig(
            base_url="https://api.metromap.com",
            version="v1",
            timeout=30,
            max_retries=3,
            rate_limit=100
        )
        
        # Feature flags (immutable)
        FEATURES = FeatureFlags(
            dark_mode=True,
            beta_features=False,
            analytics=True,
            debug_mode=False,
            cache_enabled=True
        )
        
        # Environment-specific settings (tuple of tuples)
        ENVIRONMENTS = (
            ("development", "dev.metromap.com", 5432, "dev_db"),
            ("staging", "staging.metromap.com", 5432, "staging_db"),
            ("production", "prod.metromap.com", 5432, "prod_db"),
        )
        
        # API endpoints (tuple of tuples)
        ENDPOINTS = (
            ("users", "/api/v1/users"),
            ("products", "/api/v1/products"),
            ("orders", "/api/v1/orders"),
            ("analytics", "/api/v1/analytics"),
            ("auth", "/api/v1/auth"),
        )
        
        @classmethod
        def get_database_url(cls) -> str:
            """Build database connection URL from configuration."""
            return f"postgresql://{cls.DATABASE.user}:{cls.DATABASE.password}@{cls.DATABASE.host}:{cls.DATABASE.port}/{cls.DATABASE.database}"
        
        @classmethod
        def get_endpoint(cls, name: str) -> Optional[str]:
            """Get API endpoint URL by name."""
            for endpoint_name, url in cls.ENDPOINTS:
                if endpoint_name == name:
                    return f"{cls.API.base_url}{url}"
            return None
        
        @classmethod
        def is_feature_enabled(cls, feature_name: str) -> bool:
            """Check if a feature flag is enabled."""
            return getattr(cls.FEATURES, feature_name, False)
        
        @classmethod
        def get_environment_config(cls, env_name: str) -> Optional[Dict[str, Any]]:
            """Get environment-specific configuration."""
            for env in cls.ENVIRONMENTS:
                if env[0] == env_name:
                    return {
                        "name": env[0],
                        "host": env[1],
                        "port": env[2],
                        "database": env[3]
                    }
            return None
        
        @classmethod
        def validate_config(cls) -> Tuple[bool, List[str]]:
            """
            Validate all configuration settings.
            
            Returns:
                Tuple of (is_valid, list of issues)
            """
            issues = []
            
            # Check database config
            if not cls.DATABASE.host:
                issues.append("Database host not configured")
            if not cls.DATABASE.port or not isinstance(cls.DATABASE.port, int):
                issues.append("Database port must be a valid integer")
            
            # Check API config
            if not cls.API.base_url.startswith(('http://', 'https://')):
                issues.append("API base_url must start with http:// or https://")
            if cls.API.timeout <= 0:
                issues.append("API timeout must be positive")
            
            return len(issues) == 0, issues
    
    # CONSTANTS USING REGULAR TUPLES
    print("\n1. CONSTANT DEFINITIONS")
    print("-" * 40)
    
    # HTTP status codes (immutable constant)
    HTTP_STATUS = (
        (200, "OK"),
        (201, "Created"),
        (400, "Bad Request"),
        (401, "Unauthorized"),
        (403, "Forbidden"),
        (404, "Not Found"),
        (500, "Internal Server Error"),
    )
    
    print("HTTP Status Codes:")
    for code, message in HTTP_STATUS:
        print(f"  {code}: {message}")
    
    # Days of week (immutable constant)
    DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print(f"\nDays of week: {DAYS_OF_WEEK}")
    
    # Month names (immutable constant)
    MONTHS = (
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    )
    print(f"Months: {', '.join(MONTHS)}")
    
    # DEMONSTRATION
    print("\n2. CONFIGURATION DEMONSTRATION")
    print("-" * 40)
    
    # Access database config
    print(f"Database host: {ConfigurationManager.DATABASE.host}")
    print(f"Database port: {ConfigurationManager.DATABASE.port}")
    print(f"Database URL: {ConfigurationManager.get_database_url()}")
    
    # Access API config
    print(f"\nAPI Base URL: {ConfigurationManager.API.base_url}")
    print(f"API Version: {ConfigurationManager.API.version}")
    print(f"Users endpoint: {ConfigurationManager.get_endpoint('users')}")
    print(f"Products endpoint: {ConfigurationManager.get_endpoint('products')}")
    
    # Feature flags
    print(f"\nDark mode enabled: {ConfigurationManager.is_feature_enabled('dark_mode')}")
    print(f"Beta features: {ConfigurationManager.is_feature_enabled('beta_features')}")
    print(f"Debug mode: {ConfigurationManager.is_feature_enabled('debug_mode')}")
    
    # Environment config
    print(f"\nDevelopment environment: {ConfigurationManager.get_environment_config('development')}")
    print(f"Production environment: {ConfigurationManager.get_environment_config('production')}")
    
    # Validate configuration
    is_valid, issues = ConfigurationManager.validate_config()
    print(f"\nConfiguration valid: {is_valid}")
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    
    # IMMUTABILITY BENEFITS
    print("\n3. WHY USE TUPLES FOR CONFIGURATION?")
    print("-" * 40)
    
    benefits = [
        "✓ Configuration cannot be accidentally modified at runtime",
        "✓ Memory efficient (less overhead than dictionaries)",
        "✓ Hashable (can be used as dictionary keys)",
        "✓ Faster access than dictionaries for fixed data",
        "✓ Self-documenting with namedtuple",
        "✓ Thread-safe (immutable = no race conditions)"
    ]
    
    for benefit in benefits:
        print(benefit)
    
    # COMPARISON: TUPLE VS DICT FOR CONFIG
    print("\n4. TUPLE VS DICTIONARY FOR CONFIGURATION")
    print("-" * 40)
    
    # Dictionary config (mutable - can be changed)
    dict_config = {
        "host": "localhost",
        "port": 5432,
        "database": "myapp"
    }
    
    # Tuple config (immutable - cannot be changed)
    tuple_config = (
        ("host", "localhost"),
        ("port", 5432),
        ("database", "myapp"),
    )
    
    # Convert tuple to dict when needed
    dict_from_tuple = dict(tuple_config)
    
    print(f"Dictionary config: {dict_config}")
    print(f"Tuple config: {tuple_config}")
    print(f"Tuple as dict: {dict_from_tuple}")
    print("\nUse tuples for constants, dictionaries for runtime configuration")


if __name__ == "__main__":
    demonstrate_tuple_basics()
    demonstrate_tuple_unpacking()
    demonstrate_named_tuples()
    build_configuration_system()
```

---

## 🔑 Section 3: Dictionaries – Key-Value Power

Dictionaries store data in key-value pairs. They provide O(1) lookup time, making them perfect for fast data retrieval.

**SOLID Principle Applied: Interface Segregation** – Dictionaries provide focused methods for key-based operations: keys(), values(), items(), get(), etc.

**Design Pattern: Repository Pattern** – Dictionaries act as in-memory repositories for fast key-based data access.

```python
"""
DICTIONARIES: KEY-VALUE POWER

This section covers dictionary creation, manipulation, and common patterns.
Dictionaries provide O(1) lookup by key.

SOLID Principle: Interface Segregation
- Dictionary methods each serve a specific purpose
- Keys(), values(), items() for different access patterns

Design Pattern: Repository Pattern
- In-memory key-value store
- Fast O(1) access by key
"""

from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, Counter
from datetime import datetime


def demonstrate_dictionary_basics():
    """
    Demonstrates fundamental dictionary operations.
    
    Dictionaries are created with curly braces {} or dict() constructor.
    Keys must be immutable (strings, numbers, tuples).
    Values can be any type.
    """
    print("=" * 60)
    print("SECTION 3A: DICTIONARY BASICS")
    print("=" * 60)
    
    # DICTIONARY CREATION
    print("\n1. CREATING DICTIONARIES")
    print("-" * 40)
    
    # Empty dictionary
    empty_dict = {}
    empty_dict_constructor = dict()
    print(f"Empty dict: {empty_dict}")
    
    # Dictionary with initial values
    user = {
        "name": "Alice Chen",
        "age": 28,
        "email": "alice@example.com",
        "is_active": True
    }
    print(f"User dict: {user}")
    
    # Using dict() constructor
    product = dict(
        sku="TECH-001",
        name="Laptop",
        price=999.99,
        in_stock=True
    )
    print(f"Product dict: {product}")
    
    # From list of tuples
    pairs = [("name", "Bob"), ("age", 30), ("city", "Boston")]
    from_pairs = dict(pairs)
    print(f"From pairs: {from_pairs}")
    
    # ACCESSING VALUES
    print("\n2. ACCESSING VALUES")
    print("-" * 40)
    
    user = {"name": "Alice", "age": 28, "email": "alice@example.com"}
    
    # Using square brackets (raises KeyError if key doesn't exist)
    print(f"user['name']: {user['name']}")
    
    # Using get() method (returns None or default if key doesn't exist)
    print(f"user.get('age'): {user.get('age')}")
    print(f"user.get('phone'): {user.get('phone')}")
    print(f"user.get('phone', 'N/A'): {user.get('phone', 'N/A')}")
    
    # ADDING AND UPDATING
    print("\n3. ADDING AND UPDATING")
    print("-" * 40)
    
    settings = {"theme": "light", "notifications": True}
    print(f"Original: {settings}")
    
    # Add new key-value pair
    settings["language"] = "en"
    print(f"After adding language: {settings}")
    
    # Update existing key
    settings["theme"] = "dark"
    print(f"After updating theme: {settings}")
    
    # Update multiple values
    settings.update({"font_size": 14, "notifications": False})
    print(f"After update(): {settings}")
    
    # REMOVING VALUES
    print("\n4. REMOVING VALUES")
    print("-" * 40)
    
    data = {"a": 1, "b": 2, "c": 3, "d": 4}
    print(f"Original: {data}")
    
    # pop() - removes and returns value
    removed = data.pop("b")
    print(f"After pop('b'): removed {removed}, dict: {data}")
    
    # popitem() - removes and returns last inserted (Python 3.7+)
    key, value = data.popitem()
    print(f"After popitem(): removed ({key}: {value}), dict: {data}")
    
    # del - deletes key
    del data["c"]
    print(f"After del['c']: {data}")
    
    # clear() - removes all
    data.clear()
    print(f"After clear(): {data}")
    
    # CHECKING EXISTENCE
    print("\n5. CHECKING EXISTENCE")
    print("-" * 40)
    
    user = {"name": "Alice", "age": 28}
    
    print(f"'name' in user: {'name' in user}")
    print(f"'phone' in user: {'phone' in user}")
    print(f"'age' not in user: {'age' not in user}")
    
    # DICTIONARY VIEWS
    print("\n6. DICTIONARY VIEWS")
    print("-" * 40)
    
    product = {"name": "Laptop", "price": 999, "brand": "TechCorp"}
    
    # Keys view
    keys = product.keys()
    print(f"Keys: {keys}")
    
    # Values view
    values = product.values()
    print(f"Values: {values}")
    
    # Items view (key-value pairs)
    items = product.items()
    print(f"Items: {items}")
    
    # Views are dynamic - they update when dict changes
    product["in_stock"] = True
    print(f"After adding 'in_stock': Keys: {product.keys()}")


def demonstrate_dictionary_iteration():
    """
    Demonstrates different ways to iterate over dictionaries.
    
    Dictionaries can be iterated over keys, values, or key-value pairs.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: DICTIONARY ITERATION")
    print("=" * 60)
    
    inventory = {
        "apple": 50,
        "banana": 30,
        "cherry": 25,
        "date": 15,
        "elderberry": 10
    }
    
    print(f"Inventory: {inventory}")
    
    # ITERATING OVER KEYS
    print("\n1. ITERATING OVER KEYS")
    print("-" * 40)
    
    print("Products in stock:")
    for product in inventory:
        print(f"  {product}")
    
    # Explicit keys() method
    for product in inventory.keys():
        print(f"  {product}")
    
    # ITERATING OVER VALUES
    print("\n2. ITERATING OVER VALUES")
    print("-" * 40)
    
    print("Quantities:")
    for quantity in inventory.values():
        print(f"  {quantity}")
    
    # ITERATING OVER KEY-VALUE PAIRS
    print("\n3. ITERATING OVER ITEMS")
    print("-" * 40)
    
    print("Product - Quantity:")
    for product, quantity in inventory.items():
        print(f"  {product}: {quantity}")
    
    # DICTIONARY COMPREHENSIONS
    print("\n4. DICTIONARY COMPREHENSIONS")
    print("-" * 40)
    
    # Square all values
    squares = {x: x**2 for x in range(5)}
    print(f"Squares: {squares}")
    
    # Filter products with quantity > 20
    well_stocked = {p: q for p, q in inventory.items() if q > 20}
    print(f"Well-stocked (>20): {well_stocked}")
    
    # Transform values
    double_quantity = {p: q * 2 for p, q in inventory.items()}
    print(f"Double quantities: {double_quantity}")
    
    # Conditional transformation
    status = {p: "high" if q > 25 else "low" for p, q in inventory.items()}
    print(f"Stock status: {status}")
    
    # PRACTICAL ITERATION PATTERNS
    print("\n5. PRACTICAL ITERATION PATTERNS")
    print("-" * 40)
    
    # Finding max value
    max_product = max(inventory, key=inventory.get)
    print(f"Product with highest quantity: {max_product} ({inventory[max_product]})")
    
    # Sorting by key
    sorted_by_key = dict(sorted(inventory.items()))
    print(f"Sorted by product name: {sorted_by_key}")
    
    # Sorting by value
    sorted_by_value = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
    print(f"Sorted by quantity (descending): {sorted_by_value}")
    
    # Filtering with condition
    filtered = {k: v for k, v in inventory.items() if v >= 20 and len(k) > 4}
    print(f"Filtered (qty>=20 and name length>4): {filtered}")


def demonstrate_advanced_dictionary_patterns():
    """
    Demonstrates advanced dictionary patterns like defaultdict and Counter.
    
    These specialized dictionary types simplify common patterns.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: ADVANCED DICTIONARY PATTERNS")
    print("=" * 60)
    
    # DEFAULTDICT (Auto-initializes missing keys)
    print("\n1. DEFAULTDICT")
    print("-" * 40)
    
    from collections import defaultdict
    
    # List defaultdict (group items)
    groups = defaultdict(list)
    words = ["apple", "banana", "apricot", "blueberry", "avocado"]
    
    for word in words:
        groups[word[0]].append(word)
    
    print("Words grouped by first letter:")
    for letter, word_list in groups.items():
        print(f"  {letter}: {word_list}")
    
    # Int defaultdict (counting)
    counts = defaultdict(int)
    data = ["a", "b", "a", "c", "a", "b", "d"]
    
    for item in data:
        counts[item] += 1
    
    print(f"\nCounts: {dict(counts)}")
    
    # Set defaultdict (unique collections)
    unique_groups = defaultdict(set)
    items = [("fruit", "apple"), ("fruit", "banana"), ("fruit", "apple"), ("color", "red"), ("color", "blue")]
    
    for category, value in items:
        unique_groups[category].add(value)
    
    print(f"Unique groups: {dict(unique_groups)}")
    
    # COUNTER (Counts hashable objects)
    print("\n2. COUNTER")
    print("-" * 40)
    
    from collections import Counter
    
    # Count characters in string
    text = "abracadabra"
    char_counts = Counter(text)
    print(f"Character counts in '{text}': {char_counts}")
    
    # Most common elements
    print(f"Most common character: {char_counts.most_common(1)}")
    print(f"Top 3 characters: {char_counts.most_common(3)}")
    
    # Count list items
    votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "Bob"]
    vote_counts = Counter(votes)
    print(f"\nVote counts: {vote_counts}")
    print(f"Winner: {vote_counts.most_common(1)[0][0]}")
    
    # Counter arithmetic
    inventory = Counter(apple=10, banana=5, cherry=8)
    sold = Counter(apple=3, banana=2, cherry=1)
    remaining = inventory - sold
    print(f"\nInventory: {inventory}")
    print(f"Sold: {sold}")
    print(f"Remaining: {remaining}")
    
    # MERGING DICTIONARIES
    print("\n3. MERGING DICTIONARIES")
    print("-" * 40)
    
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 4, "c": 5, "d": 6}
    
    # Python 3.9+ merge operator |
    merged = dict1 | dict2
    print(f"dict1 | dict2: {merged} (dict2 values override)")
    
    # Update method (modifies in-place)
    dict1_copy = dict1.copy()
    dict1_copy.update(dict2)
    print(f"update(): {dict1_copy}")
    
    # Dictionary unpacking
    unpacked = {**dict1, **dict2}
    print(f"Unpacking: {unpacked}")


def build_user_profile_system():
    """
    Complete user profile system using dictionaries.
    
    This demonstrates a production-ready user management system
    with profiles, preferences, and analytics.
    
    SOLID Principles Applied:
    - Single Responsibility: UserProfile manages user data
    - Open/Closed: Extensible with new profile fields
    
    Design Patterns:
    - Repository Pattern: User storage and retrieval
    - Factory Pattern: User profile creation
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: USER PROFILE SYSTEM")
    print("=" * 60)
    
    from typing import Dict, List, Any, Optional
    from collections import defaultdict
    from datetime import datetime
    import uuid
    
    class UserProfile:
        """
        Manages individual user profile data.
        
        SOLID: Single Responsibility - Manages one user's data
        """
        
        def __init__(self, user_id: str, email: str, name: str):
            """
            Initialize a new user profile.
            
            Args:
                user_id: Unique user identifier
                email: User's email address
                name: User's full name
            """
            self.user_id = user_id
            self.email = email
            self.name = name
            self.created_at = datetime.now()
            self.last_login = None
            self.is_active = True
            self.is_verified = False
            
            # Nested dictionaries for organized data
            self.preferences: Dict[str, Any] = {
                "theme": "light",
                "language": "en",
                "notifications": True,
                "email_frequency": "daily"
            }
            
            self.profile: Dict[str, Any] = {
                "age": None,
                "location": None,
                "bio": "",
                "avatar_url": None,
                "website": None
            }
            
            self.purchase_history: List[Dict[str, Any]] = []
            self.activity_log: List[Dict[str, Any]] = []
        
        def update_preferences(self, updates: Dict[str, Any]) -> 'UserProfile':
            """Update user preferences."""
            self.preferences.update(updates)
            self._log_activity("preferences_updated", {"updates": list(updates.keys())})
            return self
        
        def update_profile(self, updates: Dict[str, Any]) -> 'UserProfile':
            """Update profile information."""
            self.profile.update(updates)
            self._log_activity("profile_updated", {"updates": list(updates.keys())})
            return self
        
        def record_purchase(self, order_id: str, amount: float, items: List[str]) -> 'UserProfile':
            """Record a purchase in user history."""
            purchase = {
                "order_id": order_id,
                "amount": amount,
                "items": items,
                "date": datetime.now().isoformat(),
                "status": "completed"
            }
            self.purchase_history.append(purchase)
            self._log_activity("purchase", {"order_id": order_id, "amount": amount})
            return self
        
        def record_login(self) -> 'UserProfile':
            """Record user login."""
            self.last_login = datetime.now()
            self._log_activity("login", {"timestamp": self.last_login.isoformat()})
            return self
        
        def _log_activity(self, action: str, details: Dict[str, Any]) -> None:
            """Log user activity for analytics."""
            self.activity_log.append({
                "action": action,
                "details": details,
                "timestamp": datetime.now().isoformat()
            })
        
        def get_summary(self) -> Dict[str, Any]:
            """Get user profile summary."""
            total_spent = sum(p["amount"] for p in self.purchase_history)
            
            # Determine user tier based on spending
            if total_spent > 1000:
                tier = "platinum"
            elif total_spent > 500:
                tier = "gold"
            elif total_spent > 100:
                tier = "silver"
            else:
                tier = "bronze"
            
            return {
                "user_id": self.user_id,
                "name": self.name,
                "email": self.email,
                "tier": tier,
                "total_spent": total_spent,
                "order_count": len(self.purchase_history),
                "is_active": self.is_active,
                "is_verified": self.is_verified,
                "preferences": self.preferences,
                "profile": self.profile,
                "created_at": self.created_at.isoformat(),
                "last_login": self.last_login.isoformat() if self.last_login else None
            }
        
        def to_dict(self) -> Dict[str, Any]:
            """Convert user profile to dictionary for storage."""
            return {
                "user_id": self.user_id,
                "email": self.email,
                "name": self.name,
                "created_at": self.created_at.isoformat(),
                "last_login": self.last_login.isoformat() if self.last_login else None,
                "is_active": self.is_active,
                "is_verified": self.is_verified,
                "preferences": self.preferences,
                "profile": self.profile,
                "purchase_history": self.purchase_history,
                "activity_log": self.activity_log
            }
        
        @classmethod
        def from_dict(cls, data: Dict[str, Any]) -> 'UserProfile':
            """Create UserProfile from dictionary data."""
            user = cls(data["user_id"], data["email"], data["name"])
            user.created_at = datetime.fromisoformat(data["created_at"])
            user.last_login = datetime.fromisoformat(data["last_login"]) if data["last_login"] else None
            user.is_active = data["is_active"]
            user.is_verified = data["is_verified"]
            user.preferences = data["preferences"]
            user.profile = data["profile"]
            user.purchase_history = data["purchase_history"]
            user.activity_log = data["activity_log"]
            return user
        
        def __str__(self) -> str:
            """User-friendly string representation."""
            summary = self.get_summary()
            return f"User: {summary['name']} ({summary['email']}) - {summary['tier'].upper()} tier"
    
    class UserRepository:
        """
        Manages user storage and retrieval.
        
        SOLID: Single Responsibility - Manages user collection
        Design Pattern: Repository Pattern - Centralized user storage
        """
        
        def __init__(self):
            self._users: Dict[str, UserProfile] = {}  # user_id -> UserProfile
            self._email_index: Dict[str, str] = {}  # email -> user_id
        
        def create_user(self, email: str, name: str) -> UserProfile:
            """
            Create a new user profile.
            
            Args:
                email: User's email address
                name: User's full name
                
            Returns:
                Created UserProfile instance
            """
            if email in self._email_index:
                raise ValueError(f"User with email {email} already exists")
            
            user_id = str(uuid.uuid4())[:8]
            user = UserProfile(user_id, email, name)
            
            self._users[user_id] = user
            self._email_index[email] = user_id
            
            return user
        
        def get_user(self, user_id: str = None, email: str = None) -> Optional[UserProfile]:
            """
            Get user by ID or email.
            
            Args:
                user_id: User ID to look up
                email: Email to look up
                
            Returns:
                UserProfile or None if not found
            """
            if email:
                user_id = self._email_index.get(email)
            
            if user_id:
                return self._users.get(user_id)
            
            return None
        
        def update_user(self, user: UserProfile) -> None:
            """Update user in repository."""
            self._users[user.user_id] = user
            self._email_index[user.email] = user.user_id
        
        def delete_user(self, user_id: str) -> bool:
            """
            Delete user from repository.
            
            Returns:
                True if deleted, False if not found
            """
            user = self._users.get(user_id)
            if user:
                del self._email_index[user.email]
                del self._users[user_id]
                return True
            return False
        
        def get_all_users(self) -> List[UserProfile]:
            """Get all users."""
            return list(self._users.values())
        
        def get_statistics(self) -> Dict[str, Any]:
            """Get user repository statistics."""
            users = self._users.values()
            
            # Calculate user tiers
            tiers = defaultdict(int)
            for user in users:
                summary = user.get_summary()
                tiers[summary["tier"]] += 1
            
            return {
                "total_users": len(self._users),
                "active_users": sum(1 for u in users if u.is_active),
                "verified_users": sum(1 for u in users if u.is_verified),
                "tiers": dict(tiers),
                "total_revenue": sum(summary["total_spent"] for u in users)
            }
    
    # DEMONSTRATION
    print("\n📦 DEMONSTRATION: USER PROFILE SYSTEM")
    print("-" * 40)
    
    # Create repository
    repo = UserRepository()
    
    # Create users
    print("\n1. CREATING USER PROFILES")
    print("-" * 40)
    
    alice = repo.create_user("alice@example.com", "Alice Chen")
    bob = repo.create_user("bob@example.com", "Bob Smith")
    charlie = repo.create_user("charlie@example.com", "Charlie Brown")
    
    print(f"Created: {alice}")
    print(f"Created: {bob}")
    print(f"Created: {charlie}")
    
    # Update user preferences
    print("\n2. UPDATING PREFERENCES")
    print("-" * 40)
    
    alice.update_preferences({
        "theme": "dark",
        "language": "zh",
        "notifications": False
    })
    
    bob.update_preferences({
        "theme": "light",
        "email_frequency": "weekly"
    })
    
    print(f"Alice preferences: {alice.preferences}")
    print(f"Bob preferences: {bob.preferences}")
    
    # Update profile information
    print("\n3. UPDATING PROFILE INFORMATION")
    print("-" * 40)
    
    alice.update_profile({
        "age": 28,
        "location": "San Francisco, CA",
        "bio": "Software Engineer and Python enthusiast"
    })
    
    print(f"Alice profile: {alice.profile}")
    
    # Record purchases
    print("\n4. RECORDING PURCHASES")
    print("-" * 40)
    
    alice.record_purchase("ORD-001", 1299.99, ["Laptop", "Mouse"])
    alice.record_purchase("ORD-002", 89.99, ["Keyboard"])
    bob.record_purchase("ORD-003", 59.99, ["Headphones"])
    alice.record_purchase("ORD-004", 199.99, ["Monitor"])
    
    print(f"Alice orders: {len(alice.purchase_history)}")
    print(f"Bob orders: {len(bob.purchase_history)}")
    
    # Record logins
    print("\n5. RECORDING LOGINS")
    print("-" * 40)
    
    alice.record_login()
    bob.record_login()
    alice.record_login()
    
    # Get user summaries
    print("\n6. USER SUMMARIES")
    print("-" * 40)
    
    for user in [alice, bob, charlie]:
        summary = user.get_summary()
        print(f"\n{user.name}:")
        print(f"  Tier: {summary['tier'].upper()}")
        print(f"  Total spent: ${summary['total_spent']:.2f}")
        print(f"  Orders: {summary['order_count']}")
        print(f"  Active: {summary['is_active']}")
    
    # Repository statistics
    print("\n7. REPOSITORY STATISTICS")
    print("-" * 40)
    
    stats = repo.get_statistics()
    print(f"Total users: {stats['total_users']}")
    print(f"Active users: {stats['active_users']}")
    print(f"Verified users: {stats['verified_users']}")
    print(f"User tiers: {stats['tiers']}")
    print(f"Total revenue: ${stats['total_revenue']:.2f}")
    
    # Get user by email
    print("\n8. RETRIEVING BY EMAIL")
    print("-" * 40)
    
    retrieved = repo.get_user(email="alice@example.com")
    print(f"Retrieved: {retrieved}")
    
    # Serialization example
    print("\n9. SERIALIZATION (TO DICTIONARY)")
    print("-" * 40)
    
    alice_dict = alice.to_dict()
    print(f"Alice as dict: {list(alice_dict.keys())}")
    
    # Activity log
    print("\n10. ACTIVITY LOG")
    print("-" * 40)
    
    for activity in alice.activity_log[-5:]:  # Last 5 activities
        print(f"  {activity['timestamp']}: {activity['action']}")


if __name__ == "__main__":
    demonstrate_dictionary_basics()
    demonstrate_dictionary_iteration()
    demonstrate_advanced_dictionary_patterns()
    build_user_profile_system()
```

---

## 🎯 Section 4: Sets – Unique and Unordered Collections

Sets store unique, unordered elements. They're perfect for removing duplicates, membership testing, and mathematical set operations.

**SOLID Principle Applied: Interface Segregation** – Sets provide set-specific operations (union, intersection, difference) not found in other collections.

**Design Pattern: Collection Pattern** – Sets implement mathematical set theory operations.

```python
"""
SETS: UNIQUE AND UNORDERED COLLECTIONS

This section covers set creation, operations, and use cases.
Sets store unique elements and support mathematical set operations.

SOLID Principle: Interface Segregation
- Sets provide mathematical set operations (union, intersection)
- Methods specific to uniqueness and membership

Design Pattern: Collection Pattern
- Mathematical set operations
- O(1) membership testing
"""

from typing import Set, List, Any
from collections import Counter


def demonstrate_set_basics():
    """
    Demonstrates fundamental set operations.
    
    Sets are created with curly braces {} or set() constructor.
    They store only unique elements (no duplicates).
    Order is not guaranteed.
    """
    print("=" * 60)
    print("SECTION 4A: SET BASICS")
    print("=" * 60)
    
    # SET CREATION
    print("\n1. CREATING SETS")
    print("-" * 40)
    
    # Empty set (note: {} is empty dict, not set!)
    empty_set = set()
    print(f"Empty set: {empty_set} (type: {type(empty_set).__name__})")
    
    # Set with values
    fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate removed
    print(f"Fruits set: {fruits} (duplicate 'apple' removed)")
    
    # From list (removes duplicates)
    numbers_list = [1, 2, 2, 3, 3, 3, 4]
    numbers_set = set(numbers_list)
    print(f"List: {numbers_list}")
    print(f"Set from list: {numbers_set}")
    
    # From string (unique characters)
    char_set = set("abracadabra")
    print(f"Unique chars in 'abracadabra': {char_set}")
    
    # UNIQUENESS PROPERTY
    print("\n2. UNIQUENESS (No Duplicates)")
    print("-" * 40)
    
    duplicates = [1, 1, 2, 2, 3, 3, 1, 2, 3]
    unique = set(duplicates)
    print(f"List with duplicates: {duplicates}")
    print(f"Set (unique only): {unique}")
    
    # ADDING AND REMOVING
    print("\n3. ADDING AND REMOVING")
    print("-" * 40)
    
    colors = {"red", "green", "blue"}
    print(f"Original: {colors}")
    
    # add() - adds single element
    colors.add("yellow")
    print(f"After add('yellow'): {colors}")
    
    # Adding duplicate does nothing
    colors.add("red")
    print(f"After add('red') again: {colors} (unchanged)")
    
    # update() - adds multiple elements
    colors.update(["purple", "orange", "pink"])
    print(f"After update(): {colors}")
    
    # remove() - removes element (raises KeyError if not found)
    colors.remove("pink")
    print(f"After remove('pink'): {colors}")
    
    # discard() - removes if present (no error if not)
    colors.discard("brown")
    print(f"After discard('brown'): {colors}")
    
    # pop() - removes and returns arbitrary element
    removed = colors.pop()
    print(f"After pop(): removed '{removed}', remaining: {colors}")
    
    # clear() - removes all
    colors.clear()
    print(f"After clear(): {colors}")
    
    # MEMBERSHIP TESTING (O(1) - very fast!)
    print("\n4. MEMBERSHIP TESTING (O(1))")
    print("-" * 40)
    
    valid_colors = {"red", "green", "blue", "yellow", "purple"}
    
    test_colors = ["red", "orange", "blue", "brown"]
    
    for color in test_colors:
        is_valid = color in valid_colors
        print(f"Is '{color}' valid? {is_valid}")
    
    # LENGTH AND ITERATION
    print("\n5. LENGTH AND ITERATION")
    print("-" * 40)
    
    tags = {"python", "programming", "tutorial", "coding"}
    print(f"Number of tags: {len(tags)}")
    
    print("Iterating over tags:")
    for tag in tags:
        print(f"  {tag}")
    
    # SET COMPREHENSIONS
    print("\n6. SET COMPREHENSIONS")
    print("-" * 40)
    
    # Square numbers
    squares = {x**2 for x in range(10)}
    print(f"Squares: {squares}")
    
    # Filter even numbers
    evens = {x for x in range(20) if x % 2 == 0}
    print(f"Even numbers: {evens}")
    
    # Unique characters from list of words
    words = ["hello", "world", "python", "code"]
    unique_chars = {char for word in words for char in word}
    print(f"Unique characters: {unique_chars}")


def demonstrate_set_operations():
    """
    Demonstrates mathematical set operations.
    
    Sets support union, intersection, difference, and symmetric difference.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: SET OPERATIONS")
    print("=" * 60)
    
    # Define sample sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # UNION (all elements from both sets)
    print("\n1. UNION (| or union())")
    print("-" * 40)
    
    union_operator = set_a | set_b
    union_method = set_a.union(set_b)
    print(f"Union using |: {union_operator}")
    print(f"Union using union(): {union_method}")
    
    # INTERSECTION (elements in both sets)
    print("\n2. INTERSECTION (& or intersection())")
    print("-" * 40)
    
    intersection_operator = set_a & set_b
    intersection_method = set_a.intersection(set_b)
    print(f"Intersection using &: {intersection_operator}")
    print(f"Intersection using intersection(): {intersection_method}")
    
    # DIFFERENCE (elements in A but not in B)
    print("\n3. DIFFERENCE (- or difference())")
    print("-" * 40)
    
    difference_operator = set_a - set_b
    difference_method = set_a.difference(set_b)
    print(f"Difference A - B: {difference_operator}")
    print(f"Difference B - A: {set_b - set_a}")
    
    # SYMMETRIC DIFFERENCE (elements in either, but not both)
    print("\n4. SYMMETRIC DIFFERENCE (^ or symmetric_difference())")
    print("-" * 40)
    
    sym_diff_operator = set_a ^ set_b
    sym_diff_method = set_a.symmetric_difference(set_b)
    print(f"Symmetric difference using ^: {sym_diff_operator}")
    print(f"Symmetric difference using symmetric_difference(): {sym_diff_method}")
    
    # SUBSET AND SUPERSET
    print("\n5. SUBSET AND SUPERSET")
    print("-" * 40)
    
    set_c = {1, 2, 3}
    set_d = {1, 2, 3, 4, 5}
    
    print(f"Set C: {set_c}")
    print(f"Set D: {set_d}")
    print(f"C is subset of D? {set_c.issubset(set_d)}")
    print(f"D is superset of C? {set_d.issuperset(set_c)}")
    print(f"C is proper subset? {set_c < set_d}")
    
    # DISJOINT (no common elements)
    print("\n6. DISJOINT (no common elements)")
    print("-" * 40)
    
    set_e = {1, 2, 3}
    set_f = {4, 5, 6}
    set_g = {3, 4, 5}
    
    print(f"Set E: {set_e}, Set F: {set_f}")
    print(f"Are E and F disjoint? {set_e.isdisjoint(set_f)}")
    print(f"Are E and G disjoint? {set_e.isdisjoint(set_g)}")
    
    # PRACTICAL EXAMPLES
    print("\n7. PRACTICAL EXAMPLES")
    print("-" * 40)
    
    # Find common interests
    alice_interests = {"reading", "swimming", "coding", "hiking"}
    bob_interests = {"coding", "gaming", "hiking", "photography"}
    
    common = alice_interests & bob_interests
    unique_to_alice = alice_interests - bob_interests
    all_interests = alice_interests | bob_interests
    
    print(f"Alice's interests: {alice_interests}")
    print(f"Bob's interests: {bob_interests}")
    print(f"Common interests: {common}")
    print(f"Unique to Alice: {unique_to_alice}")
    print(f"All interests: {all_interests}")


def build_analytics_system():
    """
    Complete website analytics system using sets.
    
    This demonstrates using sets for tracking unique visitors,
    finding overlaps, and analyzing user behavior.
    
    SOLID Principles Applied:
    - Single Responsibility: Each analytics function has one purpose
    - Open/Closed: New metrics can be added
    
    Design Patterns:
    - Collection Pattern: Set-based visitor tracking
    - Singleton Pattern: Single analytics instance
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: WEBSITE ANALYTICS SYSTEM")
    print("=" * 60)
    
    from typing import Set, Dict, List, Optional
    from collections import defaultdict
    from datetime import datetime, date
    
    class WebsiteAnalytics:
        """
        Tracks website visitors and behavior using sets.
        
        Sets are perfect for unique visitor tracking because:
        - Automatic duplicate elimination
        - Fast membership testing (O(1))
        - Set operations for overlap analysis
        
        Design Pattern: Singleton Pattern - Single analytics instance
        """
        
        def __init__(self):
            # Daily unique visitors (date -> set of user_ids)
            self.daily_visitors: Dict[str, Set[str]] = defaultdict(set)
            
            # Page views (page -> set of user_ids)
            self.page_views: Dict[str, Set[str]] = defaultdict(set)
            
            # User sessions (user_id -> list of actions)
            self.sessions: Dict[str, List[Dict]] = defaultdict(list)
            
            # Conversion events (event_type -> count)
            self.conversions: Dict[str, int] = defaultdict(int)
            
            # Referral sources (source -> set of user_ids)
            self.referrals: Dict[str, Set[str]] = defaultdict(set)
        
        def track_visit(self, user_id: str, page: str, 
                        referrer: Optional[str] = None,
                        user_agent: Optional[str] = None) -> 'WebsiteAnalytics':
            """
            Track a page visit.
            
            Args:
                user_id: Unique user identifier
                page: Page URL or name
                referrer: Where the user came from
                user_agent: Browser/device information
                
            Returns:
                Self for method chaining
            """
            today = date.today().isoformat()
            
            # Track daily unique visitor
            self.daily_visitors[today].add(user_id)
            
            # Track page view
            self.page_views[page].add(user_id)
            
            # Track referral
            if referrer:
                self.referrals[referrer].add(user_id)
            
            # Track session
            self.sessions[user_id].append({
                "page": page,
                "timestamp": datetime.now().isoformat(),
                "user_agent": user_agent
            })
            
            return self
        
        def track_conversion(self, event_type: str, user_id: str, 
                            value: Optional[float] = None) -> 'WebsiteAnalytics':
            """
            Track a conversion event (purchase, signup, etc.).
            
            Args:
                event_type: Type of conversion
                user_id: User who converted
                value: Optional monetary value
                
            Returns:
                Self for method chaining
            """
            self.conversions[event_type] += 1
            print(f"  Conversion: {event_type} by {user_id}" + 
                  (f" (${value:.2f})" if value else ""))
            return self
        
        def get_daily_unique_visitors(self, date_str: Optional[str] = None) -> int:
            """Get number of unique visitors for a specific date."""
            if not date_str:
                date_str = date.today().isoformat()
            return len(self.daily_visitors.get(date_str, set()))
        
        def get_weekly_active_users(self) -> int:
            """Get unique visitors in the last 7 days."""
            week_ago = date.today().replace(day=date.today().day - 7).isoformat()
            weekly_users = set()
            
            for date_str, visitors in self.daily_visitors.items():
                if date_str >= week_ago:
                    weekly_users.update(visitors)
            
            return len(weekly_users)
        
        def get_page_overlap(self, page1: str, page2: str) -> Set[str]:
            """Find users who visited both pages."""
            visitors1 = self.page_views.get(page1, set())
            visitors2 = self.page_views.get(page2, set())
            return visitors1 & visitors2
        
        def get_conversion_funnel(self, pages: List[str]) -> List[Dict]:
            """
            Analyze conversion funnel through page sequence.
            
            Args:
                pages: Ordered list of pages in funnel
                
            Returns:
                List of funnel step data
            """
            funnel_data = []
            previous_visitors = None
            
            for step, page in enumerate(pages, 1):
                visitors = self.page_views.get(page, set())
                
                if previous_visitors is None:
                    # First step
                    count = len(visitors)
                    funnel_data.append({
                        "step": step,
                        "page": page,
                        "visitors": count,
                        "conversion_rate": 100.0
                    })
                else:
                    # Subsequent steps - users who made it from previous step
                    converted = len(visitors & previous_visitors)
                    rate = (converted / len(previous_visitors)) * 100 if previous_visitors else 0
                    funnel_data.append({
                        "step": step,
                        "page": page,
                        "visitors": converted,
                        "conversion_rate": rate
                    })
                
                previous_visitors = visitors
            
            return funnel_data
        
        def get_user_path(self, user_id: str) -> List[str]:
            """Get the sequence of pages visited by a user."""
            pages = []
            for action in self.sessions.get(user_id, []):
                pages.append(action["page"])
            return pages
        
        def get_popular_pages(self, limit: int = 10) -> List[tuple]:
            """Get most visited pages by unique visitor count."""
            page_counts = [(page, len(visitors)) for page, visitors in self.page_views.items()]
            page_counts.sort(key=lambda x: x[1], reverse=True)
            return page_counts[:limit]
        
        def get_referral_summary(self) -> Dict[str, int]:
            """Get summary of referral sources."""
            return {source: len(users) for source, users in self.referrals.items()}
        
        def get_retention_rate(self, cohort_date: str, days_later: int) -> float:
            """
            Calculate user retention rate.
            
            Args:
                cohort_date: Date of user acquisition (YYYY-MM-DD)
                days_later: Days after acquisition to check
                
            Returns:
                Retention rate as percentage
            """
            cohort_visitors = self.daily_visitors.get(cohort_date, set())
            
            from datetime import timedelta
            target_date = (datetime.fromisoformat(cohort_date) + 
                          timedelta(days=days_later)).date().isoformat()
            
            retained_visitors = self.daily_visitors.get(target_date, set())
            
            if not cohort_visitors:
                return 0.0
            
            retained_count = len(cohort_visitors & retained_visitors)
            return (retained_count / len(cohort_visitors)) * 100
        
        def generate_report(self) -> str:
            """Generate comprehensive analytics report."""
            report_lines = []
            report_lines.append("=" * 60)
            report_lines.append("WEBSITE ANALYTICS REPORT")
            report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report_lines.append("=" * 60)
            
            # Visitor statistics
            today_visitors = self.get_daily_unique_visitors()
            weekly_visitors = self.get_weekly_active_users()
            
            report_lines.append("\n📊 VISITOR STATISTICS:")
            report_lines.append(f"  Today's unique visitors: {today_visitors}")
            report_lines.append(f"  Weekly active users: {weekly_visitors}")
            
            # Popular pages
            report_lines.append("\n📈 POPULAR PAGES:")
            for page, count in self.get_popular_pages(5):
                report_lines.append(f"  {page}: {count} unique visitors")
            
            # Referrals
            report_lines.append("\n🔗 REFERRAL SOURCES:")
            for source, count in self.get_referral_summary().items():
                report_lines.append(f"  {source}: {count} users")
            
            # Conversions
            if self.conversions:
                report_lines.append("\n💰 CONVERSIONS:")
                for event, count in self.conversions.items():
                    report_lines.append(f"  {event}: {count}")
            
            report_lines.append("\n" + "=" * 60)
            
            return "\n".join(report_lines)
    
    # DEMONSTRATION
    print("\n📊 DEMONSTRATION: WEBSITE ANALYTICS")
    print("-" * 40)
    
    # Create analytics instance
    analytics = WebsiteAnalytics()
    
    # Simulate website traffic
    print("\n1. TRACKING VISITS")
    print("-" * 40)
    
    # Day 1 traffic
    analytics.track_visit("user_001", "home", referrer="google")
    analytics.track_visit("user_002", "home", referrer="direct")
    analytics.track_visit("user_001", "products")
    analytics.track_visit("user_003", "home", referrer="facebook")
    analytics.track_visit("user_001", "pricing")
    analytics.track_visit("user_002", "products")
    analytics.track_visit("user_004", "home", referrer="google")
    
    # Day 2 traffic (simulate different date)
    # Note: In production, date would be handled automatically
    print("  Simulated 7 days of traffic...")
    
    # Track conversions
    print("\n2. TRACKING CONVERSIONS")
    print("-" * 40)
    analytics.track_conversion("signup", "user_003")
    analytics.track_conversion("purchase", "user_001", 99.99)
    analytics.track_conversion("purchase", "user_002", 49.99)
    
    # Get analytics
    print("\n3. VISITOR STATISTICS")
    print("-" * 40)
    print(f"Today's unique visitors: {analytics.get_daily_unique_visitors()}")
    print(f"Weekly active users: {analytics.get_weekly_active_users()}")
    
    # Page overlap analysis
    print("\n4. PAGE OVERLAP ANALYSIS")
    print("-" * 40)
    overlap = analytics.get_page_overlap("home", "products")
    print(f"Users who visited both Home and Products: {len(overlap)}")
    print(f"Users: {overlap}")
    
    # Conversion funnel
    print("\n5. CONVERSION FUNNEL")
    print("-" * 40)
    funnel = analytics.get_conversion_funnel(["home", "products", "pricing", "purchase"])
    
    for step in funnel:
        print(f"  Step {step['step']} ({step['page']}): {step['visitors']} users ({step['conversion_rate']:.1f}%)")
    
    # Popular pages
    print("\n6. POPULAR PAGES")
    print("-" * 40)
    for page, count in analytics.get_popular_pages():
        print(f"  {page}: {count} unique visitors")
    
    # Referral analysis
    print("\n7. REFERRAL ANALYSIS")
    print("-" * 40)
    for source, count in analytics.get_referral_summary().items():
        print(f"  {source}: {count} users")
    
    # User path analysis
    print("\n8. USER PATH ANALYSIS")
    print("-" * 40)
    user_path = analytics.get_user_path("user_001")
    print(f"User 001 path: {' → '.join(user_path)}")
    
    # Complete report
    print("\n9. COMPLETE REPORT")
    print("-" * 40)
    report = analytics.generate_report()
    print(report)
    
    # SET OPERATIONS IN ANALYTICS
    print("\n10. SET OPERATIONS FOR ADVANCED ANALYTICS")
    print("-" * 40)
    
    # Create sample data for demonstration
    mobile_users = {"user_001", "user_002", "user_005"}
    desktop_users = {"user_002", "user_003", "user_004"}
    converted_users = {"user_001", "user_003"}
    
    print(f"Mobile users: {mobile_users}")
    print(f"Desktop users: {desktop_users}")
    print(f"Converted users: {converted_users}")
    
    # Find users who converted on mobile
    mobile_conversions = mobile_users & converted_users
    print(f"Mobile conversions: {mobile_conversions}")
    
    # Find users who used both mobile and desktop
    cross_platform = mobile_users & desktop_users
    print(f"Cross-platform users: {cross_platform}")
    
    # Find users who haven't converted yet
    not_converted = (mobile_users | desktop_users) - converted_users
    print(f"Users not converted: {not_converted}")
    
    # Conversion rate by platform
    mobile_rate = len(mobile_users & converted_users) / len(mobile_users) * 100 if mobile_users else 0
    desktop_rate = len(desktop_users & converted_users) / len(desktop_users) * 100 if desktop_users else 0
    
    print(f"Mobile conversion rate: {mobile_rate:.1f}%")
    print(f"Desktop conversion rate: {desktop_rate:.1f}%")


if __name__ == "__main__":
    demonstrate_set_basics()
    demonstrate_set_operations()
    build_analytics_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Lists** – Ordered, mutable sequences. Perfect for shopping carts, playlists, and any collection that changes over time. Methods: append(), remove(), sort(), pop().

- **Tuples** – Ordered, immutable sequences. Perfect for fixed data like coordinates, configuration, and database records. Use namedtuple for self-documenting code.

- **Dictionaries** – Key-value pairs with O(1) lookup. Perfect for user profiles, caches, and fast data retrieval. Methods: keys(), values(), items(), get().

- **Sets** – Unordered collections of unique elements. Perfect for unique visitor tracking, duplicate removal, and membership testing. Operations: union (|), intersection (&), difference (-).

- **SOLID Principles Applied** – Single Responsibility (each collection type has one purpose), Interface Segregation (specialized methods per type), Liskov Substitution (consistent interfaces).

- **Design Patterns Used** – Collection Pattern (uniform access), Value Object Pattern (immutable tuples), Repository Pattern (dictionary storage), Builder Pattern (method chaining), Singleton Pattern (single analytics instance).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Variables & Data Types – The Rails of Python

- **📚 Series A Catalog:** Foundations Station – View all 7 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 2 | 5 | 29% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **7** | **45** | **13%** |

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap: Reading the Map
4. Series 0, Story 4: The 2026 Python Metromap: Avoiding Derailments
5. Series 0, Story 5: The 2026 Python Metromap: From Passenger to Driver
6. Series A, Story 1: The 2026 Python Metromap: Variables & Data Types – The Rails of Python
7. Series A, Story 2: The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets

**Next Story:** Series A, Story 3: The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More

---

## 📝 Your Invitation

You've mastered collections. Now build something with what you've learned:

1. **Build a shopping cart** – Use lists to store items. Implement add, remove, and quantity update operations.

2. **Create a user profile system** – Use dictionaries to store user data. Add nested preferences and history.

3. **Build an analytics dashboard** – Use sets to track unique visitors. Calculate conversion funnels.

4. **Create configuration manager** – Use tuples for immutable settings. Use namedtuple for self-documenting config.

5. **Combine collection types** – Build an order system with list of dicts, each containing product details.

**You've mastered collections. Next stop: Operators!**

---

*Found this helpful? Clap, comment, and share what you built with collections. Next stop: Operators!* 🚇