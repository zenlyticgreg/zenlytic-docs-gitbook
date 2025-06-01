#!/bin/bash

# Function to rename files and update references
rename_and_update() {
    local old_name=$1
    local new_name=$2
    local md_file=$3
    
    # Rename the file
    mv "exported_articles/images/$old_name" "exported_articles/images/$new_name"
    
    # Update references in the markdown file
    sed -i '' "s|$old_name|$new_name|g" "exported_articles/$md_file"
}

# Batch 1: workspace-settings.md
rename_and_update "Screenshot+2023-02-17+at+1.41.03+PM.png" "workspace-settings-1.png" "workspace-settings.md"
rename_and_update "Screenshot+2023-02-17+at+1.42.46+PM.png" "workspace-settings-2.png" "workspace-settings.md"
rename_and_update "Screenshot+2023-02-17+at+1.44.01+PM.png" "workspace-settings-3.png" "workspace-settings.md"

# Batch 2: following-up-from-a-dashboard.md
rename_and_update "Screen+Recording+2023-05-08+at+1.36.39+PM.gif" "following-up-from-dashboard-1.gif" "following-up-from-a-dashboard.md"
rename_and_update "Untitledwiwiscreenshot+.gif" "following-up-from-dashboard-2.gif" "following-up-from-a-dashboard.md"

# Batch 3: git-data-model-setup.md
rename_and_update "Screenshot+2023-06-08+at+11.25.43+AM.png" "git-data-model-setup-1.png" "git-data-model-setup.md"
rename_and_update "Screenshot+2023-06-08+at+11.28.57+AM.png" "git-data-model-setup-2.png" "git-data-model-setup.md"
rename_and_update "Screenshot+2023-06-08+at+11.32.04+AM.png" "git-data-model-setup-3.png" "git-data-model-setup.md"
rename_and_update "Screenshot+2023-06-08+at+11.32.20+AM.png" "git-data-model-setup-4.png" "git-data-model-setup.md"
rename_and_update "Screenshot+2023-06-08+at+11.32.43+AM.png" "git-data-model-setup-5.png" "git-data-model-setup.md"
rename_and_update "Screenshot+2023-06-08+at+11.33.07+AM.png" "git-data-model-setup-6.png" "git-data-model-setup.md"

# Batch 4: dashboards.md
rename_and_update "Screen+Recording+2023-05-08+at+2.01.53+PM.gif" "dashboards-1.gif" "dashboards.md"

# Batch 5: mysql-setup.md
rename_and_update "Screenshot+2025-02-23+at+3_28_51%E2%80%AFPM.png" "mysql-setup-1.png" "mysql-setup.md"

# Batch 6: creating-a-new-dashboard.md
rename_and_update "Screen+Recording+2023-05-08+at+10.41.20+AM.gif" "creating-dashboard-1.gif" "creating-a-new-dashboard.md"
rename_and_update "Screen+Recording+2023-05-08+at+10.41.20+AM2.gif" "creating-dashboard-2.gif" "creating-a-new-dashboard.md"

# Batch 7: workspace-groups-and-permissions.md
rename_and_update "Screen+Recording+2023-05-08+at+11.37.07+AMwiw+.gif" "workspace-groups-1.gif" "workspace-groups-and-permissions.md"
rename_and_update "Screen+Recording+2023-05-10+at+7.09.34+PMgifgif.gif" "workspace-groups-2.gif" "workspace-groups-and-permissions.md"

# Batch 8: connecting-to-github-with-a-deploy-key.md
rename_and_update "Screenshot+2023-02-03+at+2.39.21+PM.png" "github-deploy-key-1.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.42.06+PM.png" "github-deploy-key-2.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.45.00+PM.png" "github-deploy-key-3.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.46.57+PM.png" "github-deploy-key-4.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.48.04+PM.png" "github-deploy-key-5.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.49.12+PM.png" "github-deploy-key-6.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.49.25+PM.png" "github-deploy-key-7.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.49.50+PM.png" "github-deploy-key-8.png" "connecting-to-github-with-a-deploy-key.md"
rename_and_update "Screenshot+2023-02-03+at+2.53.04+PM.png" "github-deploy-key-9.png" "connecting-to-github-with-a-deploy-key.md"

# Batch 9: sql-server-setup.md
rename_and_update "Screenshot+2023-09-18+at+6.08.07+PM.png" "sql-server-setup-1.png" "sql-server-setup.md"

# Batch 10: bigquery-setup.md
rename_and_update "Screenshot+2023-10-02+at+5.51.34+PM.png" "bigquery-setup-1.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-16+at+2.50.27%E2%80%AFPM.png" "bigquery-setup-2.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-17+at+7.14.59%E2%80%AFPM.png" "bigquery-setup-3.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-17+at+7.15.27%E2%80%AFPM.png" "bigquery-setup-4.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-17+at+7.12.45%E2%80%AFPM.png" "bigquery-setup-5.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-17+at+7.17.45%E2%80%AFPM.png" "bigquery-setup-6.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-17+at+7.19.05%E2%80%AFPM.png" "bigquery-setup-7.png" "bigquery-setup.md"
rename_and_update "Screenshot+2024-01-17+at+7.19.40%E2%80%AFPM.png" "bigquery-setup-8.png" "bigquery-setup.md"

# Batch 11: user-journey.md
rename_and_update "Screen+Recording+2023-02-17+at+1.55.05+PM.gif" "user-journey-1.gif" "user-journey.md"

# Batch 12: slice-and-explore.md
rename_and_update "Screen+Recording+2023-02-06+at+7.58.12+AM.gif" "slice-explore-1.gif" "slice-and-explore.md"
rename_and_update "Screen+Recording+2023-02-06+at+8.07.57+AM.gif" "slice-explore-2.gif" "slice-and-explore.md"

# Batch 13: databricks-setup.md
rename_and_update "Screenshot+2024-01-30+at+2.47.09%E2%80%AFPM.png" "databricks-setup-1.png" "databricks-setup.md"
rename_and_update "Screenshot+2024-01-30+at+2.50.58%E2%80%AFPM.png" "databricks-setup-2.png" "databricks-setup.md"
rename_and_update "Screenshot+2024-01-30+at+2.53.17%E2%80%AFPM.png" "databricks-setup-3.png" "databricks-setup.md"

# Batch 14: redshift-setup.md
rename_and_update "Screenshot+2023-06-08+at+10.51.33+AM.png" "redshift-setup-1.png" "redshift-setup.md"
rename_and_update "Screenshot+2023-06-08+at+10.55.39+AM.png" "redshift-setup-2.png" "redshift-setup.md"

# Batch 15: getting-started.md
rename_and_update "Screenshot+2023-01-24+at+7.17.29+AM.png" "getting-started-1.png" "getting-started.md"
rename_and_update "Screenshot+2023-01-24+at+7.17.40+AM.png" "getting-started-2.png" "getting-started.md"
rename_and_update "Screenshot+2023-01-24+at+7.46.27+AM.png" "getting-started-3.png" "getting-started.md"
rename_and_update "Screenshot+2023-01-24+at+7.47.09+AM.png" "getting-started-4.png" "getting-started.md"

# Batch 16: time-periods.md
rename_and_update "Screenshot+2023-01-24+at+7.57.41+AM.png" "time-periods-1.png" "time-periods.md"

# Batch 17: baskets.md
rename_and_update "Screen+Recording+2023-02-17+at+2.04.35+PM.gif" "baskets-1.gif" "baskets.md"

# Batch 18: editing-dashboards.md
rename_and_update "Screen+Recording+2023-05-08+at+11.07.13+AM.gif" "editing-dashboards-1.gif" "editing-dashboards.md"
rename_and_update "Screen+Recording+2023-05-08+at+12.30.30+PM.gif" "editing-dashboards-2.gif" "editing-dashboards.md"
rename_and_update "Screen+Recording+2023-05-08+at+12.46.26+PM.gif" "editing-dashboards-3.gif" "editing-dashboards.md"
rename_and_update "Screen+Recording+2023-05-08+at+12.46.26+PMwiwi.gif" "editing-dashboards-4.gif" "editing-dashboards.md"

# Batch 19: azure-synapse-setup.md
rename_and_update "Screenshot+2024-02-02+at+6.04.12%E2%80%AFPM.png" "azure-synapse-setup-1.png" "azure-synapse-setup.md"

# Batch 20: explain-change.md
rename_and_update "Screenshot+2023-01-24+at+8.11.01+AM.png" "explain-change-1.png" "explain-change.md"
rename_and_update "Screenshot+2023-01-24+at+8.12.03+AM.png" "explain-change-2.png" "explain-change.md"

# Batch 21: table-calculations.md
rename_and_update "Screenshot+2023-02-02+at+8.50.33+PM.png" "table-calculations-1.png" "table-calculations.md"

# Batch 22: funnel.md
rename_and_update "Screenshot+2023-01-24+at+8.27.30+AM.png" "funnel-1.png" "funnel.md"
rename_and_update "Screenshot+2023-01-24+at+8.27.55+AM.png" "funnel-2.png" "funnel.md"

# Batch 23: compare.md
rename_and_update "Screenshot+2023-01-24+at+8.16.17+AM.png" "compare-1.png" "compare.md"
rename_and_update "Screenshot+2023-01-24+at+8.16.59+AM.png" "compare-2.png" "compare.md"

# Batch 24: data-model-editor.md
rename_and_update "Screenshot+2023-04-14+at+5.01.40+PM.png" "data-model-editor-1.png" "data-model-editor.md"
rename_and_update "Screenshot+2023-04-14+at+4.55.06+PM.png" "data-model-editor-2.png" "data-model-editor.md"
rename_and_update "Screenshot+2023-04-14+at+4.54.51+PM.png" "data-model-editor-3.png" "data-model-editor.md"
rename_and_update "Screenshot+2023-04-14+at+4.55.20+PM.png" "data-model-editor-4.png" "data-model-editor.md"
rename_and_update "Screenshot+2023-05-10+at+6.00.00+PM.png" "data-model-editor-5.png" "data-model-editor.md"

# Batch 25: postgres-setup.md
rename_and_update "Screenshot+2023-06-08+at+11.04.57+AM.png" "postgres-setup-1.png" "postgres-setup.md"

# Batch 26: dashboard-filters.md
rename_and_update "Screen+Recording+2023-05-08+at+11.51.52+AM.gif" "dashboard-filters-1.gif" "dashboard-filters.md"
rename_and_update "Screen+Recording+2023-05-08+at+12.08.49+PM.gif" "dashboard-filters-2.gif" "dashboard-filters.md"
rename_and_update "Screen+Recording+2023-05-08+at+12.26.13+PM.gif" "dashboard-filters-3.gif" "dashboard-filters.md"

# Batch 27: snowflake-setup.md
rename_and_update "Screenshot+2023-06-08+at+10.12.54+AM.png" "snowflake-setup-1.png" "snowflake-setup.md"
rename_and_update "Screenshot+2023-06-08+at+10.08.33+AM.png" "snowflake-setup-2.png" "snowflake-setup.md"
rename_and_update "Screenshot+2023-06-08+at+10.16.51+AM.png" "snowflake-setup-3.png" "snowflake-setup.md"

# Batch 28: follow-ups.md
rename_and_update "Screen+Recording+2023-02-06+at+11.12.11+AM.gif" "follow-ups-1.gif" "follow-ups.md"
rename_and_update "Screen+Recording+2023-02-06+at+11.39.49+AM.gif" "follow-ups-2.gif" "follow-ups.md"
rename_and_update "Screen+Recording+2023-02-06+at+11.18.11+AM.gif" "follow-ups-3.gif" "follow-ups.md"

# Batch 29: motherduck-setup.md
rename_and_update "Screenshot+2023-10-16+at+8.28.49+AM.png" "motherduck-setup-1.png" "motherduck-setup.md" 