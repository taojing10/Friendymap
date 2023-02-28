from flask import Flask,render_template
import boto3
from botocore.exceptions import ClientError
import json
import pymongo
import certifi
import data.mongo_setup as mongo_setup
import connectdbpw

app = Flask(__name__)

AWS_ACCESS_KEY = connectdbpw.AWS_ACCESS_KEY_ID
AWS_SECRET_KEY = connectdbpw.SECRET_ACCESS_KEY

#amazon secretmanager code
Secret_Name = "MongoDB_connection"
Region_Name = "us-east-1"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
    )
get_secret_value_response = client.get_secret_value(
    SecretId=secret_name
    )

secret_jason = get_secret_value_response['MongoDB_connection']

secret = json.loads(secret_jason)

connection_string = secret["MongoDB_connection"]

try: 
  client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
except Exception:
  print("error:"+Exception)

myDb = client["Friendymap_db"]


def main():
   moongo_setup.global_init()


if __name__ == '__main__': 
     app.run(debug=True) 
   