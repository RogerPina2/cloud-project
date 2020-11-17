import os
import dotenv
import boto3

dotenv.load_dotenv()

session = boto3.session.Session(
        aws_access_key_id=os.getenv("ACCESS_KEY"),
        aws_secret_access_key=os.getenv("SECRET_KEY"),
    )

def client(region_name):
    return session.client("ec2", region_name=region_name)

def resource(region_name):
    return session.resource("ec2", region_name=region_name)