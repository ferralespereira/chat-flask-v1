from wtforms import Form, StringField, validators


class LoginForm(Form):
    """name"""
    name = StringField('Username', [validators.DataRequired(), validators.Length(min=3, max=15), validators.Regexp(r'^[\w.@+-]+$') ])
