import logging
import os
import json
import azure.functions as func
from azure.data.tables import TableServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request to get visitor count.')
    
    try:
        # Get connection string and table name from environment variables
        connection_string = os.environ["COSMOS_CONNECTION_STRING"]
        table_name = os.environ["TABLE_NAME"]
        
        # Create the table service
        table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
        table_client = table_service.get_table_client(table_name)
        
        # Get visitor counter entity - use a fixed partition and row key
        try:
            counter_entity = table_client.get_entity(partition_key="counter", row_key="visits")
            count = counter_entity.get("count", 0)
        except Exception as e:
            logging.warning(f"Counter entity not found: {str(e)}. Creating new entity.")
            # If entity doesn't exist, create it
            counter_entity = {"PartitionKey": "counter", "RowKey": "visits", "count": 0}
            table_client.create_entity(counter_entity)
            count = 0
        
        # Return the count as a JSON response
        return func.HttpResponse(
            json.dumps({"count": count}),
            mimetype="application/json",
            status_code=200
        )
    
    except Exception as e:
        logging.error(f"Error retrieving visitor count: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )