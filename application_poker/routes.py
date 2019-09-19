import flask
from application_poker import app
import application_poker.poker_back_end as back_end
import application_poker.forms

@app.route('/poker', methods=('GET', 'POST'))
def launch_poker_game():
    form = application_poker.forms.MoveNext()
    if form.validate_on_submit():
        back_end.Player.move_to_next_player(back_end.players)
        print("Next is {}".format(back_end.Player.active_player))

    cards=back_end.generate_cards(3)
    return flask.render_template('poker_game.html',players=back_end.players,cards=cards, Player=back_end.Player, form=form)


@app.route("/",  methods=('GET', 'POST'))
def config_game():
    form=application_poker.forms.ConfigGame()

    if form.validate_on_submit():
        back_end.players=[]

        player=back_end.Player(form.name_1.data,int(form.chips_1.data),form.avatar_1.data,1)
        back_end.players.append(player)

        player=back_end.Player(form.name_2.data,int(form.chips_2.data),form.avatar_2.data,2)
        back_end.players.append(player)

        player=back_end.Player(form.name_3.data,int(form.chips_3.data),form.avatar_3.data,3)
        back_end.players.append(player)

        player=back_end.Player(form.name_4.data,int(form.chips_4.data),form.avatar_4.data,4)
        back_end.players.append(player)


        return flask.redirect(flask.url_for('launch_poker_game'))
    else:
        return flask.render_template('config.html',form=form)




