from app import create_app, db
from app.models.content import Lesson, Course

app = create_app()

with app.app_context():
    # Delete all existing lessons
    print("Deleting existing lessons...")
    db.session.query(Lesson).delete()
    db.session.commit()
    print("All previous lessons have been deleted.")
    
    # Define Beginner and Intermediate courses
    beginner_course = Course(
        title="Python for Beginners",
        level="Beginner",
        description="Learn Python from scratch with hands-on examples and exercises."
    )
    intermediate_course = Course(
        title="Python Intermediate",
        level="Intermediate",
        description="Enhance your Python skills with advanced concepts and real-world scenarios."
    )
    db.session.add_all([beginner_course, intermediate_course])
    db.session.commit()

    # Beginner Lessons
    beginner_lessons = [
        Lesson(
            title="Introduction to Python",
            content="""
                ### Objectives:
                1. Understand what Python is and its use cases.
                2. Set up the Python environment and write your first program.

                ### Problem Situation:
                **Context:** A student wants to learn how to automate tasks using Python.
                **Task:** Install Python, write a program to print "Hello, World!", and explore Python's features.
                **Directive:** Write a program that displays "Hello, World!".

                ### Lesson Content:
                ```python
                print("Hello, World!")
                ```

                ### Jeux Bilingue:
                1. Python - Python
                2. Automation - Automatisation
                3. Task - Tâche
                4. Program - Programme
                5. Output - Sortie
            """,
            course_id=beginner_course.id,
            is_free=True  # Marked as free
        ),
        Lesson(
            title="Variables and Data Types",
            content="""
                ### Objectives:
                1. Learn how to declare and use variables.
                2. Understand different data types in Python.

                ### Problem Situation:
                **Context:** A teacher wants to store students' scores for a test in variables.
                **Task:** Write a program that stores a student's name, test score, and grade.
                **Directive:** Use variables to hold data and print them.

                ### Lesson Content:
                ```python
                student_name = "Alice"
                test_score = 95
                grade = "A"

                print(f"Student: {student_name}, Score: {test_score}, Grade: {grade}")
                ```

                ### Jeux Bilingue:
                1. Variable - Variable
                2. Data - Donnée
                3. Score - Score
                4. Grade - Note
                5. Print - Imprimer
            """,
            course_id=beginner_course.id,
            is_free=True  # Marked as free
        ),
        # Add more lessons here, marking some as paid
        Lesson(
            title="Control Structures: Conditionals",
            content="""
                ### Objectives:
                1. Learn how to use `if`, `else`, and `elif` statements.
                2. Write programs with conditional logic.

                ### Problem Situation:
                **Context:** A shopkeeper wants to provide discounts to customers based on their total purchase amount.
                **Task:** Write a program to calculate the discount based on the purchase amount.
                **Directive:** Use conditional statements to determine the discount.

                ### Lesson Content:
                ```python
                total_amount = 120

                if total_amount > 100:
                    discount = 10
                elif total_amount > 50:
                    discount = 5
                else:
                    discount = 0

                print(f"Discount: {discount}%")
                ```

                ### Jeux Bilingue:
                1. Condition - Condition
                2. Discount - Remise
                3. Purchase - Achat
                4. Amount - Montant
                5. Logic - Logique
            """,
            course_id=beginner_course.id,
            is_free=False  # Paid content
        ),
    ]

    # Intermediate Lessons
    intermediate_lessons = [
        Lesson(
            title="Object-Oriented Programming (OOP)",
            content="""
                ### Objectives:
                1. Understand the principles of OOP (Encapsulation, Inheritance, Polymorphism).
                2. Create classes and objects in Python.

                ### Problem Situation:
                **Context:** A software company needs to create a library system to manage books and authors.
                **Task:** Use classes to define a `Book` and `Author`.
                **Directive:** Write a program to manage books and authors using OOP.

                ### Lesson Content:
                ```python
                class Book:
                    def __init__(self, title, author):
                        self.title = title
                        self.author = author

                    def display_info(self):
                        print(f"Title: {self.title}, Author: {self.author}")

                book1 = Book("Python Basics", "John Doe")
                book1.display_info()
                ```

                ### Jeux Bilingue:
                1. Object - Objet
                2. Class - Classe
                3. Inheritance - Héritage
                4. Polymorphism - Polymorphisme
                5. Encapsulation - Encapsulation
            """,
            course_id=intermediate_course.id,
            is_free=False  # Paid content
        ),
        # Add more lessons here
    ]

    # Save all lessons to the database
    db.session.add_all(beginner_lessons + intermediate_lessons)
    db.session.commit()

    print("All lessons have been successfully populated into the database!")
