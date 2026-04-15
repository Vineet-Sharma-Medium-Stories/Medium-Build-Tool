# The 2026 Python Metromap: Sets – Unique & Fast

## Series C: Data Structures Express | Story 4 of 5

![The 2026 Python Metromap/images/Sets – Unique and Fast](images/Sets – Unique and Fast.png)

## 📖 Introduction

**Welcome to the fourth stop on the Data Structures Express Line.**

You've mastered lists for ordered sequences, tuples for immutable data, and dictionaries for key-value lookups. But what about when you need to track unique items? When you need to find common elements between collections? When you need to remove duplicates efficiently?

That's where sets come in.

Sets are unordered collections of unique, hashable elements. They provide O(1) average-case membership testing—lightning fast for checking if an item exists. Sets shine at mathematical operations: union, intersection, difference, and symmetric difference. They're perfect for tracking unique visitors, finding common friends, removing duplicates, and analyzing relationships between collections.

This story—**The 2026 Python Metromap: Sets – Unique & Fast**—is your guide to mastering Python sets. We'll build a complete unique visitor tracking system for website analytics. We'll create a friend recommendation engine using set operations. We'll implement a duplicate file finder that identifies identical files across directories. We'll build a tag-based content recommendation system. And we'll create a complete set-based analytics platform for e-commerce.

**Let's get unique.**

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

- 🔑 **The 2026 Python Metromap: Dictionaries – Key-Value Power** – User profile system; product catalog; caching system; dependency injection.

- 🎯 **The 2026 Python Metromap: Sets – Unique & Fast** – Unique visitor tracking; friend recommendation; duplicate file finder; content recommendation. **⬅️ YOU ARE HERE**

- 📝 **The 2026 Python Metromap: Comprehensions – One-Line Power** – Data transformation pipelines; filtered iterations; nested structure creation. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🎯 Section 1: Set Fundamentals – Creation, Operations, and Methods

Sets are unordered collections of unique, hashable elements with O(1) membership testing.

**SOLID Principle Applied: Interface Segregation** – Sets provide mathematical set operations distinct from sequences.

**Design Pattern: Collection Pattern** – Mathematical set operations (union, intersection, difference).

```python
"""
SET FUNDAMENTALS: CREATION, OPERATIONS, AND METHODS

This section covers the basics of creating and using sets.

SOLID Principle: Interface Segregation
- Sets provide mathematical set operations

Design Pattern: Collection Pattern
- Mathematical set operations (union, intersection, difference)
"""

from typing import Set, List, Any
import time


def demonstrate_set_creation():
    """
    Demonstrates different ways to create sets.
    
    Sets are created with curly braces {} or set() constructor.
    They store only unique elements (no duplicates).
    """
    print("=" * 60)
    print("SECTION 1A: CREATING SETS")
    print("=" * 60)
    
    # EMPTY SET (NOTE: {} is empty dict!)
    print("\n1. CREATING EMPTY SETS")
    print("-" * 40)
    
    empty_set = set()
    not_a_set = {}  # This is a dictionary!
    
    print(f"  empty_set: {empty_set} (type: {type(empty_set).__name__})")
    print(f"  {{}}: {not_a_set} (type: {type(not_a_set).__name__})")
    print("  ⚠️ Use set() for empty sets, not {}")
    
    # SET WITH VALUES
    print("\n2. SETS WITH VALUES")
    print("-" * 40)
    
    fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate removed
    numbers = {1, 2, 3, 4, 5}
    mixed = {1, "hello", 3.14, True}
    
    print(f"  fruits: {fruits} (duplicate 'apple' removed)")
    print(f"  numbers: {numbers}")
    print(f"  mixed: {mixed}")
    
    # FROM OTHER ITERABLES
    print("\n3. CREATING SETS FROM OTHER ITERABLES")
    print("-" * 40)
    
    # From list (removes duplicates)
    list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    from_list = set(list_with_duplicates)
    print(f"  set({list_with_duplicates}): {from_list}")
    
    # From string (unique characters)
    from_string = set("abracadabra")
    print(f"  set('abracadabra'): {from_string}")
    
    # From tuple
    from_tuple = set((1, 2, 3, 2, 1))
    print(f"  set((1,2,3,2,1)): {from_tuple}")
    
    # SET COMPREHENSION
    print("\n4. SET COMPREHENSION")
    print("-" * 40)
    
    squares = {x**2 for x in range(10)}
    evens = {x for x in range(20) if x % 2 == 0}
    
    print(f"  squares: {squares}")
    print(f"  evens: {evens}")


def demonstrate_set_operations():
    """
    Demonstrates mathematical set operations.
    
    Sets support union, intersection, difference, and symmetric difference.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: SET OPERATIONS")
    print("=" * 60)
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"  Set A: {set_a}")
    print(f"  Set B: {set_b}")
    
    # UNION (|) - elements in either set
    print("\n1. UNION (| or union())")
    print("-" * 40)
    
    union_operator = set_a | set_b
    union_method = set_a.union(set_b)
    print(f"  A | B: {union_operator}")
    print(f"  A.union(B): {union_method}")
    
    # INTERSECTION (&) - elements in both sets
    print("\n2. INTERSECTION (& or intersection())")
    print("-" * 40)
    
    intersection_operator = set_a & set_b
    intersection_method = set_a.intersection(set_b)
    print(f"  A & B: {intersection_operator}")
    print(f"  A.intersection(B): {intersection_method}")
    
    # DIFFERENCE (-) - elements in A but not in B
    print("\n3. DIFFERENCE (- or difference())")
    print("-" * 40)
    
    difference_operator = set_a - set_b
    difference_method = set_a.difference(set_b)
    print(f"  A - B: {difference_operator}")
    print(f"  B - A: {set_b - set_a}")
    
    # SYMMETRIC DIFFERENCE (^) - elements in either, but not both
    print("\n4. SYMMETRIC DIFFERENCE (^ or symmetric_difference())")
    print("-" * 40)
    
    sym_diff_operator = set_a ^ set_b
    sym_diff_method = set_a.symmetric_difference(set_b)
    print(f"  A ^ B: {sym_diff_operator}")
    print(f"  A.symmetric_difference(B): {sym_diff_method}")
    
    # SUBSET AND SUPERSET
    print("\n5. SUBSET AND SUPERSET")
    print("-" * 40)
    
    set_c = {1, 2, 3}
    set_d = {1, 2, 3, 4, 5}
    
    print(f"  Set C: {set_c}")
    print(f"  Set D: {set_d}")
    print(f"  C.issubset(D): {set_c.issubset(set_d)}")
    print(f"  D.issuperset(C): {set_d.issuperset(set_c)}")
    print(f"  C < D (proper subset): {set_c < set_d}")
    
    # DISJOINT (no common elements)
    print("\n6. DISJOINT")
    print("-" * 40)
    
    set_e = {1, 2, 3}
    set_f = {4, 5, 6}
    set_g = {3, 4, 5}
    
    print(f"  Set E: {set_e}, Set F: {set_f}")
    print(f"  E.isdisjoint(F): {set_e.isdisjoint(set_f)}")
    print(f"  E.isdisjoint(G): {set_e.isdisjoint(set_g)}")


def demonstrate_set_methods():
    """
    Demonstrates set methods for adding, removing, and modifying.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: SET METHODS")
    print("=" * 60)
    
    colors = {"red", "green", "blue"}
    print(f"  Original: {colors}")
    
    # ADDING ELEMENTS
    print("\n1. ADDING ELEMENTS")
    print("-" * 40)
    
    colors.add("yellow")
    print(f"  add('yellow'): {colors}")
    
    colors.add("red")  # Adding duplicate does nothing
    print(f"  add('red') again: {colors} (unchanged)")
    
    # UPDATE (add multiple elements)
    colors.update(["purple", "orange", "pink"])
    print(f"  update(['purple', 'orange', 'pink']): {colors}")
    
    # REMOVING ELEMENTS
    print("\n2. REMOVING ELEMENTS")
    print("-" * 40)
    
    # remove() - raises KeyError if not found
    colors.remove("pink")
    print(f"  remove('pink'): {colors}")
    
    try:
        colors.remove("brown")
    except KeyError as e:
        print(f"  remove('brown'): KeyError - {e}")
    
    # discard() - no error if not found
    colors.discard("brown")
    print(f"  discard('brown'): {colors} (no error)")
    
    # pop() - removes and returns arbitrary element
    removed = colors.pop()
    print(f"  pop(): removed '{removed}', remaining: {colors}")
    
    # clear() - removes all elements
    temp_set = {1, 2, 3}
    temp_set.clear()
    print(f"  clear(): {temp_set}")
    
    # COPYING SETS
    print("\n3. COPYING SETS")
    print("-" * 40)
    
    original = {1, 2, 3}
    shallow_copy = original.copy()
    shallow_copy.add(4)
    
    print(f"  Original: {original} (unchanged)")
    print(f"  Copy: {shallow_copy}")


def demonstrate_set_membership_performance():
    """
    Demonstrates the O(1) membership testing performance of sets.
    
    Sets are much faster than lists for checking if an item exists.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: SET MEMBERSHIP PERFORMANCE (O(1))")
    print("=" * 60)
    
    # Create test data
    size = 100000
    list_data = list(range(size))
    set_data = set(range(size))
    
    # Test membership in list (O(n))
    print("\n1. LIST MEMBERSHIP (O(n) - slow)")
    print("-" * 40)
    
    start = time.time()
    result = 99999 in list_data
    list_time = time.time() - start
    print(f"  Checking 99999 in list: {list_time:.6f}s")
    
    start = time.time()
    result = -1 in list_data
    list_time_missing = time.time() - start
    print(f"  Checking -1 in list: {list_time_missing:.6f}s")
    
    # Test membership in set (O(1) - fast)
    print("\n2. SET MEMBERSHIP (O(1) - fast)")
    print("-" * 40)
    
    start = time.time()
    result = 99999 in set_data
    set_time = time.time() - start
    print(f"  Checking 99999 in set: {set_time:.6f}s")
    
    start = time.time()
    result = -1 in set_data
    set_time_missing = time.time() - start
    print(f"  Checking -1 in set: {set_time_missing:.6f}s")
    
    print(f"\n  Performance difference:")
    print(f"    List: {list_time:.6f}s, Set: {set_time:.6f}s")
    print(f"    Set is {list_time / set_time:.0f}x faster!")
    
    print("\n  💡 Use sets when you need:")
    print("     • Fast membership testing ('in' operator)")
    print("     • Unique elements (no duplicates)")
    print("     • Mathematical set operations (union, intersection)")
    print("     • Removing duplicates from sequences")


def demonstrate_frozenset():
    """
    Demonstrates frozenset - immutable version of set.
    
    Frozensets are hashable and can be used as dictionary keys.
    """
    print("\n" + "=" * 60)
    print("SECTION 1E: FROZENSET – IMMUTABLE SETS")
    print("=" * 60)
    
    # CREATING FROZENSET
    print("\n1. CREATING FROZENSETS")
    print("-" * 40)
    
    regular_set = {1, 2, 3}
    frozen = frozenset([1, 2, 3, 3, 2, 1])
    
    print(f"  regular_set: {regular_set} (mutable)")
    print(f"  frozenset: {frozen} (immutable)")
    
    # IMMUTABILITY
    print("\n2. IMMUTABILITY")
    print("-" * 40)
    
    try:
        frozen.add(4)
    except AttributeError as e:
        print(f"  Cannot modify: {e}")
    
    # CAN BE USED AS DICTIONARY KEYS (unlike regular sets)
    print("\n3. FROZENSETS AS DICTIONARY KEYS")
    print("-" * 40)
    
    # Regular sets cannot be dictionary keys
    try:
        bad_dict = {{1, 2}: "value"}
    except TypeError as e:
        print(f"  Regular set as key: {e}")
    
    # Frozensets can be dictionary keys
    good_dict = {frozenset([1, 2]): "value"}
    print(f"  Frozenset as key: {good_dict}")
    
    # Practical: Group by set of tags
    articles = [
        ("Article 1", frozenset(["python", "programming"])),
        ("Article 2", frozenset(["python", "data"])),
        ("Article 3", frozenset(["programming", "algorithms"]))
    ]
    
    tag_groups = {}
    for title, tags in articles:
        if tags not in tag_groups:
            tag_groups[tags] = []
        tag_groups[tags].append(title)
    
    print(f"  Grouped by tags: {tag_groups}")


if __name__ == "__main__":
    demonstrate_set_creation()
    demonstrate_set_operations()
    demonstrate_set_methods()
    demonstrate_set_membership_performance()
    demonstrate_frozenset()
```

---

## 📊 Section 2: Website Analytics – Unique Visitor Tracking

A complete website analytics system using sets for tracking unique visitors, page overlaps, and conversion funnels.

**SOLID Principles Applied:**
- Single Responsibility: Each analytics function has one purpose
- Open/Closed: New metrics can be added

**Design Patterns:**
- Singleton Pattern: Single analytics instance
- Observer Pattern: Track user actions

```python
"""
WEBSITE ANALYTICS: UNIQUE VISITOR TRACKING

This section builds a website analytics system using sets.

SOLID Principles Applied:
- Single Responsibility: Each function has one purpose
- Open/Closed: New metrics can be added

Design Patterns:
- Singleton Pattern: Single analytics instance
- Observer Pattern: Track user actions
"""

from typing import Set, Dict, List, Optional, Any, Tuple
from collections import defaultdict
from datetime import datetime, date, timedelta
from dataclasses import dataclass, field
import json


@dataclass
class VisitorSession:
    """Represents a visitor session."""
    user_id: str
    session_id: str
    pages: List[str] = field(default_factory=list)
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    referrer: Optional[str] = None
    user_agent: Optional[str] = None


class WebsiteAnalytics:
    """
    Website analytics using sets for unique tracking.
    
    Design Pattern: Singleton Pattern - Single analytics instance
    """
    
    def __init__(self):
        # Daily unique visitors: date -> set of user_ids
        self.daily_visitors: Dict[str, Set[str]] = defaultdict(set)
        
        # Hourly unique visitors: hour -> set of user_ids
        self.hourly_visitors: Dict[str, Set[str]] = defaultdict(set)
        
        # Page views: page -> set of user_ids
        self.page_views: Dict[str, Set[str]] = defaultdict(set)
        
        # Referral sources: source -> set of user_ids
        self.referrals: Dict[str, Set[str]] = defaultdict(set)
        
        # User sessions: user_id -> list of sessions
        self.sessions: Dict[str, List[VisitorSession]] = defaultdict(list)
        
        # Conversion events: event_type -> set of user_ids
        self.conversions: Dict[str, Set[str]] = defaultdict(set)
        
        # Current active sessions
        self.active_sessions: Dict[str, VisitorSession] = {}
    
    def _get_date_key(self, dt: datetime = None) -> str:
        """Get date string key."""
        if dt is None:
            dt = datetime.now()
        return dt.strftime("%Y-%m-%d")
    
    def _get_hour_key(self, dt: datetime = None) -> str:
        """Get hour string key."""
        if dt is None:
            dt = datetime.now()
        return dt.strftime("%Y-%m-%d %H:00")
    
    def track_page_view(self, user_id: str, page: str, 
                        referrer: Optional[str] = None,
                        user_agent: Optional[str] = None) -> None:
        """
        Track a page view for a user.
        
        Args:
            user_id: Unique user identifier
            page: Page URL or name
            referrer: Referral source
            user_agent: Browser/device information
        """
        now = datetime.now()
        
        # Track daily unique visitors
        date_key = self._get_date_key(now)
        self.daily_visitors[date_key].add(user_id)
        
        # Track hourly unique visitors
        hour_key = self._get_hour_key(now)
        self.hourly_visitors[hour_key].add(user_id)
        
        # Track page views
        self.page_views[page].add(user_id)
        
        # Track referral
        if referrer:
            self.referrals[referrer].add(user_id)
        
        # Track session
        session_id = f"{user_id}_{now.strftime('%Y%m%d')}"
        
        if session_id not in self.active_sessions:
            session = VisitorSession(
                user_id=user_id,
                session_id=session_id,
                referrer=referrer,
                user_agent=user_agent
            )
            self.active_sessions[session_id] = session
            self.sessions[user_id].append(session)
        
        self.active_sessions[session_id].pages.append(page)
    
    def track_conversion(self, user_id: str, event_type: str) -> None:
        """
        Track a conversion event.
        
        Args:
            user_id: User who converted
            event_type: Type of conversion (purchase, signup, etc.)
        """
        self.conversions[event_type].add(user_id)
    
    def end_session(self, session_id: str) -> None:
        """End a user session."""
        if session_id in self.active_sessions:
            self.active_sessions[session_id].end_time = datetime.now()
            del self.active_sessions[session_id]
    
    def get_daily_unique_visitors(self, days: int = 7) -> Dict[str, int]:
        """Get unique visitors for the last N days."""
        result = {}
        today = date.today()
        
        for i in range(days):
            d = today - timedelta(days=i)
            date_key = d.isoformat()
            result[date_key] = len(self.daily_visitors.get(date_key, set()))
        
        return result
    
    def get_hourly_traffic(self, date_str: str = None) -> Dict[str, int]:
        """Get hourly unique visitors for a specific date."""
        if date_str is None:
            date_str = date.today().isoformat()
        
        result = {}
        for hour in range(24):
            hour_key = f"{date_str} {hour:02d}:00"
            result[f"{hour:02d}:00"] = len(self.hourly_visitors.get(hour_key, set()))
        
        return result
    
    def get_page_overlap(self, page1: str, page2: str) -> Set[str]:
        """Find users who visited both pages."""
        visitors1 = self.page_views.get(page1, set())
        visitors2 = self.page_views.get(page2, set())
        return visitors1 & visitors2
    
    def get_unique_page_visitors(self, page: str) -> int:
        """Get number of unique visitors to a page."""
        return len(self.page_views.get(page, set()))
    
    def get_top_pages(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Get most visited pages by unique visitor count."""
        page_counts = [(page, len(visitors)) for page, visitors in self.page_views.items()]
        page_counts.sort(key=lambda x: x[1], reverse=True)
        return page_counts[:limit]
    
    def get_referral_summary(self) -> Dict[str, int]:
        """Get summary of referral sources."""
        return {source: len(users) for source, users in self.referrals.items()}
    
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
                    "conversion_rate": round(rate, 1)
                })
            
            previous_visitors = visitors
        
        return funnel_data
    
    def get_conversion_rate(self, conversion_event: str) -> float:
        """Calculate conversion rate for an event."""
        all_visitors = set()
        for visitors in self.daily_visitors.values():
            all_visitors.update(visitors)
        
        converters = self.conversions.get(conversion_event, set())
        
        if not all_visitors:
            return 0.0
        
        return (len(converters) / len(all_visitors)) * 100
    
    def get_user_journey(self, user_id: str) -> List[str]:
        """Get the sequence of pages visited by a user."""
        pages = []
        for session in self.sessions.get(user_id, []):
            pages.extend(session.pages)
        return pages
    
    def find_similar_users(self, user_id: str, limit: int = 5) -> List[Tuple[str, float]]:
        """
        Find users with similar page viewing patterns.
        
        Returns:
            List of (user_id, similarity_score) tuples
        """
        user_pages = set(self.get_user_journey(user_id))
        
        similarities = []
        for other_user in self.get_all_users():
            if other_user == user_id:
                continue
            
            other_pages = set(self.get_user_journey(other_user))
            
            if not user_pages or not other_pages:
                similarity = 0.0
            else:
                intersection = len(user_pages & other_pages)
                union = len(user_pages | other_pages)
                similarity = (intersection / union) * 100
            
            similarities.append((other_user, round(similarity, 1)))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:limit]
    
    def get_all_users(self) -> Set[str]:
        """Get all unique users."""
        all_users = set()
        for visitors in self.daily_visitors.values():
            all_users.update(visitors)
        return all_users
    
    def get_retention_cohort(self, cohort_date: str, days: int = 30) -> Dict[int, float]:
        """
        Calculate retention rates for a cohort.
        
        Args:
            cohort_date: Date of first visit (YYYY-MM-DD)
            days: Number of days to track
            
        Returns:
            Dictionary of day -> retention rate
        """
        cohort = self.daily_visitors.get(cohort_date, set())
        retention = {}
        
        cohort_start = datetime.strptime(cohort_date, "%Y-%m-%d").date()
        
        for day in range(1, days + 1):
            target_date = cohort_start + timedelta(days=day)
            target_key = target_date.isoformat()
            returning = self.daily_visitors.get(target_key, set())
            
            retained = len(cohort & returning)
            retention[day] = (retained / len(cohort)) * 100 if cohort else 0
        
        return retention
    
    def generate_report(self) -> str:
        """Generate comprehensive analytics report."""
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("WEBSITE ANALYTICS REPORT")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        # Daily visitors
        daily = self.get_daily_unique_visitors(7)
        report_lines.append("\n📊 DAILY UNIQUE VISITORS (Last 7 days):")
        for date_str, count in daily.items():
            report_lines.append(f"  {date_str}: {count}")
        
        # Top pages
        report_lines.append("\n📈 TOP PAGES:")
        for page, count in self.get_top_pages(5):
            report_lines.append(f"  {page}: {count} unique visitors")
        
        # Referrals
        report_lines.append("\n🔗 TOP REFERRAL SOURCES:")
        referrals = self.get_referral_summary()
        sorted_refs = sorted(referrals.items(), key=lambda x: x[1], reverse=True)
        for source, count in sorted_refs[:5]:
            report_lines.append(f"  {source}: {count} users")
        
        # Conversions
        report_lines.append("\n💰 CONVERSION RATES:")
        for event in self.conversions:
            rate = self.get_conversion_rate(event)
            report_lines.append(f"  {event}: {rate:.1f}%")
        
        report_lines.append("\n" + "=" * 60)
        
        return "\n".join(report_lines)


def demonstrate_analytics_system():
    """
    Demonstrate the website analytics system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: WEBSITE ANALYTICS SYSTEM")
    print("=" * 60)
    
    analytics = WebsiteAnalytics()
    
    print("\n1. TRACKING PAGE VIEWS")
    print("-" * 40)
    
    # Simulate user traffic
    analytics.track_page_view("user_001", "home", referrer="google")
    analytics.track_page_view("user_002", "home", referrer="direct")
    analytics.track_page_view("user_001", "products")
    analytics.track_page_view("user_003", "home", referrer="facebook")
    analytics.track_page_view("user_001", "pricing")
    analytics.track_page_view("user_002", "products")
    analytics.track_page_view("user_002", "pricing")
    analytics.track_page_view("user_004", "home", referrer="google")
    analytics.track_page_view("user_001", "checkout")
    analytics.track_page_view("user_003", "products")
    analytics.track_page_view("user_003", "checkout")
    
    print("  Tracked 11 page views from 4 users")
    
    print("\n2. TRACKING CONVERSIONS")
    print("-" * 40)
    
    analytics.track_conversion("user_001", "purchase")
    analytics.track_conversion("user_003", "purchase")
    analytics.track_conversion("user_004", "signup")
    
    print("  Tracked 3 conversions")
    
    print("\n3. UNIQUE VISITOR STATISTICS")
    print("-" * 40)
    
    daily = analytics.get_daily_unique_visitors(1)
    for date_str, count in daily.items():
        print(f"  {date_str}: {count} unique visitors")
    
    print("\n4. PAGE OVERLAP ANALYSIS (Set Intersection)")
    print("-" * 40)
    
    home_products_overlap = analytics.get_page_overlap("home", "products")
    print(f"  Users who visited both Home and Products: {len(home_products_overlap)}")
    print(f"  Users: {home_products_overlap}")
    
    products_pricing_overlap = analytics.get_page_overlap("products", "pricing")
    print(f"  Users who visited both Products and Pricing: {len(products_pricing_overlap)}")
    
    print("\n5. CONVERSION FUNNEL (Set Operations)")
    print("-" * 40)
    
    funnel = analytics.get_conversion_funnel(["home", "products", "pricing", "checkout", "purchase"])
    
    for step in funnel:
        print(f"  Step {step['step']} ({step['page']}): {step['visitors']} users ({step['conversion_rate']:.1f}%)")
    
    print("\n6. CONVERSION RATES")
    print("-" * 40)
    
    purchase_rate = analytics.get_conversion_rate("purchase")
    signup_rate = analytics.get_conversion_rate("signup")
    
    print(f"  Purchase conversion rate: {purchase_rate:.1f}%")
    print(f"  Signup conversion rate: {signup_rate:.1f}%")
    
    print("\n7. USER JOURNEY ANALYSIS")
    print("-" * 40)
    
    journey = analytics.get_user_journey("user_001")
    print(f"  User 001 journey: {' → '.join(journey)}")
    
    print("\n8. SIMILAR USERS (Set Similarity)")
    print("-" * 40)
    
    similar = analytics.find_similar_users("user_001")
    print("  Users similar to user_001:")
    for user, score in similar:
        print(f"    {user}: {score}% similarity")
    
    print("\n9. COMPREHENSIVE REPORT")
    print("-" * 40)
    
    report = analytics.generate_report()
    print(report)


if __name__ == "__main__":
    demonstrate_analytics_system()
```

---

## 👥 Section 3: Friend Recommendation Engine

A complete friend recommendation system using set operations to find common interests and mutual friends.

**SOLID Principles Applied:**
- Single Responsibility: Each recommendation strategy has one purpose
- Open/Closed: New recommendation strategies can be added

**Design Patterns:**
- Strategy Pattern: Different recommendation algorithms
- Composite Pattern: Combine multiple strategies

```python
"""
FRIEND RECOMMENDATION ENGINE

This section builds a friend recommendation engine using set operations.

SOLID Principles Applied:
- Single Responsibility: Each strategy has one purpose
- Open/Closed: New strategies can be added

Design Patterns:
- Strategy Pattern: Different recommendation algorithms
- Composite Pattern: Combine multiple strategies
"""

from typing import Set, Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum


class InterestCategory(Enum):
    """Interest categories."""
    TECHNOLOGY = "technology"
    SPORTS = "sports"
    MUSIC = "music"
    MOVIES = "movies"
    BOOKS = "books"
    GAMING = "gaming"
    TRAVEL = "travel"
    FOOD = "food"
    ART = "art"
    SCIENCE = "science"


@dataclass
class User:
    """Represents a user in the social network."""
    user_id: str
    name: str
    age: int
    city: str
    interests: Set[InterestCategory] = field(default_factory=set)
    friends: Set[str] = field(default_factory=set)
    
    def add_interest(self, interest: InterestCategory) -> None:
        """Add an interest to the user."""
        self.interests.add(interest)
    
    def add_friend(self, friend_id: str) -> None:
        """Add a friend."""
        self.friends.add(friend_id)
    
    def remove_friend(self, friend_id: str) -> None:
        """Remove a friend."""
        self.friends.discard(friend_id)
    
    def get_common_interests(self, other: 'User') -> Set[InterestCategory]:
        """Get common interests with another user."""
        return self.interests & other.interests
    
    def get_interest_similarity(self, other: 'User') -> float:
        """Calculate interest similarity score (Jaccard index)."""
        if not self.interests and not other.interests:
            return 0.0
        
        intersection = len(self.interests & other.interests)
        union = len(self.interests | other.interests)
        return intersection / union if union > 0 else 0.0


class SocialGraph:
    """
    Social graph with friend relationships.
    
    Design Pattern: Graph Pattern - Users as nodes, friendships as edges
    """
    
    def __init__(self):
        self.users: Dict[str, User] = {}
    
    def add_user(self, user: User) -> None:
        """Add a user to the graph."""
        self.users[user.user_id] = user
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        return self.users.get(user_id)
    
    def add_friendship(self, user_id1: str, user_id2: str) -> bool:
        """Add a friendship between two users."""
        user1 = self.get_user(user_id1)
        user2 = self.get_user(user_id2)
        
        if not user1 or not user2:
            return False
        
        user1.add_friend(user2.user_id)
        user2.add_friend(user1.user_id)
        return True
    
    def get_friends(self, user_id: str) -> Set[str]:
        """Get all friends of a user."""
        user = self.get_user(user_id)
        return user.friends if user else set()
    
    def get_friends_of_friends(self, user_id: str) -> Dict[str, int]:
        """
        Get friends of friends (excluding direct friends and self).
        
        Returns:
            Dictionary mapping user_id to number of mutual friends
        """
        user = self.get_user(user_id)
        if not user:
            return {}
        
        friends = user.friends
        candidates = defaultdict(int)
        
        for friend_id in friends:
            friend = self.get_user(friend_id)
            if friend:
                for fof_id in friend.friends:
                    if fof_id != user_id and fof_id not in friends:
                        candidates[fof_id] += 1
        
        return dict(candidates)
    
    def get_mutual_friends(self, user_id1: str, user_id2: str) -> Set[str]:
        """Get mutual friends between two users."""
        user1 = self.get_user(user_id1)
        user2 = self.get_user(user_id2)
        
        if not user1 or not user2:
            return set()
        
        return user1.friends & user2.friends


class RecommendationStrategy:
    """Base class for recommendation strategies."""
    
    def recommend(self, social_graph: SocialGraph, user_id: str, limit: int = 10) -> List[Tuple[str, float]]:
        """Recommend users with scores."""
        raise NotImplementedError


class FriendsOfFriendsStrategy(RecommendationStrategy):
    """Recommend friends of friends."""
    
    def recommend(self, social_graph: SocialGraph, user_id: str, limit: int = 10) -> List[Tuple[str, float]]:
        fof = social_graph.get_friends_of_friends(user_id)
        # Score is number of mutual friends
        results = [(uid, score) for uid, score in fof.items()]
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:limit]


class InterestSimilarityStrategy(RecommendationStrategy):
    """Recommend users with similar interests."""
    
    def recommend(self, social_graph: SocialGraph, user_id: str, limit: int = 10) -> List[Tuple[str, float]]:
        user = social_graph.get_user(user_id)
        if not user:
            return []
        
        scores = []
        friends = user.friends
        
        for other_id, other in social_graph.users.items():
            if other_id == user_id or other_id in friends:
                continue
            
            similarity = user.get_interest_similarity(other)
            if similarity > 0:
                scores.append((other_id, round(similarity * 100, 1)))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:limit]


class HybridRecommendationStrategy(RecommendationStrategy):
    """
    Combine multiple strategies with weights.
    
    Design Pattern: Composite Pattern - Combines multiple strategies
    """
    
    def __init__(self, strategies: List[Tuple[RecommendationStrategy, float]]):
        """
        Initialize with strategies and their weights.
        
        Args:
            strategies: List of (strategy, weight) tuples
        """
        self.strategies = strategies
    
    def recommend(self, social_graph: SocialGraph, user_id: str, limit: int = 10) -> List[Tuple[str, float]]:
        scores = defaultdict(float)
        
        for strategy, weight in self.strategies:
            results = strategy.recommend(social_graph, user_id, limit * 2)
            for uid, score in results:
                scores[uid] += score * weight
        
        # Normalize to 0-100
        if scores:
            max_score = max(scores.values())
            if max_score > 0:
                scores = {uid: (s / max_score) * 100 for uid, s in scores.items()}
        
        results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return results[:limit]


class RecommendationEngine:
    """
    Friend recommendation engine.
    
    Design Pattern: Strategy Pattern - Pluggable recommendation strategies
    """
    
    def __init__(self, social_graph: SocialGraph):
        self.social_graph = social_graph
        self.strategy: RecommendationStrategy = FriendsOfFriendsStrategy()
    
    def set_strategy(self, strategy: RecommendationStrategy) -> None:
        """Set the recommendation strategy."""
        self.strategy = strategy
    
    def recommend_friends(self, user_id: str, limit: int = 10) -> List[Tuple[User, float]]:
        """Get friend recommendations for a user."""
        results = self.strategy.recommend(self.social_graph, user_id, limit)
        
        recommendations = []
        for uid, score in results:
            user = self.social_graph.get_user(uid)
            if user:
                recommendations.append((user, score))
        
        return recommendations


def demonstrate_recommendation_engine():
    """
    Demonstrate the friend recommendation engine.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: FRIEND RECOMMENDATION ENGINE")
    print("=" * 60)
    
    # Create social graph
    graph = SocialGraph()
    
    print("\n1. CREATING USERS WITH INTERESTS")
    print("-" * 40)
    
    # Create users
    alice = User("alice", "Alice", 28, "NYC")
    alice.interests = {InterestCategory.TECHNOLOGY, InterestCategory.BOOKS, InterestCategory.TRAVEL}
    
    bob = User("bob", "Bob", 30, "NYC")
    bob.interests = {InterestCategory.TECHNOLOGY, InterestCategory.GAMING, InterestCategory.MOVIES}
    
    charlie = User("charlie", "Charlie", 25, "Boston")
    charlie.interests = {InterestCategory.TECHNOLOGY, InterestCategory.BOOKS, InterestCategory.MUSIC}
    
    diana = User("diana", "Diana", 32, "NYC")
    diana.interests = {InterestCategory.TRAVEL, InterestCategory.FOOD, InterestCategory.ART}
    
    eve = User("eve", "Eve", 27, "NYC")
    eve.interests = {InterestCategory.TECHNOLOGY, InterestCategory.GAMING, InterestCategory.SCIENCE}
    
    frank = User("frank", "Frank", 29, "Boston")
    frank.interests = {InterestCategory.SPORTS, InterestCategory.GAMING, InterestCategory.MOVIES}
    
    for user in [alice, bob, charlie, diana, eve, frank]:
        graph.add_user(user)
        print(f"  Added: {user.name} ({', '.join(i.value for i in user.interests)})")
    
    # Add friendships
    print("\n2. ADDING FRIENDSHIPS")
    print("-" * 40)
    
    graph.add_friendship("alice", "bob")
    graph.add_friendship("alice", "charlie")
    graph.add_friendship("bob", "eve")
    graph.add_friendship("bob", "frank")
    graph.add_friendship("charlie", "diana")
    graph.add_friendship("diana", "eve")
    
    print("  Friendships created:")
    print("    Alice ↔ Bob, Alice ↔ Charlie")
    print("    Bob ↔ Eve, Bob ↔ Frank")
    print("    Charlie ↔ Diana, Diana ↔ Eve")
    
    print("\n3. MUTUAL FRIENDS (Set Intersection)")
    print("-" * 40)
    
    mutual = graph.get_mutual_friends("alice", "eve")
    print(f"  Mutual friends between Alice and Eve: {mutual}")
    
    print("\n4. FRIENDS OF FRIENDS")
    print("-" * 40)
    
    fof = graph.get_friends_of_friends("alice")
    print(f"  Friends of friends for Alice:")
    for uid, count in fof.items():
        user = graph.get_user(uid)
        print(f"    {user.name}: {count} mutual friends")
    
    print("\n5. INTEREST SIMILARITY")
    print("-" * 40)
    
    similarity = alice.get_interest_similarity(eve)
    print(f"  Interest similarity (Alice vs Eve): {similarity * 100:.1f}%")
    
    print("\n6. FRIENDS OF FRIENDS RECOMMENDATIONS")
    print("-" * 40)
    
    engine = RecommendationEngine(graph)
    engine.set_strategy(FriendsOfFriendsStrategy())
    recommendations = engine.recommend_friends("alice")
    
    print("  Recommended friends for Alice:")
    for user, score in recommendations:
        print(f"    {user.name}: {score} mutual friends")
    
    print("\n7. INTEREST-BASED RECOMMENDATIONS")
    print("-" * 40)
    
    engine.set_strategy(InterestSimilarityStrategy())
    recommendations = engine.recommend_friends("alice")
    
    print("  Recommended friends for Alice:")
    for user, score in recommendations:
        print(f"    {user.name}: {score:.1f}% interest match")
    
    print("\n8. HYBRID RECOMMENDATIONS")
    print("-" * 40)
    
    hybrid = HybridRecommendationStrategy([
        (FriendsOfFriendsStrategy(), 0.6),
        (InterestSimilarityStrategy(), 0.4)
    ])
    engine.set_strategy(hybrid)
    recommendations = engine.recommend_friends("alice")
    
    print("  Hybrid recommendations for Alice:")
    for user, score in recommendations:
        print(f"    {user.name}: {score:.1f}% combined score")
    
    print("\n9. RECOMMENDATION EXPLANATIONS")
    print("-" * 40)
    
    for user, score in recommendations[:3]:
        common_interests = alice.get_common_interests(user)
        mutual_friends = graph.get_mutual_friends("alice", user.user_id)
        
        print(f"\n  {user.name}:")
        if common_interests:
            print(f"    Common interests: {', '.join(i.value for i in common_interests)}")
        if mutual_friends:
            print(f"    Mutual friends: {', '.join(mutual_friends)}")


if __name__ == "__main__":
    demonstrate_recommendation_engine()
```

---

## 📁 Section 4: Duplicate File Finder

A complete duplicate file finder using sets and hashing to identify identical files across directories.

**SOLID Principles Applied:**
- Single Responsibility: Each class handles one aspect of duplicate detection
- Open/Closed: New hashing algorithms can be added

**Design Patterns:**
- Strategy Pattern: Different hashing strategies
- Iterator Pattern: Recursive directory traversal

```python
"""
DUPLICATE FILE FINDER

This section builds a duplicate file finder using sets and hashing.

SOLID Principles Applied:
- Single Responsibility: Each class handles one aspect
- Open/Closed: New hashing algorithms can be added

Design Patterns:
- Strategy Pattern: Different hashing strategies
- Iterator Pattern: Recursive directory traversal
"""

from typing import Dict, List, Set, Tuple, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
import hashlib
import os
from collections import defaultdict


@dataclass
class FileInfo:
    """Information about a file."""
    path: Path
    name: str
    size: int
    modified_time: datetime
    hash: Optional[str] = None
    
    def __hash__(self):
        return hash(self.path)
    
    def __eq__(self, other):
        if not isinstance(other, FileInfo):
            return False
        return self.path == other.path


class HashStrategy:
    """Base class for hashing strategies."""
    
    def compute_hash(self, file_path: Path) -> str:
        """Compute hash of a file."""
        raise NotImplementedError


class MD5HashStrategy(HashStrategy):
    """MD5 hashing strategy."""
    
    def compute_hash(self, file_path: Path) -> str:
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


class SHA256HashStrategy(HashStrategy):
    """SHA256 hashing strategy (more secure)."""
    
    def compute_hash(self, file_path: Path) -> str:
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()


class FastHashStrategy(HashStrategy):
    """Fast hashing using size + first/last chunks."""
    
    def compute_hash(self, file_path: Path) -> str:
        """Compute a fast hash using size and sample chunks."""
        size = os.path.getsize(file_path)
        
        with open(file_path, "rb") as f:
            # Read first 1KB
            first_chunk = f.read(1024)
            
            # Read last 1KB
            f.seek(max(0, size - 1024))
            last_chunk = f.read(1024)
        
        # Combine size and chunks
        combined = f"{size}:{first_chunk}:{last_chunk}"
        return hashlib.md5(combined.encode()).hexdigest()


class DuplicateFinder:
    """
    Finds duplicate files using sets and hash grouping.
    
    Design Pattern: Strategy Pattern - Pluggable hashing strategies
    """
    
    def __init__(self, hash_strategy: Optional[HashStrategy] = None):
        self.hash_strategy = hash_strategy or MD5HashStrategy()
        self.files: List[FileInfo] = []
    
    def scan_directory(self, directory: Path, recursive: bool = True) -> None:
        """
        Scan a directory for files.
        
        Args:
            directory: Directory to scan
            recursive: Whether to scan subdirectories
        """
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        if recursive:
            for file_path in directory.rglob("*"):
                if file_path.is_file():
                    self.add_file(file_path)
        else:
            for file_path in directory.iterdir():
                if file_path.is_file():
                    self.add_file(file_path)
    
    def add_file(self, file_path: Path) -> None:
        """Add a single file to the scanner."""
        try:
            stat = file_path.stat()
            file_info = FileInfo(
                path=file_path,
                name=file_path.name,
                size=stat.st_size,
                modified_time=datetime.fromtimestamp(stat.st_mtime)
            )
            self.files.append(file_info)
        except (OSError, PermissionError):
            print(f"  Could not read: {file_path}")
    
    def compute_hashes(self, progress_callback: Optional[callable] = None) -> None:
        """Compute hashes for all files."""
        total = len(self.files)
        for i, file_info in enumerate(self.files):
            if progress_callback:
                progress_callback(i + 1, total, file_info.path.name)
            file_info.hash = self.hash_strategy.compute_hash(file_info.path)
    
    def find_duplicates_by_size(self) -> Dict[int, List[FileInfo]]:
        """Group files by size (first pass for duplicates)."""
        size_groups = defaultdict(list)
        for file_info in self.files:
            size_groups[file_info.size].append(file_info)
        
        # Only keep sizes with multiple files
        return {size: files for size, files in size_groups.items() if len(files) > 1}
    
    def find_duplicates_by_hash(self) -> Dict[str, List[FileInfo]]:
        """Group files by hash (definitive duplicates)."""
        # First filter by size for efficiency
        size_groups = self.find_duplicates_by_size()
        
        hash_groups = defaultdict(list)
        
        for size, files in size_groups.items():
            for file_info in files:
                if file_info.hash is None:
                    self.hash_strategy.compute_hash(file_info.path)
                hash_groups[file_info.hash].append(file_info)
        
        # Only keep hashes with multiple files
        return {hash_val: files for hash_val, files in hash_groups.items() if len(files) > 1}
    
    def get_duplicate_sets(self) -> List[List[FileInfo]]:
        """Get list of duplicate file sets."""
        hash_groups = self.find_duplicates_by_hash()
        return list(hash_groups.values())
    
    def get_duplicate_stats(self) -> Dict[str, Any]:
        """Get statistics about duplicates."""
        duplicate_sets = self.get_duplicate_sets()
        
        total_duplicate_files = sum(len(files) for files in duplicate_sets)
        total_duplicate_size = sum(
            files[0].size * (len(files) - 1) for files in duplicate_sets
        )
        
        return {
            "total_files_scanned": len(self.files),
            "duplicate_sets": len(duplicate_sets),
            "duplicate_files": total_duplicate_files,
            "duplicate_size_bytes": total_duplicate_size,
            "duplicate_size_mb": round(total_duplicate_size / (1024 * 1024), 2),
            "wasted_space_mb": round(total_duplicate_size / (1024 * 1024), 2)
        }
    
    def generate_report(self) -> str:
        """Generate a duplicate file report."""
        stats = self.get_duplicate_stats()
        duplicate_sets = self.get_duplicate_sets()
        
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("DUPLICATE FILE REPORT")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        report_lines.append(f"\n📊 STATISTICS:")
        report_lines.append(f"  Files scanned: {stats['total_files_scanned']:,}")
        report_lines.append(f"  Duplicate sets: {stats['duplicate_sets']}")
        report_lines.append(f"  Duplicate files: {stats['duplicate_files']:,}")
        report_lines.append(f"  Wasted space: {stats['wasted_space_mb']:.2f} MB")
        
        if duplicate_sets:
            report_lines.append(f"\n📁 DUPLICATE FILES:")
            for i, file_set in enumerate(duplicate_sets[:10], 1):
                size_mb = file_set[0].size / (1024 * 1024)
                report_lines.append(f"\n  Set {i}: {len(file_set)} files ({size_mb:.2f} MB each)")
                for file_info in file_set[:5]:
                    report_lines.append(f"    • {file_info.path}")
                if len(file_set) > 5:
                    report_lines.append(f"    ... and {len(file_set) - 5} more")
        
        report_lines.append("\n" + "=" * 60)
        
        return "\n".join(report_lines)


def demonstrate_duplicate_finder():
    """
    Demonstrate the duplicate file finder.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: DUPLICATE FILE FINDER")
    print("=" * 60)
    
    import tempfile
    import shutil
    
    # Create temporary directory with duplicate files
    print("\n1. CREATING TEST DIRECTORY WITH DUPLICATES")
    print("-" * 40)
    
    temp_dir = tempfile.mkdtemp()
    print(f"  Created temp directory: {temp_dir}")
    
    def create_file(path: str, content: str):
        with open(path, 'w') as f:
            f.write(content)
    
    # Create unique files
    create_file(os.path.join(temp_dir, "file1.txt"), "Unique content A")
    create_file(os.path.join(temp_dir, "file2.txt"), "Unique content B")
    
    # Create duplicates
    create_file(os.path.join(temp_dir, "dup1.txt"), "Duplicate content X")
    create_file(os.path.join(temp_dir, "dup2.txt"), "Duplicate content X")
    create_file(os.path.join(temp_dir, "dup3.txt"), "Duplicate content X")
    
    # Create another duplicate set
    create_file(os.path.join(temp_dir, "data1.csv"), "1,2,3,4,5")
    create_file(os.path.join(temp_dir, "data2.csv"), "1,2,3,4,5")
    
    # Create subdirectory with more duplicates
    subdir = os.path.join(temp_dir, "subdir")
    os.makedirs(subdir)
    create_file(os.path.join(subdir, "dup1.txt"), "Duplicate content X")
    create_file(os.path.join(subdir, "data3.csv"), "1,2,3,4,5")
    
    print("  Created files:")
    print("    Unique: file1.txt, file2.txt")
    print("    Duplicates (3x): dup1.txt, dup2.txt, dup3.txt")
    print("    Duplicates (2x): data1.csv, data2.csv")
    print("    Subdirectory duplicates: dup1.txt (copy), data3.csv (copy)")
    
    # Find duplicates
    print("\n2. SCANNING FOR DUPLICATES")
    print("-" * 40)
    
    finder = DuplicateFinder(MD5HashStrategy())
    finder.scan_directory(Path(temp_dir), recursive=True)
    
    def show_progress(current, total, filename):
        print(f"  Hashing: [{current}/{total}] {filename}")
    
    finder.compute_hashes(show_progress)
    
    print("\n3. DUPLICATE ANALYSIS")
    print("-" * 40)
    
    stats = finder.get_duplicate_stats()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value}")
    
    print("\n4. DUPLICATE SETS")
    print("-" * 40)
    
    duplicate_sets = finder.get_duplicate_sets()
    for i, file_set in enumerate(duplicate_sets, 1):
        print(f"\n  Set {i}: {len(file_set)} copies")
        for file_info in file_set:
            print(f"    {file_info.path}")
    
    print("\n5. COMPLETE REPORT")
    print("-" * 40)
    
    report = finder.generate_report()
    print(report)
    
    # Clean up
    shutil.rmtree(temp_dir)
    print(f"\n  Cleaned up: {temp_dir}")


if __name__ == "__main__":
    demonstrate_duplicate_finder()
```

---

## 🏷️ Section 5: Tag-Based Content Recommendation

A complete content recommendation system using sets and tags.

**SOLID Principles Applied:**
- Single Responsibility: Each recommendation strategy has one purpose
- Open/Closed: New content types can be added

**Design Patterns:**
- Strategy Pattern: Different recommendation strategies
- Repository Pattern: Content storage

```python
"""
TAG-BASED CONTENT RECOMMENDATION

This section builds a content recommendation system using sets and tags.

SOLID Principles Applied:
- Single Responsibility: Each strategy has one purpose
- Open/Closed: New content types can be added

Design Patterns:
- Strategy Pattern: Different recommendation strategies
- Repository Pattern: Content storage
"""

from typing import Set, Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
import json


@dataclass
class Content:
    """Represents a piece of content."""
    id: str
    title: str
    type: str  # article, video, product, etc.
    tags: Set[str] = field(default_factory=set)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    views: int = 0
    likes: int = 0
    
    def add_tag(self, tag: str) -> None:
        """Add a tag to the content."""
        self.tags.add(tag)
    
    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the content."""
        self.tags.discard(tag)
    
    def get_tag_similarity(self, other: 'Content') -> float:
        """Calculate tag similarity (Jaccard index)."""
        if not self.tags and not other.tags:
            return 0.0
        
        intersection = len(self.tags & other.tags)
        union = len(self.tags | other.tags)
        return intersection / union if union > 0 else 0.0
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "type": self.type,
            "tags": list(self.tags),
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "views": self.views,
            "likes": self.likes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Content':
        """Create from dictionary."""
        content = cls(
            id=data["id"],
            title=data["title"],
            type=data["type"],
            tags=set(data["tags"]),
            metadata=data.get("metadata", {}),
            created_at=datetime.fromisoformat(data["created_at"]) if "created_at" in data else datetime.now(),
            views=data.get("views", 0),
            likes=data.get("likes", 0)
        )
        return content


class ContentRepository:
    """
    Content repository for storage and retrieval.
    
    Design Pattern: Repository Pattern - Centralized content storage
    """
    
    def __init__(self):
        self.contents: Dict[str, Content] = {}
        self.tag_index: Dict[str, Set[str]] = defaultdict(set)  # tag -> set of content_ids
    
    def add_content(self, content: Content) -> None:
        """Add content to repository."""
        self.contents[content.id] = content
        
        for tag in content.tags:
            self.tag_index[tag].add(content.id)
    
    def get_content(self, content_id: str) -> Optional[Content]:
        """Get content by ID."""
        return self.contents.get(content_id)
    
    def get_by_tag(self, tag: str) -> List[Content]:
        """Get all content with a specific tag."""
        content_ids = self.tag_index.get(tag, set())
        return [self.contents[cid] for cid in content_ids if cid in self.contents]
    
    def get_by_tags(self, tags: Set[str]) -> List[Content]:
        """Get content that has ANY of the given tags."""
        content_ids = set()
        for tag in tags:
            content_ids.update(self.tag_index.get(tag, set()))
        return [self.contents[cid] for cid in content_ids if cid in self.contents]
    
    def get_by_all_tags(self, tags: Set[str]) -> List[Content]:
        """Get content that has ALL of the given tags."""
        if not tags:
            return []
        
        content_ids = self.tag_index.get(next(iter(tags)), set())
        for tag in tags:
            content_ids &= self.tag_index.get(tag, set())
        
        return [self.contents[cid] for cid in content_ids if cid in self.contents]
    
    def get_all_content(self) -> List[Content]:
        """Get all content."""
        return list(self.contents.values())
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get repository statistics."""
        all_tags = set()
        for tags in self.tag_index.keys():
            all_tags.add(tags)
        
        return {
            "total_content": len(self.contents),
            "unique_tags": len(self.tag_index),
            "avg_tags_per_content": sum(len(c.tags) for c in self.contents.values()) / len(self.contents) if self.contents else 0,
            "most_popular_tags": self.get_most_popular_tags(10)
        }
    
    def get_most_popular_tags(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Get most frequently used tags."""
        tag_counts = [(tag, len(ids)) for tag, ids in self.tag_index.items()]
        tag_counts.sort(key=lambda x: x[1], reverse=True)
        return tag_counts[:limit]


class RecommendationStrategy:
    """Base class for recommendation strategies."""
    
    def recommend(self, repository: ContentRepository, content_id: str, limit: int = 10) -> List[Tuple[Content, float]]:
        """Recommend content with scores."""
        raise NotImplementedError


class TagBasedRecommendation(RecommendationStrategy):
    """Recommend content with similar tags."""
    
    def recommend(self, repository: ContentRepository, content_id: str, limit: int = 10) -> List[Tuple[Content, float]]:
        source = repository.get_content(content_id)
        if not source:
            return []
        
        scores = []
        for other in repository.get_all_content():
            if other.id == content_id:
                continue
            
            similarity = source.get_tag_similarity(other)
            if similarity > 0:
                scores.append((other, round(similarity * 100, 1)))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:limit]


class PopularityRecommendation(RecommendationStrategy):
    """Recommend popular content (most views/likes)."""
    
    def __init__(self, weight_views: float = 0.5, weight_likes: float = 0.5):
        self.weight_views = weight_views
        self.weight_likes = weight_likes
    
    def recommend(self, repository: ContentRepository, content_id: str, limit: int = 10) -> List[Tuple[Content, float]]:
        scores = []
        for content in repository.get_all_content():
            if content.id == content_id:
                continue
            
            # Normalize scores (simplified)
            score = (content.views * self.weight_views) + (content.likes * self.weight_likes)
            scores.append((content, score))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:limit]


class CollaborativeRecommendation(RecommendationStrategy):
    """
    Collaborative filtering based on user interactions.
    
    Recommends content that users with similar preferences liked.
    """
    
    def __init__(self, user_history: Dict[str, Set[str]]):
        """
        Initialize with user interaction history.
        
        Args:
            user_history: Dict mapping user_id to set of content_ids they liked
        """
        self.user_history = user_history
    
    def recommend(self, repository: ContentRepository, content_id: str, limit: int = 10) -> List[Tuple[Content, float]]:
        # Find users who liked this content
        users_who_liked = set()
        for user_id, liked in self.user_history.items():
            if content_id in liked:
                users_who_liked.add(user_id)
        
        if not users_who_liked:
            return []
        
        # Find other content liked by these users
        candidate_scores = defaultdict(float)
        for user_id in users_who_liked:
            for liked_id in self.user_history[user_id]:
                if liked_id != content_id:
                    candidate_scores[liked_id] += 1
        
        # Get content objects
        recommendations = []
        for content_id, score in candidate_scores.items():
            content = repository.get_content(content_id)
            if content:
                recommendations.append((content, score))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:limit]


class HybridRecommendation(RecommendationStrategy):
    """
    Combine multiple recommendation strategies.
    
    Design Pattern: Composite Pattern - Combines multiple strategies
    """
    
    def __init__(self, strategies: List[Tuple[RecommendationStrategy, float]]):
        self.strategies = strategies
    
    def recommend(self, repository: ContentRepository, content_id: str, limit: int = 10) -> List[Tuple[Content, float]]:
        scores = defaultdict(float)
        
        for strategy, weight in self.strategies:
            results = strategy.recommend(repository, content_id, limit * 2)
            for content, score in results:
                scores[content.id] += score * weight
        
        # Normalize
        if scores:
            max_score = max(scores.values())
            if max_score > 0:
                scores = {cid: (s / max_score) * 100 for cid, s in scores.items()}
        
        recommendations = []
        for content_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]:
            content = repository.get_content(content_id)
            if content:
                recommendations.append((content, round(score, 1)))
        
        return recommendations


def demonstrate_recommendation_system():
    """
    Demonstrate the content recommendation system.
    """
    print("\n" + "=" * 60)
    print("SECTION 5: TAG-BASED CONTENT RECOMMENDATION")
    print("=" * 60)
    
    # Create repository
    repo = ContentRepository()
    
    print("\n1. ADDING CONTENT WITH TAGS")
    print("-" * 40)
    
    # Create content
    contents = [
        Content("c1", "Python for Beginners", "article", {"python", "programming", "beginner"}),
        Content("c2", "Advanced Python", "article", {"python", "programming", "advanced"}),
        Content("c3", "Data Science with Python", "article", {"python", "data", "machine-learning"}),
        Content("c4", "JavaScript Fundamentals", "article", {"javascript", "programming", "beginner"}),
        Content("c5", "React Tutorial", "article", {"javascript", "react", "frontend"}),
        Content("c6", "Machine Learning Basics", "article", {"machine-learning", "data", "beginner"}),
        Content("c7", "Deep Learning", "article", {"machine-learning", "ai", "advanced"}),
        Content("c8", "Web Development Guide", "article", {"web", "html", "css", "javascript"})
    ]
    
    # Set view counts and likes
    contents[0].views = 1000
    contents[0].likes = 850
    contents[1].views = 500
    contents[1].likes = 420
    contents[2].views = 800
    contents[2].likes = 700
    contents[3].views = 600
    contents[3].likes = 480
    contents[4].views = 700
    contents[4].likes = 620
    contents[5].views = 750
    contents[5].likes = 650
    contents[6].views = 400
    contents[6].likes = 350
    contents[7].views = 550
    contents[7].likes = 500
    
    for content in contents:
        repo.add_content(content)
        print(f"  Added: {content.title} - tags: {', '.join(content.tags)}")
    
    print("\n2. TAG-BASED RECOMMENDATIONS (Set Similarity)")
    print("-" * 40)
    
    tag_rec = TagBasedRecommendation()
    recommendations = tag_rec.recommend(repo, "c1")
    
    print("  Content similar to 'Python for Beginners':")
    for content, score in recommendations:
        common = contents[0].get_tag_similarity(content)
        print(f"    {content.title}: {score:.1f}% match (common tags: {', '.join(contents[0].tags & content.tags)})")
    
    print("\n3. POPULARITY-BASED RECOMMENDATIONS")
    print("-" * 40)
    
    pop_rec = PopularityRecommendation(weight_views=0.6, weight_likes=0.4)
    recommendations = pop_rec.recommend(repo, "c1")
    
    print("  Popular content (based on views/likes):")
    for content, score in recommendations[:5]:
        print(f"    {content.title}: {score:.0f} points ({content.views} views, {content.likes} likes)")
    
    print("\n4. GETTING CONTENT BY TAGS (Set Operations)")
    print("-" * 40)
    
    # Content with ANY of these tags (union)
    python_content = repo.get_by_tags({"python", "javascript"})
    print(f"  Content with Python OR JavaScript tags: {len(python_content)} items")
    for c in python_content:
        print(f"    {c.title}")
    
    # Content with ALL of these tags (intersection)
    python_beginner = repo.get_by_all_tags({"python", "beginner"})
    print(f"\n  Content with Python AND Beginner tags: {len(python_beginner)} items")
    for c in python_beginner:
        print(f"    {c.title}")
    
    print("\n5. COLLABORATIVE FILTERING")
    print("-" * 40)
    
    # Simulate user history
    user_history = {
        "user1": {"c1", "c2", "c3"},
        "user2": {"c1", "c4", "c5"},
        "user3": {"c2", "c3", "c6", "c7"},
        "user4": {"c4", "c5", "c8"}
    }
    
    collab_rec = CollaborativeRecommendation(user_history)
    recommendations = collab_rec.recommend(repo, "c1")
    
    print("  Users who liked 'Python for Beginners' also liked:")
    for content, score in recommendations:
        print(f"    {content.title} (liked by {int(score)} users)")
    
    print("\n6. HYBRID RECOMMENDATIONS")
    print("-" * 40)
    
    hybrid = HybridRecommendation([
        (TagBasedRecommendation(), 0.5),
        (PopularityRecommendation(), 0.3),
        (CollaborativeRecommendation(user_history), 0.2)
    ])
    
    recommendations = hybrid.recommend(repo, "c1")
    
    print("  Hybrid recommendations for 'Python for Beginners':")
    for content, score in recommendations:
        print(f"    {content.title}: {score:.1f}% confidence")
    
    print("\n7. REPOSITORY STATISTICS")
    print("-" * 40)
    
    stats = repo.get_statistics()
    for key, value in stats.items():
        if key == "most_popular_tags":
            print(f"  {key}:")
            for tag, count in value[:5]:
                print(f"    {tag}: {count} items")
        else:
            print(f"  {key}: {value}")


if __name__ == "__main__":
    demonstrate_recommendation_system()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Set Basics** – Created with `{}` or `set()`. Stores unique, unordered elements. O(1) membership testing.

- **Set Operations** – Union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`). Subset (`<=`), superset (`>=`), disjoint (`isdisjoint()`).

- **Set Methods** – `add()`, `remove()` (raises error), `discard()` (no error), `pop()` (arbitrary), `clear()`, `copy()`, `update()` (add multiple).

- **Frozenset** – Immutable version of set. Hashable, can be used as dictionary keys.

- **Performance** – O(1) membership vs O(n) for lists. Use sets for fast lookups and uniqueness.

- **Analytics System** – Track unique visitors with daily/hourly sets. Page overlap with intersection. Conversion funnels with sequential intersection.

- **Friend Recommendation** – Friends of friends with mutual friend counting. Interest similarity with Jaccard index. Hybrid recommendations.

- **Duplicate File Finder** – Group by size, then hash. Sets for deduplication. Recursive directory scanning.

- **Content Recommendation** – Tag-based similarity. Popularity ranking. Collaborative filtering. Hybrid strategies.

- **SOLID Principles Applied** – Single Responsibility (each class has one purpose), Open/Closed (new strategies can be added), Interface Segregation (clean interfaces), Dependency Inversion (depends on abstractions).

- **Design Patterns Used** – Strategy Pattern (recommendation algorithms), Repository Pattern (content storage), Singleton Pattern (analytics instance), Iterator Pattern (directory traversal), Composite Pattern (hybrid strategies).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Dictionaries – Key-Value Power

- **📚 Series C Catalog:** Data Structures Express – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Comprehensions – One-Line Power (Series C, Story 5)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 4 | 1 | 80% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **22** | **30** | **42%** |

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

**Next Story:** Series C, Story 5: The 2026 Python Metromap: Comprehensions – One-Line Power

---

## 📝 Your Invitation

You've mastered sets. Now build something with what you've learned:

1. **Build a spell checker** – Use a set of dictionary words for O(1) lookup. Suggest corrections based on edit distance.

2. **Create a playlist deduplicator** – Remove duplicate songs from playlists using sets. Find common songs between playlists.

3. **Build a social network analyzer** – Find mutual friends, recommend connections, detect communities using set operations.

4. **Create an inventory system** – Track unique products, find out-of-stock items, analyze category overlaps.

5. **Build a security system** – Track blocked IPs, detect suspicious patterns, analyze login attempts with sets.

**You've mastered sets. Next stop: Comprehensions!**

---

*Found this helpful? Clap, comment, and share what you built with sets. Next stop: Comprehensions!* 🚇