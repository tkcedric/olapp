from flask import Blueprint, jsonify, request
from functools import wraps
from app.models.content import Topic
#from app import db
from app.models.content import Topic

topics_routes = Blueprint('topics', __name__)

# Middleware to ensure only admins can access certain routes
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_role = request.headers.get("Role")  # Assume role is sent in the header
        if user_role != "admin":
            return jsonify({"error": "Access forbidden: Admins only"}), 403
        return f(*args, **kwargs)
    return decorated_function

# Fetch all topics
# Fetch a single topic by ID
@topics_routes.route('/topics', methods=['GET'])
def get_topics():
    from app.models.content import Topic  # Lazy import
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    topics = Topic.query.paginate(page=page, per_page=per_page)

    return jsonify({
        "topics": [
            {
                "id": topic.id,
                "name": topic.name,
                "description": topic.description,
                "summary": topic.summary,
                "is_free": topic.is_free
            } for topic in topics.items
        ],
        "total": topics.total,
        "pages": topics.pages,
        "current_page": topics.page
    })


# Add a new topic
@topics_routes.route('/topics', methods=['POST'])
@admin_required
def create_topic():
    from app import db  # Lazy import
    from app.models.content import Topic  # Lazy import
    data = request.json
    new_topic = Topic(
        name=data['name'],
        description=data.get('description', ''),
        summary=data.get('summary', ''),
        is_free=data.get('is_free', False)
    )
    db.session.add(new_topic)
    db.session.commit()
    return jsonify({"message": "Topic created successfully!", "id": new_topic.id}), 201

# Update an existing topic
@topics_routes.route('/topics/<int:topic_id>', methods=['PUT'], endpoint='update_topic')
@admin_required
def update_topic(topic_id):
    from flask import request
    from app import db  # Lazy import
    from app.models.content import Topic  # Lazy import

    data = request.json
    topic = Topic.query.get(topic_id)

    if not topic:
        return jsonify({"error": "Topic not found"}), 404

    # Update topic fields
    topic.name = data.get('name', topic.name)
    topic.description = data.get('description', topic.description)
    topic.summary = data.get('summary', topic.summary)
    topic.is_free = data.get('is_free', topic.is_free)

    db.session.commit()

    return jsonify({"message": "Topic updated successfully!"})



# Delete topic by ID
@topics_routes.route('/topics/<int:topic_id>', methods=['DELETE'])
@admin_required
def delete_topic(topic_id):
    from app.models.content import Topic  # Lazy import
    from app import db  # Lazy import
    
    topic = Topic.query.get(topic_id)

    if not topic:
        return jsonify({"error": "Topic not found"}), 404

    db.session.delete(topic)
    db.session.commit()

    return jsonify({"message": "Topic deleted successfully!"})

# Fetch topic details by ID
@topics_routes.route('/topics/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    topic = Topic.query.get(topic_id)
    if not topic:
        return jsonify({"error": "Topic not found"}), 404

    return jsonify({
        "id": topic.id,
        "name": topic.name,
        "description": topic.description,
        "summary": topic.summary
    })