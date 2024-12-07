"""
AppName:Flask_wtf_server
purpose: example of using the Flask WTForms
"""
# Dependencies
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

# Internal Modules
app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap5(app)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='log in')


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the Flask_wtf_server website
    """
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    """
    Takes user to Homepage of the Flask_wtf_server website
    """
    form = MyForm()
    if form.validate_on_submit() and request.method == 'POST':
        if form.email.data == "fname.lname@abc.com" and form.password.data == "12345678":
            return render_template('success.html', form=form)
        else:
            return render_template('denied.html', form=form)
    return render_template('login.html', form=form)


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
