import boto3
from boto3.dynamodb.conditions import Key  

def lambda_handler(event, context):
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    nuevos_datos = event['body']['alumno_datos']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression="SET alumno_datos = :val1",
        ExpressionAttributeValues={
            ':val1': nuevos_datos
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'message': 'Alumno actualizado correctamente',
        'updated_attributes': response.get('Attributes', {})
    }
