import boto3 as aws

s3 = aws.client('s3')
# s3.create_bucket(Bucket='dockvulner-my-first-bucket') # Gonna throw error if name is not unique

# with open('my-bucket.txt', 'w') as file:
#     file.write('My bucket upload')

# s3.upload_file(Filename='my-bucket.txt', Bucket='dockvulner-my-first-bucket', Key='first_file')
# s3.download_file(Bucket='dockvulner-my-first-bucket', Key='first_file', Filename='downloaded_file')
