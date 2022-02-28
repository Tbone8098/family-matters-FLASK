from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class PlaylistsHasSong(model_base.base_model):
    table = 'playlists_has_songs'
    def __init__(self, data):
        super().__init__(data)
        self.playlist_id = data['playlist_id']
        self.song_id = data['song_id']