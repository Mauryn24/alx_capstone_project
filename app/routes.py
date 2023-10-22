from app import app, db, bcrypt
# import app decorators from app pakage

from flask import render_template, url_for, flash, redirect, request, session
# Import the Flask class from the flask module

# Import User and Workout models from models.py
# Import User and Workout models from models.py
from app.models import User, Workout

from flask_login import login_user, current_user, logout_user, login_required

from flask import jsonify

# user_id = current_user.id


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
        phone=phone,
        confirm=confirm,
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
    # info = Workout.query.all()
    if current_user.is_authenticated:
        user_id =  current_user.id  # Get the current user's ID

        # Query workouts for the current user
        info = Workout.query.filter_by(user_id=user_id).all()

        return render_template('timeline.html', info=info)
    return render_template('timeline.html')


@app.route('/api/workouts/', methods=['GET', 'POST'])
def get_workouts():

    if request.method == 'POST':
        exercise = request.form.get('exercise')
        sets = request.form.get('sets')
        reps = request.form.get('reps')
        weight = request.form.get('weight')
        duration = request.form.get('duration')
        date = request.form.get('date')
        MET = 3
        calories_burned = (MET * int(sets) * int(weight) * int(reps) * int(duration)/60)/1000
        calories_burned = float(calories_burned)
        weight = request.form.get('weight')
        user_id = request.form.get('user_id')

        print('user_id', user_id)
        print('date', date)
        workout = Workout(user_id=user_id, exercise=exercise, sets=sets, reps=reps,
                          weight=weight, duration=duration, date=date, calories_burned=calories_burned)
        db.session.add(workout)
        db.session.commit()

        # Assuming current_user is logged in (you're using Flask-Login)
    if current_user.is_authenticated:
        user_id =  current_user.id  # Get the current user's ID

        # Query workouts for the current user
        info = Workout.query.filter_by(user_id=user_id).all()

        return render_template('timeline.html', info=info)
    else:
        return jsonify({'error': 'User not logged in'}), 404

@app.route('/auth/login/', methods=['GET', 'POST'])
def login():
    # check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    # if user is not logged in
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # check if their email == to form.email.data
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
    else:
        return render_template('auth/login.html')


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

@app.route('/edit_workout/<int:workout_id>/', methods=['GET', 'POST'])
def edit_workout(workout_id):
    workout = Workout.query.get(workout_id)
    if request.method == 'POST':
        workout.exercise = request.form['exercise']
        workout.sets = request.form['sets']
        workout.reps = request.form['reps']
        workout.duration = request.form['duration']
        workout.date = request.form['date']
        db.session.commit()
        flash('Workout updated successfully!', 'success')
        return redirect(url_for('timeline'))
    return render_template('update.html', workout=workout)

@app.route('/delete_workout/<int:workout_id>/')
def delete_workout(workout_id):
    
    info = Workout.query.get(workout_id)
    db.session.delete(info)
    db.session.commit()
    flash('Workout deleted successfully!', 'success')
    return redirect(url_for('timeline'))
