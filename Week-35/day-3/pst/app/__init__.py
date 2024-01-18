from flask import Flask, render_template
from app.config import Config
from .forms import SignUpForm

# const express = require('express')


app = Flask(__name__)
# const app = express()
app.config.from_object(Config)  # This connects our config to our app


# Routes


@app.route("/")
def index():
    my_data = {
        "title": "PST Demo!!!",
        "header": "Hello world PST",
        "students": ["bob", "bill", "joe", "jane"],
    }

    return render_template("index.html", data=my_data)


@app.route("/signup")
def signup():
    new_form = SignUpForm()
    if new_form.validate_on_submit():
        return "hello world"
    return render_template("signup.html", new_form=new_form)
