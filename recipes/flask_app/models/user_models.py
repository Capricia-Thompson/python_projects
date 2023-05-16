from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

REGEX_EMAIL = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


class User:
    DB = "recipes"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.all_recipes = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,%(email)s,%(password)s);"""
        result = connectToMySQL('recipes').query_db(query, data)
        print(result)
        return result

    @staticmethod
    def valid_user(user):
        is_valid = True
        if len(user['fname']) < 1:
            flash("First name is required.", 'reg')
            is_valid = False
        if len(user['lname']) < 1:
            flash("Last name is required.", 'reg')
            is_valid = False
        if len(user['email']) < 1:
            flash("Email is required.", 'reg')
            is_valid = False
        if not (re.match(REGEX_EMAIL, user['email'])):
            flash("Email format not valid.", 'reg')
            is_valid = False
        if len(user['password']) < 6:
            flash("Password must be at least 7 characters long.", 'reg')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password entered must match.", 'reg')
            is_valid = False
        return is_valid

    @classmethod
    def get_user_by_email(cls, data):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL('recipes').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL('recipes').query_db(query, data)
        return cls(result)
