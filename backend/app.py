import os
from app import create_app, db
from app.models.user import User  # Ensure this is imported to initialize the table
from app.models.content import Topic, Question, Answer, Progress, CourseProgress

app = create_app()

# Initialize the database
with app.app_context():
    db.create_all()  # This ensures the database and tables are created

if __name__ == "__main__":
    app.run(debug=True)


# Add GCC directory to PATH
os.environ["PATH"] += os.pathsep + r"C:\MinGW\bin"
# Debug: Print the updated PATH
print("Updated PATH:", os.environ["PATH"])
import subprocess

gcc_test = subprocess.run(['gcc', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("GCC Test Output:", gcc_test.stdout or gcc_test.stderr)

for rule in app.url_map.iter_rules():
    print(f"Endpoint: {rule.endpoint}, Methods: {rule.methods}, URL: {rule}")
