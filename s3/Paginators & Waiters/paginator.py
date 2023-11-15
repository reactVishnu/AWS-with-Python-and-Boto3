import boto3

"""S3 conn"""
s3 = boto3.client('s3')


"""
A paginator is a convenient way to iterate over paginated results from AWS operations,
handling the underlying mechanics of making multiple requests to retrieve all the results.
list_objects_v2 operation, which is used to list objects in an S3 bucket.
The v2 in the operation name indicates that this is the second version of the operation.
"""
paginator = s3.get_paginator('list_objects_v2')

"""
paginate: This method is called on the paginator object to initiate the paginated operation. 
It takes various parameters depending on the specific AWS service operation being paginated.
"""
results = paginator.paginate(Bucket="first-bucket-mac")
print(len(list(results)))
for item in results:
    print(item['Contents'][0]['Key'])

