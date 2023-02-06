#!/usr/bin/python3
""" Flask web application
"""



from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    """route display
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """route display
    """
    return "HBNB"

@app.route('/c/<text>')
def print_C(text):
    """display C followed by <text>
    """
    return "C {}".format(escape(text.replace("_", " ")))

@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def print_Python(text):
    """display  python followed by <text>
    """
    return "Python {}".format(escape(text.replace("_", " ")))

@app.route('/number/<int:n>')
def print_int(n):
    """display n if type(int)
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
	"""run app on port 5000
	"""
	app.run(debug=True, port=5000, host='0.0.0.0')
