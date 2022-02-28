from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_playlist, model_song

@app.route('/refit/page/playlist')
def refit_playlist():
    months = ['january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'octuber', 'november', 'december']
    context = {
        'all_playlists': model_playlist.Playlist.get_all(),
        'all_months': months,
    }
    return render_template('admin/refit/playlist.html', **context)

@app.route('/playlist/create', methods=['post'])
def create_playlist():
    model_playlist.Playlist.create(**request.form, user_id = session['uuid'])
    return redirect('/refit/page/playlist')

@app.route('/playlist/<int:id>')
def show_playlist(id):
    pass 

@app.route('/playlist/<int:id>/edit')
def edit_playlist(id):
    context = {
        'playlist': model_playlist.Playlist.get_one(id = id),
        'all_songs': model_song.Song.get_all()
    }
    return render_template('/admin/refit/playlist_show.html', **context)

@app.route('/playlist/<int:id>/update', methods=['post'])
def update_playlist(id):

    if not model_playlist.Playlist.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_playlist.Playlist.update_one(id=id, **data)

    pass 

@app.route('/playlist/<int:id>/delete')
def delete_playlist(id):
    model_playlist.Playlist.delete_one(id=id)
    return redirect('/refit/page/playlist')

