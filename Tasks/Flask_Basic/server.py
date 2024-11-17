"""
App_Name: server.py
Purpose: acts as a server for a flask website
"""
# Dependencies
from random import random, randint
from  flask import  Flask
# Internal modules

# CONSTANTS
app = Flask(__name__)
# Methods-------------------------------------------------------------------
@app.route("/")
def home()-> str:
    """
    Here is the Starting point of an App : server.py
    to do acts as a server for a flask website
    """
    # To do
    return '<h1>"Guess a number between 0 and 9" <h1>'\
           '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3Nj'\
            'ExaWJhbzl0b2NhMTFxdmlhbGViazQ0MGVncmxrNTFnaWU4YTQzcHZtNCZlcD1'\
            '2MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.webp">'

@app.route('/<int:number>')
def result(number:int)-> str:
    """
    will run a result is correct
    :param number:
    :return:
    """
    random_number = randint(0,10)
    print (random_number)
    if number > random_number:
        return '<h1 style="text-color: YELLOW">"Too High! Try again!" <h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if number < random_number:
        return  '<h1 style="text-color: RED">"Too low! Try again!" <h1>'\
           '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    return '<h1 style="text-color: GREEN">you Found me</h1>' \
          '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == '__main__':
    app.run(debug=True)
