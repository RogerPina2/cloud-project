from .parameters import session

from .AMI import get_AMI_id_from_AMI_name
from .SecurityGroup import get_SG_id_from_GroupName

def create_LaunchConfiguration(region_name, LaunchConfigurationName, AMI_name, keypair, SG_GroupName):
    
    AMI_id = get_AMI_id_from_AMI_name(region_name, AMI_name)
    SG_id = get_SG_id_from_GroupName(region_name, SG_GroupName)

    client = session.client('autoscaling', region_name=region_name)

    client.create_launch_configuration(
        LaunchConfigurationName=LaunchConfigurationName,
        ImageId=AMI_id,
        KeyName=keypair,
        SecurityGroups=[
            SG_id
        ],
        InstanceType='t2.micro'
    )

def delete_LaunchConfiguration(region_name, LaunchConfigurationName):

    client = session.client('autoscaling', region_name=region_name)

    client.delete_launch_configuration(
        LaunchConfigurationName=LaunchConfigurationName
    )