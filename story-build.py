#!/usr/bin/env python3
"""
Extract tables and mermaid diagrams from markdown and generate PNG images.
Uses Playwright for reliable rendering with GitHub-style formatting.
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
import tempfile
import sys

def normalize(text, max_length=30):
    """Convert text to normalized filename with length limit."""
    if not text:
        return "untitled"
    text = text.replace(' ', '-')
    text = re.sub(r'[^a-zA-Z0-9\-]', '', text)
    text = text.lower()
    text = text.strip('-')
    return text if text else "untitled"

def normalize_filename(filename):
    """Normalize filename to remove special characters that might cause issues"""
    filename = Path(filename).name
    filename = filename.replace(' ', '-')
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.replace('%20', '-')
    return filename

def create_filename(prefix, index, title, max_length=30):
    """Create a filename with hash if needed"""
    safe_title = normalize(title, max_length)
    base = f"{prefix}_{index:02d}_{safe_title}"
    
    original_normalized = normalize(title, 100)
    if len(original_normalized) > max_length:
        text_hash = hashlib.md5(original_normalized.encode()).hexdigest()[:4]
        return f"{base}-{text_hash}"
    return base

def extract_tables(content):
    """Extract markdown tables from content"""
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
    """Extract mermaid diagrams from content"""
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

def extract_images_from_markdown(content):
    """Extract all image references from markdown content"""
    all_images = []
    image_pattern = r'!\[(.*?)\]\(([^)]+)\)'
    images = re.findall(image_pattern, content)
    
    for alt, path in images:
        path = path.strip()
        all_images.append((alt, path))
    
    html_img_pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>'
    html_images = re.findall(html_img_pattern, content)
    
    for path in html_images:
        path = path.strip()
        all_images.append(("", path))
    
    return all_images

def copy_missing_images(original_file, output_dir):
    """Copy images from the original file's directory and images folder to the output images folder"""
    original_dir = Path(original_file).parent
    images_dir = output_dir / 'images'
    images_dir.mkdir(exist_ok=True)
    original_images_dir = original_dir / 'images'
    
    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    images = extract_images_from_markdown(content)
    copied_count = 0
    
    for alt, img_path in images:
        if img_path.startswith('http://') or img_path.startswith('https://'):
            continue
        
        img_path = img_path.strip()
        img_path = re.sub(r'^[<>\'"]+|[<>\'"]+$', '', img_path)
        img_path = img_path.replace('%20', ' ')
        img_path = img_path.split('?')[0]
        img_path = img_path.split('#')[0]
        
        possible_paths = []
        possible_paths.append(original_dir / img_path)
        possible_paths.append(original_dir / Path(img_path).name)
        possible_paths.append(original_images_dir / Path(img_path).name)
        
        if 'images/' in img_path:
            clean_path = img_path.replace('images/', '')
            possible_paths.append(original_dir / clean_path)
            possible_paths.append(original_images_dir / clean_path)
        
        if ' ' in img_path:
            no_spaces = img_path.replace(' ', '-')
            possible_paths.append(original_dir / no_spaces)
            possible_paths.append(original_images_dir / no_spaces)
            no_spaces_underscore = img_path.replace(' ', '_')
            possible_paths.append(original_dir / no_spaces_underscore)
            possible_paths.append(original_images_dir / no_spaces_underscore)
        
        if '.' not in Path(img_path).suffix:
            for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
                possible_paths.append(original_dir / (img_path + ext))
                possible_paths.append(original_images_dir / (img_path + ext))
                if ' ' in img_path:
                    possible_paths.append(original_dir / (img_path.replace(' ', '-') + ext))
                    possible_paths.append(original_images_dir / (img_path.replace(' ', '-') + ext))
        
        found = False
        for img_file in possible_paths:
            if img_file.exists() and img_file.is_file():
                if img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
                    safe_filename = normalize_filename(img_file.name)
                    target_file = images_dir / safe_filename
                    if not target_file.exists():
                        shutil.copy2(str(img_file), str(target_file))
                        print(f"  Copied: {img_file.name} -> {safe_filename}")
                        copied_count += 1
                        found = True
                        break
        
        if not found and img_path:
            pass
    
    return copied_count

def extract_bold_or_heading_from_markdown(content):
    """Extract title from markdown content: first bold, then heading"""
    lines = content.split('\n')
    
    for line in lines[:5]:
        bold_matches = re.findall(r'\*\*(.+?)\*\*|__(.+?)__', line)
        if bold_matches:
            for match in bold_matches:
                title = match[0] or match[1]
                if title and len(title) > 3:
                    return title.strip()
    
    for line in lines[:5]:
        if line.startswith('# '):
            return line[2:].strip()
        elif line.startswith('## '):
            return line[3:].strip()
    
    return None

def parse_markdown_table(table_content):
    """Parse markdown table and return structured data"""
    lines = table_content.strip().split('\n')
    if len(lines) < 2:
        return None
    
    header_line = lines[0]
    headers = [h.strip() for h in header_line.split('|') if h.strip()]
    
    separator_line = lines[1]
    alignments = []
    for sep in separator_line.split('|'):
        sep = sep.strip()
        if ':-:' in sep:
            alignments.append('center')
        elif ':-' in sep:
            alignments.append('left')
        elif '-:' in sep:
            alignments.append('right')
        elif '-' in sep:
            alignments.append('left')
        else:
            alignments.append('left')
    
    rows = []
    for line in lines[2:]:
        if line.strip():
            cells = [c.strip() for c in line.split('|')]
            if cells and cells[0] == '':
                cells = cells[1:]
            if cells and cells[-1] == '':
                cells = cells[:-1]
            rows.append(cells)
    
    return {
        'headers': headers,
        'alignments': alignments,
        'rows': rows
    }

def format_markdown_cell(cell):
    """Convert markdown formatting in a cell to HTML"""
    if not cell:
        return ""
    
    cell = cell.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    cell = re.sub(r'`([^`]+)`', r'<code>\1</code>', cell)
    cell = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', cell)
    cell = re.sub(r'___(.+?)___', r'<strong><em>\1</em></strong>', cell)
    cell = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell)
    cell = re.sub(r'__(.+?)__', r'<strong>\1</strong>', cell)
    cell = re.sub(r'\*(.+?)\*', r'<em>\1</em>', cell)
    cell = re.sub(r'_(.+?)_', r'<em>\1</em>', cell)
    
    emoji_map = {
        ':white_check_mark:': '✅', ':heavy_check_mark:': '✔️', ':warning:': '⚠️',
        ':arrows_counterclockwise:': '🔄', ':moneybag:': '💰', ':cloud:': '☁️',
        ':whale:': '🐳', ':octopus:': '🐙', ':alarm_clock:': '⏰', ':star:': '⭐',
        ':star2:': '🌟', ':fire:': '🔥', ':rocket:': '🚀', ':key:': '🔒',
        ':closed_lock_with_key:': '🔑', ':checkered_flag:': '🏁', ':gear:': '⚙️',
        ':book:': '📚', ':zap:': '⚡', ':package:': '📦', ':hammer:': '🔨',
        ':wrench:': '🔧', ':bulb:': '💡', ':chart_with_upwards_trend:': '📈',
        ':chart_with_downwards_trend:': '📉', ':sparkles:': '✨', ':tada:': '🎉',
        ':x:': '❌', ':heavy_multiplication_x:': '✖️',
    }
    
    for emoji_code, emoji_char in emoji_map.items():
        cell = cell.replace(emoji_code, emoji_char)
    
    cell = re.sub(r':([a-z_]+):', lambda m: f'<span class="emoji">:{m.group(1)}:</span>', cell)
    cell = cell.replace('\n', '<br>')
    
    return cell

def create_github_style_html(table_data, title=""):
    """Create HTML with GitHub-style table formatting"""
    formatted_headers = [format_markdown_cell(h) for h in table_data['headers']]
    formatted_rows = [[format_markdown_cell(cell) for cell in row] for row in table_data['rows']]
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ background: white; padding: 40px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.5; color: #1f2328; }}
        .markdown-body {{ max-width: 100%; margin: 0 auto; }}
        .markdown-body table {{ border-spacing: 0; border-collapse: collapse; display: block; width: max-content; max-width: 100%; overflow: auto; margin: 20px 0; }}
        .markdown-body table th, .markdown-body table td {{ padding: 6px 13px; border: 1px solid #d0d7de; }}
        .markdown-body table th {{ font-weight: 600; background-color: #f6f8fa; }}
        .markdown-body table tr:nth-child(2n) {{ background-color: #f6f8fa; }}
        .markdown-body table th.text-center, .markdown-body table td.text-center {{ text-align: center; }}
        .markdown-body table th.text-right, .markdown-body table td.text-right {{ text-align: right; }}
        .markdown-body table th.text-left, .markdown-body table td.text-left {{ text-align: left; }}
        h2 {{ font-size: 1.5em; font-weight: 600; margin-top: 24px; margin-bottom: 16px; padding-bottom: 0.3em; border-bottom: 1px solid #d0d7de; }}
        code {{ padding: 0.2em 0.4em; font-size: 85%; background-color: rgba(175, 184, 193, 0.2); border-radius: 6px; font-family: monospace; }}
        strong {{ font-weight: 600; }}
        em {{ font-style: italic; }}
        .table-container {{ overflow-x: auto; margin: 20px 0; }}
        .emoji {{ font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif; }}
    </style>
</head>
<body>
    <div class="markdown-body">
"""
    if title:
        html += f'        <h2>{format_markdown_cell(title)}</h2>\n'
    
    html += '        <div class="table-container">\n'
    html += '          <table>\n'
    html += '            <thead>\n'
    html += '              <tr>\n'
    for i, header in enumerate(formatted_headers):
        align = table_data['alignments'][i] if i < len(table_data['alignments']) else 'left'
        html += f'                <th class="text-{align}">{header}</th>\n'
    html += '              </tr>\n'
    html += '            </thead>\n'
    html += '            <tbody>\n'
    for row in formatted_rows:
        html += '              <tr>\n'
        for i, cell in enumerate(row):
            align = table_data['alignments'][i] if i < len(table_data['alignments']) else 'left'
            html += f'                <td class="text-{align}">{cell}</td>\n'
        html += '              </tr>\n'
    html += '            </tbody>\n'
    html += '          </table>\n'
    html += '        </div>\n'
    html += '    </div>\n'
    html += '</body>\n'
    html += '</html>'
    
    return html

def create_mermaid_html(mermaid_code):
    """Create HTML with mermaid diagram that auto-adjusts height"""
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@11.9.0/dist/mermaid.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            background: white; 
            padding: 20px; 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif; 
            min-height: 100vh;
        }}
        .mermaid-container {{ 
            display: inline-block; 
            width: 100%; 
            min-height: 100%;
        }}
        .mermaid {{ 
            text-align: center; 
            background: white; 
            width: 100%; 
            height: auto;
            display: block;
        }}
        .mermaid svg {{ 
            max-width: 100%; 
            height: auto;
            display: block;
            margin: 0 auto;
        }}
    </style>
</head>
<body>
    <div class="mermaid-container">
        <pre class="mermaid" style="height: auto; min-height: 200px; white-space: pre-wrap;">
{mermaid_code}
        </pre>
    </div>
    <script>
        window.onload = () => {{
            mermaid.initialize({{
                startOnLoad: true,
                theme: 'base',
                themeVariables: {{
                    background: '#ffffff', 
                    primaryColor: '#ffffff', 
                    primaryBorderColor: '#333333',
                    primaryTextColor: '#333333', 
                    lineColor: '#666666', 
                    secondaryColor: '#f6f8fa',
                    tertiaryColor: '#ffffff', 
                    fontSize: '14px',
                    fontFamily: '-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif'
                }},
                flowchart: {{ 
                    useMaxWidth: true, 
                    htmlLabels: true, 
                    curve: 'basis', 
                    padding: 15 
                }},
                sequence: {{ 
                    diagramMarginX: 50, 
                    diagramMarginY: 10, 
                    actorMargin: 50, 
                    width: 150, 
                    height: 65, 
                    useMaxWidth: true 
                }},
                er: {{ useMaxWidth: true }},
                gitGraph: {{ useMaxWidth: true }}
            }});
            
            // Render and signal when complete
            mermaid.contentLoaded();
            
            // Wait for SVG to be fully rendered
            setTimeout(() => {{
                const mermaidElements = document.querySelectorAll('.mermaid');
                mermaidElements.forEach(el => {{
                    const svg = el.querySelector('svg');
                    if (svg) {{
                        const height = svg.getBoundingClientRect().height;
                        const width = svg.getBoundingClientRect().width;
                        if (height > 0) {{
                            el.style.height = height + 'px';
                            el.style.width = width + 'px';
                        }}
                    }}
                }});
                window.mermaidRendered = true;
            }}, 1500);
        }};
    </script>
</body>
</html>"""
    return html

def render_with_playwright(html_content, output_png, width=1400, is_mermaid=False):
    """Render HTML content using Playwright and save as PNG"""
    try:
        from playwright.sync_api import sync_playwright
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(html_content)
            html_file = f.name
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            
            # Create page with appropriate initial size
            if is_mermaid:
                # Start with a large viewport to accommodate tall diagrams
                page = browser.new_page(viewport={'width': width, 'height': 4000})
            else:
                page = browser.new_page(viewport={'width': width, 'height': 800})
            
            page.goto(f'file://{html_file}')
            
            if is_mermaid:
                try:
                    # Wait for mermaid to render
                    page.wait_for_function('window.mermaidRendered === true', timeout=15000)
                except:
                    print(f"      Timeout waiting for mermaid, waiting 3 seconds...")
                    time.sleep(3)
                
                # Wait a bit more for any animations
                time.sleep(1)
                
                # Get the actual content height
                content_height = page.evaluate('''() => {
                    const element = document.querySelector('.mermaid');
                    if (element) {
                        const rect = element.getBoundingClientRect();
                        return rect.height;
                    }
                    return document.body.scrollHeight;
                }''')
                
                # Resize viewport to fit content exactly
                if content_height and content_height > 0:
                    new_height = int(content_height + 80)  # Add padding
                    page.set_viewport_size({'width': width, 'height': new_height})
                    # Wait for resize to take effect
                    time.sleep(0.5)
            else:
                time.sleep(1)
            
            # Get the element to screenshot
            if is_mermaid:
                element = page.query_selector('.mermaid')
                if not element:
                    element = page.query_selector('body')
            else:
                element = page.query_selector('.markdown-body')
            
            if element:
                # Get element bounding box
                box = element.bounding_box()
                if box:
                    # Add padding around the element
                    padding = 30
                    
                    # Calculate clip area
                    clip_x = max(0, box['x'] - padding)
                    clip_y = max(0, box['y'] - padding)
                    clip_width = box['width'] + (padding * 2)
                    clip_height = box['height'] + (padding * 2)
                    
                    # Take screenshot
                    page.screenshot(
                        path=str(output_png),
                        clip={
                            'x': clip_x,
                            'y': clip_y,
                            'width': clip_width,
                            'height': clip_height
                        }
                    )
                else:
                    # Fallback to full page
                    page.screenshot(path=str(output_png), full_page=True)
            else:
                # Fallback to full page
                page.screenshot(path=str(output_png), full_page=True)
            
            browser.close()
        
        # Cleanup
        os.unlink(html_file)
        
        # Verify the PNG was created
        if output_png.exists() and output_png.stat().st_size > 5000:
            return True
        else:
            if output_png.exists():
                print(f"      Generated PNG is too small: {output_png.stat().st_size} bytes")
            return False
            
    except Exception as e:
        print(f"      Playwright error: {e}")
        return False

def generate_png_for_diagram(md_file, include_title_in_image=True):
    """Generate PNG for mermaid diagram"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    mermaid_match = re.search(r'```mermaid\n(.*?)\n```', content, re.DOTALL)
    if not mermaid_match:
        return False
    
    mermaid_code = mermaid_match.group(1)
    output_png = Path(md_file).with_suffix('.png')
    
    html_content = create_mermaid_html(mermaid_code)
    return render_with_playwright(html_content, output_png, width=1400, is_mermaid=True)

def generate_png_for_table(md_file, include_title_in_image=True):
    """Generate PNG for table"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title = extract_bold_or_heading_from_markdown(content)
    if not title:
        lines = content.split('\n')
        if lines and lines[0].startswith('# '):
            title = lines[0][2:].strip()
    
    lines = content.split('\n')
    content_without_title = '\n'.join([l for l in lines if not (l.startswith('# ') or l.startswith('## '))])
    
    table_data = parse_markdown_table(content_without_title.strip())
    if not table_data:
        return False
    
    html_content = create_github_style_html(table_data, title if include_title_in_image else "")
    output_png = Path(md_file).with_suffix('.png')
    return render_with_playwright(html_content, output_png, width=1400, is_mermaid=False)

def check_playwright():
    """Check if Playwright is installed and working"""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
        return True
    except ImportError:
        return False
    except Exception:
        return False

def install_playwright():
    """Install Playwright and browsers"""
    print("Installing Playwright...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'playwright'], check=True)
        print("✓ Playwright installed")
        print("Installing Chromium browser...")
        subprocess.run(['playwright', 'install', 'chromium'], check=True)
        print("✓ Chromium installed")
        print("\n✅ Playwright setup complete!")
        return True
    except Exception as e:
        print(f"❌ Failed to install Playwright: {e}")
        return False

def create_combined_file(original_file, out_dir, folder_name, table_info, diagram_info, with_image_titles=False):
    """Create single combined markdown file with images and enhanced titles"""
    github_base = "https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/blob/main/"
    
    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    table_idx = 0
    diagram_idx = 0
    
    images_dir = out_dir / 'images'
    existing_images = [f.name for f in images_dir.glob("*") if f.is_file()] if images_dir.exists() else []
    
    while i < len(lines):
        line = lines[i]
        
        img_match = re.match(r'!\[(.*?)\]\((.*?)\)', line.strip())
        if img_match and not line.strip().startswith('|') and 'mermaid' not in line:
            alt_text = img_match.group(1)
            img_path = img_match.group(2)
            
            if 'mermaid' in img_path.lower():
                new_lines.append(line)
                i += 1
                continue
            
            img_filename = Path(img_path).name
            found = False
            for existing in existing_images:
                if existing == img_filename or existing == normalize_filename(img_filename):
                    new_lines.append(f"![{alt_text}](images/{existing})")
                    found = True
                    break
            
            if not found:
                original_dir = Path(original_file).parent
                original_images_dir = original_dir / 'images'
                original_file_path = original_images_dir / img_filename
                if original_file_path.exists():
                    safe_name = normalize_filename(img_filename)
                    target_file = images_dir / safe_name
                    if not target_file.exists():
                        shutil.copy2(str(original_file_path), str(target_file))
                    new_lines.append(f"![{alt_text}](images/{safe_name})")
                else:
                    new_lines.append(line)
            i += 1
        
        elif line.strip().startswith('|') and i+1 < len(lines) and '---' in lines[i+1]:
            title = ""
            for j in range(max(0, i-10), i):
                bold_matches = re.findall(r'\*\*(.+?)\*\*|__(.+?)__', lines[j])
                if bold_matches:
                    for match in bold_matches:
                        title = match[0] or match[1]
                        if title and len(title) > 3:
                            break
                    if title:
                        break
            
            if not title:
                for j in range(max(0, i-10), i):
                    if lines[j].startswith('# '):
                        title = lines[j][2:].strip()
                        break
                    elif lines[j].startswith('## '):
                        title = lines[j][3:].strip()
                        break
            
            while i < len(lines) and (lines[i].strip().startswith('|') or '---' in lines[i]):
                i += 1
            
            if table_idx < len(table_info):
                base_name = table_info[table_idx][4]
                img_file = f"images/{base_name}.png"
                md_file = f"{base_name}.md"
                
                if with_image_titles and title:
                    new_lines.append(f"### {title}")
                    new_lines.append("")
                
                new_lines.append(f"![{title if title else 'Table'}]({img_file})")
                new_lines.append("")
                new_lines.append(f"[View Source]({github_base}{folder_name}/{md_file})")
                new_lines.append("")
                table_idx += 1
        
        elif line.strip() == '```mermaid':
            title = ""
            for j in range(max(0, i-10), i):
                bold_matches = re.findall(r'\*\*(.+?)\*\*|__(.+?)__', lines[j])
                if bold_matches:
                    for match in bold_matches:
                        title = match[0] or match[1]
                        if title and len(title) > 3:
                            break
                    if title:
                        break
            
            if not title:
                for j in range(max(0, i-10), i):
                    if lines[j].startswith('# '):
                        title = lines[j][2:].strip()
                        break
                    elif lines[j].startswith('## '):
                        title = lines[j][3:].strip()
                        break
            
            new_lines.append(line)
            i += 1
            while i < len(lines) and lines[i].strip() != '```':
                i += 1
            if i < len(lines):
                new_lines.append(lines[i])
                i += 1
            
            if diagram_idx < len(diagram_info):
                base_name = diagram_info[diagram_idx][3]
                img_file = f"images/{base_name}.png"
                md_file = f"{base_name}.md"
                
                new_lines.append("")
                if with_image_titles and title:
                    new_lines.append(f"### {title}")
                    new_lines.append("")
                
                new_lines.append(f"![{title if title else 'Diagram'}]({img_file})")
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

def main():
    parser = argparse.ArgumentParser(description='Extract tables and diagrams from markdown and generate PNG images.')
    parser.add_argument('input_file', nargs='?', 
                       default="Code to Cluster: Building a Bulletproof Kubernetes Deployment Pipeline on AWS.md",
                       help='Input markdown file')
    parser.add_argument('--with-image-title', action='store_true',
                       help='Include titles above images in the combined markdown file')
    parser.add_argument('--install-playwright', action='store_true',
                       help='Install Playwright for rendering')
    
    args = parser.parse_args()
    
    if args.install_playwright:
        install_playwright()
        return
    
    input_file = args.input_file
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        return
    
    if not check_playwright():
        print("\n❌ Playwright not properly installed. Please run:")
        print("   python3 table_extractor.py --install-playwright")
        return
    
    folder = normalize(Path(input_file).stem, 30)
    out = Path(folder)
    out.mkdir(exist_ok=True)
    
    print(f"Output folder: {out}/")
    print(f"Include image titles: {args.with_image_title}")
    print()
    
    print("Checking for missing images from parent folder...")
    copied_images = copy_missing_images(input_file, out)
    if copied_images > 0:
        print(f"  ✓ Copied {copied_images} missing images")
    else:
        print(f"  No missing images found to copy")
    print()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tables = extract_tables(content)
    diagrams = extract_diagrams(content)
    
    print(f"Found {len(tables)} tables, {len(diagrams)} diagrams")
    print()
    
    table_info = []
    diagram_info = []
    
    print("Saving markdown files...")
    for i, (title, table_content, line) in enumerate(tables, 1):
        base_name = create_filename("table", i, title)
        name = f"{base_name}.md"
        path = out / name
        has_icons = bool(re.search(r'[✓✔⚠️🔄💰☁️🐳🐙⏰⭐🌟🔥🚀🔒🔑]', table_content))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n{table_content}\n")
        table_info.append((title, path, line, has_icons, base_name))
        print(f"  OK Table {i}: {name}")
    
    for i, (title, diagram_content, line) in enumerate(diagrams, 1):
        base_name = create_filename("diagram", i, title)
        name = f"{base_name}.md"
        path = out / name
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n```mermaid\n{diagram_content}\n```\n")
        diagram_info.append((title, path, line, base_name))
        print(f"  OK Diagram {i}: {name}")
    
    print("\nGenerating PNG images with Playwright...")
    images_dir = out / 'images'
    images_dir.mkdir(exist_ok=True)
    
    successful_tables = 0
    for i, (title, path, line, has_icons, base_name) in enumerate(table_info, 1):
        print(f"  Table {i}: {base_name}.png")
        if generate_png_for_table(path, include_title_in_image=args.with_image_title):
            successful_tables += 1
            print(f"    ✓ Success")
        else:
            print(f"    ✗ Failed")
        print()
    
    successful_diagrams = 0
    for i, (title, path, line, base_name) in enumerate(diagram_info, 1):
        print(f"  Diagram {i}: {base_name}.png")
        if generate_png_for_diagram(path, include_title_in_image=args.with_image_title):
            successful_diagrams += 1
            print(f"    ✓ Success")
        else:
            print(f"    ✗ Failed")
        print()
    
    time.sleep(2)
    
    print("\nMoving PNG files to images folder...")
    for png_file in out.glob("*.png"):
        if png_file.exists() and "temp_" not in png_file.name:
            target = images_dir / png_file.name
            shutil.move(str(png_file), str(target))
            print(f"  Moved: {png_file.name}")
    
    png_count = len(list(images_dir.glob("*.png")))
    
    print("\nCreating combined markdown file with enhanced titles...")
    combined = create_combined_file(input_file, out, folder, table_info, diagram_info, args.with_image_title)
    print(f"  OK Created: {combined.name}")
    
    print("Creating README...")
    readme_content = f"""# {folder.replace('-', ' ').title()}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- Tables: {len(tables)} ({successful_tables} successful)
- Diagrams: {len(diagrams)} ({successful_diagrams} successful)
- PNG Images: {png_count}
- Copied Images: {copied_images}

## Combined Document
- [{folder}.md]({folder}.md) - Single file with all images

---
### Rendering Method
- GitHub-style markdown tables with proper formatting (bold, italic, code, emojis)
- Mermaid diagrams rendered with mermaid.js (full height support for tall diagrams)
- Titles extracted from bold text (preferred) or headings
- All content rendered with Playwright (headless Chromium) for high quality
"""
    
    with open(out / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("\n" + "=" * 50)
    print("COMPLETE!")
    print("=" * 50)
    print(f"\nResults:")
    print(f"  ✓ Tables: {successful_tables}/{len(tables)}")
    print(f"  ✓ Diagrams: {successful_diagrams}/{len(diagrams)}")
    print(f"  ✓ PNG images: {png_count}")
    print(f"  ✓ Copied images: {copied_images}")
    print(f"\nOutput directory: {out}/")

if __name__ == "__main__":
    main()