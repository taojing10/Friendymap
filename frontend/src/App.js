import './App.css';
import { useJsApiLoader, GoogleMap, Marker} from '@react-google-maps/api';
import {useState, useEffect} from "react";

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
  credentials: creds
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
const secret =JSON.parse(secret_json);

const mapStyles = {        
  height: "100vh",
  width: "100%"};

function App() {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: secret["REACT_APP_GOOGLE_MAP_API"]
  });

  const [ currentPosition, setCurrentPosition ] = useState({
    lat: 38.89766, lng: -77.0365 })
    const success = position => {
    setCurrentPosition ({lat: position.coords.latitude,
      lng: position.coords.longitude} );}

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(success); 
  },[navigator.geolocation]
  )

  if (isLoaded) {
    return (
      <GoogleMap mapContainerStyle={mapStyles} zoom={13}
      center={currentPosition}> <Marker position={currentPosition} />
      </GoogleMap>);} 
      

      else {
    return (<></>);
  }
}

export default App;