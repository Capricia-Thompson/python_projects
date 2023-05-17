from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books


class Author:
    DB = 'books'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []

    @classmethod
    def get_all_authors(cls):
        query = """SELECT * FROM authors"""
        results = connectToMySQL('books').query_db(query)
        print(results)
        all_authors = []
        for row in results:
            all_authors.append(cls(row))
        return all_authors

    @classmethod
    def create_author(cls, data):
        query = """INSERT INTO authors (name) VALUES(%(name)s)"""
        result = connectToMySQL('books').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_author(cls, id):
        query = """SELECT * FROM authors LEFT JOIN favorites on authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id=%(id)s"""
        data = {
            'id': id
        }
        results = connectToMySQL('books').query_db(query, data)
        print(results)
        author = cls(results[0])
        for row in results:
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_pages': row['num_pages'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            author.fav_books.append(books.Book(book_data))
        return author

    @classmethod
    def add_fav_book(cls, data):
        query = """INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s,%(author_id)s);"""
        result = connectToMySQL('books').query_db(query, data)
        return result
