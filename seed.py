import os
from graphql_flask.app import create_app
from graphql_flask.db import db
from graphql_flask.models import User, Post


def seed():

    user1 = User(
        name="Renato Aragorn",
        email="aragorn@teste.com"
    )

    post1 = Post()
    post1.title = "Título do post"
    post1.body = "Conteúdo do post"
    post1.author = user1

    db.session.add(post1)
    db.session.add(user1)
    db.session.commit()

    print(User.query.all())
    print(Post.query.all())


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = create_app(basedir + '/config.py')
    with app.app_context():
        seed()
