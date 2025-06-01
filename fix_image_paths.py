import os
import re
from pathlib import Path

def fix_image_paths(directory):
    # Regular expression to match markdown image syntax
    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    
    # Walk through all markdown files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_depth = len(Path(file_path).relative_to(directory).parts) - 1
                
                # Read the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Function to fix each image path
                def replace_image_path(match):
                    alt_text = match.group(1)
                    path = match.group(2)
                    
                    # Skip if path is already relative or is a URL
                    if path.startswith('http') or path.startswith('../'):
                        return match.group(0)
                    
                    # Fix paths starting with /assets/ or /images/
                    if path.startswith('/assets/') or path.startswith('/images/'):
                        # Remove leading slash and add appropriate number of ../
                        new_path = '../' * relative_depth + path.lstrip('/')
                        return f'![{alt_text}]({new_path})'
                    
                    return match.group(0)
                
                # Apply the fixes
                new_content = re.sub(image_pattern, replace_image_path, content)
                
                # Write back if changes were made
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Fixed image paths in: {file_path}')

if __name__ == '__main__':
    # Run the script on the docs directory
    fix_image_paths('docs') 