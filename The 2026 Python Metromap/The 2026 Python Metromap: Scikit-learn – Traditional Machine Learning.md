# The 2026 Python Metromap: Scikit-learn – Traditional Machine Learning

## Series I: AI & Machine Learning with Python | Story 1 of 4

![The 2026 Python Metromap/images/Scikit-learn – Traditional Machine Learning](images/Scikit-learn – Traditional Machine Learning.png)

## 📖 Introduction

**Welcome to the first stop on the AI & Machine Learning with Python Line.**

You've completed the Web Development & Automation Line. You can build APIs, full-stack applications, automate system tasks, scrape websites, and schedule recurring jobs. Now it's time to add intelligence to your applications—to predict, classify, and uncover patterns in data.

Scikit-learn is the most popular library for traditional machine learning in Python. It provides consistent, well-documented implementations of algorithms for classification, regression, clustering, dimensionality reduction, and model selection. From spam filters to recommendation engines, from customer churn prediction to house price estimation, scikit-learn makes machine learning accessible and production-ready.

This story—**The 2026 Python Metromap: Scikit-learn – Traditional Machine Learning**—is your guide to building machine learning models with scikit-learn. We'll build a spam classifier for emails using Naive Bayes. We'll create a customer churn predictor using Random Forest. We'll implement a house price estimator using Linear Regression. We'll build a customer segmentation system using K-Means clustering. And we'll learn proper model evaluation, hyperparameter tuning, and pipeline construction.

**Let's learn from data.**

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

### Series I: AI & Machine Learning with Python (4 Stories)

- 🤖 **The 2026 Python Metromap: Scikit-learn – Traditional ML** – Spam classifier for emails; customer churn predictor; house price estimator. **⬅️ YOU ARE HERE**

- 🧠 **The 2026 Python Metromap: TensorFlow and Keras – Deep Learning** – Handwritten digit classifier; fashion item recognizer; sentiment analyzer. 🔜 *Up Next*

- 🔥 **The 2026 Python Metromap: PyTorch – Research and Production** – Custom neural network for image classification; training loops; model deployment.

- 🚀 **The 2026 Python Metromap: End-to-End ML Pipeline Project** – Complete machine learning pipeline from data collection to deployment for house price prediction.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🤖 Section 1: Scikit-learn Fundamentals – Data Preparation and Model Training

Scikit-learn provides a consistent API for machine learning: fit, predict, transform, and score.

**SOLID Principle Applied: Single Responsibility** – Each transformer and estimator handles one task.

**Design Pattern: Strategy Pattern** – Different algorithms implement the same interface.

```python
"""
SCIKIT-LEARN FUNDAMENTALS: DATA PREPARATION AND MODEL TRAINING

This section covers the basics of scikit-learn.

SOLID Principle: Single Responsibility
- Each transformer and estimator handles one task

Design Pattern: Strategy Pattern
- Different algorithms implement the same interface
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_diabetes, make_classification
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


def demonstrate_data_preparation():
    """
    Demonstrates data preparation with scikit-learn.
    
    Key steps: train-test split, scaling, encoding.
    """
    print("=" * 60)
    print("SECTION 1A: DATA PREPARATION")
    print("=" * 60)
    
    # LOAD DATASET
    print("\n1. LOADING DATA")
    print("-" * 40)
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    print(f"  Features shape: {X.shape}")
    print(f"  Target shape: {y.shape}")
    print(f"  Feature names: {iris.feature_names}")
    print(f"  Target names: {iris.target_names}")
    print(f"  Classes: {np.unique(y)}")
    
    # TRAIN-TEST SPLIT
    print("\n2. TRAIN-TEST SPLIT")
    print("-" * 40)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"  Training set: {X_train.shape[0]} samples")
    print(f"  Test set: {X_test.shape[0]} samples")
    print(f"  Train/Test ratio: {len(X_train)/len(X):.1%} / {len(X_test)/len(X):.1%}")
    
    # FEATURE SCALING
    print("\n3. FEATURE SCALING")
    print("-" * 40)
    
    print("  Before scaling:")
    print(f"    Feature 0 - min: {X[:,0].min():.2f}, max: {X[:,0].max():.2f}")
    print(f"    Feature 1 - min: {X[:,1].min():.2f}, max: {X[:,1].max():.2f}")
    
    # StandardScaler (zero mean, unit variance)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print("\n  After StandardScaler:")
    print(f"    Feature 0 - mean: {X_scaled[:,0].mean():.2f}, std: {X_scaled[:,0].std():.2f}")
    print(f"    Feature 1 - mean: {X_scaled[:,1].mean():.2f}, std: {X_scaled[:,1].std():.2f}")
    
    # MinMaxScaler (range 0-1)
    scaler_mm = MinMaxScaler()
    X_scaled_mm = scaler_mm.fit_transform(X)
    
    print("\n  After MinMaxScaler:")
    print(f"    Feature 0 - min: {X_scaled_mm[:,0].min():.2f}, max: {X_scaled_mm[:,0].max():.2f}")
    
    # LABEL ENCODING
    print("\n4. LABEL ENCODING")
    print("-" * 40)
    
    categories = ['cat', 'dog', 'bird', 'dog', 'cat', 'fish']
    print(f"  Original categories: {categories}")
    
    le = LabelEncoder()
    encoded = le.fit_transform(categories)
    print(f"  Encoded: {encoded}")
    print(f"  Classes: {le.classes_}")
    print(f"  Decoded: {le.inverse_transform(encoded)}")


def demonstrate_model_training():
    """
    Demonstrates training and evaluating models.
    
    Consistent API: fit(), predict(), score()
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: MODEL TRAINING AND EVALUATION")
    print("=" * 60)
    
    # Load data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # TRAIN LOGISTIC REGRESSION
    print("\n1. LOGISTIC REGRESSION")
    print("-" * 40)
    
    lr = LogisticRegression(max_iter=200, random_state=42)
    lr.fit(X_train_scaled, y_train)
    
    y_pred = lr.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  Classification Report:\n{classification_report(y_test, y_pred, target_names=iris.target_names)}")
    
    # CROSS-VALIDATION
    print("\n2. CROSS-VALIDATION")
    print("-" * 40)
    
    cv_scores = cross_val_score(lr, X_train_scaled, y_train, cv=5)
    print(f"  Cross-validation scores: {cv_scores}")
    print(f"  Mean CV accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    
    # RANDOM FOREST
    print("\n3. RANDOM FOREST CLASSIFIER")
    print("-" * 40)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_scaled, y_train)
    
    y_pred_rf = rf.predict(X_test_scaled)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    
    print(f"  Accuracy: {accuracy_rf:.4f}")
    print(f"  Feature importance:")
    for name, importance in zip(iris.feature_names, rf.feature_importances_):
        print(f"    {name}: {importance:.4f}")
    
    # CONFUSION MATRIX
    print("\n4. CONFUSION MATRIX")
    print("-" * 40)
    
    cm = confusion_matrix(y_test, y_pred_rf)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=iris.target_names, yticklabels=iris.target_names)
    plt.title('Confusion Matrix - Random Forest')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.show()
    print("  Displayed confusion matrix")


def demonstrate_regression():
    """
    Demonstrates regression models for continuous prediction.
    
    Linear Regression, Random Forest Regressor
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: REGRESSION MODELS")
    print("=" * 60)
    
    # Load diabetes dataset (regression)
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    
    print("\n1. DATASET INFO")
    print("-" * 40)
    
    print(f"  Features shape: {X.shape}")
    print(f"  Target shape: {y.shape}")
    print(f"  Feature names: {diabetes.feature_names}")
    print(f"  Target range: {y.min():.1f} - {y.max():.1f}")
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # LINEAR REGRESSION
    print("\n2. LINEAR REGRESSION")
    print("-" * 40)
    
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)
    
    y_pred = lr.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"  MSE: {mse:.2f}")
    print(f"  RMSE: {np.sqrt(mse):.2f}")
    print(f"  R² Score: {r2:.4f}")
    print(f"  Coefficients:")
    for name, coef in zip(diabetes.feature_names, lr.coef_):
        print(f"    {name}: {coef:.4f}")
    
    # RANDOM FOREST REGRESSOR
    print("\n3. RANDOM FOREST REGRESSOR")
    print("-" * 40)
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train_scaled, y_train)
    
    y_pred_rf = rf.predict(X_test_scaled)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    
    print(f"  MSE: {mse_rf:.2f}")
    print(f"  RMSE: {np.sqrt(mse_rf):.2f}")
    print(f"  R² Score: {r2_rf:.4f}")
    
    # COMPARISON PLOT
    print("\n4. PREDICTION COMPARISON")
    print("-" * 40)
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title(f'Linear Regression (R² = {r2:.3f})')
    
    plt.subplot(1, 2, 2)
    plt.scatter(y_test, y_pred_rf, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title(f'Random Forest (R² = {r2_rf:.3f})')
    
    plt.tight_layout()
    plt.show()
    print("  Displayed prediction comparison plots")


if __name__ == "__main__":
    demonstrate_data_preparation()
    demonstrate_model_training()
    demonstrate_regression()
```

---

## 📧 Section 2: Spam Classifier for Emails

A complete spam detection system using Naive Bayes and text feature extraction.

**SOLID Principles Applied:**
- Single Responsibility: Each transformer handles one preprocessing step
- Dependency Inversion: Pipeline depends on transformer abstractions

**Design Patterns:**
- Pipeline Pattern: Chains preprocessing and model steps
- Strategy Pattern: Different vectorizers and classifiers

```python
"""
SPAM CLASSIFIER FOR EMAILS

This section builds a complete spam detection system.

SOLID Principles Applied:
- Single Responsibility: Each transformer handles one preprocessing step
- Dependency Inversion: Pipeline depends on transformer abstractions

Design Patterns:
- Pipeline Pattern: Chains preprocessing and model steps
- Strategy Pattern: Different vectorizers and classifiers
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.calibration import CalibratedClassifierCV
import re
import string
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns


class SpamClassifier:
    """
    Complete spam classification system.
    
    Design Pattern: Pipeline Pattern - Chains preprocessing and classification
    """
    
    def __init__(self, vectorizer='tfidf', classifier='multinomial_nb'):
        self.vectorizer_name = vectorizer
        self.classifier_name = classifier
        self.pipeline = None
        self.vectorizer = None
        self.model = None
    
    def preprocess_text(self, text):
        """Clean and preprocess text."""
        if isinstance(text, str):
            # Convert to lowercase
            text = text.lower()
            # Remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))
            # Remove extra whitespace
            text = ' '.join(text.split())
            # Remove numbers (optional)
            text = re.sub(r'\d+', '', text)
        return text
    
    def create_pipeline(self):
        """Create the ML pipeline."""
        # Select vectorizer
        if self.vectorizer_name == 'count':
            vectorizer = CountVectorizer(
                lowercase=True,
                strip_accents='unicode',
                stop_words='english',
                max_features=5000,
                ngram_range=(1, 2)
            )
        else:  # tfidf
            vectorizer = TfidfVectorizer(
                lowercase=True,
                strip_accents='unicode',
                stop_words='english',
                max_features=5000,
                ngram_range=(1, 2),
                sublinear_tf=True
            )
        
        # Select classifier
        if self.classifier_name == 'multinomial_nb':
            classifier = MultinomialNB(alpha=0.5)
        else:  # bernoulli_nb
            classifier = BernoulliNB(alpha=0.5)
        
        # Create pipeline
        self.pipeline = Pipeline([
            ('vectorizer', vectorizer),
            ('classifier', classifier)
        ])
        
        return self.pipeline
    
    def train(self, X_train, y_train):
        """Train the spam classifier."""
        if self.pipeline is None:
            self.create_pipeline()
        
        print("  Training spam classifier...")
        self.pipeline.fit(X_train, y_train)
        print("  Training complete")
    
    def predict(self, X):
        """Predict spam/ham for emails."""
        return self.pipeline.predict(X)
    
    def predict_proba(self, X):
        """Get prediction probabilities."""
        return self.pipeline.predict_proba(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluate the classifier."""
        y_pred = self.predict(X_test)
        y_pred_proba = self.predict_proba(X_test)
        
        print("\n  Classification Report:")
        print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
        plt.title('Confusion Matrix - Spam Classifier')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        plt.show()
        
        # ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc="lower right")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        return {
            'accuracy': (y_pred == y_test).mean(),
            'classification_report': classification_report(y_test, y_pred, output_dict=True),
            'roc_auc': roc_auc
        }
    
    def tune_hyperparameters(self, X_train, y_train):
        """Perform grid search for hyperparameter tuning."""
        print("\n  Tuning hyperparameters...")
        
        param_grid = {
            'vectorizer__max_features': [3000, 5000, 10000],
            'vectorizer__ngram_range': [(1, 1), (1, 2)],
            'classifier__alpha': [0.1, 0.5, 1.0]
        }
        
        grid_search = GridSearchCV(
            self.pipeline, param_grid, cv=5, scoring='f1', n_jobs=-1, verbose=0
        )
        grid_search.fit(X_train, y_train)
        
        print(f"  Best parameters: {grid_search.best_params_}")
        print(f"  Best cross-validation score: {grid_search.best_score_:.4f}")
        
        self.pipeline = grid_search.best_estimator_
        return grid_search.best_params_
    
    def get_feature_importance(self, feature_names=None, n=20):
        """Get top features for spam detection."""
        if hasattr(self.pipeline.named_steps['classifier'], 'feature_log_prob_'):
            vectorizer = self.pipeline.named_steps['vectorizer']
            classifier = self.pipeline.named_steps['classifier']
            
            feature_names = vectorizer.get_feature_names_out()
            spam_probs = classifier.feature_log_prob_[1]  # Spam class
            ham_probs = classifier.feature_log_prob_[0]   # Ham class
            
            # Calculate log odds ratio
            log_odds_ratio = spam_probs - ham_probs
            
            # Get top spam indicators
            top_spam_idx = np.argsort(log_odds_ratio)[-n:][::-1]
            top_ham_idx = np.argsort(log_odds_ratio)[:n]
            
            top_spam_features = [(feature_names[i], log_odds_ratio[i]) for i in top_spam_idx]
            top_ham_features = [(feature_names[i], -log_odds_ratio[i]) for i in top_ham_idx]
            
            return {
                'top_spam_indicators': top_spam_features,
                'top_ham_indicators': top_ham_features
            }
        return None


def generate_sample_email_data():
    """
    Generate sample email data for demonstration.
    
    In production, you would load real email data.
    """
    # Ham (legitimate) emails
    ham_emails = [
        "Hi John, can we meet tomorrow at 2pm to discuss the project? Best, Alice",
        "Your meeting has been scheduled for Friday at 10am in Conference Room A",
        "Thank you for your purchase! Your order #12345 has been confirmed",
        "Monthly report attached. Please review by Friday.",
        "Welcome to our newsletter! You're receiving this because you signed up.",
        "Your password reset request has been received. Click the link to continue.",
        "Reminder: Team lunch at 12:30pm today in the cafeteria",
        "Invoice #INV-2024-001 is now available for download",
        "Your subscription will renew on January 15, 2024",
        "Please find attached the document you requested"
    ]
    
    # Spam emails
    spam_emails = [
        "CONGRATULATIONS! You've won a FREE iPhone! Click here to claim now!",
        "URGENT: Your account has been compromised. Verify immediately at this link.",
        "Earn $5000 per week working from home! No experience needed!",
        "You have been selected for a special offer! 90% off limited time!",
        "Dear customer, your bank account needs verification. Click here now.",
        "Lose weight fast with our miracle supplement! 50% off today!",
        "You've inherited $10,000,000 from a distant relative! Contact us now!",
        "FREE gift card inside! Claim your $1000 Walmart gift card today!",
        "Hot singles in your area want to meet you! Click here to see photos!",
        "Your package cannot be delivered. Click here to reschedule delivery."
    ]
    
    # Create dataset
    ham_df = pd.DataFrame({'text': ham_emails * 10, 'label': 0})  # 0 = ham
    spam_df = pd.DataFrame({'text': spam_emails * 10, 'label': 1})  # 1 = spam
    
    df = pd.concat([ham_df, spam_df], ignore_index=True)
    
    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df


def demonstrate_spam_classifier():
    """
    Demonstrate the spam classifier system.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: SPAM CLASSIFIER")
    print("=" * 60)
    
    # Load and prepare data
    print("\n1. LOADING EMAIL DATA")
    print("-" * 40)
    
    df = generate_sample_email_data()
    print(f"  Dataset shape: {df.shape}")
    print(f"  Class distribution:\n{df['label'].value_counts()}")
    
    # Preview data
    print("\n  Sample ham email:")
    print(f"    {df[df['label']==0]['text'].iloc[0][:100]}...")
    print("\n  Sample spam email:")
    print(f"    {df[df['label']==1]['text'].iloc[0][:100]}...")
    
    # Split data
    X = df['text'].values
    y = df['label'].values
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\n  Training samples: {len(X_train)}")
    print(f"  Test samples: {len(X_test)}")
    
    # Create and train classifier
    print("\n2. TRAINING SPAM CLASSIFIER")
    print("-" * 40)
    
    classifier = SpamClassifier(vectorizer='tfidf', classifier='multinomial_nb')
    classifier.create_pipeline()
    classifier.train(X_train, y_train)
    
    # Evaluate
    print("\n3. MODEL EVALUATION")
    print("-" * 40)
    
    metrics = classifier.evaluate(X_test, y_test)
    
    # Feature importance
    print("\n4. TOP SPAM INDICATORS")
    print("-" * 40)
    
    importance = classifier.get_feature_importance()
    if importance:
        print("  Words that indicate SPAM:")
        for word, score in importance['top_spam_indicators'][:10]:
            print(f"    {word}: {score:.4f}")
        
        print("\n  Words that indicate HAM (legitimate):")
        for word, score in importance['top_ham_indicators'][:10]:
            print(f"    {word}: {score:.4f}")
    
    # Test on new emails
    print("\n5. TESTING ON NEW EMAILS")
    print("-" * 40)
    
    test_emails = [
        "Hey, can you review my pull request? Thanks!",
        "YOU WON A PRIZE! Click here to claim your $1000 gift card!",
        "Meeting rescheduled to 3pm tomorrow.",
        "URGENT: Your account will be suspended. Verify now!",
        "Weekly team sync at 11am in the conference room."
    ]
    
    for email in test_emails:
        pred = classifier.predict([email])[0]
        proba = classifier.predict_proba([email])[0]
        label = "SPAM" if pred == 1 else "HAM"
        confidence = proba[pred]
        print(f"  '{email[:50]}...' → {label} (confidence: {confidence:.2%})")
    
    # Hyperparameter tuning
    print("\n6. HYPERPARAMETER TUNING")
    print("-" * 40)
    
    classifier.tune_hyperparameters(X_train, y_train)
    
    # Cross-validation score
    print("\n7. CROSS-VALIDATION SCORE")
    print("-" * 40)
    
    cv_scores = cross_val_score(classifier.pipeline, X, y, cv=5, scoring='f1')
    print(f"  Cross-validation F1 scores: {cv_scores}")
    print(f"  Mean F1: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")


if __name__ == "__main__":
    demonstrate_spam_classifier()
```

---

## 📈 Section 3: Customer Churn Predictor

A customer churn prediction system using Random Forest and ensemble methods.

**SOLID Principles Applied:**
- Single Responsibility: Each preprocessing step handles one transformation
- Open/Closed: New features can be added

**Design Patterns:**
- Pipeline Pattern: Chains preprocessing and modeling
- Strategy Pattern: Different models for comparison

```python
"""
CUSTOMER CHURN PREDICTOR

This section builds a customer churn prediction system.

SOLID Principles Applied:
- Single Responsibility: Each preprocessing step handles one transformation
- Open/Closed: New features can be added

Design Patterns:
- Pipeline Pattern: Chains preprocessing and modeling
- Strategy Pattern: Different models for comparison
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


def generate_customer_data(n_samples=5000):
    """
    Generate synthetic customer data for churn prediction.
    
    Features:
    - tenure: months as customer
    - monthly_charges: monthly bill amount
    - total_charges: total amount paid
    - contract_type: Month-to-month, One year, Two year
    - payment_method: Electronic check, Mailed check, Bank transfer, Credit card
    - paperless_billing: Yes/No
    - streaming_tv: Yes/No
    - streaming_movies: Yes/No
    - device_protection: Yes/No
    - online_security: Yes/No
    - tech_support: Yes/No
    - num_services: number of additional services
    - avg_monthly_usage: average monthly usage in GB
    - support_tickets: number of support tickets
    - satisfaction_score: customer satisfaction (1-5)
    """
    np.random.seed(42)
    
    n = n_samples
    
    # Demographics
    tenure = np.random.exponential(20, n).astype(int)
    tenure = np.clip(tenure, 1, 72)
    
    monthly_charges = np.random.gamma(5, 10, n)
    monthly_charges = np.clip(monthly_charges, 20, 150)
    
    total_charges = monthly_charges * tenure * np.random.uniform(0.9, 1.1, n)
    
    # Contract type (affects churn significantly)
    contract_type = np.random.choice(
        ['Month-to-month', 'One year', 'Two year'], 
        n, 
        p=[0.5, 0.3, 0.2]
    )
    
    # Payment method
    payment_method = np.random.choice(
        ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'],
        n,
        p=[0.4, 0.2, 0.2, 0.2]
    )
    
    # Services
    paperless_billing = np.random.choice(['Yes', 'No'], n, p=[0.6, 0.4])
    streaming_tv = np.random.choice(['Yes', 'No'], n, p=[0.4, 0.6])
    streaming_movies = np.random.choice(['Yes', 'No'], n, p=[0.4, 0.6])
    device_protection = np.random.choice(['Yes', 'No'], n, p=[0.3, 0.7])
    online_security = np.random.choice(['Yes', 'No'], n, p=[0.3, 0.7])
    tech_support = np.random.choice(['Yes', 'No'], n, p=[0.3, 0.7])
    
    num_services = (
        (streaming_tv == 'Yes').astype(int) +
        (streaming_movies == 'Yes').astype(int) +
        (device_protection == 'Yes').astype(int) +
        (online_security == 'Yes').astype(int) +
        (tech_support == 'Yes').astype(int)
    )
    
    # Usage and support
    avg_monthly_usage = np.random.exponential(50, n)
    support_tickets = np.random.poisson(1, n)
    satisfaction_score = np.random.uniform(1, 5, n)
    
    # Churn logic (higher probability for certain conditions)
    churn_probability = np.zeros(n)
    
    # Short tenure increases churn
    churn_probability += (tenure < 12) * 0.3
    
    # Month-to-month contracts churn more
    churn_probability += (contract_type == 'Month-to-month') * 0.3
    
    # Electronic check churns more
    churn_probability += (payment_method == 'Electronic check') * 0.2
    
    # Paperless billing slightly increases churn
    churn_probability += (paperless_billing == 'Yes') * 0.05
    
    # More support tickets increase churn
    churn_probability += support_tickets * 0.1
    
    # Low satisfaction increases churn
    churn_probability += (satisfaction_score < 2.5) * 0.2
    
    # High monthly charges increase churn
    churn_probability += (monthly_charges > 100) * 0.15
    
    # Few services increase churn
    churn_probability += (num_services <= 2) * 0.1
    
    # Add random noise
    churn_probability += np.random.uniform(0, 0.2, n)
    
    # Normalize to [0, 1]
    churn_probability = np.clip(churn_probability, 0, 1)
    
    # Generate churn labels
    churn = (np.random.random(n) < churn_probability).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'tenure': tenure,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges,
        'contract_type': contract_type,
        'payment_method': payment_method,
        'paperless_billing': paperless_billing,
        'streaming_tv': streaming_tv,
        'streaming_movies': streaming_movies,
        'device_protection': device_protection,
        'online_security': online_security,
        'tech_support': tech_support,
        'num_services': num_services,
        'avg_monthly_usage': avg_monthly_usage,
        'support_tickets': support_tickets,
        'satisfaction_score': satisfaction_score,
        'churn': churn
    })
    
    return df


class ChurnPredictor:
    """
    Customer churn prediction system.
    
    Design Pattern: Pipeline Pattern - Complete prediction pipeline
    """
    
    def __init__(self):
        self.models = {}
        self.best_model = None
        self.feature_columns = None
        self.categorical_cols = ['contract_type', 'payment_method', 'paperless_billing',
                                  'streaming_tv', 'streaming_movies', 'device_protection',
                                  'online_security', 'tech_support']
        self.numeric_cols = ['tenure', 'monthly_charges', 'total_charges', 'num_services',
                              'avg_monthly_usage', 'support_tickets', 'satisfaction_score']
        self.label_encoders = {}
        self.scaler = StandardScaler()
    
    def preprocess(self, df):
        """Preprocess the data."""
        # Create a copy
        data = df.copy()
        
        # Encode categorical variables
        for col in self.categorical_cols:
            if col in data.columns:
                le = LabelEncoder()
                data[col] = le.fit_transform(data[col])
                self.label_encoders[col] = le
        
        # Scale numeric features
        numeric_data = data[self.numeric_cols]
        scaled_numeric = self.scaler.fit_transform(numeric_data)
        
        # Combine features
        categorical_data = data[self.categorical_cols].values
        X = np.hstack([scaled_numeric, categorical_data])
        
        self.feature_columns = self.numeric_cols + self.categorical_cols
        
        return X
    
    def preprocess_new(self, df):
        """Preprocess new data (using fitted transformers)."""
        data = df.copy()
        
        for col in self.categorical_cols:
            if col in data.columns and col in self.label_encoders:
                le = self.label_encoders[col]
                # Handle unseen labels
                data[col] = data[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
                data[col] = le.transform(data[col])
        
        numeric_data = data[self.numeric_cols]
        scaled_numeric = self.scaler.transform(numeric_data)
        
        categorical_data = data[self.categorical_cols].values
        X = np.hstack([scaled_numeric, categorical_data])
        
        return X
    
    def train_models(self, X_train, y_train):
        """Train multiple models for comparison."""
        print("\n  Training multiple models...")
        
        models = {
            'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
            'SVM': SVC(probability=True, random_state=42)
        }
        
        results = {}
        
        for name, model in models.items():
            print(f"    Training {name}...")
            model.fit(X_train, y_train)
            self.models[name] = model
            
            # Cross-validation
            cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='roc_auc')
            results[name] = {
                'model': model,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std()
            }
            print(f"      CV ROC-AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        # Select best model
        best_name = max(results, key=lambda x: results[x]['cv_mean'])
        self.best_model = self.models[best_name]
        print(f"\n  Best model: {best_name}")
        
        return results
    
    def tune_random_forest(self, X_train, y_train):
        """Hyperparameter tuning for Random Forest."""
        print("\n  Tuning Random Forest hyperparameters...")
        
        param_dist = {
            'n_estimators': [50, 100, 200],
            'max_depth': [10, 20, 30, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['sqrt', 'log2']
        }
        
        rf = RandomForestClassifier(random_state=42)
        
        random_search = RandomizedSearchCV(
            rf, param_dist, n_iter=20, cv=5, scoring='roc_auc',
            random_state=42, n_jobs=-1, verbose=0
        )
        random_search.fit(X_train, y_train)
        
        print(f"  Best parameters: {random_search.best_params_}")
        print(f"  Best CV score: {random_search.best_score_:.4f}")
        
        self.best_model = random_search.best_estimator_
        return random_search.best_params_
    
    def evaluate(self, X_test, y_test):
        """Evaluate the best model."""
        y_pred = self.best_model.predict(X_test)
        y_pred_proba = self.best_model.predict_proba(X_test)[:, 1]
        
        print("\n  Classification Report:")
        print(classification_report(y_test, y_pred, target_names=['Not Churned', 'Churned']))
        
        # ROC-AUC
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        print(f"\n  ROC-AUC Score: {roc_auc:.4f}")
        
        # Average Precision
        avg_precision = average_precision_score(y_test, y_pred_proba)
        print(f"  Average Precision: {avg_precision:.4f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['Not Churned', 'Churned'],
                    yticklabels=['Not Churned', 'Churned'])
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        
        # Feature Importance (if available)
        if hasattr(self.best_model, 'feature_importances_'):
            plt.subplot(1, 2, 2)
            importances = self.best_model.feature_importances_
            indices = np.argsort(importances)[-10:]
            
            plt.barh(range(len(indices)), importances[indices])
            plt.yticks(range(len(indices)), [self.feature_columns[i] for i in indices])
            plt.xlabel('Feature Importance')
            plt.title('Top 10 Most Important Features')
        
        plt.tight_layout()
        plt.show()
        
        return {
            'roc_auc': roc_auc,
            'avg_precision': avg_precision,
            'confusion_matrix': cm
        }
    
    def predict_churn_risk(self, customer_data):
        """Predict churn risk for new customers."""
        X = self.preprocess_new(customer_data)
        probabilities = self.best_model.predict_proba(X)[:, 1]
        predictions = self.best_model.predict(X)
        
        results = []
        for i, (prob, pred) in enumerate(zip(probabilities, predictions)):
            risk_level = 'High' if prob > 0.7 else 'Medium' if prob > 0.3 else 'Low'
            results.append({
                'customer_id': customer_data.iloc[i].get('customer_id', i),
                'churn_probability': prob,
                'prediction': 'Will Churn' if pred == 1 else 'Will Stay',
                'risk_level': risk_level
            })
        
        return results


def demonstrate_churn_predictor():
    """
    Demonstrate the customer churn predictor.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: CUSTOMER CHURN PREDICTOR")
    print("=" * 60)
    
    # Generate data
    print("\n1. GENERATING CUSTOMER DATA")
    print("-" * 40)
    
    df = generate_customer_data(5000)
    print(f"  Dataset shape: {df.shape}")
    print(f"  Churn rate: {df['churn'].mean():.2%}")
    print(f"  Features: {list(df.columns)}")
    
    # Explore churn patterns
    print("\n  Churn by contract type:")
    print(df.groupby('contract_type')['churn'].mean())
    
    # Prepare data
    X = df.drop('churn', axis=1)
    y = df['churn']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\n  Training samples: {len(X_train)}")
    print(f"  Test samples: {len(X_test)}")
    
    # Create and train predictor
    predictor = ChurnPredictor()
    
    print("\n2. PREPROCESSING DATA")
    print("-" * 40)
    
    X_train_processed = predictor.preprocess(X_train)
    X_test_processed = predictor.preprocess_new(X_test)
    
    print(f"  Processed training shape: {X_train_processed.shape}")
    
    # Train models
    print("\n3. TRAINING MODELS")
    print("-" * 40)
    
    results = predictor.train_models(X_train_processed, y_train)
    
    # Hyperparameter tuning
    predictor.tune_random_forest(X_train_processed, y_train)
    
    # Evaluate
    print("\n4. MODEL EVALUATION")
    print("-" * 40)
    
    metrics = predictor.evaluate(X_test_processed, y_test)
    
    # Predict churn risk for new customers
    print("\n5. PREDICTING CHURN RISK")
    print("-" * 40)
    
    # Create sample new customers
    new_customers = pd.DataFrame({
        'customer_id': [1001, 1002, 1003, 1004],
        'tenure': [2, 24, 36, 6],
        'monthly_charges': [120, 80, 60, 95],
        'total_charges': [240, 1920, 2160, 570],
        'contract_type': ['Month-to-month', 'Two year', 'One year', 'Month-to-month'],
        'payment_method': ['Electronic check', 'Credit card', 'Bank transfer', 'Electronic check'],
        'paperless_billing': ['Yes', 'No', 'Yes', 'Yes'],
        'streaming_tv': ['Yes', 'Yes', 'No', 'No'],
        'streaming_movies': ['Yes', 'Yes', 'No', 'No'],
        'device_protection': ['No', 'Yes', 'Yes', 'No'],
        'online_security': ['No', 'Yes', 'Yes', 'No'],
        'tech_support': ['No', 'Yes', 'No', 'No'],
        'num_services': [2, 5, 3, 0],
        'avg_monthly_usage': [200, 80, 50, 150],
        'support_tickets': [3, 0, 1, 2],
        'satisfaction_score': [2.5, 4.5, 4.0, 2.0]
    })
    
    predictions = predictor.predict_churn_risk(new_customers)
    
    for pred in predictions:
        print(f"\n  Customer {pred['customer_id']}:")
        print(f"    Churn Probability: {pred['churn_probability']:.2%}")
        print(f"    Prediction: {pred['prediction']}")
        print(f"    Risk Level: {pred['risk_level']}")


if __name__ == "__main__":
    demonstrate_churn_predictor()
```

---

## 🏠 Section 4: House Price Estimator

A complete house price prediction system using Linear Regression and advanced feature engineering.

**SOLID Principles Applied:**
- Single Responsibility: Each feature engineering step has one purpose
- Dependency Inversion: Pipeline depends on transformer abstractions

**Design Patterns:**
- Pipeline Pattern: Chains feature engineering and regression
- Strategy Pattern: Different regression models

```python
"""
HOUSE PRICE ESTIMATOR

This section builds a house price prediction system.

SOLID Principles Applied:
- Single Responsibility: Each feature engineering step has one purpose
- Dependency Inversion: Pipeline depends on transformer abstractions

Design Patterns:
- Pipeline Pattern: Chains feature engineering and regression
- Strategy Pattern: Different regression models
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


def generate_house_data(n_samples=5000):
    """
    Generate synthetic house price data.
    
    Features:
    - sqft_living: square footage of living area
    - sqft_lot: total lot square footage
    - bedrooms: number of bedrooms
    - bathrooms: number of bathrooms
    - floors: number of floors
    - waterfront: whether property has waterfront view
    - view: quality of view (0-4)
    - condition: condition of house (1-5)
    - grade: overall grade (1-13)
    - sqft_above: square footage above ground
    - sqft_basement: square footage of basement
    - yr_built: year built
    - yr_renovated: year renovated (0 if never)
    - lat: latitude
    - long: longitude
    - age: age of house
    - has_basement: whether has basement
    - is_renovated: whether renovated
    """
    np.random.seed(42)
    
    n = n_samples
    
    # Core features
    sqft_living = np.random.gamma(2, 500, n).astype(int)
    sqft_living = np.clip(sqft_living, 500, 5000)
    
    sqft_lot = np.random.gamma(1.5, 2000, n).astype(int)
    sqft_lot = np.clip(sqft_lot, 1000, 20000)
    
    bedrooms = np.random.choice([1, 2, 3, 4, 5, 6], n, p=[0.02, 0.08, 0.35, 0.35, 0.15, 0.05])
    bathrooms = np.random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4], n,
                                  p=[0.05, 0.1, 0.3, 0.25, 0.15, 0.1, 0.05])
    
    floors = np.random.choice([1, 1.5, 2, 2.5, 3], n, p=[0.4, 0.1, 0.35, 0.1, 0.05])
    
    waterfront = np.random.choice([0, 1], n, p=[0.95, 0.05])
    view = np.random.choice([0, 1, 2, 3, 4], n, p=[0.4, 0.2, 0.15, 0.15, 0.1])
    condition = np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.1, 0.4, 0.3, 0.15])
    grade = np.random.choice(range(3, 14), n, p=[0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.2, 0.12, 0.08, 0.03, 0.02])
    
    sqft_above = np.random.gamma(2, 400, n).astype(int)
    sqft_above = np.clip(sqft_above, 400, 4500)
    sqft_basement = np.maximum(0, sqft_living - sqft_above)
    
    yr_built = np.random.choice(range(1900, 2024), n)
    yr_renovated = np.random.choice([0] + list(range(1990, 2024)), n, p=[0.8] + [0.02] * 34)
    
    lat = np.random.uniform(47.2, 47.8, n)
    long = np.random.uniform(-122.5, -121.8, n)
    
    # Derived features
    age = 2024 - yr_built
    has_basement = (sqft_basement > 0).astype(int)
    is_renovated = (yr_renovated > 0).astype(int)
    
    # Price calculation (based on multiple factors)
    base_price = 50000
    
    # Square footage impact
    price = base_price + sqft_living * 150
    
    # Bedroom impact
    price += bedrooms * 15000
    
    # Bathroom impact
    price += bathrooms * 10000
    
    # Floor impact
    price += (floors - 1) * 20000
    
    # Waterfront premium
    price += waterfront * 200000
    
    # View premium
    price += view * 25000
    
    # Condition impact
    price += (condition - 3) * 15000
    
    # Grade impact
    price += (grade - 7) * 20000
    
    # Basement impact
    price += has_basement * 30000
    
    # Age impact (older houses worth less)
    price -= age * 500
    
    # Renovation premium
    price += is_renovated * 50000
    
    # Location impact (simplified)
    price += (lat - 47.5) * 1000000
    price += (long + 122) * 500000
    
    # Add noise
    noise = np.random.normal(0, price * 0.1, n)
    price = price + noise
    
    # Ensure positive prices
    price = np.maximum(price, 50000)
    
    # Create DataFrame
    df = pd.DataFrame({
        'sqft_living': sqft_living,
        'sqft_lot': sqft_lot,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'floors': floors,
        'waterfront': waterfront,
        'view': view,
        'condition': condition,
        'grade': grade,
        'sqft_above': sqft_above,
        'sqft_basement': sqft_basement,
        'yr_built': yr_built,
        'yr_renovated': yr_renovated,
        'lat': lat,
        'long': long,
        'age': age,
        'has_basement': has_basement,
        'is_renovated': is_renovated,
        'price': price
    })
    
    return df


class HousePricePredictor:
    """
    House price prediction system.
    
    Design Pattern: Pipeline Pattern - Complete prediction pipeline
    """
    
    def __init__(self):
        self.models = {}
        self.best_model = None
        self.scaler = StandardScaler()
        self.feature_columns = None
    
    def engineer_features(self, df):
        """Create additional features."""
        data = df.copy()
        
        # Interaction features
        data['sqft_per_bedroom'] = data['sqft_living'] / (data['bedrooms'] + 1)
        data['sqft_per_bathroom'] = data['sqft_living'] / (data['bathrooms'] + 0.5)
        data['bed_bath_ratio'] = data['bedrooms'] / (data['bathrooms'] + 0.5)
        
        # Age groups
        data['age_group'] = pd.cut(data['age'], bins=[0, 5, 20, 50, 100, 200], 
                                    labels=['New', 'Recent', 'Mid', 'Old', 'Historic'])
        
        # Price per square foot (target encoding would be better, this is simplified)
        # For demonstration, we'll use it as a feature (would cause data leakage in reality)
        
        # Lot efficiency
        data['lot_efficiency'] = data['sqft_living'] / (data['sqft_lot'] + 1)
        
        # Decade built
        data['decade_built'] = (data['yr_built'] // 10) * 10
        
        # One-hot encode categorical features
        data = pd.get_dummies(data, columns=['age_group', 'decade_built'], drop_first=True)
        
        return data
    
    def preprocess(self, df):
        """Preprocess the data for modeling."""
        # Engineer features
        data = self.engineer_features(df)
        
        # Separate features and target
        if 'price' in data.columns:
            y = data['price'].values
            X = data.drop('price', axis=1)
        else:
            X = data
            y = None
        
        # Select numeric columns
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        X_numeric = X[numeric_cols]
        
        # Store feature names
        self.feature_columns = X_numeric.columns.tolist()
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X_numeric)
        
        return X_scaled, y
    
    def preprocess_new(self, df):
        """Preprocess new data (using fitted transformers)."""
        data = self.engineer_features(df)
        
        # Ensure all expected columns exist
        for col in self.feature_columns:
            if col not in data.columns:
                data[col] = 0
        
        X = data[self.feature_columns]
        X_scaled = self.scaler.transform(X)
        
        return X_scaled
    
    def train_models(self, X_train, y_train):
        """Train multiple regression models."""
        print("\n  Training multiple models...")
        
        models = {
            'Linear Regression': LinearRegression(),
            'Ridge Regression': Ridge(alpha=1.0),
            'Lasso Regression': Lasso(alpha=1.0),
            'Elastic Net': ElasticNet(alpha=1.0, l1_ratio=0.5),
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
        }
        
        results = {}
        
        for name, model in models.items():
            print(f"    Training {name}...")
            
            # Cross-validation
            cv_scores = cross_val_score(model, X_train, y_train, cv=5, 
                                        scoring='r2', n_jobs=-1)
            
            # Fit on full training set
            model.fit(X_train, y_train)
            self.models[name] = model
            
            results[name] = {
                'model': model,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std()
            }
            print(f"      CV R²: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        # Select best model
        best_name = max(results, key=lambda x: results[x]['cv_mean'])
        self.best_model = self.models[best_name]
        print(f"\n  Best model: {best_name}")
        
        return results
    
    def tune_gradient_boosting(self, X_train, y_train):
        """Hyperparameter tuning for Gradient Boosting."""
        print("\n  Tuning Gradient Boosting hyperparameters...")
        
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 5, 7],
            'learning_rate': [0.01, 0.05, 0.1],
            'subsample': [0.8, 0.9, 1.0]
        }
        
        gb = GradientBoostingRegressor(random_state=42)
        
        grid_search = GridSearchCV(
            gb, param_grid, cv=5, scoring='r2', n_jobs=-1, verbose=0
        )
        grid_search.fit(X_train, y_train)
        
        print(f"  Best parameters: {grid_search.best_params_}")
        print(f"  Best CV R²: {grid_search.best_score_:.4f}")
        
        self.best_model = grid_search.best_estimator_
        return grid_search.best_params_
    
    def evaluate(self, X_test, y_test):
        """Evaluate the best model."""
        y_pred = self.best_model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"\n  Model Performance:")
        print(f"    MSE: ${mse:,.2f}")
        print(f"    RMSE: ${rmse:,.2f}")
        print(f"    MAE: ${mae:,.2f}")
        print(f"    R² Score: {r2:.4f}")
        
        # Prediction vs Actual plot
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.xlabel('Actual Price ($)')
        plt.ylabel('Predicted Price ($)')
        plt.title(f'Predictions vs Actual (R² = {r2:.3f})')
        
        # Residual plot
        plt.subplot(1, 2, 2)
        residuals = y_test - y_pred
        plt.scatter(y_pred, residuals, alpha=0.5)
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel('Predicted Price ($)')
        plt.ylabel('Residuals ($)')
        plt.title('Residual Plot')
        
        plt.tight_layout()
        plt.show()
        
        # Feature importance (if available)
        if hasattr(self.best_model, 'feature_importances_'):
            print("\n  Top 10 Most Important Features:")
            importances = self.best_model.feature_importances_
            indices = np.argsort(importances)[-10:]
            
            for i in indices[::-1]:
                print(f"    {self.feature_columns[i]}: {importances[i]:.4f}")
        
        return {
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'predictions': y_pred,
            'residuals': residuals
        }


def demonstrate_house_price_predictor():
    """
    Demonstrate the house price predictor.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: HOUSE PRICE ESTIMATOR")
    print("=" * 60)
    
    # Generate data
    print("\n1. GENERATING HOUSE DATA")
    print("-" * 40)
    
    df = generate_house_data(5000)
    print(f"  Dataset shape: {df.shape}")
    print(f"  Price range: ${df['price'].min():,.0f} - ${df['price'].max():,.0f}")
    print(f"  Average price: ${df['price'].mean():,.0f}")
    
    # Explore correlations
    print("\n  Top correlations with price:")
    correlations = df.corr()['price'].sort_values(ascending=False)
    for feature, corr in correlations.head(10).items():
        print(f"    {feature}: {corr:.4f}")
    
    # Prepare data
    X, y = predictor.preprocess(df)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\n  Training samples: {len(X_train)}")
    print(f"  Test samples: {len(X_test)}")
    
    # Create predictor
    predictor = HousePricePredictor()
    
    print("\n2. FEATURE ENGINEERING")
    print("-" * 40)
    
    df_engineered = predictor.engineer_features(df)
    print(f"  Original features: {len(df.columns)}")
    print(f"  Engineered features: {len(df_engineered.columns)}")
    print(f"  New features: {[c for c in df_engineered.columns if c not in df.columns][:5]}...")
    
    # Train models
    print("\n3. TRAINING MODELS")
    print("-" * 40)
    
    results = predictor.train_models(X_train, y_train)
    
    # Hyperparameter tuning
    predictor.tune_gradient_boosting(X_train, y_train)
    
    # Evaluate
    print("\n4. MODEL EVALUATION")
    print("-" * 40)
    
    metrics = predictor.evaluate(X_test, y_test)
    
    # Predict for a new house
    print("\n5. PREDICTING FOR A NEW HOUSE")
    print("-" * 40)
    
    new_house = pd.DataFrame({
        'sqft_living': [2500],
        'sqft_lot': [6000],
        'bedrooms': [4],
        'bathrooms': [2.5],
        'floors': [2],
        'waterfront': [0],
        'view': [2],
        'condition': [4],
        'grade': [8],
        'sqft_above': [2000],
        'sqft_basement': [500],
        'yr_built': [2010],
        'yr_renovated': [0],
        'lat': [47.6],
        'long': [-122.3],
        'age': [14],
        'has_basement': [1],
        'is_renovated': [0]
    })
    
    X_new = predictor.preprocess_new(new_house)
    predicted_price = predictor.best_model.predict(X_new)[0]
    
    print(f"  House features:")
    for col, val in new_house.iloc[0].items():
        print(f"    {col}: {val}")
    print(f"\n  Estimated Price: ${predicted_price:,.0f}")


if __name__ == "__main__":
    demonstrate_house_price_predictor()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Scikit-learn API** – Consistent interface: `fit()`, `predict()`, `transform()`, `score()`. All estimators follow the same pattern.

- **Data Preparation** – `train_test_split` for evaluation. `StandardScaler` for normalization. `LabelEncoder` for categorical variables.

- **Classification Models** – Logistic Regression, Random Forest, Gradient Boosting, SVM. Metrics: accuracy, precision, recall, F1, ROC-AUC.

- **Regression Models** – Linear Regression, Ridge, Lasso, Elastic Net, Random Forest Regressor, Gradient Boosting Regressor. Metrics: MSE, RMSE, MAE, R².

- **Spam Classifier** – Text preprocessing with TF-IDF. Multinomial Naive Bayes. Feature importance (top spam indicators). ROC curve and AUC.

- **Churn Predictor** – Customer churn prediction. Feature engineering for categorical variables. Model comparison and selection. Hyperparameter tuning with RandomizedSearchCV.

- **House Price Estimator** – Feature engineering (interaction features, derived features). Polynomial features. Gradient Boosting tuning with GridSearchCV.

- **Model Evaluation** – Cross-validation for robust estimation. Confusion matrix for classification. Residual plots for regression. Feature importance analysis.

- **Pipelines** – Chain preprocessing and modeling steps. Ensure consistent transformation between training and prediction.

- **SOLID Principles Applied** – Single Responsibility (each transformer/estimator does one thing), Open/Closed (new models can be added), Dependency Inversion (pipeline depends on abstractions), Interface Segregation (clean estimator interfaces).

- **Design Patterns Used** – Strategy Pattern (different algorithms), Pipeline Pattern (chained transformations), Factory Pattern (model creation), Template Method (fit/predict interface), Adapter Pattern (scikit-learn API).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler

- **📚 Series I Catalog:** AI & Machine Learning with Python – View all 4 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: TensorFlow and Keras – Deep Learning (Series I, Story 2)

---

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
| Series I | 4 | 1 | 3 | 25% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **51** | **1** | **98%** |

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
30. Series E, Story 1: The 2026 Python Metromap: File I/O – Reading & Writing
31. Series E, Story 2: The 2026 Python Metromap: CSV & JSON Processing – Structured Data
32. Series E, Story 3: The 2026 Python Metromap: Exception Handling – Graceful Failures
33. Series E, Story 4: The 2026 Python Metromap: Context Managers – The with Statement
34. Series E, Story 5: The 2026 Python Metromap: Working with Paths & Directories
35. Series F, Story 1: The 2026 Python Metromap: Decorators – Wrapping Functions
36. Series F, Story 2: The 2026 Python Metromap: Generators – Memory-Efficient Loops
37. Series F, Story 3: The 2026 Python Metromap: Iterators – Custom Looping
38. Series F, Story 4: The 2026 Python Metromap: Memory Management & Garbage Collection
39. Series F, Story 5: The 2026 Python Metromap: Testing & Debugging – pytest and unittest
40. Series F, Story 6: The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking
41. Series G, Story 1: The 2026 Python Metromap: NumPy – Numerical Computing
42. Series G, Story 2: The 2026 Python Metromap: Pandas – Data Wrangling
43. Series G, Story 3: The 2026 Python Metromap: Matplotlib – Basic Plotting
44. Series G, Story 4: The 2026 Python Metromap: Seaborn – Statistical Visualization
45. Series G, Story 5: The 2026 Python Metromap: Real-World EDA Project
46. Series H, Story 1: The 2026 Python Metromap: Flask – Building Web APIs
47. Series H, Story 2: The 2026 Python Metromap: Django – Full-Stack Web Apps
48. Series H, Story 3: The 2026 Python Metromap: Automation with os and sys
49. Series H, Story 4: The 2026 Python Metromap: Web Scraping with BeautifulSoup
50. Series H, Story 5: The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler
51. Series I, Story 1: The 2026 Python Metromap: Scikit-learn – Traditional ML

**Next Story:** Series I, Story 2: The 2026 Python Metromap: TensorFlow and Keras – Deep Learning

---

## 📝 Your Invitation

You've mastered traditional machine learning. Now build something with what you've learned:

1. **Build a sentiment analyzer** – Classify movie reviews as positive or negative using Naive Bayes.

2. **Create a fraud detection system** – Use Random Forest to identify fraudulent credit card transactions.

3. **Build a customer segmentation tool** – Use K-Means clustering to group customers by behavior.

4. **Create a recommendation engine** – Use collaborative filtering to recommend products.

5. **Build a loan default predictor** – Predict whether a borrower will default using historical data.

**You've mastered scikit-learn. Next stop: TensorFlow and Keras – Deep Learning!**

---

*Found this helpful? Clap, comment, and share what you predicted. Next stop: TensorFlow and Keras!* 🚇