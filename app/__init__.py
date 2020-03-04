from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.Util import timestamp_to_string
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
app.jinja_env.globals.update(timestamp_to_string=timestamp_to_string)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors
