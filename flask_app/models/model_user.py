from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA, bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User(model_base.base_model):
    table = 'Users'
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.pw = data['pw']
        self.email = data['email']
        self.fullname = f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @staticmethod
    def validation(data):
        is_valid = True

        if len(data['first_name']) < 1:
            flash('First Name is required', 'err_user_first_name')
            is_valid = False

        if len(data['last_name']) < 1:
            flash('Last Name is required', 'err_user_last_name')
            is_valid = False

        if len(data['email']) < 1:
            flash('Email is required', 'err_user_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'err_user_email')
            is_valid = False

        if len(data['pw']) < 7:
            flash('Password is required and must be more than 7 characters', 'err_user_pw')
            is_valid = False

        if len(data['confirm_pw']) < 7:
            flash('Confirm Password is required and must be more than 7 characters', 'err_user_confirm_pw')
            is_valid = False

        elif data['confirm_pw'] != data['pw']:
            flash('Passwords do not match', 'err_user_confirm_pw')
            is_valid = False


        return is_valid

    @staticmethod
    def validation_login(data):
        is_valid = True


        if len(data['email']) < 1:
            flash('Email is required', 'err_user_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'err_user_email')
            is_valid = False

        if len(data['pw']) < 1:
            flash('Password is required', 'err_user_pw')
            is_valid = False
        
        if is_valid:
            potential_user = User.get_one(email=data['email'])
            if not potential_user:
                flash('No User Found', 'err_user_email')
                is_valid = False
            elif not bcrypt.check_password_hash(potential_user.pw, data['pw']): 
                flash('Bad Password', 'err_user_pw')
                is_valid = False
            else:
                session['uuid'] = potential_user.id
                session['user_name'] = potential_user.fullname

        return is_valid