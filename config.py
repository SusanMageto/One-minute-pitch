# from logging import DEBUG
import os


class Config:

    '''
    Describes the general configurations
    '''
    SECRET_KEY = 'SECRET_KEY'

    
    # DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # emails configuration

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):

    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql://icaxmzfybmixos:01a81413e95891fd7b8d8e628adf2a3ed42abace20edd806f6e53ee6925717dd@ec2-52-86-56-90.compute-1.amazonaws.com:5432/d7fomhk6lof5t8?sslmode=require"
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",)




class DevConfig(Config):

    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitches'
    
    DEBUG=True
    



class TestConfig(Config):

    '''
    Test configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''


    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:password@localhost/pitchweb'
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
