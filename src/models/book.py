from ..extensions import db
from flask_login import UserMixin
class Books(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_email=db.Column(db.String,db.ForeignKey('user.email'))
    book_name=db.Column(db.String(255), nullable=False)
    book_url = db.Column(db.String(255), nullable=False)
    txt_url=db.Column(db.String(255),nullable=False)