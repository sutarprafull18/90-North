# store_document/app.py
import json
import boto3
import base64
import os

s3 = boto3.client('s3')
BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    document_base64 = event.get('document')
    document_name = event.get('document_name')

    if document_base64 is None or document_name is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing document or document_name in the request')
        }

    document_data = base64.b64decode(document_base64)

    s3.put_object(Bucket=BUCKET_NAME, Key=document_name, Body=document_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Document stored successfully')
    }
