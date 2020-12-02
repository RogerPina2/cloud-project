import time
import boto3

from .parameters import session

def launch_PostgreDB_instance(region_name):

    client = session.client('ec2', region_name=region_name)

    resource = session.resource('ec2', region_name=region_name)

    # create a new EC2 instance
    instance_response = resource.create_instances(        
        ImageId='ami-0dd9f0e7df0f0a138',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='kp-ohio',
        UserData="""#!/bin/sh
sudo apt update
cd /home/ubuntu
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

    instance = instance_response[0]

    instance.wait_until_running()

    response = client.describe_instance_status(InstanceIds=[instance.id])

    while (response['InstanceStatuses'][0]['InstanceStatus']['Status'] != 'ok'):
        print(response['InstanceStatuses'][0]['InstanceStatus']['Status'])
        time.sleep(20)
        response = client.describe_instance_status(InstanceIds=[instance.id])

    return print('Instance created, running and passed')


def launch_OMR_instance(region_name, DB_host):

    client = session.client('ec2', region_name=region_name)

    resource = session.resource('ec2', region_name=region_name)

    instance_response = resource.create_instances(
        ImageId='ami-0885b1f6bd170450c',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='kp-nv',
        UserData="""#!/bin/sh
sudo apt update
cd /home/ubuntu
git clone https://github.com/RogerPina2/tasks.git
sudo sed -i "84 c \\\t'HOST': '{0}'," tasks/portfolio/settings.py
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

    instance = instance_response[0]

    instance.wait_until_running()

    response = client.describe_instance_status(InstanceIds=[instance.id])

    while (response['InstanceStatuses'][0]['InstanceStatus']['Status'] != 'ok'):
        print(response['InstanceStatuses'][0]['InstanceStatus']['Status'])
        time.sleep(20)
        response = client.describe_instance_status(InstanceIds=[instance.id])

    return print('Instance created, running and passed')

def terminate_an_instance(region_name, instanceTagName):

    instanceId = get_instanceId(region_name, instanceTagName)

    resource = session.resource('ec2', region_name=region_name)
    instance = resource.Instance(instanceId)

    client = session.client('ec2', region_name=region_name)
    client.terminate_instances(
        InstanceIds=[
            instanceId
        ]
    )

    instance.wait_until_terminated()

    return print('Instance terminated')

def get_instanceId(region_name, instanceTagName):
    
    client = session.client('ec2', region_name=region_name)

    Filters=[
        {
            'Name': 'tag:Name', 
            'Values': [instanceTagName]
            },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
            }
    ]

    response = client.describe_instances(Filters=Filters)

    while(response['Reservations'] == []):
        time.sleep(10)
        response = client.describe_instances(Filters=Filters)

    instanceId = response['Reservations'][0]['Instances'][0]['InstanceId']

    return instanceId