from ..extensions import db

class UserContest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, db.ForeignKey('user.email'), nullable=False)  # Change to user_email
    # user = db.relationship('User', backref='contests', foreign_keys=[user_email])
    # contest_user = db.relationship('User', backref='contests', foreign_keys=[user_email])
    contest_id = db.Column(db.Integer, nullable=False)
    biology = db.Column(db.Integer, nullable=True)  # Data for subject 1
    history = db.Column(db.Integer, nullable=True)  # Data for subject 2
    chemistry = db.Column(db.Integer, nullable=True)  # Data for subject 3
    geography = db.Column(db.Integer, nullable=True)  # Data for subject 4
    total = db.Column(db.Integer, nullable=True)
    registered = db.Column(db.Boolean, default=False)
    finished_contest = db.Column(db.Boolean, default=False)

    def __init__(self, user_email, contest_id,registered):
        self.user_email = user_email
        self.contest_id = contest_id
        self.registered=registered
