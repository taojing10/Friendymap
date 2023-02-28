# Backend Flask server for Friendymap

The backend server uses the Flask framework.
This documentation explains how to configure and test backend server.


## Environment requirements

You need to install and update the latest python version in your computer.


To check the version installed, open a terminal window and entering the following:

>**_python --version_** 

**Note**: _python/python2 should be pre-installed, if not, you may download and install from [Python2 download](https://www.python.org/downloads/release/python-2718/).

>**_python3 --version_**

**Note**: _python3 download address [Python3 download](https://www.python.org/downloads/release/python-3111/).



## Configuring

To configure backend server, you need to:

- Create an Environment
- Activate the Environment
- Install Flask

### _Create an Environment_
1.Make a separate directory for your project:

  >**_mkdir Friendymap_**  

2.Move into the directory:

  >**_cd Friendymap_** 

3.Within the directory, create the virtual environment for Flask. When you create the environment, a new folder appears in your project directory with the environment’s name.

  >**_python3 -m venv (name of environment)_**

### _Active the Environment_

  >**_(name of environment)</bin/activate_**

### _Install Flask_

  >**_pip install Flask_**

## Testing
### _Test the Development Environment_
1.Create a simple Flask application to test the newly created development environment.

2.Make a file in the Flask project folder called hello.py.

3.Edit the file using a _text editor_ (VS code) and add the following code to make an application that prints "Hello Friendymap!":
>**_from flask import Flask  
>app = Flask(__name __)  
>@app.route('/')  
>def hello_world():  
>return 'Hello Friendymap!'_**

4.Save the file and close.

5.Using the console, navigate to the project folder using the cd command.

6.Set the FLASK_APP environment variable.

  >**_export FLASK_APP=hello.py_**

7.Run the Flask application with:

  >**_flask run_**

![](https://phoenixnap.com/kb/wp-content/uploads/2021/04/Running-a-flask-application.png)

The output prints out a confirmation message and the address.

8.Copy and paste the address into the browser to see the project running!