# Azure Resume Challenge - Infrastructure

This directory contains the Infrastructure as Code (IaC) components for the Azure Resume Challenge using ARM templates.

## Resources Created

The ARM templates in this directory will create the following Azure resources:

1. **Storage Account** - For hosting the static website
   - Static website hosting enabled
   - CORS configured for API access

2. **Azure Function App** - For the visitor counter API
   - Python runtime
   - Consumption plan (serverless)
   - Application settings for CosmosDB connection

3. **CosmosDB Account** - For storing visitor count data
   - Table API enabled
   - "visitors" table created automatically

4. **Azure CDN** - For HTTPS and improved performance
   - Standard Microsoft CDN profile
   - Endpoint configured to point to the storage account

5. **Application Insights** - For monitoring and logging
   - Connected to the Function App

## Files

- `main.json` - Main ARM template defining all resources
- `parameters.dev.json` - Parameters for development environment
- `parameters.prod.json` - Parameters for production environment
- `deploy.sh` - Bash script to simplify deployment

## Deployment Instructions

### Prerequisites

- Azure CLI installed
- Logged in to your Azure account (`az login`)
- Proper permissions to create resources in your subscription

### Deployment Steps

1. Navigate to the infrastructure directory
   ```bash
   cd infrastructure
   ```

2. Make the deployment script executable
   ```bash
   chmod +x deploy.sh
   ```

3. Deploy to development environment
   ```bash
   ./deploy.sh azure-resume-dev-rg ukwest dev
   ```

4. Deploy to production environment
   ```bash
   ./deploy.sh azure-resume-prod-rg ukwest prod
   ```

### Parameters

The deployment script accepts the following parameters:
1. Resource Group Name (required)
2. Azure Region (optional, defaults to "eastus")
3. Environment (optional, defaults to "dev")

### Manual Deployment

You can also deploy the ARM templates manually using Azure CLI:

```bash
az group create --name azure-resume-dev-rg --location eastus

az deployment group create \
    --resource-group azure-resume-dev-rg \
    --template-file main.json \
    --parameters @parameters.dev.json
```

## Post-Deployment Configuration

After deployment, the script will:
1. Enable static website hosting on the storage account
2. Display the URLs for:
   - Static website
   - CDN endpoint
   - Function App

## Outputs

The deployment outputs include:
- Storage Account Name
- Function App Name
- CosmosDB Account Name
- CDN Endpoint URL
- Static Website URL

## Testing the Deployment

After successful deployment, you can verify the infrastructure by:

1. Accessing the static website URL (should show a default page)
2. Checking the Function App in the Azure Portal
3. Verifying that the CosmosDB table has been created

## Cleanup

To remove all deployed resources when no longer needed:

```bash
az group delete --name azure-resume-dev-rg --yes
az group delete --name azure-resume-prod-rg --yes
```