#!/usr/bin/env python3
"""
Story Final Processor
Replaces mermaid diagrams and tables in the original story with image blocks
containing links to their respective .md files on GitHub.
Optimized for Medium's editor paste behavior.
"""

import os
import re
import argparse
from datetime import datetime
from pathlib import Path
import story_utils as utils

class StoryFinalProcessor:
    def __init__(self, filename, github_base_url):
        self.filename = filename
        self.github_base_url = github_base_url.rstrip('/')
        self.story_name = utils.sanitize_filename(os.path.splitext(os.path.basename(filename))[0])
        # Correct folder structure: story-name/content/
        self.content_dir = f"{self.story_name}/content"
        self.output_filename = f"{self.story_name}_final.md"
        self.log_entries = []
        self.replacements_made = 0
        
        # Counters
        self.mermaid_count = 0
        self.table_count = 0
        
    def _log(self, message, level="INFO"):
        log_entry = utils.format_log_entry(message, level)
        self.log_entries.append(log_entry)
        print(log_entry)
    
    def _extract_mermaid_diagrams(self, content):
        """Extract all mermaid diagrams with their positions and titles"""
        diagrams = []
        lines = content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip() == '```mermaid' or line.strip().startswith('```mermaid'):
                diagram_lines = []
                start_line = i
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    diagram_lines.append(lines[i])
                    i += 1
                diagram_content = '\n'.join(diagram_lines).strip()
                if diagram_content:
                    # Calculate position
                    position = utils.calculate_position(lines, start_line)
                    end_position = position + sum(len(l) + 1 for l in diagram_lines) + len('```mermaid\n```') + 2
                    
                    # Extract title using shared utility
                    title = utils.extract_title_from_content(lines, start_line)
                    
                    self.mermaid_count += 1
                    diagrams.append({
                        'title': title,
                        'content': diagram_content,
                        'position': position,
                        'start': position,
                        'end': end_position,
                        'match': f"```mermaid\n{diagram_content}\n```"
                    })
            i += 1
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
                    start_pos = utils.calculate_position(lines, table_start)
                    end_pos = start_pos + sum(len(l) + 1 for l in table_lines)
                    
                    # Extract title using shared utility
                    title = utils.extract_title_from_content(lines, table_start)
                    
                    self.table_count += 1
                    tables.append({
                        'title': title,
                        'content': table_content,
                        'position': start_pos,
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
        """Generate GitHub link using the same filename logic as story_processor.py"""
        filename = utils.get_element_filename(element_type, index, title)
        return f"{self.github_base_url}/blob/main/{self.content_dir}/{filename}"
    
    def _create_image_block(self, element_type, index, title, github_link):
        """Create the replacement image block with mermaid-01.png for all"""
        type_display = "Mermaid Diagram" if element_type == 'mermaid' else "Table"
        
        # Using HTML for the caption to ensure proper rendering in Medium
        return f"""
![{type_display} {index}: {title}](images/mermaid-01.png)
<div style="text-align: center;"><em>{type_display} {index}: {title} (<a href="{github_link}">View Source</a>)</em></div>

"""
    
    def _add_footer(self, content):
        """Add footer text with HTML formatting for Medium compatibility"""
        footer = """

---
<div style="text-align: center;">
<p><em>Questions? Feedback? Comment? leave a response below.</em><br>
<em>If you're implementing something similar and want to discuss architectural tradeoffs, I'm always happy to connect with fellow engineers tackling these challenges.</em></p>
</div>
"""
        return content + footer
    
    def _fix_formatting_for_medium(self, content):
        """
        Comprehensive fix for Medium paste compatibility.
        
        Medium requires:
        - Properly formatted code blocks with fences and no leading spaces inside
        - Asterisks for bullet points
        - Consistent spacing
        """
        lines = content.split('\n')
        result_lines = []
        in_code_block = False
        code_block_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for code block markers
            if line.strip().startswith('```'):
                if not in_code_block:
                    # Start of code block - ensure it has language specifier
                    in_code_block = True
                    code_block_lines = ['```csharp']  # Default to csharp if no language specified
                else:
                    # End of code block
                    in_code_block = False
                    code_block_lines.append('```')
                    
                    # Add the complete code block with proper formatting
                    result_lines.extend(code_block_lines)
                    result_lines.append('')  # Add blank line after code block
                    code_block_lines = []
                i += 1
                continue
            
            if in_code_block:
                # Inside code block - remove ALL leading/trailing spaces but preserve indentation
                # Medium doesn't handle leading spaces well in code blocks
                stripped_line = line.rstrip()
                if stripped_line:  # Only add non-empty lines
                    # Remove leading spaces but preserve one level of indentation for readability
                    # This helps with code that needs indentation to be readable
                    if stripped_line.startswith('    '):
                        # Keep 4 spaces for code indentation
                        code_block_lines.append(stripped_line)
                    else:
                        # Remove all leading spaces
                        code_block_lines.append(stripped_line.lstrip())
                i += 1
                continue
            
            # Handle bullet points outside code blocks
            if line.strip().startswith('- '):
                # Convert to asterisk bullet
                bullet_content = line.strip()[2:]  # Remove '- ' prefix
                result_lines.append(f"* {bullet_content}")
            elif line.strip().startswith('  - '):
                # Nested bullet
                bullet_content = line.strip()[4:]  # Remove '  - ' prefix
                result_lines.append(f"  * {bullet_content}")
            else:
                result_lines.append(line)
            
            i += 1
        
        # Handle case where code block wasn't closed
        if in_code_block and code_block_lines:
            code_block_lines.append('```')
            result_lines.extend(code_block_lines)
        
        # Post-process to ensure code blocks are properly formatted
        final_lines = []
        i = 0
        while i < len(result_lines):
            line = result_lines[i]
            
            # Check for code block start
            if line.strip().startswith('```') and i + 1 < len(result_lines):
                final_lines.append(line)  # Add the opening fence
                i += 1
                
                # Add code content until closing fence
                while i < len(result_lines) and not result_lines[i].strip().startswith('```'):
                    code_line = result_lines[i]
                    # Ensure code lines don't have leading spaces except for indentation
                    if code_line.strip():
                        # Keep indentation for code readability
                        final_lines.append(code_line)
                    i += 1
                
                # Add closing fence if found
                if i < len(result_lines) and result_lines[i].strip().startswith('```'):
                    final_lines.append('```')
                    i += 1
                    # Add blank line after code block
                    final_lines.append('')
            else:
                final_lines.append(line)
                i += 1
        
        # Join with appropriate newlines
        return '\n'.join(final_lines)
    
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
        
        # Fix formatting for Medium compatibility
        modified_content = self._fix_formatting_for_medium(modified_content)
        self._log("Fixed formatting for Medium paste")
        
        # Add footer
        modified_content = self._add_footer(modified_content)
        self._log("Added footer text")
        
        # Write the final file
        output_path = os.path.join(os.path.dirname(self.filename) or '.', self.output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        self._log(f"Created final file: {output_path}")
        
        # Create log file
        timestamp = utils.get_log_timestamp()
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