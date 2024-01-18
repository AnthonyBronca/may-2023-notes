# const express = require('express)
from flask import Flask, render_template
from app.config import Config
from .data.users import users
from .routes import forms, main


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(routes.forms.bp)
app.register_blueprint(routes.main.bp)
