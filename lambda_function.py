import json

def lambda_handler(event, context):
    print(json.dumps(event, indent=4))  # Print the full event object


import json
import boto3
import string
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ShortLinks')

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  # Debug log to check structure

    # Use `.get()` to safely extract the 'body'
    body_str = event.get('body', '{}')  # Defaults to empty JSON if missing
    try:
        body = json.loads(body_str) if isinstance(body_str, str) else body_str
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON format"})
        }

    if 'url' in body:
        short_code = generate_code()
        table.put_item(Item={'shortCode': short_code, 'url': body['url']})
        return {
            "statusCode": 200,
            "body": json.dumps({"shortUrl": f"https://your-api-url/{short_code}"})
        }
    
    elif 'shortCode' in body:
        response = table.get_item(Key={'shortCode': body['shortCode']})
        if 'Item' in response:
            return {
                "statusCode": 200,
                "body": json.dumps({"url": response['Item']['url']})
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Short code not found"})
            }

    return {
        "statusCode": 400,
        "body": json.dumps({"error": "Invalid request format"})
    }
