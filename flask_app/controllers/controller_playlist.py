from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper_func import checkLogin
from flask_app.models import model_playlist, model_song

@app.route('/admin/refit/page/playlist')
@checkLogin
def refit_playlist():
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'octuber', 'november', 'december']
    context = {
        'all_playlists': model_playlist.Playlist.get_all(),
        'all_months': months,
    }
    return render_template('admin/refit/playlist.html', **context)

@app.route('/playlist/create', methods=['post'])
@checkLogin
def create_playlist():
    model_playlist.Playlist.create(**request.form, user_id = session['uuid'])
    return redirect('/admin/refit/page/playlist')

@app.route('/admin/playlist/<int:id>/edit')
@checkLogin
def edit_playlist(id):
    context = {
        'playlist': model_playlist.Playlist.get_one(id = id),
        'all_songs': model_song.Song.get_all()
    }
    return render_template('/admin/refit/playlist_show.html', **context)

@app.route('/admin/refit/playlist/<int:id>/update', methods=['post'])
def playlist_update(id):
    model_playlist.Playlist.update_one(**request.form, id=id)
    return redirect(f'/admin/playlist/{id}/edit')

@app.route('/admin/playlist/<int:id>/delete')
@checkLogin
def delete_playlist(id):
    model_playlist.Playlist.delete_one(id=id)
    return redirect('/admin/refit/page/playlist')

