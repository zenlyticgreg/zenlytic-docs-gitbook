# Using Entra to Authenticate Snowflake in Zenlytic

This guide will walk you through the process of setting up Microsoft Entra (formerly Azure AD) authentication for Snowflake in Zenlytic.

## Prerequisites

- A Microsoft Entra account with administrative access
- A Snowflake account with administrative access
- A Zenlytic account with administrative access

## Overview

The integration process involves:
1. Setting up OAuth in Snowflake
2. Configuring Entra application
3. Connecting Zenlytic to use Entra authentication

## Step 1: Snowflake OAuth Setup

1. Log into your Snowflake account
2. Navigate to Admin > Security > OAuth
3. Click "Create OAuth Integration"
4. Configure the following settings:
   - Name: `zenlytic-entra`
   - OAuth Client Type: `Confidential`
   - Redirect URI: `https://app.zenlytic.com/oauth/callback`
   - Access Token Lifetime: `3600` (1 hour)
   - Refresh Token Lifetime: `604800` (7 days)

![Snowflake OAuth Configuration](/assets/entra-snowflake/snowflake_oauth.png)

5. After creation, note down the following values:
   - Client ID
   - Client Secret
   - OAuth Token URL
   - OAuth Authorization URL

6. Configure the redirect URI in Snowflake:
   - Navigate to the OAuth integration settings
   - Add the redirect URI: `https://app.zenlytic.com/oauth/callback`

![Snowflake Redirect URI Configuration](/assets/entra-snowflake/snowflake_redirect_uri.png)

7. Set up the token configuration:
   - Configure the token settings as shown below
   - Ensure the token lifetime matches your security requirements

![Snowflake Token Configuration](/assets/entra-snowflake/snowflake_redirect_uri_token.png)

## Step 2: Entra Application Configuration

1. Log into the Microsoft Entra admin center
2. Navigate to Applications > App registrations
3. Click "New registration"
4. Configure the following:
   - Name: `Zenlytic Snowflake Integration`
   - Supported account types: `Single tenant`
   - Redirect URI: `https://app.zenlytic.com/oauth/callback`

5. Set up the application as a single-page application:
   - Navigate to Authentication
   - Select "Single-page application" as the platform
   - Add the redirect URI

![Entra Single Page App Configuration](/assets/entra-snowflake/snowflake_single_page_app.png)

6. After registration, note down:
   - Application (client) ID
   - Directory (tenant) ID

7. Create a client secret:
   - Go to Certificates & secrets
   - Click "New client secret"
   - Note down the secret value immediately

## Step 3: Zenlytic Configuration

1. Log into your Zenlytic account
2. Navigate to Settings > Integrations > Snowflake
3. Select "Microsoft Entra" as the authentication method
4. Enter the following information:
   - Entra Client ID
   - Entra Client Secret
   - Entra Tenant ID
   - Snowflake OAuth Client ID
   - Snowflake OAuth Client Secret
   - Snowflake OAuth Token URL
   - Snowflake OAuth Authorization URL

For detailed information about what to send to Zenlytic and how to send it, see [Microsoft Entra Snowflake: What to Send](microsoft_entra_snowflake_what_to_send.md).

## Testing the Integration

1. In Zenlytic, attempt to connect to Snowflake
2. You should be redirected to Microsoft Entra for authentication
3. After successful authentication, you'll be redirected back to Zenlytic
4. Verify that you can access Snowflake data in Zenlytic

## Troubleshooting

If you encounter issues:

1. Verify all OAuth URLs are correct
2. Check that the redirect URIs match exactly
3. Ensure all client IDs and secrets are entered correctly
4. Check Entra application permissions
5. Verify Snowflake OAuth integration is active

## Support

If you need assistance:
- Contact Zenlytic support at support@zenlytic.com
- Reference this integration guide in your support request

## Additional Notes

- The OAuth integration must be configured in both Snowflake and Entra
- All redirect URIs must match exactly
- Client secrets should be stored securely
- Token lifetimes can be adjusted based on your security requirements
- The integration supports both development and production environments 