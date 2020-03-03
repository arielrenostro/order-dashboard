import datetime
import json
import os
from uuid import uuid4

import boto3


class RequestException(Exception):

    def __init__(self, message):
        self.message = message



def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.getenv('ORDER_TABLE', 'order'))

        body = json.loads(event['body'])

        items = []
        for item in body['items']:
            quantity = item.get('quantity')
            if not quantity:
                raise RequestException("Quantidade de um item não foi informada!")

            unity = item.get('unity')
            if not unity:
                raise RequestException("Unidade de um item não foi informada!")

            description = item.get('description')
            if not description:
                raise RequestException("Descrição de um item não foi informada!")

            items.append(
                {
                    'quantity': quantity,
                    'unity': unity,
                    'description': description,
                }
            )

        company = body.get('company')
        if not company:
            raise RequestException('Empresa não informada!')

        client = body.get('client')
        if not client:
            raise RequestException('Cliente não informado!')

        exp_time = body.get('expTime')
        if not exp_time:
            raise RequestException('Prazo não informado!')

        table.put_item(
            Item={
                'id': str(uuid4()),
                'company': company,
                'client': client,
                'expTime': exp_time,
                'status': 'PENDING',
                'items': items,
            },
        )

        return {
            'statusCode': 201,
            'body': json.dumps({
                'ok': True
            }),
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
