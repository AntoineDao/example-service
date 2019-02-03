import uuid
from flask import abort
from app.resources.database import Example, db
from sqlalchemy import or_


def get_all_examples():
    return Example.query.all()

def get_example(public_id):
    example = Example.query.filter_by(id=public_id).first()
    if not example:
        return abort(404)
    return example

def save_example(data):
    new = Example.query.filter(or_(Example.email.like(data['email']),
                                 Example.username.like(data['username']))).first()
    print(new)
    if new is not None:
        return abort(400, 'username or email already taken')

    new = Example.from_dict(data)
    db.session.add(new)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()
        raise

    return new, 201
