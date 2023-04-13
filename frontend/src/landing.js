import React, { useState } from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';
import './post-event-popup.css';
import HamburgerMenu from './components/HamburgerMenu';

const containerStyle = {
  width: '100%',
  height: '100vh'
};

const center = {
  lat: 38.9072,
  lng: -77.0369
};

function Map() {
  // const [showRegistration, setShowRegistration] = useState(false);
  const [showCreateEvent, setShowCreateEvent] = useState(false);
  const [showLogin, setShowLogin] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const showCreateEventPopup = () => {
    setShowCreateEvent(true);
  };

  const showLoginPopup = () => {
    setShowLogin(true);
  };

  const loginUser = async (username, password) => {
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error:', error);
    }
  };
  

  const handleLoginSubmit = async () => {
    console.log('handleLoginSubmit called');
    const result = await loginUser(username, password);
  
    if (result.success) {
      console.log('Login successful');
      setShowLogin(false);
    } else {
      console.log('Login failed');
    }
  };
  
  

  return (
    <>
      <HamburgerMenu onCreateEventClick={showCreateEventPopup} onLoginClick={showLoginPopup} />
      <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}>
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={center}
          zoom={10}
        >
          {showCreateEvent && (
            <div className="post-event-popup">
              <h2>Create an Event</h2>
              <div className="circle"><span>E</span></div>
              <form>
                <label htmlFor="event-name">Event Name:</label>
                <input type="text" id="event-name" />
                <br />

                <label htmlFor="event-time">Event Time:</label>
                <input type="text" id="event-time" />
                <br />

                <label htmlFor="event-location">Event Location:</label>
                <input type="text" id="event-location" />
                <br />

                <label htmlFor="event-description">Event Description:</label>
                <textarea id="event-description" />
                <br />

                <button type="submit">Publish</button>
              </form>
            </div>
          )}
          {showLogin && (
            <div className="post-event-popup">
              <h2>Login</h2>
              <div className="circle">
                <span>L</span>
              </div>
              <form onSubmit={handleLoginSubmit}>
                <label htmlFor="username">Username:</label>
                <input
                  type="text"
                  id="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
                <br />

                <label htmlFor="password">Password:</label>
                <input
                  type="password"
                  id="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <br />

                <button type="submit">Login</button>
                <p>Don't have an account yet? <a href="#">Sign up now!</a></p>

              </form>
            </div>
          )}

          

        </GoogleMap>
      </LoadScript>
    </>
  );
}

export default Map;
