from flask_app import app
import jsonpickle
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_post, model_category, model_page, model_playlist, model_refit_page

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

@app.route('/refit_on_the_road')
def refit_on_the_road():
    context = {
        'page': model_refit_page.RefitPage.get_all()[0]
    }
    print(context)
    return render_template('/main/refit/refit_on_the_road.html', **context)

@app.route('/life_on_the_road')
def life_on_the_road():
    query = "SELECT * FROM posts ORDER BY category_id;"
    posts = model_post.Post.one_off(query)
    # print(posts)
    context = {
        'all_featured_posts': model_post.Post.get_all(is_public=1, is_featured=1),
        'all_categories': model_category.Category.get_all(),
        'about_us': model_page.Page.get_one(custom_url="about_us")
    }
    return render_template('/main/life_on_the_road.html', **context)

@app.route('/page_not_found')
def page_not_found():
    return render_template('/main/page_not_found.html')

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return 'page not found'