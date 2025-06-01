import os
import shutil
from pathlib import Path

def create_section_readme(section_path, title):
    """Create a README.md file for a section."""
    readme_content = f"# {title}\n\nThis section contains documentation about {title.lower()}."
    with open(os.path.join(section_path, "README.md"), "w") as f:
        f.write(readme_content)

def reorganize_structure():
    # Define the new structure
    structure = {
        "1_getting_started": {
            "title": "Getting Started",
            "files": [
                "getting-started.md",
                "user-journey.md",
                "user-roles.md",
                "workspace-settings.md",
                "workspace-groups-and-permissions.md"
            ]
        },
        "2_data_sources": {
            "title": "Data Sources",
            "files": [
                "bigquery-setup.md",
                "snowflake-setup.md",
                "redshift-setup.md",
                "postgres-setup.md",
                "mysql-setup.md",
                "sql-server-setup.md",
                "azure-synapse-setup.md",
                "databricks-setup.md",
                "druid-setup.md",
                "trino-onboarding.md",
                "motherduck-setup.md",
                "git-data-model-setup.md"
            ]
        },
        "3_authentication": {
            "title": "Authentication & Security",
            "files": [
                "microsoft-entra-zenlytic.md",
                "okta-zenlytic.md",
                "eu-ip-whitelisting.md",
                "login-troubleshooting.md",
                "connecting-to-github-with-a-deploy-key.md"
            ]
        },
        "4_dashboards": {
            "title": "Dashboards & Analysis",
            "files": [
                "dashboards.md",
                "creating-a-new-dashboard.md",
                "editing-dashboards.md",
                "dashboard-filters.md",
                "merged-results.md",
                "table-calculations.md",
                "time-periods.md",
                "filtering.md",
                "slicing.md",
                "slice-and-explore.md",
                "compare.md",
                "funnel.md",
                "baskets.md",
                "explain-change.md"
            ]
        },
        "5_data_modeling": {
            "title": "Data Modeling",
            "files": [
                "data-model-editor.md",
                "ai-onboarding.md"
            ]
        },
        "6_follow_ups": {
            "title": "Follow-ups & Notifications",
            "files": [
                "follow-ups.md",
                "following-up-from-a-dashboard.md"
            ]
        }
    }

    # Create new structure
    for section, info in structure.items():
        # Create section directory
        os.makedirs(section, exist_ok=True)
        
        # Create README.md for section
        create_section_readme(section, info["title"])
        
        # Move and rename files
        for file in info["files"]:
            # Handle files in subdirectories
            old_path = os.path.join("docs", file)
            if not os.path.exists(old_path):
                # Try to find the file in subdirectories
                for root, _, files in os.walk("docs"):
                    if file in files:
                        old_path = os.path.join(root, file)
                        break
            
            if os.path.exists(old_path):
                new_name = file.replace("-", "_")
                new_path = os.path.join(section, new_name)
                try:
                    shutil.copy2(old_path, new_path)
                    print(f"Copied {old_path} to {new_path}")
                except Exception as e:
                    print(f"Error copying {old_path}: {str(e)}")
            else:
                print(f"Warning: Could not find file {file}")

    # Create new SUMMARY.md
    summary_content = "# Summary\n\n"
    for section, info in structure.items():
        summary_content += f"* [{info['title']}]({section}/README.md)\n"
        for file in info["files"]:
            new_name = file.replace("-", "_")
            title = new_name.replace("_", " ").replace(".md", "").title()
            summary_content += f"  * [{title}]({section}/{new_name})\n"
    
    with open("SUMMARY.md", "w") as f:
        f.write(summary_content)

    # Copy assets directory
    if os.path.exists("assets"):
        try:
            shutil.copytree("assets", "assets_new", dirs_exist_ok=True)
            print("Copied assets directory to assets_new")
        except Exception as e:
            print(f"Error copying assets directory: {str(e)}")

if __name__ == "__main__":
    reorganize_structure() 