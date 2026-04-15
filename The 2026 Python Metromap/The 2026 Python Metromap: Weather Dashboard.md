# The 2026 Python Metromap: Weather Dashboard

## Series J: Capstone Projects | Story 2 of 3

![The 2026 Python Metromap/images/Weather Dashboard](images/Weather Dashboard.png)

## 📖 Introduction

**Welcome to the second stop on the Capstone Projects Line.**

You've built a complete CLI expense tracker with OOP, file storage, and data visualization. You've mastered the fundamentals of building real-world applications. Now it's time to step into the world of web development.

This story—**The 2026 Python Metromap: Weather Dashboard**—is your gateway to full-stack web development. You'll build a professional weather dashboard that integrates with real-world APIs, implements caching for performance, creates responsive frontends, and deploys with Docker. You'll learn how to build Flask web applications, work with external APIs, implement Redis caching, create interactive HTML/CSS/JS frontends, and deploy your application to the cloud.

This isn't just a weather app—it's a complete web application that demonstrates API integration, performance optimization, responsive design, and production deployment.

**Let's build your first full-stack web application.**

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

- 🌤️ **The 2026 Python Metromap: Weather Dashboard** – Flask web application; OpenWeatherMap API integration; Redis caching; HTML/CSS/JS frontend. **⬅️ YOU ARE HERE**

- 🎯 **The 2026 Python Metromap: ML-Powered Recommendation Engine** – Full-stack recommendation system with Pandas data processing; Scikit-learn collaborative filtering; Flask API; Docker deployment. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🌐 Section 1: Flask Backend & API Integration

Build the Flask backend with OpenWeatherMap API integration and proper error handling.

**SOLID Principles Applied:**
- Single Responsibility: Each module handles one aspect (API, caching, validation)
- Dependency Inversion: Backend depends on API abstractions
- Open/Closed: New weather providers can be added

**Design Pattern: Facade Pattern** – Simplifies weather API complexity

```python
"""
WEATHER DASHBOARD - SECTION 1: FLASK BACKEND & API INTEGRATION

This section implements the Flask backend with OpenWeatherMap API integration.

SOLID Principles Applied:
- Single Responsibility: Each module handles one aspect (API, caching, validation)
- Dependency Inversion: Backend depends on API abstractions
- Open/Closed: New weather providers can be added

Design Pattern: Facade Pattern - Simplifies weather API complexity
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, asdict
from functools import wraps
from pathlib import Path

import requests
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import redis
from werkzeug.middleware.proxy_fix import ProxyFix

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==================== DATA MODELS ====================

@dataclass
class WeatherData:
    """Represents weather data for a location."""
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    wind_speed: float
    wind_direction: int
    description: str
    icon: str
    sunrise: int
    sunset: int
    timestamp: datetime
    lat: float = 0.0
    lon: float = 0.0
    
    @property
    def temp_celsius(self) -> float:
        """Temperature in Celsius."""
        return self.temperature
    
    @property
    def temp_fahrenheit(self) -> float:
        """Temperature in Fahrenheit."""
        return (self.temperature * 9/5) + 32
    
    @property
    def formatted_sunrise(self) -> str:
        """Formatted sunrise time."""
        return datetime.fromtimestamp(self.sunrise).strftime('%H:%M:%S')
    
    @property
    def formatted_sunset(self) -> str:
        """Formatted sunset time."""
        return datetime.fromtimestamp(self.sunset).strftime('%H:%M:%S')
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data['timestamp'] = self.timestamp.isoformat()
        data['temp_fahrenheit'] = self.temp_fahrenheit
        data['formatted_sunrise'] = self.formatted_sunrise
        data['formatted_sunset'] = self.formatted_sunset
        return data


@dataclass
class ForecastData:
    """Represents weather forecast data."""
    city: str
    country: str
    forecasts: List[Dict[str, Any]]
    timestamp: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'city': self.city,
            'country': self.country,
            'forecasts': self.forecasts,
            'timestamp': self.timestamp.isoformat()
        }


@dataclass
class FavoriteCity:
    """Represents a user's favorite city."""
    city: str
    country: str
    lat: float
    lon: float
    added_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'city': self.city,
            'country': self.country,
            'lat': self.lat,
            'lon': self.lon,
            'added_at': self.added_at.isoformat()
        }


# ==================== WEATHER API SERVICE ====================

class WeatherAPIError(Exception):
    """Custom exception for weather API errors."""
    pass


class WeatherService:
    """
    Service for interacting with weather APIs.
    
    Design Pattern: Facade Pattern - Simplifies API complexity
    SOLID Principle: Single Responsibility - Only handles API calls
    """
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key is required")
        
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.geo_url = "http://api.openweathermap.org/geo/1.0"
        
    def get_current_weather(self, city: str, country_code: str = None) -> WeatherData:
        """
        Get current weather for a city.
        
        Args:
            city: City name
            country_code: Optional two-letter country code
            
        Returns:
            WeatherData object with current conditions
            
        Raises:
            WeatherAPIError: If API request fails
        """
        try:
            # Build query
            query = f"{city}"
            if country_code:
                query += f",{country_code}"
            
            # Make API request
            params = {
                'q': query,
                'appid': self.api_key,
                'units': 'metric'  # Celsius
            }
            
            response = requests.get(f"{self.base_url}/weather", params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Parse response
            weather_data = WeatherData(
                city=data['name'],
                country=data['sys']['country'],
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                humidity=data['main']['humidity'],
                pressure=data['main']['pressure'],
                wind_speed=data['wind']['speed'],
                wind_direction=data['wind'].get('deg', 0),
                description=data['weather'][0]['description'],
                icon=data['weather'][0]['icon'],
                sunrise=data['sys']['sunrise'],
                sunset=data['sys']['sunset'],
                timestamp=datetime.now(),
                lat=data['coord']['lat'],
                lon=data['coord']['lon']
            )
            
            logger.info(f"Retrieved weather for {city}, {country_code}")
            return weather_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise WeatherAPIError(f"Failed to fetch weather data: {str(e)}")
        except KeyError as e:
            logger.error(f"Unexpected API response format: {e}")
            raise WeatherAPIError("Invalid response from weather service")
    
    def get_weather_by_coordinates(self, lat: float, lon: float) -> WeatherData:
        """
        Get current weather by coordinates.
        
        Args:
            lat: Latitude
            lon: Longitude
            
        Returns:
            WeatherData object
        """
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(f"{self.base_url}/weather", params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            weather_data = WeatherData(
                city=data['name'],
                country=data['sys']['country'],
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                humidity=data['main']['humidity'],
                pressure=data['main']['pressure'],
                wind_speed=data['wind']['speed'],
                wind_direction=data['wind'].get('deg', 0),
                description=data['weather'][0]['description'],
                icon=data['weather'][0]['icon'],
                sunrise=data['sys']['sunrise'],
                sunset=data['sys']['sunset'],
                timestamp=datetime.now(),
                lat=lat,
                lon=lon
            )
            
            return weather_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise WeatherAPIError(f"Failed to fetch weather data: {str(e)}")
    
    def get_forecast(self, city: str, country_code: str = None, days: int = 5) -> ForecastData:
        """
        Get weather forecast for a city.
        
        Args:
            city: City name
            country_code: Optional country code
            days: Number of days for forecast (1-5)
            
        Returns:
            ForecastData with 3-hour interval forecasts
        """
        try:
            # Build query
            query = f"{city}"
            if country_code:
                query += f",{country_code}"
            
            params = {
                'q': query,
                'appid': self.api_key,
                'units': 'metric',
                'cnt': min(days * 8, 40)  # 8 readings per day (3-hour intervals)
            }
            
            response = requests.get(f"{self.base_url}/forecast", params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Process forecast data
            forecasts = []
            for item in data['list'][:days * 8]:
                forecast = {
                    'datetime': datetime.fromtimestamp(item['dt']),
                    'temperature': item['main']['temp'],
                    'feels_like': item['main']['feels_like'],
                    'humidity': item['main']['humidity'],
                    'pressure': item['main']['pressure'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                    'wind_speed': item['wind']['speed'],
                    'pop': item.get('pop', 0) * 100  # Probability of precipitation
                }
                forecasts.append(forecast)
            
            forecast_data = ForecastData(
                city=data['city']['name'],
                country=data['city']['country'],
                forecasts=forecasts,
                timestamp=datetime.now()
            )
            
            logger.info(f"Retrieved forecast for {city} ({days} days)")
            return forecast_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Forecast API request failed: {e}")
            raise WeatherAPIError(f"Failed to fetch forecast: {str(e)}")
    
    def search_cities(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for cities by name.
        
        Args:
            query: City name search query
            limit: Maximum number of results
            
        Returns:
            List of city suggestions with coordinates
        """
        try:
            params = {
                'q': query,
                'limit': limit,
                'appid': self.api_key
            }
            
            response = requests.get(f"{self.geo_url}/direct", params=params, timeout=10)
            response.raise_for_status()
            
            cities = []
            for city in response.json():
                cities.append({
                    'name': city['name'],
                    'country': city['country'],
                    'lat': city['lat'],
                    'lon': city['lon'],
                    'state': city.get('state', '')
                })
            
            return cities
            
        except requests.exceptions.RequestException as e:
            logger.error(f"City search failed: {e}")
            return []


# ==================== CACHING SERVICE ====================

class CacheService:
    """
    Service for caching weather data.
    
    Design Pattern: Proxy Pattern - Adds caching layer to API calls
    SOLID Principle: Single Responsibility - Only handles caching logic
    """
    
    def __init__(self, redis_url: str = None, default_ttl: int = 300):
        """
        Initialize cache service.
        
        Args:
            redis_url: Redis connection URL
            default_ttl: Default cache TTL in seconds (5 minutes)
        """
        self.default_ttl = default_ttl
        self.redis_client = None
        
        # Try to connect to Redis
        redis_url = redis_url or os.getenv('REDIS_URL', 'redis://localhost:6379/0')
        try:
            self.redis_client = redis.from_url(redis_url)
            self.redis_client.ping()
            logger.info("Redis cache connected successfully")
        except Exception as e:
            logger.warning(f"Redis connection failed, using memory cache: {e}")
            self.redis_client = None
    
    def _get_key(self, prefix: str, identifier: str) -> str:
        """Generate cache key."""
        return f"weather:{prefix}:{identifier}"
    
    def get_weather(self, city: str, country: str = None) -> Optional[WeatherData]:
        """Get cached weather data."""
        if not self.redis_client:
            return None
        
        key = self._get_key('current', f"{city}_{country or ''}")
        try:
            cached = self.redis_client.get(key)
            if cached:
                data = json.loads(cached)
                logger.info(f"Cache hit for {city}")
                return WeatherData(**data)
        except Exception as e:
            logger.error(f"Cache read error: {e}")
        
        return None
    
    def set_weather(self, city: str, weather_data: WeatherData, ttl: int = None) -> bool:
        """Cache weather data."""
        if not self.redis_client:
            return False
        
        key = self._get_key('current', f"{city}_{weather_data.country}")
        ttl = ttl or self.default_ttl
        
        try:
            self.redis_client.setex(
                key,
                ttl,
                json.dumps(weather_data.to_dict(), default=str)
            )
            logger.info(f"Cached weather for {city} (TTL: {ttl}s)")
            return True
        except Exception as e:
            logger.error(f"Cache write error: {e}")
            return False
    
    def get_forecast(self, city: str, country: str = None, days: int = 5) -> Optional[ForecastData]:
        """Get cached forecast data."""
        if not self.redis_client:
            return None
        
        key = self._get_key('forecast', f"{city}_{country or ''}_{days}")
        try:
            cached = self.redis_client.get(key)
            if cached:
                data = json.loads(cached)
                logger.info(f"Cache hit for forecast {city}")
                return ForecastData(**data)
        except Exception as e:
            logger.error(f"Cache read error: {e}")
        
        return None
    
    def set_forecast(self, city: str, forecast_data: ForecastData, days: int = 5, ttl: int = None) -> bool:
        """Cache forecast data."""
        if not self.redis_client:
            return False
        
        key = self._get_key('forecast', f"{city}_{forecast_data.country}_{days}")
        ttl = ttl or (self.default_ttl * 2)  # Forecast cached longer
        
        try:
            self.redis_client.setex(
                key,
                ttl,
                json.dumps(forecast_data.to_dict(), default=str)
            )
            logger.info(f"Cached forecast for {city} (TTL: {ttl}s)")
            return True
        except Exception as e:
            logger.error(f"Cache write error: {e}")
            return False
    
    def clear_city_cache(self, city: str) -> bool:
        """Clear cache for a specific city."""
        if not self.redis_client:
            return False
        
        try:
            pattern = self._get_key('*', f"{city}_*")
            keys = self.redis_client.keys(pattern)
            if keys:
                self.redis_client.delete(*keys)
                logger.info(f"Cleared cache for {city} ({len(keys)} keys)")
            return True
        except Exception as e:
            logger.error(f"Cache clear error: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        if not self.redis_client:
            return {'status': 'disabled', 'message': 'Redis not connected'}
        
        try:
            info = self.redis_client.info()
            return {
                'status': 'connected',
                'used_memory': info.get('used_memory_human', 'N/A'),
                'total_keys': self.redis_client.dbsize(),
                'hit_rate': 'N/A'  # Would need additional tracking
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}


# ==================== FLASK APPLICATION ====================

def create_app(config: Dict[str, Any] = None) -> Flask:
    """
    Application factory for Flask.
    
    Design Pattern: Factory Pattern - Creates configured Flask app
    SOLID Principle: Single Responsibility - Only creates and configures app
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
    
    # Apply custom config
    if config:
        app.config.update(config)
    
    # Initialize services
    app.weather_service = WeatherService()
    app.cache_service = CacheService()
    
    # Setup rate limiting
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"]
    )
    
    # Setup proxy fix for running behind reverse proxy
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    
    # Register blueprints
    from weather_dashboard.routes import main_bp, api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal server error: {error}")
        return jsonify({'error': 'Internal server error'}), 500
    
    @app.errorhandler(WeatherAPIError)
    def weather_api_error(error):
        logger.error(f"Weather API error: {error}")
        return jsonify({'error': str(error)}), 502
    
    logger.info("Weather Dashboard application initialized")
    return app


# ==================== ROUTES ====================

# Create blueprints for routes
from flask import Blueprint

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')


@main_bp.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')


@main_bp.route('/weather')
def weather_page():
    """Render weather page for a specific city."""
    city = request.args.get('city', '')
    if not city:
        return redirect(url_for('main.index'))
    
    return render_template('weather.html', city=city)


@api_bp.route('/weather/current')
@limiter.limit("30 per minute")
def get_current_weather():
    """
    API endpoint for current weather.
    
    Query parameters:
        city: City name
        country: Optional country code
        lat: Latitude (alternative to city)
        lon: Longitude (alternative to city)
    """
    city = request.args.get('city')
    country = request.args.get('country')
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    # Validate input
    if not city and not (lat and lon):
        return jsonify({'error': 'City name or coordinates required'}), 400
    
    try:
        # Try to get from cache first
        weather_service = current_app.weather_service
        cache_service = current_app.cache_service
        
        weather_data = None
        
        if city:
            # Check cache
            weather_data = cache_service.get_weather(city, country)
            
            if not weather_data:
                # Fetch from API
                weather_data = weather_service.get_current_weather(city, country)
                # Cache for 5 minutes
                cache_service.set_weather(city, weather_data, ttl=300)
        else:
            # Fetch by coordinates
            weather_data = weather_service.get_weather_by_coordinates(lat, lon)
        
        return jsonify({
            'success': True,
            'data': weather_data.to_dict()
        })
        
    except WeatherAPIError as e:
        return jsonify({'success': False, 'error': str(e)}), 502
    except Exception as e:
        logger.error(f"Unexpected error in weather endpoint: {e}")
        return jsonify({'success': False, 'error': 'Internal server error'}), 500


@api_bp.route('/weather/forecast')
@limiter.limit("30 per minute")
def get_weather_forecast():
    """
    API endpoint for weather forecast.
    
    Query parameters:
        city: City name
        country: Optional country code
        days: Number of days (1-5)
    """
    city = request.args.get('city')
    country = request.args.get('country')
    days = min(int(request.args.get('days', 5)), 5)
    
    if not city:
        return jsonify({'error': 'City name required'}), 400
    
    try:
        weather_service = current_app.weather_service
        cache_service = current_app.cache_service
        
        # Try cache
        forecast = cache_service.get_forecast(city, country, days)
        
        if not forecast:
            # Fetch from API
            forecast = weather_service.get_forecast(city, country, days)
            # Cache for 10 minutes
            cache_service.set_forecast(city, forecast, days, ttl=600)
        
        return jsonify({
            'success': True,
            'data': forecast.to_dict()
        })
        
    except WeatherAPIError as e:
        return jsonify({'success': False, 'error': str(e)}), 502
    except Exception as e:
        logger.error(f"Unexpected error in forecast endpoint: {e}")
        return jsonify({'success': False, 'error': 'Internal server error'}), 500


@api_bp.route('/cities/search')
def search_cities():
    """Search for cities by name."""
    query = request.args.get('q', '')
    limit = min(int(request.args.get('limit', 5)), 10)
    
    if not query or len(query) < 2:
        return jsonify({'success': True, 'data': []})
    
    try:
        weather_service = current_app.weather_service
        cities = weather_service.search_cities(query, limit)
        
        return jsonify({
            'success': True,
            'data': cities
        })
        
    except Exception as e:
        logger.error(f"City search error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/favorites', methods=['GET', 'POST', 'DELETE'])
def manage_favorites():
    """
    Manage favorite cities.
    
    GET: List favorites
    POST: Add favorite
    DELETE: Remove favorite
    """
    # In production, this would use a database
    # For demo, using session storage
    if 'favorites' not in session:
        session['favorites'] = []
    
    if request.method == 'GET':
        return jsonify({
            'success': True,
            'data': session['favorites']
        })
    
    elif request.method == 'POST':
        data = request.get_json()
        city = data.get('city')
        
        if not city:
            return jsonify({'error': 'City name required'}), 400
        
        # Check if already in favorites
        if city not in session['favorites']:
            session['favorites'].append(city)
            session.modified = True
        
        return jsonify({
            'success': True,
            'data': session['favorites']
        })
    
    elif request.method == 'DELETE':
        city = request.args.get('city')
        
        if city and city in session['favorites']:
            session['favorites'].remove(city)
            session.modified = True
        
        return jsonify({
            'success': True,
            'data': session['favorites']
        })


@api_bp.route('/cache/stats')
def cache_stats():
    """Get cache statistics."""
    cache_service = current_app.cache_service
    stats = cache_service.get_stats()
    
    return jsonify({
        'success': True,
        'data': stats
    })


@api_bp.route('/cache/clear/<city>', methods=['DELETE'])
def clear_city_cache(city):
    """Clear cache for a specific city."""
    cache_service = current_app.cache_service
    
    if cache_service.clear_city_cache(city):
        return jsonify({'success': True, 'message': f'Cache cleared for {city}'})
    else:
        return jsonify({'success': False, 'message': 'Failed to clear cache'}), 500


# Helper to access current_app in routes
from flask import current_app

def demonstrate_backend():
    """
    Demonstrate the backend functionality.
    """
    print("\n" + "=" * 60)
    print("SECTION 1: FLASK BACKEND & API INTEGRATION")
    print("=" * 60)
    
    # Test API key
    print("\n1. TESTING API CONNECTION")
    print("-" * 40)
    
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print_warning("No API key found. Set OPENWEATHER_API_KEY environment variable")
        print_info("Get a free API key from: https://openweathermap.org/api")
        return
    
    try:
        weather_service = WeatherService(api_key)
        print_success("Weather service initialized successfully")
    except ValueError as e:
        print_error(f"Failed to initialize: {e}")
        return
    
    # Test weather lookup
    print("\n2. TESTING WEATHER LOOKUP")
    print("-" * 40)
    
    test_cities = ["London", "New York", "Tokyo"]
    
    for city in test_cities:
        try:
            weather = weather_service.get_current_weather(city)
            print(f"\n  {city}, {weather.country}:")
            print(f"    Temperature: {weather.temperature}°C ({weather.temp_fahrenheit:.1f}°F)")
            print(f"    Conditions: {weather.description}")
            print(f"    Humidity: {weather.humidity}%")
            print(f"    Wind: {weather.wind_speed} m/s")
        except WeatherAPIError as e:
            print_error(f"  Failed to get weather for {city}: {e}")
    
    # Test forecast
    print("\n3. TESTING FORECAST")
    print("-" * 40)
    
    try:
        forecast = weather_service.get_forecast("London", days=3)
        print(f"\n  3-day forecast for {forecast.city}, {forecast.country}:")
        print(f"  Total forecasts: {len(forecast.forecasts)}")
        
        # Show daily summary
        daily_temps = {}
        for f in forecast.forecasts:
            day = f['datetime'].strftime('%Y-%m-%d')
            if day not in daily_temps:
                daily_temps[day] = []
            daily_temps[day].append(f['temperature'])
        
        for day, temps in list(daily_temps.items())[:3]:
            avg_temp = sum(temps) / len(temps)
            print(f"    {day}: {avg_temp:.1f}°C (avg)")
            
    except WeatherAPIError as e:
        print_error(f"Failed to get forecast: {e}")
    
    # Test city search
    print("\n4. TESTING CITY SEARCH")
    print("-" * 40)
    
    search_queries = ["Paris", "San Francisco", "Sydney"]
    
    for query in search_queries:
        cities = weather_service.search_cities(query, limit=3)
        print(f"\n  Results for '{query}':")
        for city in cities:
            print(f"    {city['name']}, {city['country']} "
                  f"({city['lat']:.2f}, {city['lon']:.2f})")
    
    # Test caching
    print("\n5. TESTING CACHE")
    print("-" * 40)
    
    cache_service = CacheService()
    stats = cache_service.get_stats()
    print(f"  Cache status: {stats['status']}")
    
    if stats['status'] == 'connected':
        print(f"  Redis memory: {stats['used_memory']}")
        print(f"  Total keys: {stats['total_keys']}")
    
    # Flask app creation
    print("\n6. FLASK APPLICATION")
    print("-" * 40)
    
    app = create_app()
    print(f"  App name: {app.name}")
    print(f"  Secret key set: {bool(app.config['SECRET_KEY'])}")
    print(f"  Debug mode: {app.debug}")
    
    print("\n  Registered routes:")
    for rule in app.url_map.iter_rules():
        if not rule.rule.startswith('/static'):
            print(f"    {rule.methods} {rule.rule}")
    
    print("\n✅ Backend setup complete!")
    print_info("To run the server: python app.py")
    print_info("Or use: flask run --host=0.0.0.0 --port=5000")


# Helper functions for colored output (for testing)
def print_success(text):
    print(f"\033[92m✓ {text}\033[0m")

def print_error(text):
    print(f"\033[91m✗ {text}\033[0m")

def print_warning(text):
    print(f"\033[93m⚠ {text}\033[0m")

def print_info(text):
    print(f"\033[94mℹ {text}\033[0m")


if __name__ == "__main__":
    demonstrate_backend()
    
    # Run the Flask app if executed directly
    if os.getenv('RUN_APP', 'False').lower() == 'true':
        app = create_app()
        app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## 🎨 Section 2: Responsive Frontend with HTML/CSS/JS

Build a beautiful, responsive frontend with modern HTML5, CSS3, and vanilla JavaScript.

**SOLID Principles Applied:**
- Single Responsibility: Separation of HTML (structure), CSS (presentation), JS (behavior)
- Open/Closed: Easy to add new UI components

**Design Pattern: Observer Pattern** – Event listeners for user interactions

```html
<!-- WEATHER DASHBOARD - SECTION 2: FRONTEND TEMPLATES -->
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <meta name="description" content="Real-time weather dashboard with forecasts and interactive maps">
    <title>{% block title %}Weather Dashboard{% endblock %}</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='favicon.ico') }}">
    
    <!-- CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">
                <i class="fas fa-cloud-sun"></i>
                <span>Weather<span class="brand-highlight">Dashboard</span></span>
            </div>
            
            <div class="nav-search">
                <form id="search-form" class="search-form">
                    <input type="text" 
                           id="city-search" 
                           placeholder="Search city..." 
                           autocomplete="off"
                           class="search-input">
                    <button type="submit" class="search-btn">
                        <i class="fas fa-search"></i>
                    </button>
                    <div id="search-suggestions" class="search-suggestions"></div>
                </form>
            </div>
            
            <div class="nav-menu">
                <button class="nav-btn" id="refresh-btn" title="Refresh">
                    <i class="fas fa-sync-alt"></i>
                </button>
                <button class="nav-btn" id="favorites-btn" title="Favorites">
                    <i class="fas fa-star"></i>
                </button>
                <button class="nav-btn" id="settings-btn" title="Settings">
                    <i class="fas fa-cog"></i>
                </button>
            </div>
        </div>
    </nav>
    
    <!-- Main Content -->
    <main class="main-content">
        {% block content %}{% endblock %}
    </main>
    
    <!-- Favorites Sidebar -->
    <div id="favorites-sidebar" class="sidebar">
        <div class="sidebar-header">
            <h3><i class="fas fa-star"></i> Favorite Cities</h3>
            <button class="close-sidebar">&times;</button>
        </div>
        <div id="favorites-list" class="favorites-list">
            <!-- Favorites will be loaded here -->
        </div>
    </div>
    
    <!-- Settings Modal -->
    <div id="settings-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Settings</h3>
                <button class="close-modal">&times;</button>
            </div>
            <div class="modal-body">
                <div class="setting-group">
                    <label for="temp-unit">Temperature Unit</label>
                    <select id="temp-unit">
                        <option value="celsius">Celsius (°C)</option>
                        <option value="fahrenheit">Fahrenheit (°F)</option>
                    </select>
                </div>
                <div class="setting-group">
                    <label for="default-city">Default City</label>
                    <input type="text" id="default-city" placeholder="Enter default city">
                </div>
                <div class="setting-group">
                    <label>
                        <input type="checkbox" id="auto-refresh"> Auto-refresh every 5 minutes
                    </label>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn-secondary" id="cancel-settings">Cancel</button>
                <button class="btn-primary" id="save-settings">Save</button>
            </div>
        </div>
    </div>
    
    <!-- Loading Overlay -->
    <div id="loading-overlay" class="loading-overlay" style="display: none;">
        <div class="spinner"></div>
        <p>Loading weather data...</p>
    </div>
    
    <!-- JavaScript -->
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Weather Dashboard - Home{% endblock %}

{% block content %}
<div class="container">
    <!-- Hero Section -->
    <div class="hero-section">
        <h1 class="hero-title">
            <i class="fas fa-cloud-sun-rain"></i>
            Weather Dashboard
        </h1>
        <p class="hero-subtitle">Real-time weather data for cities worldwide</p>
        
        <div class="hero-search">
            <form id="hero-search-form">
                <input type="text" 
                       id="hero-city-input" 
                       placeholder="Enter city name (e.g., London, New York, Tokyo)"
                       class="hero-search-input">
                <button type="submit" class="hero-search-btn">
                    <i class="fas fa-arrow-right"></i> Get Weather
                </button>
            </form>
        </div>
    </div>
    
    <!-- Popular Cities Section -->
    <div class="popular-cities">
        <h2 class="section-title">
            <i class="fas fa-globe-americas"></i>
            Popular Cities
        </h2>
        <div class="cities-grid" id="popular-cities-grid">
            <!-- Popular cities will be loaded here -->
        </div>
    </div>
    
    <!-- Recent Searches Section -->
    <div class="recent-searches" id="recent-searches" style="display: none;">
        <h2 class="section-title">
            <i class="fas fa-history"></i>
            Recent Searches
        </h2>
        <div class="recent-list" id="recent-list"></div>
    </div>
    
    <!-- Weather Tips Section -->
    <div class="weather-tips">
        <h2 class="section-title">
            <i class="fas fa-lightbulb"></i>
            Weather Tips
        </h2>
        <div class="tips-grid">
            <div class="tip-card">
                <i class="fas fa-umbrella"></i>
                <h3>Rainy Days</h3>
                <p>Always carry an umbrella when rain probability exceeds 30%</p>
            </div>
            <div class="tip-card">
                <i class="fas fa-temperature-high"></i>
                <h3>Hot Weather</h3>
                <p>Stay hydrated and avoid outdoor activities during peak sun hours (11 AM - 3 PM)</p>
            </div>
            <div class="tip-card">
                <i class="fas fa-snowflake"></i>
                <h3>Cold Weather</h3>
                <p>Layer your clothing and protect extremities from frostbite</p>
            </div>
            <div class="tip-card">
                <i class="fas fa-wind"></i>
                <h3>Strong Winds</h3>
                <p>Secure outdoor objects and avoid walking near trees or buildings</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
    // Load popular cities on page load
    document.addEventListener('DOMContentLoaded', () => {
        loadPopularCities();
        loadRecentSearches();
    });
    
    async function loadPopularCities() {
        const popularCities = [
            'London,UK', 'New York,US', 'Tokyo,JP', 
            'Paris,FR', 'Sydney,AU', 'Cape Town,ZA'
        ];
        
        const grid = document.getElementById('popular-cities-grid');
        grid.innerHTML = '<div class="loading-spinner"><i class="fas fa-spinner fa-spin"></i> Loading...</div>';
        
        const weatherPromises = popularCities.map(city => {
            const [name, country] = city.split(',');
            return fetch(`/api/weather/current?city=${name}&country=${country}`)
                .then(res => res.json());
        });
        
        const results = await Promise.allSettled(weatherPromises);
        
        grid.innerHTML = '';
        results.forEach((result, index) => {
            if (result.status === 'fulfilled' && result.value.success) {
                const weather = result.value.data;
                const card = createWeatherCard(weather);
                grid.appendChild(card);
            } else {
                console.error(`Failed to load weather for ${popularCities[index]}`);
            }
        });
    }
    
    function createWeatherCard(weather) {
        const card = document.createElement('div');
        card.className = 'city-card';
        card.onclick = () => {
            window.location.href = `/weather?city=${weather.city}`;
        };
        
        const temp = weather.temperature;
        const icon = getWeatherIcon(weather.icon);
        
        card.innerHTML = `
            <div class="city-card-header">
                <h3>${weather.city}, ${weather.country}</h3>
                <i class="fas ${icon}"></i>
            </div>
            <div class="city-card-temp">
                ${temp}°C
            </div>
            <div class="city-card-desc">
                ${weather.description}
            </div>
            <div class="city-card-details">
                <span><i class="fas fa-tint"></i> ${weather.humidity}%</span>
                <span><i class="fas fa-wind"></i> ${weather.wind_speed} m/s</span>
            </div>
        `;
        
        return card;
    }
    
    function getWeatherIcon(iconCode) {
        const iconMap = {
            '01d': 'fa-sun',
            '01n': 'fa-moon',
            '02d': 'fa-cloud-sun',
            '02n': 'fa-cloud-moon',
            '03d': 'fa-cloud',
            '03n': 'fa-cloud',
            '04d': 'fa-cloud',
            '04n': 'fa-cloud',
            '09d': 'fa-cloud-rain',
            '09n': 'fa-cloud-rain',
            '10d': 'fa-cloud-sun-rain',
            '10n': 'fa-cloud-moon-rain',
            '11d': 'fa-bolt',
            '11n': 'fa-bolt',
            '13d': 'fa-snowflake',
            '13n': 'fa-snowflake',
            '50d': 'fa-smog',
            '50n': 'fa-smog'
        };
        return iconMap[iconCode] || 'fa-cloud';
    }
    
    function loadRecentSearches() {
        const recent = JSON.parse(localStorage.getItem('recentSearches') || '[]');
        if (recent.length > 0) {
            const section = document.getElementById('recent-searches');
            const list = document.getElementById('recent-list');
            section.style.display = 'block';
            list.innerHTML = recent.map(city => `
                <div class="recent-item" onclick="window.location.href='/weather?city=${city}'">
                    <i class="fas fa-history"></i>
                    <span>${city}</span>
                </div>
            `).join('');
        }
    }
    
    // Hero search form
    document.getElementById('hero-search-form')?.addEventListener('submit', (e) => {
        e.preventDefault();
        const city = document.getElementById('hero-city-input').value.trim();
        if (city) {
            // Save to recent searches
            let recent = JSON.parse(localStorage.getItem('recentSearches') || '[]');
            recent = [city, ...recent.filter(c => c !== city)].slice(0, 10);
            localStorage.setItem('recentSearches', JSON.stringify(recent));
            window.location.href = `/weather?city=${encodeURIComponent(city)}`;
        }
    });
</script>
{% endblock %}
```

```html
<!-- templates/weather.html -->
{% extends "base.html" %}

{% block title %}Weather Dashboard - {{ city }}{% endblock %}

{% block content %}
<div class="weather-container">
    <div class="weather-header">
        <button class="back-btn" onclick="history.back()">
            <i class="fas fa-arrow-left"></i> Back
        </button>
        <button class="favorite-btn" id="favorite-toggle">
            <i class="far fa-star"></i> Add to Favorites
        </button>
    </div>
    
    <!-- Current Weather -->
    <div class="current-weather" id="current-weather">
        <div class="loading-state">
            <i class="fas fa-spinner fa-spin"></i>
            <p>Loading weather data...</p>
        </div>
    </div>
    
    <!-- Forecast Section -->
    <div class="forecast-section">
        <h2 class="section-title">
            <i class="fas fa-calendar-week"></i>
            5-Day Forecast
        </h2>
        <div class="forecast-grid" id="forecast-grid">
            <div class="loading-state">
                <i class="fas fa-spinner fa-spin"></i>
                <p>Loading forecast...</p>
            </div>
        </div>
    </div>
    
    <!-- Hourly Forecast -->
    <div class="hourly-section">
        <h2 class="section-title">
            <i class="fas fa-clock"></i>
            Hourly Forecast (Next 24 Hours)
        </h2>
        <div class="hourly-scroll" id="hourly-forecast">
            <div class="loading-state">
                <i class="fas fa-spinner fa-spin"></i>
                <p>Loading hourly data...</p>
            </div>
        </div>
    </div>
    
    <!-- Additional Details -->
    <div class="details-section">
        <h2 class="section-title">
            <i class="fas fa-info-circle"></i>
            Detailed Information
        </h2>
        <div class="details-grid" id="weather-details">
            <!-- Details will be populated -->
        </div>
    </div>
</div>

<script>
    const city = "{{ city }}";
    let currentWeather = null;
    let forecastData = null;
    
    document.addEventListener('DOMContentLoaded', () => {
        loadWeatherData();
        loadForecastData();
        checkFavoriteStatus();
        
        // Favorite toggle
        document.getElementById('favorite-toggle')?.addEventListener('click', toggleFavorite);
        
        // Refresh button
        document.getElementById('refresh-btn')?.addEventListener('click', () => {
            loadWeatherData(true);
            loadForecastData(true);
        });
    });
    
    async function loadWeatherData(forceRefresh = false) {
        const container = document.getElementById('current-weather');
        container.innerHTML = '<div class="loading-state"><i class="fas fa-spinner fa-spin"></i><p>Loading weather data...</p></div>';
        
        try {
            const url = `/api/weather/current?city=${encodeURIComponent(city)}${forceRefresh ? '&_=' + Date.now() : ''}`;
            const response = await fetch(url);
            const data = await response.json();
            
            if (data.success) {
                currentWeather = data.data;
                displayCurrentWeather(currentWeather);
            } else {
                container.innerHTML = `<div class="error-state"><i class="fas fa-exclamation-triangle"></i><p>${data.error}</p></div>`;
            }
        } catch (error) {
            console.error('Failed to load weather:', error);
            container.innerHTML = '<div class="error-state"><i class="fas fa-exclamation-triangle"></i><p>Failed to load weather data</p></div>';
        }
    }
    
    function displayCurrentWeather(weather) {
        const container = document.getElementById('current-weather');
        const tempUnit = localStorage.getItem('tempUnit') || 'celsius';
        const temperature = tempUnit === 'celsius' ? weather.temperature : weather.temp_fahrenheit;
        const tempSymbol = tempUnit === 'celsius' ? '°C' : '°F';
        
        const icon = getWeatherIcon(weather.icon);
        
        container.innerHTML = `
            <div class="weather-main-card">
                <div class="weather-location">
                    <h1>${weather.city}, ${weather.country}</h1>
                    <p class="weather-time">Updated: ${new Date(weather.timestamp).toLocaleString()}</p>
                </div>
                
                <div class="weather-primary">
                    <div class="weather-icon">
                        <i class="fas ${icon} fa-5x"></i>
                    </div>
                    <div class="weather-temp">
                        <span class="temp-value">${Math.round(temperature)}</span>
                        <span class="temp-unit">${tempSymbol}</span>
                    </div>
                    <div class="weather-desc">
                        ${weather.description}
                        <span class="feels-like">Feels like ${Math.round(tempUnit === 'celsius' ? weather.feels_like : (weather.feels_like * 9/5 + 32))}${tempSymbol}</span>
                    </div>
                </div>
                
                <div class="weather-details-grid">
                    <div class="detail-item">
                        <i class="fas fa-tint"></i>
                        <span>Humidity</span>
                        <strong>${weather.humidity}%</strong>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-wind"></i>
                        <span>Wind Speed</span>
                        <strong>${weather.wind_speed} m/s</strong>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-gauge-high"></i>
                        <span>Pressure</span>
                        <strong>${weather.pressure} hPa</strong>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-sun"></i>
                        <span>Sunrise</span>
                        <strong>${weather.formatted_sunrise}</strong>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-moon"></i>
                        <span>Sunset</span>
                        <strong>${weather.formatted_sunset}</strong>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-compass"></i>
                        <span>Wind Direction</span>
                        <strong>${weather.wind_direction}°</strong>
                    </div>
                </div>
            </div>
        `;
    }
    
    async function loadForecastData(forceRefresh = false) {
        try {
            const url = `/api/weather/forecast?city=${encodeURIComponent(city)}&days=5${forceRefresh ? '&_=' + Date.now() : ''}`;
            const response = await fetch(url);
            const data = await response.json();
            
            if (data.success) {
                forecastData = data.data;
                displayForecast(forecastData);
                displayHourlyForecast(forecastData);
                displayDetails(forecastData);
            } else {
                console.error('Failed to load forecast:', data.error);
            }
        } catch (error) {
            console.error('Failed to load forecast:', error);
        }
    }
    
    function displayForecast(forecast) {
        const grid = document.getElementById('forecast-grid');
        
        // Group forecasts by day
        const dailyForecasts = {};
        forecast.forecasts.forEach(f => {
            const date = new Date(f.datetime).toLocaleDateString();
            if (!dailyForecasts[date]) {
                dailyForecasts[date] = {
                    temps: [],
                    descriptions: [],
                    icons: [],
                    humidity: [],
                    pops: []
                };
            }
            dailyForecasts[date].temps.push(f.temperature);
            dailyForecasts[date].descriptions.push(f.description);
            dailyForecasts[date].icons.push(f.icon);
            dailyForecasts[date].humidity.push(f.humidity);
            dailyForecasts[date].pops.push(f.pop);
        });
        
        // Calculate daily averages
        const dailyData = Object.entries(dailyForecasts).map(([date, data]) => {
            const avgTemp = data.temps.reduce((a, b) => a + b, 0) / data.temps.length;
            const mostCommonDesc = data.descriptions.sort((a, b) =>
                data.descriptions.filter(v => v === a).length - data.descriptions.filter(v => v === b).length
            ).pop();
            const mostCommonIcon = data.icons.sort((a, b) =>
                data.icons.filter(v => v === a).length - data.icons.filter(v => v === b).length
            ).pop();
            const avgHumidity = data.humidity.reduce((a, b) => a + b, 0) / data.humidity.length;
            const maxPop = Math.max(...data.pops);
            
            return { date, avgTemp, mostCommonDesc, mostCommonIcon, avgHumidity, maxPop };
        }).slice(0, 5);
        
        const tempUnit = localStorage.getItem('tempUnit') || 'celsius';
        
        grid.innerHTML = dailyData.map(day => {
            const temp = tempUnit === 'celsius' ? day.avgTemp : (day.avgTemp * 9/5 + 32);
            const icon = getWeatherIcon(day.mostCommonIcon);
            const date = new Date(day.date);
            const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
            
            return `
                <div class="forecast-card">
                    <div class="forecast-day">${dayName}</div>
                    <div class="forecast-date">${date.toLocaleDateString()}</div>
                    <i class="fas ${icon} fa-3x"></i>
                    <div class="forecast-temp">${Math.round(temp)}°${tempUnit === 'celsius' ? 'C' : 'F'}</div>
                    <div class="forecast-desc">${day.mostCommonDesc}</div>
                    <div class="forecast-details">
                        <span><i class="fas fa-tint"></i> ${Math.round(day.avgHumidity)}%</span>
                        <span><i class="fas fa-cloud-rain"></i> ${Math.round(day.maxPop)}%</span>
                    </div>
                </div>
            `;
        }).join('');
    }
    
    function displayHourlyForecast(forecast) {
        const container = document.getElementById('hourly-forecast');
        const next24Hours = forecast.forecasts.slice(0, 8); // 8 * 3 = 24 hours
        const tempUnit = localStorage.getItem('tempUnit') || 'celsius';
        
        container.innerHTML = next24Hours.map(f => {
            const temp = tempUnit === 'celsius' ? f.temperature : (f.temperature * 9/5 + 32);
            const time = new Date(f.datetime).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            const icon = getWeatherIcon(f.icon);
            
            return `
                <div class="hourly-card">
                    <div class="hourly-time">${time}</div>
                    <i class="fas ${icon} fa-2x"></i>
                    <div class="hourly-temp">${Math.round(temp)}°</div>
                    <div class="hourly-desc">${f.description}</div>
                    <div class="hourly-rain">
                        <i class="fas fa-cloud-rain"></i> ${Math.round(f.pop)}%
                    </div>
                </div>
            `;
        }).join('');
    }
    
    function displayDetails(forecast) {
        const container = document.getElementById('weather-details');
        
        // Calculate additional metrics
        const allTemps = forecast.forecasts.map(f => f.temperature);
        const maxTemp = Math.max(...allTemps);
        const minTemp = Math.min(...allTemps);
        const avgTemp = allTemps.reduce((a, b) => a + b, 0) / allTemps.length;
        
        const allHumidity = forecast.forecasts.map(f => f.humidity);
        const avgHumidity = allHumidity.reduce((a, b) => a + b, 0) / allHumidity.length;
        
        const rainDays = forecast.forecasts.filter(f => f.pop > 50).length;
        
        container.innerHTML = `
            <div class="detail-card">
                <h3><i class="fas fa-chart-line"></i> Temperature Range</h3>
                <p>Max: ${Math.round(maxTemp)}°C / Min: ${Math.round(minTemp)}°C</p>
                <p>Average: ${Math.round(avgTemp)}°C</p>
            </div>
            <div class="detail-card">
                <h3><i class="fas fa-tint"></i> Humidity</h3>
                <p>Average: ${Math.round(avgHumidity)}%</p>
                <p>Comfort Level: ${avgHumidity < 40 ? 'Dry' : avgHumidity > 70 ? 'Humid' : 'Comfortable'}</p>
            </div>
            <div class="detail-card">
                <h3><i class="fas fa-cloud-rain"></i> Precipitation</h3>
                <p>Rainy periods: ${rainDays} out of ${forecast.forecasts.length} intervals</p>
                <p>Highest chance: ${Math.max(...forecast.forecasts.map(f => f.pop))}%</p>
            </div>
            <div class="detail-card">
                <h3><i class="fas fa-info-circle"></i> Recommendations</h3>
                ${getRecommendations(avgTemp, avgHumidity, rainDays)}
            </div>
        `;
    }
    
    function getRecommendations(temp, humidity, rainDays) {
        let recommendations = [];
        
        if (temp > 30) recommendations.push('🌡️ Very hot - stay hydrated and avoid sun exposure');
        else if (temp < 10) recommendations.push('🧥 Cold weather - wear warm clothing');
        
        if (humidity > 80) recommendations.push('💧 High humidity - expect muggy conditions');
        
        if (rainDays > 10) recommendations.push('☔ High chance of rain - carry an umbrella');
        
        if (recommendations.length === 0) {
            recommendations.push('✅ Pleasant weather expected');
        }
        
        return `<ul>${recommendations.map(r => `<li>${r}</li>`).join('')}</ul>`;
    }
    
    async function toggleFavorite() {
        const isFavorite = await checkFavoriteStatus();
        const btn = document.getElementById('favorite-toggle');
        
        if (isFavorite) {
            // Remove from favorites
            const response = await fetch(`/api/favorites?city=${encodeURIComponent(city)}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                btn.innerHTML = '<i class="far fa-star"></i> Add to Favorites';
                showNotification('Removed from favorites');
            }
        } else {
            // Add to favorites
            const response = await fetch('/api/favorites', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ city: city })
            });
            if (response.ok) {
                btn.innerHTML = '<i class="fas fa-star"></i> In Favorites';
                showNotification('Added to favorites');
            }
        }
    }
    
    async function checkFavoriteStatus() {
        const response = await fetch('/api/favorites');
        const data = await response.json();
        const isFavorite = data.data.includes(city);
        
        const btn = document.getElementById('favorite-toggle');
        if (btn) {
            btn.innerHTML = isFavorite ? '<i class="fas fa-star"></i> In Favorites' : '<i class="far fa-star"></i> Add to Favorites';
        }
        
        return isFavorite;
    }
    
    function showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.innerHTML = `<i class="fas fa-info-circle"></i> ${message}`;
        document.body.appendChild(notification);
        setTimeout(() => notification.remove(), 3000);
    }
    
    function getWeatherIcon(iconCode) {
        const iconMap = {
            '01d': 'fa-sun', '01n': 'fa-moon',
            '02d': 'fa-cloud-sun', '02n': 'fa-cloud-moon',
            '03d': 'fa-cloud', '03n': 'fa-cloud',
            '04d': 'fa-cloud', '04n': 'fa-cloud',
            '09d': 'fa-cloud-rain', '09n': 'fa-cloud-rain',
            '10d': 'fa-cloud-sun-rain', '10n': 'fa-cloud-moon-rain',
            '11d': 'fa-bolt', '11n': 'fa-bolt',
            '13d': 'fa-snowflake', '13n': 'fa-snowflake',
            '50d': 'fa-smog', '50n': 'fa-smog'
        };
        return iconMap[iconCode] || 'fa-cloud';
    }
</script>
{% endblock %}
```

```css
/* static/css/style.css */

/* ==================== RESET & VARIABLES ==================== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    /* Colors */
    --primary-color: #4a90e2;
    --primary-dark: #357abd;
    --secondary-color: #f39c12;
    --success-color: #27ae60;
    --danger-color: #e74c3c;
    --warning-color: #f1c40f;
    --dark-color: #2c3e50;
    --light-color: #ecf0f1;
    --gray-color: #95a5a6;
    
    /* Gradients */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-weather: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --gradient-sunset: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    
    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;
    
    /* Shadows */
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 20px rgba(0,0,0,0.1);
    --shadow-xl: 0 20px 40px rgba(0,0,0,0.15);
    
    /* Border Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 20px;
    
    /* Transitions */
    --transition-fast: 0.2s ease;
    --transition-normal: 0.3s ease;
    --transition-slow: 0.5s ease;
}

body {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: var(--dark-color);
    line-height: 1.6;
    min-height: 100vh;
}

/* ==================== NAVIGATION ==================== */
.navbar {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: var(--shadow-md);
    position: sticky;
    top: 0;
    z-index: 1000;
    padding: var(--spacing-md) 0;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-xl);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--spacing-lg);
}

.nav-brand {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary-color);
}

.nav-brand i {
    margin-right: var(--spacing-sm);
}

.brand-highlight {
    color: var(--secondary-color);
}

.nav-search {
    flex: 1;
    max-width: 400px;
    position: relative;
}

.search-form {
    display: flex;
    position: relative;
}

.search-input {
    flex: 1;
    padding: var(--spacing-sm) var(--spacing-md);
    border: 2px solid var(--light-color);
    border-radius: var(--radius-md);
    font-size: 1rem;
    transition: var(--transition-fast);
}

.search-input:focus {
    outline: none;
    border-color: var(--primary-color);
}

.search-btn {
    position: absolute;
    right: var(--spacing-sm);
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: var(--gray-color);
    cursor: pointer;
    padding: var(--spacing-sm);
}

.search-suggestions {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-lg);
    z-index: 1000;
    display: none;
}

.search-suggestions.active {
    display: block;
}

.suggestion-item {
    padding: var(--spacing-sm) var(--spacing-md);
    cursor: pointer;
    transition: var(--transition-fast);
}

.suggestion-item:hover {
    background: var(--light-color);
}

.nav-menu {
    display: flex;
    gap: var(--spacing-sm);
}

.nav-btn {
    background: none;
    border: none;
    font-size: 1.2rem;
    color: var(--gray-color);
    cursor: pointer;
    padding: var(--spacing-sm);
    border-radius: var(--radius-md);
    transition: var(--transition-fast);
}

.nav-btn:hover {
    background: var(--light-color);
    color: var(--primary-color);
}

/* ==================== MAIN CONTENT ==================== */
.main-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--spacing-2xl) var(--spacing-xl);
}

/* Hero Section */
.hero-section {
    text-align: center;
    padding: var(--spacing-2xl) 0;
    color: white;
}

.hero-title {
    font-size: 3rem;
    margin-bottom: var(--spacing-md);
    animation: fadeInUp 0.6s ease;
}

.hero-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: var(--spacing-xl);
    animation: fadeInUp 0.6s ease 0.1s both;
}

.hero-search {
    max-width: 500px;
    margin: 0 auto;
    animation: fadeInUp 0.6s ease 0.2s both;
}

.hero-search-input {
    width: 100%;
    padding: var(--spacing-md) var(--spacing-lg);
    font-size: 1rem;
    border: none;
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-lg);
    margin-bottom: var(--spacing-md);
}

.hero-search-btn {
    background: var(--secondary-color);
    color: white;
    border: none;
    padding: var(--spacing-md) var(--spacing-xl);
    font-size: 1rem;
    border-radius: var(--radius-xl);
    cursor: pointer;
    transition: var(--transition-fast);
}

.hero-search-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

/* Section Titles */
.section-title {
    font-size: 1.8rem;
    margin: var(--spacing-2xl) 0 var(--spacing-lg) 0;
    color: white;
    text-align: center;
}

.section-title i {
    margin-right: var(--spacing-sm);
}

/* Popular Cities Grid */
.cities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-2xl);
}

.city-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    cursor: pointer;
    transition: var(--transition-normal);
    box-shadow: var(--shadow-md);
}

.city-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}

.city-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--spacing-md);
}

.city-card-header h3 {
    font-size: 1.2rem;
    color: var(--dark-color);
}

.city-card-header i {
    font-size: 2rem;
    color: var(--secondary-color);
}

.city-card-temp {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: var(--spacing-sm);
}

.city-card-desc {
    color: var(--gray-color);
    margin-bottom: var(--spacing-md);
    text-transform: capitalize;
}

.city-card-details {
    display: flex;
    justify-content: space-between;
    color: var(--gray-color);
    font-size: 0.9rem;
}

/* Tips Grid */
.tips-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: var(--spacing-lg);
    margin-top: var(--spacing-lg);
}

.tip-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    text-align: center;
    transition: var(--transition-normal);
}

.tip-card i {
    font-size: 2.5rem;
    color: var(--secondary-color);
    margin-bottom: var(--spacing-md);
}

.tip-card h3 {
    margin-bottom: var(--spacing-sm);
    color: var(--dark-color);
}

.tip-card p {
    color: var(--gray-color);
    font-size: 0.9rem;
}

/* Weather Page Styles */
.weather-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    box-shadow: var(--shadow-xl);
}

.weather-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: var(--spacing-xl);
}

.back-btn, .favorite-btn {
    padding: var(--spacing-sm) var(--spacing-lg);
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: var(--transition-fast);
    font-size: 1rem;
}

.back-btn {
    background: var(--gray-color);
    color: white;
}

.favorite-btn {
    background: var(--secondary-color);
    color: white;
}

.back-btn:hover, .favorite-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

/* Current Weather Card */
.current-weather {
    margin-bottom: var(--spacing-xl);
}

.weather-main-card {
    background: var(--gradient-weather);
    border-radius: var(--radius-xl);
    padding: var(--spacing-xl);
    color: white;
}

.weather-location h1 {
    font-size: 2rem;
    margin-bottom: var(--spacing-sm);
}

.weather-time {
    opacity: 0.9;
    font-size: 0.9rem;
}

.weather-primary {
    display: flex;
    align-items: center;
    justify-content: space-around;
    margin: var(--spacing-xl) 0;
}

.weather-icon i {
    font-size: 5rem;
}

.weather-temp {
    font-size: 4rem;
    font-weight: 700;
}

.temp-unit {
    font-size: 1.5rem;
}

.weather-desc {
    text-align: center;
    text-transform: capitalize;
}

.feels-like {
    display: block;
    font-size: 0.9rem;
    opacity: 0.9;
    margin-top: var(--spacing-sm);
}

.weather-details-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: var(--spacing-md);
    margin-top: var(--spacing-xl);
}

.detail-item {
    text-align: center;
    padding: var(--spacing-sm);
    background: rgba(255, 255, 255, 0.2);
    border-radius: var(--radius-md);
}

.detail-item i {
    font-size: 1.5rem;
    margin-bottom: var(--spacing-sm);
    display: block;
}

.detail-item span {
    display: block;
    font-size: 0.8rem;
    opacity: 0.9;
}

.detail-item strong {
    display: block;
    font-size: 1.1rem;
    margin-top: var(--spacing-xs);
}

/* Forecast Grid */
.forecast-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: var(--spacing-md);
    margin-bottom: var(--spacing-xl);
}

.forecast-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-md);
    text-align: center;
    box-shadow: var(--shadow-md);
    transition: var(--transition-fast);
}

.forecast-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.forecast-day {
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: var(--spacing-xs);
}

.forecast-date {
    font-size: 0.8rem;
    color: var(--gray-color);
    margin-bottom: var(--spacing-md);
}

.forecast-card i {
    font-size: 2.5rem;
    margin: var(--spacing-md) 0;
}

.forecast-temp {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: var(--spacing-xs);
}

.forecast-desc {
    font-size: 0.8rem;
    color: var(--gray-color);
    text-transform: capitalize;
    margin-bottom: var(--spacing-sm);
}

.forecast-details {
    display: flex;
    justify-content: center;
    gap: var(--spacing-md);
    font-size: 0.8rem;
    color: var(--gray-color);
}

/* Hourly Forecast */
.hourly-section {
    margin-bottom: var(--spacing-xl);
}

.hourly-scroll {
    display: flex;
    overflow-x: auto;
    gap: var(--spacing-md);
    padding: var(--spacing-md) 0;
}

.hourly-card {
    flex: 0 0 auto;
    min-width: 120px;
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-md);
    text-align: center;
    box-shadow: var(--shadow-sm);
}

.hourly-time {
    font-weight: 600;
    margin-bottom: var(--spacing-sm);
}

.hourly-card i {
    font-size: 1.5rem;
    margin: var(--spacing-sm) 0;
}

.hourly-temp {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: var(--spacing-xs);
}

.hourly-desc {
    font-size: 0.7rem;
    color: var(--gray-color);
    text-transform: capitalize;
}

.hourly-rain {
    font-size: 0.7rem;
    color: var(--primary-color);
    margin-top: var(--spacing-xs);
}

/* Details Section */
.details-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-lg);
}

.detail-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-md);
}

.detail-card h3 {
    color: var(--primary-color);
    margin-bottom: var(--spacing-md);
}

.detail-card ul {
    list-style: none;
    padding-left: 0;
}

.detail-card li {
    padding: var(--spacing-xs) 0;
    color: var(--gray-color);
}

/* Sidebar */
.sidebar {
    position: fixed;
    top: 0;
    right: -400px;
    width: 400px;
    height: 100vh;
    background: white;
    box-shadow: var(--shadow-xl);
    z-index: 1100;
    transition: right 0.3s ease;
    overflow-y: auto;
}

.sidebar.open {
    right: 0;
}

.sidebar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-lg);
    border-bottom: 1px solid var(--light-color);
}

.close-sidebar {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--gray-color);
}

.favorites-list {
    padding: var(--spacing-md);
}

.favorite-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-md);
    margin-bottom: var(--spacing-sm);
    background: var(--light-color);
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: var(--transition-fast);
}

.favorite-item:hover {
    background: #e0e0e0;
}

/* Modal */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1200;
    align-items: center;
    justify-content: center;
}

.modal.open {
    display: flex;
}

.modal-content {
    background: white;
    border-radius: var(--radius-lg);
    max-width: 500px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
    animation: slideIn 0.3s ease;
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-lg);
    border-bottom: 1px solid var(--light-color);
}

.close-modal {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
}

.modal-body {
    padding: var(--spacing-lg);
}

.setting-group {
    margin-bottom: var(--spacing-lg);
}

.setting-group label {
    display: block;
    margin-bottom: var(--spacing-sm);
    font-weight: 500;
}

.setting-group select,
.setting-group input[type="text"] {
    width: 100%;
    padding: var(--spacing-sm) var(--spacing-md);
    border: 1px solid var(--light-color);
    border-radius: var(--radius-md);
    font-size: 1rem;
}

.modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: var(--spacing-sm);
    padding: var(--spacing-lg);
    border-top: 1px solid var(--light-color);
}

/* Loading States */
.loading-state {
    text-align: center;
    padding: var(--spacing-xl);
    color: var(--gray-color);
}

.loading-spinner {
    text-align: center;
    padding: var(--spacing-xl);
}

.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    z-index: 1300;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
}

.spinner {
    width: 50px;
    height: 50px;
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-top-color: white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: var(--spacing-md);
}

/* Notification */
.notification {
    position: fixed;
    bottom: var(--spacing-xl);
    right: var(--spacing-xl);
    background: white;
    padding: var(--spacing-md) var(--spacing-lg);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-lg);
    z-index: 1400;
    animation: slideInRight 0.3s ease;
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

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(100px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-container {
        flex-direction: column;
        gap: var(--spacing-md);
    }
    
    .nav-search {
        max-width: 100%;
        width: 100%;
    }
    
    .hero-title {
        font-size: 2rem;
    }
    
    .weather-primary {
        flex-direction: column;
        gap: var(--spacing-md);
    }
    
    .sidebar {
        width: 100%;
        right: -100%;
    }
    
    .cities-grid {
        grid-template-columns: 1fr;
    }
    
    .forecast-grid {
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    }
}

@media (max-width: 480px) {
    .main-content {
        padding: var(--spacing-md);
    }
    
    .weather-container {
        padding: var(--spacing-md);
    }
    
    .weather-details-grid {
        grid-template-columns: 1fr;
    }
}
```

```javascript
// static/js/app.js

/**
 * Weather Dashboard - Main Application JavaScript
 * 
 * Design Pattern: Observer Pattern - Event listeners for user interactions
 * SOLID Principle: Single Responsibility - Each function handles one aspect
 */

// ==================== DOM Elements ====================
const searchForm = document.getElementById('search-form');
const citySearch = document.getElementById('city-search');
const searchSuggestions = document.getElementById('search-suggestions');
const refreshBtn = document.getElementById('refresh-btn');
const favoritesBtn = document.getElementById('favorites-btn');
const settingsBtn = document.getElementById('settings-btn');
const favoritesSidebar = document.getElementById('favorites-sidebar');
const settingsModal = document.getElementById('settings-modal');
const loadingOverlay = document.getElementById('loading-overlay');

// ==================== Global State ====================
let autoRefreshInterval = null;
let currentCity = null;

// ==================== Utility Functions ====================

/**
 * Show loading overlay
 */
function showLoading() {
    if (loadingOverlay) {
        loadingOverlay.style.display = 'flex';
    }
}

/**
 * Hide loading overlay
 */
function hideLoading() {
    if (loadingOverlay) {
        loadingOverlay.style.display = 'none';
    }
}

/**
 * Show notification message
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    
    const icons = {
        success: 'fa-check-circle',
        error: 'fa-exclamation-circle',
        info: 'fa-info-circle',
        warning: 'fa-exclamation-triangle'
    };
    
    notification.innerHTML = `
        <i class="fas ${icons[type]}"></i>
        <span>${message}</span>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Format date for display
 */
function formatDate(date, format = 'full') {
    const d = new Date(date);
    
    if (format === 'time') {
        return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } else if (format === 'date') {
        return d.toLocaleDateString();
    } else {
        return d.toLocaleString();
    }
}

/**
 * Get weather icon class
 */
function getWeatherIcon(iconCode) {
    const iconMap = {
        '01d': 'fa-sun',
        '01n': 'fa-moon',
        '02d': 'fa-cloud-sun',
        '02n': 'fa-cloud-moon',
        '03d': 'fa-cloud',
        '03n': 'fa-cloud',
        '04d': 'fa-cloud',
        '04n': 'fa-cloud',
        '09d': 'fa-cloud-rain',
        '09n': 'fa-cloud-rain',
        '10d': 'fa-cloud-sun-rain',
        '10n': 'fa-cloud-moon-rain',
        '11d': 'fa-bolt',
        '11n': 'fa-bolt',
        '13d': 'fa-snowflake',
        '13n': 'fa-snowflake',
        '50d': 'fa-smog',
        '50n': 'fa-smog'
    };
    return iconMap[iconCode] || 'fa-cloud';
}

/**
 * Get temperature in user's preferred unit
 */
function formatTemperature(tempCelsius) {
    const unit = localStorage.getItem('tempUnit') || 'celsius';
    if (unit === 'fahrenheit') {
        return {
            value: Math.round((tempCelsius * 9/5) + 32),
            unit: '°F'
        };
    }
    return {
        value: Math.round(tempCelsius),
        unit: '°C'
    };
}

// ==================== Search Functionality ====================

/**
 * Search for cities based on query
 */
async function searchCities(query) {
    if (query.length < 2) {
        searchSuggestions.classList.remove('active');
        return;
    }
    
    try {
        const response = await fetch(`/api/cities/search?q=${encodeURIComponent(query)}&limit=5`);
        const data = await response.json();
        
        if (data.success && data.data.length > 0) {
            displaySearchSuggestions(data.data);
        } else {
            searchSuggestions.classList.remove('active');
        }
    } catch (error) {
        console.error('City search failed:', error);
        searchSuggestions.classList.remove('active');
    }
}

/**
 * Display search suggestions
 */
function displaySearchSuggestions(cities) {
    searchSuggestions.innerHTML = cities.map(city => `
        <div class="suggestion-item" data-city="${city.name}" data-country="${city.country}">
            <i class="fas fa-city"></i>
            <strong>${city.name}</strong>, ${city.country}
            ${city.state ? `<span class="suggestion-state">(${city.state})</span>` : ''}
        </div>
    `).join('');
    
    searchSuggestions.classList.add('active');
    
    // Add click handlers
    document.querySelectorAll('.suggestion-item').forEach(item => {
        item.addEventListener('click', () => {
            const city = item.dataset.city;
            if (city) {
                window.location.href = `/weather?city=${encodeURIComponent(city)}`;
            }
        });
    });
}

/**
 * Close search suggestions when clicking outside
 */
document.addEventListener('click', (e) => {
    if (!searchForm?.contains(e.target)) {
        searchSuggestions?.classList.remove('active');
    }
});

// Search input handler
if (citySearch) {
    let debounceTimer;
    citySearch.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            searchCities(e.target.value);
        }, 300);
    });
}

// Search form submission
if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const query = citySearch?.value.trim();
        if (query) {
            // Save to recent searches
            let recent = JSON.parse(localStorage.getItem('recentSearches') || '[]');
            recent = [query, ...recent.filter(c => c !== query)].slice(0, 10);
            localStorage.setItem('recentSearches', JSON.stringify(recent));
            
            window.location.href = `/weather?city=${encodeURIComponent(query)}`;
        }
    });
}

// ==================== Favorites Management ====================

/**
 * Load and display favorites
 */
async function loadFavorites() {
    try {
        const response = await fetch('/api/favorites');
        const data = await response.json();
        
        if (data.success && data.data.length > 0) {
            displayFavorites(data.data);
        } else {
            const favoritesList = document.getElementById('favorites-list');
            if (favoritesList) {
                favoritesList.innerHTML = '<div class="empty-state">No favorites yet. Add cities you love!</div>';
            }
        }
    } catch (error) {
        console.error('Failed to load favorites:', error);
    }
}

/**
 * Display favorites in sidebar
 */
function displayFavorites(favorites) {
    const favoritesList = document.getElementById('favorites-list');
    if (!favoritesList) return;
    
    if (favorites.length === 0) {
        favoritesList.innerHTML = '<div class="empty-state">No favorites yet. Add cities you love!</div>';
        return;
    }
    
    favoritesList.innerHTML = favorites.map(city => `
        <div class="favorite-item" data-city="${city}">
            <span><i class="fas fa-star"></i> ${city}</span>
            <div class="favorite-actions">
                <button class="favorite-view" title="View weather">
                    <i class="fas fa-eye"></i>
                </button>
                <button class="favorite-remove" title="Remove from favorites">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        </div>
    `).join('');
    
    // Add event handlers
    document.querySelectorAll('.favorite-view').forEach((btn, index) => {
        btn.addEventListener('click', () => {
            const city = favorites[index];
            window.location.href = `/weather?city=${encodeURIComponent(city)}`;
        });
    });
    
    document.querySelectorAll('.favorite-remove').forEach((btn, index) => {
        btn.addEventListener('click', async (e) => {
            e.stopPropagation();
            const city = favorites[index];
            await removeFavorite(city);
        });
    });
}

/**
 * Remove city from favorites
 */
async function removeFavorite(city) {
    try {
        const response = await fetch(`/api/favorites?city=${encodeURIComponent(city)}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showNotification(`${city} removed from favorites`, 'success');
            loadFavorites(); // Refresh list
        } else {
            showNotification('Failed to remove from favorites', 'error');
        }
    } catch (error) {
        console.error('Failed to remove favorite:', error);
        showNotification('Failed to remove from favorites', 'error');
    }
}

// Favorites button handler
if (favoritesBtn) {
    favoritesBtn.addEventListener('click', () => {
        favoritesSidebar?.classList.add('open');
        loadFavorites();
    });
}

// Close sidebar
document.querySelector('.close-sidebar')?.addEventListener('click', () => {
    favoritesSidebar?.classList.remove('open');
});

// ==================== Settings Management ====================

/**
 * Load settings from localStorage
 */
function loadSettings() {
    const tempUnit = localStorage.getItem('tempUnit') || 'celsius';
    const defaultCity = localStorage.getItem('defaultCity') || '';
    const autoRefresh = localStorage.getItem('autoRefresh') === 'true';
    
    const tempUnitSelect = document.getElementById('temp-unit');
    const defaultCityInput = document.getElementById('default-city');
    const autoRefreshCheckbox = document.getElementById('auto-refresh');
    
    if (tempUnitSelect) tempUnitSelect.value = tempUnit;
    if (defaultCityInput) defaultCityInput.value = defaultCity;
    if (autoRefreshCheckbox) autoRefreshCheckbox.checked = autoRefresh;
    
    // Setup auto-refresh
    if (autoRefresh && currentCity) {
        startAutoRefresh();
    }
}

/**
 * Save settings
 */
function saveSettings() {
    const tempUnit = document.getElementById('temp-unit')?.value || 'celsius';
    const defaultCity = document.getElementById('default-city')?.value || '';
    const autoRefresh = document.getElementById('auto-refresh')?.checked || false;
    
    localStorage.setItem('tempUnit', tempUnit);
    localStorage.setItem('defaultCity', defaultCity);
    localStorage.setItem('autoRefresh', autoRefresh);
    
    // Refresh current page to apply temperature unit change
    if (window.location.pathname === '/weather') {
        loadWeatherData(true);
        loadForecastData(true);
    }
    
    // Setup auto-refresh
    if (autoRefresh) {
        startAutoRefresh();
    } else {
        stopAutoRefresh();
    }
    
    showNotification('Settings saved', 'success');
    closeSettingsModal();
}

/**
 * Start auto-refresh
 */
function startAutoRefresh() {
    stopAutoRefresh();
    autoRefreshInterval = setInterval(() => {
        if (window.location.pathname === '/weather') {
            console.log('Auto-refreshing weather data...');
            if (typeof loadWeatherData === 'function') {
                loadWeatherData(true);
            }
            if (typeof loadForecastData === 'function') {
                loadForecastData(true);
            }
        }
    }, 5 * 60 * 1000); // 5 minutes
}

/**
 * Stop auto-refresh
 */
function stopAutoRefresh() {
    if (autoRefreshInterval) {
        clearInterval(autoRefreshInterval);
        autoRefreshInterval = null;
    }
}

/**
 * Open settings modal
 */
function openSettingsModal() {
    loadSettings();
    settingsModal?.classList.add('open');
}

/**
 * Close settings modal
 */
function closeSettingsModal() {
    settingsModal?.classList.remove('open');
}

// Settings button handler
if (settingsBtn) {
    settingsBtn.addEventListener('click', openSettingsModal);
}

// Modal close handlers
document.querySelector('.close-modal')?.addEventListener('click', closeSettingsModal);
document.getElementById('cancel-settings')?.addEventListener('click', closeSettingsModal);
document.getElementById('save-settings')?.addEventListener('click', saveSettings);

// Close modal when clicking outside
settingsModal?.addEventListener('click', (e) => {
    if (e.target === settingsModal) {
        closeSettingsModal();
    }
});

// ==================== Refresh Functionality ====================

if (refreshBtn) {
    refreshBtn.addEventListener('click', () => {
        showNotification('Refreshing weather data...', 'info');
        
        // Reload current page data
        if (window.location.pathname === '/weather') {
            if (typeof loadWeatherData === 'function') {
                loadWeatherData(true);
            }
            if (typeof loadForecastData === 'function') {
                loadForecastData(true);
            }
        } else {
            // Refresh popular cities if on homepage
            if (typeof loadPopularCities === 'function') {
                loadPopularCities();
            }
        }
    });
}

// ==================== Cache Management ====================

/**
 * Get cache statistics
 */
async function getCacheStats() {
    try {
        const response = await fetch('/api/cache/stats');
        const data = await response.json();
        
        if (data.success) {
            console.log('Cache stats:', data.data);
            return data.data;
        }
    } catch (error) {
        console.error('Failed to get cache stats:', error);
    }
    return null;
}

// ==================== Page Initialization ====================

document.addEventListener('DOMContentLoaded', () => {
    console.log('Weather Dashboard initialized');
    
    // Load user preferences
    loadSettings();
    
    // Set current city from URL if on weather page
    if (window.location.pathname === '/weather') {
        const urlParams = new URLSearchParams(window.location.search);
        currentCity = urlParams.get('city');
    }
    
    // Initialize auto-refresh if enabled
    if (localStorage.getItem('autoRefresh') === 'true' && currentCity) {
        startAutoRefresh();
    }
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + K: Focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            citySearch?.focus();
        }
        
        // Escape: Close modals
        if (e.key === 'Escape') {
            closeSettingsModal();
            favoritesSidebar?.classList.remove('open');
            searchSuggestions?.classList.remove('active');
        }
        
        // Ctrl/Cmd + R: Refresh (without page reload)
        if ((e.ctrlKey || e.metaKey) && e.key === 'r') {
            e.preventDefault();
            refreshBtn?.click();
        }
    });
    
    // Add service worker for offline support (optional)
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js').catch(err => {
            console.log('Service worker registration failed:', err);
        });
    }
});

// ==================== Error Handling ====================

window.addEventListener('error', (e) => {
    console.error('Global error:', e.error);
    showNotification('An unexpected error occurred', 'error');
});

// Handle offline status
window.addEventListener('online', () => {
    showNotification('Back online! Refreshing data...', 'success');
    refreshBtn?.click();
});

window.addEventListener('offline', () => {
    showNotification('You are offline. Some features may be unavailable.', 'warning');
});

// ==================== Performance Monitoring ====================

// Log page load performance
window.addEventListener('load', () => {
    if (performance && performance.timing) {
        const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
        console.log(`Page load time: ${loadTime}ms`);
    }
});

// Export functions for use in other scripts
window.weatherDashboard = {
    showNotification,
    formatTemperature,
    getWeatherIcon,
    loadFavorites,
    getCacheStats
};
```

---

## 🐳 Section 3: Docker & Deployment

Containerize the application with Docker and deploy to production.

**SOLID Principles Applied:**
- Single Responsibility: Each service has its own container
- Dependency Inversion: Services depend on environment variables

**Design Pattern: Container Pattern** – Isolated deployment units

```dockerfile
# Dockerfile
"""
Dockerfile for Weather Dashboard application.

Design Pattern: Container Pattern - Isolated deployment unit
"""

FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --gid 1001 appuser

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--worker-class", "sync", "app:app"]
```

```yaml
# docker-compose.yml
"""
Docker Compose configuration for Weather Dashboard.

Design Pattern: Orchestration Pattern - Manages multiple containers
"""

version: '3.8'

services:
  # Redis cache service
  redis:
    image: redis:7-alpine
    container_name: weather-redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    command: redis-server --appendonly yes
    networks:
      - weather-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  # Flask web application
  web:
    build: .
    container_name: weather-web
    restart: unless-stopped
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - FLASK_DEBUG=0
      - REDIS_URL=redis://redis:6379/0
      - OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}
      - FLASK_SECRET_KEY=${FLASK_SECRET_KEY}
    depends_on:
      redis:
        condition: service_healthy
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
    networks:
      - weather-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Nginx reverse proxy (optional)
  nginx:
    image: nginx:alpine
    container_name: weather-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - web
    networks:
      - weather-network
    profiles:
      - production

# Networks
networks:
  weather-network:
    driver: bridge

# Volumes
volumes:
  redis-data:
```

```txt
# requirements.txt
"""
Python dependencies for Weather Dashboard.
"""

# Core dependencies
Flask==2.3.3
Flask-Caching==2.0.2
Flask-Limiter==3.3.1
Flask-Session==0.5.0

# API and HTTP
requests==2.31.0
gunicorn==21.2.0

# Caching
redis==5.0.0

# Data validation and serialization
pydantic==2.3.0
python-dotenv==1.0.0

# Development dependencies (optional)
pytest==7.4.2
pytest-cov==4.1.0
black==23.9.1
flake8==6.1.0

# Production monitoring
prometheus-flask-exporter==0.22.4
```

```yaml
# docker-compose.prod.yml
"""
Production Docker Compose configuration with monitoring.
"""

version: '3.8'

services:
  redis:
    image: redis:7-alpine
    restart: always
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data
    networks:
      - weather-network

  web:
    build: .
    restart: always
    environment:
      - FLASK_ENV=production
      - REDIS_URL=redis://:${REDIS_PASSWORD}@redis:6379/0
      - OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}
      - FLASK_SECRET_KEY=${FLASK_SECRET_KEY}
    depends_on:
      - redis
    networks:
      - weather-network
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure

  nginx:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.prod.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - web
    networks:
      - weather-network

  prometheus:
    image: prom/prometheus:latest
    restart: always
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    ports:
      - "9090:9090"
    networks:
      - weather-network

  grafana:
    image: grafana/grafana:latest
    restart: always
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
    volumes:
      - grafana-data:/var/lib/grafana
    ports:
      - "3000:3000"
    networks:
      - weather-network
    depends_on:
      - prometheus

networks:
  weather-network:
    driver: bridge

volumes:
  redis-data:
  prometheus-data:
  grafana-data:
```

```nginx
# nginx.conf
"""
Nginx configuration for reverse proxy and load balancing.
"""

events {
    worker_connections 1024;
}

http {
    upstream weather_backend {
        least_conn;
        server web:5000 max_fails=3 fail_timeout=30s;
    }

    server {
        listen 80;
        server_name weather.example.com;
        
        # Redirect HTTP to HTTPS
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name weather.example.com;

        # SSL configuration
        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;

        # Security headers
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-XSS-Protection "1; mode=block" always;

        # Gzip compression
        gzip on;
        gzip_vary on;
        gzip_min_length 1024;
        gzip_types text/plain text/css text/xml text/javascript application/javascript application/json;

        # Static files caching
        location /static/ {
            alias /app/static/;
            expires 30d;
            add_header Cache-Control "public, immutable";
        }

        # Proxy to Flask app
        location / {
            proxy_pass http://weather_backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            # Timeouts
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }

        # Health check endpoint
        location /health {
            proxy_pass http://weather_backend/health;
            access_log off;
        }
    }
}
```

```yaml
# .github/workflows/deploy.yml
"""
GitHub Actions CI/CD pipeline.
"""

name: Deploy Weather Dashboard

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=app --cov-report=xml
      env:
        OPENWEATHER_API_KEY: ${{ secrets.OPENWEATHER_API_KEY }}
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: |
          ${{ secrets.DOCKER_USERNAME }}/weather-dashboard:latest
          ${{ secrets.DOCKER_USERNAME }}/weather-dashboard:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      uses: appleboy/ssh-action@v0.1.5
      with:
        host: ${{ secrets.DEPLOY_HOST }}
        username: ${{ secrets.DEPLOY_USER }}
        key: ${{ secrets.DEPLOY_KEY }}
        script: |
          cd /app/weather-dashboard
          docker-compose -f docker-compose.prod.yml pull
          docker-compose -f docker-compose.prod.yml up -d --remove-orphans
          docker system prune -f
```

```python
# deploy.py
"""
Deployment script for production.
"""

import os
import subprocess
import sys
from pathlib import Path


class DeploymentManager:
    """
    Manages production deployment.
    
    Design Pattern: Facade Pattern - Simplifies deployment complexity
    """
    
    def __init__(self, environment='production'):
        self.environment = environment
        self.project_root = Path(__file__).parent
    
    def check_prerequisites(self) -> bool:
        """Check if all prerequisites are installed."""
        print("Checking prerequisites...")
        
        # Check Docker
        try:
            subprocess.run(['docker', '--version'], check=True, capture_output=True)
            print("✓ Docker installed")
        except subprocess.CalledProcessError:
            print("✗ Docker not found")
            return False
        
        # Check Docker Compose
        try:
            subprocess.run(['docker-compose', '--version'], check=True, capture_output=True)
            print("✓ Docker Compose installed")
        except subprocess.CalledProcessError:
            print("✗ Docker Compose not found")
            return False
        
        # Check environment variables
        required_vars = ['OPENWEATHER_API_KEY', 'FLASK_SECRET_KEY']
        missing_vars = []
        
        for var in required_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"✗ Missing environment variables: {', '.join(missing_vars)}")
            return False
        
        print("✓ Environment variables set")
        return True
    
    def build_images(self) -> bool:
        """Build Docker images."""
        print("\nBuilding Docker images...")
        
        compose_file = 'docker-compose.yml'
        if self.environment == 'production':
            compose_file = 'docker-compose.prod.yml'
        
        result = subprocess.run(
            ['docker-compose', '-f', compose_file, 'build'],
            cwd=self.project_root
        )
        
        if result.returncode == 0:
            print("✓ Images built successfully")
            return True
        else:
            print("✗ Failed to build images")
            return False
    
    def start_services(self) -> bool:
        """Start all services."""
        print("\nStarting services...")
        
        compose_file = 'docker-compose.yml'
        if self.environment == 'production':
            compose_file = 'docker-compose.prod.yml'
        
        result = subprocess.run(
            ['docker-compose', '-f', compose_file, 'up', '-d'],
            cwd=self.project_root
        )
        
        if result.returncode == 0:
            print("✓ Services started")
            return True
        else:
            print("✗ Failed to start services")
            return False
    
    def check_health(self) -> bool:
        """Check service health."""
        print("\nChecking service health...")
        
        import requests
        import time
        
        # Wait for services to start
        time.sleep(5)
        
        try:
            response = requests.get('http://localhost:5000/health', timeout=10)
            if response.status_code == 200:
                print("✓ Web service is healthy")
                return True
        except requests.exceptions.RequestException:
            pass
        
        print("✗ Web service health check failed")
        return False
    
    def view_logs(self):
        """View service logs."""
        print("\nShowing recent logs...")
        
        compose_file = 'docker-compose.yml'
        if self.environment == 'production':
            compose_file = 'docker-compose.prod.yml'
        
        subprocess.run(
            ['docker-compose', '-f', compose_file, 'logs', '--tail=50'],
            cwd=self.project_root
        )
    
    def stop_services(self):
        """Stop all services."""
        print("\nStopping services...")
        
        compose_file = 'docker-compose.yml'
        if self.environment == 'production':
            compose_file = 'docker-compose.prod.yml'
        
        subprocess.run(
            ['docker-compose', '-f', compose_file, 'down'],
            cwd=self.project_root
        )
        
        print("✓ Services stopped")
    
    def deploy(self):
        """Complete deployment process."""
        print("=" * 60)
        print("WEATHER DASHBOARD DEPLOYMENT")
        print("=" * 60)
        
        if not self.check_prerequisites():
            print("\nDeployment failed: Prerequisites not met")
            return False
        
        if not self.build_images():
            return False
        
        if not self.start_services():
            return False
        
        if not self.check_health():
            print("\nWarning: Health check failed")
            self.view_logs()
            return False
        
        print("\n" + "=" * 60)
        print("✅ DEPLOYMENT SUCCESSFUL!")
        print("=" * 60)
        print("\nApplication is running at: http://localhost:5000")
        print("API documentation: http://localhost:5000/api/docs")
        print("Health check: http://localhost:5000/health")
        
        return True


def main():
    """Main deployment entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Deploy Weather Dashboard')
    parser.add_argument('--env', choices=['development', 'production'], default='development')
    parser.add_argument('--action', choices=['deploy', 'stop', 'logs'], default='deploy')
    
    args = parser.parse_args()
    
    manager = DeploymentManager(environment=args.env)
    
    if args.action == 'deploy':
        success = manager.deploy()
        sys.exit(0 if success else 1)
    elif args.action == 'stop':
        manager.stop_services()
    elif args.action == 'logs':
        manager.view_logs()


if __name__ == '__main__':
    main()
```

---

## 📊 Takeaway from This Story

**What You Built:**

- **Complete Flask Backend** – RESTful API with proper error handling and rate limiting
- **Weather API Integration** – OpenWeatherMap integration with current conditions and forecasts
- **Redis Caching** – Performance optimization with 5-minute cache TTL
- **Responsive Frontend** – Modern HTML5/CSS3 with mobile-first design
- **Interactive UI** – Vanilla JavaScript with search, favorites, and settings
- **Data Visualization** – Weather forecasts with daily and hourly views
- **Docker Containerization** – Multi-container deployment with Docker Compose
- **Production Deployment** – Nginx reverse proxy, load balancing, monitoring

**SOLID Principles Applied:**
- **Single Responsibility** – API service, cache service, frontend each have one job
- **Open/Closed** – New weather providers can be added without changing existing code
- **Liskov Substitution** – Cache implementations are interchangeable
- **Interface Segregation** – Small, focused service interfaces
- **Dependency Inversion** – High-level services depend on abstractions

**Design Patterns Used:**
- **Facade Pattern** – WeatherService simplifies API complexity
- **Proxy Pattern** – CacheService adds caching layer
- **Factory Pattern** – create_app() creates configured Flask app
- **Observer Pattern** – Event listeners for UI interactions
- **Container Pattern** – Docker containers for isolation
- **Orchestration Pattern** – Docker Compose for multi-service management

**Key Technologies:**
- **Flask** – Web framework with blueprints and extensions
- **Redis** – In-memory caching for performance
- **OpenWeatherMap API** – Real-time weather data
- **Docker** – Containerization for consistent deployment
- **Nginx** – Reverse proxy and load balancing
- **Gunicorn** – Production WSGI server
- **Prometheus/Grafana** – Monitoring and visualization
- **GitHub Actions** – CI/CD automation

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: CLI Expense Tracker

- **📚 Series J Catalog:** Capstone Projects – View all 3 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: ML-Powered Recommendation Engine (Series J, Story 3)

---

## 🎯 Your Challenge

Now that you've built the Weather Dashboard, here's how to extend it:

1. **Add weather alerts** – Severe weather notifications via email/SMS
2. **Add historical data** – Track and visualize historical weather patterns
3. **Add air quality index** – Integrate air quality API
4. **Add weather maps** – Interactive radar maps with Leaflet.js
5. **Add user accounts** – Persistent favorites across devices
6. **Add mobile app** – React Native or Flutter mobile client
7. **Add voice search** – Speech recognition for city search
8. **Add weather comparisons** – Compare two cities side-by-side
9. **Add travel recommendations** – Best time to visit based on weather
10. **Add API rate limiting dashboard** – Monitor API usage and costs

**You've built a full-stack web application. Next stop: ML-Powered Recommendation Engine!**

---

*Found this helpful? Clap, comment, and share your weather dashboard. Next stop: ML-Powered Recommendation Engine!* 🚇

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
| Series J | 3 | 2 | 1 | 67% |

**Next Story to Generate:**
1. Series J, Story 3: ML-Powered Recommendation Engine (Full-stack with collaborative filtering, Pandas, Scikit-learn, Flask API, Docker)