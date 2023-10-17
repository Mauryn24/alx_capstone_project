from app import app, db, bcrypt
# import app decorators from app pakage

from flask import render_template, url_for, flash, redirect, request
# Import the Flask class from the flask module

# Import User and Workout models from models.py
from app.models import User, Workout  # Import User and Workout models from models.py

from flask_login import login_user, current_user, logout_user, login_required


# Define a route for the root URL ("/")
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit/', methods=['POST'])
def submit():
    name = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    confirm = request.form['confirm_password']
    password = request.form['password']
    user = User(
    fullname=name,
    email=email,
    phone = phone,
    confirm = confirm,
    password_hash=bcrypt.generate_password_hash(password)
        )
    db.session.add(user)
    db.session.commit()
    flash('User created successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/timeline/')
@login_required
def timeline():
    return render_template('timeline.html')

@app.route('/auth/login/', methods=['GET', 'POST'])
def login():
    #check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('dashboard')) 
    
    # if user is not logged in
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        #check if their email == to form.email.data
        user = User.query.filter_by(email=email).first()
        # if user exists and the data he/she entered exists in the db
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            
            
            # check this line
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
           # return  redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    else:return render_template('auth/login.html')

@app.route('/auth/signUp/')
def signUp():    
    return render_template('auth/signUp.html')

# logout route
@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home'))

# accounts route
@app.route('/account')
@login_required
def account():
    return render_template('acccount.html', title='Account')