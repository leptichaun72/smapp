@@@app.py

from flask import Flask
from config import db_file 
from views.index import db, primary_bp

application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = db_file
application.register_blueprint(primary_bp)
application.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
#db = SQLAlchemy(application)
db.init_app(application)
with application.app_context():
    db.create_all()

application.run(debug=True)


@@@config.py
import os
from pytz import timezone

#define Eastern timezone
eastern = timezone('US/Eastern')

project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(project_dir, "toilet.db"))


@@@models.py
#from database import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Broker(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),unique=True,nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),nullable=True)

#class Stock(db.Model):
#    id = db.Columm(db.Integer,primary_key=True)
#    name = db.Column(db.Text,unique=True)
#    symbol = db.Column(db.String(8),unique=True,nullable=False)
#    lots = db.relationship("Lot


@@@views/index.py
#from flask import Blueprint,render_template,request,redirect,url_for

#import sys
#import os
#sys.path.append(os.getcwd() + '/..')

from models import db, Broker
print(Broker)
print(db)

from flask import Blueprint, \
    render_template, \
    request, \
    redirect, \
    url_for

primary_bp = Blueprint("primary_blueprint", __name__, template_folder="templates", static_folder="static", static_url_path="/assets")

@primary_bp.route("/")
def index():
    rob = Broker(name="bobbyhod")
    db.session.add(rob)
    db.session.commit()
    return "i am pOnee!!"

