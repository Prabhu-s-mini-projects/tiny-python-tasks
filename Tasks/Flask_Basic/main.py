"""
Basic of FLASK framework
"""

from flask import Flask
app = Flask(__name__)
print(f"{ __name__ = } ")

def make_bold(function):
    """Outer Function"""
    def wrapper():
        """inner function"""
        a = function()
        return f"<b>{a}</b>"
    return wrapper()


@app.route("/")
def hello_world():
    """Home page"""
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    """Bye page"""
    return "<p>Bye!</p>"

@app.route("/<name>")
def greet(name):
    """ Greeting Page"""
    return f'<h1 style="text-align: center"> Greetings {name}!</h1>'\
            '<p>You are Grasping Concept like this. Keep Going ahead !</p>'\
            '<img src="https://i0.wp.com/images.onwardstate.com/uploads/2015'\
             '/05/oie_14175751vZSQRLEn.gif?fit=650%2C408&ssl=1">'

if __name__ == "__main__":
    app.run(debug=True)
