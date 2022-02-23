from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA

class Block(model_base.base_model):
    table = 'blocks'
    def __init__(self, data):
        super().__init__(data)
        self.page_id = data['page_id']
        self.type = data['type']