from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.categories import categories
from flask_app.models.items import items
from flask_app.models.sellers import sellers


@app.route('/shopping_cart')
def new_categorie():
    return render_template('',seller=sellers.get_all(), categories=Categories.get_all(), items=Items.get_all() )

@app.route('/shopping_cart/new')
def shopping_cart():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = Users.get_by_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('', user=user)

@app.route('/shopping_cart/new/post', methods=['POST'])
def shopping_cart_post():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Users.validate_user(request.form):
        return redirect('/user/new')

    data = {
        'id': session['user_id'],
        'quantity': request.form['quantity'],
        'user_id': session['user_id']
    }
    shopping_cart.save(data)
    return redirect('/dashboard')



@app.route('/shopping_cart/edit/<int:id>')
def edit_item(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    user = Users.get_by_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('',user=user,  item=Items.get_by_id({'id': id}))

@app.route('/shopping_cart/edit/process/<int:id>', methods=['POST'])
def edit_quantity(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not User.validate_user(request.form):
        return redirect(f'/shopping_cart/edit/{id}')

    data = {
        'id': session['user_id'],
        'quantity': request.form['quantity'],
        'user_id': session['user_id']
    }
    Shopping_cart.update(data)
    return redirect('/dashboard')



@app.route('/shopping_cart/destroy/<int:id>')
def remove_from_cart(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    shopping_cart.destroy({'id':id})
    return redirect('/dashboard')