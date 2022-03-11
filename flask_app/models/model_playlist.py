from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_song
from flask_app import DATABASE_SCHEMA
import re

class Playlist(model_base.base_model):
    table = 'Playlists'
    def __init__(self, data):
        super().__init__(data)
        self.month = data['month']
        self.year = data['year']
        self.user_id = data['user_id']
        self.spotify_url = data['spotify_url']

    def __repr__(self) -> str:
        return f"{self.month.capitalize()} {self.year}"

    @property
    def songs(self):
        query = f"SELECT * FROM songs JOIN playlists_has_songs ON songs.id = playlists_has_songs.song_id WHERE playlists_has_songs.playlist_id = {self.id};"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if results:
            all_songs = []
            for dict in results:
                all_songs.append(model_song.Song(dict))
            return all_songs
        return []
