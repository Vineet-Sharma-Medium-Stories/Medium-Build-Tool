#!/usr/bin/env python3
"""
Story Final Processor
Replaces mermaid diagrams and tables in the original story with image blocks
containing links to their respective .md files on GitHub.
"""

import os
import re
import argparse
from datetime import datetime
from pathlib import Path

class StoryFinalProcessor:
    def __init__(self, filename, github_base_url):
        self.filename = filename
        self.github_base_url = github_base_url.rstrip('/')
        self.story_name = self._sanitize_filename(os.path.splitext(os.path.basename(filename))[0])
        # Correct folder structure: story-name/content/
        self.content_dir = f"{self.story_name}/content"
        self.output_filename = f"{self.story_name}_final.md"
        self.log_entries = []
        self.replacements_made = 0
        
    def _sanitize_filename(self, name):
        """Strip filename to fit git commit standards"""
        name = re.sub(r'[\s_]+', '-', name.lower())
        name = re.sub(r'[^a-z0-9-]', '', name)
        name = re.sub(r'-+', '-', name)
        return name.strip('-')
    
    def _log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.log_entries.append(log_entry)
        print(log_entry)
    
    def _extract_mermaid_diagrams(self, content):
        """Extract all mermaid diagrams with their positions and titles"""
        diagrams = []
        pattern = r'```mermaid\n(.*?)```'
        
        for match in re.finditer(pattern, content, re.DOTALL):
            diagram_content = match.group(1).strip()
            
            # Find the title (look for preceding heading or bold text)
            text_before = content[max(0, match.start()-500):match.start()]
            title = "Mermaid Diagram"
            
            # Look for heading
            lines_before = text_before.split('\n')
            for line in reversed(lines_before):
                heading_match = re.match(r'^#{1,6}\s+(.+)', line)
                if heading_match:
                    title = heading_match.group(1).strip()
                    break
            
            if title == "Mermaid Diagram":
                # Look for bold text
                bold_match = re.search(r'\*\*(.+?)\*\*', text_before[-200:])
                if bold_match:
                    title = bold_match.group(1).strip()
            
            diagrams.append({
                'title': title,
                'content': diagram_content,
                'start': match.start(),
                'end': match.end(),
                'match': match.group(0)
            })
        
        return diagrams
    
    def _extract_tables(self, content):
        """Extract all markdown tables with their positions and titles"""
        tables = []
        lines = content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            if '|' in line and i + 1 < len(lines):
                next_line = lines[i + 1]
                if '|' in next_line and '---' in next_line:
                    table_lines = [line, next_line]
                    table_start = i
                    j = i + 2
                    
                    while j < len(lines) and '|' in lines[j] and not lines[j].strip().startswith('```'):
                        table_lines.append(lines[j])
                        j += 1
                    
                    table_content = '\n'.join(table_lines)
                    
                    # Calculate start and end positions
                    start_pos = sum(len(l) + 1 for l in lines[:table_start])
                    end_pos = start_pos + sum(len(l) + 1 for l in table_lines)
                    
                    # Find title
                    title = "Table"
                    for k in range(max(0, i-10), i):
                        heading_match = re.match(r'^#{1,6}\s+(.+)', lines[k])
                        if heading_match:
                            title = heading_match.group(1).strip()
                            break
                        bold_match = re.search(r'\*\*(.+?)\*\*', lines[k])
                        if bold_match:
                            title = bold_match.group(1)
                            break
                    
                    tables.append({
                        'title': title,
                        'content': table_content,
                        'start': start_pos,
                        'end': end_pos,
                        'line_start': table_start,
                        'line_end': j
                    })
                    
                    i = j
                    continue
            i += 1
        
        return tables
    
    def _get_github_link(self, element_type, index, title):
        """Generate GitHub link for the element file - matches your URL structure"""
        safe_title = self._sanitize_filename(title)[:30]
        prefix = 'm' if element_type == 'mermaid' else 't'
        filename = f"{index:02d}-{prefix}-{safe_title}.md"
        # URL format: https://github.com/.../blob/main/story-name/content/filename.md
        return f"{self.github_base_url}/blob/main/{self.content_dir}/{filename}"
    
    def _create_image_block(self, element_type, index, title, github_link):
        """Create the replacement image block with mermaid-01.png for all"""
        type_display = "Mermaid Diagram" if element_type == 'mermaid' else "Table"
        
        return f"""
![{type_display} {index}: {title}](images/mermaid-01.png)
*{type_display} {index}: {title} ([View Source]({github_link}))*

"""
    
    def _add_footer(self, content):
        """Add footer text at the end of the story"""
        footer = """

---
*Questions? Feedback? Comment? leave a response below. If you're implementing something similar and want to discuss architectural tradeoffs, I'm always happy to connect with fellow engineers tackling these challenges.*
"""
        return content + footer
    
    def process(self):
        """Main processing function"""
        self._log(f"Starting to process file: {self.filename}")
        self._log(f"GitHub base URL: {self.github_base_url}")
        self._log(f"Content directory: {self.content_dir}")
        
        # Read input file
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            self._log(f"File not found: {self.filename}", "ERROR")
            return
        except Exception as e:
            self._log(f"Error reading file: {str(e)}", "ERROR")
            return
        
        # Extract elements
        diagrams = self._extract_mermaid_diagrams(content)
        tables = self._extract_tables(content)
        
        self._log(f"Found {len(diagrams)} mermaid diagrams")
        self._log(f"Found {len(tables)} tables")
        
        # Sort all elements by position (descending to avoid index shifting)
        all_elements = []
        
        for i, diag in enumerate(diagrams, 1):
            all_elements.append({
                'type': 'mermaid',
                'index': i,
                'start': diag['start'],
                'end': diag['end'],
                'title': diag['title'],
                'original': diag['match']
            })
        
        for i, table in enumerate(tables, 1):
            all_elements.append({
                'type': 'table',
                'index': i,
                'start': table['start'],
                'end': table['end'],
                'title': table['title'],
                'original': table['content']
            })
        
        # Sort by position in reverse order (so we replace from end to start)
        all_elements.sort(key=lambda x: x['start'], reverse=True)
        
        # Replace elements from end to beginning to maintain positions
        modified_content = content
        for element in all_elements:
            github_link = self._get_github_link(element['type'], element['index'], element['title'])
            image_block = self._create_image_block(element['type'], element['index'], element['title'], github_link)
            
            # Replace the original content with image block
            modified_content = modified_content[:element['start']] + image_block + modified_content[element['end']:]
            self.replacements_made += 1
            self._log(f"Replaced {element['type']} {element['index']}: {element['title']}")
        
        # Add footer
        modified_content = self._add_footer(modified_content)
        self._log("Added footer text")
        
        # Write the final file
        output_path = os.path.join(os.path.dirname(self.filename) or '.', self.output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        self._log(f"Created final file: {output_path}")
        
        # Create log file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"final_process_log_{timestamp}.log"
        log_path = os.path.join(os.path.dirname(self.filename) or '.', log_filename)
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.log_entries))
        
        self._log(f"Created log file: {log_path}")
        
        # Summary
        self._log("=" * 50)
        self._log("PROCESSING COMPLETE")
        self._log(f"Original file: {self.filename}")
        self._log(f"Output file: {self.output_filename}")
        self._log(f"Total replacements made: {self.replacements_made}")
        self._log(f"Mermaid diagrams replaced: {len(diagrams)}")
        self._log(f"Tables replaced: {len(tables)}")
        self._log("=" * 50)

def main():
    parser = argparse.ArgumentParser(description='Replace diagrams and tables with image blocks containing GitHub links')
    parser.add_argument('filename', help='Path to the input markdown file')
    parser.add_argument('--github-url', required=True, 
                       help='GitHub base URL (e.g., https://github.com/Vineet-Sharma-Medium-Stories/Medium-Build-Tool)')
    
    args = parser.parse_args()
    
    processor = StoryFinalProcessor(args.filename, args.github_url)
    processor.process()

if __name__ == "__main__":
    main()