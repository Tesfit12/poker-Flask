import flask
from application_poker import app
import application_poker.poker_back_end

@app.route('/')
def index():
    return flask.render_template('test.html')


@app.route('/poker')
def launch_poker_game():
    cards=application_poker.poker_back_end.generate_cards(4)



    return flask.render_template('poker.html',cards=cards)

