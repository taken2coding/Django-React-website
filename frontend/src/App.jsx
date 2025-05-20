// frontend/src/App.jsx
import { useEffect, useState } from 'react';
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

function App() {
  const [books, setBooks] = useState([]);
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState(null);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState(localStorage.getItem('access_token') || '');

  // Fetch books (API key, from previous setup)
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/books/?q=', {
      headers: {
        'Authorization': `Api-Key ${import.meta.env.VITE_API_KEY}`,
      },
    })
      .then((res) => setBooks(res.data))
      .catch((err) => setError(err.message));
  }, []);

  // Fetch profile (JWT)
  useEffect(() => {
    if (token) {
      axios.get('http://127.0.0.1:8000/api/profile/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then((res) => setProfile(res.data))
        .catch((err) => {
          setError(err.message);
          setToken('');
          localStorage.removeItem('access_token');
        });
    }
  }, [token]);

  // Handle login
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/token/', { username, password });
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
      <ul>{books.map((book, i) => <li key={i}>{book.title}</li>)}</ul>

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

export default App;