import React, { useState } from 'react';

const TestLogin = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

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
      console.log('loginUser response:', data);
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
    } else {
      console.log('Login failed');
    }
  };

  return (
    <div>
      <h2>Login</h2>
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

      <button type="button" onClick={handleLoginSubmit}>
        Login
      </button>
    </div>
  );
};

export default TestLogin;
