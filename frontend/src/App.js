import './App.css';
import { useJsApiLoader, GoogleMap, Marker } from '@react-google-maps/api';
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager";

const creds = {
  accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.REACT_APP_SECRET_ACCESS_KEY
};

const secret_name = "REACT_APP_GOOGLE_MAP_API";


const client = new SecretsManagerClient({
  region: "us-east-1",
  credentials: creds,
});

let response;

try {
  response = await client.send(
    new GetSecretValueCommand({
      SecretId: secret_name,
      VersionStage: "AWSCURRENT", 
    })
  );
} catch (error) {
    throw error;
}

const secret_json = response.SecretString;

const secret = JSON.parse(secret_json);

const center = { lat: 38.89766, lng: -77.0365 };

const containerStyle = { width: '100%', height: '100vh' };

function App() {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: secret["REACT_APP_GOOGLE_MAP_API"],
    libraries:["places"],
  }); 

  if (isLoaded) {
    return (
      <GoogleMap zoom={10} center={center} mapContainerStyle={containerStyle}>
        <Marker position={center} />
      </GoogleMap>
    );
  } else {
    return (<></>);
  }
}


//The google.maps.Map() constructor is used to create the map object
//Initialize the map and set the initial viewport bounds.

const map = new google.maps.Map(document.querySelector('GoogleMap'), {
  zoom: 10,
  center: {lat: 38.89766, lng: -77.0365} // dc
});


//Add an event listener for the "idle" event, which fires when the map 
//has finished loading and panning to a new location.

google.maps.event.addListener(map,'idle', function() {
  var bounds = map.getBounds(); // retrieves the bounds of the current viewport 
  var ne = bounds.getNorthEast(); // .The bounds object contains the latitude and longitude
  var sw = bounds.getSouthWest();

// get the current viewport bounds and use them to fetch the posts that fall within 
//that area using AJAX call to your server-side API to fetch the posts.
  $.ajax({
    url: '/api/posts',
    type: 'GET',
    data: {
      'ne_lat': ne.lat(),
      'ne_lng': ne.lng(),
      'sw_lat': sw.lat(),
      'sw_lng': sw.lng()
    },
    success: function(posts) {
      //code to display the posts goes here
      for (var i = 0; i < posts.length; i++) {
        var post = posts[i];

        var marker = new google.maps.Marker({
          position: {lat: post.lat, lng: post.lng},
          map: map,
          title: post.title
        });
      }
    }
  });
});

export default App;

