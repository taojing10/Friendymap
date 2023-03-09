from flask import Flask, request, jsonify
from flask_pymongo import MongoClient
import db_connection

app = Flask('login')

mongo_client = db_connection.get_mongo_client()
db = mongo_client.Friendymap_db
users = db.user

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
