from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper_func import checkLogin
from flask_app.models import model_refit_page, model_playlist


@app.route('/admin/refit_page')
@checkLogin
def new_refit_page():
    page = model_refit_page.RefitPage.get_all()
    if not page:
        page_id = model_refit_page.RefitPage.create(user_id=session['uuid'])
        page = model_refit_page.RefitPage.get_one(id=page_id)
    else:
        page = page[0]
    context = {
        'page': page,
        'all_playlists': model_playlist.Playlist.get_all()
    }
    return render_template('admin/refit/refit_page.html', **context)

@app.route('/admin/refit_page/<int:id>/update', methods=['post'])
@checkLogin
def update_refit_page(id):
    data = {
        **request.form
    }
    del data['files']
    model_refit_page.RefitPage.update_one(id=id, **data)
    return redirect('/admin/refit_page')