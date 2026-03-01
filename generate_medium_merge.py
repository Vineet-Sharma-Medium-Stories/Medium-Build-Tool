import re
import os
import sys

def strict_slug(text, max_len=30):
    # Standardized truncation logic 
    name_only = os.path.splitext(os.path.basename(text))[0]
    slug = re.sub(r'[^\w\s-]', '', name_only).strip().lower()
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug[:max_len].strip('-')

def generate_medium(original_file, user="sharma-vineet", repo="medium-stories"):
    if not os.path.exists(original_file):
        print(f"❌ Error: {original_file} not found at root.")
        return

    story_folder = strict_slug(original_file)
    content_dir = os.path.join(story_folder, 'content')
    github_base = f"https://github.com/{user}/{repo}/blob/main/{story_folder}/content"

    if not os.path.exists(content_dir):
        print(f"❌ Error: Content folder '{content_dir}' not found. Run Script 1 first.")
        return

    with open(original_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # --- 1. Replace Mermaid with Placeholder and GitHub Link ---
    # Matches Mermaid blocks 
    text = re.sub(r'```mermaid\n.*?\n```', 
                  f"\n\n> [IMAGE_PLACEHOLDER: Mermaid Diagram]\n> *Source: [View Diagram Code]({github_base})*\n\n", 
                  text, flags=re.DOTALL)
    
    # --- 2. Replace Tables with Content from .md Files ---
    # This logic identifies tables and swaps them for the extracted .md files 
    table_pattern = r'((?:\|.*\|(?:\n|$))+(?:\|[:\s-]*\|(?:\n|$))(?:\|.*\|(?:\n|$))*)'
    table_files = sorted([f for f in os.listdir(content_dir) if 'table' in f or 'tbl' in f])
    
    def table_replacer(match):
        if table_files:
            target_file = table_files.pop(0)
            file_path = os.path.join(content_dir, target_file)
            with open(file_path, 'r', encoding='utf-8') as tf:
                table_content = tf.read()
            # Return the content of the .md file + the absolute link for Medium users 
            return f"\n\n{table_content}\n\n*Source: [View Original Table]({github_base}/{target_file})*\n\n"
        return match.group(0)

    text = re.sub(table_pattern, table_replacer, text)

    # --- 3. Save Final Merge (No Header/Footer) ---
    output_path = os.path.join(story_folder, f"{story_folder}_merge.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✅ Success: Generated {output_path} with injected .md tables.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_medium_merge.py \"Story Name.md\"")
    else:
        generate_medium(sys.argv[1])