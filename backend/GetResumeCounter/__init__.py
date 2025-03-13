import logging
import os
import json
import azure.functions as func
from azure.data.tables import TableServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request to get visitor count.')
    
    try:
        # Debug connection string value
        connection_string = os.environ.get("COSMOS_CONNECTION_STRING", "Not Found")
        table_name = os.environ.get("TABLE_NAME", "Not Found")
        
        logging.info(f"Connection string exists: {'Yes' if connection_string != 'Not Found' else 'No'}")
        logging.info(f"Table name: {table_name}")
        
        # Return debugging info (temporarily)
        return func.HttpResponse(
            json.dumps({"debug": "Connection check", 
                       "has_connection_string": connection_string != "Not Found",
                       "table_name": table_name}),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"Debug error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )