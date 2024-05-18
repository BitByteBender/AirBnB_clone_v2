#!/usr/bin/python3
"""
    Import Flask class from flask module
    Flask app instance creation
"""
from flask import Flask, render_template
web_flask = Flask(__name__)


@web_flask.route('/', strict_slashes=False)
def main_route():
    """
        Returns a string as a response
    """
    return ("Hello HBNB!")


@web_flask.route("/hbnb", strict_slashes=False)
def second_route():
    """
        Returns a string as a response
    """
    return ("HBNB")


@web_flask.route("/c/<var>", strict_slashes=False)
def dynamic_route(var):
    """
        Returns a string based on var as a response
        replaces underscore with a space
    """
    var = var.replace('_', ' ')
    return ("C " + str(var))


@web_flask.route("/python", strict_slashes=False)
@web_flask.route("/python/", strict_slashes=False)
def default_route():
    """
        Returns a default  string
    """
    return ("Python is cool")


@web_flask.route("/python/<var>", strict_slashes=False)
def extra_dynamic_route(var):
    """
        Returns a string based on var as a response
        replaces underscore with a space
    """
    var = var.replace('_', ' ')
    return ("Python " + str(var))


@web_flask.route("/number/<int:n>", strict_slashes=False)
def third_route(n):
    """
        Returns an integer based on n as a response
    """
    return (str(n) + " is a number")


@web_flask.route("/number_template/<int:n>", strict_slashes=False)
def number_tmplt_route(n):
    """
        Renders an HTML page if n is an integer
    """
    return render_template("5-number.html", n=n)


@web_flask.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even_route(n):
    """
        Renders an HTML page with an odd or even
    """
    fpath = '6-number_odd_or_even.html'
    if (n % 2 == 0):
        return render_template(fpath, num=n, num_check="even")
    else:
        return render_template(fpath, num=n, num_check="odd")


if __name__ == "__main__":
    """
        Runs the Flask app
    """
    web_flask.run(host="0.0.0.0", port=5000)
