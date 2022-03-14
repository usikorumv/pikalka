from models.Products import Products
from core.Controller import Controller

class Addcontroller:
    def __init__(self):
        self.addView = self.loadView("add")
        self.products = Products()

    def add(self, id, name, description, barcode, price):
        response = self.products.add(id, name, description, barcode, price)

        if response > 0:
            return 'Success'
        else:
            return 'Error'
        self.addView.close()

    def get_products(self):
        products = self.products.get_all()
        if products:
            return products
        else:
            return "Error"

    def main(self):
        self.addView.main()