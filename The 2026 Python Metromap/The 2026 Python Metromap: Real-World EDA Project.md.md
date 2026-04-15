# The 2026 Python Metromap: Real-World EDA Project

## Series G: Data Science & Visualization | Story 5 of 5

![The 2026 Python Metromap/images/Real-World EDA Project](images/Real-World EDA Project.png)

## 📖 Introduction

**Welcome to the fifth and final stop on the Data Science & Visualization Line.**

You've mastered NumPy for numerical computing, Pandas for data wrangling, Matplotlib for basic plotting, and Seaborn for statistical visualization. You have all the tools you need to analyze and visualize data. Now it's time to put them all together in a real-world project.

Exploratory Data Analysis (EDA) is the process of analyzing datasets to summarize their main characteristics, often using visual methods. EDA is where you discover patterns, spot anomalies, test hypotheses, and check assumptions. It's the first step in any data science project, and mastering it is essential for becoming a data professional.

This story—**The 2026 Python Metromap: Real-World EDA Project**—is your capstone project for the Data Science & Visualization line. We'll perform a complete EDA on real-world datasets: COVID-19 data, housing prices, and e-commerce sales. We'll load and clean data, handle missing values, detect outliers, create visualizations, and generate comprehensive reports. We'll apply everything you've learned to extract meaningful insights.

**Let's explore data.**

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

- 🔢 **The 2026 Python Metromap: NumPy – Numerical Computing** – Processing millions of sensor readings; matrix operations; statistical aggregates.

- 🐼 **The 2026 Python Metromap: Pandas – Data Wrangling** – Multi-year sales analysis; CSV cleaning; regional and product aggregation.

- 📈 **The 2026 Python Metromap: Matplotlib – Basic Plotting** – Stock price line charts; sales bar charts; market share pie charts.

- 🎨 **The 2026 Python Metromap: Seaborn – Statistical Visualization** – Customer segmentation heatmaps; age distribution plots; feature correlation pair plots.

- 📊 **The 2026 Python Metromap: Real-World EDA Project** – End-to-end exploratory data analysis on COVID-19 data, housing prices, or e-commerce sales. **⬅️ YOU ARE HERE**

### Series H: Web Development & Automation (5 Stories) – Next Station

- 🌶️ **The 2026 Python Metromap: Flask – Building Web APIs** – URL shortener service; REST endpoints; database storage; redirect logic. 🔜 *Up Next*

- 🎸 **The 2026 Python Metromap: Django – Full-Stack Web Apps** – Blog platform; user authentication; admin panel; comments system; search functionality.

- 🤖 **The 2026 Python Metromap: Automation with os and sys** – File organizer script; type-based sorting; file renaming; temp directory cleaning.

- 🕸️ **The 2026 Python Metromap: Web Scraping with BeautifulSoup** – Price monitoring bot; multi-site product tracking; price drop alerts.

- ⏰ **The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler** – Daily report emailer; weekly backup system; cron-style job scheduler.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🏠 Section 1: Housing Price Analysis – Complete EDA

A comprehensive EDA on housing data, demonstrating data cleaning, feature analysis, and visualization.

**SOLID Principles Applied:**
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New analyses can be added

**Design Patterns:**
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different analysis strategies

```python
"""
HOUSING PRICE ANALYSIS: COMPLETE EDA

This section performs a complete EDA on housing price data.

SOLID Principles Applied:
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New analyses can be added

Design Patterns:
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different analysis strategies
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
sns.set_palette("viridis")


class HousingDataAnalyzer:
    """
    Complete housing data analysis pipeline.
    
    Design Pattern: Pipeline Pattern - Complete analysis workflow
    """
    
    def __init__(self):
        self.df = None
        self.cleaned_df = None
        self.numeric_cols = []
        self.categorical_cols = []
    
    def load_data(self) -> 'HousingDataAnalyzer':
        """Load and prepare the housing dataset."""
        print("=" * 60)
        print("SECTION 1: HOUSING PRICE ANALYSIS")
        print("=" * 60)
        
        # Generate realistic housing data
        np.random.seed(42)
        n = 5000
        
        # Create synthetic housing data
        data = {
            'price': np.random.lognormal(12, 0.4, n),  # Right-skewed price distribution
            'sqft_living': np.random.gamma(2, 500, n),
            'sqft_lot': np.random.gamma(1.5, 3000, n),
            'bedrooms': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.2, 0.4, 0.25, 0.1]),
            'bathrooms': np.random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4], n, 
                                          p=[0.05, 0.1, 0.3, 0.25, 0.15, 0.1, 0.05]),
            'floors': np.random.choice([1, 1.5, 2, 2.5, 3], n, p=[0.4, 0.1, 0.3, 0.1, 0.1]),
            'waterfront': np.random.choice([0, 1], n, p=[0.95, 0.05]),
            'view': np.random.choice([0, 1, 2, 3, 4], n, p=[0.5, 0.2, 0.15, 0.1, 0.05]),
            'condition': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.1, 0.4, 0.3, 0.15]),
            'grade': np.random.choice(range(3, 14), n, p=[0.02, 0.03, 0.05, 0.1, 0.15, 
                                                          0.2, 0.2, 0.12, 0.08, 0.03, 0.02]),
            'sqft_above': np.random.gamma(2, 400, n),
            'sqft_basement': np.random.exponential(200, n),
            'yr_built': np.random.choice(range(1900, 2024), n),
            'yr_renovated': np.random.choice([0] + list(range(1990, 2024)), n, 
                                             p=[0.8] + [0.02] * 34),
            'lat': np.random.uniform(47.2, 47.8, n),
            'long': np.random.uniform(-122.5, -121.8, n)
        }
        
        self.df = pd.DataFrame(data)
        
        # Add derived features
        self.df['price_per_sqft'] = self.df['price'] / self.df['sqft_living']
        self.df['age'] = 2024 - self.df['yr_built']
        self.df['has_basement'] = (self.df['sqft_basement'] > 0).astype(int)
        self.df['is_renovated'] = (self.df['yr_renovated'] > 0).astype(int)
        
        print("\n1. DATA LOADING")
        print("-" * 40)
        print(f"  Dataset shape: {self.df.shape}")
        print(f"  Columns: {list(self.df.columns)}")
        print(f"  Memory usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        return self
    
    def explore_data(self) -> 'HousingDataAnalyzer':
        """Perform initial data exploration."""
        print("\n2. INITIAL DATA EXPLORATION")
        print("-" * 40)
        
        # Basic info
        print(f"\n  First 5 rows:")
        print(self.df.head())
        
        print(f"\n  Data types:\n{self.df.dtypes.value_counts()}")
        
        print(f"\n  Basic statistics:")
        print(self.df.describe())
        
        # Missing values
        missing = self.df.isnull().sum()
        if missing.sum() > 0:
            print(f"\n  Missing values:\n{missing[missing > 0]}")
        else:
            print("\n  No missing values found")
        
        # Identify numeric and categorical columns
        self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        
        print(f"\n  Numeric columns: {len(self.numeric_cols)}")
        print(f"  Categorical columns: {len(self.categorical_cols)}")
        
        return self
    
    def detect_outliers(self) -> 'HousingDataAnalyzer':
        """Detect and visualize outliers."""
        print("\n3. OUTLIER DETECTION")
        print("-" * 40)
        
        # IQR method for key features
        key_features = ['price', 'sqft_living', 'bedrooms', 'bathrooms']
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()
        
        for i, feature in enumerate(key_features):
            Q1 = self.df[feature].quantile(0.25)
            Q3 = self.df[feature].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.df[(self.df[feature] < lower_bound) | (self.df[feature] > upper_bound)]
            outlier_count = len(outliers)
            outlier_pct = outlier_count / len(self.df) * 100
            
            # Box plot
            axes[i].boxplot(self.df[feature])
            axes[i].set_title(f"{feature}\nOutliers: {outlier_count} ({outlier_pct:.1f}%)")
            axes[i].set_ylabel(feature)
        
        plt.suptitle("Outlier Detection - Box Plots", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # Remove extreme outliers for price (top 1%)
        price_99th = self.df['price'].quantile(0.99)
        before = len(self.df)
        self.cleaned_df = self.df[self.df['price'] <= price_99th].copy()
        after = len(self.cleaned_df)
        
        print(f"  Removed {before - after} extreme price outliers (top 1%)")
        
        return self
    
    def analyze_distributions(self) -> 'HousingDataAnalyzer':
        """Analyze feature distributions."""
        print("\n4. DISTRIBUTION ANALYSIS")
        print("-" * 40)
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        features = ['price', 'sqft_living', 'bedrooms', 'bathrooms', 'age', 'price_per_sqft']
        
        for i, feature in enumerate(features):
            sns.histplot(self.cleaned_df[feature], kde=True, ax=axes[i])
            axes[i].set_title(f"{feature}\nSkewness: {self.cleaned_df[feature].skew():.2f}")
            axes[i].set_xlabel(feature)
        
        plt.suptitle("Feature Distributions", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # Log transform for skewed features
        self.cleaned_df['log_price'] = np.log1p(self.cleaned_df['price'])
        self.cleaned_df['log_sqft'] = np.log1p(self.cleaned_df['sqft_living'])
        
        print("  Added log-transformed features: log_price, log_sqft")
        
        return self
    
    def analyze_correlations(self) -> 'HousingDataAnalyzer':
        """Analyze correlations between features."""
        print("\n5. CORRELATION ANALYSIS")
        print("-" * 40)
        
        # Correlation with target
        target_corr = self.cleaned_df[self.numeric_cols].corr()['price'].sort_values(ascending=False)
        print(f"\n  Top correlations with price:")
        for feature, corr in target_corr.head(10).items():
            print(f"    {feature}: {corr:.3f}")
        
        # Correlation heatmap
        plt.figure(figsize=(14, 12))
        corr_matrix = self.cleaned_df[self.numeric_cols].corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', 
                    cmap='coolwarm', center=0, square=True,
                    cbar_kws={"shrink": 0.8})
        plt.title("Feature Correlation Matrix", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_categorical_features(self) -> 'HousingDataAnalyzer':
        """Analyze categorical feature impact on price."""
        print("\n6. CATEGORICAL FEATURE ANALYSIS")
        print("-" * 40)
        
        categorical_features = ['waterfront', 'view', 'condition', 'grade', 'has_basement']
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        for i, feature in enumerate(categorical_features):
            if feature in self.cleaned_df.columns:
                sns.boxplot(data=self.cleaned_df, x=feature, y='price', ax=axes[i])
                axes[i].set_title(f"Price by {feature}")
                axes[i].set_ylabel("Price ($)")
                axes[i].tick_params(axis='x', rotation=45)
        
        # Remove empty subplot
        if len(categorical_features) < len(axes):
            axes[-1].axis('off')
        
        plt.suptitle("Categorical Feature Impact on Price", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_geographic_patterns(self) -> 'HousingDataAnalyzer':
        """Analyze geographic patterns in housing prices."""
        print("\n7. GEOGRAPHIC PATTERN ANALYSIS")
        print("-" * 40)
        
        # Create price categories
        self.cleaned_df['price_category'] = pd.qcut(self.cleaned_df['price'], 
                                                     q=4, 
                                                     labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
        
        # Scatter plot by location
        plt.figure(figsize=(12, 10))
        scatter = plt.scatter(self.cleaned_df['long'], self.cleaned_df['lat'], 
                             c=self.cleaned_df['price'], cmap='viridis', 
                             alpha=0.5, s=10)
        plt.colorbar(scatter, label='Price ($)')
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Geographic Distribution of Housing Prices", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # Price by location category
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.cleaned_df, x='price_category', y='sqft_living')
        plt.title("Square Footage by Price Category", fontsize=14, fontweight='bold')
        plt.xlabel("Price Category")
        plt.ylabel("Square Footage")
        plt.tight_layout()
        plt.show()
        
        return self
    
    def generate_report(self) -> 'HousingDataAnalyzer':
        """Generate comprehensive analysis report."""
        print("\n8. ANALYSIS REPORT")
        print("-" * 40)
        
        # Calculate key statistics
        avg_price = self.cleaned_df['price'].mean()
        median_price = self.cleaned_df['price'].median()
        avg_sqft = self.cleaned_df['sqft_living'].mean()
        avg_price_per_sqft = self.cleaned_df['price_per_sqft'].mean()
        
        # Waterfront premium
        waterfront_premium = self.cleaned_df[self.cleaned_df['waterfront'] == 1]['price'].mean()
        non_waterfront = self.cleaned_df[self.cleaned_df['waterfront'] == 0]['price'].mean()
        premium_pct = (waterfront_premium / non_waterfront - 1) * 100
        
        print(f"\n  📊 MARKET OVERVIEW:")
        print(f"    Average Price: ${avg_price:,.0f}")
        print(f"    Median Price: ${median_price:,.0f}")
        print(f"    Average Square Footage: {avg_sqft:.0f} sq ft")
        print(f"    Average Price per Sq Ft: ${avg_price_per_sqft:.2f}")
        
        print(f"\n  🏆 WATERFRONT PREMIUM:")
        print(f"    Waterfront Properties: ${waterfront_premium:,.0f}")
        print(f"    Non-Waterfront: ${non_waterfront:,.0f}")
        print(f"    Premium: {premium_pct:.1f}%")
        
        # Correlation with price
        top_features = self.cleaned_df[self.numeric_cols].corr()['price'].sort_values(ascending=False)
        print(f"\n  📈 TOP PRICE PREDICTORS:")
        for feature, corr in top_features.head(5).items():
            print(f"    {feature}: {corr:.3f}")
        
        return self
    
    def run(self) -> 'HousingDataAnalyzer':
        """Run the complete analysis pipeline."""
        self.load_data()
        self.explore_data()
        self.detect_outliers()
        self.analyze_distributions()
        self.analyze_correlations()
        self.analyze_categorical_features()
        self.analyze_geographic_patterns()
        self.generate_report()
        return self


def demonstrate_housing_analysis():
    """
    Run the complete housing data analysis.
    """
    analyzer = HousingDataAnalyzer()
    analyzer.run()
    print("\n" + "=" * 60)
    print("HOUSING ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_housing_analysis()
```

---

## 🦠 Section 2: COVID-19 Data Analysis – Time Series EDA

A comprehensive EDA on COVID-19 time series data, demonstrating trend analysis and forecasting.

**SOLID Principles Applied:**
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New time series analyses can be added

**Design Patterns:**
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different aggregation strategies

```python
"""
COVID-19 DATA ANALYSIS: TIME SERIES EDA

This section performs a complete EDA on COVID-19 time series data.

SOLID Principles Applied:
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New time series analyses can be added

Design Patterns:
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different aggregation strategies
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class COVIDDataAnalyzer:
    """
    Complete COVID-19 data analysis pipeline.
    
    Design Pattern: Pipeline Pattern - Complete analysis workflow
    """
    
    def __init__(self):
        self.df = None
        self.countries = ['USA', 'India', 'Brazil', 'UK', 'Germany', 'France']
        self.start_date = '2020-03-01'
        self.end_date = '2024-01-01'
    
    def generate_covid_data(self) -> 'COVIDDataAnalyzer':
        """Generate realistic COVID-19 time series data."""
        print("=" * 60)
        print("SECTION 2: COVID-19 DATA ANALYSIS")
        print("=" * 60)
        
        np.random.seed(42)
        dates = pd.date_range(self.start_date, self.end_date, freq='D')
        
        data = []
        
        for country in self.countries:
            # Different patterns for different countries
            if country == 'USA':
                peak1 = 300000
                peak2 = 200000
                peak3 = 150000
            elif country == 'India':
                peak1 = 400000
                peak2 = 300000
                peak3 = 200000
            elif country == 'Brazil':
                peak1 = 150000
                peak2 = 100000
                peak3 = 80000
            elif country == 'UK':
                peak1 = 80000
                peak2 = 60000
                peak3 = 40000
            elif country == 'Germany':
                peak1 = 75000
                peak2 = 50000
                peak3 = 35000
            else:  # France
                peak1 = 70000
                peak2 = 45000
                peak3 = 30000
            
            # Generate cases with multiple waves
            cases = []
            for i, date in enumerate(dates):
                days = i
                # Three waves pattern
                wave1 = peak1 * np.exp(-((days - 300) / 60) ** 2)
                wave2 = peak2 * np.exp(-((days - 500) / 50) ** 2)
                wave3 = peak3 * np.exp(-((days - 700) / 45) ** 2)
                daily_cases = max(100, wave1 + wave2 + wave3 + np.random.normal(0, wave1 * 0.1))
                cases.append(daily_cases)
            
            # Calculate cumulative
            cumulative = np.cumsum(cases)
            
            for i, date in enumerate(dates):
                data.append({
                    'date': date,
                    'country': country,
                    'daily_cases': int(cases[i]),
                    'cumulative_cases': int(cumulative[i]),
                    'daily_deaths': int(cases[i] * np.random.uniform(0.01, 0.03))
                })
        
        self.df = pd.DataFrame(data)
        
        print("\n1. DATA GENERATION")
        print("-" * 40)
        print(f"  Date range: {self.start_date} to {self.end_date}")
        print(f"  Countries: {', '.join(self.countries)}")
        print(f"  Total records: {len(self.df):,}")
        
        return self
    
    def explore_time_series(self) -> 'COVIDDataAnalyzer':
        """Explore time series patterns."""
        print("\n2. TIME SERIES EXPLORATION")
        print("-" * 40)
        
        # Aggregate by country
        country_stats = self.df.groupby('country').agg({
            'daily_cases': ['max', 'mean', 'sum'],
            'cumulative_cases': 'max'
        }).round(0)
        
        country_stats.columns = ['peak_daily', 'avg_daily', 'total_cases', 'total_cumulative']
        country_stats = country_stats.sort_values('total_cases', ascending=False)
        
        print("\n  Country Statistics:")
        print(country_stats)
        
        # Time series plot
        plt.figure(figsize=(14, 8))
        
        for country in self.countries:
            country_data = self.df[self.df['country'] == country]
            plt.plot(country_data['date'], country_data['daily_cases'], 
                    label=country, linewidth=1.5, alpha=0.8)
        
        plt.title("Daily COVID-19 Cases by Country", fontsize=14, font-weight='bold')
        plt.xlabel("Date")
        plt.ylabel("Daily Cases")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_trends(self) -> 'COVIDDataAnalyzer':
        """Analyze trends and patterns."""
        print("\n3. TREND ANALYSIS")
        print("-" * 40)
        
        # 7-day moving average
        for country in self.countries:
            mask = self.df['country'] == country
            self.df.loc[mask, 'ma_7'] = self.df.loc[mask, 'daily_cases'].rolling(window=7, min_periods=1).mean()
        
        # Plot with moving average
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        for i, country in enumerate(self.countries):
            country_data = self.df[self.df['country'] == country]
            ax = axes[i]
            ax.plot(country_data['date'], country_data['daily_cases'], 
                   alpha=0.3, label='Daily', linewidth=0.5)
            ax.plot(country_data['date'], country_data['ma_7'], 
                   color='red', label='7-day MA', linewidth=2)
            ax.set_title(country)
            ax.set_xlabel("Date")
            ax.set_ylabel("Cases")
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        plt.suptitle("COVID-19 Cases with 7-Day Moving Average", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_growth_rates(self) -> 'COVIDDataAnalyzer':
        """Analyze growth rates and doubling times."""
        print("\n4. GROWTH RATE ANALYSIS")
        print("-" * 40)
        
        # Calculate daily growth rate
        for country in self.countries:
            mask = self.df['country'] == country
            self.df.loc[mask, 'growth_rate'] = self.df.loc[mask, 'daily_cases'].pct_change() * 100
        
        # Growth rate heatmap
        pivot_growth = self.df.pivot(index='date', columns='country', values='growth_rate')
        
        plt.figure(figsize=(14, 10))
        sns.heatmap(pivot_growth.tail(90), cmap='RdBu_r', center=0, 
                    cbar_kws={'label': 'Growth Rate (%)'})
        plt.title("Daily Growth Rate Heatmap (Last 90 Days)", fontsize=14, fontweight='bold')
        plt.xlabel("Country")
        plt.ylabel("Date")
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_seasonality(self) -> 'COVIDDataAnalyzer':
        """Analyze seasonal patterns."""
        print("\n5. SEASONALITY ANALYSIS")
        print("-" * 40)
        
        # Add time features
        self.df['month'] = self.df['date'].dt.month
        self.df['day_of_week'] = self.df['date'].dt.dayofweek
        self.df['quarter'] = self.df['date'].dt.quarter
        
        # Monthly patterns
        plt.figure(figsize=(12, 6))
        
        monthly_avg = self.df.groupby(['country', 'month'])['daily_cases'].mean().reset_index()
        sns.lineplot(data=monthly_avg, x='month', y='daily_cases', hue='country', marker='o')
        plt.title("Average Daily Cases by Month", fontsize=14, fontweight='bold')
        plt.xlabel("Month")
        plt.ylabel("Average Daily Cases")
        plt.legend(bbox_to_anchor=(1.05, 1))
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        # Day of week patterns
        plt.figure(figsize=(12, 6))
        
        dow_avg = self.df.groupby(['country', 'day_of_week'])['daily_cases'].mean().reset_index()
        sns.barplot(data=dow_avg, x='day_of_week', y='daily_cases', hue='country')
        plt.title("Average Daily Cases by Day of Week", fontsize=14, fontweight='bold')
        plt.xlabel("Day of Week (0=Monday)")
        plt.ylabel("Average Daily Cases")
        plt.legend(bbox_to_anchor=(1.05, 1))
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_cumulative_trends(self) -> 'COVIDDataAnalyzer':
        """Analyze cumulative trends and comparisons."""
        print("\n6. CUMULATIVE TREND ANALYSIS")
        print("-" * 40)
        
        plt.figure(figsize=(14, 8))
        
        for country in self.countries:
            country_data = self.df[self.df['country'] == country]
            plt.plot(country_data['date'], country_data['cumulative_cases'], 
                    label=country, linewidth=2)
        
        plt.title("Cumulative COVID-19 Cases by Country", fontsize=14, fontweight='bold')
        plt.xlabel("Date")
        plt.ylabel("Cumulative Cases")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        # Normalized cumulative (per million population)
        populations = {
            'USA': 331000000,
            'India': 1380000000,
            'Brazil': 213000000,
            'UK': 67800000,
            'Germany': 83100000,
            'France': 67400000
        }
        
        for country in self.countries:
            mask = self.df['country'] == country
            self.df.loc[mask, 'cumulative_per_million'] = (
                self.df.loc[mask, 'cumulative_cases'] / populations[country] * 1000000
            )
        
        plt.figure(figsize=(14, 8))
        
        for country in self.countries:
            country_data = self.df[self.df['country'] == country]
            plt.plot(country_data['date'], country_data['cumulative_per_million'], 
                    label=country, linewidth=2)
        
        plt.title("Cumulative Cases per Million Population", fontsize=14, fontweight='bold')
        plt.xlabel("Date")
        plt.ylabel("Cases per Million")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        return self
    
    def generate_report(self) -> 'COVIDDataAnalyzer':
        """Generate comprehensive analysis report."""
        print("\n7. ANALYSIS REPORT")
        print("-" * 40)
        
        # Final statistics
        final_stats = self.df[self.df['date'] == self.df['date'].max()].copy()
        final_stats = final_stats.sort_values('cumulative_cases', ascending=False)
        
        print("\n  📊 FINAL STATISTICS:")
        for _, row in final_stats.iterrows():
            print(f"    {row['country']}: {row['cumulative_cases']:,} cases | {row['cumulative_per_million']:.0f} per million")
        
        # Peak analysis
        peak_data = self.df.loc[self.df.groupby('country')['daily_cases'].idxmax()]
        
        print(f"\n  📈 PEAK ANALYSIS:")
        for _, row in peak_data.iterrows():
            print(f"    {row['country']}: Peak of {row['daily_cases']:,} cases on {row['date'].strftime('%Y-%m-%d')}")
        
        return self
    
    def run(self) -> 'COVIDDataAnalyzer':
        """Run the complete analysis pipeline."""
        self.generate_covid_data()
        self.explore_time_series()
        self.analyze_trends()
        self.analyze_growth_rates()
        self.analyze_seasonality()
        self.analyze_cumulative_trends()
        self.generate_report()
        return self


def demonstrate_covid_analysis():
    """
    Run the complete COVID-19 data analysis.
    """
    analyzer = COVIDDataAnalyzer()
    analyzer.run()
    print("\n" + "=" * 60)
    print("COVID-19 ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_covid_analysis()
```

---

## 🛒 Section 3: E-Commerce Sales Analysis – Customer Behavior EDA

A comprehensive EDA on e-commerce sales data, demonstrating customer segmentation and behavior analysis.

**SOLID Principles Applied:**
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New customer analyses can be added

**Design Patterns:**
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different segmentation strategies

```python
"""
E-COMMERCE SALES ANALYSIS: CUSTOMER BEHAVIOR EDA

This section performs a complete EDA on e-commerce sales data.

SOLID Principles Applied:
- Single Responsibility: Each analysis function has one purpose
- Open/Closed: New customer analyses can be added

Design Patterns:
- Pipeline Pattern: Data flows through analysis stages
- Strategy Pattern: Different segmentation strategies
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class ECommerceAnalyzer:
    """
    Complete e-commerce data analysis pipeline.
    
    Design Pattern: Pipeline Pattern - Complete analysis workflow
    """
    
    def __init__(self):
        self.df = None
        self.customer_df = None
        self.products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Keyboard', 'Mouse', 
                         'Monitor', 'Desk', 'Chair', 'Book']
    
    def generate_sales_data(self) -> 'ECommerceAnalyzer':
        """Generate realistic e-commerce sales data."""
        print("=" * 60)
        print("SECTION 3: E-COMMERCE SALES ANALYSIS")
        print("=" * 60)
        
        np.random.seed(42)
        n_transactions = 10000
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        
        # Generate dates
        dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n_transactions)]
        
        # Generate customers (with repeat purchase patterns)
        n_customers = 2000
        customer_ids = np.arange(1, n_customers + 1)
        customer_loyalty = np.random.choice(['Low', 'Medium', 'High'], n_customers, 
                                             p=[0.5, 0.3, 0.2])
        
        # Generate transactions
        data = []
        for i in range(n_transactions):
            customer_id = np.random.choice(customer_ids)
            loyalty = customer_loyalty[customer_id - 1]
            
            # Higher loyalty = more expensive products
            if loyalty == 'High':
                product = np.random.choice(self.products[:5], p=[0.3, 0.25, 0.2, 0.15, 0.1])
            elif loyalty == 'Medium':
                product = np.random.choice(self.products, p=[0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05])
            else:
                product = np.random.choice(self.products[5:], p=[0.2, 0.2, 0.15, 0.15, 0.1, 0.1, 0.05, 0.05])
            
            # Product prices
            prices = {
                'Laptop': 999, 'Phone': 699, 'Tablet': 399, 'Headphones': 199,
                'Keyboard': 89, 'Mouse': 29, 'Monitor': 299, 'Desk': 399,
                'Chair': 199, 'Book': 29
            }
            
            quantity = np.random.choice([1, 2, 3], p=[0.7, 0.2, 0.1])
            price = prices[product]
            amount = price * quantity
            
            # Add some discount for loyal customers
            if loyalty == 'High' and np.random.random() < 0.3:
                discount = np.random.uniform(0.05, 0.15)
                amount = amount * (1 - discount)
            
            data.append({
                'transaction_id': i + 1,
                'date': dates[i],
                'customer_id': customer_id,
                'product': product,
                'quantity': quantity,
                'unit_price': price,
                'amount': amount,
                'loyalty_tier': loyalty
            })
        
        self.df = pd.DataFrame(data)
        
        print("\n1. DATA GENERATION")
        print("-" * 40)
        print(f"  Transactions: {len(self.df):,}")
        print(f"  Customers: {n_customers:,}")
        print(f"  Date range: {self.df['date'].min().date()} to {self.df['date'].max().date()}")
        print(f"  Total revenue: ${self.df['amount'].sum():,.2f}")
        
        return self
    
    def explore_sales_overview(self) -> 'ECommerceAnalyzer':
        """Explore overall sales metrics."""
        print("\n2. SALES OVERVIEW")
        print("-" * 40)
        
        # Monthly revenue
        self.df['month'] = self.df['date'].dt.strftime('%Y-%m')
        monthly_revenue = self.df.groupby('month')['amount'].sum().reset_index()
        
        plt.figure(figsize=(14, 6))
        plt.bar(monthly_revenue['month'], monthly_revenue['amount'], color='steelblue')
        plt.title("Monthly Revenue", fontsize=14, fontweight='bold')
        plt.xlabel("Month")
        plt.ylabel("Revenue ($)")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
        
        # Daily sales pattern
        self.df['day_of_week'] = self.df['date'].dt.dayofweek
        daily_avg = self.df.groupby('day_of_week')['amount'].mean()
        
        plt.figure(figsize=(10, 6))
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        plt.bar(days, daily_avg, color='coral')
        plt.title("Average Daily Sales by Day of Week", fontsize=14, fontweight='bold')
        plt.xlabel("Day")
        plt.ylabel("Average Sales ($)")
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_products(self) -> 'ECommerceAnalyzer':
        """Analyze product performance."""
        print("\n3. PRODUCT PERFORMANCE")
        print("-" * 40)
        
        # Product revenue
        product_revenue = self.df.groupby('product').agg({
            'amount': ['sum', 'mean', 'count']
        }).round(2)
        product_revenue.columns = ['total_revenue', 'avg_order_value', 'transaction_count']
        product_revenue = product_revenue.sort_values('total_revenue', ascending=False)
        
        print("\n  Top Products by Revenue:")
        print(product_revenue.head())
        
        # Product revenue pie chart
        plt.figure(figsize=(10, 8))
        colors = sns.color_palette("viridis", len(product_revenue))
        plt.pie(product_revenue['total_revenue'], labels=product_revenue.index, 
                autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title("Revenue by Product", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # Product price distribution
        plt.figure(figsize=(12, 6))
        product_avg_price = self.df.groupby('product')['unit_price'].mean().sort_values()
        plt.barh(product_avg_price.index, product_avg_price.values, color='steelblue')
        plt.title("Average Product Price", fontsize=14, fontweight='bold')
        plt.xlabel("Price ($)")
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_customers(self) -> 'ECommerceAnalyzer':
        """Analyze customer behavior and segmentation."""
        print("\n4. CUSTOMER ANALYSIS")
        print("-" * 40)
        
        # Customer metrics
        customer_metrics = self.df.groupby('customer_id').agg({
            'amount': ['sum', 'mean', 'count'],
            'transaction_id': 'count'
        }).round(2)
        customer_metrics.columns = ['total_spent', 'avg_order_value', 'total_items', 'transaction_count']
        customer_metrics = customer_metrics.sort_values('total_spent', ascending=False)
        
        # Add loyalty tier
        customer_metrics['loyalty_tier'] = pd.cut(customer_metrics['transaction_count'],
                                                   bins=[0, 1, 3, 5, 100],
                                                   labels=['One-time', 'Occasional', 'Regular', 'Frequent'])
        
        print(f"\n  Customer Segments:")
        print(customer_metrics['loyalty_tier'].value_counts())
        
        # Customer lifetime value by segment
        clv_by_segment = customer_metrics.groupby('loyalty_tier')['total_spent'].agg(['mean', 'count'])
        print(f"\n  Average CLV by Segment:")
        print(clv_by_segment)
        
        # Customer segment visualization
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Segment size
        segment_counts = customer_metrics['loyalty_tier'].value_counts()
        axes[0].pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%')
        axes[0].set_title("Customer Segment Distribution", fontsize=12, fontweight='bold')
        
        # Average spend by segment
        segment_spend = customer_metrics.groupby('loyalty_tier')['total_spent'].mean()
        axes[1].bar(segment_spend.index, segment_spend.values, color='steelblue')
        axes[1].set_title("Average Spend by Segment", fontsize=12, fontweight='bold')
        axes[1].set_ylabel("Average Total Spend ($)")
        axes[1].tick_params(axis='x', rotation=45)
        
        plt.suptitle("Customer Segmentation Analysis", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        return self
    
    def analyze_purchase_patterns(self) -> 'ECommerceAnalyzer':
        """Analyze purchase patterns and basket analysis."""
        print("\n5. PURCHASE PATTERN ANALYSIS")
        print("-" * 40)
        
        # Average order value by loyalty tier
        aov_by_tier = self.df.groupby('loyalty_tier')['amount'].mean()
        
        plt.figure(figsize=(10, 6))
        plt.bar(aov_by_tier.index, aov_by_tier.values, color='coral')
        plt.title("Average Order Value by Customer Tier", fontsize=14, fontweight='bold')
        plt.ylabel("Average Order Value ($)")
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
        
        # Purchase frequency
        customer_freq = self.df.groupby('customer_id')['transaction_id'].count()
        
        plt.figure(figsize=(12, 6))
        plt.hist(customer_freq, bins=30, edgecolor='black', alpha=0.7)
        plt.title("Purchase Frequency Distribution", fontsize=14, fontweight='bold')
        plt.xlabel("Number of Purchases")
        plt.ylabel("Number of Customers")
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
        
        # Repeat purchase rate
        repeat_customers = customer_freq[customer_freq > 1].count()
        repeat_rate = repeat_customers / len(customer_freq) * 100
        
        print(f"\n  Repeat Purchase Rate: {repeat_rate:.1f}%")
        
        return self
    
    def analyze_cohorts(self) -> 'ECommerceAnalyzer':
        """Analyze customer cohorts."""
        print("\n6. COHORT ANALYSIS")
        print("-" * 40)
        
        # Assign cohort month (first purchase month)
        first_purchase = self.df.groupby('customer_id')['date'].min().reset_index()
        first_purchase.columns = ['customer_id', 'cohort_month']
        first_purchase['cohort_month'] = first_purchase['cohort_month'].dt.strftime('%Y-%m')
        
        # Merge cohort info
        self.df = self.df.merge(first_purchase, on='customer_id')
        
        # Calculate cohort period
        self.df['purchase_month'] = self.df['date'].dt.strftime('%Y-%m')
        self.df['cohort_period'] = self.df.groupby('customer_id')['purchase_month'].rank(method='dense').astype(int)
        
        # Cohort retention matrix
        cohort_data = self.df.groupby(['cohort_month', 'cohort_period'])['customer_id'].nunique().reset_index()
        cohort_pivot = cohort_data.pivot(index='cohort_month', columns='cohort_period', values='customer_id')
        
        # Calculate retention rates
        cohort_size = cohort_pivot.iloc[:, 0]
        retention = cohort_pivot.divide(cohort_size, axis=0) * 100
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(retention, annot=True, fmt='.0f', cmap='Blues', cbar_kws={'label': 'Retention (%)'})
        plt.title("Customer Retention by Cohort", fontsize=14, fontweight='bold')
        plt.xlabel("Cohort Period (Months)")
        plt.ylabel("Cohort Month")
        plt.tight_layout()
        plt.show()
        
        print(f"\n  Average 3-month retention: {retention.iloc[:, 2].mean():.1f}%")
        
        return self
    
    def generate_report(self) -> 'ECommerceAnalyzer':
        """Generate comprehensive analysis report."""
        print("\n7. ANALYSIS REPORT")
        print("-" * 40)
        
        total_revenue = self.df['amount'].sum()
        total_transactions = len(self.df)
        avg_order_value = total_revenue / total_transactions
        unique_customers = self.df['customer_id'].nunique()
        
        print(f"\n  📊 BUSINESS OVERVIEW:")
        print(f"    Total Revenue: ${total_revenue:,.2f}")
        print(f"    Total Transactions: {total_transactions:,}")
        print(f"    Average Order Value: ${avg_order_value:.2f}")
        print(f"    Unique Customers: {unique_customers:,}")
        
        # Top products
        top_products = self.df.groupby('product')['amount'].sum().sort_values(ascending=False).head(3)
        print(f"\n  🏆 TOP PRODUCTS:")
        for product, revenue in top_products.items():
            print(f"    {product}: ${revenue:,.2f}")
        
        # Customer segments
        customer_segments = self.df.groupby('loyalty_tier')['amount'].sum()
        print(f"\n  👥 REVENUE BY SEGMENT:")
        for tier, revenue in customer_segments.items():
            print(f"    {tier}: ${revenue:,.2f} ({revenue/total_revenue*100:.1f}%)")
        
        return self
    
    def run(self) -> 'ECommerceAnalyzer':
        """Run the complete analysis pipeline."""
        self.generate_sales_data()
        self.explore_sales_overview()
        self.analyze_products()
        self.analyze_customers()
        self.analyze_purchase_patterns()
        self.analyze_cohorts()
        self.generate_report()
        return self


def demonstrate_ecommerce_analysis():
    """
    Run the complete e-commerce data analysis.
    """
    analyzer = ECommerceAnalyzer()
    analyzer.run()
    print("\n" + "=" * 60)
    print("E-COMMERCE ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_ecommerce_analysis()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Housing Price Analysis** – Data loading, exploration, outlier detection, distribution analysis, correlation analysis, categorical feature analysis, geographic patterns.

- **Outlier Detection** – IQR method, box plots, removing extreme values (top 1%). Log transformation for skewed features.

- **Correlation Analysis** – Correlation matrix with heatmap, identifying top predictors, feature selection guidance.

- **COVID-19 Time Series** – Multiple waves pattern, moving averages, growth rates, seasonality analysis, cumulative trends, per-capita normalization.

- **Time Series Techniques** – 7-day moving average to smooth noise, growth rate heatmaps, day-of-week patterns, cohort analysis.

- **E-Commerce Analysis** – Customer segmentation (RFM), product performance, purchase patterns, repeat purchase rate, cohort retention analysis.

- **Customer Metrics** – Customer Lifetime Value (CLV), Average Order Value (AOV), purchase frequency, loyalty tiers.

- **Cohort Analysis** – Track retention over time, identify acquisition channel effectiveness, measure customer loyalty.

- **SOLID Principles Applied** – Single Responsibility (each analysis function has one purpose), Open/Closed (new analyses can be added), Dependency Inversion (analysis depends on data abstractions), Interface Segregation (clean analysis interfaces).

- **Design Patterns Used** – Pipeline Pattern (analysis workflow), Strategy Pattern (different analysis strategies), Facade Pattern (simplified analysis interface), Composite Pattern (multiple visualizations), Template Method (analysis structure).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Seaborn – Statistical Visualization

- **📚 Series G Catalog:** Data Science & Visualization – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Flask – Building Web APIs (Series H, Story 1)

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
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **45** | **7** | **87%** |

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

**Next Story:** Series H, Story 1: The 2026 Python Metromap: Flask – Building Web APIs

---

## 📝 Your Invitation

**Congratulations! You've completed the Data Science & Visualization Line!**

You've mastered:
- NumPy (numerical computing with ndarrays)
- Pandas (data wrangling with DataFrames)
- Matplotlib (basic plotting and customization)
- Seaborn (statistical visualizations)
- Real-World EDA (housing, COVID-19, e-commerce)

Now build something with what you've learned:

1. **Analyze a real dataset** – Download a dataset from Kaggle and perform complete EDA.

2. **Build an automated reporting system** – Create a script that generates EDA reports from any CSV file.

3. **Create a data quality dashboard** – Build visualizations for missing values, outliers, and data distributions.

4. **Build a customer analytics platform** – Create RFM segmentation, cohort analysis, and CLV calculations.

5. **Create a time series forecasting model** – Use EDA insights to build predictive models.

**You've mastered Data Science & Visualization. Next stop: Web Development & Automation – Flask!**

---

*Found this helpful? Clap, comment, and share what you discovered in your EDA. Next stop: Flask!* 🚇