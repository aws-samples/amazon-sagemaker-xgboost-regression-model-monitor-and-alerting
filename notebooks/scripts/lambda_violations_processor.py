"""
Copyright 2021 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket name and the object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    # Process only constraint violations file
    if key.endswith('constraint_violations.json'):
        print('Triggered on constraint violations file {}'.format(key))
        try:
            # Get the object from S3 and read the violations data
            response = s3.get_object(Bucket=bucket, Key=key)
            violations = json.loads(response['Body'].read().decode('utf-8'))
            print(violations)
            # TODO: Write your alerting logic here
            return
        except Exception as e:
            print(e)
            raise e
    else:
        print('Processing ignored. Triggered on file {}'.format(key))
        return
