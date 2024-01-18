from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SampleForm(FlaskForm):
    name = StringField("name")
    password = PasswordField("password")
    submit = SubmitField("Submit")
    # input field for names
    # password field for password
    # submit field
