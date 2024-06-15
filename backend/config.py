import os
from dotenv import load_dotenv

# read .env file
load_dotenv()

# Path of top-level dir for this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="12435")
    SQLALCHEMY_DB_URI = "sqlite:///books.db"
    SQLALCHEMY_TRACK_MOIDIFCATIONS = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DB_URI = "sqlite:///test.db"


class ProdConfig(Config):
    FLASK_ENV = "production"
