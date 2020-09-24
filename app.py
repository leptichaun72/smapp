from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db_file 
from views.index import primary_bp

application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = db_file
application.register_blueprint(primary_bp)
application.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
db = SQLAlchemy(application)

application.run(debug=True)

