from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.programs_models import Program


class Dojo:
    DB = 'login_reg'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.all_programs = []

    # @classmethod
    # def get_all_dojos(cls):
    #     query = """SELECT * FROM dojos;"""
    #     result = connectToMySQL('login_reg').query_db(query)
    #     print(result)
    #     all_dojos = []
    #     for dojo in result:
    #         all_dojos.append(cls(dojo))
    #     return all_dojos

    # @classmethod
    # def get_all_dojo_programs(cls, data):
    #     query = """SELECT * FROM programs LEFT JOIN dojos ON dojos.id = programs.dojo_id WHERE dojo_id = %(id)s;"""
    #     results = connectToMySQL('login_reg').query_db(query, data)
    #     print(results)
    #     one_dojo = cls(results[0])
    #     for program in results:
    #         program_data = {
    #             'id': program['id'],
    #             'name': program['name'],
    #             'dojo_id': program['dojo_id']
    #         }
    #         one_dojo.all_programs.append(Program(program_data))
    #     return one_dojo
