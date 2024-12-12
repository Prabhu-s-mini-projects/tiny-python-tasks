"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Float, ScalarResult
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
all_books= []


class Base(DeclarativeBase):
    """ Base class
    """
    pass


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    """ creates table"""
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


def create_new_record(new_book: Book) -> None:
    """ will add a new items to the DB"""
    with app.app_context():
        # new_book = Book(
        #     title ="Books_name_1",
        #     author = "Author_name_1",
        #     review = 9.3
        #                  )
        db.session.add(new_book)
        db.session.commit()


def read_all_records() -> ScalarResult:
    """reads all the record from the Database"""
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        books = result.scalars()
    return books


def read_a_record(book_id: int) -> ScalarResult:
    """will return a single record from the database"""
    # To do
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == book_id)).scalar()
    return book


def delete_a_record(book_id: int) -> None:
    """Will delete a single record from the system """
    with app.app_context():
        result = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Books, book_id)
        db.session.delete(result)
        db.session.commit()


def update_a_record(book: Book) -> None:
    """ Will update the data on the DB"""
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == Book.id)).scalar()
        book_to_update.review = book.review
        db.session.commit()


all_books.append(list(read_all_records()))


@app.route('/')
def home() -> str:
    """Takes you to the homepage"""

    return render_template("index.html",
                           books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add() -> str | object:
    """add a new books to DB"""
    if request.method == 'POST':
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)

        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit_rating/<book_id>', methods=['GET', 'POST'])
def edit_rating(book_id: int) -> object:
    """Updates the rating or the existing books"""
    book = read_a_record(book_id)
    if request.method == "POST":
        rating = request.form["rating"]
        book.review = float(rating)
        update_a_record(book)
        return redirect(url_for('home'))
    return render_template("edit_rating.html",
                           book=book)


if __name__ == "__main__":
    app.run(debug=True)
