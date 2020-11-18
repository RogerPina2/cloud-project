from .parameters import session

from .instances import get_instanceId

def create_AMI_from_instance(region_name, instanceTagName, AMI_name):

    instanceId = get_instanceId(region_name, instanceTagName)

    client = session.client('ec2', region_name=region_name)

    client.create_image(
        Name=AMI_name,
        InstanceId=instanceId
    )



