# -*- coding: UTF-8 -*-

# Put database models here.
from . import db

class User(db.Model):
    __tablename__='user'
    # columns
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(15))
    telephone = db.Column(db.String(12), primary_key=True, unique=True)
    age = db.Column(db.Integer, default=0)