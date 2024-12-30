from app import create_app, db
from app.models.user import User  # Ensure this is imported to initialize the table

app = create_app()

# Initialize the database
with app.app_context():
    db.create_all()  # This ensures the database and tables are created

if __name__ == "__main__":
    app.run(debug=True)
