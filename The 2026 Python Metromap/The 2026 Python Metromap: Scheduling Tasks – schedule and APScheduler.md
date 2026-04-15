# The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler

## Series H: Web Development & Automation | Story 5 of 5

![The 2026 Python Metromap/images/Scheduling Tasks – schedule and APScheduler](images/Scheduling Tasks – schedule and APScheduler.png)

## 📖 Introduction

**Welcome to the fifth and final stop on the Web Development & Automation Line.**

You've mastered web development with Flask and Django, system automation with os and sys, and web scraping with BeautifulSoup. You can build APIs, full-stack applications, organize files, monitor systems, and extract data from websites. But all these tasks require manual triggering. What if you could run them automatically—every hour, every day, every week?

Scheduled task automation is the final piece of the automation puzzle. The `schedule` library provides a simple, human-friendly syntax for running jobs at intervals. APScheduler (Advanced Python Scheduler) offers more powerful features: persistent job storage, cron-style scheduling, and concurrent execution. Together, they let you automate recurring tasks like daily report generation, weekly backups, hourly data scraping, and email notifications.

This story—**The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler**—is your guide to task automation. We'll build a daily report emailer that sends automated reports. We'll create a weekly backup system that archives and rotates backups. We'll implement a cron-style job scheduler with APScheduler. We'll build a complete task scheduler with persistent storage. And we'll create a monitoring system that checks services and sends alerts.

**Let's schedule.**

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

- 🕸️ **The 2026 Python Metromap: Web Scraping with BeautifulSoup** – Price monitoring bot; multi-site product tracking; price drop alerts.

- ⏰ **The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler** – Daily report emailer; weekly backup system; cron-style job scheduler. **⬅️ YOU ARE HERE**

### Series I: AI & Machine Learning with Python (4 Stories) – Next Station

- 🤖 **The 2026 Python Metromap: Scikit-learn – Traditional ML** – Spam classifier for emails; customer churn predictor; house price estimator. 🔜 *Up Next*

- 🧠 **The 2026 Python Metromap: TensorFlow and Keras – Deep Learning** – Handwritten digit classifier; fashion item recognizer; sentiment analyzer.

- 🔥 **The 2026 Python Metromap: PyTorch – Research and Production** – Custom neural network for image classification; training loops; model deployment.

- 🚀 **The 2026 Python Metromap: End-to-End ML Pipeline Project** – Complete machine learning pipeline from data collection to deployment for house price prediction.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## ⏰ Section 1: Schedule Library – Simple Task Scheduling

The `schedule` library provides a simple, human-readable API for running tasks at intervals.

**SOLID Principle Applied: Single Responsibility** – Each scheduled job performs one task.

**Design Pattern: Command Pattern** – Scheduled jobs are commands executed at specified times.

```python
"""
SCHEDULE LIBRARY: SIMPLE TASK SCHEDULING

This section covers the schedule library for basic task scheduling.

SOLID Principle: Single Responsibility
- Each scheduled job performs one task

Design Pattern: Command Pattern
- Scheduled jobs are commands executed at specified times
"""

import schedule
import time
import datetime
from typing import Callable, List, Dict, Any
from dataclasses import dataclass
import random


def demonstrate_schedule_basics():
    """
    Demonstrates basic schedule library usage.
    
    Schedule provides a simple, human-readable API for scheduling tasks.
    """
    print("=" * 60)
    print("SECTION 1A: SCHEDULE LIBRARY BASICS")
    print("=" * 60)
    
    # BASIC SCHEDULING
    print("\n1. BASIC SCHEDULING SYNTAX")
    print("-" * 40)
    
    def job():
        print(f"  Job executed at {datetime.datetime.now().strftime('%H:%M:%S')}")
    
    # Schedule examples (commented to avoid actual execution)
    print("""
    # Schedule every 10 minutes
    schedule.every(10).minutes.do(job)
    
    # Schedule every hour
    schedule.every().hour.do(job)
    
    # Schedule every day at 10:30
    schedule.every().day.at("10:30").do(job)
    
    # Schedule every Monday at 09:00
    schedule.every().monday.at("09:00").do(job)
    
    # Schedule every Wednesday at 13:15
    schedule.every().wednesday.at("13:15").do(job)
    
    # Schedule every 5 to 10 minutes (random interval)
    schedule.every(5).to(10).minutes.do(job)
    """)
    
    # RUNNING SCHEDULER
    print("\n2. RUNNING THE SCHEDULER")
    print("-" * 40)
    
    print("""
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)
    """)
    
    # PRACTICAL EXAMPLE
    print("\n3. PRACTICAL EXAMPLE")
    print("-" * 40)
    
    # Create some jobs
    def greet(name):
        print(f"  Hello, {name}! It's {datetime.datetime.now().strftime('%H:%M:%S')}")
    
    def report_status():
        print(f"  Status check at {datetime.datetime.now().strftime('%H:%M:%S')}")
    
    # Schedule jobs (simulated)
    print("  Scheduling jobs:")
    print("    - greet('Alice') every 30 seconds")
    print("    - report_status() every minute")
    
    # In a real script, you would run:
    # schedule.every(30).seconds.do(greet, "Alice")
    # schedule.every(1).minutes.do(report_status)
    # 
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


def demonstrate_job_cancellation():
    """
    Demonstrates canceling and managing scheduled jobs.
    
    Jobs can be canceled by tag or by reference.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: JOB MANAGEMENT")
    print("=" * 60)
    
    # Clear any existing jobs
    schedule.clear()
    
    print("\n1. JOB TAGS")
    print("-" * 40)
    
    def backup_job():
        print("  Running backup...")
    
    def cleanup_job():
        print("  Running cleanup...")
    
    # Schedule with tags
    schedule.every().day.at("02:00").do(backup_job).tag("backup", "daily")
    schedule.every().hour.do(cleanup_job).tag("cleanup", "hourly")
    schedule.every().monday.at("03:00").do(backup_job).tag("backup", "weekly")
    
    print("  Scheduled jobs with tags:")
    for job in schedule.jobs:
        print(f"    {job} - tags: {job.tags}")
    
    print("\n2. GETTING JOBS BY TAG")
    print("-" * 40)
    
    backup_jobs = schedule.get_jobs("backup")
    print(f"  Jobs with 'backup' tag: {len(backup_jobs)}")
    
    daily_jobs = schedule.get_jobs("daily")
    print(f"  Jobs with 'daily' tag: {len(daily_jobs)}")
    
    print("\n3. CANCELING JOBS")
    print("-" * 40)
    
    # Cancel by tag
    schedule.clear("hourly")
    print(f"  After clearing 'hourly' tag: {len(schedule.jobs)} jobs remaining")
    
    # Cancel all
    schedule.clear()
    print(f"  After clearing all: {len(schedule.jobs)} jobs")
    
    # JOB RETURN VALUES
    print("\n4. JOB RETURN VALUES")
    print("-" * 40)
    
    def job_with_return():
        return "Job completed successfully"
    
    job = schedule.every(10).seconds.do(job_with_return)
    # In a real script, you would check job.last_run


def build_daily_report_system():
    """
    Builds a daily report generation and email system using schedule.
    
    Design Pattern: Command Pattern - Report generation as scheduled command
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: DAILY REPORT SYSTEM")
    print("=" * 60)
    
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import json
    import os
    
    class DailyReportSystem:
        """
        Automated daily report generation and email system.
        
        Design Pattern: Command Pattern - Report generation as scheduled command
        """
        
        def __init__(self, report_dir="reports"):
            self.report_dir = report_dir
            os.makedirs(report_dir, exist_ok=True)
            self.report_history = []
        
        def generate_sales_report(self) -> Dict:
            """Generate a sales report (simulated)."""
            # Simulate data collection
            total_sales = random.randint(5000, 20000)
            orders_count = random.randint(50, 200)
            top_product = random.choice(["Laptop", "Mouse", "Keyboard", "Monitor"])
            
            report = {
                "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                "total_sales": total_sales,
                "orders_count": orders_count,
                "average_order_value": round(total_sales / orders_count, 2),
                "top_product": top_product,
                "conversion_rate": round(random.uniform(2.0, 5.0), 1)
            }
            
            # Save report to file
            filename = f"{self.report_dir}/sales_{report['date']}.json"
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            
            self.report_history.append(report)
            print(f"  Sales report generated: ${total_sales:,.2f} from {orders_count} orders")
            return report
        
        def generate_system_health_report(self) -> Dict:
            """Generate a system health report."""
            import psutil
            
            report = {
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent,
                "uptime": time.time() - psutil.boot_time()
            }
            
            filename = f"{self.report_dir}/health_{datetime.datetime.now().strftime('%Y%m%d')}.json"
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"  Health report generated: CPU {report['cpu_percent']}%, Memory {report['memory_percent']}%")
            return report
        
        def send_email_report(self, recipient: str, subject: str, report_data: Dict) -> bool:
            """Send email report (simulated)."""
            # In production, use actual SMTP
            print(f"  [EMAIL] To: {recipient}")
            print(f"  [EMAIL] Subject: {subject}")
            print(f"  [EMAIL] Report: {json.dumps(report_data, indent=2)[:200]}...")
            return True
        
        def generate_and_send_daily_report(self, recipient: str):
            """Generate and send daily report."""
            print(f"\n  📊 Generating daily report for {recipient}...")
            
            # Generate reports
            sales_report = self.generate_sales_report()
            health_report = self.generate_system_health_report()
            
            # Create summary
            summary = f"""
            Daily Report - {sales_report['date']}
            
            SALES SUMMARY:
            - Total Sales: ${sales_report['total_sales']:,.2f}
            - Orders: {sales_report['orders_count']}
            - Average Order: ${sales_report['average_order_value']:.2f}
            - Top Product: {sales_report['top_product']}
            - Conversion Rate: {sales_report['conversion_rate']}%
            
            SYSTEM HEALTH:
            - CPU Usage: {health_report['cpu_percent']}%
            - Memory Usage: {health_report['memory_percent']}%
            - Disk Usage: {health_report['disk_percent']}%
            """
            
            # Send email
            self.send_email_report(recipient, f"Daily Report - {sales_report['date']}", {"summary": summary})
            
            return {"sales": sales_report, "health": health_report}
        
        def cleanup_old_reports(self, days_to_keep: int = 30):
            """Delete reports older than specified days."""
            cutoff = time.time() - (days_to_keep * 24 * 60 * 60)
            deleted = 0
            
            for filename in os.listdir(self.report_dir):
                filepath = os.path.join(self.report_dir, filename)
                if os.path.getmtime(filepath) < cutoff:
                    os.remove(filepath)
                    deleted += 1
            
            print(f"  Cleaned up {deleted} old reports")
            return deleted
        
        def schedule_daily_report(self, report_time: str = "09:00", recipient: str = "admin@example.com"):
            """Schedule daily report generation."""
            schedule.every().day.at(report_time).do(
                self.generate_and_send_daily_report, recipient
            ).tag("daily_report")
            print(f"  Scheduled daily report at {report_time}")
        
        def schedule_weekly_cleanup(self, day: str = "sunday", time_str: str = "01:00"):
            """Schedule weekly cleanup."""
            getattr(schedule.every(), day).at(time_str).do(
                self.cleanup_old_reports, 30
            ).tag("weekly_cleanup")
            print(f"  Scheduled weekly cleanup on {day} at {time_str}")
        
        def run(self):
            """Run the scheduler."""
            print("\n  Starting scheduler...")
            print("  Press Ctrl+C to stop\n")
            
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n  Scheduler stopped")
    
    # Demonstrate the system
    print("\n1. SETTING UP DAILY REPORT SYSTEM")
    print("-" * 40)
    
    report_system = DailyReportSystem()
    
    # Schedule jobs
    report_system.schedule_daily_report(report_time="09:00", recipient="admin@example.com")
    report_system.schedule_weekly_cleanup(day="sunday", time_str="01:00")
    
    print("\n2. SCHEDULED JOBS")
    print("-" * 40)
    
    for job in schedule.jobs:
        print(f"  {job}")
    
    # Manual execution for demonstration
    print("\n3. MANUAL REPORT GENERATION (DEMO)")
    print("-" * 40)
    
    report_system.generate_and_send_daily_report("demo@example.com")
    
    # Clean up
    schedule.clear()
    import shutil
    if os.path.exists("reports"):
        shutil.rmtree("reports")
    
    print("\n  Demo complete, cleaned up")


def demonstrate_schedule_with_decorators():
    """
    Demonstrates using decorators with schedule library.
    
    Custom decorators can add logging, retry, and error handling.
    """
    print("\n" + "=" * 60)
    print("SECTION 1D: DECORATORS FOR SCHEDULED JOBS")
    print("=" * 60)
    
    from functools import wraps
    
    # LOGGING DECORATOR
    def log_job(func):
        """Log when job starts and finishes."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"  [START] {func.__name__} at {datetime.datetime.now().strftime('%H:%M:%S')}")
            try:
                result = func(*args, **kwargs)
                print(f"  [END] {func.__name__} completed")
                return result
            except Exception as e:
                print(f"  [ERROR] {func.__name__} failed: {e}")
                raise
        return wrapper
    
    # RETRY DECORATOR
    def retry(max_attempts=3, delay=1):
        """Retry job on failure."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise
                        print(f"  Retry {attempt + 1}/{max_attempts} after error: {e}")
                        time.sleep(delay)
                return None
            return wrapper
        return decorator
    
    # TIMING DECORATOR
    def time_job(func):
        """Measure job execution time."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = (time.time() - start) * 1000
            print(f"  [TIMING] {func.__name__} took {duration:.2f}ms")
            return result
        return wrapper
    
    # Example job with decorators
    @log_job
    @time_job
    @retry(max_attempts=2, delay=0.5)
    def data_sync_job():
        """Synchronize data with external API."""
        print("    Syncing data...")
        # Simulate work
        time.sleep(0.1)
        # Simulate occasional failure
        if random.random() < 0.3:
            raise ConnectionError("API temporarily unavailable")
        print("    Sync complete")
        return {"synced": 100}
    
    print("\n  Running data sync job (with decorators):")
    try:
        result = data_sync_job()
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  Job failed after retries: {e}")
    
    print("\n  Decorator benefits:")
    print("    ✓ Automatic logging of job start/end")
    print("    ✓ Performance timing")
    print("    ✓ Retry on failure")
    print("    ✓ Error handling")


if __name__ == "__main__":
    demonstrate_schedule_basics()
    demonstrate_job_cancellation()
    build_daily_report_system()
    demonstrate_schedule_with_decorators()
```

---

## 🔧 Section 2: APScheduler – Advanced Task Scheduling

APScheduler (Advanced Python Scheduler) provides more powerful scheduling features: cron expressions, persistent job storage, and concurrent execution.

**SOLID Principles Applied:**
- Single Responsibility: Each scheduler handles one type of job
- Open/Closed: New job stores and executors can be added

**Design Patterns:**
- Factory Pattern: Creates schedulers with different configurations
- Observer Pattern: Monitors job execution

```python
"""
APSCHEDULER: ADVANCED TASK SCHEDULING

This section covers APScheduler for advanced task scheduling.

SOLID Principles Applied:
- Single Responsibility: Each scheduler handles one type of job
- Open/Closed: New job stores and executors can be added

Design Patterns:
- Factory Pattern: Creates schedulers with different configurations
- Observer Pattern: Monitors job execution
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime, timedelta
import time
import logging


def demonstrate_apscheduler_basics():
    """
    Demonstrates basic APScheduler functionality.
    
    APScheduler supports interval, cron, and date triggers.
    """
    print("=" * 60)
    print("SECTION 2A: APSCHEDULER BASICS")
    print("=" * 60)
    
    # INTERVAL TRIGGER
    print("\n1. INTERVAL TRIGGER (every N seconds/minutes/hours)")
    print("-" * 40)
    
    def interval_job():
        print(f"  Interval job executed at {datetime.now().strftime('%H:%M:%S')}")
    
    # Create scheduler
    scheduler = BackgroundScheduler()
    
    # Add job with interval trigger
    scheduler.add_job(
        interval_job,
        trigger='interval',
        seconds=10,
        id='interval_job_1',
        replace_existing=True
    )
    
    print("  Added job: runs every 10 seconds")
    
    # CRON TRIGGER
    print("\n2. CRON TRIGGER (like Linux cron)")
    print("-" * 40)
    
    def cron_job():
        print(f"  Cron job executed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Examples (commented to avoid execution)
    print("""
    # Run every hour at minute 0
    scheduler.add_job(cron_job, trigger='cron', hour='*', minute='0')
    
    # Run every day at 9:30 AM
    scheduler.add_job(cron_job, trigger='cron', hour=9, minute=30)
    
    # Run every Monday at 10:00 AM
    scheduler.add_job(cron_job, trigger='cron', day_of_week='mon', hour=10, minute=0)
    
    # Run on 1st of every month at midnight
    scheduler.add_job(cron_job, trigger='cron', day=1, hour=0, minute=0)
    
    # Run every 15 minutes
    scheduler.add_job(cron_job, trigger='cron', minute='*/15')
    """)
    
    # DATE TRIGGER
    print("\n3. DATE TRIGGER (run once at specific time)")
    print("-" * 40)
    
    def one_time_job():
        print(f"  One-time job executed at {datetime.now().strftime('%H:%M:%S')}")
    
    # Run in 5 seconds
    run_time = datetime.now() + timedelta(seconds=5)
    scheduler.add_job(
        one_time_job,
        trigger='date',
        run_date=run_time,
        id='one_time_job'
    )
    print(f"  Added job: runs once at {run_time.strftime('%H:%M:%S')}")
    
    # Start scheduler
    scheduler.start()
    print("\n  Scheduler started")
    
    # Let jobs run for a few seconds
    time.sleep(8)
    
    # Shutdown
    scheduler.shutdown()
    print("\n  Scheduler shutdown")


def demonstrate_apscheduler_job_management():
    """
    Demonstrates managing jobs (pause, resume, modify, remove).
    """
    print("\n" + "=" * 60)
    print("SECTION 2B: JOB MANAGEMENT")
    print("=" * 60)
    
    scheduler = BackgroundScheduler()
    
    def job_a():
        print(f"  Job A executed at {datetime.now().strftime('%H:%M:%S')}")
    
    def job_b():
        print(f"  Job B executed at {datetime.now().strftime('%H:%M:%S')}")
    
    def job_c():
        print(f"  Job C executed at {datetime.now().strftime('%H:%M:%S')}")
    
    # Add jobs
    scheduler.add_job(job_a, 'interval', seconds=5, id='job_a')
    scheduler.add_job(job_b, 'interval', seconds=7, id='job_b')
    scheduler.add_job(job_c, 'interval', seconds=10, id='job_c')
    
    print("\n1. LISTING JOBS")
    print("-" * 40)
    
    for job in scheduler.get_jobs():
        print(f"  {job.id} - next run: {job.next_run_time.strftime('%H:%M:%S') if job.next_run_time else 'N/A'}")
    
    print("\n2. PAUSING AND RESUMING JOBS")
    print("-" * 40)
    
    # Pause a job
    scheduler.pause_job('job_b')
    print("  Paused job_b")
    
    # Resume a job
    scheduler.resume_job('job_b')
    print("  Resumed job_b")
    
    print("\n3. MODIFYING JOBS")
    print("-" * 40)
    
    # Change interval
    scheduler.reschedule_job('job_a', trigger='interval', seconds=3)
    print("  Changed job_a interval to 3 seconds")
    
    print("\n4. REMOVING JOBS")
    print("-" * 40)
    
    scheduler.remove_job('job_c')
    print("  Removed job_c")
    
    print(f"\n  Remaining jobs: {len(scheduler.get_jobs())}")
    
    scheduler.shutdown()


def build_weekly_backup_system():
    """
    Builds a weekly backup system using APScheduler.
    
    Design Pattern: Command Pattern - Backup as scheduled command
    """
    print("\n" + "=" * 60)
    print("SECTION 2C: WEEKLY BACKUP SYSTEM")
    print("=" * 60)
    
    import shutil
    import os
    from pathlib import Path
    
    class BackupSystem:
        """
        Automated backup system with scheduling.
        
        Design Pattern: Command Pattern - Backup as scheduled command
        """
        
        def __init__(self, source_dir: str, backup_dir: str):
            self.source_dir = Path(source_dir)
            self.backup_dir = Path(backup_dir)
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            self.scheduler = BackgroundScheduler()
            self.backup_history = []
        
        def perform_backup(self, backup_type: str = "full") -> Dict:
            """Perform a backup of the source directory."""
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"backup_{backup_type}_{timestamp}"
            backup_path = self.backup_dir / backup_name
            
            print(f"\n  📦 Starting {backup_type} backup: {backup_name}")
            start_time = time.time()
            
            try:
                # Create backup
                shutil.copytree(self.source_dir, backup_path, ignore_dangling_symlinks=True)
                
                # Calculate size
                total_size = sum(f.stat().st_size for f in backup_path.rglob('*') if f.is_file())
                size_mb = total_size / (1024 * 1024)
                
                # Record backup
                backup_record = {
                    "name": backup_name,
                    "path": str(backup_path),
                    "type": backup_type,
                    "size_mb": round(size_mb, 2),
                    "timestamp": datetime.now().isoformat(),
                    "duration_seconds": round(time.time() - start_time, 2)
                }
                self.backup_history.append(backup_record)
                
                print(f"  ✅ Backup complete: {size_mb:.2f} MB in {backup_record['duration_seconds']:.1f}s")
                return backup_record
                
            except Exception as e:
                print(f"  ❌ Backup failed: {e}")
                return {"error": str(e)}
        
        def rotate_backups(self, keep_count: int = 10):
            """Delete old backups, keeping only the most recent N."""
            backups = sorted(self.backup_dir.glob("backup_*"))
            
            if len(backups) <= keep_count:
                return 0
            
            to_delete = backups[:-keep_count]
            deleted = 0
            
            for backup in to_delete:
                shutil.rmtree(backup)
                deleted += 1
                print(f"  Deleted old backup: {backup.name}")
            
            # Update history
            self.backup_history = self.backup_history[-keep_count:]
            
            return deleted
        
        def schedule_weekly_backup(self, day_of_week: str = 'sun', hour: int = 2, minute: int = 0):
            """Schedule weekly full backup."""
            self.scheduler.add_job(
                self.perform_backup,
                trigger='cron',
                day_of_week=day_of_week,
                hour=hour,
                minute=minute,
                args=['full'],
                id='weekly_backup',
                replace_existing=True
            )
            print(f"  Scheduled weekly backup on {day_of_week} at {hour:02d}:{minute:02d}")
        
        def schedule_daily_incremental(self, hour: int = 1, minute: int = 0):
            """Schedule daily incremental backup."""
            self.scheduler.add_job(
                self.perform_backup,
                trigger='cron',
                hour=hour,
                minute=minute,
                args=['incremental'],
                id='daily_backup',
                replace_existing=True
            )
            print(f"  Scheduled daily incremental backup at {hour:02d}:{minute:02d}")
        
        def schedule_backup_rotation(self, day_of_week: str = 'sun', hour: int = 3, minute: int = 0):
            """Schedule weekly backup rotation."""
            self.scheduler.add_job(
                self.rotate_backups,
                trigger='cron',
                day_of_week=day_of_week,
                hour=hour,
                minute=minute,
                args=[10],
                id='backup_rotation',
                replace_existing=True
            )
            print(f"  Scheduled backup rotation on {day_of_week} at {hour:02d}:{minute:02d}")
        
        def add_event_listeners(self):
            """Add listeners for job events."""
            def job_listener(event):
                if event.exception:
                    print(f"  [ERROR] Job {event.job_id} failed: {event.exception}")
                else:
                    print(f"  [INFO] Job {event.job_id} completed successfully")
            
            self.scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
        
        def start(self):
            """Start the backup scheduler."""
            self.add_event_listeners()
            self.scheduler.start()
            print("\n  Backup scheduler started")
        
        def stop(self):
            """Stop the backup scheduler."""
            self.scheduler.shutdown()
            print("  Backup scheduler stopped")
        
        def get_status(self) -> Dict:
            """Get backup system status."""
            return {
                "scheduler_running": self.scheduler.running,
                "jobs": [
                    {
                        "id": job.id,
                        "next_run": job.next_run_time.strftime('%Y-%m-%d %H:%M:%S') if job.next_run_time else None
                    }
                    for job in self.scheduler.get_jobs()
                ],
                "backup_count": len(self.backup_history),
                "last_backup": self.backup_history[-1] if self.backup_history else None
            }
    
    # DEMONSTRATION
    print("\n1. SETTING UP BACKUP SYSTEM")
    print("-" * 40)
    
    import tempfile
    temp_dir = tempfile.mkdtemp()
    source = Path(temp_dir) / "source"
    backup = Path(temp_dir) / "backups"
    
    source.mkdir()
    
    # Create some test files
    for i in range(5):
        (source / f"file_{i}.txt").write_text(f"Content of file {i}")
    
    (source / "subdir").mkdir()
    (source / "subdir" / "nested.txt").write_text("Nested content")
    
    print(f"  Source directory: {source}")
    print(f"  Backup directory: {backup}")
    
    # Create backup system
    backup_system = BackupSystem(str(source), str(backup))
    
    print("\n2. SCHEDULING BACKUPS")
    print("-" * 40)
    
    backup_system.schedule_weekly_backup(day_of_week='sun', hour=2, minute=0)
    backup_system.schedule_daily_incremental(hour=1, minute=0)
    backup_system.schedule_backup_rotation(day_of_week='sun', hour=3, minute=0)
    
    print("\n3. MANUAL BACKUP (DEMO)")
    print("-" * 40)
    
    result = backup_system.perform_backup("full")
    
    print("\n4. BACKUP SYSTEM STATUS")
    print("-" * 40)
    
    status = backup_system.get_status()
    print(f"  Scheduler running: {status['scheduler_running']}")
    print(f"  Backup count: {status['backup_count']}")
    
    if status['last_backup']:
        last = status['last_backup']
        print(f"  Last backup: {last['name']} ({last['size_mb']} MB)")
    
    # Clean up
    import shutil
    shutil.rmtree(temp_dir)
    print("\n  Cleaned up temp directory")


def demonstrate_persistent_job_store():
    """
    Demonstrates using persistent job storage with APScheduler.
    
    Jobs persist across application restarts when using SQLite or Redis.
    """
    print("\n" + "=" * 60)
    print("SECTION 2D: PERSISTENT JOB STORAGE")
    print("=" * 60)
    
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
    
    print("\n1. SQLITE JOB STORE")
    print("-" * 40)
    
    # Configure SQLite job store
    jobstores = {
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }
    
    scheduler = BackgroundScheduler(jobstores=jobstores)
    
    def persistent_job():
        print(f"  Persistent job executed at {datetime.now().strftime('%H:%M:%S')}")
    
    # Add job - it will persist in database
    scheduler.add_job(
        persistent_job,
        'interval',
        seconds=30,
        id='persistent_job_1',
        replace_existing=True
    )
    
    print("  Job added to persistent storage")
    print("  Jobs will survive application restarts")
    
    # Show stored jobs
    print(f"\n  Stored jobs: {[job.id for job in scheduler.get_jobs()]}")
    
    scheduler.shutdown()
    
    print("\n2. JOB STORE OPTIONS")
    print("-" * 40)
    
    stores = [
        ("SQLite", "sqlite:///jobs.sqlite", "Good for single process"),
        ("PostgreSQL", "postgresql://user:pass@localhost/db", "Production use"),
        ("Redis", "redis://localhost:6379", "Fast, distributed"),
        ("MongoDB", "mongodb://localhost:27017", "Document-based"),
    ]
    
    for name, url, use_case in stores:
        print(f"  {name:12} - {use_case}")
        print(f"    URL: {url}")
    
    # Clean up
    import os
    if os.path.exists("jobs.sqlite"):
        os.remove("jobs.sqlite")
        print("\n  Cleaned up job store")


if __name__ == "__main__":
    demonstrate_apscheduler_basics()
    demonstrate_apscheduler_job_management()
    build_weekly_backup_system()
    demonstrate_persistent_job_store()
```

---

## 📧 Section 3: Email and Notification Scheduler

A complete email and notification scheduling system for automated alerts and reports.

**SOLID Principles Applied:**
- Single Responsibility: Each notifier handles one channel
- Open/Closed: New notification channels can be added

**Design Patterns:**
- Strategy Pattern: Different notification strategies
- Observer Pattern: Notifies subscribers

```python
"""
EMAIL AND NOTIFICATION SCHEDULER

This section builds a notification scheduling system.

SOLID Principles Applied:
- Single Responsibility: Each notifier handles one channel
- Open/Closed: New notification channels can be added

Design Patterns:
- Strategy Pattern: Different notification strategies
- Observer Pattern: Notifies subscribers
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
import json
import os


@dataclass
class Notification:
    """Represents a notification to be sent."""
    id: str
    title: str
    message: str
    recipients: List[str]
    channel: str  # email, sms, slack, webhook
    scheduled_time: datetime
    data: Dict[str, Any] = field(default_factory=dict)
    sent: bool = False
    sent_at: Optional[datetime] = None
    error: Optional[str] = None


class NotificationChannel(ABC):
    """Abstract base class for notification channels."""
    
    @abstractmethod
    def send(self, notification: Notification) -> bool:
        pass
    
    @abstractmethod
    def get_channel_name(self) -> str:
        pass


class EmailChannel(NotificationChannel):
    """Email notification channel."""
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def get_channel_name(self) -> str:
        return "email"
    
    def send(self, notification: Notification) -> bool:
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(notification.recipients)
            msg['Subject'] = notification.title
            
            msg.attach(MIMEText(notification.message, 'plain'))
            
            # Add attachments if any
            for attachment in notification.data.get('attachments', []):
                with open(attachment, 'rb') as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                    msg.attach(part)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
            
            print(f"  Email sent to {', '.join(notification.recipients)}")
            return True
            
        except Exception as e:
            print(f"  Email failed: {e}")
            return False


class SlackChannel(NotificationChannel):
    """Slack webhook notification channel."""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    def get_channel_name(self) -> str:
        return "slack"
    
    def send(self, notification: Notification) -> bool:
        try:
            import requests
            
            payload = {
                "text": f"*{notification.title}*\n{notification.message}",
                "username": "Notification Bot",
                "icon_emoji": ":bell:"
            }
            
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            response.raise_for_status()
            
            print(f"  Slack notification sent")
            return True
            
        except Exception as e:
            print(f"  Slack notification failed: {e}")
            return False


class ConsoleChannel(NotificationChannel):
    """Console notification channel (for testing)."""
    
    def get_channel_name(self) -> str:
        return "console"
    
    def send(self, notification: Notification) -> bool:
        print(f"\n  📧 CONSOLE NOTIFICATION")
        print(f"  To: {', '.join(notification.recipients)}")
        print(f"  Title: {notification.title}")
        print(f"  Message: {notification.message[:100]}...")
        return True


class NotificationScheduler:
    """
    Schedules and sends notifications.
    
    Design Pattern: Strategy Pattern - Pluggable notification channels
    """
    
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.channels: Dict[str, NotificationChannel] = {}
        self.notifications: List[Notification] = []
        self._setup_defaults()
    
    def _setup_defaults(self):
        """Setup default notification channel."""
        self.register_channel(ConsoleChannel())
    
    def register_channel(self, channel: NotificationChannel) -> 'NotificationScheduler':
        """Register a notification channel."""
        self.channels[channel.get_channel_name()] = channel
        print(f"  Registered channel: {channel.get_channel_name()}")
        return self
    
    def schedule_notification(self, notification: Notification) -> str:
        """Schedule a notification to be sent."""
        # Store notification
        self.notifications.append(notification)
        
        # Schedule job
        self.scheduler.add_job(
            self._send_notification,
            trigger='date',
            run_date=notification.scheduled_time,
            args=[notification.id],
            id=f"notify_{notification.id}",
            replace_existing=True
        )
        
        print(f"  Scheduled notification '{notification.title}' for {notification.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return notification.id
    
    def schedule_recurring(self, title: str, message: str, recipients: List[str],
                          channel: str, cron_expr: str, **kwargs) -> str:
        """Schedule a recurring notification using cron expression."""
        notification_id = f"recurring_{int(datetime.now().timestamp())}"
        
        def recurring_job():
            notification = Notification(
                id=f"{notification_id}_{datetime.now().timestamp()}",
                title=title,
                message=message,
                recipients=recipients,
                channel=channel,
                scheduled_time=datetime.now(),
                data=kwargs
            )
            self._send_notification(notification.id, notification)
        
        self.scheduler.add_job(
            recurring_job,
            trigger=CronTrigger.from_crontab(cron_expr),
            id=notification_id,
            replace_existing=True
        )
        
        print(f"  Scheduled recurring notification '{title}' with cron: {cron_expr}")
        return notification_id
    
    def _send_notification(self, notification_id: str, notification: Notification = None):
        """Send a notification."""
        if notification is None:
            # Find notification by ID
            notification = next((n for n in self.notifications if n.id == notification_id), None)
            if not notification:
                print(f"  Notification {notification_id} not found")
                return
        
        channel = self.channels.get(notification.channel)
        if not channel:
            print(f"  Channel '{notification.channel}' not found")
            notification.error = f"Channel '{notification.channel}' not found"
            return
        
        success = channel.send(notification)
        notification.sent = success
        notification.sent_at = datetime.now() if success else None
        
        if not success:
            notification.error = "Failed to send"
    
    def start(self):
        """Start the scheduler."""
        self.scheduler.start()
        print("  Notification scheduler started")
    
    def stop(self):
        """Stop the scheduler."""
        self.scheduler.shutdown()
        print("  Notification scheduler stopped")
    
    def get_pending_notifications(self) -> List[Notification]:
        """Get notifications that haven't been sent yet."""
        return [n for n in self.notifications if not n.sent]
    
    def get_sent_notifications(self, limit: int = 20) -> List[Notification]:
        """Get recently sent notifications."""
        sent = [n for n in self.notifications if n.sent]
        return sorted(sent, key=lambda x: x.sent_at, reverse=True)[:limit]
    
    def cancel_notification(self, notification_id: str) -> bool:
        """Cancel a scheduled notification."""
        try:
            self.scheduler.remove_job(f"notify_{notification_id}")
            # Remove from list
            self.notifications = [n for n in self.notifications if n.id != notification_id]
            print(f"  Cancelled notification {notification_id}")
            return True
        except Exception as e:
            print(f"  Failed to cancel: {e}")
            return False


def build_alert_monitoring_system():
    """
    Builds an alert monitoring system with scheduled checks.
    
    Design Pattern: Observer Pattern - Monitors and alerts on conditions
    """
    print("\n" + "=" * 60)
    print("SECTION 3: ALERT MONITORING SYSTEM")
    print("=" * 60)
    
    import psutil
    import random
    
    class AlertMonitor:
        """
        Monitors system metrics and sends alerts.
        
        Design Pattern: Observer Pattern - Observes metrics and alerts
        """
        
        def __init__(self, notifier: NotificationScheduler):
            self.notifier = notifier
            self.thresholds = {
                "cpu_percent": 80,
                "memory_percent": 85,
                "disk_percent": 90
            }
            self.alert_history = []
        
        def check_cpu(self) -> bool:
            """Check CPU usage."""
            cpu_percent = psutil.cpu_percent(interval=1)
            
            if cpu_percent > self.thresholds["cpu_percent"]:
                self._send_alert(
                    "High CPU Usage Alert",
                    f"CPU usage is at {cpu_percent}% (threshold: {self.thresholds['cpu_percent']}%)",
                    {"cpu_percent": cpu_percent, "threshold": self.thresholds["cpu_percent"]}
                )
                return True
            return False
        
        def check_memory(self) -> bool:
            """Check memory usage."""
            memory = psutil.virtual_memory()
            
            if memory.percent > self.thresholds["memory_percent"]:
                self._send_alert(
                    "High Memory Usage Alert",
                    f"Memory usage is at {memory.percent}% (threshold: {self.thresholds['memory_percent']}%)",
                    {"memory_percent": memory.percent, "threshold": self.thresholds["memory_percent"]}
                )
                return True
            return False
        
        def check_disk(self) -> bool:
            """Check disk usage."""
            disk = psutil.disk_usage('/')
            
            if disk.percent > self.thresholds["disk_percent"]:
                self._send_alert(
                    "High Disk Usage Alert",
                    f"Disk usage is at {disk.percent}% (threshold: {self.thresholds['disk_percent']}%)",
                    {"disk_percent": disk.percent, "threshold": self.thresholds["disk_percent"]}
                )
                return True
            return False
        
        def check_service_health(self, service_name: str, health_check_url: str) -> bool:
            """Check if a service is healthy."""
            try:
                import requests
                response = requests.get(health_check_url, timeout=10)
                
                if response.status_code != 200:
                    self._send_alert(
                        f"Service Down Alert: {service_name}",
                        f"Service {service_name} returned status {response.status_code}",
                        {"service": service_name, "status_code": response.status_code}
                    )
                    return False
                return True
                
            except Exception as e:
                self._send_alert(
                    f"Service Unreachable: {service_name}",
                    f"Could not reach service {service_name}: {e}",
                    {"service": service_name, "error": str(e)}
                )
                return False
        
        def _send_alert(self, title: str, message: str, data: Dict):
            """Send an alert notification."""
            notification = Notification(
                id=f"alert_{int(datetime.now().timestamp())}",
                title=title,
                message=message,
                recipients=["admin@example.com"],
                channel="console",  # Use console for demo
                scheduled_time=datetime.now(),
                data=data
            )
            
            self.notifier.schedule_notification(notification)
            self.alert_history.append({
                "timestamp": datetime.now().isoformat(),
                "title": title,
                "message": message,
                "data": data
            })
        
        def run_health_check(self):
            """Run all health checks."""
            print(f"\n  Running health check at {datetime.now().strftime('%H:%M:%S')}")
            
            self.check_cpu()
            self.check_memory()
            self.check_disk()
        
        def schedule_health_checks(self, interval_minutes: int = 5):
            """Schedule regular health checks."""
            self.notifier.scheduler.add_job(
                self.run_health_check,
                trigger=IntervalTrigger(minutes=interval_minutes),
                id="health_check",
                replace_existing=True
            )
            print(f"  Scheduled health checks every {interval_minutes} minutes")
        
        def get_alert_summary(self) -> Dict:
            """Get alert summary."""
            return {
                "total_alerts": len(self.alert_history),
                "last_alert": self.alert_history[-1] if self.alert_history else None,
                "alerts_by_type": self._group_alerts_by_type()
            }
        
        def _group_alerts_by_type(self) -> Dict:
            """Group alerts by type."""
            groups = {}
            for alert in self.alert_history:
                title = alert["title"]
                groups[title] = groups.get(title, 0) + 1
            return groups
    
    # DEMONSTRATION
    print("\n1. SETTING UP NOTIFICATION SYSTEM")
    print("-" * 40)
    
    notifier = NotificationScheduler()
    monitor = AlertMonitor(notifier)
    
    print("\n2. SCHEDULING HEALTH CHECKS")
    print("-" * 40)
    
    monitor.schedule_health_checks(interval_minutes=1)
    
    print("\n3. SCHEDULING DAILY SUMMARY")
    print("-" * 40)
    
    def send_daily_summary():
        """Send daily alert summary."""
        summary = monitor.get_alert_summary()
        
        message = f"""
        Daily Alert Summary
        ===================
        Total Alerts: {summary['total_alerts']}
        
        Alerts by Type:
        """
        for alert_type, count in summary['alerts_by_type'].items():
            message += f"\n  - {alert_type}: {count}"
        
        notification = Notification(
            id=f"daily_summary_{datetime.now().strftime('%Y%m%d')}",
            title="Daily Alert Summary",
            message=message,
            recipients=["admin@example.com"],
            channel="console",
            scheduled_time=datetime.now().replace(hour=18, minute=0, second=0)
        )
        notifier.schedule_notification(notification)
    
    # Schedule daily summary
    notifier.scheduler.add_job(
        send_daily_summary,
        trigger=CronTrigger(hour=18, minute=0),
        id="daily_summary",
        replace_existing=True
    )
    print("  Scheduled daily summary at 18:00")
    
    print("\n4. MANUAL HEALTH CHECK (DEMO)")
    print("-" * 40)
    
    monitor.run_health_check()
    
    print("\n5. ALERT SUMMARY")
    print("-" * 40)
    
    summary = monitor.get_alert_summary()
    print(f"  Total alerts: {summary['total_alerts']}")
    
    if summary['last_alert']:
        print(f"  Last alert: {summary['last_alert']['title']}")
    
    print("\n  Monitoring system ready")
    print("  (Scheduler would continue running in production)")


if __name__ == "__main__":
    build_alert_monitoring_system()
```

---

## 🚀 Section 4: Complete Task Scheduler Application

A complete task scheduler application with persistent storage, job management, and web interface.

**SOLID Principles Applied:**
- Single Responsibility: Each component has one purpose
- Open/Closed: New job types can be added

**Design Patterns:**
- Command Pattern: Jobs as commands
- Repository Pattern: Persistent job storage
- Factory Pattern: Creates jobs from configuration

```python
"""
COMPLETE TASK SCHEDULER APPLICATION

This section builds a complete task scheduler with persistent storage.

SOLID Principles Applied:
- Single Responsibility: Each component has one purpose
- Open/Closed: New job types can be added

Design Patterns:
- Command Pattern: Jobs as commands
- Repository Pattern: Persistent job storage
- Factory Pattern: Creates jobs from configuration
"""

import json
import os
import time
import threading
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging


class JobStatus(Enum):
    """Job status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobType(Enum):
    """Types of jobs."""
    COMMAND = "command"
    PYTHON_FUNCTION = "python_function"
    HTTP_REQUEST = "http_request"
    FILE_OPERATION = "file_operation"
    BACKUP = "backup"
    REPORT = "report"


@dataclass
class ScheduledJob:
    """Represents a scheduled job."""
    id: str
    name: str
    job_type: JobType
    config: Dict[str, Any]
    schedule: str  # cron expression or interval
    enabled: bool = True
    status: JobStatus = JobStatus.PENDING
    last_run: Optional[datetime] = None
    last_result: Optional[str] = None
    next_run: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data['job_type'] = self.job_type.value
        data['status'] = self.status.value
        data['last_run'] = self.last_run.isoformat() if self.last_run else None
        data['next_run'] = self.next_run.isoformat() if self.next_run else None
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ScheduledJob':
        """Create from dictionary."""
        data['job_type'] = JobType(data['job_type'])
        data['status'] = JobStatus(data['status'])
        if data['last_run']:
            data['last_run'] = datetime.fromisoformat(data['last_run'])
        if data['next_run']:
            data['next_run'] = datetime.fromisoformat(data['next_run'])
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        data['updated_at'] = datetime.fromisoformat(data['updated_at'])
        return cls(**data)


class JobExecutor:
    """
    Executes different types of jobs.
    
    Design Pattern: Command Pattern - Executes job commands
    """
    
    @staticmethod
    def execute_command(command: str) -> tuple:
        """Execute a shell command."""
        import subprocess
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timed out"
        except Exception as e:
            return False, "", str(e)
    
    @staticmethod
    def execute_python_function(module: str, function: str, args: List = None, kwargs: Dict = None) -> tuple:
        """Execute a Python function."""
        import importlib
        try:
            mod = importlib.import_module(module)
            func = getattr(mod, function)
            args = args or []
            kwargs = kwargs or {}
            result = func(*args, **kwargs)
            return True, str(result), ""
        except Exception as e:
            return False, "", str(e)
    
    @staticmethod
    def execute_http_request(url: str, method: str = "GET", headers: Dict = None, body: Dict = None) -> tuple:
        """Execute an HTTP request."""
        import requests
        try:
            headers = headers or {}
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=30)
            elif method.upper() == "POST":
                response = requests.post(url, json=body, headers=headers, timeout=30)
            elif method.upper() == "PUT":
                response = requests.put(url, json=body, headers=headers, timeout=30)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=headers, timeout=30)
            else:
                return False, "", f"Unsupported method: {method}"
            
            return response.status_code == 200, response.text, ""
        except Exception as e:
            return False, "", str(e)
    
    @staticmethod
    def execute_backup(source: str, destination: str) -> tuple:
        """Execute a backup job."""
        import shutil
        from pathlib import Path
        try:
            source_path = Path(source)
            dest_path = Path(destination)
            
            if not source_path.exists():
                return False, "", f"Source not found: {source}"
            
            dest_path.mkdir(parents=True, exist_ok=True)
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            backup_path = dest_path / backup_name
            
            shutil.copytree(source_path, backup_path)
            return True, f"Backup created at {backup_path}", ""
        except Exception as e:
            return False, "", str(e)


class TaskScheduler:
    """
    Complete task scheduler application.
    
    Design Pattern: Command Pattern - Manages and executes scheduled jobs
    Design Pattern: Repository Pattern - Persistent job storage
    """
    
    def __init__(self, db_path: str = "jobs.sqlite"):
        self.db_path = db_path
        self.scheduler = BackgroundScheduler(
            jobstores={'default': SQLAlchemyJobStore(url=f'sqlite:///{db_path}')}
        )
        self.jobs: Dict[str, ScheduledJob] = {}
        self.executor = JobExecutor()
        self._load_jobs()
        self._setup_listeners()
    
    def _load_jobs(self):
        """Load jobs from persistent storage."""
        jobs_file = "scheduled_jobs.json"
        if os.path.exists(jobs_file):
            try:
                with open(jobs_file, 'r') as f:
                    data = json.load(f)
                    for job_data in data:
                        job = ScheduledJob.from_dict(job_data)
                        self.jobs[job.id] = job
                        if job.enabled:
                            self._schedule_job(job)
                print(f"  Loaded {len(self.jobs)} jobs from storage")
            except Exception as e:
                print(f"  Error loading jobs: {e}")
    
    def _save_jobs(self):
        """Save jobs to persistent storage."""
        jobs_file = "scheduled_jobs.json"
        with open(jobs_file, 'w') as f:
            json.dump([job.to_dict() for job in self.jobs.values()], f, indent=2)
    
    def _setup_listeners(self):
        """Setup job execution listeners."""
        def job_listener(event):
            job_id = event.job_id
            if job_id in self.jobs:
                job = self.jobs[job_id]
                if event.exception:
                    job.status = JobStatus.FAILED
                    job.last_result = str(event.exception)
                else:
                    job.status = JobStatus.COMPLETED
                    job.last_result = "Success"
                job.last_run = datetime.now()
                self._save_jobs()
        
        self.scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    
    def _schedule_job(self, job: ScheduledJob):
        """Schedule a job in APScheduler."""
        try:
            # Parse schedule (cron expression)
            parts = job.schedule.split()
            if len(parts) == 5:  # Cron format: minute hour day month day_of_week
                trigger = CronTrigger(
                    minute=parts[0], hour=parts[1], day=parts[2],
                    month=parts[3], day_of_week=parts[4]
                )
            elif len(parts) == 2 and parts[0].isdigit():  # Interval format: "minutes seconds"
                minutes = int(parts[0])
                seconds = int(parts[1]) if len(parts) > 1 else 0
                trigger = IntervalTrigger(minutes=minutes, seconds=seconds)
            else:
                raise ValueError(f"Invalid schedule format: {job.schedule}")
            
            # Create execution function
            def job_wrapper():
                self._execute_job(job.id)
            
            self.scheduler.add_job(
                job_wrapper,
                trigger=trigger,
                id=job.id,
                replace_existing=True
            )
            
            # Update next run time
            aps_job = self.scheduler.get_job(job.id)
            if aps_job and aps_job.next_run_time:
                job.next_run = aps_job.next_run_time
            
            print(f"  Scheduled job: {job.name} ({job.schedule})")
            
        except Exception as e:
            print(f"  Failed to schedule job {job.name}: {e}")
    
    def _execute_job(self, job_id: str):
        """Execute a job by ID."""
        job = self.jobs.get(job_id)
        if not job or not job.enabled:
            return
        
        print(f"\n  Executing job: {job.name} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        job.status = JobStatus.RUNNING
        self._save_jobs()
        
        success = False
        result = ""
        error = ""
        
        try:
            if job.job_type == JobType.COMMAND:
                success, result, error = self.executor.execute_command(job.config['command'])
            elif job.job_type == JobType.HTTP_REQUEST:
                success, result, error = self.executor.execute_http_request(
                    job.config['url'],
                    job.config.get('method', 'GET'),
                    job.config.get('headers'),
                    job.config.get('body')
                )
            elif job.job_type == JobType.BACKUP:
                success, result, error = self.executor.execute_backup(
                    job.config['source'],
                    job.config['destination']
                )
            elif job.job_type == JobType.PYTHON_FUNCTION:
                success, result, error = self.executor.execute_python_function(
                    job.config['module'],
                    job.config['function'],
                    job.config.get('args', []),
                    job.config.get('kwargs', {})
                )
            else:
                error = f"Unsupported job type: {job.job_type}"
            
            job.status = JobStatus.COMPLETED if success else JobStatus.FAILED
            job.last_result = result if success else error
            job.last_run = datetime.now()
            
            print(f"  Job completed: {'SUCCESS' if success else 'FAILED'}")
            if result:
                print(f"    Result: {result[:200]}")
            
        except Exception as e:
            job.status = JobStatus.FAILED
            job.last_result = str(e)
            print(f"  Job failed: {e}")
        
        finally:
            self._save_jobs()
    
    def add_job(self, job: ScheduledJob) -> bool:
        """Add a new scheduled job."""
        if job.id in self.jobs:
            return False
        
        self.jobs[job.id] = job
        if job.enabled:
            self._schedule_job(job)
        self._save_jobs()
        return True
    
    def update_job(self, job_id: str, updates: Dict) -> bool:
        """Update an existing job."""
        if job_id not in self.jobs:
            return False
        
        job = self.jobs[job_id]
        for key, value in updates.items():
            if hasattr(job, key):
                setattr(job, key, value)
        
        job.updated_at = datetime.now()
        
        # Reschedule if enabled
        if job.enabled:
            self.scheduler.remove_job(job_id)
            self._schedule_job(job)
        
        self._save_jobs()
        return True
    
    def delete_job(self, job_id: str) -> bool:
        """Delete a job."""
        if job_id not in self.jobs:
            return False
        
        self.scheduler.remove_job(job_id)
        del self.jobs[job_id]
        self._save_jobs()
        return True
    
    def enable_job(self, job_id: str) -> bool:
        """Enable a job."""
        if job_id not in self.jobs:
            return False
        
        job = self.jobs[job_id]
        job.enabled = True
        self._schedule_job(job)
        self._save_jobs()
        return True
    
    def disable_job(self, job_id: str) -> bool:
        """Disable a job."""
        if job_id not in self.jobs:
            return False
        
        job = self.jobs[job_id]
        job.enabled = False
        self.scheduler.remove_job(job_id)
        self._save_jobs()
        return True
    
    def run_job_now(self, job_id: str) -> bool:
        """Run a job immediately."""
        if job_id not in self.jobs:
            return False
        
        # Run in background thread to not block
        thread = threading.Thread(target=self._execute_job, args=(job_id,))
        thread.start()
        return True
    
    def get_job(self, job_id: str) -> Optional[ScheduledJob]:
        """Get a job by ID."""
        return self.jobs.get(job_id)
    
    def get_all_jobs(self) -> List[ScheduledJob]:
        """Get all jobs."""
        return list(self.jobs.values())
    
    def get_jobs_by_status(self, status: JobStatus) -> List[ScheduledJob]:
        """Get jobs by status."""
        return [j for j in self.jobs.values() if j.status == status]
    
    def get_jobs_by_type(self, job_type: JobType) -> List[ScheduledJob]:
        """Get jobs by type."""
        return [j for j in self.jobs.values() if j.job_type == job_type]
    
    def start(self):
        """Start the scheduler."""
        self.scheduler.start()
        print("  Task scheduler started")
    
    def stop(self):
        """Stop the scheduler."""
        self.scheduler.shutdown()
        print("  Task scheduler stopped")
    
    def get_statistics(self) -> Dict:
        """Get scheduler statistics."""
        jobs = self.jobs.values()
        return {
            "total_jobs": len(jobs),
            "enabled_jobs": sum(1 for j in jobs if j.enabled),
            "by_status": {
                status.value: sum(1 for j in jobs if j.status == status)
                for status in JobStatus
            },
            "by_type": {
                job_type.value: sum(1 for j in jobs if j.job_type == job_type)
                for job_type in JobType
            },
            "last_run": max((j.last_run for j in jobs if j.last_run), default=None)
        }


def demonstrate_task_scheduler():
    """
    Demonstrate the complete task scheduler.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: COMPLETE TASK SCHEDULER")
    print("=" * 60)
    
    # Create scheduler
    scheduler = TaskScheduler()
    
    print("\n1. ADDING JOBS")
    print("-" * 40)
    
    # Add a command job
    job1 = ScheduledJob(
        id="job_1",
        name="Disk Usage Check",
        job_type=JobType.COMMAND,
        config={"command": "df -h"},
        schedule="*/5 * * * *",  # Every 5 minutes
        enabled=True
    )
    scheduler.add_job(job1)
    
    # Add an HTTP request job
    job2 = ScheduledJob(
        id="job_2",
        name="Health Check API",
        job_type=JobType.HTTP_REQUEST,
        config={
            "url": "https://api.example.com/health",
            "method": "GET"
        },
        schedule="0 * * * *",  # Every hour
        enabled=True
    )
    scheduler.add_job(job2)
    
    # Add a backup job
    job3 = ScheduledJob(
        id="job_3",
        name="Daily Backup",
        job_type=JobType.BACKUP,
        config={
            "source": "/path/to/source",
            "destination": "/path/to/backup"
        },
        schedule="0 2 * * *",  # Daily at 2 AM
        enabled=True
    )
    scheduler.add_job(job3)
    
    print("\n2. LISTING JOBS")
    print("-" * 40)
    
    for job in scheduler.get_all_jobs():
        print(f"  {job.id}: {job.name} - {job.schedule} - {'Enabled' if job.enabled else 'Disabled'}")
    
    print("\n3. JOB STATISTICS")
    print("-" * 40)
    
    stats = scheduler.get_statistics()
    print(f"  Total jobs: {stats['total_jobs']}")
    print(f"  Enabled jobs: {stats['enabled_jobs']}")
    print(f"  By type: {stats['by_type']}")
    
    print("\n4. UPDATING A JOB")
    print("-" * 40)
    
    scheduler.update_job("job_1", {"enabled": False})
    print("  Disabled job_1")
    
    print("\n5. RUNNING JOB MANUALLY (DEMO)")
    print("-" * 40)
    
    # Create a simple test job
    test_job = ScheduledJob(
        id="test_job",
        name="Test Job",
        job_type=JobType.COMMAND,
        config={"command": "echo 'Hello from scheduled task'"},
        schedule="0 * * * *",
        enabled=False
    )
    scheduler.add_job(test_job)
    
    print("  Running test job manually...")
    scheduler.run_job_now("test_job")
    time.sleep(1)  # Wait for execution
    
    test_job_result = scheduler.get_job("test_job")
    if test_job_result:
        print(f"  Job status: {test_job_result.status.value}")
        print(f"  Result: {test_job_result.last_result}")
    
    print("\n6. CLEANING UP")
    print("-" * 40)
    
    scheduler.delete_job("test_job")
    print("  Deleted test job")
    
    # Clean up files
    import os
    if os.path.exists("scheduled_jobs.json"):
        os.remove("scheduled_jobs.json")
    if os.path.exists("jobs.sqlite"):
        os.remove("jobs.sqlite")
    print("  Cleaned up storage files")


if __name__ == "__main__":
    demonstrate_task_scheduler()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Schedule Library** – Simple, human-readable syntax. `schedule.every(10).minutes.do(job)`. Run pending jobs in loop.

- **Schedule Intervals** – Seconds, minutes, hours, days, weeks. Day of week (Monday, Tuesday). Time of day (`.at("10:30")`).

- **Job Management** – Tags for grouping. Cancel by tag or reference. Clear all jobs.

- **APScheduler** – Advanced scheduling with cron expressions. Three trigger types: interval, cron, date.

- **Cron Expressions** – `minute hour day month day_of_week`. Examples: `0 * * * *` (hourly), `0 2 * * *` (daily at 2 AM), `*/15 * * * *` (every 15 minutes).

- **Job Stores** – In-memory, SQLite, PostgreSQL, Redis. Jobs persist across restarts.

- **Backup System** – Schedule weekly full backups. Daily incremental backups. Automatic rotation.

- **Notification Scheduler** – Email, Slack, console notifications. Schedule recurring alerts. Monitor system health.

- **Task Scheduler** – Complete job management system. Support for commands, HTTP requests, backups, Python functions. Persistent storage.

- **SOLID Principles Applied** – Single Responsibility (each scheduler component has one purpose), Open/Closed (new job types can be added), Dependency Inversion (depends on abstractions), Interface Segregation (clean scheduler interfaces).

- **Design Patterns Used** – Command Pattern (scheduled jobs), Strategy Pattern (different job types), Observer Pattern (job listeners), Factory Pattern (job creation), Repository Pattern (persistent storage), Proxy Pattern (job execution wrapper).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Web Scraping with BeautifulSoup

- **📚 Series H Catalog:** Web Development & Automation – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Scikit-learn – Traditional ML (Series I, Story 1)

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
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **50** | **2** | **96%** |

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

**Next Story:** Series I, Story 1: The 2026 Python Metromap: Scikit-learn – Traditional ML

---

## 📝 Your Invitation

**Congratulations! You've completed the Web Development & Automation Line!**

You've mastered:
- Flask (REST APIs, URL shorteners, task management)
- Django (full-stack web apps, admin interface, authentication)
- os and sys (file organization, system monitoring, automation)
- BeautifulSoup (web scraping, price monitoring, news aggregation)
- Schedule and APScheduler (task scheduling, backups, notifications)

Now build something with what you've learned:

1. **Build a social media posting bot** – Schedule posts to Twitter, LinkedIn, Facebook.

2. **Create a website uptime monitor** – Check websites regularly, send alerts when down.

3. **Build a data backup service** – Schedule backups of databases to cloud storage.

4. **Create a report generator** – Pull data from APIs, generate PDF reports, email them.

5. **Build a job application tracker** – Scrape job boards, schedule daily checks, send summaries.

**You've mastered Web Development & Automation. Next stop: AI & Machine Learning – Scikit-learn!**

---

*Found this helpful? Clap, comment, and share what you automated. Next stop: Scikit-learn!* 🚇