import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy()

db.app = app

db.init_app(app)
if not os.path.exists('telegraph.db'):
    db.create_all()

from . import views