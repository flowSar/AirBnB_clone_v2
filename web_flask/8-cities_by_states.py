#!/usr/bin/python3
"""fetch dada and display it"""
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_data():
    from models import storage
    from models.state import State
    from models.city import City
    cities = storage.all(City)
    states = storage.all(State)
    storage.close()
    return render_template('7-states_list.html', states=states, cities=cities)

@app.teardown_appcontext
def close_storage(exception=None):
    """tear down method"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
