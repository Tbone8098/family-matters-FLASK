from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper_func import checkLogin
from flask_app.models import model_song, model_playlist_has_songs

@app.route('/song/create', methods=['post'])
@checkLogin
def create_song():
    playlist_id = request.form['playlist_id']
    data = {**request.form}
    del data['playlist_id']
    model_song.Song.create(**data, user_id=session['uuid'])
    return redirect(f'/playlist/{playlist_id}/edit')

@app.route('/song/add', methods=['post'])
@checkLogin
def add_song():
    playlist_id = request.form['playlist_id']
    model_playlist_has_songs.PlaylistsHasSong.create(**request.form)
    return redirect(f'/playlist/{playlist_id}/edit')

@app.route('/api/song/<int:id>')
def get_song(id):
    song = model_song.Song.get_one(id=id)
    song_serialized = song.serialize()
    msg = {
        'data': song_serialized
    }
    return jsonify(msg)

