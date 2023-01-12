# Create a New React APP
[source](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app)

Run the following - replace my_app with the your folder name

`npx create-react-app my-app`

`cd my-app`

`npm start`
	
	

# Learn the folder structure:
1. **./public/index.html** is the entry for the webpage. Element: **root** is the entry(`    <div id="root"></div>`)
2. **./src/index.js** is the entry for our code. `root.render()` reads our code and render to website. In this case, index.js' code calls app.js for detailed code. So **./src/app.js** is our main source code.
An alternative way to only use index.js is :

	~~~jsx
	const root = ReactDOM.createRoot(document.getElementById('root'));
	root.render(<MyComponent />)
	~~~
3. The above two files are necessary, the other files in ./src can be deleted if no need.


# Install @react-google-maps/api package to integrate google map.
[source](https://www.npmjs.com/package/@react-google-maps/api)

Install the package with npm:
`npm i -S @react-google-maps/api`
(this will install the package as dependency. We can find that package.json has added dependency: react-google-maps/api.

# Code the App - basic version
1. Clean up **App.js** by replacing the code in `return()` to `<div>Map<div/>`. Run `npm install` and `npm start` to see if there is a map in the web, it indicates our code runs successfully.
2. Replace our title from "React app" to "My Map". In ./public/index.html, change the title element to `<title>My Map</title>`.
3. Import **useJsApiLoader, GoogleMap, Marker** hooker from @react-google-map/api for use.
`import { GoogleMap, useJsApiLoader, Marker } from '@react-google-maps/api';  ` 

	`import + {}` means import **hooks** from package. Hooks are _functions_ that let you “hook into” React state and lifecycle features from function components. Hooks don’t work inside classes — they let you use React without classes.
	
	Official Docs for @react-google-maps/api is in this [link](https://react-google-maps-api-docs.netlify.app/). **useJsApiLoader** is a component of the package [source code](https://github.com/JustFly1984/react-google-maps-api/blob/develop/packages/react-google-maps-api/src/useJsApiLoader.tsx). It accepts an object that has bunch of properties as an argument and return two objects: 1. _isLoaded_, a boolean value; and 2. _loadError_, an error object. **GoogleMap** is another component [source code](https://github.com/JustFly1984/react-google-maps-api/blob/develop/packages/react-google-maps-api/src/GoogleMap.tsx). This map component inside which all other components render. **Marker** is also a component in the package [source code](https://github.com/JustFly1984/react-google-maps-api/blob/develop/packages/react-google-maps-api/src/components/drawing/Marker.tsx). This is to set up marker in the map.



4. Load google map script with API key (refer to this [link](https://developers.google.com/maps/documentation/javascript/get-api-key) to create an API key):


	~~~jsx
  	const { isLoaded } = useJsApiLoader({
    	id: 'google-map-script',
    	googleMapsApiKey: "Your Key"
 	}); 
	~~~
	
	Consider situation where mapscript is not loaded: return nothing messege.
	
	~~~jsx
	 if (!isLoaded) {
    	return (<></>)
  	 };
  ~~~
  An alternative way is to use [inline if statement](https://reactjs.org/docs/conditional-rendering.html) `condition ? true : false`. We can optimize it later after we have the main code block done.
  
5. Working on app code to return a map.

	* **Replace the placeholder** `<div>Map</div>` to GoogleMap component `<GoogleMap></GoogleMap>`
	* Add necessary props to GoogleMap: zoom, center, mapContainerStle. Given them a few value as placeholder: 
	
		~~~jsx
		<GoogleMap 
	      zoom={10} 
	      center={{ lat: 38.89766, lng: -77.0365}} 
	      mapContainerStyle={{ width: '400px', height: '400px' }}
	    >
	    </GoogleMap>
	    ~~~
	* Add a marker to our center: 

		~~~jsx
	<GoogleMap 
	      zoom={10} 
	      center={{ lat: 38.89766, lng: -77.0365}} 
	      mapContainerStyle={{ width: '400px', height: '400px' }}
    >
      	  <Marker position={{ lat: 38.89766, lng: -77.0365}} />
    </GoogleMap>
    ~~~
   
   To use **inline if statement** directly, we can combine the #4 code and #5 code as below:
   
   ~~~jsx
     return isLoaded ? (
	    <GoogleMap zoom={10} center={center} mapContainerStyle={containerStyle}>
	      <Marker position={center} />
	    </GoogleMap>
	  ) : <></>
   ~~~
	
Now we have a basic map.

# Optimize Code


1. GoogleMap's props can be set as variables for better reference:

		`const containerStyle = {   lat: 38.89766, lng: -77.0365 };`
		`const containerStyle = { width: '400px', height: '400px' }`
		
	To set the map matching the screen we can set the container style as the below:
		
		`const containerStyle = { width: '100%', height: '100vh' }`
2. GoogleMap Key should not be committed to our code directly. It raised security issue. We can add a local environment to run it or set up global configure. Setting up global configure will not be discussed in this session.

	Instruction of set up local environment for the key can be referred [here](https://create-react-app.dev/docs/adding-custom-environment-variables/).
	- Step 1: create a .env file under the root folder.
	- Step 2: create a variable starting with `REACT_APP` to save your key. For example, `REACT_APP_GOOGLE_MAP_KEY=YOUR KEY HERE`
	- Step 3: in the App.js code, replace `googleMapsApiKey: "Your Key"` to `googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAP_KEY`
	- Step 4: save and close the project. Rerun the server in terminal: 
`npm install` and `npm start`


	


# FAQ
1. Why doesn't .env.local work? 

	The variable must be started with `REACT_APP` per this [instruction](https://create-react-app.dev/docs/adding-custom-environment-variables/). Changing any environment variables will require you to restart the development server if it is running.


	
	
