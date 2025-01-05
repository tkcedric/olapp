from flask import Blueprint, jsonify, request
from app import db
from app.models.content import Question, Topic
from app.middleware import role_required

questions_routes = Blueprint('questions', __name__)

# Add a new question (Admin Only)
@questions_routes.route('/questions/<int:topic_id>', methods=['POST'])
@role_required(["admin"])
def add_question(topic_id):
    data = request.json
    topic = Topic.query.get(topic_id)

    if not topic:
        return jsonify({"error": "Topic not found"}), 404

    new_question = Question(
        text=data['text'],
        question_type=data['type'],
        year=data.get('year', None),
        paper_type=data.get('paper_type', None),
        topic_id=topic_id
    )
    db.session.add(new_question)
    db.session.commit()

    return jsonify({"message": "Question added successfully!", "id": new_question.id}), 201
