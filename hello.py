#!/usr/bin/env python3

from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello home page!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    msg = f'<h1>Hello I am {name}</h1>'
    
    return msg, 201, {'Content-Type': 'text/html'}

@app.route('/greet2/<name>/', methods=['POST'])
def greet2(name):
    msg = f'You are meeting {name}'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/users/<name>', methods=['POST'])
def create_user(name):

    msg = f'user {name} created'
    return make_response(msg, 201)

@app.route('/users/<name>', methods=['GET'])
def get_user(name):

    msg = f'Hello {name}'
    return make_response(msg, 200)