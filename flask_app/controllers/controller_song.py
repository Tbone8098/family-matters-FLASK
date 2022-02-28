from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_song, model_playlist_has_songs

@app.route('/song/new')
def new_song():
    pass 

@app.route('/song/create', methods=['post'])
def create_song():
    playlist_id = request.form['playlist_id']
    data = {**request.form}
    del data['playlist_id']
    model_song.Song.create(**data, user_id=session['uuid'])
    return redirect(f'/playlist/{playlist_id}/edit')

@app.route('/song/add', methods=['post'])
def add_song():
    playlist_id = request.form['playlist_id']
    model_playlist_has_songs.PlaylistsHasSong.create(**request.form)
    return redirect(f'/playlist/{playlist_id}/edit')

@app.route('/song/<int:id>')
def show_song(id):
    pass 

@app.route('/song/<int:id>/edit')
def edit_song(id):
    pass 

@app.route('/song/<int:id>/update', methods=['post'])
def update_song(id):

    if not model_song.Song.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_song.Song.update_one(id=id, **data)

    pass 

@app.route('/song/<int:id>/delete')
def delete_song(id):
    model_song.Song.delete_one(id=id)
    pass 
