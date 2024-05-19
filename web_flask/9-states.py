#!/usr/bin/python3
""" Runs a Flask web-app """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Tearsdown SQLAlchemy Session """
    storage.close()


@app.route("/states", strict_slashes=False)
def list_of_states():
    """ Renders an HTML page """
    states = sorted(storage.all(State).values(),
                    key=lambda x: x.name)
    return (render_template("9-states.html", states=states))


@app.route("/states/<id>", strict_slashes=False)
def dynamic_state(id):
    """ Renders an HTML page by id """
    state = next((s for s in storage.all(State).values()
                  if s.id == id), None)
    return (render_template("9-states.html", st=state))


if __name__ == "__main__":
    """ Calls & runs flask app """
    app.run(host="0.0.0.0", port=5000)
