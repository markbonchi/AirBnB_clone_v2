#!/usr/bin/python3
""" 
Flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes:
	/: display "Hello HBNB!"
	/hbnb: display "HBNB"
	/c/<text>: display "C ", followed by the value of the text variable (replace underscore _ symbols with a space )
	/python/(<text>): display "Python ", followed by the value of the text variable (replace underscore _ symbols with a space )
	    +The default value of text is "is cool"
	/number/<n>: display "n is a number" only if n is an integer
	/number_template/<n>: display a HTML page only if n is an integer:
	    +H1 tag: "Number: n" inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from flask import render_template
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
def Python(text):
    """display  python followed by <text>
    """
    return "Python {}".format(escape(text.replace("_", " ")))

@app.route('/number/<int:n>')
def number(n):
    """display n if type(int)
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """display HTML page if n is type(int)
    """
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """display HTML page if <int:n> is even or odd
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
	"""run app on port 5000
	"""
	app.run(debug=True, port=5000, host='0.0.0.0')
