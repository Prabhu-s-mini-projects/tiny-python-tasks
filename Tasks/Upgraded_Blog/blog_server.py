"""
AppName:Blog_server
purpose: will act as a server for upgraded blog
"""
# Dependencies
from flask import Flask, render_template

# Internal Modules
app = Flask(__name__)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the Blog_server website
    """
    return render_template('index.html')


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
