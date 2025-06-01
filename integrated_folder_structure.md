# Integrated Folder Structure for zenlytic-docs

## Overview
This document outlines how to integrate the current project's content into zenlytic-docs as part of the integrated documentation. The goal is to ensure a seamless folder structure, consistent naming conventions, and proper organization.

## Integration Strategy

### 1. Folder Naming & Numbering
- **zenlytic-docs** uses numbered, snake_case folders for each major section (e.g., `2_tips_and_tricks`, `3_zenlytic_ui`, `5_data_modeling`).
- Each folder contains a `README.md` as the section landing page, and all content files are also snake_case, often with a leading number for ordering.

### 2. How to Integrate Your Content

#### A. Map Your Sections to Existing or New Folders

**Example mapping:**

| Your Section                    | zenlytic-docs Section/Filename Suggestion         |
|---------------------------------|--------------------------------------------------|
| Getting Started                 | `2_tips_and_tricks/` or new `1_getting_started/` |
| Data Sources                    | `3_zenlytic_ui/` (if UI-focused) or new section  |
| Authentication & Security       | `3_zenlytic_ui/` or new section                  |
| Dashboards & Analysis           | `3_zenlytic_ui/`                                 |
| Data Modeling                   | `5_data_modeling/`                               |
| Follow-ups & Notifications      | `3_zenlytic_ui/` or new section                  |

- If your content fits an existing section, move the files into that folder.
- If it's a new area, create a new numbered folder (e.g., `10_intercom_docs/`).

#### B. File Naming

- Rename files to use snake_case and, if you want to control order, prefix with a number (e.g., `1_getting_started.md`, `2_user_journey.md`).
- Each section should have a `README.md` as an overview.

#### C. Example Structure

Suppose you want to add your docs as a new section:

```
10_intercom_docs/
  README.md
  1_getting_started.md
  2_user_journey.md
  3_user_roles.md
  4_workspace_settings.md
  5_workspace_groups_and_permissions.md
  6_data_sources.md
  7_authentication.md
  8_dashboards.md
  9_data_modeling.md
  10_follow_ups.md
assets/
```

Or, if you want to merge into existing sections, place your files in the appropriate folders and update the `SUMMARY.md` accordingly.

### 3. Update SUMMARY.md

- Add your new section and files to the `SUMMARY.md` in the same style as the rest of the project.
- Example:

```markdown
* [Intercom Docs](10_intercom_docs/README.md)
  * [Getting Started](10_intercom_docs/1_getting_started.md)
  * [User Journey](10_intercom_docs/2_user_journey.md)
  ...
```

### 4. Assets

- Place all images and other assets in the top-level `assets/` directory, as zenlytic-docs does.

### 5. Final Tips

- Use snake_case for all file and folder names.
- Use numbered prefixes for ordering if needed.
- Each section should have a `README.md` as a landing page.
- Update all internal links to match the new paths.

## Next Steps

1. **Create the Folder:**  
   Create `10_intercom_docs/` in zenlytic-docs.

2. **Copy Files:**  
   Copy all files to their new locations as mapped.

3. **Create README.md:**  
   Add a `README.md` in `10_intercom_docs/` as a landing page.

4. **Update SUMMARY.md:**  
   Add the new section and files to zenlytic-docs' `SUMMARY.md`.

5. **Move Assets:**  
   Move all assets to the top-level `assets/` directory.

This integrated folder structure ensures a seamless import into zenlytic-docs, following its folder naming and numbering conventions. 