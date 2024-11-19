"""
App_Name: MY_personal_site_server
Purpose: act as a server to run the personal site
"""
# Dependencies
from flask import  Flask, render_template
# Internal modules

# CONSTANTS
app = Flask(__name__)
# Methods-------------------------------------------------------------------

@app.route("/")
def main() -> str:
    """
    Here is the Starting point of an App : MY_personal_site_server
    to do act as a server to run the personal site
    """
    # To do
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
