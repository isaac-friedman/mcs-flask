import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'there will be a 128-bit random string here at some point'
    TESTING = False 
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
