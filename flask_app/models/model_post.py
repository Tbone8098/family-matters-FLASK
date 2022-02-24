from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user, model_page, model_category
from flask_app import DATABASE_SCHEMA
import re

class Post(model_base.base_model):
    table = 'posts'
    def __init__(self, data):
        super().__init__(data)
        self.page_id = data['page_id']
        self.category_id = data['category_id']

    @property
    def page(self):
        return model_page.Page.get_one(id=self.page_id)

    @property
    def category(self):
        return model_category.Category.get_one(id=self.category_id)
