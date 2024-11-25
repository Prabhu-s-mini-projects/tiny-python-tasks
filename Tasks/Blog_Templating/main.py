"""
AppName:Blog_template
purpose: server
"""
import requests
# Dependencies
from flask import Flask, render_template

# Internal Modules
app = Flask(__name__)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the Blog_template website
    """
    response = requests.get(url="https://api.npoint.io/64c4c05d34812b411e06", timeout=10)
    posts = response.json()
    return render_template(
        'index.html',
        posts=posts
    )


@app.route('/post/<post_id>')
def detail_blog(post_id: str) -> str:
    """
    Takes user to detailed blog of the Blog_template website
    """
    print(post_id)
    response = requests.get(url="https://api.npoint.io/64c4c05d34812b411e06", timeout=10)
    post = response.json()[int(post_id) - 1]
    return render_template(
        'post.html',
        post=post
    )


@app.route('/bootstrap')
def bootstrap() -> str:
    """
    Takes user to bootstrap blog of the Blog_template website
    """
    return render_template('bootstrap.html')


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
