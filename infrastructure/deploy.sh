#!/bin/bash

# Variables
RESOURCE_GROUP_NAME=$1
LOCATION=$2
ENVIRONMENT=$3

# Default values if not provided
if [ -z "$RESOURCE_GROUP_NAME" ]; then
    echo "Resource group name not provided. Using default: azure-resume-dev-rg"
    RESOURCE_GROUP_NAME="azure-resume-dev-rg"
fi

if [ -z "$LOCATION" ]; then
    echo "Location not provided. Using default: eastus"
    LOCATION="eastus"
fi

if [ -z "$ENVIRONMENT" ]; then
    echo "Environment not provided. Using default: dev"
    ENVIRONMENT="dev"
fi

# Check if resource group exists, create if not
if [ $(az group exists --name $RESOURCE_GROUP_NAME) = false ]; then
    echo "Resource group $RESOURCE_GROUP_NAME does not exist. Creating..."
    az group create --name $RESOURCE_GROUP_NAME --location $LOCATION
    echo "Resource group created."
else
    echo "Resource group $RESOURCE_GROUP_NAME already exists."
fi

# Deploy ARM template
echo "Deploying ARM template for $ENVIRONMENT environment..."
az deployment group create \
    --resource-group $RESOURCE_GROUP_NAME \
    --template-file main.json \
    --parameters @parameters.$ENVIRONMENT.json \
    --verbose

if [ $? -eq 0 ]; then
    echo "Deployment completed successfully."
    
    # Enable static website hosting on the storage account
    STORAGE_ACCOUNT=$(az deployment group show \
        --resource-group $RESOURCE_GROUP_NAME \
        --name main \
        --query properties.outputs.storageAccountName.value \
        -o tsv)
    
    echo "Enabling static website hosting on storage account: $STORAGE_ACCOUNT"
    az storage blob service-properties update \
        --account-name $STORAGE_ACCOUNT \
        --static-website \
        --index-document index.html \
        --404-document 404.html
    
    # Get the static website URL
    STATIC_WEBSITE_URL=$(az deployment group show \
        --resource-group $RESOURCE_GROUP_NAME \
        --name main \
        --query properties.outputs.storageStaticWebsiteUrl.value \
        -o tsv)
    
    # Get the CDN endpoint URL
    CDN_ENDPOINT_URL=$(az deployment group show \
        --resource-group $RESOURCE_GROUP_NAME \
        --name main \
        --query properties.outputs.cdnEndpointUrl.value \
        -o tsv)
    
    echo "Static website URL: $STATIC_WEBSITE_URL"
    echo "CDN endpoint URL: $CDN_ENDPOINT_URL"
    
    # Get the Function App name
    FUNCTION_APP_NAME=$(az deployment group show \
        --resource-group $RESOURCE_GROUP_NAME \
        --name main \
        --query properties.outputs.functionAppName.value \
        -o tsv)
    
    echo "Azure Function App name: $FUNCTION_APP_NAME"
    echo "Function App URL: https://$FUNCTION_APP_NAME.azurewebsites.net"
    
    echo "Deployment and configuration completed successfully."
else
    echo "Deployment failed."
fi