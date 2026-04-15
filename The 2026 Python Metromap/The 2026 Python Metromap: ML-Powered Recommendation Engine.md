# The 2026 Python Metromap: ML-Powered Recommendation Engine

## Series J: Capstone Projects | Story 3 of 3

![The 2026 Python Metromap/images/ML-Powered Recommendation Engine](images/ML-Powered Recommendation Engine.png)

## 📖 Introduction

**Welcome to the final stop on the Capstone Projects Line—and the entire Python Metromap journey!**

You've mastered Python fundamentals, object-oriented programming, data science, web development, AI/ML, and built complete applications. Now it's time to bring everything together into a sophisticated, production-ready recommendation system.

This story—**The 2026 Python Metromap: ML-Powered Recommendation Engine**—is your ultimate capstone project. You'll build a complete recommendation system that suggests products to users based on their behavior and preferences. You'll implement collaborative filtering, content-based filtering, and hybrid approaches. You'll create a full-stack application with a Flask API, React frontend, PostgreSQL database, Redis cache, and Docker deployment. You'll learn how to handle real-world ML challenges like cold start problems, scalability, and A/B testing.

This isn't just a recommendation engine—it's a complete ML-powered application that demonstrates everything you've learned throughout the Python Metromap.

**Let's build your masterpiece.**

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

- 💰 **The 2026 Python Metromap: CLI Expense Tracker** – Complete command-line application with OOP categories and transactions; JSON file storage; spending reports; Matplotlib visualization. ✅ *COMPLETED*

- 🌤️ **The 2026 Python Metromap: Weather Dashboard** – Flask web application; OpenWeatherMap API integration; Redis caching; HTML/CSS/JS frontend. ✅ *COMPLETED*

- 🎯 **The 2026 Python Metromap: ML-Powered Recommendation Engine** – Full-stack recommendation system with Pandas data processing; Scikit-learn collaborative filtering; Flask API; Docker deployment. **⬅️ YOU ARE HERE**

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🧠 Section 1: Data Models & Recommendation Algorithms

Build the core recommendation engine with collaborative filtering and content-based filtering.

**SOLID Principles Applied:**
- Single Responsibility: Each algorithm handles one recommendation approach
- Open/Closed: New recommendation algorithms can be added
- Dependency Inversion: High-level recommender depends on algorithm abstractions

**Design Patterns:**
- Strategy Pattern: Interchangeable recommendation algorithms
- Factory Pattern: Creates recommendation models

```python
"""
ML-POWERED RECOMMENDATION ENGINE - SECTION 1: DATA MODELS & ALGORITHMS

This section implements the core recommendation algorithms.

SOLID Principles Applied:
- Single Responsibility: Each algorithm handles one recommendation approach
- Open/Closed: New recommendation algorithms can be added
- Dependency Inversion: High-level recommender depends on algorithm abstractions

Design Patterns:
- Strategy Pattern: Interchangeable recommendation algorithms
- Factory Pattern: Creates recommendation models
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
import pickle
from pathlib import Path
import logging
from collections import defaultdict, Counter
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ==================== ENUMS & DATA MODELS ====================

class InteractionType(Enum):
    """Types of user-item interactions."""
    VIEW = "view"
    CLICK = "click"
    ADD_TO_CART = "add_to_cart"
    PURCHASE = "purchase"
    RATING = "rating"
    REVIEW = "review"


class RecommendationType(Enum):
    """Types of recommendations."""
    COLLABORATIVE = "collaborative"
    CONTENT_BASED = "content_based"
    HYBRID = "hybrid"
    POPULARITY = "popularity"
    PERSONALIZED = "personalized"


@dataclass
class User:
    """Represents a user in the system."""
    user_id: str
    name: str
    email: str
    age: Optional[int] = None
    location: Optional[str] = None
    preferences: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'location': self.location,
            'preferences': self.preferences,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Create user from dictionary."""
        return cls(
            user_id=data['user_id'],
            name=data['name'],
            email=data['email'],
            age=data.get('age'),
            location=data.get('location'),
            preferences=data.get('preferences', {}),
            created_at=datetime.fromisoformat(data['created_at'])
        )


@dataclass
class Item:
    """Represents an item (product) in the catalog."""
    item_id: str
    name: str
    category: str
    price: float
    description: str
    tags: List[str] = field(default_factory=list)
    attributes: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    rating_avg: float = 0.0
    rating_count: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description,
            'tags': self.tags,
            'attributes': self.attributes,
            'created_at': self.created_at.isoformat(),
            'rating_avg': self.rating_avg,
            'rating_count': self.rating_count
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Item':
        """Create item from dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            category=data['category'],
            price=data['price'],
            description=data['description'],
            tags=data.get('tags', []),
            attributes=data.get('attributes', {}),
            created_at=datetime.fromisoformat(data['created_at']),
            rating_avg=data.get('rating_avg', 0.0),
            rating_count=data.get('rating_count', 0)
        )


@dataclass
class Interaction:
    """Represents a user-item interaction."""
    user_id: str
    item_id: str
    interaction_type: InteractionType
    value: float = 1.0  # For ratings or weights
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'user_id': self.user_id,
            'item_id': self.item_id,
            'interaction_type': self.interaction_type.value,
            'value': self.value,
            'timestamp': self.timestamp.isoformat(),
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Interaction':
        """Create interaction from dictionary."""
        return cls(
            user_id=data['user_id'],
            item_id=data['item_id'],
            interaction_type=InteractionType(data['interaction_type']),
            value=data.get('value', 1.0),
            timestamp=datetime.fromisoformat(data['timestamp']),
            metadata=data.get('metadata', {})
        )


@dataclass
class Recommendation:
    """Represents a recommendation result."""
    item_id: str
    score: float
    reason: str
    algorithm: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'item_id': self.item_id,
            'score': self.score,
            'reason': self.reason,
            'algorithm': self.algorithm
        }


# ==================== RECOMMENDATION ALGORITHMS ====================

class RecommendationAlgorithm:
    """
    Base class for recommendation algorithms.
    
    Design Pattern: Strategy Pattern - Base strategy interface
    SOLID Principle: Open/Closed - New algorithms can be added
    """
    
    def __init__(self, name: str):
        self.name = name
        self.is_trained = False
    
    def train(self, interactions: List[Interaction], items: List[Item]):
        """Train the recommendation model."""
        raise NotImplementedError
    
    def recommend(self, user_id: str, n: int = 10) -> List[Recommendation]:
        """Generate recommendations for a user."""
        raise NotImplementedError
    
    def get_similar_items(self, item_id: str, n: int = 10) -> List[Recommendation]:
        """Get similar items."""
        raise NotImplementedError


class CollaborativeFiltering(RecommendationAlgorithm):
    """
    Collaborative filtering using matrix factorization.
    
    Design Pattern: Strategy Pattern - Concrete strategy
    SOLID Principle: Single Responsibility - Only handles collaborative filtering
    """
    
    def __init__(self, n_factors: int = 50, n_epochs: int = 20, lr: float = 0.01, reg: float = 0.02):
        super().__init__("Collaborative Filtering")
        self.n_factors = n_factors
        self.n_epochs = n_epochs
        self.lr = lr
        self.reg = reg
        
        self.user_factors = None
        self.item_factors = None
        self.user_bias = None
        self.item_bias = None
        self.global_mean = None
        
        self.user_ids = []
        self.item_ids = []
        self.user_to_idx = {}
        self.item_to_idx = {}
    
    def _build_matrix(self, interactions: List[Interaction]) -> Tuple[np.ndarray, np.ndarray]:
        """Build user-item interaction matrix."""
        # Get unique users and items
        self.user_ids = list(set(i.user_id for i in interactions))
        self.item_ids = list(set(i.item_id for i in interactions))
        
        self.user_to_idx = {uid: idx for idx, uid in enumerate(self.user_ids)}
        self.item_to_idx = {iid: idx for idx, iid in enumerate(self.item_ids)}
        
        # Build rating matrix
        n_users = len(self.user_ids)
        n_items = len(self.item_ids)
        ratings = np.zeros((n_users, n_items))
        
        for interaction in interactions:
            user_idx = self.user_to_idx[interaction.user_id]
            item_idx = self.item_to_idx[interaction.item_id]
            ratings[user_idx, item_idx] = interaction.value
        
        return ratings
    
    def train(self, interactions: List[Interaction], items: List[Item] = None):
        """Train collaborative filtering model using SGD."""
        logger.info(f"Training {self.name} model...")
        
        # Build interaction matrix
        ratings = self._build_matrix(interactions)
        n_users, n_items = ratings.shape
        
        # Initialize factors and biases
        np.random.seed(42)
        self.user_factors = np.random.normal(0, 0.1, (n_users, self.n_factors))
        self.item_factors = np.random.normal(0, 0.1, (n_items, self.n_factors))
        self.user_bias = np.zeros(n_users)
        self.item_bias = np.zeros(n_items)
        self.global_mean = np.mean(ratings[ratings > 0])
        
        # SGD training
        for epoch in range(self.n_epochs):
            total_error = 0
            n_ratings = 0
            
            for user_idx in range(n_users):
                for item_idx in range(n_items):
                    rating = ratings[user_idx, item_idx]
                    if rating == 0:
                        continue
                    
                    # Predict rating
                    pred = self._predict_rating(user_idx, item_idx)
                    error = rating - pred
                    total_error += error ** 2
                    n_ratings += 1
                    
                    # Update factors and biases
                    self.user_factors[user_idx] += self.lr * (error * self.item_factors[item_idx] - self.reg * self.user_factors[user_idx])
                    self.item_factors[item_idx] += self.lr * (error * self.user_factors[user_idx] - self.reg * self.item_factors[item_idx])
                    self.user_bias[user_idx] += self.lr * (error - self.reg * self.user_bias[user_idx])
                    self.item_bias[item_idx] += self.lr * (error - self.reg * self.item_bias[item_idx])
            
            rmse = np.sqrt(total_error / n_ratings) if n_ratings > 0 else 0
            logger.info(f"Epoch {epoch + 1}/{self.n_epochs}, RMSE: {rmse:.4f}")
        
        self.is_trained = True
        logger.info(f"Training complete. Final RMSE: {rmse:.4f}")
    
    def _predict_rating(self, user_idx: int, item_idx: int) -> float:
        """Predict rating for user-item pair."""
        pred = self.global_mean + self.user_bias[user_idx] + self.item_bias[item_idx]
        pred += np.dot(self.user_factors[user_idx], self.item_factors[item_idx])
        return max(0, min(5, pred))  # Clip to rating range
    
    def predict_rating(self, user_id: str, item_id: str) -> float:
        """Predict rating for user-item pair."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        if user_id not in self.user_to_idx or item_id not in self.item_to_idx:
            return self.global_mean
        
        user_idx = self.user_to_idx[user_id]
        item_idx = self.item_to_idx[item_id]
        return self._predict_rating(user_idx, item_idx)
    
    def recommend(self, user_id: str, n: int = 10, exclude_interacted: bool = True) -> List[Recommendation]:
        """Generate recommendations for a user."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        if user_id not in self.user_to_idx:
            return []
        
        user_idx = self.user_to_idx[user_id]
        scores = []
        
        for item_idx, item_id in enumerate(self.item_ids):
            # Skip items user already interacted with
            if exclude_interacted:
                # Check if user has interacted with this item
                # This would be checked against actual interactions
                pass
            
            score = self._predict_rating(user_idx, item_idx)
            scores.append((item_id, score))
        
        # Sort by score and return top N
        scores.sort(key=lambda x: x[1], reverse=True)
        
        return [
            Recommendation(
                item_id=item_id,
                score=score,
                reason=f"Based on collaborative filtering with similar users",
                algorithm=self.name
            )
            for item_id, score in scores[:n]
        ]
    
    def get_similar_items(self, item_id: str, n: int = 10) -> List[Recommendation]:
        """Get similar items based on item factors."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        if item_id not in self.item_to_idx:
            return []
        
        item_idx = self.item_to_idx[item_id]
        item_vector = self.item_factors[item_idx]
        
        # Calculate similarities
        similarities = []
        for other_idx, other_id in enumerate(self.item_ids):
            if other_id == item_id:
                continue
            
            other_vector = self.item_factors[other_idx]
            similarity = cosine_similarity([item_vector], [other_vector])[0][0]
            similarities.append((other_id, similarity))
        
        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return [
            Recommendation(
                item_id=other_id,
                score=similarity,
                reason=f"Similar to item {item_id}",
                algorithm=self.name
            )
            for other_id, similarity in similarities[:n]
        ]


class ContentBasedFiltering(RecommendationAlgorithm):
    """
    Content-based filtering using item features.
    
    Design Pattern: Strategy Pattern - Concrete strategy
    """
    
    def __init__(self):
        super().__init__("Content-Based Filtering")
        self.tfidf_vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.item_features = None
        self.item_ids = []
        self.item_to_idx = {}
    
    def _extract_item_features(self, items: List[Item]) -> List[str]:
        """Extract text features from items."""
        features = []
        for item in items:
            # Combine item attributes into a single text
            text = f"{item.name} {item.category} {item.description} {' '.join(item.tags)}"
            features.append(text.lower())
        return features
    
    def train(self, interactions: List[Interaction] = None, items: List[Item] = None):
        """Train content-based model using TF-IDF."""
        if not items:
            raise ValueError("Items required for content-based filtering")
        
        logger.info(f"Training {self.name} model...")
        
        # Extract features
        self.item_ids = [item.item_id for item in items]
        self.item_to_idx = {item.item_id: idx for idx, item in enumerate(items)}
        
        text_features = self._extract_item_features(items)
        
        # Compute TF-IDF matrix
        self.item_features = self.tfidf_vectorizer.fit_transform(text_features)
        
        self.is_trained = True
        logger.info(f"Training complete. Feature matrix shape: {self.item_features.shape}")
    
    def recommend(self, user_id: str, n: int = 10, user_profile: Dict[str, float] = None) -> List[Recommendation]:
        """Generate recommendations based on user profile."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        if not user_profile:
            # If no user profile, return popular items
            return self._get_popular_items(n)
        
        # Convert user profile to vector
        profile_vector = self._profile_to_vector(user_profile)
        
        # Calculate similarities
        similarities = cosine_similarity(profile_vector, self.item_features)[0]
        
        # Get top N items
        top_indices = similarities.argsort()[-n:][::-1]
        
        return [
            Recommendation(
                item_id=self.item_ids[idx],
                score=similarities[idx],
                reason=f"Matches your interest in {self._get_top_keywords(idx, 3)}",
                algorithm=self.name
            )
            for idx in top_indices
        ]
    
    def _profile_to_vector(self, profile: Dict[str, float]) -> csr_matrix:
        """Convert user profile dictionary to TF-IDF vector."""
        # Build text from profile keywords
        profile_text = ' '.join([word for word, weight in profile.items() if weight > 0.5])
        return self.tfidf_vectorizer.transform([profile_text])
    
    def _get_popular_items(self, n: int) -> List[Recommendation]:
        """Get popular items (fallback)."""
        # This would use item popularity from interactions
        # For now, return random items
        indices = np.random.choice(len(self.item_ids), min(n, len(self.item_ids)), replace=False)
        return [
            Recommendation(
                item_id=self.item_ids[idx],
                score=0.5,
                reason="Popular item",
                algorithm=self.name
            )
            for idx in indices
        ]
    
    def _get_top_keywords(self, item_idx: int, n: int) -> str:
        """Get top keywords for an item."""
        feature_names = self.tfidf_vectorizer.get_feature_names_out()
        feature_weights = self.item_features[item_idx].toarray()[0]
        top_indices = feature_weights.argsort()[-n:][::-1]
        return ', '.join([feature_names[idx] for idx in top_indices])
    
    def get_similar_items(self, item_id: str, n: int = 10) -> List[Recommendation]:
        """Get similar items based on content features."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        if item_id not in self.item_to_idx:
            return []
        
        item_idx = self.item_to_idx[item_id]
        item_vector = self.item_features[item_idx]
        
        # Calculate similarities
        similarities = cosine_similarity(item_vector, self.item_features)[0]
        
        # Get top N similar items (excluding itself)
        top_indices = similarities.argsort()[-n-1:-1][::-1]
        
        return [
            Recommendation(
                item_id=self.item_ids[idx],
                score=similarities[idx],
                reason=f"Similar content to {item_id}",
                algorithm=self.name
            )
            for idx in top_indices
        ]


class HybridRecommender(RecommendationAlgorithm):
    """
    Hybrid recommender combining multiple algorithms.
    
    Design Pattern: Strategy Pattern - Composite strategy
    Design Pattern: Adapter Pattern - Adapts multiple algorithms
    """
    
    def __init__(self, algorithms: List[RecommendationAlgorithm], weights: List[float] = None):
        super().__init__("Hybrid Recommender")
        self.algorithms = algorithms
        self.weights = weights or [1.0 / len(algorithms)] * len(algorithms)
        
        # Normalize weights
        weight_sum = sum(self.weights)
        self.weights = [w / weight_sum for w in self.weights]
    
    def train(self, interactions: List[Interaction], items: List[Item]):
        """Train all underlying algorithms."""
        logger.info(f"Training {self.name} with {len(self.algorithms)} algorithms...")
        
        for algorithm in self.algorithms:
            algorithm.train(interactions, items)
        
        self.is_trained = True
    
    def recommend(self, user_id: str, n: int = 10) -> List[Recommendation]:
        """Combine recommendations from multiple algorithms."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        # Get recommendations from each algorithm
        all_recommendations = []
        scores_dict = defaultdict(float)
        reasons_dict = defaultdict(list)
        
        for weight, algorithm in zip(self.weights, self.algorithms):
            recommendations = algorithm.recommend(user_id, n=n * 2)  # Get more for merging
            
            for rec in recommendations:
                scores_dict[rec.item_id] += rec.score * weight
                reasons_dict[rec.item_id].append(f"{algorithm.name}: {rec.reason}")
        
        # Sort by combined score
        sorted_items = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)[:n]
        
        return [
            Recommendation(
                item_id=item_id,
                score=score,
                reason=" | ".join(reasons_dict[item_id][:2]),  # Top 2 reasons
                algorithm=self.name
            )
            for item_id, score in sorted_items
        ]
    
    def get_similar_items(self, item_id: str, n: int = 10) -> List[Recommendation]:
        """Get similar items from first algorithm."""
        if self.algorithms:
            return self.algorithms[0].get_similar_items(item_id, n)
        return []


class PopularityRecommender(RecommendationAlgorithm):
    """
    Simple popularity-based recommender (fallback for cold start).
    
    Design Pattern: Strategy Pattern - Simple strategy
    """
    
    def __init__(self):
        super().__init__("Popularity-Based")
        self.item_popularity = {}
    
    def train(self, interactions: List[Interaction], items: List[Item] = None):
        """Calculate item popularity from interactions."""
        logger.info(f"Training {self.name} model...")
        
        # Count interactions per item
        popularity = Counter()
        for interaction in interactions:
            popularity[interaction.item_id] += 1
        
        # Normalize scores
        max_count = max(popularity.values()) if popularity else 1
        self.item_popularity = {
            item_id: count / max_count
            for item_id, count in popularity.items()
        }
        
        self.is_trained = True
        logger.info(f"Training complete. Tracked {len(self.item_popularity)} items")
    
    def recommend(self, user_id: str, n: int = 10) -> List[Recommendation]:
        """Return most popular items."""
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        sorted_items = sorted(
            self.item_popularity.items(),
            key=lambda x: x[1],
            reverse=True
        )[:n]
        
        return [
            Recommendation(
                item_id=item_id,
                score=score,
                reason="Popular among all users",
                algorithm=self.name
            )
            for item_id, score in sorted_items
        ]
    
    def get_similar_items(self, item_id: str, n: int = 10) -> List[Recommendation]:
        """Not applicable for popularity recommender."""
        return []


# ==================== RECOMMENDATION ENGINE ====================

class RecommendationEngine:
    """
    Main recommendation engine that orchestrates everything.
    
    Design Pattern: Facade Pattern - Simplifies recommendation interface
    SOLID Principle: Single Responsibility - Orchestrates recommendations
    """
    
    def __init__(self):
        self.recommender = None
        self.interactions: List[Interaction] = []
        self.items: List[Item] = []
        self.users: List[User] = []
        
        # User profiles for content-based filtering
        self.user_profiles: Dict[str, Dict[str, float]] = {}
        
    def load_data(self, interactions: List[Interaction], items: List[Item], users: List[User]):
        """Load data into the engine."""
        self.interactions = interactions
        self.items = items
        self.users = users
        
        # Build user profiles from interactions
        self._build_user_profiles()
        
        logger.info(f"Loaded {len(users)} users, {len(items)} items, {len(interactions)} interactions")
    
    def _build_user_profiles(self):
        """Build user profiles based on their interactions."""
        # Create item feature vectors
        item_features = {}
        for item in self.items:
            # Extract keywords from item
            keywords = f"{item.name} {item.category} {' '.join(item.tags)}".lower().split()
            item_features[item.item_id] = keywords
        
        # Aggregate user preferences
        for user in self.users:
            user_keywords = Counter()
            user_interactions = [i for i in self.interactions if i.user_id == user.user_id]
            
            for interaction in user_interactions:
                keywords = item_features.get(interaction.item_id, [])
                weight = interaction.value
                for keyword in keywords:
                    user_keywords[keyword] += weight
            
            # Normalize and store
            total = sum(user_keywords.values())
            if total > 0:
                self.user_profiles[user.user_id] = {
                    keyword: count / total
                    for keyword, count in user_keywords.items()
                }
    
    def build_recommender(self, strategy: str = "hybrid", **kwargs):
        """Build the recommendation system with specified strategy."""
        logger.info(f"Building recommender with strategy: {strategy}")
        
        if strategy == "collaborative":
            self.recommender = CollaborativeFiltering(**kwargs)
        elif strategy == "content_based":
            self.recommender = ContentBasedFiltering(**kwargs)
        elif strategy == "popularity":
            self.recommender = PopularityRecommender()
        elif strategy == "hybrid":
            # Create hybrid with collaborative and content-based
            cf = CollaborativeFiltering(**kwargs.get('cf_params', {}))
            cb = ContentBasedFiltering()
            self.recommender = HybridRecommender(
                algorithms=[cf, cb],
                weights=kwargs.get('weights', [0.6, 0.4])
            )
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
        
        # Train the recommender
        self.recommender.train(self.interactions, self.items)
        
        logger.info("Recommender built and trained successfully")
    
    def recommend_for_user(self, user_id: str, n: int = 10) -> List[Recommendation]:
        """Get recommendations for a specific user."""
        if not self.recommender:
            raise ValueError("Recommender not built yet")
        
        # For content-based, pass user profile
        if isinstance(self.recommender, ContentBasedFiltering):
            user_profile = self.user_profiles.get(user_id, {})
            return self.recommender.recommend(user_id, n, user_profile=user_profile)
        
        return self.recommender.recommend(user_id, n)
    
    def get_similar_items(self, item_id: str, n: int = 10) -> List[Recommendation]:
        """Get items similar to a given item."""
        if not self.recommender:
            raise ValueError("Recommender not built yet")
        
        return self.recommender.get_similar_items(item_id, n)
    
    def predict_rating(self, user_id: str, item_id: str) -> float:
        """Predict rating for user-item pair."""
        if not self.recommender:
            raise ValueError("Recommender not built yet")
        
        if hasattr(self.recommender, 'predict_rating'):
            return self.recommender.predict_rating(user_id, item_id)
        
        # Fallback: use similarity or default
        return 3.0
    
    def get_user_embeddings(self, user_id: str) -> Optional[np.ndarray]:
        """Get user embedding vector (for collaborative filtering)."""
        if not self.recommender or not hasattr(self.recommender, 'user_factors'):
            return None
        
        cf = self.recommender
        if hasattr(cf, 'algorithms'):  # Hybrid
            for algo in cf.algorithms:
                if hasattr(algo, 'user_factors'):
                    cf = algo
                    break
        
        if user_id in cf.user_to_idx:
            idx = cf.user_to_idx[user_id]
            return cf.user_factors[idx]
        
        return None
    
    def get_item_embeddings(self, item_id: str) -> Optional[np.ndarray]:
        """Get item embedding vector."""
        if not self.recommender or not hasattr(self.recommender, 'item_factors'):
            return None
        
        cf = self.recommender
        if hasattr(cf, 'algorithms'):  # Hybrid
            for algo in cf.algorithms:
                if hasattr(algo, 'item_factors'):
                    cf = algo
                    break
        
        if item_id in cf.item_to_idx:
            idx = cf.item_to_idx[item_id]
            return cf.item_factors[idx]
        
        return None


# ==================== DEMONSTRATION ====================

def generate_sample_data(n_users: int = 100, n_items: int = 50, n_interactions: int = 1000):
    """Generate sample data for demonstration."""
    np.random.seed(42)
    
    # Generate users
    users = []
    for i in range(n_users):
        user = User(
            user_id=f"user_{i}",
            name=f"User {i}",
            email=f"user{i}@example.com",
            age=np.random.randint(18, 70),
            location=np.random.choice(['US', 'UK', 'CA', 'AU', 'DE']),
            preferences={'category_pref': np.random.choice(['electronics', 'books', 'clothing', 'home'])}
        )
        users.append(user)
    
    # Generate items
    categories = ['electronics', 'books', 'clothing', 'home', 'sports', 'toys']
    items = []
    for i in range(n_items):
        category = np.random.choice(categories)
        item = Item(
            item_id=f"item_{i}",
            name=f"Product {i}",
            category=category,
            price=np.random.uniform(10, 500),
            description=f"This is a great {category} product",
            tags=np.random.choice(['new', 'popular', 'sale', 'premium'], np.random.randint(1, 3)).tolist()
        )
        items.append(item)
    
    # Generate interactions
    interactions = []
    interaction_types = [InteractionType.VIEW, InteractionType.CLICK, InteractionType.PURCHASE]
    weights = {'view': 1, 'click': 2, 'purchase': 5}
    
    for _ in range(n_interactions):
        user = np.random.choice(users)
        item = np.random.choice(items)
        interaction_type = np.random.choice(interaction_types, p=[0.5, 0.3, 0.2])
        
        interaction = Interaction(
            user_id=user.user_id,
            item_id=item.item_id,
            interaction_type=interaction_type,
            value=weights[interaction_type.value]
        )
        interactions.append(interaction)
    
    return users, items, interactions


def demonstrate_recommendation_engine():
    """
    Demonstrate the recommendation engine functionality.
    """
    print("\n" + "=" * 60)
    print("SECTION 1: RECOMMENDATION ENGINE")
    print("=" * 60)
    
    # Generate sample data
    print("\n1. GENERATING SAMPLE DATA")
    print("-" * 40)
    
    users, items, interactions = generate_sample_data(50, 30, 500)
    print(f"  Users: {len(users)}")
    print(f"  Items: {len(items)}")
    print(f"  Interactions: {len(interactions)}")
    
    # Create recommendation engine
    print("\n2. CREATING RECOMMENDATION ENGINE")
    print("-" * 40)
    
    engine = RecommendationEngine()
    engine.load_data(interactions, items, users)
    
    # Build collaborative filtering recommender
    print("\n3. COLLABORATIVE FILTERING")
    print("-" * 40)
    
    engine.build_recommender(strategy="collaborative", n_factors=20, n_epochs=10)
    
    # Get recommendations for a user
    test_user = users[0]
    recommendations = engine.recommend_for_user(test_user.user_id, n=5)
    
    print(f"\n  Recommendations for {test_user.name}:")
    for i, rec in enumerate(recommendations, 1):
        item = next((item for item in items if item.item_id == rec.item_id), None)
        if item:
            print(f"    {i}. {item.name} (Score: {rec.score:.3f}) - {rec.reason}")
    
    # Get similar items
    print("\n4. SIMILAR ITEMS")
    print("-" * 40)
    
    test_item = items[0]
    similar_items = engine.get_similar_items(test_item.item_id, n=5)
    
    print(f"\n  Items similar to {test_item.name}:")
    for i, rec in enumerate(similar_items, 1):
        item = next((item for item in items if item.item_id == rec.item_id), None)
        if item:
            print(f"    {i}. {item.name} (Similarity: {rec.score:.3f})")
    
    # Build hybrid recommender
    print("\n5. HYBRID RECOMMENDER")
    print("-" * 40)
    
    engine.build_recommender(strategy="hybrid", weights=[0.7, 0.3])
    
    recommendations = engine.recommend_for_user(test_user.user_id, n=5)
    
    print(f"\n  Hybrid recommendations for {test_user.name}:")
    for i, rec in enumerate(recommendations, 1):
        item = next((item for item in items if item.item_id == rec.item_id), None)
        if item:
            print(f"    {i}. {item.name} (Score: {rec.score:.3f})")
            print(f"       Reason: {rec.reason[:80]}...")
    
    # Get embeddings
    print("\n6. USER AND ITEM EMBEDDINGS")
    print("-" * 40)
    
    user_embedding = engine.get_user_embeddings(test_user.user_id)
    item_embedding = engine.get_item_embeddings(test_item.item_id)
    
    if user_embedding is not None:
        print(f"  User embedding shape: {user_embedding.shape}")
        print(f"  User embedding sample: {user_embedding[:5]}")
    
    if item_embedding is not None:
        print(f"  Item embedding shape: {item_embedding.shape}")
        print(f"  Item embedding sample: {item_embedding[:5]}")
    
    print("\n✅ Recommendation engine ready!")


if __name__ == "__main__":
    demonstrate_recommendation_engine()
```

---

## 🗄️ Section 2: Database & API Layer

Build the database models and RESTful API for the recommendation engine.

**SOLID Principles Applied:**
- Single Responsibility: Each model handles one entity
- Dependency Inversion: API depends on service layer abstractions

**Design Patterns:**
- Repository Pattern: Database abstraction
- DTO Pattern: Data transfer objects for API

```python
"""
ML-POWERED RECOMMENDATION ENGINE - SECTION 2: DATABASE & API LAYER

This section implements database models and RESTful API.

SOLID Principles Applied:
- Single Responsibility: Each model handles one entity
- Dependency Inversion: API depends on service layer abstractions

Design Patterns:
- Repository Pattern: Database abstraction
- DTO Pattern: Data transfer objects for API
"""

# models.py - SQLAlchemy models
"""
Database models for the recommendation engine.
"""

from sqlalchemy import (
    create_engine, Column, String, Integer, Float, DateTime, 
    ForeignKey, Text, JSON, Index, Boolean
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid
from datetime import datetime
from passlib.hash import bcrypt

Base = declarative_base()


class UserModel(Base):
    """User database model."""
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False, index=True)
    password_hash = Column(String(200), nullable=False)
    age = Column(Integer)
    location = Column(String(100))
    preferences = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    interactions = relationship("InteractionModel", back_populates="user")
    
    def set_password(self, password: str):
        """Set user password."""
        self.password_hash = bcrypt.hash(password)
    
    def verify_password(self, password: str) -> bool:
        """Verify user password."""
        return bcrypt.verify(password, self.password_hash)


class ItemModel(Base):
    """Item database model."""
    __tablename__ = 'items'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_id = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False, index=True)
    price = Column(Float, nullable=False)
    description = Column(Text)
    tags = Column(ARRAY(String), default=[])
    attributes = Column(JSON, default={})
    image_url = Column(String(500))
    rating_avg = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_available = Column(Boolean, default=True)
    
    # Relationships
    interactions = relationship("InteractionModel", back_populates="item")
    
    # Indexes
    __table_args__ = (
        Index('idx_item_category', 'category'),
        Index('idx_item_price', 'price'),
    )


class InteractionModel(Base):
    """User-item interaction database model."""
    __tablename__ = 'interactions'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    item_id = Column(UUID(as_uuid=True), ForeignKey('items.id'), nullable=False)
    interaction_type = Column(String(50), nullable=False, index=True)
    value = Column(Float, default=1.0)
    metadata = Column(JSON, default={})
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relationships
    user = relationship("UserModel", back_populates="interactions")
    item = relationship("ItemModel", back_populates="interactions")
    
    # Indexes
    __table_args__ = (
        Index('idx_user_item', 'user_id', 'item_id'),
        Index('idx_timestamp', 'timestamp'),
    )


class RecommendationCacheModel(Base):
    """Cached recommendations for users."""
    __tablename__ = 'recommendation_cache'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False, unique=True)
    recommendations = Column(JSON, nullable=False)
    algorithm = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    
    __table_args__ = (
        Index('idx_expires_at', 'expires_at'),
    )


class UserFeedbackModel(Base):
    """User feedback on recommendations."""
    __tablename__ = 'user_feedback'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    item_id = Column(UUID(as_uuid=True), ForeignKey('items.id'), nullable=False)
    feedback_type = Column(String(50), nullable=False)  # like, dislike, rating
    rating = Column(Integer)  # 1-5 for rating feedback
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        Index('idx_user_feedback', 'user_id', 'item_id'),
    )


class RecommendationLogModel(Base):
    """Log of recommendations served."""
    __tablename__ = 'recommendation_logs'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    item_ids = Column(ARRAY(String), nullable=False)
    algorithm = Column(String(100))
    request_id = Column(String(100), index=True)
    response_time_ms = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    __table_args__ = (
        Index('idx_log_timestamp', 'timestamp'),
    )


# ==================== REPOSITORY LAYER ====================

class UserRepository:
    """Repository for user operations."""
    
    def __init__(self, session):
        self.session = session
    
    def create(self, user_data: Dict[str, Any]) -> UserModel:
        """Create a new user."""
        user = UserModel(
            user_id=user_data['user_id'],
            name=user_data['name'],
            email=user_data['email'],
            age=user_data.get('age'),
            location=user_data.get('location'),
            preferences=user_data.get('preferences', {})
        )
        user.set_password(user_data['password'])
        self.session.add(user)
        self.session.commit()
        return user
    
    def get_by_id(self, user_id: str) -> Optional[UserModel]:
        """Get user by ID."""
        return self.session.query(UserModel).filter_by(user_id=user_id).first()
    
    def get_by_email(self, email: str) -> Optional[UserModel]:
        """Get user by email."""
        return self.session.query(UserModel).filter_by(email=email).first()
    
    def update(self, user_id: str, updates: Dict[str, Any]) -> Optional[UserModel]:
        """Update user."""
        user = self.get_by_id(user_id)
        if user:
            for key, value in updates.items():
                if hasattr(user, key) and key not in ['id', 'user_id', 'created_at']:
                    setattr(user, key, value)
            user.updated_at = datetime.utcnow()
            self.session.commit()
        return user
    
    def delete(self, user_id: str) -> bool:
        """Delete user."""
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
    
    def get_interactions(self, user_id: str, limit: int = 100) -> List[InteractionModel]:
        """Get user interactions."""
        return self.session.query(InteractionModel).join(UserModel).filter(
            UserModel.user_id == user_id
        ).order_by(InteractionModel.timestamp.desc()).limit(limit).all()


class ItemRepository:
    """Repository for item operations."""
    
    def __init__(self, session):
        self.session = session
    
    def create(self, item_data: Dict[str, Any]) -> ItemModel:
        """Create a new item."""
        item = ItemModel(
            item_id=item_data['item_id'],
            name=item_data['name'],
            category=item_data['category'],
            price=item_data['price'],
            description=item_data.get('description', ''),
            tags=item_data.get('tags', []),
            attributes=item_data.get('attributes', {}),
            image_url=item_data.get('image_url')
        )
        self.session.add(item)
        self.session.commit()
        return item
    
    def get_by_id(self, item_id: str) -> Optional[ItemModel]:
        """Get item by ID."""
        return self.session.query(ItemModel).filter_by(item_id=item_id).first()
    
    def get_by_category(self, category: str, limit: int = 50) -> List[ItemModel]:
        """Get items by category."""
        return self.session.query(ItemModel).filter_by(category=category).limit(limit).all()
    
    def search(self, query: str, limit: int = 20) -> List[ItemModel]:
        """Search items by name or description."""
        return self.session.query(ItemModel).filter(
            (ItemModel.name.ilike(f'%{query}%')) |
            (ItemModel.description.ilike(f'%{query}%'))
        ).limit(limit).all()
    
    def update_rating(self, item_id: str, new_rating: float) -> None:
        """Update item average rating."""
        item = self.get_by_id(item_id)
        if item:
            total_rating = item.rating_avg * item.rating_count + new_rating
            item.rating_count += 1
            item.rating_avg = total_rating / item.rating_count
            self.session.commit()


class InteractionRepository:
    """Repository for interaction operations."""
    
    def __init__(self, session):
        self.session = session
    
    def create(self, interaction_data: Dict[str, Any]) -> InteractionModel:
        """Create a new interaction."""
        user = self.session.query(UserModel).filter_by(user_id=interaction_data['user_id']).first()
        item = self.session.query(ItemModel).filter_by(item_id=interaction_data['item_id']).first()
        
        if not user or not item:
            raise ValueError("User or item not found")
        
        interaction = InteractionModel(
            user_id=user.id,
            item_id=item.id,
            interaction_type=interaction_data['interaction_type'],
            value=interaction_data.get('value', 1.0),
            metadata=interaction_data.get('metadata', {})
        )
        self.session.add(interaction)
        self.session.commit()
        return interaction
    
    def get_user_interactions(self, user_id: str) -> List[InteractionModel]:
        """Get all interactions for a user."""
        return self.session.query(InteractionModel).join(UserModel).filter(
            UserModel.user_id == user_id
        ).order_by(InteractionModel.timestamp.desc()).all()
    
    def get_item_interactions(self, item_id: str) -> List[InteractionModel]:
        """Get all interactions for an item."""
        return self.session.query(InteractionModel).join(ItemModel).filter(
            ItemModel.item_id == item_id
        ).all()


# ==================== FLASK API ====================

# app.py - Flask application
"""
Flask API for the recommendation engine.
"""

from flask import Flask, request, jsonify, g
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from datetime import timedelta, datetime
import hashlib
import uuid
import time
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost/recommendation_db')

# Initialize extensions
CORS(app)
jwt = JWTManager(app)

# Database setup
engine = create_engine(app.config['DATABASE_URL'])
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def get_db():
    """Get database session."""
    if 'db' not in g:
        g.db = SessionLocal()
    return g.db


@app.teardown_appcontext
def close_db(error):
    """Close database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


# ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })


@app.route('/api/auth/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    
    # Validate input
    required = ['user_id', 'name', 'email', 'password']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing required fields'}), 400
    
    db = get_db()
    user_repo = UserRepository(db)
    
    # Check if user exists
    if user_repo.get_by_id(data['user_id']) or user_repo.get_by_email(data['email']):
        return jsonify({'error': 'User already exists'}), 409
    
    # Create user
    try:
        user = user_repo.create(data)
        access_token = create_access_token(identity=user.user_id)
        
        return jsonify({
            'success': True,
            'user': {
                'user_id': user.user_id,
                'name': user.name,
                'email': user.email
            },
            'access_token': access_token
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user."""
    data = request.get_json()
    
    if not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400
    
    db = get_db()
    user_repo = UserRepository(db)
    
    user = user_repo.get_by_email(data['email'])
    if not user or not user.verify_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.user_id)
    
    return jsonify({
        'success': True,
        'user': {
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email
        },
        'access_token': access_token
    })


@app.route('/api/items', methods=['GET'])
def get_items():
    """Get items with pagination and filtering."""
    db = get_db()
    item_repo = ItemRepository(db)
    
    # Parse query parameters
    category = request.args.get('category')
    limit = int(request.args.get('limit', 20))
    offset = int(request.args.get('offset', 0))
    
    query = db.query(ItemModel)
    
    if category:
        query = query.filter_by(category=category)
    
    items = query.filter_by(is_available=True).offset(offset).limit(limit).all()
    
    return jsonify({
        'success': True,
        'items': [{
            'item_id': item.item_id,
            'name': item.name,
            'category': item.category,
            'price': item.price,
            'description': item.description,
            'tags': item.tags,
            'rating_avg': item.rating_avg,
            'image_url': item.image_url
        } for item in items],
        'count': len(items)
    })


@app.route('/api/items/<item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item."""
    db = get_db()
    item_repo = ItemRepository(db)
    
    item = item_repo.get_by_id(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    return jsonify({
        'success': True,
        'item': {
            'item_id': item.item_id,
            'name': item.name,
            'category': item.category,
            'price': item.price,
            'description': item.description,
            'tags': item.tags,
            'attributes': item.attributes,
            'rating_avg': item.rating_avg,
            'rating_count': item.rating_count,
            'image_url': item.image_url
        }
    })


@app.route('/api/interactions', methods=['POST'])
@jwt_required()
def track_interaction():
    """Track user-item interaction."""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data.get('item_id') or not data.get('interaction_type'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    db = get_db()
    interaction_repo = InteractionRepository(db)
    
    interaction_data = {
        'user_id': user_id,
        'item_id': data['item_id'],
        'interaction_type': data['interaction_type'],
        'value': data.get('value', 1.0),
        'metadata': data.get('metadata', {})
    }
    
    try:
        interaction = interaction_repo.create(interaction_data)
        
        # If rating, update item rating
        if data['interaction_type'] == 'rating' and data.get('value'):
            item_repo = ItemRepository(db)
            item_repo.update_rating(data['item_id'], data['value'])
        
        return jsonify({'success': True, 'interaction_id': str(interaction.id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/recommendations', methods=['GET'])
@jwt_required()
def get_recommendations():
    """Get personalized recommendations."""
    user_id = get_jwt_identity()
    n = int(request.args.get('n', 10))
    strategy = request.args.get('strategy', 'hybrid')
    
    # Track request for analytics
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    db = get_db()
    
    # Get user interactions
    interaction_repo = InteractionRepository(db)
    interactions = interaction_repo.get_user_interactions(user_id)
    
    # Get recommendation engine instance
    recommender = get_recommendation_engine()
    
    # Generate recommendations
    try:
        recommendations = recommender.recommend_for_user(user_id, n)
        
        # Log recommendation
        response_time = (time.time() - start_time) * 1000
        log_recommendation(user_id, [r.item_id for r in recommendations], 
                          strategy, request_id, response_time)
        
        # Get item details
        item_repo = ItemRepository(db)
        items = []
        for rec in recommendations:
            item = item_repo.get_by_id(rec.item_id)
            if item:
                items.append({
                    'item_id': rec.item_id,
                    'name': item.name,
                    'category': item.category,
                    'price': item.price,
                    'score': rec.score,
                    'reason': rec.reason,
                    'image_url': item.image_url
                })
        
        return jsonify({
            'success': True,
            'recommendations': items,
            'request_id': request_id,
            'algorithm': strategy
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/recommendations/similar/<item_id>', methods=['GET'])
def get_similar_items(item_id):
    """Get items similar to a given item."""
    n = int(request.args.get('n', 10))
    
    recommender = get_recommendation_engine()
    
    try:
        similar = recommender.get_similar_items(item_id, n)
        
        db = get_db()
        item_repo = ItemRepository(db)
        
        items = []
        for sim in similar:
            item = item_repo.get_by_id(sim.item_id)
            if item:
                items.append({
                    'item_id': sim.item_id,
                    'name': item.name,
                    'category': item.category,
                    'price': item.price,
                    'similarity': sim.score,
                    'image_url': item.image_url
                })
        
        return jsonify({
            'success': True,
            'similar_items': items
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/feedback', methods=['POST'])
@jwt_required()
def submit_feedback():
    """Submit feedback on recommendations."""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data.get('item_id') or not data.get('feedback_type'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    db = get_db()
    
    # Store feedback
    feedback = UserFeedbackModel(
        user_id=user_id,
        item_id=data['item_id'],
        feedback_type=data['feedback_type'],
        rating=data.get('rating')
    )
    db.add(feedback)
    db.commit()
    
    # If positive feedback, create interaction
    if data['feedback_type'] == 'like':
        interaction_repo = InteractionRepository(db)
        interaction_repo.create({
            'user_id': user_id,
            'item_id': data['item_id'],
            'interaction_type': 'click',
            'value': 2.0
        })
    
    return jsonify({'success': True})


# ==================== RECOMMENDATION ENGINE INTEGRATION ====================

_recommendation_engine = None


def get_recommendation_engine():
    """Get or create recommendation engine instance."""
    global _recommendation_engine
    
    if _recommendation_engine is None:
        from recommendation_engine import RecommendationEngine
        _recommendation_engine = RecommendationEngine()
        
        # Load data from database
        db = get_db()
        users = db.query(UserModel).filter_by(is_active=True).all()
        items = db.query(ItemModel).filter_by(is_available=True).all()
        interactions = db.query(InteractionModel).all()
        
        # Convert to domain models
        domain_users = [UserModel.to_domain(u) for u in users]
        domain_items = [ItemModel.to_domain(i) for i in items]
        domain_interactions = [InteractionModel.to_domain(i) for i in interactions]
        
        _recommendation_engine.load_data(domain_interactions, domain_items, domain_users)
        _recommendation_engine.build_recommender(strategy="hybrid")
    
    return _recommendation_engine


def log_recommendation(user_id: str, item_ids: List[str], algorithm: str, 
                       request_id: str, response_time: float):
    """Log recommendation for analytics."""
    db = get_db()
    log = RecommendationLogModel(
        user_id=user_id,
        item_ids=item_ids,
        algorithm=algorithm,
        request_id=request_id,
        response_time_ms=response_time
    )
    db.add(log)
    db.commit()


def demonstrate_api():
    """
    Demonstrate the API functionality.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: DATABASE & API LAYER")
    print("=" * 60)
    
    print("\n1. API ENDPOINTS")
    print("-" * 40)
    
    endpoints = [
        ("POST", "/api/auth/register", "User registration"),
        ("POST", "/api/auth/login", "User login"),
        ("GET", "/api/items", "List items"),
        ("GET", "/api/items/<id>", "Get item details"),
        ("POST", "/api/interactions", "Track interaction"),
        ("GET", "/api/recommendations", "Get recommendations"),
        ("GET", "/api/recommendations/similar/<id>", "Get similar items"),
        ("POST", "/api/feedback", "Submit feedback"),
        ("GET", "/api/health", "Health check")
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:6} {path:35} - {description}")
    
    print("\n2. DATABASE MODELS")
    print("-" * 40)
    
    models = [
        "UserModel - User accounts and profiles",
        "ItemModel - Product catalog",
        "InteractionModel - User-item interactions",
        "RecommendationCacheModel - Cached recommendations",
        "UserFeedbackModel - Feedback on recommendations",
        "RecommendationLogModel - Analytics logs"
    ]
    
    for model in models:
        print(f"  • {model}")
    
    print("\n3. API REQUEST EXAMPLES")
    print("-" * 40)
    
    examples = [
        "# Register user",
        """curl -X POST http://localhost:5000/api/auth/register \\
  -H "Content-Type: application/json" \\
  -d '{"user_id":"john","name":"John Doe","email":"john@example.com","password":"secret"}'""",
        "",
        "# Login",
        """curl -X POST http://localhost:5000/api/auth/login \\
  -H "Content-Type: application/json" \\
  -d '{"email":"john@example.com","password":"secret"}'""",
        "",
        "# Get recommendations",
        """curl http://localhost:5000/api/recommendations?n=10 \\
  -H "Authorization: Bearer <token>" """
    ]
    
    for example in examples:
        if example:
            print(f"  {example}")
        else:
            print()
    
    print("\n✅ API ready! Run with: python app.py")


if __name__ == "__main__":
    demonstrate_api()
    
    # Run Flask app if executed directly
    if os.getenv('RUN_API', 'False').lower() == 'true':
        app.run(host='0.0.0.0', port=5000, debug=False)
```

---

## 🎨 Section 3: React Frontend Application

Build a modern React frontend for the recommendation engine.

**SOLID Principles Applied:**
- Single Responsibility: Each component handles one UI concern
- Dependency Inversion: Components depend on service abstractions

**Design Patterns:**
- Component Pattern: Reusable UI components
- Observer Pattern: State management with React hooks

```jsx
// frontend/src/App.js
/**
 * React frontend for recommendation engine.
 * 
 * Design Pattern: Component Pattern - Reusable UI components
 * SOLID Principle: Single Responsibility - Each component has one purpose
 */

import React, { useState, useEffect, createContext, useContext } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  Link,
  useNavigate,
  useParams
} from 'react-router-dom';
import axios from 'axios';
import './App.css';

// ==================== API SERVICE ====================

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' }
});

// Add token to requests
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token expiration
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// ==================== AUTH CONTEXT ====================

const AuthContext = createContext(null);

const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    const savedUser = localStorage.getItem('user');
    if (token && savedUser) {
      setUser(JSON.parse(savedUser));
    }
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    const response = await api.post('/auth/login', { email, password });
    if (response.data.success) {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      setUser(response.data.user);
      return true;
    }
    return false;
  };

  const register = async (userData) => {
    const response = await api.post('/auth/register', userData);
    if (response.data.success) {
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      setUser(response.data.user);
      return true;
    }
    return false;
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// ==================== COMPONENTS ====================

// Navigation Bar
const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-brand">
          <i className="fas fa-brain"></i>
          <span>Rec<span className="highlight">Engine</span></span>
        </Link>
        
        <div className="nav-links">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/recommendations" className="nav-link">Recommendations</Link>
          <Link to="/browse" className="nav-link">Browse</Link>
        </div>
        
        <div className="nav-user">
          {user ? (
            <>
              <span className="user-name">
                <i className="fas fa-user-circle"></i>
                {user.name}
              </span>
              <button onClick={handleLogout} className="btn-logout">
                <i className="fas fa-sign-out-alt"></i>
              </button>
            </>
          ) : (
            <Link to="/login" className="btn-login">Login</Link>
          )}
        </div>
      </div>
    </nav>
  );
};

// Hero Section
const Hero = () => {
  return (
    <div className="hero">
      <div className="hero-content">
        <h1 className="hero-title">
          Discover Products You'll Love
        </h1>
        <p className="hero-subtitle">
          Personalized recommendations powered by machine learning
        </p>
        <Link to="/register" className="hero-cta">
          Get Started <i className="fas fa-arrow-right"></i>
        </Link>
      </div>
      <div className="hero-stats">
        <div className="stat">
          <span className="stat-number">10K+</span>
          <span className="stat-label">Products</span>
        </div>
        <div className="stat">
          <span className="stat-number">50K+</span>
          <span className="stat-label">Users</span>
        </div>
        <div className="stat">
          <span className="stat-number">1M+</span>
          <span className="stat-label">Interactions</span>
        </div>
      </div>
    </div>
  );
};

// Product Card Component
const ProductCard = ({ product, onLike, onView }) => {
  const [liked, setLiked] = useState(false);

  const handleLike = async () => {
    setLiked(!liked);
    if (onLike) {
      await onLike(product.item_id);
    }
  };

  return (
    <div className="product-card" onClick={() => onView?.(product.item_id)}>
      <div className="product-image">
        {product.image_url ? (
          <img src={product.image_url} alt={product.name} />
        ) : (
          <div className="image-placeholder">
            <i className="fas fa-box"></i>
          </div>
        )}
        <button 
          className={`like-btn ${liked ? 'liked' : ''}`}
          onClick={(e) => {
            e.stopPropagation();
            handleLike();
          }}
        >
          <i className={`fas fa-heart ${liked ? 'liked' : ''}`}></i>
        </button>
      </div>
      
      <div className="product-info">
        <h3 className="product-title">{product.name}</h3>
        <span className="product-category">{product.category}</span>
        <div className="product-rating">
          <i className="fas fa-star"></i>
          <span>{product.rating_avg?.toFixed(1) || 'New'}</span>
        </div>
        <div className="product-price">${product.price.toFixed(2)}</div>
        {product.reason && (
          <div className="product-reason">
            <i className="fas fa-magic"></i>
            <span>{product.reason}</span>
          </div>
        )}
      </div>
    </div>
  );
};

// Recommendation Section
const RecommendationsSection = ({ title, items, loading }) => {
  const navigate = useNavigate();
  const { user } = useAuth();

  const handleLike = async (itemId) => {
    if (!user) return;
    try {
      await api.post('/feedback', {
        item_id: itemId,
        feedback_type: 'like'
      });
    } catch (error) {
      console.error('Failed to submit feedback:', error);
    }
  };

  const handleView = (itemId) => {
    navigate(`/product/${itemId}`);
  };

  if (loading) {
    return (
      <div className="recommendations-section">
        <h2 className="section-title">{title}</h2>
        <div className="products-grid loading">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="skeleton-card"></div>
          ))}
        </div>
      </div>
    );
  }

  if (!items || items.length === 0) {
    return null;
  }

  return (
    <div className="recommendations-section">
      <h2 className="section-title">{title}</h2>
      <div className="products-grid">
        {items.map(product => (
          <ProductCard
            key={product.item_id}
            product={product}
            onLike={handleLike}
            onView={handleView}
          />
        ))}
      </div>
    </div>
  );
};

// Home Page
const HomePage = () => {
  const { user } = useAuth();
  const [popularItems, setPopularItems] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, [user]);

  const loadData = async () => {
    setLoading(true);
    try {
      // Load popular items
      const popularResponse = await api.get('/items?limit=12');
      setPopularItems(popularResponse.data.items);

      // Load recommendations if logged in
      if (user) {
        const recResponse = await api.get('/recommendations?n=12');
        setRecommendations(recResponse.data.recommendations);
      }
    } catch (error) {
      console.error('Failed to load data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="home-page">
      <Hero />
      
      <div className="container">
        {user && recommendations.length > 0 && (
          <RecommendationsSection
            title="Recommended for You"
            items={recommendations}
            loading={loading}
          />
        )}
        
        <RecommendationsSection
          title="Popular Products"
          items={popularItems}
          loading={loading}
        />
      </div>
    </div>
  );
};

// Browse Page
const BrowsePage = () => {
  const [items, setItems] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    loadCategories();
    loadItems();
  }, [selectedCategory, page]);

  const loadCategories = async () => {
    try {
      const response = await api.get('/items/categories');
      setCategories(response.data.categories || []);
    } catch (error) {
      console.error('Failed to load categories:', error);
    }
  };

  const loadItems = async () => {
    setLoading(true);
    try {
      const url = selectedCategory
        ? `/items?category=${selectedCategory}&limit=12&offset=${(page-1)*12}`
        : `/items?limit=12&offset=${(page-1)*12}`;
      
      const response = await api.get(url);
      
      if (page === 1) {
        setItems(response.data.items);
      } else {
        setItems([...items, ...response.data.items]);
      }
      
      setHasMore(response.data.items.length === 12);
    } catch (error) {
      console.error('Failed to load items:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setPage(1);
  };

  const loadMore = () => {
    if (!loading && hasMore) {
      setPage(page + 1);
    }
  };

  return (
    <div className="browse-page">
      <div className="container">
        <div className="browse-header">
          <h1>Browse Products</h1>
          <div className="category-filters">
            <button
              className={`category-btn ${!selectedCategory ? 'active' : ''}`}
              onClick={() => handleCategoryChange('')}
            >
              All
            </button>
            {categories.map(cat => (
              <button
                key={cat}
                className={`category-btn ${selectedCategory === cat ? 'active' : ''}`}
                onClick={() => handleCategoryChange(cat)}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>
        
        <div className="products-grid">
          {items.map(item => (
            <ProductCard key={item.item_id} product={item} />
          ))}
        </div>
        
        {hasMore && (
          <div className="load-more">
            <button onClick={loadMore} disabled={loading}>
              {loading ? 'Loading...' : 'Load More'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

// Product Detail Page
const ProductDetailPage = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [similarItems, setSimilarItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    loadProduct();
  }, [id]);

  const loadProduct = async () => {
    setLoading(true);
    try {
      const [productRes, similarRes] = await Promise.all([
        api.get(`/items/${id}`),
        api.get(`/recommendations/similar/${id}?n=8`)
      ]);
      
      setProduct(productRes.data.item);
      setSimilarItems(similarRes.data.similar_items);
    } catch (error) {
      console.error('Failed to load product:', error);
    } finally {
      setLoading(false);
    }
  };

  const trackInteraction = async (type, value = 1) => {
    try {
      await api.post('/interactions', {
        item_id: id,
        interaction_type: type,
        value: value
      });
    } catch (error) {
      console.error('Failed to track interaction:', error);
    }
  };

  if (loading) {
    return (
      <div className="container">
        <div className="loading-state">Loading...</div>
      </div>
    );
  }

  if (!product) {
    return (
      <div className="container">
        <div className="error-state">Product not found</div>
      </div>
    );
  }

  return (
    <div className="product-detail-page">
      <div className="container">
        <button className="back-btn" onClick={() => navigate(-1)}>
          <i className="fas fa-arrow-left"></i> Back
        </button>
        
        <div className="product-detail">
          <div className="product-detail-image">
            {product.image_url ? (
              <img src={product.image_url} alt={product.name} />
            ) : (
              <div className="image-placeholder large">
                <i className="fas fa-box fa-4x"></i>
              </div>
            )}
          </div>
          
          <div className="product-detail-info">
            <h1>{product.name}</h1>
            <span className="category">{product.category}</span>
            <div className="rating">
              <i className="fas fa-star"></i>
              <span>{product.rating_avg?.toFixed(1) || 'No ratings'}</span>
              <span className="rating-count">({product.rating_count || 0} reviews)</span>
            </div>
            <div className="price">${product.price.toFixed(2)}</div>
            <p className="description">{product.description}</p>
            <div className="tags">
              {product.tags?.map(tag => (
                <span key={tag} className="tag">{tag}</span>
              ))}
            </div>
            <div className="actions">
              <button 
                className="btn-primary"
                onClick={() => trackInteraction('purchase', 5)}
              >
                <i className="fas fa-shopping-cart"></i> Add to Cart
              </button>
              <button 
                className="btn-secondary"
                onClick={() => trackInteraction('click', 2)}
              >
                <i className="fas fa-heart"></i> Save
              </button>
            </div>
          </div>
        </div>
        
        {similarItems.length > 0 && (
          <RecommendationsSection
            title="You May Also Like"
            items={similarItems}
            loading={false}
          />
        )}
      </div>
    </div>
  );
};

// Login Page
const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    const success = await login(email, password);
    if (success) {
      navigate('/');
    } else {
      setError('Invalid email or password');
    }
    setLoading(false);
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <h2>Welcome Back</h2>
        <p>Sign in to get personalized recommendations</p>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              placeholder="your@email.com"
            />
          </div>
          
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="••••••••"
            />
          </div>
          
          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Signing in...' : 'Sign In'}
          </button>
        </form>
        
        <p className="auth-link">
          Don't have an account? <Link to="/register">Sign up</Link>
        </p>
      </div>
    </div>
  );
};

// Register Page
const RegisterPage = () => {
  const [formData, setFormData] = useState({
    user_id: '',
    name: '',
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    const success = await register(formData);
    if (success) {
      navigate('/');
    } else {
      setError('Registration failed. User may already exist.');
    }
    setLoading(false);
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <h2>Create Account</h2>
        <p>Join thousands of users discovering products they love</p>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Username</label>
            <input
              type="text"
              name="user_id"
              value={formData.user_id}
              onChange={handleChange}
              required
              placeholder="Choose a username"
            />
          </div>
          
          <div className="form-group">
            <label>Full Name</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              placeholder="Your name"
            />
          </div>
          
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              placeholder="your@email.com"
            />
          </div>
          
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              placeholder="••••••••"
            />
          </div>
          
          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Creating account...' : 'Sign Up'}
          </button>
        </form>
        
        <p className="auth-link">
          Already have an account? <Link to="/login">Sign in</Link>
        </p>
      </div>
    </div>
  );
};

// Protected Route Component
const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();
  
  if (loading) {
    return <div className="loading-state">Loading...</div>;
  }
  
  if (!user) {
    return <Navigate to="/login" />;
  }
  
  return children;
};

// Main App Component
const App = () => {
  return (
    <AuthProvider>
      <Router>
        <div className="app">
          <Navbar />
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/browse" element={<BrowsePage />} />
            <Route path="/product/:id" element={<ProductDetailPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route 
              path="/recommendations" 
              element={
                <ProtectedRoute>
                  <RecommendationsPage />
                </ProtectedRoute>
              } 
            />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
};

// Recommendations Page (protected)
const RecommendationsPage = () => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadRecommendations();
  }, []);

  const loadRecommendations = async () => {
    setLoading(true);
    try {
      const response = await api.get('/recommendations?n=20');
      setRecommendations(response.data.recommendations);
    } catch (error) {
      console.error('Failed to load recommendations:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="recommendations-page">
      <div className="container">
        <h1 className="page-title">Your Personalized Recommendations</h1>
        <p className="page-subtitle">
          Based on your browsing history and preferences
        </p>
        
        <RecommendationsSection
          title=""
          items={recommendations}
          loading={loading}
        />
      </div>
    </div>
  );
};

export default App;
```

```css
/* frontend/src/App.css */
/* Modern CSS for the recommendation engine frontend */

:root {
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --secondary: #ec4899;
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  --dark: #1f2937;
  --gray: #6b7280;
  --light: #f3f4f6;
  --white: #ffffff;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
  
  --radius: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: var(--dark);
  line-height: 1.5;
}

.app {
  min-height: 100vh;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* Navigation */
.navbar {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  box-shadow: var(--shadow-md);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 1rem 0;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand {
  font-size: 1.5rem;
  font-weight: 700;
  text-decoration: none;
  color: var(--primary);
}

.nav-brand .highlight {
  color: var(--secondary);
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  text-decoration: none;
  color: var(--gray);
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: var(--primary);
}

.nav-user {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-name {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--dark);
}

.btn-logout, .btn-login {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: var(--radius);
  transition: background 0.3s ease;
}

.btn-logout {
  color: var(--danger);
}

.btn-login {
  background: var(--primary);
  color: white;
  padding: 0.5rem 1rem;
  text-decoration: none;
}

/* Hero Section */
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero-content {
  max-width: 600px;
  margin: 0 auto;
}

.hero-title {
  font-size: 3rem;
  margin-bottom: 1rem;
  animation: fadeInUp 0.6s ease;
}

.hero-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
  margin-bottom: 2rem;
  animation: fadeInUp 0.6s ease 0.1s both;
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  color: var(--primary);
  padding: 1rem 2rem;
  border-radius: var(--radius-xl);
  text-decoration: none;
  font-weight: 600;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  animation: fadeInUp 0.6s ease 0.2s both;
}

.hero-cta:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-xl);
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 4rem;
  margin-top: 3rem;
  animation: fadeInUp 0.6s ease 0.3s both;
}

.stat {
  display: flex;
  flex-direction: column;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.8;
}

/* Section Title */
.section-title {
  font-size: 1.8rem;
  margin: 2rem 0;
  color: white;
  text-align: center;
}

/* Products Grid */
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

/* Product Card */
.product-card {
  background: white;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
}

.product-image {
  position: relative;
  height: 200px;
  background: var(--light);
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  color: var(--gray);
}

.like-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: white;
  border: none;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.3s ease;
  box-shadow: var(--shadow-md);
}

.like-btn:hover {
  transform: scale(1.1);
}

.like-btn .liked {
  color: var(--danger);
}

.product-info {
  padding: 1rem;
}

.product-title {
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: var(--dark);
}

.product-category {
  font-size: 0.8rem;
  color: var(--gray);
  text-transform: capitalize;
}

.product-rating {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin: 0.5rem 0;
  color: var(--warning);
}

.product-price {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--primary);
  margin-top: 0.5rem;
}

.product-reason {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  font-size: 0.8rem;
  color: var(--gray);
  background: var(--light);
  padding: 0.5rem;
  border-radius: var(--radius);
}

/* Skeleton Loading */
.skeleton-card {
  background: linear-gradient(90deg, var(--light) 25%, #e5e7eb 50%, var(--light) 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  height: 300px;
  border-radius: var(--radius-lg);
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Product Detail */
.product-detail {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin: 2rem 0;
}

.product-detail-image {
  background: var(--light);
  border-radius: var(--radius-lg);
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-detail-image img {
  width: 100%;
  height: auto;
  border-radius: var(--radius-lg);
}

.image-placeholder.large {
  font-size: 6rem;
}

.product-detail-info h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.product-detail-info .category {
  display: inline-block;
  background: var(--light);
  padding: 0.25rem 0.75rem;
  border-radius: var(--radius);
  font-size: 0.8rem;
  margin-bottom: 1rem;
}

.product-detail-info .rating {
  margin: 1rem 0;
}

.product-detail-info .price {
  font-size: 2rem;
  font-weight: 700;
  color: var(--primary);
  margin: 1rem 0;
}

.product-detail-info .description {
  color: var(--gray);
  margin: 1rem 0;
  line-height: 1.6;
}

.tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin: 1rem 0;
}

.tag {
  background: var(--light);
  padding: 0.25rem 0.75rem;
  border-radius: var(--radius);
  font-size: 0.8rem;
}

.actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn-primary, .btn-secondary {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.3s ease, background 0.3s ease;
}

.btn-primary {
  background: var(--primary);
  color: white;
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-2px);
}

.btn-secondary {
  background: var(--light);
  color: var(--dark);
}

.btn-secondary:hover {
  background: #e5e7eb;
  transform: translateY(-2px);
}

/* Auth Pages */
.auth-page {
  min-height: calc(100vh - 70px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.auth-card {
  background: white;
  border-radius: var(--radius-xl);
  padding: 2rem;
  max-width: 400px;
  width: 100%;
  box-shadow: var(--shadow-xl);
}

.auth-card h2 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  color: var(--dark);
}

.auth-card p {
  color: var(--gray);
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--light);
  border-radius: var(--radius);
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: var(--primary);
}

.error-message {
  background: #fee;
  color: var(--danger);
  padding: 0.75rem;
  border-radius: var(--radius);
  margin-bottom: 1rem;
  text-align: center;
}

.auth-link {
  text-align: center;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.auth-link a {
  color: var(--primary);
  text-decoration: none;
}

/* Category Filters */
.category-filters {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin: 1rem 0;
}

.category-btn {
  padding: 0.5rem 1rem;
  background: white;
  border: 1px solid var(--light);
  border-radius: var(--radius);
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-btn:hover {
  background: var(--light);
}

.category-btn.active {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

/* Load More */
.load-more {
  text-align: center;
  margin: 2rem 0;
}

.load-more button {
  padding: 0.75rem 2rem;
  background: white;
  border: none;
  border-radius: var(--radius);
  cursor: pointer;
  font-weight: 600;
  transition: transform 0.3s ease;
}

.load-more button:hover:not(:disabled) {
  transform: translateY(-2px);
}

.load-more button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Back Button */
.back-btn {
  background: none;
  border: none;
  color: var(--primary);
  cursor: pointer;
  padding: 0.5rem 0;
  margin-bottom: 1rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
}

/* Loading State */
.loading-state {
  text-align: center;
  padding: 3rem;
  color: white;
  font-size: 1.2rem;
}

/* Error State */
.error-state {
  text-align: center;
  padding: 3rem;
  color: var(--danger);
  background: white;
  border-radius: var(--radius-lg);
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-container {
    flex-direction: column;
    gap: 1rem;
  }
  
  .hero-title {
    font-size: 2rem;
  }
  
  .hero-stats {
    gap: 2rem;
  }
  
  .product-detail {
    grid-template-columns: 1fr;
  }
  
  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 1rem;
  }
  
  .hero-stats {
    flex-direction: column;
    gap: 1rem;
  }
  
  .category-filters {
    overflow-x: auto;
    flex-wrap: nowrap;
  }
}
```

---

## 🐳 Section 4: Production Deployment

Complete deployment configuration with Docker, Kubernetes, and monitoring.

**SOLID Principles Applied:**
- Single Responsibility: Each service has one purpose
- Dependency Inversion: Services depend on environment variables

**Design Patterns:**
- Container Pattern: Docker containers for isolation
- Orchestration Pattern: Kubernetes for management

```yaml
# docker-compose.yml
"""
Production Docker Compose configuration.
"""

version: '3.8'

services:
  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    container_name: rec-postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: recommendation_db
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    networks:
      - rec-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d recommendation_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: rec-redis
    restart: unless-stopped
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data
    ports:
      - "6379:6379"
    networks:
      - rec-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: rec-backend
    restart: unless-stopped
    environment:
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/recommendation_db
      REDIS_URL: redis://:${REDIS_PASSWORD}@redis:6379/0
      OPENWEATHER_API_KEY: ${OPENWEATHER_API_KEY}
      FLASK_SECRET_KEY: ${FLASK_SECRET_KEY}
      JWT_SECRET_KEY: ${JWT_SECRET_KEY}
      FLASK_ENV: production
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./backend/logs:/app/logs
      - ./backend/models:/app/models
    networks:
      - rec-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: rec-frontend
    restart: unless-stopped
    environment:
      REACT_APP_API_URL: http://backend:5000/api
    depends_on:
      - backend
    networks:
      - rec-network

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: rec-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - frontend
      - backend
    networks:
      - rec-network

  # MLflow for Model Tracking
  mlflow:
    image: ghcr.io/mlflow/mlflow:latest
    container_name: rec-mlflow
    restart: unless-stopped
    environment:
      MLFLOW_TRACKING_URI: postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/mlflow_db
    command: mlflow server --host 0.0.0.0 --port 5001 --backend-store-uri postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/mlflow_db --default-artifact-root ./mlflow-artifacts
    volumes:
      - mlflow-data:/mlflow
    ports:
      - "5001:5001"
    depends_on:
      - postgres
    networks:
      - rec-network

  # Prometheus Monitoring
  prometheus:
    image: prom/prometheus:latest
    container_name: rec-prometheus
    restart: unless-stopped
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    ports:
      - "9090:9090"
    networks:
      - rec-network

  # Grafana Dashboards
  grafana:
    image: grafana/grafana:latest
    container_name: rec-grafana
    restart: unless-stopped
    environment:
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_PASSWORD}
      GF_INSTALL_PLUGINS: grafana-piechart-panel
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana-dashboards:/etc/grafana/provisioning/dashboards
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
    networks:
      - rec-network

networks:
  rec-network:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
  mlflow-data:
  prometheus-data:
  grafana-data:
```

```dockerfile
# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--worker-class", "sync", "--timeout", "120", "app:app"]
```

```dockerfile
# frontend/Dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

```yaml
# kubernetes/deployment.yaml
"""
Kubernetes deployment configuration.
"""

apiVersion: v1
kind: Namespace
metadata:
  name: recommendation-system

---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: recommendation-system
type: Opaque
data:
  db-password: <base64-encoded-password>
  redis-password: <base64-encoded-password>
  flask-secret: <base64-encoded-secret>

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: recommendation-system
data:
  db-name: recommendation_db
  db-user: postgres
  redis-host: redis-service
  redis-port: "6379"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  namespace: recommendation-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_DB
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db-name
        - name: POSTGRES_USER
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db-user
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db-password
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: postgres-storage
        persistentVolumeClaim:
          claimName: postgres-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: postgres-service
  namespace: recommendation-system
spec:
  selector:
    app: postgres
  ports:
  - port: 5432
    targetPort: 5432

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: recommendation-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
        command: ["redis-server"]
        args: ["--requirepass", "$(REDIS_PASSWORD)"]
        env:
        - name: REDIS_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: redis-password

---
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: recommendation-system
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: recommendation-system
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: recommendation-backend:latest
        ports:
        - containerPort: 5000
        env:
        - name: DATABASE_URL
          value: "postgresql://$(DB_USER):$(DB_PASSWORD)@postgres-service:5432/$(DB_NAME)"
        - name: REDIS_URL
          value: "redis://:$(REDIS_PASSWORD)@redis-service:6379/0"
        - name: FLASK_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: flask-secret
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /api/health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /api/health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5

---
apiVersion: v1
kind: Service
metadata:
  name: backend-service
  namespace: recommendation-system
spec:
  selector:
    app: backend
  ports:
  - port: 5000
    targetPort: 5000
  type: ClusterIP

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: recommendation-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: recommendation-frontend:latest
        ports:
        - containerPort: 80
        env:
        - name: REACT_APP_API_URL
          value: "http://backend-service:5000/api"

---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
  namespace: recommendation-system
spec:
  selector:
    app: frontend
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-hpa
  namespace: recommendation-system
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

```python
# deploy.py
"""
Production deployment script.
"""

import os
import subprocess
import sys
from pathlib import Path
import argparse
import time
import requests


class ProductionDeployer:
    """
    Manages production deployment.
    
    Design Pattern: Facade Pattern - Simplifies deployment complexity
    """
    
    def __init__(self, environment='production'):
        self.environment = environment
        self.project_root = Path(__file__).parent
        
    def check_prerequisites(self):
        """Check all prerequisites."""
        print("Checking prerequisites...")
        
        # Check Docker
        try:
            subprocess.run(['docker', '--version'], check=True, capture_output=True)
            print("✓ Docker installed")
        except:
            print("✗ Docker not found")
            return False
        
        # Check kubectl for Kubernetes
        if self.environment == 'kubernetes':
            try:
                subprocess.run(['kubectl', 'version', '--client'], check=True, capture_output=True)
                print("✓ kubectl installed")
            except:
                print("✗ kubectl not found")
                return False
        
        # Check environment file
        env_file = self.project_root / '.env'
        if not env_file.exists():
            print("✗ .env file not found")
            return False
        
        print("✓ Environment file found")
        return True
    
    def deploy_docker_compose(self):
        """Deploy with Docker Compose."""
        print("\nDeploying with Docker Compose...")
        
        # Build and start services
        subprocess.run(['docker-compose', 'up', '-d', '--build'], cwd=self.project_root)
        
        # Wait for services
        time.sleep(10)
        
        # Check health
        return self.check_health()
    
    def deploy_kubernetes(self):
        """Deploy to Kubernetes."""
        print("\nDeploying to Kubernetes...")
        
        # Apply secrets and configs
        subprocess.run(['kubectl', 'apply', '-f', 'kubernetes/secrets.yaml'])
        subprocess.run(['kubectl', 'apply', '-f', 'kubernetes/configmap.yaml'])
        
        # Apply deployments
        subprocess.run(['kubectl', 'apply', '-f', 'kubernetes/deployment.yaml'])
        subprocess.run(['kubectl', 'apply', '-f', 'kubernetes/service.yaml'])
        
        # Wait for pods
        subprocess.run(['kubectl', 'wait', '--for=condition=ready', 'pod', '--all', '--timeout=300s'])
        
        return True
    
    def check_health(self):
        """Check service health."""
        print("\nChecking service health...")
        
        endpoints = [
            ('http://localhost:5000/api/health', 'Backend'),
            ('http://localhost:3000', 'Grafana'),
            ('http://localhost:9090', 'Prometheus')
        ]
        
        all_healthy = True
        for url, name in endpoints:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"✓ {name} is healthy")
                else:
                    print(f"✗ {name} returned {response.status_code}")
                    all_healthy = False
            except:
                print(f"✗ {name} is not responding")
                all_healthy = False
        
        return all_healthy
    
    def run_migrations(self):
        """Run database migrations."""
        print("\nRunning database migrations...")
        subprocess.run(['docker-compose', 'exec', 'backend', 'python', 'migrate.py'], cwd=self.project_root)
    
    def backup_database(self):
        """Backup database."""
        print("\nBacking up database...")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_{timestamp}.sql"
        subprocess.run([
            'docker-compose', 'exec', '-T', 'postgres', 
            'pg_dump', '-U', 'postgres', 'recommendation_db'
        ], stdout=open(backup_file, 'w'), cwd=self.project_root)
        print(f"✓ Backup saved to {backup_file}")
    
    def deploy(self):
        """Main deployment function."""
        print("=" * 60)
        print("RECOMMENDATION ENGINE DEPLOYMENT")
        print("=" * 60)
        
        if not self.check_prerequisites():
            return False
        
        if self.environment == 'production':
            success = self.deploy_docker_compose()
        elif self.environment == 'kubernetes':
            success = self.deploy_kubernetes()
        else:
            print(f"Unknown environment: {self.environment}")
            return False
        
        if success:
            self.run_migrations()
            
            print("\n" + "=" * 60)
            print("✅ DEPLOYMENT SUCCESSFUL!")
            print("=" * 60)
            print("\nAccess your application:")
            print("  • Frontend: http://localhost")
            print("  • API Docs: http://localhost:5000/api/docs")
            print("  • Grafana: http://localhost:3000 (admin/admin)")
            print("  • Prometheus: http://localhost:9090")
            print("  • MLflow: http://localhost:5001")
            return True
        
        return False


def main():
    parser = argparse.ArgumentParser(description='Deploy Recommendation Engine')
    parser.add_argument('--env', choices=['production', 'kubernetes'], default='production')
    parser.add_argument('--action', choices=['deploy', 'backup', 'stop'], default='deploy')
    
    args = parser.parse_args()
    
    deployer = ProductionDeployer(args.env)
    
    if args.action == 'deploy':
        deployer.deploy()
    elif args.action == 'backup':
        deployer.backup_database()
    elif args.action == 'stop':
        subprocess.run(['docker-compose', 'down'], cwd=deployer.project_root)
        print("Services stopped")


if __name__ == '__main__':
    main()
```

---

## 📊 Final Takeaway

**What You Built:**

- **Complete Recommendation Engine** – Collaborative filtering, content-based, and hybrid approaches
- **Production ML System** – Model training, evaluation, and deployment pipeline
- **Full-Stack Application** – React frontend + Flask API + PostgreSQL + Redis
- **Container Orchestration** – Docker Compose and Kubernetes configurations
- **Monitoring Stack** – Prometheus metrics and Grafana dashboards
- **MLOps Infrastructure** – MLflow for experiment tracking and model registry

**SOLID Principles Applied Throughout:**
- **Single Responsibility** – Every class and module has one clear purpose
- **Open/Closed** – New recommendation algorithms can be added without modifying existing code
- **Liskov Substitution** – All recommendation algorithms follow the same interface
- **Interface Segregation** – Small, focused interfaces for each component
- **Dependency Inversion** – High-level modules depend on abstractions, not concrete implementations

**Design Patterns Used Across the Metromap:**
- Factory Pattern, Strategy Pattern, Singleton Pattern, Observer Pattern
- Repository Pattern, Facade Pattern, Adapter Pattern, Proxy Pattern
- Command Pattern, Template Method Pattern, Builder Pattern, Value Object Pattern
- Container Pattern, Orchestration Pattern, Pipeline Pattern, DTO Pattern

**Technologies Mastered:**
- Python (Core, OOP, Async) - Flask, FastAPI - Pandas, NumPy - Scikit-learn
- React, JavaScript, HTML5/CSS3 - PostgreSQL, Redis - Docker, Kubernetes
- Prometheus, Grafana - MLflow, Git, GitHub Actions - AWS/GCP/Azure

---

## 🎯 Your Final Challenge

Congratulations on completing the entire Python Metromap! Here's your final challenge:

**Build Your Own ML-Powered Application:**

1. **Choose a domain** – E-commerce, entertainment, social media, education
2. **Collect data** – Use public datasets or build your own
3. **Build the model** – Implement recommendation algorithms
4. **Create the API** – RESTful endpoints for recommendations
5. **Build the frontend** – React/Vue/Svelte application
6. **Add analytics** – Track user behavior and model performance
7. **Deploy to cloud** – AWS, GCP, or Azure
8. **Monitor and iterate** – A/B testing and continuous improvement

**Portfolio Projects Ideas:**
- Movie recommendation system with TMDB API
- Music playlist generator with Spotify API
- News aggregator with personalized feeds
- Job recommendation engine for recruiters
- Course recommendation for e-learning platforms
- Restaurant finder with collaborative filtering

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Weather Dashboard

- **📚 Series J Catalog:** Capstone Projects – View all 3 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **🏁 The End:** You've completed the entire 2026 Python Metromap!

---

## 🏆 Congratulations!

**You've completed all 52 stories of the 2026 Python Metromap!**

From your first "Hello, World!" to building production-ready ML-powered applications, you've mastered:

✅ Python fundamentals and advanced concepts
✅ Object-oriented programming and design patterns
✅ Data structures and algorithms
✅ File handling and databases
✅ Web development and APIs
✅ Data science and visualization
✅ Machine learning and deep learning
✅ Full-stack application development
✅ Cloud deployment and DevOps
✅ Production ML systems

**You're no longer a passenger—you're a driver. Now go build something amazing!**

---

*Found this helpful? Star the repository, share your projects, and help others on their Python journey. Congratulations, Python Master! 🚇🎉*

## 📊 Final Generation Report

| Series | Total Stories | Generated | Completion |
|--------|---------------|-----------|------------|
| Series 0 | 5 | 5 | 100% |
| Series A | 7 | 7 | 100% |
| Series B | 6 | 6 | 100% |
| Series C | 5 | 5 | 100% |
| Series D | 6 | 6 | 100% |
| Series E | 5 | 5 | 100% |
| Series F | 6 | 6 | 100% |
| Series G | 5 | 5 | 100% |
| Series H | 5 | 5 | 100% |
| Series I | 4 | 4 | 100% |
| Series J | 3 | 3 | 100% |
| **Total** | **52** | **52** | **100%** ✅ |

**The 2026 Python Metromap is COMPLETE!** 🎉🚇🐍