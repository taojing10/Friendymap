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
    googleMapsApiKey: secret["REACT_APP_GOOGLE_MAP_API"]
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

export default App;
