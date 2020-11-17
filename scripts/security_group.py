from .parameters import session

def create_security_group(region_name, GroupName, Description, Tags={'Name':'', 'Owner':'Roger Pina'}):

    client = session.client('ec2', region_name=region_name)

    client.create_security_group(
        GroupName=GroupName,
        Description=Description,
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [
                    {'Key' : 'Name', 'Value' : Tags['Name']},
                    {'Key' : 'Owner', 'Value' : Tags['Owner']}
                ]
            }
        ]
    )

def add_IpPermission(region_name, GroupName, Port, CidrIp='0.0.0.0/0', Description=''):

    client = session.client('ec2', region_name=region_name)

    client.authorize_security_group_ingress(
        GroupName=GroupName,
        IpPermissions=[
            {
                'FromPort': Port,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': CidrIp,
                        'Description': Description,
                    },
                ],
                'ToPort': Port,
            },
        ],
    )