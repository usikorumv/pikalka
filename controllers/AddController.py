from models.Products import Products

class Addcontroller:
    def __init__(self):
        self.products = Products()

    def add(self, name, description, barcode):
        response = self.products.add(name, description, barcode)

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