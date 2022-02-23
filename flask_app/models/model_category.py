from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Category(model_base.base_model):
    table = 'categories'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']

    @staticmethod
    def validation(data):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash('Name is required', 'err_category_name')

        return is_valid

    @staticmethod
    def api_validation(data):
        errors = {}

        if len(data['name']) < 1:
            errors['err_category_name'] = "Name is required"

        return errors