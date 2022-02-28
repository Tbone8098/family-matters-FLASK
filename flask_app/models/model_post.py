from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user, model_page, model_category
from flask_app import DATABASE_SCHEMA
import re

class Post(model_base.base_model):
    table = 'posts'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.category_id = data['category_id']
        self.cover_picture = data['cover_picture']
        self.synopsis = data['synopsis']
        self.is_featured = data['is_featured']
        self.is_public = data['is_public']
        self.user_id = data['user_id']
        self.content = data['content']

    @property
    def category(self):
        return model_category.Category.get_one(id=self.category_id)
