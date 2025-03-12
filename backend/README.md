# Azure Resume Challenge - Backend API

This directory contains the Azure Functions API for the resume visitor counter.

## Functions

There are two HTTP-triggered functions:

1. **GetResumeCounter** - Retrieves the current visitor count from CosmosDB Table API
2. **UpdateResumeCounter** - Increments the visitor count and returns the updated value

## Local Development Setup

### Prerequisites

- [Python 3.8 or later](https://www.python.org/downloads/)
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Visual Studio Code](https://code.visualstudio.com/) with [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) (recommended)

### Setup Steps

1. Create a Python virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up local.settings.json
   - Copy the connection string for your CosmosDB account from the Azure Portal
   - Update the `COSMOS_CONNECTION_STRING` value in local.settings.json

4. Start the Functions locally
   ```bash
   func start
   ```

## API Endpoints

When running locally, the API endpoints are:

- GET http://localhost:7071/api/GetResumeCounter
- GET/POST http://localhost:7071/api/UpdateResumeCounter

When deployed to Azure, replace `localhost:7071` with your function app URL.

## Response Format

Both endpoints return JSON in the following format:

```json
{
  "count": 42
}
```

## Testing

This project includes unit tests that mock the CosmosDB Table API to test functionality without requiring a real database connection.

Run tests with:

```bash
python -m unittest discover -s tests
```

## Deployment

The functions can be deployed to Azure using:

```bash
func azure functionapp publish <FUNCTION_APP_NAME>
```

Or preferably, use the CI/CD pipeline configured in the GitHub workflow.

## Troubleshooting

- **Missing Connection String**: If you get connection errors, ensure the `COSMOS_CONNECTION_STRING` environment variable is set correctly.
- **Table Not Found**: The function will automatically create the table and counter entity if they don't exist.
- **CORS Issues**: If you're having CORS issues when calling from your frontend, check the CORS settings in the Azure Portal for your Function App.