# Azure Resume Challenge

This repository contains my implementation of the Azure Resume Challenge - a hands-on project to showcase cloud skills by building and deploying a personal resume website on Microsoft Azure.

## Project Overview

This project implements a cloud-based resume website with the following components:
- Frontend static website hosted in Azure Storage
- Backend API built with Azure Functions
- Visitor counter using CosmosDB
- CI/CD pipeline using GitHub Actions
- Infrastructure as Code using ARM templates
- HTTPS and CDN implementation

## Implementation Phases

### Phase 1: Initial Setup ✅
- Create Azure account
- Set up GitHub repository
- Create resource groups
- Configure service principal for GitHub Actions

### Phase 2: Infrastructure as Code Development ✅
- Develop ARM templates for required resources
- Test deployments
- Commit templates to repository

### Phase 3: Backend API Development ✅
- Create Azure Functions project
- Implement CosmosDB integration
- Develop visitor counter functionality

### Phase 4: Frontend Resume Website ✅
- Design and develop HTML/CSS resume
- Create JavaScript for visitor counter
- Implement API integration

### Phase 5: CI/CD Pipeline Implementation ✅
- Set up GitHub Actions secrets
- Create infrastructure deployment workflow
- Develop frontend and backend deployment workflows

### Phase 6: Integration and Security 🔄
- Connect custom domain
- Configure HTTPS
- Implement CORS settings
- Test full functionality

### Phase 7: Finalization 🔄
- Create documentation
- Perform testing
- Optimize performance
- Configure monitoring

## Getting Started

### Prerequisites
- Azure account
- GitHub account
- Azure CLI installed locally
- Visual Studio Code (recommended)

### Development Setup
1. Clone this repository
2. Set up required Azure resources using the ARM templates
3. Run the frontend locally for testing
4. Run the Azure Functions locally using Azure Functions Core Tools

## Deployment

The project uses GitHub Actions for automated deployment:
- Changes to ARM templates trigger infrastructure updates
- Changes to frontend code deploy to Azure Storage
- Changes to API code deploy to Azure Functions

## Resources

- [Azure Resume Challenge Official Guide](https://github.com/madebygps/cloud-resume-challenge)
- [Azure Documentation](https://docs.microsoft.com/en-us/azure/)
- [Azure Functions Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.