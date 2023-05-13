from flask_app.config.mysqlconnection import connectToMySQL


class Program:
    DB = 'login_reg'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.dojo_id = data['dojo_id']
