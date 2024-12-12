"""
AppName:SQL Lite server
purpose: basic server
"""
# Dependencies
# import  sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """ Base class
    """
    pass


db = SQLAlchemy(model_class=Base)
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection..db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    """ creates table"""
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


# # CREATE RECORD
# with app.app_context():
#     new_book = Books(id=2, title="Harry", author="J. K. Rowling", review=9.3)
#     db.session.add(new_book)
#     db.session.commit()
#


@app.route('/')
def home() -> str:
    """Takes you to the homepage"""

    return render_template("index.html")


# def main()-> None:
#     """
#     start of a method
#     :return:
#     """
#
#     db = sqlite3.connect("books-collection.db")
#
#     cursor = db.cursor()
#
#     # cursor.execute(
#     #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
#     #     " author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
#     cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter_2', 'J. K. Rowling', '9.3')")
#
#     db.commit()


# ------------------------------------------
if __name__ == "__main__":
    # main()
    app.run(debug=True)
