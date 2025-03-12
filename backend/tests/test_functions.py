import unittest
import json
import os
from unittest.mock import patch, MagicMock

import azure.functions as func
from GetResumeCounter import main as get_counter_main
from UpdateResumeCounter import main as update_counter_main

class TestFunctions(unittest.TestCase):
    
    @patch('GetResumeCounter.TableServiceClient')
    def test_get_counter(self, mock_table_service):
        # Mock request
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/GetResumeCounter',
            params={}
        )
        
        # Mock environment variables
        os.environ["COSMOS_CONNECTION_STRING"] = "mock_connection_string"
        os.environ["TABLE_NAME"] = "visitors"
        
        # Mock the table client and get_entity method
        mock_table_client = MagicMock()
        mock_table_service.from_connection_string.return_value.get_table_client.return_value = mock_table_client
        mock_table_client.get_entity.return_value = {"count": 42}
        
        # Call the function
        response = get_counter_main(req)
        
        # Check the response
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.get_body())
        self.assertEqual(response_body.get("count"), 42)
    
    @patch('UpdateResumeCounter.TableServiceClient')
    def test_update_counter(self, mock_table_service):
        # Mock request
        req = func.HttpRequest(
            method='POST',
            body=None,
            url='/api/UpdateResumeCounter',
            params={}
        )
        
        # Mock environment variables
        os.environ["COSMOS_CONNECTION_STRING"] = "mock_connection_string"
        os.environ["TABLE_NAME"] = "visitors"
        
        # Mock the table client and get_entity method
        mock_table_client = MagicMock()
        mock_table_service.from_connection_string.return_value.get_table_client.return_value = mock_table_client
        mock_table_client.get_entity.return_value = {"count": 42}
        
        # Call the function
        response = update_counter_main(req)
        
        # Check the response
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.get_body())
        self.assertEqual(response_body.get("count"), 43)  # Incremented by 1
        
        # Verify that upsert_entity was called with the right parameters
        mock_table_client.upsert_entity.assert_called_once()
        args, kwargs = mock_table_client.upsert_entity.call_args
        self.assertEqual(args[0].get("count"), 43)

    @patch('GetResumeCounter.TableServiceClient')
    def test_get_counter_not_found(self, mock_table_service):
        # Mock request
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/GetResumeCounter',
            params={}
        )
        
        # Mock environment variables
        os.environ["COSMOS_CONNECTION_STRING"] = "mock_connection_string"
        os.environ["TABLE_NAME"] = "visitors"
        
        # Mock the table client and get_entity method to raise an exception
        mock_table_client = MagicMock()
        mock_table_service.from_connection_string.return_value.get_table_client.return_value = mock_table_client
        mock_table_client.get_entity.side_effect = Exception("Entity not found")
        
        # Call the function
        response = get_counter_main(req)
        
        # Check the response
        self.assertEqual(response.status_code, 200)
        response_body = json.loads(response.get_body())
        self.assertEqual(response_body.get("count"), 0)
        
        # Verify that create_entity was called
        mock_table_client.create_entity.assert_called_once()

if __name__ == '__main__':
    unittest.main()