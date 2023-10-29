from flask_login import UserMixin
from ..extensions import db
from datetime import datetime
class Contest(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    subject =db.Column(db.String)
    contest_data = db.Column(db.String)  # Store JSON data as a string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_approved = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False)
