from app import app, db, User, Product
from werkzeug.security import generate_password_hash

def reset_database():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        print("✅ Dropped all tables")
        
        # Create all tables
        db.create_all()
        print("✅ Created fresh tables")

if __name__ == '__main__':
    reset_database()