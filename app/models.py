"""
    This module defines the database for the application.

    classes:
        User: Represents a user in the database
        Workout: Represents a workout in the database
        Goal: Represents user goals in the database
        UserProfile: Represents user profiles in the database
"""

# Import necessary modules and extensions
from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Define the user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """
    Load a user given their ID.

    Args:
        user_id (int): The user's ID.

    Returns:
        User: The User object corresponding to the provided ID.
    """
    return User.query.get(int(user_id))

# Define the User class
class User(UserMixin, db.Model):
    """
    Model representing user accounts.

    Attributes:
        id (int): Unique identifier for the user.
        fullname (str): Full name of the user.
        email (str): Email address of the user (used for login).
        phone (str): User's contact phone number.
        confirm (str): Confirm password.
        image_file (str): User's profile image file (default is 'default.jpg').
        password_hash (str): Securely hashed user password.
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False) 
    phone = db.Column(db.String(100), nullable=False)
    confirm = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(100), nullable=False)
    Workout = db.relationship('Workout', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.id}', '{self.fullname}', '{self.email}', '{self.phone}', '{self.image_file}')"
    
    def set_password(self, password):
        """
        Set the password for the user.

        Args:
            password (str): The password to set.

        Returns:
            None
        """
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """
        Check if the provided password matches the user's hashed password.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the provided password matches the user's password; otherwise, False.
        """
        return check_password_hash(self.password_hash, password.encode('utf-8'))

# Define the Workout class
class Workout(db.Model):
    """
    Model representing workout data.

    Attributes:
        id (int): Unique identifier for the workout.
        exercise (str): Name of the exercise.
        sets (int): Number of sets performed.
        reps (int): Number of repetitions per set.
        weight (int): Weight lifted in kilograms.
        duration (int): Duration of the workout in minutes.
        date (str): Date and time of the workout.
        calories_burned (int): Estimated calories burned during the workout.
        user_id (int): User ID of the associated user.
    """
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(100), nullable=True)
    calories_burned = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"workouts('{self.exercise}', '{self.sets}', '{self.reps}', '{self.weight}', '{self.duration}', '{self.date}', '{self.calories_burned}')"
    
# Define the Goal class
class Goal(db.Model):
    """
    Model representing user goals.

    Attributes:
        id (int): Unique identifier for the goal.
        user_id (int): User ID of the associated user.
        description (str): Description of the user's goal.
        accomplished (bool): Goal accomplishment status (default is False).
    """
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    accomplished = db.Column(db.Boolean, default=False)

# Define the UserProfile class
class UserProfile(db.Model):
    """
    Model representing user profiles.

    Attributes:
        id (int): Unique identifier for the user profile.
        user_id (int): User ID of the associated user.
        gender (str): User's gender.
        height (int): User's height in centimeters.
        age (int): User's age.
        weight (int): User's weight in kilograms.
    """
    __tablename__ = 'user_profile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)