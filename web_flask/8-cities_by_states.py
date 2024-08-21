#!/usr/bin/python3
"""fetch dada and display it"""
from flask import Flask, request, render_template
from models import storage
# from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
import os

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_data():

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        all_states = storage._DBStorage__session.query(State).all()
        states = {}
        for state in all_states:
            states[state.name] = state         
    else:
        states = storage.all(State)
    storage.close()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_storage(exception=None):
    """tear down method"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
