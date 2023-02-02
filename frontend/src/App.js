import './App.css';
import { useJsApiLoader, GoogleMap, Marker} from '@react-google-maps/api';
import {useState, useEffect} from "react";

const mapStyles = {        
  height: "100vh",
  width: "100%"};

function App() {
  const { isLoaded } = useJsApiLoader({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAP_API,}); 

  const [ currentPosition, setCurrentPosition ] = useState({
    lat: 38.89766, lng: -77.0365 });
  
    const success = position => {
    console.log(position.coords)
    setCurrentPosition ({lat: position.coords.latitude,
      lng: position.coords.longitude} );};

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(success);
  },[navigator.geolocation])

  if (isLoaded) {
    console.log(currentPosition)
    return (
      <GoogleMap mapContainerStyle={mapStyles} zoom={13}
      center={currentPosition}>
      
          <Marker position={currentPosition} />
  
      </GoogleMap>);} 
      
      else {
    return (<></>);}
}

export default App;