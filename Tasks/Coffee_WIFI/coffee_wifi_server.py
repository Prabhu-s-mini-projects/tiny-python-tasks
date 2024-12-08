'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
import csv

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    """ Form for the coffee machine"""
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField(
        'Coffee',
        choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'),
                 ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
        validators=[DataRequired()]
    )
    wifi = SelectField(
        'Wifi',
        choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                 ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')],
        validators=[DataRequired()]
    )
    power = SelectField(
        'Power',
        choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                 ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    """ for the home page"""
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    """For add page"""
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    """reads the csv file"""
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
