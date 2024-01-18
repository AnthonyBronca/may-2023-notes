from flask import Blueprint, render_template, redirect
from app.forms import SampleForm
from app.data import users

bp = Blueprint("form", __name__, url_prefix="/forms")


@bp.route("/new_user", methods=["GET", "POST"])
def sample_form():
    form = SampleForm()
    if form.validate_on_submit():
        # add additional functionality
        new_user = {"id": len(users) + 1, "name": form.data["name"]}
        users.append(new_user)
        print(users)
        return redirect("/", 302)

    if form.errors:
        print(form.errors)
        return form.errors

    return render_template("form.html", form=form)
