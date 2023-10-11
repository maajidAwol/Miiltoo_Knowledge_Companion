
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
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(120))
    profile_pic = db.Column(db.String(255))
    school_level = db.Column(db.String(50))
    age = db.Column(db.Integer)
    school_name = db.Column(db.String(100))
    verification_code = db.Column(db.String(4))
    verified = db.Column(db.Boolean)

    def __init__(self, email, password, username=None, profile_pic=None, school_level=None, age=None, school_name=None, verified=False,verification_code =None):
        self.email = email
        self.password = password
        self.username = username
        self.profile_pic = profile_pic
        self.school_level = school_level
        self.age = age
        self.school_name = school_name
        self.verified = verified
        self.verification_code = verification_code
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
# def generate_verification_code():
#     return ''.join(random.choice(string.digits) for _ in range(4))
def generate_verification_code():
    first_digit = random.choice(string.digits[1:])  # Choose a digit from 1 to 9
    rest_of_digits = ''.join(random.choice(string.digits) for _ in range(3))
    return first_digit + rest_of_digits
def generate_random_password():
    first_digit = random.choice(string.digits[1:])  # Choose a digit from 1 to 9
    rest_of_digits = ''.join(random.choice(string.digits) for _ in range(5))
    return first_digit + rest_of_digits
def register_user(username, email ,password):
    # Check if the username already exists
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        # Username already exists, return False to indicate registration failure
        return False

    # Generate a 4-digit verification code
    verification_code = generate_verification_code()

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user and add it to the database
    send_verification_email(email, verification_code)
    new_user = User(username=username,email=email, password=hashed_password, verification_code = verification_code)
    db.session.add(new_user)
    db.session.commit()

    # Send the verification code to the user's email


    # Return True to indicate successful registration
    return True

def send_verification_email(email, verification_code):
    msg = Message('Email Confirmation Code', sender='your_email@gmail.com', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)
def send_(email, verification_code):
    msg = Message('Email Confirmation Code', sender='your_email@gmail.com', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)

def login_auth(email, password):
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password) and user.verified:
        # Password is correct, allow login
        session['logged_in'] = True
        session["google_name"] = user.username
        session["google_email"] = email

        return True

    # Password is incorrect
    return False
def send_password(email):
    existing_user = User.query.filter_by(username=email).first()

    if existing_user and existing_user.verified:
        # Username already exists, return False to indicate registration failure
        print()
        password = generate_random_password()
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        existing_user.password = hashed_password
        db.session.commit()
        print("after"+existing_user.password)
        msg = Message('Email Confirmation Code', sender='miltooknowledgecompanion@gmail.com', recipients=[email])
        msg.body = f'Your new password is: {password}'
        mail.send(msg)
        return True
    else:
        return False





