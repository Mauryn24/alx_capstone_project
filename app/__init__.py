# Import necessary modules and extensions for the Flask application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_bcrypt import Bcrypt
import secrets
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Custom command to initialize the database using Flask CLI
@app.cli.command()
def init_db():
    """Initialize the database."""
    db.create_all()

# Push the application context to make it available
app.app_context().push()

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Initialize the LoginManager for user authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Change 'auth.login' to your actual login route

# Configure the static files
app.static_url_path = '/static'
app.static_folder = 'static'

# Import routes after initializing extensions (for better organization)
from app import routes

# Generate a secret key for the Flask application
secret_key = secrets.token_hex(32)

# Set the secret key for the Flask application (make sure to use the generated secret key)
app.config['SECRET_KEY'] = 'your_secret_key'