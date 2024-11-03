import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'minhasenhaultrasecreta'
