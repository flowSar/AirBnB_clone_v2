#!/usr/bin/python3
"""fetch dada and display it"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
import os

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_data():
    """fetch and display states on html page"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage._DBStorage__session.query(State).all()
        sorted_states = sorted(states, key=lambda state: state.name)
        return render_template('7-states_list.html', states=sorted_states)
    else:
        states = storage.all(State)
        sorted_states = sorted(states.values(), key=lambda state: state.name)
        return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_storage(exception=None):
    """tear down method"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
