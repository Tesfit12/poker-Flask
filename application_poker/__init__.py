import flask

app = flask.Flask(__name__)

from application_poker import routes
