# Friendymap

## Project Info

Owner: Jing Tao (@taojing10)

Tech Leader: Zhe Cai (@czahie)

Contributors:
- Yuxiang Wang（@allenwang60）
- Sharon Zhou ([@shafact](https://github.com/Shafact))
- Xinnan Wu (@xinnanw)
- Villajwl (@villajwl)
- Chelsea (@chewysea)

## Frontend

### Create React App

`npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

`npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

`npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

`npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

### Integrate Google Map API

1. Install the package with npm:
   `npm i -S @react-google-maps/api`
   (this will install the package as dependency. We can find that package.json has added dependency: react-google-maps/api. 

2. Run the app with

   `npm start`



## Backend

### Flask

The backend server uses the Flask framework.
This documentation explains how to configure and test backend server.

#### Environment requirements

You need to install and update the latest python version in your computer.


To check the version installed, open a terminal window and entering the following:

>**_python --version_** 

**Note**: _python/python2 should be pre-installed, if not, you may download and install from [Python2 download](https://www.python.org/downloads/release/python-2718/).

>**_python3 --version_**

**Note**: _python3 download address [Python3 download](https://www.python.org/downloads/release/python-3111/).

#### Configuring

To configure backend server, you need to:

- Create an Environment
- Activate the Environment
- Install Flask

##### _Create an Environment_

1.Make a separate directory for your project:

  >**_mkdir Friendymap_**  

2.Move into the directory:

  >**_cd Friendymap_** 

3.Within the directory, create the virtual environment for Flask. When you create the environment, a new folder appears in your project directory with the environment’s name.

  >**_python3 -m venv (name of environment)_**

##### _Active the Environment_

  >**_(name of environment)</bin/activate_**

##### _Install Flask_

  >**_pip install Flask_**

### Testing

#### _Test the Development Environment_

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

