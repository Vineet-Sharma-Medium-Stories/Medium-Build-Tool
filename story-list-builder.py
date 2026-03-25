#!/usr/bin/env python3
"""
Story Management Script
Scans for markdown files and adds new stories to Stories.md.
Preserves all existing content and only adds new stories.
Uses standard markdown tables for better compatibility.
"""

import os
import sys
import re
import urllib.parse
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def encode_path_for_markdown(path):
    """
    Encode special characters in path for markdown links
    """
    parts = path.split('/')
    encoded_parts = []
    for part in parts:
        encoded_part = part.replace(' ', '%20')
        encoded_part = encoded_part.replace('(', '%28')
        encoded_part = encoded_part.replace(')', '%29')
        encoded_part = encoded_part.replace(':', '%3A')
        encoded_parts.append(encoded_part)
    return '/'.join(encoded_parts)

def find_markdown_files(parent_dir):
    """
    Scan ONLY immediate subfolders and root level for .md files.
    Does NOT search recursively - only one level deep.
    """
    markdown_files = []
    parent_path = Path(parent_dir).resolve()
    
    print(f"\n📁 Scanning root level: {parent_path}")
    
    # 1. Scan root level (parent directory) for .md files
    for file in parent_path.iterdir():
        if file.is_file() and file.suffix.lower() == '.md' and file.name != "Image Prompt.md":
            print(f"   ✓ Found at root: {file.name}")
            encoded_name = encode_path_for_markdown(file.name)
            markdown_files.append({
                'name': file.name,
                'path': str(file),
                'rel_path': encoded_name,
                'folder': '.'
            })
    
    # 2. Scan ONLY immediate subfolders (one level deep)
    for item in parent_path.iterdir():
        if item.is_dir():
            folder_name = item.name
            print(f"\n📂 Scanning folder: {folder_name}/ (only direct files)")
            
            encoded_folder = encode_path_for_markdown(folder_name)
            file_count = 0
            
            for file in item.iterdir():
                if file.is_file() and file.suffix.lower() == '.md' and file.name != "Image Prompt.md":
                    print(f"   ✓ Found in {folder_name}/: {file.name}")
                    encoded_filename = encode_path_for_markdown(file.name)
                    markdown_files.append({
                        'name': file.name,
                        'path': str(file),
                        'rel_path': f"{encoded_folder}/{encoded_filename}",
                        'folder': folder_name
                    })
                    file_count += 1
            
            if file_count == 0:
                print(f"   ℹ️  No markdown files found in {folder_name}/")
    
    return markdown_files

def parse_stories_file(content):
    """
    Parse Stories.md and extract all stories with their current data
    Returns: stories dict, folder_data dict
    """
    stories = {}
    folder_data = defaultdict(lambda: {'stories': [], 'total': 0, 'published': 0})
    
    lines = content.split('\n')
    current_folder = None
    
    for line in lines:
        # Detect folder headers
        if line.startswith('### '):
            folder_line = line[4:].strip()
            # Extract folder name without counts
            if '(' in folder_line:
                current_folder = folder_line[:folder_line.index('(')].strip()
            else:
                current_folder = folder_line
        
        # Detect table rows (markdown format)
        elif line.startswith('|') and not line.startswith('|---') and not line.startswith('| Story'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 4 and current_folder and '[' in parts[0] and ']' in parts[0]:
                # Extract story name from markdown link
                story_match = re.search(r'\[([^\]]+)\]\([^\)]+\)', parts[0])
                if story_match:
                    story_name = story_match.group(1)
                    status = parts[1] if len(parts) > 1 else "Draft"
                    published = parts[2] if len(parts) > 2 else "--"
                    created = parts[3] if len(parts) > 3 else ""
                    
                    # Remove ✅ emoji if present
                    published = published.replace('✅ ', '')
                    
                    key = f"{current_folder}/{story_name}"
                    stories[key] = {
                        'name': story_name,
                        'folder': current_folder,
                        'status': status,
                        'published': published,
                        'created': created
                    }
                    
                    # Update folder data
                    folder_data[current_folder]['stories'].append(story_name)
                    folder_data[current_folder]['total'] += 1
                    if published != "--":
                        folder_data[current_folder]['published'] += 1
    
    return stories, folder_data

def rebuild_stories_file(stories_file, all_markdown_files, existing_stories):
    """
    Completely rebuild Stories.md with all stories, preserving existing status/dates
    """
    # Group markdown files by folder
    files_by_folder = defaultdict(list)
    for md_file in all_markdown_files:
        folder_name = "Root Level" if md_file['folder'] == '.' else md_file['folder']
        files_by_folder[folder_name].append(md_file)
    
    # Prepare all stories with their data
    all_stories_data = []
    
    for folder, files in files_by_folder.items():
        for file in sorted(files, key=lambda x: x['name']):
            key = f"{folder}/{file['name']}"
            if key in existing_stories:
                # Use existing data
                story_data = existing_stories[key]
                all_stories_data.append({
                    'name': file['name'],
                    'folder': folder,
                    'rel_path': file['rel_path'],
                    'status': story_data['status'],
                    'published': story_data['published'],
                    'created': story_data['created']
                })
            else:
                # New story
                current_date = datetime.now().strftime("%d/%m/%Y")
                all_stories_data.append({
                    'name': file['name'],
                    'folder': folder,
                    'rel_path': file['rel_path'],
                    'status': 'Draft',
                    'published': '--',
                    'created': current_date
                })
    
    # Group by folder for output
    stories_by_folder = defaultdict(list)
    for story in all_stories_data:
        stories_by_folder[story['folder']].append(story)
    
    # Calculate global statistics
    total_stories = len(all_stories_data)
    draft_stories = len([s for s in all_stories_data if s['status'] == 'Draft'])
    published_stories = len([s for s in all_stories_data if s['published'] != '--'])
    
    # Build the new content
    new_content = []
    
    # Header
    new_content.append("# Stories")
    new_content.append("")
    new_content.append("*Technical Articles*")
    new_content.append("")
    
    # Summary
    new_content.append("## Summary")
    new_content.append("")
    new_content.append(f"**Total Stories:** {total_stories}")
    new_content.append(f"**📝 Draft:** {draft_stories}")
    new_content.append(f"**✅ Published:** {published_stories}")
    new_content.append("")
    new_content.append("---")
    new_content.append("")
    
    # Story List
    new_content.append("## Story List")
    new_content.append("")
    
    # Process folders: subfolders first, then Root Level
    folders = [f for f in stories_by_folder.keys() if f != "Root Level"]
    folders.sort()
    if "Root Level" in stories_by_folder:
        folders.append("Root Level")
    
    for folder in folders:
        stories = stories_by_folder[folder]
        folder_total = len(stories)
        folder_published = len([s for s in stories if s['published'] != '--'])
        
        new_content.append(f"### {folder} ({folder_total} stories, {folder_published} published)")
        new_content.append("")
        new_content.append("| Story | Status | Published | Created |")
        new_content.append("|-------|--------|-----------|---------|")
        
        for story in stories:
            story_link = f"[{story['name']}]({story['rel_path']})"
            published_display = story['published']
            if published_display != "--":
                published_display = f"✅ {published_display}"
            
            new_content.append(f"| {story_link} | {story['status']} | {published_display} | {story['created']} |")
        
        new_content.append("")
    
    # Last updated
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_content.append("---")
    new_content.append("")
    new_content.append(f"*Last updated: {current_time}*")
    
    # Write to file
    with open(stories_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_content))
    
    return total_stories, draft_stories, published_stories, len([s for s in all_stories_data if s['status'] == 'Draft' and s['published'] == '--' and s not in existing_stories.values()])

def main():
    """
    Main function
    """
    script_dir = Path(__file__).parent
    parent_dir = script_dir
    stories_file = script_dir / "Stories.md"
    
    print("=" * 70)
    print("📚 STORY MANAGEMENT SYSTEM")
    print("=" * 70)
    print(f"📍 Directory: {parent_dir}")
    print(f"📄 Stories file: {stories_file}")
    print("-" * 70)
    
    # Find all markdown files
    print("\n🔍 SCANNING FOR MARKDOWN FILES")
    print("-" * 70)
    markdown_files = find_markdown_files(parent_dir)
    
    print("\n" + "=" * 70)
    print("📊 SCAN RESULTS")
    print("-" * 70)
    
    if not markdown_files:
        print("❌ No markdown files found!")
        return
    
    # Count by location
    root_files = [f for f in markdown_files if f['folder'] == '.']
    folder_files = [f for f in markdown_files if f['folder'] != '.']
    
    print(f"📁 Total markdown files found: {len(markdown_files)}")
    print(f"   📄 Root level: {len(root_files)} file(s)")
    
    if folder_files:
        folders = set(f['folder'] for f in folder_files)
        print(f"   📂 Subfolders: {len(folder_files)} file(s) in {len(folders)} folder(s)")
        for folder in sorted(folders):
            count = len([f for f in folder_files if f['folder'] == folder])
            print(f"      • {folder}/: {count} file(s)")
    
    # Parse existing Stories.md if it exists
    existing_stories = {}
    if stories_file.exists():
        print("\n🔍 PARSING EXISTING STORIES.MD")
        print("-" * 70)
        with open(stories_file, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        existing_stories, folder_data = parse_stories_file(existing_content)
        print(f"📝 Found {len(existing_stories)} existing stories")
        print(f"📂 Found {len(folder_data)} existing folders")
        
        # Show existing published count
        existing_published = len([s for s in existing_stories.values() if s['published'] != '--'])
        print(f"✅ Existing published stories: {existing_published}")
    
    # Rebuild Stories.md
    print("\n📝 REBUILDING STORIES.MD")
    print("-" * 70)
    total, draft, published, new_count = rebuild_stories_file(stories_file, markdown_files, existing_stories)
    
    print("\n" + "=" * 70)
    print("✅ OPERATION COMPLETE")
    print("-" * 70)
    print(f"📊 Final Statistics:")
    print(f"   • Total stories: {total}")
    print(f"   • 📝 Draft stories: {draft}")
    print(f"   • ✅ Published stories: {published}")
    if new_count > 0:
        print(f"   • ✨ New stories added: {new_count}")
    else:
        print(f"   • 🔄 No new stories added")
    
    print("\n📋 Table Columns:")
    print("   • Story - Clickable link to the markdown file")
    print("   • Status - Current status (Draft, Published, etc.)")
    print("   • Published - Publication date (-- if not published)")
    print("   • Created - Date when story was added (DD/MM/YYYY format)")
    print("\n💡 Note: All statistics are calculated from actual data")
    print("   Published count = stories with actual dates (not '--')")
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)