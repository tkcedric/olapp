from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    # Register blueprints
    from app.routes.user import user_routes
    app.register_blueprint(user_routes, url_prefix='/user')

    return app
