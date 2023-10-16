from app import create_app
# import app variable from the app package
app = create_app()

if __name__ == '_main_':
    app.run(debug=True)