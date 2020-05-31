from flask import Flask


def create_app(config_file):

    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    # Inicializa bando de dados
    from graphql_flask.db import db
    from graphql_flask.models import User, Post
    with app.app_context():
        db.init_app(app)
        db.create_all()

    @app.route('/')
    def hello_world():
        return 'Hello from graphql tutorial!'

    # Registra as blueprints
    from graphql_flask.graphql_api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
