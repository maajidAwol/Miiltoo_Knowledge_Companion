from ..extensions import db
from flask_login import UserMixin
class Books(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_url = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref=db.backref('books', lazy=True))