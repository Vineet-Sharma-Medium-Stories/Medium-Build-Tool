#!/usr/bin/env python3
"""
Table to PNG Converter
Creates beautiful tables with tick (✓) and cross (✗) symbols,
white/gray shades, and clean line separators
"""

import os
import re
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import story_utils as utils


class TableToPNGConverter:
    def __init__(self, story_name, content_dir=None):
        self.story_name = story_name
        if content_dir:
            self.content_dir = content_dir
        else:
            self.content_dir = f"{story_name}/content"
        self.images_dir = f"{story_name}/images"
        self.log_entries = []
        
        # Statistics
        self.converted_count = 0
        self.failed_count = 0
        
        # Beautiful white/gray styling
        self.header_bg = "#505050"  # Medium-dark gray header
        self.header_text = "#ffffff"  # White text
        self.header_font_size = 14
        
        self.row_colors = ["#ffffff", "#f5f5f5"]  # White and very light gray
        self.cell_text_color = "#333333"  # Dark gray text
        self.cell_font_size = 13
        
        self.border_color = "#c0c0c0"  # Light gray borders
        self.separator_color = "#a0a0a0"  # Medium gray for separators
        self.border_width = 1
        
        # Spacing
        self.cell_padding_left = 15
        self.cell_padding_right = 15
        self.cell_padding_vertical = 8
        self.cell_min_width = 90
        
        # Symbol colors
        self.tick_color = "#2e7d32"  # Green for ticks
        self.cross_color = "#c62828"  # Red for crosses
        self.symbol_font_size = 14  # Slightly larger for symbols
        
        # Fonts
        self.regular_font = None
        self.bold_font = None
        self.symbol_font = None
        
    def _log(self, message, level="INFO"):
        log_entry = utils.format_log_entry(message, level)
        self.log_entries.append(log_entry)
        print(log_entry)
    
    def _find_table_files(self):
        """Find all table files in content directory"""
        table_files = []
        pattern = re.compile(r'(\d+)-t-.*\.md$')
        
        try:
            content_path = Path(self.content_dir)
            if not content_path.exists():
                self._log(f"Content directory not found: {self.content_dir}", "ERROR")
                return []
            
            for file_path in content_path.iterdir():
                if file_path.is_file():
                    match = pattern.match(file_path.name)
                    if match:
                        index = int(match.group(1))
                        table_files.append({
                            'index': index,
                            'filename': file_path.name,
                            'path': str(file_path),
                            'base_name': os.path.splitext(file_path.name)[0]
                        })
            
            table_files.sort(key=lambda x: x['index'])
            return table_files
            
        except Exception as e:
            self._log(f"Error scanning content directory: {str(e)}", "ERROR")
            return []
    
    def _parse_markdown_table(self, content):
        """Parse markdown table into rows and columns"""
        lines = content.strip().split('\n')
        
        # Find table content
        table_lines = []
        for line in lines:
            if '|' in line:
                table_lines.append(line)
        
        if len(table_lines) < 2:
            return None, None
        
        # Parse header (first line)
        header = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
        
        # Parse data rows (skip separator line if present)
        data_rows = []
        start_idx = 2 if len(table_lines) > 1 and '---' in table_lines[1] else 1
        
        for i in range(start_idx, len(table_lines)):
            row = [cell.strip() for cell in table_lines[i].split('|')[1:-1]]
            # Pad row if needed
            while len(row) < len(header):
                row.append('')
            if any(cell for cell in row if cell):
                data_rows.append(row[:len(header)])
        
        return header, data_rows
    
    def _load_fonts(self):
        """Load fonts that support ✓ and ✗ symbols"""
        font_paths = [
            # Linux
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
            
            # macOS
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Helvetica-Bold.ttc",
            "/Library/Fonts/Arial.ttf",
            "/Library/Fonts/Arial Bold.ttf",
            
            # Windows
            "C:\\Windows\\Fonts\\arial.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf",
            "C:\\Windows\\Fonts\\segoeui.ttf",
            "C:\\Windows\\Fonts\\segoeuib.ttf",
        ]
        
        # Try to load fonts
        for font_path in font_paths:
            try:
                if os.path.exists(font_path):
                    if "Bold" in font_path or "bold" in font_path or "bd" in font_path:
                        if not self.bold_font:
                            self.bold_font = ImageFont.truetype(font_path, self.header_font_size)
                            self._log(f"Loaded bold font: {os.path.basename(font_path)}")
                    else:
                        if not self.regular_font:
                            self.regular_font = ImageFont.truetype(font_path, self.cell_font_size)
                            self.symbol_font = ImageFont.truetype(font_path, self.symbol_font_size)
                            self._log(f"Loaded regular font: {os.path.basename(font_path)}")
            except:
                continue
        
        # Fallback
        if not self.regular_font:
            self.regular_font = ImageFont.load_default()
            self.symbol_font = self.regular_font
        if not self.bold_font:
            self.bold_font = self.regular_font
    
    def _get_text_dimensions(self, draw, text, font):
        """Get text dimensions"""
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]
        except:
            return font.getsize(text)
    
    def _calculate_dimensions(self, draw, header, data_rows):
        """Calculate optimal table dimensions"""
        col_widths = []
        for col_idx in range(len(header)):
            max_width = self._get_text_dimensions(draw, header[col_idx], self.bold_font)[0]
            
            for row in data_rows:
                if col_idx < len(row):
                    cell_width = self._get_text_dimensions(draw, str(row[col_idx]), self.regular_font)[0]
                    max_width = max(max_width, cell_width)
            
            col_width = max_width + self.cell_padding_left + self.cell_padding_right
            col_widths.append(max(col_width, self.cell_min_width))
        
        # Calculate row height
        sample_text = "Ag✓✗"
        header_height = self._get_text_dimensions(draw, sample_text, self.bold_font)[1] + (self.cell_padding_vertical * 2)
        cell_height = self._get_text_dimensions(draw, sample_text, self.regular_font)[1] + (self.cell_padding_vertical * 2)
        
        table_width = sum(col_widths) + (self.border_width * (len(header) + 1))
        table_height = header_height + (cell_height * len(data_rows)) + (self.border_width * 2)
        
        return table_width, table_height, col_widths, header_height, cell_height
    
    def _draw_cell_with_symbols(self, draw, x, y, width, height, text, bg_color):
        """Draw a cell with special handling for ✓ and ✗ symbols"""
        # Draw cell background
        draw.rectangle(
            [(x, y), (x + width, y + height)],
            fill=bg_color,
            outline=None,
            width=0
        )
        
        # Process text for symbols
        text = str(text)
        
        # Check if this cell contains only a symbol
        if text in ["✓", "✗"]:
            # Use symbol font and color
            font = self.symbol_font
            color = self.tick_color if text == "✓" else self.cross_color
        else:
            # Use regular font and color
            font = self.regular_font
            color = self.cell_text_color
        
        # Draw text left-aligned
        text_width, text_height = self._get_text_dimensions(draw, text, font)
        text_x = x + self.cell_padding_left
        text_y = y + (height - text_height) // 2
        draw.text((text_x, text_y), text, fill=color, font=font)
    
    def _create_table_image(self, header, data_rows, output_path):
        """Create a beautiful table with ticks, crosses, and line separators"""
        try:
            # Load fonts
            self._load_fonts()
            
            # Create temporary draw
            temp_img = Image.new('RGB', (1, 1))
            temp_draw = ImageDraw.Draw(temp_img)
            
            # Calculate dimensions
            width, height, col_widths, header_height, cell_height = self._calculate_dimensions(
                temp_draw, header, data_rows
            )
            
            # Add padding around the whole table
            padding = 15
            width += padding * 2
            height += padding * 2
            
            # Create image with white background
            image = Image.new('RGB', (width, height), '#ffffff')
            draw = ImageDraw.Draw(image)
            
            # Calculate table area
            table_x = padding
            table_y = padding
            table_width = width - (padding * 2)
            table_height = height - (padding * 2)
            
            # Draw header background
            draw.rectangle(
                [(table_x, table_y), (table_x + table_width, table_y + header_height)],
                fill=self.header_bg
            )
            
            # Draw header cells
            x = table_x
            for col_idx, col_name in enumerate(header):
                # Draw vertical separators between header cells
                if col_idx > 0:
                    draw.line(
                        [(x, table_y), (x, table_y + header_height)],
                        fill=self.separator_color,
                        width=self.border_width
                    )
                
                # Draw header text
                text_width, text_height = self._get_text_dimensions(draw, col_name, self.bold_font)
                text_x = x + self.cell_padding_left
                text_y = table_y + (header_height - text_height) // 2
                draw.text((text_x, text_y), col_name, fill=self.header_text, font=self.bold_font)
                
                x += col_widths[col_idx]
            
            # Draw header bottom separator (thicker)
            draw.line(
                [(table_x, table_y + header_height), (table_x + table_width, table_y + header_height)],
                fill=self.separator_color,
                width=self.border_width * 2
            )
            
            # Draw data rows
            y = table_y + header_height
            for row_idx, row in enumerate(data_rows):
                # Draw row background
                bg_color = self.row_colors[row_idx % 2]
                draw.rectangle(
                    [(table_x, y), (table_x + table_width, y + cell_height)],
                    fill=bg_color
                )
                
                # Draw vertical separators and cells
                x = table_x
                for col_idx, cell in enumerate(row):
                    # Draw vertical separators
                    if col_idx > 0:
                        draw.line(
                            [(x, y), (x, y + cell_height)],
                            fill=self.separator_color,
                            width=self.border_width
                        )
                    
                    # Draw cell content (with symbol handling)
                    self._draw_cell_with_symbols(draw, x, y, col_widths[col_idx], cell_height, cell, bg_color)
                    
                    x += col_widths[col_idx]
                
                # Draw row separator (except for last row)
                if row_idx < len(data_rows) - 1:
                    draw.line(
                        [(table_x, y + cell_height), (table_x + table_width, y + cell_height)],
                        fill=self.separator_color,
                        width=self.border_width
                    )
                
                y += cell_height
            
            # Draw outer border
            draw.rectangle(
                [(table_x, table_y), (table_x + table_width, table_y + table_height)],
                outline=self.border_color,
                width=self.border_width * 2
            )
            
            # Save image
            image.save(output_path, 'PNG', quality=95, optimize=True)
            return True
            
        except Exception as e:
            self._log(f"Error creating image: {str(e)}", "ERROR")
            return False
    
    def convert_all_tables(self):
        """Convert all table files to PNG images"""
        self._log("Starting table to PNG conversion")
        
        # Create images directory
        images_path = Path(self.images_dir)
        images_path.mkdir(parents=True, exist_ok=True)
        
        # Find all table files
        table_files = self._find_table_files()
        
        if not table_files:
            self._log("No table files found", "WARNING")
            return
        
        self._log(f"Found {len(table_files)} table files")
        
        for table_file in table_files:
            try:
                # Read table file
                with open(table_file['path'], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Skip title line if present
                if content.startswith('# '):
                    content = '\n'.join(content.split('\n')[1:])
                
                # Parse table
                header, data_rows = self._parse_markdown_table(content)
                
                if not header or not data_rows:
                    self._log(f"Failed to parse table: {table_file['filename']}", "WARNING")
                    self.failed_count += 1
                    continue
                
                # Generate output
                output_filename = f"{table_file['base_name']}.png"
                output_path = images_path / output_filename
                
                if self._create_table_image(header, data_rows, str(output_path)):
                    self.converted_count += 1
                    self._log(f"  Created: {output_filename}")
                else:
                    self.failed_count += 1
                    
            except Exception as e:
                self._log(f"Error processing {table_file['filename']}: {str(e)}", "ERROR")
                self.failed_count += 1
        
        # Summary
        self._log("=" * 50)
        self._log("CONVERSION COMPLETE")
        self._log(f"Total tables: {len(table_files)}")
        self._log(f"Converted: {self.converted_count}")
        self._log(f"Failed: {self.failed_count}")
        self._log(f"Images saved to: {self.images_dir}")
        self._log("=" * 50)
        
        # Log file
        timestamp = utils.get_log_timestamp()
        log_filename = f"table_to_png_log_{timestamp}.log"
        log_path = Path(self.story_name) / log_filename
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.log_entries))

def main():
    parser = argparse.ArgumentParser(description='Convert table markdown files to beautiful PNG images with ticks and crosses')
    parser.add_argument('story_name', help='Name of the story folder')
    parser.add_argument('--content-dir', help='Path to content directory (optional)')
    
    args = parser.parse_args()
    
    converter = TableToPNGConverter(args.story_name, args.content_dir)
    converter.convert_all_tables()

if __name__ == "__main__":
    main()