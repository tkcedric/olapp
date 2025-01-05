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
    ])
# Initialize progress for a specific user and topic
@progress_routes.route('/progress/<int:user_id>/<int:topic_id>', methods=['POST'])
def initialize_progress(user_id, topic_id):
    # Check if progress already exists
    progress = Progress.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if not progress:
        # Create a new progress record
        progress = Progress(
            user_id=user_id,
            topic_id=topic_id,
            total_questions=10,  # Replace with dynamic question count if needed
            answered_correctly=0,
            completed=False
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
    data = request.json
    progress = Progress.query.filter_by(user_id=user_id, topic_id=topic_id).first()

    if not progress:
        return jsonify({"error": "Progress record not found"}), 404

    # Update the progress record
    progress.answered_correctly += data.get('answered_correctly', 0)
    progress.completed = progress.answered_correctly >= progress.total_questions

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
