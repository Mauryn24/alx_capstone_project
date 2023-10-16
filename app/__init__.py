from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# # Import the login function from flask_login
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'auth.login'  # Change 'auth.login' to your actual login route

# Configure the static files
app.static_url_path = '/static'
app.static_folder = 'static'

# Import routes after initializing extensions (for better organization)
from app import routes

def create_app():
    app = Flask(__name__)