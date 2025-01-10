from flask import Blueprint, request, jsonify, current_app
from flask_mail import Message
from app import mail  # Import `mail` and `app` from your app setup

email_routes = Blueprint('email', __name__)

@email_routes.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    try:
        msg = Message(
            subject="Registration Information",
            recipients=['gceolcomputerscience@gmail.com'],  # Recipient email address
            sender=current_app.config['MAIL_DEFAULT_SENDER'],  # Use default sender here
            body=f"User information:\n{data}"  # Replace with the actual content
        )
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        current_app.logger.error(f"Failed to send email: {e}")
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500
