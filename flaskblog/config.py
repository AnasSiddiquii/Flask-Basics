# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

class Config:
    SECRET_KEY = 'ab1c7263106be15a8cd243a10b5ec8cc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
