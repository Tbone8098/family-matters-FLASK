from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Person(model_base.base_model):
    table = 'people'
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.avatar = data['avatar']
        self.gender = data['gender']
        

    def __repr__(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
