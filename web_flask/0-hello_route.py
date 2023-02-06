#!/usr/bin/python3
""" Start Flask web application
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
	"""route display
	"""
	return "Hello HBNB!"

if __name__ == "__main__":
	"""run app on port 5000
	"""
	app.run(debug=True, port=5000, host='0.0.0.0')
