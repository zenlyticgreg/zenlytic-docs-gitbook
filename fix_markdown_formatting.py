import os
import re
from pathlib import Path

def fix_markdown_formatting(directory):
    # Regular expressions for various formatting patterns
    heading_pattern = r'^([#]+)\s*(.*?)$'
    list_pattern = r'^\s*[-*]\s+(.*?)$'
    code_block_pattern = r'```(.*?)```'
    
    # Walk through all markdown files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Read the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix heading formatting
                def fix_heading(match):
                    hashes = match.group(1)
                    text = match.group(2).strip()
                    return f'{hashes} {text}'
                
                # Fix list formatting
                def fix_list(match):
                    item = match.group(1).strip()
                    return f'* {item}'
                
                # Fix code block formatting
                def fix_code_block(match):
                    code = match.group(1).strip()
                    return f'```\n{code}\n```'
                
                # Apply fixes
                new_content = content
                
                # Fix headings
                new_content = re.sub(heading_pattern, fix_heading, new_content, flags=re.MULTILINE)
                
                # Fix lists
                new_content = re.sub(list_pattern, fix_list, new_content, flags=re.MULTILINE)
                
                # Fix code blocks
                new_content = re.sub(code_block_pattern, fix_code_block, new_content, flags=re.DOTALL)
                
                # Fix common formatting issues
                new_content = re.sub(r'\n{3,}', '\n\n', new_content)  # Remove excessive newlines
                new_content = re.sub(r' {2,}', ' ', new_content)  # Remove excessive spaces
                new_content = re.sub(r'\t', '    ', new_content)  # Replace tabs with spaces
                
                # Fix image alt text formatting
                new_content = re.sub(r'!\[(.*?)\s*-\s*(.*?)\]', r'![\1]', new_content)  # Remove redundant alt text
                
                # Fix link formatting
                new_content = re.sub(r'\[(.*?)\]\((.*?)\)', lambda m: f'[{m.group(1).strip()}]({m.group(2).strip()})', new_content)
                
                # Write back if changes were made
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Fixed formatting in: {file_path}')

if __name__ == '__main__':
    # Run the script on the docs directory
    fix_markdown_formatting('docs') 