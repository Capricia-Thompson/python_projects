from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.authors import Author
from flask_app.models.books import Book


@app.route('/')
def home():
    all_authors = Author.get_all_authors()
    return render_template('authors.html', all_authors=all_authors)


@app.route('/create_author', methods=['POST'])
def create_author():
    data = {
        'name': request.form['name']
    }
    Author.create_author(data)
    return redirect('/')


@app.route('/author/<int:id>')
def show_author(id):
    author = Author.get_author(id)
    all_books = Book.get_all_books()
    return render_template('author_show.html', author=author, all_books=all_books)


@app.route('/add_fav_book', methods=['POST'])
def add_fav_book():
    data = {'author_id': request.form['author_id'],
            'book_id': request.form['book_id']}
    Author.add_fav_book(data)
    return redirect(f'/author/{data["author_id"]}')
