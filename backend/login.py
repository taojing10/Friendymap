import boto3, json, os, connectdbpw
from flask import *
from flask_pymongo import PyMongo, MongoClient
from botocore.exceptions import ClientError

app = Flask(__name__)

def get_secret():

    # Retrieve the Mongodb connection from AWS Secret Manager
    secret_name = "MongoDB_connection"
    region_name = "us-east-1"

    # Create a boto3 session and retrieve the secret value
    session = boto3.session.Session(
        aws_access_key_id=connectdbpw.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=connectdbpw.SECRET_ACCESS_KEY
    )
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = json.loads(get_secret_value_response['SecretBinary'])

    return json.loads(secret)

# Connect to the Mongodb using the MongoClient object
secrets = get_secret()
mongodb_uri = secrets['mongodb_uri']
client = MongoClient(mongodb_uri)
db = client['MongoDB_connection']
users = db['users']

def validate_password(username, password):

    # Check if the given username exists in the database and if the password is correct.
    # Return the user info if the username and password are correct, or None if not.

    user = users.find_one({'username': username})
    if not user:
        return None
    if user['password'] != password:
        return None
    return user

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request body
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the user exists in the database and validate the password
    user = validate_password(username, password)

    if not user:
        return False

    # If the user and password are correct, return a success message
    return True

