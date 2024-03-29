from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignUpForm(FlaskForm):
    username = StringField(
        "username",
    )
    password = PasswordField("password")
    submit_button = SubmitField("Submit me!!!")
