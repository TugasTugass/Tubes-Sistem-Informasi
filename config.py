import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/tokokuefauzia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
