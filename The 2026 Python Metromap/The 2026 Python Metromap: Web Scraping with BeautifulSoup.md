# The 2026 Python Metromap: Web Scraping with BeautifulSoup

## Series H: Web Development & Automation | Story 4 of 5

![The 2026 Python Metromap/images/Web Scraping with BeautifulSoup](images/Web Scraping with BeautifulSoup.png)

## 📖 Introduction

**Welcome to the fourth stop on the Web Development & Automation Line.**

You've mastered system automation—organizing files, monitoring resources, and creating backups. But what about data that exists only on the web? Product prices, news articles, stock data, job listings—all hidden behind websites. To extract this data, you need web scraping.

Web scraping is the process of automatically extracting information from websites. BeautifulSoup is Python's most popular library for parsing HTML and XML documents. Combined with the Requests library for fetching web pages, you can build powerful scrapers that extract, clean, and save data from almost any website.

This story—**The 2026 Python Metromap: Web Scraping with BeautifulSoup**—is your guide to ethical web scraping. We'll build a price monitoring bot that tracks products across multiple e-commerce sites and alerts on price drops. We'll create a news aggregator that extracts headlines and articles. We'll build a job scraper that finds positions matching your criteria. We'll implement a real estate listing scraper. And we'll learn how to respect robots.txt, handle rate limiting, and scrape responsibly.

**Let's scrape the web.**

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

### Series H: Web Development & Automation (5 Stories)

- 🌶️ **The 2026 Python Metromap: Flask – Building Web APIs** – URL shortener service; REST endpoints; database storage; redirect logic.

- 🎸 **The 2026 Python Metromap: Django – Full-Stack Web Apps** – Blog platform; user authentication; admin panel; comments system; search functionality.

- 🤖 **The 2026 Python Metromap: Automation with os and sys** – File organizer script; type-based sorting; file renaming; temp directory cleaning.

- 🕸️ **The 2026 Python Metromap: Web Scraping with BeautifulSoup** – Price monitoring bot; multi-site product tracking; price drop alerts. **⬅️ YOU ARE HERE**

- ⏰ **The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler** – Daily report emailer; weekly backup system; cron-style job scheduler. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🕸️ Section 1: BeautifulSoup Basics – Parsing HTML

BeautifulSoup parses HTML and XML documents, providing Pythonic ways to navigate, search, and modify the parse tree.

**SOLID Principle Applied: Single Responsibility** – BeautifulSoup handles parsing; Requests handles fetching.

**Design Pattern: Adapter Pattern** – BeautifulSoup adapts HTML to a navigable Python object.

```python
"""
BEAUTIFULSOUP BASICS: PARSING HTML

This section covers the fundamentals of web scraping with BeautifulSoup.

SOLID Principle: Single Responsibility
- BeautifulSoup handles parsing; Requests handles fetching

Design Pattern: Adapter Pattern
- BeautifulSoup adapts HTML to a navigable Python object
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict, Optional
import time


def demonstrate_requests_and_soup():
    """
    Demonstrates fetching web pages and parsing with BeautifulSoup.
    
    Note: Using example.com for demonstration (safe, always available).
    """
    print("=" * 60)
    print("SECTION 1A: REQUESTS AND BEAUTIFULSOUP")
    print("=" * 60)
    
    # FETCHING A WEB PAGE
    print("\n1. FETCHING A WEB PAGE")
    print("-" * 40)
    
    url = "https://example.com"
    print(f"  Fetching: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"  Status code: {response.status_code}")
        print(f"  Content length: {len(response.text)} characters")
    except requests.RequestException as e:
        print(f"  Error: {e}")
        return
    
    # PARSING WITH BEAUTIFULSOUP
    print("\n2. PARSING HTML WITH BEAUTIFULSOUP")
    print("-" * 40)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"  Title: {soup.title.string}")
    print(f"  Title tag: {soup.title}")
    print(f"  First paragraph: {soup.p.string if soup.p else 'None'}")
    
    # FINDING ELEMENTS
    print("\n3. FINDING ELEMENTS")
    print("-" * 40)
    
    # Find by tag name
    headings = soup.find_all('h1')
    print(f"  H1 tags: {len(headings)}")
    
    # Find by class
    # Note: example.com may not have classes, this is illustrative
    elements = soup.find_all(class_="some-class")
    print(f"  Elements with class 'some-class': {len(elements)}")
    
    # Find by id
    element = soup.find(id="some-id")
    print(f"  Element with id 'some-id': {element}")
    
    # Find by attribute
    links = soup.find_all('a')
    print(f"  Links found: {len(links)}")
    for link in links[:3]:
        print(f"    {link.get('href')} - {link.string}")


def demonstrate_finding_methods():
    """
    Demonstrates various BeautifulSoup finding methods.
    
    Methods: find(), find_all(), select(), find_parent(), find_next()
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: FINDING METHODS")
    print("=" * 60)
    
    # Sample HTML for demonstration
    html = """
    <html>
        <body>
            <div class="container">
                <h1>Main Title</h1>
                <p class="description">This is a description paragraph.</p>
                <div class="content">
                    <h2>Section 1</h2>
                    <p>First paragraph in section 1.</p>
                    <p>Second paragraph in section 1.</p>
                </div>
                <div class="content">
                    <h2>Section 2</h2>
                    <p>First paragraph in section 2.</p>
                    <ul>
                        <li>Item 1</li>
                        <li>Item 2</li>
                        <li>Item 3</li>
                    </ul>
                </div>
                <div id="footer">
                    <p>&copy; 2024 Example Site</p>
                    <a href="/privacy">Privacy Policy</a>
                    <a href="/terms">Terms of Service</a>
                </div>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # FIND_ALL - Get all matching elements
    print("\n1. find_all() - Get all matching elements")
    print("-" * 40)
    
    all_paragraphs = soup.find_all('p')
    print(f"  All paragraphs: {len(all_paragraphs)}")
    for p in all_paragraphs:
        print(f"    {p.string}")
    
    # FIND - Get first matching element
    print("\n2. find() - Get first matching element")
    print("-" * 40)
    
    first_h2 = soup.find('h2')
    print(f"  First H2: {first_h2.string}")
    
    # FIND_BY_CLASS
    print("\n3. find by class")
    print("-" * 40)
    
    content_divs = soup.find_all(class_="content")
    print(f"  Content divs: {len(content_divs)}")
    
    # FIND_BY_ID
    print("\n4. find by id")
    print("-" * 40)
    
    footer = soup.find(id="footer")
    print(f"  Footer found: {footer is not None}")
    
    # CSS SELECTORS (select method)
    print("\n5. CSS SELECTORS (select method)")
    print("-" * 40)
    
    # Select by class
    items = soup.select('.content')
    print(f"  '.content' selector: {len(items)} elements")
    
    # Select by id
    footer = soup.select('#footer')
    print(f"  '#footer' selector: {len(footer)} elements")
    
    # Select nested elements
    paragraphs_in_content = soup.select('.content p')
    print(f"  '.content p' selector: {len(paragraphs_in_content)} elements")
    
    # Select list items
    list_items = soup.select('ul li')
    print(f"  'ul li' selector: {len(list_items)} items")
    for li in list_items:
        print(f"    {li.string}")
    
    # FIND_PARENT - Navigate up
    print("\n6. find_parent() - Navigate up the tree")
    print("-" * 40)
    
    first_li = soup.find('li')
    parent_ul = first_li.find_parent('ul')
    print(f"  LI's parent UL: {parent_ul is not None}")
    
    # FIND_NEXT_SIBLING - Navigate sideways
    print("\n7. find_next_sibling() - Navigate sideways")
    print("-" * 40)
    
    first_p = soup.find('p')
    second_p = first_p.find_next_sibling('p')
    if second_p:
        print(f"  Next sibling paragraph: {second_p.string}")
    
    # FIND_ALL_TEXT - Get all text
    print("\n8. get_text() - Extract text")
    print("-" * 40)
    
    text = soup.get_text()
    print(f"  Full text length: {len(text)} characters")
    print(f"  Preview: {text[:200]}...")


def demonstrate_navigation():
    """
    Demonstrates navigating the parse tree.
    
    Navigation properties: .parent, .parents, .children, .contents, .next_sibling
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: NAVIGATING THE PARSE TREE")
    print("=" * 60)
    
    html = """
    <div class="article">
        <h1>Article Title</h1>
        <div class="meta">
            <span class="author">John Doe</span>
            <span class="date">2024-01-15</span>
        </div>
        <div class="content">
            <p>First paragraph of the article.</p>
            <p>Second paragraph with <strong>bold text</strong>.</p>
            <p>Third paragraph.</p>
        </div>
        <div class="comments">
            <div class="comment">
                <span class="comment-author">Alice</span>
                <p>Great article!</p>
            </div>
            <div class="comment">
                <span class="comment-author">Bob</span>
                <p>Very informative.</p>
            </div>
        </div>
    </div>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # .parent - Get parent element
    print("\n1. .parent - Get parent element")
    print("-" * 40)
    
    author_span = soup.find(class_="author")
    parent = author_span.parent
    print(f"  Author's parent: {parent.name}")
    
    # .parents - Get all ancestors
    print("\n2. .parents - Get all ancestors")
    print("-" * 40)
    
    print("  Author's ancestors:")
    for ancestor in author_span.parents:
        print(f"    {ancestor.name}")
        if ancestor.name == 'html':
            break
    
    # .children - Get direct children
    print("\n3. .children - Get direct children")
    print("-" * 40)
    
    article = soup.find(class_="article")
    print("  Article's direct children:")
    for child in article.children:
        if child.name:
            print(f"    {child.name}")
    
    # .contents - Get children as list
    print("\n4. .contents - Get children as list")
    print("-" * 40)
    
    comments_div = soup.find(class_="comments")
    print(f"  Comments count: {len(list(comments_div.children))}")
    
    # .next_sibling / .previous_sibling
    print("\n5. .next_sibling / .previous_sibling")
    print("-" * 40)
    
    first_p = soup.find('p')
    second_p = first_p.find_next_sibling('p')
    print(f"  First P: {first_p.string[:30]}...")
    print(f"  Next P: {second_p.string[:30]}...")


def demonstrate_attribute_access():
    """
    Demonstrates accessing and manipulating attributes.
    
    Access attributes like dictionary keys or with .attrs.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: ATTRIBUTE ACCESS")
    print("=" * 60)
    
    html = """
    <div class="container main-content" id="main" data-id="123">
        <a href="https://example.com/page1" class="link external">Link 1</a>
        <a href="https://example.com/page2" class="link">Link 2</a>
        <img src="image.jpg" alt="Sample image" width="300" height="200">
    </div>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div')
    
    # GET ATTRIBUTES
    print("\n1. GETTING ATTRIBUTES")
    print("-" * 40)
    
    # As dictionary
    print(f"  All attributes: {div.attrs}")
    
    # By key
    print(f"  class attribute: {div.get('class')}")
    print(f"  id attribute: {div.get('id')}")
    print(f"  data-id attribute: {div.get('data-id')}")
    
    # Using bracket notation
    print(f"  class with []: {div['class']}")
    
    # CHECK ATTRIBUTE EXISTENCE
    print("\n2. CHECKING ATTRIBUTE EXISTENCE")
    print("-" * 40)
    
    print(f"  Has 'class': {'class' in div.attrs}")
    print(f"  Has 'data-value': {'data-value' in div.attrs}")
    
    # GET LINKS
    print("\n3. EXTRACTING LINKS")
    print("-" * 40)
    
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.string
        print(f"  {text}: {href}")
    
    # GET IMAGE INFO
    print("\n4. EXTRACTING IMAGE INFO")
    print("-" * 40)
    
    img = soup.find('img')
    print(f"  Src: {img.get('src')}")
    print(f"  Alt: {img.get('alt')}")
    print(f"  Width: {img.get('width')}")
    print(f"  Height: {img.get('height')}")


def demonstrate_working_with_sample_page():
    """
    Demonstrates scraping a real (simulated) product page.
    
    This creates a mock HTML page and scrapes product information.
    """
    print("\n" + "=" * 60)
    print("SECTION 1E: SCRAPING A PRODUCT PAGE")
    print("=" * 60)
    
    # Simulated product page HTML
    product_html = """
    <html>
    <head><title>Product Page - Awesome Widget</title></head>
    <body>
        <div class="product">
            <h1 class="product-title">Awesome Widget Pro</h1>
            <div class="product-price">
                <span class="current-price">$99.99</span>
                <span class="original-price">$149.99</span>
                <span class="discount">33% off</span>
            </div>
            <div class="product-rating">
                <span class="rating-value">4.5</span>
                <span class="rating-count">(127 reviews)</span>
            </div>
            <div class="product-availability">
                <span class="in-stock">In Stock</span>
            </div>
            <div class="product-description">
                <p>The Awesome Widget Pro is the latest and greatest widget on the market.</p>
                <p>Features include:</p>
                <ul>
                    <li>High performance</li>
                    <li>Long battery life</li>
                    <li>Easy to use</li>
                </ul>
            </div>
            <div class="product-specs">
                <table>
                    <tr><td>Weight</td><td>1.2 lbs</td></tr>
                    <tr><td>Dimensions</td><td>10 x 5 x 2 inches</td></tr>
                    <tr><td>Color</td><td>Black</td></tr>
                </table>
            </div>
            <div class="related-products">
                <div class="related-item">
                    <h3>Widget Basic</h3>
                    <span class="price">$49.99</span>
                </div>
                <div class="related-item">
                    <h3>Widget Deluxe</h3>
                    <span class="price">$199.99</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    soup = BeautifulSoup(product_html, 'html.parser')
    
    # Extract product information
    print("\n1. EXTRACTING PRODUCT INFORMATION")
    print("-" * 40)
    
    # Title
    title = soup.find('h1', class_='product-title')
    print(f"  Title: {title.string if title else 'N/A'}")
    
    # Price
    current_price = soup.find('span', class_='current-price')
    original_price = soup.find('span', class_='original-price')
    discount = soup.find('span', class_='discount')
    
    print(f"  Current Price: {current_price.string if current_price else 'N/A'}")
    print(f"  Original Price: {original_price.string if original_price else 'N/A'}")
    print(f"  Discount: {discount.string if discount else 'N/A'}")
    
    # Rating
    rating = soup.find('span', class_='rating-value')
    rating_count = soup.find('span', class_='rating-count')
    print(f"  Rating: {rating.string if rating else 'N/A'} {rating_count.string if rating_count else ''}")
    
    # Availability
    availability = soup.find('span', class_='in-stock')
    print(f"  Availability: {availability.string if availability else 'N/A'}")
    
    # Description (first paragraph)
    description = soup.select('.product-description p')
    if description:
        print(f"  Description: {description[0].string[:60]}...")
    
    # Specifications
    print("\n2. EXTRACTING SPECIFICATIONS")
    print("-" * 40)
    
    specs = {}
    table_rows = soup.select('.product-specs table tr')
    for row in table_rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            specs[cells[0].string] = cells[1].string
    
    for key, value in specs.items():
        print(f"  {key}: {value}")
    
    # Related products
    print("\n3. EXTRACTING RELATED PRODUCTS")
    print("-" * 40)
    
    related = soup.select('.related-item')
    for item in related:
        name = item.find('h3')
        price = item.find('span', class_='price')
        print(f"  {name.string if name else 'N/A'}: {price.string if price else 'N/A'}")


if __name__ == "__main__":
    demonstrate_requests_and_soup()
    demonstrate_finding_methods()
    demonstrate_navigation()
    demonstrate_attribute_access()
    demonstrate_working_with_sample_page()
```

---

## 🏷️ Section 2: Price Monitoring Bot

A complete price monitoring bot that tracks products across multiple e-commerce sites and alerts on price drops.

**SOLID Principles Applied:**
- Single Responsibility: Each component handles one aspect (fetching, parsing, alerting)
- Open/Closed: New sites can be added without modifying core logic

**Design Patterns:**
- Strategy Pattern: Different parsing strategies for different sites
- Observer Pattern: Alert system for price changes

```python
"""
PRICE MONITORING BOT

This section builds a complete price monitoring bot.

SOLID Principles Applied:
- Single Responsibility: Each component handles one aspect
- Open/Closed: New sites can be added without modifying core logic

Design Patterns:
- Strategy Pattern: Different parsing strategies for different sites
- Observer Pattern: Alert system for price changes
"""

import re
import json
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


@dataclass
class Product:
    """Represents a product being monitored."""
    id: str
    name: str
    url: str
    target_price: float
    current_price: Optional[float] = None
    last_check: Optional[datetime] = None
    price_history: List[Dict] = field(default_factory=list)
    alert_threshold: float = 0.0  # Alert when price drops below this


@dataclass
class PriceAlert:
    """Price drop alert."""
    product_id: str
    product_name: str
    old_price: float
    new_price: float
    drop_percent: float
    url: str
    timestamp: datetime


class PriceParser(ABC):
    """
    Abstract base class for price parsers.
    
    Design Pattern: Strategy Pattern - Different parsing strategies
    """
    
    @abstractmethod
    def can_handle(self, url: str) -> bool:
        """Check if this parser can handle the URL."""
        pass
    
    @abstractmethod
    def parse_price(self, html: str) -> Optional[float]:
        """Extract price from HTML."""
        pass
    
    @abstractmethod
    def parse_product_name(self, html: str) -> Optional[str]:
        """Extract product name from HTML."""
        pass


class AmazonParser(PriceParser):
    """Parser for Amazon product pages."""
    
    def can_handle(self, url: str) -> bool:
        return 'amazon.com' in url.lower() or 'amazon.' in url.lower()
    
    def parse_price(self, html: str) -> Optional[float]:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Try multiple selectors that Amazon uses
        selectors = [
            '#priceblock_ourprice',
            '#priceblock_dealprice',
            '.a-price .a-offscreen',
            '.a-price-whole',
            '[data-a-price]'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text()
                # Extract numeric value
                match = re.search(r'[\d,]+\.?\d*', price_text)
                if match:
                    price_str = match.group().replace(',', '')
                    try:
                        return float(price_str)
                    except ValueError:
                        continue
        
        return None
    
    def parse_product_name(self, html: str) -> Optional[str]:
        soup = BeautifulSoup(html, 'html.parser')
        
        selectors = [
            '#productTitle',
            '.a-size-large',
            '.product-title-word-break'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text().strip()
        
        return None


class EbayParser(PriceParser):
    """Parser for eBay product pages."""
    
    def can_handle(self, url: str) -> bool:
        return 'ebay.com' in url.lower() or 'ebay.' in url.lower()
    
    def parse_price(self, html: str) -> Optional[float]:
        soup = BeautifulSoup(html, 'html.parser')
        
        selectors = [
            '#prcIsum',
            '.vi-price',
            '[itemprop="price"]',
            '.notranslate .display-price'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text()
                match = re.search(r'[\d,]+\.?\d*', price_text)
                if match:
                    price_str = match.group().replace(',', '')
                    try:
                        return float(price_str)
                    except ValueError:
                        continue
        
        return None
    
    def parse_product_name(self, html: str) -> Optional[str]:
        soup = BeautifulSoup(html, 'html.parser')
        
        selectors = [
            '#itemTitle',
            '.it-ttl',
            '[itemprop="name"]'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text().strip()
        
        return None


class GenericParser(PriceParser):
    """Generic parser that tries to find price in common patterns."""
    
    def can_handle(self, url: str) -> bool:
        return True  # Fallback for any URL
    
    def parse_price(self, html: str) -> Optional[float]:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Look for common price patterns
        price_patterns = [
            r'\$\s*([\d,]+\.?\d*)',  # $99.99
            r'([\d,]+\.?\d*)\s*USD',  # 99.99 USD
            r'price[:\s]*\$?([\d,]+\.?\d*)',  # price: $99.99
        ]
        
        # Search in text
        text = soup.get_text()
        for pattern in price_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                price_str = match.group(1).replace(',', '')
                try:
                    return float(price_str)
                except ValueError:
                    continue
        
        # Look for elements with price-related classes
        price_elements = soup.find_all(class_=re.compile(r'price|cost|amount', re.I))
        for elem in price_elements:
            text = elem.get_text()
            match = re.search(r'[\d,]+\.?\d*', text)
            if match:
                price_str = match.group().replace(',', '')
                try:
                    return float(price_str)
                except ValueError:
                    continue
        
        return None
    
    def parse_product_name(self, html: str) -> Optional[str]:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Try to get title
        title = soup.find('title')
        if title:
            return title.get_text().strip()
        
        # Try H1
        h1 = soup.find('h1')
        if h1:
            return h1.get_text().strip()
        
        return None


class PriceMonitor:
    """
    Monitors product prices and triggers alerts.
    
    Design Pattern: Observer Pattern - Alerts observers of price changes
    """
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.parsers: List[PriceParser] = [
            AmazonParser(),
            EbayParser(),
            GenericParser()
        ]
        self.alert_callbacks: List[Callable] = []
        self.check_interval = 3600  # 1 hour default
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    
    def add_product(self, product: Product) -> None:
        """Add a product to monitor."""
        self.products[product.id] = product
        print(f"  Added product: {product.name}")
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product from monitoring."""
        if product_id in self.products:
            del self.products[product_id]
            print(f"  Removed product: {product_id}")
            return True
        return False
    
    def add_alert_callback(self, callback: Callable) -> None:
        """Add a callback for price drop alerts."""
        self.alert_callbacks.append(callback)
    
    def _get_parser(self, url: str) -> Optional[PriceParser]:
        """Get the appropriate parser for a URL."""
        for parser in self.parsers:
            if parser.can_handle(url):
                return parser
        return None
    
    def _fetch_page(self, url: str) -> Optional[str]:
        """Fetch a web page."""
        headers = {
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None
    
    def check_product(self, product: Product) -> Optional[PriceAlert]:
        """Check a single product's price."""
        parser = self._get_parser(product.url)
        if not parser:
            print(f"  No parser found for {product.url}")
            return None
        
        html = self._fetch_page(product.url)
        if not html:
            return None
        
        # Parse price and name
        price = parser.parse_price(html)
        name = parser.parse_product_name(html)
        
        if name:
            product.name = name
        
        if price is None:
            print(f"  Could not parse price for {product.url}")
            return None
        
        old_price = product.current_price
        product.current_price = price
        product.last_check = datetime.now()
        
        # Record price history
        product.price_history.append({
            "price": price,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 100 entries
        if len(product.price_history) > 100:
            product.price_history = product.price_history[-100:]
        
        # Check for price drop
        if old_price is not None and price < old_price:
            drop_amount = old_price - price
            drop_percent = (drop_amount / old_price) * 100
            
            if drop_percent >= product.alert_threshold:
                alert = PriceAlert(
                    product_id=product.id,
                    product_name=product.name,
                    old_price=old_price,
                    new_price=price,
                    drop_percent=drop_percent,
                    url=product.url,
                    timestamp=datetime.now()
                )
                return alert
        
        return None
    
    def check_all_products(self) -> List[PriceAlert]:
        """Check all products and return alerts."""
        alerts = []
        
        for product in self.products.values():
            print(f"  Checking: {product.name}")
            alert = self.check_product(product)
            if alert:
                alerts.append(alert)
                for callback in self.alert_callbacks:
                    try:
                        callback(alert)
                    except Exception as e:
                        print(f"  Alert callback error: {e}")
            
            # Be respectful - delay between requests
            time.sleep(2)
        
        return alerts
    
    def get_product_status(self) -> List[Dict]:
        """Get status of all monitored products."""
        status = []
        for product in self.products.values():
            status.append({
                "id": product.id,
                "name": product.name,
                "current_price": product.current_price,
                "target_price": product.target_price,
                "last_check": product.last_check.isoformat() if product.last_check else None,
                "url": product.url,
                "price_history_count": len(product.price_history)
            })
        return status
    
    def save_state(self, filename: str) -> None:
        """Save monitor state to file."""
        state = {
            "products": [
                {
                    "id": p.id,
                    "name": p.name,
                    "url": p.url,
                    "target_price": p.target_price,
                    "current_price": p.current_price,
                    "alert_threshold": p.alert_threshold,
                    "price_history": p.price_history,
                    "last_check": p.last_check.isoformat() if p.last_check else None
                }
                for p in self.products.values()
            ]
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
        print(f"  Saved state to {filename}")
    
    def load_state(self, filename: str) -> None:
        """Load monitor state from file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            for product_data in state.get("products", []):
                product = Product(
                    id=product_data["id"],
                    name=product_data["name"],
                    url=product_data["url"],
                    target_price=product_data["target_price"],
                    current_price=product_data.get("current_price"),
                    alert_threshold=product_data.get("alert_threshold", 0),
                    price_history=product_data.get("price_history", [])
                )
                if product_data.get("last_check"):
                    product.last_check = datetime.fromisoformat(product_data["last_check"])
                self.products[product.id] = product
            
            print(f"  Loaded {len(self.products)} products from {filename}")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"  Could not load state: {e}")


class AlertNotifier:
    """Handles sending price drop alerts."""
    
    def __init__(self, email_config: Optional[Dict] = None):
        self.email_config = email_config
        self.alerts: List[PriceAlert] = []
    
    def console_alert(self, alert: PriceAlert) -> None:
        """Print alert to console."""
        print(f"\n  🔔 PRICE DROP ALERT!")
        print(f"  Product: {alert.product_name}")
        print(f"  Price dropped from ${alert.old_price:.2f} to ${alert.new_price:.2f}")
        print(f"  Drop: {alert.drop_percent:.1f}%")
        print(f"  URL: {alert.url}")
        self.alerts.append(alert)
    
    def email_alert(self, alert: PriceAlert) -> bool:
        """Send email alert (requires email config)."""
        if not self.email_config:
            return False
        
        subject = f"Price Drop Alert: {alert.product_name}"
        body = f"""
        Price Drop Alert!
        
        Product: {alert.product_name}
        Old Price: ${alert.old_price:.2f}
        New Price: ${alert.new_price:.2f}
        Drop: {alert.drop_percent:.1f}%
        
        View product: {alert.url}
        
        Time: {alert.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.email_config['from']
            msg['To'] = self.email_config['to']
            
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(self.email_config['username'], self.email_config['password'])
                server.send_message(msg)
            
            print(f"  Email alert sent to {self.email_config['to']}")
            return True
        except Exception as e:
            print(f"  Email error: {e}")
            return False
    
    def webhook_alert(self, alert: PriceAlert, webhook_url: str) -> bool:
        """Send alert to webhook (e.g., Discord, Slack)."""
        payload = {
            "content": f"🔔 **Price Drop Alert!**\n"
                       f"**Product:** {alert.product_name}\n"
                       f"**Price:** ${alert.old_price:.2f} → ${alert.new_price:.2f} ({alert.drop_percent:.1f}%)\n"
                       f"**Link:** {alert.url}"
        }
        
        try:
            response = requests.post(webhook_url, json=payload, timeout=10)
            response.raise_for_status()
            print(f"  Webhook alert sent")
            return True
        except Exception as e:
            print(f"  Webhook error: {e}")
            return False
    
    def get_recent_alerts(self, hours: int = 24) -> List[PriceAlert]:
        """Get alerts from the last N hours."""
        cutoff = datetime.now().timestamp() - (hours * 3600)
        return [a for a in self.alerts if a.timestamp.timestamp() > cutoff]


def demonstrate_price_monitor():
    """
    Demonstrate the price monitoring bot.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: PRICE MONITORING BOT")
    print("=" * 60)
    
    # Create monitor
    monitor = PriceMonitor()
    notifier = AlertNotifier()
    
    # Add alert callback
    monitor.add_alert_callback(notifier.console_alert)
    
    # Add products to monitor (using example URLs for demonstration)
    # In real usage, these would be actual product URLs
    products = [
        Product(
            id="prod_001",
            name="Example Product 1",
            url="https://example.com/product1",
            target_price=50.00,
            alert_threshold=10  # Alert on 10% drop
        ),
        Product(
            id="prod_002",
            name="Example Product 2",
            url="https://example.com/product2",
            target_price=100.00,
            alert_threshold=5  # Alert on 5% drop
        )
    ]
    
    print("\n1. ADDING PRODUCTS TO MONITOR")
    print("-" * 40)
    
    for product in products:
        monitor.add_product(product)
    
    print("\n2. CURRENT PRODUCT STATUS")
    print("-" * 40)
    
    status = monitor.get_product_status()
    for s in status:
        print(f"  {s['name']}: Target ${s['target_price']:.2f}")
    
    print("\n3. CHECKING PRODUCT PRICES")
    print("-" * 40)
    
    # Note: In a real scenario, this would fetch actual web pages
    # For demonstration, we'll simulate price checks
    print("  Simulating price checks...")
    
    # Simulate price updates (in real code, would fetch from web)
    for product in monitor.products.values():
        # Simulate price (for demo only)
        import random
        simulated_price = product.target_price * (0.85 + random.random() * 0.3)
        product.current_price = simulated_price
        product.last_check = datetime.now()
        product.price_history.append({
            "price": simulated_price,
            "timestamp": datetime.now().isoformat()
        })
        
        if simulated_price < product.target_price:
            drop_percent = (product.target_price - simulated_price) / product.target_price * 100
            if drop_percent >= product.alert_threshold:
                alert = PriceAlert(
                    product_id=product.id,
                    product_name=product.name,
                    old_price=product.target_price,
                    new_price=simulated_price,
                    drop_percent=drop_percent,
                    url=product.url,
                    timestamp=datetime.now()
                )
                notifier.console_alert(alert)
    
    print("\n4. PRICE HISTORY")
    print("-" * 40)
    
    for product in monitor.products.values():
        print(f"\n  {product.name}:")
        for entry in product.price_history[-3:]:
            print(f"    ${entry['price']:.2f} at {entry['timestamp'][:16]}")
    
    print("\n5. SAVING AND LOADING STATE")
    print("-" * 40)
    
    monitor.save_state("monitor_state.json")
    monitor.load_state("monitor_state.json")
    
    import os
    if os.path.exists("monitor_state.json"):
        os.remove("monitor_state.json")
    
    print("\n6. PRICE MONITORING BEST PRACTICES")
    print("-" * 40)
    
    best_practices = [
        "✓ Respect robots.txt (check before scraping)",
        "✓ Add delays between requests (1-5 seconds)",
        "✓ Use caching to avoid repeated requests",
        "✓ Handle rate limiting gracefully",
        "✓ Set a proper User-Agent header",
        "✓ Monitor only when necessary, not continuously",
        "✓ Handle errors and retry with backoff",
        "✓ Store results to avoid data loss"
    ]
    
    for practice in best_practices:
        print(f"  {practice}")


if __name__ == "__main__":
    demonstrate_price_monitor()
```

---

## 📰 Section 3: News Aggregator and Job Scraper

A news aggregator that extracts headlines and articles, and a job scraper that finds positions matching criteria.

**SOLID Principles Applied:**
- Single Responsibility: Each scraper handles one source
- Open/Closed: New sources can be added

**Design Patterns:**
- Strategy Pattern: Different scraping strategies
- Factory Pattern: Creates appropriate scraper

```python
"""
NEWS AGGREGATOR AND JOB SCRAPER

This section builds scrapers for news and job listings.

SOLID Principles Applied:
- Single Responsibility: Each scraper handles one source
- Open/Closed: New sources can be added

Design Patterns:
- Strategy Pattern: Different scraping strategies
- Factory Pattern: Creates appropriate scraper
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import time
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class NewsArticle:
    """Represents a news article."""
    title: str
    url: str
    source: str
    published_date: Optional[datetime] = None
    summary: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    scraped_at: datetime = field(default_factory=datetime.now)


@dataclass
class JobListing:
    """Represents a job listing."""
    title: str
    company: str
    location: str
    url: str
    source: str
    salary: Optional[str] = None
    description: Optional[str] = None
    posted_date: Optional[datetime] = None
    job_type: Optional[str] = None  # Full-time, Part-time, Remote, etc.
    scraped_at: datetime = field(default_factory=datetime.now)


class NewsScraper(ABC):
    """Abstract base class for news scrapers."""
    
    @abstractmethod
    def get_source_name(self) -> str:
        pass
    
    @abstractmethod
    def scrape_headlines(self, limit: int = 20) -> List[NewsArticle]:
        pass
    
    @abstractmethod
    def scrape_article(self, url: str) -> Optional[NewsArticle]:
        pass


class HackerNewsScraper(NewsScraper):
    """Scraper for Hacker News (news.ycombinator.com)."""
    
    def get_source_name(self) -> str:
        return "Hacker News"
    
    def scrape_headlines(self, limit: int = 20) -> List[NewsArticle]:
        articles = []
        url = "https://news.ycombinator.com/"
        
        try:
            response = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all story links
            story_rows = soup.select('.athing')
            
            for row in story_rows[:limit]:
                title_elem = row.select_one('.titleline > a')
                if title_elem:
                    title = title_elem.get_text()
                    article_url = title_elem.get('href')
                    
                    # Get score and other metadata from next row
                    next_row = row.find_next_sibling('tr')
                    score_elem = next_row.select_one('.score') if next_row else None
                    
                    articles.append(NewsArticle(
                        title=title,
                        url=article_url if article_url.startswith('http') else f"https://news.ycombinator.com/{article_url}",
                        source=self.get_source_name(),
                        summary=f"Score: {score_elem.get_text() if score_elem else 'N/A'}"
                    ))
                    
            print(f"  Scraped {len(articles)} articles from {self.get_source_name()}")
            
        except Exception as e:
            print(f"  Error scraping {self.get_source_name()}: {e}")
        
        return articles
    
    def scrape_article(self, url: str) -> Optional[NewsArticle]:
        """Scrape a single article from Hacker News."""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title')
            title_text = title.get_text() if title else "Unknown"
            
            # Try to get meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            summary = meta_desc.get('content') if meta_desc else None
            
            return NewsArticle(
                title=title_text,
                url=url,
                source=self.get_source_name(),
                summary=summary[:200] if summary else None
            )
        except Exception as e:
            print(f"  Error scraping article: {e}")
            return None


class RSSFeedScraper(NewsScraper):
    """Generic RSS feed scraper."""
    
    def __init__(self, feed_url: str, source_name: str):
        self.feed_url = feed_url
        self.source_name = source_name
    
    def get_source_name(self) -> str:
        return self.source_name
    
    def scrape_headlines(self, limit: int = 20) -> List[NewsArticle]:
        import feedparser
        
        articles = []
        try:
            feed = feedparser.parse(self.feed_url)
            
            for entry in feed.entries[:limit]:
                published = None
                if hasattr(entry, 'published_parsed'):
                    published = datetime(*entry.published_parsed[:6])
                
                articles.append(NewsArticle(
                    title=entry.get('title', 'No Title'),
                    url=entry.get('link', ''),
                    source=self.source_name,
                    published_date=published,
                    summary=entry.get('summary', '')[:200]
                ))
            
            print(f"  Scraped {len(articles)} articles from {self.source_name} RSS")
        except Exception as e:
            print(f"  Error scraping RSS feed {self.source_name}: {e}")
        
        return articles
    
    def scrape_article(self, url: str) -> Optional[NewsArticle]:
        # RSS feeds typically don't have full articles
        return None


class NewsAggregator:
    """
    Aggregates news from multiple sources.
    
    Design Pattern: Composite Pattern - Combines multiple scrapers
    """
    
    def __init__(self):
        self.scrapers: List[NewsScraper] = []
        self.articles: List[NewsArticle] = []
    
    def add_scraper(self, scraper: NewsScraper) -> 'NewsAggregator':
        """Add a news scraper."""
        self.scrapers.append(scraper)
        return self
    
    def fetch_all(self, limit_per_source: int = 10) -> List[NewsArticle]:
        """Fetch headlines from all sources."""
        all_articles = []
        
        for scraper in self.scrapers:
            print(f"  Fetching from {scraper.get_source_name()}...")
            articles = scraper.scrape_headlines(limit_per_source)
            all_articles.extend(articles)
            time.sleep(1)  # Be respectful
        
        self.articles = all_articles
        return all_articles
    
    def search(self, keyword: str) -> List[NewsArticle]:
        """Search articles by keyword."""
        keyword_lower = keyword.lower()
        return [a for a in self.articles if keyword_lower in a.title.lower()]
    
    def get_by_source(self, source: str) -> List[NewsArticle]:
        """Get articles by source."""
        return [a for a in self.articles if a.source == source]
    
    def get_latest(self, n: int = 10) -> List[NewsArticle]:
        """Get latest n articles."""
        sorted_articles = sorted(self.articles, key=lambda x: x.scraped_at, reverse=True)
        return sorted_articles[:n]
    
    def generate_summary(self) -> str:
        """Generate a summary of fetched articles."""
        summary = []
        summary.append("=" * 60)
        summary.append("NEWS AGGREGATOR SUMMARY")
        summary.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        summary.append("=" * 60)
        
        # Group by source
        sources = {}
        for article in self.articles:
            if article.source not in sources:
                sources[article.source] = []
            sources[article.source].append(article)
        
        for source, articles in sources.items():
            summary.append(f"\n📰 {source} ({len(articles)} articles):")
            for i, article in enumerate(articles[:5], 1):
                summary.append(f"  {i}. {article.title}")
                summary.append(f"     {article.url[:60]}...")
        
        summary.append("\n" + "=" * 60)
        return "\n".join(summary)


class JobScraper(ABC):
    """Abstract base class for job scrapers."""
    
    @abstractmethod
    def get_source_name(self) -> str:
        pass
    
    @abstractmethod
    def search_jobs(self, keyword: str, location: str = "", limit: int = 20) -> List[JobListing]:
        pass


class RemoteOKScraper(JobScraper):
    """Scraper for RemoteOK (remote jobs)."""
    
    def get_source_name(self) -> str:
        return "RemoteOK"
    
    def search_jobs(self, keyword: str, location: str = "", limit: int = 20) -> List[JobListing]:
        jobs = []
        url = f"https://remoteok.com/remote-{keyword}-jobs"
        
        try:
            response = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            job_cards = soup.select('.job')
            
            for card in job_cards[:limit]:
                title_elem = card.select_one('.company h2')
                company_elem = card.select_one('.company h3')
                link_elem = card.select_one('a[href*="/remote-jobs/"]')
                
                if title_elem and company_elem and link_elem:
                    title = title_elem.get_text().strip()
                    company = company_elem.get_text().strip()
                    job_url = "https://remoteok.com" + link_elem.get('href')
                    
                    # Get salary/location info
                    location_elem = card.select_one('.location')
                    loc = location_elem.get_text().strip() if location_elem else "Remote"
                    
                    jobs.append(JobListing(
                        title=title,
                        company=company,
                        location=loc,
                        url=job_url,
                        source=self.get_source_name(),
                        job_type="Remote"
                    ))
            
            print(f"  Found {len(jobs)} jobs from {self.get_source_name()}")
        except Exception as e:
            print(f"  Error scraping {self.get_source_name()}: {e}")
        
        return jobs


class IndeedScraper(JobScraper):
    """Scraper for Indeed job listings."""
    
    def get_source_name(self) -> str:
        return "Indeed"
    
    def search_jobs(self, keyword: str, location: str = "", limit: int = 20) -> List[JobListing]:
        jobs = []
        url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
        
        try:
            response = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            job_cards = soup.select('.jobsearch-SerpJobCard')
            
            for card in job_cards[:limit]:
                title_elem = card.select_one('.jobtitle')
                company_elem = card.select_one('.company')
                location_elem = card.select_one('.location')
                link_elem = card.select_one('a[href*="/viewjob"]')
                
                if title_elem and company_elem and link_elem:
                    title = title_elem.get_text().strip()
                    company = company_elem.get_text().strip()
                    loc = location_elem.get_text().strip() if location_elem else "Not specified"
                    job_url = "https://www.indeed.com" + link_elem.get('href')
                    
                    jobs.append(JobListing(
                        title=title,
                        company=company,
                        location=loc,
                        url=job_url,
                        source=self.get_source_name()
                    ))
            
            print(f"  Found {len(jobs)} jobs from {self.get_source_name()}")
        except Exception as e:
            print(f"  Error scraping {self.get_source_name()}: {e}")
        
        return jobs


class JobAggregator:
    """
    Aggregates job listings from multiple sources.
    
    Design Pattern: Composite Pattern - Combines multiple scrapers
    """
    
    def __init__(self):
        self.scrapers: List[JobScraper] = []
        self.jobs: List[JobListing] = []
    
    def add_scraper(self, scraper: JobScraper) -> 'JobAggregator':
        """Add a job scraper."""
        self.scrapers.append(scraper)
        return self
    
    def search_all(self, keyword: str, location: str = "", limit_per_source: int = 20) -> List[JobListing]:
        """Search jobs across all sources."""
        all_jobs = []
        
        for scraper in self.scrapers:
            print(f"  Searching {scraper.get_source_name()} for '{keyword}'...")
            jobs = scraper.search_jobs(keyword, location, limit_per_source)
            all_jobs.extend(jobs)
            time.sleep(2)  # Be respectful
        
        self.jobs = all_jobs
        return all_jobs
    
    def filter_by_company(self, company: str) -> List[JobListing]:
        """Filter jobs by company."""
        company_lower = company.lower()
        return [j for j in self.jobs if company_lower in j.company.lower()]
    
    def filter_by_location(self, location: str) -> List[JobListing]:
        """Filter jobs by location."""
        location_lower = location.lower()
        return [j for j in self.jobs if location_lower in j.location.lower()]
    
    def filter_by_job_type(self, job_type: str) -> List[JobListing]:
        """Filter jobs by type (Remote, Full-time, etc.)."""
        type_lower = job_type.lower()
        return [j for j in self.jobs if j.job_type and type_lower in j.job_type.lower()]
    
    def get_summary(self) -> str:
        """Generate a summary of found jobs."""
        summary = []
        summary.append("=" * 60)
        summary.append("JOB SEARCH SUMMARY")
        summary.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        summary.append("=" * 60)
        
        # Group by source
        sources = {}
        for job in self.jobs:
            if job.source not in sources:
                sources[job.source] = []
            sources[job.source].append(job)
        
        summary.append(f"\n📊 TOTAL JOBS FOUND: {len(self.jobs)}")
        
        for source, jobs in sources.items():
            summary.append(f"\n📌 {source} ({len(jobs)} jobs):")
            for i, job in enumerate(jobs[:5], 1):
                summary.append(f"  {i}. {job.title} at {job.company}")
                summary.append(f"     Location: {job.location}")
                if job.salary:
                    summary.append(f"     Salary: {job.salary}")
                summary.append(f"     {job.url[:60]}...")
        
        summary.append("\n" + "=" * 60)
        return "\n".join(summary)


def demonstrate_news_and_job_scrapers():
    """
    Demonstrate news aggregator and job scraper.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: NEWS AGGREGATOR AND JOB SCRAPER")
    print("=" * 60)
    
    # NEWS AGGREGATOR
    print("\n1. NEWS AGGREGATOR")
    print("-" * 40)
    
    aggregator = NewsAggregator()
    aggregator.add_scraper(HackerNewsScraper())
    
    # Add RSS feeds (example feeds)
    # aggregator.add_scraper(RSSFeedScraper("https://feeds.bbci.co.uk/news/rss.xml", "BBC News"))
    # aggregator.add_scraper(RSSFeedScraper("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "NY Times"))
    
    print("\n  Fetching news headlines...")
    articles = aggregator.fetch_all(limit_per_source=10)
    
    print(f"\n  Total articles fetched: {len(articles)}")
    
    print("\n  Latest headlines:")
    for article in aggregator.get_latest(5):
        print(f"    • {article.title[:60]}...")
    
    # JOB AGGREGATOR
    print("\n2. JOB AGGREGATOR")
    print("-" * 40)
    
    job_aggregator = JobAggregator()
    job_aggregator.add_scraper(RemoteOKScraper())
    # job_aggregator.add_scraper(IndeedScraper())
    
    search_term = "python"
    print(f"\n  Searching for '{search_term}' jobs...")
    jobs = job_aggregator.search_all(search_term, limit_per_source=10)
    
    print(f"\n  Total jobs found: {len(jobs)}")
    
    if jobs:
        print("\n  Sample job listings:")
        for job in jobs[:3]:
            print(f"\n    📌 {job.title} at {job.company}")
            print(f"       Location: {job.location}")
            print(f"       URL: {job.url[:60]}...")
    
    print("\n3. SCRAPING BEST PRACTICES")
    print("-" * 40)
    
    best_practices = [
        "✓ Always check robots.txt before scraping",
        "✓ Set a reasonable User-Agent string",
        "✓ Add delays between requests (1-5 seconds)",
        "✓ Handle rate limiting (429 responses)",
        "✓ Use caching to avoid redundant requests",
        "✓ Respect copyright and terms of service",
        "✓ Identify yourself in requests",
        "✓ Consider using official APIs when available"
    ]
    
    for practice in best_practices:
        print(f"  {practice}")


if __name__ == "__main__":
    demonstrate_news_and_job_scrapers()
```

---

## 📋 Section 4: Real Estate Listing Scraper

A real estate listing scraper that extracts property information, prices, and details.

**SOLID Principles Applied:**
- Single Responsibility: Each scraper handles one property type
- Open/Closed: New property sources can be added

**Design Patterns:**
- Strategy Pattern: Different parsing strategies
- Builder Pattern: Builds property objects

```python
"""
REAL ESTATE LISTING SCRAPER

This section builds a scraper for real estate listings.

SOLID Principles Applied:
- Single Responsibility: Each scraper handles one property type
- Open/Closed: New property sources can be added

Design Patterns:
- Strategy Pattern: Different parsing strategies
- Builder Pattern: Builds property objects
"""

import re
import json
import time
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


@dataclass
class PropertyListing:
    """Represents a real estate property listing."""
    title: str
    price: float
    address: str
    url: str
    source: str
    bedrooms: Optional[int] = None
    bathrooms: Optional[float] = None
    square_feet: Optional[int] = None
    lot_size: Optional[str] = None
    property_type: Optional[str] = None
    year_built: Optional[int] = None
    description: Optional[str] = None
    features: List[str] = field(default_factory=list)
    images: List[str] = field(default_factory=list)
    agent_name: Optional[str] = None
    agent_phone: Optional[str] = None
    listed_date: Optional[datetime] = None
    scraped_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "price": self.price,
            "address": self.address,
            "url": self.url,
            "source": self.source,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "square_feet": self.square_feet,
            "lot_size": self.lot_size,
            "property_type": self.property_type,
            "year_built": self.year_built,
            "description": self.description[:200] if self.description else None,
            "features": self.features[:5],
            "agent_name": self.agent_name,
            "listed_date": self.listed_date.isoformat() if self.listed_date else None,
            "scraped_at": self.scraped_at.isoformat()
        }


class PropertyScraper(ABC):
    """Abstract base class for property scrapers."""
    
    @abstractmethod
    def get_source_name(self) -> str:
        pass
    
    @abstractmethod
    def search(self, location: str, max_price: Optional[float] = None,
               min_bedrooms: Optional[int] = None, limit: int = 20) -> List[PropertyListing]:
        pass
    
    @abstractmethod
    def get_property_details(self, url: str) -> Optional[PropertyListing]:
        pass


class ZillowScraper(PropertyScraper):
    """Scraper for Zillow property listings."""
    
    def get_source_name(self) -> str:
        return "Zillow"
    
    def search(self, location: str, max_price: Optional[float] = None,
               min_bedrooms: Optional[int] = None, limit: int = 20) -> List[PropertyListing]:
        listings = []
        
        # Build search URL
        search_url = f"https://www.zillow.com/homes/{location}_rb/"
        
        try:
            response = requests.get(search_url, timeout=30, 
                                   headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find property cards (Zillow's structure is complex, this is simplified)
            property_cards = soup.select('[data-testid="property-card"]')
            
            for card in property_cards[:limit]:
                # Extract address
                address_elem = card.select_one('[data-testid="address"]')
                address = address_elem.get_text().strip() if address_elem else "Unknown"
                
                # Extract price
                price_elem = card.select_one('[data-testid="price"]')
                price_text = price_elem.get_text().strip() if price_elem else "$0"
                price = self._parse_price(price_text)
                
                # Extract link
                link_elem = card.select_one('a')
                url = "https://www.zillow.com" + link_elem.get('href') if link_elem else ""
                
                # Extract beds/baths
                beds_elem = card.select_one('[data-testid="bed-bath"]')
                beds_text = beds_elem.get_text().strip() if beds_elem else ""
                bedrooms = self._parse_beds(beds_text)
                bathrooms = self._parse_baths(beds_text)
                
                # Extract sqft
                sqft_elem = card.select_one('[data-testid="sqft"]')
                sqft_text = sqft_elem.get_text().strip() if sqft_elem else ""
                sqft = self._parse_sqft(sqft_text)
                
                # Filter by criteria
                if max_price and price > max_price:
                    continue
                if min_bedrooms and bedrooms and bedrooms < min_bedrooms:
                    continue
                
                listings.append(PropertyListing(
                    title=f"Property in {address}",
                    price=price,
                    address=address,
                    url=url,
                    source=self.get_source_name(),
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    square_feet=sqft
                ))
            
            print(f"  Found {len(listings)} properties from {self.get_source_name()}")
            
        except Exception as e:
            print(f"  Error scraping {self.get_source_name()}: {e}")
        
        return listings
    
    def get_property_details(self, url: str) -> Optional[PropertyListing]:
        """Get detailed information about a property."""
        try:
            response = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract details
            title_elem = soup.find('title')
            title = title_elem.get_text().strip() if title_elem else "Unknown"
            
            # Price
            price_elem = soup.select_one('[data-testid="price"]')
            price_text = price_elem.get_text().strip() if price_elem else "$0"
            price = self._parse_price(price_text)
            
            # Address
            address_elem = soup.select_one('[data-testid="address"]')
            address = address_elem.get_text().strip() if address_elem else "Unknown"
            
            # Description
            desc_elem = soup.select_one('[data-testid="description"]')
            description = desc_elem.get_text().strip() if desc_elem else None
            
            # Features
            features = []
            feature_elems = soup.select('[data-testid="feature"]')
            for feat in feature_elems[:10]:
                features.append(feat.get_text().strip())
            
            return PropertyListing(
                title=title,
                price=price,
                address=address,
                url=url,
                source=self.get_source_name(),
                description=description,
                features=features
            )
            
        except Exception as e:
            print(f"  Error getting property details: {e}")
            return None
    
    def _parse_price(self, price_text: str) -> float:
        """Parse price from text."""
        match = re.search(r'[\d,]+', price_text)
        if match:
            price_str = match.group().replace(',', '')
            try:
                return float(price_str)
            except ValueError:
                pass
        return 0.0
    
    def _parse_beds(self, text: str) -> Optional[int]:
        """Parse number of bedrooms from text."""
        match = re.search(r'(\d+)\s*(?:bed|bd)', text, re.I)
        if match:
            return int(match.group(1))
        return None
    
    def _parse_baths(self, text: str) -> Optional[float]:
        """Parse number of bathrooms from text."""
        match = re.search(r'(\d+(?:\.\d+)?)\s*(?:bath|ba)', text, re.I)
        if match:
            return float(match.group(1))
        return None
    
    def _parse_sqft(self, text: str) -> Optional[int]:
        """Parse square footage from text."""
        match = re.search(r'(\d+(?:,\d+)?)\s*(?:sqft|sq\s*ft)', text, re.I)
        if match:
            sqft_str = match.group(1).replace(',', '')
            try:
                return int(sqft_str)
            except ValueError:
                pass
        return None


class RealtorScraper(PropertyScraper):
    """Scraper for Realtor.com property listings."""
    
    def get_source_name(self) -> str:
        return "Realtor.com"
    
    def search(self, location: str, max_price: Optional[float] = None,
               min_bedrooms: Optional[int] = None, limit: int = 20) -> List[PropertyListing]:
        listings = []
        
        # Build search URL (simplified)
        search_url = f"https://www.realtor.com/realestateandhomes-search/{location.replace(' ', '_')}"
        
        try:
            response = requests.get(search_url, timeout=30, 
                                   headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            property_cards = soup.select('[data-testid="property-card"]')
            
            for card in property_cards[:limit]:
                # Extract address
                address_elem = card.select_one('[data-testid="address"]')
                address = address_elem.get_text().strip() if address_elem else "Unknown"
                
                # Extract price
                price_elem = card.select_one('[data-testid="price"]')
                price_text = price_elem.get_text().strip() if price_elem else "$0"
                price = self._parse_price(price_text)
                
                # Extract link
                link_elem = card.select_one('a')
                url = link_elem.get('href') if link_elem else ""
                if url and not url.startswith('http'):
                    url = "https://www.realtor.com" + url
                
                # Filter by criteria
                if max_price and price > max_price:
                    continue
                
                listings.append(PropertyListing(
                    title=f"Property in {address}",
                    price=price,
                    address=address,
                    url=url,
                    source=self.get_source_name()
                ))
            
            print(f"  Found {len(listings)} properties from {self.get_source_name()}")
            
        except Exception as e:
            print(f"  Error scraping {self.get_source_name()}: {e}")
        
        return listings
    
    def get_property_details(self, url: str) -> Optional[PropertyListing]:
        """Get detailed information about a property."""
        try:
            response = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title_elem = soup.find('title')
            title = title_elem.get_text().strip() if title_elem else "Unknown"
            
            # Price
            price_elem = soup.select_one('[data-testid="price"]')
            price_text = price_elem.get_text().strip() if price_elem else "$0"
            price = self._parse_price(price_text)
            
            # Address
            address_elem = soup.select_one('[data-testid="address"]')
            address = address_elem.get_text().strip() if address_elem else "Unknown"
            
            return PropertyListing(
                title=title,
                price=price,
                address=address,
                url=url,
                source=self.get_source_name()
            )
            
        except Exception as e:
            print(f"  Error getting property details: {e}")
            return None
    
    def _parse_price(self, price_text: str) -> float:
        """Parse price from text."""
        match = re.search(r'[\d,]+', price_text)
        if match:
            price_str = match.group().replace(',', '')
            try:
                return float(price_str)
            except ValueError:
                pass
        return 0.0


class PropertyAggregator:
    """
    Aggregates property listings from multiple sources.
    
    Design Pattern: Composite Pattern - Combines multiple scrapers
    """
    
    def __init__(self):
        self.scrapers: List[PropertyScraper] = []
        self.listings: List[PropertyListing] = []
    
    def add_scraper(self, scraper: PropertyScraper) -> 'PropertyAggregator':
        """Add a property scraper."""
        self.scrapers.append(scraper)
        return self
    
    def search_all(self, location: str, max_price: Optional[float] = None,
                   min_bedrooms: Optional[int] = None,
                   limit_per_source: int = 20) -> List[PropertyListing]:
        """Search properties across all sources."""
        all_listings = []
        
        for scraper in self.scrapers:
            print(f"  Searching {scraper.get_source_name()} in {location}...")
            listings = scraper.search(location, max_price, min_bedrooms, limit_per_source)
            all_listings.extend(listings)
            time.sleep(2)
        
        # Sort by price
        all_listings.sort(key=lambda x: x.price)
        self.listings = all_listings
        return all_listings
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> List[PropertyListing]:
        """Filter listings by price range."""
        return [l for l in self.listings if min_price <= l.price <= max_price]
    
    def filter_by_bedrooms(self, bedrooms: int) -> List[PropertyListing]:
        """Filter listings by minimum bedrooms."""
        return [l for l in self.listings if l.bedrooms and l.bedrooms >= bedrooms]
    
    def get_cheapest(self, n: int = 5) -> List[PropertyListing]:
        """Get cheapest listings."""
        sorted_listings = sorted(self.listings, key=lambda x: x.price)
        return sorted_listings[:n]
    
    def get_most_expensive(self, n: int = 5) -> List[PropertyListing]:
        """Get most expensive listings."""
        sorted_listings = sorted(self.listings, key=lambda x: x.price, reverse=True)
        return sorted_listings[:n]
    
    def generate_report(self) -> str:
        """Generate a property search report."""
        report = []
        report.append("=" * 60)
        report.append("PROPERTY SEARCH REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        if not self.listings:
            report.append("\nNo properties found.")
            return "\n".join(report)
        
        # Statistics
        prices = [l.price for l in self.listings]
        report.append(f"\n📊 SEARCH STATISTICS:")
        report.append(f"  Total properties found: {len(self.listings)}")
        report.append(f"  Price range: ${min(prices):,.0f} - ${max(prices):,.0f}")
        report.append(f"  Average price: ${sum(prices)/len(prices):,.0f}")
        
        # Properties with bedrooms
        with_bedrooms = [l for l in self.listings if l.bedrooms]
        if with_bedrooms:
            avg_bedrooms = sum(l.bedrooms for l in with_bedrooms) / len(with_bedrooms)
            report.append(f"  Average bedrooms: {avg_bedrooms:.1f}")
        
        report.append(f"\n🏠 TOP 5 CHEAPEST PROPERTIES:")
        for i, listing in enumerate(self.get_cheapest(5), 1):
            report.append(f"\n  {i}. {listing.title}")
            report.append(f"     Price: ${listing.price:,.0f}")
            report.append(f"     Address: {listing.address[:60]}...")
            if listing.bedrooms:
                report.append(f"     Bedrooms: {listing.bedrooms}")
            report.append(f"     Source: {listing.source}")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)
    
    def export_to_csv(self, filename: str) -> None:
        """Export listings to CSV."""
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            if not self.listings:
                return
            
            fieldnames = ['title', 'price', 'address', 'url', 'source', 
                         'bedrooms', 'bathrooms', 'square_feet']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for listing in self.listings:
                writer.writerow({
                    'title': listing.title,
                    'price': listing.price,
                    'address': listing.address,
                    'url': listing.url,
                    'source': listing.source,
                    'bedrooms': listing.bedrooms or '',
                    'bathrooms': listing.bathrooms or '',
                    'square_feet': listing.square_feet or ''
                })
        
        print(f"  Exported {len(self.listings)} listings to {filename}")


def demonstrate_property_scraper():
    """
    Demonstrate the real estate scraper.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: REAL ESTATE LISTING SCRAPER")
    print("=" * 60)
    
    aggregator = PropertyAggregator()
    aggregator.add_scraper(ZillowScraper())
    # aggregator.add_scraper(RealtorScraper())
    
    print("\n1. SEARCHING FOR PROPERTIES")
    print("-" * 40)
    
    location = "San Francisco, CA"
    print(f"  Searching in: {location}")
    
    listings = aggregator.search_all(location, max_price=1500000, min_bedrooms=2, limit_per_source=10)
    
    print(f"\n  Found {len(listings)} properties")
    
    print("\n2. CHEAPEST PROPERTIES")
    print("-" * 40)
    
    cheapest = aggregator.get_cheapest(3)
    for prop in cheapest:
        print(f"\n  ${prop.price:,.0f} - {prop.address}")
        if prop.bedrooms:
            print(f"    {prop.bedrooms} beds, {prop.bathrooms} baths")
        print(f"    Source: {prop.source}")
    
    print("\n3. PROPERTY SEARCH REPORT")
    print("-" * 40)
    
    report = aggregator.generate_report()
    print(report[:500] + "...")
    
    print("\n4. SCRAPING ETHICS AND LEGAL CONSIDERATIONS")
    print("-" * 40)
    
    ethics = [
        "✓ Always check robots.txt before scraping",
        "✓ Respect rate limits (don't overload servers)",
        "✓ Identify your scraper with a User-Agent",
        "✓ Use official APIs when available",
        "✓ Don't scrape personal or copyrighted data",
        "✓ Store data responsibly, don't republish without permission",
        "✓ Be aware that terms of service may prohibit scraping",
        "✓ Consider the impact on the website's resources"
    ]
    
    for item in ethics:
        print(f"  {item}")


if __name__ == "__main__":
    demonstrate_property_scraper()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **BeautifulSoup Basics** – Parse HTML with `BeautifulSoup(html, 'html.parser')`. Navigate with `find()`, `find_all()`, `select()` (CSS selectors).

- **Finding Methods** – `find()` (first match), `find_all()` (all matches), `select()` (CSS selectors). Filter by tag, class, id, attributes.

- **Navigation** – `.parent`, `.parents`, `.children`, `.contents`, `.next_sibling`, `.previous_sibling`. Traverse the parse tree.

- **Attribute Access** – `element['attribute']`, `element.get('attribute')`, `element.attrs`. Extract href, src, class, id.

- **Price Monitoring Bot** – Track product prices, detect drops, send alerts. Multiple parsers for different sites (Amazon, eBay, generic). Save/load state.

- **News Aggregator** – Scrape headlines from Hacker News, RSS feeds. Search by keyword, filter by source, generate summaries.

- **Job Scraper** – Search job listings from RemoteOK, Indeed. Filter by company, location, job type.

- **Real Estate Scraper** – Extract property listings, prices, details. Filter by price, bedrooms. Generate reports, export to CSV.

- **Ethical Scraping** – Respect robots.txt, add delays, identify yourself, use APIs when available, don't overload servers.

- **SOLID Principles Applied** – Single Responsibility (each scraper handles one source), Open/Closed (new sources can be added), Dependency Inversion (scrapers depend on abstractions), Interface Segregation (clean scraper interfaces).

- **Design Patterns Used** – Strategy Pattern (different parsing strategies), Observer Pattern (price drop alerts), Composite Pattern (aggregators combine scrapers), Factory Pattern (parser selection), Builder Pattern (property object construction), Adapter Pattern (BeautifulSoup adapts HTML).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Automation with os and sys

- **📚 Series H Catalog:** Web Development & Automation – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler (Series H, Story 5)

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
| Series H | 5 | 4 | 1 | 80% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **49** | **3** | **94%** |

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

**Next Story:** Series H, Story 5: The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler

---

## 📝 Your Invitation

You've mastered web scraping. Now build something with what you've learned:

1. **Build a cryptocurrency price tracker** – Scrape prices from multiple exchanges, detect changes.

2. **Create a weather data scraper** – Extract forecasts from weather websites.

3. **Build a social media post collector** – Scrape posts from public profiles (respect terms of service).

4. **Create a product review analyzer** – Scrape reviews, analyze sentiment, extract common themes.

5. **Build a stock market news aggregator** – Collect financial news, filter by ticker symbol.

**You've mastered web scraping. Next stop: Scheduling Tasks!**

---

*Found this helpful? Clap, comment, and share what you scraped. Next stop: Scheduling Tasks!* 🚇