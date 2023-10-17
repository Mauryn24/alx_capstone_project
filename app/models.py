"""
    This module defines the database for the application.

    classses:
        User: Represents a user in the database
        Workout: Represents a workout in the database

"""

# from app import db, login_manager
# #import the database from app.py

from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#load_user function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#user class with fullname, email, phone number, password, confirm password
class User(UserMixin, db.Model):
    __tablename__ = 'user'


    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False) 
    phone = db.Column(db.String(100), nullable=False)
    confirm = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(100), nullable=False)
    Workout = db.relationship('Workout', backref='author', lazy=True)

    # how our objects is printed
    def __repr__(self):
        return f"User('{self.fullname}', '{self.email}', '{self.phone}', '{self.image_file}')"
    
    # set_password function
    def set_password(self, password):
        """
            set the password for the user.
            Args:
                password(str): The password to set

            Returns:
                None
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
#workout class with exercise, sets, reps, weight, duration, date, calories_burned
class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(100), nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"workouts('{self.exercise}', '{self.sets}', '{self.reps}', '{self.weight}', '{self.duration}', '{self.date}', '{self.calories_burned}')"