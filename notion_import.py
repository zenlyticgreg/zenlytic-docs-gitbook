import os
import requests
from notion_client import Client
import json
from pathlib import Path
import time
from urllib.parse import urlparse
import mimetypes
import shutil
import hashlib

class NotionImporter:
    def __init__(self, api_key, config_file="notion_pages.json"):
        self.notion = Client(auth=api_key)
        self.config = self.load_config(config_file)
        self.setup_directories()
        self.image_counter = {}  # Track image counts for unique naming
        self.list_counters = {}  # Add a counter for each list

    def load_config(self, config_file):
        """Load configuration from JSON file"""
        with open(config_file, 'r') as f:
            return json.load(f)

    def setup_directories(self):
        """Create necessary directories"""
        dirs = [
            self.config['output_structure']['docs_dir'],
            self.config['output_structure']['assets_dir'],
            self.config['output_structure']['final_docs_dir'],
            self.config['output_structure']['final_assets_dir']
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)

    def get_unique_filename(self, original_filename, page_filename):
        """Generate a unique filename for images based on the page filename"""
        # Get the base name of the page file (without .md)
        page_base = os.path.splitext(page_filename)[0]
        
        # Get the extension from the original filename
        _, ext = os.path.splitext(original_filename)
        
        # Create a counter for this page's images
        if page_base not in self.image_counter:
            self.image_counter[page_base] = 0
        self.image_counter[page_base] += 1
        
        # Generate new filename: page_name_image_1.ext
        return f"{page_base}_image_{self.image_counter[page_base]}{ext}"

    def download_image(self, url, original_filename, page_filename):
        """Download image from Notion"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Generate unique filename based on page name
                filename = self.get_unique_filename(original_filename, page_filename)
                
                # Save to staging directory
                staging_path = os.path.join(self.config['output_structure']['assets_dir'], filename)
                with open(staging_path, 'wb') as f:
                    f.write(response.content)
                
                # Copy to final directory if different
                final_path = os.path.join(self.config['output_structure']['final_assets_dir'], filename)
                if staging_path != final_path:
                    shutil.copy2(staging_path, final_path)
                
                print(f"Downloaded image: {filename}")
                return filename
            print(f"Failed to download image: {url}")
            return None
        except Exception as e:
            print(f"Error downloading image {url}: {e}")
            return None

    def process_blocks(self, blocks, page_id, page_filename):
        """Process Notion blocks and convert to markdown"""
        markdown = []
        for block in blocks.get('results', []):
            block_type = block.get('type')
            
            if block_type == 'paragraph':
                text = self.get_text_from_rich_text(block.get('paragraph', {}).get('rich_text', []))
                if text:
                    markdown.append(text)
            
            elif block_type == 'heading_1':
                text = self.get_text_from_rich_text(block.get('heading_1', {}).get('rich_text', []))
                if text:
                    markdown.append(f"# {text}")
            
            elif block_type == 'heading_2':
                text = self.get_text_from_rich_text(block.get('heading_2', {}).get('rich_text', []))
                if text:
                    markdown.append(f"## {text}")
            
            elif block_type == 'heading_3':
                text = self.get_text_from_rich_text(block.get('heading_3', {}).get('rich_text', []))
                if text:
                    markdown.append(f"### {text}")
            
            elif block_type == 'bulleted_list_item':
                text = self.get_text_from_rich_text(block.get('bulleted_list_item', {}).get('rich_text', []))
                if text:
                    markdown.append(f"- {text}")
            
            elif block_type == 'numbered_list_item':
                # Get the list ID to track numbering
                list_id = block.get('id')
                if list_id not in self.list_counters:
                    self.list_counters[list_id] = 1
                number = self.list_counters[list_id]
                self.list_counters[list_id] += 1
                text = block.get('numbered_list_item', {}).get('rich_text', [{}])[0].get('text', {}).get('content', '')
                markdown.append(f"{number}. {text}")
            
            elif block_type == 'image':
                image_url = block.get('image', {}).get('file', {}).get('url')
                if image_url:
                    parsed_url = urlparse(image_url)
                    original_filename = os.path.basename(parsed_url.path)
                    if not original_filename:
                        original_filename = f"image_{int(time.time())}.png"
                    filename = self.download_image(image_url, original_filename, page_filename)
                    if filename:
                        markdown.append(f"![{filename}](/assets/entra-snowflake/{filename})")
            
            # Handle code blocks
            elif block_type == 'code':
                code_text = self.get_text_from_rich_text(block.get('code', {}).get('rich_text', []))
                language = block.get('code', {}).get('language', '')
                if code_text:
                    markdown.append(f"```{language}\n{code_text}\n```")
            
            # Process child blocks if they exist
            if block.get('has_children', False):
                child_blocks = self.notion.blocks.children.list(block_id=block['id'])
                child_markdown = self.process_blocks(child_blocks, page_id, page_filename)
                markdown.extend(child_markdown)

        return markdown

    def get_text_from_rich_text(self, rich_text):
        """Extract text from Notion's rich text format"""
        return ''.join([rt.get('plain_text', '') for rt in rich_text])

    def import_page(self, page_config):
        """Import a Notion page and its content"""
        page_id = page_config['id']
        filename = page_config['filename']
        
        print(f"Importing page {page_id} ({filename})...")
        
        try:
            # Get page content
            page = self.notion.pages.retrieve(page_id=page_id)
            title = self.get_text_from_rich_text(page.get('properties', {}).get('title', {}).get('title', []))
            
            # Get page blocks
            blocks = self.notion.blocks.children.list(block_id=page_id)
            
            # Process blocks to markdown
            markdown_content = self.process_blocks(blocks, page_id, filename)
            
            # Save markdown file to staging directory
            staging_path = os.path.join(self.config['output_structure']['docs_dir'], filename)
            with open(staging_path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(markdown_content))
            
            # Copy to final directory if different
            final_path = os.path.join(self.config['output_structure']['final_docs_dir'], filename)
            if staging_path != final_path:
                shutil.copy2(staging_path, final_path)
            
            print(f"Successfully imported: {title} -> {filename}")
            
            return True
                
        except Exception as e:
            print(f"Error importing page {page_id}: {e}")
            return False

def main():
    # Get Notion API key from environment
    api_key = os.getenv('NOTION_API_KEY')
    if not api_key:
        print("Error: NOTION_API_KEY environment variable not set")
        return

    # Initialize importer
    importer = NotionImporter(api_key)

    # Process each page in the configuration
    for page in importer.config['pages']:
        if importer.import_page(page):
            print(f"Successfully imported {page['filename']}")
        else:
            print(f"Failed to import {page['filename']}")

if __name__ == "__main__":
    main() 