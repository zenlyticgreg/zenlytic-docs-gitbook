#!/bin/bash

# Function to fix formatting in a markdown file
fix_formatting() {
    local file=$1
    
    # Fix image formatting (ensure proper spacing)
    sed -i '' 's|!\[\](images/|!\[\](/images/|g' "$file"
    
    # Fix headers using dashes to use hash symbols
    sed -i '' 's/^\([A-Za-z0-9 ]*\)\s*-\{3,\}$/# \1/g' "$file"
    
    # Fix line breaks after images
    sed -i '' 's/!\[\](\/images\/[^)]*)\)/!\[\](\/images\/\1)\n\n/g' "$file"
    
    # Fix multiple consecutive blank lines
    sed -i '' '/^$/N;/^\n$/D' "$file"
    
    # Fix relative links to use proper GitBook format
    sed -i '' 's|https://intercom.help/zenlytic/en/articles/|/|g' "$file"
    sed -i '' 's|https://docs.zenlytic.com/docs/|/|g' "$file"
    
    # Add proper spacing around images
    sed -i '' 's/\([^!]\)!\[\]/\1\n\n!\[\]/g' "$file"
    sed -i '' 's/!\[\]\([^)]*\)/!\[\]\1\n\n/g' "$file"
}

# Process all markdown files
for file in exported_articles/*.md; do
    echo "Processing $file..."
    fix_formatting "$file"
done 