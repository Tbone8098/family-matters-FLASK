from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_block, model_content

@app.route('/block/new')
def new_block():
    pass 

@app.route('/api/block/content/create', methods=['post'])
def create_block():
    block_id = model_block.Block.create(**request.form, type="content")
    id =model_content.Content.create(block_id=block_id, content="Insert Text Here")
    msg = {
        'status': 200,
        'data': {
            'id': id,
        }
    }
    return jsonify(msg)

@app.route('/block/<int:id>')
def show_block(id):
    pass 

@app.route('/block/<int:id>/edit')
def edit_block(id):
    pass 

@app.route('/api/block/content/<int:id>/update', methods=['post'])
def update_block(id):
    model_content.Content.update_one(id=id, **request.form)
    return jsonify(msg="success")

@app.route('/block/<int:id>/delete')
def delete_block(id):
    model_block.Block.delete_one(id=id)
    pass 

