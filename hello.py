#!/usr/bin/env python3

from flask import Flask, request, make_response, send_file, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello home page!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    msg = f'<h1>Hello I am {name}</h1>'
    
    return msg, 201, {'Content-Type': 'text/html'}

@app.route('/users/<name>', methods=['POST'])
def create_user(name):

    msg = f'user {name} created'
    return make_response(msg, 205)

@app.route('/users/<name>', methods=['GET'])
def get_user(name):

    msg = f'Hello {name}'
    return make_response(msg, 200)

@app.route('/image')
def get_image():

    filename = 'airplane-sunset.jpg'
    return send_file(filename, mimetype='image/jpg')

movies = {
    1: 'Toy Story',
    2: 'Star Wars',
    3: 'Kung Fu Panda',
    4: 'The Lion King',
    5: 'Ip Man'
}

@app.route('/movies')
def get_movies():
    return movies

# converting tuple to json through jsonify func
@app.route('/movie/random')
def random_movie():
    movie = random.choice(list(movies.items()))
    return jsonify(movie)

@app.route('/stache/<animal>')
def listen_animal(animal):
    sound = f'Hear a {animal} roar!'
    print(type(sound))
    return render_template('animals/roar.html', creature=sound)

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.errorhandler(404)
def cant_find_page(err):
    return render_template('404.html'), 404
