
# Markdown Table & Mermaid Diagram Extractor

A powerful Python tool that extracts tables and mermaid diagrams from markdown files and generates high-quality PNG images using `yyds_md2png`. Perfect for documentation, presentations, and sharing on platforms that don't support native markdown rendering.

## 📋 Features

- **Extract Tables** - Automatically detects and extracts markdown tables with their context
- **Extract Mermaid Diagrams** - Extracts mermaid code blocks and generates diagrams
- **PNG Generation** - Creates high-quality PNG images (1024px wide) with proper formatting
- **Icon Support** - Preserves emoji icons (✅, ❌, ⚠️, 🆓, 💰, etc.) in tables
- **Organized Output** - Creates a structured folder with all extracted content
- **Combined Document** - Generates a single markdown file with images replacing original markup
- **Source Links** - Includes "View Source" links to GitHub for each extracted element
- **Customizable** - Control image titles, themes, and output formatting

## 🚀 Installation

### Prerequisites

1. **Python 3.6+** - Ensure Python is installed
2. **Node.js and npm** - Required for yyds_md2png
3. **yyds_md2png** - The markdown to PNG converter

### Step 1: Install Node.js and npm

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm

# macOS (using Homebrew)
brew install node

# Windows
# Download from https://nodejs.org/
```

### Step 2: Install yyds_md2png

```bash
# Set Chinese mirror for reliable Chromium download (recommended)
export PUPPETEER_DOWNLOAD_BASE_URL=https://cdn.npmmirror.com/binaries/chrome-for-testing

# Install yyds_md2png globally
npm install -g yyds_md2png
```

### Step 3: Verify Installation

```bash
# Check if yyds_md2png is installed
yyds_md2png --version
```

### Step 4: Download the Python Script

Save the script as `extract_tables.py` in your project directory.

## 📖 Usage

### Basic Usage

```bash
# Run with default input file
python3 extract_tables.py

# Run with custom input file
python3 extract_tables.py "my-document.md"

# Run with image titles enabled
python3 extract_tables.py --with-image-title

# Run with custom file and image titles
python3 extract_tables.py "my-document.md" --with-image-title
```

### Command Line Arguments

| Argument | Description |
|----------|-------------|
| `input_file` | Input markdown file (default: "Code to Cluster: Building a Bulletproof Kubernetes Deployment Pipeline on AWS.md") |
| `--with-image-title` | Include titles above images in the combined markdown file |

### Output Structure

```
output-folder-name/
├── README.md                 # Main index with all links
├── output-folder-name.md     # Combined document with images
├── images/                   # All generated PNG images
│   ├── table_01_*.png
│   ├── table_02_*.png
│   ├── diagram_01_*.png
│   └── ...
├── table_01_*.md            # Individual table markdown files
├── table_02_*.md
├── diagram_01_*.md          # Individual diagram markdown files
└── diagram_02_*.md
```

## 🎨 Customization Options

### 1. Table Appearance

The tool uses default GitHub-style tables. To customize table appearance, you can modify the `generate_png` function in the script:

```python
# Add CSS styling for custom table appearance
styled_content = f"""---
css: |
    body {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
        line-height: 1.6;
        padding: 40px;
        max-width: 1200px;
        margin: 0 auto;
        background: white;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        font-size: 14px;
        box-shadow: 0 2px 3px rgba(0,0,0,0.1);
    }}
    th {{
        background-color: #f2f2f2;
        font-weight: 600;
        padding: 12px;
        border: 1px solid #ddd;
    }}
    td {{
        padding: 12px;
        border: 1px solid #ddd;
    }}
    tr:nth-child(even) {{
        background-color: #f9f9f9;
    }}
---
"""
```

### 2. Mermaid Diagram Themes

yyds_md2png supports various mermaid themes. Modify the `generate_png` function:

```python
# Available themes: default, dark, forest, neutral
cmd = [
    'yyds_md2png',
    str(md_file),
    '--mermaid-theme', 'neutral'  # Change theme here
]
```

Common mermaid themes:
- `default` - Light theme (default)
- `dark` - Dark theme
- `forest` - Green-themed
- `neutral` - Neutral colors

### 3. Image Width and Quality

Adjust the image dimensions in the `generate_png` function:

```python
# For wider images (e.g., 1400px)
cmd = [
    'yyds_md2png',
    str(md_file),
    '--width', '1400'  # Change width here
]
```

### 4. Custom Templates

yyds_md2png supports different output templates:

```python
# Available templates: github, medium, etc.
cmd = [
    'yyds_md2png',
    str(md_file),
    '--template', 'github'  # Change template here
]
```

### 5. Icon Detection

The script automatically detects icons in tables. You can customize the icon pattern:

```python
# Modify the regex pattern in the script
has_icons = bool(re.search(r'[✅❌⚠️🆓💰☁️🐳🐙⎈⭐🌟🔥🚀🔒🔑]', content))
# Add or remove icons as needed
```

## 🔧 Troubleshooting

### Issue: No PNG files generated

**Solution:** Check if yyds_md2png is installed correctly:

```bash
which yyds_md2png
yyds_md2png --version
```

### Issue: Images are too small

**Solution:** Increase the width in the generation command:

```python
cmd = ['yyds_md2png', str(md_file), '--width', '1400']
```

### Issue: Icons not displaying in images

**Solution:** Ensure your system has emoji fonts:

```bash
# Ubuntu/Debian
sudo apt install fonts-noto-color-emoji

# macOS
# Emoji fonts are built-in

# Windows
# Segoe UI Emoji is built-in
```

### Issue: Mermaid diagrams not rendering

**Solution:** Update yyds_md2png and check mermaid syntax:

```bash
npm update -g yyds_md2png
```

### Issue: Filename too long errors

**Solution:** The script automatically truncates long filenames and adds a hash. No action needed.

### Issue: "_default" files are not being renamed

**Solution:** The script automatically renames all `_default_*.png` files to the correct names. If this fails, you can manually rename them:

```bash
# Manual rename example
mv table_01_*_default_*.png images/table_01_correct-name.png
```

## 📝 Examples

### Example 1: Basic Extraction

```bash
python3 extract_tables.py my-document.md
```

Output:
```
Output folder: my-document/
Found 5 tables, 2 diagrams

Saving markdown files...
  OK Table 1: table_01_ci-cd-options.md
  OK Table 2: table_02_registry-options.md
  OK Diagram 1: diagram_01_architecture.md

Generating PNG images...
  Generating table_01_ci-cd-options.png...
    Generation completed
  Generating diagram_01_architecture.png...
    Generation completed

COMPLETE!
```

### Example 2: With Image Titles

```bash
python3 extract_tables.py --with-image-title
```

This will include `### Table Title` above each image in the combined document.

### Example 3: Custom GitHub Repository Links

The script includes "View Source" links pointing to:
```
https://github.com/Vineet-Sharma-Medium-Stories/Medium-Assets/{folder}/{filename}
```

You can modify the `github_base` variable in the script to point to your own repository:

```python
github_base = "https://github.com/your-username/your-repo/"
```

## ⚙️ Advanced Configuration

### Modifying Image Quality

Edit the `generate_png` function to adjust quality:

```python
cmd = [
    'yyds_md2png',
    str(md_file),
    '--quality', '100',  # 0-100, default is usually 80
    '--width', '1200'
]
```

### Changing Output Directory Structure

Modify the `folder` variable to change the output folder name:

```python
folder = "my-custom-output-folder"  # Instead of auto-generated name
```

### Adding Custom CSS for All Images

Add global styling in the `generate_png` function:

```python
def generate_png(md_file, include_title_in_image=True):
    # Add custom CSS wrapper
    with open(md_file, 'r') as f:
        content = f.read()
    
    wrapped_content = f"""---
css: |
    body {{ font-family: 'Courier New', monospace; }}
    table {{ border: 2px solid red; }}
---
{content}
"""
    # Write to temp file and process...
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests! Areas for improvement:
- Additional output formats (SVG, PDF)
- More customization options
- Support for other diagram types
- Batch processing multiple files

## 📄 License

MIT License - feel free to use and modify for your needs.

## 🙏 Acknowledgments

- [yyds_md2png](https://www.npmjs.com/package/yyds_md2png) - Excellent markdown to PNG converter
- All contributors and users of this tool

## 📬 Contact

For questions, suggestions, or feedback:
- GitHub Issues: [Create an issue](https://github.com/your-repo/issues)
- Email: your-email@example.com

https://bulkresizephotos.com/en
---

**Happy Documenting!** 🚀

*If you find this tool useful, please give it a star on GitHub!* ⭐
```