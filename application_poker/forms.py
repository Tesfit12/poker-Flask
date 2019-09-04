from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField,SelectField
from wtforms.validators import DataRequired

class ConfigGame(FlaskForm):
    name_1 = StringField('Name', validators=[DataRequired()])
    chips_1 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])
    avatar_1 = RadioField('Avatar', choices=[('avatar_1.png','avatar_1.png'),('avatar_2.png','avatar_2.png')])

    name_2 = StringField('Name', validators=[DataRequired()])
    chips_2 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])

    name_3 = StringField('Name', validators=[DataRequired()])
    chips_3 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])

    name_4 = StringField('Name', validators=[DataRequired()])
    chips_4 = SelectField('Chips', choices=[('1000', '1000 chips'), ('2000', '2000 chips'), ('3000', '3000 chips')], validators=[DataRequired()])



    submit = SubmitField('Start the game')
