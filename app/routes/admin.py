# -*- coding: UTF-8 -*-

# Define a module: admin
from flask import Blueprint
from .. import app, db
from .. import models

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def index():
    user = models.User(
        name = 'username',
        telephone = '12345678909',
        age = 23,
    )
    db.session.add(user)
    db.session.commit()
    return "hello admin"