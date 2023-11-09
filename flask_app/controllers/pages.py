from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_bcrypt import Bcrypt
import datetime
import random
bcrypt = Bcrypt(app)
from flask_app.models.class_users import Users

@app.route('/')
def page_home():
    test=Users.get_all();
    print(test)
    return f"Hello There! You can see me?<br>There are about {len(test)} users in buyable_schema.";