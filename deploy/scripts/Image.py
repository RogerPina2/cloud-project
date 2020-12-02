import time

from .parameters import session

from .Instances import get_instanceId

def create_AMI_from_instance(region_name, instanceTagName, AMI_name):

    client = session.client('ec2', region_name=region_name)
    resource = session.resource('ec2', region_name=region_name)

    instanceId = get_instanceId(region_name, instanceTagName)

    image_response = client.create_image(
        Name=AMI_name,
        InstanceId=instanceId
    )

    imageId = image_response['ImageId']
    image = resource.Image(imageId)
    
    print('Waiting Image state return available')

    while (image.state != 'available'):
        image = resource.Image(imageId)
        print('image state: {}'.format(image.state))
        time.sleep(30)

    return print('Image exists and is available')

def delete_AMI(region_name, AMI_name):

    AMI_id = get_AMI_id_from_AMI_name(region_name, AMI_name)

    client = session.client('ec2', region_name=region_name)

    client.deregister_image(
        ImageId=AMI_id
    )

    print('image deleted')

    time.sleep(120)

def get_AMI_id_from_AMI_name(region_name, AMI_name):

    client = session.client('ec2', region_name=region_name)

    response = client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    AMI_name,
                ]
            },
        ],
    )

    AMI_id = response['Images'][0]['ImageId']

    return AMI_id


