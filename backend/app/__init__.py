from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.db import db  # Import from the new db.py
from app.models.content import Topic, Question, Answer, Progress, Course, Lesson, CourseProgress
from app.models.user import User
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gce_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    CORS(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes.user import user_routes
    from app.routes.topics import topics_routes
    from app.routes.questions import questions_routes
    from app.routes.courses import courses_routes
    from app.routes.lesson import lessons_routes
    from app.routes.editor import editor_routes
    from app.routes.answers import answers_routes
    from app.routes.progress import progress_routes

    app.register_blueprint(user_routes, url_prefix='/api')
    app.register_blueprint(topics_routes, url_prefix='/api')
    app.register_blueprint(questions_routes, url_prefix='/api')
    app.register_blueprint(courses_routes, url_prefix='/api')
    app.register_blueprint(lessons_routes, url_prefix='/api')
    app.register_blueprint(editor_routes, url_prefix='/api')
    app.register_blueprint(answers_routes, url_prefix='/api')
    app.register_blueprint(progress_routes, url_prefix='/api')

    # Import models and create database tables
    with app.app_context():
        from app.models.user import User
        from app.models.content import Topic, Question, Answer, Progress, Course, Lesson, CourseProgress
        db.create_all()

    return app
