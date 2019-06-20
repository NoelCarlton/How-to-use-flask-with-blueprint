from flask import Flask
from . import config
from .app import admin, index

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
app.config.from_pyfile('config.py')
app.register_blueprint(admin.admin)
app.register_blueprint(index.app)