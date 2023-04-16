from flask import Flask, redirect, request, jsonify, session
from flask_session import Session
from flask_pymongo import MongoClient
import db_connection
import bcrypt

app = Flask('login')

# Configuring Session in Flask
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

mongo_client = db_connection.get_mongo_client()
db = mongo_client.Friendymap_db
users = db.user
events = db.event

def validate_password(username, password):
    # Check if the given username exists in the database and if the password is correct.
    # Return the user info if the username and password are correct, or None if not.
    user = users.find_one({'username': username})
    if not user:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
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
    # if the user and password are correct, add user in session
    session["username"] = username
    # If the user and password are correct, return a success message
    return jsonify({'success': True})

@app.route('/register', methods=['POST'])
def register():
    # Get the new user's info from website
    username = request.json.get('username')
    password = request.json.get('password')

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Check if the username already exists in the db
    existing_user = users.find_one({'username': username})

    if existing_user:
        # If the username is already taken
        return jsonify({'success': False, 'message': 'Username already exists'})

    # If the username is not taken, add the new user into the database
    new_user = {'username': username, 'password': hashed_password}
    users.insert_one(new_user)

    return jsonify({'success': True, 'message': 'User registered successfully'})

# Route to add a new event
@app.route('/event', methods=['POST'])
def add_event():
    username = session['username']  # check if user is logged in because only logged-in users can create events
    if username:
        event_name = request.json['event_name']
        event_time = request.json['event_time']
        event_description = request.json['event_description']
        event = {'event_name': event_name, 'event_time': event_time, 'event_description': event_description}
        events.insert_one(event)
        return jsonify({'message': 'Event added successfully!'})
    else:
        return jsonify({'message': 'user not login, return to login page'})

if __name__ == '__main__':
    app.run(debug=True)
