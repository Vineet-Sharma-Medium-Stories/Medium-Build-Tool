
# GitHub Copilot Mastery - From Code to Production
## VS Code Integration, Enterprise Workflows, and Best Practices

### Introduction: From AI Assistant to Production Partner

Throughout this series, we've explored GitHub Copilot's capabilities—from intelligent code completion to multi-file editing, test generation, and refactoring. In Story 1, we built the foundation with the Intelligence Layer, understanding how Copilot completes code, understands context, and learns your patterns. In Story 2, we expanded into the Integration Ecosystem, connecting Copilot with IDEs, chat interfaces, CLI tools, and GitHub pull requests. In Story 3, we mastered the Advanced Workflow Engine, generating multi-file features, comprehensive tests, documentation, and refactoring legacy code.

Now, in this final story, we bring everything together. The true measure of any development tool is how it performs in real-world, production environments. This story takes you on a complete journey from zero to production, showing how Copilot integrates with VS Code to build production-ready applications, establish enterprise workflows, and implement best practices that ensure security, quality, and maintainability at scale. You'll learn how to configure VS Code for optimal Copilot experience, set up CI/CD pipelines, implement security scanning, and establish team workflows that leverage Copilot effectively while maintaining code quality and security standards.

```mermaid
graph TB
    subgraph "GitHub Copilot Production Journey"
        A[VS Code Integration<br/>IDE Configuration] --> E[Development Environment]
        B[Enterprise Workflows<br/>Team Collaboration] --> F[Production-Ready<br/>Applications]
        C[Security Best Practices<br/>Code Quality] --> F
        D[Continuous Improvement<br/>Learning & Optimization] --> F
    end
    
    style A fill:#2DA44E,color:#fff
    style B fill:#2DA44E,color:#fff
    style C fill:#2DA44E,color:#fff
    style D fill:#2DA44E,color:#fff
    style F fill:#c8e6c9
```

---

## Complete GitHub Copilot Mastery Series (4 stories):

- 🚀 [**1. GitHub Copilot Mastery - The Intelligence Layer: Code Completion, Context Awareness, AI Suggestions, and Learning Patterns**](#) – A deep dive into semantic code completion, intelligent context understanding, advanced AI suggestions beyond autocomplete, and personalized pattern learning.

- 🔌 [**2. GitHub Copilot Mastery - The Integration Ecosystem: IDE Support, Chat Interface, CLI Tools, and Pull Request Integration**](#) – How to leverage Copilot across your entire development workflow with VS Code integration, natural language chat, command-line tools, and GitHub PR assistance.

- ⚡ [**3. GitHub Copilot Mastery - The Advanced Workflow Engine: Multi-File Editing, Test Generation, Documentation, and Refactoring**](#) – Mastering complex code generation across multiple files, automated test suite creation, intelligent documentation generation, and AI-powered code refactoring.

- 🏗️ [**4. GitHub Copilot Mastery - From Code to Production: VS Code Integration, Enterprise Workflows, and Best Practices**](#) – A hands-on guide to integrating Copilot with VS Code, building production-ready applications, establishing team workflows, and implementing security best practices. *(This story)*

---

## Part 1: VS Code Integration — The Ultimate Development Environment

### Step 1: Complete VS Code Configuration for Copilot

#### Install and Configure Essential Extensions

```bash
# Install GitHub Copilot and supporting extensions
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.black-formatter
code --install-extension ms-python.flake8
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-docker
code --install-extension GitHub.vscode-pull-request-github

# Verify installations
code --list-extensions | grep -E "copilot|python|gitlens"
```

#### Create Comprehensive VS Code Settings

Create `.vscode/settings.json` for optimal Copilot experience:

```json
{
  // ============================================
  // GitHub Copilot Configuration
  // ============================================
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true,
    "yaml": true,
    "json": true,
    "dockerfile": true
  },
  
  "github.copilot.editor.enableAutoCompletions": true,
  "github.copilot.editor.enableCodeActions": true,
  "github.copilot.editor.enableInlineChat": true,
  
  "github.copilot.advanced": {
    "debug.enable": false,
    "debug.overrideProxyUrl": "",
    "usePreciseCompletions": true,
    "useSelectedCompletion": true,
    "useNewPanel": true
  },
  
  // ============================================
  // Chat Interface Configuration
  // ============================================
  "github.copilot.chat.localeOverride": "en",
  "github.copilot.chat.codeBlock.keepLanguage": true,
  "github.copilot.chat.feedback": true,
  "github.copilot.chat.suggestionsEnabled": true,
  
  // ============================================
  // Keybindings for Copilot
  // ============================================
  "github.copilot.keybindings": {
    "accept": "tab",
    "next": "alt+]",
    "prev": "alt+[",
    "toggle": "ctrl+shift+enter",
    "inlineChat": "ctrl+i",
    "chat": "ctrl+shift+i"
  },
  
  // ============================================
  // Python Development Configuration
  // ============================================
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.terminal.activateEnvInCurrentTerminal": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "88"],
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.linting.pylintEnabled": false,
  
  // ============================================
  // Editor Configuration
  // ============================================
  "editor.formatOnSave": true,
  "editor.formatOnPaste": false,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll": true
  },
  "editor.wordWrap": "on",
  "editor.fontSize": 14,
  "editor.fontFamily": "'Fira Code', 'Cascadia Code', 'Courier New', monospace",
  "editor.fontLigatures": true,
  "editor.lineHeight": 1.6,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.renderWhitespace": "boundary",
  "editor.renderControlCharacters": true,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  
  // ============================================
  // Files and Workspace
  // ============================================
  "files.associations": {
    "CLAUDE.md": "markdown",
    "*.skill.md": "markdown",
    "Dockerfile.*": "dockerfile"
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.coverage": true,
    "**/.mypy_cache": true
  },
  
  // ============================================
  // Git Integration
  // ============================================
  "git.autofetch": true,
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "gitlens.codeLens.enabled": true,
  "gitlens.currentLine.enabled": true,
  "gitlens.hovers.currentLine.over": "line",
  
  // ============================================
  // Terminal Configuration
  // ============================================
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.fontFamily": "'Fira Code', 'Cascadia Code', monospace",
  "terminal.integrated.cursorStyle": "line",
  "terminal.integrated.shellIntegration.enabled": true,
  
  // ============================================
  // Workbench Appearance
  // ============================================
  "workbench.colorTheme": "Default Dark+",
  "workbench.iconTheme": "vscode-icons",
  "workbench.startupEditor": "none",
  "workbench.editor.enablePreview": false,
  
  // ============================================
  // Extensions Recommendations
  // ============================================
  "extensions.ignoreRecommendations": false
}
```

#### Create Custom Keybindings for Copilot

Create `.vscode/keybindings.json`:

```json
[
  // ============================================
  // Copilot Keybindings
  // ============================================
  {
    "key": "tab",
    "command": "editor.action.inlineSuggest.commit",
    "when": "inlineSuggestionVisible && !config.editor.tabCompletion"
  },
  {
    "key": "alt+]",
    "command": "editor.action.inlineSuggest.next",
    "when": "inlineSuggestionVisible"
  },
  {
    "key": "alt+[",
    "command": "editor.action.inlineSuggest.previous",
    "when": "inlineSuggestionVisible"
  },
  {
    "key": "ctrl+shift+enter",
    "command": "github.copilot.toggle",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+i",
    "command": "github.copilot.inlineChat.start",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+i",
    "command": "github.copilot.chat.open",
    "when": "editorTextFocus"
  },
  
  // ============================================
  // Quick Fix and Refactoring
  // ============================================
  {
    "key": "ctrl+.",
    "command": "editor.action.quickFix",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+r",
    "command": "editor.action.refactor",
    "when": "editorTextFocus"
  },
  
  // ============================================
  // Test Execution
  // ============================================
  {
    "key": "ctrl+shift+t",
    "command": "python.runtests",
    "when": "editorTextFocus && editorLangId == 'python'"
  },
  {
    "key": "ctrl+shift+d",
    "command": "workbench.debug.action.toggleRepl",
    "when": "editorTextFocus"
  }
]
```

### Step 2: Create VS Code Tasks for Copilot Integration

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Copilot: Generate Feature",
      "type": "shell",
      "command": "echo 'Generate feature with Copilot'",
      "dependsOn": [],
      "presentation": {
        "reveal": "always",
        "panel": "dedicated",
        "clear": true
      },
      "problemMatcher": []
    },
    {
      "label": "Copilot: Generate Tests",
      "type": "shell",
      "command": "copilot-test-generator ${file}",
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    },
    {
      "label": "Copilot: Review Code",
      "type": "shell",
      "command": "copilot-review ${file}",
      "group": "none",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    },
    {
      "label": "Run All Tests",
      "type": "shell",
      "command": "pytest tests/ -v --cov=src --cov-report=html",
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    },
    {
      "label": "Start Development Server",
      "type": "shell",
      "command": "uvicorn src.main:app --reload --host 0.0.0.0 --port 8000",
      "group": "none",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      },
      "isBackground": true
    },
    {
      "label": "Build Docker Image",
      "type": "shell",
      "command": "docker build -t ${workspaceFolderBasename}:latest .",
      "group": "build",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    }
  ]
}
```

### Step 3: Create VS Code Launch Configuration for Debugging

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI with Copilot",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["src.main:app", "--reload", "--port", "8000"],
      "jinja": true,
      "justMyCode": true,
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    },
    {
      "name": "Python: Pytest",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["${workspaceFolder}/tests", "-v", "--cov=src"],
      "console": "integratedTerminal"
    },
    {
      "name": "Python: Debug with Copilot",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "env": {
        "PYTHONPATH": "${workspaceFolder}",
        "COPILOT_DEBUG": "true"
      },
      "justMyCode": false
    }
  ]
}
```

---

## Part 2: Building Production-Ready Applications

### Step 1: Complete E-Commerce Application with Copilot

Let's build a production-ready e-commerce API using Copilot-assisted development:

```python
# Create the project structure with Copilot assistance
# In VS Code, open Copilot Chat and type:
# "Create a production-ready e-commerce API with FastAPI, including product catalog, orders, users, and authentication"

# Copilot generates the following structure:

"""
ecommerce-api/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   ├── order_service.py
│   │   └── user_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── products.py
│   │   ├── orders.py
│   │   ├── users.py
│   │   └── auth.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   ├── cache.py
│   │   └── logger.py
│   └── middleware/
│       ├── __init__.py
│       ├── auth.py
│       └── rate_limit.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_models.py
│   │   ├── test_services.py
│   │   └── test_schemas.py
│   └── integration/
│       ├── test_api.py
│       └── test_database.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── .vscode/
│   ├── settings.json
│   ├── tasks.json
│   └── launch.json
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── Makefile
├── README.md
└── CLAUDE.md
"""
```

### Step 2: Production-Ready Configuration with Copilot

```python
# File: src/config/settings.py
# Use Copilot to generate production-ready settings with environment validation

from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import Field, validator, EmailStr
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings with environment variable validation."""
    
    # ============================================
    # Application Configuration
    # ============================================
    APP_NAME: str = Field("E-Commerce API", env="APP_NAME")
    APP_VERSION: str = Field("2.0.0", env="APP_VERSION")
    APP_ENV: str = Field("development", env="APP_ENV")
    DEBUG: bool = Field(False, env="DEBUG")
    
    # ============================================
    # Server Configuration
    # ============================================
    HOST: str = Field("0.0.0.0", env="HOST")
    PORT: int = Field(8000, env="PORT")
    WORKERS: int = Field(4, env="WORKERS")
    
    # ============================================
    # Database Configuration
    # ============================================
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    DATABASE_POOL_SIZE: int = Field(20, env="DATABASE_POOL_SIZE")
    DATABASE_MAX_OVERFLOW: int = Field(10, env="DATABASE_MAX_OVERFLOW")
    DATABASE_ECHO: bool = Field(False, env="DATABASE_ECHO")
    
    # ============================================
    # Redis Cache Configuration
    # ============================================
    REDIS_URL: str = Field(..., env="REDIS_URL")
    REDIS_MAX_CONNECTIONS: int = Field(50, env="REDIS_MAX_CONNECTIONS")
    CACHE_TTL: int = Field(3600, env="CACHE_TTL")  # 1 hour
    
    # ============================================
    # Security Configuration
    # ============================================
    SECRET_KEY: str = Field(..., env="SECRET_KEY", min_length=32)
    JWT_ALGORITHM: str = Field("HS256", env="JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(15, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = Field(7, env="JWT_REFRESH_TOKEN_EXPIRE_DAYS")
    PASSWORD_RESET_TOKEN_EXPIRE_HOURS: int = Field(24, env="PASSWORD_RESET_TOKEN_EXPIRE_HOURS")
    
    # ============================================
    # CORS Configuration
    # ============================================
    CORS_ORIGINS: List[str] = Field(
        ["http://localhost:3000", "http://localhost:8000"],
        env="CORS_ORIGINS"
    )
    CORS_CREDENTIALS: bool = Field(True, env="CORS_CREDENTIALS")
    
    # ============================================
    # Rate Limiting
    # ============================================
    RATE_LIMIT_ENABLED: bool = Field(True, env="RATE_LIMIT_ENABLED")
    RATE_LIMIT_REQUESTS: int = Field(100, env="RATE_LIMIT_REQUESTS")
    RATE_LIMIT_PERIOD: int = Field(60, env="RATE_LIMIT_PERIOD")  # seconds
    
    # ============================================
    # Payment Configuration
    # ============================================
    STRIPE_API_KEY: Optional[str] = Field(None, env="STRIPE_API_KEY")
    STRIPE_WEBHOOK_SECRET: Optional[str] = Field(None, env="STRIPE_WEBHOOK_SECRET")
    PAYMENT_SUCCESS_URL: str = Field("/payment/success", env="PAYMENT_SUCCESS_URL")
    PAYMENT_CANCEL_URL: str = Field("/payment/cancel", env="PAYMENT_CANCEL_URL")
    
    # ============================================
    # Email Configuration
    # ============================================
    SMTP_HOST: Optional[str] = Field(None, env="SMTP_HOST")
    SMTP_PORT: int = Field(587, env="SMTP_PORT")
    SMTP_USER: Optional[str] = Field(None, env="SMTP_USER")
    SMTP_PASSWORD: Optional[str] = Field(None, env="SMTP_PASSWORD")
    FROM_EMAIL: EmailStr = Field("noreply@ecommerce.com", env="FROM_EMAIL")
    
    # ============================================
    # Logging Configuration
    # ============================================
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")
    LOG_FORMAT: str = Field("json", env="LOG_FORMAT")
    LOG_FILE: Optional[str] = Field(None, env="LOG_FILE")
    
    # ============================================
    # Validators
    # ============================================
    @validator("DATABASE_URL")
    def validate_database_url(cls, v: str) -> str:
        """Validate database URL format."""
        if not v.startswith(("postgresql://", "postgresql+asyncpg://")):
            raise ValueError("DATABASE_URL must be a PostgreSQL connection string")
        return v
    
    @validator("SECRET_KEY")
    def validate_secret_key(cls, v: str) -> str:
        """Validate secret key strength."""
        if len(v) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters")
        return v
    
    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v):
        """Parse CORS origins from string to list."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
```

### Step 3: Production Database Models

```python
# File: src/models/base.py
# Copilot generates base model with audit fields

from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """Base model with common fields and functionality."""
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    
    @declared_attr
    def __tablename__(cls):
        """Generate table name from class name."""
        return cls.__name__.lower() + "s"
    
    def soft_delete(self):
        """Soft delete the record."""
        self.is_deleted = True
    
    def restore(self):
        """Restore a soft-deleted record."""
        self.is_deleted = False
    
    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
```

```python
# File: src/models/product.py
# Copilot generates product model with relationships

from sqlalchemy import Column, Integer, String, Float, Text, JSON, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import BaseModel

class Product(BaseModel):
    """Product model with catalog information."""
    
    __tablename__ = "products"
    
    name = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    short_description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    compare_at_price = Column(Float, nullable=True)  # Original price for sales
    cost_per_unit = Column(Float, nullable=True)  # For profit calculations
    sku = Column(String(100), unique=True, nullable=False, index=True)
    barcode = Column(String(100), nullable=True)
    stock_quantity = Column(Integer, default=0, nullable=False)
    low_stock_threshold = Column(Integer, default=10)
    weight = Column(Float, nullable=True)  # For shipping calculations
    dimensions = Column(JSON, nullable=True)  # {length, width, height, unit}
    
    # Relationships
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
    
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
    
    # Metadata
    tags = Column(JSON, default=list)  # List of tags
    metadata = Column(JSON, default=dict)  # Additional product attributes
    seo_title = Column(String(255), nullable=True)
    seo_description = Column(String(500), nullable=True)
    
    def is_in_stock(self) -> bool:
        """Check if product is in stock."""
        return self.stock_quantity > 0
    
    def is_low_stock(self) -> bool:
        """Check if product is low on stock."""
        return self.stock_quantity <= self.low_stock_threshold
    
    def update_stock(self, quantity_change: int) -> None:
        """Update stock quantity with validation."""
        new_quantity = self.stock_quantity + quantity_change
        if new_quantity < 0:
            raise ValueError(f"Insufficient stock for product {self.id}")
        self.stock_quantity = new_quantity
```

---

## Part 3: Enterprise Workflows and Team Collaboration

### Step 1: GitHub Actions CI/CD Pipeline

Create `.github/workflows/ci.yml` for continuous integration:

```yaml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: '3.11'
  POETRY_VERSION: '1.4.2'

jobs:
  lint:
    name: Linting
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: |
          pip install black flake8 mypy isort
      
      - name: Check formatting with black
        run: black --check src/ tests/
      
      - name: Check imports with isort
        run: isort --check-only src/ tests/
      
      - name: Lint with flake8
        run: flake8 src/ --count --max-complexity=10 --statistics
      
      - name: Type check with mypy
        run: mypy src/ --ignore-missing-imports

  test:
    name: Testing
    runs-on: ubuntu-latest
    needs: lint
    
    services:
      postgres:
        image: postgres:15-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Cache pip packages
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov pytest-asyncio pytest-mock
      
      - name: Run tests with coverage
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
          REDIS_URL: redis://localhost:6379
          SECRET_KEY: test-secret-key-for-ci-environment
          APP_ENV: testing
        run: |
          pytest tests/ -v --cov=src --cov-report=xml --cov-report=html
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          flags: unittests
          name: codecov-umbrella
          fail_ci_if_error: false

  security:
    name: Security Scan
    runs-on: ubuntu-latest
    needs: test
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install security tools
        run: |
          pip install bandit safety
      
      - name: Run Bandit security scanner
        run: bandit -r src/ -f json -o bandit-report.json || true
      
      - name: Check dependencies for vulnerabilities
        run: safety check -r requirements.txt --json > safety-report.json || true
      
      - name: Upload security reports
        uses: actions/upload-artifact@v3
        with:
          name: security-reports
          path: |
            bandit-report.json
            safety-report.json

  docker:
    name: Docker Build
    runs-on: ubuntu-latest
    needs: [lint, test, security]
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=sha,prefix={{branch}}-
            type=raw,value=latest,enable={{is_default_branch}}
      
      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          build-args: |
            BUILD_VERSION=${{ github.sha }}
            BUILD_DATE=${{ github.event.head_commit.timestamp }}
```

### Step 2: Continuous Deployment Workflow

Create `.github/workflows/cd.yml`:

```yaml
name: CD Pipeline

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

env:
  DOCKER_REGISTRY: ghcr.io
  KUBE_NAMESPACE: ecommerce

jobs:
  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    environment: staging
    if: github.event_name == 'workflow_dispatch' && github.event.inputs.environment == 'staging'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'latest'
      
      - name: Set up Kubernetes config
        run: |
          mkdir -p $HOME/.kube
          echo "${{ secrets.STAGING_KUBE_CONFIG }}" | base64 --decode > $HOME/.kube/config
      
      - name: Deploy to staging
        run: |
          kubectl set image deployment/ecommerce-api \
            ecommerce-api=${{ env.DOCKER_REGISTRY }}/${{ github.repository }}:${{ github.sha }} \
            -n ${{ env.KUBE_NAMESPACE }}
          
          kubectl rollout status deployment/ecommerce-api \
            -n ${{ env.KUBE_NAMESPACE }} \
            --timeout=5m
      
      - name: Run smoke tests
        run: |
          ./scripts/smoke-test.sh https://staging.ecommerce.com
      
      - name: Notify team
        uses: slackapi/slack-github-action@v1.24.0
        with:
          payload: |
            {
              "text": "✅ Staging deployment successful!\nVersion: ${{ github.sha }}\nEnvironment: staging"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}

  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    environment: production
    needs: deploy-staging
    if: startsWith(github.ref, 'refs/tags/v')
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'latest'
      
      - name: Set up Kubernetes config
        run: |
          mkdir -p $HOME/.kube
          echo "${{ secrets.PRODUCTION_KUBE_CONFIG }}" | base64 --decode > $HOME/.kube/config
      
      - name: Database backup
        run: |
          kubectl exec -n ${{ env.KUBE_NAMESPACE }} postgres-0 -- \
            pg_dump -U ecommerce ecommerce > backup-$(date +%Y%m%d-%H%M%S).sql
      
      - name: Canary deployment
        run: |
          # Deploy canary with 10% traffic
          kubectl set image deployment/ecommerce-api-canary \
            ecommerce-api=${{ env.DOCKER_REGISTRY }}/${{ github.repository }}:${{ github.ref_name }} \
            -n ${{ env.KUBE_NAMESPACE }}
          
          kubectl rollout status deployment/ecommerce-api-canary \
            -n ${{ env.KUBE_NAMESPACE }} \
            --timeout=5m
          
          # Wait for canary validation
          echo "Waiting 5 minutes for canary validation..."
          sleep 300
          
          # Full deployment
          kubectl set image deployment/ecommerce-api \
            ecommerce-api=${{ env.DOCKER_REGISTRY }}/${{ github.repository }}:${{ github.ref_name }} \
            -n ${{ env.KUBE_NAMESPACE }}
          
          kubectl rollout status deployment/ecommerce-api \
            -n ${{ env.KUBE_NAMESPACE }} \
            --timeout=5m
      
      - name: Post-deployment validation
        run: |
          ./scripts/validate-deployment.sh https://api.ecommerce.com
      
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: ${{ github.ref_name }}
          name: Release ${{ github.ref_name }}
          generate_release_notes: true
      
      - name: Notify team
        uses: slackapi/slack-github-action@v1.24.0
        with:
          payload: |
            {
              "text": "🚀 Production deployment successful!\nVersion: ${{ github.ref_name }}\nEnvironment: production\nDeployed by: ${{ github.actor }}"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

---

## Part 4: Best Practices and Security Guidelines

### Step 1: Copilot Security Best Practices

Create a team policy for Copilot usage:

```yaml
# .github/COPILOT-POLICY.md

# GitHub Copilot Security and Usage Policy

## Overview
This document outlines best practices for using GitHub Copilot in our organization to ensure code quality, security, and consistency.

## 1. Code Review Requirements

### Mandatory Review
- **All Copilot-generated code must be reviewed** before committing
- Use PR reviews with at least one approver for all changes
- Run security scans on all generated code

### Review Checklist
- [ ] Does the code follow our coding standards?
- [ ] Are there any security vulnerabilities?
- [ ] Are secrets or credentials hardcoded?
- [ ] Does the code include proper error handling?
- [ ] Are there comprehensive tests?

## 2. Security Guidelines

### Never Accept Suggestions For:
```python
# ❌ Never accept:
SECRET_KEY = "hardcoded-secret"
PASSWORD = "password123"
API_KEY = "sk_live_123456"

# ✅ Always use environment variables:
SECRET_KEY = os.getenv("SECRET_KEY")
```

### Sensitive Operations
- Always review authentication and authorization code
- Validate all user inputs in generated code
- Ensure SQL queries use parameterized statements
- Check for proper encryption implementations

## 3. Quality Standards

### Required Patterns
- All functions must include type hints
- Add docstrings for public APIs
- Include error handling for external calls
- Write tests for all new functionality

### Prohibited Patterns
- No `eval()` or `exec()` without review
- No hardcoded secrets or credentials
- No raw SQL queries without parameterization
- No unsafe deserialization

## 4. Team Workflow

### Development Process
1. **Planning**: Use Copilot Chat to discuss architecture
2. **Implementation**: Generate code with Copilot
3. **Review**: PR review with Copilot-assisted review
4. **Testing**: Generate tests with Copilot
5. **Documentation**: Generate API docs with Copilot

### Quality Gates
- ✅ All tests passing
- ✅ Code coverage > 85%
- ✅ Security scan passed
- ✅ Linting passed
- ✅ Type checking passed

## 5. Copilot Configuration

### Required Settings
```json
{
  "github.copilot.advanced.usePreciseCompletions": true,
  "github.copilot.editor.enableCodeActions": true,
  "github.copilot.chat.suggestionsEnabled": true
}
```

### Prohibited Settings
- Disable auto-accept of suggestions
- Require manual trigger for sensitive operations
- Enable audit logging
```

### Step 2: Pre-commit Hooks for Copilot Code

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: copilot-code-review
        name: Copilot Code Review
        entry: python scripts/copilot-review.py
        language: python
        files: \.py$
        stages: [commit]
      
      - id: security-scan
        name: Security Scan
        entry: bandit
        language: system
        files: \.py$
        args: ["-r", "src/", "-f", "json", "-o", "bandit-report.json"]
      
      - id: check-secrets
        name: Check for Secrets
        entry: python scripts/check-secrets.py
        language: python
        files: \.(py|yaml|json|env)$
      
      - id: type-check
        name: Type Check
        entry: mypy
        language: system
        files: \.py$
        args: ["src/", "--ignore-missing-imports"]
```

### Step 3: Secret Detection Script

Create `scripts/check-secrets.py`:

```python
#!/usr/bin/env python3
"""
Pre-commit hook to detect hardcoded secrets in Copilot-generated code.
"""

import re
import sys
from pathlib import Path

# Patterns for detecting potential secrets
SECRET_PATTERNS = [
    # API Keys
    (r'(api[_-]?key|apikey)\s*=\s*["\']([^"\']+)["\']', 'API Key'),
    (r'(sk_live_|pk_live_)[a-zA-Z0-9]+', 'Stripe Live Key'),
    (r'(ghp_|gho_|ghu_|ghs_)[a-zA-Z0-9]+', 'GitHub Token'),
    
    # AWS Credentials
    (r'(aws_access_key_id|AWS_ACCESS_KEY_ID)\s*=\s*["\']([^"\']+)["\']', 'AWS Access Key'),
    (r'(aws_secret_access_key|AWS_SECRET_ACCESS_KEY)\s*=\s*["\']([^"\']+)["\']', 'AWS Secret Key'),
    
    # Database Credentials
    (r'(password|passwd|pwd)\s*=\s*["\']([^"\']+)["\']', 'Database Password'),
    (r'postgresql://[^:]+:([^@]+)@', 'PostgreSQL Password'),
    
    # JWT Tokens
    (r'secret(_key)?\s*=\s*["\']([^"\']{32,})["\']', 'JWT Secret'),
    
    # Generic Secrets
    (r'(token|secret|credential)\s*=\s*["\']([^"\']{16,})["\']', 'Generic Secret'),
]

def scan_file(file_path: Path) -> list:
    """Scan a file for potential secrets."""
    issues = []
    
    try:
        content = file_path.read_text()
        
        for pattern, description in SECRET_PATTERNS:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                line_number = content[:match.start()].count('\n') + 1
                issues.append({
                    'file': file_path,
                    'line': line_number,
                    'pattern': description,
                    'matched': match.group(0)
                })
    except Exception as e:
        print(f"Error scanning {file_path}: {e}")
    
    return issues

def main():
    """Main entry point."""
    files = sys.argv[1:] if len(sys.argv) > 1 else []
    
    if not files:
        files = list(Path('src').rglob('*.py'))
        files.extend(list(Path('tests').rglob('*.py')))
    
    all_issues = []
    
    for file in files:
        file_path = Path(file)
        if file_path.exists():
            issues = scan_file(file_path)
            all_issues.extend(issues)
    
    if all_issues:
        print("\n🔴 Potential secrets found in code:")
        print("=" * 60)
        
        for issue in all_issues:
            print(f"\n📁 {issue['file']}:{issue['line']}")
            print(f"   Pattern: {issue['pattern']}")
            print(f"   Match: {issue['matched'][:50]}...")
        
        print("\n" + "=" * 60)
        print("⚠️  Please remove hardcoded secrets and use environment variables!")
        print("   Never commit secrets to version control.")
        
        sys.exit(1)
    
    print("✅ No secrets detected")
    sys.exit(0)

if __name__ == "__main__":
    main()
```

---

## Part 5: Complete Development Workflow in Action

### Hands-On Session: Building a Production Feature

```bash
# Start VS Code with the project
code ecommerce-api

# Open terminal and start Copilot session
# In VS Code, press Ctrl+Shift+I to open Copilot Chat
```

**Step 1: Plan the Feature with Copilot Chat**

```
> I need to add a product review system with ratings, comments, and moderation.
  Include average rating calculation, review validation, and admin approval workflow.
  Also need API endpoints for CRUD operations and comprehensive tests.

# Copilot Chat responds with plan:

## Feature: Product Review System

### Components:
1. **Models** (src/models/review.py)
   - Review model with rating (1-5), comment, status
   - Relationships with Product and User
   - Average rating calculation

2. **Schemas** (src/schemas/review.py)
   - ReviewCreate, ReviewUpdate, ReviewResponse
   - Validation rules for ratings and comments

3. **Services** (src/services/review_service.py)
   - CRUD operations
   - Moderation workflow
   - Rating aggregation
   - Cache invalidation

4. **API Endpoints** (src/api/reviews.py)
   - GET /products/{id}/reviews
   - POST /products/{id}/reviews
   - PATCH /reviews/{id}
   - DELETE /reviews/{id}
   - POST /reviews/{id}/approve (admin)

5. **Tests** (tests/unit/test_review.py, tests/integration/test_review_api.py)
   - Unit tests for all methods
   - Integration tests for API endpoints
   - Edge cases and validation

### Estimated: 6 files, 800 lines, 45 tests
```

**Step 2: Generate Models with Copilot**

```python
# In VS Code, create new file src/models/review.py
# Copilot generates the model as you type:

from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from src.models.base import BaseModel

class ReviewStatus(enum.Enum):
    """Review moderation status."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FLAGGED = "flagged"

class Review(BaseModel):
    """Product review model with moderation."""
    
    __tablename__ = "reviews"
    
    rating = Column(Integer, nullable=False)
    title = Column(String(200), nullable=True)
    comment = Column(Text, nullable=True)
    status = Column(Enum(ReviewStatus), default=ReviewStatus.PENDING)
    helpful_count = Column(Integer, default=0)
    reported_count = Column(Integer, default=0)
    
    # Foreign keys
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    product = relationship("Product", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
    
    # Moderation fields
    moderated_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    moderated_at = Column(DateTime(timezone=True), nullable=True)
    moderation_note = Column(Text, nullable=True)
    
    def approve(self, moderator_id: int, note: str = None):
        """Approve a review."""
        self.status = ReviewStatus.APPROVED
        self.moderated_by = moderator_id
        self.moderated_at = func.now()
        self.moderation_note = note
        # Update product rating
        self.product.update_average_rating()
    
    def reject(self, moderator_id: int, reason: str):
        """Reject a review."""
        self.status = ReviewStatus.REJECTED
        self.moderated_by = moderator_id
        self.moderated_at = func.now()
        self.moderation_note = reason
    
    def report(self):
        """Flag a review as reported."""
        self.reported_count += 1
        if self.reported_count >= 5:
            self.status = ReviewStatus.FLAGGED
```

**Step 3: Generate Service Layer**

```python
# File: src/services/review_service.py
# Copilot generates complete service:

from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from src.models.review import Review, ReviewStatus
from src.models.product import Product
from src.schemas.review import ReviewCreate, ReviewUpdate, ReviewResponse
from src.core.cache import CacheClient
from src.core.exceptions import NotFoundError, ValidationError, PermissionError
import structlog

logger = structlog.get_logger()

class ReviewService:
    """Service for managing product reviews."""
    
    def __init__(self, db: AsyncSession, cache: CacheClient):
        self.db = db
        self.cache = cache
        self.cache_prefix = "product:reviews:"
        self.cache_ttl = 300  # 5 minutes
    
    async def create_review_async(
        self,
        product_id: int,
        user_id: int,
        review_data: ReviewCreate
    ) -> ReviewResponse:
        """
        Create a new review for a product.
        
        Args:
            product_id: Product being reviewed
            user_id: User creating the review
            review_data: Review data
            
        Returns:
            Created review
            
        Raises:
            NotFoundError: If product not found
            ValidationError: If user already reviewed this product
        """
        logger.info("creating_review", product_id=product_id, user_id=user_id)
        
        # Check if product exists
        product = await self.db.get(Product, product_id)
        if not product:
            raise NotFoundError(f"Product {product_id} not found")
        
        # Check if user already reviewed this product
        stmt = select(Review).where(
            and_(
                Review.product_id == product_id,
                Review.user_id == user_id
            )
        )
        result = await self.db.execute(stmt)
        existing = result.scalar_one_or_none()
        
        if existing:
            raise ValidationError("You have already reviewed this product")
        
        # Create review
        review = Review(
            product_id=product_id,
            user_id=user_id,
            rating=review_data.rating,
            title=review_data.title,
            comment=review_data.comment
        )
        
        self.db.add(review)
        await self.db.commit()
        await self.db.refresh(review)
        
        # Invalidate cache
        await self._invalidate_cache(product_id)
        
        logger.info("review_created", review_id=review.id)
        return ReviewResponse.model_validate(review)
    
    async def get_product_reviews_async(
        self,
        product_id: int,
        status: Optional[ReviewStatus] = None,
        page: int = 1,
        page_size: int = 20
    ) -> Dict[str, Any]:
        """
        Get reviews for a product with pagination.
        
        Args:
            product_id: Product ID
            status: Filter by status (default: approved only)
            page: Page number
            page_size: Items per page
            
        Returns:
            Paginated reviews with metadata
        """
        # Check cache first
        cache_key = f"{self.cache_prefix}{product_id}:{status}:{page}:{page_size}"
        cached = await self.cache.get(cache_key)
        
        if cached:
            logger.info("reviews_cache_hit", product_id=product_id)
            return cached
        
        # Build query
        stmt = select(Review).where(Review.product_id == product_id)
        
        if status:
            stmt = stmt.where(Review.status == status)
        else:
            # Default to approved reviews for public view
            stmt = stmt.where(Review.status == ReviewStatus.APPROVED)
        
        # Get total count
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = await self.db.scalar(count_stmt)
        
        # Apply pagination
        offset = (page - 1) * page_size
        stmt = stmt.offset(offset).limit(page_size)
        stmt = stmt.order_by(Review.created_at.desc())
        
        result = await self.db.execute(stmt)
        reviews = result.scalars().all()
        
        response = {
            "items": [ReviewResponse.model_validate(r) for r in reviews],
            "total": total,
            "page": page,
            "page_size": page_size,
            "has_next": offset + page_size < total
        }
        
        # Cache for future requests
        await self.cache.set(cache_key, response, ex=self.cache_ttl)
        
        return response
    
    async def update_review_async(
        self,
        review_id: int,
        user_id: int,
        review_data: ReviewUpdate,
        is_admin: bool = False
    ) -> ReviewResponse:
        """
        Update a review.
        
        Args:
            review_id: Review ID
            user_id: User making the update
            review_data: Update data
            is_admin: Whether user is admin
            
        Returns:
            Updated review
            
        Raises:
            NotFoundError: If review not found
            PermissionError: If user not authorized
        """
        logger.info("updating_review", review_id=review_id, user_id=user_id)
        
        review = await self.db.get(Review, review_id)
        if not review:
            raise NotFoundError(f"Review {review_id} not found")
        
        # Check permissions
        if not is_admin and review.user_id != user_id:
            raise PermissionError("You don't have permission to update this review")
        
        # Update fields
        update_data = review_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(review, field, value)
        
        await self.db.commit()
        await self.db.refresh(review)
        
        # Invalidate cache
        await self._invalidate_cache(review.product_id)
        
        return ReviewResponse.model_validate(review)
    
    async def delete_review_async(
        self,
        review_id: int,
        user_id: int,
        is_admin: bool = False
    ) -> None:
        """
        Delete a review.
        
        Args:
            review_id: Review ID
            user_id: User making the deletion
            is_admin: Whether user is admin
        """
        logger.info("deleting_review", review_id=review_id, user_id=user_id)
        
        review = await self.db.get(Review, review_id)
        if not review:
            raise NotFoundError(f"Review {review_id} not found")
        
        # Check permissions
        if not is_admin and review.user_id != user_id:
            raise PermissionError("You don't have permission to delete this review")
        
        await self.db.delete(review)
        await self.db.commit()
        
        # Invalidate cache
        await self._invalidate_cache(review.product_id)
    
    async def moderate_review_async(
        self,
        review_id: int,
        moderator_id: int,
        action: str,
        note: str = None
    ) -> ReviewResponse:
        """
        Moderate a review (approve/reject).
        
        Args:
            review_id: Review ID
            moderator_id: Moderator user ID
            action: 'approve' or 'reject'
            note: Moderation note
            
        Returns:
            Updated review
        """
        logger.info("moderating_review", review_id=review_id, moderator_id=moderator_id)
        
        review = await self.db.get(Review, review_id)
        if not review:
            raise NotFoundError(f"Review {review_id} not found")
        
        if action == "approve":
            review.approve(moderator_id, note)
        elif action == "reject":
            review.reject(moderator_id, note)
        else:
            raise ValidationError(f"Invalid action: {action}")
        
        await self.db.commit()
        await self.db.refresh(review)
        
        # Invalidate cache
        await self._invalidate_cache(review.product_id)
        
        return ReviewResponse.model_validate(review)
    
    async def _invalidate_cache(self, product_id: int) -> None:
        """Invalidate all cache keys for a product."""
        pattern = f"{self.cache_prefix}{product_id}:*"
        keys = await self.cache.keys(pattern)
        if keys:
            await self.cache.delete(*keys)
            logger.info("cache_invalidated", product_id=product_id, count=len(keys))
```

**Step 4: Generate Tests**

```python
# File: tests/unit/test_review_service.py
# Copilot generates comprehensive tests:

import pytest
from unittest.mock import AsyncMock, patch
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.review_service import ReviewService
from src.models.review import Review, ReviewStatus
from src.schemas.review import ReviewCreate, ReviewUpdate

class TestReviewService:
    """Test suite for ReviewService."""
    
    @pytest.fixture
    def mock_db(self):
        """Mock database session."""
        return AsyncMock(spec=AsyncSession)
    
    @pytest.fixture
    def mock_cache(self):
        """Mock cache client."""
        return AsyncMock()
    
    @pytest.fixture
    def service(self, mock_db, mock_cache):
        """Create service instance."""
        return ReviewService(mock_db, mock_cache)
    
    @pytest.mark.asyncio
    async def test_create_review_success(self, service, mock_db, mock_cache):
        """Test successful review creation."""
        # Arrange
        product_id = 1
        user_id = 2
        review_data = ReviewCreate(
            rating=5,
            title="Great product!",
            comment="Works perfectly, highly recommend."
        )
        
        mock_product = AsyncMock()
        mock_product.id = product_id
        mock_db.get.return_value = mock_product
        
        mock_review = AsyncMock()
        mock_review.id = 123
        mock_review.product_id = product_id
        mock_review.user_id = user_id
        mock_review.rating = 5
        mock_review.title = "Great product!"
        
        mock_db.add.return_value = None
        mock_db.commit.return_value = None
        mock_db.refresh.return_value = None
        
        # Act
        result = await service.create_review_async(product_id, user_id, review_data)
        
        # Assert
        assert result.id == 123
        assert result.product_id == product_id
        assert result.rating == 5
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_cache.delete.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_create_review_product_not_found(self, service, mock_db):
        """Test review creation with non-existent product."""
        # Arrange
        product_id = 999
        user_id = 2
        review_data = ReviewCreate(rating=5, title="Test")
        
        mock_db.get.return_value = None
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            await service.create_review_async(product_id, user_id, review_data)
        
        assert "not found" in str(exc_info.value).lower()
    
    @pytest.mark.asyncio
    async def test_get_product_reviews_success(self, service, mock_db, mock_cache):
        """Test retrieving product reviews."""
        # Arrange
        product_id = 1
        mock_cache.get.return_value = None  # Cache miss
        
        mock_reviews = [
            AsyncMock(id=1, rating=5, status=ReviewStatus.APPROVED),
            AsyncMock(id=2, rating=4, status=ReviewStatus.APPROVED)
        ]
        
        mock_result = AsyncMock()
        mock_result.scalars.return_value.all.return_value = mock_reviews
        mock_db.execute.return_value = mock_result
        mock_db.scalar.return_value = 2
        
        # Act
        result = await service.get_product_reviews_async(product_id)
        
        # Assert
        assert len(result["items"]) == 2
        assert result["total"] == 2
        assert result["page"] == 1
        assert result["has_next"] is False
        mock_cache.set.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_product_reviews_with_cache(self, service, mock_cache):
        """Test retrieving reviews from cache."""
        # Arrange
        product_id = 1
        cached_data = {
            "items": [],
            "total": 0,
            "page": 1,
            "page_size": 20,
            "has_next": False
        }
        mock_cache.get.return_value = cached_data
        
        # Act
        result = await service.get_product_reviews_async(product_id)
        
        # Assert
        assert result == cached_data
        mock_cache.get.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_update_review_success(self, service, mock_db, mock_cache):
        """Test successful review update."""
        # Arrange
        review_id = 1
        user_id = 2
        update_data = ReviewUpdate(rating=4, comment="Updated review")
        
        mock_review = AsyncMock()
        mock_review.id = review_id
        mock_review.user_id = user_id
        mock_review.product_id = 1
        mock_db.get.return_value = mock_review
        
        # Act
        result = await service.update_review_async(review_id, user_id, update_data)
        
        # Assert
        assert result.rating == 4
        assert result.comment == "Updated review"
        mock_db.commit.assert_called_once()
        mock_cache.delete.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_update_review_permission_denied(self, service, mock_db):
        """Test updating review without permission."""
        # Arrange
        review_id = 1
        user_id = 2  # Different from review owner
        update_data = ReviewUpdate(rating=4)
        
        mock_review = AsyncMock()
        mock_review.id = review_id
        mock_review.user_id = 3  # Different user
        mock_db.get.return_value = mock_review
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            await service.update_review_async(review_id, user_id, update_data)
        
        assert "permission" in str(exc_info.value).lower()
    
    @pytest.mark.asyncio
    async def test_moderate_review_approve(self, service, mock_db, mock_cache):
        """Test approving a review."""
        # Arrange
        review_id = 1
        moderator_id = 10
        mock_review = AsyncMock()
        mock_review.id = review_id
        mock_review.product_id = 1
        mock_db.get.return_value = mock_review
        
        # Act
        result = await service.moderate_review_async(review_id, moderator_id, "approve")
        
        # Assert
        mock_review.approve.assert_called_once_with(moderator_id, None)
        mock_db.commit.assert_called_once()
        mock_cache.delete.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_moderate_review_reject(self, service, mock_db, mock_cache):
        """Test rejecting a review."""
        # Arrange
        review_id = 1
        moderator_id = 10
        note = "Inappropriate content"
        mock_review = AsyncMock()
        mock_review.id = review_id
        mock_review.product_id = 1
        mock_db.get.return_value = mock_review
        
        # Act
        result = await service.moderate_review_async(review_id, moderator_id, "reject", note)
        
        # Assert
        mock_review.reject.assert_called_once_with(moderator_id, note)
        mock_db.commit.assert_called_once()
        mock_cache.delete.assert_called_once()
```

---

## Summary: The Complete GitHub Copilot Experience

```mermaid
mindmap
  root((GitHub Copilot<br/>Production Mastery))
    VS Code Integration
      Custom Settings
      Keybindings
      Tasks & Launch
      Extensions
    Enterprise Workflows
      CI/CD Pipeline
      Security Scanning
      Code Review
      Team Policies
    Best Practices
      Secret Detection
      Pre-commit Hooks
      Quality Gates
      Security Guidelines
    Production Features
      Rate Limiting
      Caching
      Error Handling
      Monitoring
```

### Key Takeaways

| Aspect | Benefit |
|--------|---------|
| **VS Code Integration** | Seamless AI assistance within your IDE |
| **Enterprise Workflows** | Automated CI/CD, security, and quality gates |
| **Security Best Practices** | No secrets, safe code, vulnerability scanning |
| **Team Collaboration** | Consistent patterns, shared configurations |
| **Production Readiness** | Monitoring, logging, error handling |

### Final Command Reference

```bash
# VS Code Shortcuts
Ctrl+Shift+I    # Open Copilot Chat
Ctrl+I          # Inline Chat
Tab             # Accept suggestion
Alt+]/[         # Cycle suggestions

# Git Commands
gh pr create    # Create PR with Copilot description
gh copilot explain  # Explain command
gh copilot suggest  # Suggest command

# Testing
pytest tests/ -v --cov=src
pytest --cov-report=html

# Security
bandit -r src/
safety check -r requirements.txt

# Deployment
kubectl apply -f kubernetes/
kubectl rollout status deployment/ecommerce-api
```

---

## Conclusion: Your AI-Powered Development Future

Throughout this four-part series, we've explored the complete GitHub Copilot ecosystem:

1. **The Intelligence Layer**: Code completion, context awareness, AI suggestions, and learning patterns
2. **The Integration Ecosystem**: IDE support, chat interface, CLI tools, and pull request integration
3. **The Advanced Workflow Engine**: Multi-file editing, test generation, documentation, and refactoring
4. **From Code to Production**: VS Code integration, enterprise workflows, and best practices

These features combine to create a development experience that is:
- **Smarter**: With intelligent completions and context awareness
- **Faster**: With multi-file editing and test generation
- **Safer**: With security scanning and best practices
- **More Collaborative**: With team workflows and consistent patterns
- **Production-Ready**: With CI/CD, monitoring, and deployment automation

```mermaid
graph LR
    subgraph "Your Development Journey"
        A[Start] --> B[Learn Features]
        B --> C[Configure Environment]
        C --> D[Build with Copilot]
        D --> E[Enterprise Workflows]
        E --> F[Production Deploy]
    end
    
    subgraph "GitHub Copilot Evolution"
        G[AI Assistant] --> H[IDE Partner]
        H --> I[Team Collaborator]
        I --> J[Production Platform]
    end
    
    style A fill:#2DA44E,color:#fff
    style F fill:#2DA44E,color:#fff
    style J fill:#2DA44E,color:#fff
```

---

*End of GitHub Copilot Mastery Series*

*Found this helpful? Follow for more deep dives into AI-assisted development, modern architectures, and production best practices.*