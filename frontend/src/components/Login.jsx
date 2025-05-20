// Handle login
import React, { useState } from 'react';
import axios from 'axios';

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/api/token/', { username, password });
      const { access, refresh } = res.data;
      setToken(access);
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      setError(null);
    } catch (err) {
      setError('Login failed');
    }
  };

  return (
    <div>
      <h1>Books</h1>
      {error && <p>Error: {error}</p>}
      <ul>{books.map((book, i) => <li key={i}>{book}</li>)}</ul>

      <h2>Login</h2>
      {!token ? (
        <form onSubmit={handleLogin}>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Username"
            required
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            required
          />
          <button type="submit">Login</button>
        </form>
      ) : (
        <button onClick={() => {
          setToken('');
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          setProfile(null);
        }}>Logout</button>
      )}

      {profile && (
        <div>
          <h2>Profile</h2>
          <p>Username: {profile.username}</p>
          <p>Email: {profile.email}</p>
          <p>ID: {profile.id}</p>
        </div>
      )}
    </div>
  );
}