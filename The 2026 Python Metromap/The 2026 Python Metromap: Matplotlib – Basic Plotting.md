# The 2026 Python Metromap: Matplotlib – Basic Plotting

## Series G: Data Science & Visualization | Story 3 of 5

![The 2026 Python Metromap/images/Matplotlib – Basic Plotting](images/Matplotlib – Basic Plotting.png)

## 📖 Introduction

**Welcome to the third stop on the Data Science & Visualization Line.**

You've mastered NumPy for numerical computing and Pandas for data wrangling. You can clean, transform, and aggregate data from multiple sources. But data analysis isn't complete until you can visualize your insights. Numbers in tables are informative, but charts and graphs tell stories that numbers alone cannot.

Matplotlib is the foundational visualization library in Python. It provides complete control over every aspect of your plots—from simple line charts to complex multi-panel figures. While it has a steeper learning curve than some modern libraries, understanding Matplotlib gives you the power to create any visualization imaginable. Almost every other Python visualization library (Seaborn, Plotly, etc.) builds on Matplotlib.

This story—**The 2026 Python Metromap: Matplotlib – Basic Plotting**—is your guide to mastering Matplotlib. We'll create line charts for time series data, bar charts for comparisons, scatter plots for relationships, histograms for distributions, and pie charts for proportions. We'll customize every aspect: colors, labels, titles, legends, grids, and annotations. We'll create subplots and multi-panel figures. We'll build a complete financial dashboard and a sales performance report.

**Let's visualize.**

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

- 📈 **The 2026 Python Metromap: Matplotlib – Basic Plotting** – Stock price line charts; sales bar charts; market share pie charts. **⬅️ YOU ARE HERE**

- 🎨 **The 2026 Python Metromap: Seaborn – Statistical Visualization** – Customer segmentation heatmaps; age distribution plots; feature correlation pair plots. 🔜 *Up Next*

- 📊 **The 2026 Python Metromap: Real-World EDA Project** – End-to-end exploratory data analysis on COVID-19 data, housing prices, or e-commerce sales.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 📈 Section 1: Matplotlib Basics – Your First Plot

Matplotlib's pyplot module provides a MATLAB-like interface for creating plots quickly.

**SOLID Principle Applied: Single Responsibility** – Each plotting function creates one type of visualization.

**Design Pattern: Facade Pattern** – Pyplot provides a simplified interface to Matplotlib's complex internals.

```python
"""
MATPLOTLIB BASICS: YOUR FIRST PLOT

This section covers the fundamentals of creating plots with Matplotlib.

SOLID Principle: Single Responsibility
- Each plotting function creates one type of visualization

Design Pattern: Facade Pattern
- Pyplot provides a simplified interface to Matplotlib's internals
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def demonstrate_line_plot():
    """
    Demonstrates creating basic line plots.
    
    Line plots are ideal for showing trends over time or continuous data.
    """
    print("=" * 60)
    print("SECTION 1A: LINE PLOTS")
    print("=" * 60)
    
    # Create data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.exp(-x/5) * np.sin(x)
    
    # SIMPLE LINE PLOT
    print("\n1. SIMPLE LINE PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1)
    plt.title("Simple Sine Wave")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid(True, alpha=0.3)
    plt.show()
    print("  Displayed sine wave plot")
    
    # MULTIPLE LINES
    print("\n2. MULTIPLE LINES ON ONE PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'b-', label='sin(x)', linewidth=2)
    plt.plot(x, y2, 'r--', label='cos(x)', linewidth=2)
    plt.plot(x, y3, 'g-.', label='damped sin(x)', linewidth=2)
    plt.title("Trigonometric Functions")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.show()
    print("  Displayed multiple line plot with legend")
    
    # CUSTOMIZING LINE STYLES
    print("\n3. LINE STYLES AND MARKERS")
    print("-" * 40)
    
    x_points = np.linspace(0, 5, 10)
    y_points = x_points ** 2
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points, 'ro-', linewidth=2, markersize=8, 
             markerfacecolor='red', markeredgecolor='darkred')
    plt.title("Line with Markers")
    plt.xlabel("X")
    plt.ylabel("X²")
    plt.grid(True, alpha=0.3)
    plt.show()
    print("  Displayed line plot with custom markers")
    
    # STOCK PRICE EXAMPLE
    print("\n4. REAL-WORLD: STOCK PRICE TREND")
    print("-" * 40)
    
    # Generate simulated stock data
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    prices = 100 + np.cumsum(np.random.randn(100) * 2)
    
    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, 'b-', linewidth=1.5)
    plt.title("Stock Price Trend - January to April 2024")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("  Displayed stock price trend")


def demonstrate_bar_chart():
    """
    Demonstrates creating bar charts for categorical comparisons.
    
    Bar charts are ideal for comparing values across categories.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: BAR CHARTS")
    print("=" * 60)
    
    # VERTICAL BAR CHART
    print("\n1. VERTICAL BAR CHART")
    print("-" * 40)
    
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    values = [235, 189, 312, 278, 201]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color='steelblue', edgecolor='black')
    plt.title("Product Sales by Category")
    plt.xlabel("Product")
    plt.ylabel("Sales (units)")
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on top of bars
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                str(value), ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    print("  Displayed vertical bar chart with labels")
    
    # HORIZONTAL BAR CHART
    print("\n2. HORIZONTAL BAR CHART")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(categories, values, color='coral', edgecolor='black')
    plt.title("Product Sales by Category")
    plt.xlabel("Sales (units)")
    plt.ylabel("Product")
    plt.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for bar, value in zip(bars, values):
        plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                str(value), ha='left', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    print("  Displayed horizontal bar chart")
    
    # GROUPED BAR CHART
    print("\n3. GROUPED BAR CHART (Multiple Series)")
    print("-" * 40)
    
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    product_a = [120, 135, 150, 145]
    product_b = [90, 105, 115, 125]
    product_c = [75, 85, 95, 100]
    
    x = np.arange(len(categories))
    width = 0.25
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width, product_a, width, label='Product A', color='steelblue')
    plt.bar(x, product_b, width, label='Product B', color='coral')
    plt.bar(x + width, product_c, width, label='Product C', color='seagreen')
    
    plt.title("Quarterly Sales by Product")
    plt.xlabel("Quarter")
    plt.ylabel("Sales (units)")
    plt.xticks(x, categories)
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed grouped bar chart")
    
    # STACKED BAR CHART
    print("\n4. STACKED BAR CHART")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, product_a, label='Product A', color='steelblue')
    plt.bar(categories, product_b, bottom=product_a, label='Product B', color='coral')
    plt.bar(categories, product_c, bottom=np.array(product_a) + np.array(product_b), 
            label='Product C', color='seagreen')
    
    plt.title("Quarterly Sales Stacked by Product")
    plt.xlabel("Quarter")
    plt.ylabel("Sales (units)")
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed stacked bar chart")


def demonstrate_scatter_plot():
    """
    Demonstrates creating scatter plots for relationships between variables.
    
    Scatter plots reveal correlations, clusters, and outliers.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: SCATTER PLOTS")
    print("=" * 60)
    
    # BASIC SCATTER PLOT
    print("\n1. BASIC SCATTER PLOT")
    print("-" * 40)
    
    # Generate data with correlation
    np.random.seed(42)
    x = np.random.randn(200) * 10 + 50
    y = x * 0.8 + np.random.randn(200) * 10
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.6, c='steelblue', edgecolors='black', linewidth=0.5)
    plt.title("Correlation Between Variables")
    plt.xlabel("Variable X")
    plt.ylabel("Variable Y")
    plt.grid(True, alpha=0.3)
    
    # Add trend line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", linewidth=2, label=f"Trend: y = {z[0]:.2f}x + {z[1]:.2f}")
    plt.legend()
    plt.tight_layout()
    plt.show()
    print("  Displayed scatter plot with trend line")
    
    # SCATTER PLOT WITH SIZE AND COLOR ENCODING
    print("\n2. SCATTER PLOT WITH SIZE AND COLOR")
    print("-" * 40)
    
    n_points = 100
    x = np.random.rand(n_points) * 100
    y = np.random.rand(n_points) * 100
    sizes = np.random.rand(n_points) * 500
    colors = np.random.rand(n_points)
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')
    plt.colorbar(scatter, label='Color Scale')
    plt.title("Scatter Plot with Size and Color Encoding")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed scatter plot with variable size and color")
    
    # REAL-WORLD: SALES VS MARKETING SPEND
    print("\n3. REAL-WORLD: MARKETING ROI ANALYSIS")
    print("-" * 40)
    
    # Generate marketing data
    marketing_spend = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])
    sales = marketing_spend * 2.5 + np.random.randn(len(marketing_spend)) * 500
    
    plt.figure(figsize=(10, 6))
    plt.scatter(marketing_spend, sales, s=100, c='steelblue', alpha=0.7, edgecolors='black')
    plt.title("Marketing ROI Analysis")
    plt.xlabel("Marketing Spend ($)")
    plt.ylabel("Sales ($)")
    plt.grid(True, alpha=0.3)
    
    # Add regression line
    z = np.polyfit(marketing_spend, sales, 1)
    p = np.poly1d(z)
    plt.plot(marketing_spend, p(marketing_spend), "r--", linewidth=2)
    
    # Annotate a point
    max_idx = np.argmax(sales)
    plt.annotate(f"Max ROI: ${sales[max_idx]:,.0f}", 
                xy=(marketing_spend[max_idx], sales[max_idx]),
                xytext=(marketing_spend[max_idx] + 500, sales[max_idx] - 500),
                arrowprops=dict(arrowstyle='->', color='red'))
    
    plt.tight_layout()
    plt.show()
    print("  Displayed marketing ROI scatter plot with annotation")


def demonstrate_histogram():
    """
    Demonstrates creating histograms for distribution analysis.
    
    Histograms show the frequency distribution of a single variable.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: HISTOGRAMS")
    print("=" * 60)
    
    # BASIC HISTOGRAM
    print("\n1. BASIC HISTOGRAM")
    print("-" * 40)
    
    # Generate normal distribution data
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)
    
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
    plt.title("Distribution of Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed basic histogram")
    
    # HISTOGRAM WITH STATISTICS
    print("\n2. HISTOGRAM WITH STATISTICS OVERLAY")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
    
    # Add vertical lines for mean and median
    mean_val = np.mean(data)
    median_val = np.median(data)
    plt.axvline(mean_val, color='red', linestyle='-', linewidth=2, label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
    
    plt.title("Distribution with Statistics")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed histogram with mean and median lines")
    
    # MULTIPLE HISTOGRAMS (Overlaid)
    print("\n3. MULTIPLE HISTOGRAMS (Comparison)")
    print("-" * 40)
    
    # Generate data for two groups
    group_a = np.random.normal(95, 10, 500)
    group_b = np.random.normal(105, 12, 500)
    
    plt.figure(figsize=(10, 6))
    plt.hist(group_a, bins=30, alpha=0.5, label='Group A', color='steelblue', edgecolor='black')
    plt.hist(group_b, bins=30, alpha=0.5, label='Group B', color='coral', edgecolor='black')
    plt.title("Distribution Comparison - Group A vs Group B")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed overlaid histograms")
    
    # REAL-WORLD: AGE DISTRIBUTION
    print("\n4. REAL-WORLD: AGE DISTRIBUTION")
    print("-" * 40)
    
    # Generate age data
    ages = np.random.normal(35, 12, 500)
    ages = np.clip(ages, 18, 80)
    
    plt.figure(figsize=(10, 6))
    plt.hist(ages, bins=20, color='seagreen', edgecolor='black', alpha=0.7, rwidth=0.9)
    plt.title("Customer Age Distribution")
    plt.xlabel("Age (years)")
    plt.ylabel("Number of Customers")
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add age group annotations
    age_groups = [(18, 30, 'Young'), (30, 45, 'Middle'), (45, 60, 'Senior'), (60, 80, 'Elderly')]
    for start, end, label in age_groups:
        plt.axvspan(start, end, alpha=0.1, color='gray')
        plt.text((start + end)/2, plt.ylim()[1] * 0.9, label, ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    print("  Displayed age distribution with demographic annotations")


if __name__ == "__main__":
    demonstrate_line_plot()
    demonstrate_bar_chart()
    demonstrate_scatter_plot()
    demonstrate_histogram()
```

---

## 🎨 Section 2: Customizing Plots – Colors, Labels, and Styles

Matplotlib offers extensive customization options to make your plots publication-ready.

**SOLID Principle Applied: Open/Closed** – Customizations can be added without changing plotting logic.

**Design Pattern: Decorator Pattern** – Styles and customizations decorate the base plot.

```python
"""
CUSTOMIZING PLOTS: COLORS, LABELS, AND STYLES

This section covers advanced customization techniques.

SOLID Principle: Open/Closed
- Customizations can be added without changing plotting logic

Design Pattern: Decorator Pattern
- Styles and customizations decorate the base plot
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D


def demonstrate_color_customization():
    """
    Demonstrates color customization options.
    
    Colors can be specified by name, hex code, RGB, or colormap.
    """
    print("=" * 60)
    print("SECTION 2A: COLOR CUSTOMIZATION")
    print("=" * 60)
    
    # DATA
    x = np.linspace(0, 10, 50)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x + np.pi/2)
    
    # COLOR BY NAME
    print("\n1. COLOR BY NAME")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, color='red', linewidth=2, label='Red')
    plt.plot(x, y2, color='blue', linewidth=2, label='Blue')
    plt.plot(x, y3, color='green', linewidth=2, label='Green')
    plt.title("Named Colors")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    print("  Displayed plot with named colors")
    
    # COLOR BY HEX CODE
    print("\n2. COLOR BY HEX CODE")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, color='#FF5733', linewidth=2, label='#FF5733')
    plt.plot(x, y2, color='#33FF57', linewidth=2, label='#33FF57')
    plt.plot(x, y3, color='#3357FF', linewidth=2, label='#3357FF')
    plt.title("Hex Colors")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    print("  Displayed plot with hex colors")
    
    # COLOR BY RGB (0-1 range)
    print("\n3. COLOR BY RGB VALUES")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, color=(0.8, 0.2, 0.2), linewidth=2, label='RGB (0.8,0.2,0.2)')
    plt.plot(x, y2, color=(0.2, 0.8, 0.2), linewidth=2, label='RGB (0.2,0.8,0.2)')
    plt.plot(x, y3, color=(0.2, 0.2, 0.8), linewidth=2, label='RGB (0.2,0.2,0.8)')
    plt.title("RGB Colors")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    print("  Displayed plot with RGB colors")
    
    # COLORMAPS
    print("\n4. COLORMAPS FOR GRADIENT VISUALIZATION")
    print("-" * 40)
    
    # Create 2D data
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(Z, cmap='viridis', extent=[-3, 3, -3, 3])
    plt.colorbar(label='Intensity')
    plt.title("Viridis Colormap")
    
    plt.subplot(1, 2, 2)
    plt.imshow(Z, cmap='plasma', extent=[-3, 3, -3, 3])
    plt.colorbar(label='Intensity')
    plt.title("Plasma Colormap")
    
    plt.tight_layout()
    plt.show()
    print("  Displayed colormap examples")
    
    # CUSTOM COLOR MAPS
    print("\n5. CUSTOM COLOR MAP FROM LIST")
    print("-" * 40)
    
    from matplotlib.colors import LinearSegmentedColormap
    colors = ['darkblue', 'blue', 'cyan', 'yellow', 'red']
    custom_cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
    
    plt.figure(figsize=(8, 6))
    plt.imshow(Z, cmap=custom_cmap, extent=[-3, 3, -3, 3])
    plt.colorbar(label='Intensity')
    plt.title("Custom Colormap")
    plt.tight_layout()
    plt.show()
    print("  Displayed custom colormap")


def demonstrate_style_customization():
    """
    Demonstrates line styles, markers, and plot styling.
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: STYLE CUSTOMIZATION")
    print("=" * 60)
    
    x = np.linspace(0, 10, 20)
    y = np.sin(x)
    
    # LINE STYLES
    print("\n1. LINE STYLES")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='Solid (b-)')
    plt.plot(x, y + 0.5, 'r--', linewidth=2, label='Dashed (r--)')
    plt.plot(x, y + 1.0, 'g-.', linewidth=2, label='Dash-dot (g-.)')
    plt.plot(x, y + 1.5, 'm:', linewidth=2, label='Dotted (m:)')
    plt.title("Line Styles")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed line style examples")
    
    # MARKER STYLES
    print("\n2. MARKER STYLES")
    print("-" * 40)
    
    x_points = np.linspace(0, 5, 10)
    y_points = x_points ** 2
    
    plt.figure(figsize=(12, 6))
    
    markers = ['o', 's', '^', 'D', 'v', '*', 'x', '+', 'p']
    for i, marker in enumerate(markers):
        y_offset = i * 5
        plt.plot(x_points, y_points + y_offset, marker=marker, linestyle='-', 
                linewidth=1, markersize=8, label=f"Marker: '{marker}'")
    
    plt.title("Marker Styles")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(ncol=3)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed marker style examples")
    
    # BUILT-IN STYLES
    print("\n3. BUILT-IN STYLES")
    print("-" * 40)
    
    print("  Available styles:", plt.style.available[:10], "...")
    
    styles = ['ggplot', 'seaborn-v0_8-darkgrid', 'fivethirtyeight', 'bmh']
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, style in enumerate(styles):
        with plt.style.context(style):
            ax = axes[i]
            ax.plot(x, y, 'b-', linewidth=2)
            ax.plot(x, y + 0.5, 'r--', linewidth=2)
            ax.set_title(f"Style: {style}")
            ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    print("  Displayed different style themes")


def demonstrate_annotation_and_text():
    """
    Demonstrates adding annotations, text, and shapes to plots.
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: ANNOTATIONS AND TEXT")
    print("=" * 60)
    
    # Create sample data
    x = np.linspace(0, 10, 100)
    y = np.exp(-x/5) * np.sin(x)
    
    # BASIC TEXT AND TITLES
    print("\n1. TEXT AND TITLES")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    
    # Add title with customization
    plt.title("Damped Sine Wave", fontsize=16, fontweight='bold', color='navy')
    
    # Axis labels
    plt.xlabel("Time (seconds)", fontsize=12, fontstyle='italic')
    plt.ylabel("Amplitude", fontsize=12)
    
    # Add text box
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(7, 0.5, 'Damped Oscillation', fontsize=10,
            verticalalignment='top', bbox=props)
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed plot with customized text")
    
    # ANNOTATIONS
    print("\n2. ANNOTATIONS WITH ARROWS")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    
    # Find peaks
    peaks_idx = np.where((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:]))[0] + 1
    peak_x = x[peaks_idx[:3]]
    peak_y = y[peaks_idx[:3]]
    
    plt.plot(peak_x, peak_y, 'ro', markersize=8, label='Peaks')
    
    # Annotate each peak
    for i, (px, py) in enumerate(zip(peak_x, peak_y)):
        plt.annotate(f'Peak {i+1}', xy=(px, py), xytext=(px + 0.5, py + 0.1),
                    arrowprops=dict(arrowstyle='->', color='red', lw=1),
                    fontsize=10, fontweight='bold')
    
    plt.title("Peak Detection with Annotations")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed plot with arrow annotations")
    
    # SHAPES AND PATCHES
    print("\n3. SHAPES AND PATCHES")
    print("-" * 40)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2)
    
    # Add rectangle highlight
    rect = Rectangle((2, -0.5), 3, 1, facecolor='yellow', alpha=0.3)
    ax.add_patch(rect)
    
    # Add vertical line
    ax.axvline(x=5, color='red', linestyle='--', linewidth=2, alpha=0.7)
    
    # Add horizontal line
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=1, alpha=0.5)
    
    # Add vertical span
    ax.axvspan(7, 8, alpha=0.3, color='green')
    
    plt.title("Plot with Shapes and Highlighting")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed plot with shapes and highlights")
    
    # LEGEND CUSTOMIZATION
    print("\n4. CUSTOM LEGENDS")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    line1, = plt.plot(x, y, 'b-', linewidth=2, label='Signal')
    line2, = plt.plot(x, np.cos(x), 'r--', linewidth=2, label='Reference')
    
    # Custom legend
    legend = plt.legend(loc='upper right', frameon=True, fancybox=True, 
                       shadow=True, fontsize=10)
    legend.get_frame().set_facecolor('lightyellow')
    legend.get_frame().set_alpha(0.8)
    
    plt.title("Custom Legend")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("  Displayed plot with custom legend")


if __name__ == "__main__":
    demonstrate_color_customization()
    demonstrate_style_customization()
    demonstrate_annotation_and_text()
```

---

## 📊 Section 3: Advanced Plots – Pie, Area, and Box Plots

Advanced plot types for specific visualization needs.

**SOLID Principle Applied: Single Responsibility** – Each plot type serves a specific analytical purpose.

**Design Pattern: Strategy Pattern** – Different plot strategies for different data types.

```python
"""
ADVANCED PLOTS: PIE, AREA, AND BOX PLOTS

This section covers specialized plot types for specific analysis needs.

SOLID Principle: Single Responsibility
- Each plot type serves a specific analytical purpose

Design Pattern: Strategy Pattern
- Different plot strategies for different data types
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demonstrate_pie_charts():
    """
    Demonstrates pie charts for proportional data.
    
    Pie charts show parts of a whole. Use sparingly - bar charts are often better.
    """
    print("=" * 60)
    print("SECTION 3A: PIE CHARTS")
    print("=" * 60)
    
    # BASIC PIE CHART
    print("\n1. BASIC PIE CHART")
    print("-" * 40)
    
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales = [25, 35, 20, 15, 5]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    
    plt.figure(figsize=(8, 8))
    plt.pie(sales, labels=categories, colors=colors, autopct='%1.1f%%', 
            startangle=90, explode=(0.05, 0, 0, 0, 0))
    plt.title("Market Share by Product")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    print("  Displayed basic pie chart")
    
    # PIE CHART WITH CUSTOM LABELS
    print("\n2. PIE CHART WITH DETAILED LABELS")
    print("-" * 40)
    
    plt.figure(figsize=(10, 8))
    
    # Custom autopct function
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return f'{pct:.1f}%\n({val:,})'
        return my_autopct
    
    wedges, texts, autotexts = plt.pie(sales, labels=categories, colors=colors,
                                       autopct=make_autopct(sales), startangle=90,
                                       shadow=True, explode=(0.05, 0, 0, 0, 0))
    
    # Style the text
    for text in texts:
        text.set_fontsize(12)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
    
    plt.title("Sales Distribution by Product", fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    print("  Displayed pie chart with formatted labels")
    
    # DONUT CHART
    print("\n3. DONUT CHART (Pie with hole)")
    print("-" * 40)
    
    plt.figure(figsize=(8, 8))
    
    wedges, texts, autotexts = plt.pie(sales, labels=categories, colors=colors,
                                       autopct='%1.1f%%', startangle=90,
                                       pctdistance=0.85)
    
    # Create a circle for the donut hole
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    plt.title("Market Share (Donut Chart)", fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    print("  Displayed donut chart")


def demonstrate_area_plots():
    """
    Demonstrates area plots for cumulative data over time.
    
    Area plots show how components contribute to a total over time.
    """
    print("\n" + "=" * 60)
    print("SECTION 3B: AREA PLOTS")
    print("=" * 60)
    
    # Create time series data
    dates = pd.date_range('2024-01-01', periods=12, freq='M')
    product_a = np.array([10, 12, 15, 18, 22, 25, 28, 30, 32, 35, 38, 40])
    product_b = np.array([5, 7, 10, 12, 15, 18, 20, 22, 25, 27, 30, 32])
    product_c = np.array([2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])
    
    # BASIC AREA PLOT
    print("\n1. BASIC AREA PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(12, 6))
    plt.fill_between(dates, product_a, alpha=0.5, label='Product A', color='steelblue')
    plt.fill_between(dates, product_b, alpha=0.5, label='Product B', color='coral')
    plt.fill_between(dates, product_c, alpha=0.5, label='Product C', color='seagreen')
    plt.title("Monthly Sales by Product (Overlapping)")
    plt.xlabel("Month")
    plt.ylabel("Sales (units)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("  Displayed overlapping area plot")
    
    # STACKED AREA PLOT
    print("\n2. STACKED AREA PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(12, 6))
    plt.stackplot(dates, product_a, product_b, product_c, 
                  labels=['Product A', 'Product B', 'Product C'],
                  colors=['steelblue', 'coral', 'seagreen'], alpha=0.7)
    plt.title("Monthly Sales by Product (Stacked)")
    plt.xlabel("Month")
    plt.ylabel("Total Sales (units)")
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("  Displayed stacked area plot")
    
    # FILL BETWEEN WITH CONDITION
    print("\n3. FILL BETWEEN (Highlighting Regions)")
    print("-" * 40)
    
    x = np.linspace(0, 10, 200)
    y = np.sin(x)
    
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    
    # Fill where sin(x) > 0
    plt.fill_between(x, y, 0, where=(y > 0), color='green', alpha=0.3, label='Positive')
    
    # Fill where sin(x) < 0
    plt.fill_between(x, y, 0, where=(y < 0), color='red', alpha=0.3, label='Negative')
    
    plt.title("Sine Wave with Highlighted Regions")
    plt.xlabel("X")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    plt.tight_layout()
    plt.show()
    print("  Displayed conditional fill between")


def demonstrate_box_plots():
    """
    Demonstrates box plots for statistical distributions.
    
    Box plots show median, quartiles, outliers, and distribution spread.
    """
    print("\n" + "=" * 60)
    print("SECTION 3C: BOX PLOTS")
    print("=" * 60)
    
    # Generate data for multiple groups
    np.random.seed(42)
    data_group_a = np.random.normal(50, 10, 100)
    data_group_b = np.random.normal(60, 15, 100)
    data_group_c = np.random.normal(55, 8, 100)
    data_group_d = np.random.normal(45, 12, 100)
    
    # BASIC BOX PLOT
    print("\n1. BASIC BOX PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.boxplot([data_group_a, data_group_b, data_group_c, data_group_d],
                labels=['Group A', 'Group B', 'Group C', 'Group D'])
    plt.title("Distribution Comparison - Box Plot")
    plt.ylabel("Values")
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed basic box plot")
    
    # HORIZONTAL BOX PLOT
    print("\n2. HORIZONTAL BOX PLOT")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    bp = plt.boxplot([data_group_a, data_group_b, data_group_c, data_group_d],
                     labels=['Group A', 'Group B', 'Group C', 'Group D'],
                     vert=False, patch_artist=True)
    
    # Customize colors
    colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightyellow']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    plt.title("Distribution Comparison - Horizontal Box Plot")
    plt.xlabel("Values")
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.show()
    print("  Displayed horizontal box plot")
    
    # BOX PLOT WITH NOTCH (confidence interval)
    print("\n3. BOX PLOT WITH NOTCH")
    print("-" * 40)
    
    plt.figure(figsize=(10, 6))
    plt.boxplot([data_group_a, data_group_b, data_group_c, data_group_d],
                labels=['Group A', 'Group B', 'Group C', 'Group D'],
                notch=True, patch_artist=True)
    plt.title("Box Plot with Notch (95% Confidence Interval)")
    plt.ylabel("Values")
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
    print("  Displayed box plot with notch")
    
    # VIOLIN PLOT (Enhanced box plot)
    print("\n4. VIOLIN PLOT (Kernel Density + Box Plot)")
    print("-" * 40)
    
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Box plot
    ax1.boxplot([data_group_a, data_group_b, data_group_c, data_group_d],
                labels=['A', 'B', 'C', 'D'])
    ax1.set_title("Box Plot")
    ax1.set_ylabel("Values")
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Violin plot
    parts = ax2.violinplot([data_group_a, data_group_b, data_group_c, data_group_d],
                           positions=[1, 2, 3, 4], showmeans=True, showmedians=True)
    ax2.set_xticks([1, 2, 3, 4])
    ax2.set_xticklabels(['A', 'B', 'C', 'D'])
    ax2.set_title("Violin Plot (Shows Distribution Shape)")
    ax2.set_ylabel("Values")
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()
    print("  Displayed violin plot comparison")
    
    # REAL-WORLD: SALARY DISTRIBUTION BY DEPARTMENT
    print("\n5. REAL-WORLD: SALARY ANALYSIS")
    print("-" * 40)
    
    # Generate salary data by department
    departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Operations']
    salaries = {
        'Engineering': np.random.normal(95000, 15000, 50),
        'Sales': np.random.normal(85000, 20000, 50),
        'Marketing': np.random.normal(75000, 12000, 50),
        'HR': np.random.normal(65000, 10000, 50),
        'Operations': np.random.normal(80000, 14000, 50)
    }
    
    data_to_plot = [salaries[dept] for dept in departments]
    
    plt.figure(figsize=(12, 6))
    bp = plt.boxplot(data_to_plot, labels=departments, patch_artist=True,
                     notch=True, widths=0.6)
    
    # Color by department
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    plt.title("Salary Distribution by Department", fontsize=14, fontweight='bold')
    plt.ylabel("Annual Salary ($)")
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add horizontal line for company average
    company_avg = np.mean([np.mean(s) for s in data_to_plot])
    plt.axhline(y=company_avg, color='red', linestyle='--', linewidth=2, 
                label=f'Company Avg: ${company_avg:,.0f}')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    print("  Displayed salary distribution box plot")


if __name__ == "__main__":
    demonstrate_pie_charts()
    demonstrate_area_plots()
    demonstrate_box_plots()
```

---

## 📈 Section 4: Subplots and Multi-Panel Figures

Creating multiple plots in a single figure for comprehensive analysis.

**SOLID Principle Applied: Single Responsibility** – Each subplot displays one aspect of the data.

**Design Pattern: Composite Pattern** – Figure contains multiple subplots as components.

```python
"""
SUBPLOTS AND MULTI-PANEL FIGURES

This section covers creating multiple plots in a single figure.

SOLID Principle: Single Responsibility
- Each subplot displays one aspect of the data

Design Pattern: Composite Pattern
- Figure contains multiple subplots as components
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demonstrate_subplot_basics():
    """
    Demonstrates creating subplots using plt.subplot().
    
    Subplots allow multiple visualizations in one figure.
    """
    print("=" * 60)
    print("SECTION 4A: SUBPLOT BASICS")
    print("=" * 60)
    
    # Create data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.exp(-x/5)
    
    # METHOD 1: plt.subplot()
    print("\n1. USING plt.subplot()")
    print("-" * 40)
    
    plt.figure(figsize=(12, 8))
    
    # Subplot 1 (2 rows, 2 columns, position 1)
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, 'b-')
    plt.title('Sine Wave')
    plt.grid(True, alpha=0.3)
    
    # Subplot 2 (2,2,2)
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, 'r-')
    plt.title('Cosine Wave')
    plt.grid(True, alpha=0.3)
    
    # Subplot 3 (2,2,3)
    plt.subplot(2, 2, 3)
    plt.plot(x, y3, 'g-')
    plt.ylim(-5, 5)
    plt.title('Tangent')
    plt.grid(True, alpha=0.3)
    
    # Subplot 4 (2,2,4)
    plt.subplot(2, 2, 4)
    plt.plot(x, y4, 'm-')
    plt.title('Exponential Decay')
    plt.grid(True, alpha=0.3)
    
    plt.suptitle('Trigonometric Functions', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed 2x2 subplot grid")
    
    # METHOD 2: plt.subplots()
    print("\n2. USING plt.subplots()")
    print("-" * 40)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    axes[0, 0].plot(x, y1, 'b-')
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].grid(True, alpha=0.3)
    
    axes[0, 1].plot(x, y2, 'r-')
    axes[0, 1].set_title('Cosine Wave')
    axes[0, 1].grid(True, alpha=0.3)
    
    axes[1, 0].plot(x, y3, 'g-')
    axes[1, 0].set_ylim(-5, 5)
    axes[1, 0].set_title('Tangent')
    axes[1, 0].grid(True, alpha=0.3)
    
    axes[1, 1].plot(x, y4, 'm-')
    axes[1, 1].set_title('Exponential Decay')
    axes[1, 1].grid(True, alpha=0.3)
    
    fig.suptitle('Trigonometric Functions', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed 2x2 subplot grid using subplots()")


def demonstrate_uneven_subplots():
    """
    Demonstrates creating subplots with different sizes.
    
    GridSpec allows complex layouts with different subplot dimensions.
    """
    print("\n" + "=" * 60)
    print("SECTION 4B: UNEVEN SUBPLOTS")
    print("=" * 60)
    
    from matplotlib.gridspec import GridSpec
    
    # Create data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    # GRIDSPEC FOR COMPLEX LAYOUTS
    print("\n1. COMPLEX LAYOUT WITH GridSpec")
    print("-" * 40)
    
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(3, 3, figure=fig)
    
    # Large plot (spanning first two rows, first two columns)
    ax1 = fig.add_subplot(gs[0:2, 0:2])
    ax1.plot(x, y1, 'b-', linewidth=2)
    ax1.set_title('Main Signal', fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Top-right plot
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.plot(x, y2, 'r-')
    ax2.set_title('Reference')
    ax2.grid(True, alpha=0.3)
    
    # Bottom-right plot
    ax3 = fig.add_subplot(gs[1, 2])
    ax3.plot(x, y3, 'g-')
    ax3.set_title('Product')
    ax3.grid(True, alpha=0.3)
    
    # Bottom row, full width
    ax4 = fig.add_subplot(gs[2, :])
    ax4.plot(x, np.abs(y1), 'm-')
    ax4.set_title('Absolute Value')
    ax4.grid(True, alpha=0.3)
    
    fig.suptitle('Complex Layout with GridSpec', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed complex layout with uneven subplots")
    
    # DASHBOARD LAYOUT
    print("\n2. DASHBOARD-STYLE LAYOUT")
    print("-" * 40)
    
    # Generate financial data
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    prices = 100 + np.cumsum(np.random.randn(100) * 2)
    volume = np.random.randint(1000, 5000, 100)
    returns = np.diff(prices) / prices[:-1] * 100
    returns = np.append([0], returns)
    
    fig = plt.figure(figsize=(14, 10))
    gs = GridSpec(3, 2, figure=fig, height_ratios=[2, 1, 1])
    
    # Price chart (top, spanning both columns)
    ax_price = fig.add_subplot(gs[0, :])
    ax_price.plot(dates, prices, 'b-', linewidth=2)
    ax_price.set_title('Stock Price', fontsize=14, fontweight='bold')
    ax_price.set_ylabel('Price ($)')
    ax_price.grid(True, alpha=0.3)
    ax_price.axhline(y=prices.mean(), color='r', linestyle='--', alpha=0.5)
    
    # Volume chart (middle left)
    ax_volume = fig.add_subplot(gs[1, 0])
    ax_volume.bar(dates, volume, width=0.8, color='steelblue', alpha=0.7)
    ax_volume.set_title('Trading Volume')
    ax_volume.set_ylabel('Volume')
    ax_volume.grid(True, alpha=0.3, axis='y')
    
    # Returns histogram (middle right)
    ax_returns = fig.add_subplot(gs[1, 1])
    ax_returns.hist(returns, bins=30, color='coral', edgecolor='black', alpha=0.7)
    ax_returns.set_title('Returns Distribution')
    ax_returns.set_xlabel('Return (%)')
    ax_returns.set_ylabel('Frequency')
    ax_returns.axvline(x=0, color='red', linestyle='--')
    ax_returns.grid(True, alpha=0.3, axis='y')
    
    # Summary statistics (bottom, spanning both columns)
    ax_stats = fig.add_subplot(gs[2, :])
    ax_stats.axis('off')
    
    stats_text = f"""
    Summary Statistics:
    Start Price: ${prices[0]:.2f}
    End Price: ${prices[-1]:.2f}
    Total Return: {(prices[-1]/prices[0]-1)*100:.1f}%
    Max Price: ${np.max(prices):.2f}
    Min Price: ${np.min(prices):.2f}
    Avg Daily Return: {np.mean(returns):.2f}%
    Volatility: {np.std(returns):.2f}%
    """
    
    ax_stats.text(0.1, 0.5, stats_text, fontsize=12, verticalalignment='center',
                 fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='lightyellow'))
    
    fig.suptitle('Financial Dashboard', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed financial dashboard with complex layout")


def build_sales_dashboard():
    """
    Builds a complete sales dashboard with multiple plots.
    
    Design Pattern: Composite Pattern - Multiple visualizations in one dashboard.
    """
    print("\n" + "=" * 60)
    print("SECTION 4C: SALES DASHBOARD")
    print("=" * 60)
    
    # Generate sales data
    np.random.seed(42)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Sales by product category
    electronics = np.random.randint(100, 200, 12)
    clothing = np.random.randint(80, 150, 12)
    books = np.random.randint(50, 100, 12)
    home = np.random.randint(60, 120, 12)
    
    # Regional sales
    regions = ['North', 'South', 'East', 'West']
    regional_sales = np.random.randint(500, 1500, 4)
    
    # Customer satisfaction by month
    satisfaction = np.random.uniform(3.5, 4.8, 12)
    
    # Create dashboard
    fig = plt.figure(figsize=(16, 10))
    
    # 1. Monthly Sales by Category (Stacked Area)
    ax1 = plt.subplot(2, 2, 1)
    ax1.stackplot(months, electronics, clothing, books, home,
                  labels=['Electronics', 'Clothing', 'Books', 'Home'],
                  colors=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'], alpha=0.7)
    ax1.set_title('Monthly Sales by Category', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Sales ($K)')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(range(12))
    ax1.set_xticklabels(months, rotation=45)
    
    # 2. Regional Sales (Horizontal Bar Chart)
    ax2 = plt.subplot(2, 2, 2)
    bars = ax2.barh(regions, regional_sales, color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
    ax2.set_title('Sales by Region', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Sales ($K)')
    
    # Add value labels
    for bar, value in zip(bars, regional_sales):
        ax2.text(value + 10, bar.get_y() + bar.get_height()/2, f'${value}K', 
                va='center', fontsize=10)
    ax2.grid(True, alpha=0.3, axis='x')
    
    # 3. Product Performance (Pie Chart)
    ax3 = plt.subplot(2, 2, 3)
    total_sales = [np.sum(electronics), np.sum(clothing), np.sum(books), np.sum(home)]
    categories = ['Electronics', 'Clothing', 'Books', 'Home']
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    explode = (0.05, 0, 0, 0)
    
    wedges, texts, autotexts = ax3.pie(total_sales, labels=categories, colors=colors,
                                       autopct='%1.1f%%', startangle=90, explode=explode)
    ax3.set_title('Total Sales by Category', fontsize=12, fontweight='bold')
    
    # 4. Customer Satisfaction Trend (Line Chart)
    ax4 = plt.subplot(2, 2, 4)
    ax4.plot(months, satisfaction, 'o-', color='#9b59b6', linewidth=2, markersize=6)
    ax4.set_title('Customer Satisfaction Trend', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Month')
    ax4.set_ylabel('Rating (1-5)')
    ax4.set_ylim(3, 5)
    ax4.grid(True, alpha=0.3)
    ax4.axhline(y=4.0, color='green', linestyle='--', alpha=0.5, label='Target')
    ax4.legend()
    ax4.set_xticks(range(12))
    ax4.set_xticklabels(months, rotation=45)
    
    # Add horizontal target line
    ax4.axhline(y=4.0, color='green', linestyle='--', alpha=0.5)
    
    # Main title
    fig.suptitle('Sales Performance Dashboard', fontsize=18, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.show()
    print("  Displayed complete sales dashboard")


if __name__ == "__main__":
    demonstrate_subplot_basics()
    demonstrate_uneven_subplots()
    build_sales_dashboard()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Line Plots** – `plt.plot(x, y)` for trends over time. Multiple lines, custom colors, markers, line styles.

- **Bar Charts** – `plt.bar()` for comparisons. Vertical, horizontal, grouped, stacked. Add value labels.

- **Scatter Plots** – `plt.scatter()` for relationships. Size and color encoding. Trend lines with `np.polyfit()`.

- **Histograms** – `plt.hist()` for distributions. Bins, statistics overlay, multiple groups.

- **Pie Charts** – `plt.pie()` for proportions. Use sparingly. Donut charts, custom labels, explode.

- **Area Plots** – `plt.fill_between()` and `plt.stackplot()` for cumulative data. Conditional highlighting.

- **Box Plots** – `plt.boxplot()` for statistical distributions. Median, quartiles, outliers. Violin plots for distribution shape.

- **Subplots** – `plt.subplot()` and `plt.subplots()` for multiple plots. GridSpec for complex layouts.

- **Customization** – Colors (named, hex, RGB), colormaps, line styles, markers, annotations, shapes, legends.

- **Real-World Applications** – Stock price trends, marketing ROI, salary distributions, sales dashboards, financial dashboards.

- **SOLID Principles Applied** – Single Responsibility (each plot type has one purpose), Open/Closed (customizations add without changing core), Dependency Inversion (plots depend on data abstractions), Interface Segregation (clean plotting interfaces).

- **Design Patterns Used** – Facade Pattern (pyplot interface), Decorator Pattern (style customizations), Composite Pattern (multi-panel figures), Strategy Pattern (different plot types).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Pandas – Data Wrangling

- **📚 Series G Catalog:** Data Science & Visualization – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Seaborn – Statistical Visualization (Series G, Story 4)

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
| Series G | 5 | 3 | 2 | 60% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **43** | **9** | **83%** |

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

**Next Story:** Series G, Story 4: The 2026 Python Metromap: Seaborn – Statistical Visualization

---

## 📝 Your Invitation

You've mastered Matplotlib. Now build something with what you've learned:

1. **Build a portfolio dashboard** – Create a multi-panel dashboard showing stock prices, volume, returns, and moving averages.

2. **Create a sales report generator** – Generate automated sales reports with bar charts, line charts, and pie charts from CSV data.

3. **Build a data explorer** – Create interactive plots that update based on user input (using matplotlib widgets).

4. **Create a statistical summary plot** – Combine box plots, histograms, and Q-Q plots for distribution analysis.

5. **Build a real-time monitoring dashboard** – Create plots that update with streaming data.

**You've mastered Matplotlib. Next stop: Seaborn!**

---

*Found this helpful? Clap, comment, and share what you visualized. Next stop: Seaborn!* 🚇