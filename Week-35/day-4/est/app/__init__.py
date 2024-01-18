# const express = require('express)
from flask import Flask, render_template
from app.config import Config
from .forms import SampleForm
from .data.users import users

# const app = express()

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    site_info = {
        "title": "Flask + Jinja",
        "header": "Users",
        "users": users,
    }

    return render_template("index.html", site_info=site_info)


@app.route("/form")
def sample_form():
    form = SampleForm()
    if form.validate_on_submit():
        return "Hello World"
    return render_template("form.html", form=form)


"""

app.route("/", (req,res) => {
    res.send("Hello world")

})
"""
