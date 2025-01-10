from app import create_app, db
from app.models.user import User
import re

app = create_app()

def extract_student_data_from_email(email_content):
    """
    Extract student data from the email content.
    The email content should have a predictable structure.
    """
    data = {}
    
    # Regular expressions to extract fields
    data["name"] = re.search(r"Your Name:\s*(.*)", email_content).group(1).strip()
    data["email"] = re.search(r"Email:\s*(.*)", email_content).group(1).strip()
    data["phone"] = re.search(r"Phone Number:\s*(.*)", email_content).group(1).strip()
    data["password"] = re.search(r"Password:\s*(.*)", email_content).group(1).strip()
    data["transaction_id"] = re.search(r"Transaction ID:\s*(.*)", email_content).group(1).strip()

    return data

def create_student_user(student_data):
    """
    Create a student user in the database.
    """
    existing_user = User.query.filter_by(email=student_data["email"]).first()
    if existing_user:
        print(f"User with email {student_data['email']} already exists. Skipping.")
        return

    # Create new user
    new_user = User(
        username=student_data["name"],
        email=student_data["email"],
        password=student_data["password"],  # Ensure passwords are hashed in your app
        role="student",
    )
    db.session.add(new_user)
    db.session.commit()
    print(f"User {student_data['name']} created successfully!")

if __name__ == "__main__":
    with app.app_context():
        print("Starting to process emails...")

        # Example: Simulate reading email content
        example_email = """
        Your Name: John Doe
        Email: john.doe@example.com
        Phone Number: 123456789
        Password: secret123
        Transaction ID: ABCD1234
        """

        # Extract student data
        student_data = extract_student_data_from_email(example_email)
        print(f"Extracted Data: {student_data}")

        # Create student user
        create_student_user(student_data)

        print("Finished processing.")
