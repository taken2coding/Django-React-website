import { Container, Card } from 'react-bootstrap';

function Home() {
  return (
    <Container className="mt-5">
      <Card>
        <Card.Body>
          <Card.Title>Welcome to My Secure Site</Card.Title>
          <Card.Text>
            This is a secure website built with Django and React.
          </Card.Text>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default Home;