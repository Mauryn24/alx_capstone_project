# Import the Flask class from the flask module
from flask import Flask

# Import the render_template function from the flask module
from flask import render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

if (__name__ == '__main__'):
    app.run(debug=True)