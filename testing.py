import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='no_name_123')

