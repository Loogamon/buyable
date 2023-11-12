from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_bcrypt import Bcrypt
import datetime
import random
bcrypt = Bcrypt(app)
from flask_app.models.class_usersession import UserSession
from flask_app.models.class_users import Users
from flask_app.models.class_models import Items
from flask_app.models.class_models import Categories

@app.route('/action/category',methods=['POST'])
def action_category():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    action=request.args.get('t')
    print(request.form)
    print(action)
    if action=="add":
        valid=Categories.check_valid(request.form)
        if not valid:
            session["prev_name"]=request.form['item_name']
            return redirect("/category/add");
        session["prev_name"]=""
        Categories.save(request.form)
    if action=="edit":
        valid=Categories.check_valid(request.form)
        if not valid:
             return redirect(f"/category/edit?id={request.form['item_id']}");
        Categories.update(request.form)
    return redirect("/sellers");