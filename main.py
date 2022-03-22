from controllers.AddController import Addcontroller
# from controllers.UpdateController import Updatecontroller
#
# def add_customer_view():
#     while True:
#         name = input("Enter the name of product: ")
#         description = input('Enter description: ')
#         barcode = int(input("Enter barcode: "))
#         price = int(input("Enter price: "))
#         controller = Addcontroller()
#         print(controller.add(name, description, barcode, price))
#         answer = input('Do you want to add on more? yes/no: ')
#         if answer == 'yes' or answer == 'y':
#             continue
#         else:
#             break
#
# def get_customers_view():
#     controller = Addcontroller()
#     print(controller.get_products())
#
# # def update_view():
# #     id = int(input("Enter id: "))
# #     name = input("Enter the name of product: ")
# #     description = input('Enter description: ')
# #     barcode = int(input("Enter barcode: "))
# #     price = int(input("Enter price: "))
# #     controller = Updatecontroller()
# #     print(controller.update(id, name, description, barcode, price))
#
# def main():
#     answer = int(input("1)Get all products\n2)Add products\n3)Update products\nChoose 1/2/3: "))
#     if answer == 2:
#         add_customer_view()
#     elif answer == 1:
#         get_customers_view()
#     # elif answer == 3:
#     #     update_view()
#     else:
#         print("Error")
#
# from core import Core
from core.Core import Core


class Main:
    @staticmethod
    def run():
        try:
            app = Core.openController("home")
            app.main()
        except Exception as e :
            print(str(e))

if __name__ == "__main__":
    Main.run()