from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """name"""
    name = StringField('Username', validators=[DataRequired()])
