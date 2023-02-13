from flask import Flask, render_template, request, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
user = db["users"]

@app.route('/register', methods=[ 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        account = user.find_one({'username' : request.form['username']})

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