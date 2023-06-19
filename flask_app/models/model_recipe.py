from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

db = "Recipe_schema"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.date_made = data['date_made']


    @staticmethod
    def validate_recipe(new_recipe):
        isValid = True
        if len(new_recipe['name']) < 3:
            flash("The recipe name must at least 3 characters", "recipe")
            isValid = False
        if len(new_recipe['description']) < 3:
            flash("The description must not be empty", "recipe")
            isValid = False
        if len(new_recipe['instructions']) < 3:
            flash("The Instructions must not be empty", "recipe")
            isValid = False
        return isValid
    
    @classmethod
    def get_all(cls):
        query = """SELECT recipes.name AS name, under30, first_name, recipes.id AS id
                    FROM users JOIN recipes
                    ON users.id = recipes.users_id;"""
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def add_recipe(cls, data):
        query = """INSERT INTO recipes (name, description, instructions, under30, date_made, user_id ) 
                   VALUES (%(name)s, %(description)s, %(instructions)s, %(under30)s, %(date_made)s, %(user_id)s)"""
        result = connectToMySQL(db).query_db(query, data)
        return result

