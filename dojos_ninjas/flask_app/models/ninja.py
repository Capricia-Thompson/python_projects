from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojo_ninjas(cls, dojo_id):
        query = """SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s ;"""
        data = {'dojo_id': dojo_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo_ninjas = []
        for ninja in results:
            dojo_ninjas.append(cls(ninja))
        return dojo_ninjas

    @classmethod
    def create(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"""
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return results
