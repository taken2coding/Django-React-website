import { Container, Card } from 'react-bootstrap';
import axios from 'axios';
import { useState, useEffect } from 'react';

function About() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/profile/`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setUserData(response.data);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };
    fetchUserData();
  }, []);

  return (
    <Container className="mt-5">
      <Card>
        <Card.Body>
          <Card.Title>About Us</Card.Title>
          <Card.Text>
            This page is only accessible to authenticated users.
            {userData && (
              <p>Welcome, {userData.username}! Your email is {userData.email}</p>
            )}
          </Card.Text>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default About;