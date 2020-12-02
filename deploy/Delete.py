from .scripts.parameters import north_virginia, ohio
from .scripts.KeyPair import delete_KeyPair
from .scripts.SecurityGroup import delete_SecurityGroup
from .scripts.Instances import terminate_an_instance
from .scripts.Image import delete_AMI
from .scripts.LoadBalancer import delete_LB_to_ORM
from .scripts.LaunchConfiguration import delete_LaunchConfiguration
from .scripts.AutoScaling import delete_AutoScaling

def delete():
    """
        Delete all.
    """
    delete_AutoScaling(north_virginia, 'AS')
    delete_LaunchConfiguration(north_virginia, 'LC_ORM')
    delete_LB_to_ORM(north_virginia, 'LB')
    delete_AMI(north_virginia, 'ORM_AMI')
    # terminate_an_instance(north_virginia, 'ORM')
    delete_SecurityGroup(north_virginia, 'ORM')
    delete_KeyPair(north_virginia, 'kp-nv')

    terminate_an_instance(ohio, 'Database')
    delete_SecurityGroup(ohio, 'DB')
    delete_KeyPair(ohio, 'kp-ohio')
