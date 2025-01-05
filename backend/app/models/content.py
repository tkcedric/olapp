from app.models.user import User  # Import User model
from app.db import db
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    summary = db.Column(db.Text, nullable=True)
    is_free = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Topic {self.name}>"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    paper_type = db.Column(db.String(50), nullable=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    topic = db.relationship('Topic', backref=db.backref('questions', lazy=True))

    def __repr__(self):
        return f"<Question {self.text[:50]}>"

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question = db.relationship('Question', backref=db.backref('answers', lazy=True))

    def __repr__(self):
        return f"<Answer {self.text}>"

class Task(db.Model):  # Added Task model
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    code_snippet = db.Column(db.Text, nullable=False)
    expected_output = db.Column(db.Text, nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    lesson = db.relationship('Lesson', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f"<Task {self.description}>"

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    total_questions = db.Column(db.Integer, default=0)
    answered_correctly = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    topic = db.relationship('Topic', backref=db.backref('progress', lazy=True))

    def __repr__(self):
        return f"<Progress User {self.user_id} - Topic {self.topic_id}>"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)  # Beginner, Intermediate, Advanced
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Course {self.title}>"

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    course = db.relationship('Course', backref=db.backref('lessons', lazy=True))
    is_free = db.Column(db.Boolean, default=False)  # Indicates if the lesson is free

    def __repr__(self):
        return f"<Lesson {self.title}>"

class CourseProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<CourseProgress User {self.user_id} Lesson {self.lesson_id}>"

class UserAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f"<UserAccess User {self.user_id} Lesson {self.lesson_id}>"
