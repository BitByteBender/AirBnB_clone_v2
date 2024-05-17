#!usr/bin/python3

from flask import Flask

web_flask = Flask(__name__) 


@web_flask.route('/', strict_slashes=False)
def Hello_Flask():
    return ("Hello HBNB!")


if (__name__ == "__main__"):
    web_flask.run(host="0.0.0.0", port=5000)
