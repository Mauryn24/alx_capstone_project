from app import app, db, bcrypt
# import app decorators from app pakage

from flask import render_template, url_for, flash, redirect
# Import the Flask class from the flask module

# Import User and Workout models from models.py
from app.models import User, Workout  # Import User and Workout models from models.py

from app.forms import LoginForm, SignUpForm # Import your login form
#import LoginFotm from app

from flask_login import login_user, current_user, logout_user


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

@app.route('/auth/login/', methods=['GET', 'POST'])
def login():
    #check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    # if user is not logged in
    form = LoginForm()
    if form.validate_on_submit():
        #check if their email == to form.email.data
        user = User.query.filter_by(email=form.email.data).first()
        # if user exists and the data he/she entered exists in the db
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('auth/login.html', form=form)

@app.route('/auth/signUp/', methods=['GET', 'POST'])
def signUp():

    #check if user is already signed
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    # if user is not logged in
    form = SignUpForm()
    if form.validate_on_submit():
        # Add user to database here
        user = User(
            fullname=form.fullname.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('User created successfully!', 'success')
        #redirect to login page
        return redirect(url_for('login'))
    
    return render_template('auth/signUp.html', form=form)

# logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))