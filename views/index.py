from flask import Blueprint, \
                  render_template, \
                  request, \
                  redirect, \
                  url_for

primary_bp = Blueprint("primary_blueprint", __name__, template_folder="templates", static_folder="static", static_url_path="/assets")

@primary_bp.route("/")
def index():
    return render_template("index.jade")

@primary_bp.route("/dummy")
def dummy():
    return render_template("dummy.jade")

