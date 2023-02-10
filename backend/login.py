from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:*****/database_name"
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("home page")

#create a collection in Mongodb to store user information (username and password)
users_collection = mongo.db.users

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        #get user info from the form
        username = request.form["username"]
        password = request.form["password"]

        #check if both username and password r correct
        existing_user = users_collection.find_one({"username": username, "password": password})
        if existing_user:
            # store the user ID in the session to keep the user logged in
            session["user_id"] = str(existing_user["_id"])
            return "Successfully logged in"
        else:
            return "Incorrect username or password"

    return render_template("login page")
