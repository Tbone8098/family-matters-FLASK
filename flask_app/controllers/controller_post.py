from cmath import log
from flask_app import app
from flask import render_template, redirect, session, request, jsonify

from flask_app.models import model_post, model_category, model_page

@app.route('/posts')          
def post_new():
    session['page'] = 'Posts'
    context = {
        'all_posts': model_post.Post.get_all(),
        'all_categories': model_category.Category.get_all()
    }
    return render_template('admin/post.html', **context)

@app.route('/post/create', methods=['POST'])          
def post_create():
    id = model_post.Post.create(**request.form, user_id=session['uuid'])
    return redirect(f'/post/{id}/edit')

@app.route('/post/<int:id>')          
def post_show(id):
    context = {
        'post': model_post.Post.get_one(id=id),
    }
    return render_template('main/post_show.html', **context)

@app.route('/post/<int:id>/edit')          
def post_edit(id):
    session['page'] = 'Edit Post'
    context = {
        'post': model_post.Post.get_one(id=id),
        'all_categories': model_category.Category.get_all()
    }
    return render_template('admin/post_edit.html', **context)

@app.route('/post/<int:id>/update', methods=['POST'])          
def post_update(id):
    print("*****************")
    print(request.form)
    data ={**request.form}
    del data['files']
    print(data)
    print("*****************")
    model_post.Post.update_one(**data, id=id)
    return redirect(f'/post/{id}/edit')

@app.route('/api/post/<int:id>/update', methods=['POST'])          
def api_post_update(id):
    data ={**request.form}
    model_post.Post.update_one(**data, id=id)
    return jsonify(msg='success')

@app.route('/post/<int:id>/delete')          
def post_delete(id):
    model_post.Post.delete_one(id=id)
    return redirect('/posts')
