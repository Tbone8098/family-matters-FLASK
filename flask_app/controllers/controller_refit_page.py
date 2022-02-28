from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_refit_page, model_playlist

@app.route('/refit_page')
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

@app.route('/refit_page/create', methods=['post'])
def create_refit_page():

    if not model_refit_page.RefitPage.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    id = model_refit_page.RefitPage.create(**data)

    pass 

@app.route('/refit_page/<int:id>')
def show_refit_page(id):
    pass 

@app.route('/refit_page/<int:id>/edit')
def edit_refit_page(id):
    pass 

@app.route('/refit_page/<int:id>/update', methods=['post'])
def update_refit_page(id):
    data = {
        **request.form
    }
    del data['files']
    model_refit_page.RefitPage.update_one(id=id, **data)
    return redirect('/refit_page')

@app.route('/refit_page/<int:id>/delete')
def delete_refit_page(id):
    model_refit_page.RefitPage.delete_one(id=id)
    pass 

