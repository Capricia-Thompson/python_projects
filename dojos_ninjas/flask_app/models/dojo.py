from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, id):
        query = """SELECT * FROM dojos WHERE id=%(id)s"""
        data = {'id': id}
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = """INSERT INTO dojos (name) VALUES(%(name)s)"""
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return results

    @classmethod
    def get_ninjas_from_dojo(cls, data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"""
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        one_dojo = cls(results[0])
        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': row['dojo_id']
            }
            one_dojo.ninjas.append(Ninja(ninja_data))
        return one_dojo
