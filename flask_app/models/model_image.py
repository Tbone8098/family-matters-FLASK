from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA

class Image(model_base.base_model):
    table = 'images'
    def __init__(self, data):
        super().__init__(data)
        self.block_id = data['block_id']
        self.url = data['url']
        self.alt = data['alt']