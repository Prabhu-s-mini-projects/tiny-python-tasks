"""
AppName:Tindog
purpose: act as dog server
"""
# Dependencies
from flask import Flask, render_template

# Internal Modules
app = Flask(__name__)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the Tindog website
    """
    return render_template('index.html')


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
