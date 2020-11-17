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
git clone https://github.com/RogerPina2/cloud-project.git
cd cloud-project
sed -i 's/node1/{DB_host}/' /portfolio/settings.py
./install.sh
sudo reboot
""",
        SecurityGroups=["ORM"],
        TagSpecifications=[{
            'ResourceType' : 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'ORM'},
                {'Key': 'Owner', 'Value': 'Roger Pina'}
            ]
        }]
    )