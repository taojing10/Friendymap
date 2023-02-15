import boto3, json
from flask import *
from flask_pymongo import PyMongo
from botocore.exceptions import ClientError
# todo:getting mongodb auth

app = Flask(__name__)
# connect to secret manager resource
client = boto3.client("secretsmanager")

# retrieve secret value
def get_secret():

    secret_name = "MongoDB_connection"
    region_name = "us-east-1"

    # create a secret manager client
    client = boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

app.config["MONGO_URI"] = f"mongodb+srv://{secret_value[testuser]}:{secret_value[testpw]}@{secret_value[192.168.50.1]}/{secret_value[MongoDB]}?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def index():
    return ("home page")

#create a collection in Mongodb to store user information
users_collection = mongo.db.users

@app.route("/login", methods = ["POST"])
def login():
    #get user info from the form
    username = request.form["username"]
    password = request.form["password"]

    #check if both username and password r correct
    existing_user = users_collection.find_one({"username": username, "password": password})
    if not existing_user:
        return ("Incorrect username or password")

    #store the user ID in the session to keep the user logged in
    session["user"] = user

    return ("Successfully logged in")

