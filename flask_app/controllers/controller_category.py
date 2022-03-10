from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper_func import checkLogin
from flask_app.models import model_category, model_post

@app.route('/admin/categories')
@checkLogin
def category():
    session['page'] = 'Categories'
    context = {
        'all_categories': model_category.Category.get_all()
    }
    return render_template('admin/blog/category.html', **context)

@app.route('/admin/category/new')
@checkLogin
def new_category():
    return render_template('admin/blog/category_new.html')

@app.route('/admin/category/create', methods=['post'])
@checkLogin
def create_category():
    if not model_category.Category.validation(request.form):
        return redirect('/categories')

    model_category.Category.create(**request.form)
    return redirect('/categories') 

@app.route('/api/admin/category/create', methods=['post'])
@checkLogin
def api_create_category():
    errors = model_category.Category.api_validation(request.form)
    if errors:
        msg = {
            'status': 500,
            'errors': errors
        }
        return jsonify(msg)

    id = model_category.Category.create(**request.form)
    msg = {
        'status': 200,
        'data': {
            'type': 'addrow',
            'id': id,
            **request.form
        }
    }
    return jsonify(msg)

@app.route('/admin/api/category/<int:id>')
@checkLogin
def show_category(id):
    all_posts = model_post.Post.get_all_serialized(category_id=id, is_public=1)
    msg = {
        'content': all_posts
    }
    return jsonify(msg)

@app.route('/admin/api/category/<int:id>/update', methods=['post'])
@checkLogin
def api_update_category(id):
    model_category.Category.update_one(id=id, **request.form)
    msg = {
        'status': 200,
        'data': {
            'type': 'update cell',
            'id': id
        }
    }
    return jsonify(msg)

@app.route('/admin/category/<int:id>/delete')
@checkLogin
def delete_category(id):
    model_category.Category.delete_one(id=id)
    return redirect('/categories')
