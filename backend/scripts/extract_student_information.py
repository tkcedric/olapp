import imaplib
import email
import json

# Email account credentials
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
IMAP_SERVER = "imap.gmail.com"

def extract_student_data():
    # Connect to email server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    # Search for unread emails
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()

    students = []

    for email_id in email_ids:
        # Fetch email data
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg["subject"]
                from_email = msg["from"]

                if "Student Registration" in subject:
                    # Parse the email content
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                student_data = parse_student_email(body)
                                if student_data:
                                    students.append(student_data)

    # Save to a JSON file
    with open("scripts/students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Extracted student information saved to 'students.json'.")

def parse_student_email(body):
    # Extract student data from email body
    try:
        lines = body.split("\n")
        student = {}
        for line in lines:
            if "Name:" in line:
                student["name"] = line.split(":")[1].strip()
            elif "Email:" in line:
                student["email"] = line.split(":")[1].strip()
            elif "Password:" in line:
                student["password"] = line.split(":")[1].strip()
        return student
    except Exception as e:
        print(f"Error parsing email: {e}")
        return None

if __name__ == "__main__":
    extract_student_data()
