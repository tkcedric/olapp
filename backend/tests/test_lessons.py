def test_get_lessons(client):
    response = client.get('/api/lessons')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_lesson(client):
    response = client.post('/api/lessons', json={
        'title': 'Test Lesson',
        'content': 'This is a test lesson.',
        'course_id': 1
    })
    assert response.status_code == 201
    assert b"Lesson added successfully" in response.data
