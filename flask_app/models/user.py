from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app.models import purchase
bcrypt = Bcrypt(app)
import re
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt

class User:
    db = "giftanon" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.purchases = []
        # What changes need to be made above for this project?
        #What needs to be added her for class association?

    # Create Users Models

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users 
        (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id

    # Read Users Models

    @classmethod
    def get_by_email(cls, data):
        data = { 'email' : request.form['email'] }
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user_email = connectToMySQL(cls.db).query_db(query,data)
        if not user_email:
            return False
        return cls(user_email[0])
    
    @classmethod
    def get_user_purchases(cls, data):
        query = """
        SELECT * 
        FROM users
        LEFT JOIN purchases
        ON users.id = purchases.user_id
        WHERE users.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        purchase_list = []
        for result in results:
            this_purchase = cls(result)
            purchase_data = {
                    "id": result['id'],
                    "title": result['title'],
                    "network": result['network'],
                    "date": result['date'],
                    "description": result['description'],
                    "created_at": result['purchases.created_at'],
                    "updated_at": result['purchases.updated_at']
            }
            this_purchase.purchases.append(purchase.Purchase(purchase_data))
            purchase_list.append(this_purchase)
        return purchase_list

    # Update Users Models



    # Delete Users Models




    @staticmethod
    def validate_user(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True # we assume this is true
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", "register")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Please use a valid email address.", "register")
            is_valid = False
        if len(data['password']) < 1:
            flash("Please fill in a password.", "register")
            is_valid = False
        if data['password'] != data['c_pass']:
            flash('Passwords must match.', "register")
            is_valid = False
        if User.get_by_email(data['email']):
            flash('Email already exists.', "register")
            is_valid = False
        return is_valid