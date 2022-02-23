from cmath import log
from flask_app import DATABASE_SCHEMA
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user, model_content, model_image


class Page(model_base.base_model):
    table = 'pages'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.user_id = data['user_id']

    @property
    def author(self):
        return model_user.User.get_one(id=self.user_id)

    @property
    def blocks(self):
        query = f"SELECT * FROM blocks WHERE blocks.page_id = {self.id}"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if results:
            all_blocks = []
            for block in results:
                if block['type'] == 'content':
                    query2 = f"SELECT * FROM contents WHERE contents.block_id = {block['id']}"
                    content_block = connectToMySQL(DATABASE_SCHEMA).query_db(query2)
                    all_blocks.append(model_content.Content(content_block[0]))
                elif block.type == 'images':
                    query = f"SELECT * FROM images WHERE images.block_id = {block.id}"
                    all_blocks.append(connectToMySQL(DATABASE_SCHEMA).query_db(query))
            return all_blocks
        return []
        

    @staticmethod
    def validation(data):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash('Name is required', 'err_page_name')

        return is_valid

    @staticmethod
    def api_validation(data):
        errors = {}

        if len(data['name']) < 1:
            errors['err_category_name'] = "Name is required"

        return errors