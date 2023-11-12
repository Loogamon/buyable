from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import class_items

class ShoppingCartItem:
    DB = "buyable_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.item = None

        @classmethod
        def save(cls, data):
            query = """
                INSERT INTO shopping_cart (quantity)
                VALUES (%(quantity)s);
            """
            result = connectToMySQL(cls.DB).query_db(query, data)
            return result
        
        @classmethod
        def get_all(cls):
            query = """
                SELECT * FROM shopping_cart;
            """
            results = connectToMySQL(cls.DB).query_db(query)
            if not results:
                return []
            cart_items = []
            for cart_item in results:
                this_cart_item = cls(cart_item)
                item_data = class_items.get_one(cart_item['item_data'])
                this_cart_item.item = item_data
                cart_items.append(this_cart_item)
            return cart_items
        
        @classmethod
        def get_one(cls, cart_item_id):
            query = """
                SELECT * FROM shopping_cart WHERE id = %(id)s;
            """
            data = {'id': cart_item_id}
            results = connectToMySQL(cls.DB).query_db(query, data)
            if not results:
                return None
            return cls(results[0])
        
        @classmethod
        def update(cls, data):
            query = """
                UPDATE shopping_cart
                SET quantity = %(quantity)s
                WHERE id = %(id)s;
            """
            return connectToMySQL(cls.DB).query_db(query, data)
        
        @classmethod
        def delete(cls, id):
            query = """
                DELETE FROM shopping_cart WHERE id = %(id)s;
            """
            data = {"id": id}
            return connectToMySQL(cls.DB).query_db(query, data)