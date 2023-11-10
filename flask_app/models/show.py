from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)
from flask_app.models import user
import re

class Show:
    db = "tvshows" #which database are you using for this project
    def __init__(self, data):
        self.idshows = data['idshows']
        self.title = data['title']
        self.network = data['network']
        self.date = data['date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.maker = None

    @classmethod
    def save(cls, data):
        query = """INSERT INTO shows (title, network, date, description, user_id) 
        VALUES (%(title)s, %(network)s, %(date)s, %(description)s, %(user_id)s);"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """ 
        SELECT * 
        FROM shows
        LEFT JOIN users
        ON shows.user_id = users.id;"""
        final = connectToMySQL(cls.db).query_db(query)
        results = []
        for result in final:
            this_show = cls(result)
            user_data = {
                    "id": result['id'],
                    "first_name": result['first_name'],
                    "last_name": result['last_name'],
                    "email": result['email'],
                    "password": "",
                    "created_at": result['created_at'],
                    "updated_at": result['updated_at']
            }
            this_show.maker = user.User(user_data)
            results.append(this_show)
        return results
    
    @classmethod
    def get_by_id(cls, id):
        data = {
            "id" : id
        }
        query = """
        SELECT * 
        FROM shows
        LEFT JOIN users
        ON shows.user_id = users.id
        WHERE shows.idshows = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        show_list = []
        for result in results:
            this_show = cls(result)
            user_data = {
                    "id": result['id'],
                    "first_name": result['first_name'],
                    "last_name": result['last_name'],
                    "email": result['email'],
                    "password": "",
                    "created_at": result['users.created_at'],
                    "updated_at": result['users.updated_at']
            }
            this_show.maker = user.User(user_data)
            show_list.append(this_show)
        return show_list[0]
    
    @classmethod
    def get_by_title(cls, title):
        data = {
            "title" : title
        }
        query = """
        SELECT * 
        FROM shows
        LEFT JOIN users
        ON shows.user_id = users.id
        WHERE shows.title = %(title)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        show_list = []
        for result in results:
            this_show = cls(result)
            user_data = {
                    "id": result['id'],
                    "first_name": result['first_name'],
                    "last_name": result['last_name'],
                    "email": result['email'],
                    "password": "",
                    "created_at": result['users.created_at'],
                    "updated_at": result['users.updated_at']
            }
            this_show.maker = user.User(user_data)
            show_list.append(this_show)
            print(user_data)
        if not results:
            return False
        return show_list[0]
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE shows
        SET title = %(title)s, 
        network = %(network)s, 
        date = %(date)s, 
        description = %(description)s
        WHERE idshows = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def delete(cls, id):
        data = {
            'id' : id
        }
        query = """
        DELETE FROM shows
        WHERE idshows = %(id)s"""
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_show(data):
        is_valid = True # we assume this is true
        if len(data['title']) < 3:
            flash("Title must be at least 3 characters.", "show")
            is_valid = False
        if len(data['network']) < 3:
            flash("Network must be at least 3 characters.", "show")
            is_valid = False
        if data['date'] == '':
            flash('Insert the date aired.', "show")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters.", "show")
            is_valid = False
        return is_valid