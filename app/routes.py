# Import necessary modules and packages
from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, session, jsonify
from app.models import User, Workout, Goal, UserProfile
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3

# Define a route for the root URL ("/")
@app.route('/')
def home():
    """
    Render the home page of the web application.

    This route handles requests to the root URL ("/") and displays the 'home.html' template.

    Returns:
        HTML: Rendered 'home.html' template.
    """
    return render_template('home.html')

# Define a route for user registration
@app.route('/auth/signUp/')
def signUp():
    """
    Render the user registration page.

    This route handles requests to '/auth/signUp/' and displays the 'auth/signUp.html' template.

    Returns:
        HTML: Rendered 'auth/signUp.html' template.
    """
    return render_template('auth/signUp.html')

# Define a route for user registration form submission
@app.route('/submit/', methods=['POST'])
def submit():
    """
    Handle user registration form submission.

    This route collects user registration data from a form, creates a new User instance, and stores it in the database.

    Returns:
        HTTP Redirect: Redirects to the 'login' route after successful registration.
    """
    # Extract user registration data from the form
    name = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    confirm = request.form['confirm_password']
    password = request.form['password']

    # Create a new User instance with the provided data
    user = User(
        fullname=name,
        email=email,
        phone=phone,
        confirm=confirm,
        password_hash=bcrypt.generate_password_hash(password)
    )

    # Add the user to the database and commit the transaction
    db.session.add(user)
    db.session.commit()

    # Flash a success message
    flash('User created successfully!', 'success')

    # Redirect to the 'login' route
    return redirect(url_for('login'))

# Define a route for user login
@app.route('/auth/login/', methods=['GET', 'POST'])
def login():
    """
    Handle user login.

    This route checks if the user is already logged in. If not, it handles user login requests.
    It validates user credentials and logs in the user if valid.

    Returns:
        - HTTP Redirect: Redirects to the 'dashboard' route after successful login.
        - HTML: Renders the 'auth/login.html' template for login.
    """
    if current_user.is_authenticated:
        # If the user is already logged in, redirect to the 'dashboard'
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        # If it's a POST request, process the login form data
        email = request.form['email']
        password = request.form['password']

        # Check if a user with the provided email exists
        user = User.query.filter_by(email=email).first()

        # If the user exists and the password is correct
        if user and bcrypt.check_password_hash(user.password_hash, password):
            # Log in the user
            login_user(user)

            # Determine the next page to redirect to (if provided in the 'next' query parameter)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))

        else:
            flash('Login failed. Please check your credentials.', 'danger')
    else:
        # If it's a GET request, render the login form
        return render_template('auth/login.html')

# Define a route for user logout
@app.route('/logout/')
def logout():
    """
    Handle user logout.

    This route logs the current user out and redirects to the 'home' page.

    Returns:
        HTTP Redirect: Redirects to the 'home' route after logging out.
    """
    logout_user()
    return redirect(url_for('home'))

# Define a route for the user dashboard
@app.route('/dashboard/')
@login_required
def dashboard():
    """
    Render the user dashboard.

    This route is protected, and only authenticated users can access it.
    It displays user-specific workout statistics, such as the total number of workouts, total calories burned, and total time spent on workouts.

    Returns:
        HTML: Rendered 'dashboard.html' template with user-specific data.
    """
    # Get all workouts for the current user
    workouts = current_user.Workout

    # Calculate the total number of workouts
    total_workouts = len(workouts)

    # Calculate total calories burned
    total_calories = sum(workout.calories_burned for workout in workouts)

    # Calculate total time in minutes
    total_time = sum(workout.duration for workout in workouts)

    # Get the workout data for the current user
    current_user_id = current_user.id
    workout_data = get_workout_data_for_user(current_user_id)
    exercise_data = get_data_for_user(current_user_id)

    # Debug statements
    print("Workout Data:", workout_data)

    # Render the 'dashboard.html' template with user-specific data
    return render_template('dashboard.html', total_workouts=total_workouts, total_calories=total_calories, total_time=total_time, data=workout_data, datas=exercise_data)

# Simulated workout data (replace with actual data from your database)
# graph function to display sets against date bar graph
def get_workout_data_for_user(user_id):
    """
    Fetch and format workout data for a user.

    This function retrieves workout data for a specific user and formats it for display.

    Args:
        user_id (int): The user's ID for whom the workout data is retrieved.

    Returns:
        list: List of dictionaries containing workout data.
    """
    workouts = Workout.query.filter_by(user_id=user_id).all()
    workout_data = [{"sets": workout.sets, "date": workout.date}
                    for workout in workouts]
    return workout_data


# Simulated exercise data (replace with actual data from your database)
# graph function to display calories against date bar graph
def get_data_for_user(user_id):
    """
    Fetch and format exercise data for a user.

    This function retrieves exercise data for a specific user and formats it for display.

    Args:
        user_id (int): The user's ID for whom the exercise data is retrieved.

    Returns:
        list: List of dictionaries containing exercise data.
    """
    workout = Workout.query.filter_by(user_id=user_id).all()
    exercise_data = [{"calories_burned": workout.calories_burned,
                      "Date": workout.date} for workout in workout]
    return exercise_data

# Define a route for workout statistics
@app.route('/workout-stats/')
def workout_stats():
    """
    Render workout statistics page.

    This route fetches and displays the total calories burned for each exercise.

    Returns:
        HTML: Rendered page displaying workout statistics.
    """
    # Fetch the total calories burned for each exercise
    exercises = db.session.query(Workout.exercise, db.func.sum(
        Workout.calories_burned)).group_by(Workout.exercise).all()
    return render_template('dashboard.html', exercises=exercises)

# Define a route for the user's workout timeline
@app.route('/timeline/')
@login_required
def timeline():
    """
    Render the user's workout timeline.

    This route fetches workout information for the currently authenticated user and displays it.

    Returns:
        HTML: Rendered 'timeline.html' with user-specific workout information.
    """
    if current_user.is_authenticated:
        user_id = current_user.id  # Get the current user's ID

        # Query workouts for the current user
        info = Workout.query.filter_by(user_id=user_id).all()

        return render_template('timeline.html', info=info)
    return render_template('timeline.html')

# Define a route for handling workout data submission and retrieval
@app.route('/api/workouts/', methods=['GET', 'POST'])
def get_workouts():
    """
    Handle workout data submission and retrieval.

    This route allows users to add new workouts through a form (POST) or retrieve existing workout data (GET).
    It also calculates calories burned for each workout.

    Returns:
        - HTML: Rendered 'timeline.html' with user-specific workout information (POST request).
        - JSON: Workout data and errors (GET request).
    """
    if request.method == 'POST':
        # Process and store workout data submitted through a form
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

        # Create a new Workout instance with the provided data
        workout = Workout(user_id=user_id, exercise=exercise, sets=sets, reps=reps,
                          weight=weight, duration=duration, date=date, calories_burned=calories_burned)
        db.session.add(workout)
        db.session.commit()

        # Assuming the current user is logged in (you're using Flask-Login)
    if current_user.is_authenticated:
        user_id = current_user.id  # Get the current user's ID

        # Query workouts for the current user
        info = Workout.query.filter_by(user_id=user_id).all()

        # Render the 'timeline.html' template with user-specific data
        return render_template('timeline.html', info=info)
    else:
        # Return a JSON response with an error message if the user is not logged in
        return jsonify({'error': 'User not logged in'}), 404

# Define a route for editing a workout
@app.route('/edit_workout/<int:workout_id>/', methods=['GET', 'POST'])
def edit_workout(workout_id):
    """
    Handle editing of a specific workout.

    This route allows users to modify workout details and saves the changes to the database.

    Returns:
        - HTML: Rendered 'update.html' template with the workout data for editing.
        - HTTP Redirect: Redirects to the 'timeline' route after updating the workout.
    """
    workout = Workout.query.get(workout_id)
    if request.method == 'POST':
        # Update workout data with the form data
        workout.exercise = request.form['exercise']
        workout.sets = request.form['sets']
        workout.reps = request.form['reps']
        workout.duration = request.form['duration']
        workout.date = request.form['date']
        db.session.commit()
        flash('Workout updated successfully!', 'success')
        return redirect(url_for('timeline'))
    return render_template('update.html', workout=workout)

# Define a route for deleting a workout
@app.route('/delete_workout/<int:workout_id>/')
def delete_workout(workout_id):
    """
    Handle the deletion of a specific workout.

    This route removes the selected workout from the database.

    Returns:
        HTTP Redirect: Redirects to the 'timeline' route after deleting the workout.
    """
    info = Workout.query.get(workout_id)
    db.session.delete(info)
    db.session.commit()
    flash('Workout deleted successfully!', 'success')
    return redirect(url_for('timeline'))

# Define a route for viewing user profile and goals
@app.route('/profile/')
@login_required
def profile():
    """
    Render the user's profile and goals.

    This route fetches and displays the user's profile and goals from the database.

    Returns:
        HTML: Rendered 'profile.html' template with user-specific data.
    """
    goals = Goal.query.filter_by(user_id=current_user.id).all()  # Filter goals by user_id
    profile = UserProfile.query.filter_by(user_id=current_user.id).first()  # Get user's profile
    return render_template('profile.html', goals=goals, profile=profile)

# Define a route for adding a new goal to the user's profile
@app.route('/add_goal/', methods=['POST'])
def add_goal():
    """
    Handle the addition of a new goal to the user's profile.

    This route allows users to add new goals to their profile.

    Returns:
        HTTP Redirect: Redirects to the 'profile' route after adding the goal.
    """
    if current_user.is_authenticated:
        description = request.form.get('description')
        user_id = current_user.id
        new_goal = Goal(user_id=user_id, description=description)
        db.session.add(new_goal)
        db.session.commit()
        # Redirect to the user's profile page
        return redirect(url_for('profile'))

# Define a route for editing a goal
@app.route('/edit/<int:goal_id>')
def edit_goal(goal_id):
    """
    Render the page for editing a specific goal.

    This route allows users to modify their goal descriptions.

    Returns:
        HTML: Rendered 'edit.html' template with the goal data for editing.
    """
    goal = Goal.query.get(goal_id)
    return render_template('edit.html', goal=goal)

# Define a route for updating a goal
@app.route('/update_goal/<int:goal_id>', methods=['POST'])
def update_goal(goal_id):
    """
    Handle the update of a specific goal's description.

    This route updates the goal description and saves the changes to the database.

    Returns:
        HTTP Redirect: Redirects to the user's profile page after updating the goal.
    """
    goal = Goal.query.get(goal_id)
    goal.description = request.form.get('description')
    db.session.commit()
    return redirect('/profile')

# Define a route for deleting a goal
@app.route('/delete/<int:goal_id>')
def delete_goal(goal_id):
    """
    Handle the deletion of a specific goal.

    This route removes the selected goal from the database.

    Returns:
        HTTP Redirect: Redirects to the user's profile page after deleting the goal.
    """
    goal = Goal.query.get(goal_id)
    db.session.delete(goal)
    db.session.commit()
    return redirect('/profile')

# Define a route for updating user profile data
@app.route('/index/', methods=['POST', 'GET'])
def index():
    """
    Handle updating user profile data.

    This route allows users to provide gender, height, age, and weight information for their profile.

    Returns:
        HTTP Redirect: Redirects to the user's profile page after updating the profile.
    """
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
        return redirect(url_for('profile'))

# Define a route for editing user profile
@app.route('/edit_profile/<int:profile_id>', methods=['GET', 'POST'])
def edit_profile(profile_id):
    """
    Render the page for editing user profile data.

    This route allows users to modify their gender, height, age, and weight information and saves the changes to the database.

    Returns:
        - HTML: Rendered 'edit_profile.html' template with the profile data for editing.
        - HTTP Redirect: Redirects to the user's profile page after updating the profile.
    """
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

# Define a route for deleting user profile
@app.route('/delete_profile/<int:profile_id>')
def delete_profile(profile_id):
    """
    Handle the deletion of user profile data.

    This route removes the user's profile data from the database.

    Returns:
        HTTP Redirect: Redirects to the user's profile page after deleting the profile data.
    """
    profile = UserProfile.query.get(profile_id)
    db.session.delete(profile)
    db.session.commit()
    return redirect(url_for('profile'))

# Define a route for changing the user's password
@app.route('/change_password', methods=['POST'])
def change_password():
    """
    Handle changing the user's password.

    This route is used for changing the user's password. Note that the logic for password change is not implemented in this code and should be added.

    Returns:
        - HTML: Rendered 'profile.html' or change password page.
    """
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
