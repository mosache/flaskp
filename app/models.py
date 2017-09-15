from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<%s - %s>' % (self.username, self.email)

        # flask-login method
        # def is_autenticated(self):
        #     return True
        #
        # def is_active(self):
        #     return True
        #
        # def is_anonymous(self):
        #     return False
        #
        # def get_id(self):
        #     return str(self.id)
