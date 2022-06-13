from app import db
from datetime import datetime

class Messages(db.Model):
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), primary_key=True)
    subject = db.Column(db.String(120))
    message = db.Column(db.String(1000))
    creation_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
