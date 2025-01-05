from functools import wraps
from flask import request, jsonify

def role_required(roles):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            role = request.headers.get("Role")  # Assume role is sent in headers
            if role not in roles:
                return jsonify({"message": "Permission denied!"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
