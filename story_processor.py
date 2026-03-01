#!/usr/bin/env python3
"""
Story File Processor
Processes a markdown file to extract headers, mermaid diagrams, and tables
into separate files with a consistent structure.
"""

import os
import re
import argparse
from datetime import datetime
from pathlib import Path

class StoryProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.story_name = self._sanitize_filename(os.path.splitext(os.path.basename(filename))[0])
        self.base_output_dir = f"{self.story_name}"
        self.content_dir = os.path.join(self.base_output_dir, "content")
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_entries = []
        
        # Statistics
        self.total_words = 0
        self.mermaid_count = 0
        self.table_count = 0
        
    def _sanitize_filename(self, name):
        """Strip filename to fit git commit standards (lowercase, hyphens, no special chars)"""
        name = re.sub(r'[\s_]+', '-', name.lower())
        name = re.sub(r'[^a-z0-9-]', '', name)
        name = re.sub(r'-+', '-', name)
        return name.strip('-')
    
    def _log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.log_entries.append(log_entry)
        print(log_entry)
    
    def _count_words(self, text):
        return len(re.findall(r'\b\w+\b', text))
    
    def _extract_title_from_content(self, content, start_pos, end_pos):
        lines_before = content[max(0, start_pos-500):start_pos].split('\n')
        for line in reversed(lines_before):
            if re.match(r'^#{1,6}\s+(.+)', line):
                return re.sub(r'^#{1,6}\s+', '', line).strip()
        bold_match = re.search(r'\*\*(.+?)\*\*', content[max(0, start_pos-200):start_pos])
        if bold_match:
            return bold_match.group(1)
        return "Untitled"
    
    def _extract_mermaid_diagrams(self, content):
        diagrams = []
        lines = content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip() == '```mermaid' or line.strip().startswith('```mermaid'):
                diagram_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    diagram_lines.append(lines[i])
                    i += 1
                diagram_content = '\n'.join(diagram_lines).strip()
                if diagram_content:
                    position = sum(len(l) for l in lines[:i])
                    title = "Mermaid Diagram"
                    for j in range(max(0, i-10), i):
                        if re.match(r'^#{1,6}\s+(.+)', lines[j]):
                            title = re.sub(r'^#{1,6}\s+', '', lines[j]).strip()
                            break
                        elif '**' in lines[j]:
                            bold_match = re.search(r'\*\*(.+?)\*\*', lines[j])
                            if bold_match:
                                title = bold_match.group(1)
                                break
                    self.mermaid_count += 1
                    diagrams.append({
                        'title': title,
                        'content': diagram_content,
                        'position': position
                    })
            i += 1
        return diagrams
    
    def _extract_tables(self, content):
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
                    position = sum(len(l) for l in lines[:table_start])
                    title = "Table"
                    for k in range(max(0, table_start-10), table_start):
                        if re.match(r'^#{1,6}\s+(.+)', lines[k]):
                            title = re.sub(r'^#{1,6}\s+', '', lines[k]).strip()
                            break
                        elif '**' in lines[k]:
                            bold_match = re.search(r'\*\*(.+?)\*\*', lines[k])
                            if bold_match:
                                title = bold_match.group(1)
                                break
                    self.table_count += 1
                    tables.append({
                        'title': title,
                        'content': table_content,
                        'position': position
                    })
                    i = j
                    continue
            i += 1
        return tables
    
    def _extract_header_content(self, content):
        lines = content.split('\n')
        title = self.story_name.replace('-', ' ').title()
        for line in lines[:20]:
            if line.startswith('# '):
                title = line[2:].strip()
                break
        header_content = f"""# {title}

## Document Information
- **File Name:** {os.path.basename(self.filename)}
- **Total Words:** {self.total_words}
- **Estimated Reading Time:** {max(1, self.total_words // 200)} minutes

---"""
        return header_content
    
    def _extract_footer_content(self):
        return f"""
---
*This story was automatically generated from {os.path.basename(self.filename)} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.*"""
    
    def _create_merged_content(self, header_content, diagrams, tables, footer_content):
        merged = [header_content]
        all_elements = []
        
        for i, diag in enumerate(diagrams):
            all_elements.append({
                'type': 'mermaid',
                'position': diag['position'],
                'content': '\n\n## Mermaid Diagram ' + str(i+1) + ': ' + diag['title'] + '\n\n```mermaid\n' + diag['content'] + '\n```\n'
            })
        
        for i, table in enumerate(tables):
            all_elements.append({
                'type': 'table',
                'position': table['position'],
                'content': '\n\n## Table ' + str(i+1) + ': ' + table['title'] + '\n\n' + table['content'] + '\n'
            })
        
        all_elements.sort(key=lambda x: x['position'])
        
        for element in all_elements:
            merged.append(element['content'])
        
        merged.append(footer_content)
        return '\n'.join(merged)
    
    def process(self):
        self._log(f"Starting to process file: {self.filename}")
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            self._log(f"File not found: {self.filename}", "ERROR")
            return
        except Exception as e:
            self._log(f"Error reading file: {str(e)}", "ERROR")
            return
        
        self.total_words = self._count_words(content)
        self._log(f"Total words in document: {self.total_words}")
        
        # Create base story folder
        Path(self.base_output_dir).mkdir(parents=True, exist_ok=True)
        self._log(f"Created story folder: {self.base_output_dir}")
        
        # Create content subfolder
        Path(self.content_dir).mkdir(parents=True, exist_ok=True)
        self._log(f"Created content subfolder: {self.content_dir}")
        
        diagrams = self._extract_mermaid_diagrams(content)
        tables = self._extract_tables(content)
        
        self._log(f"Found {len(diagrams)} mermaid diagrams")
        self._log(f"Found {len(tables)} tables")
        
        header_content = self._extract_header_content(content)
        
        # Write header.md to content folder
        header_path = os.path.join(self.content_dir, "header.md")
        with open(header_path, 'w', encoding='utf-8') as f:
            f.write(header_content)
        self._log(f"Created content/header.md")
        
        # Write individual diagram files to content folder
        for i, diagram in enumerate(diagrams, 1):
            safe_title = self._sanitize_filename(diagram['title'])
            filename = f"{i:02d}-m-{safe_title[:30]}.md"
            file_path = os.path.join(self.content_dir, filename)
            diagram_content = f"# Mermaid Diagram {i}: {diagram['title']}\n\n```mermaid\n{diagram['content']}\n```\n"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(diagram_content)
            self._log(f"Created content/{filename}")
        
        # Write individual table files to content folder
        for i, table in enumerate(tables, 1):
            safe_title = self._sanitize_filename(table['title'])
            filename = f"{i:02d}-t-{safe_title[:30]}.md"
            file_path = os.path.join(self.content_dir, filename)
            table_content = f"# Table {i}: {table['title']}\n\n{table['content']}\n"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(table_content)
            self._log(f"Created content/{filename}")
        
        # Create footer in content folder
        footer_content = self._extract_footer_content()
        footer_path = os.path.join(self.content_dir, "footer.md")
        with open(footer_path, 'w', encoding='utf-8') as f:
            f.write(footer_content)
        self._log(f"Created content/footer.md")
        
        # Create merged story file in base folder
        merged_content = self._create_merged_content(header_content, diagrams, tables, footer_content)
        story_filename = f"{self.story_name}.md"
        story_path = os.path.join(self.base_output_dir, story_filename)
        with open(story_path, 'w', encoding='utf-8') as f:
            f.write(merged_content)
        self._log(f"Created merged story file: {story_filename}")
        
        # Create log file in base folder
        log_filename = f"process_log_{self.timestamp}.log"
        log_path = os.path.join(self.base_output_dir, log_filename)
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.log_entries))
        self._log(f"Created log file: {log_filename}")
        
        self._log("=" * 50)
        self._log("PROCESSING COMPLETE")
        self._log(f"Story name: {self.story_name}")
        self._log(f"Base folder: {self.base_output_dir}")
        self._log(f"Content folder: {self.content_dir}")
        self._log(f"Total words: {self.total_words}")
        self._log(f"Mermaid diagrams extracted: {len(diagrams)}")
        self._log(f"Tables extracted: {len(tables)}")
        self._log("=" * 50)

def main():
    parser = argparse.ArgumentParser(description='Process a markdown story file')
    parser.add_argument('filename', help='Path to the input markdown file')
    args = parser.parse_args()
    processor = StoryProcessor(args.filename)
    processor.process()

if __name__ == "__main__":
    main()