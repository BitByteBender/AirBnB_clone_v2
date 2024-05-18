#!/usr/bin/python3
"""
    Import Flask class from flask module
    Flask app instance creation
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """
        Returns a string as a response
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """
        Runs the Flask app
    """
    app.run(host='0.0.0.0', port=5000)
