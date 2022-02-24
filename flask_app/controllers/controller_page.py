from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_page, model_user


@app.route('/pages')
def page():
    context = {
        'all_pages': model_page.Page.get_all(is_post=0)
    }
    return render_template('admin/page.html', **context)

@app.route('/page/new')
def new_page():
    return render_template('admin/page_new.html')

@app.route('/page/create', methods=['post'])
def create_page():
    if not model_page.Page.validation(request.form):
        return redirect('/page/new')

    data = {
        **request.form,
        'user_id': session['uuid']
    }

    id = model_page.Page.create(**data)
    return redirect(f'/page/{id}/edit') 

@app.route('/api/page/create', methods=['post'])
def api_page_create():
    errors = model_page.Page.api_validation(request.form)
    if errors:
        msg = {
            'status': 500,
            'errors': errors
        }
        return jsonify(msg)

    id = model_page.Page.create(**request.form, user_id=session['uuid'])

    msg = {
        'status': 200,
        'data': {
            'id': id,
            'author': session['user_name'],
            **request.form,
        }
    }
    return jsonify(msg)

@app.route('/page/<int:id>')
def show_page(id):
    context = {
        'page': model_page.Page.get_one(id=id)
    }
    return render_template('main/page_show.html', **context)

@app.route('/page/<int:id>/edit')
def edit_page(id):
    context = {
        'page': model_page.Page.get_one(id=id)
    }
    return render_template('/admin/page_edit.html', **context)

@app.route('/page/<int:id>/update', methods=['post'])
def update_page(id):

    if not model_page.Page.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_page.Page.update_one(id=id, **data)

    pass 

@app.route('/api/page/<int:id>/update', methods=['post'])
def api_update_page(id):
    model_page.Page.update_one(**request.form, id=id)
    return jsonify(msg="success")

@app.route('/page/<int:id>/delete')
def delete_page(id):
    model_page.Page.delete_one(id=id)
    return redirect('/pages')
