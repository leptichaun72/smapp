from flask import Blueprint, render_template

primary_bp = Blueprint("primary_blueprint", __name__, template_folder="templates", static_folder="static", static_url_path="/assets")

@primary_bp.route("/")
def index():
    return render_template("form.jade")

@primary_bp.route("/haha")
def haha():
    return render_template("form.jade")
