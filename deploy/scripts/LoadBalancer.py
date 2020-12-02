from .parameters import session

from .SecurityGroup import get_SG_id_from_GroupName

def create_LB_to_ORM(region_name, LoadBalancerName):

    SG_id = get_SG_id_from_GroupName(region_name, 'ORM')

    client = session.client('elb', region_name=region_name)

    client.create_load_balancer(
        LoadBalancerName=LoadBalancerName,
        Listeners=[
            {
                'Protocol':'HTTP',
                'LoadBalancerPort':80,
                'InstancePort':8080
            }
        ],
        AvailabilityZones=[
            'us-east-1a',
            'us-east-1b',
            'us-east-1c',
            'us-east-1d',
            'us-east-1e',
            'us-east-1f',
        ],
        SecurityGroups=[
            SG_id,
        ],
        Tags=[
            {'Key': 'Name', 'Value': 'ORM'},
            {'Key': 'Owner', 'Value': 'Roger Pina'}
        ]
    )

    print('LoadBalancer {} created'.format(LoadBalancerName))

def delete_LB_to_ORM(region_name, LoadBalancerName):

    client = session.client('elb', region_name=region_name)

    client.delete_load_balancer(
        LoadBalancerName=LoadBalancerName
    )

    print('LoadBalancer {} deleted'.format(LoadBalancerName))


def get_url(region_name, LoadBalancerName):

    client = session.client('elb', region_name=region_name)

    response = client.describe_load_balancers(
        LoadBalancerNames=[
            LoadBalancerName,
        ],
    )

    dns = response['LoadBalancerDescriptions'][0]['DNSName']

    outfile = open('url', 'w')
    outfile.write(dns)
 