import boto3

"""Connection"""
client = boto3.client('s3')

"""Create a url for the object to be available in public network"""
url = client.generate_presigned_url(ClientMethod='get_object', Params={
    'Bucket': 'first-bucket-mac',
    'Key': 'resource_file'
})

print(url)

"""For deleting a bucket, it should be empty , means there are no objects there """
"""For deleting all the object"""

s3 = boto3.resource('s3')
bucket = s3.Bucket('first-bucket-mac')
print(bucket.objects.all().delete())
