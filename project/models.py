from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Story(db.Model):
    slug = db.Column(db.String(32), primary_key=True)