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

def extract_bold_or_heading_from_markdown(content):
    """Extract title from markdown content: first bold, then heading"""
    lines = content.split('\n')
    
    # First, look for bold text in the lines before the table/diagram
    for line in lines[:5]:  # Check first 5 lines
        # Look for bold patterns: **text** or __text__
        bold_matches = re.findall(r'\*\*(.+?)\*\*|__(.+?)__', line)
        if bold_matches:
            # Take the first bold text found
            for match in bold_matches:
                title = match[0] or match[1]  # Get the captured group that matched
                if title and len(title) > 3:  # Ensure it's not too short
                    return title.strip()
    
    # If no bold found, look for heading (starts with #)
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
    
    # Parse headers
    header_line = lines[0]
    headers = [h.strip() for h in header_line.split('|') if h.strip()]
    
    # Parse alignment from separator line
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
    
    # Parse data rows
    rows = []
    for line in lines[2:]:
        if line.strip():
            cells = [c.strip() for c in line.split('|')]
            # Remove empty first/last cells from leading/trailing pipes
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
    
    # First, escape HTML special characters
    cell = cell.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Handle code blocks first (to avoid interference)
    cell = re.sub(r'`([^`]+)`', r'<code>\1</code>', cell)
    
    # Handle bold and italic combinations (must be in order)
    # Bold italic
    cell = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', cell)
    cell = re.sub(r'___(.+?)___', r'<strong><em>\1</em></strong>', cell)
    
    # Bold
    cell = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell)
    cell = re.sub(r'__(.+?)__', r'<strong>\1</strong>', cell)
    
    # Italic
    cell = re.sub(r'\*(.+?)\*', r'<em>\1</em>', cell)
    cell = re.sub(r'_(.+?)_', r'<em>\1</em>', cell)
    
    # Handle emojis (GitHub emoji format :emoji:)
    emoji_map = {
        ':white_check_mark:': '✅',
        ':heavy_check_mark:': '✔️',
        ':warning:': '⚠️',
        ':arrows_counterclockwise:': '🔄',
        ':moneybag:': '💰',
        ':cloud:': '☁️',
        ':whale:': '🐳',
        ':octopus:': '🐙',
        ':alarm_clock:': '⏰',
        ':star:': '⭐',
        ':star2:': '🌟',
        ':fire:': '🔥',
        ':rocket:': '🚀',
        ':key:': '🔒',
        ':closed_lock_with_key:': '🔑',
        ':checkered_flag:': '🏁',
        ':gear:': '⚙️',
        ':book:': '📚',
        ':zap:': '⚡',
        ':package:': '📦',
        ':hammer:': '🔨',
        ':wrench:': '🔧',
        ':bulb:': '💡',
        ':chart_with_upwards_trend:': '📈',
        ':chart_with_downwards_trend:': '📉',
        ':sparkles:': '✨',
        ':tada:': '🎉',
        ':x:': '❌',
        ':heavy_multiplication_x:': '✖️',
    }
    
    for emoji_code, emoji_char in emoji_map.items():
        cell = cell.replace(emoji_code, emoji_char)
    
    # Handle any remaining emoji codes (fallback)
    cell = re.sub(r':([a-z_]+):', lambda m: f'<span class="emoji">:{m.group(1)}:</span>', cell)
    
    # Handle line breaks
    cell = cell.replace('\n', '<br>')
    
    return cell

def create_github_style_html(table_data, title=""):
    """Create HTML with GitHub-style table formatting including markdown formatting"""
    
    # Process headers with formatting
    formatted_headers = []
    for header in table_data['headers']:
        formatted_headers.append(format_markdown_cell(header))
    
    # Process rows with formatting
    formatted_rows = []
    for row in table_data['rows']:
        formatted_row = []
        for cell in row:
            formatted_row.append(format_markdown_cell(cell))
        formatted_rows.append(formatted_row)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            background: white;
            padding: 40px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            font-size: 14px;
            line-height: 1.5;
            color: #1f2328;
        }}
        
        .markdown-body {{
            max-width: 100%;
            margin: 0 auto;
        }}
        
        /* GitHub markdown table styling */
        .markdown-body table {{
            border-spacing: 0;
            border-collapse: collapse;
            display: block;
            width: max-content;
            max-width: 100%;
            overflow: auto;
            margin: 20px 0;
            font-size: 14px;
            line-height: 1.5;
        }}
        
        .markdown-body table th,
        .markdown-body table td {{
            padding: 6px 13px;
            border: 1px solid #d0d7de;
        }}
        
        .markdown-body table th {{
            font-weight: 600;
            background-color: #f6f8fa;
        }}
        
        .markdown-body table tr:nth-child(2n) {{
            background-color: #f6f8fa;
        }}
        
        /* Alignment classes */
        .markdown-body table th.text-center,
        .markdown-body table td.text-center {{
            text-align: center;
        }}
        
        .markdown-body table th.text-right,
        .markdown-body table td.text-right {{
            text-align: right;
        }}
        
        .markdown-body table th.text-left,
        .markdown-body table td.text-left {{
            text-align: left;
        }}
        
        /* Title styling */
        h2 {{
            font-size: 1.5em;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            padding-bottom: 0.3em;
            border-bottom: 1px solid #d0d7de;
            color: #1f2328;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
        }}
        
        /* Code styling for inline code */
        code {{
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(175, 184, 193, 0.2);
            border-radius: 6px;
            font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', monospace;
        }}
        
        /* Strong/Bold styling */
        strong {{
            font-weight: 600;
            color: #1f2328;
        }}
        
        /* Emphasis/Italic styling */
        em {{
            font-style: italic;
        }}
        
        /* Table container for scrolling */
        .table-container {{
            overflow-x: auto;
            margin: 20px 0;
        }}
        
        /* Ensure proper rendering of emojis */
        .emoji {{
            font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif;
        }}
        
        /* Better table cell text wrapping */
        .markdown-body table td,
        .markdown-body table th {{
            white-space: normal;
            word-wrap: break-word;
            max-width: 600px;
        }}
    </style>
</head>
<body>
    <div class="markdown-body">
"""
    
    # Add title if provided
    if title:
        html += f'        <h2>{format_markdown_cell(title)}</h2>\n'
    
    # Create table
    html += '        <div class="table-container">\n'
    html += '          <table>\n'
    
    # Header
    html += '          <thead>\n'
    html += '              <tr>\n'
    for i, header in enumerate(formatted_headers):
        align = table_data['alignments'][i] if i < len(table_data['alignments']) else 'left'
        html += f'              <th class="text-{align}">{header}</th>\n'
    html += '              </tr>\n'
    html += '          </thead>\n'
    
    # Body
    html += '          <tbody>\n'
    for row in formatted_rows:
        html += '              <tr>\n'
        for i, cell in enumerate(row):
            align = table_data['alignments'][i] if i < len(table_data['alignments']) else 'left'
            html += f'              <td class="text-{align}">{cell}</td>\n'
        html += '              </tr>\n'
    html += '          </tbody>\n'
    
    html += '          </table>\n'
    html += '        </div>\n'
    html += '    </div>\n'
    html += '</body>\n'
    html += '</html>'
    
    return html

def create_mermaid_html(mermaid_code):
    """Create HTML with mermaid diagram"""
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@11.9.0/dist/mermaid.min.js"></script>
    <style>
        body {{ 
            margin: 0; 
            padding: 40px; 
            background: white;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
        }}
        .mermaid {{ 
            text-align: center;
            background: white;
        }}
    </style>
</head>
<body>
    <pre class="mermaid">
{mermaid_code}
    </pre>
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
                    curve: 'basis'
                }},
                sequence: {{
                    diagramMarginX: 50,
                    diagramMarginY: 10,
                    actorMargin: 50,
                    width: 150,
                    height: 65,
                    boxMargin: 10,
                    boxTextMargin: 5,
                    noteMargin: 10,
                    messageMargin: 35,
                    mirrorActors: true,
                    useMaxWidth: true
                }},
                er: {{
                    useMaxWidth: true
                }},
                gitGraph: {{
                    useMaxWidth: true
                }}
            }});
            mermaid.contentLoaded();
        }};
        
        setTimeout(() => {{
            window.mermaidRendered = true;
        }}, 2000);
    </script>
</body>
</html>"""
    return html

def render_with_playwright(html_content, output_png, width=1400):
    """Render HTML content using Playwright and save as PNG"""
    try:
        from playwright.sync_api import sync_playwright
        
        # Create temp HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(html_content)
            html_file = f.name
        
        # Use Playwright to render
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=True)
            
            # Create page
            page = browser.new_page(viewport={'width': width, 'height': 800})
            
            # Load the HTML file
            page.goto(f'file://{html_file}')
            
            # Wait for content to load
            if 'mermaid' in html_content:
                try:
                    page.wait_for_function('window.mermaidRendered === true', timeout=10000)
                except:
                    time.sleep(2)
            else:
                time.sleep(1)
            
            # Get the content element
            if 'mermaid' in html_content:
                element = page.query_selector('.mermaid')
            else:
                element = page.query_selector('.markdown-body')
            
            if element:
                # Get element bounding box
                box = element.bounding_box()
                if box:
                    # Take screenshot of the element with padding
                    page.screenshot(
                        path=str(output_png),
                        clip={
                            'x': max(0, box['x'] - 20),
                            'y': max(0, box['y'] - 20),
                            'width': min(box['width'] + 40, width),
                            'height': box['height'] + 40
                        }
                    )
                else:
                    element.screenshot(path=str(output_png))
            else:
                # Fallback: screenshot the whole page
                page.screenshot(path=str(output_png), full_page=True)
            
            browser.close()
        
        # Cleanup
        os.unlink(html_file)
        
        if output_png.exists() and output_png.stat().st_size > 5000:
            return True
        else:
            if output_png.exists():
                print(f"      Playwright produced small PNG ({output_png.stat().st_size} bytes)")
            return False
            
    except ImportError:
        print(f"      Playwright not installed. Run: pip install playwright && playwright install chromium")
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
    return render_with_playwright(html_content, output_png, width=1400)

def generate_png_for_table(md_file, include_title_in_image=True):
    """Generate PNG for table with GitHub-style formatting including markdown"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title using bold first, then heading
    title = extract_bold_or_heading_from_markdown(content)
    if not title:
        # Fallback to the first line if it's a heading
        lines = content.split('\n')
        if lines and lines[0].startswith('# '):
            title = lines[0][2:].strip()
    
    # Remove the title line from content if it exists
    lines = content.split('\n')
    content_without_title = '\n'.join([l for l in lines if not (l.startswith('# ') or l.startswith('## '))])
    
    # Parse markdown table
    table_data = parse_markdown_table(content_without_title.strip())
    if not table_data:
        return False
    
    # Create HTML with GitHub styling and markdown formatting
    html_content = create_github_style_html(table_data, title if include_title_in_image else "")
    
    output_png = Path(md_file).with_suffix('.png')
    return render_with_playwright(html_content, output_png, width=1400)

def check_playwright():
    """Check if Playwright is installed and working"""
    try:
        import playwright
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"⚠️  Playwright error: {e}")
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
    
    # Check Playwright
    if not check_playwright():
        print("\n❌ Playwright not properly installed. Please run:")
        print("   python3 table_extractor.py --install-playwright")
        print("\nPlaywright is required for rendering both tables and diagrams.")
        return
    
    folder = normalize(Path(input_file).stem, 30)
    out = Path(folder)
    out.mkdir(exist_ok=True)
    
    print(f"Output folder: {out}/")
    print(f"Include image titles: {args.with_image_title}")
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
    
    # Generate PNG for tables
    successful_tables = 0
    for i, (title, path, line, has_icons, base_name) in enumerate(table_info, 1):
        print(f"  Table {i}: {base_name}.png")
        if generate_png_for_table(path, include_title_in_image=args.with_image_title):
            successful_tables += 1
            print(f"    ✓ Success")
        else:
            print(f"    ✗ Failed")
        print()
    
    # Generate PNG for diagrams
    successful_diagrams = 0
    for i, (title, path, line, base_name) in enumerate(diagram_info, 1):
        print(f"  Diagram {i}: {base_name}.png")
        if generate_png_for_diagram(path, include_title_in_image=args.with_image_title):
            successful_diagrams += 1
            print(f"    ✓ Success")
        else:
            print(f"    ✗ Failed")
        print()
    
    # Wait and move files
    time.sleep(2)
    
    print("\nMoving PNG files to images folder...")
    for png_file in out.glob("*.png"):
        if png_file.exists() and "temp_" not in png_file.name:
            target = images_dir / png_file.name
            shutil.move(str(png_file), str(target))
            print(f"  Moved: {png_file.name}")
    
    png_count = len(list(images_dir.glob("*.png")))
    
    # Create combined file with enhanced title extraction
    print("\nCreating combined markdown file with enhanced titles...")
    combined = create_combined_file(input_file, out, folder, table_info, diagram_info, args.with_image_title)
    print(f"  OK Created: {combined.name}")
    
    # Create README
    print("Creating README...")
    readme_content = f"""# {folder.replace('-', ' ').title()}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- Tables: {len(tables)} ({successful_tables} successful)
- Diagrams: {len(diagrams)} ({successful_diagrams} successful)
- PNG Images: {png_count}

## Combined Document
- [{folder}.md]({folder}.md) - Single file with all images

---
### Rendering Method
- GitHub-style markdown tables with proper formatting (bold, italic, code, emojis)
- Mermaid diagrams rendered with mermaid.js
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
    print(f"\nOutput directory: {out}/")

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
    
    while i < len(lines):
        line = lines[i]
        
        if line.strip().startswith('|') and i+1 < len(lines) and '---' in lines[i+1]:
            # Extract title from the original content (bold first, then heading)
            title = ""
            # Look for bold text in the lines before the table
            for j in range(max(0, i-10), i):
                bold_matches = re.findall(r'\*\*(.+?)\*\*|__(.+?)__', lines[j])
                if bold_matches:
                    for match in bold_matches:
                        title = match[0] or match[1]
                        if title and len(title) > 3:
                            break
                    if title:
                        break
            
            # If no bold found, look for heading
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
                
                # Add the extracted title before the image
                if with_image_titles and title:
                    new_lines.append(f"### {title}")
                    new_lines.append("")
                
                new_lines.append(f"![{title if title else 'Table'}]({img_file})")
                new_lines.append("")
                new_lines.append(f"[View Source]({github_base}{folder_name}/{md_file})")
                new_lines.append("")
                table_idx += 1
        
        elif line.strip() == '```mermaid':
            # Extract title for diagram
            title = ""
            # Look for bold text in the lines before the diagram
            for j in range(max(0, i-10), i):
                bold_matches = re.findall(r'\*\*(.+?)\*\*|__(.+?)__', lines[j])
                if bold_matches:
                    for match in bold_matches:
                        title = match[0] or match[1]
                        if title and len(title) > 3:
                            break
                    if title:
                        break
            
            # If no bold found, look for heading
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
                # Add the extracted title before the image
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

if __name__ == "__main__":
    main()