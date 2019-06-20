# -*- coding: UTF-8 -*-
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
app.config.from_pyfile('config.py') # To load instance/config.py

db = SQLAlchemy(app)

from .routes.admin import admin
from .routes.index import index

app.register_blueprint(admin)
app.register_blueprint(index)