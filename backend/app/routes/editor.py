import os
import subprocess
from flask import Blueprint, jsonify, request
from app.models.content import Lesson, Task
from app import db

editor_routes = Blueprint('editor', __name__)

# Fetch all lessons
@editor_routes.route('/lessons', methods=['GET'])
def get_lessons():
    lessons = Lesson.query.all()
    return jsonify([
        {
            "id": lesson.id,
            "title": lesson.title,
            "content": lesson.content,
            "course_id": lesson.course_id
        }
        for lesson in lessons
    ])

# Fetch a specific lesson and its tasks
@editor_routes.route('/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson_with_tasks(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    tasks = Task.query.filter_by(lesson_id=lesson.id).all()
    return jsonify({
        "id": lesson.id,
        "title": lesson.title,
        "content": lesson.content,
        "tasks": [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description
            }
            for task in tasks
        ]
    })

# Execute Python code
@editor_routes.route('/execute/python', methods=['POST'])
def execute_python():
    data = request.json
    code = data.get('code', '')

    try:
        # Execute Python code
        result = subprocess.run(
            ['python', '-c', code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5  # Limit execution time
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Code execution timed out."}), 408

# Execute C code
@editor_routes.route('/execute/c', methods=['POST'])
def execute_c():
    data = request.json
    code = data.get('code', '')

    try:
        # Save the code to a temporary file
        temp_c_file = 'temp.c'
        with open(temp_c_file, 'w') as temp_file:
            temp_file.write(code)

        # Compile the C code
        compile_result = subprocess.run(
            ['gcc', temp_c_file, '-o', 'temp.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if compile_result.returncode != 0:
            return jsonify({"stdout": "", "stderr": compile_result.stderr})

        # Execute the compiled binary
        exec_result = subprocess.run(
            ['./temp.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return jsonify({
            "stdout": exec_result.stdout,
            "stderr": exec_result.stderr
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Code execution timed out."}), 408
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Cleanup temporary files
        if os.path.exists('temp.c'):
            os.remove('temp.c')
        if os.path.exists('temp.exe'):
            os.remove('temp.exe')
