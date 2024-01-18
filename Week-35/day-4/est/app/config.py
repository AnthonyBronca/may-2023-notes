import os

# This os thing lets us read system data


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    # const SECRET_KEY = process.env.SECRET_KEY
