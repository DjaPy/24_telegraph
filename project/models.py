from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Story(db.Model):

    slug = db.Column(db.String(32), primary_key=True)
    story_title = db.Column(db.String(128))
    story_signature = db.Column(db.String(64))
    story_body = db.Column(db.Text)
    author_id = db.Column(db.String(64))
    story_uuid = db.Column(db.String(128))


    def __repr__(self):
        return '<Story {}>'.format(self.story_title)