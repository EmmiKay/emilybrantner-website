from flask_mail import Message
from app import mail

def send_email(subject, name, email, message):
    msg = Message(subject, sender=email, recipients=['embrantner@gmail.com'])
    msg.body = message
    mail.send(msg)
