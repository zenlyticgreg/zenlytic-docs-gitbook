# Intercom Help Center API Client

This script allows you to interact with Intercom's REST API to retrieve help center documentation, including articles, collections, and sections.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Intercom access token:
```
INTERCOM_ACCESS_TOKEN=your_access_token_here
```

You can find your access token in your Intercom settings under "Apps & Integrations" > "Developer Hub" > "Access Tokens".

## Usage

Run the script:
```bash
python intercom_docs.py
```

The script will:
1. Fetch all collections from your help center
2. Retrieve all articles
3. Get sections for the first collection

## API Methods

The `IntercomAPI` class provides the following methods:

- `get_articles(page=1, per_page=50)`: Retrieve help center articles
- `get_collections()`: Retrieve help center collections
- `get_sections(collection_id)`: Retrieve sections within a collection

## Error Handling

The script includes basic error handling and will display any API errors that occur during execution. 