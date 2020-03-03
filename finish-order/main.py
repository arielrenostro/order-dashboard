import json
import os

import boto3


class RequestException(Exception):

    def __init__(self, message):
        self.message = message


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.getenv('ORDER_TABLE', 'order'))

        body = json.loads(event['body']) if 'body' in event and event['body'] else {}

        id_ = body.get('id')
        if not id_:
            raise RequestException('ID não informado!')

        response = table.update_item(
            Key={
                'id': id_,
            },
            UpdateExpression="set #status=:r",
            ExpressionAttributeValues={
                ':r': 'FINISHED',
            },
            ExpressionAttributeNames={
                "#status": "status"
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'ok': 'true',
                **response
            })
        }
    except RequestException as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'ok': False,
                'message': e.message
            })
        }
