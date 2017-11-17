from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(64), index=True)
    slug = db.Column(db.String(32))
    story_title = db.Column(db.String(128))
    story_signature = db.Column(db.String(64))
    story_body = db.Column(db.Text)

    def __repr__(self):
        return '<Story {}>'.format(self.story_title)