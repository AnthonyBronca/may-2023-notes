from flask import Blueprint, render_template, redirect
from app.forms import PersonForm
from app.models import db, User

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/users")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = PersonForm()

    # If this is good data
    if form.validate_on_submit():
        # Good code -> database
        new_user = User(
            name=form.data["name"], age=form.data["age"], email=form.data["email"]
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/users")

    #    {name, age, email}
    # Bad data handler
    if form.errors:
        return form.errors

    return render_template("signup.html", form=form)
