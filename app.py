import json

def handler(event, context):
    # print(event['body'])
    body = json.loads(event['body'])
    print(body)
    return {'body': f'Hello, {body["user"]}!', 'statusCode': 200}
