from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper_func import checkLogin
from flask_app.models import model_page, model_user


@app.route('/admin/pages')
@checkLogin
def page():
    session['page'] = 'Pages'
    context = {
        'all_pages': model_page.Page.get_all()
    }
    return render_template('admin/blog/page.html', **context)

@app.route('/admin/page/new')
@checkLogin
def new_page():
    return render_template('admin/blog/page_new.html')

@app.route('/admin/page/create', methods=['post'])
@checkLogin
def create_page():
    if not model_page.Page.validation(request.form):
        return redirect('/page/new')

    data = {
        **request.form,
        'user_id': session['uuid']
    }

    id = model_page.Page.create(**data)
    return redirect(f'/page/{id}/edit') 

@app.route('/admin/api/page/create', methods=['post'])
@checkLogin
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

@app.route('/admin/<custom_url>')
@app.route('/admin/page/<int:id>')
def show_page(id=None, custom_url=None):
    if custom_url:
        page = model_page.Page.get_one(custom_url = custom_url)
    else:
        page = model_page.Page.get_one(id = id)

    if not page.is_public:
        return redirect('/page_not_found')

    context = {
        'page': page
    }
    return render_template('main/page_show.html', **context)

@app.route('/admin/page/<int:id>/edit')
@checkLogin
def edit_page(id):
    context = {
        'page': model_page.Page.get_one(id=id)
    }
    return render_template('/admin/blog/page_edit.html', **context)

@app.route('/admin/page/<int:id>/update', methods=['post'])
@checkLogin
def update_page(id):
    data = {
        **request.form
    }
    del data['files']

    model_page.Page.update_one(id=id, **data, user_id=session['uuid'])
    return redirect(f'/page/{id}/edit')

@app.route('/admin/api/page/<int:id>/update', methods=['post'])
@checkLogin
def api_update_page(id):
    model_page.Page.update_one(**request.form, id=id)
    return jsonify(msg="success")

@app.route('/admin/page/<int:id>/delete')
@checkLogin
def delete_page(id):
    model_page.Page.delete_one(id=id)
    return redirect('/pages')
