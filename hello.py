#!/usr/bin/env python3

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello home page!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    msg = f'Hello I am {name}'
    
    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

