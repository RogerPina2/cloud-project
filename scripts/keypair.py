# https://blog.ipswitch.com/how-to-create-an-ec2-instance-with-python
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-key-pairs.html

import os

from .parameters import session

def create_KeyPair(region_name, keypair_name):
    client = session.client('ec2', region_name=region_name)

    file = 'ppk/' + keypair_name + '.ppk'

    try:
        # create a file to store the key locally
        outfile = open(file, 'w')

        # call the boto ec2 function to create a key pair
        key_pair = client.create_key_pair(KeyName=keypair_name)

        # capture the key and store it in a file
        KeyPairOut = str(key_pair['KeyMaterial'])
            #print(KeyPairOut)
        outfile.write(KeyPairOut)

    except Exception as error:
        print(error)

def delete_KeyPair(region_name, keypair_name):

    client = session.client('ec2', region_name=region_name)

    # call the boto ec2 function to delete a key pair
    client.delete_key_pair(
        KeyName=keypair_name
    )

    file = 'ppk/' + keypair_name + '.ppk'

    os.remove(file)        

