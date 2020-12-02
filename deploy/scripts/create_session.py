import os 
import dotenv
import boto3

dotenv.load_dotenv()
session = boto3.session.Session(
        aws_access_key_id=os.getenv("ACCESS_KEY"),
        aws_secret_access_key=os.getenv("SECRET_KEY"),
    )
