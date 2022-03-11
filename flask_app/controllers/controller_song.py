from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper_func import checkLogin
from flask_app.models import model_song, model_playlist_has_songs

@app.route('/admin/song/create', methods=['post'])
@checkLogin
def create_song():
    playlist_id = request.form['playlist_id']
    data = {**request.form}
    del data['playlist_id']
    model_song.Song.create(**data, user_id=session['uuid'])
    return redirect(f'/admin/playlist/{playlist_id}/edit')

@app.route('/admin/song/add', methods=['post'])
@checkLogin
def add_song():
    playlist_id = request.form['playlist_id']
    model_playlist_has_songs.PlaylistsHasSong.create(**request.form)
    return redirect(f'/admin/playlist/{playlist_id}/edit')

@app.route('/api/song/<int:id>')
def get_song(id):
    song = model_song.Song.get_one(id=id)
    song_serialized = song.serialize()
    msg = {
        'data': song_serialized
    }
    return jsonify(msg)

@app.route('/admin/song/<int:id>/update', methods=['post'])
def update_song(id):
    playlist_id = request.form['playlist_id']
    data = {**request.form}
    del data['playlist_id']

    model_song.Song.update_one(**data, id=id)

    return redirect(f'/admin/playlist/{playlist_id}/edit')

@app.route('/admin/song/<int:id>/delete')
def delete_song(id):
    pass

@app.route('/admin/song/<int:song_id>/<int:playlist_id>/remove')
def remove_song(song_id, playlist_id):
    song_link = model_playlist_has_songs.PlaylistsHasSong.get_one(song_id=song_id, playlist_id=playlist_id)
    model_playlist_has_songs.PlaylistsHasSong.delete_one(id = song_link.id)

    return redirect(f'/admin/playlist/{playlist_id}/edit')