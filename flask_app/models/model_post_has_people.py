from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class PostHasPeople(model_base.base_model):
    table = 'post_has_people'
    def __init__(self, data):
        super().__init__(data)
        self.people_id = data['people_id']
        self.post_id = data['post_id']