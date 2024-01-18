from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

# v = [DataRequired()]


class SampleForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(3, 10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 12)])
    submit = SubmitField("Submit")
