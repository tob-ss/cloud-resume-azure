import logging
import os
import json
import azure.functions as func
from azure.data.tables import TableServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request to get visitor count.')
    
    try:
        # Get connection string and table name from environment variables
        connection_string = os.environ.get("COSMOS_CONNECTION_STRING", "Not Found")
        table_name = os.environ.get("TABLE_NAME", "Not Found")
        
        # Log masked version of connection string for debugging
        if connection_string != "Not Found":
            masked_conn = connection_string[:20] + "..." + connection_string[-10:] if len(connection_string) > 30 else "Connection string too short"
            conn_parts = dict(part.split('=', 1) for part in connection_string.split(';') if part and '=' in part)
            logging.info(f"Connection string starts with: {masked_conn}")
            logging.info(f"Connection string parts: {list(conn_parts.keys())}")
        else:
            logging.error("Connection string not found in environment variables")
            
        logging.info(f"Table name: {table_name}")
        
        return func.HttpResponse(
            json.dumps({
                "diagnostics": {
                    "has_connection_string": connection_string != "Not Found",
                    "connection_parts": list(conn_parts.keys()) if connection_string != "Not Found" else [],
                    "table_name": table_name
                }
            }),
            mimetype="application/json",
            status_code=200
        )
    
    except Exception as e:
        logging.error(f"Error retrieving connection details: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )