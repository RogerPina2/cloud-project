from .scripts.parameters import north_virginia, ohio
from .scripts.get_host import get_DB_host

from .scripts.KeyPair import create_KeyPair
from .scripts.SecurityGroup import create_SecurityGroup, add_IpPermission
from .scripts.Instances import launch_PostgreDB_instance, launch_OMR_instance, terminate_an_instance
from .scripts.Image import create_AMI_from_instance
from .scripts.LoadBalancer import create_LB_to_ORM, get_url
from .scripts.LaunchConfiguration import create_LaunchConfiguration
from .scripts.AutoScaling import create_AutoScaling

def create():
    """
        Create all.
    """
    # === DATABASE (ohio) ===

    # Create keypair
    create_KeyPair(ohio, 'kp-ohio')

    # Create Security Group
    create_SecurityGroup(
        ohio,
        'DB',
        'Database Security Group',
        Tags={'Name':'Database', 'Owner':'Roger Pina'}
    )

    # Add Ip permission on SG
    # ssh connection
    add_IpPermission(ohio, 'DB', 22)
    # Pg connection
    add_IpPermission(ohio, 'DB', 5432)

    # Launch an instance in ohi and install Pg
    launch_PostgreDB_instance(ohio)

    # === ORM (N. Virgínia) ===

    # Create keypair
    create_KeyPair(north_virginia, 'kp-nv')

    # Create Security Group
    create_SecurityGroup(
        north_virginia,
        'ORM',
        'Database Security Group', 
        Tags={'Name':'ORM', 'Owner':'Roger Pina'}
    )

    # Add Ip permission on SG
    add_IpPermission(north_virginia, 'ORM', 22) # ssh connection
    add_IpPermission(north_virginia, 'ORM', 8080) # http connection
    add_IpPermission(north_virginia, 'ORM', 80) # http connection for LB

    # Get the DB_host
    db_host = get_DB_host(ohio)

    # Launch an instance in N.Virgínia and install de OMR Django (Raul's git)
    launch_OMR_instance(north_virginia, db_host)

    # Create an instance Image
    create_AMI_from_instance(north_virginia, 'ORM', 'ORM_AMI')

    # Terminate the instance
    terminate_an_instance(north_virginia, 'ORM')

    # Create a LoadBalancer for ORM instances
    create_LB_to_ORM(north_virginia, 'LB')

    # Create a Launch Configuration for Auto Scaling
    create_LaunchConfiguration(north_virginia, 'LC_ORM', 'ORM_AMI', 'kp-nv', 'ORM')

    # Create an Auto Scaling using the Launch COnfiguration and LoadBalancer created
    create_AutoScaling(north_virginia, 'AS', 'LC_ORM')

    get_url(north_virginia, 'LB')
