from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField,SelectField
from wtforms.validators import DataRequired

class ConfigGame(FlaskForm):

    name_1 = StringField('Name', validators=[DataRequired()])
    chips_1 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])
    avatar_1 = RadioField('Avatar', choices=[('avatar_1.png','avatar_1.png'),('avatar_2.png','avatar_2.png'),('avatar_3.png','avatar_3.png'),('avatar_4.png','avatar_4.png'),('avatar_5.png','avatar_5.png')])

    name_2 = StringField('Name', validators=[DataRequired()])
    chips_2 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])
    avatar_2 = RadioField('Avatar', choices=[('avatar_1.png','avatar_1.png'),('avatar_2.png','avatar_2.png'),('avatar_3.png','avatar_3.png'),('avatar_4.png','avatar_4.png'),('avatar_5.png','avatar_5.png')])


    name_3 = StringField('Name', validators=[DataRequired()])
    chips_3 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])
    avatar_3 = RadioField('Avatar', choices=[('avatar_1.png','avatar_1.png'),('avatar_2.png','avatar_2.png'),('avatar_3.png','avatar_3.png'),('avatar_4.png','avatar_4.png'),('avatar_5.png','avatar_5.png')])


    name_4 = StringField('Name', validators=[DataRequired()])
    chips_4 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])
    avatar_4 = RadioField('Avatar', choices=[('avatar_1.png','avatar_1.png'),('avatar_2.png','avatar_2.png'),('avatar_3.png','avatar_3.png'),('avatar_4.png','avatar_4.png'),('avatar_5.png','avatar_5.png')])



    submit = SubmitField('Start the game')

class MoveNext(FlaskForm):
    submit = SubmitField('Move to Next Player')
