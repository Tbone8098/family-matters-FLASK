from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_category, model_user


@app.route('/categories')
def category():
    context = {
        'all_categories': model_category.Category.get_all()
    }
    return render_template('admin/category.html', **context)

@app.route('/category/new')
def new_category():
    return render_template('admin/category_new.html')

@app.route('/category/create', methods=['post'])
def create_category():
    if not model_category.Category.validation(request.form):
        return redirect('/categories')

    model_category.Category.create(**request.form)
    return redirect('/categories') 

@app.route('/api/category/create', methods=['post'])
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
            'id': id,
            **request.form
        }
    }
    return jsonify(msg)

@app.route('/category/<int:id>')
def show_category(id):
    pass 

@app.route('/category/<int:id>/edit')
def edit_category(id):
    pass 

@app.route('/category/<int:id>/update', methods=['post'])
def update_category(id):

    if not model_category.Category.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_category.Category.update_one(id=id, **data)

    pass 

@app.route('/category/<int:id>/delete')
def delete_category(id):
    model_category.Category.delete_one(id=id)
    return redirect('/categories')
