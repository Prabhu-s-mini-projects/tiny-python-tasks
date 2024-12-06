"""
AppName:Blog_server
purpose: will act as a server for upgraded blog
"""
import os
import smtplib
from pathlib import Path

# Dependencies
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

path = Path('/Users/Prabhukumar/Projects/PycharmProjects/tiny-python-tasks/.venv/.env')
load_dotenv(dotenv_path=path)

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


@app.route("/login", methods=['POST'])
def receive_data() -> str:
    """receive data from contact form"""
    error = None
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        message = request.form['message']
        phone = request.form['phone']
        details = (f"hi \n This is  {name}\n"
                   f"contact me @ {mail} or {phone}\n"
                   f"{message}")
        send_mail(message=details)
        message = "Successfully sent the Message"
    else:
        message = " data not receviesd"
    return render_template(
        "submitted.html",
        error=error,
        message=message
    )


def send_mail(message: str) -> None:
    """Sends an email from bot """
    try:
        with smtplib.SMTP(os.getenv('SMTP_ADDRESS'), port=587) as connection:
            connection.starttls()
            connection.login(
                user=os.getenv('EMAIL_ADDRESS'),
                password=os.getenv('EMAIL_PASSWORD')
            )
            connection.sendmail(
                from_addr=os.getenv('EMAIL_ADDRESS'),
                to_addrs=os.getenv('EMAIL_ADDRESS'),
                msg=message
            )
    except smtplib.SMTPException as e:
        print(f"Failed to send email : {e}")


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
