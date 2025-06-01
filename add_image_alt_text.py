#!/usr/bin/env python3

import os
import re
from pathlib import Path

def generate_alt_text(filename, context_before, context_after):
    # Remove file extension and common prefixes
    base_name = os.path.splitext(filename)[0]
    base_name = re.sub(r'^(screenshot|screen-recording|image)-', '', base_name)
    
    # Convert dashes and underscores to spaces and capitalize
    alt_text = base_name.replace('-', ' ').replace('_', ' ')
    alt_text = ' '.join(word.capitalize() for word in alt_text.split())
    
    # Add context if available, but keep it short
    if context_before:
        # Take the last sentence before the image
        sentences = re.split(r'[.!?]', context_before)
        if sentences:
            last_sentence = sentences[-1].strip()
            if len(last_sentence) > 10 and len(last_sentence) < 50:  # Only use if it's a meaningful but short sentence
                alt_text = f"{alt_text} - {last_sentence}"
    
    # Ensure alt text isn't too long
    if len(alt_text) > 100:
        alt_text = alt_text[:97] + "..."
    
    return alt_text

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image references
    image_pattern = r'!\[\]\((/images/[^)]+)\)'
    
    def replace_image(match):
        image_path = match.group(1)
        filename = os.path.basename(image_path)
        
        # Get context (text before and after the image)
        start_pos = match.start()
        end_pos = match.end()
        
        # Get 200 characters before the image
        context_before = content[max(0, start_pos-200):start_pos]
        # Get 200 characters after the image
        context_after = content[end_pos:min(len(content), end_pos+200)]
        
        # Generate alt text
        alt_text = generate_alt_text(filename, context_before, context_after)
        
        # Return the new image reference with alt text
        return f'![{alt_text}]({image_path})'
    
    # Replace all image references with ones that include alt text
    new_content = re.sub(image_pattern, replace_image, content)
    
    # Write the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    # Process all markdown files in the exported_articles directory
    articles_dir = Path('exported_articles')
    for file_path in articles_dir.glob('*.md'):
        print(f"Processing {file_path}...")
        process_markdown_file(file_path)

if __name__ == '__main__':
    main() 