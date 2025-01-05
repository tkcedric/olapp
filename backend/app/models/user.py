from app.db import db
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='student')
    session_token = db.Column(db.String(255), nullable=True)
    reset_token = db.Column(db.String(255), nullable=True)  # Added field for password reset

    def generate_reset_token(self):
        """Generate a reset token for the user."""
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(self.email, salt='password-reset-salt')

    @staticmethod
    def verify_reset_token(token):
        """Verify and decode a reset token."""
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # Token valid for 1 hour
        except Exception:
            return None
        return email
