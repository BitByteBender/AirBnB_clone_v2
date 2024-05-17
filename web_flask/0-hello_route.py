#!usr/bin/python3
""" Import Flask class from flask module """
from flask import Flask
""" Flask app instance creation """
web_flask = Flask(__name__)


@web_flask.route('/', strict_slashes=False)
def Hello():
    """ Returns a string as a response """
    return ("Hello HBNB!")


if __name__ == "__main__":
    """ Runs the Flask app """
    web_flask.run(host='0.0.0.0', port=5000)
