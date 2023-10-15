from flask import Flask, render_template, url_for
# Import the Flask class from the flask module


# Create a Flask application instance
app = Flask(__name__)

# Configure the static files
app.static_url_path = '/static'  # URL path for static files
app.static_folder = 'static'     # Folder where static files are located

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

if __name__ == '_main_':
    app.run(debug=True)