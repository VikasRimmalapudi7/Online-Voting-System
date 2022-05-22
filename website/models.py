from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    aadhar = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    isvoted=db.Column(db.Boolean,default=False,nullable=False)


class Nominnes(db.Model):
    __tablename__='nominnes'
    id = db.Column(db.Integer, primary_key=True)
    candidate_name = db.Column(db.String(150),unique=True)
    votes=db.Column(db.Integer,default=0)

    
    
    
