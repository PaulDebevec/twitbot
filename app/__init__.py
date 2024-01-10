# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import botpost_controller
app.register_blueprint(botpost_controller.bp)

# Add this line to initialize Flask-WTF
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
