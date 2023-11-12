from flask_app.models.class_users import Users
from flask import session

class UserSession:
    def __init__(self):
        self.id=None
        self.user_name="Guest"
        self.logged_on=False
        self.cart=0
        self.seller=False
    def check_status(self):
        self.cart=0
        self.seller=True
        if "user_loggedon" in session:
            user=Users.get_userinfo(session['user_email'])
            self.id=user.id
            self.user_name=f"{user.first_name} {user.last_name}"
            self.logged_on=True
            return self;
        self.logged_on=False
        return self;