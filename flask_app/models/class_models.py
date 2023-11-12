from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from datetime import datetime
import math

class Categories:
    DB = "buyable_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.when=self.time_span()

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO categories (name)
            VALUES (%(item_name)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM categories ORDER BY name;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return []
        categories = [cls(category) for category in results]
        return categories
    
    @classmethod
    def get_one(cls, category_id):
        query = "SELECT * FROM categories WHERE id = %(id)s;"
        data = {'id': category_id}
        results =connectToMySQL(cls.DB).query_db(query, data)
        if (not len(results)):
            print("BAD DATA")
            return None;
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE categories
            SET name = %(item_name)s, updated_at=NOW()
            WHERE id = %(item_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        Items.delete_by_category(id)
        query = "DELETE FROM categories WHERE id = %(id)s;"
        data = {'id': id}
        return connectToMySQL(cls.DB).query_db(query, data)

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return now.strftime("%B %d, %Y")
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hour(s) ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minute(s) ago"
        else:
            return f"{math.floor(delta.total_seconds())} second(s) ago"

    @classmethod
    def check_valid(cls,data):
        is_valid=True
        if not len(data['item_name'])>=3:
            is_valid=False
            flash("Name needs to be 3 characters or more.","categories")
        if not len(data['item_name'])<=32:
            is_valid=False
            flash("Name must be 32 characters max.","categories")
        return is_valid;


class Items:
    DB = "buyable_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.img_url = data['img_url']
        self.description = data['description']
        self.user_id = data['user_id']
        self.category = data['category_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None
        self.category = None
        self.when=self.time_span()

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO items (name, price, img_url, description, user_id, category_id)
            VALUES (%(name)s, %(price)s, %(price)s, %(img_url)s, %(description)s, %(user_id)s, %(category_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM items
            LEFT JOIN users ON items.user_id = users.id
            LEFT JOIN categories ON items.category_id = categories.id
            ORDER BY items.name;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return []
        items = []
        for item in results:
            this_item = cls(item)
            user_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['created_at'],
                'updated_at': item['updated_at']
            }
            this_item.owner = User(user_data)

            category_data = {
                'id': item['categories.id'],
                'name': item['category_name'],
                'created_at': item['categories.created_at'],
                'updated_at': item['categories.updated_at']
            }
            this_item.category = Category(category_data)

            items.append(this_item)
        return items
    
    @classmethod
    def get_all_simple(cls):
        query = """
            SELECT * FROM items
            ORDER BY items.name;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return []
        items = []
        for item in results:
            items.append(this_item)
        return items

    @classmethod
    def get_all_by_category(cls,id):
        query = """
            SELECT * FROM items
            WHERE category_id=%(id)s
            ORDER BY items.name;
        """
        data={"id": id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        if not results:
            return []
        items = []
        for item in results:
            items.append(this_item)
        return items

    @classmethod
    def get_all_by_search(cls,id):
        query = """
            SELECT * FROM items
            ORDER BY items.name;
        """
        data={"id": id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        if not results:
            return []
        items = []
        for item in results:
            items.append(this_item)
        return items

    @classmethod
    def get_all_by_user(cls,id):
        query = """
            SELECT * FROM items
            WHERE user_id=%(id)s
            ORDER BY items.name;
        """
        data={"id": id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        if not results:
            return []
        items = []
        for item in results:
            items.append(this_item)
        return items
    
    @classmethod
    def get_one(cls, item_id):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        data = {'id': item_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE items
            SET name = %(name)s, price = %(price)s, img_url = %(img_url)s,
                description = %(description)s, user_id = %(user_id)s, category_id = %(category_id)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM items WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_by_category(cls, id):
        query = "DELETE FROM items WHERE category_id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data)

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return now.strftime("%B %d, %Y")
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hour(s) ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minute(s) ago"
        else:
            return f"{math.floor(delta.total_seconds())} second(s) ago"