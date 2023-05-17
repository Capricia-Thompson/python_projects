from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import authors


class Book:
    DB = 'books'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_authors = []

    @classmethod
    def get_all_books(cls):
        query = """SELECT * FROM books"""
        results = connectToMySQL('books').query_db(query)
        print(results)
        all_books = []
        for row in results:
            all_books.append(cls(row))
        return all_books

    @classmethod
    def create_book(cls, data):
        query = """INSERT INTO books (title, num_pages) VALUES(%(title)s, %(num_pages)s)"""
        result = connectToMySQL('books').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_book(cls, id):
        query = """SELECT * FROM books LEFT JOIN favorites on books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id=%(id)s;"""
        data = {
            'id': id
        }
        results = connectToMySQL('books').query_db(query, data)
        print(results)
        book = cls(results[0])
        for row in results:
            author_data = {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            book.fav_authors.append(authors.Author(author_data))
        return book

    @classmethod
    def add_fav_author(cls, data):
        query = """INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s,%(author_id)s);"""
        result = connectToMySQL('books').query_db(query, data)
        return result
