from flask import Blueprint
from flask_graphql import GraphQLView
from graphql_flask.schemas import schema_query, schema_mutation


api = Blueprint('graphql', __name__)

api.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema_query, graphiql=True
))

api.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
    'graphql-mutation',
    schema=schema_mutation, graphiql=True
))
