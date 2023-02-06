#!/usr/bin/python3
""" Start Flask web application
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
def print_text(text):
        """display <text>
        """
        return "C {}".format(escape(text.replace("_", " ")))

if __name__ == "__main__":
	"""run app on port 5000
	"""
	app.run(debug=True, port=5000, host='0.0.0.0')
