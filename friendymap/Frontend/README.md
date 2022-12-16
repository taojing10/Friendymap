# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Install React.JS

To set up React, you will need to have Node.js and npm (Node Package Manager) installed on your computer. To check if you have these installed, you can open a terminal or command prompt and type the following commands:

node -v 

npm -v

If you see a version number for both commands, then you already have Node.js and npm installed. If you see an error message, then you will need to install Node.js and npm by following the instructions on the Node.js website: https://nodejs.org/en/

### `Install Reactjs`

Once you have Node.js and npm installed, you can use npm to install the create-react-app package, which will provide a simple way to create a new React project. To do this, open a terminal or command prompt and run the following command:

npm install -g create-react-app


### `Create a React Project`

This will install the create-react-app package globally on your computer, which means you can use it to create a new React project anywhere on your system.
To create a new React project, navigate to the directory where you want to store your project and run the following command:

npx create-react-app friendymap (or replace with any project name you want)


### `Run Your React Project`

To run your React project, navigate to the project directory and run the following command:

cd friendymap

npm start

This will start a local development server and open your default web browser to http://localhost:3000, where you should see your React application running.

Congratulations, you have successfully set up and run a React project!


# Integrate with Google Map API
There are **two steps** to set up integration with google :

1. Install all dependencies
2. Set up local environment with API key

## Install all dependencies
First of all, in the termal, run `git pull` to pull latest version of repository.

Run `npm install`to install all dependencies -- this will create a node_modules folder.

## Set up local environment with API key
1. create a file called `.env` under root folder (FRONTEND folder)
2. In the `.env` file add this line (*note: Replace `API key` with your own API key or Ask @sharon to share her key to you*)

	`REACT_APP_GOOGLE_MAPS_API_KEY=*API Key*`
	
	If you want to get your own API key plear refer to [this link](https://developers.google.com/maps/documentation/javascript/get-api-key)

## Run the Application
In your terminal, run `npm start`
