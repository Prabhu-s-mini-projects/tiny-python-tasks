"""
AppName:server_for test
purpose: will act as a test server
"""

# Dependencies
from flask import Flask, render_template
from flask_cors import CORS

# Internal Modules
app = Flask(__name__)
CORS(app)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the server_for test website
    """
    return render_template('mobile.html')


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
