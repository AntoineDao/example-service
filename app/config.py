import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DB_NAME = os.getenv('DB_NAME', 'example')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_PORT = os.getenv('DB_PORT', 5432)
    DB_SERVER = os.getenv('DB_SERVER', 'localhost')
    SQLALCHEMY_DATABASE_URI =\
        'postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}'\
        .format(db_user=DB_USER, db_password=DB_PASSWORD, db_server=DB_SERVER,
                db_port=DB_PORT, db_name=DB_NAME)


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'

    DEBUG = True
    SQLALCHEMY_DATABASE_URI =\
        "postgresql://postgres@/{db_name}"\
        .format(db_name=Config.DB_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DB_NAME = "test"

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI =\
        "postgresql://postgres@/{db_name}"\
        .format(db_name=DB_NAME)

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)
