from app import create_app, db
from app.models.user import User
from werkzeug.security import generate_password_hash
import json

app = create_app()

def add_students(file_path):
    """
    Add students to the database from a JSON file.
    """
    with open(file_path, "r") as file:
        students = json.load(file)

    with app.app_context():
        for student in students:
            # Check if the email is already registered
            if User.query.filter_by(email=student["email"]).first():
                print(f"Email {student['email']} is already registered. Skipping.")
                continue

            # Add new student
            new_user = User(
                username=student["name"],
                email=student["email"],
                password=generate_password_hash(student["password"], method="pbkdf2:sha256"),
                role="student"
            )
            db.session.add(new_user)

        db.session.commit()
        print("Students successfully added to the database.")

if __name__ == "__main__":
    # Path to the JSON file containing student data
    file_path = "scripts/students.json"
    add_students(file_path)
