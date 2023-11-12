from flask_app.config.mysqlconnection import connectToMySQL

class Categories:
    DB = "buyable_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO categories (name)
            VALUES (%(name)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM categories;
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
        if not results:
            return None
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE categories
            SET name = %(name)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM categories WHERE id = %(id)s;"
        data = {'id': id}
        return connectToMySQL(cls.DB).query_db(query, data)