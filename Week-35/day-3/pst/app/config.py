import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "blehbleh"
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    # const secretKey = process.env.SECRET_KEY
