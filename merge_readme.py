import os
import sys
import re

def strict_slug(text, max_len=30):
    # Identical truncation logic to Script 1
    name_only = os.path.splitext(os.path.basename(text))[0]
    slug = re.sub(r'[^\w\s-]', '', name_only).strip().lower()
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug[:max_len].strip('-')

def merge_readme(original_filename):
    # 1. Calculate the truncated folder path
    story_folder = strict_slug(original_filename)
    content_dir = os.path.join(story_folder, 'content')
    output_file = os.path.join(story_folder, 'README.md')
    
    if not os.path.exists(story_folder):
        print(f"❌ Error: Folder '{story_folder}' not found. Run Script 1 first.")
        return

    # 2. Read Header and Footer
    header = ""
    footer = ""
    h_path = os.path.join(story_folder, 'header.md')
    f_path = os.path.join(story_folder, 'footer.md')

    if os.path.exists(h_path):
        with open(h_path, 'r', encoding='utf-8') as h:
            header = h.read()
    
    if os.path.exists(f_path):
        with open(f_path, 'r', encoding='utf-8') as f:
            footer = f.read()

    # 3. Collect and Sort Content Assets
    assets_text = ""
    if os.path.exists(content_dir):
        files = sorted([f for f in os.listdir(content_dir) if f.endswith('.md')])
        for filename in files:
            with open(os.path.join(content_dir, filename), 'r', encoding='utf-8') as f:
                assets_text += f"### Asset: {filename}\n{f.read()}\n\n"

    # 4. Final Merge (Header + Assets + Footer)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{header}\n\n---\n\n{assets_text}\n\n---\n\n{footer}")
    
    print(f"✅ Successfully merged Header, Assets, and Footer into {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge_readme.py \"Story Name.md\"")
    else:
        merge_readme(sys.argv[1])