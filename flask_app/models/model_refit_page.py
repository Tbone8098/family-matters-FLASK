from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_playlist
from flask_app import DATABASE_SCHEMA
import re

class RefitPage(model_base.base_model):
    table = 'refit_pages'
    def __init__(self, data):
        super().__init__(data)
        self.news = data['news']
        self.schedule = data['schedule']
        self.loc = data['loc']
        self.about_me = data['about_me']
        self.about_me_picture = data['about_me_picture']
        self.user_id = data['user_id']
        self.playlist_id = data['playlist_id']
        self.banner1_picture = data['banner1_picture']
        self.banner2_picture = data['banner2_picture']

    @property
    def playlist(self):
        return model_playlist.Playlist.get_one(id=self.playlist_id)