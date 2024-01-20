from flask import Flask
from .config import Config
from .routes import main
from .models import db

# Config section
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main.bp)

# database connection

# db.init_app(app)
db.init_app(app)
