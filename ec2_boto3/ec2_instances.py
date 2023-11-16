import boto3
"""
In free tier, we have 750 hours per month, for one year!
"""


"""
Region for the instance
"""
region = 'ap-south-1'

"""RESOURCE CONN"""
ec2 = boto3.resource('ec2', region_name=region)

"""
INSTANCE CREATION - IMAGE ID(SEARCH IN WEB CONSOLE)
"""
instance = ec2.create_instances(MaxCount=1,
                                MinCount=1,
                                InstanceType='t2.nano',
                                ImageId='ami-0850beb48a8b4bb46'  # Lookup in console
                                )
print(instance)

"""
FOR LISTING ALL THE INSTANCES
"""
print(list(ec2.instances.all()))

"""
FOR GETTING ALL THE INFORMATION ABOUT AN INSTANCE
"""
client = boto3.client('ec2', region_name=region)
description = client.describe_instances(InstanceIds=['i-081cfff521b6ce0e8'])

"""
Status of a instance
"""
print(description['Reservations'][0]['Instances'][0]['State'])

"""
For stopping a instance
"""
client.stop_instances(InstanceIds=['i-081cfff521b6ce0e8'])

"""Status"""
print(description['Reservations'][0]['Instances'][0]['State'])

"""
For starting an instance.
"""
client.start_instances(InstanceIds=['i-081cfff521b6ce0e8'])
print(description['Reservations'][0]['Instances'][0]['State'])

"""
For terminating an instance
"""
client.terminate_instances(InstanceIds=['i-081cfff521b6ce0e8'])
print(description['Reservations'][0]['Instances'][0]['State'])
