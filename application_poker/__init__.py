import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'SDFwsdfdhDFG'

from application_poker import routes
