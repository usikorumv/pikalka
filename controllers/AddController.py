from models.Products import Products

class Addcontroller:
    def __init__(self):
        self.products = Products()

    def add(self, id, name, description, barcode, price):
        response = self.products.add(id, name, description, barcode, price)

        if response > 0:
            return 'Success'
        else:
            return 'Error'

    def get_products(self):
        products = self.products.get_all()
        if products:
            return products
        else:
            return "Error"

class Updatecontroller:
    def __init__(self):
        self.products = Products()

    def update(self, id, name, description, barcode, price):
        updated_product = self.products.update(id, name, description, barcode, price)
        if updated_product:
            return "Success"
        else:
            return "Error"
