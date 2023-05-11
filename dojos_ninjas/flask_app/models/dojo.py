from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
