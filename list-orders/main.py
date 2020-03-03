import decimal
import json
import os

import boto3
from boto3.dynamodb.conditions import Attr


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


class RequestException(Exception):

    def __init__(self, message):
        self.message = message


def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.getenv('ORDER_TABLE', 'order'))

        parameters = event.get('queryStringParameters', {})
        if not parameters:
            parameters = {}

        limit = 1000
        limit_parameter = limit

        args = {}
        if 'limit' in parameters:
            limit_parameter = int(parameters['limit'])
            if limit_parameter > 1000:
                limit = limit_parameter
        args['Limit'] = limit

        if parameters.get('onlyPending', 'true').lower() == 'true':
            args['FilterExpression'] = Attr('status').eq('PENDING')

        query = table.scan(**args)

        items = []
        for item in query['Items']:
            item['expTime'] = int(item['expTime'])
            items.append({
                **item
            })

        items.sort(key=lambda x: x['expTime'])

        limit = limit_parameter if limit_parameter < len(items) else len(items)
        items = items[:limit]

        return {
            'statusCode': 200,
            'body': json.dumps(items, cls=DecimalEncoder),
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
    except RequestException as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'ok': False,
                'message': e.message
            }),
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
