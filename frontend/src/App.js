import './App.css';
import { useJsApiLoader, GoogleMap, Marker } from '@react-google-maps/api';
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager"
// import { fromIni } from "@aws-sdk/credential-providers"

const creds = {
  accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.REACT_APP_SECRET_ACCESS_KEY
};

const secret_name = "Test_Map_API_Key";


const client = new SecretsManagerClient({
  region: "us-east-1",
  credentials: creds
  // credentials: fromIni({profile: 'default'})
});

let response;

try {
  response = await client.send(
    new GetSecretValueCommand({
      SecretId: secret_name,
      VersionStage: "AWSCURRENT", // VersionStage defaults to AWSCURRENT if unspecified
    })
  );
} catch (error) {
  // For a list of exceptions thrown, see
  // https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
  throw error;
}

const secret_json = response.SecretString;

// console.log(secret)

const secret = JSON.parse(secret_json);

// console.log(secret2)

// console.log(secret2['GOOGLE_MAP_API'])

const center = { lat: 38.89766, lng: -77.0365 };

const containerStyle = { width: '100%', height: '100vh' };

function App() {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: secret["GOOGLE_MAP_API"]
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
