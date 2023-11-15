import boto3

s3 = boto3.client('s3')

bucket_name = "no-name-123"
waiter = s3.get_waiter('bucket_exists')
wait_config = {"Delay": 10, "MaxAttempts": 40}

try:
    print(f'Waiting for bucket: {bucket_name}')
    waiter.wait(Bucket=bucket_name, WaiterConfig=wait_config)
    print('The Bucket has been made')
except Exception as e:
    print(e)

"""
This script is a utility for ensuring that a specific S3 bucket exists before proceeding with further 
operations.
It incorporates a waiter mechanism to pause and check for the bucket's existence at intervals,
providing a robust way to handle the asynchronous nature of resource creation in AWS.
"""
