#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_formatting(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths
    content = re.sub(r'!\[\]\(images/', '![](/images/', content)
    # Remove extra newlines between image path and closing parenthesis
    content = re.sub(r'!\[]\((/images/[^\)\n]+)\n+\)', r'![](\1)', content)
    # Also handle any case where there is whitespace before the closing parenthesis
    content = re.sub(r'!\[]\((/images/[^\)]+)\s+\)', r'![](\1)', content)
    
    # Fix headers using dashes to use hash symbols and remove extra hashes
    content = re.sub(r'^([A-Za-z0-9 ]+)\s*-{3,}$', r'# \1', content, flags=re.MULTILINE)
    content = re.sub(r'#\s*$', '', content, flags=re.MULTILINE)
    
    # Fix line breaks around images (optional, can be commented out if not needed)
    # content = re.sub(r'([^\n])(!\[\])', r'\1\n\n\2', content)
    # content = re.sub(r'(!\[\]\([^)]+\))([^\n])', r'\1\n\n\2', content)
    
    # Fix multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Fix relative links to use proper GitBook format
    content = re.sub(r'https://intercom\.help/zenlytic/en/articles/', '/', content)
    content = re.sub(r'https://docs\.zenlytic\.com/docs/', '/', content)
    
    # Fix links to use full GitBook paths
    content = re.sub(r'\[([^\]]+)\]\(/(\d+)-([^)]+)\)', r'[\1](/articles/\2-\3)', content)
    
    # Write the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Process all markdown files in the exported_articles directory
    articles_dir = Path('exported_articles')
    for file_path in articles_dir.glob('*.md'):
        print(f"Processing {file_path}...")
        fix_formatting(file_path)

if __name__ == '__main__':
    main() 