# config.py

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:myPassword@localhost:5432/botpostdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
