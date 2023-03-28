from flask import Flask, request, redirect, jsonify, url_for, make_response
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import Length
import hashlib
import db_connection
import secrets
from flask_wtf.csrf import generate_csrf



app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)
#csrf = CSRFProtect(app)


mongo_client = db_connection.get_mongo_client()
db = mongo_client.Friendymap_db
users = db.user

@app.route('/get_csrf_token')
def get_csrf_token():
    csrf_token = generate_csrf()
    response = make_response(jsonify({'csrf_token': csrf_token}))
    response.set_cookie('csrf_token', csrf_token, httponly=True, secure=True)
    return response

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=20)])
    password = PasswordField('Password', validators=[Length(min=4, max=20)])
    submit = SubmitField("submit")


def validate_username(username):
    user = users.find_one({'username': username})
    if user['password'] != hashlib.sha256('password'.encode()).hexdigest():

        if not user:
            return True

@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form,  meta={'csrf': False})

    if form.validate():
        username = form.username.data
        password = form.password.data

        # check if username already exists
        if not validate_username(username):
            return "Account already exists!"

        else:
            user = {'username': username, 'password': password}
            users.insert_one(user)
            #redirect to login page
            return redirect(url_for('login'))
    else:
        return 'Welcome'

if __name__=='__main__':
    app.run(False)