from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models. import
from flask_app.models. import 
from flask_app.models. import 


@app.route('/')
def index():
    return redirect('/seller/login')

@app.route('/seller/login')
def login():
    if 'user_id' in session:
        return redirect('/dashboard')

    return render_template('')

@app.route('/seller/login/process', methods=['POST'])
def login_success():
    seller = Seller.validate_login(request.form)
    if not seller:
        return redirect('/seller/login')

    session['seller_id'] = seller.id
    return redirect('')

@app.route('/seller/register/process', methods=['POST'])
def register_success():
    if not Seller.validate_reg(request.form):
        return redirect('/seller/login')

    seller_id = Seller.save(request.form)
    session['seller_id'] = seller_id
    return redirect('/dashboard')

@app.route('/seller/logout')
def logout():
    if 'seller_id' in session:
        session.pop('seller_id')
    return redirect('/seller/login')