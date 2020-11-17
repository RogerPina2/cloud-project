import boto3

from .parameters import session

def get_DB_host(region_name):
    
    client = session.client('ec2', region_name=region_name)

    response = client.describe_instances(
        Filters=[
            {
                'Name':'tag:Name',
                'Values':[
                    'Database'
                ]
            }
        ]
    )

    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']

    return public_ip