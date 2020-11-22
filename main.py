import os
import dotenv
import boto3

from scripts.parameters import NVirginia, Ohio
from scripts.KeyPair import create_keypair, delete_keypair
from scripts.SecurityGroup import create_SecurityGroup, delete_SecurityGroup, add_IpPermission
from scripts.instances import launch_PostgreDB_instance, launch_OMR_instance, terminate_an_instance, get_instanceId
from scripts.get_host import get_DB_host
from scripts.AMI import create_AMI_from_instance, delete_AMI
from scripts.LoadBalancer import create_LB_to_ORM, delete_LB_to_ORM
from scripts.LaunchConfiguration import create_LaunchConfiguration, delete_LaunchConfiguration
from scripts.AutoScaling import create_AutoScaling, delete_AutoScaling

from scripts.parameters import session

def create_from_0():

    # === DATABASE (Ohio) ===
    
    # Create keypair
    create_keypair(Ohio, 'kp-ohio')
    
    # Create Security Group
    create_SecurityGroup(
        Ohio,
        'DB',
        'Database Security Group', 
        Tags={'Name':'Database', 'Owner':'Roger Pina'}
    )

    # Add Ip permission on SG
    add_IpPermission(Ohio, 'DB', 22) # ssh connection
    add_IpPermission(Ohio, 'DB', 5432) # Pg connection
    
    # Launch an instance in Ohio and install Pg
    launch_PostgreDB_instance(Ohio)

    # === ORM (N. Virgínia) ===

    # Create keypair
    create_keypair(NVirginia, 'kp-nv')

    # Create Security Group
    create_SecurityGroup(
        NVirginia,
        'ORM',
        'Database Security Group', 
        Tags={'Name':'ORM', 'Owner':'Roger Pina'}
    )

    # Add Ip permission on SG
    add_IpPermission(NVirginia, 'ORM', 22) # ssh connection
    add_IpPermission(NVirginia, 'ORM', 8080) # http connection
    add_IpPermission(NVirginia, 'ORM', 80) # http connection for LB

    # Get the DB_host 
    DB_host = get_DB_host(Ohio)    

    # Launch an instance in N.Virgínia and install de OMR Django (Raul's git)
    launch_OMR_instance(NVirginia, DB_host)

    # Create an instance Image 
    create_AMI_from_instance(NVirginia, 'ORM', 'ORM_AMI')

    # Terminate the instance
    terminate_an_instance(NVirginia, 'ORM')

    # Create a LoadBalancer for ORM instances
    create_LB_to_ORM(NVirginia, 'LB')

    # Create a Launch Configuration for Auto Scaling
    create_LaunchConfiguration(NVirginia, 'LC_ORM', 'ORM_AMI', 'kp-nv', 'ORM')

    # Create an Auto Scaling using the Launch COnfiguration and LoadBalancer created
    create_AutoScaling(NVirginia, 'AS', 'LC_ORM')

    return

def delete_all():

    delete_AutoScaling(NVirginia, 'AS')
    delete_LaunchConfiguration(NVirginia, 'LC_ORM')
    delete_LB_to_ORM(NVirginia, 'LB')
    delete_AMI(NVirginia, 'ORM_AMI')
    # terminate_an_instance(NVirginia, 'ORM')
    delete_SecurityGroup(NVirginia, 'ORM')
    delete_keypair(NVirginia, 'kp-nv')

    terminate_an_instance(Ohio, 'Database')
    delete_SecurityGroup(Ohio, 'DB')
    delete_keypair(Ohio, 'kp-ohio')
    
    return 

def main():

    # create_from_0()
    # delete_all()

    return

if __name__ == '__main__':
    main()
    