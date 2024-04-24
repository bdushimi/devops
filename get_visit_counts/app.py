import json
import boto3


def lambda_handler(event, context):
    body = json.loads(event['body'])
    appName = body["app-name"]
    visit_count: int = 0

    # Create a DynamoDB Client & Connection
    dynamodb = boto3.resource('dynamodb')
    table_name = "apps-visit-counts"
    table = dynamodb.Table(table_name)

    # Get the apps visit count from dynamodb
    response = table.get_item(Key={"app-name": appName})

    if "Item" in response:
        if "count" in response["Item"]:
            visit_count = response["Item"]["count"]

    # Increment the number of visits
    visit_count += 1

    # Update the number of visits in dynamodb
    table.put_item(Item={"app-name": appName, "count": visit_count})

    response_data = {
        'app-name': f"{appName}",
        'visitCount': f"{visit_count}"
    }

    return {
        'statusCode': 200,
        "body": json.dumps(response_data),
    }
