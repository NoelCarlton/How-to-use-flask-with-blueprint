from .routes.admin import admin
from .routes.index import index
import config
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
app.register_blueprint(admin)
app.register_blueprint(index)