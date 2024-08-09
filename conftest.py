import boto3
import os
import pytest
from moto import mock_dynamodb2


os.environ['DYNAMODB_TABLE'] = 'apps-visit-counts'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def dynamodb_client(aws_credentials):
    """DynamoDB mock client."""
    with mock_dynamodb2():
        conn = boto3.client("dynamodb", region_name="us-east-1")
        yield conn


@pytest.fixture(scope='function')
def dynamodb_table(dynamodb):
    """Create a DynamoDB surveys table fixture."""
    table = dynamodb.create_table(
        TableName='apps-visit-counts',
        KeySchema=[
            {
                'AttributeName': 'app-name',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'app-name',
                'AttributeType': 'S'
            },
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    table.meta.client.get_waiter('table_exists').wait(
        TableName='apps-visit-counts')
    yield
