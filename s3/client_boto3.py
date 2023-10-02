import boto3 as aws

s3 = aws.client('s3')
s3.create_bucket(Bucket='my-first-bucket') # Gonna throw error if name is not unique