#!/usr/bin/python3
"""web flask application extract subpath"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello2():
    return 'HBNB'


@app.route('/c/<path:subpath>', strict_slashes=False)
def hello3(subpath):
    text = subpath.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<path:subpath>', strict_slashes=False)
def hello4(subpath=None):
    if not subpath:
        return 'Python is cool'
    else:
        text = subpath.replace('_', ' ')
        return f'Python {text}'


@app.route('/number/<int:subpath>', strict_slashes=False)
def hello5(subpath=None):
    return f'{subpath} is a number'


@app.route('/number_template/<int:subpath>')
@app.route('/number_odd_or_even/<int:subpath>')
def display(subpath):
    if 'number_template' in request.path:
        return render_template('5-number.html', number=subpath)
    elif 'number_odd_or_even' in request.path:
        return render_template('6-number_odd_or_even.html', number=subpath)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
