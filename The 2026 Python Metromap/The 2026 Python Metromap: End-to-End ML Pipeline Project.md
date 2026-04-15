# The 2026 Python Metromap: End-to-End ML Pipeline Project

## Series I: AI & Machine Learning with Python | Story 4 of 4

![The 2026 Python Metromap/images/End-to-End ML Pipeline Project](images/End-to-End ML Pipeline Project.png)

## 📖 Introduction

**Welcome to the final stop on the AI & Machine Learning with Python Line.**

You've conquered Scikit-learn for traditional machine learning. You've mastered TensorFlow and Keras for deep learning. You've unlocked PyTorch for research and custom models. Now it's time to bring everything together into a complete, production-ready machine learning pipeline.

This story—**The 2026 Python Metromap: End-to-End ML Pipeline Project**—is your capstone project for the AI/ML line. We'll build a complete house price prediction system from raw data to deployed API. You'll learn how to structure ML projects professionally, implement data validation pipelines, create reproducible feature engineering, track experiments with MLflow, version models with DVC, containerize with Docker, and deploy a prediction API to the cloud.

This isn't just about writing code—it's about building **production-grade ML systems** that are reliable, maintainable, and scalable. You'll learn industry best practices that data scientists and ML engineers use every day.

**Let's build your first complete ML pipeline.**

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

- 🤖 **The 2026 Python Metromap: Scikit-learn – Traditional ML** – Spam classifier for emails; customer churn predictor; house price estimator.

- 🧠 **The 2026 Python Metromap: TensorFlow and Keras – Deep Learning** – Handwritten digit classifier; fashion item recognizer; sentiment analyzer.

- 🔥 **The 2026 Python Metromap: PyTorch – Research and Production** – Custom neural network for image classification; training loops; model deployment.

- 🚀 **The 2026 Python Metromap: End-to-End ML Pipeline Project** – Complete machine learning pipeline from data collection to deployment for house price prediction. **⬅️ YOU ARE HERE**

### Series J: Capstone Projects (3 Stories) – Next Station

- 💰 **The 2026 Python Metromap: CLI Expense Tracker** – Complete command-line application with OOP categories and transactions; JSON file storage; spending reports; Matplotlib visualization. 🔜 *Up Next*

- 🌤️ **The 2026 Python Metromap: Weather Dashboard** – Flask web application; OpenWeatherMap API integration; Redis caching; HTML/CSS/JS frontend.

- 🎯 **The 2026 Python Metromap: ML-Powered Recommendation Engine** – Full-stack recommendation system with Pandas data processing; Scikit-learn collaborative filtering; Flask API; Docker deployment.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🏗️ Section 1: Project Structure & Configuration

A professional ML project follows a standard structure that separates concerns and makes collaboration easy.

**SOLID Principles Applied:**
- Single Responsibility: Each module has one purpose
- Dependency Inversion: High-level modules depend on abstractions

**Design Pattern: Factory Pattern** – Creates pipeline components

```python
"""
PROJECT STRUCTURE & CONFIGURATION

This section establishes the foundation for our ML pipeline project.

SOLID Principles Applied:
- Single Responsibility: Each module has one purpose
- Dependency Inversion: High-level modules depend on abstractions

Design Pattern: Factory Pattern - Creates pipeline components
"""

# project_structure.py
"""
Complete ML Pipeline Project Structure:

ml_pipeline_project/
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── Makefile
├── docker-compose.yml
├── Dockerfile
├── config/
│   ├── __init__.py
│   ├── config.yaml
│   └── logging.yaml
├── data/
│   ├── raw/              # Original immutable data
│   ├── processed/        # Cleaned and transformed data
│   ├── features/         # Feature-engineered data
│   ├── external/         # External data sources
│   └── models/           # Saved model files
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_selection.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── make_dataset.py
│   │   ├── validate_data.py
│   │   └── preprocess.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── build_features.py
│   │   └── feature_selector.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train_model.py
│   │   ├── predict_model.py
│   │   ├── evaluate_model.py
│   │   └── tune_model.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   └── visualize.py
│   └── api/
│       ├── __init__.py
│       ├── app.py
│       └── schemas.py
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_models.py
│   └── test_api.py
├── scripts/
│   ├── download_data.py
│   └── run_pipeline.py
└── mlflow/
    ├── mlruns/            # MLflow tracking
    └── artifacts/         # Model artifacts
"""

import os
import yaml
import logging
import logging.config
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
import sys


@dataclass
class ProjectConfig:
    """
    Central configuration for the ML pipeline.
    
    Design Pattern: Value Object Pattern - Immutable configuration container
    """
    
    # Paths
    project_root: Path = field(default_factory=lambda: Path(__file__).parent.parent)
    
    # Data paths
    raw_data_path: Path = None
    processed_data_path: Path = None
    features_data_path: Path = None
    models_path: Path = None
    
    # Model parameters
    test_size: float = 0.2
    random_state: int = 42
    n_folds: int = 5
    
    # Training parameters
    model_type: str = "random_forest"  # random_forest, gradient_boosting, xgboost
    hyperparameter_tuning: bool = True
    n_trials: int = 50
    
    # API configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_debug: bool = False
    
    # MLflow
    mlflow_tracking_uri: str = "./mlflow/mlruns"
    experiment_name: str = "house_price_prediction"
    
    def __post_init__(self):
        """Initialize paths after dataclass creation."""
        if self.raw_data_path is None:
            self.raw_data_path = self.project_root / "data" / "raw"
        if self.processed_data_path is None:
            self.processed_data_path = self.project_root / "data" / "processed"
        if self.features_data_path is None:
            self.features_data_path = self.project_root / "data" / "features"
        if self.models_path is None:
            self.models_path = self.project_root / "data" / "models"
        
        # Create directories if they don't exist
        for path in [self.raw_data_path, self.processed_data_path, 
                     self.features_data_path, self.models_path]:
            path.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def from_yaml(cls, yaml_path: Path) -> "ProjectConfig":
        """Load configuration from YAML file."""
        with open(yaml_path, 'r') as f:
            config_dict = yaml.safe_load(f)
        return cls(**config_dict)
    
    def to_yaml(self, yaml_path: Path) -> None:
        """Save configuration to YAML file."""
        config_dict = {
            'test_size': self.test_size,
            'random_state': self.random_state,
            'n_folds': self.n_folds,
            'model_type': self.model_type,
            'hyperparameter_tuning': self.hyperparameter_tuning,
            'n_trials': self.n_trials,
            'api_host': self.api_host,
            'api_port': self.api_port,
            'api_debug': self.api_debug,
            'mlflow_tracking_uri': self.mlflow_tracking_uri,
            'experiment_name': self.experiment_name
        }
        with open(yaml_path, 'w') as f:
            yaml.dump(config_dict, f, default_flow_style=False)


def setup_logging(log_config_path: Optional[Path] = None):
    """
    Setup logging configuration.
    
    Design Pattern: Singleton Pattern - Single logging configuration
    """
    if log_config_path and log_config_path.exists():
        with open(log_config_path, 'r') as f:
            log_config = yaml.safe_load(f)
        logging.config.dictConfig(log_config)
    else:
        # Default logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler('pipeline.log')
            ]
        )
    
    return logging.getLogger(__name__)


class PipelineContext:
    """
    Manages pipeline context and shared resources.
    
    Design Pattern: Context Pattern - Provides shared state across pipeline
    """
    
    def __init__(self, config: ProjectConfig):
        self.config = config
        self.logger = setup_logging()
        self.start_time = None
        self.end_time = None
        self.metrics: Dict[str, Any] = {}
        self.artifacts: Dict[str, Any] = {}
    
    def __enter__(self):
        """Context manager entry."""
        import time
        self.start_time = time.time()
        self.logger.info("Pipeline started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        import time
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        self.logger.info(f"Pipeline completed in {duration:.2f} seconds")
    
    def log_metric(self, name: str, value: float):
        """Log a metric."""
        self.metrics[name] = value
        self.logger.info(f"Metric: {name} = {value}")
    
    def save_artifact(self, name: str, artifact: Any):
        """Save an artifact."""
        self.artifacts[name] = artifact
        self.logger.info(f"Artifact saved: {name}")


def demonstrate_project_structure():
    """
    Demonstrate the project structure and configuration system.
    """
    print("\n" + "=" * 60)
    print("SECTION 1: PROJECT STRUCTURE & CONFIGURATION")
    print("=" * 60)
    
    # Create configuration
    print("\n1. CREATING PROJECT CONFIGURATION")
    print("-" * 40)
    
    config = ProjectConfig(
        test_size=0.15,
        model_type="xgboost",
        hyperparameter_tuning=True,
        n_trials=100
    )
    
    print(f"  Project root: {config.project_root}")
    print(f"  Raw data path: {config.raw_data_path}")
    print(f"  Model type: {config.model_type}")
    print(f"  Test size: {config.test_size}")
    
    # Save config to YAML
    print("\n2. SAVING CONFIGURATION TO YAML")
    print("-" * 40)
    
    config_path = config.project_root / "config" / "config.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config.to_yaml(config_path)
    print(f"  Config saved to: {config_path}")
    
    # Load config from YAML
    print("\n3. LOADING CONFIGURATION FROM YAML")
    print("-" * 40)
    
    loaded_config = ProjectConfig.from_yaml(config_path)
    print(f"  Loaded model type: {loaded_config.model_type}")
    print(f"  Loaded test size: {loaded_config.test_size}")
    
    # Pipeline context
    print("\n4. PIPELINE CONTEXT MANAGER")
    print("-" * 40)
    
    with PipelineContext(config) as ctx:
        ctx.log_metric("data_quality_score", 0.95)
        ctx.log_metric("feature_count", 45)
        ctx.save_artifact("preprocessor", "StandardScaler()")
        
        print(f"  Metrics logged: {list(ctx.metrics.keys())}")
        print(f"  Artifacts saved: {list(ctx.artifacts.keys())}")
    
    # Configuration summary
    print("\n5. CONFIGURATION SUMMARY")
    print("-" * 40)
    
    print(f"\n  {'Parameter':<25} {'Value':<20}")
    print("-" * 45)
    print(f"  {'test_size':<25} {config.test_size:<20}")
    print(f"  {'random_state':<25} {config.random_state:<20}")
    print(f"  {'model_type':<25} {config.model_type:<20}")
    print(f"  {'hyperparameter_tuning':<25} {config.hyperparameter_tuning:<20}")
    print(f"  {'n_trials':<25} {config.n_trials:<20}")
    print(f"  {'api_port':<25} {config.api_port:<20}")


if __name__ == "__main__":
    demonstrate_project_structure()
```

---

## 📊 Section 2: Data Collection & Validation

Load, validate, and clean the dataset with automated quality checks.

**SOLID Principles Applied:**
- Single Responsibility: Separate loading, validation, and cleaning
- Open/Closed: New validation rules can be added

**Design Pattern: Strategy Pattern** – Different validation strategies

```python
"""
DATA COLLECTION & VALIDATION

This section handles data loading, validation, and cleaning.

SOLID Principles Applied:
- Single Responsibility: Separate loading, validation, and cleaning
- Open/Closed: New validation rules can be added

Design Pattern: Strategy Pattern - Different validation strategies
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from sklearn.model_selection import train_test_split
import logging
from pathlib import Path
import requests
import zipfile
import io


@dataclass
class DataValidationResult:
    """
    Container for data validation results.
    
    Design Pattern: Value Object Pattern - Immutable validation results
    """
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    statistics: Dict[str, Any] = field(default_factory=dict)


class DataValidator:
    """
    Validates dataset quality and integrity.
    
    Design Pattern: Strategy Pattern - Pluggable validation rules
    """
    
    def __init__(self):
        self.rules: List[Callable] = []
        self._setup_default_rules()
    
    def _setup_default_rules(self):
        """Setup default validation rules."""
        self.rules = [
            self.check_missing_values,
            self.check_duplicates,
            self.check_outliers,
            self.check_data_types,
            self.check_target_distribution
        ]
    
    def add_rule(self, rule: Callable):
        """Add custom validation rule."""
        self.rules.append(rule)
    
    def check_missing_values(self, df: pd.DataFrame, target_col: str = None) -> Tuple[bool, str]:
        """Check for missing values."""
        missing_counts = df.isnull().sum()
        missing_cols = missing_counts[missing_counts > 0]
        
        if len(missing_cols) > 0:
            missing_report = ", ".join([f"{col}: {count}" for col, count in missing_cols.items()])
            return False, f"Missing values found: {missing_report}"
        return True, "No missing values"
    
    def check_duplicates(self, df: pd.DataFrame, target_col: str = None) -> Tuple[bool, str]:
        """Check for duplicate rows."""
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            return False, f"Found {duplicates} duplicate rows"
        return True, "No duplicate rows"
    
    def check_outliers(self, df: pd.DataFrame, target_col: str = None, 
                       threshold: float = 3) -> Tuple[bool, str]:
        """Check for outliers using Z-score."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        outlier_counts = {}
        
        for col in numeric_cols:
            z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
            outliers = (z_scores > threshold).sum()
            if outliers > 0:
                outlier_counts[col] = outliers
        
        if outlier_counts:
            report = ", ".join([f"{col}: {count}" for col, count in outlier_counts.items()])
            return False, f"Outliers detected: {report}"
        return True, "No significant outliers"
    
    def check_data_types(self, df: pd.DataFrame, target_col: str = None) -> Tuple[bool, str]:
        """Check for correct data types."""
        issues = []
        for col in df.columns:
            if df[col].dtype == 'object':
                # Check if numeric column is stored as object
                try:
                    pd.to_numeric(df[col])
                    issues.append(f"{col} should be numeric but is object")
                except:
                    pass
        if issues:
            return False, "; ".join(issues)
        return True, "Data types are appropriate"
    
    def check_target_distribution(self, df: pd.DataFrame, target_col: str) -> Tuple[bool, str]:
        """Check target variable distribution."""
        if target_col not in df.columns:
            return False, f"Target column '{target_col}' not found"
        
        target = df[target_col]
        
        # Check for constant target
        if target.nunique() == 1:
            return False, "Target variable is constant"
        
        # Check for severe imbalance (for classification)
        if target.dtype == 'object' or target.nunique() < 10:
            value_counts = target.value_counts()
            max_ratio = value_counts.max() / value_counts.sum()
            if max_ratio > 0.9:
                return False, f"Target is severely imbalanced (max ratio: {max_ratio:.2f})"
        
        return True, "Target distribution is acceptable"
    
    def validate(self, df: pd.DataFrame, target_col: str = None) -> DataValidationResult:
        """
        Run all validation rules.
        """
        errors = []
        warnings = []
        statistics = {
            'shape': df.shape,
            'missing_total': df.isnull().sum().sum(),
            'duplicates': df.duplicated().sum(),
            'numeric_columns': len(df.select_dtypes(include=[np.number]).columns),
            'categorical_columns': len(df.select_dtypes(include=['object']).columns)
        }
        
        for rule in self.rules:
            try:
                is_valid, message = rule(df, target_col)
                if not is_valid:
                    errors.append(message)
                else:
                    warnings.append(message)
            except Exception as e:
                errors.append(f"Rule {rule.__name__} failed: {str(e)}")
        
        return DataValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            statistics=statistics
        )


class DataLoader:
    """
    Loads data from various sources.
    
    Design Pattern: Factory Pattern - Creates dataframes from different sources
    """
    
    @staticmethod
    def load_ames_housing() -> pd.DataFrame:
        """
        Load the Ames Housing dataset.
        
        This dataset contains house sale prices for King County,
        including homes sold between May 2014 and May 2015.
        """
        # For demonstration, we'll create a synthetic dataset
        # In production, you would load from a real source
        np.random.seed(42)
        n_samples = 1000
        
        data = {
            'MSSubClass': np.random.choice([20, 30, 40, 45, 50], n_samples),
            'MSZoning': np.random.choice(['RL', 'RM', 'FV', 'RH'], n_samples),
            'LotFrontage': np.random.normal(70, 20, n_samples),
            'LotArea': np.random.normal(10000, 3000, n_samples),
            'Street': np.random.choice(['Pave', 'Grvl'], n_samples, p=[0.95, 0.05]),
            'Alley': np.random.choice(['Grvl', 'Pave', None], n_samples, p=[0.1, 0.05, 0.85]),
            'LotShape': np.random.choice(['Reg', 'IR1', 'IR2', 'IR3'], n_samples),
            'LandContour': np.random.choice(['Lvl', 'Bnk', 'HLS', 'Low'], n_samples),
            'Utilities': np.random.choice(['AllPub', 'NoSewr'], n_samples, p=[0.99, 0.01]),
            'LotConfig': np.random.choice(['Inside', 'Corner', 'CulDSac', 'FR2', 'FR3'], n_samples),
            'LandSlope': np.random.choice(['Gtl', 'Mod', 'Sev'], n_samples),
            'Neighborhood': np.random.choice(['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst'], n_samples),
            'Condition1': np.random.choice(['Norm', 'Feedr', 'PosN', 'Artery', 'RRAe'], n_samples),
            'Condition2': np.random.choice(['Norm', 'Feedr', 'PosN'], n_samples),
            'BldgType': np.random.choice(['1Fam', '2FmCon', 'Duplex', 'TwnhsE', 'Twnhs'], n_samples),
            'HouseStyle': np.random.choice(['1Story', '2Story', '1.5Fin', 'SFoyer', 'SLvl'], n_samples),
            'OverallQual': np.random.choice(range(1, 11), n_samples, p=[0.02, 0.03, 0.05, 0.08, 0.12, 0.15, 0.18, 0.15, 0.12, 0.10]),
            'OverallCond': np.random.choice(range(1, 11), n_samples, p=[0.03, 0.04, 0.06, 0.09, 0.12, 0.14, 0.16, 0.14, 0.12, 0.10]),
            'YearBuilt': np.random.choice(range(1900, 2010), n_samples),
            'YearRemodAdd': np.random.choice(range(1950, 2010), n_samples),
            'RoofStyle': np.random.choice(['Gable', 'Hip', 'Gambrel', 'Mansard'], n_samples),
            'RoofMatl': np.random.choice(['CompShg', 'WdShngl', 'Metal', 'Tar&Grv'], n_samples),
            'Exterior1st': np.random.choice(['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'Plywood'], n_samples),
            'Exterior2nd': np.random.choice(['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'Plywood'], n_samples),
            'MasVnrType': np.random.choice(['None', 'BrkFace', 'Stone', 'BrkCmn'], n_samples, p=[0.6, 0.2, 0.15, 0.05]),
            'MasVnrArea': np.random.normal(100, 80, n_samples),
            'ExterQual': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', 'Po'], n_samples, p=[0.1, 0.4, 0.4, 0.08, 0.02]),
            'ExterCond': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', 'Po'], n_samples, p=[0.05, 0.35, 0.5, 0.08, 0.02]),
            'Foundation': np.random.choice(['PConc', 'CBlock', 'BrkTil', 'Slab', 'Stone'], n_samples),
            'BsmtQual': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', None], n_samples, p=[0.1, 0.3, 0.4, 0.1, 0.1]),
            'BsmtCond': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', None], n_samples, p=[0.05, 0.25, 0.5, 0.1, 0.1]),
            'BsmtExposure': np.random.choice(['Gd', 'Av', 'Mn', 'No', None], n_samples, p=[0.1, 0.2, 0.2, 0.4, 0.1]),
            'BsmtFinType1': np.random.choice(['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', None], n_samples),
            'BsmtFinSF1': np.random.normal(500, 300, n_samples),
            'BsmtFinType2': np.random.choice(['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', None], n_samples),
            'BsmtFinSF2': np.random.normal(100, 150, n_samples),
            'BsmtUnfSF': np.random.normal(300, 200, n_samples),
            'TotalBsmtSF': np.random.normal(1000, 400, n_samples),
            'Heating': np.random.choice(['GasA', 'GasW', 'Wall', 'OthW'], n_samples),
            'HeatingQC': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', 'Po'], n_samples),
            'CentralAir': np.random.choice(['Y', 'N'], n_samples, p=[0.95, 0.05]),
            'Electrical': np.random.choice(['SBrkr', 'FuseF', 'FuseA', 'Mix'], n_samples),
            '1stFlrSF': np.random.normal(1200, 400, n_samples),
            '2ndFlrSF': np.random.normal(600, 300, n_samples),
            'LowQualFinSF': np.random.normal(50, 100, n_samples),
            'GrLivArea': np.random.normal(1500, 400, n_samples),
            'BsmtFullBath': np.random.choice(range(0, 3), n_samples),
            'BsmtHalfBath': np.random.choice(range(0, 2), n_samples),
            'FullBath': np.random.choice(range(1, 4), n_samples),
            'HalfBath': np.random.choice(range(0, 2), n_samples),
            'BedroomAbvGr': np.random.choice(range(1, 5), n_samples),
            'KitchenAbvGr': np.random.choice(range(1, 3), n_samples),
            'KitchenQual': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', 'Po'], n_samples),
            'TotRmsAbvGrd': np.random.choice(range(4, 11), n_samples),
            'Functional': np.random.choice(['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2'], n_samples),
            'Fireplaces': np.random.choice(range(0, 3), n_samples),
            'FireplaceQu': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', None], n_samples, p=[0.05, 0.15, 0.4, 0.1, 0.3]),
            'GarageType': np.random.choice(['Attchd', 'Detchd', 'BuiltIn', 'CarPort', None], n_samples),
            'GarageYrBlt': np.random.choice(range(1900, 2010), n_samples),
            'GarageFinish': np.random.choice(['Fin', 'RFn', 'Unf', None], n_samples),
            'GarageCars': np.random.choice(range(0, 4), n_samples),
            'GarageArea': np.random.normal(400, 200, n_samples),
            'GarageQual': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', None], n_samples),
            'GarageCond': np.random.choice(['Ex', 'Gd', 'TA', 'Fa', None], n_samples),
            'PavedDrive': np.random.choice(['Y', 'P', 'N'], n_samples, p=[0.7, 0.2, 0.1]),
            'WoodDeckSF': np.random.normal(100, 150, n_samples),
            'OpenPorchSF': np.random.normal(50, 80, n_samples),
            'EnclosedPorch': np.random.normal(30, 60, n_samples),
            '3SsnPorch': np.random.normal(20, 50, n_samples),
            'ScreenPorch': np.random.normal(40, 70, n_samples),
            'PoolArea': np.random.normal(0, 50, n_samples),
            'PoolQC': np.random.choice(['Ex', 'Gd', 'TA', None], n_samples, p=[0.01, 0.02, 0.03, 0.94]),
            'Fence': np.random.choice(['GdPrv', 'MnPrv', 'GdWo', 'MnWw', None], n_samples, p=[0.05, 0.1, 0.05, 0.1, 0.7]),
            'MiscFeature': np.random.choice(['Shed', 'Gar2', 'Othr', None], n_samples, p=[0.05, 0.02, 0.01, 0.92]),
            'MiscVal': np.random.normal(0, 200, n_samples),
            'MoSold': np.random.choice(range(1, 13), n_samples),
            'YrSold': np.random.choice([2010, 2011, 2012, 2013, 2014], n_samples),
            'SaleType': np.random.choice(['WD', 'CWD', 'New', 'COD', 'Con'], n_samples),
            'SaleCondition': np.random.choice(['Normal', 'Abnorml', 'Partial', 'AdjLand', 'Alloca'], n_samples),
            'SalePrice': np.random.normal(180000, 50000, n_samples)  # Target variable
        }
        
        df = pd.DataFrame(data)
        
        # Add realistic relationships
        df['SalePrice'] = (
            df['OverallQual'] * 15000 +
            df['GrLivArea'] * 50 +
            df['TotalBsmtSF'] * 30 +
            df['GarageArea'] * 20 +
            df['FullBath'] * 5000 +
            df['BedroomAbvGr'] * 3000 +
            np.random.normal(0, 20000, n_samples)
        )
        
        # Ensure positive prices
        df['SalePrice'] = df['SalePrice'].clip(lower=50000, upper=800000)
        
        return df
    
    @staticmethod
    def load_from_csv(filepath: Path) -> pd.DataFrame:
        """Load data from CSV file."""
        return pd.read_csv(filepath)
    
    @staticmethod
    def load_from_url(url: str) -> pd.DataFrame:
        """Load data from URL."""
        response = requests.get(url)
        return pd.read_csv(io.StringIO(response.text))


class DataPreprocessor:
    """
    Preprocesses and cleans the dataset.
    
    Design Pattern: Pipeline Pattern - Chains preprocessing steps
    """
    
    def __init__(self):
        self.steps: List[Tuple[str, Callable]] = []
    
    def add_step(self, name: str, func: Callable):
        """Add a preprocessing step."""
        self.steps.append((name, func))
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: str = 'median') -> pd.DataFrame:
        """
        Handle missing values with various strategies.
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        if strategy == 'median':
            fill_value = df[numeric_cols].median()
        elif strategy == 'mean':
            fill_value = df[numeric_cols].mean()
        elif strategy == 'zero':
            fill_value = 0
        else:
            return df
        
        df[numeric_cols] = df[numeric_cols].fillna(fill_value)
        
        # For categorical columns, fill with mode
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df[col] = df[col].fillna(df[col].mode()[0] if len(df[col].mode()) > 0 else 'Unknown')
        
        return df
    
    def remove_outliers(self, df: pd.DataFrame, threshold: float = 3) -> pd.DataFrame:
        """
        Remove outliers using Z-score.
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        z_scores = np.abs((df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std())
        mask = (z_scores < threshold).all(axis=1)
        return df[mask]
    
    def encode_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Encode categorical variables.
        """
        from sklearn.preprocessing import LabelEncoder
        
        categorical_cols = df.select_dtypes(include=['object']).columns
        df_encoded = df.copy()
        
        for col in categorical_cols:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        
        return df_encoded
    
    def scale_features(self, df: pd.DataFrame, target_col: str = None) -> pd.DataFrame:
        """
        Scale numerical features.
        """
        from sklearn.preprocessing import StandardScaler
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if target_col and target_col in numeric_cols:
            numeric_cols = numeric_cols.drop(target_col)
        
        scaler = StandardScaler()
        df_scaled = df.copy()
        df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        
        return df_scaled, scaler
    
    def process(self, df: pd.DataFrame, target_col: str = None, 
                handle_missing: bool = True, remove_outliers: bool = False,
                encode_categorical: bool = True, scale_features: bool = False) -> Tuple[pd.DataFrame, Dict]:
        """
        Run complete preprocessing pipeline.
        """
        metadata = {'original_shape': df.shape}
        df_processed = df.copy()
        
        if handle_missing:
            df_processed = self.handle_missing_values(df_processed)
            metadata['missing_handled'] = True
        
        if remove_outliers and target_col:
            df_processed = self.remove_outliers(df_processed)
            metadata['outliers_removed'] = True
            metadata['new_shape'] = df_processed.shape
        
        if encode_categorical:
            df_processed = self.encode_categorical(df_processed)
            metadata['categorical_encoded'] = True
        
        scaler = None
        if scale_features:
            df_processed, scaler = self.scale_features(df_processed, target_col)
            metadata['features_scaled'] = True
        
        return df_processed, {'metadata': metadata, 'scaler': scaler}


def demonstrate_data_pipeline():
    """
    Demonstrate complete data pipeline.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: DATA COLLECTION & VALIDATION")
    print("=" * 60)
    
    # LOAD DATA
    print("\n1. LOADING DATA")
    print("-" * 40)
    
    loader = DataLoader()
    df = loader.load_ames_housing()
    
    print(f"  Dataset shape: {df.shape}")
    print(f"  Columns: {list(df.columns[:10])}...")
    print(f"  Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    # VALIDATE DATA
    print("\n2. VALIDATING DATA")
    print("-" * 40)
    
    validator = DataValidator()
    validation_result = validator.validate(df, target_col='SalePrice')
    
    print(f"  Is valid: {validation_result.is_valid}")
    print(f"  Errors: {len(validation_result.errors)}")
    print(f"  Warnings: {len(validation_result.warnings)}")
    print(f"  Statistics: {validation_result.statistics}")
    
    if validation_result.errors:
        print(f"  Sample error: {validation_result.errors[0]}")
    
    # PREPROCESS DATA
    print("\n3. PREPROCESSING DATA")
    print("-" * 40)
    
    preprocessor = DataPreprocessor()
    df_processed, preprocess_metadata = preprocessor.process(
        df, 
        target_col='SalePrice',
        handle_missing=True,
        remove_outliers=False,
        encode_categorical=True,
        scale_features=False
    )
    
    print(f"  Processed shape: {df_processed.shape}")
    print(f"  Missing values after: {df_processed.isnull().sum().sum()}")
    print(f"  Data types: {df_processed.dtypes.value_counts().to_dict()}")
    
    # TRAIN-TEST SPLIT
    print("\n4. TRAIN-TEST SPLIT")
    print("-" * 40)
    
    X = df_processed.drop('SalePrice', axis=1)
    y = df_processed['SalePrice']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"  Training set: {X_train.shape}")
    print(f"  Test set: {X_test.shape}")
    print(f"  Target mean (train): ${y_train.mean():,.2f}")
    print(f"  Target std (train): ${y_train.std():,.2f}")
    
    # DATA SUMMARY
    print("\n5. DATA SUMMARY REPORT")
    print("-" * 40)
    
    print(f"\n  {'Metric':<25} {'Value':<20}")
    print("-" * 45)
    print(f"  {'Total samples':<25} {len(df):<20}")
    print(f"  {'Features':<25} {len(df.columns) - 1:<20}")
    print(f"  {'Missing values %':<25} {df.isnull().sum().sum() / df.size * 100:.2f}%")
    print(f"  {'Numeric features':<25} {len(df.select_dtypes(include=[np.number]).columns):<20}")
    print(f"  {'Categorical features':<25} {len(df.select_dtypes(include=['object']).columns):<20}")
    print(f"  {'Price range':<25} ${df['SalePrice'].min():,.0f} - ${df['SalePrice'].max():,.0f}")
    
    return X_train, X_test, y_train, y_test, preprocessor


if __name__ == "__main__":
    X_train, X_test, y_train, y_test, preprocessor = demonstrate_data_pipeline()
```

---

## 🤖 Section 3: Feature Engineering & Model Training

Build features and train multiple models with hyperparameter tuning.

**SOLID Principles Applied:**
- Single Responsibility: Separate feature engineering from model training
- Open/Closed: New features and models can be added

**Design Pattern: Strategy Pattern** – Interchangeable feature engineering strategies

```python
"""
FEATURE ENGINEERING & MODEL TRAINING

This section implements feature engineering and model training with MLflow tracking.

SOLID Principles Applied:
- Single Responsibility: Separate feature engineering from model training
- Open/Closed: New features and models can be added

Design Pattern: Strategy Pattern - Interchangeable feature engineering strategies
"""

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
import xgboost as xgb
import lightgbm as lgb
import mlflow
import mlflow.sklearn
from typing import Dict, Any, List, Tuple, Optional
import joblib
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


class FeatureEngineer:
    """
    Advanced feature engineering with domain knowledge.
    
    Design Pattern: Builder Pattern - Builds features incrementally
    """
    
    def __init__(self):
        self.created_features = []
    
    def create_polynomial_features(self, df: pd.DataFrame, cols: List[str], degree: int = 2) -> pd.DataFrame:
        """Create polynomial features for numeric columns."""
        df_copy = df.copy()
        for col in cols:
            if col in df.columns:
                for d in range(2, degree + 1):
                    new_col = f"{col}_poly_{d}"
                    df_copy[new_col] = df_copy[col] ** d
                    self.created_features.append(new_col)
        return df_copy
    
    def create_interaction_features(self, df: pd.DataFrame, interactions: List[Tuple[str, str]]) -> pd.DataFrame:
        """Create interaction features between pairs of columns."""
        df_copy = df.copy()
        for col1, col2 in interactions:
            if col1 in df.columns and col2 in df.columns:
                new_col = f"{col1}_x_{col2}"
                df_copy[new_col] = df_copy[col1] * df_copy[col2]
                self.created_features.append(new_col)
        return df_copy
    
    def create_aggregate_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create aggregate features based on domain knowledge."""
        df_copy = df.copy()
        
        # Total square footage
        if all(col in df.columns for col in ['GrLivArea', 'TotalBsmtSF', 'GarageArea']):
            df_copy['TotalSF'] = df_copy['GrLivArea'] + df_copy['TotalBsmtSF'] + df_copy['GarageArea']
            self.created_features.append('TotalSF')
        
        # Total bathrooms
        if all(col in df.columns for col in ['FullBath', 'HalfBath', 'BsmtFullBath', 'BsmtHalfBath']):
            df_copy['TotalBath'] = (df_copy['FullBath'] + 0.5 * df_copy['HalfBath'] + 
                                    df_copy['BsmtFullBath'] + 0.5 * df_copy['BsmtHalfBath'])
            self.created_features.append('TotalBath')
        
        # Age of house at sale
        if 'YearBuilt' in df.columns and 'YrSold' in df.columns:
            df_copy['HouseAge'] = df_copy['YrSold'] - df_copy['YearBuilt']
            self.created_features.append('HouseAge')
        
        # Remodel age
        if 'YearRemodAdd' in df.columns and 'YrSold' in df.columns:
            df_copy['RemodelAge'] = df_copy['YrSold'] - df_copy['YearRemodAdd']
            self.created_features.append('RemodelAge')
        
        # Quality score
        if 'OverallQual' in df.columns:
            df_copy['QualityScore'] = df_copy['OverallQual'] ** 2
            self.created_features.append('QualityScore')
        
        # Has basement
        if 'TotalBsmtSF' in df.columns:
            df_copy['HasBasement'] = (df_copy['TotalBsmtSF'] > 0).astype(int)
            self.created_features.append('HasBasement')
        
        # Has garage
        if 'GarageArea' in df.columns:
            df_copy['HasGarage'] = (df_copy['GarageArea'] > 0).astype(int)
            self.created_features.append('HasGarage')
        
        # Has fireplace
        if 'Fireplaces' in df.columns:
            df_copy['HasFireplace'] = (df_copy['Fireplaces'] > 0).astype(int)
            self.created_features.append('HasFireplace')
        
        return df_copy
    
    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create all features."""
        df_features = df.copy()
        
        # Create aggregate features
        df_features = self.create_aggregate_features(df_features)
        
        # Create polynomial features for important numeric columns
        important_numeric = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'GarageArea']
        existing_cols = [col for col in important_numeric if col in df_features.columns]
        df_features = self.create_polynomial_features(df_features, existing_cols, degree=2)
        
        # Create interaction features
        interactions = [
            ('OverallQual', 'GrLivArea'),
            ('OverallQual', 'TotalBsmtSF'),
            ('GrLivArea', 'GarageArea')
        ]
        existing_interactions = [(c1, c2) for c1, c2 in interactions 
                                if c1 in df_features.columns and c2 in df_features.columns]
        df_features = self.create_interaction_features(df_features, existing_interactions)
        
        return df_features


class ModelFactory:
    """
    Factory for creating and managing ML models.
    
    Design Pattern: Factory Pattern - Creates model instances
    """
    
    @staticmethod
    def create_model(model_name: str, **kwargs) -> BaseEstimator:
        """Create a model by name."""
        models = {
            'random_forest': RandomForestRegressor,
            'gradient_boosting': GradientBoostingRegressor,
            'xgboost': xgb.XGBRegressor,
            'lightgbm': lgb.LGBMRegressor,
            'ridge': Ridge,
            'lasso': Lasso,
            'elastic_net': ElasticNet,
            'svr': SVR
        }
        
        if model_name not in models:
            raise ValueError(f"Model {model_name} not found. Available: {list(models.keys())}")
        
        # Default parameters
        default_params = {
            'random_forest': {'n_estimators': 100, 'random_state': 42},
            'gradient_boosting': {'n_estimators': 100, 'random_state': 42},
            'xgboost': {'n_estimators': 100, 'random_state': 42, 'verbosity': 0},
            'lightgbm': {'n_estimators': 100, 'random_state': 42, 'verbose': -1},
            'ridge': {'alpha': 1.0},
            'lasso': {'alpha': 1.0},
            'elastic_net': {'alpha': 1.0, 'l1_ratio': 0.5},
            'svr': {'kernel': 'rbf', 'C': 1.0}
        }
        
        params = {**default_params.get(model_name, {}), **kwargs}
        return models[model_name](**params)
    
    @staticmethod
    def get_hyperparameter_grid(model_name: str) -> Dict:
        """Get hyperparameter grid for tuning."""
        grids = {
            'random_forest': {
                'n_estimators': [100, 200, 300],
                'max_depth': [10, 20, 30, None],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            },
            'gradient_boosting': {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7],
                'min_samples_split': [2, 5]
            },
            'xgboost': {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7],
                'subsample': [0.8, 0.9, 1.0],
                'colsample_bytree': [0.8, 0.9, 1.0]
            },
            'lightgbm': {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.05, 0.1],
                'num_leaves': [31, 50, 100],
                'max_depth': [-1, 10, 20]
            }
        }
        return grids.get(model_name, {})


class ModelTrainer:
    """
    Trains and evaluates models with MLflow tracking.
    
    Design Pattern: Template Method Pattern - Defines training workflow
    """
    
    def __init__(self, experiment_name: str = "house_price_prediction"):
        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)
        self.best_model = None
        self.best_score = float('inf')
        self.results = {}
    
    def train_model(self, X_train: pd.DataFrame, y_train: pd.Series,
                    model_name: str, params: Dict = None,
                    cv_folds: int = 5) -> BaseEstimator:
        """
        Train a single model with cross-validation.
        """
        model = ModelFactory.create_model(model_name, **(params or {}))
        
        # Cross-validation
        cv_scores = cross_val_score(model, X_train, y_train, 
                                    cv=cv_folds, scoring='neg_mean_squared_error')
        cv_rmse = np.sqrt(-cv_scores.mean())
        cv_std = np.sqrt(-cv_scores).std()
        
        # Train on full training set
        model.fit(X_train, y_train)
        
        return model, cv_rmse, cv_std
    
    def tune_hyperparameters(self, X_train: pd.DataFrame, y_train: pd.Series,
                            model_name: str, n_trials: int = 50,
                            cv_folds: int = 5) -> Tuple[BaseEstimator, Dict]:
        """
        Tune hyperparameters using randomized search.
        """
        model = ModelFactory.create_model(model_name)
        param_grid = ModelFactory.get_hyperparameter_grid(model_name)
        
        if not param_grid:
            return model, {}
        
        random_search = RandomizedSearchCV(
            model, param_grid, n_iter=n_trials, cv=cv_folds,
            scoring='neg_mean_squared_error', random_state=42,
            n_jobs=-1, verbose=0
        )
        
        random_search.fit(X_train, y_train)
        
        return random_search.best_estimator_, random_search.best_params_
    
    def train_multiple_models(self, X_train: pd.DataFrame, y_train: pd.Series,
                              models: List[str], tune: bool = True,
                              n_trials: int = 50) -> Dict:
        """
        Train and compare multiple models.
        """
        results = {}
        
        for model_name in models:
            print(f"\n  Training {model_name}...")
            
            with mlflow.start_run(run_name=model_name):
                # Log parameters
                mlflow.log_param("model_name", model_name)
                mlflow.log_param("tuning_performed", tune)
                
                if tune:
                    model, best_params = self.tune_hyperparameters(
                        X_train, y_train, model_name, n_trials
                    )
                    mlflow.log_params(best_params)
                else:
                    model, cv_rmse, cv_std = self.train_model(
                        X_train, y_train, model_name
                    )
                    best_params = {}
                    cv_rmse = None
                
                # Train final model
                model.fit(X_train, y_train)
                
                # Log model
                mlflow.sklearn.log_model(model, model_name)
                
                results[model_name] = {
                    'model': model,
                    'best_params': best_params,
                    'cv_rmse': cv_rmse if not tune else None
                }
                
                print(f"    Model trained successfully")
        
        return results
    
    def evaluate_models(self, models: Dict, X_test: pd.DataFrame, 
                        y_test: pd.Series) -> pd.DataFrame:
        """
        Evaluate all trained models.
        """
        evaluation_results = []
        
        for model_name, model_info in models.items():
            model = model_info['model']
            y_pred = model.predict(X_test)
            
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # Calculate percentage errors
            mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
            
            evaluation_results.append({
                'Model': model_name,
                'RMSE': rmse,
                'MAE': mae,
                'R²': r2,
                'MAPE (%)': mape
            })
            
            # Log to MLflow
            with mlflow.start_run(run_name=f"eval_{model_name}", nested=True):
                mlflow.log_metrics({
                    'rmse': rmse,
                    'mae': mae,
                    'r2': r2,
                    'mape': mape
                })
        
        results_df = pd.DataFrame(evaluation_results)
        results_df = results_df.sort_values('RMSE')
        
        # Select best model
        self.best_model = models[results_df.iloc[0]['Model']]['model']
        self.best_score = results_df.iloc[0]['RMSE']
        
        return results_df


def create_ml_pipeline(preprocessor: DataPreprocessor = None, 
                       feature_engineer: FeatureEngineer = None,
                       model: BaseEstimator = None) -> Pipeline:
    """
    Create a complete ML pipeline.
    
    Design Pattern: Pipeline Pattern - Chains preprocessing and modeling
    """
    steps = []
    
    if preprocessor:
        steps.append(('preprocessor', preprocessor))
    
    if feature_engineer:
        steps.append(('feature_engineer', feature_engineer))
    
    if model:
        steps.append(('model', model))
    
    return Pipeline(steps) if steps else None


def demonstrate_model_training():
    """
    Demonstrate complete model training pipeline.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: FEATURE ENGINEERING & MODEL TRAINING")
    print("=" * 60)
    
    # Load and prepare data
    print("\n1. PREPARING DATA")
    print("-" * 40)
    
    loader = DataLoader()
    df = loader.load_ames_housing()
    
    preprocessor = DataPreprocessor()
    df_processed, _ = preprocessor.process(
        df, target_col='SalePrice',
        handle_missing=True,
        encode_categorical=True
    )
    
    # Feature engineering
    print("\n2. FEATURE ENGINEERING")
    print("-" * 40)
    
    feature_engineer = FeatureEngineer()
    df_features = feature_engineer.create_features(df_processed)
    
    print(f"  Original features: {df_processed.shape[1]}")
    print(f"  Features after engineering: {df_features.shape[1]}")
    print(f"  New features created: {len(feature_engineer.created_features)}")
    print(f"  New features: {feature_engineer.created_features[:5]}...")
    
    # Split data
    X = df_features.drop('SalePrice', axis=1)
    y = df_features['SalePrice']
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train multiple models
    print("\n3. TRAINING MODELS")
    print("-" * 40)
    
    trainer = ModelTrainer()
    models_to_train = ['random_forest', 'gradient_boosting', 'xgboost', 'lightgbm']
    
    trained_models = trainer.train_multiple_models(
        X_train, y_train, models_to_train, tune=True, n_trials=20
    )
    
    # Evaluate models
    print("\n4. MODEL EVALUATION")
    print("-" * 40)
    
    results_df = trainer.evaluate_models(trained_models, X_test, y_test)
    
    print("\n  Model Performance Comparison:")
    print(results_df.to_string(index=False))
    
    # Feature importance
    print("\n5. FEATURE IMPORTANCE")
    print("-" * 40)
    
    best_model_name = results_df.iloc[0]['Model']
    best_model = trained_models[best_model_name]['model']
    
    if hasattr(best_model, 'feature_importances_'):
        importances = best_model.feature_importances_
        feature_names = X.columns
        
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances
        }).sort_values('importance', ascending=False).head(10)
        
        print(f"\n  Top 10 features for {best_model_name}:")
        for idx, row in importance_df.iterrows():
            print(f"    {row['feature']}: {row['importance']:.4f}")
    
    # Save best model
    print("\n6. SAVING BEST MODEL")
    print("-" * 40)
    
    model_path = Path("data/models/best_model.pkl")
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_model, model_path)
    print(f"  Best model saved to: {model_path}")
    print(f"  Best model: {best_model_name}")
    print(f"  RMSE: ${results_df.iloc[0]['RMSE']:,.2f}")
    print(f"  R²: {results_df.iloc[0]['R²']:.4f}")
    
    return best_model, results_df, feature_engineer


if __name__ == "__main__":
    best_model, results_df, feature_engineer = demonstrate_model_training()
```

---

## 🚀 Section 4: Model Deployment & API

Deploy the trained model as a REST API using FastAPI with Docker.

**SOLID Principles Applied:**
- Single Responsibility: API layer separate from model logic
- Dependency Inversion: API depends on model abstraction

**Design Pattern: Facade Pattern** – Simplifies model inference interface

```python
"""
MODEL DEPLOYMENT & API

This section deploys the trained model as a REST API.

SOLID Principles Applied:
- Single Responsibility: API layer separate from model logic
- Dependency Inversion: API depends on model abstraction

Design Pattern: Facade Pattern - Simplifies model inference interface
"""

# app.py - FastAPI application
"""
FastAPI application for house price prediction.
Run with: uvicorn app:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd
import joblib
from pathlib import Path
import logging
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="House Price Prediction API",
    description="ML model for predicting house prices based on property features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class HouseFeatures(BaseModel):
    """House features for prediction."""
    
    # Basic features
    MSSubClass: int = Field(..., description="Building class", ge=20, le=190)
    MSZoning: str = Field(..., description="Zoning classification")
    LotFrontage: float = Field(..., description="Linear feet of street connected to property", ge=0)
    LotArea: float = Field(..., description="Lot size in square feet", ge=0)
    
    # Quality and condition
    OverallQual: int = Field(..., description="Overall material and finish quality", ge=1, le=10)
    OverallCond: int = Field(..., description="Overall condition rating", ge=1, le=10)
    
    # Size features
    YearBuilt: int = Field(..., description="Original construction date", ge=1800, le=2026)
    YearRemodAdd: int = Field(..., description="Remodel date", ge=1800, le=2026)
    
    # Area features
    GrLivArea: float = Field(..., description="Above grade living area square feet", ge=0)
    TotalBsmtSF: float = Field(..., description="Total square feet of basement area", ge=0)
    GarageArea: float = Field(..., description="Size of garage in square feet", ge=0)
    
    # Room counts
    FullBath: int = Field(..., description="Full bathrooms above grade", ge=0, le=4)
    HalfBath: int = Field(..., description="Half bathrooms above grade", ge=0, le=2)
    BedroomAbvGr: int = Field(..., description="Bedrooms above grade", ge=0, le=8)
    
    # Additional features
    Fireplaces: int = Field(..., description="Number of fireplaces", ge=0, le=4)
    GarageCars: int = Field(..., description="Size of garage in car capacity", ge=0, le=4)
    
    # Sale information
    MoSold: int = Field(..., description="Month sold", ge=1, le=12)
    YrSold: int = Field(..., description="Year sold", ge=2000, le=2026)
    
    class Config:
        schema_extra = {
            "example": {
                "MSSubClass": 60,
                "MSZoning": "RL",
                "LotFrontage": 70,
                "LotArea": 10000,
                "OverallQual": 7,
                "OverallCond": 5,
                "YearBuilt": 2000,
                "YearRemodAdd": 2005,
                "GrLivArea": 1500,
                "TotalBsmtSF": 800,
                "GarageArea": 400,
                "FullBath": 2,
                "HalfBath": 1,
                "BedroomAbvGr": 3,
                "Fireplaces": 1,
                "GarageCars": 2,
                "MoSold": 6,
                "YrSold": 2020
            }
        }
    
    @validator('MSZoning')
    def validate_zoning(cls, v):
        valid_zoning = ['RL', 'RM', 'FV', 'RH', 'C (all)']
        if v not in valid_zoning:
            raise ValueError(f'MSZoning must be one of {valid_zoning}')
        return v


class PredictionRequest(BaseModel):
    """Request model for single prediction."""
    features: HouseFeatures


class BatchPredictionRequest(BaseModel):
    """Request model for batch predictions."""
    features: List[HouseFeatures]


class PredictionResponse(BaseModel):
    """Response model for predictions."""
    predicted_price: float
    predicted_price_formatted: str
    confidence_interval: Optional[Dict[str, float]] = None
    timestamp: str
    model_version: str


class BatchPredictionResponse(BaseModel):
    """Response model for batch predictions."""
    predictions: List[PredictionResponse]
    total_predictions: int
    average_price: float
    timestamp: str


class ModelInfo(BaseModel):
    """Model information response."""
    model_name: str
    model_version: str
    model_metrics: Dict[str, float]
    feature_names: List[str]
    last_updated: str


# Model Loader Singleton
class ModelLoader:
    """
    Singleton class for loading and managing the ML model.
    
    Design Pattern: Singleton Pattern - Single model instance
    """
    
    _instance = None
    _model = None
    _preprocessor = None
    _feature_engineer = None
    _metrics = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def load_model(self, model_path: Path = Path("data/models/best_model.pkl")):
        """Load the trained model and preprocessors."""
        try:
            if not model_path.exists():
                raise FileNotFoundError(f"Model not found at {model_path}")
            
            self._model = joblib.load(model_path)
            logger.info(f"Model loaded from {model_path}")
            
            # Load or create preprocessor and feature engineer
            self._preprocessor = DataPreprocessor()
            self._feature_engineer = FeatureEngineer()
            
            # Load metrics if available
            metrics_path = model_path.parent / "model_metrics.json"
            if metrics_path.exists():
                with open(metrics_path, 'r') as f:
                    self._metrics = json.load(f)
            
            return True
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            return False
    
    def get_model(self):
        """Get the loaded model."""
        if self._model is None:
            self.load_model()
        return self._model
    
    def get_metrics(self):
        """Get model metrics."""
        return self._metrics or {
            'rmse': 0,
            'mae': 0,
            'r2': 0,
            'mape': 0
        }


# Prediction Service
class PredictionService:
    """
    Service class for making predictions.
    
    Design Pattern: Facade Pattern - Simplifies prediction interface
    """
    
    def __init__(self):
        self.model_loader = ModelLoader()
        self.model_loader.load_model()
    
    def preprocess_features(self, features: Dict[str, Any]) -> pd.DataFrame:
        """Preprocess input features."""
        df = pd.DataFrame([features])
        
        # Apply preprocessing
        df_processed, _ = self.model_loader._preprocessor.process(
            df, target_col=None,
            handle_missing=True,
            encode_categorical=True
        )
        
        # Apply feature engineering
        df_features = self.model_loader._feature_engineer.create_features(df_processed)
        
        return df_features
    
    def predict_single(self, features: HouseFeatures) -> float:
        """Make a single prediction."""
        try:
            # Convert to dictionary
            features_dict = features.dict()
            
            # Preprocess
            X = self.preprocess_features(features_dict)
            
            # Ensure all expected columns are present
            model = self.model_loader.get_model()
            
            # Make prediction
            prediction = model.predict(X)[0]
            
            return max(prediction, 0)  # Ensure non-negative price
            
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Prediction failed: {str(e)}"
            )
    
    def predict_batch(self, features_list: List[HouseFeatures]) -> List[float]:
        """Make batch predictions."""
        predictions = []
        for features in features_list:
            pred = self.predict_single(features)
            predictions.append(pred)
        return predictions


# Initialize service
prediction_service = PredictionService()


# API Endpoints
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint for API health check."""
    return {
        "message": "House Price Prediction API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    model = prediction_service.model_loader.get_model()
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/model/info", response_model=ModelInfo, tags=["Model"])
async def get_model_info():
    """Get model information and metrics."""
    model = prediction_service.model_loader.get_model()
    metrics = prediction_service.model_loader.get_metrics()
    
    return ModelInfo(
        model_name="House Price Predictor",
        model_version="1.0.0",
        model_metrics=metrics,
        feature_names=[],  # Would load from saved features
        last_updated=datetime.now().isoformat()
    )


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict(request: PredictionRequest):
    """
    Predict house price based on features.
    
    Returns predicted price with confidence interval.
    """
    try:
        # Make prediction
        predicted_price = prediction_service.predict_single(request.features)
        
        # Calculate confidence interval (simplified)
        metrics = prediction_service.model_loader.get_metrics()
        margin = metrics.get('rmse', 20000) * 1.96  # 95% confidence
        
        return PredictionResponse(
            predicted_price=predicted_price,
            predicted_price_formatted=f"${predicted_price:,.2f}",
            confidence_interval={
                "lower": max(0, predicted_price - margin),
                "upper": predicted_price + margin
            },
            timestamp=datetime.now().isoformat(),
            model_version="1.0.0"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Prediction endpoint error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )


@app.post("/predict/batch", response_model=BatchPredictionResponse, tags=["Prediction"])
async def predict_batch(request: BatchPredictionRequest):
    """
    Predict house prices for multiple properties.
    """
    try:
        # Make batch predictions
        predictions = prediction_service.predict_batch(request.features)
        
        # Create response objects
        prediction_responses = []
        for pred in predictions:
            prediction_responses.append(PredictionResponse(
                predicted_price=pred,
                predicted_price_formatted=f"${pred:,.2f}",
                timestamp=datetime.now().isoformat(),
                model_version="1.0.0"
            ))
        
        return BatchPredictionResponse(
            predictions=prediction_responses,
            total_predictions=len(predictions),
            average_price=np.mean(predictions),
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        logger.error(f"Batch prediction error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch prediction failed: {str(e)}"
        )


# Dockerfile
"""
Dockerfile for containerizing the API.

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# docker-compose.yml
"""
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    environment:
      - PYTHONUNBUFFERED=1
    restart: unless-stopped

  mlflow:
    image: ghcr.io/mlflow/mlflow:latest
    ports:
      - "5000:5000"
    volumes:
      - ./mlflow:/mlflow
    command: mlflow ui --host 0.0.0.0 --port 5000 --backend-store-uri /mlflow/mlruns
"""


def test_api():
    """
    Test the API endpoints.
    """
    import requests
    
    print("\n" + "=" * 60)
    print("TESTING API ENDPOINTS")
    print("=" * 60)
    
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    print("\n1. TESTING HEALTH ENDPOINT")
    print("-" * 40)
    
    response = requests.get(f"{base_url}/health")
    print(f"  Status: {response.status_code}")
    print(f"  Response: {response.json()}")
    
    # Test prediction
    print("\n2. TESTING PREDICTION ENDPOINT")
    print("-" * 40)
    
    test_features = {
        "features": {
            "MSSubClass": 60,
            "MSZoning": "RL",
            "LotFrontage": 70,
            "LotArea": 10000,
            "OverallQual": 7,
            "OverallCond": 5,
            "YearBuilt": 2000,
            "YearRemodAdd": 2005,
            "GrLivArea": 1500,
            "TotalBsmtSF": 800,
            "GarageArea": 400,
            "FullBath": 2,
            "HalfBath": 1,
            "BedroomAbvGr": 3,
            "Fireplaces": 1,
            "GarageCars": 2,
            "MoSold": 6,
            "YrSold": 2020
        }
    }
    
    response = requests.post(f"{base_url}/predict", json=test_features)
    print(f"  Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"  Predicted price: {result['predicted_price_formatted']}")
        print(f"  Confidence interval: ${result['confidence_interval']['lower']:,.2f} - ${result['confidence_interval']['upper']:,.2f}")
    else:
        print(f"  Error: {response.text}")


def demonstrate_api_deployment():
    """
    Demonstrate API deployment concepts.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: MODEL DEPLOYMENT & API")
    print("=" * 60)
    
    print("\n1. API ENDPOINTS")
    print("-" * 40)
    
    endpoints = [
        ("GET", "/", "API information"),
        ("GET", "/health", "Health check"),
        ("GET", "/model/info", "Model information"),
        ("POST", "/predict", "Single prediction"),
        ("POST", "/predict/batch", "Batch predictions")
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:5} {path:20} - {description}")
    
    print("\n2. DEPLOYMENT OPTIONS")
    print("-" * 40)
    
    deployment_options = [
        "Local Development: uvicorn app:app --reload",
        "Production: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app",
        "Docker: docker build -t house-price-api . && docker run -p 8000:8000 house-price-api",
        "Docker Compose: docker-compose up -d",
        "Cloud Deployment: AWS ECS, GCP Cloud Run, Azure Container Instances"
    ]
    
    for option in deployment_options:
        print(f"  • {option}")
    
    print("\n3. API TESTING COMMANDS")
    print("-" * 40)
    
    commands = [
        "# Test health endpoint",
        "curl http://localhost:8000/health",
        "",
        "# Make a prediction",
        """curl -X POST "http://localhost:8000/predict" \\
     -H "Content-Type: application/json" \\
     -d '{"features": {"MSSubClass": 60, "MSZoning": "RL", ...}}'""",
        "",
        "# View API documentation",
        "open http://localhost:8000/docs"
    ]
    
    for cmd in commands:
        print(f"  {cmd}")
    
    print("\n4. PRODUCTION CHECKLIST")
    print("-" * 40)
    
    checklist = [
        "✓ Implement authentication (API keys, JWT)",
        "✓ Add rate limiting to prevent abuse",
        "✓ Set up monitoring (Prometheus, Grafana)",
        "✓ Implement request logging and audit trails",
        "✓ Add model versioning and canary deployments",
        "✓ Set up CI/CD pipeline (GitHub Actions, Jenkins)",
        "✓ Implement A/B testing framework",
        "✓ Add caching for frequent predictions (Redis)",
        "✓ Set up auto-scaling based on load",
        "✓ Implement circuit breakers for downstream services"
    ]
    
    for item in checklist:
        print(f"  {item}")


if __name__ == "__main__":
    demonstrate_api_deployment()
```

---

## 📊 Takeaway from This Story

**What You Built:**

- **Complete ML Pipeline** – From data collection to production deployment
- **Professional Project Structure** – Organized, maintainable, scalable codebase
- **Data Validation System** – Automated quality checks with custom rules
- **Feature Engineering** – Domain-specific features that improve model performance
- **Multiple Models** – Compare Random Forest, XGBoost, LightGBM, and Gradient Boosting
- **Hyperparameter Tuning** – Automated optimization with cross-validation
- **MLflow Integration** – Experiment tracking and model registry
- **REST API** – FastAPI application with comprehensive endpoints
- **Docker Deployment** – Containerized application for consistent deployment

**SOLID Principles Applied:**
- **Single Responsibility** – Each class handles one aspect (data loading, validation, preprocessing, modeling, API)
- **Open/Closed** – New features, models, and validation rules can be added without modifying existing code
- **Liskov Substitution** – All models follow sklearn BaseEstimator interface
- **Interface Segregation** – Small, focused interfaces for each component
- **Dependency Inversion** – High-level pipelines depend on abstractions, not concrete implementations

**Design Patterns Used:**
- **Factory Pattern** – Creates models, data loaders, and pipeline components
- **Strategy Pattern** – Pluggable validation rules and feature engineering strategies
- **Template Method Pattern** – Training workflow defined in base classes
- **Singleton Pattern** – Model loader and API service instances
- **Facade Pattern** – Simplified prediction interface
- **Pipeline Pattern** – Chains preprocessing and modeling steps
- **Value Object Pattern** – Immutable configuration and validation results
- **Context Pattern** – Shared state across pipeline components

**Key Technologies:**
- **Scikit-learn** – Preprocessing, models, cross-validation
- **XGBoost/LightGBM** – Gradient boosting implementations
- **FastAPI** – High-performance API framework
- **MLflow** – Experiment tracking and model management
- **Docker** – Containerization for consistent deployment
- **Pydantic** – Data validation and serialization

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: PyTorch – Research and Production

- **📚 Series I Catalog:** AI & Machine Learning with Python – View all 4 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Series:** Series J: Capstone Projects – CLI Expense Tracker

---

## 🎯 Your Capstone Challenge

Now that you've completed the entire AI/ML line, here's your capstone challenge:

**Build a Complete ML-Powered Application:**

1. **Choose a dataset** – Kaggle competition dataset or your own data
2. **Build the pipeline** – Data validation, feature engineering, model training
3. **Track experiments** – Use MLflow to log all runs
4. **Create an API** – Deploy your model with FastAPI
5. **Containerize** – Package everything with Docker
6. **Deploy to cloud** – AWS, GCP, or Azure (free tier)
7. **Add monitoring** – Track predictions and model performance
8. **Write documentation** – API docs, setup instructions, usage examples

**Project Ideas:**
- Credit risk assessment system
- Customer churn prediction with early warnings
- Real-time fraud detection API
- Product recommendation engine
- Sentiment analysis for social media
- Medical diagnosis assistant

**You've mastered the entire AI & Machine Learning line. Next stop: Capstone Projects!**

---

*Found this helpful? Clap, comment, and share your ML pipeline project. Next stop: CLI Expense Tracker!* 🚇

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
| Series I | 4 | 4 | 0 | 100% ✅ |
| Series J | 3 | 0 | 3 | 0% |

**Series I Complete!** 🎉 

**Next Stories to Generate:**
1. Series J, Story 1: CLI Expense Tracker
2. Series J, Story 2: Weather Dashboard
3. Series J, Story 3: ML-Powered Recommendation Engine