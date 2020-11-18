import os
import dotenv
import boto3

from scripts.parameters import NVirginia, Ohio
from scripts.keypair import create_keypair, delete_keypair
from scripts.security_group import create_security_group, add_IpPermission
from scripts.instances import launch_PostgreDB_instance, launch_OMR_instance, terminate_an_instance
from scripts.get_host import get_DB_host
from scripts.AMI import create_AMI_from_instance

def main():
    # create_keypair(Ohio, 'kp-ohio')
    # create_keypair(NVirginia, 'kp-nv')
    # delete_keypair(Ohio, 'kp-ohio')
    # delete_keypair(NVirginia, 'kp-nv')

    # create_security_group(
    #     Ohio,
    #     'DB',
    #     'Database Security Group', 
    #     Tags={'Name':'Database', 'Owner':'Roger Pina'}
    # )

    # add_IpPermission(Ohio, 'DB', 22)
    # add_IpPermission(Ohio, 'DB', 5432)

    # create_security_group(
    #     NVirginia,
    #     'ORM',
    #     'Database Security Group', 
    #     Tags={'Name':'ORM', 'Owner':'Roger Pina'}
    # )

    # add_IpPermission(NVirginia, 'ORM', 22)
    # add_IpPermission(NVirginia, 'ORM', 8080)

    # launch_PostgreDB_instance(Ohio)
    # DB_host = get_DB_host(Ohio)
    # launch_OMR_instance(NVirginia, DB_host)
    # create_AMI_from_instance(NVirginia, 'ORM', 'ORM_AMI')
    # terminate_an_instance(NVirginia, 'ORM')

if __name__ == '__main__':
    main()
    