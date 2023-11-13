import boto3

# first-bucket-mac

"""Boto 3 resources connect"""
s3 = boto3.resource('s3')

""" Resource helps in higher level abstraction and provides more object-oriented programming behavior. In clients,
users have to specify same thing again and again for eg:= bucket name  """

#
# """For listing all the buckets"""
# print((list(s3.buckets.all())))
# """For displaying a name"""
# print((list(s3.buckets.all()))[0].name)
#
#
# """OOP benefits of using resource"""
bucket = s3.Bucket('first-bucket-mac')
#
#
# """For uploading"""
# try:
#     bucket.upload_file(Filename="../Demo_Files/my-bucket.txt", Key="resource_file")
#     print("Resource uploaded successfully")
# except Exception as e:
#     print(f'Exception occurred {e}')
#
# """For downloading"""
# try:
#     bucket.download_file(Filename="../Demo_Files/file_downloaded", Key="resource_file")
#     print("Resource downloaded successfully")
# except Exception as e:
#     print(f'Exception occurred {e}')

"""Listing and filtering"""
print(list(bucket.objects.all()))
print(list(bucket.objects.filter(Prefix='res')))
