# Notion Documentation Import Process

This directory is used for staging and organizing documentation imported from Notion.

## Directory Structure

```
notion_imports/
├── docs/           # Staging area for markdown files
├── assets/         # Staging area for images and other assets
└── README.md       # This file
```

## Import Process

1. **Initial Import**
   - Import content from Notion into the `docs/` directory
   - Import all assets into the `assets/` directory
   - Maintain original Notion page IDs in filenames for reference

2. **Content Organization**
   - Review and clean up imported markdown
   - Update image references to point to correct locations
   - Ensure proper formatting and structure

3. **Integration**
   - Move cleaned content to appropriate sections in main documentation
   - Move assets to appropriate locations in `assets/` directory
   - Update SUMMARY.md to include new content

4. **Quality Check**
   - Verify all links work
   - Check image rendering
   - Ensure consistent formatting

## Naming Conventions

- Documentation files: `notion-{page-id}-{short-description}.md`
- Asset files: `notion-{page-id}-{asset-description}.{extension}`

## Backup

A backup branch has been created at `backup-pre-notion-imports` to preserve the state before any Notion imports.
