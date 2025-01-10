from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail
from app.db import db

__all__ = ['Lesson', 'Task', 'Topic', 'Progress', 'Question', 'Answer', 'Course', 'User']

# Initialize Flask extensions
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gce_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'gceolcomputerscience@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ubzj ikge lcjl chux'
    app.config['MAIL_DEFAULT_SENDER'] = 'gceolcomputerscience@gmail.com'  # Ensure the sender is set
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register blueprints
    from app.routes.user import user_routes
    from app.routes.topics import topics_routes
    from app.routes.questions import questions_routes
    from app.routes.courses import courses_routes
    from app.routes.lesson import lessons_routes
    from app.routes.editor import editor_routes
    from app.routes.answers import answers_routes
    from app.routes.progress import progress_routes
    from app.routes.email import email_routes

    app.register_blueprint(user_routes, url_prefix='/api')
    app.register_blueprint(topics_routes, url_prefix='/api')
    app.register_blueprint(questions_routes, url_prefix='/api')
    app.register_blueprint(courses_routes, url_prefix='/api')
    app.register_blueprint(lessons_routes, url_prefix='/api')
    app.register_blueprint(editor_routes, url_prefix='/api')
    app.register_blueprint(answers_routes, url_prefix='/api')
    app.register_blueprint(progress_routes, url_prefix='/api')
    app.register_blueprint(email_routes, url_prefix='/api')

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
