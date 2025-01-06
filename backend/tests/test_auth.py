import json

def test_register(client):
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert b"User registered successfully" in response.data


def test_login(client):
    # First, register a user
    client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })

    # Then, try to log in
    response = client.post('/api/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert b"Login successful" in response.data


def test_invalid_login(client):
    response = client.post('/api/login', json={
        'email': 'nonexistent@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert b"Invalid email or password" in response.data
