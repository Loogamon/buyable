import urllib.parse
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

@app.route('/')
def page_home():
    user=UserSession().check_status()
    cats=Categories.get_all()

    cat_sel=-1
    cat_search=request.args.get('c')
    if not cat_search == None:
        if cat_search.isdigit():
            cat_sel=int(cat_search)

    search=request.args.get('f')
    if search==None:
        search="";
    search_url=urllib.parse.quote(search, safe='')
    
    items=Items.get_all_simple()
    print("Sanitize Test:", search_url)
    return render_template("buyable_browse.html",user=user,cats=cats,cat_sel=cat_sel,search=search,search_url=search_url)


@app.errorhandler(404)
def page_404(e):
    user=UserSession().check_status()
    er={
        'title': "404 Not Found",
        'desc': "You are at a strange place. There's actually nothing to see here."
    }
    return render_template("buyable_error.html",user=user,er=er);

@app.errorhandler(405)
def page_405(e):
    user=UserSession().check_status()
    er={
        'title': "405 Not Allowed",
        'desc': "Oops. You aren't supposed to do that."
    }
    return render_template("buyable_error.html",user=user,er=er);

@app.route('/error')
def page_error():
    user=UserSession().check_status()
    er={
        'title': "Error",
        'desc': "Because it's supposed to have more specific messages... This is effectively an error within an error, or maybe you just choose to look at this page personally."
    }
    error=request.args.get('t')
    if error==None:
        return redirect('/')
    num=0
    if error.isdigit():
        num=int(error)
    
    if num==1:
        er['title']="User Not Found";
        er['desc']="Oops, there's no user nor seller here.";
    if num==2:
        er['title']="Product Not Found";
        er['desc']="Oops, there's no product here.";
    if num==3:
        er['title']="Category Not Found";
        er['desc']="Oops, there's no category here.";
    if num==5:
        er['title']="User Error";
        er['desc']="You are trying to edit something that doesn't belong to you.";
    if num==6:
        er['title']="No Categories Found";
        er['desc']="You can't add nor edit a product, if there's no categories present.";
    return render_template("buyable_error.html",user=user,er=er);

#----

@app.route('/user/login')
def page_login():
    user=UserSession().check_status()
    if user.logged_on:
        return redirect('/user/logout')
    return render_template("buyable_login.html",user=user)

@app.route('/user/logout')
def page_user_logout():
    session.clear();
    return redirect("/user/login");

# Shopping Cart & Seller's Zone

@app.route('/mycart')
def page_cart():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    return render_template("buyable_shopping_cart.html",user=user)

@app.route('/sellers')
def page_sellers():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    if user.seller:
        items=Items.get_all_by_user(user.id)
        cats=Categories.get_all()
        return render_template("buyable_sellerzone.html",user=user,cats=cats)
    return render_template("buyable_sellerzone_consumer.html",user=user,cats=cats)

# Add/Edit Pages

@app.route('/category/add')
def page_category_add():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    item={ "name": "" }
    if 'prev_name' in session:
        item["name"]=session["prev_name"]
        session["prev_name"]=""
    return render_template("buyable_categoryform.html",user=user,item=item)

@app.route('/category/edit')
def page_category_edit():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    edit_id=request.args.get('id')
    action=request.args.get('action')
    if edit_id.isdigit():
        edit_id=int(edit_id)
    else:
        return redirect("/error?t=3")
    item={ "name": "", "id": edit_id }
    cat=Categories.get_one(edit_id)
    if cat==None:
        return redirect("/error?t=3")
    if action=="delete":
        Categories.delete(edit_id)
        return redirect("/sellers")
    item['name']=cat.name
    cat_items=Items.get_all_by_category(edit_id)
    return render_template("buyable_categoryform_edit.html",user=user,item=item,cat=cat,cat_items=cat_items)

@app.route('/item/add')
def page_item_add():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    cats=Categories.get_all()
    if not len(cats)>0:
        return redirect("/error?t=6")
    item={ 
    "name": "",
    "cat": "",
    "image": "",
    "description": ""
    }
    if 'prev_name' in session:
        item["name"]=session["prev_name"]
        session["prev_name"]=""
    
    if 'prev_cat' in session:
        item["cat"]=session["prev_cat"]
        session["prev_cat"]=""
    
    if 'prev_image' in session:
        item["image"]=session["prev_image"]
        session["prev_image"]=""

    if 'prev_description' in session:
        item["description"]=session["prev_description"]
        session["prev_description"]=""

    return render_template("buyable_itemform.html",user=user,cats=cats,item=item)

@app.route('/item/edit')
def page_item_edit():
    user=UserSession().check_status()
    if not user.logged_on:
        return redirect('/user/login')
    cats=Categories.get_all()
    if not len(cats)>0:
        return redirect("/error?t=6")
    return render_template("buyable_itemform_edit.html",user=user,cats=cats)