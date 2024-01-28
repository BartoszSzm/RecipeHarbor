from src import create_app

app = create_app()

if __name__ == "__main__":
    # App should be run through WSGI like gunicorn but for development
    # just run this script directly
    app.run("127.0.0.1", port=8000, debug=True)
