import './App.css';
import { useJsApiLoader, GoogleMap, Marker } from '@react-google-maps/api';

const center = { lat: 38.89766, lng: -77.0365 };

const containerStyle = { width: '100%', height: '100vh' };

function App() {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAP_API,
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
