from app import db
from datetime import datetime

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_entry= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Time: {self.id}, {self.date_entry}>'   
