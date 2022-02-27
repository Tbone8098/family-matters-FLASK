from flask_app import app
import jsonpickle
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user, model_post, model_category

@app.route('/')
def index():
    session['page'] = 'landing page'
    return render_template('main/index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    session['page'] = 'dashboard'
    return render_template('admin/dashboard.html')

@app.route('/life_on_the_road')
def life_on_the_road():
    query = "SELECT * FROM posts WHERE category_id = (select min(category_id) from posts) AND is_public = 1 Limit 4;"
    posts = model_post.Post.one_off(query)
    print(posts)
    context = {
        'all_featured_posts': model_post.Post.get_all(is_public=1, is_featured=1),
        'all_categories': model_category.Category.get_all(),
        'all_posts': posts
    }
    return render_template('/main/life_on_the_road.html', **context)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return 'page not found'