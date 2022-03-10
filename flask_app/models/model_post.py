from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user, model_category, model_people
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
        self.posted_date = data['posted_date']

    @property
    def category(self):
        return model_category.Category.get_one(id=self.category_id)

    @property
    def author(self):
        return model_user.User.get_one(id=self.user_id)

    @property
    def people(self):
        query = f"SELECT * FROM people JOIN post_has_people ON people.id = post_has_people.people_id WHERE post_has_people.post_id = {self.id};"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        print(results)
        if results:
            all_people = []
            for person in results:
                all_people.append(model_people.Person(person))
            return all_people
        return []