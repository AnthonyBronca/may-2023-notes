from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length


v = [DataRequired(), Length(3, 12)]


# Class for whatever form this will be called
class PersonForm(FlaskForm):
    name = StringField("Name", v)
    age = IntegerField("Age", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
