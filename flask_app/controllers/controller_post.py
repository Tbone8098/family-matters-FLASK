from cmath import log
from flask_app import app
from flask import render_template, redirect, session, request, jsonify

from flask_app.models import model_post, model_category, model_page

@app.route('/posts')          
def post_new():
    context = {
        'all_posts': model_post.Post.get_all(),
        'all_categories': model_category.Category.get_all()
    }
    return render_template('admin/post.html', **context)

@app.route('/post/create', methods=['POST'])          
def post_create():
    # validate 
    # create a new page
    data = {
        **request.form,
        'is_post': 1
    }
    del data['category_id']
    page_id = model_page.Page.create(**data, user_id=session['uuid'])
    # create a new post
    model_post.Post.create(page_id=page_id, category_id=request.form['category_id'])
    return redirect('/posts')

@app.route('/post/<int:id>')          
def post_show(id):
    context = {
        'post': model_post.Post.get_one(id=id),
    }
    return render_template('page_show.html', **context)

@app.route('/post/<int:id>/edit')          
def post_edit(id):
    context = {
        'post': model_post.Post.get_one(id=id),
        'all_categories': model_category.Category.get_all()
    }
    return render_template('admin/page_edit.html', **context)

@app.route('/post/<int:id>/update', methods=['POST'])          
def post_update(id):
    return redirect('/')

@app.route('/api/post/<int:id>/update', methods=['POST'])          
def api_post_update(id):
    model_post.Post.update_one(**request.form, id=id)
    return jsonify(msg='success')



@app.route('/post/<int:id>/delete')          
def post_delete(id):
    return redirect('/')
