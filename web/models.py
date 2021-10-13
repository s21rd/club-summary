from datetime import datetime
from web import db


class Clubs(db.Model):
    __tablename__ = "clubs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    first_tweet = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def __init__(self, name=None, first_tweet=None):
        self.name = name
        self.first_tweet = first_tweet
        self.created_at = datetime.now()


def init():
    db.create_all()
