from flask import Flask, render_template, request
from botocore.exceptions import ClientError
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


@app.route('/register', methods=[ 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        account = username.find_one({'username' : request.form['username']})

        if account:
            raise ValueError("Account already exists !")
        elif not username:
            raise NameError("Username is required.")
        elif not password:
            raise ValueError("Password is required.")
        elif not email:
            raise ValueError("Email is required.")


    return render_template('/', form=form)

if __name__ == '__main__':
    app.run(debug=False)