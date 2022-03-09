import psycopg2
from psycopg2 import Error
class Products:
    """Connecting to a database"""
    def __init__(self):
        self.connection = psycopg2.connect(user="mvcbaiel",
                                           password="19172211",
                                           host="localhost",
                                           port="5432",
                                           database="mvc")
        self.cursor = self.connection.cursor()

    """Adds new product to the products table"""
    def add(self, name, description, barcode):
        response = 0

        try:
            self.cursor.execute("INSERT INTO products (name, description, barcode) VALUES (%s, %s, %s)", (name, description, barcode))
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            response += 1

        except:
            pass
        return response

    """Gets all products from table"""
    def get_all(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()