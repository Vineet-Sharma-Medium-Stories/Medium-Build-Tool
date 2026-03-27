#!/usr/bin/env python3
"""
Extract tables and mermaid diagrams from markdown and generate PNG images using yyds_md2png.
Creates organized output structure with source links.
"""

import re
import os
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
import hashlib
import shutil
import time

def normalize(text, max_length=30):
    """Convert text to normalized filename with length limit."""
    if not text:
        return "untitled"
    # Replace spaces with hyphens
    text = text.replace(' ', '-')
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\-]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text if text else "untitled"

def create_filename(prefix, index, title, max_length=30):
    """Create a filename with hash if needed"""
    safe_title = normalize(title, max_length)
    base = f"{prefix}_{index:02d}_{safe_title}"
    
    # Check if we need to add hash (if title was truncated)
    original_normalized = normalize(title, 100)  # Longer version for hash
    if len(original_normalized) > max_length:
        # Add hash for uniqueness
        text_hash = hashlib.md5(original_normalized.encode()).hexdigest()[:4]
        return f"{base}-{text_hash}"
    return base

def extract_tables(content):
    tables = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('|') and i+1 < len(lines) and '---' in lines[i+1]:
            title = f"Table {len(tables)+1}"
            j = i-1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                title = lines[j].strip()[:50]
            table = []
            start = i
            while i < len(lines) and lines[i].strip().startswith('|'):
                table.append(lines[i])
                i += 1
            tables.append((title, '\n'.join(table), start))
        else:
            i += 1
    return tables

def extract_diagrams(content):
    diags = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].strip() == '```mermaid':
            title = f"Diagram {len(diags)+1}"
            j = i-1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                title = lines[j].strip()[:50]
            code = []
            i += 1
            while i < len(lines) and lines[i].strip() != '```':
                code.append(lines[i])
                i += 1
            diags.append((title, '\n'.join(code), i))
        i += 1
    return diags

def generate_png(md_file, include_title_in_image=True):
    """Generate PNG using yyds_md2png"""
    try:
        if include_title_in_image:
            # Use original file
            cmd = ['yyds_md2png', str(md_file), '--width', '1400']
        else:
            # Read the file content
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove the first line (title) if it starts with #
            lines = content.split('\n')
            if lines and lines[0].startswith('# '):
                # Skip the title line
                content_without_title = '\n'.join(lines[1:])
            else:
                content_without_title = content
            
            # Write back to the same file temporarily (without title)
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content_without_title)
            
            # Generate PNG
            cmd = ['yyds_md2png', str(md_file)]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        time.sleep(1)  # Wait for file to be written
        return result.returncode == 0
    except Exception as e:
        print(f"      Generation error: {e}")
        return False
    finally:
        # If we modified the file, restore it
        if not include_title_in_image:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # Restore the title
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(f"# {Path(md_file).stem}\n\n{content}")

def rename_default_files_in_images_folder(images_dir):
    """Find all _default_ files in images folder and rename them without _default"""
    renamed_count = 0
    
    # Find all _default_ files in the images folder
    for default_file in images_dir.glob("*_default_*.png"):
        if default_file.exists() and default_file.stat().st_size > 5000:
            # Extract the base name (remove _default_timestamp)
            base_name = default_file.stem.split('_default_')[0]
            new_name = base_name + '.png'
            target_path = images_dir / new_name
            
            # Rename (move within same folder)
            print(f"  Found: {default_file.name}")
            shutil.move(str(default_file), str(target_path))
            print(f"  Renamed to: {new_name}")
            renamed_count += 1
    
    return renamed_count

def create_combined_file(original_file, out_dir, folder_name, table_info, diagram_info, with_image_titles=False):
    """Create single combined markdown file with images replacing original content."""
    github_base = "https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/"
    
    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    table_idx = 0
    diagram_idx = 0
    
    while i < len(lines):
        line = lines[i]
        
        if line.strip().startswith('|') and i+1 < len(lines) and '---' in lines[i+1]:
            title = ""
            j = i-1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                title = lines[j].strip()
            
            while i < len(lines) and (lines[i].strip().startswith('|') or '---' in lines[i]):
                i += 1
            
            if table_idx < len(table_info):
                base_name = table_info[table_idx][4]  # Get stored base name
                img_file = f"images/{base_name}.png"
                md_file = f"{base_name}.md"
                
                # Add image title only if flag is set
                if with_image_titles and title:
                    new_lines.append(f"### {title}")
                    new_lines.append("")
                
                new_lines.append(f"![{title}]({img_file})")
                new_lines.append("")
                new_lines.append(f"[View Source]({github_base}{folder_name}/{md_file})")
                new_lines.append("")
                table_idx += 1
        
        elif line.strip() == '```mermaid':
            title = ""
            j = i-1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                title = lines[j].strip()
            
            new_lines.append(line)
            i += 1
            while i < len(lines) and lines[i].strip() != '```':
                i += 1
            if i < len(lines):
                new_lines.append(lines[i])
                i += 1
            
            if diagram_idx < len(diagram_info):
                base_name = diagram_info[diagram_idx][3]  # Get stored base name
                img_file = f"images/{base_name}.png"
                md_file = f"{base_name}.md"
                
                new_lines.append("")
                # Add image title only if flag is set
                if with_image_titles and title:
                    new_lines.append(f"### {title}")
                    new_lines.append("")
                
                new_lines.append(f"![{title}]({img_file})")
                new_lines.append("")
                new_lines.append(f"[View Source]({github_base}{folder_name}/{md_file})")
                new_lines.append("")
                diagram_idx += 1
        else:
            new_lines.append(line)
            i += 1
    
    combined_file = out_dir / f"{folder_name}.md"
    with open(combined_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    return combined_file

def cleanup_temp_files(out_dir):
    """Remove any leftover HTML files"""
    for html_file in out_dir.glob("*.html"):
        if html_file.exists():
            html_file.unlink()

def main():
    parser = argparse.ArgumentParser(description='Extract tables and diagrams from markdown and generate PNG images.')
    parser.add_argument('input_file', nargs='?', 
                       default="Code to Cluster: Building a Bulletproof Kubernetes Deployment Pipeline on AWS.md",
                       help='Input markdown file (default: "Code to Cluster: Building a Bulletproof Kubernetes Deployment Pipeline on AWS.md")')
    parser.add_argument('--with-image-title', action='store_true',
                       help='Include titles above images in the combined markdown file')
    
    args = parser.parse_args()
    
    input_file = args.input_file
    with_image_titles = args.with_image_title
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        return
    
    folder = normalize(Path(input_file).stem, 30)
    out = Path(folder)
    out.mkdir(exist_ok=True)
    
    print(f"Output folder: {out}/")
    print(f"Include image titles: {with_image_titles}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tables = extract_tables(content)
    diagrams = extract_diagrams(content)
    
    print(f"Found {len(tables)} tables, {len(diagrams)} diagrams")
    print("")
    
    table_info = []
    diagram_info = []
    
    print("Saving markdown files...")
    for i, (title, content, line) in enumerate(tables, 1):
        base_name = create_filename("table", i, title)
        name = f"{base_name}.md"
        path = out / name
        has_icons = bool(re.search(r'[✅❌⚠️🆓💰☁️🐳🐙⎈⭐🌟🔥🚀🔒🔑]', content))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n{content}\n")
        table_info.append((title, path, line, has_icons, base_name))
        print(f"  OK Table {i}: {name}")
    
    for i, (title, content, line) in enumerate(diagrams, 1):
        base_name = create_filename("diagram", i, title)
        name = f"{base_name}.md"
        path = out / name
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n```mermaid\n{content}\n```\n")
        diagram_info.append((title, path, line, base_name))
        print(f"  OK Diagram {i}: {name}")
    
    print("\nGenerating PNG images...")
    images_dir = out / 'images'
    images_dir.mkdir(exist_ok=True)
    
    # Generate PNG for tables
    for i, (title, path, line, has_icons, base_name) in enumerate(table_info, 1):
        print(f"  Generating {base_name}.png...")
        if generate_png(path, include_title_in_image=with_image_titles):
            print(f"    Generation completed")
        else:
            print(f"    Generation failed")
    
    # Generate PNG for diagrams
    for i, (title, path, line, base_name) in enumerate(diagram_info, 1):
        print(f"  Generating {base_name}.png...")
        if generate_png(path, include_title_in_image=with_image_titles):
            print(f"    Generation completed")
        else:
            print(f"    Generation failed")
    
    # Wait a bit for all files to be written
    time.sleep(2)
    
    # Move all PNG files to images folder and rename them
    print("\nMoving and renaming PNG files to images folder...")
    
    # First, move any PNG files from output folder to images folder
    for png_file in out.glob("*.png"):
        if png_file.exists() and "temp_" not in png_file.name:
            target = images_dir / png_file.name
            shutil.move(str(png_file), str(target))
            print(f"  Moved: {png_file.name} -> images/")
    
    # Also check for PNG files in current directory
    for png_file in Path.cwd().glob("*.png"):
        if png_file.exists() and png_file.stat().st_size > 5000 and "temp_" not in png_file.name:
            target = images_dir / png_file.name
            shutil.move(str(png_file), str(target))
            print(f"  Moved: {png_file.name} -> images/")
    
    # Rename any _default files in images folder
    renamed = rename_default_files_in_images_folder(images_dir)
    if renamed > 0:
        print(f"  Renamed {renamed} _default files")
    
    # Count PNGs in images folder
    png_count = len(list(images_dir.glob("*.png")))
    
    print("\nCreating combined markdown file with images...")
    combined = create_combined_file(input_file, out, folder, table_info, diagram_info, with_image_titles)
    print(f"  OK Created: {combined.name}")
    
    print("\nCreating README...")
    github_base = "https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/"
    
    readme = []
    readme.append(f"# {folder.replace('-', ' ').title()}")
    readme.append("")
    readme.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    readme.append("")
    readme.append("## Summary")
    readme.append(f"- Tables: {len(tables)}")
    readme.append(f"- Diagrams: {len(diagrams)}")
    readme.append(f"- PNG Images: {png_count}")
    readme.append("")
    readme.append("## Combined Document")
    readme.append(f"- [{folder}.md]({folder}.md) - Single file with all images")
    if with_image_titles:
        readme.append("  - Image titles are included")
    readme.append("")
    
    if table_info:
        readme.append("## Tables")
        readme.append("")
        readme.append("| # | Title | Icons | Markdown | PNG | Size |")
        readme.append("|---|-------|-------|----------|-----|------|")
        for i, (title, path, line, has_icons, base_name) in enumerate(table_info, 1):
            icon = "✅" if has_icons else "❌"
            short_title = title[:40] + "..." if len(title) > 40 else title
            png_path = images_dir / f"{base_name}.png"
            md_filename = f"{base_name}.md"
            
            if png_path.exists():
                png_status = "✅"
                size = f"{png_path.stat().st_size // 1024}KB"
            else:
                png_status = "❌"
                size = "0KB"
            
            readme.append(f"| {i} | {short_title} | {icon} | [📄]({md_filename}) | {png_status} | {size} |")
        readme.append("")
    
    if diagram_info:
        readme.append("## Diagrams")
        readme.append("")
        readme.append("| # | Title | Markdown | PNG | Size |")
        readme.append("|---|-------|----------|-----|------|")
        for i, (title, path, line, base_name) in enumerate(diagram_info, 1):
            short_title = title[:40] + "..." if len(title) > 40 else title
            png_path = images_dir / f"{base_name}.png"
            md_filename = f"{base_name}.md"
            
            if png_path.exists():
                png_status = "✅"
                size = f"{png_path.stat().st_size // 1024}KB"
            else:
                png_status = "❌"
                size = "0KB"
            
            readme.append(f"| {i} | {short_title} | [📄]({md_filename}) | {png_status} | {size} |")
        readme.append("")
    
    readme.append("---")
    readme.append(f"### View Source Links")
    readme.append("")
    readme.append(f"- [Combined File]({github_base}{folder}/{folder}.md)")
    for i, (title, path, line, has_icons, base_name) in enumerate(table_info, 1):
        md_filename = f"{base_name}.md"
        readme.append(f"- [Table {i}]({github_base}{folder}/{md_filename})")
    for i, (title, path, line, base_name) in enumerate(diagram_info, 1):
        md_filename = f"{base_name}.md"
        readme.append(f"- [Diagram {i}]({github_base}{folder}/{md_filename})")
    
    with open(out / 'README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(readme))
    
    print(f"  OK Created: README.md")
    
    # Final cleanup - remove HTML files
    cleanup_temp_files(out)
    
    print("\n" + "=" * 50)
    print("COMPLETE!")
    print("=" * 50)
    print(f"\nOutput directory: {out}/")
    print(f"\nFiles created in {out}/:")
    print(f"  • README.md - Main index")
    print(f"  • {folder}.md - Combined document (image titles: {with_image_titles})")
    print(f"  • images/ - {png_count} PNG images")
    print(f"  • table_*.md - {len(table_info)} table files")
    print(f"  • diagram_*.md - {len(diagram_info)} diagram files")

if __name__ == "__main__":
    main()