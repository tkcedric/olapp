from flask import Blueprint, jsonify, request

courses_routes = Blueprint('courses', __name__)

@courses_routes.route('/courses', methods=['GET'])
def get_courses():
    from app.models.content import Course  # Lazy import
    courses = Course.query.all()
    return jsonify([
        {
            "id": course.id,
            "title": course.title,
            "level": course.level,
            "description": course.description
        }
        for course in courses
    ])

@courses_routes.route('/courses', methods=['POST'])
def create_course():
    from app.models.content import Course  # Lazy import
    from app import db  # Lazy import
    data = request.json
    new_course = Course(
        title=data['title'],
        level=data['level'],
        description=data.get('description', '')
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"message": "Course created successfully!", "id": new_course.id}), 201
