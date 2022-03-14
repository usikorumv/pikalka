from core.Core import Core
from models.Products import Products
from core.Controller import Controller
from tkinter import messagebox

"""
    Responsible for ShowView behavior.
"""


class ShowController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.products = Products()
        self.showView = self.loadView("show")
        # self.core = Core()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        @return All customers in database
    """

    def getproducts(self):
        data = self.products.getAll()
        return data

    """
        Opens EditController

        @param id_customer Customer id that will be edited
    """

    # def btnEdit(self, id_customer):
    #     product = self.products.get(id_customer)
    #     c = self.core.openController("edit")
    #     c.main(product, self.showView)

    """
        Deletes the chosen customer and updates the ShowView

        @param id_customer Customer id that will be edited
    """

    def btnDel(self, id_product):
        self.products.delete(id_product)
        self.showView.update()
        messagebox.showinfo("Delete customer", "Customer deleted with success!")

    """
        @Override
    """

    def main(self):
        self.showView.main()