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


@app.route("/states_list", strict_slashes=False)
def list_of_states():
    """ Renders an HTML page """
    sts = sorted(storage.all(State).values(),
                    key=lambda x: x.name)
    return (render_template("7-states_list.html", sts=sts))


if __name__ == "__main__":
    """ Calls & runs flask app """
    app.run(host="0.0.0.0", port=5000)
