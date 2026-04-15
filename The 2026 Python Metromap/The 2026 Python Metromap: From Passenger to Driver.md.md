# The 2026 Python Metromap: From Passenger to Driver

## Series 0: The Map & Mindset | Story 5 of 5

![The 2026 Python Metromap/images/From Passenger to Driver](images/From Passenger to Driver.png)

## 📖 Introduction

**Welcome to the final stop on the Map & Mindset Line.**

You have the map. You understand why old routes fail. You can read the transit system. You know how to avoid derailments. You've built the foundational mindset of a Python programmer.

But knowing how to drive and actually driving are different things.

This story—**The 2026 Python Metromap: From Passenger to Driver**—is your transition from passive learner to active builder. You'll stop riding the trains and start laying the tracks. You'll build a portfolio that proves your skills, not just documents your learning. You'll contribute to open source, share your work, and position yourself for jobs, freelance work, or personal projects.

Most importantly, you'll internalize that mastery isn't a destination—it's a practice. The Python Metromap doesn't end. It evolves as you do.

**Let's put you in the driver's seat.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure. **⬅️ YOU ARE HERE**

---

## 🗺️ A Glance at the Journey Ahead

**Series A: Foundations Station** – 7 stories covering variables, collections, operators, control flow, loops, nested logic, and input/output. You'll build e-commerce tracking, support ticket systems, and batch processors.

**Series B: Functions & Modules Yard** – 6 stories on defining functions, arguments, return values, lambdas, recursion, and modules. You'll create payment processors, report generators, and reusable libraries.

**Series C: Data Structures Express** – 5 stories on lists, tuples, dictionaries, sets, and comprehensions. You'll build todo apps, configuration systems, and recommendation engines.

**Series D: Object-Oriented Programming Line** – 6 stories on classes, constructors, inheritance, polymorphism, encapsulation, and abstraction. You'll create banking systems, vehicle fleets, and payment processors.

**Series E: File & Data Handling Line** – 5 stories on file I/O, CSV/JSON processing, exception handling, context managers, and path management. You'll build log analyzers, backup systems, and data pipelines.

**Series F: Advanced Python Engineering** – 6 stories on decorators, generators, iterators, memory management, testing, and type hints. You'll create authentication middleware, stream processors, and CI/CD pipelines.

**Series G: Data Science & Visualization** – 5 stories on NumPy, Pandas, Matplotlib, Seaborn, and exploratory data analysis. You'll analyze sales data, segment customers, and visualize insights.

**Series H: Web Development & Automation** – 5 stories on Flask, Django, automation, web scraping, and scheduling. You'll build URL shorteners, blog platforms, price monitors, and email bots.

**Series I: AI & Machine Learning with Python** – 4 stories on Scikit-learn, TensorFlow, Keras, and PyTorch. You'll create spam classifiers, image recognizers, and neural networks.

**Series J: Capstone Projects** – 3 stories integrating everything into portfolio-ready applications: expense tracker, weather dashboard, and ML recommendation engine.

---

## 🏗️ Building Your Portfolio

Your portfolio is the bridge between learning and opportunity. It proves you can build, not just understand.

```python
"""
Portfolio Builder System

This module provides a complete system for building, documenting,
and showcasing portfolio projects that prove your Python skills.

Design Pattern: Builder Pattern - constructs portfolio incrementally
Design Principle: Demonstration over Description - show, don't tell
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
from pathlib import Path


class ProjectStatus(Enum):
    """Status of a portfolio project."""
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REFACTORING = "refactoring"
    DEPLOYED = "deployed"


class SkillLevel(Enum):
    """Skill level demonstrated by a project."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


@dataclass
class Project:
    """
    Represents a portfolio project with complete documentation.
    
    This dataclass stores all metadata needed to showcase a project
    professionally, including skills demonstrated, technologies used,
    and links to live demos or source code.
    """
    name: str
    description: str
    skills_demonstrated: List[str]
    series_origin: str
    status: ProjectStatus
    skill_level: SkillLevel
    github_url: Optional[str] = None
    live_demo_url: Optional[str] = None
    completed_date: Optional[datetime] = None
    technologies: List[str] = field(default_factory=list)
    key_features: List[str] = field(default_factory=list)
    challenges_overcome: List[str] = field(default_factory=list)
    
    def to_markdown(self) -> str:
        """
        Convert project to markdown format for README files.
        
        Returns:
            Formatted markdown string suitable for GitHub README
        """
        markdown = f"""
## {self.name}

**Status:** {self.status.value.upper()}  
**Skill Level:** {self.skill_level.value.upper()}  
**Technologies:** {', '.join(self.techneworks)}

### Description
{self.description}

### Key Features
"""
        for feature in self.key_features:
            markdown += f"- {feature}\n"
        
        if self.challenges_overcome:
            markdown += "\n### Challenges Overcome\n"
            for challenge in self.challenges_overcome:
                markdown += f"- {challenge}\n"
        
        if self.github_url:
            markdown += f"\n🔗 [GitHub Repository]({self.github_url})\n"
        
        if self.live_demo_url:
            markdown += f"\n🌐 [Live Demo]({self.live_demo_url})\n"
        
        return markdown


class PortfolioBuilder:
    """
    System for building and managing a programming portfolio.
    
    This class helps you track projects, identify skill gaps,
    and generate professional portfolio documentation.
    
    Design Pattern: Builder Pattern - constructs portfolio incrementally
    """
    
    def __init__(self, owner_name: str, github_username: str):
        """
        Initialize the portfolio builder.
        
        Args:
            owner_name: Your full name for portfolio display
            github_username: Your GitHub username for repository links
        """
        self.owner_name = owner_name
        self.github_username = github_username
        self.projects: List[Project] = []
        self.skills_claimed: Dict[str, SkillLevel] = {}
    
    def add_project(self, project: Project) -> None:
        """
        Add a completed project to the portfolio.
        
        Args:
            project: The Project instance to add
        """
        self.projects.append(project)
        
        # Track skills demonstrated by this project
        for skill in project.skills_demonstrated:
            current = self.skills_claimed.get(skill, SkillLevel.BEGINNER)
            # Upgrade skill level if this project demonstrates higher proficiency
            if self._skill_level_value(project.skill_level) > self._skill_level_value(current):
                self.skills_claimed[skill] = project.skill_level
    
    def _skill_level_value(self, level: SkillLevel) -> int:
        """Convert skill level enum to numeric value for comparison."""
        values = {
            SkillLevel.BEGINNER: 1,
            SkillLevel.INTERMEDIATE: 2,
            SkillLevel.ADVANCED: 3,
            SkillLevel.EXPERT: 4
        }
        return values.get(level, 1)
    
    def create_metromap_portfolio(self, base_path: Path) -> None:
        """
        Create portfolio project folders for each Metromap series.
        
        Args:
            base_path: Directory path where portfolio projects will be created
        """
        portfolio_projects = self._define_portfolio_projects()
        
        for project_def in portfolio_projects:
            # Create folder name from project name (lowercase with underscores)
            folder_name = project_def["name"].replace(" ", "_").lower()
            project_path = base_path / folder_name
            project_path.mkdir(parents=True, exist_ok=True)
            
            # Create standard project structure
            self._create_project_structure(project_path, project_def)
            
            # Create professional README
            self._create_readme(project_path, project_def)
            
            # Create initial code files
            self._create_code_files(project_path, project_def)
            
            print(f"✅ Created portfolio project: {project_def['name']} at {project_path}")
    
    def _define_portfolio_projects(self) -> List[Dict[str, Any]]:
        """
        Define portfolio projects for each Metromap series.
        
        Returns:
            List of project definitions with metadata
        """
        return [
            {
                "name": "E-Commerce Order System",
                "series": "Series A: Foundations",
                "description": "Complete order processing system with cart management, discounts, taxes, and shipping calculations. Demonstrates core Python fundamentals in a real business context.",
                "skills": ["variables", "data types", "operators", "control flow", "loops", "collections"],
                "technologies": ["Python 3.12+"],
                "features": [
                    "Shopping cart with add/remove/update operations",
                    "Percentage and fixed-amount discount codes",
                    "Tax calculation by region",
                    "Order status tracking",
                    "Receipt generation"
                ]
            },
            {
                "name": "Banking System",
                "series": "Series D: OOP",
                "description": "Full banking application with savings, checking, and investment accounts, transfers, and interest calculation. Demonstrates object-oriented programming principles.",
                "skills": ["classes", "inheritance", "polymorphism", "encapsulation", "abstraction"],
                "technologies": ["Python 3.12+"],
                "features": [
                    "Multiple account types with different rules",
                    "Transaction history with rollback capability",
                    "Monthly interest calculation",
                    "Secure fund transfers between accounts",
                    "Account statement generation"
                ]
            },
            {
                "name": "Log Analysis Tool",
                "series": "Series E: File Handling",
                "description": "Production-grade log analyzer that parses server logs, detects errors, and generates comprehensive reports in multiple formats.",
                "skills": ["file I/O", "exception handling", "context managers", "data parsing"],
                "technologies": ["Python 3.12+", "JSON", "CSV"],
                "features": [
                    "Multi-format log parsing (Apache, Nginx, custom)",
                    "Real-time error detection and alerting",
                    "Report generation in JSON, CSV, and HTML",
                    "Pattern matching for anomaly detection",
                    "Historical trend analysis"
                ]
            },
            {
                "name": "URL Shortener API",
                "series": "Series H: Web Development",
                "description": "REST API for URL shortening with analytics, custom slugs, and expiration dates. Deployed with Docker.",
                "skills": ["Flask", "REST APIs", "database", "authentication"],
                "technologies": ["Python", "Flask", "SQLite", "Docker"],
                "features": [
                    "URL shortening with automatic slug generation",
                    "Custom slug support",
                    "Click tracking and analytics",
                    "API key authentication",
                    "Link expiration dates"
                ]
            },
            {
                "name": "Sales Data Analyzer",
                "series": "Series G: Data Science",
                "description": "End-to-end data analysis pipeline for e-commerce sales data with interactive visualizations and customer segmentation.",
                "skills": ["pandas", "numpy", "matplotlib", "seaborn", "data cleaning"],
                "technologies": ["Python", "Pandas", "Matplotlib", "Seaborn", "Jupyter"],
                "features": [
                    "Automated data cleaning and validation",
                    "Sales trend analysis by time period",
                    "Customer segmentation using RFM analysis",
                    "Product performance dashboards",
                    "Exportable reports"
                ]
            },
            {
                "name": "Spam Classifier",
                "series": "Series I: AI/ML",
                "description": "Machine learning model that classifies emails as spam or not spam with high accuracy, deployed as a web API.",
                "skills": ["scikit-learn", "NLP", "model training", "evaluation"],
                "technologies": ["Python", "scikit-learn", "pandas", "Flask", "NLP"],
                "features": [
                    "Text preprocessing and feature extraction",
                    "Multiple algorithm comparison",
                    "Model persistence and loading",
                    "REST API for predictions",
                    "Performance monitoring dashboard"
                ]
            }
        ]
    
    def _create_project_structure(self, project_path: Path, project_def: Dict[str, Any]) -> None:
        """
        Create standard project directory structure.
        
        Args:
            project_path: Path where project will be created
            project_def: Project definition dictionary
        """
        # Create standard subdirectories
        (project_path / "src").mkdir(exist_ok=True)
        (project_path / "tests").mkdir(exist_ok=True)
        (project_path / "docs").mkdir(exist_ok=True)
        (project_path / "data").mkdir(exist_ok=True)
        
        # Create __init__.py files to make src a proper Python package
        (project_path / "src" / "__init__.py").touch()
        (project_path / "tests" / "__init__.py").touch()
    
    def _create_readme(self, project_path: Path, project_def: Dict[str, Any]) -> None:
        """
        Create professional README.md for the project.
        
        Args:
            project_path: Path where README will be created
            project_def: Project definition dictionary
        """
        readme_content = f'''# {project_def["name"]}

## Overview

{project_def["description"]}

**Series:** {project_def["series"]}  
**Technologies:** {', '.join(project_def["technologies"])}

## Features

'''
        for feature in project_def["features"]:
            readme_content += f"- {feature}\n"
        
        readme_content += f'''
## Skills Demonstrated

'''
        for skill in project_def["skills"]:
            readme_content += f"- {skill}\n"
        
        readme_content += '''
## Installation

```bash
# Clone the repository
git clone https://github.com/username/project-name.git

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```python
from src.main import main

# Run the application
main()
```

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

## Project Structure

```
.
├── src/           # Source code
│   └── main.py    # Main application entry point
├── tests/         # Unit tests
├── docs/          # Documentation
├── data/          # Data files
├── requirements.txt  # Python dependencies
└── README.md      # This file
```

## License

MIT

## Author

{self.owner_name}
'''
        
        with open(project_path / "README.md", "w") as f:
            f.write(readme_content)
    
    def _create_code_files(self, project_path: Path, project_def: Dict[str, Any]) -> None:
        """
        Create initial code files for the project.
        
        Args:
            project_path: Path where code files will be created
            project_def: Project definition dictionary
        """
        # Create main.py with template
        main_content = f'''"""
{project_def["name"]}

{project_def["description"]}

This module is part of the 2026 Python Metromap portfolio.
Series: {project_def["series"]}

Design Pattern: [To be implemented based on project requirements]
Design Principle: [To be documented during implementation]
"""

from typing import List, Dict, Any, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Application:
    """
    Main application class for {project_def["name"]}.
    
    This class will be expanded during the implementation phase
    following the story in the Metromap series.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the application.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.initialized = False
        logger.info(f"Initializing {project_def["name"]}")
    
    def initialize(self) -> bool:
        """
        Initialize application resources.
        
        Returns:
            True if initialization successful, False otherwise
        """
        try:
            # Add initialization logic here
            self.initialized = True
            logger.info("Initialization complete")
            return True
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            return False
    
    def run(self) -> Dict[str, Any]:
        """
        Run the main application logic.
        
        Returns:
            Dictionary with execution results
        """
        if not self.initialized:
            logger.warning("Application not initialized. Running initialization.")
            self.initialize()
        
        logger.info("Running application")
        
        # Main application logic will be implemented here
        result = {
            "status": "success",
            "message": f"{project_def["name"]} executed successfully",
            "timestamp": datetime.now().isoformat()
        }
        
        return result


def main() -> None:
    """
    Main entry point for the application.
    
    This function is called when the script is executed directly.
    """
    print(f"Welcome to {project_def["name"]}")
    print("=" * 50)
    
    app = Application()
    
    if app.initialize():
        result = app.run()
        print(f"\nResult: {result['message']}")
    else:
        print("\nFailed to initialize application")
        return


if __name__ == "__main__":
    main()
'''
        
        with open(project_path / "src" / "main.py", "w") as f:
            f.write(main_content)
        
        # Create requirements.txt
        requirements_content = '''# Core dependencies
# Add your project dependencies here

# Example dependencies (uncomment as needed):
# pandas>=2.0.0
# numpy>=1.24.0
# flask>=2.3.0
# requests>=2.31.0

# Development dependencies
pytest>=7.0.0
pytest-cov>=4.0.0
black>=23.0.0
mypy>=1.0.0
ruff>=0.1.0
'''
        
        with open(project_path / "requirements.txt", "w") as f:
            f.write(requirements_content)
        
        # Create a simple test file
        test_content = '''"""
Unit tests for the application.

This module contains tests that verify the correctness
of the application's functionality.
"""

import pytest
from src.main import Application


class TestApplication:
    """Test suite for the Application class."""
    
    def test_initialization(self):
        """Test that application initializes correctly."""
        app = Application()
        assert app.initialized is False
        assert app.initialize() is True
        assert app.initialized is True
    
    def test_run_without_initialization(self):
        """Test that run works even without explicit initialization."""
        app = Application()
        result = app.run()
        assert result["status"] == "success"
        assert "timestamp" in result
    
    def test_custom_config(self):
        """Test that custom configuration is respected."""
        custom_config = {"debug": True, "max_retries": 3}
        app = Application(config=custom_config)
        assert app.config == custom_config
'''
        
        with open(project_path / "tests" / "test_main.py", "w") as f:
            f.write(test_content)
    
    def generate_portfolio_readme(self) -> str:
        """
        Generate a master README for the entire portfolio.
        
        Returns:
            Markdown string for portfolio homepage
        """
        portfolio_readme = f"""# {self.owner_name}'s Python Portfolio

## About Me

Python developer following the 2026 Python Metromap learning journey.
This portfolio demonstrates skills acquired through project-based learning,
with each project mapped to specific Python concepts and real-world use cases.

## Portfolio Projects

"""
        
        for project in self.projects:
            status_emoji = "✅" if project.status == ProjectStatus.COMPLETED else "🔄" if project.status == ProjectStatus.IN_PROGRESS else "📋"
            portfolio_readme += f"### {status_emoji} [{project.name}]({project.github_url or '#'})\n"
            portfolio_readme += f"{project.description}\n\n"
            portfolio_readme += f"**Skills:** {', '.join(project.skills_demonstrated)}\n"
            portfolio_readme += f"**Status:** {project.status.value}\n\n"
        
        portfolio_readme += f"""
## Skills Summary

| Skill | Level |
|-------|-------|
"""
        for skill, level in sorted(self.skills_claimed.items()):
            portfolio_readme += f"| {skill} | {level.value} |\n"
        
        portfolio_readme += """
## Learning Journey

This portfolio was built following the **2026 Python Metromap** curriculum,
a transit-system approach to Python mastery with 52 project-based stories.

### Completed Series

- Series A: Foundations Station (7 stories)
- Series B: Functions & Modules Yard (6 stories)
- Series C: Data Structures Express (5 stories)
- Series D: Object-Oriented Programming Line (6 stories)

### In Progress

- Series E: File & Data Handling Line
- Series F: Advanced Python Engineering

### Upcoming

- Series G: Data Science & Visualization
- Series H: Web Development & Automation
- Series I: AI & Machine Learning
- Series J: Capstone Projects

## Contact

- GitHub: [@{self.github_username}](https://github.com/{self.github_username})
- Email: [your-email@example.com](mailto:your-email@example.com)
- LinkedIn: [Your Profile](https://linkedin.com/in/your-profile)

---
*Built with the 2026 Python Metromap - From Passenger to Driver*
"""
        
        return portfolio_readme
    
    def get_skill_gaps(self) -> List[str]:
        """
        Identify skill gaps based on Metromap curriculum.
        
        Returns:
            List of skills not yet demonstrated in portfolio
        """
        required_skills = [
            "variables", "data types", "operators", "control flow", "loops",
            "functions", "modules", "lists", "dictionaries", "sets", "tuples",
            "classes", "inheritance", "polymorphism", "encapsulation",
            "file I/O", "exception handling", "testing", "APIs", "databases",
            "pandas", "visualization", "machine learning"
        ]
        
        demonstrated = set(self.skills_claimed.keys())
        return [skill for skill in required_skills if skill not in demonstrated]
    
    def print_portfolio_summary(self) -> None:
        """Print a formatted summary of the portfolio."""
        print("\n" + "=" * 60)
        print(f"PORTFOLIO SUMMARY: {self.owner_name}")
        print("=" * 60)
        
        print(f"\n📊 STATISTICS:")
        print(f"   Total projects: {len(self.projects)}")
        print(f"   Skills demonstrated: {len(self.skills_claimed)}")
        
        completed = sum(1 for p in self.projects if p.status == ProjectStatus.COMPLETED)
        in_progress = sum(1 for p in self.projects if p.status == ProjectStatus.IN_PROGRESS)
        
        print(f"   Completed: {completed}")
        print(f"   In progress: {in_progress}")
        
        print(f"\n📂 PROJECTS:")
        for project in self.projects:
            status_icon = "✅" if project.status == ProjectStatus.COMPLETED else "🔄"
            print(f"   {status_icon} {project.name} ({project.skill_level.value})")
        
        gaps = self.get_skill_gaps()
        if gaps:
            print(f"\n📚 SKILL GAPS ({len(gaps)} remaining):")
            for gap in gaps[:5]:
                print(f"   • {gap}")
            if len(gaps) > 5:
                print(f"   • ... and {len(gaps) - 5} more")


class ProjectDocumenter:
    """
    Documentation system for portfolio projects.
    
    This class helps create professional documentation for projects,
    including technical walkthroughs and code comments.
    
    Design Pattern: Decorator Pattern - adds documentation to projects
    """
    
    @staticmethod
    def generate_walkthrough(project: Project) -> str:
        """
        Generate a technical walkthrough for a project.
        
        Args:
            project: Project to document
            
        Returns:
            Markdown walkthrough document
        """
        walkthrough = f"""# Technical Walkthrough: {project.name}

## Overview

{project.description}

**Series Origin:** {project.series_origin}
**Skill Level:** {project.skill_level.value}
**Technologies:** {', '.join(project.technologies)}

## Architecture Overview

The {project.name} follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────┐
│                    Main Application                      │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Module 1  │  │   Module 2  │  │   Module 3  │     │
│  │  (Feature)  │  │  (Feature)  │  │  (Feature)  │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│                    Shared Utilities                      │
└─────────────────────────────────────────────────────────┘
```

## Key Design Decisions

### Decision 1: Modular Design
- **Problem:** Need to support multiple features without code duplication
- **Solution:** Separated concerns into independent modules
- **Alternatives considered:** Monolithic design (rejected due to maintainability)
- **Trade-offs:** More files to manage, but cleaner organization

### Decision 2: Configuration Management
- **Problem:** Different environments need different settings
- **Solution:** External configuration files with environment overrides
- **Alternatives considered:** Hard-coded values (rejected for flexibility)
- **Trade-offs:** Slightly more complex startup, but better deployment

## Key Code Examples

### Example: Core Functionality
```python
def core_functionality(input_data):
    '''
    This function demonstrates the core logic.
    
    Args:
        input_data: The data to process
        
    Returns:
        Processed result
    '''
    # Implementation details go here
    result = process_data(input_data)
    return result
```

## Challenges Overcome

"""
        for challenge in project.challenges_overcome:
            walkthrough += f"### {challenge}\n"
            walkthrough += f"*Solution:* [Detailed solution description]\n\n"
        
        walkthrough += """
## Lessons Learned

1. **Lesson 1:** [What you learned from this project]
2. **Lesson 2:** [Another important insight]
3. **Lesson 3:** [How this changed your approach]

## Future Improvements

- [ ] Improvement 1: [Description]
- [ ] Improvement 2: [Description]
- [ ] Improvement 3: [Description]

## Testing Strategy

The project includes comprehensive tests:
- Unit tests for individual functions
- Integration tests for module interactions
- End-to-end tests for complete workflows

---
*Documentation generated for the 2026 Python Metromap portfolio*
"""
        
        return walkthrough


def demonstrate_portfolio_building():
    """
    Demonstrate building a portfolio from Metromap projects.
    
    This function shows the complete workflow of creating,
    documenting, and presenting portfolio projects.
    """
    print("=" * 60)
    print("DEMONSTRATION: BUILDING YOUR PORTFOLIO")
    print("=" * 60)
    
    # Create portfolio builder
    builder = PortfolioBuilder(
        owner_name="Python Metromap Graduate",
        github_username="metromap-learner"
    )
    
    # Add completed projects
    print("\n1. ADDING PROJECTS TO PORTFOLIO")
    print("-" * 40)
    
    # Add E-Commerce project
    ecommerce = Project(
        name="E-Commerce Order System",
        description="Complete order processing system with cart management, discounts, taxes, and shipping calculations.",
        skills_demonstrated=["variables", "data types", "operators", "control flow", "loops", "collections"],
        series_origin="Series A: Foundations",
        status=ProjectStatus.COMPLETED,
        skill_level=SkillLevel.INTERMEDIATE,
        technologies=["Python 3.12+"],
        key_features=[
            "Shopping cart with quantity updates",
            "Discount code system with percentage and fixed amounts",
            "Tax calculation by region",
            "Order history tracking",
            "Receipt generation"
        ],
        challenges_overcome=[
            "Handling edge cases in discount stacking",
            "Optimizing cart recalculation for large carts",
            "Managing decimal precision for currency"
        ]
    )
    builder.add_project(ecommerce)
    print(f"   ✅ Added: {ecommerce.name}")
    
    # Add Banking System
    banking = Project(
        name="Banking System",
        description="Full banking application with savings, checking, and investment accounts, transfers, and interest calculation.",
        skills_demonstrated=["classes", "inheritance", "polymorphism", "encapsulation", "abstraction"],
        series_origin="Series D: OOP",
        status=ProjectStatus.COMPLETED,
        skill_level=SkillLevel.INTERMEDIATE,
        technologies=["Python 3.12+"],
        key_features=[
            "Multiple account types with different rules",
            "Transaction history with rollback capability",
            "Monthly interest calculation",
            "Secure fund transfers between accounts",
            "Account statement generation"
        ],
        challenges_overcome=[
            "Designing clean inheritance hierarchy",
            "Ensuring transaction atomicity",
            "Preventing floating point errors in financial calculations"
        ]
    )
    builder.add_project(banking)
    print(f"   ✅ Added: {banking.name}")
    
    # Add Log Analyzer
    log_analyzer = Project(
        name="Log Analysis Tool",
        description="Production-grade log analyzer that parses server logs, detects errors, and generates reports.",
        skills_demonstrated=["file I/O", "exception handling", "context managers", "data parsing"],
        series_origin="Series E: File Handling",
        status=ProjectStatus.COMPLETED,
        skill_level=SkillLevel.INTERMEDIATE,
        technologies=["Python 3.12+", "JSON", "CSV", "Regex"],
        key_features=[
            "Multi-format log parsing",
            "Real-time error detection",
            "Report generation in multiple formats",
            "Pattern matching for anomalies"
        ],
        challenges_overcome=[
            "Handling malformed log entries gracefully",
            "Processing large files without memory issues",
            "Creating efficient pattern matching"
        ]
    )
    builder.add_project(log_analyzer)
    print(f"   ✅ Added: {log_analyzer.name}")
    
    # Print portfolio summary
    builder.print_portfolio_summary()
    
    # Generate portfolio README
    print("\n2. GENERATING PORTFOLIO README")
    print("-" * 40)
    
    portfolio_readme = builder.generate_portfolio_readme()
    print(f"   Portfolio README generated ({len(portfolio_readme)} characters)")
    print("\n   Preview:")
    print(portfolio_readme[:600] + "...\n")
    
    # Generate project documentation
    print("\n3. PROJECT DOCUMENTATION")
    print("-" * 40)
    
    docer = ProjectDocumenter()
    walkthrough = docer.generate_walkthrough(ecommerce)
    print(f"   Generated technical walkthrough for {ecommerce.name}")
    print(f"   Document length: {len(walkthrough)} characters")
    
    print("\n" + "=" * 60)
    print("PORTFOLIO BUILDING CHECKLIST")
    print("=" * 60)
    
    checklist = [
        "✓ Create GitHub repository for each project",
        "✓ Write professional README with setup instructions",
        "✓ Add screenshots or demo GIFs to README",
        "✓ Write unit tests with >80% coverage",
        "✓ Add type hints to all functions",
        "✓ Document design decisions in code comments",
        "✓ Create technical walkthrough for complex projects",
        "✓ Deploy live demo where possible (Render, Vercel, etc.)",
        "✓ Add projects to LinkedIn 'Projects' section",
        "✓ Share projects on Twitter/LinkedIn with #Python",
        "✓ Include project links in your resume",
        "✓ Keep portfolio updated as you learn new skills"
    ]
    
    for item in checklist:
        print(f"   {item}")
    
    print("\n💡 PORTFOLIO BEST PRACTICES:")
    print("   • Quality over quantity: 3 great projects > 10 mediocre ones")
    print("   • Show problem-solving, not just syntax")
    print("   • Include READMEs that explain the 'why' not just the 'how'")
    print("   • Keep code clean, well-commented, and consistent")
    print("   • Demonstrate testing and documentation skills")
    print("   • Link projects together in your narrative")
    print("   • Update projects as you learn better approaches")


def demonstrate_project_scaffolding():
    """
    Demonstrate creating project folders for all Metromap portfolio projects.
    
    This shows how to create the complete project structure
    for all portfolio projects at once.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION: CREATING PROJECT FOLDERS")
    print("=" * 60)
    
    # Create temporary directory for demonstration
    import tempfile
    
    with tempfile.TemporaryDirectory() as temp_dir:
        portfolio_path = Path(temp_dir) / "python-portfolio"
        
        print(f"\n📁 Creating portfolio at: {portfolio_path}")
        
        builder = PortfolioBuilder(
            owner_name="Python Metromap Graduate",
            github_username="metromap-learner"
        )
        
        builder.create_metromap_portfolio(portfolio_path)
        
        print(f"\n✅ Portfolio created successfully!")
        print(f"\n📂 Portfolio structure:")
        
        # List created folders
        for item in portfolio_path.iterdir():
            if item.is_dir():
                print(f"   📁 {item.name}/")
                # List subdirectories
                for subitem in item.iterdir():
                    if subitem.is_dir():
                        print(f"      📁 {subitem.name}/")
                    elif subitem.suffix == ".md":
                        print(f"      📄 {subitem.name}")
                    elif subitem.suffix == ".txt":
                        print(f"      📄 {subitem.name}")
                    elif subitem.suffix == ".py":
                        print(f"      🐍 {subitem.name}")


if __name__ == "__main__":
    demonstrate_portfolio_building()
    demonstrate_project_scaffolding()
```

---

## 🌍 Contributing to Open Source

Contributing to existing projects builds real-world experience and community credibility.

```python
"""
Open Source Contribution Guide

This module guides you through making your first open source contributions,
from finding good first issues to submitting pull requests.

Design Pattern: Guide Pattern - provides structured workflow
Design Principle: Start Small - first contributions should be low-risk
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ContributionType(Enum):
    """Types of open source contributions ordered by difficulty."""
    DOCUMENTATION = "documentation"      # Easiest - fixing typos, improving docs
    TESTING = "testing"                  # Easy - writing or fixing tests
    BUG_FIX = "bug_fix"                  # Medium - fixing reported bugs
    EXAMPLE = "example_code"             # Medium - adding usage examples
    CODE_REVIEW = "code_review"          # Medium-advanced - reviewing others' code
    FEATURE = "feature"                  # Advanced - adding new functionality


@dataclass
class Contribution:
    """Records an open source contribution with metadata."""
    project_name: str
    contribution_type: ContributionType
    description: str
    pr_url: Optional[str] = None
    issue_number: Optional[int] = None
    merged: bool = False
    merged_date: Optional[datetime] = None
    lessons_learned: List[str] = None


class OpenSourceGuide:
    """
    Complete guide for making first open source contributions.
    
    This class provides workflows, checklists, and best practices
    for contributing to open source projects effectively.
    
    Design Principle: Progressive Difficulty - start with easy contributions
    """
    
    @staticmethod
    def find_good_first_issues(repo_url: str) -> List[Dict[str, Any]]:
        """
        Find good first issues in a repository.
        
        Args:
            repo_url: GitHub repository URL
            
        Returns:
            List of good first issues with metadata
        """
        # In production, this would use GitHub API
        # For demonstration, return template with realistic examples
        return [
            {
                "title": "Fix typo in README documentation",
                "labels": ["good first issue", "documentation"],
                "estimated_time": "15 minutes",
                "difficulty": "very easy",
                "skills_needed": ["attention to detail", "basic markdown"]
            },
            {
                "title": "Add missing docstring to utility function",
                "labels": ["good first issue", "documentation"],
                "estimated_time": "20 minutes",
                "difficulty": "very easy",
                "skills_needed": ["Python basics", "docstring format"]
            },
            {
                "title": "Improve error message for invalid input",
                "labels": ["good first issue", "enhancement"],
                "estimated_time": "30 minutes",
                "difficulty": "easy",
                "skills_needed": ["exception handling", "user experience"]
            },
            {
                "title": "Add unit test for edge case",
                "labels": ["good first issue", "testing"],
                "estimated_time": "45 minutes",
                "difficulty": "easy",
                "skills_needed": ["pytest", "edge case thinking"]
            }
        ]
    
    @staticmethod
    def contribution_workflow() -> Dict[str, List[str]]:
        """
        Get step-by-step contribution workflow.
        
        Returns:
            Workflow steps organized by phase
        """
        return {
            "preparation": [
                "1. Find a project you actively use and appreciate",
                "2. Read the project's CONTRIBUTING.md guidelines",
                "3. Set up the development environment locally",
                "4. Run existing tests to ensure everything works",
                "5. Build the project to verify your setup"
            ],
            "finding_issues": [
                "6. Look for 'good first issue' or 'help wanted' labels",
                "7. Read the issue carefully and understand the problem",
                "8. Comment on the issue that you're working on it",
                "9. Ask clarifying questions if anything is unclear"
            ],
            "implementation": [
                "10. Create a new branch with descriptive name (fix/issue-number-description)",
                "11. Write code following project style guide",
                "12. Add tests for your changes",
                "13. Run existing tests to ensure nothing broke",
                "14. Update documentation if needed"
            ],
            "submission": [
                "15. Commit with clear message: 'Fix #123: Description of fix'",
                "16. Push to your fork of the repository",
                "17. Open Pull Request against the main repository",
                "18. Link the issue number in PR description",
                "19. Fill out the PR template completely",
                "20. Request review from maintainers"
            ],
            "post_submission": [
                "21. Respond to review feedback promptly",
                "22. Make requested changes in additional commits",
                "23. Once approved, your PR will be merged",
                "24. Celebrate! You've contributed to open source!",
                "25. Look for another issue to contribute to"
            ]
        }
    
    @staticmethod
    def code_review_checklist() -> List[str]:
        """
        Checklist for reviewing your own code before submitting PR.
        
        Returns:
            Self-review checklist items
        """
        return [
            "✓ Code follows project style guide (PEP 8 for Python)",
            "✓ Added or updated tests for all changes",
            "✓ All tests pass locally",
            "✓ Documentation updated to reflect changes",
            "✓ No commented-out debugging code remains",
            "✓ No print statements left in production code",
            "✓ Variable names are descriptive and clear",
            "✓ Functions have docstrings explaining purpose",
            "✓ Error messages are user-friendly and clear",
            "✓ No unnecessary dependencies added",
            "✓ Changes are focused (one PR per feature/fix)",
            "✓ Commit messages are clear and follow convention"
        ]
    
    @staticmethod
    def popular_python_projects_for_beginners() -> List[Dict[str, str]]:
        """
        List of beginner-friendly Python projects.
        
        Returns:
            List of projects with labels for beginners
        """
        return [
            {
                "name": "pandas",
                "description": "Data analysis library",
                "beginner_areas": ["documentation", "examples", "error messages"],
                "labels_to_look_for": ["good first issue", "docs"]
            },
            {
                "name": "scikit-learn",
                "description": "Machine learning library",
                "beginner_areas": ["documentation", "examples", "tests"],
                "labels_to_look_for": ["good first issue", "documentation"]
            },
            {
                "name": "requests",
                "description": "HTTP library",
                "beginner_areas": ["documentation", "type hints", "tests"],
                "labels_to_look_for": ["good first issue", "help wanted"]
            },
            {
                "name": "pytest",
                "description": "Testing framework",
                "beginner_areas": ["documentation", "examples", "plugins"],
                "labels_to_look_for": ["good first issue", "docs"]
            },
            {
                "name": "Flask",
                "description": "Web framework",
                "beginner_areas": ["documentation", "examples", "tutorials"],
                "labels_to_look_for": ["good first issue", "documentation"]
            }
        ]


class ContributionTracker:
    """
    Tracks open source contributions over time.
    
    This class helps maintain momentum by tracking contributions,
    building streaks, and identifying contribution patterns.
    
    Design Pattern: Tracker Pattern - monitors progress over time
    """
    
    def __init__(self):
        """Initialize the contribution tracker."""
        self.contributions: List[Contribution] = []
        self.current_streak = 0
        self.longest_streak = 0
        self.last_contribution_date: Optional[datetime] = None
    
    def add_contribution(self, contribution: Contribution) -> None:
        """
        Record a contribution.
        
        Args:
            contribution: Contribution to record
        """
        self.contributions.append(contribution)
        self._update_streak(contribution)
    
    def _update_streak(self, contribution: Contribution) -> None:
        """
        Update contribution streak based on contribution date.
        
        Args:
            contribution: Most recent contribution
        """
        if contribution.merged_date:
            if self.last_contribution_date:
                days_diff = (contribution.merged_date - self.last_contribution_date).days
                if days_diff <= 1:
                    self.current_streak += 1
                else:
                    self.current_streak = 1
            else:
                self.current_streak = 1
            
            self.last_contribution_date = contribution.merged_date
            
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive contribution summary.
        
        Returns:
            Dictionary with contribution statistics
        """
        return {
            "total_contributions": len(self.contributions),
            "merged_count": sum(1 for c in self.contributions if c.merged),
            "acceptance_rate": (sum(1 for c in self.contributions if c.merged) / len(self.contributions)) * 100 if self.contributions else 0,
            "by_type": {
                ct.value: sum(1 for c in self.contributions if c.contribution_type == ct)
                for ct in ContributionType
            },
            "current_streak": self.current_streak,
            "longest_streak": self.longest_streak
        }
    
    def print_summary(self) -> None:
        """Print formatted contribution summary."""
        summary = self.get_summary()
        
        print("\n" + "=" * 60)
        print("OPEN SOURCE CONTRIBUTION SUMMARY")
        print("=" * 60)
        
        print(f"\n📊 STATISTICS:")
        print(f"   Total contributions: {summary['total_contributions']}")
        print(f"   Merged: {summary['merged_count']}")
        print(f"   Acceptance rate: {summary['acceptance_rate']:.1f}%")
        print(f"   Current streak: {summary['current_streak']} contributions")
        print(f"   Longest streak: {summary['longest_streak']}")
        
        print(f"\n📂 BY TYPE:")
        for contrib_type, count in summary['by_type'].items():
            if count > 0:
                bar_length = min(20, count * 2)
                bar = "█" * bar_length + "░" * (20 - bar_length)
                print(f"   {contrib_type:15} [{bar}] {count}")
    
    def get_next_recommendation(self) -> str:
        """
        Get recommendation for next contribution type.
        
        Returns:
            Recommendation string
        """
        summary = self.get_summary()
        
        # Find least-contributed type
        min_type = min(summary['by_type'].items(), key=lambda x: x[1])
        
        if min_type[1] == 0:
            return f"Try making a {min_type[0]} contribution to diversify your experience."
        elif summary['merged_count'] < 3:
            return "Focus on documentation fixes to build confidence and reputation."
        elif summary['acceptance_rate'] < 70:
            return "Review the contribution guidelines and ensure tests pass before submitting."
        else:
            return "Great work! Consider taking on a bug fix or small feature next."


def demonstrate_open_source():
    """
    Demonstrate open source contribution workflow and tracking.
    """
    print("=" * 60)
    print("DEMONSTRATION: OPEN SOURCE CONTRIBUTIONS")
    print("=" * 60)
    
    # Show workflow
    print("\n1. CONTRIBUTION WORKFLOW")
    print("-" * 40)
    
    workflow = OpenSourceGuide.contribution_workflow()
    
    for phase, steps in workflow.items():
        print(f"\n{phase.upper()}:")
        for step in steps:
            print(f"   {step}")
    
    # Find good first issues
    print("\n2. FINDING GOOD FIRST ISSUES")
    print("-" * 40)
    
    issues = OpenSourceGuide.find_good_first_issues("https://github.com/example/project")
    for issue in issues:
        print(f"\n   📌 {issue['title']}")
        print(f"      Labels: {', '.join(issue['labels'])}")
        print(f"      Estimated time: {issue['estimated_time']}")
        print(f"      Difficulty: {issue['difficulty']}")
        print(f"      Skills needed: {', '.join(issue['skills_needed'])}")
    
    # Beginner-friendly projects
    print("\n3. BEGINNER-FRIENDLY PYTHON PROJECTS")
    print("-" * 40)
    
    projects = OpenSourceGuide.popular_python_projects_for_beginners()
    for project in projects:
        print(f"\n   📦 {project['name']}: {project['description']}")
        print(f"      Good starting areas: {', '.join(project['beginner_areas'])}")
        print(f"      Look for labels: {', '.join(project['labels_to_look_for'])}")
    
    # Self-review checklist
    print("\n4. SELF-REVIEW CHECKLIST")
    print("-" * 40)
    
    checklist = OpenSourceGuide.code_review_checklist()
    for item in checklist:
        print(f"   {item}")
    
    # Track contributions
    print("\n5. CONTRIBUTION TRACKING")
    print("-" * 40)
    
    tracker = ContributionTracker()
    
    # Simulate contributions over time
    from datetime import timedelta
    
    today = datetime.now()
    
    # First contribution - documentation
    contrib1 = Contribution(
        project_name="pandas",
        contribution_type=ContributionType.DOCUMENTATION,
        description="Fixed typo in docstring of read_csv function",
        pr_url="https://github.com/pandas-dev/pandas/pull/12345",
        issue_number=12344,
        merged=True,
        merged_date=today - timedelta(days=5),
        lessons_learned=["Always read full contribution guide", "Small PRs get merged faster"]
    )
    tracker.add_contribution(contrib1)
    
    # Second contribution - testing
    contrib2 = Contribution(
        project_name="requests",
        contribution_type=ContributionType.TESTING,
        description="Added test for URL encoding edge case",
        pr_url="https://github.com/psf/requests/pull/6789",
        issue_number=6788,
        merged=True,
        merged_date=today - timedelta(days=3),
        lessons_learned=["Edge cases matter", "Parameterized tests reduce duplication"]
    )
    tracker.add_contribution(contrib2)
    
    # Third contribution - bug fix
    contrib3 = Contribution(
        project_name="pytest",
        contribution_type=ContributionType.BUG_FIX,
        description="Fixed assertion message formatting for multiline strings",
        pr_url="https://github.com/pytest-dev/pytest/pull/9876",
        issue_number=9875,
        merged=False,  # Still in review
        lessons_learned=["Bug fixes require careful testing", "Explain the 'why' in PR description"]
    )
    tracker.add_contribution(contrib3)
    
    tracker.print_summary()
    
    print(f"\n🎯 NEXT RECOMMENDATION:")
    print(f"   {tracker.get_next_recommendation()}")
    
    print("\n💡 OPEN SOURCE BEST PRACTICES:")
    print("   • Start with documentation (lowest risk, high value)")
    print("   • Fix bugs you encounter while using the library")
    print("   • Write tests for functions that lack coverage")
    print("   • Update examples when you find outdated code")
    print("   • Be responsive to reviewer feedback (within 24-48 hours)")
    print("   • Don't take rejection personally—iterate based on feedback")
    print("   • Build relationships with maintainers over time")
    print("   • Celebrate your first merged PR—it's a big deal!")


if __name__ == "__main__":
    demonstrate_open_source()
```

---

## 📝 The Job Search: Positioning Yourself

Your portfolio and contributions create the evidence employers need.

```python
"""
Job Search Positioning System

This module helps position your Python skills for job opportunities
by mapping Metromap learning to role requirements and preparing
interview materials.

Design Pattern: Strategy Pattern - different strategies for different roles
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class JobRole(Enum):
    """Python job roles with different skill requirements."""
    JUNIOR_DEVELOPER = "Junior Python Developer"
    DATA_ANALYST = "Data Analyst"
    BACKEND_ENGINEER = "Backend Engineer"
    DEVOPS_ENGINEER = "DevOps Engineer"
    DATA_SCIENTIST = "Data Scientist"
    ML_ENGINEER = "Machine Learning Engineer"
    FULL_STACK = "Full Stack Developer"


@dataclass
class InterviewAnswer:
    """STAR method interview answer structure."""
    situation: str
    task: str
    action: str
    result: str
    metrics: Optional[str] = None
    
    def to_star(self) -> str:
        """Format as complete STAR answer."""
        star = f"""**Situation:** {self.situation}
**Task:** {self.task}
**Action:** {self.action}
**Result:** {self.result}"""
        if self.metrics:
            star += f"\n**Metrics:** {self.metrics}"
        return star


class JobPositioner:
    """
    Positions your Metromap journey for specific job roles.
    
    This class maps completed Metromap series to job requirements
    and helps prepare application materials.
    
    Design Principle: Evidence-Based - map learning to job requirements
    """
    
    @staticmethod
    def get_role_requirements(role: JobRole) -> List[str]:
        """
        Get typical requirements for a job role.
        
        Args:
            role: Target job role
            
        Returns:
            List of requirement descriptions
        """
        requirements_map = {
            JobRole.JUNIOR_DEVELOPER: [
                "Python fundamentals and syntax",
                "Understanding of core data structures (lists, dicts, sets)",
                "Basic object-oriented programming knowledge",
                "Git version control workflow",
                "Problem-solving and debugging skills",
                "Ability to read and understand code"
            ],
            JobRole.DATA_ANALYST: [
                "Python fundamentals",
                "Pandas proficiency for data manipulation",
                "SQL for database querying",
                "Data visualization with Matplotlib/Seaborn",
                "Statistical thinking and basic statistics",
                "Jupyter notebooks for analysis"
            ],
            JobRole.BACKEND_ENGINEER: [
                "Advanced Python features (decorators, generators)",
                "API development (Flask, FastAPI, or Django)",
                "Database design and ORM usage",
                "Testing and debugging practices",
                "System design fundamentals",
                "RESTful API design principles"
            ],
            JobRole.DATA_SCIENTIST: [
                "Advanced Python for data science",
                "Machine learning (scikit-learn)",
                "Statistical modeling and inference",
                "Data wrangling with Pandas",
                "Model evaluation and selection",
                "Feature engineering techniques"
            ],
            JobRole.ML_ENGINEER: [
                "Expert Python skills",
                "Deep learning frameworks (PyTorch or TensorFlow)",
                "MLOps and model deployment",
                "Performance optimization",
                "Distributed training concepts",
                "Model monitoring and maintenance"
            ]
        }
        
        return requirements_map.get(role, ["Python fundamentals"])
    
    @staticmethod
    def map_metromap_to_role(role: JobRole, completed_series: List[str]) -> Dict[str, Any]:
        """
        Map completed Metromap series to job role requirements.
        
        Args:
            role: Target job role
            completed_series: List of completed Metromap series
            
        Returns:
            Mapping of requirements to evidence
        """
        # Define series to requirement mapping
        series_evidence = {
            "Series A": ["Python fundamentals", "variables", "control flow", "loops"],
            "Series B": ["functions", "modules", "code organization"],
            "Series C": ["data structures", "lists", "dictionaries", "sets"],
            "Series D": ["OOP", "classes", "inheritance", "encapsulation"],
            "Series E": ["file I/O", "exception handling", "data parsing"],
            "Series F": ["decorators", "generators", "testing", "type hints"],
            "Series G": ["pandas", "numpy", "visualization", "data analysis"],
            "Series H": ["APIs", "Flask", "Django", "automation"],
            "Series I": ["machine learning", "scikit-learn", "TensorFlow", "PyTorch"]
        }
        
        # Calculate evidence
        evidence = []
        for series in completed_series:
            if series in series_evidence:
                evidence.extend(series_evidence[series])
        
        # Get role requirements
        requirements = JobPositioner.get_role_requirements(role)
        
        # Map requirements to evidence
        mapping = {
            "role": role.value,
            "completed_series": completed_series,
            "requirements_met": requirements[:len(evidence) // 2] if evidence else [],
            "gaps": requirements[len(evidence) // 2:] if len(requirements) > len(evidence) // 2 else [],
            "recommended_next_series": JobPositioner._recommend_next_series(role, completed_series)
        }
        
        return mapping
    
    @staticmethod
    def _recommend_next_series(role: JobRole, completed_series: List[str]) -> List[str]:
        """Recommend next Metromap series based on role and progress."""
        role_priorities = {
            JobRole.JUNIOR_DEVELOPER: ["Series B", "Series D", "Series F"],
            JobRole.DATA_ANALYST: ["Series G", "Series E", "Series I.1"],
            JobRole.BACKEND_ENGINEER: ["Series H", "Series F", "Series D"],
            JobRole.DATA_SCIENTIST: ["Series I", "Series G", "Series F"],
            JobRole.ML_ENGINEER: ["Series I", "Series F", "Series H"]
        }
        
        priorities = role_priorities.get(role, ["Series B", "Series C"])
        return [p for p in priorities if p not in completed_series]
    
    @staticmethod
    def generate_resume_bullet(
        project_name: str, 
        accomplishment: str, 
        metric: Optional[str] = None,
        technology: Optional[str] = None
    ) -> str:
        """
        Generate resume bullet point from portfolio project.
        
        Args:
            project_name: Name of the project
            accomplishment: What you accomplished
            metric: Optional quantitative metric
            technology: Optional technology used
            
        Returns:
            Resume-ready bullet point
        """
        bullet = f"• {project_name}: {accomplishment}"
        if technology:
            bullet += f" using {technology}"
        if metric:
            bullet += f" ({metric})"
        return bullet
    
    @staticmethod
    def prepare_interview_answers(projects: List[Dict[str, Any]]) -> Dict[str, InterviewAnswer]:
        """
        Prepare STAR method answers for common interview questions.
        
        Args:
            projects: List of projects with details
            
        Returns:
            Dictionary mapping question types to STAR answers
        """
        answers = {}
        
        for project in projects:
            # Answer for "Tell me about a challenging project"
            answers["challenge"] = InterviewAnswer(
                situation=f"Needed to build {project['name']} to solve {project.get('problem', 'a business problem')}",
                task=f"Implement {project.get('key_feature', 'core functionality')} with constraints on {project.get('constraints', 'time and quality')}",
                action=f"Designed modular architecture, wrote tests, iterated based on feedback. {project.get('technical_approach', 'Followed best practices')}",
                result=f"Successfully delivered {project['name']} with {project.get('outcome', 'positive results')}",
                metrics=project.get('metrics')
            )
            
            # Answer for "How do you handle errors?"
            answers["errors"] = InterviewAnswer(
                situation="Encountered unexpected errors during development",
                task="Implement robust error handling without breaking user experience",
                action="Used try-except blocks, logged errors, added retry logic, and provided user-friendly messages",
                result="System handled errors gracefully with 99.9% uptime",
                metrics="Reduced crash reports by 75%"
            )
            
            # Answer for "How do you learn new technologies?"
            answers["learning"] = InterviewAnswer(
                situation="Needed to learn new technology for project requirement",
                task="Rapidly acquire and apply new skills",
                action="Followed project-based learning approach from 2026 Python Metromap, built small prototypes first",
                result="Delivered project on schedule with new technology stack",
                metrics="Learned framework in 2 weeks, delivered 3 features ahead of schedule"
            )
            
            break  # Just use first project for demonstration
        
        return answers


class JobApplicationTracker:
    """
    Tracks job applications and interviews.
    
    Design Pattern: Tracker Pattern - monitors job search progress
    """
    
    def __init__(self):
        """Initialize the job application tracker."""
        self.applications: List[Dict[str, Any]] = []
        self.interviews: List[Dict[str, Any]] = []
    
    def add_application(self, company: str, role: str, date: datetime, status: str = "applied") -> None:
        """
        Add a job application to tracking.
        
        Args:
            company: Company name
            role: Job role
            date: Application date
            status: Current status
        """
        self.applications.append({
            "company": company,
            "role": role,
            "date": date,
            "status": status,
            "follow_ups": []
        })
    
    def add_interview(self, company: str, interview_type: str, date: datetime, preparation_notes: str = "") -> None:
        """
        Add an interview to tracking.
        
        Args:
            company: Company name
            interview_type: Phone screen, technical, onsite, etc.
            date: Interview date
            preparation_notes: Notes for preparation
        """
        self.interviews.append({
            "company": company,
            "type": interview_type,
            "date": date,
            "preparation_notes": preparation_notes,
            "completed": False
        })
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get application statistics."""
        return {
            "total_applications": len(self.applications),
            "applications_by_status": {
                status: sum(1 for a in self.applications if a["status"] == status)
                for status in set(a["status"] for a in self.applications)
            },
            "total_interviews": len(self.interviews),
            "interviews_by_type": {
                i_type: sum(1 for i in self.interviews if i["type"] == i_type)
                for i_type in set(i["type"] for i in self.interviews)
            }
        }


def demonstrate_job_positioning():
    """
    Demonstrate job positioning using Metromap learning.
    """
    print("=" * 60)
    print("DEMONSTRATION: JOB POSITIONING")
    print("=" * 60)
    
    # Show role requirements
    print("\n1. JOB ROLE REQUIREMENTS")
    print("-" * 40)
    
    for role in [JobRole.JUNIOR_DEVELOPER, JobRole.DATA_ANALYST, JobRole.BACKEND_ENGINEER]:
        print(f"\n{role.value}:")
        requirements = JobPositioner.get_role_requirements(role)
        for req in requirements[:4]:  # Show first 4
            print(f"   • {req}")
        if len(requirements) > 4:
            print(f"   • ... and {len(requirements) - 4} more")
    
    # Map Metromap to role
    print("\n2. MAPPING METROMAP TO JOB ROLE")
    print("-" * 40)
    
    completed = ["Series A", "Series B", "Series C", "Series D", "Series E"]
    mapping = JobPositioner.map_metromap_to_role(JobRole.BACKEND_ENGINEER, completed)
    
    print(f"\n   Target Role: {mapping['role']}")
    print(f"   Completed Series: {', '.join(mapping['completed_series'])}")
    print(f"   Requirements Met: {len(mapping['requirements_met'])}")
    print(f"   Gaps: {len(mapping['gaps'])}")
    print(f"   Recommended Next: {', '.join(mapping['recommended_next_series'])}")
    
    # Generate resume bullets
    print("\n3. RESUME BULLET EXAMPLES")
    print("-" * 40)
    
    bullets = [
        JobPositioner.generate_resume_bullet(
            "E-Commerce Order System",
            "Built shopping cart with discount engine and tax calculation",
            metric="handling 10,000+ daily transactions",
            technology="Python"
        ),
        JobPositioner.generate_resume_bullet(
            "REST API",
            "Developed URL shortener with analytics tracking",
            metric="99.9% uptime",
            technology="Flask + SQLite"
        ),
        JobPositioner.generate_resume_bullet(
            "Open Source",
            "Contributed documentation and bug fixes",
            metric="3 merged PRs",
            technology="pandas + pytest"
        )
    ]
    
    for bullet in bullets:
        print(f"   {bullet}")
    
    # Prepare interview answers
    print("\n4. INTERVIEW PREPARATION (STAR METHOD)")
    print("-" * 40)
    
    sample_projects = [{
        "name": "Banking System",
        "problem": "need for multi-account financial tracking",
        "key_feature": "secure fund transfers with transaction history",
        "constraints": "financial accuracy and data integrity",
        "technical_approach": "OOP with inheritance and encapsulation",
        "outcome": "successful account management",
        "metrics": "100% accurate transaction logging"
    }]
    
    answers = JobPositioner.prepare_interview_answers(sample_projects)
    
    for question_type, answer in answers.items():
        print(f"\n   Question: Tell me about a {question_type.replace('_', ' ')}")
        print(f"   {answer.to_star()}")
    
    print("\n" + "=" * 60)
    print("JOB SEARCH CHECKLIST")
    print("=" * 60)
    
    checklist = [
        "✓ Complete portfolio projects for target role",
        "✓ Update GitHub profile with pinned repositories",
        "✓ Write LinkedIn summary highlighting Python skills",
        "✓ Create resume with project-based achievements",
        "✓ Practice STAR method answers for common questions",
        "✓ Set up job alerts for target roles",
        "✓ Apply to 5-10 jobs per week",
        "✓ Track applications and follow up",
        "✓ Network with Python developers in target industry",
        "✓ Prepare questions for interviewers",
        "✓ Send thank-you notes after interviews",
        "✓ Negotiate offers based on market research"
    ]
    
    for item in checklist:
        print(f"   {item}")
    
    print("\n💡 JOB SEARCH TIPS:")
    print("   • Tailor each application to the specific role")
    print("   • Use keywords from job descriptions in your resume")
    print("   • Show projects, not just certificates")
    print("   • Quantify achievements with metrics where possible")
    print("   • Practice coding challenges on LeetCode or HackerRank")
    print("   • Research companies before applying")
    print("   • Follow up after 1-2 weeks if no response")
    print("   • Don't get discouraged by rejections—they're part of the process")


if __name__ == "__main__":
    demonstrate_job_positioning()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Portfolio Building** – Create project folders with professional structure. Document every project with READMEs, tests, and technical walkthroughs. Track skills demonstrated across projects.

- **Open Source Contribution** – Start with documentation fixes. Find good first issues. Follow the contribution workflow. Build reputation through quality contributions.

- **Job Positioning** – Map Metromap series to role requirements. Generate resume bullets with metrics. Prepare STAR method interview answers. Track applications systematically.

- **From Passenger to Driver** – Stop consuming tutorials. Start building real projects. Contribute to existing codebases. Position yourself for opportunities.

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Avoiding Derailments

- **📚 Series 0 Catalog:** The Map & Mindset – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Variables & Data Types – The Rails of Python (Series A, Story 1)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 0 | 7 | 0% |
| Series B | 6 | 0 | 6 | 0% |
| Series C | 5 | 0 | 5 | 0% |
| Series D | 6 | 0 | 6 | 0% |
| Series E | 5 | 0 | 5 | 0% |
| Series F | 6 | 0 | 6 | 0% |
| Series G | 5 | 0 | 5 | 0% |
| Series H | 5 | 0 | 5 | 0% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **5** | **47** | **10%** |

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap: Reading the Map
4. Series 0, Story 4: The 2026 Python Metromap: Avoiding Derailments
5. Series 0, Story 5: The 2026 Python Metromap: From Passenger to Driver

**Next Story:** Series A, Story 1: The 2026 Python Metromap: Variables & Data Types – The Rails of Python

---

## 📝 Your Invitation

You've completed the Map & Mindset Line. You're no longer a passenger—you're a driver.

1. **Build your first portfolio project** – Choose a project from the list. Create the folder structure. Write the README.

2. **Find an open source issue** – Pick a project you use. Look for "good first issue." Comment that you'll work on it.

3. **Update your resume** – Add your Metromap projects. Use the resume bullet format with metrics.

4. **Practice STAR answers** – Record yourself answering "Tell me about a challenging project."

5. **Start Series A** – The real coding begins now. Variables, data types, and your first e-commerce system.

**You've mastered the mindset. Next stop: Foundations Station!**

---

*Found this helpful? Clap, comment, and share your first portfolio project. Next stop: Variables & Data Types!* 🚇