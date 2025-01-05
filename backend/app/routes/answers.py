from flask import Blueprint, jsonify, request
from app import db
from app.models.content import Question, Answer

answers_routes = Blueprint('answers', __name__)


# Add answer
@answers_routes.route('/answers/<int:question_id>', methods=['POST'])
def add_answer(question_id):
    from flask import request
    from app.models.content import Question, Answer

    data = request.json
    question = Question.query.get(question_id)

    if not question:
        return jsonify({"error": "Question not found"}), 404

    new_answer = Answer(
        text=data['text'],
        is_correct=data.get('is_correct', False),
        question_id=question_id
    )
    db.session.add(new_answer)
    db.session.commit()

    return jsonify({"message": "Answer added successfully!", "id": new_answer.id}), 201

# Update an answer
@answers_routes.route('/answers/<int:answer_id>', methods=['PUT'])
def update_answer(answer_id):
    from flask import request
    from app.models.content import Answer

    data = request.json
    answer = Answer.query.get(answer_id)

    if not answer:
        return jsonify({"error": "Answer not found"}), 404

    answer.text = data.get('text', answer.text)
    answer.is_correct = data.get('is_correct', answer.is_correct)

    db.session.commit()

    return jsonify({"message": "Answer updated successfully!"})

# Delete an answer
@answers_routes.route('/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    from app.models.content import Answer

    answer = Answer.query.get(answer_id)

    if not answer:
        return jsonify({"error": "Answer not found"}), 404

    db.session.delete(answer)
    db.session.commit()

    return jsonify({"message": "Answer deleted successfully!"})

# Fetch Answers for a question
@answers_routes.route('/answers/<int:question_id>', methods=['GET'])
def get_answers(question_id):
    from app.models.content import Question

    question = Question.query.get(question_id)

    if not question:
        return jsonify({"error": "Question not found"}), 404

    answers = [
        {"id": answer.id, "text": answer.text, "is_correct": answer.is_correct}
        for answer in question.answers
    ]

    return jsonify(answers)
