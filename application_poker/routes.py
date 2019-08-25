import flask
from application_poker import app
import application_poker.poker_back_end






players=[{'name':'Mike', 'chips':500},{'name':'Brad','chips':50}]
@app.route('/poker')
def launch_poker_game():
    cards=application_poker.poker_back_end.generate_cards(4)
    return flask.render_template('poker.html',cards=cards,players=players)




@app.route('/test')
def test():
    return flask.render_template('test.html')



