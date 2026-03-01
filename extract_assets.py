import re
import os
import sys

def strict_slug(text, max_len=30):
    # Strip extension, remove non-alphanumeric, replace spaces with hyphens
    name_only = os.path.splitext(os.path.basename(text))[0]
    slug = re.sub(r'[^\w\s-]', '', name_only).strip().lower()
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug[:max_len].strip('-')

def get_reading_time(text):
    words = len(text.split())
    minutes = max(1, round(words / 200))
    return words, minutes

def extract_assets(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found.")
        return

    # Generate the 30-char folder name
    story_folder = strict_slug(file_path)
    content_dir = os.path.join(story_folder, 'content')
    os.makedirs(content_dir, exist_ok=True)

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Create Header/Footer (Stats for the LINQ/AI stories)
    words, mins = get_reading_time(text)
    header_path = os.path.join(story_folder, 'header.md')
    if not os.path.exists(header_path):
        with open(header_path, 'w', encoding='utf-8') as h:
            h.write(f"# {os.path.splitext(os.path.basename(file_path))[0]}\n")
            h.write(f"**Stats:** {words} words | Estimated Reading Time: {mins} min\n")

    footer_path = os.path.join(story_folder, 'footer.md')
    if not os.path.exists(footer_path):
        with open(footer_path, 'w', encoding='utf-8') as f_file:
            f_file.write("\n---\n\nQuestions? Feedback? Comment? Leave a response below. If you’re implementing something similar and want to discuss architectural tradeoffs, I’m always happy to connect with fellow engineers tackling these challenges.")

    # Extract Mermaid and Tables (e.g., Prompt Engineering pillars)
    mermaid = re.findall(r'(?:\*\*(.*?)\*\*\n)?\s*```mermaid\n(.*?)\n```', text, re.DOTALL)
    for i, (title, block) in enumerate(mermaid, 1):
        name = strict_slug(title if title else f"diag-{i}")
        with open(os.path.join(content_dir, f'{i:02d}-{name}.md'), 'w', encoding='utf-8') as f:
            f.write(f"```mermaid\n{block.strip()}\n```")

    table_pattern = r'(?:\*\*(.*?)\*\*\n)?\s*((?:\|.*\|(?:\n|$))+)'
    tables = [m for m in re.finditer(table_pattern, text) if re.search(r'\|[:\s-]*\|', m.group(2))]
    for j, match in enumerate(tables, i + 1):
        title, table = match.group(1), match.group(2).strip()
        name = strict_slug(title if title else f"tbl-{j}")
        with open(os.path.join(content_dir, f'{j:02d}-{name}.md'), 'w', encoding='utf-8') as f:
            f.write(f"{table}\n\n**{title if title else ''}**")

    print(f"✅ Success. Folder created: {story_folder}")

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: python extract_assets.py \"Story Name.md\"")
    else: extract_assets(sys.argv[1])