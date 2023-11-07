from flask_login import UserMixin
from ..extensions import db
class User(db.Model, UserMixin):
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
    country = db.Column(db.String(255))
    city = db.Column(db.String(50))
    books= db.relationship('Books',backref='user')
    # user_contests = db.relationship('UserContest', backref='user')

