"""
AppName:HTML_forms
purpose: will act as a server for the HTML forms
"""

# Dependencies
from flask import Flask, render_template, request

# Internal Modules
app = Flask(__name__)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the HTML_forms website
    """
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login() -> str:
    """will come to action method"""
    error = None
    if request.method == 'POST':
        f_name = request.form['fname']
        l_name = request.form['lname']
    else:
        f_name = "Invalid"
        l_name = "Name"
    return render_template(
        'display.html',
        error=error,
        fname=f_name,
        lname=l_name
    )


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
