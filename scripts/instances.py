import sys
import boto3

from .parameters import session

def launch_PostgreDB_instance(region_name):

    resource = session.resource('ec2', region_name=region_name)

    # create a new EC2 instance
    instances = resource.create_instances(        
        ImageId='ami-0dd9f0e7df0f0a138',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='kp-ohio',
        UserData="""#!/bin/sh
sudo apt update
sudo apt install postgresql postgresql-contrib -y
sudo -u postgres psql -c "CREATE USER cloud WITH PASSWORD 'cloud';"
sudo -u postgres createdb -O cloud tasks
sed -i "59 c listen_addresses='*'" /etc/postgresql/10/main/postgresql.conf
sed -i "$ a host all all 0.0.0.0/0 trust" /etc/postgresql/10/main/pg_hba.conf
sudo ufw allow 5432/tcp
sudo systemctl restart postgresql
""",
        SecurityGroups=["DB"],
        TagSpecifications=[{
            'ResourceType' : 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Database'},
                {'Key': 'Owner', 'Value': 'Roger Pina'}
            ]
        }]
    )

def launch_OMR_instance(region_name, DB_host):

    resource = session.resource('ec2', region_name=region_name)

    instances = resource.create_instances(
        ImageId='ami-0885b1f6bd170450c',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='kp-nv',
        UserData="""#!/bin/sh
sudo apt update
cd /home/ubuntu
git clone https://github.com/raulikeda/tasks.git
sudo sed -i "83 c \\\t'HOST': '{0}'," tasks/portfolio/settings.py
cd tasks
./install.sh
sudo reboot
""".format(DB_host),
        SecurityGroups=["ORM"],
        TagSpecifications=[{
            'ResourceType' : 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'ORM'},
                {'Key': 'Owner', 'Value': 'Roger Pina'}
            ]
        }]
    )

def get_instanceId(region_name, instanceTagName):
    
    client = session.client('ec2', region_name=region_name)

    response = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name', 
                'Values': [instanceTagName]
                },
            {
                'Name': 'instance-state-name', 
                'Values': ['running']
                }
        ],  
    )

    instanceId = response['Reservations'][0]['Instances'][0]['InstanceId']

    return instanceId

def terminate_an_instance(region_name, instanceTagName):

    instanceId = get_instanceId(region_name, instanceTagName)

    client = session.client('ec2', region_name=region_name)

    client.terminate_instances(
        InstanceIds=[
            instanceId
        ]
    )