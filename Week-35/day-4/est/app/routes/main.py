from flask import Blueprint, render_template
from app.data import users

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    site_info = {
        "title": "Flask + Jinja",
        "header": "Users",
        "users": users,
    }

    return render_template("index.html", site_info=site_info)


@bp.route("/<int:id>")
def user(id):
    for user in users:
        if user["id"] == int(id):
            current_user = user

    return render_template("user.html", user=current_user)
