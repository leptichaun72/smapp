from flask import Flask
from views.index import primary_bp

application = Flask(__name__)
application.register_blueprint(primary_bp)
application.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

application.run(debug=True)

