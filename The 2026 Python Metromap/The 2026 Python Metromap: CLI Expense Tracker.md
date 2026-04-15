# The 2026 Python Metromap: CLI Expense Tracker

## Series J: Capstone Projects | Story 1 of 3

![The 2026 Python Metromap/images/CLI Expense Tracker](images/CLI Expense Tracker.png)

## 📖 Introduction

**Welcome to the first stop on the Capstone Projects Line.**

You've completed all the foundational series—from Python basics to advanced AI/ML. You've built neural networks, deployed ML pipelines, and mastered object-oriented programming. Now it's time to put everything together into complete, portfolio-ready applications.

This story—**The 2026 Python Metromap: CLI Expense Tracker**—is your first capstone project. You'll build a professional command-line expense tracking application that demonstrates mastery of OOP, file handling, data visualization, and user experience design. This isn't just a script—it's a complete application with multiple users, persistent storage, budget tracking, spending reports, and beautiful terminal visualizations.

You'll learn how to structure a real application, implement design patterns in practice, handle edge cases gracefully, and create an intuitive CLI interface that users will actually enjoy using.

**Let's build your first complete Python application.**

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
### Series E: File & Data Handling Line (5 Stories) – COMPLETED
### Series F: Advanced Python Engineering (6 Stories) – COMPLETED
### Series G: Data Science & Visualization (5 Stories) – COMPLETED
### Series H: Web Development & Automation (5 Stories) – COMPLETED
### Series I: AI & Machine Learning with Python (4 Stories) – COMPLETED

### Series J: Capstone Projects (3 Stories)

- 💰 **The 2026 Python Metromap: CLI Expense Tracker** – Complete command-line application with OOP categories and transactions; JSON file storage; spending reports; Matplotlib visualization. **⬅️ YOU ARE HERE**

- 🌤️ **The 2026 Python Metromap: Weather Dashboard** – Flask web application; OpenWeatherMap API integration; Redis caching; HTML/CSS/JS frontend. 🔜 *Up Next*

- 🎯 **The 2026 Python Metromap: ML-Powered Recommendation Engine** – Full-stack recommendation system with Pandas data processing; Scikit-learn collaborative filtering; Flask API; Docker deployment.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🏗️ Section 1: Domain Models & Data Structures

Build the core domain models using OOP principles with proper encapsulation and validation.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one domain concept
- Open/Closed: New transaction types can be added
- Liskov Substitution: All transaction types are interchangeable
- Interface Segregation: Focused interfaces for different behaviors
- Dependency Inversion: High-level modules depend on abstractions

**Design Pattern: Value Object Pattern** – Immutable transaction objects

```python
"""
CLI EXPENSE TRACKER - SECTION 1: DOMAIN MODELS

This section defines the core domain models for the expense tracker.

SOLID Principles Applied:
- Single Responsibility: Each class handles one domain concept
- Open/Closed: New transaction types can be added without modifying existing code
- Liskov Substitution: All transaction types are interchangeable
- Interface Segregation: Focused interfaces for different behaviors
- Dependency Inversion: High-level modules depend on abstractions

Design Pattern: Value Object Pattern - Immutable transaction objects
"""

from datetime import datetime, date
from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Optional, Union
from enum import Enum
import uuid
import re


class TransactionType(Enum):
    """Enumeration of transaction types."""
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"
    REFUND = "refund"


class Category(Enum):
    """Predefined categories with display names."""
    # Income categories
    SALARY = ("salary", "💰 Salary", TransactionType.INCOME)
    FREELANCE = ("freelance", "💼 Freelance", TransactionType.INCOME)
    INVESTMENT = ("investment", "📈 Investment", TransactionType.INCOME)
    GIFT = ("gift", "🎁 Gift", TransactionType.INCOME)
    OTHER_INCOME = ("other_income", "💵 Other Income", TransactionType.INCOME)
    
    # Expense categories
    FOOD = ("food", "🍔 Food & Dining", TransactionType.EXPENSE)
    TRANSPORT = ("transport", "🚗 Transport", TransactionType.EXPENSE)
    HOUSING = ("housing", "🏠 Housing", TransactionType.EXPENSE)
    UTILITIES = ("utilities", "💡 Utilities", TransactionType.EXPENSE)
    HEALTHCARE = ("healthcare", "🏥 Healthcare", TransactionType.EXPENSE)
    ENTERTAINMENT = ("entertainment", "🎬 Entertainment", TransactionType.EXPENSE)
    SHOPPING = ("shopping", "🛍️ Shopping", TransactionType.EXPENSE)
    EDUCATION = ("education", "📚 Education", TransactionType.EXPENSE)
    TRAVEL = ("travel", "✈️ Travel", TransactionType.EXPENSE)
    OTHER_EXPENSE = ("other_expense", "💸 Other Expense", TransactionType.EXPENSE)
    
    def __init__(self, key: str, display_name: str, transaction_type: TransactionType):
        self.key = key
        self.display_name = display_name
        self.transaction_type = transaction_type
    
    @classmethod
    def get_by_key(cls, key: str) -> Optional['Category']:
        """Get category by its key."""
        for category in cls:
            if category.key == key:
                return category
        return None
    
    @classmethod
    def get_by_type(cls, transaction_type: TransactionType) -> List['Category']:
        """Get all categories of a specific type."""
        return [c for c in cls if c.transaction_type == transaction_type]
    
    @classmethod
    def get_income_categories(cls) -> List['Category']:
        """Get all income categories."""
        return cls.get_by_type(TransactionType.INCOME)
    
    @classmethod
    def get_expense_categories(cls) -> List['Category']:
        """Get all expense categories."""
        return cls.get_by_type(TransactionType.EXPENSE)


@dataclass
class Transaction:
    """
    Represents a single financial transaction.
    
    Design Pattern: Value Object Pattern - Immutable, equality based on values
    SOLID Principle: Single Responsibility - Only represents transaction data
    """
    
    amount: float
    category: Category
    description: str
    date: date
    transaction_type: TransactionType
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    notes: str = ""
    
    def __post_init__(self):
        """Validate transaction data after initialization."""
        if self.amount <= 0:
            raise ValueError(f"Amount must be positive, got {self.amount}")
        
        if not self.description or len(self.description.strip()) == 0:
            raise ValueError("Description cannot be empty")
        
        if len(self.description) > 200:
            raise ValueError("Description too long (max 200 characters)")
        
        # Ensure transaction type matches category
        if self.category.transaction_type != self.transaction_type:
            raise ValueError(
                f"Category {self.category.display_name} is for {self.category.transaction_type.value}, "
                f"but transaction type is {self.transaction_type.value}"
            )
    
    @property
    def formatted_amount(self) -> str:
        """Return formatted amount with currency symbol."""
        symbol = "+" if self.transaction_type == TransactionType.INCOME else "-"
        return f"{symbol}${self.amount:,.2f}"
    
    @property
    def month_year(self) -> str:
        """Return month and year for grouping."""
        return self.date.strftime("%B %Y")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category.key,
            'description': self.description,
            'date': self.date.isoformat(),
            'transaction_type': self.transaction_type.value,
            'created_at': self.created_at.isoformat(),
            'tags': self.tags,
            'notes': self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Transaction':
        """Create transaction from dictionary."""
        return cls(
            id=data['id'],
            amount=data['amount'],
            category=Category.get_by_key(data['category']),
            description=data['description'],
            date=date.fromisoformat(data['date']),
            transaction_type=TransactionType(data['transaction_type']),
            created_at=datetime.fromisoformat(data['created_at']),
            tags=data.get('tags', []),
            notes=data.get('notes', '')
        )


@dataclass
class Budget:
    """
    Represents a monthly budget for a category.
    
    SOLID Principle: Single Responsibility - Manages budget limits
    """
    
    category: Category
    month: date  # First day of the month
    limit_amount: float
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    
    def __post_init__(self):
        """Validate budget data."""
        if self.limit_amount <= 0:
            raise ValueError(f"Budget limit must be positive, got {self.limit_amount}")
        
        # Ensure month is first day of month
        if self.month.day != 1:
            raise ValueError(f"Budget month must be first day of month, got {self.month}")
    
    @property
    def month_year(self) -> str:
        """Return month and year for display."""
        return self.month.strftime("%B %Y")
    
    def is_exceeded(self, total_spent: float) -> bool:
        """Check if budget is exceeded."""
        return total_spent > self.limit_amount
    
    def remaining_budget(self, total_spent: float) -> float:
        """Calculate remaining budget."""
        return max(0, self.limit_amount - total_spent)
    
    def percent_used(self, total_spent: float) -> float:
        """Calculate percentage of budget used."""
        if self.limit_amount == 0:
            return 0
        return min(100, (total_spent / self.limit_amount) * 100)


class User:
    """
    Represents a user of the expense tracker.
    
    SOLID Principles:
    - Single Responsibility: Manages user data and preferences
    - Encapsulation: Protects sensitive data
    """
    
    def __init__(self, username: str, email: str = "", currency: str = "USD"):
        self.username = username
        self.email = email
        self.currency = currency
        self.created_at = datetime.now()
        self.preferences = {
            'default_category': Category.OTHER_EXPENSE.key,
            'default_view': 'monthly',
            'notifications_enabled': True
        }
        self._validate()
    
    def _validate(self):
        """Validate user data."""
        if not self.username or len(self.username.strip()) == 0:
            raise ValueError("Username cannot be empty")
        
        if len(self.username) > 50:
            raise ValueError("Username too long (max 50 characters)")
        
        if self.email and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
            raise ValueError("Invalid email format")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary for JSON serialization."""
        return {
            'username': self.username,
            'email': self.email,
            'currency': self.currency,
            'created_at': self.created_at.isoformat(),
            'preferences': self.preferences
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Create user from dictionary."""
        user = cls(
            username=data['username'],
            email=data.get('email', ''),
            currency=data.get('currency', 'USD')
        )
        user.created_at = datetime.fromisoformat(data['created_at'])
        user.preferences = data.get('preferences', {})
        return user


def demonstrate_domain_models():
    """
    Demonstrate the domain models in action.
    """
    print("\n" + "=" * 60)
    print("SECTION 1: DOMAIN MODELS & DATA STRUCTURES")
    print("=" * 60)
    
    # CREATE USER
    print("\n1. CREATING USER")
    print("-" * 40)
    
    user = User("john_doe", "john@example.com", "USD")
    print(f"  Username: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Currency: {user.currency}")
    print(f"  Created: {user.created_at.strftime('%Y-%m-%d %H:%M')}")
    
    # CREATE TRANSACTION
    print("\n2. CREATING TRANSACTION")
    print("-" * 40)
    
    transaction = Transaction(
        amount=45.50,
        category=Category.FOOD,
        description="Dinner at Italian restaurant",
        date=date.today(),
        transaction_type=TransactionType.EXPENSE,
        tags=["dinner", "restaurant"],
        notes="Had the lasagna"
    )
    
    print(f"  ID: {transaction.id}")
    print(f"  Amount: {transaction.formatted_amount}")
    print(f"  Category: {transaction.category.display_name}")
    print(f"  Description: {transaction.description}")
    print(f"  Tags: {', '.join(transaction.tags)}")
    print(f"  Month/Year: {transaction.month_year}")
    
    # TRANSACTION VALIDATION
    print("\n3. TRANSACTION VALIDATION")
    print("-" * 40)
    
    try:
        invalid_transaction = Transaction(
            amount=-100,  # Negative amount
            category=Category.FOOD,
            description="Invalid transaction",
            date=date.today(),
            transaction_type=TransactionType.EXPENSE
        )
    except ValueError as e:
        print(f"  ✓ Validation caught: {e}")
    
    # BUDGET CREATION
    print("\n4. CREATING BUDGET")
    print("-" * 40)
    
    budget = Budget(
        category=Category.FOOD,
        month=date.today().replace(day=1),
        limit_amount=500
    )
    
    print(f"  Category: {budget.category.display_name}")
    print(f"  Month: {budget.month_year}")
    print(f"  Limit: ${budget.limit_amount:,.2f}")
    
    # Test budget calculations
    total_spent = 350.75
    print(f"\n  Total spent: ${total_spent:,.2f}")
    print(f"  Remaining: ${budget.remaining_budget(total_spent):,.2f}")
    print(f"  Usage: {budget.percent_used(total_spent):.1f}%")
    print(f"  Exceeded: {budget.is_exceeded(total_spent)}")
    
    # CATEGORY ENUMERATION
    print("\n5. CATEGORY ENUMERATION")
    print("-" * 40)
    
    print("\n  Income Categories:")
    for cat in Category.get_income_categories():
        print(f"    • {cat.display_name} ({cat.key})")
    
    print("\n  Expense Categories:")
    for cat in Category.get_expense_categories()[:5]:  # Show first 5
        print(f"    • {cat.display_name} ({cat.key})")
    
    # SERIALIZATION
    print("\n6. TRANSACTION SERIALIZATION")
    print("-" * 40)
    
    # Convert to dict
    transaction_dict = transaction.to_dict()
    print(f"  Dict: {transaction_dict}")
    
    # Recreate from dict
    reconstructed = Transaction.from_dict(transaction_dict)
    print(f"  Reconstructed: {reconstructed.description} - {reconstructed.formatted_amount}")
    print(f"  IDs match: {transaction.id == reconstructed.id}")


if __name__ == "__main__":
    demonstrate_domain_models()
```

---

## 💾 Section 2: Storage & Persistence Layer

Implement robust JSON-based storage with backup, recovery, and data validation.

**SOLID Principles Applied:**
- Single Responsibility: Storage handles only persistence
- Open/Closed: New storage backends can be added
- Dependency Inversion: High-level modules depend on storage interface

**Design Patterns:**
- Repository Pattern: Abstracts data storage
- Singleton Pattern: Single storage manager instance

```python
"""
CLI EXPENSE TRACKER - SECTION 2: STORAGE & PERSISTENCE

This section implements data persistence with JSON storage.

SOLID Principles Applied:
- Single Responsibility: Storage handles only persistence
- Open/Closed: New storage backends can be added
- Dependency Inversion: High-level modules depend on storage interface

Design Patterns:
- Repository Pattern: Abstracts data storage operations
- Singleton Pattern: Single storage manager instance
"""

import json
import os
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from datetime import datetime, date, timedelta
import logging
from contextlib import contextmanager
import hashlib
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StorageInterface:
    """
    Abstract interface for storage operations.
    
    SOLID Principle: Interface Segregation - Defines only what's needed
    Design Pattern: Interface Pattern - Contract for storage implementations
    """
    
    def save_user(self, user_data: Dict[str, Any]) -> bool:
        raise NotImplementedError
    
    def load_user(self, username: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError
    
    def save_transactions(self, username: str, transactions: List[Dict[str, Any]]) -> bool:
        raise NotImplementedError
    
    def load_transactions(self, username: str) -> List[Dict[str, Any]]:
        raise NotImplementedError
    
    def save_budgets(self, username: str, budgets: List[Dict[str, Any]]) -> bool:
        raise NotImplementedError
    
    def load_budgets(self, username: str) -> List[Dict[str, Any]]:
        raise NotImplementedError


class JSONStorage(StorageInterface):
    """
    JSON file-based storage implementation.
    
    SOLID Principles:
    - Single Responsibility: Handles JSON file operations
    - Open/Closed: Can be extended with encryption, compression
    
    Design Pattern: Repository Pattern - Abstracts data access
    """
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.backup_dir = self.data_dir / "backups"
        self._init_directories()
    
    def _init_directories(self):
        """Initialize storage directories."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Create user subdirectories
        self.users_dir = self.data_dir / "users"
        self.transactions_dir = self.data_dir / "transactions"
        self.budgets_dir = self.data_dir / "budgets"
        
        for dir_path in [self.users_dir, self.transactions_dir, self.budgets_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _get_user_file(self, username: str, data_type: str) -> Path:
        """Get file path for user data."""
        if data_type == "user":
            return self.users_dir / f"{username}.json"
        elif data_type == "transactions":
            return self.transactions_dir / f"{username}.json"
        elif data_type == "budgets":
            return self.budgets_dir / f"{username}.json"
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    
    def _backup_file(self, filepath: Path) -> None:
        """Create backup of file before modification."""
        if filepath.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{filepath.stem}_{timestamp}{filepath.suffix}"
            backup_path = self.backup_dir / backup_name
            shutil.copy2(filepath, backup_path)
            
            # Clean old backups (keep last 10)
            backups = sorted(self.backup_dir.glob(f"{filepath.stem}_*.json"))
            for old_backup in backups[:-10]:
                old_backup.unlink()
    
    def _save_json(self, filepath: Path, data: Any) -> bool:
        """Save data to JSON file with backup."""
        try:
            self._backup_file(filepath)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            logger.info(f"Saved data to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to save to {filepath}: {e}")
            return False
    
    def _load_json(self, filepath: Path) -> Optional[Any]:
        """Load data from JSON file."""
        try:
            if not filepath.exists():
                return None
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load from {filepath}: {e}")
            return None
    
    def save_user(self, user_data: Dict[str, Any]) -> bool:
        """Save user data."""
        filepath = self._get_user_file(user_data['username'], "user")
        return self._save_json(filepath, user_data)
    
    def load_user(self, username: str) -> Optional[Dict[str, Any]]:
        """Load user data."""
        filepath = self._get_user_file(username, "user")
        return self._load_json(filepath)
    
    def save_transactions(self, username: str, transactions: List[Dict[str, Any]]) -> bool:
        """Save user transactions."""
        filepath = self._get_user_file(username, "transactions")
        return self._save_json(filepath, transactions)
    
    def load_transactions(self, username: str) -> List[Dict[str, Any]]:
        """Load user transactions."""
        filepath = self._get_user_file(username, "transactions")
        data = self._load_json(filepath)
        return data if data is not None else []
    
    def save_budgets(self, username: str, budgets: List[Dict[str, Any]]) -> bool:
        """Save user budgets."""
        filepath = self._get_user_file(username, "budgets")
        return self._save_json(filepath, budgets)
    
    def load_budgets(self, username: str) -> List[Dict[str, Any]]:
        """Load user budgets."""
        filepath = self._get_user_file(username, "budgets")
        data = self._load_json(filepath)
        return data if data is not None else []
    
    def delete_user_data(self, username: str) -> bool:
        """Delete all data for a user."""
        try:
            for data_type in ["user", "transactions", "budgets"]:
                filepath = self._get_user_file(username, data_type)
                if filepath.exists():
                    filepath.unlink()
            logger.info(f"Deleted all data for user: {username}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete user data: {e}")
            return False
    
    def list_users(self) -> List[str]:
        """List all registered users."""
        users = []
        for filepath in self.users_dir.glob("*.json"):
            users.append(filepath.stem)
        return users
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get storage statistics."""
        stats = {
            'total_users': len(self.list_users()),
            'total_transactions': 0,
            'total_backups': len(list(self.backup_dir.glob("*.json"))),
            'storage_size_mb': 0
        }
        
        # Calculate total transactions and storage size
        total_size = 0
        for filepath in self.transactions_dir.glob("*.json"):
            transactions = self._load_json(filepath)
            if transactions:
                stats['total_transactions'] += len(transactions)
            total_size += filepath.stat().st_size
        
        stats['storage_size_mb'] = total_size / (1024 * 1024)
        
        return stats


class TransactionRepository:
    """
    Repository for transaction operations.
    
    Design Pattern: Repository Pattern - Domain-driven data access
    """
    
    def __init__(self, storage: JSONStorage):
        self.storage = storage
    
    def add_transaction(self, username: str, transaction: Transaction) -> bool:
        """Add a new transaction."""
        transactions = self.get_all_transactions(username)
        transactions.append(transaction.to_dict())
        return self.storage.save_transactions(username, transactions)
    
    def get_all_transactions(self, username: str) -> List[Transaction]:
        """Get all transactions for a user."""
        transaction_dicts = self.storage.load_transactions(username)
        return [Transaction.from_dict(t) for t in transaction_dicts]
    
    def get_transactions_by_date_range(self, username: str, 
                                       start_date: date, 
                                       end_date: date) -> List[Transaction]:
        """Get transactions within date range."""
        all_transactions = self.get_all_transactions(username)
        return [
            t for t in all_transactions 
            if start_date <= t.date <= end_date
        ]
    
    def get_transactions_by_category(self, username: str, 
                                     category: Category) -> List[Transaction]:
        """Get transactions by category."""
        all_transactions = self.get_all_transactions(username)
        return [t for t in all_transactions if t.category == category]
    
    def get_transactions_by_month(self, username: str, 
                                  year: int, month: int) -> List[Transaction]:
        """Get transactions for a specific month."""
        all_transactions = self.get_all_transactions(username)
        return [
            t for t in all_transactions 
            if t.date.year == year and t.date.month == month
        ]
    
    def update_transaction(self, username: str, 
                          transaction_id: str, 
                          updated_transaction: Transaction) -> bool:
        """Update an existing transaction."""
        transactions = self.get_all_transactions(username)
        
        for i, t in enumerate(transactions):
            if t.id == transaction_id:
                transactions[i] = updated_transaction
                return self.storage.save_transactions(username, [t.to_dict() for t in transactions])
        
        logger.warning(f"Transaction {transaction_id} not found")
        return False
    
    def delete_transaction(self, username: str, transaction_id: str) -> bool:
        """Delete a transaction."""
        transactions = self.get_all_transactions(username)
        filtered_transactions = [t for t in transactions if t.id != transaction_id]
        
        if len(filtered_transactions) == len(transactions):
            logger.warning(f"Transaction {transaction_id} not found")
            return False
        
        return self.storage.save_transactions(username, [t.to_dict() for t in filtered_transactions])
    
    def get_monthly_summary(self, username: str, year: int, month: int) -> Dict[str, Any]:
        """Get monthly summary of income and expenses."""
        transactions = self.get_transactions_by_month(username, year, month)
        
        total_income = sum(t.amount for t in transactions if t.transaction_type == TransactionType.INCOME)
        total_expenses = sum(t.amount for t in transactions if t.transaction_type == TransactionType.EXPENSE)
        
        expenses_by_category = defaultdict(float)
        for t in transactions:
            if t.transaction_type == TransactionType.EXPENSE:
                expenses_by_category[t.category.display_name] += t.amount
        
        return {
            'year': year,
            'month': month,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_savings': total_income - total_expenses,
            'expenses_by_category': dict(expenses_by_category),
            'transaction_count': len(transactions)
        }


class BudgetRepository:
    """
    Repository for budget operations.
    
    Design Pattern: Repository Pattern - Domain-driven data access
    """
    
    def __init__(self, storage: JSONStorage):
        self.storage = storage
    
    def add_budget(self, username: str, budget: Budget) -> bool:
        """Add a new budget."""
        budgets = self.get_all_budgets(username)
        budgets.append(budget.to_dict())
        return self.storage.save_budgets(username, budgets)
    
    def get_all_budgets(self, username: str) -> List[Budget]:
        """Get all budgets for a user."""
        budget_dicts = self.storage.load_budgets(username)
        return [Budget.from_dict(b) for b in budget_dicts]
    
    def get_budget_for_month(self, username: str, 
                            category: Category, 
                            month: date) -> Optional[Budget]:
        """Get budget for a specific category and month."""
        budgets = self.get_all_budgets(username)
        for budget in budgets:
            if budget.category == category and budget.month == month:
                return budget
        return None
    
    def update_budget(self, username: str, budget: Budget) -> bool:
        """Update an existing budget."""
        budgets = self.get_all_budgets(username)
        
        for i, b in enumerate(budgets):
            if b.category == budget.category and b.month == budget.month:
                budgets[i] = budget
                return self.storage.save_budgets(username, [b.to_dict() for b in budgets])
        
        # If not found, add it
        return self.add_budget(username, budget)
    
    def delete_budget(self, username: str, category: Category, month: date) -> bool:
        """Delete a budget."""
        budgets = self.get_all_budgets(username)
        filtered_budgets = [b for b in budgets if not (b.category == category and b.month == month)]
        
        if len(filtered_budgets) == len(budgets):
            logger.warning(f"Budget not found for {category.key} in {month}")
            return False
        
        return self.storage.save_budgets(username, [b.to_dict() for b in filtered_budgets])


def demonstrate_storage_layer():
    """
    Demonstrate the storage and persistence layer.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: STORAGE & PERSISTENCE LAYER")
    print("=" * 60)
    
    # INITIALIZE STORAGE
    print("\n1. INITIALIZING STORAGE")
    print("-" * 40)
    
    storage = JSONStorage("test_data")
    print(f"  Data directory: {storage.data_dir}")
    print(f"  Backup directory: {storage.backup_dir}")
    
    # SAVE USER
    print("\n2. SAVING USER")
    print("-" * 40)
    
    user = User("alice", "alice@example.com")
    success = storage.save_user(user.to_dict())
    print(f"  User saved: {success}")
    
    # LOAD USER
    print("\n3. LOADING USER")
    print("-" * 40)
    
    loaded_user_data = storage.load_user("alice")
    if loaded_user_data:
        loaded_user = User.from_dict(loaded_user_data)
        print(f"  Loaded user: {loaded_user.username}")
        print(f"  Email: {loaded_user.email}")
    
    # SAVE TRANSACTIONS
    print("\n4. SAVING TRANSACTIONS")
    print("-" * 40)
    
    transaction_repo = TransactionRepository(storage)
    
    # Create some transactions
    transactions = [
        Transaction(
            amount=2500.00,
            category=Category.SALARY,
            description="Monthly salary",
            date=date(2026, 3, 1),
            transaction_type=TransactionType.INCOME
        ),
        Transaction(
            amount=85.50,
            category=Category.FOOD,
            description="Grocery shopping",
            date=date(2026, 3, 5),
            transaction_type=TransactionType.EXPENSE,
            tags=["groceries", "supermarket"]
        ),
        Transaction(
            amount=45.00,
            category=Category.TRANSPORT,
            description="Uber rides",
            date=date(2026, 3, 10),
            transaction_type=TransactionType.EXPENSE
        )
    ]
    
    for transaction in transactions:
        transaction_repo.add_transaction("alice", transaction)
    
    print(f"  Added {len(transactions)} transactions")
    
    # LOAD TRANSACTIONS
    print("\n5. LOADING TRANSACTIONS")
    print("-" * 40)
    
    loaded_transactions = transaction_repo.get_all_transactions("alice")
    print(f"  Loaded {len(loaded_transactions)} transactions")
    
    for t in loaded_transactions:
        print(f"    {t.date}: {t.description} - {t.formatted_amount}")
    
    # MONTHLY SUMMARY
    print("\n6. MONTHLY SUMMARY")
    print("-" * 40)
    
    summary = transaction_repo.get_monthly_summary("alice", 2026, 3)
    print(f"  Total Income: ${summary['total_income']:,.2f}")
    print(f"  Total Expenses: ${summary['total_expenses']:,.2f}")
    print(f"  Net Savings: ${summary['net_savings']:,.2f}")
    print(f"  Transactions: {summary['transaction_count']}")
    
    print("\n  Expenses by Category:")
    for category, amount in summary['expenses_by_category'].items():
        print(f"    {category}: ${amount:,.2f}")
    
    # STORAGE STATS
    print("\n7. STORAGE STATISTICS")
    print("-" * 40)
    
    stats = storage.get_storage_stats()
    print(f"  Total users: {stats['total_users']}")
    print(f"  Total transactions: {stats['total_transactions']}")
    print(f"  Total backups: {stats['total_backups']}")
    print(f"  Storage size: {stats['storage_size_mb']:.2f} MB")
    
    # CLEANUP
    print("\n8. CLEANING UP")
    print("-" * 40)
    
    storage.delete_user_data("alice")
    print("  Test data cleaned up")
    
    # Clean test directory
    import shutil
    if Path("test_data").exists():
        shutil.rmtree("test_data")
        print("  Test directory removed")


if __name__ == "__main__":
    demonstrate_storage_layer()
```

---

## 📊 Section 3: Analytics & Reporting Engine

Build a powerful reporting engine with multiple report types and visualizations.

**SOLID Principles Applied:**
- Single Responsibility: Each report type is separate
- Open/Closed: New report types can be added

**Design Pattern: Strategy Pattern** – Different reporting strategies

```python
"""
CLI EXPENSE TRACKER - SECTION 3: ANALYTICS & REPORTING

This section implements analytics and reporting functionality.

SOLID Principles Applied:
- Single Responsibility: Each report type is separate
- Open/Closed: New report types can be added

Design Pattern: Strategy Pattern - Different reporting strategies
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, date, timedelta
from collections import defaultdict, Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from dataclasses import dataclass
import numpy as np


@dataclass
class ReportData:
    """Container for report data."""
    title: str
    generated_at: datetime
    data: Dict[str, Any]
    summary: str


class ReportGenerator:
    """
    Base class for report generation.
    
    Design Pattern: Template Method Pattern - Defines report structure
    """
    
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions
        self._validate_transactions()
    
    def _validate_transactions(self):
        """Validate transactions before generating report."""
        if not self.transactions:
            raise ValueError("No transactions to generate report")
    
    def generate(self) -> ReportData:
        """Generate the report (template method)."""
        self._pre_process()
        data = self._collect_data()
        summary = self._create_summary(data)
        return ReportData(
            title=self._get_title(),
            generated_at=datetime.now(),
            data=data,
            summary=summary
        )
    
    def _pre_process(self):
        """Hook method for preprocessing."""
        pass
    
    def _collect_data(self) -> Dict[str, Any]:
        """Collect report data (to be implemented)."""
        raise NotImplementedError
    
    def _create_summary(self, data: Dict[str, Any]) -> str:
        """Create report summary (to be implemented)."""
        raise NotImplementedError
    
    def _get_title(self) -> str:
        """Get report title (to be implemented)."""
        raise NotImplementedError


class MonthlyReport(ReportGenerator):
    """Monthly financial report."""
    
    def __init__(self, transactions: List[Transaction], year: int, month: int):
        super().__init__(transactions)
        self.year = year
        self.month = month
        self.month_transactions = [
            t for t in transactions 
            if t.date.year == year and t.date.month == month
        ]
    
    def _get_title(self) -> str:
        return f"Monthly Financial Report - {date(self.year, self.month, 1).strftime('%B %Y')}"
    
    def _collect_data(self) -> Dict[str, Any]:
        """Collect monthly report data."""
        income = [t for t in self.month_transactions if t.transaction_type == TransactionType.INCOME]
        expenses = [t for t in self.month_transactions if t.transaction_type == TransactionType.EXPENSE]
        
        total_income = sum(t.amount for t in income)
        total_expenses = sum(t.amount for t in expenses)
        net_savings = total_income - total_expenses
        
        # Expenses by category
        expenses_by_category = defaultdict(float)
        for t in expenses:
            expenses_by_category[t.category.display_name] += t.amount
        
        # Daily spending
        daily_spending = defaultdict(float)
        for t in expenses:
            daily_spending[t.date] += t.amount
        
        # Top expenses
        top_expenses = sorted(expenses, key=lambda x: x.amount, reverse=True)[:5]
        
        # Income sources
        income_by_source = defaultdict(float)
        for t in income:
            income_by_source[t.category.display_name] += t.amount
        
        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_savings': net_savings,
            'expenses_by_category': dict(expenses_by_category),
            'income_by_source': dict(income_by_source),
            'daily_spending': dict(daily_spending),
            'top_expenses': [(t.description, t.amount) for t in top_expenses],
            'transaction_count': len(self.month_transactions),
            'savings_rate': (net_savings / total_income * 100) if total_income > 0 else 0
        }
    
    def _create_summary(self, data: Dict[str, Any]) -> str:
        """Create monthly summary text."""
        return (
            f"Income: ${data['total_income']:,.2f} | "
            f"Expenses: ${data['total_expenses']:,.2f} | "
            f"Savings: ${data['net_savings']:,.2f} | "
            f"Savings Rate: {data['savings_rate']:.1f}% | "
            f"Transactions: {data['transaction_count']}"
        )


class YearlyReport(ReportGenerator):
    """Yearly financial report with trends."""
    
    def __init__(self, transactions: List[Transaction], year: int):
        super().__init__(transactions)
        self.year = year
        self.year_transactions = [t for t in transactions if t.date.year == year]
    
    def _get_title(self) -> str:
        return f"Yearly Financial Report - {self.year}"
    
    def _collect_data(self) -> Dict[str, Any]:
        """Collect yearly report data."""
        monthly_data = {}
        
        for month in range(1, 13):
            month_transactions = [t for t in self.year_transactions if t.date.month == month]
            if month_transactions:
                income = sum(t.amount for t in month_transactions if t.transaction_type == TransactionType.INCOME)
                expenses = sum(t.amount for t in month_transactions if t.transaction_type == TransactionType.EXPENSE)
                monthly_data[month] = {
                    'income': income,
                    'expenses': expenses,
                    'net': income - expenses
                }
            else:
                monthly_data[month] = {'income': 0, 'expenses': 0, 'net': 0}
        
        # Category trends
        category_trends = defaultdict(lambda: defaultdict(float))
        for t in self.year_transactions:
            if t.transaction_type == TransactionType.EXPENSE:
                category_trends[t.category.display_name][t.date.month] += t.amount
        
        total_income = sum(data['income'] for data in monthly_data.values())
        total_expenses = sum(data['expenses'] for data in monthly_data.values())
        
        # Best and worst months
        best_month = max(monthly_data.items(), key=lambda x: x[1]['net'])
        worst_month = min(monthly_data.items(), key=lambda x: x[1]['net'])
        
        return {
            'monthly_data': monthly_data,
            'category_trends': dict(category_trends),
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_savings': total_income - total_expenses,
            'best_month': best_month,
            'worst_month': worst_month,
            'average_monthly_expense': total_expenses / 12,
            'average_monthly_income': total_income / 12
        }
    
    def _create_summary(self, data: Dict[str, Any]) -> str:
        """Create yearly summary text."""
        return (
            f"Year {self.year}: Income ${data['total_income']:,.2f} | "
            f"Expenses ${data['total_expenses']:,.2f} | "
            f"Net ${data['net_savings']:,.2f} | "
            f"Avg Monthly Expense ${data['average_monthly_expense']:,.2f}"
        )


class CategoryReport(ReportGenerator):
    """Detailed category spending report."""
    
    def __init__(self, transactions: List[Transaction], category: Category, year: int = None):
        super().__init__(transactions)
        self.category = category
        self.year = year
        self.filtered_transactions = [
            t for t in transactions if t.category == category
        ]
        if year:
            self.filtered_transactions = [
                t for t in self.filtered_transactions if t.date.year == year
            ]
    
    def _get_title(self) -> str:
        title = f"Category Report - {self.category.display_name}"
        if self.year:
            title += f" ({self.year})"
        return title
    
    def _collect_data(self) -> Dict[str, Any]:
        """Collect category report data."""
        total_spent = sum(t.amount for t in self.filtered_transactions)
        
        # Monthly spending
        monthly_spending = defaultdict(float)
        for t in self.filtered_transactions:
            key = f"{t.date.year}-{t.date.month:02d}"
            monthly_spending[key] += t.amount
        
        # Transaction frequency by day of week
        weekday_spending = defaultdict(float)
        weekday_counts = defaultdict(int)
        for t in self.filtered_transactions:
            weekday = t.date.strftime('%A')
            weekday_spending[weekday] += t.amount
            weekday_counts[weekday] += 1
        
        average_by_weekday = {
            day: (weekday_spending[day] / weekday_counts[day] if weekday_counts[day] > 0 else 0)
            for day in weekday_spending
        }
        
        # Common keywords in descriptions
        keywords = Counter()
        for t in self.filtered_transactions:
            words = t.description.lower().split()
            keywords.update(words[:3])  # Top 3 words from each description
        
        return {
            'total_spent': total_spent,
            'transaction_count': len(self.filtered_transactions),
            'average_transaction': total_spent / len(self.filtered_transactions) if self.filtered_transactions else 0,
            'monthly_spending': dict(monthly_spending),
            'weekday_spending': dict(weekday_spending),
            'average_by_weekday': dict(average_by_weekday),
            'top_keywords': dict(keywords.most_common(10)),
            'largest_transaction': max(self.filtered_transactions, key=lambda x: x.amount) if self.filtered_transactions else None
        }
    
    def _create_summary(self, data: Dict[str, Any]) -> str:
        """Create category summary text."""
        return (
            f"Total spent: ${data['total_spent']:,.2f} | "
            f"Transactions: {data['transaction_count']} | "
            f"Average: ${data['average_transaction']:,.2f}"
        )


class BudgetReport(ReportGenerator):
    """Budget vs actual spending report."""
    
    def __init__(self, transactions: List[Transaction], budgets: List[Budget]):
        super().__init__(transactions)
        self.budgets = budgets
    
    def _get_title(self) -> str:
        return "Budget vs Actual Spending Report"
    
    def _collect_data(self) -> Dict[str, Any]:
        """Collect budget report data."""
        budget_performance = []
        
        for budget in self.budgets:
            # Get expenses for this category and month
            month_transactions = [
                t for t in self.transactions 
                if t.category == budget.category 
                and t.date.year == budget.month.year 
                and t.date.month == budget.month.month
                and t.transaction_type == TransactionType.EXPENSE
            ]
            
            total_spent = sum(t.amount for t in month_transactions)
            
            budget_performance.append({
                'category': budget.category.display_name,
                'month': budget.month.strftime('%B %Y'),
                'budget': budget.limit_amount,
                'actual': total_spent,
                'difference': budget.limit_amount - total_spent,
                'percentage': (total_spent / budget.limit_amount * 100) if budget.limit_amount > 0 else 0,
                'exceeded': total_spent > budget.limit_amount
            })
        
        # Sort by percentage (highest first)
        budget_performance.sort(key=lambda x: x['percentage'], reverse=True)
        
        total_budget = sum(b['budget'] for b in budget_performance)
        total_actual = sum(b['actual'] for b in budget_performance)
        
        return {
            'budget_performance': budget_performance,
            'total_budget': total_budget,
            'total_actual': total_actual,
            'overall_difference': total_budget - total_actual,
            'exceeded_count': sum(1 for b in budget_performance if b['exceeded']),
            'on_track_count': sum(1 for b in budget_performance if not b['exceeded'])
        }
    
    def _create_summary(self, data: Dict[str, Any]) -> str:
        """Create budget summary text."""
        return (
            f"Total Budget: ${data['total_budget']:,.2f} | "
            f"Actual: ${data['total_actual']:,.2f} | "
            f"Difference: ${data['overall_difference']:,.2f} | "
            f"Exceeded: {data['exceeded_count']} categories"
        )


class ReportVisualizer:
    """
    Visualizes report data with matplotlib.
    
    Design Pattern: Strategy Pattern - Different visualization strategies
    """
    
    @staticmethod
    def plot_monthly_summary(monthly_data: Dict[str, Any], save_path: str = None):
        """Plot monthly summary chart."""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # 1. Income vs Expenses
        ax1 = axes[0, 0]
        categories = ['Income', 'Expenses', 'Savings']
        values = [monthly_data['total_income'], monthly_data['total_expenses'], monthly_data['net_savings']]
        colors = ['#2ecc71', '#e74c3c', '#3498db']
        ax1.bar(categories, values, color=colors)
        ax1.set_title('Income vs Expenses vs Savings')
        ax1.set_ylabel('Amount ($)')
        ax1.grid(True, alpha=0.3)
        
        # 2. Expenses by Category (Pie Chart)
        ax2 = axes[0, 1]
        expenses = monthly_data['expenses_by_category']
        if expenses:
            categories = list(expenses.keys())
            amounts = list(expenses.values())
            ax2.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
            ax2.set_title('Expenses by Category')
        
        # 3. Daily Spending
        ax3 = axes[1, 0]
        daily = monthly_data['daily_spending']
        days = list(daily.keys())
        amounts = list(daily.values())
        ax3.plot(days, amounts, marker='o', linewidth=2, markersize=6)
        ax3.set_title('Daily Spending')
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Amount ($)')
        ax3.tick_params(axis='x', rotation=45)
        ax3.grid(True, alpha=0.3)
        
        # 4. Top Expenses
        ax4 = axes[1, 1]
        top = monthly_data['top_expenses'][:5]
        if top:
            descriptions = [t[0][:20] + '...' if len(t[0]) > 20 else t[0] for t in top]
            amounts = [t[1] for t in top]
            ax4.barh(descriptions, amounts, color='#e67e22')
            ax4.set_title('Top 5 Expenses')
            ax4.set_xlabel('Amount ($)')
        
        plt.suptitle(monthly_data.get('title', 'Monthly Financial Report'), fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=100, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_yearly_trend(yearly_data: Dict[str, Any], save_path: str = None):
        """Plot yearly trend chart."""
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        # 1. Monthly Income vs Expenses
        ax1 = axes[0]
        monthly_data = yearly_data['monthly_data']
        months = list(monthly_data.keys())
        incomes = [monthly_data[m]['income'] for m in months]
        expenses = [monthly_data[m]['expenses'] for m in months]
        
        x = range(len(months))
        width = 0.35
        ax1.bar([i - width/2 for i in x], incomes, width, label='Income', color='#2ecc71')
        ax1.bar([i + width/2 for i in x], expenses, width, label='Expenses', color='#e74c3c')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Amount ($)')
        ax1.set_title('Monthly Income vs Expenses')
        ax1.set_xticks(x)
        ax1.set_xticklabels([f'Month {m}' for m in months])
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Net Savings Trend
        ax2 = axes[1]
        net_savings = [monthly_data[m]['net'] for m in months]
        colors = ['#2ecc71' if ns >= 0 else '#e74c3c' for ns in net_savings]
        ax2.bar(x, net_savings, color=colors)
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Net Savings ($)')
        ax2.set_title('Monthly Net Savings')
        ax2.set_xticks(x)
        ax2.set_xticklabels([f'Month {m}' for m in months])
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax2.grid(True, alpha=0.3)
        
        plt.suptitle(yearly_data.get('title', 'Yearly Financial Trends'), fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=100, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_budget_performance(budget_data: Dict[str, Any], save_path: str = None):
        """Plot budget vs actual performance."""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        performance = budget_data['budget_performance']
        categories = [p['category'] for p in performance]
        budgets = [p['budget'] for p in performance]
        actuals = [p['actual'] for p in performance]
        
        x = range(len(categories))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], budgets, width, label='Budget', color='#3498db', alpha=0.7)
        ax.bar([i + width/2 for i in x], actuals, width, label='Actual', color='#e74c3c', alpha=0.7)
        
        # Add percentage labels
        for i, p in enumerate(performance):
            if p['percentage'] > 100:
                ax.text(i + width/2, p['actual'] + 10, f"{p['percentage']:.0f}%", 
                       ha='center', va='bottom', fontsize=9, color='red', fontweight='bold')
        
        ax.set_xlabel('Category')
        ax.set_ylabel('Amount ($)')
        ax.set_title('Budget vs Actual Spending by Category')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=100, bbox_inches='tight')
        
        plt.show()


def demonstrate_reporting_engine():
    """
    Demonstrate the reporting and analytics engine.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: ANALYTICS & REPORTING ENGINE")
    print("=" * 60)
    
    # CREATE SAMPLE DATA
    print("\n1. CREATING SAMPLE TRANSACTIONS")
    print("-" * 40)
    
    sample_transactions = []
    
    # Income transactions
    sample_transactions.append(Transaction(
        amount=5000.00, category=Category.SALARY,
        description="Monthly salary", date=date(2026, 3, 1),
        transaction_type=TransactionType.INCOME
    ))
    sample_transactions.append(Transaction(
        amount=1000.00, category=Category.FREELANCE,
        description="Freelance project", date=date(2026, 3, 15),
        transaction_type=TransactionType.INCOME
    ))
    
    # Expense transactions
    expenses = [
        (1200.00, Category.HOUSING, "Rent", date(2026, 3, 1)),
        (150.00, Category.UTILITIES, "Electricity bill", date(2026, 3, 5)),
        (85.50, Category.FOOD, "Groceries", date(2026, 3, 6)),
        (45.00, Category.TRANSPORT, "Uber rides", date(2026, 3, 7)),
        (32.50, Category.FOOD, "Restaurant dinner", date(2026, 3, 10)),
        (200.00, Category.SHOPPING, "New clothes", date(2026, 3, 12)),
        (60.00, Category.ENTERTAINMENT, "Movie and popcorn", date(2026, 3, 15)),
        (25.00, Category.TRANSPORT, "Gas", date(2026, 3, 18)),
        (55.00, Category.FOOD, "Coffee shop", date(2026, 3, 20)),
        (80.00, Category.HEALTHCARE, "Pharmacy", date(2026, 3, 22))
    ]
    
    for amount, category, desc, trans_date in expenses:
        sample_transactions.append(Transaction(
            amount=amount, category=category,
            description=desc, date=trans_date,
            transaction_type=TransactionType.EXPENSE
        ))
    
    print(f"  Created {len(sample_transactions)} sample transactions")
    
    # MONTHLY REPORT
    print("\n2. GENERATING MONTHLY REPORT")
    print("-" * 40)
    
    monthly_report = MonthlyReport(sample_transactions, 2026, 3)
    monthly_data = monthly_report.generate()
    
    print(f"  Title: {monthly_data.title}")
    print(f"  Summary: {monthly_data.summary}")
    print(f"  Total Income: ${monthly_data.data['total_income']:,.2f}")
    print(f"  Total Expenses: ${monthly_data.data['total_expenses']:,.2f}")
    print(f"  Net Savings: ${monthly_data.data['net_savings']:,.2f}")
    print(f"  Savings Rate: {monthly_data.data['savings_rate']:.1f}%")
    
    # CATEGORY REPORT
    print("\n3. GENERATING CATEGORY REPORT")
    print("-" * 40)
    
    food_report = CategoryReport(sample_transactions, Category.FOOD, 2026)
    food_data = food_report.generate()
    
    print(f"  Title: {food_data.title}")
    print(f"  Summary: {food_data.summary}")
    print(f"  Total spent on Food: ${food_data.data['total_spent']:,.2f}")
    print(f"  Number of transactions: {food_data.data['transaction_count']}")
    print(f"  Average transaction: ${food_data.data['average_transaction']:,.2f}")
    
    # BUDGET REPORT
    print("\n4. GENERATING BUDGET REPORT")
    print("-" * 40)
    
    # Create budgets
    budgets = [
        Budget(Category.HOUSING, date(2026, 3, 1), 1300.00),
        Budget(Category.FOOD, date(2026, 3, 1), 400.00),
        Budget(Category.TRANSPORT, date(2026, 3, 1), 100.00),
        Budget(Category.ENTERTAINMENT, date(2026, 3, 1), 150.00)
    ]
    
    budget_report = BudgetReport(sample_transactions, budgets)
    budget_data = budget_report.generate()
    
    print(f"  Title: {budget_data.title}")
    print(f"  Summary: {budget_data.summary}")
    print(f"  Exceeded categories: {budget_data.data['exceeded_count']}")
    print(f"  On-track categories: {budget_data.data['on_track_count']}")
    
    print("\n  Budget Performance:")
    for perf in budget_data.data['budget_performance']:
        status = "🔴 EXCEEDED" if perf['exceeded'] else "🟢 On track"
        print(f"    {perf['category']:20} Budget: ${perf['budget']:8,.2f} | "
              f"Actual: ${perf['actual']:8,.2f} | {perf['percentage']:.1f}% | {status}")
    
    # VISUALIZATION
    print("\n5. GENERATING VISUALIZATIONS")
    print("-" * 40)
    
    print("  Note: Visualizations would open in separate windows")
    print("  Uncomment the following lines to see the plots:")
    print("  # ReportVisualizer.plot_monthly_summary(monthly_data.data)")
    print("  # ReportVisualizer.plot_budget_performance(budget_data.data)")
    
    # Report export
    print("\n6. EXPORTING REPORTS")
    print("-" * 40)
    
    # Export to CSV
    export_dir = Path("reports")
    export_dir.mkdir(exist_ok=True)
    
    # Convert transactions to DataFrame
    df = pd.DataFrame([t.to_dict() for t in sample_transactions])
    csv_path = export_dir / f"transactions_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(csv_path, index=False)
    print(f"  Transactions exported to: {csv_path}")
    
    # Export monthly summary
    summary_df = pd.DataFrame([monthly_data.data])
    summary_csv = export_dir / f"monthly_summary_{datetime.now().strftime('%Y%m%d')}.csv"
    summary_df.to_csv(summary_csv, index=False)
    print(f"  Monthly summary exported to: {summary_csv}")


if __name__ == "__main__":
    demonstrate_reporting_engine()
```

---

## 🎮 Section 4: CLI Application & User Interface

Build the complete CLI application with interactive menus and commands.

**SOLID Principles Applied:**
- Single Responsibility: CLI handles only user interaction
- Dependency Inversion: CLI depends on service layer abstractions

**Design Patterns:**
- Command Pattern: Each CLI command is encapsulated
- Facade Pattern: Simplified interface to complex subsystems

```python
"""
CLI EXPENSE TRACKER - SECTION 4: CLI APPLICATION

This section implements the complete CLI application.

SOLID Principles Applied:
- Single Responsibility: CLI handles only user interaction
- Dependency Inversion: CLI depends on service layer abstractions

Design Patterns:
- Command Pattern: Each CLI command is encapsulated
- Facade Pattern: Simplified interface to complex subsystems
"""

import sys
import os
from typing import List, Dict, Any, Optional, Callable
from datetime import datetime, date, timedelta
import argparse
import cmd
from tabulate import tabulate
from colorama import init, Fore, Back, Style
import readline  # For better input handling

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class ConsoleColors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text: str):
    """Print formatted header."""
    print(f"\n{ConsoleColors.CYAN}{'=' * 60}{ConsoleColors.ENDC}")
    print(f"{ConsoleColors.BOLD}{ConsoleColors.CYAN}{text.center(60)}{ConsoleColors.ENDC}")
    print(f"{ConsoleColors.CYAN}{'=' * 60}{ConsoleColors.ENDC}\n")


def print_success(text: str):
    """Print success message."""
    print(f"{ConsoleColors.GREEN}✓ {text}{ConsoleColors.ENDC}")


def print_error(text: str):
    """Print error message."""
    print(f"{ConsoleColors.FAIL}✗ {text}{ConsoleColors.ENDC}")


def print_warning(text: str):
    """Print warning message."""
    print(f"{ConsoleColors.WARNING}⚠ {text}{ConsoleColors.ENDC}")


def print_info(text: str):
    """Print info message."""
    print(f"{ConsoleColors.BLUE}ℹ {text}{ConsoleColors.ENDC}")


def print_table(data: List[Dict], headers: List[str]):
    """Print formatted table."""
    table_data = [[row.get(h, '') for h in headers] for row in data]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


class ExpenseTrackerCLI(cmd.Cmd):
    """
    Main CLI application for expense tracking.
    
    Design Pattern: Command Pattern - Each do_* method is a command
    """
    
    intro = f"""
{ConsoleColors.CYAN}{'=' * 60}
{ConsoleColors.BOLD}💰 EXPENSE TRACKER - Personal Finance Manager{ConsoleColors.ENDC}
{ConsoleColors.CYAN}{'=' * 60}

Welcome to your personal expense tracker!
Type 'help' to see available commands.
Type 'help <command>' for command details.

{ConsoleColors.GREEN}Quick start:{ConsoleColors.ENDC}
  • register <username> - Create new account
  • login <username> - Login to existing account
  • add - Add a transaction
  • report - View monthly report
  • budget - Manage budgets

{ConsoleColors.CYAN}{'=' * 60}{ConsoleColors.ENDC}
"""
    
    prompt = f"{ConsoleColors.GREEN}expense-tracker>{ConsoleColors.ENDC} "
    
    def __init__(self):
        super().__init__()
        self.current_user: Optional[User] = None
        self.storage = JSONStorage()
        self.transaction_repo = TransactionRepository(self.storage)
        self.budget_repo = BudgetRepository(self.storage)
        self.visualizer = ReportVisualizer()
    
    # ==================== UTILITY METHODS ====================
    
    def _require_login(self) -> bool:
        """Check if user is logged in."""
        if not self.current_user:
            print_error("You must be logged in to use this command")
            print_info("Use 'login <username>' or 'register <username>'")
            return False
        return True
    
    def _get_current_month(self) -> Tuple[int, int]:
        """Get current year and month."""
        today = date.today()
        return today.year, today.month
    
    def _format_currency(self, amount: float) -> str:
        """Format amount as currency."""
        symbol = self.current_user.currency if self.current_user else "USD"
        return f"{symbol} ${amount:,.2f}"
    
    # ==================== COMMANDS ====================
    
    def do_register(self, arg: str):
        """
        Register a new user.
        Usage: register <username> [email]
        """
        args = arg.split()
        if not args:
            print_error("Please provide a username")
            print_info("Usage: register <username> [email]")
            return
        
        username = args[0]
        email = args[1] if len(args) > 1 else ""
        
        # Check if user already exists
        if self.storage.load_user(username):
            print_error(f"User '{username}' already exists")
            return
        
        try:
            user = User(username, email)
            if self.storage.save_user(user.to_dict()):
                print_success(f"User '{username}' registered successfully!")
                print_info(f"Now login with: login {username}")
            else:
                print_error("Failed to register user")
        except ValueError as e:
            print_error(f"Invalid data: {e}")
    
    def do_login(self, arg: str):
        """
        Login to an existing account.
        Usage: login <username>
        """
        if not arg:
            print_error("Please provide a username")
            print_info("Usage: login <username>")
            return
        
        username = arg.strip()
        user_data = self.storage.load_user(username)
        
        if not user_data:
            print_error(f"User '{username}' not found")
            print_info("Use 'register' to create a new account")
            return
        
        self.current_user = User.from_dict(user_data)
        print_success(f"Welcome back, {self.current_user.username}!")
        
        # Show quick stats
        year, month = self._get_current_month()
        summary = self.transaction_repo.get_monthly_summary(
            self.current_user.username, year, month
        )
        
        print(f"\n{ConsoleColors.CYAN}Current Month Summary:{ConsoleColors.ENDC}")
        print(f"  Income:   {self._format_currency(summary['total_income'])}")
        print(f"  Expenses: {self._format_currency(summary['total_expenses'])}")
        print(f"  Savings:  {self._format_currency(summary['net_savings'])}")
    
    def do_logout(self, arg: str):
        """Logout from current account."""
        if self.current_user:
            print_success(f"Goodbye, {self.current_user.username}!")
            self.current_user = None
        else:
            print_warning("No user is currently logged in")
    
    def do_add(self, arg: str):
        """
        Add a new transaction.
        Usage: add
        Follow the interactive prompts.
        """
        if not self._require_login():
            return
        
        print_header("ADD NEW TRANSACTION")
        
        # Transaction type
        print(f"\n{ConsoleColors.BOLD}Transaction Type:{ConsoleColors.ENDC}")
        print("1. Expense")
        print("2. Income")
        
        type_choice = input("Choose (1/2): ").strip()
        if type_choice == "1":
            transaction_type = TransactionType.EXPENSE
            categories = Category.get_expense_categories()
        elif type_choice == "2":
            transaction_type = TransactionType.INCOME
            categories = Category.get_income_categories()
        else:
            print_error("Invalid choice")
            return
        
        # Category
        print(f"\n{ConsoleColors.BOLD}Category:{ConsoleColors.ENDC}")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat.display_name}")
        
        try:
            cat_choice = int(input("Choose (1-{}): ".format(len(categories))))
            if 1 <= cat_choice <= len(categories):
                category = categories[cat_choice - 1]
            else:
                print_error("Invalid category")
                return
        except ValueError:
            print_error("Invalid input")
            return
        
        # Amount
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print_error("Amount must be positive")
                return
        except ValueError:
            print_error("Invalid amount")
            return
        
        # Description
        description = input("Description: ").strip()
        if not description:
            print_error("Description cannot be empty")
            return
        
        # Date
        date_str = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
        if date_str:
            try:
                trans_date = date.fromisoformat(date_str)
            except ValueError:
                print_error("Invalid date format")
                return
        else:
            trans_date = date.today()
        
        # Tags (optional)
        tags_str = input("Tags (comma-separated, optional): ").strip()
        tags = [t.strip() for t in tags_str.split(",")] if tags_str else []
        
        # Create transaction
        try:
            transaction = Transaction(
                amount=amount,
                category=category,
                description=description,
                date=trans_date,
                transaction_type=transaction_type,
                tags=tags
            )
            
            if self.transaction_repo.add_transaction(self.current_user.username, transaction):
                print_success(f"Transaction added successfully! ID: {transaction.id}")
                
                # Check budget alert for expenses
                if transaction_type == TransactionType.EXPENSE:
                    budget = self.budget_repo.get_budget_for_month(
                        self.current_user.username,
                        category,
                        trans_date.replace(day=1)
                    )
                    
                    if budget:
                        month_expenses = sum(
                            t.amount for t in self.transaction_repo.get_transactions_by_month(
                                self.current_user.username, trans_date.year, trans_date.month
                            )
                            if t.category == category and t.transaction_type == TransactionType.EXPENSE
                        )
                        
                        if budget.is_exceeded(month_expenses):
                            print_warning(
                                f"Budget alert! You've exceeded your {category.display_name} "
                                f"budget of ${budget.limit_amount:,.2f}"
                            )
            else:
                print_error("Failed to add transaction")
        except ValueError as e:
            print_error(f"Invalid transaction: {e}")
    
    def do_list(self, arg: str):
        """
        List transactions.
        Usage: list [month] [year]
        """
        if not self._require_login():
            return
        
        # Parse arguments
        args = arg.split()
        if args:
            try:
                year = int(args[0]) if len(args) > 0 else None
                month = int(args[1]) if len(args) > 1 else None
            except ValueError:
                print_error("Invalid year/month format")
                return
        else:
            # Default to current month
            year, month = self._get_current_month()
        
        if year and month:
            transactions = self.transaction_repo.get_transactions_by_month(
                self.current_user.username, year, month
            )
            title = f"Transactions for {date(year, month, 1).strftime('%B %Y')}"
        else:
            transactions = self.transaction_repo.get_all_transactions(
                self.current_user.username
            )
            title = "All Transactions"
        
        if not transactions:
            print_info("No transactions found")
            return
        
        print_header(title)
        
        # Prepare table data
        table_data = []
        for t in sorted(transactions, key=lambda x: x.date, reverse=True):
            table_data.append({
                'Date': t.date.strftime('%Y-%m-%d'),
                'Type': t.transaction_type.value.upper(),
                'Category': t.category.display_name,
                'Description': t.description[:30],
                'Amount': t.formatted_amount,
                'ID': t.id
            })
        
        print_table(table_data, ['Date', 'Type', 'Category', 'Description', 'Amount', 'ID'])
    
    def do_report(self, arg: str):
        """
        Generate spending report.
        Usage: report [monthly|yearly|category]
        """
        if not self._require_login():
            return
        
        args = arg.split()
        report_type = args[0] if args else "monthly"
        
        if report_type == "monthly":
            year, month = self._get_current_month()
            if len(args) > 1:
                try:
                    year = int(args[1])
                    month = int(args[2]) if len(args) > 2 else month
                except (ValueError, IndexError):
                    pass
            
            transactions = self.transaction_repo.get_all_transactions(
                self.current_user.username
            )
            
            if not transactions:
                print_info("No transactions to generate report")
                return
            
            monthly_report = MonthlyReport(transactions, year, month)
            report_data = monthly_report.generate()
            
            print_header(report_data.title)
            
            # Display summary
            print(f"{ConsoleColors.BOLD}Summary:{ConsoleColors.ENDC}")
            print(f"  {report_data.summary}\n")
            
            # Display breakdown
            print(f"{ConsoleColors.BOLD}Expenses by Category:{ConsoleColors.ENDC}")
            for category, amount in report_data.data['expenses_by_category'].items():
                percentage = (amount / report_data.data['total_expenses'] * 100) if report_data.data['total_expenses'] > 0 else 0
                bar_length = int(percentage / 2)
                bar = "█" * bar_length
                print(f"  {category:20} {self._format_currency(amount):>12} {bar} {percentage:.1f}%")
            
            # Top expenses
            print(f"\n{ConsoleColors.BOLD}Top 5 Expenses:{ConsoleColors.ENDC}")
            for i, (desc, amount) in enumerate(report_data.data['top_expenses'], 1):
                print(f"  {i}. {desc[:40]:40} {self._format_currency(amount)}")
            
            # Ask for visualization
            viz = input("\nGenerate chart? (y/n): ").strip().lower()
            if viz == 'y':
                self.visualizer.plot_monthly_summary(report_data.data)
        
        elif report_type == "yearly":
            year = int(args[1]) if len(args) > 1 else date.today().year
            
            transactions = self.transaction_repo.get_all_transactions(
                self.current_user.username
            )
            
            yearly_report = YearlyReport(transactions, year)
            report_data = yearly_report.generate()
            
            print_header(report_data.title)
            print(f"  {report_data.summary}\n")
            
            # Monthly breakdown
            print(f"{ConsoleColors.BOLD}Monthly Breakdown:{ConsoleColors.ENDC}")
            monthly_data = []
            for month, data in report_data.data['monthly_data'].items():
                monthly_data.append({
                    'Month': date(year, month, 1).strftime('%B'),
                    'Income': self._format_currency(data['income']),
                    'Expenses': self._format_currency(data['expenses']),
                    'Net': self._format_currency(data['net'])
                })
            
            print_table(monthly_data, ['Month', 'Income', 'Expenses', 'Net'])
        
        elif report_type == "category":
            # List categories
            print(f"\n{ConsoleColors.BOLD}Categories:{ConsoleColors.ENDC}")
            for i, cat in enumerate(Category, 1):
                print(f"{i}. {cat.display_name}")
            
            try:
                cat_choice = int(input("Choose category: "))
                categories = list(Category)
                if 1 <= cat_choice <= len(categories):
                    category = categories[cat_choice - 1]
                else:
                    print_error("Invalid category")
                    return
            except ValueError:
                print_error("Invalid input")
                return
            
            year = int(args[1]) if len(args) > 1 else date.today().year
            
            transactions = self.transaction_repo.get_all_transactions(
                self.current_user.username
            )
            
            category_report = CategoryReport(transactions, category, year)
            report_data = category_report.generate()
            
            print_header(report_data.title)
            print(f"  {report_data.summary}\n")
            
            print(f"{ConsoleColors.BOLD}Monthly Spending:{ConsoleColors.ENDC}")
            for month_key, amount in sorted(report_data.data['monthly_spending'].items()):
                print(f"  {month_key}: {self._format_currency(amount)}")
            
            print(f"\n{ConsoleColors.BOLD}Spending by Day of Week:{ConsoleColors.ENDC}")
            for day, amount in report_data.data['average_by_weekday'].items():
                print(f"  {day}: {self._format_currency(amount)} (avg)")
        
        else:
            print_error(f"Unknown report type: {report_type}")
            print_info("Available: monthly, yearly, category")
    
    def do_budget(self, arg: str):
        """
        Manage budgets.
        Usage: budget [set|list|check]
        """
        if not self._require_login():
            return
        
        args = arg.split()
        action = args[0] if args else "list"
        
        if action == "set":
            # List categories
            print(f"\n{ConsoleColors.BOLD}Categories:{ConsoleColors.ENDC}")
            expense_categories = Category.get_expense_categories()
            for i, cat in enumerate(expense_categories, 1):
                print(f"{i}. {cat.display_name}")
            
            try:
                cat_choice = int(input("Choose category: "))
                if 1 <= cat_choice <= len(expense_categories):
                    category = expense_categories[cat_choice - 1]
                else:
                    print_error("Invalid category")
                    return
            except ValueError:
                print_error("Invalid input")
                return
            
            # Month
            month_str = input("Month (YYYY-MM, press Enter for current): ").strip()
            if month_str:
                try:
                    budget_month = date.fromisoformat(f"{month_str}-01")
                except ValueError:
                    print_error("Invalid month format")
                    return
            else:
                today = date.today()
                budget_month = date(today.year, today.month, 1)
            
            # Amount
            try:
                limit = float(input("Budget limit: $"))
                if limit <= 0:
                    print_error("Budget limit must be positive")
                    return
            except ValueError:
                print_error("Invalid amount")
                return
            
            budget = Budget(category, budget_month, limit)
            
            if self.budget_repo.update_budget(self.current_user.username, budget):
                print_success(f"Budget set for {category.display_name} in {budget_month.strftime('%B %Y')}")
            else:
                print_error("Failed to set budget")
        
        elif action == "list":
            budgets = self.budget_repo.get_all_budgets(self.current_user.username)
            
            if not budgets:
                print_info("No budgets set")
                return
            
            print_header("Current Budgets")
            
            budget_data = []
            for budget in budgets:
                # Calculate current spending
                expenses = self.transaction_repo.get_transactions_by_month(
                    self.current_user.username,
                    budget.month.year,
                    budget.month.month
                )
                spent = sum(t.amount for t in expenses 
                           if t.category == budget.category 
                           and t.transaction_type == TransactionType.EXPENSE)
                
                budget_data.append({
                    'Category': budget.category.display_name,
                    'Month': budget.month.strftime('%B %Y'),
                    'Budget': self._format_currency(budget.limit_amount),
                    'Spent': self._format_currency(spent),
                    'Remaining': self._format_currency(budget.remaining_budget(spent)),
                    'Used': f"{budget.percent_used(spent):.1f}%"
                })
            
            print_table(budget_data, ['Category', 'Month', 'Budget', 'Spent', 'Remaining', 'Used'])
        
        elif action == "check":
            # Check budget status for current month
            year, month = self._get_current_month()
            budgets = self.budget_repo.get_all_budgets(self.current_user.username)
            
            print_header("Budget Status")
            
            alerts = []
            for budget in budgets:
                if budget.month.year == year and budget.month.month == month:
                    expenses = self.transaction_repo.get_transactions_by_month(
                        self.current_user.username, year, month
                    )
                    spent = sum(t.amount for t in expenses 
                               if t.category == budget.category 
                               and t.transaction_type == TransactionType.EXPENSE)
                    
                    if budget.is_exceeded(spent):
                        alerts.append((budget, spent))
                        print_warning(f"{budget.category.display_name}: ${spent:,.2f} / ${budget.limit_amount:,.2f} (EXCEEDED)")
                    else:
                        print_success(f"{budget.category.display_name}: ${spent:,.2f} / ${budget.limit_amount:,.2f}")
            
            if not alerts:
                print_success("All budgets on track!")
        
        else:
            print_error(f"Unknown budget action: {action}")
            print_info("Available: set, list, check")
    
    def do_delete(self, arg: str):
        """
        Delete a transaction.
        Usage: delete <transaction_id>
        """
        if not self._require_login():
            return
        
        if not arg:
            print_error("Please provide transaction ID")
            print_info("Usage: delete <transaction_id>")
            return
        
        transaction_id = arg.strip()
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete transaction {transaction_id}? (y/n): ")
        if confirm.lower() != 'y':
            print_info("Deletion cancelled")
            return
        
        if self.transaction_repo.delete_transaction(self.current_user.username, transaction_id):
            print_success(f"Transaction {transaction_id} deleted")
        else:
            print_error(f"Transaction {transaction_id} not found")
    
    def do_stats(self, arg: str):
        """
        Show account statistics.
        Usage: stats
        """
        if not self._require_login():
            return
        
        transactions = self.transaction_repo.get_all_transactions(
            self.current_user.username
        )
        
        if not transactions:
            print_info("No transactions yet")
            return
        
        print_header("Account Statistics")
        
        # Calculate statistics
        total_income = sum(t.amount for t in transactions if t.transaction_type == TransactionType.INCOME)
        total_expenses = sum(t.amount for t in transactions if t.transaction_type == TransactionType.EXPENSE)
        net_savings = total_income - total_expenses
        
        # Date range
        dates = [t.date for t in transactions]
        start_date = min(dates) if dates else date.today()
        end_date = max(dates) if dates else date.today()
        
        # Top categories
        expenses_by_category = defaultdict(float)
        for t in transactions:
            if t.transaction_type == TransactionType.EXPENSE:
                expenses_by_category[t.category.display_name] += t.amount
        
        top_categories = sorted(expenses_by_category.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Display
        print(f"{ConsoleColors.BOLD}Summary:{ConsoleColors.ENDC}")
        print(f"  Period: {start_date} to {end_date}")
        print(f"  Total Income:   {self._format_currency(total_income)}")
        print(f"  Total Expenses: {self._format_currency(total_expenses)}")
        print(f"  Net Savings:    {self._format_currency(net_savings)}")
        
        if total_income > 0:
            savings_rate = (net_savings / total_income) * 100
            print(f"  Savings Rate:   {savings_rate:.1f}%")
        
        print(f"\n{ConsoleColors.BOLD}Top Spending Categories:{ConsoleColors.ENDC}")
        for i, (category, amount) in enumerate(top_categories, 1):
            percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
            print(f"  {i}. {category:20} {self._format_currency(amount):>12} ({percentage:.1f}%)")
        
        print(f"\n{ConsoleColors.BOLD}Transaction Count:{ConsoleColors.ENDC}")
        print(f"  Total transactions: {len(transactions)}")
        print(f"  Average transaction: {self._format_currency(sum(t.amount for t in transactions) / len(transactions))}")
    
    def do_export(self, arg: str):
        """
        Export data to CSV.
        Usage: export
        """
        if not self._require_login():
            return
        
        transactions = self.transaction_repo.get_all_transactions(
            self.current_user.username
        )
        
        if not transactions:
            print_info("No transactions to export")
            return
        
        # Create export directory
        export_dir = Path("exports")
        export_dir.mkdir(exist_ok=True)
        
        # Export transactions
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = export_dir / f"{self.current_user.username}_transactions_{timestamp}.csv"
        
        df = pd.DataFrame([t.to_dict() for t in transactions])
        df.to_csv(filename, index=False)
        
        print_success(f"Transactions exported to: {filename}")
        
        # Export budgets
        budgets = self.budget_repo.get_all_budgets(self.current_user.username)
        if budgets:
            budget_filename = export_dir / f"{self.current_user.username}_budgets_{timestamp}.csv"
            budget_df = pd.DataFrame([{
                'category': b.category.key,
                'month': b.month.isoformat(),
                'limit_amount': b.limit_amount
            } for b in budgets])
            budget_df.to_csv(budget_filename, index=False)
            print_success(f"Budgets exported to: {budget_filename}")
    
    def do_help(self, arg: str):
        """Show help information."""
        if arg:
            super().do_help(arg)
        else:
            print_header("AVAILABLE COMMANDS")
            
            commands = [
                ('register <username>', 'Create new account'),
                ('login <username>', 'Login to existing account'),
                ('logout', 'Logout from current account'),
                ('add', 'Add new transaction'),
                ('list [month year]', 'List transactions'),
                ('report [monthly|yearly|category]', 'Generate reports'),
                ('budget [set|list|check]', 'Manage budgets'),
                ('delete <id>', 'Delete transaction'),
                ('stats', 'Show account statistics'),
                ('export', 'Export data to CSV'),
                ('help [command]', 'Show help'),
                ('quit', 'Exit application')
            ]
            
            print_table([{'Command': cmd, 'Description': desc} for cmd, desc in commands], 
                       ['Command', 'Description'])
            
            print(f"\n{ConsoleColors.CYAN}Tips:{ConsoleColors.ENDC}")
            print("  • Use 'help <command>' for detailed command help")
            print("  • Press Tab for command autocompletion")
            print("  • Use up/down arrows to navigate command history")
    
    def do_quit(self, arg: str):
        """Exit the application."""
        print_success("Thank you for using Expense Tracker!")
        print_info("Goodbye!")
        return True
    
    def default(self, line: str):
        """Handle unknown commands."""
        print_error(f"Unknown command: {line}")
        print_info("Type 'help' to see available commands")
    
    def emptyline(self):
        """Handle empty line input."""
        pass


def main():
    """Main entry point for the CLI application."""
    try:
        cli = ExpenseTrackerCLI()
        cli.cmdloop()
    except KeyboardInterrupt:
        print(f"\n{ConsoleColors.WARNING}\nInterrupted by user{ConsoleColors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

---

## 📊 Takeaway from This Story

**What You Built:**

- **Complete CLI Application** – Professional command-line interface with colored output
- **Domain Models** – Transaction, Category, Budget, User with proper validation
- **Persistence Layer** – JSON storage with backup, recovery, and statistics
- **Repository Pattern** – Abstracted data access for transactions and budgets
- **Reporting Engine** – Monthly, yearly, category, and budget reports
- **Visualization** – Matplotlib charts for spending patterns
- **Interactive CLI** – Full command set with autocompletion and history

**SOLID Principles Applied:**
- **Single Responsibility** – Each class has one purpose (Transaction, Storage, Report, CLI)
- **Open/Closed** – New categories, report types, and commands can be added
- **Liskov Substitution** – All transaction types work interchangeably
- **Interface Segregation** – Storage interface defines only needed methods
- **Dependency Inversion** – CLI depends on repository abstractions, not concrete storage

**Design Patterns Used:**
- **Value Object Pattern** – Immutable Transaction objects
- **Repository Pattern** – Abstracts data access logic
- **Singleton Pattern** – Single storage manager instance
- **Factory Pattern** – Creates reports and visualizations
- **Strategy Pattern** – Different reporting strategies
- **Template Method Pattern** – Report generation structure
- **Command Pattern** – CLI commands as methods
- **Facade Pattern** – Simplified CLI interface to complex subsystems

**Key Technologies:**
- **Dataclasses** – Clean domain model definitions
- **Enums** – Type-safe categories and transaction types
- **Pathlib** – Modern file path handling
- **JSON** – Human-readable data storage
- **Pandas** – Data analysis and export
- **Matplotlib** – Data visualization
- **Tabulate** – Beautiful table formatting
- **Colorama** – Cross-platform colored output
- **Cmd** – Built-in CLI framework

---

## 🔗 Navigation

- **⬅️ Previous Series:** Series I: AI & Machine Learning with Python – Complete

- **📚 Series J Catalog:** Capstone Projects – View all 3 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Weather Dashboard (Series J, Story 2)

---

## 🎯 Your Challenge

Now that you've built the Expense Tracker, here's how to extend it:

1. **Add data import** – Import transactions from CSV/Excel files
2. **Add recurring transactions** – Automatically add monthly bills
3. **Add receipt scanning** – OCR for paper receipts
4. **Add budgeting alerts** – Email/SMS notifications
5. **Add multi-currency** – Support for different currencies
6. **Add investment tracking** – Track portfolio performance
7. **Add debt tracker** – Track loans and credit cards
8. **Add API** – Create REST API for mobile apps
9. **Add database** – Migrate from JSON to SQLite/PostgreSQL
10. **Add sync** – Cloud sync between devices

**You've built a complete CLI application. Next stop: Weather Dashboard!**

---

*Found this helpful? Clap, comment, and share your expense tracker. Next stop: Weather Dashboard!* 🚇

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 5 | 0 | 100% |
| Series F | 6 | 6 | 0 | 100% |
| Series G | 5 | 5 | 0 | 100% |
| Series H | 5 | 5 | 0 | 100% |
| Series I | 4 | 4 | 0 | 100% |
| Series J | 3 | 1 | 2 | 33% |

**Next Stories to Generate:**
1. Series J, Story 2: Weather Dashboard (Flask web app, API integration, Redis caching)
2. Series J, Story 3: ML-Powered Recommendation Engine (Full-stack with collaborative filtering)