from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_post
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

    @property
    def posts(self):
        query = f"SELECT * FROM posts JOIN post_has_people ON posts.id = post_has_people.post_id WHERE post_has_people.people_id = {self.id};"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if results:
            all_posts = []
            for post in results:
                all_posts.append(model_post.Post(post))
            return all_posts
        return []
