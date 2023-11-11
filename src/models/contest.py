from flask_login import UserMixin
from ..extensions import db
from datetime import datetime, timedelta

class Contest(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    contest_id = db.Column(db.String, unique=True, nullable=False)
    contest_data = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_approved = db.Column(db.Boolean, default=False)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)
    title = db.Column(db.String, default="Mock Contest")

    @property
    def is_active(self):
        current_time = datetime.utcnow()
        return self.start_time <= current_time <= self.end_time if self.start_time and self.end_time else False
