import os
from graphql_flask.app import create_app


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = create_app(basedir + '/config.py')
    app.run()
