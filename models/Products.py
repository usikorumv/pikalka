import psycopg2

class Products:
    """Connecting to a database"""
    def __init__(self):
        self.connection = psycopg2.connect(user="baielkantin",
                                           password="19172211",
                                           host="localhost",
                                           port="5432",
                                           database="kantin_db")
        self.cursor = self.connection.cursor()

    """Adds new product to the products table"""
    def add(self, name, price, barcode):
        response = 0

        try:
            self.cursor.execute("INSERT INTO kantinproducts (name, price , barcode) VALUES (%s, %s, %s)", (name, price, barcode))
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            response += 1

        except Exception as e:
            print(e)

        return response

    """Gets all products from table"""
    def get_all(self):
        self.cursor.execute("SELECT * FROM kantinproducts")
        return self.cursor.fetchall()

    def update(self, id, name,barcode, price):
        responce = 0
        try:
            self.cursor.execute("UPDATE kantinproducts SET name = %s,barcode = %s, price = %s WHERE id = %s",
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

    def get(self, barcode):
        self.cursor.execute("SELECT * FROM kantinproducts WHERE barcode = %s", (barcode,))
        lst = []
        product = self.cursor.fetchall()
        # for i in product:
        #     print(i)
            # lst.append(i)
        # print(product)
        return product


