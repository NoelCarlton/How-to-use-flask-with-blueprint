# -*- coding: UTF-8 -*-

# Define a module: admin
from flask import Blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def index():
    return "hello admin"