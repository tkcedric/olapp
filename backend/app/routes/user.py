from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import uuid

user_routes = Blueprint('user', __name__)

@user_routes.route('/register', methods=['POST'])
def register():
    from app.models.user import User  # Import here to avoid circular import
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@user_routes.route('/login', methods=['POST'])
def login():
    from app.models.user import User  # Import here to avoid circular import
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Invalid email or password!"}), 401

    # Generate a session token
    session_token = str(uuid.uuid4())
    user.session_token = session_token
    db.session.commit()

    return jsonify({"message": "Login successful!", "session_token": session_token})
