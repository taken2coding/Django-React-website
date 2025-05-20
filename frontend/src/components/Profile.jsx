import React, { useEffect,useState } from 'react';
import axios from 'axios';


// Fetch profile (JWT)
const Profile = ({token}) => {
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState(null);

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

  return(
      <div>
          {token}&&(
          <h2>Profile</h2>
          <p>Username: {profile.username}</p>
          <p>Email: {profile.email}</p>
          <p>ID: {profile.id}</p>
          )
      </div>

  )

  }

export default Profile;