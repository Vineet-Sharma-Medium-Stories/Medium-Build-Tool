# The 2026 Python Metromap: Flask – Building Web APIs

## Series H: Web Development & Automation | Story 1 of 5

![The 2026 Python Metromap/images/Flask – Building Web APIs](images/Flask – Building Web APIs.png)

## 📖 Introduction

**Welcome to the first stop on the Web Development & Automation Line.**

You've mastered data science and visualization. You can analyze data, create stunning visualizations, and extract insights. But data is most valuable when it can be accessed and used by others. That's where web development comes in.

Flask is a lightweight, flexible web framework for Python. It's perfect for building web APIs, microservices, and small to medium web applications. Unlike full-stack frameworks like Django, Flask gives you the freedom to choose your own components while providing just enough structure to get started quickly.

This story—**The 2026 Python Metromap: Flask – Building Web APIs**—is your guide to building web APIs with Flask. We'll build a complete URL shortener service with REST endpoints, database storage, and redirect logic. We'll create a task management API with CRUD operations. We'll implement authentication and authorization. We'll build a product catalog API with search and filtering. And we'll deploy our API with proper error handling and documentation.

**Let's build APIs.**

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

- 🌶️ **The 2026 Python Metromap: Flask – Building Web APIs** – URL shortener service; REST endpoints; database storage; redirect logic. **⬅️ YOU ARE HERE**

- 🎸 **The 2026 Python Metromap: Django – Full-Stack Web Apps** – Blog platform; user authentication; admin panel; comments system; search functionality. 🔜 *Up Next*

- 🤖 **The 2026 Python Metromap: Automation with os and sys** – File organizer script; type-based sorting; file renaming; temp directory cleaning.

- 🕸️ **The 2026 Python Metromap: Web Scraping with BeautifulSoup** – Price monitoring bot; multi-site product tracking; price drop alerts.

- ⏰ **The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler** – Daily report emailer; weekly backup system; cron-style job scheduler.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🌶️ Section 1: Flask Fundamentals – Your First API

Flask is a micro-framework that makes it easy to create web applications and APIs with minimal boilerplate.

**SOLID Principle Applied: Single Responsibility** – Each route handles one specific endpoint.

**Design Pattern: Front Controller Pattern** – Flask routes requests to appropriate handlers.

```python
"""
FLASK FUNDAMENTALS: YOUR FIRST API

This section covers the basics of creating Flask applications.

SOLID Principle: Single Responsibility
- Each route handles one specific endpoint

Design Pattern: Front Controller Pattern
- Flask routes requests to appropriate handlers
"""

from flask import Flask, jsonify, request, abort, make_response
from datetime import datetime
import json

# Create Flask application
app = Flask(__name__)


# BASIC ROUTE
@app.route('/')
def home():
    """Home endpoint - returns welcome message."""
    return jsonify({
        "message": "Welcome to the Metromap API",
        "version": "1.0.0",
        "endpoints": [
            "/api/health",
            "/api/greet/<name>",
            "/api/echo",
            "/api/time"
        ]
    })


# HEALTH CHECK ENDPOINT
@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Metromap API"
    })


# PATH PARAMETER
@app.route('/api/greet/<name>')
def greet(name):
    """Greet a person by name."""
    return jsonify({
        "message": f"Hello, {name}!",
        "name": name,
        "timestamp": datetime.now().isoformat()
    })


# QUERY PARAMETERS
@app.route('/api/search')
def search():
    """Search endpoint with query parameters."""
    query = request.args.get('q', '')
    limit = request.args.get('limit', 10, type=int)
    page = request.args.get('page', 1, type=int)
    
    # Simulate search results
    results = [
        {"id": i, "name": f"Result {i}", "score": 100 - i}
        for i in range(1, min(limit + 1, 51))
    ]
    
    return jsonify({
        "query": query,
        "page": page,
        "limit": limit,
        "total": len(results),
        "results": results,
        "timestamp": datetime.now().isoformat()
    })


# POST REQUEST WITH JSON BODY
@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo back the request body."""
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    
    return jsonify({
        "echo": data,
        "received_at": datetime.now().isoformat()
    }), 201


# DIFFERENT HTTP METHODS
@app.route('/api/time', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_time():
    """Handle different HTTP methods."""
    if request.method == 'GET':
        return jsonify({
            "method": "GET",
            "current_time": datetime.now().isoformat()
        })
    elif request.method == 'POST':
        data = request.get_json() or {}
        return jsonify({
            "method": "POST",
            "received": data,
            "current_time": datetime.now().isoformat()
        }), 201
    elif request.method == 'PUT':
        data = request.get_json() or {}
        return jsonify({
            "method": "PUT",
            "updated": data,
            "current_time": datetime.now().isoformat()
        })
    else:  # DELETE
        return jsonify({
            "method": "DELETE",
            "message": "Resource deleted",
            "current_time": datetime.now().isoformat()
        })


# ERROR HANDLING
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource was not found",
        "status_code": 404
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "status_code": 500
    }), 500


# REQUEST LOGGING MIDDLEWARE
@app.before_request
def log_request():
    """Log all incoming requests."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
          f"{request.method} {request.path} - "
          f"IP: {request.remote_addr}")


def run_flask_app():
    """
    Run the Flask application.
    
    Note: In a real environment, you would use:
    flask run --host=0.0.0.0 --port=5000
    
    For demonstration, we'll show the code structure.
    """
    print("=" * 60)
    print("SECTION 1: FLASK FUNDAMENTALS")
    print("=" * 60)
    
    print("\n1. FLASK APPLICATION STRUCTURE")
    print("-" * 40)
    
    print("""
    from flask import Flask, jsonify, request
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({"message": "Hello, World!"})
    
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
    """)
    
    print("\n2. RUNNING THE APPLICATION")
    print("-" * 40)
    
    print("""
    # Set environment variables
    export FLASK_APP=app.py
    export FLASK_ENV=development
    
    # Run the application
    flask run
    
    # Or run directly
    python app.py
    
    # The API will be available at:
    # http://localhost:5000/
    """)
    
    print("\n3. TESTING THE API")
    print("-" * 40)
    
    print("""
    # GET request
    curl http://localhost:5000/
    
    # GET with path parameter
    curl http://localhost:5000/api/greet/Alice
    
    # GET with query parameters
    curl "http://localhost:5000/api/search?q=python&limit=5"
    
    # POST with JSON body
    curl -X POST http://localhost:5000/api/echo \\
         -H "Content-Type: application/json" \\
         -d '{"name": "Alice", "message": "Hello"}'
    """)
    
    print("\n4. API ENDPOINTS SUMMARY")
    print("-" * 40)
    
    endpoints = [
        ("GET", "/", "Home/Welcome"),
        ("GET", "/api/health", "Health check"),
        ("GET", "/api/greet/<name>", "Greet by name"),
        ("GET", "/api/search", "Search with query params"),
        ("POST", "/api/echo", "Echo request body"),
        ("GET/POST/PUT/DELETE", "/api/time", "Time operations")
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:8} {path:25} - {description}")


if __name__ == "__main__":
    run_flask_app()
    # Uncomment to run the actual server:
    # app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🔗 Section 2: URL Shortener Service

A complete URL shortener API with database storage, redirect logic, and analytics.

**SOLID Principles Applied:**
- Single Responsibility: Each module handles one aspect (storage, encoding, redirection)
- Dependency Inversion: Depends on storage abstraction

**Design Patterns:**
- Repository Pattern: Data storage abstraction
- Factory Pattern: Creates short codes

```python
"""
URL SHORTENER SERVICE

This section builds a complete URL shortener API.

SOLID Principles Applied:
- Single Responsibility: Each module handles one aspect
- Dependency Inversion: Depends on storage abstraction

Design Patterns:
- Repository Pattern: Data storage abstraction
- Factory Pattern: Creates short codes
"""

from flask import Flask, request, jsonify, redirect, abort
from datetime import datetime, timedelta
import string
import random
import hashlib
import sqlite3
from contextlib import contextmanager
import re

app = Flask(__name__)


# =============================================================================
# DATABASE LAYER
# =============================================================================

class Database:
    """SQLite database wrapper for URL storage."""
    
    def __init__(self, db_path='urls.db'):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize database tables."""
        with self.get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    short_code TEXT UNIQUE NOT NULL,
                    long_url TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP,
                    clicks INTEGER DEFAULT 0,
                    last_accessed TIMESTAMP,
                    user_id TEXT
                )
            ''')
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_short_code ON urls(short_code)
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS analytics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    short_code TEXT NOT NULL,
                    accessed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ip_address TEXT,
                    user_agent TEXT,
                    referer TEXT
                )
            ''')
    
    @contextmanager
    def get_connection(self):
        """Get database connection with context manager."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
    
    def create_url(self, short_code, long_url, user_id=None, expires_days=None):
        """Create a new short URL."""
        expires_at = None
        if expires_days:
            expires_at = datetime.now() + timedelta(days=expires_days)
        
        with self.get_connection() as conn:
            try:
                conn.execute(
                    "INSERT INTO urls (short_code, long_url, user_id, expires_at) VALUES (?, ?, ?, ?)",
                    (short_code, long_url, user_id, expires_at)
                )
                return True
            except sqlite3.IntegrityError:
                return False
    
    def get_url(self, short_code):
        """Get URL by short code."""
        with self.get_connection() as conn:
            result = conn.execute(
                "SELECT * FROM urls WHERE short_code = ?",
                (short_code,)
            ).fetchone()
            
            if result:
                # Check expiration
                if result['expires_at']:
                    expires_at = datetime.fromisoformat(result['expires_at'])
                    if datetime.now() > expires_at:
                        return None
                
                # Update click count
                conn.execute(
                    "UPDATE urls SET clicks = clicks + 1, last_accessed = CURRENT_TIMESTAMP "
                    "WHERE short_code = ?",
                    (short_code,)
                )
                
                return dict(result)
            return None
    
    def record_analytics(self, short_code, ip_address, user_agent, referer):
        """Record analytics for a URL access."""
        with self.get_connection() as conn:
            conn.execute(
                "INSERT INTO analytics (short_code, ip_address, user_agent, referer) "
                "VALUES (?, ?, ?, ?)",
                (short_code, ip_address, user_agent, referer)
            )
    
    def get_stats(self, short_code):
        """Get statistics for a short URL."""
        with self.get_connection() as conn:
            url_data = conn.execute(
                "SELECT clicks, created_at, last_accessed FROM urls WHERE short_code = ?",
                (short_code,)
            ).fetchone()
            
            analytics = conn.execute(
                "SELECT COUNT(*) as total, COUNT(DISTINCT ip_address) as unique_visitors "
                "FROM analytics WHERE short_code = ?",
                (short_code,)
            ).fetchone()
            
            return {
                "clicks": url_data['clicks'] if url_data else 0,
                "created_at": url_data['created_at'] if url_data else None,
                "last_accessed": url_data['last_accessed'] if url_data else None,
                "total_visits": analytics['total'] if analytics else 0,
                "unique_visitors": analytics['unique_visitors'] if analytics else 0
            }
    
    def list_urls(self, user_id=None, limit=100):
        """List URLs for a user."""
        with self.get_connection() as conn:
            if user_id:
                results = conn.execute(
                    "SELECT short_code, long_url, clicks, created_at, expires_at "
                    "FROM urls WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
                    (user_id, limit)
                ).fetchall()
            else:
                results = conn.execute(
                    "SELECT short_code, long_url, clicks, created_at, expires_at "
                    "FROM urls ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                ).fetchall()
            
            return [dict(row) for row in results]


# Initialize database
db = Database()


# =============================================================================
# URL SHORTENER HELPERS
# =============================================================================

class ShortCodeGenerator:
    """Generate unique short codes for URLs."""
    
    CHARSET = string.ascii_letters + string.digits
    CODE_LENGTH = 6
    
    @classmethod
    def generate_random(cls):
        """Generate random short code."""
        return ''.join(random.choice(cls.CHARSET) for _ in range(cls.CODE_LENGTH))
    
    @classmethod
    def generate_from_url(cls, long_url):
        """Generate short code from URL hash."""
        hash_obj = hashlib.md5(long_url.encode())
        hash_hex = hash_obj.hexdigest()
        # Take first CODE_LENGTH characters of base64-like encoding
        import base64
        b64 = base64.b64encode(hash_obj.digest()).decode('ascii')
        return b64[:cls.CODE_LENGTH].replace('+', 'A').replace('/', 'B')
    
    @classmethod
    def generate_unique(cls, long_url=None):
        """Generate a unique short code."""
        if long_url:
            code = cls.generate_from_url(long_url)
            # Check if exists
            if not db.get_url(code):
                return code
        
        # Try random codes until unique
        for _ in range(10):
            code = cls.generate_random()
            if not db.get_url(code):
                return code
        
        # Fallback to timestamp-based
        import time
        return base64.b64encode(str(int(time.time() * 1000)).encode()).decode()[:cls.CODE_LENGTH]


def validate_url(url):
    """Validate URL format."""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None


# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """
    Create a short URL.
    
    Request body:
    {
        "url": "https://example.com/very/long/url",
        "custom_code": "optional",  # Optional custom short code
        "expires_days": 30,         # Optional expiration in days
        "user_id": "user123"        # Optional user identifier
    }
    """
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' field"}), 400
    
    long_url = data['url']
    
    # Validate URL
    if not validate_url(long_url):
        return jsonify({"error": "Invalid URL format"}), 400
    
    # Get or generate short code
    custom_code = data.get('custom_code')
    if custom_code:
        # Validate custom code
        if not re.match(r'^[a-zA-Z0-9_-]+$', custom_code):
            return jsonify({"error": "Custom code can only contain letters, numbers, underscore, and hyphen"}), 400
        if len(custom_code) < 3 or len(custom_code) > 20:
            return jsonify({"error": "Custom code must be 3-20 characters"}), 400
        if db.get_url(custom_code):
            return jsonify({"error": "Custom code already exists"}), 409
        short_code = custom_code
    else:
        short_code = ShortCodeGenerator.generate_unique(long_url)
    
    # Create URL record
    user_id = data.get('user_id')
    expires_days = data.get('expires_days')
    
    success = db.create_url(short_code, long_url, user_id, expires_days)
    
    if not success:
        return jsonify({"error": "Failed to create short URL"}), 500
    
    # Generate full short URL
    base_url = request.host_url.rstrip('/')
    short_url = f"{base_url}/{short_code}"
    
    return jsonify({
        "short_code": short_code,
        "short_url": short_url,
        "long_url": long_url,
        "created_at": datetime.now().isoformat(),
        "expires_days": expires_days
    }), 201


@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect short code to original URL."""
    url_data = db.get_url(short_code)
    
    if not url_data:
        abort(404)
    
    # Record analytics
    db.record_analytics(
        short_code,
        request.remote_addr,
        request.headers.get('User-Agent', ''),
        request.headers.get('Referer', '')
    )
    
    return redirect(url_data['long_url'], code=302)


@app.route('/api/stats/<short_code>')
def get_stats(short_code):
    """Get statistics for a short URL."""
    url_data = db.get_url(short_code)
    
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404
    
    stats = db.get_stats(short_code)
    
    return jsonify({
        "short_code": short_code,
        "long_url": url_data['long_url'],
        "created_at": url_data['created_at'],
        "expires_at": url_data.get('expires_at'),
        "clicks": stats['clicks'],
        "total_visits": stats['total_visits'],
        "unique_visitors": stats['unique_visitors'],
        "last_accessed": url_data.get('last_accessed')
    })


@app.route('/api/urls', methods=['GET'])
def list_urls():
    """List all shortened URLs."""
    user_id = request.args.get('user_id')
    limit = request.args.get('limit', 100, type=int)
    
    urls = db.list_urls(user_id, limit)
    
    base_url = request.host_url.rstrip('/')
    for url in urls:
        url['short_url'] = f"{base_url}/{url['short_code']}"
    
    return jsonify({
        "total": len(urls),
        "urls": urls
    })


@app.route('/api/urls/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    """Delete a short URL."""
    # In production, you would check user authentication here
    url_data = db.get_url(short_code)
    
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404
    
    # For demo, we'll just check if it exists
    # In production, verify user owns the URL
    
    with db.get_connection() as conn:
        conn.execute("DELETE FROM urls WHERE short_code = ?", (short_code,))
        conn.execute("DELETE FROM analytics WHERE short_code = ?", (short_code,))
    
    return jsonify({"message": "Short URL deleted successfully"})


@app.route('/api/validate', methods=['POST'])
def validate_url_endpoint():
    """Validate a URL without creating a short link."""
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' field"}), 400
    
    is_valid = validate_url(data['url'])
    
    return jsonify({
        "url": data['url'],
        "valid": is_valid
    })


# =============================================================================
# ERROR HANDLERS
# =============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "Short URL not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500


def run_url_shortener():
    """
    Demonstrate the URL shortener service.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: URL SHORTENER SERVICE")
    print("=" * 60)
    
    print("\n1. API ENDPOINTS")
    print("-" * 40)
    
    endpoints = [
        ("POST", "/api/shorten", "Create short URL"),
        ("GET", "/<short_code>", "Redirect to original URL"),
        ("GET", "/api/stats/<short_code>", "Get URL statistics"),
        ("GET", "/api/urls", "List all URLs"),
        ("DELETE", "/api/urls/<short_code>", "Delete URL"),
        ("POST", "/api/validate", "Validate URL format")
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:8} {path:30} - {description}")
    
    print("\n2. EXAMPLE API CALLS")
    print("-" * 40)
    
    print("""
    # Create a short URL
    curl -X POST http://localhost:5000/api/shorten \\
         -H "Content-Type: application/json" \\
         -d '{"url": "https://www.python.org/doc/very/long/url/that/needs/shortening"}'
    
    # Response:
    {
        "short_code": "aB3xY7",
        "short_url": "http://localhost:5000/aB3xY7",
        "long_url": "https://www.python.org/doc/very/long/url/that/needs/shortening",
        "created_at": "2024-01-15T10:30:00"
    }
    
    # Visit the short URL (redirects automatically)
    curl -L http://localhost:5000/aB3xY7
    
    # Get statistics
    curl http://localhost:5000/api/stats/aB3xY7
    
    # Response:
    {
        "short_code": "aB3xY7",
        "long_url": "https://www.python.org/doc/...",
        "clicks": 42,
        "total_visits": 42,
        "unique_visitors": 15,
        "last_accessed": "2024-01-15T15:30:00"
    }
    """)
    
    print("\n3. CUSTOM SHORT CODE")
    print("-" * 40)
    
    print("""
    # Create with custom code
    curl -X POST http://localhost:5000/api/shorten \\
         -H "Content-Type: application/json" \\
         -d '{
             "url": "https://github.com/features",
             "custom_code": "github",
             "expires_days": 365
         }'
    
    # Response:
    {
        "short_code": "github",
        "short_url": "http://localhost:5000/github",
        "long_url": "https://github.com/features",
        "expires_days": 365
    }
    """)
    
    print("\n4. DATABASE SCHEMA")
    print("-" * 40)
    
    print("""
    -- URLs table
    CREATE TABLE urls (
        id INTEGER PRIMARY KEY,
        short_code TEXT UNIQUE NOT NULL,
        long_url TEXT NOT NULL,
        created_at TIMESTAMP,
        expires_at TIMESTAMP,
        clicks INTEGER DEFAULT 0,
        last_accessed TIMESTAMP,
        user_id TEXT
    );
    
    -- Analytics table
    CREATE TABLE analytics (
        id INTEGER PRIMARY KEY,
        short_code TEXT NOT NULL,
        accessed_at TIMESTAMP,
        ip_address TEXT,
        user_agent TEXT,
        referer TEXT
    );
    """)


if __name__ == "__main__":
    run_url_shortener()
    # Uncomment to run the server:
    # app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 📝 Section 3: Task Management API

A complete task management API with CRUD operations, authentication, and filtering.

**SOLID Principles Applied:**
- Single Responsibility: Each endpoint handles one resource operation
- Open/Closed: New operations can be added

**Design Patterns:**
- Repository Pattern: Task storage abstraction
- DTO Pattern: Data transfer objects for API responses

```python
"""
TASK MANAGEMENT API

This section builds a complete task management API.

SOLID Principles Applied:
- Single Responsibility: Each endpoint handles one resource operation
- Open/Closed: New operations can be added

Design Patterns:
- Repository Pattern: Task storage abstraction
- DTO Pattern: Data transfer objects for API responses
"""

from flask import Flask, request, jsonify, abort, g
from datetime import datetime
from functools import wraps
import sqlite3
from contextlib import contextmanager
import hashlib
import secrets

app = Flask(__name__)


# =============================================================================
# DATABASE LAYER
# =============================================================================

class TaskDatabase:
    """Database wrapper for task management."""
    
    def __init__(self, db_path='tasks.db'):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize database tables."""
        with self.get_connection() as conn:
            # Users table
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    email TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tasks table
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'pending',
                    priority INTEGER DEFAULT 2,
                    due_date TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    completed_at TIMESTAMP,
                    tags TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')
            
            # Create indexes
            conn.execute('CREATE INDEX IF NOT EXISTS idx_tasks_user ON tasks(user_id)')
            conn.execute('CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status)')
    
    @contextmanager
    def get_connection(self):
        """Get database connection with context manager."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
    
    # User operations
    def create_user(self, username, password_hash, email=None):
        """Create a new user."""
        with self.get_connection() as conn:
            try:
                cursor = conn.execute(
                    "INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)",
                    (username, password_hash, email)
                )
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                return None
    
    def get_user_by_username(self, username):
        """Get user by username."""
        with self.get_connection() as conn:
            result = conn.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            ).fetchone()
            return dict(result) if result else None
    
    def get_user_by_id(self, user_id):
        """Get user by ID."""
        with self.get_connection() as conn:
            result = conn.execute(
                "SELECT id, username, email, created_at FROM users WHERE id = ?",
                (user_id,)
            ).fetchone()
            return dict(result) if result else None
    
    # Task operations
    def create_task(self, user_id, title, description=None, priority=2, due_date=None, tags=None):
        """Create a new task."""
        with self.get_connection() as conn:
            cursor = conn.execute(
                """INSERT INTO tasks (user_id, title, description, priority, due_date, tags)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (user_id, title, description, priority, due_date, tags)
            )
            task_id = cursor.lastrowid
            return self.get_task(task_id, user_id)
    
    def get_task(self, task_id, user_id):
        """Get a task by ID."""
        with self.get_connection() as conn:
            result = conn.execute(
                "SELECT * FROM tasks WHERE id = ? AND user_id = ?",
                (task_id, user_id)
            ).fetchone()
            return dict(result) if result else None
    
    def get_tasks(self, user_id, status=None, priority=None, limit=100, offset=0):
        """Get tasks for a user with filters."""
        query = "SELECT * FROM tasks WHERE user_id = ?"
        params = [user_id]
        
        if status:
            query += " AND status = ?"
            params.append(status)
        
        if priority:
            query += " AND priority = ?"
            params.append(priority)
        
        query += " ORDER BY priority ASC, due_date ASC, created_at DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        with self.get_connection() as conn:
            results = conn.execute(query, params).fetchall()
            return [dict(row) for row in results]
    
    def update_task(self, task_id, user_id, updates):
        """Update a task."""
        allowed_fields = ['title', 'description', 'status', 'priority', 'due_date', 'tags']
        set_clauses = []
        params = []
        
        for field in allowed_fields:
            if field in updates:
                set_clauses.append(f"{field} = ?")
                params.append(updates[field])
        
        if not set_clauses:
            return self.get_task(task_id, user_id)
        
        params.extend([task_id, user_id])
        query = f"UPDATE tasks SET {', '.join(set_clauses)}, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND user_id = ?"
        
        with self.get_connection() as conn:
            conn.execute(query, params)
            return self.get_task(task_id, user_id)
    
    def delete_task(self, task_id, user_id):
        """Delete a task."""
        with self.get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, user_id))
            return True
    
    def complete_task(self, task_id, user_id):
        """Mark a task as completed."""
        with self.get_connection() as conn:
            conn.execute(
                "UPDATE tasks SET status = 'completed', completed_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP "
                "WHERE id = ? AND user_id = ?",
                (task_id, user_id)
            )
            return self.get_task(task_id, user_id)


# Initialize database
db = TaskDatabase()


# =============================================================================
# AUTHENTICATION
# =============================================================================

def hash_password(password):
    """Hash a password."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, password_hash):
    """Verify a password."""
    return hash_password(password) == password_hash


def generate_token():
    """Generate an authentication token."""
    return secrets.token_urlsafe(32)


# Simple token storage (in production, use Redis or JWT)
tokens = {}


def require_auth(f):
    """Decorator to require authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({"error": "Missing authorization header"}), 401
        
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return jsonify({"error": "Invalid authorization header format. Use: Bearer <token>"}), 401
        
        token = parts[1]
        user_id = tokens.get(token)
        
        if not user_id:
            return jsonify({"error": "Invalid or expired token"}), 401
        
        g.user_id = user_id
        g.user = db.get_user_by_id(user_id)
        
        return f(*args, **kwargs)
    return decorated


# =============================================================================
# API ENDPOINTS
# =============================================================================

# Authentication endpoints
@app.route('/api/auth/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    username = data['username']
    password = data['password']
    email = data.get('email')
    
    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400
    
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400
    
    password_hash = hash_password(password)
    user_id = db.create_user(username, password_hash, email)
    
    if not user_id:
        return jsonify({"error": "Username already exists"}), 409
    
    # Generate token for immediate login
    token = generate_token()
    tokens[token] = user_id
    
    return jsonify({
        "user_id": user_id,
        "username": username,
        "token": token,
        "message": "Registration successful"
    }), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login and receive authentication token."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    user = db.get_user_by_username(data['username'])
    
    if not user or not verify_password(data['password'], user['password_hash']):
        return jsonify({"error": "Invalid username or password"}), 401
    
    token = generate_token()
    tokens[token] = user['id']
    
    return jsonify({
        "token": token,
        "user_id": user['id'],
        "username": user['username']
    })


@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout():
    """Logout and invalidate token."""
    auth_header = request.headers.get('Authorization')
    token = auth_header.split()[1]
    
    if token in tokens:
        del tokens[token]
    
    return jsonify({"message": "Logged out successfully"})


# Task endpoints
@app.route('/api/tasks', methods=['GET'])
@require_auth
def get_tasks():
    """Get all tasks for the authenticated user."""
    status = request.args.get('status')
    priority = request.args.get('priority', type=int)
    limit = request.args.get('limit', 100, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    tasks = db.get_tasks(g.user_id, status, priority, limit, offset)
    
    return jsonify({
        "total": len(tasks),
        "tasks": tasks
    })


@app.route('/api/tasks', methods=['POST'])
@require_auth
def create_task():
    """Create a new task."""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    task = db.create_task(
        user_id=g.user_id,
        title=data['title'],
        description=data.get('description'),
        priority=data.get('priority', 2),
        due_date=data.get('due_date'),
        tags=','.join(data.get('tags', [])) if data.get('tags') else None
    )
    
    if not task:
        return jsonify({"error": "Failed to create task"}), 500
    
    return jsonify(task), 201


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
@require_auth
def get_task(task_id):
    """Get a specific task."""
    task = db.get_task(task_id, g.user_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify(task)


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@require_auth
def update_task(task_id):
    """Update a task."""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No update data provided"}), 400
    
    # Parse tags if present
    if 'tags' in data and isinstance(data['tags'], list):
        data['tags'] = ','.join(data['tags'])
    
    task = db.update_task(task_id, g.user_id, data)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify(task)


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
@require_auth
def delete_task(task_id):
    """Delete a task."""
    result = db.delete_task(task_id, g.user_id)
    
    if not result:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify({"message": "Task deleted successfully"})


@app.route('/api/tasks/<int:task_id>/complete', methods=['POST'])
@require_auth
def complete_task(task_id):
    """Mark a task as completed."""
    task = db.complete_task(task_id, g.user_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify(task)


# Statistics endpoint
@app.route('/api/stats', methods=['GET'])
@require_auth
def get_stats():
    """Get task statistics for the user."""
    tasks = db.get_tasks(g.user_id, limit=10000)
    
    stats = {
        "total": len(tasks),
        "completed": sum(1 for t in tasks if t['status'] == 'completed'),
        "pending": sum(1 for t in tasks if t['status'] == 'pending'),
        "in_progress": sum(1 for t in tasks if t['status'] == 'in_progress'),
        "by_priority": {
            "high": sum(1 for t in tasks if t['priority'] == 1 and t['status'] != 'completed'),
            "medium": sum(1 for t in tasks if t['priority'] == 2 and t['status'] != 'completed'),
            "low": sum(1 for t in tasks if t['priority'] == 3 and t['status'] != 'completed')
        },
        "overdue": sum(1 for t in tasks if t['due_date'] and t['due_date'] < datetime.now().isoformat() and t['status'] != 'completed')
    }
    
    return jsonify(stats)


def run_task_api():
    """
    Demonstrate the task management API.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: TASK MANAGEMENT API")
    print("=" * 60)
    
    print("\n1. API ENDPOINTS")
    print("-" * 40)
    
    endpoints = [
        ("POST", "/api/auth/register", "Register new user"),
        ("POST", "/api/auth/login", "Login and get token"),
        ("POST", "/api/auth/logout", "Logout"),
        ("GET", "/api/tasks", "Get all tasks"),
        ("POST", "/api/tasks", "Create task"),
        ("GET", "/api/tasks/<id>", "Get task"),
        ("PUT", "/api/tasks/<id>", "Update task"),
        ("DELETE", "/api/tasks/<id>", "Delete task"),
        ("POST", "/api/tasks/<id>/complete", "Complete task"),
        ("GET", "/api/stats", "Get statistics")
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:8} {path:30} - {description}")
    
    print("\n2. AUTHENTICATION FLOW")
    print("-" * 40)
    
    print("""
    # Register
    curl -X POST http://localhost:5000/api/auth/register \\
         -H "Content-Type: application/json" \\
         -d '{"username": "alice", "password": "secret123", "email": "alice@example.com"}'
    
    # Login
    curl -X POST http://localhost:5000/api/auth/login \\
         -H "Content-Type: application/json" \\
         -d '{"username": "alice", "password": "secret123"}'
    
    # Response:
    {
        "token": "abc123...",
        "user_id": 1,
        "username": "alice"
    }
    
    # Use token for authenticated requests
    curl -X GET http://localhost:5000/api/tasks \\
         -H "Authorization: Bearer abc123..."
    """)
    
    print("\n3. TASK OPERATIONS")
    print("-" * 40)
    
    print("""
    # Create a task
    curl -X POST http://localhost:5000/api/tasks \\
         -H "Authorization: Bearer <token>" \\
         -H "Content-Type: application/json" \\
         -d '{
             "title": "Complete Python Metromap",
             "description": "Finish all 52 stories",
             "priority": 1,
             "due_date": "2024-12-31",
             "tags": ["learning", "python"]
         }'
    
    # Get all tasks
    curl -X GET "http://localhost:5000/api/tasks?status=pending&priority=1" \\
         -H "Authorization: Bearer <token>"
    
    # Complete a task
    curl -X POST http://localhost:5000/api/tasks/1/complete \\
         -H "Authorization: Bearer <token>"
    """)


if __name__ == "__main__":
    run_task_api()
    # Uncomment to run the server:
    # app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 📊 Section 4: Complete API with Documentation

A complete API with OpenAPI/Swagger documentation, rate limiting, and CORS support.

**SOLID Principles Applied:**
- Single Responsibility: Each module handles one cross-cutting concern
- Dependency Inversion: Depends on documentation and rate limiting abstractions

**Design Patterns:**
- Decorator Pattern: Rate limiting as decorator
- Facade Pattern: Documentation provides simplified API view

```python
"""
COMPLETE API WITH DOCUMENTATION

This section builds a complete API with documentation and rate limiting.

SOLID Principles Applied:
- Single Responsibility: Each module handles one cross-cutting concern
- Dependency Inversion: Depends on documentation and rate limiting abstractions

Design Patterns:
- Decorator Pattern: Rate limiting as decorator
- Facade Pattern: Documentation provides simplified API view
"""

from flask import Flask, request, jsonify, render_template_string
from datetime import datetime, timedelta
from functools import wraps
import time
from collections import defaultdict

app = Flask(__name__)


# =============================================================================
# RATE LIMITING
# =============================================================================

class RateLimiter:
    """Rate limiter using token bucket algorithm."""
    
    def __init__(self, requests_per_minute=60):
        self.requests_per_minute = requests_per_minute
        self.bucket_size = requests_per_minute
        self.tokens = defaultdict(float)
        self.last_refill = defaultdict(float)
    
    def allow_request(self, client_id):
        """Check if request is allowed."""
        now = time.time()
        
        # Refill tokens
        time_passed = now - self.last_refill[client_id]
        tokens_to_add = time_passed * (self.requests_per_minute / 60)
        self.tokens[client_id] = min(self.bucket_size, self.tokens[client_id] + tokens_to_add)
        self.last_refill[client_id] = now
        
        # Check if token available
        if self.tokens[client_id] >= 1:
            self.tokens[client_id] -= 1
            return True, self.requests_per_minute
        else:
            return False, self.requests_per_minute


rate_limiter = RateLimiter(requests_per_minute=60)


def rate_limit(f):
    """Decorator to apply rate limiting."""
    @wraps(f)
    def decorated(*args, **kwargs):
        client_id = request.remote_addr
        
        # Also use API key if provided
        api_key = request.headers.get('X-API-Key')
        if api_key:
            client_id = f"{client_id}:{api_key}"
        
        allowed, limit = rate_limiter.allow_request(client_id)
        
        if not allowed:
            return jsonify({
                "error": "Rate limit exceeded",
                "message": f"Maximum {limit} requests per minute",
                "retry_after": 60
            }), 429
        
        return f(*args, **kwargs)
    return decorated


# =============================================================================
# API KEY MANAGEMENT
# =============================================================================

api_keys = {
    "test_key_123": {"name": "Test Application", "rate_limit": 120},
    "demo_key_456": {"name": "Demo App", "rate_limit": 30}
}


def require_api_key(f):
    """Decorator to require API key."""
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        if not api_key or api_key not in api_keys:
            return jsonify({"error": "Invalid or missing API key"}), 401
        
        g.api_key_info = api_keys[api_key]
        return f(*args, **kwargs)
    return decorated


# =============================================================================
# PRODUCT CATALOG API
# =============================================================================

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 29.99, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Keyboard", "price": 89.99, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Monitor", "price": 299.99, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Desk", "price": 399.99, "category": "Furniture", "in_stock": True},
    {"id": 6, "name": "Chair", "price": 199.99, "category": "Furniture", "in_stock": True},
    {"id": 7, "name": "Notebook", "price": 4.99, "category": "Stationery", "in_stock": True},
    {"id": 8, "name": "Pen", "price": 1.99, "category": "Stationery", "in_stock": True}
]


@app.route('/api/products', methods=['GET'])
@rate_limit
def get_products():
    """Get all products with optional filtering."""
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    in_stock = request.args.get('in_stock', type=lambda x: x.lower() == 'true')
    
    result = products.copy()
    
    if category:
        result = [p for p in result if p['category'].lower() == category.lower()]
    
    if min_price:
        result = [p for p in result if p['price'] >= min_price]
    
    if max_price:
        result = [p for p in result if p['price'] <= max_price]
    
    if in_stock is not None:
        result = [p for p in result if p['in_stock'] == in_stock]
    
    return jsonify({
        "total": len(result),
        "products": result,
        "filters": {
            "category": category,
            "min_price": min_price,
            "max_price": max_price,
            "in_stock": in_stock
        }
    })


@app.route('/api/products/<int:product_id>', methods=['GET'])
@rate_limit
def get_product(product_id):
    """Get a single product by ID."""
    product = next((p for p in products if p['id'] == product_id), None)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    return jsonify(product)


@app.route('/api/products/search', methods=['GET'])
@rate_limit
def search_products():
    """Search products by name."""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({"error": "Search query required"}), 400
    
    results = [p for p in products if query.lower() in p['name'].lower()]
    
    return jsonify({
        "query": query,
        "total": len(results),
        "products": results
    })


@app.route('/api/categories', methods=['GET'])
@rate_limit
def get_categories():
    """Get all product categories."""
    categories = list(set(p['category'] for p in products))
    
    return jsonify({
        "total": len(categories),
        "categories": categories
    })


# =============================================================================
# OPENAPI/ SWAGGER DOCUMENTATION
# =============================================================================

OPENAPI_SPEC = {
    "openapi": "3.0.0",
    "info": {
        "title": "Metromap Product API",
        "description": "A comprehensive product catalog API",
        "version": "1.0.0",
        "contact": {
            "name": "Metromap API Support",
            "email": "api@metromap.com"
        }
    },
    "servers": [
        {"url": "http://localhost:5000", "description": "Development server"},
        {"url": "https://api.metromap.com", "description": "Production server"}
    ],
    "paths": {
        "/api/products": {
            "get": {
                "summary": "Get all products",
                "description": "Returns a list of products with optional filtering",
                "parameters": [
                    {"name": "category", "in": "query", "schema": {"type": "string"}},
                    {"name": "min_price", "in": "query", "schema": {"type": "number"}},
                    {"name": "max_price", "in": "query", "schema": {"type": "number"}},
                    {"name": "in_stock", "in": "query", "schema": {"type": "boolean"}}
                ],
                "responses": {"200": {"description": "Successful response"}}
            }
        },
        "/api/products/{id}": {
            "get": {
                "summary": "Get product by ID",
                "parameters": [
                    {"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}
                ],
                "responses": {"200": {"description": "Product found"}, "404": {"description": "Product not found"}}
            }
        },
        "/api/products/search": {
            "get": {
                "summary": "Search products",
                "parameters": [
                    {"name": "q", "in": "query", "required": True, "schema": {"type": "string"}}
                ],
                "responses": {"200": {"description": "Search results"}}
            }
        },
        "/api/categories": {
            "get": {
                "summary": "Get categories",
                "responses": {"200": {"description": "List of categories"}}
            }
        }
    }
}


@app.route('/api/docs')
def api_documentation():
    """Serve OpenAPI documentation."""
    return jsonify(OPENAPI_SPEC)


@app.route('/api/docs/ui')
def api_docs_ui():
    """Serve Swagger UI for API documentation."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Metromap API Documentation</title>
        <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
        <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script>
            window.onload = function() {
                SwaggerUIBundle({
                    url: "/api/docs",
                    dom_id: '#swagger-ui',
                    presets: [
                        SwaggerUIBundle.presets.apis,
                        SwaggerUIBundle.SwaggerUIStandalonePreset
                    ],
                    layout: "BaseLayout"
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)


# =============================================================================
# REQUEST/ RESPONSE LOGGING
# =============================================================================

@app.before_request
def log_request_info():
    """Log incoming requests."""
    if request.method != 'GET':
        print(f"[{datetime.now().isoformat()}] {request.method} {request.path}")
        if request.is_json:
            print(f"  Body: {request.get_json()}")


@app.after_request
def add_cors_headers(response):
    """Add CORS headers to allow cross-origin requests."""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-API-Key'
    return response


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "path": request.path}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500


def run_complete_api():
    """
    Demonstrate the complete API with documentation.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: COMPLETE API WITH DOCUMENTATION")
    print("=" * 60)
    
    print("\n1. API FEATURES")
    print("-" * 40)
    
    features = [
        "✓ Rate limiting (60 requests per minute)",
        "✓ API key authentication",
        "✓ CORS support for cross-origin requests",
        "✓ OpenAPI/Swagger documentation",
        "✓ Request/Response logging",
        "✓ Error handling",
        "✓ Query parameter filtering",
        "✓ Search functionality"
    ]
    
    for feature in features:
        print(f"  {feature}")
    
    print("\n2. API ENDPOINTS")
    print("-" * 40)
    
    endpoints = [
        ("GET", "/api/products", "List all products"),
        ("GET", "/api/products/<id>", "Get product by ID"),
        ("GET", "/api/products/search", "Search products"),
        ("GET", "/api/categories", "List categories"),
        ("GET", "/api/docs", "OpenAPI specification"),
        ("GET", "/api/docs/ui", "Swagger UI documentation")
    ]
    
    for method, path, description in endpoints:
        print(f"  {method:8} {path:30} - {description}")
    
    print("\n3. API USAGE EXAMPLES")
    print("-" * 40)
    
    print("""
    # Get all products
    curl -X GET "http://localhost:5000/api/products" \\
         -H "X-API-Key: test_key_123"
    
    # Filter by category
    curl -X GET "http://localhost:5000/api/products?category=Electronics&in_stock=true" \\
         -H "X-API-Key: test_key_123"
    
    # Search products
    curl -X GET "http://localhost:5000/api/products/search?q=laptop" \\
         -H "X-API-Key: test_key_123"
    
    # Get single product
    curl -X GET "http://localhost:5000/api/products/1" \\
         -H "X-API-Key: test_key_123"
    
    # View API documentation
    open http://localhost:5000/api/docs/ui
    """)
    
    print("\n4. RATE LIMITING DEMONSTRATION")
    print("-" * 40)
    
    print("""
    # Make 61 requests quickly to see rate limiting
    for i in {1..65}; do
        curl -s "http://localhost:5000/api/products" -H "X-API-Key: test_key_123" | grep -q "rate limit" && echo "Rate limit hit at request $i" && break
    done
    
    # Response when rate limited:
    {
        "error": "Rate limit exceeded",
        "message": "Maximum 60 requests per minute",
        "retry_after": 60
    }
    """)


if __name__ == "__main__":
    run_complete_api()
    # Uncomment to run the server:
    # app.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Flask Fundamentals** – `@app.route()` decorator for endpoints. `jsonify()` for JSON responses. `request` object for accessing request data.

- **HTTP Methods** – GET (retrieve), POST (create), PUT (update), DELETE (remove). Different methods for different operations.

- **URL Parameters** – Path parameters (`/<name>`), query parameters (`request.args`), JSON body (`request.get_json()`).

- **URL Shortener** – Generate short codes (random or custom). Store in database with expiration. Redirect with 302. Track analytics (clicks, unique visitors, referrers).

- **Task Management API** – CRUD operations. User authentication with tokens. Password hashing. Task filtering by status, priority.

- **Authentication** – Register, login, logout endpoints. Token-based authentication. Password hashing with SHA256.

- **Rate Limiting** – Token bucket algorithm. Limit requests per client per minute. Return 429 status code when exceeded.

- **API Documentation** – OpenAPI/Swagger specification. Interactive documentation UI. Auto-generated from code.

- **CORS** – Cross-Origin Resource Sharing headers. Allow frontend applications to call API.

- **SOLID Principles Applied** – Single Responsibility (each endpoint handles one resource), Dependency Inversion (depends on storage abstraction), Open/Closed (new endpoints can be added), Interface Segregation (clean API interfaces).

- **Design Patterns Used** – Front Controller Pattern (Flask routing), Repository Pattern (data storage), Decorator Pattern (rate limiting, authentication), DTO Pattern (API responses), Factory Pattern (short code generation), Template Method (database connection management).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Real-World EDA Project

- **📚 Series H Catalog:** Web Development & Automation – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Django – Full-Stack Web Apps (Series H, Story 2)

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
| Series H | 5 | 1 | 4 | 20% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **46** | **6** | **88%** |

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

**Next Story:** Series H, Story 2: The 2026 Python Metromap: Django – Full-Stack Web Apps

---

## 📝 Your Invitation

You've mastered Flask. Now build something with what you've learned:

1. **Build a file upload API** – Create an endpoint that accepts file uploads, validates file types, and stores them.

2. **Create a URL health checker API** – Build an API that checks if URLs are reachable and returns status.

3. **Build a note-taking API** – Create CRUD endpoints for notes with tags and search.

4. **Create a weather API proxy** – Build an API that caches responses from a third-party weather API.

5. **Build a QR code generator API** – Create an endpoint that generates QR codes from URLs or text.

**You've mastered Flask. Next stop: Django!**

---

*Found this helpful? Clap, comment, and share what API you built. Next stop: Django!* 🚇