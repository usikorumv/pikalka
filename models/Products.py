import psycopg2
from psycopg2 import Error
class Products:
    """Connecting to a database"""
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                           password="1",
                                           host="localhost",
                                           port="5432",
                                           database="mvcdan")
        self.cursor = self.connection.cursor()

    """Adds new product to the products table"""
    def add(self, name, price, barcode):
        response = 0

        try:
            self.cursor.execute("INSERT INTO products (name, price , barcode) VALUES (%s, %s, %s)", (name, price, barcode))
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

    def update(self, id, name,barcode, price):
        responce = 0
        try:
            self.cursor.execute("UPDATE products SET name = %s,barcode = %s, price = %s WHERE id = %s",
                                (name, price,barcode, id))
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
        self.cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
        return self.cursor.fetchone()


