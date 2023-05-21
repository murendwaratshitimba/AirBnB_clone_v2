#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def is_fun(text):
    """C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def is_magic(text='is cool'):
    """ “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def is_fun(n):
    """ “n is a number” only if n is an integer"""
    return f"{n:d}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
