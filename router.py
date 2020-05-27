from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/<book>')
def index(book=None):
    return 'My book is ' + book

@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
  return 'Hello ' + first_name + ',' + last_name

@app.route('/user/<username>')
def show_user_profile(username):
    print type(username)
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    print type(post_id)
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    print type(subpath)
    # show the subpath after /path/
    return 'Subpath %s' % subpath

app.run(debug=True)