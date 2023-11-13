import boto3

"""
A low-level client representing Amazon Simple Storage Service (S3)
"""
s3 = boto3.client('s3')


""" For creating a bucket """
s3.create_bucket(Bucket='dockvulner-my-second-bucket') # Going to throw an error if name is not unique
s3.create_bucket(Bucket='first-bucket-mac')


"""For deleting a bucket"""
s3.delete_bucket(Bucket="dockvulner-my-second-bucket")


"""Uploading a file to a bucket, this creates an object in S3 storage."""
s3.upload_file(Filename='../Demo_Files/my-bucket.txt', Bucket='first-bucket-mac', Key='first_file')

"""Downloading a file from a bucket"""
s3.download_file(Bucket='first-bucket-mac', Key='first_file', Filename='../Demo_Files/downloaded_file')

"""For deleting an object or deleting an uploaded file"""
s3.delete_object(Bucket='first-bucket-mac', Key='first_file')