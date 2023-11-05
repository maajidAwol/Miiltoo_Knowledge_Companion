from ..extensions import db

class UserContest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, db.ForeignKey('user.email'), nullable=False)  # Change to user_email
    contest_id = db.Column(db.Integer, nullable=False)
    biology = db.Column(db.String)  # Data for subject 1
    history = db.Column(db.String)  # Data for subject 2
    chemistry = db.Column(db.String)  # Data for subject 3
    physics = db.Column(db.String)  # Data for subject 4
    registered = db.Column(db.Boolean, default=False)

    def __init__(self, user_email, contest_id,registered):
        self.user_email = user_email
        self.contest_id = contest_id
        self.biology = "biology"
        self.history = "history"
        self.chemistry = "chemistry"
        self.physics = "physics"
        self.registered=registered
