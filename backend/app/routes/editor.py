import subprocess
from flask import Blueprint, jsonify, request

editor_routes = Blueprint('editor', __name__)

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
    import os
    import shutil
    data = request.json
    code = data.get('code', '')

    try:
        # Save the code to a temporary file
        temp_c_file = 'temp.c'
        with open(temp_c_file, 'w') as temp_file:
            temp_file.write(code)

        # Debug: Check if file exists
        if not os.path.exists(temp_c_file):
            return jsonify({"error": "Temporary C file was not created."}), 500

        # Debug: Check working directory
        print("Current Working Directory:", os.getcwd())

        # Compile the C code
        compile_result = subprocess.run(
            ['gcc', temp_c_file, '-o', 'temp.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Debug: Log compilation output
        print("Compilation Output:", compile_result.stdout)
        print("Compilation Error:", compile_result.stderr)

        if compile_result.returncode != 0:
            return jsonify({"stdout": "", "stderr": compile_result.stderr})

        # Execute the compiled binary
        exec_result = subprocess.run(
            ['temp.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Debug: Log execution output
        print("Execution Output:", exec_result.stdout)
        print("Execution Error:", exec_result.stderr)

        return jsonify({
            "stdout": exec_result.stdout,
            "stderr": exec_result.stderr
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
