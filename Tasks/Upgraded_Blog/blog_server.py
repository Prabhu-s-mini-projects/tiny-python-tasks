"""
AppName:Blog_server
purpose: will act as a server for upgraded blog
"""
# Dependencies
import requests
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


@app.route('/contact')
def contact():
    """Takes you to the contact page"""
    return render_template('contact.html')


@app.route('/about')
def about():
    """Takes you to the contact page"""
    return render_template('about.html')


@app.route('/post')
def post():
    """Takes you to post page"""
    response = requests.get(url="https://api.npoint.io/64c4c05d34812b411e06", timeout=10)
    posts = response.json()
    return render_template(
        'post.html',
        posts=posts
    )


@app.route('/post/<p_id>')
def show_post(p_id: int):
    """Takes you to post page"""
    response = requests.get(url="https://api.npoint.io/64c4c05d34812b411e06", timeout=10)
    i_post = response.json()[int(p_id) - 1]
    return render_template(
        'show_post.html',
        post=i_post
    )

# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
