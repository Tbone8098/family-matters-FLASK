from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user

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


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return 'page not found'