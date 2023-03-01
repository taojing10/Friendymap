from flask import Flask, request, url_for, render_template, redirect
from botocore.exceptions import ClientError
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from pymongo import MongoClient
from wtforms.validators import input_required, length, ValidationError
import boto3
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def get_secret():

    secret_name = "MongoDB_connection"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return secret


secrets = get_secret()
mongodb_uri = secrets['mongodb_uri']
client = MongoClient(mongodb_uri)
db = client['database']
users = db["users"]


def validate_username(username):
    user = users.find_one({'username': username})
    if not user:
        return not user

#class RegisterForm(FlaskForm):
    #username = StringField(validators=[input_required(), length(min=4, max=20)], render_kw={"placeholder": "Username"})
    #password = PasswordField(validators=[input_required(), length(min=4, max=20)], render_kw={"placeholder": "Password"})
    #submit = SubmitField("Register")


@app.route('/register', methods=[ 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username' : request.form['username']})

        if user:
            raise ValueError("Account already exists !")
        else:
            user = {'username': username, 'password': password}
            users.insert_one(user)
            return redirect(url_for('success'))


if __name__ == '__main__':
    app.run(debug=False)