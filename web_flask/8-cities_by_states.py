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

    cities = {}
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage._DBStorage__session.query(State).all()
        for state in states:
            cities[state.name] = []
            print(f"State: {state.name}")
            for city in state.cities:
                cities[state.name] += [city]
    else:
        states = storage.all(State)
        cities = State.cities()
    storage.close()
    return render_template('7-states_list.html', cities=cities)


@app.teardown_appcontext
def close_storage(exception=None):
    """tear down method"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
