
import bcrypt
from flask import session
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import random
import string
from flask_mail import Mail, Message

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
mail = Mail()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    full_name = db.Column(db.String(120))
    profile_pic = db.Column(db.String(255))
    school_level = db.Column(db.String(50))
    age = db.Column(db.Integer)
    school_name = db.Column(db.String(100))

    def __init__(self, username, password, full_name=None, profile_pic=None, school_level=None, age=None, school_name=None):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.profile_pic = profile_pic
        self.school_level = school_level
        self.age = age
        self.school_name = school_name

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_url = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref=db.backref('books', lazy=True))
#
# import bcrypt
# from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
#
# # Create the SQLAlchemy instance
# db = SQLAlchemy()
# bcrypt = Bcrypt()
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(120), nullable=False)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#
# def register_user(username, password):
#     # Check if the username already exists
#     existing_user = User.query.filter_by(username=username).first()
#
#     if existing_user:
#         # Username already exists, return False to indicate registration failure
#         return False
#
#     # Hash the password before storing it
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#
#     # Create a new user and add it to the database
#     new_user = User(username=username, password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()
#
#     # Return True to indicate successful registration
#     return True
def generate_verification_code():
    return ''.join(random.choice(string.digits) for _ in range(4))

def register_user(username, password):
    # Check if the username already exists
    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        # Username already exists, return False to indicate registration failure
        return False

    # Generate a 4-digit verification code
    verification_code = generate_verification_code()

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user and add it to the database
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Send the verification code to the user's email
    send_verification_email(username, verification_code)

    # Return True to indicate successful registration
    return True

def send_verification_email(email, verification_code):
    msg = Message('Email Confirmation Code', sender='your_email@gmail.com', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)

def login_auth(username, password):
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # Password is correct, allow login
        session['logged_in'] = True
        session['username'] = username
        print(session["username"])
        return True

    # Password is incorrect
    return False



