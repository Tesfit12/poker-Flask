import flask
from application_poker import app
import application_poker.poker_back_end
import application_poker.forms

players=[{'name':'Mike', 'chips':500},{'name':'Brad','chips':50}]
@app.route('/poker')
def launch_poker_game():
    cards=application_poker.poker_back_end.generate_cards(4)
    return flask.render_template('poker.html',cards=cards,players=players)


@app.route("/",  methods=('GET', 'POST'))
def config_game():
    form=application_poker.forms.ConfigGame()

    if form.validate_on_submit():
        return flask.redirect(flask.url_for(''))
    else:
        return flask.render_template('config.html',form=form)




