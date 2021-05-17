from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

    @classmethod
    def add(cls,data):
        query = "INSERT INTO users (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        
        return connectToMySQL('survey').query_db(query, data)

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['location']) < 1:
            flash("location must be present.")
            is_valid = False
        if len(data['language']) < 1:
            flash("language must present.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid