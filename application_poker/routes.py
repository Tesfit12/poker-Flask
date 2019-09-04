import flask
from application_poker import app
import application_poker.poker_back_end as back_end
import application_poker.forms

@app.route('/poker')
def launch_poker_game():
    cards=back_end.generate_cards(4)
    return flask.render_template('poker.html',cards=cards,players=back_end.players)


@app.route("/",  methods=('GET', 'POST'))
def config_game():
    form=application_poker.forms.ConfigGame()

    if form.validate_on_submit():

        player=back_end.Player(form.name_1.data,int(form.chips_1.data),form.avatar_1.data)
        back_end.players.append(player)

        player=back_end.Player(form.name_2.data,int(form.chips_2.data),form.avatar_2.data)
        back_end.players.append(player)

        player=back_end.Player(form.name_3.data,int(form.chips_3.data),form.avatar_3.data)
        back_end.players.append(player)

        player=back_end.Player(form.name_4.data,int(form.chips_4.data),form.avatar_4.data)
        back_end.players.append(player)


        return flask.redirect(flask.url_for('launch_poker_game'))
    else:
        return flask.render_template('config.html',form=form)




