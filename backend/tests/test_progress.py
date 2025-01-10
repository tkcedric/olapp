def test_get_progress(client):
    # Register a new user
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    user_id = response.get_json().get('id')

    # Initialize progress
    response = client.post(f'/api/progress/{user_id}/1')  # Include user_id and topic_id in the URL
    assert response.status_code == 201

    # Test GET progress
    response = client.get('/api/progress', headers={"User-Id": str(user_id)})
    assert response.status_code == 200
    # Additional assertions...

def test_update_progress(client):
    # Register a new user
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    user_id = response.get_json().get('id')

    # Initialize progress
    response = client.post(f'/api/progress/{user_id}/1')  # Include user_id and topic_id in the URL
    assert response.status_code == 201

    # Update progress
    response = client.put(f'/api/progress/{user_id}/1', json={
        'answered_correctly': 10,
        'completed': True
    })
    assert response.status_code == 200
    # Additional assertions...

    
    updated_progress = response.get_json()
    assert updated_progress['progress']['answered_correctly'] == 10
    assert updated_progress['progress']['completed'] is True
