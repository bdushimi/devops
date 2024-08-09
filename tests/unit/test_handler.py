import json
import unittest
import pytest
from unittest import mock
import boto3
# from moto import mock_dynamodb2


# Setting the default AWS region environment variable required by the Python SDK boto3
with mock.patch.dict('os.environ', {'AWS_REGION': 'us-east-1'}):
    from get_visit_counts.app import lambda_handler


class TestUpdateVisitCountsLambdaFunction:

    # Test to see if we correctly handle the situation when input is missing
    def test_missing_body(self):
        # Mock the event
        event = {}
        response = lambda_handler(event, None)
        assert response["statusCode"] == 500
        assert response["body"] == {'event': event, 'exception': "'body'"}

    def test_missing_data(self):
        # Mock the event
        event = {
            "body": json.dumps({"app-name": ""})
        }
        response = lambda_handler(event, None)
        assert response["statusCode"] == 500
        assert response["body"] == {'event': event,
                                    'exception': 'app-name is required'}

    def test_invalid_data(self):
        # Mock the event
        event = {
            "body": json.dumps({"apps-names": ""})
        }
        response = lambda_handler(event, None)
        assert response["statusCode"] == 500
        assert response["body"] == {'event': event,
                                    'exception': "'app-name'"}
