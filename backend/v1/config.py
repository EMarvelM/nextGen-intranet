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

config = Config()
