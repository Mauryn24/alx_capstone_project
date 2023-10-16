from app import app
# import app decorators from app pakage

from flask import render_template, url_for
# Import the Flask class from the flask module

# Import User and Workout models from models.py
from app.models import User, Workout  # Import User and Workout models from models.py



# Define a route for the root URL ("/")
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile/')
def profile():
    return render_template('profile.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

@app.route('/auth/login/')
def login():
    return render_template('auth/login.html')

@app.route('/auth/signUp/')
def signUp():
    return render_template('auth/signUp.html')