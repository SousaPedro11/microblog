import os


class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'Pedro@12345'
    SECRET_KEY = os.urandom(16) or 'Pedro@12345'
