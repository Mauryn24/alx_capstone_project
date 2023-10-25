from app import app, db, bcrypt
# import app decorators from app pakage

from flask import render_template, url_for, flash, redirect, request, session, jsonify
# Import the Flask class from the flask module

# Import User and Workout models from models.py
# Import User and Workout models from models.py
from app.models import User, Workout, Goal, UserProfile

from flask_login import login_user, current_user, logout_user, login_required

from flask import jsonify

import sqlite3

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
    goals = Goal.query.all()  # Retrieve all goals from the database
    profile = UserProfile.query.all()
    return render_template('profile.html', goals=goals, profile=profile)


# Simulated workout data (replace with actual data from your database)
def get_workout_data_for_user(user_id):
    workouts = Workout.query.filter_by(user_id=user_id).all()
    workout_data = [{"sets": workout.sets, "date": workout.date}
                    for workout in workouts]
    return workout_data


def get_data_for_user(user_id):
    workout = Workout.query.filter_by(user_id=user_id).all()
    exercise_data = [{"calories_burned": workout.calories_burned,
                      "Date": workout.date} for workout in workout]
    return exercise_data


@app.route('/dashboard/')
@login_required
def dashboard():
    workouts = current_user.Workout  # Get all workouts for the current user

    total_workouts = len(workouts)  # Calculate the total number of workouts
    # Calculate total calories burned
    total_calories = sum(workout.calories_burned for workout in workouts)
    # Calculate total time in minutes
    total_time = sum(workout.duration for workout in workouts)

    # Get the workout data for the current user
    current_user_id = current_user.id
    workout_data = get_workout_data_for_user(current_user_id)
    exercise_data = get_data_for_user(current_user_id)

    # Add debug statements
    print("Workout Data:", workout_data)  # Check the value of workout_data

    return render_template('dashboard.html', total_workouts=total_workouts, total_calories=total_calories, total_time=total_time, data=workout_data, datas=exercise_data)
    # return render_template('dashboard.html')


@app.route('/timeline/')
@login_required
def timeline():
    # info = Workout.query.all()
    if current_user.is_authenticated:
        user_id = current_user.id  # Get the current user's ID

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
        calories_burned = (MET * int(sets) * int(weight) *
                           int(reps) * int(duration)/60)/1000
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
        user_id = current_user.id  # Get the current user's ID

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


@app.route('/workout-stats/')
def workout_stats():
    # Fetch the total calories burned for each exercise
    exercises = db.session.query(Workout.exercise, db.func.sum(
        Workout.calories_burned)).group_by(Workout.exercise).all()
    return render_template('dashboard.html', exercises=exercises)


@app.route('/add_goal/', methods=['POST'])
def add_goal():
    if current_user.is_authenticated:
        description = request.form.get('description')
        new_goal = Goal(user_id=current_user.id, description=description)
        db.session.add(new_goal)
        db.session.commit()
        # Redirect to the user's profile page
        return redirect(url_for('profile'))


@app.route('/edit/<int:goal_id>')
def edit_goal(goal_id):
    goal = Goal.query.get(goal_id)
    # Create an 'edit.html' template for editing
    return render_template('edit.html', goal=goal)


@app.route('/update_goal/<int:goal_id>', methods=['POST'])
def update_goal(goal_id):
    goal = Goal.query.get(goal_id)
    goal.description = request.form.get('description')
    db.session.commit()
    return redirect('/profile')


@app.route('/delete/<int:goal_id>')
def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    db.session.delete(goal)
    db.session.commit()
    return redirect('/profile')


@app.route('/change_password', methods=['POST'])
def change_password():
    if request.method == 'POST':
        # Collect the new password from the form
        new_password = request.form.get('new_password')

        # Validate the new password and perform the password update logic here

        # Flash a success message
        flash('Password changed successfully', 'success')
        # Redirect to the profile page or a success page
        return redirect(url_for('profile'))

    # Handle other cases such as GET requests or form submission errors

    return render_template('profile.html')  # Render the change password page


@app.route('/index/', methods=['POST', 'GET'])
def index():
    if current_user.is_authenticated:
        gender = request.form['gender']
        height = request.form['height']
        age = request.form['age']
        weight = request.form['weight']
        user_id = current_user.id
        profile = UserProfile(
            user_id=user_id,
            gender=gender,
            height=height,
            age=age,
            weight=weight
        )
        db.session.add(profile)
        db.session.commit()
        print(profile)
        return redirect(url_for('profile'))
    
@app.route('/edit_profile/<int:profile_id>', methods=['GET', 'POST'])
def edit_profile(profile_id):
    profile = UserProfile.query.get(profile_id)
    if request.method == 'POST':
        # Update the profile data
        profile.gender = request.form['gender']
        profile.height = request.form['height']
        profile.age = request.form['age']
        profile.weight = request.form['weight']
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('edit_profile.html', profile=profile)

@app.route('/delete_profile/<int:profile_id>')
def delete_profile(profile_id):
    profile = UserProfile.query.get(profile_id)
    db.session.delete(profile)
    db.session.commit()
    return redirect(url_for('profile'))
