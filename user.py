
import bcrypt
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy instance
db = SQLAlchemy()
bcrypt = Bcrypt()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

def register_user(username, password):
    # Check if the username already exists
    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        # Username already exists, return False to indicate registration failure
        return False

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user and add it to the database
    new_user = User(full_name=username,username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Return True to indicate successful registration
    return True
def login_auth(username, password):
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # Password is correct, allow login
        return True

    # Password is incorrect
    return False


