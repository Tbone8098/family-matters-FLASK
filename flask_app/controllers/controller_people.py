from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_people, model_post_has_people
from flask_app.config.helper_func import checkLogin

@app.route('/admin/people/new')
@checkLogin
def new_people():
    pass 

@app.route('/admin/people/create', methods=['post'])
@checkLogin
def create_people():
    post_id = request.form['post_id']
    data = {**request.form}
    del data['post_id']
    model_people.Person.create(**data)
    return redirect(f'/admin/post/{post_id}/edit')

@app.route('/admin/people/join', methods=['post'])
@checkLogin
def join_people_to_post():
    print(request.form)
    post_id = request.form['post_id']
    model_post_has_people.PostHasPeople.create(**request.form)
    return redirect(f'/admin/post/{post_id}/edit')

@app.route('/admin/people/<int:id>')
@checkLogin
def show_people(id):
    pass 

@app.route('/admin/people/<int:id>/edit')
@checkLogin
def edit_people(id):
    pass 

@app.route('/admin/people/<int:id>/update', methods=['post'])
@checkLogin
def update_people(id):
    pass 

@app.route('/admin/people/<int:id>/delete')
@checkLogin
def delete_people(id):
    model_people.Person.delete_one(id=id)
    pass 
