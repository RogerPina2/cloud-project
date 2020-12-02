import time

from .parameters import session

def create_AutoScaling(region_name, AutoScalingGroupName, LaunchConfigurationName):

    client = session.client('autoscaling', region_name=region_name)

    client.create_auto_scaling_group(
        AutoScalingGroupName=AutoScalingGroupName,
        LaunchConfigurationName=LaunchConfigurationName,
        MinSize=1,
        MaxSize=3,
        DesiredCapacity=1,
        AvailabilityZones=[
            'us-east-1a', 
            'us-east-1b', 
            'us-east-1c',
            'us-east-1d', 
            'us-east-1e', 
            'us-east-1f'
        ],
        LoadBalancerNames=[
            'LB',
        ],
        CapacityRebalance=True
    )

    time.sleep(30)

    client.update_auto_scaling_group(
        AutoScalingGroupName=AutoScalingGroupName,
        DesiredCapacity=2,
        MinSize=2
    )

    print('Auto Scalling {} created'.format(AutoScalingGroupName))


def delete_AutoScaling(region_name, AutoScalingGroupName):

    client = session.client('autoscaling', region_name=region_name)

    client.delete_auto_scaling_group(
        AutoScalingGroupName=AutoScalingGroupName,
        ForceDelete=True
    )

    print('Auto Scalling {} deleted'.format(AutoScalingGroupName))
    