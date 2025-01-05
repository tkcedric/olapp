from flask import Blueprint, jsonify, request
from app.models.content import Lesson, UserAccess
from app.models.user import User
from app import db

payment_routes = Blueprint('payment', __name__)

@payment_routes.route('/payment/lesson/<int:lesson_id>', methods=['POST'])
def pay_for_lesson(lesson_id):
    user_id = request.json.get("user_id")

    # Check if lesson exists
    lesson = Lesson.query.get(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404

    # Check if user already has access
    access = UserAccess.query.filter_by(user_id=user_id, lesson_id=lesson_id).first()
    if access:
        return jsonify({"message": "You already have access to this lesson."}), 200

    # Simulate payment processing (replace with actual payment integration)
    # Assuming payment is always successful
    new_access = UserAccess(user_id=user_id, lesson_id=lesson_id)
    db.session.add(new_access)
    db.session.commit()

    return jsonify({"message": "Payment successful. Lesson unlocked!"})
