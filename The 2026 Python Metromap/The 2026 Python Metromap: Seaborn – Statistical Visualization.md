# The 2026 Python Metromap: Seaborn – Statistical Visualization

## Series G: Data Science & Visualization | Story 4 of 5

![The 2026 Python Metromap/images/Seaborn – Statistical Visualization](images/Seaborn – Statistical Visualization.png)

## 📖 Introduction

**Welcome to the fourth stop on the Data Science & Visualization Line.**

You've mastered Matplotlib—line charts, bar charts, scatter plots, histograms, and multi-panel figures. You can create any visualization, but creating statistical plots often requires significant customization. That's where Seaborn comes in.

Seaborn is a statistical data visualization library built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. With just a few lines of code, you can create complex visualizations like heatmaps, pair plots, violin plots, and regression plots that would take dozens of lines in raw Matplotlib.

This story—**The 2026 Python Metromap: Seaborn – Statistical Visualization**—is your guide to mastering Seaborn. We'll create heatmaps for correlation matrices and customer segmentation. We'll build pair plots for exploring relationships between multiple variables. We'll create distribution plots (histograms, KDE, rug plots) and categorical plots (box plots, violin plots, swarm plots). We'll generate regression plots to visualize relationships with confidence intervals. We'll build a complete customer segmentation dashboard.

**Let's visualize statistically.**

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

### Series G: Data Science & Visualization (5 Stories)

- 🔢 **The 2026 Python Metromap: NumPy – Numerical Computing** – Processing millions of sensor readings; matrix operations; statistical aggregates.

- 🐼 **The 2026 Python Metromap: Pandas – Data Wrangling** – Multi-year sales analysis; CSV cleaning; regional and product aggregation.

- 📈 **The 2026 Python Metromap: Matplotlib – Basic Plotting** – Stock price line charts; sales bar charts; market share pie charts.

- 🎨 **The 2026 Python Metromap: Seaborn – Statistical Visualization** – Customer segmentation heatmaps; age distribution plots; feature correlation pair plots. **⬅️ YOU ARE HERE**

- 📊 **The 2026 Python Metromap: Real-World EDA Project** – End-to-end exploratory data analysis on COVID-19 data, housing prices, or e-commerce sales. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🎨 Section 1: Seaborn Basics – Setting Up and Distribution Plots

Seaborn builds on Matplotlib and integrates seamlessly with Pandas DataFrames.

**SOLID Principle Applied: Single Responsibility** – Each Seaborn function creates one type of statistical visualization.

**Design Pattern: Facade Pattern** – Seaborn provides a simplified interface for statistical plots.

```python
"""
SEABORN BASICS: SETTING UP AND DISTRIBUTION PLOTS

This section covers the fundamentals of Seaborn and distribution visualizations.

SOLID Principle: Single Responsibility
- Each Seaborn function creates one type of statistical visualization

Design Pattern: Facade Pattern
- Seaborn provides a simplified interface for statistical plots
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_palette("husl")


def demonstrate_seaborn_setup():
    """
    Demonstrates Seaborn configuration and themes.
    
    Seaborn offers several built-in themes and color palettes.
    """
    print("=" * 60)
    print("SECTION 1A: SEABORN SETUP AND THEMES")
    print("=" * 60)
    
    # Generate sample data
    np.random.seed(42)
    data = np.random.normal(0, 1, 1000)
    
    print("\n1. SEABORN THEMES")
    print("-" * 40)
    
    themes = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, theme in enumerate(themes):
        if i < len(themes):
            with sns.axes_style(theme):
                ax = axes[i]
                sns.histplot(data, kde=True, ax=ax)
                ax.set_title(f"Theme: {theme}")
    
    # Hide unused subplot
    axes[5].axis('off')
    
    plt.suptitle('Seaborn Themes Comparison', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed Seaborn theme comparison")
    
    # COLOR PALETTES
    print("\n2. COLOR PALETTES")
    print("-" * 40)
    
    palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()
    
    for i, palette in enumerate(palettes):
        sns.set_palette(palette)
        ax = axes[i]
        data = np.random.randn(50, 10)
        sns.boxplot(data=data, ax=ax)
        ax.set_title(f"Palette: {palette}")
    
    plt.suptitle('Seaborn Color Palettes', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed color palette comparison")
    
    # RESET TO DEFAULT
    sns.set_palette("husl")


def demonstrate_distribution_plots():
    """
    Demonstrates distribution plots: histograms, KDE, and rug plots.
    
    Distribution plots show how data is spread across values.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: DISTRIBUTION PLOTS")
    print("=" * 60)
    
    # Generate sample data
    np.random.seed(42)
    normal_data = np.random.normal(0, 1, 1000)
    bimodal_data = np.concatenate([np.random.normal(-2, 0.5, 500), 
                                    np.random.normal(2, 0.5, 500)])
    skewed_data = np.random.exponential(2, 1000)
    
    # HISTOGRAM
    print("\n1. HISTOGRAM (distplot/histplot)")
    print("-" * 40)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Normal distribution
    sns.histplot(normal_data, kde=True, bins=30, ax=axes[0])
    axes[0].set_title("Normal Distribution")
    
    # Bimodal distribution
    sns.histplot(bimodal_data, kde=True, bins=30, ax=axes[1])
    axes[1].set_title("Bimodal Distribution")
    
    # Skewed distribution
    sns.histplot(skewed_data, kde=True, bins=30, ax=axes[2])
    axes[2].set_title("Skewed Distribution")
    
    plt.suptitle("Distribution Plots", fontsize=14, font-weight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed histogram with KDE overlay")
    
    # KDE PLOT ONLY
    print("\n2. KDE PLOT (Kernel Density Estimate)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.kdeplot(normal_data, label='Normal', linewidth=2)
    sns.kdeplot(bimodal_data, label='Bimodal', linewidth=2)
    sns.kdeplot(skewed_data, label='Skewed', linewidth=2)
    plt.title("Kernel Density Estimate (KDE) Plots")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed KDE plots")
    
    # RUG PLOT
    print("\n3. RUG PLOT (Tick marks for each data point)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.kdeplot(normal_data, linewidth=2, label='Density')
    sns.rugplot(normal_data, color='red', alpha=0.3, height=0.05, label='Data points')
    plt.title("KDE with Rug Plot")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed KDE with rug plot")
    
    # ECOLOGICAL DATA EXAMPLE
    print("\n4. REAL-WORLD: SPECIES LENGTH DISTRIBUTIONS")
    print("-" * 40)
    
    # Load iris dataset
    iris = sns.load_dataset('iris')
    
    plt.figure(figsize=(12, 6))
    
    # Histogram with hue
    sns.histplot(data=iris, x='sepal_length', hue='species', 
                 kde=True, bins=20, alpha=0.5)
    plt.title("Sepal Length Distribution by Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
    print("  Displayed species length distributions")


def demonstrate_categorical_plots():
    """
    Demonstrates categorical plots: box plots, violin plots, swarm plots.
    
    Categorical plots compare distributions across categories.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: CATEGORICAL PLOTS")
    print("=" * 60)
    
    # Load data
    tips = sns.load_dataset('tips')
    
    print("\n1. BOX PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
    plt.title("Bill Amount by Day and Gender")
    plt.xlabel("Day of Week")
    plt.ylabel("Total Bill ($)")
    plt.tight_layout()
    plt.show()
    print("  Displayed box plot with hue")
    
    # VIOLIN PLOT
    print("\n2. VIOLIN PLOT (Box plot + KDE)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
    plt.title("Bill Distribution by Day and Gender (Violin Plot)")
    plt.xlabel("Day of Week")
    plt.ylabel("Total Bill ($)")
    plt.tight_layout()
    plt.show()
    print("  Displayed violin plot with split hue")
    
    # SWARM PLOT
    print("\n3. SWARM PLOT (All data points)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True)
    plt.title("Individual Bill Amounts by Day and Gender")
    plt.xlabel("Day of Week")
    plt.ylabel("Total Bill ($)")
    plt.tight_layout()
    plt.show()
    print("  Displayed swarm plot")
    
    # COMBINED PLOT (Box + Swarm)
    print("\n4. COMBINED PLOT (Box + Swarm)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=tips, x='day', y='total_bill', color='lightgray')
    sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex', dodge=True)
    plt.title("Bill Distribution with Individual Points")
    plt.xlabel("Day of Week")
    plt.ylabel("Total Bill ($)")
    plt.tight_layout()
    plt.show()
    print("  Displayed combined box and swarm plot")
    
    # POINT PLOT (Aggregated data)
    print("\n5. POINT PLOT (Aggregated statistics)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=tips, x='day', y='total_bill', hue='sex', 
                  dodge=True, markers=['o', 's'], linestyles=['-', '--'])
    plt.title("Average Bill by Day and Gender")
    plt.xlabel("Day of Week")
    plt.ylabel("Average Bill ($)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed point plot")
    
    # COUNT PLOT (Bar chart of frequencies)
    print("\n6. COUNT PLOT (Frequency bar chart)")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    sns.countplot(data=tips, x='day', hue='sex')
    plt.title("Number of Transactions by Day and Gender")
    plt.xlabel("Day of Week")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
    print("  Displayed count plot")


if __name__ == "__main__":
    demonstrate_seaborn_setup()
    demonstrate_distribution_plots()
    demonstrate_categorical_plots()
```

---

## 🔥 Section 2: Correlation and Heatmaps

Heatmaps visualize correlation matrices and other 2D data, making patterns immediately apparent.

**SOLID Principle Applied: Single Responsibility** – Heatmap visualizes one matrix at a time.

**Design Pattern: Strategy Pattern** – Different colormaps for different data types.

```python
"""
CORRELATION AND HEATMAPS

This section covers heatmaps for visualizing correlation matrices.

SOLID Principle: Single Responsibility
- Heatmap visualizes one matrix at a time

Design Pattern: Strategy Pattern
- Different colormaps for different data types
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demonstrate_correlation_heatmaps():
    """
    Demonstrates heatmaps for correlation matrices.
    
    Heatmaps show the strength of relationships between variables.
    """
    print("=" * 60)
    print("SECTION 2A: CORRELATION HEATMAPS")
    print("=" * 60)
    
    # Load dataset
    print("\n1. LOADING AND PREPARING DATA")
    print("-" * 40)
    
    # Load tips dataset
    tips = sns.load_dataset('tips')
    
    # Select numeric columns
    numeric_cols = ['total_bill', 'tip', 'size']
    numeric_data = tips[numeric_cols]
    
    print(f"  Dataset shape: {tips.shape}")
    print(f"  Numeric columns: {numeric_cols}")
    
    # Calculate correlation matrix
    corr_matrix = numeric_data.corr()
    print(f"\n  Correlation matrix:\n{corr_matrix}")
    
    # BASIC HEATMAP
    print("\n2. BASIC CORRELATION HEATMAP")
    print("-" * 40)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title("Correlation Heatmap - Tips Dataset", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed basic correlation heatmap")
    
    # CUSTOMIZED HEATMAP
    print("\n3. CUSTOMIZED HEATMAP")
    print("-" * 40)
    
    # Use mask to show only upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f',
                cmap='RdBu_r', center=0, square=True,
                linewidths=0.5, cbar_kws={"shrink": 0.8})
    plt.title("Correlation Heatmap (Upper Triangle)", fontsize=14, font-weight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed heatmap with upper triangle only")
    
    # REAL-WORLD: IRIS DATASET
    print("\n4. REAL-WORLD: IRIS DATASET CORRELATIONS")
    print("-" * 40)
    
    iris = sns.load_dataset('iris')
    numeric_iris = iris.select_dtypes(include=[np.number])
    corr_iris = numeric_iris.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_iris, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, square=True, linewidths=1,
                cbar_kws={"shrink": 0.8})
    plt.title("Iris Dataset - Feature Correlations", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed Iris correlation heatmap")
    
    # HIERARCHICAL CLUSTERING HEATMAP
    print("\n5. CLUSTERMAP (Hierarchical clustering)")
    print("-" * 40)
    
    # Create sample data with clusters
    np.random.seed(42)
    n_samples = 50
    n_features = 10
    
    # Create three clusters
    cluster1 = np.random.randn(n_samples, n_features) + 2
    cluster2 = np.random.randn(n_samples, n_features)
    cluster3 = np.random.randn(n_samples, n_features) - 2
    
    data = np.vstack([cluster1, cluster2, cluster3])
    df = pd.DataFrame(data, columns=[f'Feature_{i}' for i in range(n_features)])
    
    # Create clustermap
    g = sns.clustermap(df, cmap='viridis', figsize=(12, 10),
                       col_cluster=True, row_cluster=True,
                       dendrogram_ratio=0.1, cbar_pos=(0.02, 0.8, 0.03, 0.18))
    g.fig.suptitle("Clustered Data Heatmap", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed clustered heatmap with dendrograms")


def demonstrate_advanced_heatmaps():
    """
    Demonstrates advanced heatmap techniques.
    
    Including custom annotations, different colormaps, and annotations.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: ADVANCED HEATMAPS")
    print("=" * 60)
    
    # CUSTOM DATA FOR HEATMAP
    print("\n1. CUSTOM DATA HEATMAP")
    print("-" * 40)
    
    # Create time-series data for heatmap
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    hours = range(24)
    data = np.random.randn(len(dates), len(hours)) + 10
    
    # Add pattern
    for i, hour in enumerate(hours):
        if 9 <= hour <= 17:
            data[:, i] += 5
    
    df = pd.DataFrame(data, index=dates.strftime('%m-%d'), columns=hours)
    
    plt.figure(figsize=(14, 8))
    sns.heatmap(df, cmap='YlOrRd', cbar_kws={'label': 'Value'})
    plt.title("Hourly Data Heatmap", fontsize=14, fontweight='bold')
    plt.xlabel("Hour of Day")
    plt.ylabel("Date")
    plt.tight_layout()
    plt.show()
    print("  Displayed time-series heatmap")
    
    # CONFUSION MATRIX HEATMAP
    print("\n2. CONFUSION MATRIX VISUALIZATION")
    print("-" * 40)
    
    # Simulate confusion matrix
    classes = ['Class A', 'Class B', 'Class C', 'Class D']
    cm = np.array([
        [85, 8, 4, 3],
        [6, 78, 10, 6],
        [4, 9, 82, 5],
        [5, 7, 6, 82]
    ])
    
    # Normalize to percentages
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm_percent, annot=True, fmt='.1f', cmap='Blues',
                xticklabels=classes, yticklabels=classes,
                cbar_kws={'label': 'Percentage (%)'})
    plt.title("Confusion Matrix", fontsize=14, fontweight='bold')
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.show()
    print("  Displayed confusion matrix heatmap")
    
    # CUSTOM ANNOTATIONS
    print("\n3. HEATMAP WITH CUSTOM ANNOTATIONS")
    print("-" * 40)
    
    # Create sales data by region and quarter
    regions = ['North', 'South', 'East', 'West']
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    sales_data = np.array([
        [120, 135, 150, 145],
        [95, 110, 125, 130],
        [105, 115, 130, 140],
        [110, 125, 140, 155]
    ])
    
    # Create custom annotations with both value and growth
    annotations = []
    for i in range(len(regions)):
        row = []
        for j in range(len(quarters)):
            value = sales_data[i, j]
            if j > 0:
                growth = ((value - sales_data[i, j-1]) / sales_data[i, j-1]) * 100
                row.append(f"{value}\n({growth:+.1f}%)")
            else:
                row.append(f"{value}")
        annotations.append(row)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(sales_data, annot=annotations, fmt='', cmap='Greens',
                xticklabels=quarters, yticklabels=regions,
                cbar_kws={'label': 'Sales ($K)'})
    plt.title("Quarterly Sales by Region", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed heatmap with custom annotations")
    
    # TRIANGULAR HEATMAP (for correlation)
    print("\n4. TRIANGULAR HEATMAP")
    print("-" * 40)
    
    # Load flights dataset
    flights = sns.load_dataset('flights')
    flights_pivot = flights.pivot(index='month', columns='year', values='passengers')
    
    # Create mask for upper triangle
    mask = np.triu(np.ones_like(flights_pivot, dtype=bool))
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(flights_pivot, mask=mask, cmap='coolwarm',
                annot=True, fmt='d', center=flights_pivot.values.mean(),
                cbar_kws={'label': 'Passengers'})
    plt.title("Monthly Flight Passengers (Lower Triangle)", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed triangular heatmap")


def build_customer_segmentation_heatmap():
    """
    Builds a customer segmentation heatmap for marketing analysis.
    
    Design Pattern: Composite Pattern - Multiple visualizations for segmentation.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: CUSTOMER SEGMENTATION HEATMAP")
    print("=" * 60)
    
    # Generate customer data
    np.random.seed(42)
    n_customers = 200
    
    # Create customer segments
    segments = ['Premium', 'Regular', 'Budget', 'Occasional']
    segment_weights = [0.2, 0.4, 0.3, 0.1]
    customer_segments = np.random.choice(segments, n_customers, p=segment_weights)
    
    # Generate behavioral metrics by segment
    data = []
    for segment in customer_segments:
        if segment == 'Premium':
            row = [
                np.random.uniform(5000, 20000),  # Annual spend
                np.random.uniform(20, 50),       # Purchase frequency
                np.random.uniform(4.5, 5.0),     # Satisfaction
                np.random.uniform(1, 3)          # Support tickets
            ]
        elif segment == 'Regular':
            row = [
                np.random.uniform(1000, 5000),
                np.random.uniform(10, 20),
                np.random.uniform(4.0, 4.5),
                np.random.uniform(2, 5)
            ]
        elif segment == 'Budget':
            row = [
                np.random.uniform(200, 1000),
                np.random.uniform(3, 10),
                np.random.uniform(3.5, 4.0),
                np.random.uniform(3, 7)
            ]
        else:  # Occasional
            row = [
                np.random.uniform(50, 200),
                np.random.uniform(1, 3),
                np.random.uniform(3.0, 3.5),
                np.random.uniform(0, 2)
            ]
        data.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Annual_Spend', 'Purchase_Frequency', 
                                      'Satisfaction', 'Support_Tickets'])
    df['Segment'] = customer_segments
    
    print("\n1. CUSTOMER SEGMENT DATA")
    print("-" * 40)
    print(f"  Total customers: {n_customers}")
    print(f"  Segment distribution:\n{df['Segment'].value_counts()}")
    
    # Correlation heatmap by segment
    print("\n2. CORRELATION HEATMAP BY SEGMENT")
    print("-" * 40)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    for i, segment in enumerate(segments):
        segment_data = df[df['Segment'] == segment].drop('Segment', axis=1)
        corr = segment_data.corr()
        
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                    center=0, square=True, ax=axes[i],
                    cbar_kws={"shrink": 0.8})
        axes[i].set_title(f"{segment} Segment - Correlations", fontsize=12, fontweight='bold')
    
    plt.suptitle("Customer Segment Correlation Analysis", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed segment correlation heatmaps")
    
    # CLUSTER HEATMAP
    print("\n3. CUSTOMER CLUSTERING HEATMAP")
    print("-" * 40)
    
    # Normalize data for clustering
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.drop('Segment', axis=1))
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns[:-1])
    
    # Add segment labels for reference
    scaled_df['Segment'] = df['Segment']
    
    # Create clustermap
    g = sns.clustermap(scaled_df.drop('Segment', axis=1), 
                       cmap='RdBu_r', center=0,
                       figsize=(14, 12),
                       col_cluster=True, row_cluster=True,
                       dendrogram_ratio=0.1,
                       cbar_pos=(0.02, 0.8, 0.03, 0.18))
    
    # Add segment annotation
    segment_colors = {'Premium': 'red', 'Regular': 'blue', 
                      'Budget': 'green', 'Occasional': 'orange'}
    row_colors = [segment_colors[s] for s in df['Segment']]
    
    g = sns.clustermap(scaled_df.drop('Segment', axis=1), 
                       cmap='RdBu_r', center=0,
                       figsize=(14, 12),
                       row_colors=row_colors,
                       col_cluster=True, row_cluster=True,
                       dendrogram_ratio=0.1,
                       cbar_pos=(0.02, 0.8, 0.03, 0.18))
    
    g.fig.suptitle("Customer Segmentation Clustering", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed customer clustering heatmap")


if __name__ == "__main__":
    demonstrate_correlation_heatmaps()
    demonstrate_advanced_heatmaps()
    build_customer_segmentation_heatmap()
```

---

## 📊 Section 3: Pair Plots and Relationship Visualization

Pair plots visualize relationships between multiple variables simultaneously.

**SOLID Principle Applied: Single Responsibility** – Each subplot shows one relationship.

**Design Pattern: Facet Pattern** – Multiple plots arranged in a grid.

```python
"""
PAIR PLOTS AND RELATIONSHIP VISUALIZATION

This section covers pair plots for multi-variable relationships.

SOLID Principle: Single Responsibility
- Each subplot shows one relationship

Design Pattern: Facet Pattern
- Multiple plots arranged in a grid
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demonstrate_pair_plots():
    """
    Demonstrates pair plots for exploring multiple variable relationships.
    
    Pair plots show scatter plots for every pair of variables.
    """
    print("=" * 60)
    print("SECTION 3A: PAIR PLOTS")
    print("=" * 60)
    
    # Load iris dataset
    iris = sns.load_dataset('iris')
    
    print("\n1. BASIC PAIR PLOT")
    print("-" * 40)
    
    sns.pairplot(iris, hue='species')
    plt.suptitle("Iris Dataset - Pair Plot", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed basic pair plot")
    
    # CUSTOMIZED PAIR PLOT
    print("\n2. CUSTOMIZED PAIR PLOT")
    print("-" * 40)
    
    g = sns.pairplot(iris, hue='species', 
                     diag_kind='kde',
                     plot_kws={'alpha': 0.6, 's': 40, 'edgecolor': 'black'},
                     diag_kws={'fill': True})
    
    # Add title
    g.fig.suptitle("Iris Dataset - Customized Pair Plot", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed customized pair plot")
    
    # PAIR PLOT WITH SPECIFIC VARIABLES
    print("\n3. PAIR PLOT WITH SELECTED VARIABLES")
    print("-" * 40)
    
    vars_to_plot = ['sepal_length', 'sepal_width', 'petal_length']
    sns.pairplot(iris, vars=vars_to_plot, hue='species',
                 diag_kind='hist', plot_kws={'alpha': 0.6})
    plt.suptitle("Selected Variables Pair Plot", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed pair plot with selected variables")
    
    # REAL-WORLD: TIPS DATASET
    print("\n4. REAL-WORLD: TIPS DATASET PAIR PLOT")
    print("-" * 40)
    
    tips = sns.load_dataset('tips')
    numeric_cols = ['total_bill', 'tip', 'size']
    
    sns.pairplot(tips[numeric_cols])
    plt.suptitle("Tips Dataset - Numeric Variable Relationships", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed tips dataset pair plot")


def demonstrate_joint_plots():
    """
    Demonstrates joint plots for two-variable relationships.
    
    Joint plots combine scatter plots with marginal distributions.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: JOINT PLOTS")
    print("=" * 60)
    
    # Load data
    tips = sns.load_dataset('tips')
    
    # BASIC JOINT PLOT
    print("\n1. BASIC JOINT PLOT (Scatter + Histograms)")
    print("-" * 40)
    
    sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter')
    plt.suptitle("Bill vs Tip - Joint Distribution", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed basic joint plot")
    
    # JOINT PLOT WITH REGRESSION
    print("\n2. JOINT PLOT WITH REGRESSION LINE")
    print("-" * 40)
    
    sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')
    plt.suptitle("Bill vs Tip with Regression", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed joint plot with regression")
    
    # JOINT PLOT WITH HEXBIN
    print("\n3. JOINT PLOT WITH HEXBIN (For dense data)")
    print("-" * 40)
    
    sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')
    plt.suptitle("Bill vs Tip - Hexbin Plot", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed hexbin joint plot")
    
    # JOINT PLOT WITH KDE
    print("\n4. JOINT PLOT WITH KDE")
    print("-" * 40)
    
    sns.jointplot(data=tips, x='total_bill', y='tip', kind='kde', fill=True)
    plt.suptitle("Bill vs Tip - KDE Contour", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed KDE joint plot")
    
    # CUSTOMIZED JOINT PLOT
    print("\n5. CUSTOMIZED JOINT PLOT")
    print("-" * 40)
    
    g = sns.JointGrid(data=tips, x='total_bill', y='tip')
    g.plot_joint(sns.scatterplot, alpha=0.5, color='steelblue')
    g.plot_marginals(sns.histplot, color='steelblue', alpha=0.5, bins=20)
    g.set_axis_labels('Total Bill ($)', 'Tip ($)')
    g.fig.suptitle("Customized Joint Plot", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed customized joint plot")


def demonstrate_regression_plots():
    """
    Demonstrates regression plots for visualizing relationships.
    
    Regression plots show linear relationships with confidence intervals.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: REGRESSION PLOTS")
    print("=" * 60)
    
    # Load data
    tips = sns.load_dataset('tips')
    
    # BASIC REGRESSION PLOT
    print("\n1. BASIC REGRESSION PLOT (lmplot)")
    print("-" * 40)
    
    sns.lmplot(data=tips, x='total_bill', y='tip')
    plt.suptitle("Bill vs Tip - Linear Regression", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed basic regression plot")
    
    # REGRESSION WITH HUE
    print("\n2. REGRESSION PLOT WITH HUE (Multiple lines)")
    print("-" * 40)
    
    sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')
    plt.suptitle("Bill vs Tip - Regression by Gender", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed regression plot with hue")
    
    # REGRESSION WITH COLUMNS (Facets)
    print("\n3. REGRESSION PLOT WITH FACETS")
    print("-" * 40)
    
    sns.lmplot(data=tips, x='total_bill', y='tip', col='day', hue='sex')
    plt.suptitle("Bill vs Tip - Regression by Day and Gender", y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed faceted regression plot")
    
    # REGRESSION WITH POLYNOMIAL ORDER
    print("\n4. POLYNOMIAL REGRESSION (order=2)")
    print("-" * 40)
    
    sns.lmplot(data=tips, x='total_bill', y='tip', order=2)
    plt.suptitle("Quadratic Regression", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed polynomial regression")
    
    # REGRESSION WITH LOWESS (Non-parametric)
    print("\n5. LOWESS REGRESSION (Local regression)")
    print("-" * 40)
    
    sns.lmplot(data=tips, x='total_bill', y='tip', lowess=True)
    plt.suptitle("Lowess Regression (Non-parametric)", y=1.02, fontsize=14, fontweight='bold')
    plt.show()
    print("  Displayed Lowess regression")
    
    # RESIDUAL PLOT
    print("\n6. RESIDUAL PLOT (Check assumptions)")
    print("-" * 40)
    
    from scipy import stats
    
    # Calculate regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(tips['total_bill'], tips['tip'])
    predicted = intercept + slope * tips['total_bill']
    residuals = tips['tip'] - predicted
    
    plt.figure(figsize=(10, 6))
    plt.scatter(predicted, residuals, alpha=0.5)
    plt.axhline(y=0, color='red', linestyle='--')
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot - Checking Homoscedasticity", fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed residual plot")


def build_feature_correlation_dashboard():
    """
    Builds a comprehensive feature correlation dashboard.
    
    Design Pattern: Composite Pattern - Multiple related visualizations.
    """
    print("\n" + "=" * 60)
    print("SECTION 3D: FEATURE CORRELATION DASHBOARD")
    print("=" * 60)
    
    # Load Boston housing dataset (simulated if not available)
    try:
        from sklearn.datasets import fetch_california_housing
        housing = fetch_california_housing()
        df = pd.DataFrame(housing.data, columns=housing.feature_names)
        df['MedHouseVal'] = housing.target
    except:
        # Generate synthetic data
        np.random.seed(42)
        n = 1000
        df = pd.DataFrame({
            'MedInc': np.random.exponential(5, n),
            'HouseAge': np.random.uniform(1, 50, n),
            'AveRooms': np.random.uniform(1, 10, n),
            'AveBedrms': np.random.uniform(0.5, 3, n),
            'Population': np.random.uniform(100, 5000, n),
            'AveOccup': np.random.uniform(1, 5, n),
            'Latitude': np.random.uniform(32, 42, n),
            'Longitude': np.random.uniform(-124, -114, n),
            'MedHouseVal': np.random.uniform(0.5, 5, n)
        })
    
    print("\n1. FEATURE CORRELATION DASHBOARD")
    print("-" * 40)
    print(f"  Dataset shape: {df.shape}")
    print(f"  Features: {list(df.columns)}")
    
    # Create dashboard
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Correlation heatmap (top left)
    ax1 = plt.subplot(2, 2, 1)
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, square=True, ax=ax1,
                cbar_kws={"shrink": 0.8})
    ax1.set_title("Feature Correlation Matrix", fontsize=12, fontweight='bold')
    
    # 2. Top correlations with target (top right)
    ax2 = plt.subplot(2, 2, 2)
    target_corr = corr_matrix['MedHouseVal'].drop('MedHouseVal').sort_values()
    colors = ['red' if x < 0 else 'green' for x in target_corr.values]
    ax2.barh(target_corr.index, target_corr.values, color=colors)
    ax2.set_xlabel("Correlation with MedHouseVal")
    ax2.set_title("Feature Importance (Correlation with Target)", fontsize=12, fontweight='bold')
    ax2.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    ax2.grid(True, alpha=0.3, axis='x')
    
    # 3. Pair plot of top features (bottom left)
    ax3 = plt.subplot(2, 2, 3)
    top_features = target_corr.abs().nlargest(3).index.tolist()
    features_to_plot = top_features + ['MedHouseVal']
    from pandas.plotting import scatter_matrix
    scatter_matrix(df[features_to_plot], alpha=0.5, figsize=(8, 8), ax=ax3, diagonal='hist')
    ax3.set_title("Top Features Pair Plot", fontsize=12, fontweight='bold')
    
    # 4. Regression plot (bottom right)
    ax4 = plt.subplot(2, 2, 4)
    best_feature = target_corr.abs().idxmax()
    sns.regplot(data=df, x=best_feature, y='MedHouseVal', ax=ax4,
                scatter_kws={'alpha': 0.3}, line_kws={'color': 'red'})
    ax4.set_title(f"Best Predictor: {best_feature} vs Target", fontsize=12, fontweight='bold')
    ax4.set_xlabel(best_feature)
    ax4.set_ylabel("MedHouseVal")
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle("Feature Correlation Analysis Dashboard", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed feature correlation dashboard")


if __name__ == "__main__":
    demonstrate_pair_plots()
    demonstrate_joint_plots()
    demonstrate_regression_plots()
    build_feature_correlation_dashboard()
```

---

## 📊 Section 4: Multi-Plot Grids and Facets

Facet grids allow you to create multiple plots based on categorical variables.

**SOLID Principle Applied: Single Responsibility** – Each facet shows one subset of data.

**Design Pattern: Facade Pattern** – FacetGrid provides a simplified interface for multi-plot figures.

```python
"""
MULTI-PLOT GRIDS AND FACETS

This section covers creating multiple plots based on categorical variables.

SOLID Principle: Single Responsibility
- Each facet shows one subset of data

Design Pattern: Facade Pattern
- FacetGrid provides a simplified interface for multi-plot figures
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demonstrate_facet_grid():
    """
    Demonstrates FacetGrid for creating multiple plots.
    
    FacetGrid creates a grid of plots based on categorical variables.
    """
    print("=" * 60)
    print("SECTION 4A: FACET GRID")
    print("=" * 60)
    
    # Load data
    tips = sns.load_dataset('tips')
    
    # BASIC FACET GRID
    print("\n1. BASIC FACET GRID (By day)")
    print("-" * 40)
    
    g = sns.FacetGrid(tips, col='day', height=4)
    g.map(sns.histplot, 'total_bill', bins=15)
    g.set_axis_labels('Total Bill ($)', 'Count')
    g.set_titles(col_template='{col_name}')
    plt.suptitle('Bill Distribution by Day', y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed facet grid by day")
    
    # FACET GRID WITH ROW AND COLUMN
    print("\n2. FACET GRID WITH ROW AND COLUMN")
    print("-" * 40)
    
    g = sns.FacetGrid(tips, col='time', row='sex', height=4)
    g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.6)
    g.set_axis_labels('Total Bill ($)', 'Tip ($)')
    g.set_titles(col_template='{col_name}', row_template='{row_name}')
    plt.suptitle('Bill vs Tip by Time and Gender', y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed 2D facet grid")
    
    # FACET GRID WITH HUE
    print("\n3. FACET GRID WITH HUE")
    print("-" * 40)
    
    g = sns.FacetGrid(tips, col='day', hue='sex', height=4)
    g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.7)
    g.add_legend()
    g.set_axis_labels('Total Bill ($)', 'Tip ($)')
    plt.suptitle('Bill vs Tip by Day and Gender', y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed facet grid with hue")
    
    # CUSTOM MAPPING FUNCTION
    print("\n4. CUSTOM MAPPING FUNCTION")
    print("-" * 40)
    
    def plot_with_regression(data, **kwargs):
        """Custom plotting function."""
        x = data['total_bill']
        y = data['tip']
        plt.scatter(x, y, alpha=0.5, **kwargs)
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(np.sort(x), p(np.sort(x)), 'r--', linewidth=2)
        plt.text(0.05, 0.95, f'y={z[0]:.2f}x+{z[1]:.2f}', 
                transform=plt.gca().transAxes, fontsize=10)
    
    g = sns.FacetGrid(tips, col='day', height=4)
    g.map_dataframe(plot_with_regression)
    g.set_axis_labels('Total Bill ($)', 'Tip ($)')
    plt.suptitle('Bill vs Tip with Regression by Day', y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed facet grid with custom function")


def demonstrate_pair_grid():
    """
    Demonstrates PairGrid for pairwise relationships.
    
    PairGrid allows fine-grained control over pairwise plots.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: PAIR GRID")
    print("=" * 60)
    
    # Load data
    iris = sns.load_dataset('iris')
    
    # BASIC PAIR GRID
    print("\n1. BASIC PAIR GRID")
    print("-" * 40)
    
    g = sns.PairGrid(iris, hue='species')
    g.map_upper(sns.scatterplot)
    g.map_lower(sns.kdeplot)
    g.map_diag(sns.histplot)
    g.add_legend()
    plt.suptitle('Iris Dataset - Pair Grid', y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed basic pair grid")
    
    # CUSTOM PAIR GRID
    print("\n2. CUSTOM PAIR GRID")
    print("-" * 40)
    
    def corrfunc(x, y, **kwargs):
        """Display correlation coefficient."""
        r = np.corrcoef(x, y)[0, 1]
        ax = plt.gca()
        ax.annotate(f'r = {r:.2f}', xy=(0.1, 0.9), xycoords=ax.transAxes,
                    fontsize=12, fontweight='bold')
    
    g = sns.PairGrid(iris, diag_sharey=False)
    g.map_upper(sns.scatterplot, alpha=0.5)
    g.map_upper(corrfunc)
    g.map_lower(sns.kdeplot, cmap='Blues_d')
    g.map_diag(sns.histplot, kde=True)
    plt.suptitle('Iris Dataset - Custom Pair Grid', y=1.02, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed custom pair grid")


def build_complete_eda_dashboard():
    """
    Builds a complete exploratory data analysis dashboard.
    
    Design Pattern: Composite Pattern - Multiple visualization types combined.
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: COMPLETE EDA DASHBOARD")
    print("=" * 60)
    
    # Load and prepare data
    tips = sns.load_dataset('tips')
    
    # Add derived columns
    tips['tip_percent'] = (tips['tip'] / tips['total_bill']) * 100
    tips['is_weekend'] = tips['day'].isin(['Sat', 'Sun'])
    tips['party_size_category'] = pd.cut(tips['size'], bins=[0, 2, 4, 10], 
                                          labels=['Small (1-2)', 'Medium (3-4)', 'Large (5+)'])
    
    print("\n1. TIPS DATASET OVERVIEW")
    print("-" * 40)
    print(f"  Shape: {tips.shape}")
    print(f"  Columns: {list(tips.columns)}")
    print(f"  Tip percent range: {tips['tip_percent'].min():.1f}% - {tips['tip_percent'].max():.1f}%")
    
    # Create comprehensive dashboard
    fig = plt.figure(figsize=(18, 14))
    
    # 1. Distribution of total bill (top left)
    ax1 = plt.subplot(3, 3, 1)
    sns.histplot(tips['total_bill'], bins=30, kde=True, ax=ax1)
    ax1.set_title('Total Bill Distribution', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Total Bill ($)')
    
    # 2. Distribution of tip percentage (top middle)
    ax2 = plt.subplot(3, 3, 2)
    sns.histplot(tips['tip_percent'], bins=30, kde=True, color='green', ax=ax2)
    ax2.set_title('Tip Percentage Distribution', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Tip (%)')
    
    # 3. Box plot by day (top right)
    ax3 = plt.subplot(3, 3, 3)
    sns.boxplot(data=tips, x='day', y='tip_percent', ax=ax3)
    ax3.set_title('Tip % by Day', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Day')
    ax3.set_ylabel('Tip (%)')
    
    # 4. Scatter plot: bill vs tip (middle left)
    ax4 = plt.subplot(3, 3, 4)
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', alpha=0.6, ax=ax4)
    sns.regplot(data=tips, x='total_bill', y='tip', scatter=False, color='red', ax=ax4)
    ax4.set_title('Bill vs Tip', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Total Bill ($)')
    ax4.set_ylabel('Tip ($)')
    
    # 5. Violin plot by party size (middle)
    ax5 = plt.subplot(3, 3, 5)
    sns.violinplot(data=tips, x='party_size_category', y='tip_percent', ax=ax5)
    ax5.set_title('Tip % by Party Size', fontsize=12, fontweight='bold')
    ax5.set_xlabel('Party Size')
    ax5.set_ylabel('Tip (%)')
    
    # 6. Bar plot: average tip by day and gender (middle right)
    ax6 = plt.subplot(3, 3, 6)
    sns.barplot(data=tips, x='day', y='tip_percent', hue='sex', ax=ax6)
    ax6.set_title('Average Tip % by Day and Gender', fontsize=12, fontweight='bold')
    ax6.set_xlabel('Day')
    ax6.set_ylabel('Average Tip (%)')
    
    # 7. Heatmap: correlation matrix (bottom left)
    ax7 = plt.subplot(3, 3, 7)
    numeric_cols = ['total_bill', 'tip', 'size', 'tip_percent']
    corr = tips[numeric_cols].corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, ax=ax7)
    ax7.set_title('Correlation Matrix', fontsize=12, fontweight='bold')
    
    # 8. Count plot by day (bottom middle)
    ax8 = plt.subplot(3, 3, 8)
    sns.countplot(data=tips, x='day', hue='sex', ax=ax8)
    ax8.set_title('Transaction Count by Day and Gender', fontsize=12, fontweight='bold')
    ax8.set_xlabel('Day')
    ax8.set_ylabel('Count')
    
    # 9. Facet grid summary (bottom right - use inset)
    ax9 = plt.subplot(3, 3, 9)
    # Summary statistics table
    summary = tips.groupby('day').agg({
        'total_bill': ['count', 'mean', 'std'],
        'tip_percent': 'mean'
    }).round(2)
    ax9.axis('off')
    ax9.table(cellText=summary.values,
              rowLabels=summary.index,
              colLabels=['Count', 'Mean Bill', 'Std Bill', 'Avg Tip %'],
              loc='center',
              cellLoc='center')
    ax9.set_title('Summary Statistics by Day', fontsize=12, fontweight='bold')
    
    plt.suptitle('Restaurant Tips - Complete EDA Dashboard', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("\n2. COMPLETE EDA DASHBOARD")
    print("-" * 40)
    print("  Displayed comprehensive EDA dashboard with 9 plots")


if __name__ == "__main__":
    demonstrate_facet_grid()
    demonstrate_pair_grid()
    build_complete_eda_dashboard()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Seaborn Setup** – `sns.set_style()`, `sns.set_palette()`. Themes: darkgrid, whitegrid, dark, white, ticks.

- **Distribution Plots** – `histplot()` (histogram + KDE), `kdeplot()` (density), `rugplot()` (data points). `displot()` for figure-level.

- **Categorical Plots** – `boxplot()`, `violinplot()` (box + KDE), `swarmplot()` (all points), `pointplot()` (aggregated), `countplot()` (frequencies).

- **Correlation Heatmaps** – `heatmap()` for correlation matrices. `clustermap()` with hierarchical clustering. Mask for triangular display.

- **Pair Plots** – `pairplot()` for all variable pairs. `PairGrid` for fine-grained control. Diagonal plots (histogram/KDE).

- **Joint Plots** – `jointplot()` combines scatter with marginal distributions. Kinds: scatter, reg, hex, kde.

- **Regression Plots** – `lmplot()` with confidence intervals. Hue, col, row for faceting. `order` for polynomial, `lowess` for non-parametric.

- **Facet Grids** – `FacetGrid` for multiple plots based on categorical variables. Custom mapping functions.

- **Real-World Applications** – Customer segmentation heatmaps, feature correlation dashboards, restaurant tips EDA.

- **SOLID Principles Applied** – Single Responsibility (each plot type serves one purpose), Open/Closed (customizations add without changing core), Dependency Inversion (plots depend on data abstractions), Interface Segregation (clean plotting interfaces).

- **Design Patterns Used** – Facade Pattern (simplified interface), Facet Pattern (multiple plots), Composite Pattern (dashboard composition), Strategy Pattern (different plot types), Adapter Pattern (Pandas DataFrame integration).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Matplotlib – Basic Plotting

- **📚 Series G Catalog:** Data Science & Visualization – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Real-World EDA Project (Series G, Story 5)

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
| Series G | 5 | 4 | 1 | 80% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **44** | **8** | **85%** |

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

**Next Story:** Series G, Story 5: The 2026 Python Metromap: Real-World EDA Project

---

## 📝 Your Invitation

You've mastered Seaborn. Now build something with what you've learned:

1. **Build a correlation analysis dashboard** – Load any dataset, compute correlations, create heatmap and pair plot.

2. **Create a customer segmentation report** – Use heatmaps and pair plots to visualize segment differences.

3. **Build a time series heatmap** – Create a calendar heatmap showing daily metrics over time.

4. **Create an automated EDA report** – Write a function that generates distribution plots, box plots, and correlation heatmaps for any DataFrame.

5. **Build a model performance dashboard** – Create confusion matrix heatmap, ROC curve, and feature importance plots.

**You've mastered Seaborn. Next stop: Real-World EDA Project!**

---

*Found this helpful? Clap, comment, and share what you visualized with Seaborn. Next stop: Real-World EDA Project!* 🚇