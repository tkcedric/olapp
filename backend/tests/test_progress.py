def test_get_progress(client):
    # Add a user and progress data
    client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })

    client.post('/api/lessons', json={
        'title': 'Sample Lesson',
        'content': 'Sample lesson content.',
        'course_id': 1
    })

    # Add progress for the user
    response = client.post('/api/progress', json={
        'user_id': 1,
        'topic_id': 1,
        'total_questions': 10,
        'answered_correctly': 5,
        'completed': False
    })
    assert response.status_code == 201
    assert b"Progress initialized successfully" in response.data

    # Fetch progress
    response = client.get('/api/progress')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0
    assert "total_questions" in response.json[0]

def test_update_progress(client):
    # Register user and initialize progress
    client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })

    client.post('/api/progress', json={
        'user_id': 1,
        'topic_id': 1,
        'total_questions': 10,
        'answered_correctly': 5,
        'completed': False
    })

    # Update progress
    response = client.put('/api/progress/1/1', json={
        'answered_correctly': 10,
        'completed': True
    })
    assert response.status_code == 200
    assert b"Progress updated successfully" in response.data

    # Verify progress is updated
    response = client.get('/api/progress')
    assert response.status_code == 200
    progress = response.json[0]
    assert progress['answered_correctly'] == 10
    assert progress['completed'] is True
