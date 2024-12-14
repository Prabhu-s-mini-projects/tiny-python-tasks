'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Load a specific .env file
env_path = Path('/Users/Prabhukumar/Projects/PycharmProjects/tiny-python-tasks/.venv/.env')
load_dotenv(dotenv_path=env_path)

MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    """ Base class
    """


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_movies.db"
# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    """ Creates a representation of model """
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250))

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


class MyForm(FlaskForm):
    """
    Creates a blueprint of a form
    """
    rating = StringField('Your Rating Out of 10 eg:7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddMovieForm(FlaskForm):
    """
    Creates a blueprint of a form
    """
    title = StringField('Enter the Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='add')


# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film,
#     learn the story of the Sully family (Jake, Neytiri, and their kids),
#     the trouble that follows them, the lengths they go to keep each other safe,
#     the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# ## adds a new movies to the table
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

def search_movie(keyword: str) -> object:
    """Search a movie using API"""
    movie_db_url = os.getenv("MOVIE_DB_API_URL")
    params = {
        "api_key": os.getenv("MOVIE_DATABASE_API_KEY"),
        "query": keyword,
        "language": "en-US"
    }
    print(f"{ params = } ")

    response = requests.get(
        url=movie_db_url,
        params=params,
        timeout=10
    )
    response_data = response.json()['results']
    print(f"{ response_data = } ")

    return response_data


def add_new_movie(new_movie: Movie) -> None:
    """will add a new movie to DB"""
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()


def fetch_movies() -> None:
    """Extracts all the Movies from DB"""
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for index, movie in enumerate(movies):
        movies[movie].ranking = len(movies) - index
    db.session.commit()

    return movies


def fetch_a_movie(movie_id: int):
    """ fetch a movie from db based on the id"""
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    return movie


def update_a_movie(movie: Movie) -> None:
    """will update a record in Db """
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie.id)).scalar()
    movie_to_update.review = movie.review
    movie_to_update.rating = movie.rating
    db.session.commit()


def delete_a_movie(move_id: int) -> None:
    """this is the movie id"""
    movie = db.get_or_404(Movie, move_id)
    db.session.delete(movie)
    db.session.commit()


@app.route("/")
def home():
    """ Takes you to home page"""
    return render_template("index.html", movies=fetch_movies())


@app.route("/add/<movie_id>", methods=["GET", "POST"])
def edit(movie_id: int):
    """ Takes you to add page"""
    form = MyForm()
    movie = fetch_a_movie(movie_id=movie_id)
    if form.validate_on_submit() and request.method == "POST":
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        update_a_movie(movie)
        return redirect(url_for('home'))
    return render_template("edit.html",
                           form=form,
                           movie=movie
                           )


@app.route("/delete/<movie_id>")
def delete(movie_id):
    """ Takes you to home page"""
    delete_a_movie(movie_id)
    return render_template("index.html", movies=fetch_movies())


@app.route("/add", methods=["GET", "POST"])
def add():
    """ Takes you to search page"""
    new_movie_form = AddMovieForm()
    if request.method == "POST":
        print(request.form["title"])
        data = search_movie(keyword=request.form["title"])
        return render_template("select.html", movie_details=data)
    return render_template("add.html", form=new_movie_form)


@app.route("/add_to_db/<movie_id>", methods=["GET", "POST"])
def add_to_db(movie_id):
    """ adds to db page"""
    api_url = "https://api.themoviedb.org/3/movie"
    params = {
        "api_key": os.getenv("MOVIE_DATABASE_API_KEY"),
        "language": "en-US"
    }
    response = requests.get(url=f"{api_url}/{movie_id}",
                            params=params,
                            timeout=10
                            )
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        description=data["overview"],
        rating=7.3,
        ranking=5,
        review="I liked this movie.",
    )
    add_new_movie(new_movie)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
