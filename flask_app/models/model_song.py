from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Song(model_base.base_model):
    table = 'songs'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.artist = data['artist']
        self.link = data['link']
        self.user_id = data['user_id']