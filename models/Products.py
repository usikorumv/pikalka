import psycopg2
from psycopg2 import Error
class Products:
    """Connecting to a database"""
    def __init__(self):
        self.connection = psycopg2.connect(user="daniel",
                                           password="1",
                                           host="localhost",
                                           port="5432",
                                           database="mvc")
        self.cursor = self.connection.cursor()

    """Adds new product to the products table"""
    def add(self, name, description, barcode, price):
        response = 0

        try:
            self.cursor.execute("INSERT INTO products (name, description, barcode, price) VALUES (%s, %s, %s, %s)", (name, description, barcode, price))
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            response += 1

        except Exception as e:
            print(e)

        return response

    """Gets all products from table"""
    def get_all(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def update(self, id, name, description, barcode, price):
        responce = 0
        try:
            self.cursor.execute("UPDATE products SET name = %s, description = %s,barcode = %s, price = %s WHERE id = %s",
                                (name, description, barcode, price, id))
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            responce += 1
        except:
            pass

        return responce

    def delete(self, id):
        self.cursor.execute(
            "DELETE FROM products WHERE id = %s",
            (id,))
        return self.cursor.rowcount

    def get(self, id):
        self.cursor.execute("SELECT * FROM customers WHERE id = %s", (id,))
        return self.cursor.fetchone()


