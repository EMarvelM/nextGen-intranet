from os import environ
from dotenv import load_dotenv


if load_dotenv('.env'):
    print('ENVIRONMENT LOADED')


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URL')
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'ssl_mode': 'REQUIRED'
        }
    }
    JWT_SECRET_KEY = 'OAL2pry9h84[q3p40t932012]'

config = Config()
