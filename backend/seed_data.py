from app import create_app, db
from app.models.user import User
from app.models.content import Topic, Question, Answer, Course, Lesson

app = create_app()

with app.app_context():
    # Clear existing data (optional, to avoid duplicates)
    db.session.query(User).delete()
    db.session.query(Topic).delete()
    db.session.query(Question).delete()
    db.session.query(Answer).delete()
    db.session.query(Course).delete()
    db.session.query(Lesson).delete()
    db.session.commit()

    # Add sample users
    user1 = User(username="testuser", email="testuser@example.com", password="password")
    db.session.add(user1)

    # Add sample topics
    topic1 = Topic(
        name="Introduction to Programming",
        description="Learn the basics of programming.",
        summary="<p>This topic covers variables, data types, and control structures.</p>",
        is_free=True
    )
    topic2 = Topic(
        name="Data Structures",
        description="Learn about arrays, linked lists, stacks, and queues.",
        summary="<p>Understand how data is organized and manipulated.</p>",
        is_free=False
    )
    db.session.add_all([topic1, topic2])
    db.session.commit()

    # Add sample questions
    question1 = Question(
        text="What is a variable?",
        question_type="MCQ",
        year=2021,
        paper_type="Paper 1",
        topic_id=topic1.id
    )
    question2 = Question(
        text="Explain arrays in programming.",
        question_type="Structural",
        year=2022,
        paper_type="Paper 2",
        topic_id=topic2.id
    )
    db.session.add_all([question1, question2])
    db.session.commit()  # Commit questions to generate IDs

    # Add answers to the MCQ question
    answer1 = Answer(question_id=question1.id, text="A variable is a container for storing data.", is_correct=True)
    answer2 = Answer(question_id=question1.id, text="A variable is a type of function.", is_correct=False)
    db.session.add_all([answer1, answer2])
    db.session.commit()

    # Add sample courses
    course1 = Course(
        title="Introduction to Python",
        level="Beginner",
        description="Learn the basics of Python programming."
    )
    db.session.add(course1)
    db.session.commit()  # Commit course to generate ID

    # Add lessons to the course
    lesson1 = Lesson(
        title="Variables and Data Types",
        content="<p>Learn about variables and data types in Python.</p>",
        course_id=course1.id
    )
    lesson2 = Lesson(
        title="Control Structures",
        content="<p>Learn about if-else statements and loops in Python.</p>",
        course_id=course1.id
    )
    db.session.add_all([lesson1, lesson2])
    db.session.commit()

    print("Database seeded with sample users, topics, questions, and courses!")
