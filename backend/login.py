import json
from flask import Flask, request, jsonify
from flask_pymongo import MongoClient
import connectdbpw
import boto3
import certifi
import mongo_setup

app = Flask('login')

AWS_ACCESS_KEY = connectdbpw.AWS_ACCESS_KEY_ID
AWS_SECRET_KEY = connectdbpw.SECRET_ACCESS_KEY

# Retrieve the MongoDB connection from AWS Secrets Manager
secret_name = "MongoDB_connection"
region_name = "us-east-1"

# Create a boto3 session and retrieve the secret value
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)
get_secret_value_response = client.get_secret_value(SecretId=secret_name)

if 'SecretString' in get_secret_value_response:
    secret = get_secret_value_response['SecretString']
else:
    secret = json.loads(get_secret_value_response['SecretBinary'])

secrets = json.loads(secret)

# Set up the MongoDB connection
connection_string = secrets['connection_string']
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client['Friendymap_db']
users = db['User']

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
        return jsonify({'success': False})

    # If the user and password are correct, return a success message
    return jsonify({'success': True})
