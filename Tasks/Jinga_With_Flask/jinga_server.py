"""
AppName:my_webapp
purpose: act as server
"""
# Dependencies
from datetime import datetime
from random import randint

import requests
from flask import Flask, render_template

# Internal Modules
app = Flask(__name__)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the my_webapp website
    """
    year = datetime.now().year
    random_num = randint(0, 10)
    return render_template(
        'index.html',
        num=random_num,
        current_year=year,
        dev_name="Prabhukumar Sivamoorthy"
    )


@app.route('/guess/<username>')
def user_name(username: str) -> str:
    """
    Takes user page of my_webapp website
    """
    year = datetime.now().year
    response = requests.get(url=f"https://api.genderize.io?name={username}", timeout=10)
    gender = response.json().get("gender")
    response = requests.get(url=f"https://api.agify.io?name={username}", timeout=10)
    age = response.json().get("age")
    return render_template(
        'user.html',
        current_year=year,
        username=username,
        gender=gender,
        age=age
    )


@app.route('/blogs/<num>')
def blogs(num: int) -> str:
    """Takes you to blog posts """
    print(num)
    response = requests.get(url="https://api.npoint.io/64c4c05d34812b411e06", timeout=10)
    posts = response.json()
    year = datetime.now().year
    return render_template(
        'blog.html',
        current_year=year,
        posts=posts
    )


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
