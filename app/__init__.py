import os
from flask import Flask
from flask import Blueprint
from flask_restplus import Api
from flask_migrate import Migrate
from app.handlers.http import api as example
from app.resources.database import db
from app.config import config_by_name

def create_app(config=None):
    blueprint = Blueprint('example', __name__, url_prefix='/example')

    api = Api(blueprint,
            title='Example Microservice',
            version='0.0.0',
            description='An example microservice',
            doc='/doc/',
            )
    api.add_namespace(example, path='')


    app = Flask(__name__)

    if config is None:
        config = os.getenv('FLASK_ENV', 'production')

    app.config.from_object(config_by_name[config])

    db.init_app(app)
    # app.app_context().push()

    migrate = Migrate(app, db)

    app.register_blueprint(blueprint)


    return app

