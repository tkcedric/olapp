from flask import Blueprint, jsonify, request
from app.models.content import Lesson, Task, UserAccess
from app import db

lessons_routes = Blueprint('lessons', __name__)

# Fetch all lessons
@lessons_routes.route('/lessons', methods=['GET'])
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([
        {
            "id": lesson.id,
            "title": lesson.title,
            "content": lesson.content if lesson.is_free else "Paid Content",
            "course_id": lesson.course_id,
            "is_free": lesson.is_free
        }
        for lesson in lessons
    ])

# Fetch a specific lesson (with access control for paid lessons)
@lessons_routes.route('/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    from app.models.content import Lesson, UserAccess
    user_id = request.headers.get("User-Id")  # Assume user ID is sent in the headers

    lesson = Lesson.query.get(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404

    if not lesson.is_free:
        # Check if user has access
        access = UserAccess.query.filter_by(user_id=user_id, lesson_id=lesson_id).first()
        if not access:
            return jsonify({"error": "Access denied. This is a paid lesson."}), 403

    return jsonify({
        "id": lesson.id,
        "title": lesson.title,
        "content": lesson.content,
        "course_id": lesson.course_id,
        "is_free": lesson.is_free
    })

# Fetch tasks for a specific lesson
@lessons_routes.route('/lessons/<int:lesson_id>/tasks', methods=['GET'])
def get_tasks(lesson_id):
    tasks = Task.query.filter_by(lesson_id=lesson_id).all()
    return jsonify([
        {
            "id": task.id,
            "code_snippet": task.code_snippet,
            "expected_output": task.expected_output,
            "description": task.description
        }
        for task in tasks
    ])

# Submit a task for evaluation
@lessons_routes.route('/tasks/<int:task_id>/submit', methods=['POST'])
def submit_task(task_id):
    data = request.json
    user_code = data.get('code')

    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    # Placeholder logic for code execution
    # Compare user submission with the expected output
    if user_code.strip() == task.expected_output.strip():
        return jsonify({"result": "success", "message": "Great job! Your solution is correct!"})
    return jsonify({
        "result": "failure",
        "message": "Your solution is incorrect.",
        "expected_output": task.expected_output
    })

# Add a new lesson
@lessons_routes.route('/lessons', methods=['POST'])
def add_lesson():
    data = request.json
    new_lesson = Lesson(
        title=data.get('title'),
        content=data.get('content'),
        course_id=data.get('course_id'),
        is_free=data.get('is_free', False)  # Default to False if not provided
    )
    db.session.add(new_lesson)
    db.session.commit()
    return jsonify({"message": "Lesson added successfully!", "lesson_id": new_lesson.id}), 201

# Update an existing lesson
@lessons_routes.route('/lessons/<int:lesson_id>', methods=['PUT'])
def update_lesson(lesson_id):
    data = request.json
    lesson = Lesson.query.get(lesson_id)

    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404

    lesson.title = data.get('title', lesson.title)
    lesson.content = data.get('content', lesson.content)
    lesson.course_id = data.get('course_id', lesson.course_id)
    lesson.is_free = data.get('is_free', lesson.is_free)

    db.session.commit()
    return jsonify({"message": "Lesson updated successfully!"})

# Delete a lesson
@lessons_routes.route('/lessons/<int:lesson_id>', methods=['DELETE'])
def delete_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)

    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404

    db.session.delete(lesson)
    db.session.commit()
    return jsonify({"message": "Lesson deleted successfully!"})

# Add a new task to a lesson
@lessons_routes.route('/lessons/<int:lesson_id>/tasks', methods=['POST'])
def add_task(lesson_id):
    data = request.json
    new_task = Task(
        code_snippet=data.get('code_snippet'),
        expected_output=data.get('expected_output'),
        description=data.get('description'),
        lesson_id=lesson_id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully!", "task_id": new_task.id}), 201
