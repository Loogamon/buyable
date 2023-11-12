from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.categories import categories
from flask_app.models.items import items
from flask_app.models.sellers import sellers

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', seller=Sellers.get_all(), categories=Categories.get_all(), items=Items.get_all())

@app.route('/item/<int:id>')
def item_details(id):
    return render_template('',item=Items.get_by_id({'id': id}))


@app.route('/item/new')
def new_item():
    if 'seller_id' not in session:
        return redirect('/seller/login')
    seller = Selers.get_by_id({"id":session['user_id']})
    if not seller:
        return redirect('/user/logout')
    return render_template('', seller=seller)

@app.route('/item/new/post', methods=['POST'])
def new_item_post():
    if 'seller_id' not in session:
        return redirect('/user/login')
    if not Seller.validate_seller(request.form):
        return redirect('/item/new')

    data = {
        'id': session['user_id'],
        'name': request.form['name'],
        'price': request.form['price'],
        'img_url': request.form['img_url'],
        'description': request.form['description'],
        'user_id': session['user_id'],
        'category': request.form['category_id']
    }
    Items.save(data)
    return redirect('/dashboard')



@app.route('/item/edit/<int:id>')
def edit_item(id):
    if 'seller_id' not in session:
        return redirect('/user/login')
    seller = Seller.get_by_id({"id":session['seller_id']})
    if not seller:
        return redirect('/seller/logout')
    return render_template('',seller=seller,  item=Items.get_by_id({'id': id}))

@app.route('/item/edit/process/<int:id>', methods=['POST'])
def post_edit(id):
    if 'seller_id' not in session:
        return redirect('/user/login')
    if not Sellers.validate_seller(request.form):
        return redirect(f'/item/edit/{id}')

    data = {
        'id': session['user_id'],
        'name': request.form['name'],
        'price': request.form['price'],
        'img_url': request.form['img_url'],
        'description': request.form['description'],
        'user_id': session['user_id'],
        'category': request.form['category_id']

        
    }
    Items.update(data)
    return redirect('/dashboard')

@app.route('/item/buy/<int:id>')
def buy(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.get_by_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    return render_template('items.html',user=user,  item=Items.get_by_id({'id': id}))


@app.route('/item/destroy/<int:id>')
def purchased(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    Items.destroy({'id':id})
    return redirect('/dashboard')