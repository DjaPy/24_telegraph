import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.path.curdir)


SQLALCHEMY_DATABASE_URI = 'sqlite:///telegraph.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False