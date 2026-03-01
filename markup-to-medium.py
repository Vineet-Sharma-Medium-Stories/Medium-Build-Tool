#!/usr/bin/env python3
"""
README to Medium Story Converter
Converts GitHub README.md into Medium-friendly markdown
"""

import re
import argparse
from pathlib import Path

class ReadmeToMedium:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.content = self.filename.read_text(encoding="utf-8")

    def remove_badges(self):
        # Remove shields.io badges
        self.content = re.sub(r'!\[.*?\]\(https://img\.shields\.io.*?\)', '', self.content)

    def remove_html(self):
        # Remove raw HTML tags
        self.content = re.sub(r'<.*?>', '', self.content)

    def fix_images(self, base_url):
        # Convert relative image paths to absolute
        def replace(match):
            alt = match.group(1)
            path = match.group(2)
            if not path.startswith("http"):
                path = f"{base_url}/{path}"
            return f"![{alt}]({path})"

        self.content = re.sub(r'!\[(.*?)\]\((.*?)\)', replace, self.content)

    def convert(self, base_url):
        self.remove_badges()
        self.remove_html()
        self.fix_images(base_url)

        output_file = self.filename.stem + "-medium.md"
        Path(output_file).write_text(self.content, encoding="utf-8")
        print(f"Medium-ready file created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to README.md")
    parser.add_argument("--base-url", default="", help="Base GitHub raw URL for images")
    args = parser.parse_args()

    converter = ReadmeToMedium(args.filename)
    converter.convert(args.base_url)