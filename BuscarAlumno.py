import boto3
from boto3.dynamodb.conditions import Key 

def lambda_handler(event, context):

    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']


    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    item = response.get('Item')

    return {
        'statusCode': 200 if item else 404,
        'alumno': item if item else {},
        'message': 'Alumno encontrado' if item else 'Alumno no encontrado'
    }
