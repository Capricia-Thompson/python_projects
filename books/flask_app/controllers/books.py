from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.books import Book
from flask_app.models.authors import Author


@app.route('/books')
def show_books():
    all_books = Book.get_all_books()
    return render_template('books.html', all_books=all_books)


@app.route('/create_book', methods=['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_pages': request.form['num_pages']
    }
    Book.create_book(data)
    return redirect('/books')


@app.route('/book/<int:id>')
def show_book(id):
    book = Book.get_book(id)
    all_authors = Author.get_all_authors()
    return render_template('book_show.html', book=book, all_authors=all_authors)


@app.route('/add_fav_author', methods=['POST'])
def add_fav_author():
    data = {
        'book_id': request.form['book_id'],
        'author_id': request.form['author_id']
    }
    Book.add_fav_author(data)
    return redirect(f'/book/{data["book_id"]}')
