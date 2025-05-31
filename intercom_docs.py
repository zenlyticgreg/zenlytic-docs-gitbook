import os
import re
import requests
from dotenv import load_dotenv
import json
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import webbrowser
import time

# Load environment variables
load_dotenv()

EXPORT_DIR = "exported_articles"
IMAGES_DIR = os.path.join(EXPORT_DIR, "images")
TOKEN_FILE = ".intercom_token"

os.makedirs(IMAGES_DIR, exist_ok=True)

def slugify(value):
    value = str(value)
    value = value.lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    value = re.sub(r'-+', '-', value)
    value = value.strip('-')
    return value

class IntercomAPI:
    def __init__(self):
        self.access_token = os.getenv('INTERCOM_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("INTERCOM_ACCESS_TOKEN must be set in environment variables")
        
        self.base_url = "https://api.intercom.io"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json"
        }

    def get_articles(self, page=1, per_page=50):
        """Retrieve help center articles"""
        url = f"{self.base_url}/articles"
        params = {
            "page": page,
            "per_page": per_page,
            "include": "author,team"
        }
        
        try:
            print(f"\nFetching articles from: {url}")
            print(f"Using headers: {json.dumps(self.headers, indent=2)}")
            response = requests.get(url, headers=self.headers, params=params)
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            if response.status_code == 200:
                data = response.json()
                print("\nFull articles response:")
                print(json.dumps(data, indent=2))
                return data
            else:
                print(f"Error response: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching articles: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response details: {e.response.text}")
            return None

    def get_collections(self):
        """Retrieve help center collections"""
        url = f"{self.base_url}/collections"
        try:
            print(f"\nFetching collections from: {url}")
            response = requests.get(url, headers=self.headers)
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching collections: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response details: {e.response.text}")
            return None

    def get_sections(self, collection_id):
        """Retrieve sections within a collection"""
        url = f"{self.base_url}/sections"
        params = {"collection_id": collection_id}
        try:
            print(f"\nFetching sections from: {url}")
            response = requests.get(url, headers=self.headers, params=params)
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching sections: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response details: {e.response.text}")
            return None

    def get_workspace_info(self):
        """Get information about the current workspace"""
        url = f"{self.base_url}/workspace"
        try:
            print(f"\nFetching workspace info from: {url}")
            response = requests.get(url, headers=self.headers)
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching workspace info: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response details: {e.response.text}")
            return None

def download_image(url, dest_folder):
    try:
        filename = url.split("?")[0].split("/")[-1]
        local_path = os.path.join(dest_folder, filename)
        if not os.path.exists(local_path):
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open(local_path, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
        return os.path.relpath(local_path, EXPORT_DIR)
    except Exception as e:
        print(f"Failed to download image {url}: {e}")
        return url

def html_to_markdown(html, images_folder):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            local_img_path = download_image(src, images_folder)
            img["src"] = f"images/{os.path.basename(local_img_path)}"
    return md(str(soup))

def export_articles(articles):
    for article in articles.get('articles', []):
        title = article.get('title', 'Untitled')
        description = article.get('description', '')
        body_html = article.get('body', '')
        slug = slugify(title) or article.get('id')
        filename = f"{slug}.md"
        filepath = os.path.join(EXPORT_DIR, filename)

        # Convert HTML to Markdown and download images
        body_md = html_to_markdown(body_html, IMAGES_DIR)

        # Compose Markdown content
        md_content = f"# {title}\n\n"
        if description:
            md_content += f"> {description}\n\n"
        md_content += body_md

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Exported: {filepath}")

def main():
    try:
        api = IntercomAPI()
        print("\nFetching articles from Zenlytic Help Center...")
        
        # First try to get collections
        collections = api.get_collections()
        if collections:
            print(f"\nFound {len(collections.get('collections', []))} collections:")
            for collection in collections.get('collections', []):
                print(f"\nCollection: {collection.get('name', 'Untitled')}")
                print(f"ID: {collection.get('id')}")
                print("-" * 80)
        
        # Then get articles
        articles = api.get_articles()
        # Print the keys at the top level for debugging
        if articles:
            print(f"\nTop-level keys in articles response: {list(articles.keys())}")
            # Try to find the correct key for articles
            if 'articles' in articles:
                articles_list = articles['articles']
            elif 'data' in articles:
                articles_list = articles['data']
            else:
                articles_list = []
            if articles_list:
                print(f"\nFound {len(articles_list)} articles:")
                for article in articles_list:
                    print(f"\nTitle: {article.get('title', 'Untitled')}")
                    print(f"ID: {article.get('id')}")
                    print(f"URL: {article.get('url')}")
                    print(f"State: {article.get('state')}")
                    print("-" * 80)
                # Ask user if they want to export
                response = input("\nWould you like to export these articles to Markdown? (y/n): ")
                if response.lower() == 'y':
                    export_articles({'articles': articles_list})
                    print(f"\nExported {len(articles_list)} articles to '{EXPORT_DIR}/'")
            else:
                print("No articles found in the response.")
        else:
            print("No articles found or error occurred")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 