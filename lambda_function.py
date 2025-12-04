# lambda_function.py

import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    http_method = event['httpMethod']
    if http_method == 'GET':
        response = table.scan()
        return {"statusCode": 200, "body": json.dumps(response['Items'])}
    
    elif http_method == 'POST':
        body = json.loads(event['body'])
        table.put_item(Item=body)
        return {"statusCode": 200, "body": json.dumps({"message": "Item added"})}

    elif http_method == 'DELETE':
        body = json.loads(event['body'])
        table.delete_item(Key={"id": body['id']})
        return {"statusCode": 200, "body": json.dumps({"message": "Item deleted"})}

    return {"statusCode": 400, "body": json.dumps({"message": "Unsupported method"})}
    