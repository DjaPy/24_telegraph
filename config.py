import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.abspath(os.path.join(BASEDIR, 'test.db'))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_DIR
SQLALCHEMY_TRACK_MODIFICATIONS = False