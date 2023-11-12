from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.categories import categories
from flask_app.models.items import items
from flask_app.models.sellers import sellers


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', seller=sellers.get_all(), categories=Categories.get_all(), items=Items.get_all())

@app.route('/categorie/new')
def new_categorie():
    return render_template('')

@app.route('/categorie/new/post', methods=['POST'])
def new_categorie_post():

    data = {
        'id': session['categorie_id'],
        'name': request.form['name'],
        'categorie_id': session['categorie_id']
    }
    Categorie.save(data)
    return redirect('/dashboard')

@app.route('/categorie/<int:id>')
def categorie_details(id):
    return render_template('', categorie=Categories.get_by_id({'id': id}))

@app.route('/categorie/edit/<int:id>')
def edit_categorie(id):

    return render_template('',  categorie=Categories.get_by_id({'id': id}))

@app.route('/categorie/edit/process/<int:id>', methods=['POST'])
def post_changes(id):
    data = {
        'id': session['categorie_id'],
        'name': request.form['name'],
        'categorie_id': session['categorie_id']
        
    }
    Categories.update(data)
    return redirect('/dashboard')



@app.route('/categorie/destroy/<int:id>')
def remove_categorie(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    Categories.delete({'id':id})
    return redirect('/dashboard')