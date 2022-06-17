from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    # name = StringField('Nickname', validators=[DataRequired()])
    # room = StringField('Room', validators=[DataRequired()])
    # submit = SubmitField('Enter Chatroom')

    name = StringField('Username', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remeber Me')
