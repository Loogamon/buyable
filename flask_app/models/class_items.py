from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import User, Category

class Item:
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
            LEFT JOIN categories ON items.category_id = categories.id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return []
        items = []
        for item in results:
            this_item = clas(item)
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