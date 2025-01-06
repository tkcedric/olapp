from flask import Blueprint, jsonify, request
from app.models.content import Progress
from app import db

progress_routes = Blueprint('progress', __name__)

# Get all progress for a specific user
@progress_routes.route('/progress', methods=['GET'])
def get_all_user_progress():
    user_id = request.headers.get("User-Id")
    if not user_id:
        return jsonify({"error": "User ID missing in headers"}), 400

    progress_records = Progress.query.filter_by(user_id=user_id).all()
    if not progress_records:
        return jsonify({"error": "No progress records found for the user"}), 404

    return jsonify([
        {
            "id": record.id,
            "topic_id": record.topic_id,
            "total_questions": record.total_questions,
            "answered_correctly": record.answered_correctly,
            "completed": record.completed
        }
        for record in progress_records
    ]), 200

# Initialize progress for a specific user and topic
@progress_routes.route('/progress', methods=['POST'])
def initialize_progress():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    user_id = data.get('user_id')
    topic_id = data.get('topic_id')
    if not user_id or not topic_id:
        return jsonify({"error": "user_id and topic_id are required"}), 400
    
    # Check if progress already exists
    progress = Progress.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if not progress:
        # Create a new progress record
        progress = Progress(
            user_id=user_id,
            topic_id=topic_id,
            total_questions=data.get('total_questions', 10),  # Replace with dynamic question count if needed
            answered_correctly=data.get('answered_correctly', 0),
            completed=data.get('completed', False)
        )
        db.session.add(progress)
        db.session.commit()
        return jsonify({
            "message": "Progress initialized successfully!",
            "progress": {
                "id": progress.id,
                "user_id": progress.user_id,
                "topic_id": progress.topic_id,
                "total_questions": progress.total_questions,
                "answered_correctly": progress.answered_correctly,
                "completed": progress.completed
            }
        }), 201
    else:
        return jsonify({"message": "Progress already exists!"}), 200

# Update progress for a specific user and topic
@progress_routes.route('/progress/<int:user_id>/<int:topic_id>', methods=['PUT'])
def update_progress(user_id, topic_id):
    progress = Progress.query.filter_by(user_id=user_id, topic_id=topic_id).first()

    if not progress:
        return jsonify({"error": "Progress record not found"}), 404

    data = request.json
    progress.answered_correctly = data.get('answered_correctly', progress.answered_correctly)
    progress.completed = data.get('completed', progress.completed)
    db.session.commit()

    return jsonify({
        "message": "Progress updated successfully!",
        "progress": {
            "id": progress.id,
            "user_id": progress.user_id,
            "topic_id": progress.topic_id,
            "total_questions": progress.total_questions,
            "answered_correctly": progress.answered_correctly,
            "completed": progress.completed
        }
    }), 200

def test_initialize_progress(client):
    # Register a new user
    response = client.post('/api/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    user_id = response.get_json().get('id')

    # Initialize progress
    response = client.post(f'/api/progress/{user_id}/1')
    assert response.status_code == 201
    # Additional assertions...
