# The 2026 Python Metromap: Dictionaries – Key-Value Power

## Series C: Data Structures Express | Story 3 of 5

![The 2026 Python Metromap/images/Dictionaries – Key-Value Power](images/Dictionaries – Key-Value Power.png)

## 📖 Introduction

**Welcome to the third stop on the Data Structures Express Line.**

You've mastered lists for ordered sequences and tuples for immutable collections. But what about when you need to look up values by a meaningful key rather than a numeric index? What about when you need to store user profiles by username, product catalogs by SKU, or caches by request ID?

That's where dictionaries come in.

Dictionaries are unordered, mutable collections that store key-value pairs. They provide O(1) average-case lookup time, making them incredibly fast for retrieving values by key. Unlike lists where you search by position, dictionaries let you access data by meaningful identifiers—like looking up a word in a dictionary (hence the name). Each key must be unique and immutable (strings, numbers, tuples), while values can be any type.

This story—**The 2026 Python Metromap: Dictionaries – Key-Value Power**—is your guide to mastering Python dictionaries. We'll build a complete user profile system with fast lookup by username. We'll create a product catalog with search and filtering. We'll implement a caching system with LRU (Least Recently Used) eviction. We'll build a dependency injection container. And we'll create a complete e-commerce inventory system with nested dictionaries and advanced lookups.

**Let's map the keys.**

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

### Series C: Data Structures Express (5 Stories)

- 📋 **The 2026 Python Metromap: Lists – Ordered & Mutable** – Todo application; playlist manager; shopping cart system.

- 🔒 **The 2026 Python Metromap: Tuples – Immutable Collections** – GPS coordinates; database records; immutable configuration.

- 🔑 **The 2026 Python Metromap: Dictionaries – Key-Value Power** – User profile system; product catalog; caching system; dependency injection. **⬅️ YOU ARE HERE**

- 🎯 **The 2026 Python Metromap: Sets – Unique & Fast** – Duplicate removal; friend recommendation engine; common visitor detection. 🔜 *Up Next*

- 📝 **The 2026 Python Metromap: Comprehensions – One-Line Power** – Data transformation pipelines; filtered iterations; nested structure creation.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔑 Section 1: Dictionary Fundamentals – Creation, Access, and Modification

Dictionaries store key-value pairs with O(1) lookup time. Keys must be immutable and unique.

**SOLID Principle Applied: Single Responsibility** – Each dictionary maps keys to values; methods handle specific operations.

**Design Pattern: Repository Pattern** – Dictionaries act as in-memory key-value stores.

```python
"""
DICTIONARY FUNDAMENTALS: CREATION, ACCESS, AND MODIFICATION

This section covers the basics of creating, accessing, and modifying dictionaries.

SOLID Principle: Single Responsibility
- Each dictionary maps keys to values
- Methods handle specific operations

Design Pattern: Repository Pattern
- In-memory key-value storage
"""

from typing import Dict, Any, Optional, List
from collections import defaultdict
import time


def demonstrate_dictionary_creation():
    """
    Demonstrates different ways to create dictionaries.
    
    Dictionaries are created with curly braces {} or dict() constructor.
    Keys must be immutable (strings, numbers, tuples).
    """
    print("=" * 60)
    print("SECTION 1A: CREATING DICTIONARIES")
    print("=" * 60)
    
    # EMPTY DICTIONARIES
    print("\n1. CREATING EMPTY DICTIONARIES")
    print("-" * 40)
    
    empty_braces = {}
    empty_constructor = dict()
    
    print(f"  empty_braces: {empty_braces} (type: {type(empty_braces).__name__})")
    print(f"  empty_constructor: {empty_constructor}")
    
    # DICTIONARY WITH INITIAL VALUES
    print("\n2. DICTIONARY WITH INITIAL VALUES")
    print("-" * 40)
    
    user = {
        "name": "Alice Chen",
        "age": 28,
        "email": "alice@example.com",
        "is_active": True
    }
    print(f"  user: {user}")
    
    # USING DICT() CONSTRUCTOR WITH KEYWORDS
    print("\n3. USING DICT() WITH KEYWORDS")
    print("-" * 40)
    
    product = dict(
        sku="TECH-001",
        name="Laptop",
        price=999.99,
        in_stock=True
    )
    print(f"  product: {product}")
    
    # FROM LIST OF TUPLES
    print("\n4. FROM LIST OF TUPLES")
    print("-" * 40)
    
    pairs = [("name", "Bob"), ("age", 30), ("city", "Boston")]
    from_pairs = dict(pairs)
    print(f"  dict([('name', 'Bob'), ('age', 30)]): {from_pairs}")
    
    # USING ZIP TO CREATE DICTIONARY
    print("\n5. USING ZIP TO CREATE DICTIONARY")
    print("-" * 40)
    
    keys = ["name", "age", "city"]
    values = ["Charlie", 25, "Chicago"]
    zipped_dict = dict(zip(keys, values))
    print(f"  dict(zip({keys}, {values})): {zipped_dict}")
    
    # DICTIONARY COMPREHENSION
    print("\n6. DICTIONARY COMPREHENSION")
    print("-" * 40)
    
    squares = {x: x**2 for x in range(5)}
    print(f"  {{x: x**2 for x in range(5)}}: {squares}")
    
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    print(f"  Even squares: {even_squares}")


def demonstrate_dictionary_access():
    """
    Demonstrates accessing values in dictionaries.
    
    Use square brackets or get() method for safe access.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: ACCESSING DICTIONARY VALUES")
    print("=" * 60)
    
    user = {
        "name": "Alice Chen",
        "age": 28,
        "email": "alice@example.com",
        "is_active": True,
        "preferences": {
            "theme": "dark",
            "language": "en"
        }
    }
    
    print(f"  User dict: {user}")
    
    # USING SQUARE BRACKETS (raises KeyError if key doesn't exist)
    print("\n1. USING SQUARE BRACKETS []")
    print("-" * 40)
    
    print(f"  user['name']: {user['name']}")
    print(f"  user['age']: {user['age']}")
    
    try:
        print(f"  user['phone']: {user['phone']}")
    except KeyError as e:
        print(f"  Error: {e} - Key not found!")
    
    # USING GET() METHOD (returns None or default if key doesn't exist)
    print("\n2. USING GET() METHOD")
    print("-" * 40)
    
    print(f"  user.get('name'): {user.get('name')}")
    print(f"  user.get('phone'): {user.get('phone')}")
    print(f"  user.get('phone', 'N/A'): {user.get('phone', 'N/A')}")
    
    # ACCESSING NESTED DICTIONARIES
    print("\n3. ACCESSING NESTED DICTIONARIES")
    print("-" * 40)
    
    print(f"  user['preferences']['theme']: {user['preferences']['theme']}")
    print(f"  user.get('preferences', {}).get('language'): {user.get('preferences', {}).get('language')}")
    
    # KEYS, VALUES, AND ITEMS VIEWS
    print("\n4. DICTIONARY VIEWS (keys, values, items)")
    print("-" * 40)
    
    print(f"  user.keys(): {list(user.keys())}")
    print(f"  user.values(): {list(user.values())}")
    print(f"  user.items(): {list(user.items())}")
    
    # CHECKING KEY EXISTENCE
    print("\n5. CHECKING KEY EXISTENCE")
    print("-" * 40)
    
    print(f"  'name' in user: {'name' in user}")
    print(f"  'phone' in user: {'phone' in user}")
    print(f"  'email' not in user: {'email' not in user}")
    
    # GETTING DICTIONARY LENGTH
    print("\n6. DICTIONARY LENGTH")
    print("-" * 40)
    
    print(f"  len(user): {len(user)}")
    
    # ITERATING OVER DICTIONARIES
    print("\n7. ITERATING OVER DICTIONARIES")
    print("-" * 40)
    
    print("  Iterating over keys:")
    for key in user:
        print(f"    {key}: {user[key]}")
    
    print("  Iterating over items (key-value pairs):")
    for key, value in user.items():
        print(f"    {key}: {value}")


def demonstrate_dictionary_modification():
    """
    Demonstrates modifying dictionaries (adding, updating, deleting).
    
    Dictionaries are mutable and can be changed after creation.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: MODIFYING DICTIONARIES")
    print("=" * 60)
    
    settings = {"theme": "light", "notifications": True, "language": "en"}
    print(f"  Original: {settings}")
    
    # ADDING NEW KEY-VALUE PAIRS
    print("\n1. ADDING NEW KEY-VALUE PAIRS")
    print("-" * 40)
    
    settings["font_size"] = 14
    settings["auto_save"] = True
    print(f"  After adding: {settings}")
    
    # UPDATING EXISTING VALUES
    print("\n2. UPDATING EXISTING VALUES")
    print("-" * 40)
    
    settings["theme"] = "dark"
    settings["notifications"] = False
    print(f"  After updating: {settings}")
    
    # USING UPDATE() METHOD
    print("\n3. USING UPDATE() METHOD")
    print("-" * 40)
    
    settings.update({"language": "es", "timezone": "UTC", "new_feature": True})
    print(f"  After update(): {settings}")
    
    # USING SETDEFAULT() (sets value only if key doesn't exist)
    print("\n4. USING SETDEFAULT()")
    print("-" * 40)
    
    value = settings.setdefault("theme", "default_theme")
    print(f"  settings.setdefault('theme', 'default_theme'): {value}")
    
    value = settings.setdefault("new_key", "default_value")
    print(f"  settings.setdefault('new_key', 'default_value'): {value}")
    print(f"  After setdefault: {settings}")
    
    # DELETING ITEMS
    print("\n5. DELETING ITEMS")
    print("-" * 40)
    
    # Using del
    del settings["new_key"]
    print(f"  After del['new_key']: {settings}")
    
    # Using pop() - removes and returns value
    removed = settings.pop("auto_save")
    print(f"  pop('auto_save'): removed '{removed}', dict: {settings}")
    
    # Using popitem() - removes and returns last inserted (Python 3.7+)
    key, value = settings.popitem()
    print(f"  popitem(): removed ({key}: {value}), dict: {settings}")
    
    # Using clear() - removes all items
    temp_dict = {"a": 1, "b": 2}
    temp_dict.clear()
    print(f"  clear(): {temp_dict}")


def demonstrate_dictionary_comprehensions():
    """
    Demonstrates dictionary comprehensions for concise creation.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: DICTIONARY COMPREHENSIONS")
    print("=" * 60)
    
    # BASIC COMPREHENSION
    print("\n1. BASIC DICTIONARY COMPREHENSION")
    print("-" * 40)
    
    squares = {x: x**2 for x in range(10)}
    print(f"  Squares: {squares}")
    
    # WITH CONDITIONAL FILTERING
    print("\n2. WITH CONDITIONAL FILTERING")
    print("-" * 40)
    
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    print(f"  Even squares: {even_squares}")
    
    # TRANSFORMING EXISTING DICTIONARY
    print("\n3. TRANSFORMING EXISTING DICTIONARY")
    print("-" * 40)
    
    original = {"a": 1, "b": 2, "c": 3, "d": 4}
    doubled = {k: v * 2 for k, v in original.items()}
    print(f"  Original: {original}")
    print(f"  Doubled: {doubled}")
    
    # FILTERING DICTIONARY ITEMS
    print("\n4. FILTERING DICTIONARY ITEMS")
    print("-" * 40)
    
    filtered = {k: v for k, v in original.items() if v > 2}
    print(f"  Values > 2: {filtered}")
    
    # SWAPPING KEYS AND VALUES
    print("\n5. SWAPPING KEYS AND VALUES")
    print("-" * 40)
    
    original = {"apple": 5, "banana": 3, "cherry": 8}
    swapped = {v: k for k, v in original.items()}
    print(f"  Original: {original}")
    print(f"  Swapped: {swapped}")
    
    # NESTED COMPREHENSIONS
    print("\n6. NESTED DICTIONARY COMPREHENSION")
    print("-" * 40)
    
    matrix = {i: {j: i * j for j in range(3)} for i in range(3)}
    print("  Multiplication table:")
    for i, row in matrix.items():
        print(f"    {row}")


def demonstrate_defaultdict():
    """
    Demonstrates defaultdict for automatic default values.
    
    defaultdict automatically creates missing keys with a default value.
    """
    print("\n" + "=" * 60)
    print("SECTION 1E: DEFAULTDICT – AUTO-INITIALIZING DICTIONARIES")
    print("=" * 60)
    
    from collections import defaultdict
    
    # DEFAULTDICT WITH INT (for counting)
    print("\n1. DEFAULTDICT WITH INT (Counting)")
    print("-" * 40)
    
    word_counts = defaultdict(int)
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    
    for word in words:
        word_counts[word] += 1
    
    print(f"  Word counts: {dict(word_counts)}")
    
    # DEFAULTDICT WITH LIST (for grouping)
    print("\n2. DEFAULTDICT WITH LIST (Grouping)")
    print("-" * 40)
    
    groups = defaultdict(list)
    items = [("fruit", "apple"), ("fruit", "banana"), ("fruit", "cherry"),
             ("color", "red"), ("color", "blue"), ("color", "green")]
    
    for category, value in items:
        groups[category].append(value)
    
    print(f"  Grouped items: {dict(groups)}")
    
    # DEFAULTDICT WITH SET (for unique grouping)
    print("\n3. DEFAULTDICT WITH SET (Unique grouping)")
    print("-" * 40)
    
    unique_groups = defaultdict(set)
    items_with_duplicates = [("fruit", "apple"), ("fruit", "banana"), ("fruit", "apple"),
                              ("color", "red"), ("color", "blue"), ("color", "red")]
    
    for category, value in items_with_duplicates:
        unique_groups[category].add(value)
    
    print(f"  Unique groups: {dict(unique_groups)}")
    
    # DEFAULTDICT WITH CUSTOM DEFAULT
    print("\n4. DEFAULTDICT WITH CUSTOM DEFAULT FACTORY")
    print("-" * 40)
    
    def default_value():
        return {"count": 0, "items": []}
    
    stats = defaultdict(default_value)
    data = [("A", "item1"), ("A", "item2"), ("B", "item3"), ("A", "item4")]
    
    for key, item in data:
        stats[key]["count"] += 1
        stats[key]["items"].append(item)
    
    print(f"  Custom stats: {dict(stats)}")
    
    # COMPARISON: REGULAR DICT VS DEFAULTDICT
    print("\n5. COMPARISON: REGULAR DICT VS DEFAULTDICT")
    print("-" * 40)
    
    # Regular dict requires checking
    regular = {}
    for word in words:
        if word not in regular:
            regular[word] = 0
        regular[word] += 1
    
    # defaultdict is cleaner
    dd = defaultdict(int)
    for word in words:
        dd[word] += 1
    
    print(f"  Regular dict: {regular}")
    print(f"  defaultdict: {dict(dd)}")
    print("  ✓ defaultdict eliminates boilerplate code!")


if __name__ == "__main__":
    demonstrate_dictionary_creation()
    demonstrate_dictionary_access()
    demonstrate_dictionary_modification()
    demonstrate_dictionary_comprehensions()
    demonstrate_defaultdict()
```

---

## 👤 Section 2: User Profile System

A complete user profile system using dictionaries for fast lookup by username.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of user management
- Open/Closed: New user fields can be added

**Design Patterns:**
- Repository Pattern: User storage and retrieval
- Factory Pattern: Creates user profiles

```python
"""
USER PROFILE SYSTEM

This section builds a complete user profile system using dictionaries.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New user fields can be added

Design Patterns:
- Repository Pattern: User storage and retrieval
- Factory Pattern: Creates user profiles
"""

from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass
import hashlib
import re
import json


class UserValidator:
    """Validates user data before profile creation."""
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False, "Invalid email format"
        return True, "Valid"
    
    @staticmethod
    def validate_username(username: str) -> Tuple[bool, str]:
        """Validate username format."""
        if not username or len(username) < 3:
            return False, "Username must be at least 3 characters"
        if len(username) > 20:
            return False, "Username cannot exceed 20 characters"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscore"
        return True, "Valid"
    
    @staticmethod
    def validate_age(age: int) -> Tuple[bool, str]:
        """Validate age."""
        if age < 13:
            return False, "Must be at least 13 years old"
        if age > 120:
            return False, "Invalid age"
        return True, "Valid"
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password for storage."""
        return hashlib.sha256(password.encode()).hexdigest()


class UserProfile:
    """Represents a user profile with dictionary storage."""
    
    def __init__(self, username: str, email: str, age: int, password_hash: str):
        self.username = username
        self.email = email
        self.age = age
        self.password_hash = password_hash
        self.created_at = datetime.now()
        self.last_login = None
        self.is_active = True
        self.preferences: Dict[str, Any] = {
            "theme": "light",
            "language": "en",
            "notifications": True
        }
        self.profile: Dict[str, Any] = {
            "full_name": "",
            "bio": "",
            "location": "",
            "avatar_url": None
        }
        self.activity_log: List[Dict] = []
    
    def to_dict(self) -> Dict:
        """Convert user profile to dictionary."""
        return {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "password_hash": self.password_hash,
            "created_at": self.created_at.isoformat(),
            "last_login": self.last_login.isoformat() if self.last_login else None,
            "is_active": self.is_active,
            "preferences": self.preferences,
            "profile": self.profile,
            "activity_log": self.activity_log
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'UserProfile':
        """Create user profile from dictionary."""
        user = cls(
            username=data["username"],
            email=data["email"],
            age=data["age"],
            password_hash=data["password_hash"]
        )
        user.created_at = datetime.fromisoformat(data["created_at"])
        user.last_login = datetime.fromisoformat(data["last_login"]) if data["last_login"] else None
        user.is_active = data["is_active"]
        user.preferences = data["preferences"]
        user.profile = data["profile"]
        user.activity_log = data["activity_log"]
        return user
    
    def update_preferences(self, updates: Dict) -> None:
        """Update user preferences."""
        self.preferences.update(updates)
        self._log_activity("preferences_updated", list(updates.keys()))
    
    def update_profile(self, updates: Dict) -> None:
        """Update profile information."""
        self.profile.update(updates)
        self._log_activity("profile_updated", list(updates.keys()))
    
    def record_login(self) -> None:
        """Record user login."""
        self.last_login = datetime.now()
        self._log_activity("login", {})
    
    def _log_activity(self, action: str, details: Any) -> None:
        """Log user activity."""
        self.activity_log.append({
            "action": action,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_summary(self) -> Dict:
        """Get user profile summary."""
        return {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active,
            "preferences": self.preferences,
            "last_login": self.last_login.isoformat() if self.last_login else None,
            "activity_count": len(self.activity_log)
        }


class UserRepository:
    """
    Repository for user storage and retrieval using dictionaries.
    
    Design Pattern: Repository Pattern - Centralized user storage
    """
    
    def __init__(self):
        self._users: Dict[str, UserProfile] = {}  # username -> UserProfile
        self._email_index: Dict[str, str] = {}    # email -> username
    
    def create_user(self, username: str, email: str, age: int, password: str) -> Tuple[bool, str, Optional[UserProfile]]:
        """Create a new user profile."""
        # Validate inputs
        valid, msg = UserValidator.validate_username(username)
        if not valid:
            return False, msg, None
        
        valid, msg = UserValidator.validate_email(email)
        if not valid:
            return False, msg, None
        
        valid, msg = UserValidator.validate_age(age)
        if not valid:
            return False, msg, None
        
        # Check for duplicates
        if username in self._users:
            return False, f"Username '{username}' already exists", None
        
        if email in self._email_index:
            return False, f"Email '{email}' already registered", None
        
        # Create user
        password_hash = UserValidator.hash_password(password)
        user = UserProfile(username, email, age, password_hash)
        
        self._users[username] = user
        self._email_index[email] = username
        
        return True, "User created successfully", user
    
    def get_user_by_username(self, username: str) -> Optional[UserProfile]:
        """Get user by username (O(1) lookup)."""
        return self._users.get(username)
    
    def get_user_by_email(self, email: str) -> Optional[UserProfile]:
        """Get user by email (O(1) lookup via index)."""
        username = self._email_index.get(email)
        if username:
            return self._users.get(username)
        return None
    
    def authenticate(self, username: str, password: str) -> Tuple[bool, Optional[UserProfile]]:
        """Authenticate user by username and password."""
        user = self.get_user_by_username(username)
        if not user:
            return False, None
        
        password_hash = UserValidator.hash_password(password)
        if user.password_hash == password_hash:
            return True, user
        return False, None
    
    def update_user(self, username: str, updates: Dict) -> Tuple[bool, str]:
        """Update user information."""
        user = self.get_user_by_username(username)
        if not user:
            return False, "User not found"
        
        if "preferences" in updates:
            user.update_preferences(updates["preferences"])
        if "profile" in updates:
            user.update_profile(updates["profile"])
        if "email" in updates:
            valid, msg = UserValidator.validate_email(updates["email"])
            if not valid:
                return False, msg
            # Update email index
            old_email = user.email
            del self._email_index[old_email]
            user.email = updates["email"]
            self._email_index[user.email] = username
        
        return True, "User updated successfully"
    
    def delete_user(self, username: str) -> Tuple[bool, str]:
        """Delete a user."""
        user = self.get_user_by_username(username)
        if not user:
            return False, "User not found"
        
        del self._users[username]
        del self._email_index[user.email]
        return True, "User deleted successfully"
    
    def get_all_users(self) -> List[UserProfile]:
        """Get all users."""
        return list(self._users.values())
    
    def search_users(self, query: str) -> List[UserProfile]:
        """Search users by username or email."""
        query_lower = query.lower()
        results = []
        for user in self._users.values():
            if query_lower in user.username.lower() or query_lower in user.email.lower():
                results.append(user)
        return results
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get user repository statistics."""
        users = self._users.values()
        total = len(users)
        active = sum(1 for u in users if u.is_active)
        avg_age = sum(u.age for u in users) / total if total > 0 else 0
        
        return {
            "total_users": total,
            "active_users": active,
            "inactive_users": total - active,
            "average_age": round(avg_age, 1),
            "preferences_popularity": self._get_preference_stats()
        }
    
    def _get_preference_stats(self) -> Dict:
        """Get statistics on user preferences."""
        theme_counts = {}
        language_counts = {}
        
        for user in self._users.values():
            theme = user.preferences.get("theme", "unknown")
            language = user.preferences.get("language", "unknown")
            theme_counts[theme] = theme_counts.get(theme, 0) + 1
            language_counts[language] = language_counts.get(language, 0) + 1
        
        return {
            "themes": theme_counts,
            "languages": language_counts
        }


def demonstrate_user_profile_system():
    """
    Demonstrate the user profile system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: USER PROFILE SYSTEM")
    print("=" * 60)
    
    repo = UserRepository()
    
    print("\n1. CREATING USERS")
    print("-" * 40)
    
    # Create users
    success, msg, alice = repo.create_user("alice_wonder", "alice@example.com", 28, "SecurePass123")
    print(f"  Alice: {msg}")
    
    success, msg, bob = repo.create_user("bob_builder", "bob@example.com", 35, "BuildIt123")
    print(f"  Bob: {msg}")
    
    # Try duplicate
    success, msg, _ = repo.create_user("alice_wonder", "alice2@example.com", 25, "pass")
    print(f"  Duplicate username: {msg}")
    
    print("\n2. USER LOOKUP (O(1) BY USERNAME)")
    print("-" * 40)
    
    user = repo.get_user_by_username("alice_wonder")
    if user:
        print(f"  Found: {user.username} - {user.email}")
    
    user = repo.get_user_by_email("bob@example.com")
    if user:
        print(f"  Found by email: {user.username}")
    
    print("\n3. UPDATING USER PREFERENCES")
    print("-" * 40)
    
    alice.update_preferences({"theme": "dark", "language": "es"})
    bob.update_profile({"full_name": "Robert Builder", "bio": "Construction expert"})
    
    print(f"  Alice preferences: {alice.preferences}")
    print(f"  Bob profile: {bob.profile}")
    
    print("\n4. USER AUTHENTICATION")
    print("-" * 40)
    
    success, user = repo.authenticate("alice_wonder", "SecurePass123")
    print(f"  Correct password: {success}")
    
    success, user = repo.authenticate("alice_wonder", "wrongpassword")
    print(f"  Wrong password: {success}")
    
    print("\n5. SEARCHING USERS")
    print("-" * 40)
    
    results = repo.search_users("alice")
    print(f"  Search 'alice': {[u.username for u in results]}")
    
    results = repo.search_users("example.com")
    print(f"  Search 'example.com': {[u.username for u in results]}")
    
    print("\n6. USER STATISTICS")
    print("-" * 40)
    
    stats = repo.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n7. USER ACTIVITY LOG")
    print("-" * 40)
    
    alice.record_login()
    alice.update_preferences({"notifications": False})
    
    for activity in alice.activity_log:
        print(f"  {activity['action']}: {activity['details']}")
    
    print("\n8. USER SUMMARY")
    print("-" * 40)
    
    summary = alice.get_summary()
    for key, value in summary.items():
        if key != "preferences":
            print(f"  {key}: {value}")
    print(f"  preferences: {alice.preferences}")


if __name__ == "__main__":
    demonstrate_user_profile_system()
```

---

## 🏪 Section 3: Product Catalog System

A complete product catalog with search, filtering, and categorization using dictionaries.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one catalog aspect
- Open/Closed: New product attributes can be added

**Design Patterns:**
- Repository Pattern: Product storage
- Specification Pattern: Search and filter criteria

```python
"""
PRODUCT CATALOG SYSTEM

This section builds a product catalog using dictionaries.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New product attributes can be added

Design Patterns:
- Repository Pattern: Product storage
- Specification Pattern: Search and filter criteria
"""

from typing import Dict, List, Optional, Any, Callable, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class Product:
    """Represents a product in the catalog."""
    sku: str
    name: str
    price: float
    category: str
    in_stock: bool = True
    rating: float = 0.0
    tags: List[str] = field(default_factory=list)
    attributes: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "in_stock": self.in_stock,
            "rating": self.rating,
            "tags": self.tags,
            "attributes": self.attributes,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create product from dictionary."""
        return cls(
            sku=data["sku"],
            name=data["name"],
            price=data["price"],
            category=data["category"],
            in_stock=data.get("in_stock", True),
            rating=data.get("rating", 0.0),
            tags=data.get("tags", []),
            attributes=data.get("attributes", {}),
            created_at=datetime.fromisoformat(data["created_at"]) if "created_at" in data else datetime.now()
        )
    
    def __str__(self) -> str:
        stock = "✓" if self.in_stock else "✗"
        return f"{self.sku}: {self.name} - ${self.price:.2f} [{stock}]"


class ProductCatalog:
    """
    Product catalog with dictionary-based storage.
    
    Design Pattern: Repository Pattern - Product storage and retrieval
    """
    
    def __init__(self):
        self._products: Dict[str, Product] = {}  # sku -> Product
        self._category_index: Dict[str, List[str]] = {}  # category -> list of skus
        self._tag_index: Dict[str, List[str]] = {}  # tag -> list of skus
    
    def add_product(self, product: Product) -> bool:
        """Add a product to the catalog."""
        if product.sku in self._products:
            return False
        
        self._products[product.sku] = product
        
        # Update category index
        if product.category not in self._category_index:
            self._category_index[product.category] = []
        self._category_index[product.category].append(product.sku)
        
        # Update tag index
        for tag in product.tags:
            if tag not in self._tag_index:
                self._tag_index[tag] = []
            self._tag_index[tag].append(product.sku)
        
        return True
    
    def get_product(self, sku: str) -> Optional[Product]:
        """Get product by SKU (O(1) lookup)."""
        return self._products.get(sku)
    
    def update_product(self, sku: str, updates: Dict) -> bool:
        """Update a product."""
        product = self.get_product(sku)
        if not product:
            return False
        
        for key, value in updates.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        return True
    
    def delete_product(self, sku: str) -> bool:
        """Delete a product."""
        if sku not in self._products:
            return False
        
        product = self._products[sku]
        
        # Remove from indexes
        if product.category in self._category_index:
            self._category_index[product.category] = [s for s in self._category_index[product.category] if s != sku]
        
        for tag in product.tags:
            if tag in self._tag_index:
                self._tag_index[tag] = [s for s in self._tag_index[tag] if s != sku]
        
        del self._products[sku]
        return True
    
    def get_by_category(self, category: str) -> List[Product]:
        """Get all products in a category (O(1) via index)."""
        skus = self._category_index.get(category, [])
        return [self._products[sku] for sku in skus if sku in self._products]
    
    def get_by_tag(self, tag: str) -> List[Product]:
        """Get all products with a tag (O(1) via index)."""
        skus = self._tag_index.get(tag, [])
        return [self._products[sku] for sku in skus if sku in self._products]
    
    def get_all_products(self) -> List[Product]:
        """Get all products."""
        return list(self._products.values())
    
    def get_categories(self) -> List[str]:
        """Get all categories."""
        return list(self._category_index.keys())
    
    def get_tags(self) -> List[str]:
        """Get all tags."""
        return list(self._tag_index.keys())
    
    def search(self, query: str) -> List[Product]:
        """Search products by name or SKU."""
        query_lower = query.lower()
        results = []
        for product in self._products.values():
            if query_lower in product.name.lower() or query_lower in product.sku.lower():
                results.append(product)
        return results
    
    def filter(self, predicate: Callable[[Product], bool]) -> List[Product]:
        """
        Filter products using a predicate function.
        
        Design Pattern: Specification Pattern - Predicate as specification
        """
        return [p for p in self._products.values() if predicate(p)]
    
    def get_price_range(self) -> Tuple[float, float]:
        """Get min and max prices in catalog."""
        if not self._products:
            return (0.0, 0.0)
        prices = [p.price for p in self._products.values()]
        return (min(prices), max(prices))
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get catalog statistics."""
        products = self._products.values()
        total = len(products)
        in_stock = sum(1 for p in products if p.in_stock)
        
        return {
            "total_products": total,
            "in_stock": in_stock,
            "out_of_stock": total - in_stock,
            "categories": len(self._category_index),
            "tags": len(self._tag_index),
            "avg_price": sum(p.price for p in products) / total if total > 0 else 0,
            "min_price": min(p.price for p in products) if total > 0 else 0,
            "max_price": max(p.price for p in products) if total > 0 else 0
        }


class PriceRangeFilter:
    """Filter products by price range."""
    
    def __init__(self, min_price: float, max_price: float):
        self.min_price = min_price
        self.max_price = max_price
    
    def apply(self, product: Product) -> bool:
        return self.min_price <= product.price <= self.max_price


class InStockFilter:
    """Filter for in-stock products only."""
    
    def apply(self, product: Product) -> bool:
        return product.in_stock


class RatingFilter:
    """Filter by minimum rating."""
    
    def __init__(self, min_rating: float):
        self.min_rating = min_rating
    
    def apply(self, product: Product) -> bool:
        return product.rating >= self.min_rating


def demonstrate_product_catalog():
    """
    Demonstrate the product catalog system.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: PRODUCT CATALOG SYSTEM")
    print("=" * 60)
    
    catalog = ProductCatalog()
    
    print("\n1. ADDING PRODUCTS")
    print("-" * 40)
    
    products = [
        Product("P001", "Laptop", 999.99, "Electronics", True, 4.5, ["computer", "portable"]),
        Product("P002", "Mouse", 29.99, "Electronics", True, 4.2, ["computer", "peripheral"]),
        Product("P003", "Keyboard", 89.99, "Electronics", False, 4.7, ["computer", "peripheral"]),
        Product("P004", "Monitor", 299.99, "Electronics", True, 4.4, ["computer", "display"]),
        Product("P005", "Desk", 399.99, "Furniture", True, 4.3, ["office", "furniture"]),
        Product("P006", "Chair", 199.99, "Furniture", False, 4.1, ["office", "furniture"]),
        Product("P007", "Notebook", 4.99, "Stationery", True, 4.0, ["office", "paper"]),
        Product("P008", "Pen", 1.99, "Stationery", True, 3.9, ["office", "writing"])
    ]
    
    for product in products:
        catalog.add_product(product)
        print(f"  Added: {product}")
    
    print("\n2. LOOKUP BY SKU (O(1))")
    print("-" * 40)
    
    product = catalog.get_product("P001")
    print(f"  P001: {product}")
    
    product = catalog.get_product("P999")
    print(f"  P999: {product}")
    
    print("\n3. GET BY CATEGORY (via index)")
    print("-" * 40)
    
    electronics = catalog.get_by_category("Electronics")
    print(f"  Electronics: {len(electronics)} products")
    for p in electronics:
        print(f"    {p.name}: ${p.price}")
    
    print("\n4. GET BY TAG (via index)")
    print("-" * 40)
    
    computer_products = catalog.get_by_tag("computer")
    print(f"  'computer' tag: {len(computer_products)} products")
    for p in computer_products:
        print(f"    {p.name}")
    
    print("\n5. SEARCH")
    print("-" * 40)
    
    results = catalog.search("lap")
    print(f"  Search 'lap': {[p.name for p in results]}")
    
    results = catalog.search("office")
    print(f"  Search 'office': {[p.name for p in results]}")
    
    print("\n6. FILTERING")
    print("-" * 40)
    
    # Filter by price range
    price_filter = PriceRangeFilter(50, 300)
    filtered = catalog.filter(price_filter.apply)
    print(f"  Price $50-$300: {len(filtered)} products")
    for p in filtered:
        print(f"    {p.name}: ${p.price}")
    
    # Filter by in-stock
    stock_filter = InStockFilter()
    in_stock = catalog.filter(stock_filter.apply)
    print(f"\n  In stock: {len(in_stock)} products")
    
    # Combined filter
    combined = catalog.filter(lambda p: p.in_stock and p.price < 100)
    print(f"  In stock and under $100: {len(combined)} products")
    
    print("\n7. STATISTICS")
    print("-" * 40)
    
    stats = catalog.get_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: ${value:.2f}")
        else:
            print(f"  {key}: {value}")
    
    print("\n8. CATEGORIES AND TAGS")
    print("-" * 40)
    
    print(f"  Categories: {catalog.get_categories()}")
    print(f"  Tags: {catalog.get_tags()}")


if __name__ == "__main__":
    demonstrate_product_catalog()
```

---

## 💾 Section 4: LRU Cache System

A complete LRU (Least Recently Used) cache implementation using dictionaries and ordered structures.

**SOLID Principles Applied:**
- Single Responsibility: Cache handles storage and eviction
- Open/Closed: Different eviction policies can be added

**Design Patterns:**
- Proxy Pattern: Cache acts as proxy to expensive operations
- Singleton Pattern: Single cache instance

```python
"""
LRU CACHE SYSTEM

This section builds an LRU (Least Recently Used) cache using dictionaries.

SOLID Principles Applied:
- Single Responsibility: Cache handles storage and eviction
- Open/Closed: Different eviction policies can be added

Design Patterns:
- Proxy Pattern: Cache acts as proxy to expensive operations
- Singleton Pattern: Single cache instance
"""

from typing import Dict, Any, Optional, Callable, TypeVar, Generic
from dataclasses import dataclass, field
from collections import OrderedDict
from datetime import datetime
import time
import threading

K = TypeVar('K')
V = TypeVar('V')


class LRUCache(Generic[K, V]):
    """
    Least Recently Used (LRU) Cache implementation.
    
    Design Pattern: Proxy Pattern - Caches expensive operations
    """
    
    def __init__(self, capacity: int = 100):
        """
        Initialize LRU cache.
        
        Args:
            capacity: Maximum number of items to store
        """
        self.capacity = capacity
        self._cache: OrderedDict[K, V] = OrderedDict()
        self._hits = 0
        self._misses = 0
    
    def get(self, key: K) -> Optional[V]:
        """
        Get value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if not found
        """
        if key not in self._cache:
            self._misses += 1
            return None
        
        # Move to end (most recently used)
        value = self._cache.pop(key)
        self._cache[key] = value
        self._hits += 1
        return value
    
    def put(self, key: K, value: V) -> None:
        """
        Put value into cache.
        
        Args:
            key: Cache key
            value: Value to store
        """
        if key in self._cache:
            # Remove existing to update order
            self._cache.pop(key)
        elif len(self._cache) >= self.capacity:
            # Remove least recently used (first item)
            self._cache.popitem(last=False)
        
        self._cache[key] = value
    
    def contains(self, key: K) -> bool:
        """Check if key exists in cache."""
        return key in self._cache
    
    def clear(self) -> None:
        """Clear the cache."""
        self._cache.clear()
        self._hits = 0
        self._misses = 0
    
    def size(self) -> int:
        """Get current cache size."""
        return len(self._cache)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        total = self._hits + self._misses
        hit_rate = (self._hits / total * 100) if total > 0 else 0
        
        return {
            "size": self.size(),
            "capacity": self.capacity,
            "hits": self._hits,
            "misses": self._misses,
            "hit_rate": round(hit_rate, 1),
            "utilization": round(self.size() / self.capacity * 100, 1)
        }
    
    def __contains__(self, key: K) -> bool:
        return self.contains(key)
    
    def __len__(self) -> int:
        return self.size()


class TTLCache(Generic[K, V]):
    """
    Time-To-Live cache with expiration.
    
    Values expire after a specified TTL (Time To Live).
    """
    
    @dataclass
    class CacheEntry:
        value: V
        expires_at: float
    
    def __init__(self, ttl_seconds: int = 300, max_size: int = 1000):
        """
        Initialize TTL cache.
        
        Args:
            ttl_seconds: Time to live in seconds
            max_size: Maximum number of items
        """
        self.ttl = ttl_seconds
        self.max_size = max_size
        self._cache: Dict[K, TTLCache.CacheEntry] = {}
        self._hits = 0
        self._misses = 0
    
    def _is_expired(self, entry: 'TTLCache.CacheEntry') -> bool:
        """Check if cache entry has expired."""
        return time.time() > entry.expires_at
    
    def _clean_expired(self) -> None:
        """Remove expired entries."""
        expired_keys = [k for k, v in self._cache.items() if self._is_expired(v)]
        for key in expired_keys:
            del self._cache[key]
    
    def get(self, key: K) -> Optional[V]:
        """Get value from cache (checks expiration)."""
        self._clean_expired()
        
        if key not in self._cache:
            self._misses += 1
            return None
        
        entry = self._cache[key]
        if self._is_expired(entry):
            del self._cache[key]
            self._misses += 1
            return None
        
        self._hits += 1
        return entry.value
    
    def put(self, key: K, value: V) -> bool:
        """Put value into cache."""
        self._clean_expired()
        
        # Evict if at capacity
        if len(self._cache) >= self.max_size and key not in self._cache:
            # Remove oldest (simplified - remove first)
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        
        self._cache[key] = TTLCache.CacheEntry(
            value=value,
            expires_at=time.time() + self.ttl
        )
        return True
    
    def clear(self) -> None:
        """Clear the cache."""
        self._cache.clear()
        self._hits = 0
        self._misses = 0
    
    def size(self) -> int:
        """Get current cache size (excluding expired)."""
        self._clean_expired()
        return len(self._cache)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        total = self._hits + self._misses
        hit_rate = (self._hits / total * 100) if total > 0 else 0
        
        return {
            "size": self.size(),
            "max_size": self.max_size,
            "ttl_seconds": self.ttl,
            "hits": self._hits,
            "misses": self._misses,
            "hit_rate": round(hit_rate, 1)
        }


class CacheFactory:
    """
    Factory for creating different cache types.
    
    Design Pattern: Factory Pattern - Creates cache instances
    """
    
    @staticmethod
    def lru(capacity: int = 100) -> LRUCache:
        """Create LRU cache."""
        return LRUCache(capacity)
    
    @staticmethod
    def ttl(ttl_seconds: int = 300, max_size: int = 1000) -> TTLCache:
        """Create TTL cache."""
        return TTLCache(ttl_seconds, max_size)


def expensive_operation(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(0.1)  # Simulate work
    return n * n


def demonstrate_cache_system():
    """
    Demonstrate the cache system.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: LRU CACHE SYSTEM")
    print("=" * 60)
    
    # LRU Cache demonstration
    print("\n1. LRU CACHE DEMONSTRATION")
    print("-" * 40)
    
    cache = LRUCache(capacity=3)
    
    print("  Adding items:")
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"    Cache: {list(cache._cache.keys())}")
    
    print("\n  Accessing items:")
    cache.get("a")
    print(f"    After accessing 'a': {list(cache._cache.keys())}")
    
    print("\n  Adding new item (exceeds capacity):")
    cache.put("d", 4)
    print(f"    After adding 'd': {list(cache._cache.keys())}")
    print(f"    'b' was evicted (least recently used)")
    
    print("\n  Cache statistics:")
    stats = cache.get_stats()
    for key, value in stats.items():
        print(f"    {key}: {value}")
    
    # TTL Cache demonstration
    print("\n2. TTL CACHE DEMONSTRATION")
    print("-" * 40)
    
    ttl_cache = TTLCache(ttl_seconds=2, max_size=5)
    
    ttl_cache.put("key1", "value1")
    ttl_cache.put("key2", "value2")
    
    print("  Added items with 2 second TTL")
    print(f"  Get key1: {ttl_cache.get('key1')}")
    
    print("\n  Waiting 3 seconds...")
    time.sleep(3)
    
    print(f"  Get key1 after expiration: {ttl_cache.get('key1')}")
    print(f"  Cache size after cleanup: {ttl_cache.size()}")
    
    # Performance comparison
    print("\n3. CACHING PERFORMANCE DEMONSTRATION")
    print("-" * 40)
    
    compute_cache = LRUCache(capacity=10)
    
    # Without cache
    print("  Without cache:")
    start = time.time()
    results = [expensive_operation(i % 5) for i in range(20)]
    without_cache_time = time.time() - start
    print(f"    Time: {without_cache_time:.2f}s")
    
    # With cache
    print("\n  With cache:")
    start = time.time()
    cached_results = []
    for i in range(20):
        key = i % 5
        value = compute_cache.get(key)
        if value is None:
            value = expensive_operation(key)
            compute_cache.put(key, value)
        cached_results.append(value)
    with_cache_time = time.time() - start
    
    print(f"    Time: {with_cache_time:.2f}s")
    print(f"    Speedup: {without_cache_time / with_cache_time:.1f}x")
    print(f"    Cache stats: {compute_cache.get_stats()}")
    
    # Real-world: API response caching
    print("\n4. API RESPONSE CACHING EXAMPLE")
    print("-" * 40)
    
    class APIClient:
        """API client with response caching."""
        
        def __init__(self):
            self.cache = TTLCache(ttl_seconds=60, max_size=100)
            self.call_count = 0
        
        def fetch_user(self, user_id: int) -> Dict:
            """Fetch user data (with caching)."""
            cache_key = f"user_{user_id}"
            
            # Check cache first
            cached = self.cache.get(cache_key)
            if cached is not None:
                return {"source": "cache", "data": cached}
            
            # Simulate API call
            self.call_count += 1
            time.sleep(0.05)  # Simulate network delay
            user_data = {"id": user_id, "name": f"User {user_id}", "cached_at": time.time()}
            
            # Store in cache
            self.cache.put(cache_key, user_data)
            return {"source": "api", "data": user_data}
        
        def get_stats(self) -> Dict:
            return {
                "api_calls": self.call_count,
                "cache_stats": self.cache.get_stats()
            }
    
    api = APIClient()
    
    print("  First request (cache miss):")
    result = api.fetch_user(1)
    print(f"    Source: {result['source']}")
    
    print("\n  Second request (cache hit):")
    result = api.fetch_user(1)
    print(f"    Source: {result['source']}")
    
    print("\n  API Client Statistics:")
    stats = api.get_stats()
    for key, value in stats.items():
        if key == "cache_stats":
            for k, v in value.items():
                print(f"    cache_{k}: {v}")
        else:
            print(f"    {key}: {value}")


if __name__ == "__main__":
    demonstrate_cache_system()
```

---

## 🧩 Section 5: Dependency Injection Container

A complete dependency injection container using dictionaries for service registration and resolution.

**SOLID Principles Applied:**
- Dependency Inversion: High-level modules depend on abstractions
- Single Responsibility: Container manages service lifecycle

**Design Patterns:**
- Service Locator Pattern: Container locates and provides services
- Factory Pattern: Creates service instances
- Singleton Pattern: Manages shared instances

```python
"""
DEPENDENCY INJECTION CONTAINER

This section builds a DI container using dictionaries.

SOLID Principles Applied:
- Dependency Inversion: High-level modules depend on abstractions
- Single Responsibility: Container manages service lifecycle

Design Patterns:
- Service Locator Pattern: Container locates services
- Factory Pattern: Creates service instances
- Singleton Pattern: Manages shared instances
"""

from typing import Dict, Any, Type, Callable, Optional, TypeVar, Generic
from abc import ABC, abstractmethod
import threading

T = TypeVar('T')


class ServiceScope(Enum):
    """Service lifetime scope."""
    TRANSIENT = "transient"  # New instance each time
    SINGLETON = "singleton"  # Single shared instance
    SCOPED = "scoped"        # Instance per scope


class ServiceDefinition:
    """Definition of a registered service."""
    
    def __init__(self, service_type: Type, implementation: Any, scope: ServiceScope):
        self.service_type = service_type
        self.implementation = implementation
        self.scope = scope
        self.instance = None
        self._lock = threading.Lock()
    
    def resolve(self, container: 'DIContainer') -> Any:
        """Resolve service instance based on scope."""
        if self.scope == ServiceScope.TRANSIENT:
            return self._create_instance(container)
        
        if self.scope == ServiceScope.SINGLETON:
            with self._lock:
                if self.instance is None:
                    self.instance = self._create_instance(container)
                return self.instance
        
        # SCOPED - use container's scope storage
        scope_id = container.get_current_scope_id()
        if scope_id not in container._scoped_instances:
            container._scoped_instances[scope_id] = {}
        
        if self.service_type not in container._scoped_instances[scope_id]:
            container._scoped_instances[scope_id][self.service_type] = self._create_instance(container)
        
        return container._scoped_instances[scope_id][self.service_type]
    
    def _create_instance(self, container: 'DIContainer') -> Any:
        """Create a new service instance."""
        if callable(self.implementation):
            # Factory function
            return self.implementation(container)
        elif isinstance(self.implementation, type):
            # Class - resolve constructor dependencies
            return container.resolve_constructor(self.implementation)
        else:
            # Pre-created instance
            return self.implementation


class DIContainer:
    """
    Dependency Injection Container.
    
    Design Pattern: Service Locator Pattern - Central service registry
    """
    
    def __init__(self):
        self._services: Dict[Type, ServiceDefinition] = {}
        self._instances: Dict[Type, Any] = {}
        self._scoped_instances: Dict[str, Dict[Type, Any]] = {}
        self._current_scope_id: Optional[str] = None
    
    def register(self, service_type: Type, implementation: Any = None,
                 scope: ServiceScope = ServiceScope.TRANSIENT) -> 'DIContainer':
        """
        Register a service.
        
        Args:
            service_type: The interface/abstract type
            implementation: Concrete implementation (class, factory, or instance)
            scope: Service lifetime scope
            
        Returns:
            Self for method chaining
        """
        if implementation is None:
            implementation = service_type
        
        self._services[service_type] = ServiceDefinition(
            service_type, implementation, scope
        )
        return self
    
    def register_singleton(self, service_type: Type, implementation: Any = None) -> 'DIContainer':
        """Register a singleton service."""
        return self.register(service_type, implementation, ServiceScope.SINGLETON)
    
    def register_transient(self, service_type: Type, implementation: Any = None) -> 'DIContainer':
        """Register a transient service."""
        return self.register(service_type, implementation, ServiceScope.TRANSIENT)
    
    def register_instance(self, service_type: Type, instance: Any) -> 'DIContainer':
        """Register a pre-created instance."""
        return self.register(service_type, instance, ServiceScope.SINGLETON)
    
    def register_factory(self, service_type: Type, factory: Callable) -> 'DIContainer':
        """Register a factory function."""
        return self.register(service_type, factory, ServiceScope.TRANSIENT)
    
    def resolve(self, service_type: Type[T]) -> T:
        """Resolve a service."""
        if service_type not in self._services:
            raise KeyError(f"Service {service_type.__name__} not registered")
        
        return self._services[service_type].resolve(self)
    
    def resolve_constructor(self, cls: Type[T]) -> T:
        """Resolve a class's constructor dependencies."""
        import inspect
        
        # Get constructor parameters
        sig = inspect.signature(cls.__init__)
        kwargs = {}
        
        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
            
            # Get type hint
            param_type = param.annotation
            if param_type != inspect.Parameter.empty:
                try:
                    kwargs[param_name] = self.resolve(param_type)
                except KeyError:
                    # Not registered - try to create directly
                    pass
        
        return cls(**kwargs)
    
    def create_scope(self) -> 'DIContainer':
        """Create a new service scope."""
        import uuid
        scope = DIContainer()
        scope._services = self._services
        scope._current_scope_id = str(uuid.uuid4())
        return scope
    
    def get_current_scope_id(self) -> str:
        """Get current scope ID."""
        if self._current_scope_id is None:
            self._current_scope_id = "default"
        return self._current_scope_id
    
    def end_scope(self) -> None:
        """End current scope and clear scoped instances."""
        if self._current_scope_id in self._scoped_instances:
            del self._scoped_instances[self._current_scope_id]


# Example services for demonstration

class Logger:
    """Logging service."""
    
    def __init__(self):
        self.logs = []
    
    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        print(f"  {log_entry}")
    
    def get_logs(self) -> List[str]:
        return self.logs


class UserRepositoryInterface(ABC):
    """User repository interface."""
    
    @abstractmethod
    def get_user(self, user_id: int) -> Dict:
        pass


class UserRepository(UserRepositoryInterface):
    """Concrete user repository implementation."""
    
    def __init__(self, logger: Logger):
        self.logger = logger
        self._users = {
            1: {"id": 1, "name": "Alice"},
            2: {"id": 2, "name": "Bob"}
        }
    
    def get_user(self, user_id: int) -> Dict:
        self.logger.log(f"Fetching user {user_id}")
        return self._users.get(user_id, {"error": "User not found"})


class UserService:
    """User service with dependency injection."""
    
    def __init__(self, user_repository: UserRepositoryInterface, logger: Logger):
        self.user_repository = user_repository
        self.logger = logger
    
    def get_user_profile(self, user_id: int) -> Dict:
        self.logger.log(f"Getting profile for user {user_id}")
        user = self.user_repository.get_user(user_id)
        if "error" in user:
            return user
        return {
            "user_id": user["id"],
            "name": user["name"],
            "profile_complete": True
        }


def demonstrate_di_container():
    """
    Demonstrate the dependency injection container.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: DEPENDENCY INJECTION CONTAINER")
    print("=" * 60)
    
    # Create container
    container = DIContainer()
    
    print("\n1. REGISTERING SERVICES")
    print("-" * 40)
    
    # Register services
    container.register_singleton(Logger)  # Singleton - shared instance
    container.register_singleton(UserRepositoryInterface, UserRepository)  # Singleton
    container.register_transient(UserService)  # Transient - new instance each time
    
    print("  Registered: Logger (singleton)")
    print("  Registered: UserRepositoryInterface → UserRepository (singleton)")
    print("  Registered: UserService (transient)")
    
    print("\n2. RESOLVING SERVICES")
    print("-" * 40)
    
    # Resolve and use services
    logger1 = container.resolve(Logger)
    logger1.log("Application started")
    
    user_service1 = container.resolve(UserService)
    user_service2 = container.resolve(UserService)
    
    print(f"\n  UserService instances: {id(user_service1)} vs {id(user_service2)}")
    print("  Different IDs - transient creates new instances")
    
    logger2 = container.resolve(Logger)
    print(f"  Logger instances: {id(logger1)} vs {id(logger2)}")
    print("  Same ID - singleton shares instance")
    
    print("\n3. USING RESOLVED SERVICES")
    print("-" * 40)
    
    user_profile = user_service1.get_user_profile(1)
    print(f"  User 1 profile: {user_profile}")
    
    user_profile = user_service1.get_user_profile(99)
    print(f"  User 99 profile: {user_profile}")
    
    print("\n4. CONTAINER STATISTICS")
    print("-" * 40)
    
    print(f"  Registered services: {len(container._services)}")
    for service_type in container._services:
        print(f"    {service_type.__name__}")
    
    print("\n5. DEPENDENCY INJECTION BENEFITS")
    print("-" * 40)
    
    print("""
    Benefits demonstrated:
    ✓ Loose coupling - UserService depends on interface, not concrete class
    ✓ Testability - Can easily mock dependencies
    ✓ Centralized configuration - All service wiring in one place
    ✓ Lifecycle management - Container handles singleton vs transient
    ✓ Constructor injection - Dependencies automatically resolved
    """)


if __name__ == "__main__":
    demonstrate_di_container()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Dictionary Basics** – Created with `{}` or `dict()`. Key-value pairs with O(1) lookup.

- **Dictionary Operations** – Access with `[]` or `.get()`. Modify by assignment. Delete with `del` or `.pop()`.

- **Dictionary Views** – `.keys()`, `.values()`, `.items()` provide dynamic views of dictionary contents.

- **Dictionary Comprehensions** – `{k: v for k, v in iterable}` for concise creation.

- **defaultdict** – Auto-initializes missing keys. Great for counting (`int`), grouping (`list`), or unique grouping (`set`).

- **User Profile System** – Fast O(1) lookup by username. Email index for alternative lookup. Activity logging.

- **Product Catalog** – Category and tag indexes for fast filtering. Specification pattern for flexible queries.

- **LRU Cache** – OrderedDict for least-recently-used eviction. O(1) get and put operations.

- **TTL Cache** – Time-based expiration. Automatic cleanup of expired entries.

- **Dependency Injection** – Container manages service lifecycle. Constructor injection with automatic resolution.

- **SOLID Principles Applied** – Single Responsibility (each class handles one aspect), Open/Closed (new services can be added), Dependency Inversion (depends on abstractions), Interface Segregation (clean interfaces), Liskov Substitution (substitutable implementations).

- **Design Patterns Used** – Repository Pattern (data storage), Factory Pattern (cache creation), Proxy Pattern (cache as proxy), Service Locator Pattern (DI container), Singleton Pattern (shared instances), Specification Pattern (filters), Strategy Pattern (eviction policies).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Tuples – Immutable Collections

- **📚 Series C Catalog:** Data Structures Express – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Sets – Unique & Fast (Series C, Story 4)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 3 | 2 | 60% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **21** | **31** | **40%** |

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

**Next Story:** Series C, Story 4: The 2026 Python Metromap: Sets – Unique & Fast

---

## 📝 Your Invitation

You've mastered dictionaries. Now build something with what you've learned:

1. **Build a URL shortener** – Use dictionaries to map short codes to long URLs. Add click tracking and expiration.

2. **Create a configuration manager** – Load config from JSON/YAML, provide dot-notation access, support environment variable overrides.

3. **Build a simple database** – Use dictionaries as tables with indexes for fast lookups.

4. **Create a memoization decorator** – Implement a cache decorator that caches function results using dictionaries.

5. **Build a voting system** – Use dictionaries to count votes, find winners, and detect fraud.

**You've mastered dictionaries. Next stop: Sets!**

---

*Found this helpful? Clap, comment, and share what you built with dictionaries. Next stop: Sets!* 🚇