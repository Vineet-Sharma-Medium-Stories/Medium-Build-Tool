#!/usr/bin/env python3
"""
Shared utilities for story processing scripts
Provides consistent filename generation and text extraction functions
"""

import re
import os
from datetime import datetime

def sanitize_filename(name):
    """Strip filename to fit git commit standards (lowercase, hyphens, no special chars)"""
    if not name:
        return "untitled"
    name = re.sub(r'[\s_]+', '-', name.lower())
    name = re.sub(r'[^a-z0-9-]', '', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')

def extract_title_from_content(content_lines, start_line, max_lines_before=10):
    """
    Extract title from content looking at preceding lines
    Returns: title string
    """
    title = "Untitled"
    for j in range(max(0, start_line-max_lines_before), start_line):
        line = content_lines[j] if j < len(content_lines) else ""
        # Check for headings
        if re.match(r'^#{1,6}\s+(.+)', line):
            title = re.sub(r'^#{1,6}\s+', '', line).strip()
            break
        # Check for bold text
        elif '**' in line:
            bold_match = re.search(r'\*\*(.+?)\*\*', line)
            if bold_match:
                title = bold_match.group(1)
                break
    return title

def get_element_filename(element_type, index, title, max_title_length=30):
    """
    Generate consistent filename for diagram or table
    
    Args:
        element_type: 'mermaid' or 'table'
        index: integer index (1-based)
        title: element title
        max_title_length: max chars for title part
    
    Returns: filename string (e.g., "01-m-dynamic-few-shot-selection.md")
    """
    prefix = 'm' if element_type == 'mermaid' else 't'
    safe_title = sanitize_filename(title)[:max_title_length]
    return f"{index:02d}-{prefix}-{safe_title}.md"

def calculate_position(lines, line_index):
    """Calculate character position from line index"""
    return sum(len(l) + 1 for l in lines[:line_index])

def get_log_timestamp():
    """Get timestamp string for log files"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def format_log_entry(message, level="INFO"):
    """Format a log entry with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {level}: {message}"