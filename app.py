from flask import Flask,render_template
import boto3
from botocore.exceptions import ClientError
import json
import pymongo 
from flask_pymongo import MongoClient
import certifi
import data.mongo_setup as mongo_setup
import connectdbpw


app = Flask(__name__)

#use AWS secretmanager to access MongoDB database
secret_name = "MongoDB_connection"
region_name = "us-east-1"

session = boto3.session.Session(
  aws_access_key_id=connectdbpw.aws_access_key_id,
  aws_secret_access_key=connectdbpw.aws_secret_access_key
)

client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)
try:
  # call secret manager
  get_secret_value_response = client.get_secret_value(SecretId=secret_name)
except ClientError as error:
  print(error)
  
secret = json.loads(get_secret_value_response['SecretString']) 

connection_string = secret['connection_string']

try: 
  # print("connection_string", connection_string)
  # print(type(connection_string))
  # print (connection_string == "mongodb+srv://testuser:testpw@cluster0.gv9cbee.mongodb.net/?retryWrites=true&w=majority")
  client = MongoClient(connection_string, tlsCAFile=certifi.where())
  print(client.list_database_names())
except Exception as e: print(e)



# def main():
#   mongo_setup.global_init()

# if __name__ == '__main__': 
#   app.run(debug=True) 
   