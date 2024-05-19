#!/usr/bin/python3
""" Runs a Flask web-app """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Tearsdown SQLAlchemy Session """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    """ Renders an HTML page """
    states = sorted(storage.all(State).values(),
                    key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda x: x.name)
    return (render_template("10-hbnb_filters.html", states=states,
            amenities=amenities))


if __name__ == "__main__":
    """ Calls & runs flask app """
    app.run(host="0.0.0.0", port=5000)
