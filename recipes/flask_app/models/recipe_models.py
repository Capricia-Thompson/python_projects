from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user_models import User


class Recipe:
    DB = "recipes"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.time = data['time']
        self.prep_date = data['prep_date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, instructions, prep_date, time, user_id) VALUES (%(name)s, %(description)s,%(instructions)s,%(prep_date)s, %(time)s, %(user_id)s);"""
        result = connectToMySQL('recipes').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all_recipes(cls):
        query = """SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"""
        results = connectToMySQL('recipes').query_db(query)
        all_recipes = []
        for row in results:
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            recipe = cls(row)
            user = User(user_data)
            recipe.user = user
            all_recipes.append(recipe)
        print(all_recipes)
        return all_recipes

    @classmethod
    def get_recipe(cls, data):
        query = """SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"""
        results = connectToMySQL('recipes').query_db(query, data)
        recipe = results[0]
        print(recipe)
        return recipe

    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes SET name=%(name)s, description=%(description)s,instructions=%(instructions)s, prep_date=%(prep_date)s, time=%(time)s WHERE recipes.id=%(id)s;"""
        results = connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def delete_recipe(cls, id):
        query = """DELETE FROM recipes WHERE id=%(id)s;"""
        data = {'id': id}
        result = connectToMySQL('recipes').query_db(query, data)
