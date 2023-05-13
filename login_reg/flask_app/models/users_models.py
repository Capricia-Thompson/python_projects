from datetime import date, timedelta
import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    DB = "login_reg"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.birthday = data['birthday']
        self.password = data['password']

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password, birthday) VALUES (%(first_name)s, %(last_name)s,%(email)s,%(password)s,%(birthday)s);"""
        result = connectToMySQL('login_reg').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_user_by_id(cls, id):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        data = {'id': id}
        result = connectToMySQL('login_reg').query_db(query, data)
        return cls(result[0])

    @staticmethod
    def valid_user(user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash("First name is required.")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Last name is required.")
            is_valid = False
        if len(user['email']) < 1:
            flash("Email is required.")
            is_valid = False
        if datetime.datetime.strptime(user['dob'], '%Y-%m-%d').date() > date.today()-timedelta(days=3652):
            flash("You must be at least 10 years old to register.")
            is_valid = False
        if len(user['password']) < 6:
            flash("Password must be at least 7 characters long.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password entered must match.")
            is_valid = False
        return is_valid

    @classmethod
    def get_user_by_email(cls, data):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL('login_reg').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
