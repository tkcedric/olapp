from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from app import db
import uuid

user_routes = Blueprint('user', __name__)

# Register
@user_routes.route('/register', methods=['POST'])
def register():
    from app.models.user import User
    data = request.json
    role = data.get('role', 'student')
    if role not in ['student', 'admin']:
        return jsonify({"message": "Invalid role!"}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": f"User registered successfully as {role}!"})

# Login
@user_routes.route('/login', methods=['POST'])
def login():
    from app.models.user import User
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required!"}), 400

    user = User.query.filter_by(email=email).first()
    
    if not user:
        print(f"User with email {email} not found.")  # Debugging log
        return jsonify({"message": "Invalid email or password!"}), 401

    if not check_password_hash(user.password, password):
        print(f"Invalid password for user {email}.")  # Debugging log
        return jsonify({"message": "Invalid email or password!"}), 401

    session_token = str(uuid.uuid4())
    user.session_token = session_token
    db.session.commit()

    return jsonify({
        "message": "Login successful!",
        "session_token": session_token,
        "role": user.role
    })

# Logout
@user_routes.route('/logout', methods=['POST'])
def logout():
    from app.models.user import User
    data = request.json
    user = User.query.filter_by(session_token=data.get('session_token')).first()

    if not user:
        return jsonify({"message": "Invalid session token!"}), 401

    user.session_token = None
    db.session.commit()

    return jsonify({"message": "Logout successful!"})

# Get user
@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    print(f"Fetching user with ID: {user_id}")  # Debugging log
    from app.models.user import User
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found!"}), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role
    })

# Fetch all users
@user_routes.route('/users', methods=['GET'])
def get_users():
    from app.models.user import User
    users = User.query.all()
    return jsonify([
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
        for user in users
    ]), 200

# Forgot Password
@user_routes.route('/forgot-password', methods=['POST'])
def forgot_password():
    from app.models.user import User
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({"message": "Email is required!"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User with this email does not exist!"}), 404

    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    reset_token = serializer.dumps(email, salt='password-reset-salt')
    user.reset_token = reset_token
    db.session.commit()

    return jsonify({"message": "Password reset token generated!", "reset_token": reset_token})

# Reset Password
@user_routes.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    from app.models.user import User
    data = request.json
    new_password = data.get('new_password')

    if not new_password:
        return jsonify({"message": "New password is required!"}), 400

    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # Token valid for 1 hour
    except Exception:
        return jsonify({"message": "Invalid or expired token!"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User not found!"}), 404

    user.password = generate_password_hash(new_password, method='pbkdf2:sha256')
    user.reset_token = None
    db.session.commit()

    return jsonify({"message": "Password has been reset successfully!"})
