from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_bcrypt import Bcrypt
import secrets
# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

#
app.app_context().push()

bcrypt = Bcrypt(app)

# Import the login function from flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Change 'auth.login' to your actual login route

# login_manager.login_message_category = 'info'

# Configure the static files
app.static_url_path = '/static'
app.static_folder = 'static'

# Import routes after initializing extensions (for better organization)
from app import routes


# def create_app():
#     app = Flask(__name__)

# Generate a secret key for the Flask application
secret_key = secrets.token_hex(32)
# Set the secret key for the Flask application
app.config['SECRET_KEY'] = 'your_secret_key' 