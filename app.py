# TODO: Import Flask and other dependencies
# TODO: Set up Flask app
# TODO: Configure database connection
# TODO: Create routes and API endpoints
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! This is the index."

if __name__ == "__main__":
    # Run on 0.0.0.0 so it's reachable from other devices; change debug=False for production.
    app.run(host="0.0.0.0", port=5000, debug=True)
# ...existing code...
