import os
import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
import app

db = SQLAlchemy()


class Example(db.Model):
    """ Example Model for storing example related details """
    __tablename__ = "example"

    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    admin = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    test = db.Column(db.String(100))


    def __repr__(self):
        return "<User '{}'>".format(self.username)

    @classmethod
    def from_dict(cls, data):
        new = cls(
            id=data.get('id'),
            email=data.get('email'),
            admin=data.get('admin'),
            username=data.get('username')
        )
        return new
