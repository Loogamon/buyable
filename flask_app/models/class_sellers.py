from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import class_items

class Sellers:
    DB = "buyable_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.items = None

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO sellers (name, description)
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM sellers;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return []
        sellers = []
        for seller in results:
            this_seller = cls(seller)
            this_seller.items = class_items.get_items_by_seller_id(seller['id'])
            sellers.append(this_seller)
        return sellers
    
    @classmethod
    def get_one(cls, seller_id):
        query = """
            SELECT * FROM sellers WHERE %(id)s;
        """
        data ={'id': seller_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None
        this_seller = cls(results[0])
        this_seller.items = class_items.get_items_by_seller.id(seller_id)
        return this_seller
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE sellers
            SET name = %(name)s, description = %(description)s,
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM sellers WHERE id = %(id)s;"
        data = {'id': id}
        return connectToMySQL(cls.DB).query_db(query,data)