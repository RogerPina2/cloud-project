from .parameters import session

def create_SecurityGroup(region_name, GroupName, Description, Tags={'Name':'', 'Owner':'Roger Pina'}):

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

def delete_SecurityGroup(region_name, GroupName):

    client = session.client('ec2', region_name=region_name)

    client.delete_security_group(
        GroupName=GroupName
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

def get_SG_id_from_GroupName(region_name, GroupName):
    
    client = session.client('ec2', region_name=region_name)

    response = client.describe_security_groups(
        GroupNames=[
            GroupName
        ],
    )

    groupId = response['SecurityGroups'][0]['GroupId']

    return groupId
