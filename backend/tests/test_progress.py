def test_get_progress(client):
    # Register a new user
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    user_id = response.get_json().get('id')

    # Add progress data
    response = client.post('/api/progress', json={
        'user_id': user_id,
        'topic_id': 1,
        'total_questions': 10,
        'answered_correctly': 5,
        'completed': False
    })
    assert response.status_code == 200

    # Test GET progress
    response = client.get('/api/progress', headers={"User-Id": str(user_id)})
    assert response.status_code == 200
    assert len(response.get_json()) > 0


def test_update_progress(client):
    # Register a new user
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    user_id = response.get_json().get('id')

    # Add progress data
    response = client.post('/api/progress', json={
        'user_id': user_id,
        'topic_id': 1,
        'total_questions': 10,
        'answered_correctly': 5,
        'completed': False
    })
    assert response.status_code == 200

    # Test PUT progress
    response = client.put(f'/api/progress/{user_id}/1', json={
        'answered_correctly': 10,
        'completed': True
    })
    assert response.status_code == 200
    progress = response.get_json().get('progress')
    assert progress['answered_correctly'] == 10
    assert progress['completed'] is True
