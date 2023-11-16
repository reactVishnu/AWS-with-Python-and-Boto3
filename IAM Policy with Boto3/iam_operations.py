import boto3

iam_client = boto3.client('iam')

"""
For listing the users & groups
"""
print(iam_client.list_users()['Users'][0]['UserName'])
print(iam_client.list_groups())

"""
For creating a user and than adding to a group for following some certain steps of permissions
"""
response = iam_client.create_user(UserName='demo-user')
print(iam_client.add_user_to_group(UserName='demo-user', GroupName='full_permission'))

"""
For Deleting A User, the user must not be associated to any group before deleting.
"""
print(iam_client.remove_user_from_group(UserName='demo-user', GroupName='full_permission'))
print(iam_client.delete_user(UserName='demo-user'))

